#!/usr/bin/env python3
"""Check that no frozen file has changed, and that every frozen file is listed.

The frozen files are the owner's theories in sources/ (every file there,
in any folder but raw/, except README.md) and everything in foundations/. Their fingerprints are
listed in ../frozen-files.txt. A fingerprint (SHA-256) is a short code
worked out from a file's exact contents; change one character and the code
changes.

What it checks:
1. Every listed file exists and still has its fingerprint. Where the last
   commit's list (or the list in the commit given with --against) already
   had the file, the file is compared with that earlier fingerprint, so a
   later line cannot give an edited file a new one.
2. No path is listed twice.
3. Every file that should be frozen is on the list. A new theory or a
   revision is added with --add, as step 2 or 3 of the add-source skill says.
4. The list is only ever added to: every line in the earlier list is still
   there, unchanged. On a first commit there is no earlier list, and that
   is printed as "not checked".

Git is told never to change these files' line endings (.gitattributes), so
a copy on Windows has the same bytes and the same fingerprints. With
--index (the commit gate) or --commit, the contents are read from git
itself, as they will be or were committed, so a local setting that
changes what git writes to disk cannot show the check a different text; a
frozen file stored as a link to somewhere else is refused.

It prints each problem in plain words. Exit code 1 if there is any problem,
0 if there is none.

Usage:
  check_frozen_files.py [--git-root PATH] [--against COMMIT] [--index | --commit COMMIT] [REPOSITORY_ROOT]
      --git-root: where the git history is, when REPOSITORY_ROOT is a copy of
      the files about to be committed (default REPOSITORY_ROOT);
      --against: the commit whose list is the earlier one (default HEAD);
      --index: read the frozen files and the list from what is staged;
      --commit: read them from that commit, and compare with its parent
  check_frozen_files.py --add PATH [REPOSITORY_ROOT]    fingerprint a newly stored frozen file
  check_frozen_files.py --list [REPOSITORY_ROOT]        print the frozen paths, one per line
"""
import hashlib
import os
import re
import subprocess
import sys

LIST_NAME = "frozen-files.txt"
LIST_IN_REPOSITORY = f".claude/skills/error-correction/{LIST_NAME}"
LIST_LINE = re.compile(r"^([0-9a-f]{64})\s+(.+?)\s+added\s+(\S.*)$")


def list_path(repository_root):
    return os.path.join(repository_root, LIST_IN_REPOSITORY)


def fingerprint(path):
    with open(path, "rb") as frozen_file:
        return hashlib.sha256(frozen_file.read()).hexdigest()


def list_lines(text):
    """The fingerprint lines of a list, with notes and blank lines left out."""
    return [line.strip() for line in text.splitlines() if line.strip() and not line.strip().startswith("#")]


def parse(lines):
    """Return ([(path, fingerprint)], [lines that could not be read]). The path is kept whole, spaces and all."""
    entries, unreadable = [], []
    for line in lines:
        match = LIST_LINE.match(line)
        if match:
            entries.append((match.group(2), match.group(1)))
        else:
            unreadable.append(line)
    return entries, unreadable


def read_list(repository_root):
    with open(list_path(repository_root), encoding="utf-8") as list_file:
        return list_lines(list_file.read())


def frozen_by_rule(path):
    """True if the working rules freeze this path (a path from the repository root)."""
    if path.startswith("foundations/"):
        return True
    return path.startswith("sources/") and not path.startswith("sources/raw/") and path != "sources/README.md"


def should_be_frozen(repository_root):
    """Every file the working rules freeze, as paths from the repository root."""
    paths = []
    for top in ("sources", "foundations"):
        for folder, folder_names, file_names in os.walk(os.path.join(repository_root, top)):
            folder_names[:] = [name for name in folder_names if not (top == "sources" and name == "raw")]
            for file_name in sorted(file_names):
                path = os.path.relpath(os.path.join(folder, file_name), repository_root).replace(os.sep, "/")
                if frozen_by_rule(path):
                    paths.append(path)
    return sorted(paths)


def git_output(git_root, *arguments, binary=False):
    result = subprocess.run(["git", "-C", git_root, "-c", "core.quotePath=false", *arguments],
                            capture_output=True, check=False)
    return result.returncode, (result.stdout if binary else result.stdout.decode("utf-8", "replace"))


def commit_that_has(git_root, start, path, expected):
    """The most recent commit from start whose copy of path still has the fingerprint on the frozen list, so that
    the way back never restores a changed text an approved commit already holds; None if none is found."""
    code, listing = git_output(git_root, "log", "--format=%H", "-n", "200", start, "--", path)
    if code != 0:
        return None
    for commit in listing.split():
        found, content = git_output(git_root, "show", f"{commit}:{path}", binary=True)
        if found == 0 and hashlib.sha256(content).hexdigest() == expected:
            return commit
    return None


def way_back(git_root, start, path, expected):
    """The advice for a changed frozen file: the commit to take it from, and the command."""
    good = commit_that_has(git_root, start or "HEAD", path, expected) if git_root else None
    if good is None:
        return (f"put it back as it was when it was listed (no commit from {(start or 'HEAD')[:9]} back has that text;"
                " ask the owner for their copy)")
    return f"put it back as {good[:9]} has it (git checkout {good[:9]} -- '{path}')"


def check_from_git(git_root, spec, earlier):
    """The same check, reading everything from git: spec ':' is the staged files, or a commit id.

    earlier is the commit whose list is the earlier one (HEAD for the staged files, the parent for a commit)."""
    problems, notes = [], []
    code, list_text = git_output(git_root, "show", f"{spec}{LIST_IN_REPOSITORY}" if spec == ":" else f"{spec}:{LIST_IN_REPOSITORY}")
    if code != 0:
        return [f"{LIST_NAME}: not found in {'the staged files' if spec == ':' else spec}"], notes
    current = list_lines(list_text)
    entries, unreadable = parse(current)
    for line in unreadable:
        problems.append(f"{LIST_NAME}: a line that is not 'fingerprint  path  added commit': '{line[:60]}'")
    seen = {}
    for path, listed_fingerprint in entries:
        seen.setdefault(path, []).append(listed_fingerprint)
    for path, fingerprints in seen.items():
        if len(fingerprints) > 1:
            problems.append(f"{LIST_NAME}: {path} is listed {len(fingerprints)} times")
    earlier_fingerprints = {}
    previous = earlier_lines(git_root, earlier) if earlier else None
    if previous is None:
        notes.append(f"not checked: whether the list was only added to (no earlier list in {earlier or 'a parent'})")
    else:
        for line in previous:
            if line not in current:
                problems.append(f"{LIST_NAME}: a line from {earlier[:9]} has been removed or changed ('{line[:40]}...');"
                                " the list is only ever added to")
        earlier_fingerprints = dict(parse(previous)[0])
    if spec == ":":
        _, listing = git_output(git_root, "ls-files", "-s", "-z")
        files = {}
        for record in listing.split("\0"):
            if record:
                mode_and_rest, _, path = record.partition("\t")
                files[path] = mode_and_rest.split()[0]
    else:
        _, listing = git_output(git_root, "ls-tree", "-r", "-z", spec)
        files = {}
        for record in listing.split("\0"):
            if record:
                mode_and_rest, _, path = record.partition("\t")
                files[path] = mode_and_rest.split()[0]
    for path, fingerprints in seen.items():
        expected = earlier_fingerprints.get(path, fingerprints[0])
        if path not in files:
            problems.append(f"{path}: frozen file is missing")
            continue
        if files[path] == "120000":
            problems.append(f"{path}: a frozen file is stored as a link to somewhere else; store the text itself")
            continue
        _, content = git_output(git_root, "show", f"{spec}{path}" if spec == ":" else f"{spec}:{path}", binary=True)
        if hashlib.sha256(content).hexdigest() != expected:
            problems.append(f"{path}: frozen file has changed. Frozen files are never edited; "
                            f"{way_back(git_root, earlier, path, expected)}, and add any change the owner wants as a"
                            " revision through the add-source skill")
    for path in sorted(files):
        if frozen_by_rule(path) and path not in seen:
            problems.append(f"{path}: should be frozen but is not on the list; if it is a new theory or revision,"
                            " run check_frozen_files.py --add after storing it (add-source step 2 or 3)")
    return problems, notes


def earlier_lines(git_root, commit):
    """The fingerprint lines in that commit's copy of the list, or None if it has none."""
    result = subprocess.run(["git", "-C", git_root, "show", f"{commit}:{LIST_IN_REPOSITORY}"],
                            capture_output=True, text=True, check=False)
    return list_lines(result.stdout) if result.returncode == 0 else None


def check(repository_root, git_root=None, against="HEAD"):
    problems, notes = [], []
    current = read_list(repository_root)
    entries, unreadable = parse(current)
    for line in unreadable:
        problems.append(f"{LIST_NAME}: a line that is not 'fingerprint  path  added commit': '{line[:60]}'")

    seen = {}
    for path, listed_fingerprint in entries:
        seen.setdefault(path, []).append(listed_fingerprint)
    for path, fingerprints in seen.items():
        if len(fingerprints) > 1:
            problems.append(f"{LIST_NAME}: {path} is listed {len(fingerprints)} times; a frozen file has one line,"
                            " and a changed version is a new file with its own name")

    earlier = earlier_lines(git_root or repository_root, against)
    earlier_fingerprints = {}
    if earlier is None:
        notes.append(f"not checked: whether the list was only added to (the list has no earlier version in {against})")
    else:
        for line in earlier:
            if line not in current:
                problems.append(f"{LIST_NAME}: a line from {against} has been removed or changed ('{line[:40]}...');"
                                " the list is only ever added to")
        earlier_fingerprints = dict(parse(earlier)[0])

    for path, fingerprints in seen.items():
        expected = earlier_fingerprints.get(path, fingerprints[0])
        full_path = os.path.join(repository_root, path)
        if not os.path.exists(full_path):
            problems.append(f"{path}: frozen file is missing")
        elif fingerprint(full_path) != expected:
            problems.append(
                f"{path}: frozen file has changed. Frozen files are never edited; "
                f"{way_back(git_root or repository_root, against, path, expected)}, and add any change the owner wants"
                " as a revision through the add-source skill"
            )
    for path in should_be_frozen(repository_root):
        if path not in seen:
            problems.append(
                f"{path}: should be frozen but is not on the list; if it is a new theory or revision,"
                " run check_frozen_files.py --add after storing it (add-source step 2 or 3)"
            )
    return problems, notes


def add(path, repository_root):
    relative_path = os.path.relpath(os.path.abspath(path), repository_root)
    listed = [listed_path for listed_path, _ in parse(read_list(repository_root))[0]]
    if relative_path in listed:
        sys.exit(f"{relative_path} is already on the frozen list; a frozen file is never refingerprinted.")
    in_last_commit = [listed_path for listed_path, _ in parse(earlier_lines(repository_root, "HEAD") or [])[0]]
    if relative_path in in_last_commit:
        sys.exit(f"{relative_path} was on the frozen list in the last commit; it cannot be added again.")
    added_by = "not yet committed"
    commits = subprocess.run(
        ["git", "-C", repository_root, "log", "--diff-filter=A", "--format=%h", "--", relative_path],
        capture_output=True, text=True, check=False,
    ).stdout.split()
    if commits:
        added_by = commits[-1]
    with open(list_path(repository_root), "a", encoding="utf-8") as list_file:
        list_file.write(f"{fingerprint(os.path.join(repository_root, relative_path))}  {relative_path}  added {added_by}\n")
    print(f"Added {relative_path} to the frozen list.")


def main():
    arguments = sys.argv[1:]
    if arguments and arguments[0] == "--add":
        if len(arguments) < 2:
            sys.exit(__doc__)
        repository_root = os.path.abspath(arguments[2] if len(arguments) > 2 else ".")
        add(arguments[1], repository_root)
        return
    if arguments and arguments[0] == "--list":
        repository_root = os.path.abspath(arguments[1] if len(arguments) > 1 else ".")
        for path, _ in parse(read_list(repository_root))[0]:
            print(path)
        return
    git_root, against, spec = None, "HEAD", None
    while arguments[:1] and arguments[0] in ("--git-root", "--against", "--index", "--commit"):
        if arguments[0] == "--index":
            spec, arguments = ":", arguments[1:]
            continue
        if arguments[0] == "--git-root":
            git_root = os.path.abspath(arguments[1])
        elif arguments[0] == "--against":
            against = arguments[1]
        else:
            spec = arguments[1]
        arguments = arguments[2:]
    repository_root = os.path.abspath(arguments[0] if arguments else ".")
    if spec is None:
        problems, notes = check(repository_root, git_root, against)
    else:
        git_root = git_root or repository_root
        if spec == ":":
            earlier = against if git_output(git_root, "rev-parse", "-q", "--verify", against)[0] == 0 else None
        else:
            code, parent = git_output(git_root, "rev-parse", "-q", "--verify", f"{spec}^")
            earlier = parent.strip() if code == 0 else None
        problems, notes = check_from_git(git_root, spec, earlier)
    for problem in problems:
        print(problem)
    for note in notes:
        print(f"note: {note}")
    print(f"TOTAL problems: {len(problems)}")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
