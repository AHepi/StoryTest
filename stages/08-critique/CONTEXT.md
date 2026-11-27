# Stage 08: critique

**Its one job:** find what is wrong with an output (pitches, the plan, or a draft) by critics who did not write it, each hunting one kind of problem, with every finding traced to where it came from.

The rules every stage shares are in `stages/how-stages-work.md`, and are not repeated here. Unlike stages 01 to 07, this stage is run on whatever output the writer points it at, and usually more than once in a project.

## Inputs

| Layer | File | Which part | For |
|---|---|---|---|
| 4 | `stages/01-brief-and-premise/output/<project>/project-log.md` (omit for blind critics: reference, section 1) | all | where the run stands; which versions are current |
| 4 | the target: `stages/01-brief-and-premise/output/<project>/pitches-vN.md`, or the plan (`cast-vN.md`, `world-vN.md`, `plot-vN.md` and `scene-weave-vN.md` in stages 02 to 05), or a draft (`stages/07-dialogue/output/<project>/draft-vN.md`, or stage 06's) | the version named by the writer, or the highest N (for blind critics, clean story text without revision-header notes or `## Verify`) | what is criticised |
| 4 | `stages/01-brief-and-premise/output/<project>/request.md` (and the writer's raw quoted words from item 1 of any `stages/09-revision/output/<project>/feedback-N.md` — never items 2 to 5) | writer's untouched words only (for the excuse-blind goal checker; omit for a cold first reader) | testing the draft directly against what the writer asked, without workshop excuses (reference, section 1) |
| 4 | `stages/01-brief-and-premise/output/<project>/brief-vN.md` (highest N), and `premise-vN.md` when one exists (there is none before the pitches, nor for a draft brought in at stage 01) | all (including the voice and preservation record in draft-in mode; omit where the critic kind excludes it: reference, section 1) | what the work was meant to do |
| 4 | `draft-v1` (draft-in mode, when critiquing a revised draft: in stage 07's output folder, or stage 06's for an action-only draft, including split files; given only where the critic kind includes it: reference, section 1) | all | the writer's original copy, for checking voice and preservation or before-and-after comparison |
| 4 | the outputs of the stages before the target that its markers name, plus in draft-in mode any planning output built for this revision (such as `world-vN.md` or `plot-vN.md`; omit where the critic kind excludes it: reference, section 1) | the parts the markers name, or all for a draft-in planning output | tracing (reference, section 3) and checking the draft against the revision's plan |
| 4 | `stages/09-revision/output/<project>/revision-log-<target>-round-N.md` and stage 09's line-by-line diff (a file comparison showing only what changed) | the latest for this target, in a second round or narrow new-prose check (omit for blind critics: reference, section 1) | what the last round changed |
| 3 | `_config/writer.md` | questions 9, 11 and 14 | helpers at once; the critics and rounds; spoiler-free mode |
| 3 | `stages/how-stages-work.md` | all | the shared rules |
| 3 | `stages/08-critique/references/critique-rounds.md` | all | setting up a round, draft critic kinds, a finding, tracing, the ending-backwards lens, the rival |
| 3 | the craft skill for each critic's kind (where the critic kind uses one), e.g. `.claude/skills/plot/SKILL.md` | "The procedure", Diagnosing and Reply | the critic's method |
| 3 | the owner theory that skill is built on (where the critic kind uses a craft skill), e.g. `sources/gap-theory-of-narrative.md` | in full the first time in a conversation, as that skill says | the frame |
| 3 | `.claude/skills/hard-to-vary/SKILL.md` | "The quick version"; for a disputed load-bearing choice, "The procedure" | whether a choice, or a finding, does work |
| 3 | `.claude/skills/error-correction/SKILL.md` | "Before any claim reaches the owner or a writer" | the claim check on the critique itself |

For a whole work, `story-critique` leads when the writer's account has it (it is not in this repository); the critics above then take one area each.

## Process

1. **Read the project log, and name the target and the round:** which output (`pitches`, `plan`, `draft`, or a part such as `draft-ep03`), which version, and which round for that target (rounds are counted per target). Record any edits the writer made to the target since it was handed over (`stages/how-stages-work.md`, section 8).
2. **Set up the round** (reference, section 1): the kinds of critic, one agent each, none of whom wrote the target; each critic's brief is this contract with its own kind named and its input boundaries respected. In draft-in mode, when critiquing a revised draft, assign at least one critic (such as a seams and voice editor) to check the voice and preservation record against `draft-v1`, and consider an excuse-blind goal checker against `request.md`. On any draft round, do not run a general AI fix verifier (stage 09's exact-edit script handles mechanical edit checks; use the narrow new-prose check only after substantial new prose).
3. **Each critic writes its findings** in the form of the reference's section 2, and traces each one (section 3; blind critics record any visible marker and mark upstream tracing *not run*, for stage 09 to trace).
4. **Run the claim check** on each critique before it is handed on.
5. **Stop for review,** and add a project log entry naming the critiques and the number of findings each.

## Outputs

In `stages/08-critique/output/<project>/`, one file per critic per round, each finding with the marker of its target:
- `critique-<target>-round-N-<kind>.md` (for example `critique-plan-round-1-logic-and-rules.md`).

## Verify

Each critique ends with a `## Verify` section recording:
- **Independence and input boundary:** the critic wrote none of the target, read no other critic's report first, and (for blind critics such as a cold first reader or excuse-blind goal checker) received none of the files excluded by its kind (reference, section 1).
- **Each finding's trace:** it names the marker it followed and which of the three sources it found; a finding with no marker to follow says so, and a blind critic records upstream tracing as *not run (excluded by blind input boundary; traced in stage 09)*.
- **The claim check:** flip and swap run on each finding; each "held if" names the aim it waits on.
- **Voice and preservation (draft-in mode, on a revised draft):** checked against `brief-vN.md`'s voice and preservation record and `draft-v1` (or marked *not run*, with why, if this critic's kind does not cover it; at least one critic in the round must run it).
- **What was not checked,** and why.

## Review stop

The writer reads the critiques, and may strike a finding, add their own, or send the work straight to stage 09. A finding the writer rejects is recorded as rejected in the revision log, with their reason. In **spoiler-free mode**, follow `stages/how-stages-work.md`, section 3.
