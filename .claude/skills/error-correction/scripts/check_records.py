#!/usr/bin/env python3
"""Check that the workshop's records are honest and current.

The records are the project story (its numbered log and its status
lines), the README's "What is where" table, the questions file, the
corrections file, write-ups of tests and critiques, and the kept cases'
run record. What it checks:

1. The log is only ever added to. Every numbered entry in the last commit
   is still there, word for word. The one thing that may be added to an
   old entry is a line beginning "*Corrected in entry N:*", pointing
   forward to the entry that corrects it; N must be an entry that exists
   and comes later. Such a line, once there, is never changed either, and
   the log may hold no hidden text ("<!--" ... "-->").
2. The log's entries run 1, 2, 3 ... with no gap or repeat. An entry is a
   line "N. **Title**" at the start of a line; a numbered list inside an
   entry must be indented, so it is never read as an entry.
3. Every line under "Where things stand", and the "Next step", ends with
   "(as of entry N)", where N is the last entry. So each new entry forces
   every status line to be looked at again.
4. Every top-level file named with a number has a log entry with that
   number.
5. README.md names every top-level .md file, every top-level folder that
   is not hidden, and every skill folder.
6. Owner questions (Q1 ... and S1 ... in the questions file) each have a
   status: open, rechecking (answered, and the passages resting on it are
   being rechecked) or answered. A question number cited in a skill must
   exist. A citation of an answered question in a skill is flagged unless
   "answered" follows that question's own number, before any other
   question number and inside the same brackets, which says the passage
   was rechecked. Kept cases are never changed once run, so a kept case
   that cites an answered question is listed as a note (a new case is
   owed), not flagged; the run records (kept-cases/runs.md, runs/) are not
   searched. While a question is being rechecked, the skill passages that
   cite it are listed as notes.
7. Corrections in the corrections file (C1, C2 ...) each have a status,
   open or closed, and no number is used twice. Every file path the
   corrections file names in backticks exists, so "now caught by" cannot
   name a check that is gone. Every correction number the project story
   cites exists.
8. A numbered write-up of a test or a critique ("NN Test - ...",
   "NN Critique - ...") has a section "## Checks run on these notes".

It also prints, as notes that do not fail the run: kept cases not rerun
since a skill they test changed; questions being rechecked; and, when the
log has an entry the last commit did not, every status line, so that each
is looked at again rather than only restamped.

Exit code 1 if there is any problem, 0 if there is none. A part that
cannot be checked is printed as "not checked", never as passed.

Usage: check_records.py [--against COMMIT] [--also-against COMMIT]... [--git-root PATH]
                        [--log-only [--commit COMMIT]] [REPOSITORY_ROOT]
       check_records.py --fingerprints [SKILL ...] [--root REPOSITORY_ROOT]
  --git-root: where the git history is, when REPOSITORY_ROOT is a copy of
  the files about to be committed (default: REPOSITORY_ROOT).
  --also-against: for a merge, the commit being merged in (the gate passes
  it): every log entry it added since the two lines of work split must be
  kept, by number and text, as the entries of --against are. When both
  lines added an entry with the same number, the merge cannot keep both,
  and the message says to rebase instead.
  --log-only: check only that the log was added to since --against; with
  --commit, that the log in that commit was only added to since its parent
  (recheck_commits.py uses this).
  --fingerprints: print the line to add to kept-cases/runs.md. With no
  skill named (after a full kept-case run), every skill's current code.
  With skills named (after a change to them that alters no meaning), only
  those skills get their new code, and only if their code in the last
  commit matched the last run; every other skill keeps its code from the
  last run, so a skill still owed a rerun stays listed.
"""
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile

PROJECT_STORY = "StoryTest - project story.md"
QUESTIONS_PREFIX = "22 Questions"
CORRECTIONS_PREFIX = "27 Corrections"
ENTRY_START = re.compile(r"^(\d+)\. \*\*", flags=re.M)
NUMBERED_LINE = re.compile(r"^(\d+)\. (?!\*\*)(.*)$", flags=re.M)
CORRECTION_NOTE = re.compile(r"^\s*\*Corrected in entry (\d+):\*")
QUESTION_ID = re.compile(r"\b([QS]\d{1,2})\b")
CORRECTION_ID = re.compile(r"\b(C\d{1,3})\b")
STAMP = re.compile(r"\(as of entry (\d+)\)")
PATH_IN_BACKTICKS = re.compile(r"`([A-Za-z0-9_./ -]+\.(?:md|py|txt|json|sh))`")


def read_text(path):
    with open(path, encoding="utf-8") as text_file:
        return text_file.read()


def top_level_file(repository_root, prefix):
    for name in sorted(os.listdir(repository_root)):
        if name.startswith(prefix) and name.endswith(".md"):
            return name
    return None


def section(text, heading):
    """The text under '## heading' up to the next '## ' heading, or None."""
    match = re.search(r"^## " + re.escape(heading) + r"\s*$", text, flags=re.M)
    if not match:
        return None
    rest = text[match.end():]
    next_heading = re.search(r"^## ", rest, flags=re.M)
    return rest[: next_heading.start()] if next_heading else rest


def log_entries(story_text):
    """Return {number: [texts]} for the numbered entries under '## Log'."""
    log_text = section(story_text, "Log")
    if log_text is None:
        return {}
    matches = list(ENTRY_START.finditer(log_text))
    entries = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(log_text)
        entries.setdefault(int(match.group(1)), []).append(log_text[match.start():end].rstrip())
    return entries


def without_correction_notes(entry_text):
    return "\n".join(line for line in entry_text.splitlines() if not CORRECTION_NOTE.match(line)).rstrip()


def correction_notes(entry_text):
    return [line.strip() for line in entry_text.splitlines() if CORRECTION_NOTE.match(line)]


def compare_logs(earlier_text, current_text, against):
    """Problems if the current log is not the earlier log with only entries and correction notes added."""
    problems = []
    log_text = section(current_text, "Log") or ""
    if "<!--" in log_text or "-->" in log_text:
        problems.append(f"{PROJECT_STORY}: the log holds hidden text ('<!--' or '-->'); nothing in the log is hidden")
    entries = log_entries(current_text)
    for number, earlier_versions in sorted(log_entries(earlier_text).items()):
        if number not in entries:
            problems.append(f"{PROJECT_STORY}: log entry {number} has been removed (it was in {against})")
            continue
        now = entries[number][0]
        if without_correction_notes(now) != without_correction_notes(earlier_versions[0]):
            problems.append(
                f"{PROJECT_STORY}: log entry {number} has been changed since {against}. Old entries are never"
                " rewritten; put it back, add a new entry that corrects it, and if you like add a line"
                " '*Corrected in entry N:* ...' under the old one"
            )
        elif any(note not in correction_notes(now) for note in correction_notes(earlier_versions[0])):
            problems.append(f"{PROJECT_STORY}: a correction note under log entry {number} has been changed or removed"
                            f" since {against}; notes are only ever added")
    return problems


def merge_base(git_root, first, second):
    result = subprocess.run(["git", "-C", git_root, "merge-base", first, second], capture_output=True, text=True,
                            check=False)
    return result.stdout.strip() if result.returncode == 0 else None


def compare_with_the_other_side(git_root, against, other, earlier_text, story_text):
    """For a merge: problems if an entry the other side added since the two lines split is changed or gone, and the
    numbers both sides added (whose plain 'put it back' advice would overwrite the other side's entry)."""
    other_text = committed_text(git_root, other, PROJECT_STORY)
    if other_text is None:
        return [], set()
    base = merge_base(git_root, against, other)
    base_numbers = set(log_entries(committed_text(git_root, base, PROJECT_STORY) or "")) if base else set()
    ours = set(log_entries(earlier_text or ""))
    entries = log_entries(story_text)
    problems, both = [], set()
    for number, versions in sorted(log_entries(other_text).items()):
        if number in base_numbers:
            continue  # an entry from before the split: judged against the last approved commit
        if number in entries and without_correction_notes(entries[number][0]) == without_correction_notes(versions[0]):
            continue
        if number in ours:
            both.add(number)
            problems.append(
                f"{PROJECT_STORY}: both lines of work being merged added a log entry {number} ({against[:9]} and"
                f" {other[:9]}), and a merge cannot keep both under one number without rewriting one of them. Abort"
                " the merge (git merge --abort) and rebase your branch onto the other line instead (git rebase"
                " <the other branch>), numbering your own new entries after its; the rebase keeps the other line's"
                " entries as they are, and the next commit is judged against them")
        else:
            problems.append(f"{PROJECT_STORY}: log entry {number}, which the commit being merged ({other[:9]}) added,"
                            " has been changed or removed; keep it as that commit has it")
    return problems, both


def committed_text(git_root, commit, path):
    result = subprocess.run(
        ["git", "-C", git_root, "show", f"{commit}:{path}"], capture_output=True, text=True, check=False
    )
    return result.stdout if result.returncode == 0 else None


def check_log(repository_root, git_root, against, problems, notes, also_against=()):
    story_path = os.path.join(repository_root, PROJECT_STORY)
    if not os.path.exists(story_path):
        problems.append(f"{PROJECT_STORY}: missing")
        return {}, ""
    story_text = read_text(story_path)
    entries = log_entries(story_text)
    if not entries:
        problems.append(f"{PROJECT_STORY}: no numbered entries found under '## Log'")
        return entries, story_text

    numbers = sorted(entries)
    last = numbers[-1]
    for number in numbers:
        if len(entries[number]) > 1:
            problems.append(f"{PROJECT_STORY}: log entry {number} appears {len(entries[number])} times")
        for text_of_entry in entries[number]:
            for inner in NUMBERED_LINE.finditer(text_of_entry):
                problems.append(f"{PROJECT_STORY}: a numbered line inside entry {number} ('{inner.group(0)[:40]}');"
                                " indent it, so it is not read as a log entry")
            for line in text_of_entry.splitlines():
                note = CORRECTION_NOTE.match(line)
                if note and (int(note.group(1)) not in entries or int(note.group(1)) <= number):
                    problems.append(f"{PROJECT_STORY}: under entry {number}, a correction note points to entry"
                                    f" {note.group(1)}, which is not a later entry in the log")
    missing = sorted(set(range(1, last + 1)) - set(numbers))
    if missing:
        problems.append(f"{PROJECT_STORY}: log entries missing: {', '.join(map(str, missing))}")

    for heading in ("Where things stand", "Next step"):
        body = section(story_text, heading)
        if body is None:
            problems.append(f"{PROJECT_STORY}: no '## {heading}' section")
            continue
        lines = [line for line in body.splitlines() if line.startswith("- ")] if heading == "Where things stand" else [body]
        if not lines:
            problems.append(f"{PROJECT_STORY}: '## {heading}' has no lines starting '- '")
        for line in lines:
            stamps = [int(number) for number in STAMP.findall(line)]
            shown = " ".join(line.split())[:70]
            if not stamps:
                problems.append(f"{PROJECT_STORY}: under '{heading}', no '(as of entry N)' on: {shown}")
            elif max(stamps) != last:
                problems.append(
                    f"{PROJECT_STORY}: under '{heading}', a line is as of entry {max(stamps)} but the last entry is {last};"
                    f" look at it again and restamp it: {shown}"
                )

    earlier_text = committed_text(git_root, against, PROJECT_STORY)
    if earlier_text is not None and log_entries(earlier_text) and last > max(log_entries(earlier_text)):
        status_lines = [line for heading in ("Where things stand", "Next step")
                        for line in (section(story_text, heading) or "").splitlines() if line.strip()]
        notes.append(f"entry {last} is new: look at each status line again, not only its stamp:\n    "
                     + "\n    ".join(" ".join(line.split())[:150] for line in status_lines))
    if earlier_text is None:
        notes.append(f"not checked: whether old log entries were rewritten (no version of the project story in {against})")
    else:
        own = compare_logs(earlier_text, story_text, against)
        both = set()
        for other in also_against:
            found, numbers = compare_with_the_other_side(git_root, against, other, earlier_text, story_text)
            problems += found
            both |= numbers
        problems += [problem for problem in own
                     if not any(problem.startswith(f"{PROJECT_STORY}: log entry {number} has been changed since")
                                for number in both)]
    return entries, story_text


def check_numbered_files(repository_root, entries, problems):
    for name in sorted(os.listdir(repository_root)):
        match = re.match(r"^(\d+) .*\.md$", name)
        if match and int(match.group(1)) not in entries:
            problems.append(f"{name}: named with number {int(match.group(1))}, but the log has no entry with that number")
        if match and re.match(r"^\d+ (Test|Critique)\b", name):
            if not re.search(r"^## Checks run on these notes", read_text(os.path.join(repository_root, name)), flags=re.M):
                problems.append(
                    f"{name}: a test or critique write-up needs a section '## Checks run on these notes'"
                    " (which checks were run on its own notes, with their results, or 'not run')"
                )


def check_readme(repository_root, problems):
    readme_path = os.path.join(repository_root, "README.md")
    if not os.path.exists(readme_path):
        problems.append("README.md: missing")
        return
    readme_text = read_text(readme_path)
    for name in sorted(os.listdir(repository_root)):
        full_path = os.path.join(repository_root, name)
        if name.startswith("."):
            continue
        if os.path.isfile(full_path) and name.endswith(".md") and name != "README.md" and name not in readme_text:
            problems.append(f"README.md: does not name the top-level file '{name}'")
        if os.path.isdir(full_path) and f"{name}/" not in readme_text:
            problems.append(f"README.md: does not name the top-level folder '{name}/'")
    skills_folder = os.path.join(repository_root, ".claude", "skills")
    if os.path.isdir(skills_folder):
        for skill_name in sorted(os.listdir(skills_folder)):
            if os.path.isdir(os.path.join(skills_folder, skill_name)) and f".claude/skills/{skill_name}/" not in readme_text:
                problems.append(f"README.md: does not name the skill folder '.claude/skills/{skill_name}/'")


def block_status(block_text):
    status = re.search(r"Status:\**\s*([A-Za-z]+)", block_text)
    return status.group(1).lower() if status else None


def blocks(text, marker_pattern):
    """Return {id: [block texts]} for items that start with marker_pattern."""
    markers = list(re.finditer(marker_pattern, text, flags=re.M))
    found = {}
    for index, marker in enumerate(markers):
        end = markers[index + 1].start() if index + 1 < len(markers) else len(text)
        next_heading = re.search(r"^## ", text[marker.end():end], flags=re.M)
        if next_heading:
            end = marker.end() + next_heading.start()
        found.setdefault(marker.group(1), []).append(text[marker.start():end])
    return found


def check_questions(repository_root, problems, notes):
    name = top_level_file(repository_root, QUESTIONS_PREFIX)
    if name is None:
        notes.append("not checked: owner questions (no questions file)")
        return
    questions = blocks(read_text(os.path.join(repository_root, name)), r"^(?:## |- \*\*)([QS]\d{1,2})\.")
    if not questions:
        problems.append(f"{name}: no numbered questions found (headings '## Q1.' or items '- **S1.')")
    for question_id, found in sorted(questions.items()):
        if len(found) > 1:
            problems.append(f"{name}: question {question_id} is used {len(found)} times")
        status = block_status(found[0])
        if status not in ("open", "rechecking", "answered"):
            problems.append(f"{name}: question {question_id} needs 'Status: open', 'Status: rechecking' or 'Status: answered'")
        if status == "rechecking":
            notes.append(f"question {question_id} is answered and its passages are being rechecked")
    kept_cases_folder = os.path.join(repository_root, "kept-cases")
    for searched in (os.path.join(repository_root, ".claude", "skills"), kept_cases_folder):
        for folder, folder_names, file_names in os.walk(searched):
            folder_names[:] = [name for name in folder_names if name != "runs"]
            for file_name in sorted(file_names):
                if not file_name.endswith(".md") or (searched == kept_cases_folder and file_name == "runs.md"):
                    continue
                file_path = os.path.join(folder, file_name)
                shown_file = os.path.relpath(file_path, repository_root)
                is_case = searched == kept_cases_folder
                for line_number, line in enumerate(read_text(file_path).splitlines(), start=1):
                    for match in QUESTION_ID.finditer(line):
                        question_id = match.group(1)
                        if question_id not in questions:
                            problems.append(f"{shown_file}:{line_number}: cites owner question {question_id}, which is not in {name}")
                            continue
                        status = block_status(questions[question_id][0])
                        if status == "rechecking" and not is_case and not marked_answered(line, match):
                            notes.append(f"{shown_file}:{line_number}: rests on {question_id}, which is being rechecked")
                        elif status in ("answered", "rechecking") and is_case:
                            notes.append(f"{shown_file}:{line_number}: this kept case cites {question_id}, which is"
                                         " answered; keep the case as it was run, and have a new case for the"
                                         " answered point written by an agent that has not read the skills"
                                         " (references/checks-and-cases.md, section 6)")
                        elif status == "answered" and not marked_answered(line, match):
                            problems.append(
                                f"{shown_file}:{line_number}: rests on owner question {question_id}, which is answered;"
                                " recheck this passage against the answer (error-correction skill,"
                                " references/owner-answers-and-revisions.md, section 2) and write 'answered' right"
                                f" after {question_id}, inside the same brackets"
                            )


def marked_answered(line, match):
    """True if 'answered' follows this question number, before any other question number and before its brackets close.

    "(owner question Q4, answered 30 Sep: option a)" marks Q4. In "(Q2 and Q4, answered)" only Q4 is marked, so a
    passage that rests on two questions says so for each."""
    closing = line.find(")", match.end())
    after = line[match.end(): closing if closing >= 0 else len(line)]
    next_question = QUESTION_ID.search(after)
    return "answered" in (after[: next_question.start()] if next_question else after).lower()


def check_corrections(repository_root, story_text, problems, notes):
    name = top_level_file(repository_root, CORRECTIONS_PREFIX)
    if name is None:
        notes.append("not checked: corrections (no corrections file)")
        return
    corrections_text = read_text(os.path.join(repository_root, name))
    corrections = blocks(corrections_text, r"^### (C\d{1,3})\.")
    for correction_id, found in sorted(corrections.items()):
        if len(found) > 1:
            problems.append(f"{name}: correction number {correction_id} is used {len(found)} times")
        if block_status(found[0]) not in ("open", "closed"):
            problems.append(f"{name}: correction {correction_id} needs 'Status: open' or 'Status: closed'")
    for mentioned in sorted(set(PATH_IN_BACKTICKS.findall(corrections_text))):
        if "<" in mentioned or "*" in mentioned:
            continue
        candidates = [os.path.join(repository_root, mentioned)]
        skills_folder = os.path.join(repository_root, ".claude", "skills")
        if os.path.isdir(skills_folder):
            candidates += [os.path.join(skills_folder, skill, mentioned) for skill in os.listdir(skills_folder)]
        for folder, _, file_names in os.walk(os.path.join(repository_root, ".claude")):
            if os.path.basename(mentioned) in file_names and "/" not in mentioned:
                candidates.append(os.path.join(folder, mentioned))
        if not any(os.path.exists(candidate) for candidate in candidates):
            problems.append(f"{name}: names `{mentioned}`, which does not exist")
    for correction_id in sorted(set(CORRECTION_ID.findall(story_text))):
        if correction_id not in corrections:
            problems.append(f"{PROJECT_STORY}: cites correction {correction_id}, which is not in {name}")


def folder_fingerprint(folder):
    digest = hashlib.sha256()
    for current, folder_names, file_names in os.walk(folder):
        folder_names[:] = sorted(name for name in folder_names if name != "__pycache__")
        for file_name in sorted(file_names):
            path = os.path.join(current, file_name)
            digest.update(os.path.relpath(path, folder).replace(os.sep, "/").encode())
            with open(path, "rb") as content:  # Windows line endings read as Unix ones, so every machine agrees
                digest.update(content.read().replace(b"\r\n", b"\n"))
    return digest.hexdigest()[:12]


def check_kept_cases(repository_root, notes):
    runs_path = os.path.join(repository_root, "kept-cases", "runs.md")
    if not os.path.exists(runs_path):
        notes.append("not checked: kept cases (no kept-cases/runs.md)")
        return
    recorded = re.findall(r"<!-- skill fingerprints: (.*?) -->", read_text(runs_path))
    if not recorded:
        notes.append("kept cases: no run recorded yet")
        return
    last_run = dict(pair.split("=") for pair in recorded[-1].split())
    skills_folder = os.path.join(repository_root, ".claude", "skills")
    changed = [skill for skill, fingerprint in sorted(last_run.items())
               if os.path.isdir(os.path.join(skills_folder, skill))
               and folder_fingerprint(os.path.join(skills_folder, skill)) != fingerprint]
    if changed:
        notes.append("kept cases not rerun since these skills changed: " + ", ".join(changed)
                     + " (a log entry about the change should say so)")


def fingerprints_line(repository_root, named):
    """(the runs.md line, problems). named: the skills a change that alters no meaning touched, or [] for all."""
    skills_folder = os.path.join(repository_root, ".claude", "skills")
    current = {skill: folder_fingerprint(os.path.join(skills_folder, skill))
               for skill in sorted(os.listdir(skills_folder)) if skill not in ("add-source", "error-correction")
               and os.path.isdir(os.path.join(skills_folder, skill))}
    if not named:
        return current, []
    recorded = re.findall(r"<!-- skill fingerprints: (.*?) -->",
                          read_text(os.path.join(repository_root, "kept-cases", "runs.md")))
    last_run = dict(pair.split("=") for pair in recorded[-1].split()) if recorded else {}
    line, problems = dict(last_run), []
    for skill in named:
        if skill in ("add-source", "error-correction"):
            problems.append(f"{skill}: this skill has no kept cases, so it needs no fingerprint line")
            continue
        if skill not in current:
            problems.append(f"{skill}: no such skill")
            continue
        scratch = tempfile.mkdtemp(prefix="workshop-fingerprint-")
        archive = subprocess.run(["git", "-C", repository_root, "archive", "HEAD", f".claude/skills/{skill}"],
                                 capture_output=True, check=False)
        subprocess.run(["tar", "-x", "-C", scratch], input=archive.stdout, check=False)
        before = folder_fingerprint(os.path.join(scratch, ".claude", "skills", skill))
        shutil.rmtree(scratch, ignore_errors=True)
        if before != last_run.get(skill):
            problems.append(f"{skill}: in the last commit it already differed from its last kept-case run, so this"
                            " change cannot clear it. Either its cases were already owed a rerun (then write the"
                            " runs.md line without a fingerprint line: the skill stays listed until its cases are"
                            " rerun), or this change is already committed (ask for the line before committing)")
        else:
            line[skill] = current[skill]
    return line, problems


def main():
    arguments = sys.argv[1:]
    if arguments[:1] == ["--fingerprints"]:
        rest = arguments[1:]
        root = "."
        if "--root" in rest:
            root = rest[rest.index("--root") + 1]
            rest = rest[:rest.index("--root")] + rest[rest.index("--root") + 2:]
        line, problems = fingerprints_line(os.path.abspath(root), rest)
        for problem in problems:
            print(problem, file=sys.stderr)
        if problems:
            sys.exit(1)
        print("<!-- skill fingerprints: " + " ".join(f"{skill}={code}" for skill, code in sorted(line.items())) + " -->")
        return
    log_only = "--log-only" in arguments
    arguments = [argument for argument in arguments if argument != "--log-only"]
    against, git_root, commit = "HEAD", None, None
    also_against = []
    while arguments[:1] and arguments[0] in ("--against", "--also-against", "--git-root", "--commit"):
        if arguments[0] == "--against":
            against = arguments[1]
        elif arguments[0] == "--also-against":
            also_against.append(arguments[1])
        elif arguments[0] == "--commit":
            commit = arguments[1]
        else:
            git_root = os.path.abspath(arguments[1])
        arguments = arguments[2:]
    repository_root = os.path.abspath(arguments[0] if arguments else ".")
    git_root = git_root or repository_root
    problems, notes = [], []
    if log_only:
        if commit:
            current_text = committed_text(git_root, commit, PROJECT_STORY)
            parent = subprocess.run(["git", "-C", git_root, "rev-parse", "-q", "--verify", f"{commit}^"],
                                    capture_output=True, text=True, check=False).stdout.strip()
            earlier_text = committed_text(git_root, parent, PROJECT_STORY) if parent else None
            against = parent[:9] if parent else "its parent"
        else:
            current_path = os.path.join(repository_root, PROJECT_STORY)
            current_text = read_text(current_path) if os.path.exists(current_path) else None
            earlier_text = committed_text(git_root, against, PROJECT_STORY)
        if current_text is None and earlier_text is not None:
            problems.append(f"{PROJECT_STORY}: removed")
        elif current_text is not None and earlier_text is not None:
            problems += compare_logs(earlier_text, current_text, against)
        else:
            notes.append("not checked: no earlier version of the project story to compare with")
        for problem in problems:
            print(problem)
        for note in notes:
            print(f"note: {note}")
        print(f"TOTAL problems: {len(problems)}")
        sys.exit(1 if problems else 0)
    entries, story_text = check_log(repository_root, git_root, against, problems, notes, also_against)
    check_numbered_files(repository_root, entries, problems)
    check_readme(repository_root, problems)
    check_questions(repository_root, problems, notes)
    check_corrections(repository_root, story_text, problems, notes)
    check_kept_cases(repository_root, notes)
    for problem in problems:
        print(problem)
    for note in notes:
        print(f"note: {note}")
    print(f"TOTAL problems: {len(problems)}")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
