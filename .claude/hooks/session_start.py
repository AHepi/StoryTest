#!/usr/bin/env python3
"""Switch on the commit gate, and tell a new session where the workshop stands.

Claude Code runs this by itself when a session starts or resumes (see
.claude/settings.json), and adds what it prints to what the agent knows.

1. It switches on the commit gate for this copy of the repository
   (`git config core.hooksPath .githooks`), so that git runs the checks
   before every commit. This is a setting of this copy only. It says the
   gate is on only if the gate's files on disk (.githooks/) match the last
   commit's; otherwise it says which differ.
2. It looks again at the commits since the last one the gate approved
   (recheck_commits.py, which also finds that commit, walking back along
   the main line): one made with the gate skipped, a cherry-pick or rebase
   whose contents changed, or one made elsewhere.
3. It prints a few lines: the last log entry and the next step; files
   left uncommitted; corrections still open; owner questions still open;
   kept cases not rerun since their skill changed; how many commits since
   the last approved one, and the problems and notes the recheck found for
   them; planted tests retired so far; and any machine check failing now,
   compared with the last approved commit (with the lines printed under it,
   not its notes), or "could not run" if the checks themselves did not run.
   It does not run the planted-fault test, which takes minutes: a check
   changed without the gate can still stop the next commit there.
It changes nothing else in the repository. If it goes wrong it prints a
one-line notice instead.
"""
import glob
import os
import re
import shutil
import subprocess
import sys
import tempfile


def read_text(path):
    with open(path, encoding="utf-8") as text_file:
        return text_file.read()


def run(arguments, root):
    return subprocess.run(arguments, cwd=root, capture_output=True, text=True, check=False, timeout=40)


def top_level_file(root, prefix):
    for name in sorted(os.listdir(root)):
        if name.startswith(prefix) and name.endswith(".md"):
            return os.path.join(root, name)
    return None


def open_items(path, marker_pattern):
    if path is None:
        return []
    text = read_text(path)
    markers = list(re.finditer(marker_pattern, text, flags=re.M))
    found = []
    for index, marker in enumerate(markers):
        end = markers[index + 1].start() if index + 1 < len(markers) else len(text)
        block = text[marker.start():end]
        heading = re.search(r"\n## ", block)  # the next top-level heading ("### C2." is not one)
        block = block[: heading.start()] if heading else block
        status = re.search(r"Status:\**\s*([A-Za-z]+)", block)
        if status and status.group(1).lower() in ("open", "rechecking"):
            found.append(marker.group(1))
    return found


def last_approved_commit(root, recheck):
    """The last approved commit, found by the recheck's own rule (walking back along the main line), or None."""
    if not os.path.exists(recheck):
        return None
    found = run([sys.executable, recheck, "--root", root, "--last-approved"], root).stdout.strip()
    return found if re.fullmatch(r"[0-9a-f]{40}", found) else None


def lines_under_failures(output):
    """The detail lines printed under a failing check, without its notes (the gate's own reminders)."""
    shown, under_failure, in_note = [], False, False
    for line in output.splitlines():
        if not line.startswith(" "):
            under_failure = line.startswith(("FAILED", "COULD NOT RUN"))
            continue
        if line.startswith("          ") and not line.startswith("           "):
            in_note = line.strip().startswith(("note:", "not checked", "skipped on request"))
            if under_failure and not in_note:
                shown.append(line.strip())
        elif under_failure and not in_note:
            shown.append(line.strip())
    return shown


def retired_tests(root):
    """Every planted test named under '## Tests retired' in a committed review receipt."""
    names = []
    for path in sorted(glob.glob(os.path.join(root, ".claude", "reviews", "*.md"))):
        match = re.search(r"^## Tests retired\s*$(.*?)(?=^## |\Z)", read_text(path), flags=re.M | re.S)
        names += [line.strip().lstrip("-* ").strip() for line in (match.group(1) if match else "").splitlines()
                  if line.strip() and not line.strip().startswith("(")]
    return names


def main():
    root = run(["git", "rev-parse", "--show-toplevel"], os.getcwd()).stdout.strip() \
        or os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
    lines = ["Workshop status (printed by .claude/hooks/session_start.py):"]
    if os.path.isdir(os.path.join(root, ".githooks")):
        current = run(["git", "config", "core.hooksPath"], root).stdout.strip()
        if current != ".githooks":
            run(["git", "config", "core.hooksPath", ".githooks"], root)
        differ = [line.split()[-1] for line in
                  run(["git", "status", "--porcelain", "--", ".githooks"], root).stdout.splitlines() if line.strip()]
        if differ:
            lines.append("- Commit gate: switched on, BUT its files on disk differ from the last commit ("
                         + ", ".join(differ) + "); git runs the files on disk, so look at them before committing")
        else:
            lines.append("- Commit gate: on (git runs .githooks/pre-commit before every commit)")
    story = os.path.join(root, "StoryTest - project story.md")
    if os.path.exists(story):
        story_text = read_text(story)
        entries = re.findall(r"^(\d+)\. \*\*(.+?)\*\*", story_text, flags=re.M)
        if entries:
            lines.append(f"- Last log entry: {entries[-1][0]}. {entries[-1][1]}")
        next_step = re.search(r"^## Next step\s*\n+(.+?)(?:\n\n|\Z)", story_text, flags=re.M | re.S)
        if next_step:
            lines.append(f"- Next step: {' '.join(next_step.group(1).split())[:300]}")
    uncommitted = [line for line in run(["git", "status", "--porcelain"], root).stdout.splitlines() if line]
    if uncommitted:
        lines.append(f"- Left uncommitted from before: {len(uncommitted)} file(s); look at them before starting")
    corrections = open_items(top_level_file(root, "27 Corrections"), r"^### (C\d+)\.")
    if corrections:
        lines.append("- Open corrections (27 Corrections.md): " + ", ".join(corrections))
    questions = open_items(top_level_file(root, "22 Questions"), r"^(?:## |- \*\*)([QS]\d{1,2})\.")
    if questions:
        lines.append("- Owner questions still open: " + ", ".join(questions))
    scripts = os.path.join(root, ".claude", "skills", "error-correction", "scripts")
    recheck = os.path.join(scripts, "recheck_commits.py")
    if os.path.exists(recheck):
        try:
            result = run([sys.executable, recheck, "--root", root], root)
            found = [line for line in result.stdout.splitlines()
                     if line and not line.startswith(("TOTAL", "rechecked", "note:"))]
            flagged = [line[len("note: "):] for line in result.stdout.splitlines()
                       if line.startswith("note: commit") and "first commit in the history" not in line]
            counted = next((line for line in result.stdout.splitlines() if line.startswith("rechecked")), "")
            if result.returncode not in (0, 1):
                lines.append("- Recheck of earlier commits: could not run (" + " ".join(result.stderr.split())[-200:] + ")")
            elif "the commit gate is not in this history yet" not in result.stdout:
                if counted and not counted.startswith("rechecked 0 "):
                    lines.append(f"- Commits the gate did not approve: {counted}")
                if found:
                    lines.append(f"- Problems in those commits ({len(found)}); put them right with a new commit"
                                 " (error-correction skill, references/checks-and-cases.md, section 2):")
                    lines += [f"    {line}" for line in found[:8]]
                if flagged:
                    lines.append("- For a person to look at:")
                    lines += [f"    {line}" for line in flagged[:8]]
        except subprocess.TimeoutExpired:
            lines.append("- Recheck of earlier commits: could not run (it took too long)")
    checks = os.path.join(scripts, "run_all_checks.py")
    if os.path.exists(checks):
        try:
            approved = last_approved_commit(root, recheck)
            if approved:  # the checks the gate will use: the last approved commit's, not the ones on disk
                scripts_home = tempfile.mkdtemp(prefix="workshop-session-")
                archive = subprocess.run(["git", "-C", root, "archive", approved, ".claude/skills/error-correction/scripts",
                                          ".claude/skills/add-source/scripts"], capture_output=True, check=False)
                subprocess.run(["tar", "-x", "-C", scripts_home], input=archive.stdout, check=False)
                approved_checks = os.path.join(scripts_home, ".claude", "skills", "error-correction", "scripts",
                                               "run_all_checks.py")
                if os.path.exists(approved_checks):
                    checks = approved_checks
            result = run([sys.executable, checks, "--skip-books", *(["--against", approved] if approved else []),
                          root], root)
            if approved:
                shutil.rmtree(scripts_home, ignore_errors=True)
            failing = [re.sub(r"^(FAILED|COULD NOT RUN)\s+", "", line) + (" (could not run)" if line.startswith("COULD") else "")
                       for line in result.stdout.splitlines() if line.startswith(("FAILED", "COULD NOT RUN"))]
            stale = [line.strip()[len("note: "):] for line in result.stdout.splitlines()
                     if "kept cases not rerun" in line]
            if stale:
                lines.append("- " + stale[0])
            if failing:
                shown = lines_under_failures(result.stdout)
                lines.append("- Machine checks (those of the last approved commit, compared with it): FAILING: "
                             + ", ".join(failing) + (f" (compared with {approved[:9]})" if approved else ""))
                lines += [f"    {line[:200]}" for line in shown[:6]]
            elif result.returncode != 0 or "RESULT:" not in result.stdout:
                lines.append("- Machine checks: could not run (" + " ".join(result.stderr.split())[-200:] + ")")
            else:
                lines.append("- Machine checks: none failing")
        except subprocess.TimeoutExpired:
            lines.append("- Machine checks: could not run (they took too long)")
    retired = retired_tests(root)
    if retired:
        lines.append(f"- Planted tests retired so far ({len(retired)}): " + "; ".join(retired[:6]))
    lines.append("Read CLAUDE.md and the project story first. Anything that may be wrong goes through the"
                 " error-correction skill.")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as problem:
        print(f"session_start hook could not run ({problem})")
        sys.exit(0)
