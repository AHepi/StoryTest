"""Read the git commands inside a shell command, for the workshop's hooks.

The hooks refuse_check_bypass.py and after_commit.py both need to know
which git commands a shell command runs. This file does that reading once,
for both. It is not run by itself.

How it reads a command:
1. The body of a here-document (the lines between "<<END" and "END") and
   the text inside quotes are set aside, so a commit message or a note
   being written that merely mentions a command is never read as one.
   Each quoted text becomes the one word QUOTED, so the options around it
   still line up.
2. The rest is split into single commands at new lines, ; & | ( ) and $(.
3. Settings put in front (NAME=value) and wrappers (env, command, exec,
   nohup, time, sudo) are stepped over. The quoted command given to
   `bash -c '...'`, `sh -lc "..."` or `eval "..."` is read as a command
   too, but only where those words stand outside any quotes: a commit
   message that mentions `bash -c` is still only a message.
4. A command whose first word is git (or ends in /git) is a git command.
   Its options before the subcommand are read: -C folder, -c name=value,
   --git-dir, --work-tree and the rest.

It catches the usual spellings, not every possible one. A commit that
gets past it carries no gate stamp, so the next commit through the gate
judges what it got wrong in the files, with the limits the note in
refuse_check_bypass.py names.
"""
import os
import re

HERE_DOCUMENT = re.compile(r"<<-?[ \t]*(['\"]?)(\w+)\1[^\n]*\n.*?\n[ \t]*\2[ \t]*(?=\n|$)", re.S)
QUOTED_TEXT = re.compile(r"'[^']*'|\"(?:\\.|[^\"\\])*\"", re.S)
COMMAND_BREAK = re.compile(r"\$\(|&&|\|\||[\n;&|()`]")
SETTING = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=")
WRAPPERS = ("env", "command", "exec", "nohup", "time", "sudo")
GIT_OPTIONS_WITH_A_VALUE = ("-C", "-c", "--git-dir", "--work-tree", "--namespace", "--config-env", "--exec-path")


def plain_text(command):
    """The command with here-document bodies removed and each quoted text replaced by QUOTED. A quoted value
    given to a setting (NAME="...") stays joined to it, so the setting is still stepped over as one word."""
    without_documents = HERE_DOCUMENT.sub("<<DOCUMENT", command)
    return re.sub(r"= QUOTED ", "=QUOTED ", QUOTED_TEXT.sub(" QUOTED ", without_documents))


WRAPPER_BEFORE = re.compile(r"(?:^|[\s;&|(`])(?:\S*/)?(?:(?:ba|z|da)?sh\s+(?:-[A-Za-z]+\s+)*-[A-Za-z]*c[A-Za-z]*"
                            r"|eval)\s+$")


def wrapped_commands(command):
    """The quoted text given to bash -c, sh -c or eval, where those words stand outside any quotes."""
    text = HERE_DOCUMENT.sub("<<DOCUMENT", command)
    found, previous_end = [], 0
    for match in QUOTED_TEXT.finditer(text):
        if WRAPPER_BEFORE.search(text[previous_end:match.start()]):
            inner = match.group(0)[1:-1]
            found.append(inner.replace('\\"', '"') if match.group(0).startswith('"') else inner)
        previous_end = match.end()
    return found


def commands_with_source(command, depth=0):
    """Each single command, as (its words, the text whose folder changes apply to it)."""
    if depth < 3:
        for inner in wrapped_commands(command):
            for words, source in commands_with_source(inner, depth + 1):
                yield words, command + "\n" + source  # the outer command's cd first, then the wrapped one's
    for piece in COMMAND_BREAK.split(plain_text(command)):
        words = piece.split()
        while words:
            if SETTING.match(words[0]):
                words = words[1:]
            elif words[0] in WRAPPERS:
                words = words[1:]
                while words and words[0].startswith("-"):
                    words = words[1:]  # an option of the wrapper, such as env -i
            else:
                break
        if words:
            yield words, command


def single_commands(command):
    """Each single command in the shell command, as a list of words."""
    for words, _ in commands_with_source(command):
        yield words


def git_commands(command):
    """Yield (global options, subcommand, the words after it) for each git command.

    global options is a list of (option, value) pairs; value is None for an
    option that takes none.
    """
    for options, subcommand, words, _ in git_commands_with_source(command):
        yield options, subcommand, words


def git_commands_with_source(command):
    """The same, with the text whose folder changes (cd) apply to each git command."""
    for words, source in commands_with_source(command):
        if words[0] != "git" and not words[0].endswith("/git"):
            continue
        options, position = [], 1
        while position < len(words) and words[position].startswith("-"):
            word = words[position]
            name, _, attached = word.partition("=")
            if word in ("-C", "-c") or (name in GIT_OPTIONS_WITH_A_VALUE and not attached and name.startswith("--")):
                value = words[position + 1] if position + 1 < len(words) else ""
                options.append((name, value))
                position += 2
            elif word.startswith("-c") and len(word) > 2:
                options.append(("-c", word[2:]))
                position += 1
            else:
                options.append((name, attached or None))
                position += 1
        subcommand = words[position] if position < len(words) else ""
        yield options, subcommand, words[position + 1:], source


def target_folder(command, options, working_folder):
    """The folder a git command acts in: its -C folder, or the last cd before it, or the working folder."""
    folder = working_folder
    for match in re.finditer(r"(?:^|[;&|(\n])\s*(?:cd|pushd)\s+(\S+)", plain_text(command)):
        if match.group(1) != "QUOTED":
            folder = os.path.join(folder, os.path.expanduser(match.group(1)))
    for option, value in options:
        if option == "-C" and value and value != "QUOTED":
            folder = os.path.join(folder, os.path.expanduser(value))
    return os.path.normpath(folder)


def is_inside(folder, root):
    folder, root = os.path.realpath(folder), os.path.realpath(root)
    return folder == root or folder.startswith(root + os.sep)
