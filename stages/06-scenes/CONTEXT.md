# Stage 06: scenes

**Its one job:** draft every scene on the list as action: who wants what, what they do, where it turns, and where it lands, with the talk marked only by what each line must do.

The rules every stage shares are in `stages/how-stages-work.md`, and are not repeated here.

## Inputs

| Layer | File | Which part | For |
|---|---|---|---|
| 4 | `stages/01-brief-and-premise/output/<project>/project-log.md` | all | where the run stands; which versions are current |
| 4 | `stages/05-scene-weave/output/<project>/scene-weave-vN.md` (highest N; for a series, the episode's file) | the scene list and strands | which scenes, in what order, doing which job |
| 4 | `stages/02-characters/output/<project>/cast-vN.md` (highest N) | the cast sheet (wants, flaws, levers, never says) and the care plan | who wants what; how care is built |
| 4 | `stages/03-world-and-symbols/output/<project>/world-vN.md` (highest N) | the places, the surplus, what each group leaves unsaid, the symbols | where, and what the world does meanwhile |
| 4 | `stages/04-plot/output/<project>/plot-vN.md` (highest N) | the reveals and the knowledge positions | what the audience knows in each scene |
| 3 | `_config/writer.md` | questions 1, 2 and 4 | medium, length, voice |
| 3 | `stages/how-stages-work.md` | all | the shared rules |
| 3 (a record) | `stages/owner-edits.md` | rows for stage 06 | patterns in the writer's edits |
| 3 | `stages/06-scenes/references/drafting-scenes.md` | all | action now and talk in stage 07; which of McKee's five steps this stage writes; the output's shape |
| 3 | `.claude/skills/plot/references/scenes.md` | sections 1 to 5 | what a scene must change; the scene card; beats; getting in and out |
| 3 | `.claude/skills/plot/references/suspense-and-fear.md` | sections 6 and 10 | knowledge positions; questions for a scene |
| 3 | `.claude/skills/story-world/references/prose-and-film.md` | sections 2 to 6 | what the medium makes cheap |
| 3 | `.claude/skills/story-world/references/world-materials.md` | section 4 | the world's own business, in passing |
| 3 | `.claude/skills/hard-to-vary/SKILL.md` | "The quick version" | testing a choice, lightly |
| 3 | `.claude/skills/hard-to-vary/references/by-domain.md` | section 5 | the remove and swap tests for a story choice |

## Process

1. **Read the project log, and the scene list, cast, world and plot** for the scenes being drafted (a whole work, or one act or episode at a time), and record any edits the writer made to them since they were handed over (`stages/how-stages-work.md`, section 8).
2. **For each scene, fill the scene card,** with the value's charge at start and end (reference, section 2).
3. **Draft the scene as action,** beat by beat, writing the first four of McKee's five steps for each beat, and marking each line of talk by its move (reference, sections 1 and 2).
4. **Test each scene** with `hard-to-vary`'s remove test, lightly: what does the story lose without it? (`.claude/skills/hard-to-vary/references/by-domain.md`, section 5.)
5. **Verify, then stop for review,** and add a project log entry.

## Outputs

In `stages/06-scenes/output/<project>/`, each part with its marker (`[from: 06 step 3; drafting-scenes §2; scenes §2]`):
- `draft-vN.md`, or one file per act, episode or chapter (`draft-ep03-vN.md`): the scene cards and action drafts.

## Verify

In each draft file:
- **Against the scene list (stage 05):** each scene does the job, and changes the gap, that its row says; no scene is missing or added without a note.
- **Against the plot (stage 04):** each scene's knowledge position is the one planned; no fact comes out before its place in the reveal order.
- **Against the cast (stage 02):** each driver's want in the scene serves their want in the story; each character acts within their flaw, values and "never says" column, or the draft marks the surprise and why it is still them (Bond principle 7).
- **Against the world (stage 03):** the place and its rules hold; the world's own business shows where planned.

## Review stop

The writer reads the action drafts. Since no dialogue is written yet, this is the cheapest moment to move, cut or rebuild a scene. Stage 07 reads the highest-numbered draft files.
