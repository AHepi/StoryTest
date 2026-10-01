# Stage 03: world and symbols

**Its one job:** build the world the story needs, grown from the premise and the cast, and the images whose meaning changes as the story goes.

The rules every stage shares are in `stages/how-stages-work.md`, and are not repeated here.

## Inputs

| Layer | File | Which part | For |
|---|---|---|---|
| 4 | `stages/01-brief-and-premise/output/<project>/project-log.md` | all | where the run stands; which versions are current |
| 4 | `stages/01-brief-and-premise/output/<project>/premise-vN.md` (highest N) | the premise card and the seven jobs | the designing principle, the question, the turns |
| 4 | `stages/01-brief-and-premise/output/<project>/brief-vN.md` (highest N) | rules, avoid list, source material | limits on the world |
| 4 | `stages/02-characters/output/<project>/cast-vN.md` (highest N), and its handed-over copy | the cast sheet (values, flaws), the hero's change | places from values; the opening world; the writer's edits |
| 3 | `_config/writer.md` | questions 1 and 4 | medium and voice |
| 3 | `stages/how-stages-work.md` | all | the shared rules |
| 3 (a record) | `stages/owner-edits.md` | rows for stage 03 | patterns in the writer's edits |
| 3 | `stages/03-world-and-symbols/references/world-and-symbols-worksheet.md` | all | the order of work, what each group leaves unsaid, the output's shape |
| 3 | `sources/implied-world-theory.md` | in full the first time in a conversation (the story-world skill's rule), then principles 1 to 8, Part 2 sections 3 and 4, and "What it predicts" | the frame |
| 3 | `.claude/skills/story-world/SKILL.md` | "The procedure", Building, steps 1 to 12 | the method |
| 3 | `.claude/skills/story-world/references/world-from-story.md` | sections 2 to 10 | the world grown from the story |
| 3 | `.claude/skills/story-world/references/world-materials.md` | sections 1 to 8 | the materials, each for its job |
| 3 | `.claude/skills/story-world/references/prose-and-film.md` | sections 2 to 6 | what the medium makes cheap |
| 3 | `.claude/skills/story-world/references/diagnosing-a-world.md` | section 3 | the gauge for how many departures is too many |
| 3 | `.claude/skills/dialogue/references/voice.md` | section 4 | what people who share a great deal leave unsaid |
| 3 | `.claude/skills/plot/references/symbols.md` | sections 1 to 6 | symbols |
| 3 | `.claude/skills/genre/references/genres/<genre>.md` | section 3 | the genre's baseline |
| 3 | `.claude/skills/hard-to-vary/SKILL.md` | "The quick version" | testing a choice, lightly |
| 3 | `.claude/skills/hard-to-vary/references/by-domain.md` | section 5 | the remove and swap tests for a story choice |

## Process

1. **Read the project log, the premise, brief and cast,** and record any edits the writer made to the cast since it was handed over (`stages/how-stages-work.md`, section 8). Note the designing principle, the story's question, the seven jobs and the cast's values.
2. **Work through the worksheet's order** (section 1, steps 1 to 9).
3. **The symbols** (worksheet, section 1, step 10).
4. **Test the load-bearing choices** with `hard-to-vary`, lightly (story-world skill, Building step 12).
5. **Verify, then stop for review,** and add a project log entry.

## Outputs

In `stages/03-world-and-symbols/output/<project>/`, each part with its marker (`[from: 03 step 2; world-from-story §7]`), and its handed-over copy:
- `world-vN.md`: the world and its symbols, in the order of the worksheet's section 3.

## Verify

In `world-vN.md`:
- **Against the premise (stage 01):** the main departure carries the premise's question (Implied World principle 8); each of the seven jobs has a place.
- **Against the cast (stage 02):** opposed values have opposed places; the opening world presses on the hero's flaw; the symbol attached to the hero's change appears where the flaw shows and returns at the change.
- **Against the attention budget:** the number of departures a newcomer must learn before the first major turn (the gauge in `diagnosing-a-world.md`, section 3), and whether a guide is planned if it is high.
- **The groups' shorthand:** each term the audience must decode has a way in; shorthand it need not decode is left unexplained (worksheet, section 2).
- **Against the brief:** no rule broken; the source material the brief names is used where the brief asks.

## Review stop

The writer reads `world-vN.md`, edits it in place or asks for a rerun. Stage 04 reads the highest-numbered `world` file.
