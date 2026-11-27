# The revision log

*Sources: the Fourth Direction season project's practice (every finding logged as accepted or not, with exactly what changed; every earlier version kept; the owner's feedback recorded in full as the biggest revision of all), which answers the owner's wish that every critique, change and earlier version be kept; the Interpretable Context Methodology paper (mend the source, not only the output, when the same fault keeps coming back), in the workshop's own words; the workshop's own error-correction practice. No craft book adds to this stage beyond what the skills hold: McKee's warning that rewording the talk of a scene that fails as a whole drives it further wrong is already in the dialogue skill (its Diagnosing, step 2).*

Contents: 1 What a revision log holds. 2 The new version. 3 Revise at the stage the fault came from. 4 The writer's own feedback. 5 Faults in the workshop.

## 1. What a revision log holds

`revision-log-<target>-round-N.md` (the target as in the critiques it answers: `pitches`, `plan`, `draft`, or a part such as `draft-ep03`), in this order:
1. **From and to:** which file and version was revised, and the new version's name (`plot-v2.md` to `plot-v3.md`).
2. **Where critics disagreed, and how it was settled:** each clash between two findings, what was kept of each, and why. Settle these first, since each settlement changes what several findings get.
3. **One table per critique:**

| # | Finding | Verdict | What changed, and where |
|---|---|---|---|

The verdict is *accepted*, *accepted in part* (say which part is rejected, and why), or *rejected* (say why). "What changed" names the section, scene or episode, so the writer can find each change in the new version. A finding the writer struck at the review stop is *rejected*, with their reason. In **spoiler-free mode** (`stages/how-stages-work.md`, section 3), each held **story** choice decided by the workshop records both the chosen reading and the rejected alternative, so the writer can review or reverse it after reading.
4. **Unmet goals and trade-offs (no *moving the goalposts*):** compare the revised work against the writer's untouched `request.md` (and raw quoted words from item 1 of any `feedback-N.md`), not only against the brief's stand-in measures (such as word count). If the revision cannot satisfy an original goal on its original terms (for example, protecting voice and adding a new layer left a stretch longer rather than shorter), **do not move the goalposts** by redefining the goal as passed (`.claude/skills/hard-to-vary/references/word-list.md`). List it here and flag the trade-off to the writer as a non-story decision (in spoiler-free mode, phrased without story content: `stages/how-stages-work.md`, section 3).
5. **Stale:** every later output that read the revised file (`stages/how-stages-work.md`, section 7).
6. **Owed to the workshop:** any finding traced to a stage contract or reference (section 5).

**Deciding across rounds** *(from `38 Findings`, proposals 3a, 4a, 4b and 5)*:
- **Escalation of repeated points (before the final round):** while critique rounds remain before the cap in `_config/writer.md` (question 11), any finding raised independently in two critique rounds that was left open or fixed only in part is not deferred again — settle it now or put it to the writer immediately (in spoiler-free mode, settle if it is a story choice and log both sides; ask immediately if it is a scope or trade-off choice). *("Two rounds" is a rule of thumb, not a measured cutoff.)*
- **Final-round stopping rule (takes precedence on the final round):** once the last critique round `_config/writer.md` (question 11) allows is reached, fix **only** new faults caused by the previous round and plain contradictions; do **not** reopen the draft for structural or taste suggestions. List remaining suggestions — flagging any unresolved repeated point prominently — as choices for the writer (in spoiler-free mode, ask as a non-story scope question whether to authorise one more round, or log the repeated story choice beside its alternatives without reopening the draft).
- **Critic record:** in `project-log.md`, record each critic's four-bucket counts (`accepted`, `partial`, `taste/held/deferred`, `rejected-as-wrong`, and `total`) and follow `stages/08-critique/references/critique-rounds.md`, section 1, before proposing any critic replacement to the writer.

## 2. The new version

- The revised output is a new file with the next number, in the folder of the stage that made it (`stages/04-plot/output/<project>/plot-v3.md`). The old version is kept, unchanged.
- **Local draft changes by exact-edit script:** for local edits to an existing draft, write the accepted changes into a plain-text edit-order file (in JSON format — run `--help` on the script to see the layout, each edit carrying the `id` of its log row) and apply it with `python3 stages/09-revision/scripts/apply_exact_edits.py --edits <order.json>`. The script refuses to overwrite an existing version, refuses no-op, zero, or ambiguous matches, prints explicit zero-repeat status for `"all"` edits, runs script checks (forbidden patterns, sacred lines, untouched sections), measures prose story text only, and prints a line-by-line diff (a file comparison showing only what changed). Reserve whole-section rewrites for full scene rebuilds, state why in the log, and compare the whole section with `diff`.
- **Substantial new prose vs. final phrase edits:** stage 09 does not grade its own prose (`CLAUDE.md`, rule 1). When a draft revision adds substantial new story prose (new scenes or multi-sentence additions touching facts, timeline or who knows what), flag it in Verify for an independent **narrow new-prose check** in stage 08 (`stages/08-critique/references/critique-rounds.md`, section 1) before handover (or, if this is the final handover after the last round, record `independent check on new prose: not run` and ask the writer whether to run one narrow stage 08 check before reading). For pure cuts and local phrase edits, the exact-edit script's diff receipt suffices, and Verify states `new-prose check: not run (cuts and local phrase edits only)` (`CLAUDE.md`, rule 2).
- **Clean updates for revised plans (no split truth):** when revising a planning file (`brief-vN.md`, `premise-vN.md`, `cast-vN.md`, `world-vN.md`, `plot-vN.md`, `scene-weave-vN.md`), update the changed sections directly inside the new version file rather than leaving outdated earlier sections contradicted by an appended correction section (the earlier version file stays untouched for history). Never verbally retract a rule in a planning file inside a revision log without writing the next version of that planning file.
- Each changed part carries a new marker naming this round (`[from: 09 round 2, logic 4; structure-and-conflict §3]`), so a later critique can see what was revised and why.
- Change only what the log says. A change made for no finding is either added to the log, with its reason, or taken out.

## 3. Revise at the stage the fault came from

A finding's trace (`stages/08-critique/references/critique-rounds.md`, section 3) says where to mend it. Mend it at the earliest stage it came from, then let the change run forward: a weak reveal that came from the plot is mended in the plot, and the scenes that carry it are then stale, rather than patched scene by scene. The dialogue skill's rule is the same at small scale: when a whole scene fails, fix the scene before the words.

## 4. The writer's own feedback

The writer's feedback is the largest revision, and is recorded in full, as the season's "Owner feedback 1" was, in `feedback-N.md`:
1. **What the writer said,** quoted word for word, with the date, and anything they attached.
2. **How it was read:** said back as the line on taking a request from the owner in `CLAUDE.md` asks, with the nearest other reading; when that line's signs say the reading is in doubt, follow it: ask, and do nothing risky, costly or hard to undo on any reading until the writer answers.
3. **What was checked,** and what it found.
4. **The rules it gives,** numbered. For each, ask the writer whether it holds for this project only (it goes into the next brief, stage 01) or for every project (it goes into `_config/writer.md`). If the feedback turns on **spoiler-free mode** (`stages/how-stages-work.md`, section 3), record that rule here, write `Spoiler-free mode: on` into `project-log.md` immediately (so every later stage sees it before a new brief is written), and apply it at once to every report to the writer.
5. **What changed:** a new version of the stage it bears on, or, when the writer rejects the direction, a new brief and a new run of stage 01, with every earlier file kept.

## 5. Faults in the workshop

A finding or an edit that shows by itself that a contract or reference is wrong (it misreads an owner theory, gives a wrong rule, or points to the wrong place) goes to the `error-correction` skill as a sign at once. For the rest, before closing a round, look at two things together: the findings traced to a stage contract or reference (section 1, item 6), and the rows of `stages/owner-edits.md` for the stages this round touched. When the same kind of fault or edit keeps coming back to one stage, propose a change to that stage's contract or reference at the review stop, as `stages/how-stages-work.md`, section 8, says. The output is mended now either way; the source change goes through the `error-correction` skill, like any change to what the workshop says.
