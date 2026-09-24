#!/usr/bin/env python3
"""The commit gate: check exactly what is about to be committed.

Git runs this by itself before every `git commit`, and before a merge that
makes a merge commit, through .githooks/pre-commit and
.githooks/pre-merge-commit (switched on for a copy of the repository by
`git config core.hooksPath .githooks`; the session-start hook does that).

When the gate passes a commit, the commit's message is stamped with the
exact contents it approved ("Workshop-gate: approved <tree>";
.githooks/prepare-commit-msg adds it). The last approved commit is found by
walking back along the main line (from the last commit to its first
parent, and so on): the first commit that is approved. A commit is
approved if its stamp matches its own contents, or if it is a merge made
without the gate that is exactly git's automatic merge of its two parents
(GitHub's merge button makes such a merge when there is no conflict), when
one parent is approved and the other is approved too or from before the
gate and already inside the approved one's history, and not both of them
changed the checks (nobody tested those together). Without
`git merge-tree --write-tree` (git older than 2.38) no such merge counts,
and a merge in progress is judged against its first parent. Normally it is simply
the last commit. A merge made on GitHub with a conflict resolved by hand is
not approved, so the walk goes on to its first parent: the main line's
entries and checks are what count, as in a merge made through the gate.

The checks come from the last approved commit, never from the files being
changed, and the files are compared with it: a check cannot be loosened in
the same commit as the work it would stop, and a changed check takes
effect only once a commit carrying it has been approved. If commits were
made since then without the gate (with the gate skipped or switched off, a
rebase, a commit made on GitHub), whatever they got wrong in the files is
judged now, against the last approved commit: it stops this commit until a
commit puts it right, and a commit that puts it right clears it. A check
they loosened is the exception: it is judged only by the planted-fault
test and its own late review (references/checks-and-cases.md, section 2).
In a merge, the log entries the other side added since the two lines of
work split are kept too, by number and text. Two exceptions, each said
aloud when it applies:
- the commit that first brings the gate in has no earlier version, so it
  is checked by the checks it brings;
- a commit that changes only checks, with nothing else but new review
  receipts, made straight on top of an approved commit, is checked by its
  own changed machine checks (run_all_checks.py and the checks it runs), so
  a wrong one of those can be corrected even when it stops every commit;
  its review receipt is still checked by the last approved commit's receipt
  check, and that commit's planted-fault test must still pass on the
  changed checks. The log entry for it follows in the next commit. This
  does not reach the receipt check, the recheck, the planted-fault test or
  the gate script itself (this file, which always comes from the last
  commit): see references/checks-and-cases.md, section 2, for what to do
  when one of those is wrong.

What it does:
1. Copies the staged files, and only those, to a scratch folder, and runs
   every machine check on that copy (run_all_checks.py), comparing records
   with the last approved commit and reading the frozen files from git's
   staging area for this commit (the one `git commit -a` or
   `git commit <file>` makes for itself, when it does).
2. Checks that the change carries a complete review receipt
   (review_receipt.py); for a merge, that the merge's own changes do.
3. Looks again at the commits since the last approved one, for what only
   the history can show (recheck_commits.py): their review receipts, a
   withdrawal a receipt claims, book files, and changes to the gate's own
   files; for a merge, also the commits it brings in.
4. Refuses a change to, or the deletion of, a review receipt that the last
   approved commit has: receipts are only ever added to.
5. If this commit's own change touches a check, a hook, the allowed-titles
   list or the settings, refuses it if it also changes other work. Whenever
   the staged checks differ from the last approved commit's, runs that
   commit's planted-fault test on them (every fault its checks caught must
   still be caught, unless the receipt retires the test by name under
   "Tests retired", with why), and the changed test too.
If everything passes, it notes the approved contents in .git for the stamp.
If anything fails, the commit is stopped and the reason printed, including
any script that could not run. Either way it writes "passed" or "stopped"
to the file .githooks/pre-commit names in WORKSHOP_GATE_RESULT, so that
pre-commit can tell a stop from a crash of this script.

What it cannot do: git runs .githooks/pre-commit from the disk, and this
script comes from the last commit, whether or not the gate approved it.
So an agent who edits them can switch the gate off, and a commit made
outside the gate that changes them is run in its changed form, whether or
not the change was meant to loosen anything. The recheck reports such a
change for a person to look at. Only a check run outside the repository
(owner question S10) or the owner can catch everything.

A failing check is a sign that something may be wrong: see the
error-correction skill, references/checks-and-cases.md, section 2. If the
check itself is wrong, correct the check, with its planted-fault test, in
its own commit. Never get round it.

Usage (git runs it): check_commit.py [--checks-from HEAD|staged]
  (--checks-from staged is obeyed only when the last commit has no gate)
"""
import os
import re
import shutil
import signal
import subprocess
import sys
import tempfile

SCRIPTS = ".claude/skills/error-correction/scripts"
ADD_SOURCE_SCRIPTS = ".claude/skills/add-source/scripts"
CHECK_PREFIXES = (SCRIPTS + "/", ADD_SOURCE_SCRIPTS + "/", ".claude/hooks/", ".githooks/")
CHECK_FILES = (".claude/settings.json", ".gitattributes")
ALLOWED_WITH_A_CHECK_CHANGE = ("StoryTest - project story.md", "sources/README.md")
ALLOWED_PREFIXES_WITH_A_CHECK_CHANGE = (".claude/reviews/", "27 Corrections")
UNPROTECTED_TESTS = ("maps", "owner quotes")  # every other planted test guards the gate, the log, the
# frozen files, the receipts, the books or the hooks, and is retired only with the owner as reviewer
STAMP_KEY = "Workshop-gate"
INSIDE_THE_TEST = "WORKSHOP_INSIDE_PLANTED_FAULT_TEST"
TEST_COPY_PREFIX = "workshop-test-"  # the name test_checks.py gives its copies
RECEIPT_NAME = re.compile(r"^\.claude/reviews/[0-9a-f]{16}\.md$")
GATE_SCRIPT = f"{SCRIPTS}/check_commit.py"
CHECK_PATHS = (".claude/skills/error-correction/scripts", ".claude/skills/add-source/scripts", ".claude/hooks", ".githooks",
               ".claude/settings.json", ".gitattributes")  # the files a check change touches
RESULT_FILE = "WORKSHOP_GATE_RESULT"  # where pre-commit asks for "passed" or "stopped"
CRASHED = re.compile(r"^(Traceback \(most recent call last\)|\w*(Error|Exception)\b)", re.M)  # Python's own report of a broken script


def git(root, *arguments):
    return subprocess.run(["git", "-C", root, "-c", "core.quotePath=false", *arguments],
                          capture_output=True, text=True, check=False)


def environment_for_copies():
    """The settings for scripts that make their own throwaway repositories: without any that git set for this
    commit (every name beginning GIT_, such as GIT_INDEX_FILE, or GIT_REFLOG_ACTION during a merge), which would
    otherwise reach into the copies' own commits and merges."""
    return {name: value for name, value in os.environ.items() if not name.startswith("GIT_")}


def environment_for_this_repository():
    """The settings for scripts that read this repository: as for copies, but keeping git's staging area for this
    commit (GIT_INDEX_FILE, as a full path), which `git commit -a` and `git commit <file>` make for themselves."""
    environment = environment_for_copies()
    if os.environ.get("GIT_INDEX_FILE"):
        environment["GIT_INDEX_FILE"] = os.path.abspath(os.environ["GIT_INDEX_FILE"])
    return environment


def inside_the_planted_fault_test(root):
    """True only in one of the planted-fault test's own copies, with its setting on.

    test_checks.py sets WORKSHOP_INSIDE_PLANTED_FAULT_TEST so that a commit
    made in one of its copies does not start the whole test again. The
    setting alone is not enough: set by hand, or left over in a shell, it
    would skip the planted-fault test on a real commit. So it counts only in
    a folder named workshop-test-... directly inside the system's temporary
    folder, which is where test_checks.py makes its copies.
    """
    if not os.environ.get(INSIDE_THE_TEST):
        return False
    folder = os.path.realpath(root)
    return (os.path.basename(folder).startswith(TEST_COPY_PREFIX)
            and os.path.dirname(folder) == os.path.realpath(tempfile.gettempdir()))


class Approval:
    """Which commits count as approved (the note at the top of this file says how); the same rule as in
    recheck_commits.py, which session start asks."""

    def __init__(self, root, starts=("HEAD",)):
        self.root = root
        self.stamped = set()
        listing = git(root, "log", f"--format=%H %T%x1f%(trailers:key={STAMP_KEY},valueonly,separator=%x1f)%x1e",
                      *starts).stdout
        for record in listing.split("\x1e"):
            head, _, stamps = record.strip().partition("\x1f")
            if head:
                commit, tree = head.split()
                if f"approved {tree}" in [stamp.strip() for stamp in stamps.split("\x1f")]:
                    self.stamped.add(commit)
        self.gate_added = git(root, "log", "--diff-filter=A", "--format=%H", *starts, "--", GATE_SCRIPT).stdout.split()
        self.judged = {}

    def before_the_gate(self, commit):
        return not any(git(self.root, "merge-base", "--is-ancestor", added, commit).returncode == 0
                       for added in self.gate_added)

    def approved(self, commit):
        if commit not in self.judged:
            self.judged[commit] = False  # while it is being judged
            self.judged[commit] = commit in self.stamped or self.automatic_merge_of_approved(commit)
        return self.judged[commit]

    def automatic_merge_of_approved(self, commit):
        parents = git(self.root, "rev-list", "--parents", "-n", "1", commit).stdout.split()[1:]
        if len(parents) != 2 or self.before_the_gate(commit):
            return False
        merged = git(self.root, "merge-tree", "--write-tree", *parents)
        own_tree = git(self.root, "rev-parse", f"{commit}^{{tree}}").stdout.strip()
        if merged.returncode != 0 or merged.stdout.split("\n", 1)[0].strip() != own_tree:
            return False
        approved = [parent for parent in parents if self.approved(parent)]
        for parent in parents:  # a parent from before the gate counts only if an approved parent already holds it
            if parent not in approved and not (self.before_the_gate(parent) and any(
                    git(self.root, "merge-base", "--is-ancestor", parent, other).returncode == 0 for other in approved)):
                return False
        if len(approved) == 2 and all(git(self.root, "diff", "--quiet", parent, commit, "--", *CHECK_PATHS).returncode
                                      for parent in parents):
            return False  # both lines changed the checks: nobody tested them together
        return bool(approved)

    def last_approved_commit(self, start="HEAD"):
        """Walking back along the main line from start, the first approved commit; None if the walk reaches the
        commits from before the gate, or the start of the history, first."""
        main_line = git(self.root, "rev-list", "--first-parent", start).stdout.split()
        end = next((index for index, commit in enumerate(main_line)
                    if commit in self.stamped or self.before_the_gate(commit)), len(main_line))
        for commit in reversed(main_line[:end]):  # oldest first, so that each merge finds its first parent judged
            self.approved(commit)
        for commit in main_line[:end + 1]:
            if self.approved(commit):
                return commit
        return None

    def not_approved_since(self, approved_commit, start="HEAD"):
        since = git(self.root, "rev-list", start, f"^{approved_commit}").stdout.split()
        return [commit for commit in since if not self.approved(commit)]


def is_check_file(path):
    return path.startswith(CHECK_PREFIXES) or path in CHECK_FILES


def run_script(label, arguments, environment=None, timeout=900):
    """Run a script; return (exit code, printed output, and a line naming it if it could not run)."""
    try:
        process = subprocess.Popen([sys.executable, *arguments], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   text=True, env=environment, start_new_session=True)
    except OSError as problem:
        return 2, "", f"COULD NOT RUN  {label}: {problem}"
    try:
        output, errors = process.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        os.killpg(process.pid, signal.SIGKILL)  # stop the script and everything it started
        process.communicate()
        return 2, "", f"COULD NOT RUN  {label}: it took longer than {timeout} seconds and was stopped"
    trouble = ""
    if process.returncode not in (0, 1) or CRASHED.search(errors):
        last_lines = " | ".join(errors.strip().splitlines()[-3:])
        trouble = f"COULD NOT RUN  {label} (exit {process.returncode}): {last_lines}"
    return process.returncode, output, trouble


def indented(text):
    return "".join(f"          {line}\n" for line in text.splitlines() if line.strip())


def staged_changes(root, base):
    """[(kind, path)] of what is staged against base (a commit or a tree), with moves shown as delete and add."""
    fields = [field for field in git(root, "diff", "--cached", "--no-renames", "--name-status", "-z", base)
              .stdout.split("\0") if field]
    return list(zip(fields[0::2], fields[1::2]))


def automatic_merge(root, first, second):
    """The tree git would make by merging the two with no hand changes; if this git cannot say (older than 2.38),
    the first commit, so that the whole change is judged rather than none of it."""
    result = git(root, "merge-tree", "--write-tree", first, second)
    tree = result.stdout.split("\n", 1)[0].strip()
    return tree if result.returncode in (0, 1) and tree else first


def commits_being_merged(root):
    """The commits a merge in progress brings in: MERGE_HEAD once git has written it (a merge finished with git
    commit); or, while git runs the pre-merge-commit hook, the names git passes in GIT_REFLOG_ACTION ("merge side");
    or, for a pull, what git fetched for merging (FETCH_HEAD, the lines not marked not-for-merge)."""
    merge_head = git(root, "rev-parse", "-q", "--verify", "MERGE_HEAD").stdout.strip()
    if merge_head:
        return [merge_head]
    action = os.environ.get("GIT_REFLOG_ACTION", "")
    if action.startswith("pull"):
        fetch_head = git(root, "rev-parse", "--git-path", "FETCH_HEAD").stdout.strip()
        fetch_head = fetch_head if os.path.isabs(fetch_head) else os.path.join(root, fetch_head)
        try:
            with open(fetch_head, encoding="utf-8") as fetched:
                return [line.split()[0] for line in fetched if line.strip() and "not-for-merge" not in line]
        except OSError:
            return []
    if not action.startswith("merge "):
        return []
    found = [git(root, "rev-parse", "-q", "--verify", f"{name}^{{commit}}").stdout.strip() for name in action.split()[1:]]
    return [commit for commit in found if commit]


def main():
    requested = "HEAD"
    if "--checks-from" in sys.argv:
        requested = sys.argv[sys.argv.index("--checks-from") + 1]
    root = git(os.getcwd(), "rev-parse", "--show-toplevel").stdout.strip() or os.getcwd()
    has_head = git(root, "rev-parse", "-q", "--verify", "HEAD").returncode == 0
    head_has_the_gate = has_head and git(root, "cat-file", "-e", f"HEAD:{SCRIPTS}/check_commit.py").returncode == 0
    head_commit = git(root, "rev-parse", "HEAD").stdout.strip() if has_head else ""
    merging = commits_being_merged(root)
    merge_head = merging[0] if merging else ""
    base = automatic_merge(root, "HEAD", merge_head) if (merge_head and head_has_the_gate) else "HEAD"
    changes = staged_changes(root, base) if has_head else []
    names = [path for _, path in changes]
    changed_checks = [name for name in names if is_check_file(name)]
    added_receipts = [path for kind, path in changes if kind == "A" and RECEIPT_NAME.match(path)]
    others = [name for name in names if not is_check_file(name) and name not in ALLOWED_WITH_A_CHECK_CHANGE
              and not name.startswith(ALLOWED_PREFIXES_WITH_A_CHECK_CHANGE)]

    approval = Approval(root) if head_has_the_gate else None
    approved_commit = approval.last_approved_commit() if approval else None
    judged_against = approved_commit or head_commit  # the commit the checks come from and the files are compared with
    on_top_of_approved = judged_against == head_commit
    only_checks = (head_has_the_gate and on_top_of_approved and not merge_head and bool(changed_checks)
                   and all(name in changed_checks or name in added_receipts for name in names))
    since_approved = staged_changes(root, judged_against) if has_head else []
    checks_changed = [path for _, path in since_approved if is_check_file(path)]

    scratch = tempfile.mkdtemp(prefix="workshop-commit-")
    snapshot = os.path.join(scratch, "staged")
    approved_checks = os.path.join(scratch, "checks")
    failed = False
    lines = []
    try:
        subprocess.run(["git", "-C", root, "checkout-index", "-a", f"--prefix={snapshot}/"], check=True,
                       capture_output=True)
        if head_has_the_gate:
            if requested != "HEAD":
                lines.append("note: the gate was asked to take its checks from the staged files; the last commit has"
                             " the gate, so the checks of the last approved commit are used")
            if approved_commit is None:
                shallow = git(root, "rev-parse", "--is-shallow-repository").stdout.strip() == "true"
                lines.append("note: walking back along the main line, no commit is approved by the gate, so the"
                             " checks come from the last commit and the files are compared with it"
                             + ("; this copy's history is cut short (a shallow clone): fetch the whole history with"
                                " git fetch --unshallow, so the gate can find the last approved commit"
                                if shallow else ""))
            elif not on_top_of_approved:
                count = len(approval.not_approved_since(approved_commit))
                lines.append(f"note: the last commit the gate approved, walking back along the main line, is"
                             f" {approved_commit[:9]}; {count} commit(s) since then were not approved by the gate,"
                             " so the checks come from it and the files are compared with it")
            os.makedirs(approved_checks)
            archive = subprocess.run(["git", "-C", root, "archive", judged_against, SCRIPTS, ADD_SOURCE_SCRIPTS],
                                     capture_output=True, check=True)
            subprocess.run(["tar", "-x", "-C", approved_checks], input=archive.stdout, check=True)
        else:
            approved_checks = snapshot
            lines.append("note: the commit gate is new in this commit, so its checks come from the staged files;"
                         " this one commit is checked by the checks it brings in")
        approved_scripts = os.path.join(approved_checks, SCRIPTS)
        staged_scripts = os.path.join(snapshot, SCRIPTS)
        judging_scripts = staged_scripts if only_checks else approved_scripts
        if only_checks:
            lines.append("note: this commit changes only checks, so its own changed machine checks run on it; its"
                         " receipt is checked by the last approved commit's receipt check, and that commit's"
                         " planted-fault test judges the changed checks")

        code, output, trouble = run_script(
            "run_all_checks.py",
            [os.path.join(judging_scripts, "run_all_checks.py"), "--staged", "--git-root", root,
             *(["--against", judged_against] if head_has_the_gate else []),
             *[option for commit in merging for option in ("--also-against", commit)],
             "--books-from", os.path.join(root, "sources", "raw"), snapshot],
            environment_for_this_repository())
        lines.append(output.replace(snapshot + "/", "").replace(snapshot, "(staged files)").rstrip())
        if trouble:
            lines.append(trouble)
        failed = failed or code != 0

        code, output, trouble = run_script("review_receipt.py",
                                           [os.path.join(approved_scripts, "review_receipt.py"), "check", "--root", root])
        lines.append(f"{'passed  ' if code == 0 else 'FAILED  '}  review receipt\n{indented(output)}".rstrip())
        if trouble:
            lines.append(trouble)
        failed = failed or code != 0

        reviews_touched = [path for kind, path in since_approved
                           if path.startswith(".claude/reviews/") and kind in ("M", "D")]
        if reviews_touched:
            failed = True
            lines.append("FAILED    a review receipt already committed is changed or deleted\n" + indented(
                ", ".join(reviews_touched) + "\nReceipts are only ever added to. A correction to one is a new file"
                f" that points to it. Put it back as the last approved commit has it: git checkout {judged_against[:9]}"
                " -- <receipt>"))

        recheck = os.path.join(approved_scripts, "recheck_commits.py")
        if os.path.exists(recheck):
            code, output, trouble = run_script(
                "recheck_commits.py", [recheck, "--root", root, *(["--also", merge_head] if merge_head else [])],
                environment_for_this_repository())
            if "not checked: the commit gate is not in this history yet" in output:
                lines.append("not run   earlier commits the gate did not approve (the gate is not in the history yet)")
            else:
                shown = output if code != 0 else "\n".join(
                    line for line in output.splitlines() if line.startswith(("rechecked", "not checked", "note:")))
                lines.append(f"{'passed  ' if code == 0 else 'FAILED  '}  earlier commits the gate did not approve\n"
                             f"{indented(shown)}".rstrip())
            if trouble:
                lines.append(trouble)
            failed = failed or code != 0

        inside_the_test = inside_the_planted_fault_test(root)
        if head_has_the_gate and changed_checks and others:
            failed = True
            lines.append("FAILED    a check is changed together with other work\n" + indented(
                f"changed checks: {', '.join(changed_checks)}\nother files: {', '.join(others)}\n"
                "A check is corrected in its own commit (with its review receipt, and the log), so that"
                " it is reviewed on its own and cannot pass the work it would have stopped. Unstage the"
                " other files (git restore --staged <file>) and commit them afterwards."))
            lines.append("not run   the planted-fault tests (the commit is stopped already)")
        elif head_has_the_gate and checks_changed:
            if inside_the_test:
                lines.append("not run   the planted-fault tests (this commit is made inside the planted-fault test"
                             " itself, which must not call itself again)")
            else:
                failed = run_planted_fault_tests(os.path.join(approved_scripts, "test_checks.py"), snapshot, root,
                                                 judged_against, "the last approved commit's planted-fault test, on"
                                                 " the changed checks", lines, allow_retired=True) or failed
                if any(f"{SCRIPTS}/{name}" in checks_changed for name in ("test_checks.py", "test_the_gate.py")):
                    failed = run_planted_fault_tests(os.path.join(staged_scripts, "test_checks.py"), snapshot, root,
                                                     judged_against, "the changed planted-fault test", lines,
                                                     allow_retired=False) or failed
        elif not head_has_the_gate and changed_checks and not inside_the_test:
            failed = run_planted_fault_tests(os.path.join(staged_scripts, "test_checks.py"), snapshot, root,
                                             judged_against, "the planted-fault test brought in", lines,
                                             allow_retired=False) or failed

        if not failed:
            tree = git(root, "write-tree").stdout.strip()
            passed_file = git(root, "rev-parse", "--git-path", "workshop-gate-passed").stdout.strip()
            passed_file = passed_file if os.path.isabs(passed_file) else os.path.join(root, passed_file)
            with open(passed_file, "w", encoding="utf-8") as record:
                record.write(tree + "\n")
    except subprocess.CalledProcessError as problem:
        failed = True
        lines.append(f"COULD NOT RUN  copying the staged files or the checks: {problem}")
    finally:
        shutil.rmtree(scratch, ignore_errors=True)

    if os.environ.get(RESULT_FILE):
        try:
            with open(os.environ[RESULT_FILE], "w", encoding="utf-8") as result:
                result.write("stopped\n" if failed else "passed\n")
        except OSError:
            pass
    print("\n".join(line for line in lines if line))
    if failed:
        print(
            "\nCOMMIT STOPPED. A failed check is a sign that something may be wrong: see the error-correction skill,"
            " references/checks-and-cases.md, section 2 (usually the check is right: put right what it found)."
            " If the check itself is wrong, correct the check in its own commit. Never get round it.",
            file=sys.stderr,
        )
        return 1
    print("All checks passed; committing.")
    return 0


def retired_tests(root, since):
    """{test name: whether the owner is named first as reviewer} for every test named under "Tests retired" in a
    review receipt added since the last approved commit, in the staged files (this commit's own receipt, and those
    that came with a merge, a rebase or a commit made without the gate)."""
    added = [path for kind, path in staged_changes(root, since) if kind == "A" and RECEIPT_NAME.match(path)] \
        if since else []
    retired = {}
    for path in added:
        receipt = git(root, "show", f":{path}")
        if receipt.returncode != 0:
            continue
        match = re.search(r"^## Tests retired\s*$(.*?)(?=^## |\Z)", receipt.stdout, flags=re.M | re.S)
        reviewer = re.search(r"\*\*Reviewed by:\*\*[ \t]*([^\n]*)", receipt.stdout)
        owner = (reviewer.group(1) if reviewer else "").strip().lower().startswith(("the owner", "owner"))
        for line in (match.group(1) if match else "").splitlines():
            name = line.strip().lstrip("-* ").strip()
            if name and not name.startswith("("):
                retired[name] = retired.get(name, False) or owner
    return retired


def run_planted_fault_tests(test_script, snapshot, root, since, label, lines, allow_retired):
    """Run a planted-fault test on the staged checks; return True if it failed."""
    if not os.path.exists(test_script):
        lines.append(f"FAILED    {label}: there is no such test, so the changed checks cannot be tested; a check"
                     " change is never committed untested")
        return True
    environment = {**environment_for_copies(), INSIDE_THE_TEST: "1"}
    code, output, trouble = run_script(label, [test_script, snapshot], environment)
    failures = [line[len("FAILED"):].strip() for line in output.splitlines() if line.startswith("FAILED")]
    could_not_run = [name for name in failures if name.endswith("could not run")]
    retired = retired_tests(root, since) if allow_retired else {}
    named = [name for name in failures if name in retired and name not in could_not_run]
    retired_here = [name for name in named if name.startswith(UNPROTECTED_TESTS) or retired[name]]
    protected_without_owner = [name for name in named if name not in retired_here]
    unexplained = [name for name in failures if name not in retired_here]
    failed = bool(trouble) or (code != 0 and (bool(unexplained) or not failures))
    not_run = re.search(r"not run: (\d+)", output)
    lines.append(f"{'FAILED  ' if failed else 'passed  '}  {label}"
                 + (f" ({not_run.group(1)} test(s) not run inside it)" if not_run and not failed else ""))
    for name in retired_here:
        lines.append(f"          retired in a receipt: {name}")
    for name in protected_without_owner:
        lines.append(f"          NOT retired (it guards the workshop, so the owner must be named first as reviewer):"
                     f" {name}")
    if failed:
        shown = [line for line in output.splitlines() if not line.startswith("ok")]
        lines.append(indented("\n".join(shown)).rstrip())
        if allow_retired and unexplained:
            lines.append(indented(
                "A planted fault the last approved commit's checks caught is no longer caught. If the check was meant to"
                " change so that this test no longer fits, name the test, one per line, under '## Tests retired' in"
                " the review receipt, with why; the reviewer must have seen it. A test that could not run is never"
                " retired, and any test but those of the maps and the owner quotes is retired only with the owner"
                " named first under 'Reviewed by' (the owner then agrees to lose that guard).").rstrip())
    if trouble:
        lines.append(trouble)
    return failed


if __name__ == "__main__":
    sys.exit(main())
