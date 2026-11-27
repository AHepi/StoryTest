# Entry 46 review record: draft-in mode, voice and preservation record, and spoiler-free mode

- **Date:** 27 November 2026
- **Scope:** `CONTEXT.md`, `_config/questionnaire.md`, `_config/writer.md`, `stages/how-stages-work.md`, `stages/01-brief-and-premise/CONTEXT.md`, `stages/01-brief-and-premise/references/premise-worksheet.md`, `stages/02-characters/CONTEXT.md`, `stages/03-world-and-symbols/CONTEXT.md`, `stages/04-plot/CONTEXT.md`, `stages/05-scene-weave/CONTEXT.md`, `stages/06-scenes/CONTEXT.md`, `stages/07-dialogue/CONTEXT.md`, `stages/08-critique/CONTEXT.md`, `stages/08-critique/references/critique-rounds.md`, `stages/09-revision/CONTEXT.md`, `stages/09-revision/references/revision-log.md`.
- **Note on scope:** `CONTEXT.md`, `stages/`, and `_config/` are not yet enforced by the commit gate (owner question S15), so this independent review is recorded here on trust, with a trace, per `CLAUDE.md` rule 1.
- **Book text:** none added (all changes are workshop stage process rules drawn from *The Unseen Orchard* run and `CLAUDE.md` / `_config/`).
- **Reviewer:** Independent Stage Reviewer (`research` subagent `011f60444df57b47c724b4bb727c8c36`, read-only, combining `use-tester` and `theory-checker` roles).
- **Round 1 verdict:** Passed after changes (6 must-change, 5 should-change, 3 notes). All 14 findings applied.
- **Round 2 (narrow second look) verdict:** Passed (2 minor non-blocking notes left open per `reviews-and-briefs.md` section 4).

---

## Round 1 reviewer report (verbatim)

# Independent Review (use-tester + theory-checker): Staged Draft-in & Spoiler-Free Mode Changes

Reviewed `git diff --cached` across all 13 staged files (`CONTEXT.md`, `_config/questionnaire.md`, `_config/writer.md`, `stages/how-stages-work.md`, `stages/01-brief-and-premise/CONTEXT.md`, `stages/01-brief-and-premise/references/premise-worksheet.md`, `stages/02-characters/CONTEXT.md`, `stages/03-world-and-symbols/CONTEXT.md`, `stages/04-plot/CONTEXT.md`, `stages/05-scene-weave/CONTEXT.md`, `stages/08-critique/CONTEXT.md`, `stages/09-revision/CONTEXT.md`, `stages/09-revision/references/revision-log.md`) plus the full surrounding contracts, worksheets, untouched stages 06–07, `CLAUDE.md`, `owner-terms.md`, `22 Questions`, `27 Corrections.md`, `sources/*.md`, and `kept-cases/` titles and "Aimed at" lines only. No files were edited.

---

## Numbered Findings

1. **[must-change]** **Target:** `stages/08-critique/CONTEXT.md` line 51.
   **Defect:** The spoiler-free review-stop rule says the report gives "counts, kinds of findings and what was checked **only**, with no story content", dropping **what was not checked**.
   **Grounds:** `CLAUDE.md` rule 2 (line 29: "Not run is never passed ... Say what was not checked"), `.claude/skills/error-correction/SKILL.md` line 195 ("Before any claim reaches the owner or a writer ... Say what was not checked"), `stages/how-stages-work.md` line 60 ("what was checked, and what was not checked"), and `stages/09-revision/CONTEXT.md` line 52 ("what was checked and what was not checked only"). Walked in Case (a) stage 08.
   **Connection:** Following stage 08's contract hides unrun checks (including critics marking Voice and preservation *not run*) from the writer in spoiler-free mode. Also an immediate instance of Kind 6 error (`27 Corrections.md` line 16: copied rule drifting).
   **Verdict:** **bears**.

2. **[must-change]** **Target:** `stages/how-stages-work.md` line 60; also `_config/questionnaire.md` line 27, `stages/09-revision/CONTEXT.md` line 30, `stages/09-revision/references/revision-log.md` line 17.
   **Defect:** "Any choice normally held for the writer is decided by the workshop using the reading nearest the brief" is unscoped and swallows non-story choices (cost, helper/critic counts, committing story files to git, ambiguous scope in a request, whether a feedback rule is project-only or standing).
   **Grounds:** `CLAUDE.md` line 8 (C17: when a request has more than one plain reading, ask and do nothing risky, costly or hard to undo until answered), `CLAUDE.md` line 32 ("What the owner values is an input"), `_config/writer.md` Q13 (line 24: "Anything risky, costly or hard to undo"), and owner question S16 (`stages/01-brief-and-premise/CONTEXT.md` line 39). Walked in Case (a) and Case (c3).
   **Connection:** Non-story questions carry no story content and spoil nothing; letting spoiler-free mode decide them unilaterally contradicts C17, Q13, and S16. Scope the rule explicitly to **story choices** (choices whose question would reveal story content), leaving non-story doubts, cost/helper limits, and project-vs-standing questions governed by `CLAUDE.md` and `_config/writer.md` Q13.
   **Verdict:** **bears**.

3. **[must-change]** **Target:** `stages/01-brief-and-premise/CONTEXT.md` line 44 (step 5, final clause).
   **Defect:** "if the request itself already names the next stages, record that reading in `project-log.md` before continuing" lets stage 01 skip its review stop and run straight into later stages.
   **Grounds:** Directly contradicts `stages/how-stages-work.md` line 37 ("Which stage runs next is always your call at a review stop; nothing runs on to a later stage by itself"), line 49 ("After every stage the agent stops"), `CONTEXT.md` line 60 ("Every arrow passes through a review stop"), `_config/writer.md` Q8 line 19 ("After every stage (the default), until you say otherwise"), and stage 01's own Review stop (lines 70–72). Walked in Case (a) (and seen in `stages/01-brief-and-premise/output/unseen-orchard/project-log.md` entry 1, where skipping the stop proceeded on an unverified guess about which chapters were "the middle").
   **Connection:** Two contracts give opposite orders. Either always stop after stage 01 (respecting Q8 and letting the writer verify scope/baseline or confirm helpers under S16), or move any narrow bypass into `stages/how-stages-work.md` section 3 (one home) gated on explicit writer instruction to run through, zero doubt under C17, and no unconfirmed helpers under S16.
   **Verdict:** **bears**.

4. **[must-change]** **Target:** `stages/01-brief-and-premise/CONTEXT.md` line 44; `stages/08-critique/CONTEXT.md` line 14; `stages/09-revision/CONTEXT.md` lines 17 & 47; `stages/06-scenes/CONTEXT.md` lines 12–15 & 40–46; `stages/07-dialogue/CONTEXT.md` lines 12–15 & 43–49.
   **Defect:** Draft-in mode breaks in four connected places around stages 06 and 07:
   - (a) Stage 01 step 5 (line 44) saves every brought-in draft to `stages/07-dialogue/output/<project>/draft-v1.md`, with no branch for saving an action-only draft to `stages/06-scenes/output/<project>/` — contradicting `stages/how-stages-work.md` line 43 and stages 02–05 Inputs ("or stage 06's draft if action-only").
   - (b) Stage 08 line 14 and stage 09 line 17 load only `stages/07-dialogue/output/<project>/draft-v1*.md`, omitting stage 06's `draft-v1*.md` (contrast stage 08 line 12 right above it, which includes stage 06).
   - (c) Stages 06 and 07 received no draft-in mode rule at all: neither marks unbuilt planning files (`cast`, `world`, `plot`, `scene-weave`) optional in draft-in mode, neither loads `brief-vN.md` (or `draft-vN`), and neither has a draft-in Verify fallback.
   - (d) Consequently, **stage 09 Verify line 47** ("for each revised output, rerun its own stage's Verify against its inputs") stalls in *every* draft-in draft revision — both Case (a) (prose draft in stage 07) and Case (c2) (action-only draft in stage 06) — because rerunning stage 07's or stage 06's Verify demands unbuilt upstream sheets with no draft-in rule.
   **Grounds:** Walked Case (a) (stage 09 Verify) and Case (c2) (action-only draft through stages 01, 06, 07, 08, 09); `stages/how-stages-work.md` lines 31 & 43.
   **Connection:** Leaves action-only brought-in drafts with no way through stages 01, 06, 07, 08, or 09, and breaks stage 09's own Verify step even on a standard prose manuscript in Case (a).
   **Verdict:** **bears**.

5. **[must-change]** **Target:** `stages/09-revision/references/revision-log.md` line 37; `stages/how-stages-work.md` line 60; `stages/02-characters/CONTEXT.md` line 15; `stages/03-world-and-symbols/CONTEXT.md` line 16; `stages/04-plot/CONTEXT.md` line 17; `stages/05-scene-weave/CONTEXT.md` line 17; `stages/06-scenes/CONTEXT.md` line 16; `stages/07-dialogue/CONTEXT.md` line 16.
   **Defect:** Spoiler-free mode fails to propagate across stages in three ways:
   - (a) Switching spoiler-free mode on via feedback (`revision-log.md` line 37) records the rule only in `feedback-N.md` ("record that rule here"). Neither stage 08 nor stages 02–07 load `feedback-N.md`; `brief-v1.md` still says "normal review stops"; and nothing tells stage 09 to log the active mode switch in `project-log.md` immediately or states that a feedback switch overrides `brief-v1.md` until `brief-v2.md` is written.
   - (b) Stages 02–07 do not load `_config/writer.md` question 14 (only stages 01, 08, 09 do), and stages 06–07 do not load `brief-vN.md` at all. Under `how-stages-work.md` line 31 ("loads exactly the files and sections its Inputs table names, and no others"), a standing Q14 setting or mid-run switch is invisible to stages 02–07.
   - (c) `how-stages-work.md` line 60 says workshop-decided held choices are "recorded in the revision log", which does not exist during stages 01–07 (e.g. stage 03 in Case (a)).
   **Grounds:** Walked Case (a) (stage 03 in spoiler-free mode) and Case (c3) (feedback switching spoiler-free mode on before stage 08 or stage 03).
   **Connection:** Spoilers cannot be undone. Recording active spoiler-free mode immediately in `project-log.md` (which every stage already reads first, with explicit precedence over older `brief-vN.md`), loading Q14 in stages 02–07 (or making Q14 readable by every stage in `how-stages-work.md`), and naming where stages 01–07 record held story choices (that stage's output and/or `project-log.md`, alongside the rejected alternative) closes the leak.
   **Verdict:** **bears**.

6. **[must-change]** **Target:** `stages/08-critique/CONTEXT.md` lines 14, 15, 30 & 46; `stages/08-critique/references/critique-rounds.md` lines 11–13; `stages/09-revision/CONTEXT.md` lines 12, 15 & 44.
   **Defect:** Two draft-in hand-off breaks between stages 03, 08, and 09:
   - (a) `stages/how-stages-work.md` line 42 promises "Every critique (stage 08) and revision (stage 09) checks against this baseline and `draft-v1`", yet neither stage 08 `Process` step 2 (line 30) nor `critique-rounds.md` section 1 (line 11) tells the round setup to assign a critic to Voice and preservation in draft-in mode on a revised draft, while stage 08 Verify line 46 lets any critic mark it `*not run*` ("if outside this critic's kind"). On `_config/writer.md` Q11's default critics (logic/rules; theme/hard-to-vary; care/suspense/structure), every critic can opt out, leaving only stage 09 (the reviser) checking its own preservation. Meanwhile, loading `draft-v1` into every critic's Inputs (line 14) conflicts with a cold-first-reader critic who must read only the revised draft blind.
   - (b) Stage 01 line 44 anticipates `01 -> planning stage (e.g. 03) -> 08 or 09`. Yet stage 08 line 15 loads earlier outputs only when the target's markers name them (`draft-v1` has no markers, so `01 -> 03 -> 08` cannot load `world-v1.md`), and stage 09 line 15 loads earlier outputs only when critique findings trace to them (so `01 -> 03 -> 09`, the exact path *The Unseen Orchard* used, has no Inputs row to load `world-v1.md` and no findings for Verify line 44).
   **Grounds:** Walked Case (a) (`01 -> 03 -> 08/09`); `CLAUDE.md` rule 1 ("Nobody grades their own work") & rule 2 ("Not run is never passed"); `stages/how-stages-work.md` lines 31 & 42; `stages/01-brief-and-premise/CONTEXT.md` line 44.
   **Connection:** Without (a), stage 08 fails to enforce independent voice/preservation review on default rounds (or spoils a blind cold reader with `draft-v1`). Without (b), Case (a) stalls right after stage 03 finishes `world-v1.md`. Fix: in stage 08 Process step 2 / `critique-rounds.md` section 1, require at least one critic in a draft-in round on a revised draft to check Voice and preservation against `draft-v1` (while keeping `draft-v1` out of any blind cold-reader critic's brief); and in stages 08 & 09 Inputs, include any planning output built in draft-in mode (e.g. `world-vN.md`) when critiquing or revising against the brief/plan, noting in stage 09 Verify that an initial brief/plan-driven revision logs against the brief/feedback rules when no critique round ran yet.
   **Verdict:** **bears**.

7. **[should-change]** **Target:** `stages/01-brief-and-premise/CONTEXT.md` lines 42 & 44 (Process steps 4 and 5).
   **Defect:** Execution order is inverted in draft-in mode: step 4 tells the agent to write `brief-v1.md` using worksheet section 2 (which requires measuring `## Voice and preservation baseline` directly from `draft-v1`), before step 5 saves the draft as `draft-v1.md` and declares draft-in mode.
   **Grounds:** Walked Case (a) obeying `stages/how-stages-work.md` line 33 ("works through its Process, in order"); `stages/01-brief-and-premise/references/premise-worksheet.md` line 32.
   **Connection:** Forces the agent to jump ahead to step 5, save `draft-v1`, then return to step 4. Put saving a brought-in draft (and entering draft-in mode) before writing `brief-v1.md`.
   **Verdict:** **bears**.

8. **[should-change]** **Target:** `CONTEXT.md` line 15; `stages/01-brief-and-premise/CONTEXT.md` line 47 (step 8).
   **Defect:** (a) `CONTEXT.md` line 15 ends the combined "bring your own premise or draft" cell with `(its step 5; draft-in mode)`, reading as if a brought-in premise also enters draft-in mode (contradicting `how-stages-work.md` line 41 and stage 01 line 44). (b) Stage 01 step 8 (line 47) adds `(in draft-in mode, brief-vN.md)` to `brief-vN.md, pitches-vN.md and premise-vN.md`, still leaving a brought-in premise (which has no `pitches-vN.md`) uncovered.
   **Grounds:** Walked Case (c1) (bringing own premise); `stages/how-stages-work.md` line 41; `stages/01-brief-and-premise/CONTEXT.md` line 44.
   **Connection:** Writing `(its step 5; draft-in mode for a draft)` in `CONTEXT.md` and `(brief-vN.md only in draft-in mode; brief-vN.md and premise-vN.md for a brought-in premise)` in stage 01 step 8 removes both ambiguities.
   **Verdict:** **bears**.

9. **[should-change]** **Target:** `stages/01-brief-and-premise/references/premise-worksheet.md` lines 32–37; `stages/how-stages-work.md` line 42; `stages/09-revision/CONTEXT.md` line 46.
   **Defect:** Three mismatches around the baseline:
   - (a) `premise-worksheet.md` line 32 and `how-stages-work.md` line 42 name `brief-v1.md`, whereas stages 02–09 read `brief-vN.md (highest N)`. Nothing says `brief-v2.md` (written after feedback, `premise-worksheet.md` line 28) must carry forward the baseline measured from `draft-v1`.
   - (b) `premise-worksheet.md` lines 34–37 prescribe prose-PDF specifics ("mean words per paragraph and count of unusually long paragraphs", "chapter endings", "for a PDF, inspect its fonts", unconditional "beyond raw word count") without marking prose metrics as medium-dependent (the workshop's own mediums in `_config/writer.md` Q1 include screenplays and TV scripts, plus action-only stage-06 drafts) or adding stage 01 Verify line 64's "where relevant" qualifier to item 5.
   - (c) `stages/09-revision/CONTEXT.md` line 46 lists specific checks after the em-dash ("untouched boundaries unedited, sacred lines verified verbatim, formatting rules checked, and any text counts run on story text only") that drop prose voice/rhythm (paragraph shape, register, recurring constructions) and judgment signals (items 2 and 5 of `premise-worksheet.md` section 2).
   **Grounds:** Walked Case (a) stage 09, Case (c2) action-only draft, Case (c3) `brief-v2.md`; hard-to-vary swap test; `_config/writer.md` line 9.
   **Connection:** Carry the baseline in every `brief-vN.md` (measured once from `draft-v1`), state what is held across media (with prose/PDF details marked as examples for prose/PDF drafts, plus recording any length cutoff used), qualify item 5 with "where relevant", and have stage 09 Verify check all items of the baseline rather than an incomplete restatement.
   **Verdict:** **bears**.

10. **[should-change]** **Target:** `stages/05-scene-weave/CONTEXT.md` lines 15 & 29.
    **Defect:** Inputs line 15 loads `brief-vN.md (highest N; required in draft-in mode)` with `rules, avoid list, and in draft-in mode the Voice and preservation baseline`, while Process step 1 (line 29) says to read `brief-vN.md` only "In **draft-in mode**, also read `brief-vN.md`".
    **Grounds:** Walked Case (b) (nearest innocent neighbour: lock-keeper short story); `stages/how-stages-work.md` line 31; compare stages 02–04 (which always load and read `brief-vN.md`).
    **Connection:** In a scratch run, stage 05 either loads a file Process step 1 never reads or stalls on whether `(required in draft-in mode)` means optional outside draft-in mode. Align line 15 and line 29 (either always read `brief-vN.md` as in stages 02–04, or mark line 15 `(highest N; draft-in mode only)`).
    **Verdict:** **bears**.

11. **[should-change]** **Target:** `stages/how-stages-work.md` lines 43 & 60; `stages/01-brief-and-premise/CONTEXT.md` line 44; `stages/02`–`05` `CONTEXT.md` (Inputs & Verify); `stages/08-critique/CONTEXT.md` lines 14, 17, 51; `stages/09-revision/CONTEXT.md` lines 17, 18, 30, 52; `_config/writer.md` line 25.
    **Defect:** Rule duplication, naming drift, and a narrow filename glob:
    - (a) Three names for one mode: `spoiler-free (surprise) mode`, `spoiler-free mode` (stages 08 line 17, 09 line 18), and bare `surprise mode` (stage 01 line 44, `_config/writer.md` line 25, `how-stages-work.md` line 60) — where `surprise` already carries three owner-theory senses (`owner-terms.md` section 11.4).
    - (b) The draft-in Verify rule is pasted verbatim into four contracts (stages 02 line 50, 03 line 47, 04 line 48, 05 line 41), and the spoiler-free review-stop rule is restated in `how-stages-work.md` line 60, stage 08 line 51 (already drifted: Finding 1), and stage 09 line 52, while stages 01–07 omit it.
    - (c) The glob `draft-vN*.md` / `draft-v1*.md` matches `draft-v1.md` and `draft-v1-part1.md`, but not the episodic split pattern `draft-ep03-vN.md` named in `stages/06-scenes/CONTEXT.md` line 38 and `stages/07-dialogue/CONTEXT.md` line 41.
    **Grounds:** `CLAUDE.md` line 14 ("use that one word for that one thing"), `owner-terms.md` section 11.4 & H23, `CONTEXT.md` line 60 ("each rule is kept there only"), `stages/how-stages-work.md` line 3 ("so each rule has one home"), `27 Corrections.md` line 16 (Kind 6).
    **Connection:** Use one name (`spoiler-free mode`, glossed once in `how-stages-work.md` section 3 as "what the writer called keeping it a surprise"), point briefly to `stages/how-stages-work.md` sections 2 and 3 instead of copying full rule clauses into contracts, and refer to `draft-vN` / `draft-v1` (including split files) rather than `draft-vN*.md`.
    **Verdict:** **bears**.

12. **[note]** **Target:** `stages/how-stages-work.md` line 42; `stages/03-world-and-symbols/CONTEXT.md` lines 13 & 28; `stages/08-critique/CONTEXT.md` line 46; `stages/09-revision/CONTEXT.md` line 46.
    **Defect:** Bare-shortening "Voice and preservation baseline" to `baseline` (`how-stages-work.md` line 42, stage 08 line 46, stage 09 line 46) — and placing it above "the genre's baseline" in stage 03 (lines 13 & 28) — reuses the Implied World theory's frozen key term `Baseline` ("what the audience assumes by default. That's the real world plus the habits of the genre", `sources/implied-world-theory.md` line 12; `owner-terms.md` section 2.1).
    **Grounds:** `sources/implied-world-theory.md` line 12; `owner-terms.md` section 2.1 & H23; `CLAUDE.md` line 14.
    **Connection:** Keep the full phrase `voice and preservation baseline` everywhere (never bare `baseline`), or use a distinct noun such as `voice and preservation record/profile`, so stage 03 and stage 08 story-world critics never conflate the two.
    **Verdict:** **bears**.

13. **[note]** **Target:** `_config/writer.md` lines 5 & 25; `stages/01-brief-and-premise/CONTEXT.md` line 39.
    **Defect:** Question 14 is marked `(*to confirm*)`, and `_config/writer.md` line 5 says to ask the writer the first time any `*to confirm*` answer would decide something (S16). On Case (b) (a brand-new story from scratch, where the writer must see rival premises to choose one in step 7), a literal reader may stall on whether to ask about Q14 before starting stage 01.
    **Grounds:** Walked Case (b) stage 01 step 1; `_config/writer.md` lines 5 & 25; `_config/questionnaire.md` line 27; `22 Questions` S16.
    **Connection:** Clarifying in Q14 that the default stopgap ("normal review stops; turns on when asked") stays quiet unless a request/feedback mentions spoilers or surprise prevents noise on innocent-neighbour scratch runs. (Also pre-existing note: stage 01's Inputs lines 23–35 still load 13 scratch-premise craft/theory files in draft-in mode even when no rivals are written.)
    **Verdict:** **bears** (minor; **held if** S16 is settled to ask on every `*to confirm*` row).

14. **[note]** **Target:** `stages/01-brief-and-premise/CONTEXT.md` lines 70–72; `stages/01-brief-and-premise/references/premise-worksheet.md` line 36; `stages/how-stages-work.md` line 60.
    **Defect:** In draft-in mode with spoiler-free mode on (Case (a)), `brief-v1.md` stores sacred closing lines (item 4), while stage 01's Review stop invites the writer to read and edit `brief-vN.md` in place.
    **Grounds:** Walked Case (a) stage 01 review stop.
    **Connection:** One line in `how-stages-work.md` section 3 noting that in spoiler-free mode the writer does not open stage outputs (including `brief-vN.md`'s sacred lines) at review stops — relying on the spoiler-free summary until ready to read — prevents accidental self-spoiling.
    **Verdict:** **bears**.

*(Stall list, hard-to-vary marks, pointers/theory/kept-cases checks, and what was not checked recorded in Round 1 conversation transcript; final verdict: Passed after changes.)*

---

## Round 2 (narrow second look) reviewer report (verbatim)

# Narrow Second Look: Staged Draft-in & Spoiler-Free Mode Changes (16 files)

Checked `round2-delta.diff` and the full staged changes (`git diff --cached`, 16 files) against all 14 findings from round 1, verified term/pointer/glob consistency across `CONTEXT.md`, `_config/`, and `stages/` (excluding `output/`), ran `python3 .claude/skills/add-source/scripts/check_maps.py .` (`TOTAL problems: 0`, exit 0), and re-walked Cases (a), (b), (c1), (c2), and (c3) on the edited lines. No files were edited.

## Findings 1–14 Verification

All 14 findings are answered in content with no missed spots or partial fixes:

1. **Finding 1 (must-change — stage 08 dropped "what was not checked"):** Applied. `stages/08-critique/CONTEXT.md` line 51 now points to `stages/how-stages-work.md`, section 3, whose line 64 explicitly requires `what was checked, and what was not checked (CLAUDE.md, rule 2)`.
2. **Finding 2 (must-change — unscoped "Any choice"):** Applied. `stages/how-stages-work.md` line 65, `_config/questionnaire.md` line 27, `stages/09-revision/CONTEXT.md` line 30, and `stages/09-revision/references/revision-log.md` line 17 all scope workshop-decided choices to **story choices** (whose question would reveal story content), explicitly keeping request ambiguity (`CLAUDE.md` C17), helper/cost limits (`_config/writer.md` Q9/Q13, S16), git committing (Q12), and project-vs-standing feedback rules asked as normal.
3. **Finding 3 (must-change — stage 01 review-stop contradiction):** Applied. The bypass was removed from `stages/01-brief-and-premise/CONTEXT.md` step 5 (line 44); step 8 (line 47) now stops under `stages/how-stages-work.md`, section 3; and the single guarded rule lives in `stages/how-stages-work.md` lines 37 and 60 (gated on no C17 doubt and no unconfirmed S16 helper/cost stopgaps).
4. **Finding 4 (must-change — stage 06/07 draft-in breaks & action-only paths):** Applied. Stage 01 step 3 (line 41) routes full drafts to stage 07 and action-only drafts to stage 06; stage 08 line 14 and stage 09 line 17 accept `draft-v1` from either folder; `stages/06-scenes/CONTEXT.md` and `stages/07-dialogue/CONTEXT.md` now have full draft-in Inputs, Process step 1, and Verify fallback (`how-stages-work.md`, section 2); and stage 09 Verify line 47 reruns each revised stage's Verify under `how-stages-work.md`, section 2.
5. **Finding 5 (must-change — spoiler-free propagation & stages 01–07 held choices):** Applied. `Spoiler-free mode: on` is written immediately into `project-log.md` at stage 01 step 3 (line 41) and on mid-run feedback (`revision-log.md` line 37), with explicit precedence over older `brief-vN.md` (`how-stages-work.md` line 63); all stages 02–09 now load `_config/writer.md` question 14 (and stage 01 loads `all`); and `how-stages-work.md` line 65 places stages 01–07 held story choices in a `Held story choices` note inside that stage's output (count only in `project-log.md`).
6. **Finding 6 (must-change — stage 08 preservation assignment, blind cold reader, and stage 03 -> 08/09 hand-off):** Applied. `stages/08-critique/CONTEXT.md` (lines 13–15, 30, 46), `stages/08-critique/references/critique-rounds.md` (lines 11, 13), `stages/how-stages-work.md` (line 42), and `stages/09-revision/CONTEXT.md` (lines 15, 44) require at least one critic in each draft-in round on a revised draft to check the voice and preservation record against `draft-v1`, keep `draft-v1`/brief/plan out of a blind first reader's brief, load draft-in planning outputs (`world-vN.md`, `plot-vN.md`, etc.) in stages 08 and 09, and cover an initial brief/feedback/plan-driven revision in stage 09 Verify line 44.
7. **Finding 7 (should-change — stage 01 step 4/5 inversion):** Applied. Saving `draft-v1` moved to step 3 (`stages/01-brief-and-premise/CONTEXT.md` line 41), with pointers updated in `CONTEXT.md` line 15 (`steps 3 and 5`) and `stages/how-stages-work.md` line 41 (`step 3`). Verified zero stale `step 5` draft-in pointers remain.
8. **Finding 8 (should-change — own-premise precision):** Applied (`CONTEXT.md` line 15: `draft-in mode for a draft`; stage 01 step 8 line 47: `in draft-in mode, brief-vN.md only; for a brought-in premise, brief-vN.md and premise-vN.md`).
9. **Finding 9 (should-change — `brief-vN.md` carry-forward, medium-generalized record, stage 09 full check):** Applied (`premise-worksheet.md` lines 32–37; `how-stages-work.md` line 42; stage 01 Verify line 64; stage 09 Verify line 46).
10. **Finding 10 (should-change — stage 05 `brief-vN.md` alignment):** Applied (`stages/05-scene-weave/CONTEXT.md` lines 15 & 29 now match stages 02–04).
11. **Finding 11 (should-change — naming, deduplication, globs):** Applied. Single name `spoiler-free mode` throughout (glossed once in `how-stages-work.md` line 62); zero remaining `surprise mode` or `draft-vN*`/`draft-v1*` globs (verified via grep); Verify and Review stop clauses in stages 02–09 point concisely to `stages/how-stages-work.md` sections 2 and 3.
12. **Finding 12 (note — `baseline` collision):** Applied cleanly by renaming to `voice and preservation record`. Verified via grep: only the 4 Implied World theory uses of `baseline` remain across `CONTEXT.md`, `_config/`, and `stages/`.
13. **Finding 13 (note — Q14 `*to confirm*` quiet on normal runs):** Applied (`_config/writer.md` line 25).
14. **Finding 14 (note — don't invite writer to open `brief-vN.md`/outputs in spoiler-free mode):** Applied (`stages/how-stages-work.md` line 64).

## Re-Walk & Check for New Issues

- **Cases (a), (b), (c1), (c2), (c3) re-walked on edited lines:** Zero stalls and zero contradictions. Every hand-off (`01 -> 03 -> 09 -> 08 -> 09`, scratch lock-keeper run, own-premise run, action-only draft through `01 -> 06 -> 07 -> 08 -> 09`, and mid-run feedback activating spoiler-free mode) now runs cleanly end to end.
- **Two minor non-blocking notes (recorded open; no changes required):**
  1. `stages/how-stages-work.md` line 37 says `(unless the writer explicitly waives intermediate stops for a run: section 3)` while line 60 says `only when the writer's request explicitly names the later stages to run through` — slight phrasing difference, already safely guarded in practice by the C17 doubt check in the same sentence.
  2. `stages/07-dialogue/CONTEXT.md` line 17 lists `draft-vN (draft-in mode only: in stage 07's output folder, including split files)`; on a first pass over an action-only draft brought into stage 06 (Case (c2)), stage 06's `draft-v1` is already loaded by line 12 and stage 07's folder has no `draft-vN` yet (clear in context; adding "if present" would be minor polish only).

## What Was Not Checked

Same bounds as round 1: no live multi-agent helper/critic runs, no commit-gate / `test_checks.py` / `overlap_check.py` runs (stages and `_config/` are outside the gate per S15), and no reading of `kept-cases/` bodies/answers.

## Final Verdict

**Passed.** All 6 must-change findings, 5 should-change findings, and 3 notes are resolved cleanly with no new defects introduced.
