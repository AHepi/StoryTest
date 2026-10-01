#!/usr/bin/env python3
"""Test the checks themselves, by planting known faults in a throwaway copy.

A check that has never been seen to fail tells us nothing when it passes.
So for each kind of fault a check is meant to catch, this script makes a
fresh copy of the repository in a temporary folder (with its own git
history of one commit), plants that one fault, and confirms the check
catches it, and, where it matters, that it catches it for the right
reason (the words it must print). For most faults it also plants an
innocent neighbour: a change that looks close but is not a fault, which
the check must let pass. It tests the review receipts, the commit gate,
the recheck of commits the gate did not approve, and the hooks the same
way, and confirms that the unchanged copy passes every check. Each copy's
one commit carries the gate's stamp, as a real history does once the gate
has approved a commit.

One test runs the gate's own planted-fault stage for real, which starts
this whole test again inside it. That test is left out (and listed as not
run) when this run is itself inside the planted-fault test, so it cannot
call itself without end.

Nothing in the real repository is changed. Book texts are not copied; the
copying check is tested against a small made-up "book" instead. The
settings git gives a commit that is being made (such as GIT_INDEX_FILE)
are removed first, so the throwaway copies never write into the real
repository.

The commit gate's own tests are kept in test_the_gate.py beside this
file, which this file runs, handing it these helpers (this file alone
would pass the 100,000-byte limit on text files).

It prints one line per test and a total. Exit code 1 if any test fails.

Usage: test_checks.py [REPOSITORY_ROOT]
"""
import concurrent.futures
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

for setting in [name for name in os.environ if name.startswith("GIT_")] + ["N"]:
    os.environ.pop(setting, None)  # a setting git gave the commit being made (during a merge, GIT_REFLOG_ACTION too)
# Every gate and recheck run inside this test's copies sees this setting, and does not start this test again
# (without it, a gate test that changes a check would start the whole test inside itself, without end).
ALREADY_INSIDE = bool(os.environ.get("WORKSHOP_INSIDE_PLANTED_FAULT_TEST"))
os.environ["WORKSHOP_INSIDE_PLANTED_FAULT_TEST"] = "1"
NOT_RUN = []  # tests left out of this run, printed as not run, never as passed
RECEIPT_PATH = re.compile(r"\.claude/reviews/[0-9a-f]{16}\.md")  # a receipt form is found by its path
LEFT_OVER = []  # folders outside the copies that a test made, removed at the end

SCRIPTS = os.path.join(".claude", "skills", "error-correction", "scripts")
ADD_SOURCE_SCRIPTS = os.path.join(".claude", "skills", "add-source", "scripts")
HOOKS = os.path.join(".claude", "hooks")
PROJECT_STORY = "StoryTest - project story.md"
TERM_SHEET = ".claude/skills/error-correction/references/owner-terms.md"
NO_SIGNING = ["-c", "commit.gpgsign=false", "-c", "user.name=test", "-c", "user.email=test@example.com"]
SKIP_THE_GATE = "--no" + "-verify"  # spelled in two parts so that this file's text is not taken for a command
CRAFT_SKILLS = ("story-world", "plot", "character", "dialogue", "genre")
BOOK_TEXT = ("The lantern keeper counted every ship that failed to come home before the winter storms. "
             "Perhaps the finest duel of any cowboy picture sits in Once Upon a Time in the West, a slow sad epic "
             "about railways, rather than at its close. Once Upon a Time in the West is a film the keeper never saw.")
# Every word of this "book" is invented for the test; no line of any real book is used.


def git(copy_root, *arguments, check=True):
    return subprocess.run(["git", *arguments], cwd=copy_root, check=check, capture_output=True, text=True)


def copy_repository(repository_root, prefix="workshop-test-", stamped=True):
    """A fresh copy with its own git history of one commit, stamped as approved by the gate (unless stamped is
    False), without books or the real .git."""
    copy_root = tempfile.mkdtemp(prefix=prefix)
    shutil.copytree(repository_root, copy_root, dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns(".git", "raw", "__pycache__"))
    git(copy_root, "init", "-q")
    git(copy_root, "add", "-A")
    tree = git(copy_root, "write-tree").stdout.strip()
    git(copy_root, *NO_SIGNING, "commit", "-q", "-m", f"copy\n\nWorkshop-gate: approved {tree}" if stamped else "copy")
    return copy_root


def run(copy_root, script, *arguments, stdin_text=None, environment=None, working_folder=None):
    result = subprocess.run([sys.executable, os.path.join(copy_root, script), *arguments],
                            cwd=working_folder or copy_root, capture_output=True, text=True, input=stdin_text,
                            env={**os.environ, **(environment or {})}, check=False)
    return result.returncode, result.stdout + result.stderr


def edit(copy_root, relative_path, change):
    path = os.path.join(copy_root, relative_path)
    with open(path, encoding="utf-8") as text_file:
        text = text_file.read()
    new_text = change(text)
    if new_text == text:
        raise AssertionError(f"the planted change to {relative_path} changed nothing; the test is broken")
    with open(path, "w", encoding="utf-8") as text_file:
        text_file.write(new_text)


def write(copy_root, relative_path, text):
    path = os.path.join(copy_root, relative_path)
    os.makedirs(os.path.dirname(path) or copy_root, exist_ok=True)
    with open(path, "w", encoding="utf-8") as text_file:
        text_file.write(text)


def replace_once(old, new):
    def change(text):
        if old not in text:
            raise AssertionError(f"planting failed: '{old[:60]}' not found")
        return text.replace(old, new, 1)
    return change


def named(copy_root, prefix):
    return next(name for name in os.listdir(copy_root) if name.startswith(prefix))


def last_entry_number(copy_root):
    with open(os.path.join(copy_root, PROJECT_STORY), encoding="utf-8") as story:
        return max(int(number) for number in re.findall(r"^(\d+)\. \*\*", story.read(), flags=re.M))


def add_log_entry(copy_root, restamp, body="Planted by test_checks.py."):
    number = last_entry_number(copy_root) + 1

    def change(text):
        text = text.replace("\n## Next step", f"{number}. **A test entry.** {body}\n\n## Next step", 1)
        if restamp:
            text = re.sub(r"\(as of entry \d+\)", f"(as of entry {number})", text)
        return text
    edit(copy_root, PROJECT_STORY, change)


def add_to_traps(skill, line):
    return lambda copy_root: edit(copy_root, f".claude/skills/{skill}/SKILL.md",
                                  replace_once("## Traps\n", "## Traps\n\n" + line + "\n"))


def change_shared_passage(copy_root, skills):
    for skill in skills:
        edit(copy_root, f".claude/skills/{skill}/SKILL.md",
             replace_once("**Before sending, check the notes themselves.**", "**Before sending, check your notes.**"))


def set_question_status(copy_root, question_id, status):
    edit(copy_root, named(copy_root, "22 Questions"),
         lambda text: re.sub(r"(" + ("## " if question_id.startswith("Q") else r"- \*\*") + question_id
                             + r"\..*?Status:\**\s*)open", r"\g<1>" + status, text, count=1, flags=re.S))


def add_planted_questions(copy_root):
    edit(copy_root, named(copy_root, "22 Questions"), lambda text: text.rstrip("\n")
         + "\n- **S98. Planted.** A planted question. Status: answered.\n"
         + "- **S99. Planted.** A planted question. Status: answered.\n")


def loosen_the_log_check(copy_root):
    """Switch off the records check's comparison of old log entries, in either wording the check has had."""
    def change(text):
        for old, new in (("        own = compare_logs(earlier_text, story_text, against)\n", "        own = []\n"),
                         ("        problems += compare_logs(earlier_text, story_text, against)\n", "        pass\n")):
            if old in text:
                return text.replace(old, new, 1)
        raise AssertionError("planting failed: the records check's comparison of old entries was not found")
    edit(copy_root, os.path.join(SCRIPTS, "check_records.py"), change)


def give_theory_a_second_line(copy_root):
    edit(copy_root, "sources/bond-theory.md", lambda text: text + " ")
    with open(os.path.join(copy_root, "sources/bond-theory.md"), "rb") as theory:
        new_fingerprint = hashlib.sha256(theory.read()).hexdigest()
    edit(copy_root, ".claude/skills/error-correction/frozen-files.txt",
         lambda text: text + f"{new_fingerprint}  sources/bond-theory.md  added planted\n")


def store_theory_with_a_space(copy_root):
    write(copy_root, "sources/my new theory.md", "# A new theory\n")
    code, output = run(copy_root, os.path.join(SCRIPTS, "check_frozen_files.py"), "--add", "sources/my new theory.md",
                       copy_root)
    if code != 0:
        raise AssertionError(f"--add failed: {output}")


def break_a_script(relative_path):
    return lambda copy_root: edit(copy_root, relative_path, replace_once("\nimport ", "\nthis line is not python\nimport "))


def checkout_like_windows(copy_root, keep_attributes):
    if not keep_attributes:
        os.remove(os.path.join(copy_root, ".gitattributes"))
        git(copy_root, "add", "-A")
        git(copy_root, *NO_SIGNING, "commit", "-q", "-m", "no attributes")
    git(copy_root, "config", "core.autocrlf", "true")
    for folder in ("sources", "foundations"):
        for name in os.listdir(os.path.join(copy_root, folder)):
            if name.endswith(".md"):
                os.remove(os.path.join(copy_root, folder, name))
    git(copy_root, "checkout", "--", "sources", "foundations")


def tests():
    """(name, command, plant, expect_caught, must_print). expect_caught True: exit 1; False: exit 0.

    must_print, if given, is a pattern the output must contain, so a fault is caught for the right reason."""
    frozen = [os.path.join(SCRIPTS, "check_frozen_files.py")]
    maps = [os.path.join(ADD_SOURCE_SCRIPTS, "check_maps.py")]
    records = [os.path.join(SCRIPTS, "check_records.py")]
    quotes = [os.path.join(SCRIPTS, "check_owner_quotes.py")]
    everything = [os.path.join(SCRIPTS, "run_all_checks.py"), "--skip-books"]
    corrections, catch = "27 Corrections", "26 Test"
    return [
        ("frozen: one character changed in a theory", frozen,
         lambda copy_root: edit(copy_root, "sources/bond-theory.md", lambda text: text.replace("e", "E", 1)), True,
         "bond-theory.md: frozen file has changed"),
        ("frozen: a frozen file deleted", frozen,
         lambda copy_root: os.remove(os.path.join(copy_root, "sources/gap-theory-of-narrative.md")), True,
         "frozen file is missing"),
        ("frozen: a new theory stored but not fingerprinted", frozen,
         lambda copy_root: write(copy_root, "sources/new-theory.md", "# New theory\n"), True, "should be frozen"),
        ("frozen: a file of another kind stored in sources/ but not listed", frozen,
         lambda copy_root: write(copy_root, "sources/notes.txt", "notes\n"), True, "notes.txt: should be frozen"),
        ("frozen: a line taken off the fingerprint list", frozen,
         lambda copy_root: edit(copy_root, ".claude/skills/error-correction/frozen-files.txt",
                                lambda text: "\n".join(line for line in text.splitlines()
                                                       if "bond-theory" not in line) + "\n"), True,
         "removed or changed"),
        ("frozen: a second line gives an edited theory a new fingerprint", frozen, give_theory_a_second_line, True,
         "listed 2 times"),
        ("frozen: a new theory stored in a subfolder of sources/ but not listed", frozen,
         lambda copy_root: write(copy_root, "sources/revisions/bond-theory-2.md", "# A revision\n"), True,
         "revisions/bond-theory-2.md: should be frozen"),
        ("frozen, neighbour: the source register sources/README.md edited", frozen,
         lambda copy_root: edit(copy_root, "sources/README.md", lambda text: text + "\nA new line.\n"), False, None),
        ("frozen, neighbour: a theory whose name has spaces, added with --add", frozen,
         store_theory_with_a_space, False, None),
        ("frozen, neighbour: a Windows-style checkout (the line endings setting on)", frozen,
         lambda copy_root: checkout_like_windows(copy_root, keep_attributes=True), False, None),
        ("frozen: the same checkout without .gitattributes changes the fingerprints", frozen,
         lambda copy_root: checkout_like_windows(copy_root, keep_attributes=False), True, "frozen file has changed"),
        ("maps: myth.md's node removed, 'mythic family' left", maps,
         lambda copy_root: edit(copy_root, ".claude/skills/genre/SKILL.md", replace_once('    MY["myth.md"]\n', "")),
         True, "myth.md has no node"),
        ("maps, neighbour: the family label reworded", maps,
         lambda copy_root: edit(copy_root, ".claude/skills/genre/SKILL.md",
                                replace_once('"mythic family"', '"family of myths"')), False, None),
        ("maps: scenes.md's row removed from the map (still named in another table)", maps,
         lambda copy_root: edit(copy_root, ".claude/skills/plot/SKILL.md",
                                lambda text: re.sub(r"^\| ordering scenes.*\n", "", text, count=1, flags=re.M)),
         True, "scenes.md has no row"),
        ("maps: a map row points into another skill without naming it", maps,
         lambda copy_root: edit(copy_root, ".claude/skills/character/SKILL.md", replace_once(
             "| You are... | Open | To get |\n|---|---|---|\n",
             "| You are... | Open | To get |\n|---|---|---|\n| fearing | `references/suspense-and-fear.md` | fear |\n")),
         True, "suspense-and-fear.md"),
        ("maps, neighbour: the same pointer naming its skill (plot)", maps,
         lambda copy_root: edit(copy_root, ".claude/skills/character/SKILL.md", replace_once(
             "| You are... | Open | To get |\n|---|---|---|\n",
             "| You are... | Open | To get |\n|---|---|---|\n"
             "| fearing | the plot skill's `references/suspense-and-fear.md` | fear |\n")), False, None),
        ("maps: a pointer whose skill is named only far back on the line", maps,
         add_to_traps("character", "- The plot skill " + "is where this is treated at length, " * 4
                      + "see `references/suspense-and-fear.md`."), True, "suspense-and-fear.md"),
        ("maps: a pointer to section 17 of a nine-section module", maps,
         add_to_traps("plot", "- See section 17 of `references/scenes.md`."), True, "section 17"),
        ("maps, neighbour: a pointer to section 9 of the same module", maps,
         add_to_traps("plot", "- See section 9 of `references/scenes.md`."), False, None),
        ("maps: a module with no row or node", maps,
         lambda copy_root: write(copy_root, ".claude/skills/plot/references/orphan.md", "# Orphan\n"), True,
         "orphan.md"),
        ("maps: a misspelt path", maps,
         lambda copy_root: edit(copy_root, ".claude/skills/dialogue/SKILL.md",
                                lambda text: text.replace("references/voice.md", "references/voise.md", 1)), True,
         "voise.md"),
        ("maps: a description over the length limit", maps,
         lambda copy_root: edit(copy_root, ".claude/skills/plot/SKILL.md",
                                lambda text: text.replace("description: ", "description: " + "x" * 1100, 1)), True,
         "limit"),
        ("maps: a shared passage changed in one skill only", maps,
         lambda copy_root: change_shared_passage(copy_root, ("plot",)), True, "differs"),
        ("maps, neighbour: the shared passage changed the same way in all five", maps,
         lambda copy_root: change_shared_passage(copy_root, CRAFT_SKILLS), False, None),
        ("maps: a shared passage's opening marker deleted in one skill, and that copy changed", maps,
         lambda copy_root: (edit(copy_root, ".claude/skills/plot/SKILL.md",
                                 lambda text: re.sub(r"<!-- shared: reply-check;[^>]*-->\n", "", text, count=1)),
                            change_shared_passage(copy_root, ("plot",))), True, "should carry the shared passage"),
        ("records: an old log entry rewritten", records,
         lambda copy_root: edit(copy_root, PROJECT_STORY, replace_once("5. **", "5. **Rewritten. ")), True,
         "log entry 5 has been changed"),
        ("records: the end of an old entry's first line rewritten (entry 12)", records,
         lambda copy_root: edit(copy_root, PROJECT_STORY, lambda text: re.sub(
             r"^(12\. \*\*[^\n]*)$", lambda match: match.group(1) + " Rewritten.", text, count=1, flags=re.M)),
         True, "log entry 12 has been changed"),
        ("records: an indented line inside an old entry rewritten (entry 29)", records,
         lambda copy_root: edit(copy_root, PROJECT_STORY, replace_once(
             "    - **What they found, in plain words.** The commit gate could be got round:",
             "    - **What they found, in plain words.** The commit gate could not be got round:")), True,
         "log entry 29 has been changed"),
        ("hooks registered: the session-start hook taken out of the settings", everything,
         lambda copy_root: edit(copy_root, ".claude/settings.json", lambda text: text.replace(
             '"SessionStart"', '"SessionStartOff"', 1)), True,
         "hook runs .claude/hooks/session_start.py"),
        ("hooks registered: every hook switched off in the settings (disableAllHooks)", everything,
         lambda copy_root: edit(copy_root, ".claude/settings.json", replace_once(
             '{\n  "hooks"', '{\n  "disableAllHooks": true,\n  "hooks"')), True, "disableAllHooks"),
        ("hooks registered: the session-start hook narrowed to new sessions only", everything,
         lambda copy_root: edit(copy_root, ".claude/settings.json", replace_once(
             '"startup|resume|clear|compact"', '"startup"')), True, "no SessionStart for resume hook"),
        ("hooks registered: the frozen-file hook no longer covering MultiEdit", everything,
         lambda copy_root: edit(copy_root, ".claude/settings.json", replace_once(
             '"Edit|Write|MultiEdit|NotebookEdit"', '"Edit|Write"')), True, "no PreToolUse for MultiEdit hook"),
        ("hooks registered, neighbour: the frozen-file hook's matcher written as a pattern covering every tool",
         everything, lambda copy_root: edit(copy_root, ".claude/settings.json", replace_once(
             '"Edit|Write|MultiEdit|NotebookEdit"', '".*"')), False, None),
        ("hooks registered: the hook that refuses ways round the gate taken out", everything,
         lambda copy_root: edit(copy_root, ".claude/settings.json", replace_once(
             "refuse_check_bypass.py", "some_other_hook.py")), True, "no PreToolUse for Bash hook runs"),
        ("hooks registered, neighbour: another hook added beside the workshop's", everything,
         lambda copy_root: edit(copy_root, ".claude/settings.json", replace_once(
             '"PostToolUse": [', '"PostToolUse": [\n      {"matcher": "Read", "hooks": [{"type": "command", "command":'
             ' "true"}]},')), False, None),
        ("no book files: the one large record allowed by name, once its contents change", everything,
         lambda copy_root: edit(copy_root, "kept-cases/runs/2026-09-24-before-entry-27.md",
                                lambda text: text + "\nAn added line.\n"), True, "a large text file"),
        ("no book files, neighbour: the one large record allowed by name, with Windows line endings", everything,
         lambda copy_root: edit(copy_root, "kept-cases/runs/2026-09-24-before-entry-27.md",
                                lambda text: text.replace("\n", "\r\n")), False, None),
        ("records: the last committed entry rewritten", records,
         lambda copy_root: edit(copy_root, PROJECT_STORY, lambda text: re.sub(
             r"^(" + str(last_entry_number(copy_root)) + r"\. \*\*[^\n]*)$",
             lambda match: match.group(1) + " Rewritten.", text, count=1, flags=re.M)),
         True, "has been changed since"),
        ("records, neighbour: a correction note under an old entry, pointing to a later one", records,
         lambda copy_root: edit(copy_root, PROJECT_STORY, lambda text: re.sub(
             r"(^5\. \*\*.*$)", r"\1\n    *Corrected in entry " + str(last_entry_number(copy_root)) + ":* a planted note.",
             text, count=1, flags=re.M)), False, None),
        ("records: a correction note pointing to an earlier entry", records,
         lambda copy_root: edit(copy_root, PROJECT_STORY, lambda text: re.sub(
             r"(^5\. \*\*.*$)", r"\1\n    *Corrected in entry 3:* a planted note.", text, count=1, flags=re.M)), True,
         "not a later entry"),
        ("records, neighbour: a new entry with every status line restamped", records,
         lambda copy_root: add_log_entry(copy_root, restamp=True), False, None),
        ("records: a new entry with the status lines left stale", records,
         lambda copy_root: add_log_entry(copy_root, restamp=False), True, "restamp"),
        ("records: an unindented numbered list inside a new entry", records,
         lambda copy_root: add_log_entry(copy_root, restamp=True, body="Steps:\n1. read the file;\n2. fixed the row."),
         True, "numbered line inside entry"),
        ("records, neighbour: the same list indented", records,
         lambda copy_root: add_log_entry(copy_root, restamp=True,
                                         body="Steps:\n    1. read the file;\n    2. fixed the row."), False, None),
        ("records: a numbered top-level file with no log entry", records,
         lambda copy_root: (write(copy_root, "99 Stray note.md", "# 99 Stray note\n"),
                            edit(copy_root, "README.md", lambda text: text + "\n`99 Stray note.md`\n")), True,
         "no entry with that number"),
        ("records: a top-level file README does not name", records,
         lambda copy_root: write(copy_root, "Notes.md", "# Notes\n"), True, "does not name the top-level file"),
        ("records: a skill cites an owner question that does not exist", records,
         add_to_traps("plot", "- An open point (owner question Q42)."), True, "Q42, which is not in"),
        ("records, neighbour: a skill cites an open owner question", records,
         add_to_traps("plot", "- An open point (owner question Q2)."), False, None),
        ("records: a skill cites an owner question marked answered", records,
         lambda copy_root: (add_to_traps("plot", "- An open point (owner question Q2).")(copy_root),
                            set_question_status(copy_root, "Q2", "answered")), True,
         r"plot/SKILL\.md:\d+: rests on owner question Q2"),
        ("records, neighbour: the cited question is being rechecked", records,
         lambda copy_root: (add_to_traps("plot", "- An open point (owner question Q2).")(copy_root),
                            set_question_status(copy_root, "Q2", "rechecking")), False, None),
        ("records: two questions answered, but only the second marked beside its number", records,
         lambda copy_root: (add_planted_questions(copy_root),
                            add_to_traps("plot", "- Two points (owner questions S98 and S99, answered: a).")(copy_root)),
         True, "rests on owner question S98"),
        ("records, neighbour: each of the two marked answered beside its own number", records,
         lambda copy_root: (add_planted_questions(copy_root), add_to_traps(
             "plot", "- Two points (owner question S98, answered: a; owner question S99, answered: b).")(copy_root)),
         False, None),
        ("records, neighbour: a kept case cites an answered question; it is listed, never failed", records,
         lambda copy_root: (add_planted_questions(copy_root),
                            edit(copy_root, "kept-cases/03-villain-with-four-blank-levers.md",
                                 lambda text: text + "\n- A planted open point (S98).\n")), False,
         r"kept-cases/03[^:]*:\d+: this kept case cites S98"),
        ("records, neighbour: while a question is being rechecked, a kept case citing it is listed", records,
         lambda copy_root: (add_planted_questions(copy_root), edit(copy_root, named(copy_root, "22 Questions"),
                            replace_once("S98. Planted.** A planted question. Status: answered.",
                                         "S98. Planted.** A planted question. Status: rechecking.")),
                            edit(copy_root, "kept-cases/03-villain-with-four-blank-levers.md",
                                 lambda text: text + "\n- A planted open point (S98).\n")), False,
         r"kept-cases/03[^:]*:\d+: this kept case cites S98"),
        ("records: a correction note under an old entry changed", records,
         lambda copy_root: edit(copy_root, PROJECT_STORY, replace_once("*Corrected in entry 28:* the two misreadings",
                                                                       "*Corrected in entry 28:* the misreadings")),
         True, "a correction note under log entry 22"),
        ("records: hidden text in the log", records,
         lambda copy_root: edit(copy_root, PROJECT_STORY, replace_once("\n3. **", "\n<!-- hidden -->\n3. **")),
         True, "hidden text"),
        ("records: a correction with no status", records,
         lambda copy_root: edit(copy_root, named(copy_root, corrections),
                                lambda text: re.sub(r"(### C1\..*?)Status:", r"\1State:", text, count=1, flags=re.S)),
         True, "C1 needs"),
        ("records: the corrections file names a check that does not exist", records,
         lambda copy_root: edit(copy_root, named(copy_root, corrections),
                                lambda text: text + "\nNow caught by `check_nothing.py`.\n"), True, "check_nothing.py"),
        ("records: a test write-up without its checks section", records,
         lambda copy_root: edit(copy_root, named(copy_root, catch),
                                replace_once("## Checks run on these notes", "## Notes")), True,
         "Checks run on these notes"),
        ("owner quotes: a quotation of a theory altered", quotes,
         lambda copy_root: edit(copy_root, TERM_SHEET, replace_once("“The bond is a promise.”",
                                                                    "“The bond is a contract.”")), True, "contract"),
        ("owner quotes: a quotation credited to the wrong theory", quotes,
         lambda copy_root: edit(copy_root, TERM_SHEET, replace_once("“The bond is a promise.” (Bond",
                                                                    "“The bond is a promise.” (Gap")), True,
         "credited to the Gap theory"),
        ("owner quotes: a made-up quotation in straight quotes, credited to a theory", quotes,
         lambda copy_root: edit(copy_root, TERM_SHEET, lambda text: text
                                + '\n"The bond is a contract, signed in blood." (Bond, The limits of care)\n'),
         True, "signed in blood"),
        ("owner quotes: a made-up quotation cited '(from Bond, ...)'", quotes,
         lambda copy_root: edit(copy_root, TERM_SHEET, lambda text: text
                                + '\n"Care is a contract." (from Bond, The limits of care)\n'),
         True, "Care is a contract"),
        ("no book files: a book copy forced into git", everything,
         lambda copy_root: (write(copy_root, "sources/raw/book.txt", "text\n"),
                            git(copy_root, "add", "-f", "sources/raw/book.txt")), True, "FAILED    no book files"),
        ("no book files, neighbour: a book copy git ignores", everything,
         lambda copy_root: write(copy_root, "sources/raw/book.txt", "text\n"), False, None),
        ("no book files: a large text file elsewhere", everything,
         lambda copy_root: write(copy_root, "notes/big.txt", "word " * 30000), True, "FAILED    no book files"),
        ("allowed titles: a phrase from a book added to the allowed list", everything,
         lambda copy_root: edit(copy_root, ".claude/skills/add-source/scripts/overlap-allowed.txt",
                                lambda text: text + "the lantern keeper counted every ship\n"), True,
         "FAILED    allowed titles"),
        ("allowed titles: a single word cut from a title put on the allowed list", everything,
         lambda copy_root: edit(copy_root, ".claude/skills/add-source/scripts/overlap-allowed.txt",
                                lambda text: text + "the\n"), True, "FAILED    allowed titles"),
        ("a check script that breaks is reported as could not run, never as passed", everything,
         break_a_script(os.path.join(SCRIPTS, "check_owner_quotes.py")), True, r"COULD NOT RUN\s+owner quotes"),
    ]


def single_check_test(repository_root, name, command, plant, expect_caught, must_print):
    copy_root = copy_repository(repository_root)
    try:
        plant(copy_root)
        code, output = run(copy_root, command[0], *command[1:], copy_root)
        passed = (code == 1) if expect_caught else (code == 0)
        if passed and must_print and not re.search(must_print, output):
            passed, output = False, f"caught, but not for the planted reason (expected: {must_print})\n{output}"
    except Exception as problem:  # any failure to plant is reported, never hidden
        passed, output = False, f"could not plant the fault: {problem}"
    finally:
        shutil.rmtree(copy_root, ignore_errors=True)
    return name, passed, output


def copying_check_tests(repository_root):
    results = []
    copy_root = copy_repository(repository_root)
    books = tempfile.mkdtemp(prefix="workshop-book-")
    book = os.path.join(books, "made-up-book.txt")
    write(books, "made-up-book.txt", BOOK_TEXT)
    overlap = os.path.join(ADD_SOURCE_SCRIPTS, "overlap_check.py")
    module = ".claude/skills/plot/references/scenes.md"
    edit(copy_root, module, lambda text: text + "\nThe film is Once upon a time in the West, a title only.\n")
    code, output = run(copy_root, overlap, book, module)
    results.append(("copying, neighbour: an allowed film title with a word either side", code == 0, output))
    edit(copy_root, module, lambda text: text + "\nSurely duel of any cowboy picture sits in once upon a time in the west,"
                                                " a slow sad epic about railways rather soon.\n")
    code, output = run(copy_root, overlap, book, module)
    results.append(("copying: 7 copied words, a film title, then 7 more (14 outside the title)", code == 1, output))
    edit(copy_root, module, lambda text: text + "\nThe lantern keeper counted every ship that failed to come home.\n")
    code, output = run(copy_root, overlap, book, module)
    results.append(("copying: a run of eleven words from the book", code == 1, output))
    code, output = run(copy_root, overlap, os.path.join(books, "no-such-book.txt"), module)
    results.append(("copying: a missing book is reported as not run", code == 3 and "NOT RUN" in output, output))
    code, output = run(copy_root, overlap, book, ".claude/skils")
    results.append(("copying: a misspelt folder is reported as not run", code == 3 and "NOT RUN" in output, output))
    code, output = run(copy_root, overlap, book, module, environment={"N": "40"})
    results.append(("copying: a setting named N outside the command changes nothing", code == 1, output))
    write(copy_root, "drafts/notes.txt", "The lantern keeper counted every ship that failed to come home.\n")
    code, output = run(copy_root, overlap, book, "drafts")
    results.append(("copying: a copied run in a .txt file is read too", code == 1 and "notes.txt" in output, output))
    shutil.rmtree(copy_root)

    copy_root = copy_repository(repository_root)
    write(copy_root, "drafts/notes.md", "The lantern keeper counted every ship that failed to come home.\n")
    edit(copy_root, "README.md", lambda text: text + "\n`drafts/` holds drafts.\n")
    code, output = run(copy_root, os.path.join(SCRIPTS, "run_all_checks.py"), "--books-from", books, copy_root)
    results.append(("copying: a copied run in a new top-level folder", code == 1
                    and "FAILED    copying from books" in output, output))
    shutil.rmtree(copy_root)
    shutil.rmtree(books)
    return results


def fill_receipt(copy_root, reviewer, maker, verdict, report=True, commit=None, blank=()):
    extra = ["--commit", commit] if commit else []
    code, output = run(copy_root, os.path.join(SCRIPTS, "review_receipt.py"), "new", "--root", copy_root, *extra)
    path = RECEIPT_PATH.search(output)
    if not path:
        raise AssertionError(f"no receipt form was written: {output}")
    answers = {
        "Change": "a planted change, to test the receipts",
        "Maker": maker,
        "Reviewed by": reviewer,
        "Findings": "none",
        "Book text": "none added, because the change is a planted test line",
        "Verdict": verdict,
    }

    def fill(text):
        for name, answer in answers.items():
            text = re.sub(r"(\*\*" + re.escape(name) + r":\*\*)[^\n]*", lambda match: match.group(1)
                          + ("" if name in blank else " " + answer), text, count=1)
        if report:
            text = re.sub(r"(## Reviewer's report\n\n)\([^\n]*\)", r"\1" + ("The reviewer read the planted change"
                          " line by line against the theory it cites, ran the map and records checks, and found"
                          " nothing that bears. It named what it did not check: the other skills, the kept cases,"
                          " and the copying check, which cannot run without the books. Verdict: passed."), text)
        return text
    edit(copy_root, path.group(0), fill)
    git(copy_root, "add", path.group(0))
    return path.group(0)


def fresh_change(repository_root, line="- A planted rule, for testing the receipts."):
    copy_root = copy_repository(repository_root)
    add_to_traps("plot", line)(copy_root)
    git(copy_root, "add", "-A")
    return copy_root


def receipt_tests(repository_root):
    """Each receipt test runs on its own, so one that cannot be planted is named, and never hides the others."""
    results = []
    receipt = os.path.join(SCRIPTS, "review_receipt.py")

    def check(copy_root, *extra):
        return run(copy_root, receipt, "check", "--root", copy_root, *extra)

    def each(name, test):
        """Run one test in its own copy; a test that cannot be planted is reported as failed, by its own name."""
        copies = []

        def new_copy(make=copy_repository, **options):
            copy_root = make(repository_root, **options)
            copies.append(copy_root)
            return copy_root
        try:
            outcome = test(new_copy)
            results.extend(outcome if isinstance(outcome, list) else [outcome])
        except Exception as problem:  # any failure to plant is reported, never hidden
            results.append((name, False, f"could not plant the fault: {problem}"))
        for copy_root in copies:
            shutil.rmtree(copy_root, ignore_errors=True)

    def no_receipt_then_edited_after_review(new_copy):
        copy_root = new_copy(fresh_change)
        code, output = check(copy_root)
        outcome = [("receipts: a staged change to a skill with no receipt", code == 1, output)]
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed")
        code, output = check(copy_root)
        outcome.append(("receipts, neighbour: the same change with a complete receipt", code == 0, output))
        edit(copy_root, ".claude/skills/plot/SKILL.md", replace_once("for testing the receipts.",
                                                                     "for testing the receipts. Edited after review."))
        git(copy_root, "add", "-A")
        code, output = check(copy_root)
        outcome.append(("receipts: an edit made after the review", code == 1, output))
        return outcome

    each("receipts: a staged change to a skill with no receipt", no_receipt_then_edited_after_review)

    for name, arguments, must_print in (
        ("receipts: the reviewer is the maker", dict(reviewer="lead agent", maker="lead agent", verdict="passed"),
         "nobody grades their own work"),
        ("receipts: Maker, Reviewed by and Findings left empty",
         dict(reviewer="theory-checker", maker="lead agent", verdict="passed",
              blank=("Maker", "Reviewed by", "Findings")), "'Maker' is empty"),
        ("receipts: a full receipt without the reviewer's report",
         dict(reviewer="theory-checker", maker="lead agent", verdict="passed", report=False), "Reviewer's report"),
    ):
        def faulty_form(new_copy, name=name, arguments=arguments, must_print=must_print):
            copy_root = new_copy(fresh_change)
            fill_receipt(copy_root, **arguments)
            code, output = check(copy_root)
            return (name, code == 1 and must_print in output, output)
        each(name, faulty_form)

    def unfilled_form(new_copy):
        copy_root = new_copy(fresh_change)
        code, output = run(copy_root, receipt, "new", "--root", copy_root)
        path = RECEIPT_PATH.search(output).group(0)
        edit(copy_root, path, lambda text: re.sub(r"(\*\*Verdict:\*\*)[^\n]*", r"\1 passed", text))
        git(copy_root, "add", path)
        code, output = check(copy_root)
        return ("receipts: a form left unfilled except the verdict", code == 1 and "hint" in output, output)

    each("receipts: a form left unfilled except the verdict", unfilled_form)

    def light_receipt_for_a_check(new_copy):
        copy_root = new_copy()
        edit(copy_root, os.path.join(SCRIPTS, "check_records.py"), lambda text: text + "\n# a planted comment\n")
        git(copy_root, "add", "-A")
        fill_receipt(copy_root, "none", "lead agent", "light (a comment only)", report=False)
        code, output = check(copy_root)
        return ("receipts: a light receipt for a change to a check", code == 1 and "never enough" in output, output)

    each("receipts: a light receipt for a change to a check", light_receipt_for_a_check)

    def light_receipt_for_a_typo(new_copy):
        copy_root = new_copy(fresh_change)
        fill_receipt(copy_root, "none", "lead agent", "light (a typo in a trap line)", report=False)
        code, output = check(copy_root)
        return ("receipts, neighbour: a light receipt for a typo in a skill", code == 0, output)

    each("receipts, neighbour: a light receipt for a typo in a skill", light_receipt_for_a_typo)

    def accented_module(new_copy):
        copy_root = new_copy()
        write(copy_root, ".claude/skills/plot/references/café.md", "# A module with an accented name\n")
        git(copy_root, "add", "-A")
        code, output = check(copy_root)
        return ("receipts: a new module with an accented name and no receipt", code == 1
                and "no review receipt" in output, output)

    each("receipts: a new module with an accented name and no receipt", accented_module)

    def record_needs_no_receipt(new_copy):
        copy_root = new_copy()
        edit(copy_root, PROJECT_STORY, lambda text: text.replace("## Word list", "## Word list\n\n- **Planted:** a record.", 1))
        git(copy_root, "add", "-A")
        code, output = check(copy_root)
        return ("receipts, neighbour: a change to a record needs no receipt", code == 0, output)

    each("receipts, neighbour: a change to a record needs no receipt", record_needs_no_receipt)

    def not_passed_for_a_staged_change(new_copy):
        copy_root = new_copy(fresh_change)
        fill_receipt(copy_root, "theory-checker", "lead agent", "not passed (withdrawn in this commit)")
        code, output = check(copy_root)
        return ("receipts: 'not passed' for a staged change", code == 1 and "must begin with one of" in output, output)

    each("receipts: 'not passed' for a staged change", not_passed_for_a_staged_change)

    def late_receipt_not_passed(new_copy):
        copy_root = new_copy(fresh_change)
        git(copy_root, *NO_SIGNING, "commit", "-q", "-m", "unreviewed")
        commit = git(copy_root, "rev-parse", "HEAD").stdout.strip()
        fill_receipt(copy_root, "theory-checker", "lead agent", "not passed (withdrawn in the next commit)",
                     commit=commit)
        code, output = check(copy_root, "--commit", commit)
        return ("receipts, neighbour: a late receipt may record a review that did not pass", code == 0
                and "did not pass" in output, output)

    each("receipts, neighbour: a late receipt may record a review that did not pass", late_receipt_not_passed)

    def late_receipt_found(new_copy):
        copy_root = new_copy(fresh_change)
        git(copy_root, *NO_SIGNING, "commit", "-q", "-m", "unreviewed")
        commit = git(copy_root, "rev-parse", "HEAD").stdout.strip()
        code, output = check(copy_root, "--commit", commit)
        missing_first = code == 1
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed", commit=commit)
        git(copy_root, *NO_SIGNING, "commit", "-q", "-m", "late receipt")
        code, output = check(copy_root, "--commit", commit)
        return ("receipts, neighbour: a receipt written late, in a later commit, is found", missing_first
                and code == 0, output)

    each("receipts, neighbour: a receipt written late, in a later commit, is found", late_receipt_found)

    def book_registered_with_its_module(new_copy):
        copy_root = new_copy()
        edit(copy_root, "sources/README.md", replace_once(
            "| Work | Edition read | Supplied | Feeds | Overlap check |\n|---|---|---|---|---|\n",
            "| Work | Edition read | Supplied | Feeds | Overlap check |\n|---|---|---|---|---|\n"
            "| Marian Placeholder, *A Made-Up Book on Endings* | planted | planted | plot | pending |\n"))
        write(copy_root, ".claude/skills/plot/references/planted-endings.md",
              "# Planted endings\n\nPlaceholder's rule of endings, written for the test.\n")
        git(copy_root, "add", "-A")
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed", blank=("Book text",))
        code, output = check(copy_root)
        return ("receipts: a book registered in the same commit as a module drawing on it, with the books absent,"
                " needs the Book-text line", code == 1 and "Book text" in output, output)

    each("receipts: a book registered in the same commit as a module drawing on it needs the Book-text line",
         book_registered_with_its_module)

    def module_drawing_on_mckee_alone(new_copy):
        copy_root = new_copy()
        write(copy_root, ".claude/skills/dialogue/references/planted-mckee.md",
              "# A planted module\n\nMcKee's point, restated for the test.\n")
        git(copy_root, "add", "-A")
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed", blank=("Book text",))
        code, output = check(copy_root)
        return ("receipts: a module drawing on McKee alone, with the books absent, needs the Book-text line",
                code == 1 and "Book text" in output, output)

    each("receipts: a module drawing on McKee alone needs the Book-text line", module_drawing_on_mckee_alone)
    return results


def gate_commit(copy_root, *arguments):
    git(copy_root, "config", "core.hooksPath", ".githooks")
    result = git(copy_root, *NO_SIGNING, "commit", "-q", *arguments, check=False)
    return result.returncode, result.stdout + result.stderr


def commit_skipping_the_gate(copy_root, message):
    git(copy_root, "add", "-A")
    git(copy_root, *NO_SIGNING, "commit", "-q", SKIP_THE_GATE, "-m", message)


def record_change(copy_root, text="a record"):
    edit(copy_root, PROJECT_STORY,
         lambda story: story.replace("## Word list", f"## Word list\n\n- **Planted:** {text}.", 1))
    git(copy_root, "add", "-A")


def gate_tests(repository_root):
    return the_gate_tests("gate_tests")(repository_root)


def more_gate_tests(repository_root):
    return the_gate_tests("more_gate_tests")(repository_root)


def the_gate_tests(name):
    """The commit gate's tests, kept in test_the_gate.py beside this file, which hands them this file's helpers."""
    def run_them(repository_root):
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import test_the_gate
        return getattr(test_the_gate, name)(repository_root, sys.modules[__name__])
    return run_them


HOOK_COMMANDS = (
    # (command, should be refused, should get the claim reminder)
    ("git add -A && git commit -m done", False, True),
    (f"git commit {SKIP_THE_GATE} -m done", True, True),
    ("git commit -nam done", True, True),
    ("git commit --no-veri -m x", True, True),
    ("git -c core.hookspath=/dev/null commit -m x", True, True),
    ("git -c core.hooksPath=.githooks commit -m x", False, True),
    ('git commit -m "fix; & other -n stuff"', False, True),
    ('git commit -m "$(cat <<\'EOF\'\nmessage line\nEOF\n)" ' + SKIP_THE_GATE, True, True),
    ('git -C "folder with space" commit -n', True, True),
    ("env git commit -n", True, True),
    ("/usr/bin/git commit -n -m x", True, True),
    ("GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.hooksPath GIT_CONFIG_VALUE_0=/dev/null git commit -m x", True, True),
    ("rm .githooks/pre-commit", True, False),
    ("cd .githooks && cat > pre-commit <<'E'\nexit 0\nE", True, False),
    ("chmod -x .githooks/pre-commit", True, False),
    ("chmod +x .githooks/pre-commit", False, False),
    (f'git commit -m "mentions {SKIP_THE_GATE} and -n here"', False, True),
    ("git config core.hooksPath || echo off", False, False),
    ("git config --get core.hooksPath", False, False),
    ("git config core.hooksPath elsewhere", True, False),
    ("git config --unset core.hooksPath", True, False),
    ("git config unset core.hooksPath", True, False),
    ("git config core.hooksPath .githooks", False, False),
    ("cd /tmp && git config core.hooksPath hooks", False, False),
    ("git -C /tmp commit -n -m x", False, True),
    (f"cat > notes.md <<END\ngit commit {SKIP_THE_GATE}\nEND", False, False),
    ("echo 'git will save a commit'", False, False),
    ("git commit --amend -m x", False, True),
    ("git commit -m new", False, True),
    (f"git merge {SKIP_THE_GATE} feature", True, False),
    ("bash -c 'git commit -n -m x'", True, True),
    ("eval 'git commit -n -m x'", True, True),
    ("git rev-parse HEAD > .git/workshop-gate-passed", True, False),
    ("sed --in-place s/a/b/ .githooks/pre-commit", True, False),
    ("bash -c 'echo hello'", False, False),
    ("git commit -m \"fix: eval 'git commit -n' is refused now\"", False, True),
    ("echo \"run: bash -c 'git commit -n -m x' to skip\" > notes.md", False, False),
    ("ls .git/workshop-* 2>/dev/null", False, False),
    ("bash -c 'cd /tmp && git commit -n -m x'", False, True),
    ('git config core.hooksPath "$PWD/.githooks"', False, False),
    ("git config core.hooksPath '$PWD/.githooks'", True, False),
    ('cd .claude && git config core.hooksPath "$PWD/.githooks"', True, False),
    ("bash -lc 'git commit -n -m x'", True, True),
    ("rm .git/workshop-gate-passed", True, False),
    ('git config core.hooksPath "/tmp/an-old-copy/.githooks"', True, False),
    ("GIT_CONFIG_PARAMETERS=\"'core.hookspath=/dev/null'\" git commit -m x", True, True),
)


def hook_tests(repository_root):
    results = []
    copy_root = copy_repository(repository_root)
    environment = {"CLAUDE_PROJECT_DIR": copy_root}
    protect = os.path.join(HOOKS, "protect_frozen_files.py")
    for path, should_refuse in (("sources/bond-theory.md", True), ("sources/README.md", False),
                                ("sources/bond-theory-revision-1.md", False)):
        hook_input = json.dumps({"tool_name": "Edit", "tool_input": {"file_path": os.path.join(copy_root, path)},
                                 "cwd": copy_root})
        code, output = run(copy_root, protect, stdin_text=hook_input, environment=environment)
        results.append((f"hook: {'refuses' if should_refuse else 'allows'} an edit to {path}",
                        code == 0 and ('"deny"' in output) == should_refuse, output))
    other_repository = tempfile.mkdtemp(prefix="workshop-other-")
    git(other_repository, "init", "-q")
    hook_input = json.dumps({"tool_name": "Write", "tool_input": {
        "file_path": os.path.join(copy_root, "sources/bond-theory.md")}, "cwd": other_repository})
    code, output = run(copy_root, protect, stdin_text=hook_input, environment={"CLAUDE_PROJECT_DIR": other_repository},
                       working_folder=other_repository)
    results.append(("hook: refuses an edit to a frozen file made from another repository's folder",
                    '"deny"' in output, output))
    shutil.rmtree(other_repository)

    bypass = os.path.join(HOOKS, "refuse_check_bypass.py")
    after = os.path.join(HOOKS, "after_commit.py")
    for command, should_refuse, should_remind in HOOK_COMMANDS:
        hook_input = json.dumps({"tool_name": "Bash", "tool_input": {"command": command}, "cwd": copy_root})
        _, refused = run(copy_root, bypass, stdin_text=hook_input, environment=environment)
        _, reminded = run(copy_root, after, stdin_text=hook_input, environment=environment)
        shown = " ".join(command.split())[:48]
        results.append((f"hook: '{shown}' is {'refused' if should_refuse else 'let through'}"
                        f" and {'gets' if should_remind else 'does not get'} the claim reminder",
                        ('"deny"' in refused) == should_refuse and ("additionalContext" in reminded) == should_remind
                        and "could not run" not in refused + reminded, refused + reminded))

    command = 'git config core.hooksPath "$PWD/.githooks"'
    for folder, should_refuse in ((os.path.join(copy_root, "sources"), True), (copy_root, False)):
        hook_input = json.dumps({"tool_name": "Bash", "tool_input": {"command": command}, "cwd": folder})
        _, refused = run(copy_root, bypass, stdin_text=hook_input, environment=environment)
        where = "a folder inside the project" if should_refuse else "the project's top folder"
        results.append((f"hook: the gate folder named by $PWD from {where} is "
                        f"{'refused' if should_refuse else 'let through'}",
                        ('"deny"' in refused) == should_refuse and "could not run" not in refused, refused))

    code, output = run(copy_root, os.path.join(HOOKS, "session_start.py"), environment=environment)
    hooks_path = git(copy_root, "config", "core.hooksPath", check=False).stdout.strip()
    results.append(("hook: session start switches the commit gate on and prints the status",
                    hooks_path == ".githooks" and "Last log entry" in output and "none failing" in output
                    and "Open corrections" in output and "Commit gate: on" in output, output))
    add_to_traps("plot", "- A rule committed with the gate skipped.")(copy_root)
    commit_skipping_the_gate(copy_root, "skipped")
    code, output = run(copy_root, os.path.join(HOOKS, "session_start.py"), environment=environment)
    results.append(("hook: session start reports a commit the gate never approved",
                    "Commits the gate did not approve" in output, output))
    break_a_script(os.path.join(SCRIPTS, "run_all_checks.py"))(copy_root)
    git(copy_root, "add", "-A")  # a broken check in a commit stamped as approved (session start uses that commit's)
    tree = git(copy_root, "write-tree").stdout.strip()
    git(copy_root, *NO_SIGNING, "commit", "-q", SKIP_THE_GATE, "-m", f"broken\n\nWorkshop-gate: approved {tree}")
    code, output = run(copy_root, os.path.join(HOOKS, "session_start.py"), environment=environment)
    results.append(("hook: session start says the checks could not run when they are broken",
                    "Machine checks: could not run" in output, output))
    shutil.rmtree(copy_root)

    copy_root = copy_repository(repository_root)
    add_log_entry(copy_root, True)
    edit(copy_root, PROJECT_STORY, replace_once("5. **", "5. **Rewritten. "))
    code, output = run(copy_root, os.path.join(HOOKS, "session_start.py"), environment={"CLAUDE_PROJECT_DIR": copy_root})
    results.append(("hook: session start shows the lines under a failing check, not the check's own notes",
                    "log entry 5 has been changed" in output and "look at each status line again" not in output
                    and "*Updated" not in output, output))
    shutil.rmtree(copy_root)
    return results


def setting_tests(repository_root):
    """The planted-fault test's own setting skips nothing outside the test's copies."""
    copy_root = copy_repository(repository_root)
    plain_folder = tempfile.mkdtemp(prefix="workshop-plain-")
    nested_folder = os.path.join(copy_root, "workshop-test-inside")
    os.makedirs(nested_folder)
    results = []
    for script in ("check_commit",):
        asking = (f"import sys; sys.path.insert(0, {os.path.join(copy_root, SCRIPTS)!r}); import {script}; "
                  f"print([{script}.inside_the_planted_fault_test(folder) for folder in "
                  f"({copy_root!r}, {plain_folder!r}, {nested_folder!r})])")
        result = subprocess.run([sys.executable, "-c", asking], capture_output=True, text=True, check=False,
                                env={**os.environ, "WORKSHOP_INSIDE_PLANTED_FAULT_TEST": "1"})
        output = result.stdout + result.stderr
        results.append((f"{script}: the planted-fault test's setting, set outside the test's own copies, skips"
                        " nothing", "[True, False, False]" in output, output))
    shutil.rmtree(copy_root, ignore_errors=True)
    shutil.rmtree(plain_folder, ignore_errors=True)
    return results


def main():
    repository_root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
    jobs = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        def unchanged_copy():
            copy_root = copy_repository(repository_root)
            code, output = run(copy_root, os.path.join(SCRIPTS, "run_all_checks.py"), "--skip-books", copy_root)
            shutil.rmtree(copy_root)
            return [("the unchanged copy passes every check", code == 0, output)]

        def as_group(function):
            def group():
                try:
                    return function(repository_root)
                except Exception as problem:  # a group that breaks is reported, never hidden
                    return [(f"{function.__name__} could not run", False, str(problem))]
            return group

        jobs.append(pool.submit(unchanged_copy))
        for test in tests():
            jobs.append(pool.submit(lambda test=test: [single_check_test(repository_root, *test)]))
        for function in (copying_check_tests, receipt_tests, gate_tests, more_gate_tests, hook_tests,
                         setting_tests):
            jobs.append(pool.submit(as_group(function)))
        results = [result for job in jobs for result in job.result()]

    for folder in LEFT_OVER:
        shutil.rmtree(folder, ignore_errors=True)
    failures = 0
    for name, passed, output in results:
        print(f"{'ok    ' if passed else 'FAILED'}  {name}")
        if not passed:
            failures += 1
            for line in output.strip().splitlines()[:14]:
                print(f"          {line}")
    for name in NOT_RUN:
        print(f"not run  {name}")
    print(f"TOTAL tests: {len(results)}, failed: {failures}" + (f", not run: {len(NOT_RUN)}" if NOT_RUN else ""))
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
