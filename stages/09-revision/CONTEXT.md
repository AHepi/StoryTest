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
| 4 | the earlier outputs the findings trace to, plus in draft-in mode any planning output built for this revision (such as `world-vN.md` or `plot-vN.md`) | the parts the findings name, or all for a draft-in planning output | revising at the stage the fault came from, or carrying a draft-in plan into the draft |
| 4 | `stages/01-brief-and-premise/output/<project>/request.md` (and any prior `stages/09-revision/output/<project>/feedback-N.md`) | the writer's untouched words | checking against original goals (no *moving the goalposts*: reference, section 1) |
| 4 | `stages/01-brief-and-premise/output/<project>/brief-vN.md` (highest N) | the rules; in draft-in mode, the voice and preservation record | limits |
| 4 | `draft-v1` (draft-in mode, when revising a draft: in stage 07's output folder, or stage 06's for an action-only draft, including split files) | all | the writer's original copy, to hold to the voice and preservation record |
| 3 | `_config/writer.md` | questions 9, 11, 13 and 14 | helpers, rounds, what to ask first, spoiler-free mode |
| 3 | `stages/how-stages-work.md` | all | the shared rules |
| 3 (a record) | `stages/owner-edits.md` | rows for the stages this round touches | patterns in the writer's edits |
| 3 | `stages/09-revision/references/revision-log.md` | all | the log, exact edits, no moving the goalposts, clean plan updates, escalation and stopping rules, feedback, faults in the workshop |
| 3 | `stages/09-revision/scripts/apply_exact_edits.py` | run via python3 | applying local draft edits without unlogged drift, running script checks on sacred lines/patterns/untouched sections, and counting prose story text only |
| 3 | `stages/08-critique/references/critique-rounds.md` | sections 1 and 3 | critic records, narrow new-prose check, and how findings were traced |
| 3 | the craft skill each finding cites | the sections the finding cites | making the change |
| 3 | `CLAUDE.md` | the line on taking a request from the owner | reading the writer's feedback |

## Process

1. **Read the project log, and the critiques as the writer left them,** and any feedback, and record any edits the writer made to the target since it was handed over (`stages/how-stages-work.md`, section 8). For feedback, write `feedback-N.md` first (reference, section 4), and say the reading back.
2. **Settle the clashes** between findings (reference, section 1, item 2).
3. **Decide each finding:** accepted, accepted in part, or rejected, with the reason, applying the escalation and final-round stopping rules (reference, section 1). In **spoiler-free mode**, follow `stages/how-stages-work.md`, section 3, for held story choices (non-story questions — including unmet original goals, scope trade-offs, and critic-lineup proposals — are still asked as normal).
4. **Revise at the stage each fault came from** (reference, sections 2 and 3; for findings from blind critics whose upstream trace was *not run*, trace them before editing): write the next version there, with new markers, changing only what the log says. Apply local draft edits with `stages/09-revision/scripts/apply_exact_edits.py`, and update revised planning files cleanly in place inside the new version (no contradictory addenda or verbal retractions).
5. **Check against `request.md` and list what is now stale:** record any unmet goal or trade-off without *moving the goalposts* (reference, section 1, item 4), and list stale outputs in the log and the project log.
6. **Look for faults in the workshop** (reference, section 5).
7. **Verify, then stop for review,** and add a project log entry (including each critic's four-bucket counts — `accepted`, `partial`, `taste/held/deferred`, `rejected-as-wrong` — and `total`).

## Outputs

- In `stages/09-revision/output/<project>/`: `revision-log-<target>-round-N.md`; `feedback-N.md` for each piece of the writer's feedback; optionally the edit-order file (`edit-order-<target>-round-N.json`) if kept beside the log once the script's diff receipt is recorded.
- In the folder of each stage revised: its next version (`plot-v3.md`), the earlier ones kept.

## Verify

In `revision-log-<target>-round-N.md`:
- **Every finding answered:** each finding in each critique of the round has a row, and each row a verdict (or, for an initial draft-in revision run from feedback and a planning output before any critique round, every rule in the brief, feedback and planning output has a row).
- **Only the logged changes, and every accepted change landed:** for local draft edits, backed by `apply_exact_edits.py`'s receipt (applied edit ids, match counts, zero-repeat status and line-by-line diff); for whole-scene rebuilds, revised planning files (`brief`, `premise`, `cast`, `world`, `plot`, `scene-weave`), or pitches, backed by an explicit `diff` against the previous version confirming every accepted change landed (with reason for whole-scene rebuilds).
- **No moving the goalposts:** checked against `request.md` (and raw quoted words in item 1 of any `feedback-N.md`); any unmet goal or trade-off is recorded under `## Unmet goals and trade-offs` and flagged to the writer.
- **Voice and preservation (draft-in mode, when revising a draft):** every item of `brief-vN.md`'s voice and preservation record (`stages/01-brief-and-premise/references/premise-worksheet.md`, section 2) checked against `draft-v1` — script-run checks (untouched boundaries, formatting, sacred lines verbatim, prose story-text-only counts) via `apply_exact_edits.py`, plus voice, rhythm, and judgment signals where relevant.
- **New-prose check (when revising a draft):** state whether this revision added substantial new story prose (flagging a narrow new-prose check for the next stage 08 round — or, on the final handover, noting `independent check on new prose: not run` and asking whether the writer wants one narrow stage 08 check before reading), or state `not run (cuts and local phrase edits only — exact-edit script diff verified)` (`CLAUDE.md`, rule 2).
- **Earlier stages still agree:** for each revised output, rerun its own stage's Verify against its inputs (in draft-in mode, following `stages/how-stages-work.md`, section 2); list any later output made stale.
- **Feedback:** each rule drawn from the writer's feedback is placed in the brief or `_config/writer.md`, as the writer chose, or waits on their answer.

## Review stop

The writer reads the log and the new version. Next: another critique round (at most as many as `_config/writer.md` allows before it comes to the writer), the next stage, or a rerun of a stale one. In **spoiler-free mode**, follow `stages/how-stages-work.md`, section 3.
