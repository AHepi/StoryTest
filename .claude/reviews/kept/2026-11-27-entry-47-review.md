# Entry 47 review record: stages 08–09 anti-gaming upgrade and exact-edit script

- **Date:** 27 November 2026
- **Scope:** `stages/how-stages-work.md`, `stages/01-brief-and-premise/CONTEXT.md`, `stages/01-brief-and-premise/references/premise-worksheet.md`, `stages/08-critique/CONTEXT.md`, `stages/08-critique/references/critique-rounds.md`, `stages/09-revision/CONTEXT.md`, `stages/09-revision/references/revision-log.md`, `stages/09-revision/scripts/apply_exact_edits.py`, `stages/09-revision/scripts/test_apply_exact_edits.py`.
- **Note on scope:** `stages/` is not yet enforced by the commit gate (owner question S15), so this independent review is recorded here on trust, with a trace, per `CLAUDE.md` rule 1.
- **Book text:** none added.
- **Reviewer:** Stage 08-09 & Script Reviewer (`research` subagent `3d3aebaf99cef26dfe7ac7691b5642fc`, read-only, combining `use-tester`, `theory-checker`, and script-review roles).
- **Round 1 verdict:** Passed after changes (7 must-change, 5 should-change, 1 note). All 13 findings applied.
- **Round 2 (narrow second look) verdict:** Passed (2 minor non-blocking script edge-case notes recorded open per `reviews-and-briefs.md` section 4).

---

## Round 1 reviewer report (verbatim)

# Independent Review (use-tester + theory-checker + script-review): Staged Stages 08–09 Anti-Gaming Upgrade

Reviewed `git diff --cached` across all 7 staged files (`stages/01-brief-and-premise/references/premise-worksheet.md`, `stages/08-critique/CONTEXT.md`, `stages/08-critique/references/critique-rounds.md`, `stages/09-revision/CONTEXT.md`, `stages/09-revision/references/revision-log.md`, `stages/09-revision/scripts/apply_exact_edits.py`, `stages/09-revision/scripts/test_apply_exact_edits.py`), plus full surrounding contracts (`stages/how-stages-work.md`, `_config/writer.md`, `stages/01`, `03`, `06`, `07` contracts & references, `CONTEXT.md`, `README.md`), `CLAUDE.md`, `.claude/agents/use-tester.md`, `.claude/agents/theory-checker.md`, `.claude/skills/error-correction/references/owner-terms.md`, `27 Corrections.md`, `38 Findings - what the revision rounds say about the process.md`, `22 Questions - meanings only you can settle.md`, and `kept-cases/` titles and "Aimed at" lines only. No repository file was edited.

**Checks run:**
- `python3 stages/09-revision/scripts/test_apply_exact_edits.py -v` -> 11/11 tests OK.
- `python3 .claude/skills/add-source/scripts/check_maps.py` -> `TOTAL problems: 0`.
- `python3 .claude/skills/error-correction/scripts/run_all_checks.py` -> all run checks passed (`copying from books`: NOT RUN).
- `apply_exact_edits.py --count` on real `stages/07-dialogue/output/unseen-orchard/draft-v1-part*.md` and `draft-v8-part*.md` -> ran cleanly on standard `## N. Title` drafts.
- 14 adversarial edge-case tests against `apply_exact_edits.py` in memory / ephemeral `TemporaryDirectory` -> reproduced the script defects below.
- `kept-cases/` check (01–11 titles and "Aimed at" lines only): **0 kept-case answers leaked** into any staged text or test fixture.
- Owner-theory terms (`owner-terms.md`) and named theory cases (Hitchcock's bomb under the table, Joffrey, *Psycho*, "the door dilated", *Chronicle of a Death Foretold*): **0 owner-term misuses or contradictions** of the four narrative theories (`who knows what` avoids H7; `voice and preservation record` and `spoiler-free mode` stay clean). All updated section/item pointers (`revision-log.md` section 1 items 2, 4, 6; `critique-rounds.md` sections 1, 3; `premise-worksheet.md` section 2; `38 Findings` proposals 3a, 4a, 4b, 5) land on the right headings/items.

## Numbered Findings (Round 1)

1. **[must-change]** **Target:** `stages/09-revision/scripts/apply_exact_edits.py` lines 330–334 (and `stages/09-revision/scripts/test_apply_exact_edits.py` docstring line 10).
   **Defect:** Literal string `sacred_lines` checks `if item in target_text:`, bypassable via `## Verify` echo or appended text; untested.
   **Verdict:** **bears**.
2. **[must-change]** **Target:** `stages/09-revision/scripts/apply_exact_edits.py` lines 107–110, 367–399, 539–571.
   **Defect:** Dict overwrite silently drops duplicate `##` headings; prefix collision blocks `## Chapter 1` vs `## Chapter 10`; `--count --section` silently sums colliding prefixes and exits 0 on 0 matches.
   **Verdict:** **bears**.
3. **[must-change]** **Target:** `stages/09-revision/scripts/apply_exact_edits.py` lines 202–207, 247–259, 494–503; `stages/09-revision/CONTEXT.md` line 47.
   **Defect:** Zero-repeat check status never printed in receipt; no-op edits (`find == replace`) accepted as applied.
   **Verdict:** **bears**.
4. **[must-change]** **Target:** `stages/08-critique/CONTEXT.md` lines 11, 30–32, 44–45; `stages/08-critique/references/critique-rounds.md` lines 22–23, 43–46.
   **Defect:** `project-log.md` (and `feedback-N.md` items 2–5, revision-header notes, `## Verify`) leaked to blind critics; blind critics stalled on section 3 tracing.
   **Verdict:** **bears**.
5. **[must-change]** **Target:** `stages/09-revision/references/revision-log.md` lines 23–24; `stages/09-revision/CONTEXT.md` line 32.
   **Defect:** Direct clash between Escalation of repeated points and Final-round stopping rule on Round 2 under Q11's default 2-round cap.
   **Verdict:** **bears**.
6. **[must-change]** **Target:** `stages/08-critique/CONTEXT.md:17`, `critique-rounds.md:25, 27`, `stages/09-revision/CONTEXT.md:24, 28–41, 50`, `revision-log.md:31`.
   **Defect:** `Narrow prose regression check` straddled stages 08 and 09 without a Process step, independence/Q9/Q11 rule, output filename, non-overwriting loop-back, or Stage 08 diff input.
   **Verdict:** **bears**.
7. **[must-change]** **Target:** `stages/09-revision/CONTEXT.md:47, 50`; `revision-log.md:32`.
   **Defect:** Stage 09 Verify stalled on revised planning files and pitches (missing `premise-vN.md` too), and Verify line 50 was unscoped.
   **Verdict:** **bears**.
8. **[should-change]** **Target:** `stages/09-revision/scripts/apply_exact_edits.py:40, 124–130`.
   **Defect:** No-`##` drafts stripped full-italic/bold story paragraphs; external `[from: ...]` markers on header notes counted as story text; `VERIFY_HEADING` could truncate `## Verify the Alibi`.
   **Verdict:** **bears**.
9. **[should-change]** **Target:** `stages/09-revision/scripts/apply_exact_edits.py` (relative paths, dangling symlinks, sequential line label & stale comment, uncaught input-validation tracebacks, dead variable, missing `--help` schema, test gaps).
   **Verdict:** **bears**.
10. **[should-change]** **Target:** `critique-rounds.md:16`, `stages/09-revision/CONTEXT.md:36`, `revision-log.md:25`.
    **Defect:** Missing 4th verdict bucket (`taste/held/deferred`), ambiguous >50% denominator, and missing independence/writer-approval guard when Stage 09 judges critic records.
    **Verdict:** **bears**.
11. **[should-change]** **Target:** `stages/how-stages-work.md:65`.
    **Defect:** Shared spoiler-free non-story choices list out of sync with unmet original goals / trade-offs.
    **Verdict:** **bears**.
12. **[should-change]** **Target:** `stages/08-critique/` & `stages/09-revision/` prose.
    **Defect:** Technical jargon (`LLM`, `deterministic`, `proxy metrics`, `regression`, `unified diff`, unglossed `JSON`) and three names instead of workshop's `moving the goalposts` (`CLAUDE.md:14`).
    **Verdict:** **bears**.
13. **[note]** **Target:** Minor scoping & consistency polish across stage 01, 08, 09 Inputs/Outputs/Process.
    **Verdict:** **bears**.

*(Full Round 1 stall list and hard-to-vary table recorded in Round 1 conversation transcript; final verdict: Passed after changes.)*

---

## Round 2 (narrow second look) reviewer report (verbatim)

# Narrow Second Look: Staged Stages 08–09 Anti-Gaming Upgrade (9 files)

Inspected `/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ef2c6cfa-651a-4a14-ae80-a75bfc078983/scratch/item2-round2-delta.diff` and the full staged changes (`git diff --cached`, 9 files: `stages/how-stages-work.md`, `stages/01-brief-and-premise/CONTEXT.md`, `stages/01-brief-and-premise/references/premise-worksheet.md`, `stages/08-critique/CONTEXT.md`, `stages/08-critique/references/critique-rounds.md`, `stages/09-revision/CONTEXT.md`, `stages/09-revision/references/revision-log.md`, `stages/09-revision/scripts/apply_exact_edits.py`, `stages/09-revision/scripts/test_apply_exact_edits.py`). No repository file was edited.

**Checks run:**
- `python3 stages/09-revision/scripts/test_apply_exact_edits.py -v` -> **12/12 tests OK**.
- `python3 .claude/skills/add-source/scripts/check_maps.py` -> `TOTAL problems: 0`.
- `python3 .claude/skills/error-correction/scripts/run_all_checks.py` -> all run checks passed (`copying from books`: NOT RUN).
- Re-ran all Round 1 adversarial tests against `apply_exact_edits.py` plus 9 new edge-case tests (`N1`–`N9`) in memory / ephemeral `TemporaryDirectory`.
- Grepped all 7 staged markdown files for residual technical jargon (`deterministic`, `LLM`, `proxy`, `regression`, `goalpost migration`, `redefinition`, `unified diff`): **0 hits**.
- Re-walked Cases (a), (b), and (c) across the edited lines.

---

## Findings 1–13 Verification

All 13 findings (7 must-change, 5 should-change, 1 note) are genuinely resolved in content:

1. **Finding 1 (must-change — literal `sacred_lines` bypass):** Resolved (`apply_exact_edits.py:474–508`). Literal entries now check `story_exact_entries` (extracted from story text before `## Verify`, excluding header notes) for exact line/paragraph match by default, with opt-in `{"text": ..., "match": "substring"}` still scoped to story text. Both `## Verify`-echo and appended-text bypasses failed as required on re-test.
2. **Finding 2 (must-change — duplicate `##` headings, prefix collisions, `--count --section`):** Resolved (`apply_exact_edits.py:96–129, 551–594, 738–773`). List-based `split_sections_by_h2` preserves duplicates (duplicate `## Interlude` caught); exact-first + alphanumeric-boundary matching handles `## Chapter 1` vs `## Chapter 10` and `## Act I` vs `## Act II` cleanly; `--count --section` prints `[sections: ...]` and exits 1 on zero matches (including multi-file split drafts, verified in Test N9). *(See minor open notes 1–2 below.)*
3. **Finding 3 (must-change — zero-repeat receipt & no-op edits):** Resolved (`apply_exact_edits.py:304–306, 354–384, 688–689`). No-op `find == replace` is refused in both `one` and `all` modes; every `match='all'` edit prints explicit `zero-repeat=0 remaining`, `zero-repeat=NOT RUN (disabled by order)`, or `zero-repeat=NOT RUN (replacement contains find)`.
4. **Finding 4 (must-change — blind critics' `project-log.md` leak & tracing stall):** Resolved (`stages/08-critique/CONTEXT.md:11–13, 32, 45`; `critique-rounds.md:22–23, 48`; `stages/09-revision/CONTEXT.md:33`). Both blind critics now exclude `project-log.md`, `feedback-N.md` items 2–5, revision-header notes, and `## Verify`; blind critics record visible markers and mark upstream tracing *not run (excluded by blind input boundary; traced in stage 09)*, which Stage 09 step 4 traces before editing.
5. **Finding 5 (must-change — Escalation vs Final-round stopping clash on Round 2):** Resolved (`stages/09-revision/references/revision-log.md:23–24`). Escalation is explicitly scoped to before the final round, and Final-round stopping explicitly takes precedence on the final round (flagging any unresolved repeated point prominently as a writer choice — or in spoiler-free mode asking as a non-story scope question whether to authorise one more round, or logging both sides without reopening the draft).
6. **Finding 6 (must-change — `Narrow prose regression check` straddling Stages 08 & 09):** Resolved cleanly via Option (ii) and renamed **narrow new-prose check** (`stages/08-critique/CONTEXT.md:17, 31`; `critique-rounds.md:25, 27`; `stages/09-revision/CONTEXT.md:24, 50`; `revision-log.md:31`). Lives strictly in Stage 08 as a normal independent critic (inheriting Stage 08 outputs, independence, and Q9/Q11 rules), with Stage 09's line-by-line diff added to Stage 08 Inputs line 17; Stage 09 Verify line 50 only flags substantial new prose for the next Stage 08 round (or notes `independent check on new prose: not run` and asks the writer on final handover), and states `not run (cuts and local phrase edits only — exact-edit script diff verified)` for cuts/phrase edits.
7. **Finding 7 (must-change — Stage 09 Verify stalling on planning files/pitches):** Resolved (`stages/09-revision/CONTEXT.md:47, 50`; `revision-log.md:32`). Verify line 47 now branches cleanly for revised planning files (`brief`, `premise`, `cast`, `world`, `plot`, `scene-weave`), pitches, and whole-scene rebuilds via explicit `diff`; Verify line 50 is scoped to `(when revising a draft)`; `premise-vN.md` is added to `revision-log.md:32`.
8. **Finding 8 (should-change — no-`##` drafts, external header markers, `VERIFY_HEADING`):** Resolved (`apply_exact_edits.py:44, 131–139, 174, 215–228`). Verified live: `## Verify the Alibi` is not truncated; `**bold**` and post-first-paragraph full-italic lines in no-`##` drafts are counted and checked by `forbidden_patterns`; external markers on header notes (`*Revised...* [from: ...]`) are stripped as header notes.
9. **Finding 9 (should-change — relative paths, dangling symlinks, line-number label, input validation, `--help` schema, tests):** Resolved (`apply_exact_edits.py:48–71, 286–317, 351, 388–403, 412–451, 609–645, 685`; `test_apply_exact_edits.py`). Preferring `base_dir` over CWD (while still falling back cleanly to repo-root relative paths, verified in Test N8), `os.path.lexists` + `os.path.realpath`, accurate sequential line-number wording, clean validation on bad JSON/types/regexes, full schema in `--help`, and expanded unit tests all pass.
10. **Finding 10 (should-change — critic record 4th bucket, denominator, writer-approval guard):** Resolved (`critique-rounds.md:16`; `stages/09-revision/CONTEXT.md:36`; `revision-log.md:25`). All four buckets (`accepted`, `partial`, `taste/held/deferred`, `rejected-as-wrong`) + `total` are logged; threshold is unambiguously `rejected-as-wrong > half of total findings`; replacement is **proposed** to the writer as a non-story decision (never silently dropping a critic, especially a blind critic).
11. **Finding 11 (should-change — sync `stages/how-stages-work.md:65`):** Resolved (`stages/how-stages-work.md:65` now includes `unmet original goals or scope trade-offs (phrased without story content), and proposing a change to the critic lineup` among non-story choices still asked in spoiler-free mode).
12. **Finding 12 (should-change — `CLAUDE.md:14` plain words & unifying `moving the goalposts`):** Resolved across all modified markdown files (`AI fix verifier`, `script-run checks`, `stand-in measures`, `line-by-line diff (a file comparison showing only what changed)`, `narrow new-prose check`, JSON format glossed with `--help` pointer, and unified on `*moving the goalposts*` citing `.claude/skills/hard-to-vary/references/word-list.md`).
13. **Finding 13 (note — 5 polish items):** All 5 resolved (`stages/08-critique/CONTEXT.md:11–17, 21–22, 31`; `stages/01-brief-and-premise/CONTEXT.md:22`; `premise-worksheet.md:34`; `stages/09-revision/CONTEXT.md:40`).

---

## Re-Walk of Cases (a), (b), (c) & Minor Non-Blocking Open Notes

- **Cases (a), (b), and (c) re-walked on the edited lines:** Zero stalls, zero rule contradictions, zero jargon/term drift, and zero bypasses across all three scenarios.
- **Two minor non-blocking open notes in `apply_exact_edits.py`** (recorded open per `reviews-and-briefs.md` section 4; neither allows a bypass or corrupts output — both fail safe or print `0 words [sections: none]`):
  1. `apply_exact_edits.py:98–107` (`heading_matches_selector`): if someone passes an empty/whitespace-only selector (`""` or `"   "`) in `untouched_sections` or `--count --section ""`, `sel` becomes `""` and `sel[-1].isalnum()` raises `IndexError` (exits 1 without writing target). Adding `if not sel: return None` prevents the traceback.
  2. `apply_exact_edits.py:746–748` (`run_count_command`): checks `seen_per_selector` against `split_sections_by_h2(text)` before `## Verify` is stripped, so `--count file.md --section "## Verify"` prints `[sections: none]: 0 words` and exits `0` instead of `1`. Checking `counts["matched_headings"]` aligns it with `extract_story_paragraphs`.

## What Was Not Checked

Same bounds as Round 1: no live multi-agent helper/critic runs, no `test_checks.py` or `overlap_check.py` (no check/skill file modified; no books present/added), no reading of `kept-cases/` bodies, and no Windows-filesystem CRLF run.

## Final Verdict

**Passed.** All 7 must-change findings, 5 should-change findings, and 1 note are cleanly resolved with no new blocking defects or contradictions introduced (2 minor non-blocking script edge-case notes recorded open above).
