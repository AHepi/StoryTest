#!/bin/bash
# Start MiMo's fresh-eyes critique of one round of The Long Places in the background, then return at once.
# Usage: start_long_places_critique.sh INPUT_FOLDER FIRST_LAYOUT(1 or 0) ROUND_FOLDER
M="$(cd "$(dirname "$0")" && pwd)"
IN="$1"; FIRST="$2"; OUT="$3"
mkdir -p "$OUT"
LIST="$OUT/mimo-input-list.txt"
: > "$LIST"
for n in $(seq -w 1 14); do
  if [ "$FIRST" = "1" ]; then echo "$IN/30-chapter-$n.md" >> "$LIST"; else echo "$IN/chapter-$n.md" >> "$LIST"; fi
done
nohup python3 "$M/mimo_tasks.py" critique "$LIST" "/home/user/StoryTest/stories/the-long-places/01 Concept - in your words, with the villain added.md" "$OUT/critique-mimo.md" > "$OUT/mimo-critique.log" 2>&1 &
echo "started MiMo critique for $OUT"
