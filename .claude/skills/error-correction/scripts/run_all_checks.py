#!/usr/bin/env python3
"""Run every machine check the workshop has, and give one plain summary.

The checks:
- frozen files: no frozen file changed, every frozen file listed, the list
  only added to (check_frozen_files.py);
- maps: every module on its skill's map, every path and section pointer
  lands, shared passages identical (add-source/scripts/check_maps.py);
- records: the log only added to, status lines current, README complete,
  owner questions and corrections numbered with a status, write-ups carry
  the checks run on them (check_records.py);
- owner quotes: every quotation of an owner theory in the term sheet is
  word for word, and credited to the right theory (check_owner_quotes.py);
- no book files: nothing under sources/raw/, no ebook file, and no text
  file over 100,000 bytes anywhere in the files checked, of any kind, the
  workshop's own kept records included, except the one record named in
  LARGE_RECORDS_ALLOWED, and only while its contents still match the
  fingerprint given there (it was written before the limit covered kept
  records; later kept-case runs are kept one file per case);
- hooks registered: .claude/settings.json still tells Claude Code to run
  the workshop's four hooks: session_start.py when a session starts,
  resumes or is compacted, protect_frozen_files.py before every file edit
  (Edit, Write, MultiEdit and NotebookEdit), refuse_check_bypass.py before
  every shell command, and after_commit.py after every shell command, and
  does not switch all hooks off ("disableAllHooks"). A matcher is read as
  Claude Code reads it: empty or "*" covers everything, otherwise it is a
  pattern the tool's name must match. Without them the gate is not switched
  on in a fresh copy and nothing stands in front of the frozen files. What
  it cannot see: settings kept outside the repository, such as the local
  settings file beside settings.json or a person's own settings, which can
  switch hooks off too;
- allowed titles: the copying check's allowed list holds only authors and
  titles named in the source register (overlap_check.py
  --check-allowed-list). With --against, the register is read as it was in
  that commit, so a title newly added to the register is copy-checked with
  the old list before it can go on the list;
- copying from books: overlap_check.py against every book text, reading
  every text file in the files checked (the endings in TEXT_ENDINGS). Books are local copies only, so in
  most sessions this cannot run; it is then reported as NOT RUN, never as
  passed.

Each check is reported as passed, FAILED, NOT RUN (books absent), or
COULD NOT RUN (the check script itself broke, for example with a Python
error). The exit code is 1 if any check failed or could not run, 0
otherwise. NOT RUN does not fail the run, but it is printed, because
nothing is known about what an unrun check would find.

The checks are taken from this script's own folder and the add-source
skill's scripts folder beside it, not from the files being checked. The
commit gate uses that to run the last approved commit's checks on the staged files.

Usage: run_all_checks.py [--skip-books] [--staged] [--git-root PATH] [--against COMMIT]
                         [--also-against COMMIT]... [--books-from FOLDER] [REPOSITORY_ROOT]
  REPOSITORY_ROOT  the files to check (default: the current folder); the
                   commit gate passes a copy of exactly what is staged
  --git-root       where the git history is, if not REPOSITORY_ROOT
  --books-from     where the book texts are (default: REPOSITORY_ROOT/sources/raw)
  --staged         the files are a copy of what is staged: the frozen check
                   then reads the frozen files from git's staged copy itself
  --against        the commit the log, the frozen list and the register are
                   compared with (default: the last commit); the commit gate
                   passes the last commit it approved
  --also-against   (for a merge; may be given more than once) the commit
                   being merged in: the log entries it added since the two
                   lines of work split must be kept, by number and text
"""
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CRASHED = re.compile(r"^(Traceback \(most recent call last\)|\w*(Error|Exception)\b)", re.M)  # Python's own report of a broken script
BOOK_ENDINGS = (".epub", ".azw3", ".azw", ".mobi", ".pdf", ".kfx")
TEXT_ENDINGS = (".md", ".txt", ".json", ".py", ".js", ".sh", ".html", ".csv", ".yaml", ".yml", ".xml", ".tex", ".rst")
LARGE_RECORDS_ALLOWED = {  # path: the fingerprint (SHA-256) its contents must still have
    "kept-cases/runs/2026-09-24-before-entry-27.md": "1d14c95d8365bc59c10522c38d62813458d3b78647cdd038fa2f26ad131be5f9",
}
HOOKS_NEEDED = (  # (the moment, what its matcher must cover (a tool, or how a session began), the hook script)
    ("SessionStart", "startup", "session_start.py"),
    ("SessionStart", "resume", "session_start.py"),
    ("SessionStart", "compact", "session_start.py"),
    ("PreToolUse", "Edit", "protect_frozen_files.py"),
    ("PreToolUse", "Write", "protect_frozen_files.py"),
    ("PreToolUse", "MultiEdit", "protect_frozen_files.py"),
    ("PreToolUse", "NotebookEdit", "protect_frozen_files.py"),
    ("PreToolUse", "Bash", "refuse_check_bypass.py"),
    ("PostToolUse", "Bash", "after_commit.py"),
)
LARGE_TEXT = 100_000  # bytes; the book texts run to hundreds of thousands


def run_script(arguments, repository_root):
    """(exit code, output); exit code 2 means the script could not run."""
    try:
        result = subprocess.run(
            [sys.executable] + arguments, cwd=repository_root, capture_output=True, text=True, check=False,
            timeout=600,
        )
    except (OSError, subprocess.TimeoutExpired) as problem:
        return 2, f"could not run: {problem}"
    code = result.returncode
    if code not in (0, 1, 3) or CRASHED.search(result.stderr) or (code in (0, 1) and "TOTAL" not in result.stdout):
        code = 2  # it broke, or ended without its closing TOTAL line, so it did not really run
    return code, (result.stdout + result.stderr).strip()


def verdict_for(code):
    return {0: "passed", 1: "FAILED", 3: "NOT RUN"}.get(code, "COULD NOT RUN")


def files_that_could_be_committed(repository_root):
    """Every file git would take: tracked, plus new files it does not ignore. In a copy of the
    staged files (which has no .git folder) that is simply every file."""
    if os.path.isdir(os.path.join(repository_root, ".git")) or os.path.isfile(os.path.join(repository_root, ".git")):
        listed = subprocess.run(
            ["git", "-C", repository_root, "ls-files", "--cached", "--others", "--exclude-standard"],
            capture_output=True, text=True, check=False,
        ).stdout.splitlines()
        return [os.path.normpath(path) for path in listed if path]
    paths = []
    for folder, folder_names, file_names in os.walk(repository_root):
        folder_names[:] = [name for name in folder_names if name != ".git"]
        relative_folder = os.path.relpath(folder, repository_root)
        paths += [os.path.normpath(os.path.join(relative_folder, file_name)) for file_name in file_names]
    return paths


def allowed_large_record(full_path, relative_path):
    """True only for a record named in LARGE_RECORDS_ALLOWED whose contents still match its fingerprint. Line
    endings are read as git stores them, so a Windows copy, whose files end their lines differently, matches too."""
    if relative_path not in LARGE_RECORDS_ALLOWED:
        return False
    with open(full_path, "rb") as record:
        contents = record.read().replace(b"\r\n", b"\n")
    return hashlib.sha256(contents).hexdigest() == LARGE_RECORDS_ALLOWED[relative_path]


def matcher_covers(matcher, name):
    """Whether a hook's matcher covers a tool or a way a session began, read as Claude Code reads it."""
    if matcher in ("", "*"):
        return True
    try:
        return re.fullmatch(matcher, name) is not None
    except re.error:
        return matcher == name


def hooks_not_registered(repository_root):
    """The workshop's hooks that .claude/settings.json no longer registers, each as a sentence."""
    path = os.path.join(repository_root, ".claude", "settings.json")
    try:
        with open(path, encoding="utf-8") as settings_file:
            settings = json.load(settings_file)
        hooks = settings.get("hooks", {}) or {}
    except (OSError, ValueError, AttributeError) as problem:
        return [f".claude/settings.json: could not be read ({problem})"]
    missing = []
    if settings.get("disableAllHooks"):
        missing.append(".claude/settings.json: \"disableAllHooks\" switches every hook off, the workshop's included")
    for moment, tool, script in HOOKS_NEEDED:
        found = False
        for group in hooks.get(moment, []) or []:
            matcher = group.get("matcher", "") or ""
            covers = matcher_covers(matcher, tool)
            commands = " ".join(hook.get("command", "") for hook in group.get("hooks", []) or [])
            found = found or (covers and f".claude/hooks/{script}" in commands)
        if not found:
            where = f"{moment} for {tool}"
            missing.append(f".claude/settings.json: no {where} hook runs .claude/hooks/{script}")
    return missing


def book_files(repository_root):
    found = []
    for relative_path in files_that_could_be_committed(repository_root):
        file_name = os.path.basename(relative_path)
        full_path = os.path.join(repository_root, relative_path)
        if not os.path.exists(full_path):
            continue
        if relative_path.startswith(os.path.join("sources", "raw") + os.sep):
            found.append(f"{relative_path}: book copies in sources/raw/ are never committed")
        elif file_name.lower().endswith(BOOK_ENDINGS):
            found.append(f"{relative_path}: an ebook or PDF file; books are never committed")
        elif (file_name.lower().endswith(TEXT_ENDINGS) and os.path.getsize(full_path) > LARGE_TEXT
              and not allowed_large_record(full_path, relative_path.replace(os.sep, "/"))):
            found.append(f"{relative_path}: a large text file; if it is a book, it must not be committed")
    return found


def main():
    arguments = sys.argv[1:]
    skip_books = "--skip-books" in arguments
    staged = "--staged" in arguments
    arguments = [argument for argument in arguments if argument not in ("--skip-books", "--staged")]
    git_root = books_folder = against = None
    also_against = []
    while arguments[:1] and arguments[0] in ("--git-root", "--books-from", "--against", "--also-against"):
        if arguments[0] == "--git-root":
            git_root = os.path.abspath(arguments[1])
        elif arguments[0] == "--against":
            against = arguments[1]
        elif arguments[0] == "--also-against":
            also_against.append(arguments[1])
        else:
            books_folder = os.path.abspath(arguments[1])
        arguments = arguments[2:]
    repository_root = os.path.abspath(arguments[0] if arguments else ".")
    git_root = git_root or repository_root
    books_folder = books_folder or os.path.join(repository_root, "sources", "raw")
    add_source_scripts = os.path.join(os.path.dirname(os.path.dirname(HERE)), "add-source", "scripts")
    results = []

    for label, command in (
        ("frozen files", [os.path.join(HERE, "check_frozen_files.py"), "--git-root", git_root]
         + (["--against", against] if against else []) + (["--index"] if staged else []) + [repository_root]),
        ("maps", [os.path.join(add_source_scripts, "check_maps.py"), repository_root]),
        ("records", [os.path.join(HERE, "check_records.py"), "--git-root", git_root]
         + (["--against", against] if against else [])
         + [option for commit in also_against for option in ("--also-against", commit)] + [repository_root]),
        ("owner quotes", [os.path.join(HERE, "check_owner_quotes.py"), repository_root]),
    ):
        code, output = run_script(command, repository_root)
        results.append((label, verdict_for(code), output))

    register = os.path.join(repository_root, "sources", "README.md")
    earlier_register = None
    if against:
        shown = subprocess.run(["git", "-C", git_root, "show", f"{against}:sources/README.md"],
                               capture_output=True, text=True, check=False)
        if shown.returncode == 0:
            earlier_register = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8")
            earlier_register.write(shown.stdout)
            earlier_register.close()
            register = earlier_register.name
    code, output = run_script([os.path.join(add_source_scripts, "overlap_check.py"), "--check-allowed-list",
                               register,
                               os.path.join(repository_root, ".claude", "skills", "add-source", "scripts",
                                            "overlap-allowed.txt")], repository_root)
    if earlier_register:
        os.remove(earlier_register.name)
        output = output.replace(f"{os.path.basename(os.path.dirname(earlier_register.name))}/README.md",
                                f"sources/README.md as it was in {against[:9]}")
    results.append(("allowed titles", verdict_for(code), output))

    found = book_files(repository_root)
    results.append(("no book files", "FAILED" if found else "passed", "\n".join(found)))

    missing = hooks_not_registered(repository_root)
    results.append(("hooks registered", "FAILED" if missing else "passed", "\n".join(missing)))

    books = sorted(glob.glob(os.path.join(books_folder, "*.txt")))
    if skip_books:
        results.append(("copying from books", "NOT RUN", "skipped on request (--skip-books)"))
    elif not books:
        results.append(("copying from books", "NOT RUN",
                        "no book text here; the review receipt must say what book text a change adds"))
    else:
        codes, outputs = [], []
        for book in books:
            code, output = run_script([os.path.join(add_source_scripts, "overlap_check.py"), book, "."],
                                      repository_root)
            if code != 0:
                codes.append(code)
                outputs.append(f"-- {os.path.basename(book)}\n{output}")
        worst = next((code for code in (2, 1, 3) if code in codes), 0)  # could not run, then failed, then not run
        results.append(("copying from books", verdict_for(worst),
                        "\n".join(outputs) or f"0 problem spans against {len(books)} book(s)"))

    any_failed = False
    for label, verdict, output in results:
        print(f"{verdict:8}  {label}")
        in_note = False
        for line in output.splitlines():
            in_note = line.startswith("note:") or (in_note and line.startswith("    "))
            if line.startswith("TOTAL") or (verdict == "passed" and not in_note):
                continue
            print(f"          {line}")
        any_failed = any_failed or verdict in ("FAILED", "COULD NOT RUN")
    print("RESULT: " + ("some checks FAILED" if any_failed else "no check failed"))
    sys.exit(1 if any_failed else 0)


if __name__ == "__main__":
    main()
