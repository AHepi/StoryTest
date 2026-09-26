# Stage 05: scene weave

**Its one job:** turn the plot into an ordered list of scenes (and, for a series, of episodes), each with one core action and a reason to be there. With stages 02 to 04, this is the plan.

The rules every stage shares are in `stages/how-stages-work.md`, and are not repeated here.

## Inputs

| Layer | File | Which part | For |
|---|---|---|---|
| 4 | `stages/01-brief-and-premise/output/<project>/project-log.md` | all | where the run stands; which versions are current |
| 4 | `stages/04-plot/output/<project>/plot-vN.md` (highest N) | the jobs table, the reveals, the knowledge positions, the genre beat map | what the scenes must do |
| 4 | `stages/02-characters/output/<project>/cast-vN.md` (highest N) | the moral line and the care plan | where care and the moral steps fall |
| 4 | `stages/03-world-and-symbols/output/<project>/world-vN.md` (highest N) | the places, the symbols' appearances | where scenes happen; where symbols return |
| 3 | `_config/writer.md` | questions 1 and 2 | medium and length (episodes, running time, words) |
| 3 | `stages/how-stages-work.md` | all | the shared rules |
| 3 (a record) | `stages/owner-edits.md` | rows for stage 05 | patterns in the writer's edits |
| 3 | `stages/05-scene-weave/references/scene-weave-worksheet.md` | all | the order of work, the season level, the output's shape |
| 3 | `.claude/skills/plot/references/scenes.md` | sections 1, 5, 6 and 7 | what a scene must change; opening and closing; the scene list; strands |
| 3 | `.claude/skills/plot/references/suspense-and-fear.md` | sections 6 and 7 | knowledge positions; the ratchet |
| 3 | `sources/gap-theory-of-narrative.md` | principles 4 and 5, Part 2 section 4 (mystery and wonder), and writer's question 2 | which questions close, when, and whether the emphasis matches |
| 3 | `.claude/skills/hard-to-vary/SKILL.md` | "The quick version" | testing a choice, lightly |
| 3 | `.claude/skills/hard-to-vary/references/by-domain.md` | section 5 | the remove and swap tests for a story choice |

## Process

1. **Read the project log, the plot, cast and world,** and record any edits the writer made to them since they were handed over (`stages/how-stages-work.md`, section 8).
2. **Work through the worksheet's order** (section 1, steps 1 to 7).
3. **Test the list** with `hard-to-vary`'s remove test, lightly: a scene whose removal loses no job is cut, merged, or given a job (`.claude/skills/hard-to-vary/references/by-domain.md`, section 5).
4. **Verify, then stop for review,** and add a project log entry.

## Outputs

In `stages/05-scene-weave/output/<project>/`, each part with its marker (`[from: 05 step 2; scenes §6]`):
- `scene-weave-vN.md`: the scene list and, for a series, the episode table (worksheet, section 3); for a long series, one file per episode as well.

## Verify

In `scene-weave-vN.md`:
- **Against the plot (stage 04):** every job in the jobs table is done by at least one scene; every reveal has its scene, in the order stage 04 set.
- **Against the cast (stage 02):** each step of the moral line and each rung of the care plan has its scene, before the scene that needs it.
- **Against the world (stage 03):** each scene is in a place stage 03 planned; a scene that needs a new place is listed at the review stop, since stage 03's output then needs a new version (`stages/how-stages-work.md`, section 7); each symbol's appearances are in the list.
- **Open questions:** every question the plan opens is assigned to this episode, this season, a later season (named), or left as a wonder, and the emphasis matches: a question the plan presses is never filed as a wonder, and a wonder is mentioned in passing and never pressed (Gap principle 5, Part 2 section 4, writer's question 2).
- **The tension chart:** none of the faults in `suspense-and-fear.md`, section 7, or each one is there on purpose and says why.

## Review stop

The writer reads the plan. This is where the season work's critique rounds ran: point stage 08 at the plan (stages 02 to 05 together) before any scene is drafted, when a change costs least. Stage 06 reads the highest-numbered `scene-weave` file.
