# Stage 04: plot

**Its one job:** decide what happens and in what order the audience finds it out: the chain of events from the breach to the settlement, the reveals, who tells it, and the genre's beats.

The rules every stage shares are in `stages/how-stages-work.md`, and are not repeated here.

## Inputs

| Layer | File | Which part | For |
|---|---|---|---|
| 4 | `stages/01-brief-and-premise/output/<project>/project-log.md` | all | where the run stands; which versions are current |
| 4 | `stages/01-brief-and-premise/output/<project>/premise-vN.md` (highest N) | the premise card and the seven jobs | the spine |
| 4 | `stages/02-characters/output/<project>/cast-vN.md` (highest N) | the cast sheet, the hero's change, the opponents, the moral line | who drives, who resists, the moral steps |
| 4 | `stages/03-world-and-symbols/output/<project>/world-vN.md` (highest N) | the departures and stakes, the places, the symbols | where each turn happens, what things cost |
| 4 | `stages/01-brief-and-premise/output/<project>/brief-vN.md` (highest N) | rules and avoid list | limits |
| 3 | `_config/writer.md` | questions 1 and 2 | medium and length |
| 3 | `stages/how-stages-work.md` | all | the shared rules |
| 3 (a record) | `stages/owner-edits.md` | rows for stage 04 | patterns in the writer's edits |
| 3 | `stages/04-plot/references/plot-worksheet.md` | all | the order of work, the jobs table, the plan at two levels, the output's shape |
| 3 | `sources/gap-theory-of-narrative.md` | in full the first time in a conversation (the plot skill's rule), then principles 2, 4, 6 and 7 and the five questions | the frame |
| 3 | `sources/anticipation-theory.md` | in full before the suspense module's first full use (the plot skill's rule), then principles 1, 6 and 7 | suspense |
| 3 | `.claude/skills/plot/SKILL.md` | "The procedure", Building, steps 1 to 8 | the method |
| 3 | `.claude/skills/plot/references/structure-and-conflict.md` | sections 2 to 9 | the jobs, conflict, crisis and climax |
| 3 | `.claude/skills/plot/references/reveals-and-withholding.md` | sections 1 to 7 | the reveals |
| 3 | `.claude/skills/plot/references/telling-and-perspective.md` | sections 1 to 7 | the teller |
| 3 | `.claude/skills/plot/references/suspense-and-fear.md` | sections 1, 6 and 7 | the four terms, knowledge positions, the ratchet |
| 3 | `.claude/skills/plot/references/premise-and-theme.md` | sections 7 and 8 | when the meaning shows; the settlement and false endings |
| 3 | `.claude/skills/genre/SKILL.md` | "The procedure", Building, steps 5 to 7 | beats, guarantees, twists |
| 3 | `.claude/skills/genre/references/genres/<genre>.md` | sections 4, 6 and 9 | guarantees, beats, suspense and knowledge |
| 3 | `.claude/skills/hard-to-vary/SKILL.md` | "The quick version" | testing a choice, lightly |
| 3 | `.claude/skills/hard-to-vary/references/by-domain.md` | section 5 | the remove and swap tests for a story choice |

## Process

1. **Read the project log, the premise, cast, world and brief,** and record any edits the writer made to them since they were handed over (`stages/how-stages-work.md`, section 8).
2. **Work through the worksheet's order** (section 1, steps 1 to 8).
3. **Test each load-bearing choice** with `hard-to-vary` (plot skill, Building step 8).
4. **Verify, then stop for review,** and add a project log entry.

## Outputs

In `stages/04-plot/output/<project>/`, each part with its marker (`[from: 04 step 2; plot-worksheet §3; structure-and-conflict §2]`):
- `plot-vN.md`: the plot, in the order of the worksheet's section 4, with its handed-over copy.

## Verify

In `plot-vN.md`:
- **Against the premise (stage 01):** the plot tracks the designing principle; the ending answers the story's question; the settlement matches the premise card's "change or settlement" line, or says what changed and why.
- **Against the cast (stage 02):** every step of the moral line is an event in the jobs table; the main opponent is present in the final clash, not a stand-in (the Battle row's check in `structure-and-conflict.md`, section 2).
- **Against the world (stage 03):** each turn happens in its planned place, and the stakes are the ones the world sets (Gap principle 2).
- **The reveals:** logic, weight and pace (`reveals-and-withholding.md`, section 4), and fair withholding (section 7 there).
- **Against the genre file:** each beat's job is done or knowingly done without; any guarantee broken is broken on purpose.

## Review stop

The writer reads `plot-vN.md`, edits it in place or asks for a rerun. Stage 05 reads the highest-numbered `plot` file. With the cast and the world, this is most of what the season work called the plan; stage 08 can be run on it now, before any scene is listed.
