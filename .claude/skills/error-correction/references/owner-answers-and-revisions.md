# Owner answers, revisions, and premises that fail

Open this when the owner answers a question, when an owner theory is revised, when a check, brief or reviewer is found to have been broken, or when a frozen text itself seems to be wrong.

Contents: 1 What losing a licence means. 2 An owner answer. 3 A revised theory. 4 A frozen text that seems wrong. 5 A check, brief or reviewer found broken. 6 Traps.

## 1. What losing a licence means

**Case.** The map checker was found to miss five of six planted faults. Every "Map check: 0 problems" recorded since log entry 17 had rested on it.

**Point.** A passage, a record or a verdict is usable only while everything it rests on still stands, and only within its scope: the question it was made for. When a premise is withdrawn, what rests on it loses its licence: it may not be relied on until it has been rechecked. It does not become false. The old "0 problems" results were not wrong, just unsupported, and rerunning the repaired checker rechecked them (foundation, Part IX, K2: a passage is usable only with its licence, within its scope, while its premises are live; withdrawing a premise removes the licence, not the truth). A passage used outside the question it was made for has no licence there either, even when every premise stands. The same holds for a skill passage resting on a stopgap reading, when the owner answers the question behind it.

## 2. An owner answer

1. **Record the answer** in the questions file (`22 Questions - meanings only you can settle.md`) under its question, in the owner's own words and with the date, as a line "**Answer (date):** ..." after the question's text; where the question's own wording says it is put to the owner, leave it as it was asked. Set the question's status to `rechecking`. The records check then reports it as being rechecked, rather than failing every passage that cites it.
2. **Find every passage that rests on it:**
   - passages that cite the question's number: `grep -rn "Q<n>" .claude/skills`, with the question's own number for `Q<n>` (the records check lists them too: as problems once the question is answered, as notes while it is being rechecked). Search the skills only, never `kept-cases/`: an agent that changes the skills never reads the kept cases, or the cases turn into an answer key. The records check names the kept cases that cite the question, by file and line only, while it is being rechecked and once it is answered;
   - passages labelled as the workshop's reading on the same point, which may carry no number: `grep -rn -i "workshop's reading\|stopgap\|put to the owner\|workshop stretches\|workshop's extension" .claude/skills`, then read each hit for the point in question;
   - passages that restate the reading in other words: search for the question's key terms.
3. **Recheck each passage** against the answer, and rewrite it to state the answer as the owner's meaning: take out "a question put to the owner" and any stopgap the answer settles, and write "answered" right after that question's number, inside the same brackets (for example "(owner question Q<n>, answered 30 Sep: option b)"); on a line that rests on two questions, do it for each. Where it must change further, change it through the loop. This changes meaning even for a passage that already followed the answer, since a reading becomes the owner's settled meaning, and drift from the owner's meaning is the workshop's commonest error: theory-checker compares each changed passage with the owner's words before its receipt is written (the review can be short), and the kept cases for its skill are rerun. It never takes a light receipt or the typo route.
   - **A kept case** that the records check names is not changed: it stays as it was run. A new case that grades the answered point is written by an agent that has not read the skills, given the case's file name and the owner's answer, in a commit separate from the skill changes (`checks-and-cases.md`, section 6).
4. **Close it.** When no passage rests on the old stopgap, set the status to `answered`. The records check will now fail any passage that cites the question without saying it was answered.
5. **Log it** in the project story: the answer, the passages changed, and the correction number if one was opened.

**Readings the owner has not seen.** About a hundred passages carry "the workshop's reading" and have no question behind them. When you touch a section for another reason, list its readings, marked *held if* the reading stands, and add them in batches to the questions file, so the owner sees them. Do not mass-edit the skills to do it.

## 3. A revised theory

The add-source skill, Step 3, stores the revision. Then:
1. List what the revision changes: principles added, removed, reworded or renumbered.
2. Every passage that cites a changed principle, or restates its claim in other words, loses its licence. Find them by the principle's name and number and by its key words.
3. Recheck and change them through the loop, as for an owner answer. Citations of renumbered principles are updated.
4. Where the old and new versions disagree about something the revision does not mention, leave the passage alone and put it to the owner as a question.

## 4. A frozen text that seems wrong

A frozen text (`foundations/`, and the owner theories in `sources/`) is never edited, not even to fix a typo. The edit hook refuses it and the fingerprint check catches any other route. But the owner's own theories can be wrong: their foundation says so of itself, and lists what would refute it. If a theory gives a wrong verdict on a real case, or none, or contradicts another theory:
- record it as a correction, with the case, the passage and the connection;
- put it to the owner as a question;
- until the owner decides, the skills follow the theory and label the problem where it bites. The rule "never contradict the theory" governs how skills are written. It does not govern whether a failure is recorded, and hiding a counter-case to protect a theory is itself an error.

## 5. A check, brief or reviewer found broken

When a check turns out to have passed faults, or a brief or a reviewer turns out to have carried an error:
1. Name what rested on it: records of the check passing, files written from the brief, findings from the reviewer. Name them by log entry, commit or receipt.
2. Add a log entry that withdraws their licence. Do not rewrite the old records.
3. Recheck what can be rechecked (rerun the corrected check; review the files written from the brief) and record the result.
4. Correct the check, brief or reviewer through the loop. Its planted faults, or a planted fault for the reviewer, show the correction works.

## 6. Traps

- **Treating a withdrawn premise as proof of the opposite.** The passage has lost its licence; it has not been shown false.
- **Searching only for the question's number.** Readings restated in other words carry no number.
- **Settling a question for the owner.** An answer inferred from what the owner "would probably want" is the workshop choosing the input. Ask.
- **Editing a frozen text because it is plainly wrong.** Record it, and ask.
