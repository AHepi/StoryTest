#!/usr/bin/env python3
"""Check that every quotation of an owner theory in the term sheet is exact.

The term sheet (references/owner-terms.md) quotes the owner's theories
so that a reviewer can check a passage against the owner's own words. A
quotation there is text in curly quotes followed by a place in brackets
that starts with a theory's short name: Implied World, Gap, Anticipation
or Bond. For example: “The bond is a promise.” (Bond, The limits of care).

What it checks, for each quotation:
1. the words appear exactly in the theory it names (not in another one);
2. it is at most 15 words long.
Curly-quoted text with no theory place after it is reported too. Text in
straight quotes ("...") with a theory's place in brackets after it, and a
block quote (a line starting "> ") ending in such a place, are read the
same way, so a quotation cannot slip past by its quote marks. A place may
begin "from" ("(from Bond, ...)").

It prints each problem in plain words. Exit code 1 if there is any
problem, 0 if there is none.

Usage: check_owner_quotes.py [REPOSITORY_ROOT] [FILE ...]
  (default file: the term sheet)
"""
import os
import re
import sys

THEORY_FILES = {
    "Implied World": "implied-world-theory.md",
    "Gap": "gap-theory-of-narrative.md",
    "Anticipation": "anticipation-theory.md",
    "Bond": "bond-theory.md",
}
TERM_SHEET = os.path.join(".claude", "skills", "error-correction", "references", "owner-terms.md")
LONGEST_QUOTATION = 15


def check_file(sheet_path, theory_texts, shown_name):
    problems, good = [], 0
    with open(sheet_path, encoding="utf-8") as sheet_file:
        sheet = sheet_file.read()
    theory_names = "|".join(re.escape(name) for name in THEORY_FILES)
    curly = re.finditer(r"“(.*?)”(\s*\(([^)]*)\))?", sheet, flags=re.S)
    straight = re.finditer(r'"([^"\n]+)"(\s*\(((?:from )?(?:' + theory_names + r')\b[^)]*)\))', sheet)
    block = re.finditer(r'^> +"?([^\n“”]+?)"?(\s*\(((?:from )?(?:' + theory_names + r')\b[^)]*)\))\s*$', sheet, flags=re.M)
    for match in sorted(list(curly) + list(straight) + list(block), key=lambda found: found.start()):
        quotation, place = match.group(1), match.group(3) or ""
        if place.startswith("from "):
            place = place[len("from "):]
        line_number = sheet[: match.start()].count("\n") + 1
        theory = next((name for name in THEORY_FILES if place.startswith(name)), None)
        if theory is None:
            problems.append(f"{shown_name}:{line_number}: “{quotation[:60]}” has no theory named after it")
            continue
        words = [word for word in quotation.replace("*", "").split() if re.search(r"[A-Za-z0-9]", word)]
        if quotation not in theory_texts[theory]:
            found_in = [name for name in THEORY_FILES if quotation in theory_texts[name]]
            problems.append(
                f"{shown_name}:{line_number}: “{quotation[:60]}” is credited to the {theory} theory but is not"
                f" found there word for word" + (f"; it is in the {', '.join(found_in)} theory" if found_in else "")
            )
        elif len(words) > LONGEST_QUOTATION:
            problems.append(f"{shown_name}:{line_number}: a quotation of {len(words)} words; keep it to {LONGEST_QUOTATION}")
        else:
            good += 1
    return problems, good


def main():
    arguments = sys.argv[1:]
    repository_root = os.path.abspath(arguments[0] if arguments else ".")
    files = arguments[1:] or [os.path.join(repository_root, TERM_SHEET)]
    theory_texts = {}
    for name, file_name in THEORY_FILES.items():
        with open(os.path.join(repository_root, "sources", file_name), encoding="utf-8") as theory_file:
            theory_texts[name] = theory_file.read()
    problems, good = [], 0
    for path in files:
        if not os.path.exists(path):
            problems.append(f"{os.path.relpath(path, repository_root)}: missing")
            continue
        found, matched = check_file(path, theory_texts, os.path.relpath(path, repository_root))
        problems += found
        good += matched
    for problem in problems:
        print(problem)
    print(f"{good} quotations match their theory word for word")
    print(f"TOTAL problems: {len(problems)}")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
