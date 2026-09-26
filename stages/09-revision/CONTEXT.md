# Stage 09: revision

**Its one job:** answer every finding and every piece of the writer's feedback, make the next version of what was criticised, and log exactly what changed and why, keeping every earlier version.

The rules every stage shares are in `stages/how-stages-work.md`, and are not repeated here. Like stage 08, this stage runs on whatever output was criticised, as often as the project needs.

## Inputs

| Layer | File | Which part | For |
|---|---|---|---|
| 4 | `stages/01-brief-and-premise/output/<project>/project-log.md` | all | where the run stands; which versions are current |
| 4 | `stages/08-critique/output/<project>/critique-<target>-round-N-*.md` (this round) | all, as the writer left them at the review stop | the findings |
| 4 | the writer's feedback, as given, with anything attached | all | the largest revision |
| 4 | the target named in the critiques (the version they criticised) | all | what is revised |
| 4 | the earlier outputs the findings trace to | the parts the findings name | revising at the stage the fault came from |
| 4 | `stages/01-brief-and-premise/output/<project>/brief-vN.md` (highest N) | the rules | limits |
| 3 | `_config/writer.md` | questions 9, 11 and 13 | helpers, rounds, what to ask first |
| 3 | `stages/how-stages-work.md` | all | the shared rules |
| 3 (a record) | `stages/owner-edits.md` | rows for the stages this round touches | patterns in the writer's edits |
| 3 | `stages/09-revision/references/revision-log.md` | all | the log, the new version, where to revise, feedback, faults in the workshop |
| 3 | `stages/08-critique/references/critique-rounds.md` | section 3 | how findings were traced |
| 3 | the craft skill each finding cites | the sections the finding cites | making the change |
| 3 | `CLAUDE.md` | the line on taking a request from the owner | reading the writer's feedback |

## Process

1. **Read the project log, and the critiques as the writer left them,** and any feedback, and record any edits the writer made to the target since it was handed over (`stages/how-stages-work.md`, section 8). For feedback, write `feedback-N.md` first (reference, section 4), and say the reading back.
2. **Settle the clashes** between findings (reference, section 1, item 2).
3. **Decide each finding:** accepted, accepted in part, or rejected, with the reason.
4. **Revise at the stage each fault came from** (reference, section 3): write the next version there, with new markers, changing only what the log says.
5. **List what is now stale** in the log and the project log.
6. **Look for faults in the workshop** (reference, section 5).
7. **Verify, then stop for review,** and add a project log entry.

## Outputs

- In `stages/09-revision/output/<project>/`: `revision-log-<target>-round-N.md`; `feedback-N.md` for each piece of the writer's feedback.
- In the folder of each stage revised: its next version (`plot-v3.md`), the earlier ones kept.

## Verify

In `revision-log-<target>-round-N.md`:
- **Every finding answered:** each finding in each critique of the round has a row, and each row a verdict.
- **Only the logged changes:** the new version differs from the old only where the log says (compare the two files).
- **Earlier stages still agree:** for each revised output, rerun its own stage's Verify against its inputs; list any later output made stale.
- **Feedback:** each rule drawn from the writer's feedback is placed in the brief or `_config/writer.md`, as the writer chose, or waits on their answer.

## Review stop

The writer reads the log and the new version. Next: another critique round (at most as many as `_config/writer.md` allows before it comes to the writer), the next stage, or a rerun of a stale one.
