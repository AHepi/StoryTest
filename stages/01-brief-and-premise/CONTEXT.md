# Stage 01: brief and premise

**Its one job:** turn the writer's request into a brief the whole run can build on, write rival premises, and choose one with the writer. When the writer brings their own premise or draft, this stage writes the brief and takes that in instead of writing rivals.

The rules every stage shares (versions, markers, the Verify section, review stops, helpers, the project log) are in `stages/how-stages-work.md`, and are not repeated here.

## Inputs

Load these, and nothing else. *Layer 3* is reference, to follow as rules; *Layer 4* is this project's material, to work on.

| Layer | File | Which part | For |
|---|---|---|---|
| 4 | the writer's request, as given, with everything attached | all | what is asked |
| 4 | `stages/01-brief-and-premise/output/<project>/project-log.md` | all, once it exists | where the run stands |
| 4 | `stages/08-critique/output/<project>/critique-pitches-round-N-*.md` (only after step 6) | all | the reviews of the rivals, for the choice |
| 4 | `stages/09-revision/output/<project>/` (only when starting again after the writer's feedback) | the latest feedback file, and the latest revision log | what changed and why |
| 3 | `_config/writer.md` | all | standing preferences |
| 3 | `_config/questionnaire.md` | the questions with no answer yet | what to ask |
| 3 | `stages/how-stages-work.md` | all | the shared rules |
| 3 (a record) | `stages/owner-edits.md` | rows for stage 01 | patterns in the writer's edits |
| 3 | `stages/01-brief-and-premise/references/premise-worksheet.md` | all | the order of work, the brief, the card |
| 3 | `CLAUDE.md` | the line on taking a request from the owner | saying the request back |
| 3 | `.claude/skills/plot/references/premise-and-theme.md` | sections 1 to 7 and 9 | premise line, claim, the world's question, designing principle, the final choice, who learns what, the rivals |
| 3 | `.claude/skills/plot/references/structure-and-conflict.md` | section 2 | the seven jobs, for the chosen premise |
| 3 | `.claude/skills/plot/SKILL.md` | "The procedure", Building, steps 2 and 3 | the normal, the breach and the story, for the seven jobs |
| 3 | `.claude/skills/genre/SKILL.md` | "Built on", and "The procedure", Building, steps 1 to 4 | naming the genre and what it promises |
| 3 | `.claude/skills/genre/references/how-genres-work.md` | sections 2, 4, 5 and 8 | promises and guarantees, the genre's question, the twelve genres, blends |
| 3 | `.claude/skills/genre/references/genres/<genre>.md` | sections 1 to 4, 7, 10 and 11, for each genre a rival uses | its promise, baseline, guarantees, question, subgenres and blends, twists |
| 3 | `sources/gap-theory-of-narrative.md` | in full the first time in a conversation (the plot skill's rule), then principles 2, 5 and 7, Part 2 sections 4 and 6, and the five questions | the normal, the breach, promises, the settlement |
| 3 | `sources/implied-world-theory.md` | Part 2 sections 1 and 2, and for Horror or Fantasy section 3 (the genre skill's rule) | the baseline and departures |
| 3 | `sources/anticipation-theory.md` | principles 1, 5 and 6 and Part 2 sections 1, 5 and 6, and for Horror or Fantasy principles 3 and 8 and Part 2 sections 3 and 8 (the genre skill's rule) | guarantees, and care before the threat |
| 3 | `sources/bond-theory.md` | the ten levers and principle 4 (the genre skill's rule) | which levers a genre's hero runs on |
| 3 | `.claude/skills/character/references/building-a-cast.md` | section 12, its last rival, and section 11, its test | whose story to tell |
| 3 | `.claude/skills/character/references/building-a-character.md` | section 4 | the two kinds of flaw |
| 3 | `.claude/skills/character/references/change-and-growth.md` | section 9 | when the hero does not change |

## Process

1. **Read the settings.** Read `_config/writer.md`. If a question in `_config/questionnaire.md` has no answer and this project needs one (the medium, usually), ask it, with a suggested answer, and write the answer in. An answer still marked *to confirm* is a stopgap (owner question S16): the first time it would decide something in this run (how many helpers or critics to start, a standing rule on what a story may do), say it back to the writer and wait for their word before starting any helper.
2. **Say the request back,** as the line on taking a request from the owner in `CLAUDE.md` asks: what is asked, what is not, and the nearest other reading. When that line's signs say the reading is in doubt, follow it: ask which is meant, and do nothing risky, costly or hard to undo on any reading until the writer answers.
3. **Save the request** word for word as `request.md`, listing each attachment and whether it may be committed, and start `project-log.md` with its first entry.
4. **Write the brief,** `brief-v1.md`, in the order of the worksheet's section 2.
5. **Write the rivals,** `pitches-v1.md`: as many as `_config/writer.md` says, each filling the card in the worksheet's section 3, with sections 4 to 6. When helpers write them, each gets the brief, the worksheet, and the files the card cites (the Inputs rows for the Gap theory, `premise-and-theme.md`, the genre skill and its files, and `building-a-cast.md`), starts from a different kind of story (the worksheet's section 3), and sees no other rival.
   **If the writer brings their own premise,** save it as `premise-v1.md`, fill in only the card's lines it leaves open, marked as the workshop's suggestions for the writer to accept or strike, and go on to step 7's seven jobs. **If they bring a draft,** save it as `stages/07-dialogue/output/<project>/draft-v1.md` (split as `stages/how-stages-work.md`, section 4, says), keep step 4's brief to a line or two if that is all the draft needs, and stop for the writer to choose the next stage (usually 08).
6. **Have the rivals read,** when `_config/writer.md` says so: run stage 08 on `pitches-v1.md`, with critics who wrote none of them. It reads the brief and the pitches only, since there is no premise yet, and writes `critique-pitches-round-N-<kind>.md`. Then come back here.
7. **Choose, with the writer.** Run the worksheet's section 8, with the reviews in hand. Write `premise-v1.md`: the chosen card, what it borrows from the others and why, the writer's reasons in their words, and the seven jobs (worksheet, section 7).
8. **Verify, then stop for review.** Add the Verify sections below to `brief-vN.md`, `pitches-vN.md` and `premise-vN.md`, add a project log entry, and stop.

## Outputs

All in `stages/01-brief-and-premise/output/<project>/`, each part carrying its marker (`[from: 01 step 5; premise-worksheet §3]`):
- `request.md`: the request, word for word.
- `brief-vN.md`: the brief.
- `pitches-vN.md`: the rival premises, each on the card.
- `premise-vN.md`: the chosen premise, its reasons, and the seven jobs.
- `project-log.md`: the project's numbered log (`stages/how-stages-work.md`, section 11).
- `handed-over/`: an untouched copy of each file handed over, unless story work is committed (`stages/how-stages-work.md`, section 4).

## Verify

Before the review stop, check and record:
- **In `brief-vN.md`, the brief against the request:** everything asked is in the brief; anything the brief adds is marked as an addition, with why.
- **In `brief-vN.md`, the brief against `_config/writer.md`:** each standing preference is applied, or the brief says why not; each one still *to confirm* is marked as a stopgap.
- **In `pitches-vN.md`, each rival against the brief:** it breaks no rule and repeats nothing on the avoid list.
- **In `premise-vN.md`, the designing principle:** the swap test in `premise-and-theme.md`, section 5 (could it describe dozens of other stories in the genre?).
- **In `premise-vN.md`, the premise against its genre file:** it keeps the genre's promise (section 2 of the genre file), or twists how the promise is kept (section 11 there), never drops it; an expected mystery of a guest genre that the story never presses is not owed (`how-genres-work.md`, section 8); any guarantee (section 4 of the genre file) it means to break is named.
- **In `premise-vN.md`, the seven jobs:** the self-revelation answers the need point for point (`structure-and-conflict.md`, section 2, the check column), or the premise says the hero does not change and what the settlement measures instead.

## Review stop

This is the stop where the writer's changes matter most: the brief and the premise set the direction of everything after. The writer can edit `brief-vN.md` or `premise-vN.md` in place, ask for another round of rivals, or choose differently. Stage 02 reads whatever is in the highest-numbered `premise` and `brief` files when it starts.
