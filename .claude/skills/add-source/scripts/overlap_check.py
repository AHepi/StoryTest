#!/usr/bin/env python3
"""Flag verbatim overlap between repo text and a copyrighted source.

What it does: lowers the case of both texts, evens out curly quotes and
dashes, and reports, for each repository file, every run of N or more
consecutive words (default 8) that also appears somewhere in the source,
with overlapping runs merged into one span. Only .md files are read when a
folder is given. A result of zero spans is the rule for anything committed.

Usage: overlap_check.py SOURCE.txt FILE_OR_FOLDER [...]
Set N in the environment to change the run length, e.g. N=6.
"""
import os
import re
import sys

RUN_LENGTH = int(os.environ.get("N", "8"))


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


def files_to_check(paths_given):
    file_paths = []
    for path in paths_given:
        if os.path.isdir(path):
            for folder, _, file_names in os.walk(path):
                if "/.git" in folder:
                    continue
                file_paths += [
                    os.path.join(folder, file_name)
                    for file_name in file_names
                    if file_name.endswith(".md")
                ]
        else:
            file_paths.append(path)
    return sorted(file_paths)


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
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    with open(sys.argv[1], encoding="utf-8", errors="ignore") as source_file:
        source_runs = runs_of(words_of(source_file.read()), RUN_LENGTH)
    total_spans = 0
    for file_path in files_to_check(sys.argv[2:]):
        with open(file_path, encoding="utf-8", errors="ignore") as checked_file:
            file_words = words_of(checked_file.read())
        spans = shared_spans(file_words, source_runs)
        if not spans:
            continue
        total_spans += len(spans)
        print(f"== {file_path}: {len(spans)} span(s)")
        for span_start, span_end in spans:
            print(f"   [{span_end - span_start} words] {' '.join(file_words[span_start:span_end])}")
    print(f"TOTAL spans >= {RUN_LENGTH} words: {total_spans}")


if __name__ == "__main__":
    main()
