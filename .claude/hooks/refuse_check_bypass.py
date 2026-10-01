#!/usr/bin/env python3
"""Refuse a shell command that would get round the workshop's commit gate.

Claude Code runs this by itself before every shell command (see
.claude/settings.json). The commit gate is git's own pre-commit hook in
.githooks/ (a hook is a small program that git, or Claude Code, runs by
itself at a set moment). This script refuses the usual ways of getting
round that gate:
- a commit or merge that tells git to skip its hooks (--no-verify, or -n
  on a commit, alone or in a group such as -nam, or a shortened
  --no-veri...);
- pointing git's hooks somewhere else or unsetting them (git config
  core.hooksPath ..., git -c core.hooksPath=..., or the same setting passed
  through GIT_CONFIG_... settings), in any letter case;
- deleting, moving, emptying or overwriting the gate's own files in
  .githooks/, or taking away their permission to run;
- writing by hand the records the gate keeps in .git (workshop-...), which
  would make a commit look approved by the gate.
It lets through read-only questions (git config core.hooksPath with no
value), setting the hooks to the gate's own folder (by its short name or
its full path), text that only mentions these words (a commit message, a
note being written), and anything done in another repository. It reads a
command wrapped in `bash -c`, `sh -c` or `eval` too.

It catches the usual spellings, not every possible one. What gets past
it is a commit the gate did not approve: the next commit through the gate
compares the files with the last approved commit, so what such a commit
got wrong in the files stops it until put right, and the recheck
(recheck_commits.py, at session start and before each commit) asks for
its review receipt. Some things are not stopped that way, among them a
change to the gate's own files, which runs in its changed form and is only
noted, and a loosened check, judged only by the planted-fault test and its
late review; those known are listed in the error-correction skill,
references/checks-and-cases.md, section 2, "What the gate cannot do".

If this script itself goes wrong, it lets the command through and prints
a notice, so that a fault here never stops ordinary work.
"""
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from git_command_reading import git_commands_with_source, is_inside, single_commands, target_folder  # noqa: E402

GATE_FOLDER = ".githooks"
COMMIT_OPTIONS_WITH_A_VALUE = ("--message", "--file", "--reuse-message", "--reedit-message", "--template",
                               "--author", "--date", "--fixup", "--squash", "--cleanup", "--trailer",
                               "--pathspec-from-file")
SHORT_OPTIONS_WITH_A_VALUE = "mFCct"   # the value is the rest of the word, or the next word
SHORT_OPTIONS_WITH_AN_OPTIONAL_VALUE = "uS"   # the value, if any, is the rest of the word
SETTINGS_BY_ENVIRONMENT = re.compile(r"GIT_CONFIG_(?:PARAMETERS|KEY_\d+|COUNT)", re.I)
FILE_COMMANDS_THAT_REMOVE = ("rm", "mv", "unlink", "truncate", "shred")
FILE_COMMANDS_THAT_WRITE_TO_THE_LAST = ("cp", "install", "ln", "tee")

SKIPPING = ("This command would make git skip the workshop's commit gate (.githooks/pre-commit), which runs every"
            " check before a commit.")
MOVING = ("This command would point git's hooks away from the workshop's commit gate (.githooks), or switch the"
          " gate off.")
REMOVING = "This command would remove, empty or overwrite the commit gate's own files in .githooks/."
RECORDS = ("This command would write or remove by hand the records the commit gate keeps in .git (workshop-...),"
           " which would make a commit look approved by the gate.")
ADVICE = (" A failing check is a sign that something may be wrong: work it through with the error-correction skill"
          " (references/checks-and-cases.md, section 2). If the check itself is wrong, correct the check in its own"
          " commit. Never get round it.")


def is_the_gate_setting(name):
    return name.lower() == "core.hookspath"


PROJECT_ROOT = [None]  # set by main, so that the gate's folder is also known by its full path
GATE_RECORDS = re.compile(r"\.git/workshop-")


def is_the_gate_folder(value):
    if value.rstrip("/") in (GATE_FOLDER, "./" + GATE_FOLDER):
        return True
    return bool(PROJECT_ROOT[0]) and os.path.isabs(value) and \
        os.path.realpath(value.rstrip("/")) == os.path.realpath(os.path.join(PROJECT_ROOT[0], GATE_FOLDER))


def commit_skips_hooks(words):
    skip_next = False
    for word in words:
        if skip_next:
            skip_next = False
            continue
        if word == "--":
            break
        if word.startswith("--"):
            name = word.split("=", 1)[0]
            if len(name) >= len("--no-veri") and "--no-verify".startswith(name):
                return True
            if name in COMMIT_OPTIONS_WITH_A_VALUE and "=" not in word:
                skip_next = True
            continue
        if word.startswith("-") and len(word) > 1:
            letters = word[1:]
            for index, letter in enumerate(letters):
                if letter == "n":
                    return True
                if letter in SHORT_OPTIONS_WITH_A_VALUE:
                    skip_next = index == len(letters) - 1
                    break
                if letter in SHORT_OPTIONS_WITH_AN_OPTIONAL_VALUE:
                    break
    return False


def config_moves_hooks(words, raw_command, shell_at_root=False):
    """True if a git config command sets core.hooksPath to anything but .githooks, or unsets it. shell_at_root says
    whether the shell stands in the project's top folder, the only place where $PWD names it."""
    unsetting = False
    plain = []
    skip_next = False
    for word in words:
        if skip_next:
            skip_next = False
            continue
        if word in ("--unset", "--unset-all"):
            unsetting = True
        elif word in ("--file", "-f", "--blob", "--type", "--default", "--comment", "--value"):
            skip_next = True
        elif word == "--remove-section":
            unsetting = True
        elif not word.startswith("-"):
            plain.append(word)
    if plain and plain[0] in ("set", "unset", "get", "list", "edit", "rename-section", "remove-section"):
        mode, plain = plain[0], plain[1:]
        unsetting = unsetting or mode in ("unset", "remove-section")
        if mode in ("get", "list"):
            return False
    if not plain:
        return False
    key = plain[0]
    if key == "QUOTED":
        return "hookspath" in raw_command.lower()
    if len(plain) > 1 and plain[1] == "QUOTED" and is_the_gate_setting(key) and not unsetting:
        quoted = re.search(r"hookspath\s+(['\"])(.*?)\1", raw_command, flags=re.I)
        quote, value = (quoted.group(1), quoted.group(2).rstrip("/")) if quoted else ("", "")
        # $PWD is the project folder only inside double quotes (single quotes keep it as written, and git would
        # then look for a folder named "$PWD"), only when the shell stands in the project's top folder (not a
        # folder inside it), and only if the command has not moved to another folder first
        moved = re.search(r"(^|[;&|(]\s*)(cd|pushd)\s", raw_command) is not None
        pwd_here = (quote == '"' and shell_at_root and not moved
                    and value in ("$PWD/" + GATE_FOLDER, "${PWD}/" + GATE_FOLDER))
        return not (value in (GATE_FOLDER, "./" + GATE_FOLDER) or pwd_here or is_the_gate_folder(value))
    if key.lower() == "core" and unsetting:
        return True  # removing the whole [core] section removes the setting too
    if not is_the_gate_setting(key):
        return False
    if unsetting:
        return True
    return len(plain) > 1 and not is_the_gate_folder(plain[1])


def touches_the_gate_files(command, working_folder, project_root):
    """The reason to refuse, if the command changes the gate's files or its records in .git; else None."""
    gate_folder = os.path.join(project_root, GATE_FOLDER)
    git_folder = os.path.join(project_root, ".git")

    def is_gate_path(word, folder):
        return word != "QUOTED" and is_inside(os.path.join(folder, os.path.expanduser(word)), gate_folder)

    def is_gate_record(word, folder):
        return (word != "QUOTED" and GATE_RECORDS.search(word) is not None
                and is_inside(os.path.dirname(os.path.join(folder, os.path.expanduser(word))), git_folder))

    folder = working_folder
    for words in single_commands(command):
        if words[0] in ("cd", "pushd"):
            if len(words) > 1 and words[1] != "QUOTED":
                folder = os.path.normpath(os.path.join(folder, os.path.expanduser(words[1])))
            continue
        for index, word in enumerate(words):
            redirect = re.match(r"^\d*>>?(.*)$", word)
            if redirect:
                target = redirect.group(1) or (words[index + 1] if index + 1 < len(words) else "")
                if target and is_gate_record(target, folder):
                    return RECORDS
                if target and is_gate_path(target, folder) and os.path.exists(os.path.join(folder, target)):
                    return REMOVING
        name = os.path.basename(words[0])
        arguments = [word for word in words[1:] if not word.startswith("-") and not re.match(r"^\d*>", word)]
        if name in FILE_COMMANDS_THAT_REMOVE and any(is_gate_path(word, folder) for word in arguments):
            return REMOVING
        if name in FILE_COMMANDS_THAT_WRITE_TO_THE_LAST and arguments and is_gate_path(arguments[-1], folder):
            if os.path.exists(os.path.join(folder, arguments[-1])):
                return REMOVING
        edits_in_place = (name == "sed" and any(word.startswith(("-i", "--in-place")) for word in words[1:])) or \
            (name == "perl" and any(word.startswith("-") and "i" in word for word in words[1:]))
        if edits_in_place and any(is_gate_path(word, folder) for word in arguments):
            return REMOVING
        writes_records = (
            (name in FILE_COMMANDS_THAT_REMOVE + ("tee", "touch") or edits_in_place)
            and any(is_gate_record(word, folder) for word in arguments)) or (
            name in FILE_COMMANDS_THAT_WRITE_TO_THE_LAST and arguments and is_gate_record(arguments[-1], folder))
        if writes_records:
            return RECORDS
        if name == "chmod" and any(is_gate_path(word, folder) for word in arguments):
            mode = next((word for word in words[1:] if not is_gate_path(word, folder)), "")
            digits = mode[-3] if len(mode) >= 3 else mode[:1]
            if ("-" in mode and "x" in mode) or (mode.isdigit() and not int(digits) & 1):
                return REMOVING
        if (name == "git" or name.endswith("/git")) and len(words) > 1 and words[1] in ("rm", "mv"):
            if any(is_gate_path(word, folder) for word in words[2:]):
                return REMOVING
    return None


def reason_to_refuse(command, working_folder, project_root):
    for options, subcommand, words, source in git_commands_with_source(command):
        if not is_inside(target_folder(source, options, working_folder), project_root):
            continue  # another repository: not the workshop's gate
        for option, value in options:
            if option == "-c" and value:
                name, _, setting = value.partition("=")
                if (name == "QUOTED" and "hookspath" in command.lower()) or (
                        is_the_gate_setting(name) and not is_the_gate_folder(setting)):
                    return MOVING
            if option == "--config-env" and value and is_the_gate_setting(value.split("=", 1)[0]):
                return MOVING
        if subcommand == "commit" and commit_skips_hooks(words):
            return SKIPPING
        if subcommand in ("merge", "pull") and "--no-verify" in words:
            return SKIPPING
        shell_at_root = os.path.realpath(working_folder) == os.path.realpath(project_root)
        if subcommand == "config" and config_moves_hooks(words, command, shell_at_root):
            return MOVING
        if SETTINGS_BY_ENVIRONMENT.search(command) and "hookspath" in command.lower():
            return MOVING
    return touches_the_gate_files(command, working_folder, project_root)


def main():
    try:
        hook_input = json.load(sys.stdin)
        command = (hook_input.get("tool_input") or {}).get("command") or ""
        working_folder = hook_input.get("cwd") or os.getcwd()
        project_root = os.environ.get("CLAUDE_PROJECT_DIR") or subprocess.run(
            ["git", "-C", working_folder, "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, check=False).stdout.strip() or working_folder
        PROJECT_ROOT[0] = project_root
        reason = reason_to_refuse(command, working_folder, project_root)
        if reason:
            json.dump({"hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason + ADVICE,
            }}, sys.stdout)
        return 0
    except Exception as problem:  # a fault here must never block ordinary work
        print(f"refuse_check_bypass hook could not run ({problem}); the command was not checked", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
