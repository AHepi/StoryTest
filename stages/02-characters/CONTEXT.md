# Stage 02: characters

**Its one job:** build the cast the premise needs: who wants what, who opposes whom, how the hero changes (or why not), how the story argues its view through what they do, and how the audience comes to care.

The rules every stage shares are in `stages/how-stages-work.md`, and are not repeated here.

## Inputs

| Layer | File | Which part | For |
|---|---|---|---|
| 4 | `stages/01-brief-and-premise/output/<project>/project-log.md` | all | where the run stands; which versions are current |
| 4 | `stages/01-brief-and-premise/output/<project>/premise-vN.md` (highest N), and its handed-over copy | all | the premise card and the seven jobs; the writer's edits |
| 4 | `stages/01-brief-and-premise/output/<project>/brief-vN.md` (highest N), and its handed-over copy | rules, avoid list, open questions | limits on the cast; the writer's edits |
| 3 | `_config/writer.md` | questions 1, 4 and 6 | medium, voice, standing rules |
| 3 | `stages/how-stages-work.md` | all | the shared rules |
| 3 (a record) | `stages/owner-edits.md` | rows for stage 02 | patterns in the writer's edits |
| 3 | `stages/02-characters/references/cast-sheet-and-moral-line.md` | all | the cast sheet, the care plan, the order of work |
| 3 | `sources/bond-theory.md` | in full the first time in a conversation (the character skill's rule), then the ladder of care, the ten levers, principles 2, 4 and 6, and the limits of care | how care is built, and held through a harmful act |
| 3 | `.claude/skills/character/SKILL.md` | "The procedure": Building, steps 1 to 8, and Diagnosing, step 3 | the method; which levers build each rung, and the rungs for an opponent |
| 3 | `.claude/skills/character/references/building-a-character.md` | sections 4 to 9 | flaw and need, desire, ghost, values, choice |
| 3 | `.claude/skills/character/references/building-a-cast.md` | sections 1 to 9 | the cast as a whole |
| 3 | `.claude/skills/character/references/opponents.md` | sections 1 to 10 | the opponents, including a threat that is not a person (section 9) |
| 3 | `.claude/skills/character/references/change-and-growth.md` | sections 1 to 6 and 9 | the hero's change, or none |
| 3 | `.claude/skills/plot/references/premise-and-theme.md` | sections 6, 7 and 9 | theme argued through action, when it shows, the rivals |
| 3 | `.claude/skills/plot/SKILL.md` | "Traps", the trap "Letting a checklist decide" | steps fitted from books are prompts, not rules |
| 3 | `.claude/skills/dialogue/references/voice.md` | section 4 | what each would never say |
| 3 | `.claude/skills/genre/references/genres/<genre>.md` | sections 5 and 8 | the genre's usual hero and opponent, and where its care comes from |
| 3 | `.claude/skills/hard-to-vary/SKILL.md` | "The quick version" | testing a choice, lightly |
| 3 | `.claude/skills/hard-to-vary/references/by-domain.md` | section 5 | the remove and swap tests for a story choice |

## Process

1. **Read the project log, the premise and the brief,** and record any edits the writer made to them since they were handed over (`stages/how-stages-work.md`, section 8). Note the hero, the seven jobs, the story's question, and any rule that limits the cast.
2. **Fill the cast sheet** (reference, section 1): hero and main opponent first, then each other major character; a threat that is not a person follows `opponents.md`, section 9, instead of taking a row.
3. **The hero's change,** worked from the end (reference, section 3, step 2).
4. **The opponents,** each striking at the hero's flaw a different way.
5. **The moral line, with its care plan** (reference, section 2), or a note that the story's question is not a moral one. For a short work, fold or leave out steps as the reference's stopgap for owner question S17 says, naming which and why.
6. **The care plan** for each lead: which rung by which point, and what builds it (`.claude/skills/character/SKILL.md`, Building step 7).
7. **Test the load-bearing choices** with `hard-to-vary`, lightly, as the character skill's Building step 8 says: if a character's backstory, want or flaw could be swapped for another and nothing in the story changed, it is doing no work.
8. **Verify, then stop for review,** and add a project log entry.

## Outputs

In `stages/02-characters/output/<project>/`, each part with its marker (`[from: 02 step 5; cast-sheet-and-moral-line §2; bond-theory principle 2]`), and its handed-over copy (`stages/how-stages-work.md`, section 4):
- `cast-vN.md`: the cast sheet, the hero's change, the opponents, the moral line with its care plan, and the care plan for each lead.

## Verify

In `cast-vN.md`:
- **Against the premise (stage 01):** the hero's start and end match the premise card's "change or settlement" line, or the difference is marked and explained; the hero's want is the premise's desire.
- **Against the premise's question:** every major character has an answer to it on the sheet, and no two are the same.
- **Against the brief:** no rule broken, nothing from the avoid list.
- **Against the Bond theory:** for each act on the moral line that harms someone, the care plan names what holds the audience's allegiance through it (alignment, principle 2, or a balancing lever, principle 4), or says the story means to lose it there; each lead is carried by the three or four levers the character skill's Building step 3 asks for, with the ones kept low named.
- **Against the genre file:** the hero and opponent fit, or knowingly twist, the genre's usual pair (section 5 of the genre file).

## Review stop

The writer reads `cast-vN.md` and edits it in place, or asks for a rerun. Stage 03 reads the highest-numbered `cast` file. If the writer changes the premise instead, stage 02's output is stale (`stages/how-stages-work.md`, section 7).
