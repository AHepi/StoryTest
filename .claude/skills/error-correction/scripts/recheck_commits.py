#!/usr/bin/env python3
"""Look again at the commits the commit gate has not approved, for what only the history can show.

When the gate passes a commit, it stamps the commit's message with a line
"Workshop-gate: approved <tree>", naming the exact contents it approved
(.githooks/prepare-commit-msg adds it). A merge made without the gate that
is exactly git's automatic merge of two approved parents (as GitHub's merge
button makes when there is no conflict) counts as approved too, as the gate
counts it (check_commit.py's note says when a parent from before the gate
counts, and why a merge of two lines that both changed the checks does
not). Before it approves a
commit, the gate has looked at everything before it, so every commit an
approved commit reaches back to is settled, and is never looked at again.
The commits left are the ones made since, without the gate: with the gate
skipped or switched off, a rebase or cherry-pick whose contents changed, a
merge made on GitHub with a conflict resolved by hand, a commit made on
GitHub or on a machine without the gate. The last approved commit is found
the way the gate finds it: walking back along the main line (each commit's
first parent), the first approved one.

What those commits got wrong in the files (a frozen theory edited, an old
log entry rewritten, a receipt deleted) is not judged here: the gate judges
it at the next commit, by comparing the staged files with the last approved
commit and running that commit's checks, so it stops every commit until a
commit puts it right, and clears when one does. A check they loosened is
the exception: the gate judges it only by the last approved commit's
planted-fault test, and it rests on its own late review
(references/checks-and-cases.md, section 2).
What only the history can show is looked at here, for each commit since
the last approved one:
1. its review receipt, if it changed a reviewed file (review_receipt.py
   check --commit, taken from the last approved commit). A rebase that
   leaves the change itself as it was keeps its fingerprint, so it finds
   the receipt it already has. For a merge, only its own changes.
2. A receipt whose verdict says the review did not pass and the change was
   withdrawn is believed only if the files show it: every line the commit
   added is gone again, every line it removed is back, and the commit's own
   change can no longer be undone from the files (so a change that only
   reordered lines is not taken as withdrawn while the new order stands).
3. A book file it added (under sources/raw/, an ebook or PDF, or a text
   file over 100,000 bytes, apart from the one large record the no-book-files
   check allows by name while its contents are unchanged) is reported as a
   note, even if a later commit
   removed it: it stays in the history, and only rewriting the history takes
   it out, which is the owner's decision.
4. A change it made to the gate's own files is reported as a note, for a
   person to look at: the gate cannot judge a change to itself. It still
   needs its review receipt (item 1).
Notes (items 3 and 4) are shown at session start and in the gate's output
only until a commit through the gate is approved. After a pull, a rebase, a
cherry-pick or a merge made mid-session, run this script before the next
commit, so a note is seen before that commit; the agent copies each note
into the log entry of the commit it is about to make (or, if a note is
first seen in the output of a commit already passed, into the next entry)
and tells the owner.
Nothing else is a stop, so everything this reports can be put right with a
new commit: a receipt written late, or a withdrawal made for real.

What it cannot do: a commit made outside the gate that changes this
script, or the hook that runs it, is run in its changed form at session
start, whether or not the change was meant to loosen anything; the gate
itself takes this script from the last approved commit. A stamp typed by
hand would be a false statement in the history, which only a person would
see. Only a check run outside the repository (owner question S10) or the
owner can catch those. It does not rerun the maps, owner-quotes and copying
checks on each commit: the gate runs them at the next commit on the files
as they then are, so a copied passage added and removed between two
commits through the gate is not seen.

It stops after about a minute and a half and says how many commits it did
not reach: not checked is never passed.

Exit code 1 if there is any problem, 0 if there is none.

Usage: recheck_commits.py [--root PATH] [--also COMMIT] [--last-approved]
  --also: also look at the commits that COMMIT brings in and the last
          commit does not have (the gate passes the commit being merged)
  --last-approved: print only the last approved commit (or "none"), for
          session start
"""
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile
import time

SCRIPTS = ".claude/skills/error-correction/scripts"
GATE_SCRIPT = f"{SCRIPTS}/check_commit.py"
CHECK_PATHS = (".claude/skills/error-correction/scripts", ".claude/skills/add-source/scripts", ".claude/hooks", ".githooks",
               ".claude/settings.json", ".gitattributes")  # the files a check change touches
GATE_OWN_FILES = (".githooks/", ".claude/hooks/", f"{SCRIPTS}/check_commit.py", f"{SCRIPTS}/recheck_commits.py",
                  ".claude/settings.json")
BOOK_ENDINGS = (".epub", ".azw3", ".azw", ".mobi", ".pdf", ".kfx")
TEXT_ENDINGS = (".md", ".txt", ".json", ".py", ".js", ".sh", ".html", ".csv", ".yaml", ".yml", ".xml", ".tex", ".rst")
LARGE_TEXT = 100_000  # bytes, the same limit the no-book-files check uses
STAMP_KEY = "Workshop-gate"
TIME_LIMIT = 90  # seconds
CLEAN_ENVIRONMENT = {name: value for name, value in os.environ.items() if not name.startswith("GIT_")}
if os.environ.get("GIT_INDEX_FILE"):  # git's staging area for this commit, which `git commit -a` makes for itself
    CLEAN_ENVIRONMENT["GIT_INDEX_FILE"] = os.path.abspath(os.environ["GIT_INDEX_FILE"])
try:  # the one large record the no-book-files check allows by name, from the same folder
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from run_all_checks import LARGE_RECORDS_ALLOWED
except Exception:
    LARGE_RECORDS_ALLOWED = {}


def git(root, *arguments, input_text=None):
    result = subprocess.run(["git", "-C", root, "-c", "core.quotePath=false", *arguments], capture_output=True,
                            text=True, check=False, env=CLEAN_ENVIRONMENT, input=input_text)
    return result.returncode, result.stdout.strip()


class Approval:
    """Which commits count as approved (the note at the top of this file says how); the same rule as in
    check_commit.py."""

    def __init__(self, root, starts=("HEAD",)):
        self.root = root
        self.stamped = set()
        _, listing = git(root, "log", f"--format=%H %T%x1f%(trailers:key={STAMP_KEY},valueonly,separator=%x1f)%x1e",
                         *starts)
        for record in listing.split("\x1e"):
            head, _, stamps = record.strip().partition("\x1f")
            if head:
                commit, tree = head.split()
                if f"approved {tree}" in [stamp.strip() for stamp in stamps.split("\x1f")]:
                    self.stamped.add(commit)
        self.gate_added = git(root, "log", "--diff-filter=A", "--format=%H", *starts, "--", GATE_SCRIPT)[1].split()
        self.judged = {}

    def before_the_gate(self, commit):
        return not any(git(self.root, "merge-base", "--is-ancestor", added, commit)[0] == 0
                       for added in self.gate_added)

    def approved(self, commit):
        if commit not in self.judged:
            self.judged[commit] = False  # while it is being judged
            self.judged[commit] = commit in self.stamped or self.automatic_merge_of_approved(commit)
        return self.judged[commit]

    def automatic_merge_of_approved(self, commit):
        parents = git(self.root, "rev-list", "--parents", "-n", "1", commit)[1].split()[1:]
        if len(parents) != 2 or self.before_the_gate(commit):
            return False
        code, merged = git(self.root, "merge-tree", "--write-tree", *parents)
        own_tree = git(self.root, "rev-parse", f"{commit}^{{tree}}")[1]
        if code != 0 or merged.split("\n", 1)[0].strip() != own_tree:
            return False
        approved = [parent for parent in parents if self.approved(parent)]
        for parent in parents:  # a parent from before the gate counts only if an approved parent already holds it
            if parent not in approved and not (self.before_the_gate(parent) and any(
                    git(self.root, "merge-base", "--is-ancestor", parent, other)[0] == 0 for other in approved)):
                return False
        if len(approved) == 2 and all(git(self.root, "diff", "--quiet", parent, commit, "--", *CHECK_PATHS)[0]
                                      for parent in parents):
            return False  # both lines changed the checks: nobody tested them together
        return bool(approved)

    def last_approved_commit(self, start="HEAD"):
        """Walking back along the main line from start, the first approved commit; None if the walk reaches the
        commits from before the gate, or the start of the history, first."""
        main_line = git(self.root, "rev-list", "--first-parent", start)[1].split()
        end = next((index for index, commit in enumerate(main_line)
                    if commit in self.stamped or self.before_the_gate(commit)), len(main_line))
        for commit in reversed(main_line[:end]):  # oldest first, so that each merge finds its first parent judged
            self.approved(commit)
        for commit in main_line[:end + 1]:
            if self.approved(commit):
                return commit
        return None


def first_gate_commit(root):
    _, added = git(root, "log", "--diff-filter=A", "--format=%H", "--", GATE_SCRIPT)
    return added.splitlines()[-1] if added else None


def run(arguments, root, timeout=120):
    try:
        result = subprocess.run([sys.executable, *arguments], cwd=root, capture_output=True, text=True,
                                check=False, timeout=timeout, env=CLEAN_ENVIRONMENT)
    except subprocess.TimeoutExpired:
        return 2, "could not run: it took too long"
    code = result.returncode if result.returncode in (0, 1) else 2
    return code, (result.stdout + result.stderr).strip()


def problem_lines(output):
    return [line for line in output.splitlines()
            if line and not line.startswith(("TOTAL", "note:", "review receipt:", "    ", "not checked"))]


def changed(root, commit, parent):
    """[(kind, path)] of the commit against its first parent."""
    _, status = git(root, "diff", "--no-renames", "--name-status", "-z", parent, commit)
    fields = [field for field in status.split("\0") if field]
    return list(zip(fields[0::2], fields[1::2]))


def lines_of(root, spec):
    code, text = git(root, "show", spec)
    return set(text.splitlines()) if code == 0 else set()


def still_holding_the_change(root, commit, parent, changes):
    """The files in which a change said to be withdrawn is still there, now (in the staged files)."""
    still = []
    for _, path in changes:
        if path.startswith(".claude/reviews/"):
            continue
        before, after, now = lines_of(root, f"{parent}:{path}"), lines_of(root, f"{commit}:{path}"), \
            lines_of(root, f":{path}")
        added = {line for line in after - before if line.strip()}
        removed = {line for line in before - after if line.strip()}
        if (added & now) or (removed - now):
            still.append(path)
    return still


def change_still_applies(root, commit, parent, changes):
    """True if the commit's own change could still be undone from the staged files, which means it is still there."""
    paths = [path for _, path in changes if not path.startswith(".claude/reviews/")]
    if not paths:
        return False
    patch = subprocess.run(["git", "-C", root, "diff", "--binary", "--no-renames", parent, commit, "--", *paths],
                           capture_output=True, check=False, env=CLEAN_ENVIRONMENT).stdout
    result = subprocess.run(["git", "-C", root, "apply", "--check", "--reverse", "--cached", "-"], input=patch,
                            capture_output=True, check=False, env=CLEAN_ENVIRONMENT)
    return result.returncode == 0


def allowed_large_record(root, commit, path):
    """True only for the one large record the no-book-files check allows by name, with its contents unchanged."""
    if path not in LARGE_RECORDS_ALLOWED:
        return False
    contents = subprocess.run(["git", "-C", root, "show", f"{commit}:{path}"], capture_output=True, check=False,
                              env=CLEAN_ENVIRONMENT).stdout.replace(b"\r\n", b"\n")
    return hashlib.sha256(contents).hexdigest() == LARGE_RECORDS_ALLOWED[path]


def looks_like_a_book(root, commit, path):
    name = path.lower()
    if path.startswith("sources/raw/") or name.endswith(BOOK_ENDINGS):
        return True
    if name.endswith(TEXT_ENDINGS):
        code, size = git(root, "cat-file", "-s", f"{commit}:{path}")
        return (code == 0 and size.isdigit() and int(size) > LARGE_TEXT
                and not allowed_large_record(root, commit, path))
    return False


def recheck_one(root, commit, parents, scripts, problems, notes):
    short = commit[:9]
    code, output = run([os.path.join(scripts, "review_receipt.py"), "check", "--commit", commit, "--root", root],
                       root)
    if code:
        problems += [f"commit {short}: {line}" for line in problem_lines(output)] or \
                    [f"commit {short}: the review receipt check could not run"]
    withdrawn = "did not pass; the change was withdrawn" in output
    if len(parents) > 1:
        return  # the commits a merge brings in are looked at in their own right
    changes = changed(root, commit, parents[0])
    if withdrawn:
        still = still_holding_the_change(root, commit, parents[0], changes)
        if not still and change_still_applies(root, commit, parents[0], changes):
            still = [path for _, path in changes if not path.startswith(".claude/reviews/")]
        if still:
            problems.append(f"commit {short}: its receipt says the change was withdrawn, but it is still in"
                            f" {', '.join(still)}; take it out (git revert --no-commit {short}, then commit through"
                            " the gate), or get a review that passes")
    for kind, path in changes:
        if kind in ("A", "M") and looks_like_a_book(root, commit, path):
            notes.append(f"commit {short} added {path}, which looks like a book file; if it is one, it stays in the"
                         " history even after it is removed, and only rewriting the history takes it out: tell the"
                         " owner")
    gate_own = [path for _, path in changes if path.startswith(GATE_OWN_FILES)]
    if gate_own:
        notes.append(f"commit {short} changed the gate's own files without the gate ({', '.join(gate_own)}); a"
                     " person should look at it, because the gate cannot judge a change to itself")


def main():
    arguments = sys.argv[1:]
    only_the_last_approved = "--last-approved" in arguments
    arguments = [argument for argument in arguments if argument != "--last-approved"]
    root = also = None
    while arguments[:1] and arguments[0] in ("--root", "--also"):
        if arguments[0] == "--root":
            root = os.path.abspath(arguments[1])
        else:
            also = arguments[1]
        arguments = arguments[2:]
    if root is None:
        root = git(os.getcwd(), "rev-parse", "--show-toplevel")[1] or os.getcwd()

    if only_the_last_approved:
        found = Approval(root).last_approved_commit() if git(root, "rev-parse", "-q", "--verify", "HEAD")[0] == 0 \
            else None
        print(found or "none")
        return 0
    if git(root, "rev-parse", "-q", "--verify", "HEAD")[0] != 0:
        print("not checked: there are no commits yet")
        print("TOTAL problems: 0")
        return 0
    gate_commit = first_gate_commit(root)
    if gate_commit is None:
        print("not checked: the commit gate is not in this history yet")
        print("TOTAL problems: 0")
        return 0

    starts = ["HEAD"] + ([also] if also else [])
    approval = Approval(root, starts)
    base = approval.last_approved_commit()
    code, before_the_gate = git(root, "rev-parse", "-q", "--verify", f"{gate_commit}^")
    excluded = sorted(approval.stamped) + ([before_the_gate] if code == 0 else [])
    _, listed = git(root, "rev-list", "--reverse", "--parents", "--stdin",
                    input_text="\n".join(starts + [f"^{commit}" for commit in excluded]) + "\n")
    rows = [line.split() for line in listed.splitlines() if line]
    rows = [row for row in rows if not (len(row) == 3 and approval.approved(row[0]))]  # automatic merges

    scripts_from = base or gate_commit
    scripts_home = tempfile.mkdtemp(prefix="workshop-recheck-")
    problems, notes = [], []
    began, reached = time.time(), 0
    try:
        archive = subprocess.run(["git", "-C", root, "archive", scripts_from, SCRIPTS], capture_output=True,
                                 check=False, env=CLEAN_ENVIRONMENT)
        subprocess.run(["tar", "-x", "-C", scripts_home], input=archive.stdout, check=False)
        scripts = os.path.join(scripts_home, SCRIPTS)
        if not os.path.exists(os.path.join(scripts, "review_receipt.py")):
            print(f"could not run: no review_receipt.py in {scripts_from[:9]}")
            print("TOTAL problems: 1")
            return 1
        for row in rows:
            if time.time() - began > TIME_LIMIT:
                break
            reached += 1
            if len(row) == 1:
                notes.append(f"commit {row[0][:9]} is the first commit in the history: there is nothing to compare"
                             " it with")
                continue
            recheck_one(root, row[0], row[1:], scripts, problems, notes)
    finally:
        shutil.rmtree(scripts_home, ignore_errors=True)

    for problem in problems:
        print(problem)
    for note in notes:
        print(f"note: {note}")
    if reached < len(rows):
        print(f"not checked: {len(rows) - reached} later commit(s); the recheck ran out of time")
    since = f"since the last approved commit, {base[:9]}" if base else "since the gate came in (no commit is approved)"
    print(f"rechecked {reached} commit(s) the gate did not approve, {since}")
    print(f"TOTAL problems: {len(problems)}")
    return 1 if problems or reached < len(rows) else 0


if __name__ == "__main__":
    sys.exit(main())
