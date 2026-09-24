#!/usr/bin/env python3
"""Flag verbatim overlap between repo text and a copyrighted source.

What it does: lowers the case of both texts, evens out curly quotes and
dashes, and reports, for each repository file, every run of 8 or more
consecutive words that also appears somewhere in the source, with
overlapping runs merged into one span. When a folder is given, every text
file in it is read (Markdown, plain text, scripts and data), except in
.git and sources/raw/ (where the book copies themselves sit).

Allowed spans: titles of works, and names of authors, are allowed. They are
listed, one per line, in overlap-allowed.txt beside this script (lines
starting with # are notes on who allowed what, and when). A span is
allowed only if, once every allowed title or name inside it is taken out,
fewer than 3 words are left, counted together (a word such as "in" or
"the" on either side of a title). Allowed spans are printed but do not
count as problems.

The allowed list may hold only whole titles and whole author names from
the source register (sources/README.md): an author or a title in the
"Registered works" table, or a line under "Other titles the copying check
allows". A single word or a part of a title is refused, since common
words ("the", "story") would then drop out of every span.
`overlap_check.py --check-allowed-list REGISTER` checks that, so a phrase
from a book cannot be allowed by adding it to the list.

Exit codes, so a hook or another script can use the result:
  0  no problem spans (the rule for anything committed)
  1  one or more spans that are not allowed: rewrite them
  3  the check could not run (the source text, or a file or folder to
     check, is missing); this is never a pass: "not run" means nothing is
     known about copying

Usage: overlap_check.py [--run-length NUMBER] SOURCE.txt FILE_OR_FOLDER [...]
       overlap_check.py --check-allowed-list REGISTER [ALLOWED_LIST]
The run length can be changed by hand with --run-length (default 8); the
commit gate always uses 8, and no setting outside the command changes it.
"""
import os
import re
import sys

RUN_LENGTH = 8
TEXT_ENDINGS = (".md", ".txt", ".json", ".py", ".js", ".sh", ".html", ".csv", ".yaml", ".yml", ".xml", ".tex", ".rst")
ALLOWED_LIST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "overlap-allowed.txt")
MOST_WORDS_BESIDE_A_TITLE = 3  # a span is allowed only if fewer words than this are left outside titles and names
EXIT_PROBLEMS = 1
EXIT_NOT_RUN = 3


def words_of(text):
    text = text.replace("’", "'").replace("‘", "'")
    text = text.replace("“", '"').replace("”", '"')
    text = text.replace("—", " ").replace("–", " ")
    return re.findall(r"[a-z0-9']+", text.lower())


def runs_of(word_list, run_length):
    return {
        tuple(word_list[start:start + run_length])
        for start in range(len(word_list) - run_length + 1)
    }


def allowed_lines(allowed_list=ALLOWED_LIST):
    if not os.path.exists(allowed_list):
        return []
    with open(allowed_list, encoding="utf-8") as allowed_file:
        lines = [line.strip() for line in allowed_file]
    return [line for line in lines if line and not line.startswith("#")]


def allowed_entries(allowed_list=ALLOWED_LIST):
    return [words_of(line) for line in allowed_lines(allowed_list)]


def is_allowed(span_words, entries):
    """True if taking every allowed entry out of the span leaves fewer than MOST_WORDS_BESIDE_A_TITLE words."""
    keep = [True] * len(span_words)
    for entry in entries:
        if not entry:
            continue
        for start in range(len(span_words) - len(entry) + 1):
            if span_words[start:start + len(entry)] == entry:
                for position in range(start, start + len(entry)):
                    keep[position] = False
    return sum(keep) < MOST_WORDS_BESIDE_A_TITLE


def registered_titles_and_authors(register_path):
    """Word lists of every author and title the register names, and every line under 'Other titles'."""
    with open(register_path, encoding="utf-8") as register_file:
        register = register_file.read()
    names = []
    works = register.split("## Registered works", 1)[-1].split("\n## ", 1)[0]
    for row in re.findall(r"^\| ([^|]+) \|", works, flags=re.M):
        author, _, title = row.partition(",")
        title = title.replace("*", "").strip()
        names += [author, title, title.split(":", 1)[0]]  # a title may also be given without its subtitle
    other = re.search(r"^## Other titles the copying check allows\s*$(.*?)(?=^## |\Z)", register, flags=re.M | re.S)
    if other:
        names += re.findall(r"^- \*([^*]+)\*", other.group(1), flags=re.M)
    return [" ".join(words_of(name)) for name in names if words_of(name)]


def check_allowed_list(register_path, allowed_list=ALLOWED_LIST):
    """Problems with the allowed list: any line that is not an author or title (or part of one) in the register."""
    known = registered_titles_and_authors(register_path)
    problems = []
    for line in allowed_lines(allowed_list):
        phrase = " ".join(words_of(line))
        if phrase not in known:
            problems.append(f"{os.path.basename(allowed_list)}: '{line}' is not a whole author name or title named in"
                            f" {os.path.basename(os.path.dirname(register_path))}/README.md; only whole titles and names"
                            " may be allowed")
    return problems


def files_to_check(paths_given):
    """(the files to read, every one with a text ending in TEXT_ENDINGS, and the paths given that do not exist)."""
    file_paths, missing = [], []
    for path in paths_given:
        if os.path.isdir(path):
            for folder, folder_names, file_names in os.walk(path):
                folder_names[:] = [name for name in folder_names if name != ".git"
                                   and os.path.join(folder, name).replace(os.sep, "/").split("/")[-2:] != ["sources", "raw"]]
                file_paths += [os.path.join(folder, file_name) for file_name in file_names
                               if file_name.lower().endswith(TEXT_ENDINGS)]
        elif os.path.exists(path):
            file_paths.append(path)
        else:
            missing.append(path)
    return sorted(file_paths), missing


def shared_spans(file_words, source_runs):
    """Return (start, end) word positions of maximal runs shared with the source."""
    matching_starts = [
        start
        for start in range(len(file_words) - RUN_LENGTH + 1)
        if tuple(file_words[start:start + RUN_LENGTH]) in source_runs
    ]
    if not matching_starts:
        return []
    spans = []
    span_start, span_end = matching_starts[0], matching_starts[0] + RUN_LENGTH
    for start in matching_starts[1:]:
        if start <= span_end:
            span_end = start + RUN_LENGTH
        else:
            spans.append((span_start, span_end))
            span_start, span_end = start, start + RUN_LENGTH
    spans.append((span_start, span_end))
    return spans


def main():
    global RUN_LENGTH
    if sys.argv[1:2] == ["--run-length"]:
        RUN_LENGTH = int(sys.argv[2])
        del sys.argv[1:3]
    if sys.argv[1:2] == ["--check-allowed-list"]:
        problems = check_allowed_list(sys.argv[2], *(sys.argv[3:4]))
        for problem in problems:
            print(problem)
        print(f"TOTAL problems: {len(problems)}")
        sys.exit(EXIT_PROBLEMS if problems else 0)
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    source_path = sys.argv[1]
    if not os.path.exists(source_path):
        print(f"NOT RUN: the source text {source_path} is not here, so nothing is known about copying from it.")
        print("Books are kept only as local copies in sources/raw/. Do not commit text drawn from this book until the check has run.")
        sys.exit(EXIT_NOT_RUN)
    with open(source_path, encoding="utf-8", errors="ignore") as source_file:
        source_runs = runs_of(words_of(source_file.read()), RUN_LENGTH)
    entries = allowed_entries()
    file_paths, missing = files_to_check(sys.argv[2:])
    if missing:
        print(f"NOT RUN: {', '.join(missing)} is not here, so nothing is known about copying in it.")
        sys.exit(EXIT_NOT_RUN)
    problem_spans = 0
    for file_path in file_paths:
        with open(file_path, encoding="utf-8", errors="ignore") as checked_file:
            file_words = words_of(checked_file.read())
        spans = shared_spans(file_words, source_runs)
        if not spans:
            continue
        print(f"== {file_path}: {len(spans)} span(s)")
        for span_start, span_end in spans:
            span_words = file_words[span_start:span_end]
            if is_allowed(span_words, entries):
                label = "allowed (title or name)"
            else:
                label = "PROBLEM"
                problem_spans += 1
            print(f"   [{span_end - span_start} words, {label}] {' '.join(span_words)}")
    print(f"TOTAL problem spans >= {RUN_LENGTH} words: {problem_spans}")
    sys.exit(EXIT_PROBLEMS if problem_spans else 0)


if __name__ == "__main__":
    main()
