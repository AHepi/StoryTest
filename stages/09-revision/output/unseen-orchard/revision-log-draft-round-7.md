# Revision log: draft, round 7 (critique round 5 → draft 8)

*Stage 09, round 7. Target: `draft-v7-part1.md` to `part3.md`. Findings: `stages/08-critique/output/unseen-orchard/critique-draft-round-5-fix-check.md` (the fix check: 24 of 25 round-4 findings done, SV9 partly; 12 new problems, here FC1 to FC12) and `critique-draft-round-5-second-reader.md` (a second cold reader: SR1 to SR10). Feedback 3: the workshop decides. New version: `draft-v8-part1.md` to `part3.md`. [from: 09 steps 1 to 7; revision-log §1]*

## The fix check

| Problem | Verdict | What was done |
|---|---|---|
| FC1 Tomas's reason for the outstation cut (unlogged) | Accepted | The writer's sentence back: "He had chosen that position to control a store and the households held with it." |
| FC2 the sign of the lie repeats the writer's spectacles | Accepted | "She glanced at the guard by the door." |
| FC3 frames "once the boarders were across" contradicts A's burn report | Accepted | "for carrying news between the sides" |
| FC4 FR5 recorded both ways | Accepted | Recorded here: FR5 was decided for "matched" (the crossing checks found her as she had been), so the voice in ch. 10 is not the reversal. `world-v3.md` §11 item 4's "the swapped halves of the lore" is withdrawn by this line (the file is kept as committed; this log corrects it) |
| FC5 "its fabrication owners" points to Serrat | Accepted | "the old claims of Nearbank's fabrication owners on the people who worked for them. The claims had been disputed for years." |
| FC6 "what to do" uses up the writer's ch. 10 line | Accepted | SV's wording back: "where to put her hands" |
| FC7 the orchard story's opening repeats ch. 7's | Accepted | "He said, without looking at her, ..."; "The fruit came right for neither side." |
| FC8 "did not answer" twice (unlogged line) | Accepted | "The pilot did not answer at once." cut |
| FC9 the limit on Tomas's command cut (unlogged) | Accepted | The writer's sentences back: "within the charter and her instructions", "civilian supplies, accommodation" |
| FC10 SV9(b) half done | Accepted | The writer's "Nessa followed the fuel commitments down the page and found the tug" back |
| FC11 "as if" and "the way" similes | Accepted | Four "as if" to the writer's "as though"; ch. 3: "She glanced at the bird as she passed it."; "as easily as people at home said safe travels" |
| FC12 the round 6 log's counts | Accepted | Recounted below, story text only, by a script that skips headings, file notes and scene-break lines; it gives the fix check's figures. The round 6 log is kept as written; this table corrects it |

The fix check's other notes: the six unlogged changes in round 6 are FC1, FC8, FC9 and three it judged harmless (Orra's line on the family's interest, cut when the war line went in; "Not as a mirror would:" joined to its sentence; the *Patience* paragraph reworded and split). They are logged here.

## The second reader

| Finding | Verdict | What was done |
|---|---|---|
| SR1 frame logistics as a brief, then sums | Accepted in part | Ch. 9: the shop's purpose given in one line ("Every crossing the occupation made was serviced there."). Ch. 10's sums are the writer's and stay: the first reader of round 4 tested the same point and dropped it ("the sums are what make it a real dilemma") |
| SR2 terms between "Tomas was not in the report" and Tomas | Accepted (trim; order kept) | Ch. 11's terms cut to two sentences; the wait is kept, since it is the writer's order |
| SR3 ch. 5 opens on people the reader cannot place | Accepted | Two clauses: Orra "who ran her House's purchasing from Surety"; the man on the screen "an older man of her House" |
| SR4 the outstation not placed; the plan in shorthand | Accepted in part | FC1's restored sentence places the outstation; the plan is the writer's dialogue and stays |
| SR5 the shop's purpose told late; "cartridges" | Accepted | As SR1; ch. 4: "the crossing cartridges" |
| SR6 Tomas's question about the pilot | Kept (held; decided) | Kept, with FC2's sign. The writer asked for people lost in a collapsed identity who go looking; Tomas, stripped of the orchard and his command, asking where the seeker went is that, left unanswered |
| SR7 "repinned" | Rejected | The writer's word, from the trade; it reads in context ("She had repinned on Wren's side" after "She was in space") |
| SR8 ch. 1's ship section | Rejected | The writer's own chapter, untouched by every revision; not part of what was asked |
| SR9 the last gesture staged two ways | Rejected (as round 6) | The writer's sentence, kept exactly |
| SR10 "He changed one more time" | Rejected | The writer's sentence, as in the PDF; it may mean the interval was changed once more. Not a revision's to correct |

## The middle, measured (story text only)

| Chapters 5 to 9 | Draft 1 (the writer's) | Draft 6 | Draft 7 | Draft 8 |
|---|---|---|---|---|
| Words | 5,338 | 4,846 | 5,558 | 5,605 |
| Paragraphs | 311 | 227 | 324 | 323 |
| Words per paragraph | 17.2 | 21.3 | 17.2 | 17.4 |
| Paragraphs of 60 words or more | 6 | 10 | 3 | 3 |

(Script: `count_middle.sh` in the session's scratch folder, an `awk` count; not committed.) Draft 8's middle is 5% longer than the writer's. The two cold readers on how it reads: round 4, of draft 6, "The middle's cost is murk, not slowness"; round 5, of draft 7, "dense but alive. Nearly every stretch of paperwork ends in a signature or a refusal that costs someone something". The writer's word was "dense"; the paperwork that made it so is cut, and the length went to people and to the layer the writer asked for. Whether that answers "too dense" is the writer's to judge on reading.

## Verify

- **Every finding answered:** 12 + 10 rows; *agrees*.
- **Only the logged changes:** the maker's own `diff` of draft 7 and draft 8; not checked again by another agent. The changes are single phrases or sentences, each named by a checker.
- **The writer's last sentence:** `diff` of the last line of draft 1 and draft 8 printed nothing.
- **"as if", "the way" similes, straight quotes, italics in draft 8:** `grep` found none.
