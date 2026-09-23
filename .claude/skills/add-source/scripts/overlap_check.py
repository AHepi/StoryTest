#!/usr/bin/env python3
"""Flag verbatim overlap between repo text and a copyrighted source.

Usage: overlap_check.py SOURCE.txt FILE_OR_DIR [...]
Reports, per file, every run of >= N consecutive words (default 8) that also
appears in SOURCE, merged into maximal spans.
"""
import os
import re
import sys

N = int(os.environ.get("N", "8"))


def words(text):
    text = text.replace("’", "'").replace("‘", "'")
    text = text.replace("“", '"').replace("”", '"')
    text = text.replace("—", " ").replace("–", " ")
    return re.findall(r"[a-z0-9']+", text.lower())


def grams(ws, n):
    return {tuple(ws[i:i + n]) for i in range(len(ws) - n + 1)}


def main():
    src = words(open(sys.argv[1], encoding="utf-8", errors="ignore").read())
    src_grams = grams(src, N)
    paths = []
    for p in sys.argv[2:]:
        if os.path.isdir(p):
            for root, _, files in os.walk(p):
                if "/.git" in root:
                    continue
                paths += [os.path.join(root, f) for f in files if f.endswith(".md")]
        else:
            paths.append(p)
    total = 0
    for path in sorted(paths):
        ws = words(open(path, encoding="utf-8", errors="ignore").read())
        hits = [i for i in range(len(ws) - N + 1) if tuple(ws[i:i + N]) in src_grams]
        if not hits:
            continue
        spans, start, end = [], hits[0], hits[0] + N
        for i in hits[1:]:
            if i <= end:
                end = i + N
            else:
                spans.append((start, end))
                start, end = i, i + N
        spans.append((start, end))
        total += len(spans)
        print(f"== {path}: {len(spans)} span(s)")
        for s, e in spans:
            print(f"   [{e - s} words] {' '.join(ws[s:e])}")
    print(f"TOTAL spans >= {N} words: {total}")


if __name__ == "__main__":
    main()
