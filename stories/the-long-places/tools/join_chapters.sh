#!/bin/bash
# Join the fourteen chapter files of one revision of The Long Places into one document, in order,
# so that a single reviewer can read the whole revision as one file.
# Usage: join_chapters.sh FOLDER OUTPUT_FILE
IN="$1"; OUT="$2"
: > "$OUT"
for n in $(seq -w 1 14); do
  cat "$IN/chapter-$n.md" >> "$OUT"
  printf '\n\n' >> "$OUT"
done
echo "joined $(wc -w < "$OUT") words into $OUT"
