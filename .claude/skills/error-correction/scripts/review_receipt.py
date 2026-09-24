#!/usr/bin/env python3
"""Tie every change to what the workshop says to a review of that exact change.

A review receipt is a short file in .claude/reviews/ that records who
reviewed a change, what they found, what was done about each finding, the
verdict, and the reviewer's own report, pasted word for word. Its name is
the change's fingerprint: a short code worked out from the exact change
about to be committed (the staged difference from the last commit; staged
means marked with git add to go into the next commit). Change one
character after the review and the fingerprint changes, so the receipt no
longer fits and the change needs a review of its own. That is the point: a
fix made after a review was the workshop's commonest source of new errors.

What this can and cannot show: it checks that the receipt exists, fits the
change, is filled in (no field left empty or still holding the form's
bracketed hint), names a reviewer other than the maker, and carries the
reviewer's report. It cannot tell whether the named reviewer really ran.
That part is on trust, with a trace: a made-up report would be a false
statement in a kept file.

Which changes need a receipt: changes to files under .claude/skills/,
.claude/agents/, .claude/hooks/ and .githooks/, to .claude/settings.json,
.gitattributes and CLAUDE.md, to kept cases (kept-cases/, except its run
record runs.md and runs/), and to numbered top-level write-ups. Records
that are added to all the time (the project story, README, the questions
file, the corrections file) do not.

A light receipt ("Reviewed by: none", verdict "light (why)") is allowed for
a change that alters no meaning (a typo, a link, a map row). It is never
allowed for a change to a check, a hook, the settings file, .gitattributes,
the frozen list or the allowed-titles list: those always get a full review.

A receipt written late, for a commit already made (--commit), may also
record a review that did not pass: "not passed (withdrawn in ...)", naming
where the change was taken back out. That is never allowed for a staged
change: a change that did not pass is not committed.

For a merge, only the merge's own changes need a receipt: whatever it
holds beyond the automatic merge of its parents (usually nothing). The
commits it brings in carry their own receipts.

Commands:
  review_receipt.py fingerprint      print the fingerprint of the staged change, and the files it covers
  review_receipt.py new              write a receipt form for the staged change, to be filled in
  review_receipt.py check            exit 1 unless the staged change has a complete, staged receipt
  review_receipt.py check --commit C  the same for a commit already made (C against its parent); the
                                      receipt may be in C itself or added by a later commit
  review_receipt.py new --commit C    write a form for a commit already made (a receipt written late)
All take [--root PATH] (default: the git top folder of the current folder).
"""
import glob
import hashlib
import os
import re
import subprocess
import sys

REVIEWS_FOLDER = ".claude/reviews"
RECORD_PREFIXES = ("22 Questions", "27 Corrections")
IN_SCOPE_PREFIXES = (".claude/skills/", ".claude/agents/", ".claude/hooks/", ".githooks/", "kept-cases/")
IN_SCOPE_FILES = ("CLAUDE.md", ".claude/settings.json", ".gitattributes")
NOT_IN_SCOPE = ("kept-cases/runs.md", "kept-cases/runs/")
NEVER_LIGHT_PREFIXES = (".claude/skills/error-correction/scripts/", ".claude/skills/add-source/scripts/",
                        ".claude/hooks/", ".githooks/")
NEVER_LIGHT_FILES = (".claude/settings.json", ".gitattributes", ".claude/skills/error-correction/frozen-files.txt")
VERDICTS = ("passed", "passed after changes", "light")
LATE_VERDICTS = VERDICTS + ("not passed",)
EMPTY_TREE = "4b825dc642cb6eb9a060e54bf8d69288fbee4904"  # git's name for a tree with nothing in it
REPORT_HEADING = "## Reviewer's report"
SHORTEST_REPORT = 40  # words; a report shorter than this is a verdict, not a report


def git(root, *arguments):
    result = subprocess.run(["git", "-C", root, "-c", "core.quotePath=false", *arguments],
                            capture_output=True, text=True, check=False)
    return result.returncode, result.stdout


def automatic_merge(root, first, second):
    """The tree git would make by merging the two commits with no hand changes (conflicts left marked); if this git
    cannot say (older than 2.38), the first commit, so that the whole change needs its receipt rather than none of it."""
    code, output = git(root, "merge-tree", "--write-tree", first, second)
    tree = output.split("\n", 1)[0].strip()
    return tree if code in (0, 1) and tree else first


def commits_being_merged(root):
    """The commits a merge in progress brings in: MERGE_HEAD once git has written it (a merge finished with git
    commit), or, while git runs the pre-merge-commit hook, the names git passes in GIT_REFLOG_ACTION ("merge side")."""
    code, merge_head = git(root, "rev-parse", "-q", "--verify", "MERGE_HEAD")
    if code == 0 and merge_head.strip():
        return [merge_head.strip()]
    action = os.environ.get("GIT_REFLOG_ACTION", "")
    if action.startswith("pull"):
        _, fetch_head = git(root, "rev-parse", "--git-path", "FETCH_HEAD")
        fetch_head = fetch_head.strip()
        fetch_head = fetch_head if os.path.isabs(fetch_head) else os.path.join(root, fetch_head)
        try:
            with open(fetch_head, encoding="utf-8") as fetched:
                return [line.split()[0] for line in fetched if line.strip() and "not-for-merge" not in line]
        except OSError:
            return []
    if not action.startswith("merge "):
        return []
    found = []
    for name in action.split()[1:]:
        code, commit = git(root, "rev-parse", "-q", "--verify", f"{name}^{{commit}}")
        if code == 0 and commit.strip():
            found.append(commit.strip())
    return found


def comparison(root, commit=None):
    """The two sides of the change a receipt covers, as arguments for git diff."""
    if commit is None:
        merging = commits_being_merged(root)
        if merging:
            return ["--cached", automatic_merge(root, "HEAD", merging[0])]
        return ["--cached"]
    code, parents = git(root, "rev-list", "--parents", "-n", "1", commit)
    parents = parents.split()[1:]
    if not parents:
        return [EMPTY_TREE, commit]
    if len(parents) > 1:
        return [automatic_merge(root, parents[0], parents[1]), commit]
    return [f"{commit}^", commit]


def in_scope(path):
    if path.startswith(REVIEWS_FOLDER + "/") or path in NOT_IN_SCOPE or path.startswith(NOT_IN_SCOPE[1]):
        return False
    if path.startswith(IN_SCOPE_PREFIXES) or path in IN_SCOPE_FILES:
        return True
    return "/" not in path and re.match(r"^\d+ .*\.md$", path) is not None and not path.startswith(RECORD_PREFIXES)


def never_light(path):
    return path.startswith(NEVER_LIGHT_PREFIXES) or path in NEVER_LIGHT_FILES


def changed_files(root, commit=None):
    range_arguments = comparison(root, commit)
    _, names = git(root, "diff", *range_arguments, "--name-only", "--no-renames", "-z")
    return sorted(name for name in names.split("\0") if name and in_scope(name))


def fingerprint(root, commit=None):
    """The change's fingerprint: made from the names of the files it changes, the lines it adds and removes, and
    the one unchanged line either side of each change, which holds its place; not from git's internal names for
    the files, nor the line numbers. So a rebase or a cherry-pick that leaves the change and its neighbouring lines
    as they were keeps the fingerprint, and finds the receipt it already has; a line moved after its review, or an
    edit made right next to the change, gives a new fingerprint and needs a new review."""
    files = changed_files(root, commit)
    if not files:
        return None, files
    range_arguments = comparison(root, commit)
    _, difference = git(root, "diff", *range_arguments, "--no-color", "--no-ext-diff", "--unified=1",
                        "--binary", "--no-renames", "--", *files)
    kept = [line for line in difference.splitlines() if not line.startswith(("index ", "@@"))]
    return hashlib.sha256("\n".join(kept).encode()).hexdigest()[:16], files


def receipt_path(fingerprint_code):
    return f"{REVIEWS_FOLDER}/{fingerprint_code}.md"


def field(text, name):
    """The value of '- **name:** value', read to the end of its own line only."""
    match = re.search(r"\*\*" + re.escape(name) + r":\*\*[ \t]*([^\n]*)", text)
    return match.group(1).strip() if match else ""


def section(text, heading):
    start = text.find(heading)
    if start < 0:
        return ""
    rest = text[start + len(heading):]
    next_heading = re.search(r"^## ", rest, flags=re.M)
    return (rest[: next_heading.start()] if next_heading else rest).strip()


def book_authors(root, commit=None):
    """The authors in the source register both before and after the change (the last commit and the staged files
    for a staged change; the commit's parent and the commit for a commit already made): so a change can neither drop
    a book from the register nor add one, together with a module drawing on it, and skip its Book text line."""
    authors = set()
    for place in ([f"{commit}^", commit] if commit else ["HEAD", ""]):
        code, text = git(root, "show", f"{place}:sources/README.md")
        if code == 0:
            works = text.split("Registered works", 1)[-1]
            authors |= set(re.findall(r"^\| ([A-Z][\w.'-]+(?: [A-Z][\w.'-]+)+),", works, flags=re.M))
    return sorted(authors)


def books_present(root):
    return bool(glob.glob(os.path.join(root, "sources", "raw", "*.txt")))


def draws_on_a_book(root, files, commit=None):
    authors = [author.split()[-1] for author in book_authors(root, commit)]
    for path in files:
        if not path.startswith(".claude/skills/") or not path.endswith(".md"):
            continue
        spec = f":{path}" if commit is None else f"{commit}:{path}"
        code, text = git(root, "show", spec)
        if code == 0 and any(re.search(r"\b" + author + r"\b", text) for author in authors):
            return True
    return False


def find_receipt(root, path, commit):
    """The receipt's text and where it was found, or (None, where it was looked for)."""
    places = [":"] if commit is None else [f"{commit}:", "HEAD:", ":"]
    for place in places:
        found, text = git(root, "show", f"{place}{path}")
        if found == 0:
            return text, place
    return None, ", ".join("the staged files" if place == ":" else place.rstrip(":") for place in places)


def problems_with_text(text, path, files, root, commit):
    problems = []
    for name in ("Change", "Maker", "Reviewed by", "Findings", "Verdict"):
        value = field(text, name)
        if not value:
            problems.append(f"{path}: '{name}' is empty")
        elif value.startswith("("):
            problems.append(f"{path}: '{name}' still holds the form's hint in brackets; replace it with the answer")
    reviewer, maker, verdict = field(text, "Reviewed by"), field(text, "Maker"), field(text, "Verdict").lower()
    light = verdict.startswith("light")
    allowed_verdicts = VERDICTS if commit is None else LATE_VERDICTS
    if verdict and not verdict.startswith("(") and not any(verdict.startswith(allowed) for allowed in allowed_verdicts):
        problems.append(f"{path}: 'Verdict' must begin with one of: {', '.join(allowed_verdicts)}")
    if verdict.startswith("not passed") and "withdrawn" not in verdict:
        problems.append(f"{path}: a late review that did not pass says where the change was withdrawn:"
                        " 'not passed (withdrawn in <commit or this commit>)'")
    if reviewer.lower().startswith("none") and not light:
        problems.append(f"{path}: no reviewer is named, so the verdict can only be 'light' (no meaning change)")
    if light and len(verdict) < len("light (x)"):
        problems.append(f"{path}: a light verdict must say why no review was needed")
    if light:
        checks_changed = [name for name in files if never_light(name)]
        if checks_changed:
            problems.append(f"{path}: a light receipt is never enough for a change to a check, a hook, a list or the"
                            f" settings ({', '.join(checks_changed)}); it needs a full review")
    if reviewer and maker and reviewer.lower() == maker.lower() and not light:
        problems.append(f"{path}: the reviewer is the maker; nobody grades their own work")
    if not light:
        report = section(text, REPORT_HEADING)
        if report.startswith("("):
            problems.append(f"{path}: '{REPORT_HEADING}' still holds the form's hint; paste the reviewer's report")
        elif len(report.split()) < SHORTEST_REPORT:
            problems.append(f"{path}: a full receipt carries the reviewer's own report, pasted word for word under"
                            f" '{REPORT_HEADING}' (or the path of the kept file that holds it, with its first lines);"
                            " a verdict alone is not a receipt")
    book_text = field(text, "Book text")
    needs_book_text = not books_present(root) and draws_on_a_book(root, files, commit)
    if needs_book_text and (not book_text or book_text.startswith("(")):
        problems.append(
            f"{path}: the book texts are not here, so the copying check cannot run, and a changed module draws on a"
            " book; say in 'Book text:' what book text the change adds (normally 'none added, because ...')"
        )
    return problems


def problems_with(root, commit=None):
    code, files = fingerprint(root, commit)
    if code is None:
        return [], None, files
    path = receipt_path(code)
    text, where = find_receipt(root, path, commit)
    if text is None:
        if commit is None and os.path.exists(os.path.join(root, path)):
            return [f"the receipt {path} exists but is not staged: git add it"], code, files
        how = "review_receipt.py new" if commit is None else f"review_receipt.py new --commit {commit[:9]}"
        return [f"no review receipt {path} in {where} for this change to: {', '.join(files)}"
                f" (make one with {how} after an independent review; see the error-correction skill,"
                " references/reviews-and-briefs.md, section 2)"], code, files
    return problems_with_text(text, path, files, root, commit), code, files


FORM = """# Review of change {code}

- **Change:** (one line: what changed, and why; then the plan, fixed before the change: for a full correction it is in the correction's record; for a smaller change, say what was on the list and anything added to it, and when)
- **Files:** {files}
- **Maker:** (the agent or person who made the change)
- **Reviewed by:** (theory-checker, use-tester, copy-checker, the owner, or none for a light receipt)
- **Findings:** (each finding's target; what is wrong; applied or rejected, and why. Or: none)
- **Marks on new or changed rules, rivals and examples:** (each: held, held if, two routes, loose, idle or unknown, with what holds it. Or: none changed)
- **Book text:** (only if the book texts are absent and a changed module draws on a book: none added, because ...)
- **Verdict:** (passed / passed after changes / light (no meaning change: why); for a receipt written late, also: not passed (withdrawn in <commit>), once the change is taken back out)

'passed after changes' is written only after a reviewer has seen the changes: the Findings line gives the
first review's findings as applied or rejected, and the report below is the re-review of the edits.

## Reviewer's report

(paste the reviewer's report here, word for word, or give the path of the kept file that holds it and copy its first lines; not needed for a light receipt)

## Tests retired

(only for a change to a check: each planted-fault test from the last approved commit that no longer fits the changed check, and why; the reviewer must have seen this; for any test but those of the maps and the owner quotes, the owner must be named first under 'Reviewed by'. Or leave this section out.)
"""


def main():
    arguments = sys.argv[1:]
    root = None
    if "--root" in arguments:
        index = arguments.index("--root")
        root = os.path.abspath(arguments[index + 1])
        del arguments[index:index + 2]
    if root is None:
        _, top = git(os.getcwd(), "rev-parse", "--show-toplevel")
        root = top.strip() or os.getcwd()
    commit = None
    if "--commit" in arguments:
        index = arguments.index("--commit")
        commit = arguments[index + 1]
        del arguments[index:index + 2]
    command = arguments[0] if arguments else "check"

    if command == "fingerprint":
        code, files = fingerprint(root, commit)
        print("no receipt needed: nothing in the reviewed files is changed" if code is None
              else f"{code}\ncovers: {', '.join(files)}\nreceipt: {receipt_path(code)}")
        return 0
    if command == "new":
        code, files = fingerprint(root, commit)
        if code is None:
            print("no receipt needed: nothing in the reviewed files is changed")
            return 0
        path = os.path.join(root, receipt_path(code))
        if os.path.exists(path):
            sys.exit(f"{receipt_path(code)} already exists")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as receipt:
            receipt.write(FORM.format(code=code, files=", ".join(files)))
        print(f"wrote {receipt_path(code)}: fill it in from the review, then git add it")
        return 0
    if command == "check":
        problems, code, _ = problems_with(root, commit)
        for problem in problems:
            print(problem)
        if code is None:
            print("review receipt: not needed (no reviewed file changed)")
        elif not problems:
            text_of_receipt = find_receipt(root, receipt_path(code), commit)[0] or ""
            if field(text_of_receipt, "Verdict").lower().startswith("not passed"):
                print(f"review receipt: {receipt_path(code)} records a review that did not pass; the change was withdrawn")
            else:
                print(f"review receipt: {receipt_path(code)} is complete")
        return 1 if problems else 0
    sys.exit(__doc__)


if __name__ == "__main__":
    sys.exit(main())
