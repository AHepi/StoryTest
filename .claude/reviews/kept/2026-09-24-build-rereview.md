# Re-review of the error-correction build's first answers, 24 September 2026

What this is: the three re-reviewers' reports, word for word as each agent returned it, one after another. Each looked only at the edits made after the first review round (the difference between the reviewed state and the answered state), with the first round's findings. They made no edits; every experiment ran in scratch copies. How each finding was answered is in the build's review receipt. No book text is quoted in them. Kept for log entry 29.

---

## 1. theory-checker

## Theory-checker re-review of the entry 29 edits (content against the owner theories, the foundation and the records)

I read CLAUDE.md, the term sheet, the kinds table and C1–C15, the three kept first-round reports, findings-answered.md, and the diff `git -C …/rereview diff HEAD~1`. The live repository matches rereview HEAD for every file I compared. I made no edits. Checks were run in a scratch copy (`…/scratchpad/tc-copy`).

Overall: the edits answer most first-round findings in content, not just in wording. Two must-change items remain. The one that matters most is the owner-caught Catch order-word error: it has survived a third time, and four records now say the file is clean.

### Findings (target; defect; grounds; connection; verdict; severity)

**F1. Order words still in file 26, while the records call the search clean.**
- **Target:** `26 Test - The Catch - two versions.md`:
  - line 48: "Iona no longer works it out" (inside fault 1's table, the part that was tested)
  - line 74: "Her reason for going becomes…"
  - line 81: "B's puck scene breaks A's four-line rhythm"
  - line 106: "what B loses in Iona"
  - borderline: line 124 "B was trimmed".
- **Records that say the search is clean:** file 26 line 127; C1 line 36 ("finds only direction-free uses"; "put right through the reason for file 26"); S12 line 97 ("File 26 now gives its verdicts without assuming an order"); project story line 131 (title "every finding put right"), line 133, and status line 12 ("all their findings have been put right or answered").
- **Defect:** each phrase assumes B was made from A. The maker searched a fixed list of words ("cut … keeps"). It stopped at that list, which is the exact error C1's second paragraph records.
- **Grounds:** my `grep -n -i -E "no longer|becomes|breaks A's|loses"` output. error-correction SKILL.md line 193 ("Search the whole text…") and trap line 247 ("Stopping the search at what you noticed"). The owner's "I'm really not sure which". The maker's own grep, rerun, is literally clean, so the list is at fault, not the search.
- **Connection:** the owner is told for a third time that B came second, and is told the problem is fixed. The stage (the rig) is also at fault: the claim check (SKILL.md 193) and the reply check ("cuts", "adds", "restores") both give closed lists, and that is how the search stops early.
- **Verdict:** bears. **Severity:** must change.
- **What must change:**
  - Reword the four phrases.
  - Correct the four records.
  - Make the lists in the claim check and the reply check explicitly examples, and ask the agent to read every sentence that compares the two versions.
  - Record the recurrence in C1.

**F2. "Every finding of both notes has now been applied" is not true.**
- **Target:** file 26 line 126.
- **Unapplied finding 1:** the break test's N20 found the napkin ring optional in A, a second route, because of A:789, A:1022 and the bar. Line 89 still lists it without qualification under "carry these into A".
- **Unapplied finding 2:** N1's "pulls" found that bringing A:285 and A:590 into B, while B keeps B:873-875 and B:544-553, gives three routes to one job. Fault 1's fix (line 55, "bring these into B from A") carries no caveat.
- **Also unapplied:** N20's A:697 point.
- **Grounds:** the kept break-test JSON (`holds_it`, `pulls`, `new_wording`). A:789 reads "Nearly the whole charge. Nothing left for a second try."
- **Connection:** this is RC3's own defect, still present: the owner is told the correction follows the test, but it follows only part of it.
- **Verdict:** bears. **Severity:** must change. Apply these findings, or list them as unapplied with reasons.

**F3. C12 still credits the Gap theory with a warning it never gives.**
- **Target:** 27 Corrections.md line 122 (C12 Connection): "raising the emphasis the Gap theory warns gives the turn away".
- **Grounds:** Gap Part 2 §4 says emphasis sets which promise an open question carries. No passage warns that emphasis gives a turn away. This is CC2(a)'s wrong credit.
- **Connection:** C12's next paragraph says that credit was corrected, yet the record keeps it. A later theory-checker searching C12 (step 7) would take it as the theory's reading.
- **Verdict:** bears. **Severity:** should change.

**F4. The bomb is narrowed to "the theory's case of suspense".**
- **Target:** writing-rules-and-rivals.md line 9; C12 line 124; project story line 132 ("your case of suspense").
- **Grounds:** Gap line 59 uses the bomb for both schedules: "simply goes off … fifteen seconds of surprise"; "Show them the bomb first … suspense". The five-gaps table (Knowledge row) and Anticipation line 41 (the time term) use it too.
- **Connection:** the half that was dropped, the unshown bomb, is the theory's case of surprise. That is exactly the half the new surprise branch needs walked through it (F5).
- **Verdict:** bears. **Severity:** should change.

**F5. The planting rule and the theory's own surprise case.**
- **Target:** plot/references/reveals-and-withholding.md line 30.
  - Its first sentence requires every fact a later turn depends on to be noticeable beforehand.
  - Its surprise branch ("keep the showing light enough…") assumes there is a showing.
- **Grounds:** the Gap theory's surprise schedule is the bomb that "simply goes off" (line 59), with no showing at all. The Anticipation theory gives such threats their own rung: Shock, "arrives without warning" (line 25). Rule card step 4.
- **Connection:** walked through §2, the unshown bomb comes out as an unplanted turn.
- **Verdict:** does not bear yet. The test that settles it: decide whether §2 governs a turn meant as a shock.
  - If it does, the rule fails the theory's own case.
  - If it does not, say so (for example: "a shock needs no set-up and buys seconds").
- **Severity:** should change.
- **Minor, same line:** "(section 1)" points to a section that never mentions the bomb (it is in §3).

**F6. C12 names a catch the rule card does not carry.**
- **Target:** C12 line 126, "Now caught by … walking the theory's own cases through the rule for what each case is a case of".
- **Defect:** the rule card (writing-rules line 25) has no such step.
- **Connection:** the record claims a catch that isn't in place, so the stage that let C12's second error through is unchanged.
- **Verdict:** bears. **Severity:** should change: add the step to the card.

**F7. The plan cannot be written in the receipt before the change.**
- **Target:** error-correction SKILL.md line 158: "Plan, written down before changing anything … otherwise in the review receipt's 'Change' line".
- **Grounds:** reviews-and-briefs.md §2 steps 1 and 5, and review_receipt.py. `new` makes the receipt for the staged change, named by its fingerprint. The form's Change hint asks only for "what changed, and why".
- **Connection:** for every correction that is not a full one, the plan can only be written after the change. PF3's defect stands.
- **Verdict:** bears. **Severity:** should change.

**F8. C15's plan, and the plan part missing from older records.**
- **Target:** C15 line 149, "plan: …"; also C2–C13, whose "Put right…" parts have no plan part.
- **Defect:** C15's plan is not marked as written before the change. The only copy I found is in fix_corrections.py (14:14), after test-run-1.txt (14:03). C2–C13 omit the plan part without saying "does not apply, and why".
- **Grounds:** recording.md line 26 ("the plan as it was written before the change"), line 31, and trap line 60. C1 is honest about this ("not written down before").
- **Verdict:** does not bear yet for C15. The test: produce an earlier copy of the plan, or relabel it "written after". Bears for the omitted plan parts.
- **Severity:** should change.

**F9. The "Open corrections" status line disagrees with the corrections' own close conditions.**
- **Target:** project story line 14.
- **Mismatches:**
  - C1 also needs the kept cases rerun (line 38).
  - C4 needs the gate to have been seen stopping a real commit (line 62), not the build commit passing through.
  - C15 needs a re-review that finds no way round left (line 151).
- **Connection:** RC8 is only partly answered.
- **Verdict:** bears. **Severity:** should change.

**F10. The correction note in file 26 still says "and nothing else".**
- **Target:** file 26 line 9.
- **Changes the note does not list:**
  - line 88: "it fits the book-and-leaf picture both versions use"
  - line 91: "Nothing on the page decides…"
  - line 91: new advice, "keep Iona's look at Jude's ring (A:435)"
  - line 96: "You have said you are not sure…"
- **Verdict:** bears. **Severity:** minor (what remains of RC1).

**F11. Taste items listed as B's gains.**
- **Target:** file 26 line 91 "Choices of taste, not gains", under the heading at line 86 "What B does better (carry these into A)".
- **Defect:** the heading and the item contradict each other.
- **Verdict:** bears. **Severity:** minor.

**F12. "Reached this verdict separately" overstates.**
- **Target:** file 26 line 26, "reached this verdict separately, from different angles".
- **Grounds:** H43 (the lead gave the agents its own pre-selected list of differences), and file 26's own line 129 (the checks count as one).
- **Verdict:** bears. **Severity:** minor.

**F13. Readings without a question number.**
- **Target:** the reply check in all five craft skills (e.g. plot/SKILL.md line 139), and add-source Step 4.
- **Defect:** both say "the workshop's reading, with its question number". Most readings have none: owner-answers line 25 counts about a hundred.
- **Grounds:** the rule card (line 20) and theory-checker both say "if there is one".
- **Connection:** an agent must invent a number or drop the label.
- **Verdict:** bears. **Severity:** minor.

**F14. The "Bears" mapping is unlabelled and incomplete.**
- **Target:** SKILL.md lines 92-98, and diagram line 59.
- **Defects:**
  - The mapping from marks to verdicts is the workshop's (hard-to-vary SKILL.md 113: mappings are "said as such"), yet it is credited "(Part IX, bearing)", where the foundation says nothing about "not settled".
  - "Two routes" is not mapped.
  - hard-to-vary's "held if" also covers a part held only by an unknown part (reporting.md line 10), which this mapping sends elsewhere without saying so.
  - The diagram sends "held if" only to "ask the owner", though a writer's aim is asked of the writer.
- **Verdict:** bears. **Severity:** minor.

**F15. Re-tune and new part: the two skills now disagree, and nothing records it.**
- **Target:** SKILL.md line 107 says "both are built … These are hard-to-vary's words".
- **Grounds:** hard-to-vary word-list.md line 45 maps "re-tune, or build a new part" to Part IV's selection and construction responses.
- **Connection:** the maker was right not to edit hard-to-vary (S11). But the disagreement is recorded neither in C9 nor in S11, so it will be lost.
- **Verdict:** bears. **Severity:** minor.

**F16. The two statements of the tripwire rule differ.**
- **Target:** SKILL.md line 211 says "committed text in a check, a brief…"; reviews-and-briefs.md line 44 says "it is in a check or a brief".
- **Defect:** the two disagree, and a brief is never committed (C5 line 69), so the SKILL.md tripwire can never fire for a brief.
- **Verdict:** bears. **Severity:** minor.

**F17. Two passages not brought into line.**
- **Target:** writing-rules-and-rivals.md line 40, "knocks down the side's whole bundle" (a third copy of the wording PF17 flagged); and rule card step 2 (line 23), "If nothing, it is idle: cut it".
- **Defect:** step 2 has no "in groups", unlike hard-to-vary SKILL.md 162 and the error-correction stance (line 128).
- **Verdict:** bears. **Severity:** minor.

**F18. Kinds-table rows 1 and 2 are stale.**
- **Target:** 27 Corrections.md lines 11-12, "Last seen: entry 23 / 22".
- **Defect:** the entry-27 re-tune made both kinds: a neighbouring-sense use of the bomb, and the Q7 stretch credited to the theory. CC17 also found "implication" misused in the term sheet. Row 6 was updated for this; rows 1 and 2 were not.
- **Also:** row 1 names kept cases 04, 08 and 09 as catches, though C14 records defects in exactly those items on owner terms.
- **Verdict:** bears. **Severity:** minor.

**F19. Entry 29 overstates the tagging.**
- **Target:** project story line 133, "Passages resting on open questions now carry the question's number".
- **Counter-examples:**
  - The S4 reading at plot suspense-and-fear.md line 89 ("often through what it stands for") has neither a label nor a number, though S4 says it is "Marked as the workshop's reading".
  - The S7 tone row at genre/SKILL.md line 160 has no number.
- **Verdict:** bears. **Severity:** minor.

**F20. Wording copies and stale lines.**
- owner-terms.md line 7 says "S1 to S9", but the sheet now cites S13.
- The worked example's step 4 (SKILL.md line 30), "Plan, written down first", contradicts C1 ("not written down before the change").
- README line 13 still says "what does each fix cost?" (the wording CC15 changed).
- README line 20 says the gate enforces the review itself; CLAUDE.md now marks the review "on trust, with a trace".
- The project story uses "measure" as a noun (PF15 kept "metric").
- **Verdict:** bears. **Severity:** minor.

**F21. C14 doesn't say how the defective cases will be read in the next run.**
- **Target:** C14's plan keeps the defective cases as the keep-working occasions.
- **Defect:** it doesn't say how the defective items are to be read in run 2.
- **Grounds:** Part XI (a protected condition is judged on stated occasions). RC9 to RC22.
- **Connection:** a result on a defective item would be read as a skill result.
- **Verdict:** bears. **Severity:** minor.

**F22. One loose specific in the planting rule.**
- **Target:** reveals-and-withholding.md line 30, "a fact that is easy to miss usually needs more than one scene".
- **Defect:** swap in "a held shot or a character's attention in one scene" and the rule does the same job, so the specific is loose. It also partly brings back C12's "in different scenes".
- **Verdict:** bears. **Severity:** minor.

### Marks on new or changed rules
- **Planting rule, "noticeable before the turn" (Egri, built):** held, by the set-up job, for turns meant to be earned. Held if §2's scope excludes shocks (F5).
- **Planting rule, "one clear showing can be enough":** held.
- **Planting rule, "more than one scene":** loose.
- **Planting rule, the Q7 promise clause:** held if Q7.
- **Planting rule, the split between a surprise turn and a suspense turn:** held (Gap Part 2 §3).
- **Reply check, "say what it rests on":** held (C1, H41).
- **Reply check, "with its question number":** loose (F13).
- **Reply check, "in proportion":** unknown. The kept-case rerun settles it (CC8).
- **Reply check, the pushback handling:** held (PW9's case).
- **Mapping from marks to verdicts:** held, but as the workshop's mapping, unlabelled and incomplete (F14).
- **Step 4, the plan in the receipt:** idle as written (F7).
- **Tripwires:** held (PW4's walks).
- **Rule card steps 1 and 3:** held.
- **Rule card step 2:** loose against hard-to-vary's instruction to remove in groups.
- **checks-and-cases §3 and §6, and owner-answers §2 and §3:** held.
- **Rivals:** none new or changed.
- **Worked example:** the Catch example in error-correction comes from a real correction (C1), not from a kept case. It does reach kept case 11's conclusion, so leave it to PW10's rerun (unknown).

### Checked and found right
- **Answered in content:** PF1–PF23, except as noted in F14, F15 and F17. PW1 only partly (F1); PW2 was not checked by me (script behaviour, test_checks.py not run); PW3–PW14 applied. CC1–CC19. RC4–RC8, RC15–RC17, RC23 and RC24, with RC1, RC2 and RC3 partly (F10, F1, F2) and RC8 partly (F9).
- **Reasons given for not applying:** sound for RC9–RC14 and RC18–RC22 (like-with-like comparison), for PF6 on hard-to-vary (S11), and for PW10, CC8 and CC9 ("does not bear yet").
- **Foundation citations:** in SKILL.md's Words and Built on, they match Parts I, IV, IX (K1, K2, K3, receipts, the active route), X, XI (the three attributions, losses) and XIV.
- **Term sheet:** the changes to 1.1, 1.3, 9.2, 11.2 and §13 are faithful.
- **Question tags:** the new tags (Q2, Q4, Q5, Q6, Q7, S1, S2, S5, S6, S8, S13) point to questions that contain the point.
- **The reply check:**
  - It is identical in all five skills: the md5 is the same for each.
  - The run: check_maps.py 0 problems; check_records.py 0 problems; check_owner_quotes.py "104 quotations match".
- **File 26's new line references:** every one I opened matches the scripts. These were A:285, 435, 495, 590, 1022, 1308 and 115, and B:161, 174, 418-420, 480, 502, 544-553, 551, 563, 608, 641, 830-833, 873-875, 960, 968, 977 and 1248-1252. "Book-and-leaf" is in both versions (A:565, B:536).
- **Records:** the kept design ledger contains design-final.md word for word. The gate is switched on in the repository (`core.hooksPath` is `.githooks`).

### Not checked
- What the scripts and hooks actually do: test_checks.py and the gate were not run by me.
- The kept cases in full, and any case run.
- The copying check and copy-checker.
- Whether the kept first-round reports match the originals (I checked only the design ledger).
- The substance of file 26's faults 2 to 5.
- The break test beyond the lines I opened.
- The accuracy of H1 to H47.
- Modules of dialogue, genre and story-world beyond the diff.
- Whether the reply check is followed in practice.

### Overall verdict: **passed after changes**
Must change:
- **F1:** remove the four order phrases in file 26, correct C1, S12, file 26 line 127, the entry 29 title and bullet, and status line 12, and make the order-word lists in the claim check and the reply check open-ended.
- **F2:** apply the break test's unapplied findings, or list them as unapplied.

Should change: F3–F9. These edits then need a look of their own, by a reviewer who did not make them (reviews-and-briefs §2 step 4).

Main files: `/home/user/StoryTest/26 Test - The Catch - two versions.md`, `/home/user/StoryTest/27 Corrections.md`, `/home/user/StoryTest/.claude/skills/error-correction/SKILL.md`, `/home/user/StoryTest/.claude/skills/plot/references/reveals-and-withholding.md`.
---

## 2. use-tester

## Use-tester re-review: the error-correction process walked through situations (a) to (h), and the craft skills' routes to the reply check

**Overall verdict: passed after changes.** Four things must change, each listed below. Two are dead ends that force either a false record or a blocked repository. One silently erases the only trace that kept cases are owed. One is a way round the gate that CLAUDE.md tells the owner is caught "by itself". The first round's findings PW3, PW4 (in SKILL.md), PW5, PW9, PW12, PW13 and PW14 did land, and routes (c), (d), (e) and (f) now run on their light paths.

The edited scratch repository (`rereview`) has a HEAD identical to the live working tree; I checked every tracked file with `cmp`. All runs happened in copies under `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/`: `ut-walk`, `ut-walk-b`, `ut-walk-e` and `ut-walk-g2`. Gate outputs are saved beside them: `ut-c-output.txt`, `ut-g1.txt`, `ut-g2.txt`, `ut-g3.txt`, `ut-f1.txt`, `ut-f2.txt`, `ut-f3.txt` and `ut-e1.txt`. The reviewer reports inside my scratch receipts are my own, marked "simulated".

### Must change

**M1. Situation (b): once the owner answers a question, it can never be closed.**
- **Target:**
  - `.claude/skills/error-correction/references/owner-answers-and-revisions.md` lines 21–22 (a kept case "is not changed"; step 4 "Close it").
  - `references/checks-and-cases.md` line 74 ("The records check lists every kept case...").
  - `scripts/check_records.py` lines 258–276. It scans every `.md` file under `kept-cases/`, including `runs/`.
  - `scripts/test_checks.py` lines 304–306. This planted test *expects* kept case 03 to fail.
- **Defect:** the procedure says a kept case that cites the question stays exactly as it was run. The records check fails that case, and also fails the grader's notes in `kept-cases/runs/`, until "answered" is written beside the number. Neither file may be changed. So setting the status to `answered` stops every commit. The only state that passes is `rechecking`, and the session start then shows the owner the answered question as still open.
- **Grounds:** in `ut-walk-b` I set Q3 to answered and marked the four skill passages "(Q3, answered 24 Sep: option b)", leaving case 03 as it was. `check_records.py` then printed:
  - "kept-cases/03-villain-with-four-blank-levers.md:28: rests on owner question Q3, which is answered; ... write 'answered' beside after Q3"
  - the same for `kept-cases/runs/2026-09-24-before-entry-27.md:230`
  - "TOTAL problems: 2", exit 1.

  With the status set to `rechecking` it printed "TOTAL problems: 0", and the session start printed "Owner questions still open: Q1, Q2, Q3, ...". The kept cases and run records also cite Q1, Q2, Q4–Q7, S5 and S6, so the first answer to any of those hits the same wall.
- **Connection:** the check tells the agent to edit what the procedure forbids editing ("a changed case is a new case", `kept-cases/README.md` line 47; run records are never rewritten). The agent must either break the kept record or leave the owner's answer showing as open. There is no way back.
- **Proposed change:**
  - Only list kept cases (never fail them), and skip `runs.md` and `runs/`.
  - Make the check's behaviour and checks-and-cases.md line 74 say the same thing.
  - Plant the innocent neighbour: question answered, old case kept, new case added, and the check passes.
- **Verdict:** bears.

**M2. Situation (g): a late review that does not pass cannot be recorded. Every commit is stopped, and so is the correction to the check.**
- **Target:**
  - `scripts/review_receipt.py` line 57 (`VERDICTS`).
  - `references/checks-and-cases.md` line 39 ("put it right with a new commit: a receipt written late...").
  - `recheck_commits.py` lines 103–109, which `check_commit.py` lines 136–145 run on every commit.
- **Defect:** a receipt must begin with "passed", "passed after changes" or "light". A commit made where the gate was off, whose late review rejects it, can only be cleared by writing a verdict the reviewer did not give. Until then every commit is stopped, including the one that withdraws the change. Correcting the receipt check does not help, because the gate judges the correction with the last commit's receipt check.
- **Grounds:**
  - In `ut-walk` I pulled an outside commit (made in a clone with no gate) that put C12's number back into plot ("Show every clue ... at least twice").
  - A late receipt with the verdict "not passed" was refused: "'Verdict' must begin with one of: passed, passed after changes, light".
  - The withdrawal, with its own complete receipt, was stopped: "FAILED earlier commits the gate may not have seen / commit defe411e4: no review receipt ...".
  - It went through only after I wrote "passed after changes" above a pasted report that ends "Verdict: not passed".
  - I then staged a correction to `review_receipt.py` allowing "not passed", together with a late receipt for a second outside commit. The gate stopped it: "commit 985d2150f: ... 'Verdict' must begin with one of: passed, passed after changes, light".
- **Connection:** the only way the text leaves open is a false record in a kept file, which reviews-and-briefs.md lines 70 and 72 forbid, or getting round the gate.
- **Proposed change:**
  - Allow "not passed (withdrawn in <commit>)" on receipts checked with `--commit` only, never for a staged change.
  - Say in checks-and-cases.md section 2 what to do when the late review does not pass.
  - Say what to do when a check that stops every commit is itself the wrong one.
  - Plant each case.
- **Verdict:** bears.

**M3. Situation (g): an outside commit that loosens a check is never flagged, and the gate stays loosened.**
- **Target:**
  - `.claude/hooks/session_start.py` lines 87–91. It runs the recheck from the files on disk.
  - `check_commit.py` lines 107–112. It takes the checks from the last commit.
  - `recheck_commits.py` line 107.
  - The claims at CLAUDE.md lines 39–40, SKILL.md line 228, and the last row of the kinds table in `27 Corrections.md`.
- **Defect:** the recheck judges an unchecked commit with that commit's own checks.
- **Grounds:**
  - In `ut-walk-g2` an outside commit made `review_receipt.py`'s `problems_with` return nothing, and added an unreviewed plot rule. It arrived by fast-forward.
  - The session start printed no "Commits the gate may not have seen" line, and "Machine checks: none failing".
  - A second unreviewed plot rule then went through the gate: "passed review receipt / review receipt: not needed ... All checks passed; committing."
- **Connection:** CLAUDE.md tells the owner that "every commit the gate did not see is rechecked" and that a check "cannot pass the work it would stop | By itself". checks-and-cases.md line 47 requires planting "a commit it never sees". The planted test plants only a skill change.
- **Proposed change:** run the recheck with the checks from the last commit it passed (the marker commit), and flag any check change in commits not yet rechecked. Plant it. Until then, scope the three claims.
- **Verdict:** bears.

**M4. Situation (e): the route for a change that alters no meaning erases the kept-case notice for every skill.**
- **Target:**
  - `SKILL.md` line 204.
  - `references/checks-and-cases.md` line 61.
  - `check_records.py` lines 336–345 (it reads only the last fingerprint line) and 350–354 (`--fingerprints` prints every skill's current code).
- **Defect:** following the typo route records the current fingerprints of *all* skills. Skills whose meaning changed and whose cases were never rerun then read as up to date.
- **Grounds:**
  - Before, in `ut-walk-e`, the records check printed "kept cases not rerun since these skills changed: character, dialogue, genre, plot, story-world".
  - I fixed a one-word typo in `plot/references/scenes.md` exactly as row 1 says: a light receipt with its Book text line, a `runs.md` line from `--fingerprints`, and a log entry. The gate printed "All checks passed; committing."
  - Afterwards, `check_records.py . | grep -c "kept cases not rerun"` printed 0.
- **Connection:** this is the only trace for the CLAUDE.md line 47 rule that kept cases are rerun after a skill changes. All five craft skills are owed a rerun now (C1, C3 and C12 wait on it), and the first typo commit would hide that.
- **Proposed change:** record only the touched skill's new code, and only if its old code matched the last run; carry the others forward. Plant it: a typo in one skill while another is stale, and the other stays listed.
- **Verdict:** bears.

### Should change

**S1. Situation (g): the session start never lists open corrections.**
- **Target:** `.claude/hooks/session_start.py` lines 52–53. The claims are at SKILL.md line 232 and recording.md line 54 ("the session-start hook lists open corrections, so it is not forgotten"). The planted test at `test_checks.py` lines 707–709 does not check for it.
- **Defect:** `block[1:]` of a "### C1." heading begins with "## ", so each block is cut to one character and no status is found.
- **Grounds:** the session start printed no "Open corrections" line, though 14 corrections are open. I called `open_items` directly and it returned `[]`. In walk (f) I corrected the cut and it printed "Open corrections (27 Corrections.md): C1, … C15". A new planted test failed on the old hook (119 tests, 1 failed) and passed on the new one.
- **Connection:** in situation (g) the agent starting a session is not shown the open corrections. The fault is older than this round, but this round's claims rest on it.
- **Verdict:** bears.

**S2. Situation (c): a stale stamp is also reported as a failure of earlier commits.**
- **Target:** `recheck_commits.py` line 118. It calls `check_records.py` without `--log-only`, although `check_records.py`'s docstring (lines 51–52) says it does. Lines 119–121 count the indented status-line notes as problems.
- **Grounds:** I added entry 30 without restamping and committed with the gate on. The gate printed "FAILED records" (6 lines) and then "FAILED earlier commits the gate may not have seen … rechecked 0 commit(s) since 1e92459fe / TOTAL problems: 13". After a restamp the commit went through.
- **Connection:** checks-and-cases.md line 39 says "If the stop names a commit the gate did not see, put it right with a new commit", which sends the agent looking for a fault in a commit that does not exist. The light answer can still be reached, which is why this is not a must.
- **Verdict:** bears.

**S3. Situation (a): reviews-and-briefs.md makes almost every review finding a tripwire.**
- **Target:** `references/reviews-and-briefs.md` line 44, against SKILL.md lines 210–215.
- **Defect:** line 44 gives these examples of a tripwire: "the finding is of a kind the corrections file says is already caught, or it is in a check or a brief". Every one of the 17 kinds in the table names a catch. A finding on a *staged* change is that catch working.
- **Grounds:** I walked (a): theory-checker finds a wrong-theory credit in a staged change. SKILL.md's row "A meaning changes in one place" says one line in the receipt. Line 44 says a full correction, because the kinds table lists wrong credits as "caught now by `theory-checker`". The map sends an agent who is answering a review to this module.
- **Connection:** PW4 is put right in SKILL.md but survives in the module the agent actually opens.
- **Verdict:** bears.

**S4. "List" is used in two senses.**
- **Target:** SKILL.md line 207, reviews-and-briefs.md line 30 and checks-and-cases.md line 33, against `check_commit.py` lines 52–53 and add-source/SKILL.md lines 43 and 72.
- **Defect:** the text says a changed "check, hook or list" goes in a commit of its own and that the gate refuses it mixed with other work. The gate does refuse that for the allowed-titles list, but not for the frozen list. add-source requires the frozen list's new line in the same commit as the new source.
- **Grounds:** I asked the scripts directly. `frozen-files.txt`: the own-commit rule is False, never-light is True. `overlap-allowed.txt`: both True.
- **Connection:** when storing a new theory, the agent meets two instructions at odds and must guess which to follow.
- **Verdict:** bears.

### Minor
- **Situation (f): no command given.** `checks-and-cases.md` line 47 says "run the new tests on the old check too" but gives no command. I improvised one: HEAD's files with the new test dropped in. Verdict: bears.
- **Situation (f): the check's description must come later.** A check's description (checks-and-cases.md, or the table in CLAUDE.md) cannot go in the check's own commit. The gate printed "FAILED a check is changed together with other work … commit them afterwards" (`ut-f3.txt`). No module warns that the description is stale between the two commits. Target: checks-and-cases.md line 49. Verdict: bears.
- **Situation (h): wrong pointer.** `plot/references/reveals-and-withholding.md` line 30 says "as with the bomb under the table (section 1)". That module's section 1 holds *Columbo* and *Speed*. The bomb is in its section 3 (line 40) and in suspense-and-fear.md section 1 (line 20). Verdict: bears.
- **Situation (h): building route may miss the guidance.** The guidance on how often to show a planted fact sits under section 2, "Mystery or wonder". Section 6's "Set-up and payoff" (line 77) does not point to it. The diagnosing route and the quick version do reach it; the building route may not. Verdict: does not bear yet. The settling test is a fresh agent given a building question about a clue.
- **Situation (g): wrong command in the hint.** The session-start message for a late receipt says "make one with review_receipt.py new". For a commit already made it should be `new --commit <commit>`. Target: `review_receipt.py` lines 200–202. Verdict: bears.
- **Craft routes: one route leaves the character skill.** character/SKILL.md line 36 ("testing whether a trait … is doing work") sends the agent to hard-to-vary, which has its own report form, with no pointer back to Step 8 or 9. The matching rows in genre, dialogue and plot point back into Building. Verdict: bears.
- **Situation (d): a detour.** CLAUDE.md line 20 sends "a writer objects" to the error-correction skill, and that skill sends it straight back to the craft skill's reply check. Verdict: bears.
- **Situation (a): "reading" in two senses.** SKILL.md line 211 says "a reading of a theory". Elsewhere "reading" means the labelled "workshop's reading". For a committed wrong credit the agent cannot tell whether this tripwire fires; the fifth tripwire fires anyway. Verdict: bears.
- **Situation (b): garbled message.** The check prints "write 'answered' beside after Q3" (`check_records.py` lines 274–275). Verdict: bears.
- **Situation (b): the search promise fails during rechecking.** owner-answers-and-revisions.md line 17 says "(the records check lists them too)". While the status is `rechecking`, the check lists no passages, only "question Q3 is answered and its passages are being rechecked". Verdict: bears.
- **An older fault.** The glob `sources/*-theory.md` (README.md line 55, use-tester.md line 13, theory-checker.md line 13) misses `gap-theory-of-narrative.md`. My own first search skipped the Gap theory's bomb line because of it. Verdict: bears.

### Kept cases (titles and "Aimed at" lines only)
- **Case 01 against reveals-and-withholding.md line 30** ("being seen is the point, as with the bomb"): the bomb is the theory's own case and was already in the module (line 40) and in suspense-and-fear.md. Case 01 passed in Run 1 before this wording existed, so the wording hands it no answer it lacked. Does not bear.
- **The reply check's "she's lying" example against case 10:** it does not tell the same story, as far as the titles show. Does not bear.
- **Case 11 (PW10):** still does not bear yet, as the maker says.

### Stall list
- **(a)** S3 and the "reading" item. Otherwise "How much to do" row 2 gives the steps clearly.
- **(b)** M1, and the search promise that fails during rechecking. Two improvisations:
  - no template for where the answer goes in the questions file;
  - "(Q3, answered…)" leaves the sentence "is a question put to the owner" stale, and nothing says whether that edit gets a light or a full receipt.
- **(c)** S2. "The stop is a sign (the skill's loop, step 1)" does not say where to write the sign down. Otherwise: restamp, commit again, passed.
- **(d)** Followable. The CLAUDE.md detour. "Go further, as a correction" leaves it unclear whether that means the corrections file.
- **(e)** M4. "One line in the next log entry" became a whole entry, which forced six restamps.
- **(f)** Worked end to end: correction C16, with the hook, its test, receipt, log and correction in one commit, and both planted-fault runs passed (43 seconds). Plus the two (f) items under Minor, and M2's deadlock.
- **(g)** S1, M2, M3, and the wrong command in the hint. It is unclear whether an unreviewed commit made elsewhere fires a tripwire.
- **(h)** The two (h) items under Minor.

### Walked and found right
- **(c)** PW5 is in place: the gate's stop message names checks-and-cases.md section 2, and the map row and diagram node are there.
- **"How much to do"** now ties each weight to its steps, and says gate stops and writers' objections are not tripwires.
- **(d)** The reply check handles the pushback. The dialogue skill's flaws-and-fixes.md line 111 answers the lying-character case.
- **(e)** The light receipt with its Book text line was accepted with the book texts absent. The hard-to-vary exception is named.
- **The live copy:** `git config --get core.hooksPath` prints `.githooks`. The live bypass hook refused my scratch command that would have unset it.
- **(g)** A plain outside commit with no receipt is reported at session start and at the next commit.
- **Mixed commits:** a check changed together with other work is refused, with a clear message.
- **(h)** The changed plot rule agrees with:
  - Gap theory line 59 ("Show them the bomb first and you get fifteen minutes of suspense");
  - Anticipation theory line 41 (the bomb and the time term);
  - line 47 (*Chronicle of a Death Foretold*: uncertainty moves "from whether to how");
  - *Psycho*'s surprise (line 67).
- **Craft routes:** in all five craft skills, Building, Diagnosing and the quick version end at the reply check. I followed it on three small cases without stalling: a twist's clue in plot, the lying line in dialogue, and a broken guarantee in genre.

### Not checked
- I ran no kept cases and no copy-checker; the copying check printed NOT RUN in the scratch copies.
- I did not test merges, rebases or cherry-picks, and did not try line-ending cases.
- I read owner-terms.md only where Q3 appears.
- I did not fully read `check_maps.py`, `overlap_check.py`, `check_frozen_files.py` or `refuse_check_bypass.py`.
- I did not re-verify the PF, CC, RC or S answers beyond what the walks touched. PW2 (unfilled receipts) I saw only in passing.
- I did not test the hooks in a fresh live session.

### Side effect in the live repository
I wrote two Python cache files into the git-ignored `.claude/skills/error-correction/scripts/__pycache__/` of the live repository, then deleted them. Only that folder's timestamp changed. `git status --short` shows 30 entries before and after, and no tracked file changed.

### Verdict: passed after changes
These must change, and the edits need a re-review of their own:
1. **M1:** the owner-answer procedure against kept cases and run records.
2. **M2:** late receipts that do not pass, and a way to correct a check that stops every commit.
3. **M3:** recheck unchecked commits with the last rechecked commit's checks, or scope the claims in CLAUDE.md, SKILL.md and the kinds table.
4. **M4:** the fingerprint line for a change that alters no meaning.

S1 to S4 should change as well.
---

## 3. scripts and hooks

# Re-review of the workshop's scripts and hooks, 24 September 2026

**Overall verdict: not passed.** Two findings must change, 12 should change and 7 are minor. The rewrite closes all 17 of the first reviewer's findings in the form they were reported, but I found new ways round the gate. The two that must change are in the gate's entry file and in the recheck of earlier commits, which the notes call "the real safety net".

**How I worked.** I made no edits and no commits in /home/user/StoryTest. Every experiment ran in a scratch copy under /tmp/rr/ (one commit, gate switched on), with no GIT_INDEX_FILE or GIT_DIR set. The helpers are:
- /tmp/rr/mk.sh makes a copy.
- /tmp/rr/fill_receipt.py fills in a receipt form. On purpose, its "reviewer's report" is the word "word" 45 times, to show which steps rest only on trust.
- /tmp/rr/hooktry.py feeds commands to the two refusal hooks.

The scripts, hooks, .githooks and .gitattributes in the real working copy were byte-for-byte the same as the rereview snapshot's last commit, both at the start and again at 14:45 UTC. During my review the maker edited 20 prose files (CLAUDE.md, SKILL.md, the story and others); every CLAUDE.md or skill line I quote was re-read after those edits. No book text is quoted anywhere below.

---

## 1. The first reviewer's findings, tried again

- **S1 (the gate trusted the files it checks): closed for both routes.**
  - Route A (/tmp/rr/s1a): check_records.py loosened on disk and not staged, with entry 5 rewritten and staged. The gate printed "FAILED records … log entry 5 has been changed since HEAD" and "COMMIT STOPPED".
  - Route B (/tmp/rr/s1b): the check change, the entry 7 rewrite and a receipt in one commit. It printed "FAILED records … log entry 7 has been changed since HEAD" and stopped.
  - New routes this change leaves open: N1, N3, N4, N5 and N12 below.
- **S2 (second frozen-list line): closed.** It printed "frozen-files.txt: sources/bond-theory.md is listed 2 times …" and "frozen file has changed". A receipt naming no reviewer was refused: "a light receipt is never enough … (.claude/skills/error-correction/frozen-files.txt)".
- **S3 (receipt form holes): closed.**
  - (a) Empty fields: "'Maker' is empty / 'Reviewed by' is empty / 'Findings' is empty".
  - (b) The untouched form: "'Change' still holds the form's hint in brackets …" and "'## Reviewer's report' still holds the form's hint".
  - (c) Light receipts for a check: see S2.
  - The CLAUDE.md row now says "On trust". Only the report's length is checked: 45 repeats of "word" passed in every trial.
- **S4 (copying check): (a) closed, (b) and (c) partly.**
  - (a) The same 21-word run as before (14 words outside the film title) now prints "[21 words, PROBLEM] … TOTAL problem spans >= 8 words: 1", exit 1.
  - (b) A whole book sentence put in the source register is caught, because the register itself is copy-checked ("FAILED copying from books"). Single title words still get onto the allowed list: N11.
  - (c) A new folder's .md files are read (the planted test passes). Other file types are not: N10.
- **S5 (gate off in the real repository): closed.** `git config --get core.hooksPath` prints ".githooks".
- **S6 (merges, cherry-picks, fast-forwards): closed for the reported routes.**
  - `merge --no-ff` of a theory edit printed "FAILED frozen files … COMMIT STOPPED".
  - A cherry-pick got in (exit 0), then the recheck printed "frozen files since 46bb8edcb: sources/bond-theory.md: frozen file has changed … TOTAL problems: 1".
  - A log rewrite brought in by fast-forward: run_all_checks printed "passed records", but the recheck printed "records since 46bb8edcb: … log entry 7 has been changed".
  - The recheck itself has new gaps: N2, N6, N7, N8.
- **S7 (GIT_INDEX_FILE): closed.** `git commit -a` of a check change printed "passed the last commit's planted-fault test … All checks passed; committing." (27 s). `git commit <two files>` with a third file staged committed only the two named files.
- **S8 (a check that cannot run shown as passing): closed.**
  - A misspelt folder: "NOT RUN: .claude/skils is not here …", exit 3.
  - run_all_checks.py broken on disk: session start printed "Machine checks: could not run (Traceback … NameError …)". The gate was unaffected, because it uses the last commit's copy.
- **S9 (bypass spellings): closed as proposed.** All the spellings and false alarms the first reviewer listed are planted tests and pass. New gaps: N13.
- **S10 (Windows line endings): closed.** With autocrlf=true and a fresh checkout, a README commit printed "passed frozen files … All checks passed".
- **S11 (edit hook from another folder): closed.** An edit to /tmp/rr/base's theory, sent from the folder /tmp with the project set to another copy, was REFUSED.
- **S12 (spaces; non-.md files; first-commit note): closed.** `--add "sources/my new theory.md"` then printed "TOTAL problems: 0", and the edit hook REFUSED edits to it. sources/notes.txt printed "should be frozen". The real repository prints "not checked: whether the list was only added to …". Small gap: N20.
- **S13 to S16: closed.** Each has a planted test that prints ok: straight-quoted quotation; shared marker deleted; accented file name; unindented numbered list and correction note pointing backward. check_commit.py uses `-z` and `core.quotePath=false`. Small gap: N18.
- **S17 (single-letter names): closed for the Python scripts.** A scan found only the function names git, run, add and one. Remainders: N21.

---

## 2. New findings

**N1. The gate's entry file is read from disk and can switch the gate to the staged checks. Verdict: bears. Must change.**
- **Target:** .githooks/pre-commit lines 15–26; check_commit.py lines 94–96, 107–116, 149 and 162; session_start.py line 68.
- **Defect:** git runs .githooks/pre-commit from disk, never from the last commit. check_commit.py obeys that file's `--checks-from staged` even when the last commit contains the gate. One unstaged word therefore makes the gate take every check from the staged files. That also skips the refusal of a check change mixed with other work, and the last commit's planted-fault test. A staged change to pre-commit is also the copy on disk, so it takes effect for its own commit.
- **Grounds:**
  - /tmp/rr/e6: `--checks-from staged` written into pre-commit on disk only. check_records.py (loosened to skip entry 7), an entry 7 rewrite, a plot rule and a receipt were staged together. The gate printed "note: the commit gate is new in this commit, so its checks come from the staged files …", every check "passed", then "All checks passed; committing."
  - /tmp/rr/pc: `exit 0` staged as line 2 of pre-commit, with an unreviewed plot rule and no receipt. The commit went in with no gate output, exit 0. Session start then printed "- Commit gate: on (git runs .githooks/pre-commit before every commit)".
  - protect_frozen_files.py let through a Claude Edit of .githooks/pre-commit.
- **Connection:** CLAUDE.md says the gate "runs the checks as they were in the last commit, so a check cannot be loosened in the same commit". S1 is answered "applied", but the entry file is the one piece that does not come from the last commit.
- **Proposed change:**
  - check_commit.py always uses the last commit's gate when the last commit has one, and the argument is dropped.
  - The gate records the tree (the exact staged snapshot) it approved, in .git.
  - The recheck and session start report any commit whose tree the gate never approved.
  - Session start says "Commit gate: on" only when .githooks/pre-commit matches the last commit's copy.
  - Planted tests for both routes.

**N2. The recheck runs checks taken from the very commits it rechecks. Verdict: bears. Must change.**
- **Target:** recheck_commits.py lines 40, 107 and 117–118; check_commit.py lines 136–139; session_start.py lines 87–91.
- **Defect:** The recheck of commits the gate never saw uses the review-receipt, frozen-file and records checks from the newest commit (at the gate) or from disk (at session start). So an unseen commit can loosen those checks and use them in the same commit. The recheck also reruns only those three checks. It skips the maps, owner-quotes, copying and book-file checks, the mixed-change refusal and the planted-fault test.
- **Grounds:**
  - /tmp/rr/e5: one `--no-verify` commit skipped entry 7 in check_records.py, rewrote entry 7, and carried the 45-"word" receipt. The recheck printed "rechecked 1 commit(s) since 46bb8edcb / TOTAL problems: 0". The next gate commit printed "passed earlier commits the gate may not have seen … All checks passed; committing."
  - /tmp/rr/e5b: the same with no receipt, and review_receipt.py loosened in the same commit. The recheck printed "TOTAL problems: 0". Session start printed "- Machine checks: none failing" and nothing about unseen commits.
- **Connection:** refuse_check_bypass.py's note says "The real safety net is the recheck …". The CLAUDE.md row says "every commit the gate did not see is rechecked". This repeats the S1 defect one level down.
- **Proposed change:**
  - Take the recheck's scripts from its starting commit (the last one known to be checked), extracted with git archive.
  - Run the whole gate on each unseen commit against its parent.
  - Flag any unseen commit that changes a check.
  - Planted tests for both runs above.

**N3. Across two commits, a loosened check can still pass the work it would stop. Verdict: bears. Should change.**
- **Target:** the CLAUDE.md row "A check is corrected in its own commit, and cannot pass the work it would stop | By itself …"; test_checks.py line 258, the only planted log rewrite.
- **Defect:** Across two commits, a loosened check does pass the work it would stop. Only the receipt (on trust) and the planted faults stand in the way, and the planted rewrite covers only entry 5's title line.
- **Grounds:** /tmp/rr/s1c. Commit 1 was check_records.py skipping entry 7, alone, with the 45-"word" receipt. It printed "passed the last commit's planted-fault test, on the changed checks … All checks passed; committing." Commit 2, the entry 7 rewrite, printed "All checks passed; committing."
- **Connection:** "By itself" holds within one commit only.
- **Proposed change:** Reword the row: "by itself within one commit; across commits, on trust (the receipt) plus the planted faults". Plant rewrites of a body line, of the last entry, and of other entries.

**N4. "Tests retired" can retire whole test groups under one name, and any test at all. Verdict: bears. Should change.**
- **Target:** check_commit.py lines 189–212; test_checks.py line 739.
- **Defect:**
  - When a whole group of tests crashes, test_checks prints one line, "<group> could not run". That one name can be retired, which silently retires every test in the group, and the gate counts it as one.
  - Names are matched as any piece of the free text in the section.
  - Any test can be retired, including those guarding the log, the frozen files, the receipts and the gate itself.
- **Grounds:**
  - /tmp/rr/e1c: commit 1 stopped check_records comparing old entries, and retired "records: an old log entry rewritten" and the loosened-on-disk gate test. It printed "(2 test(s) retired in the receipt) … All checks passed". Commit 2 rewrote entry 12 and passed.
  - /tmp/rr/e1d: commit 1 reworded review_receipt.py's "wrote …:" message, which crashes two groups, and let light receipts cover checks. It retired "receipt_tests could not run; gate_tests could not run", and the gate printed "(2 test(s) retired)". Those two groups hold 12 receipt tests and 11 gate and recheck tests.
  - Commit 2 then changed check_records with "Reviewed by: none, light (a small tidy)" and passed. Commit 3 rewrote entry 7 and passed.
- **Connection:** CLAUDE.md rule 2, "Not run is never passed".
- **Proposed change:**
  - A "could not run" line is never retirable.
  - Match each retired name as a whole line, and print each retired test by name.
  - Retiring needs a full receipt, and session start lists retirements since the last session.
  - Tests guarding the log, the frozen files, the receipts and the gate can be retired only with the owner named as reviewer.

**N5. Moving a check out of its folder hides it from the mixed-change rule, and a missing planted-fault test is only "not run". Verdict: bears. Should change.**
- **Target:** check_commit.py line 98 (no `--no-renames`) and lines 201–204.
- **Defect:** git reports a moved file under its new name only, so moving a check out of the scripts folder is not seen as a check change. Once test_checks.py is gone from the last commit, the planted-fault stage prints "not run" and the commit goes ahead.
- **Grounds:** /tmp/rr/rn.
  - `git mv …/test_checks.py kept-cases/test_checks_old.py`, with a plot rule, document edits and a receipt. The gate's staged list showed only "kept-cases/test_checks_old.py". There was no "changed together with other work" line, and it printed "All checks passed; committing."
  - Next, check_records was loosened. It printed "not run the last commit's planted-fault test, on the changed checks (there is no such test)", then "All checks passed; committing."
- **Connection:** Rule 2, and the mixed-change rule. review_receipt.py already uses `--no-renames`.
- **Proposed change:** Add `--no-renames` at line 98. A missing test, when the last commit has the gate, counts as a failure. Add a planted test.

**N6. The recheck's starting point can be moved by hand, and merge commits are skipped. Verdict: bears. Should change.**
- **Target:** recheck_commits.py lines 61–66, 105–106 and 130–132.
- **Defect:** The recheck's starting point is a plain file in .git (.git/workshop-checked-up-to) that anyone can overwrite. Merge commits are skipped for receipts, although a merge commit can carry changes of its own.
- **Grounds:**
  - /tmp/rr/e4: an unseen rewrite of entry 7 was reported, then `git rev-parse HEAD > .git/workshop-checked-up-to` was run. The recheck printed "rechecked 0 commit(s) … TOTAL problems: 0", the next gate commit passed, and session start printed "Machine checks: none failing". The bypass hook let that command through.
  - /tmp/rr/em: a merge commit made with `--no-verify` that added a plot rule itself. The recheck printed "rechecked 2 commit(s) … TOTAL problems: 0", while `review_receipt.py check --commit HEAD` printed "no review receipt …", exit 1.
- **Connection:** The same safety-net claim as N2.
- **Proposed change:** The shell hook refuses writes to .git/workshop-*. Session start says when the marker is newer than the last tree the gate approved (see N1). For a merge, ask for a receipt for any difference from the automatic merge of its parents (git merge-tree).

**N7. An honest merge commit of reviewed work is stopped, and the planted merge test passes for a different reason than its name. Verdict: bears. Should change.**
- **Target:** check_commit.py line 98 and review_receipt.py lines 80–93, which fingerprint the whole staged difference; test_checks.py lines 622–624.
- **Defect:** For a merge commit the gate asks for one receipt covering all the branch's changes together, although each commit was reviewed. The planted test "a merge commit runs the gate, which finds the unreviewed commit it brings in" is stopped only by that missing receipt: the recheck never looks at the branch's commits.
- **Grounds:**
  - /tmp/rr/hm: two reviewed branch commits each printed "All checks passed". `git merge --no-ff` then printed "FAILED review receipt / no review receipt .claude/reviews/c5c41c1fd2e835a0.md … .claude/skills/character/SKILL.md, .claude/skills/plot/SKILL.md" and "COMMIT STOPPED".
  - /tmp/rr/pm, the planted test's own scenario: "passed earlier commits … rechecked 1 commit(s)" and "FAILED review receipt".
- **Connection:** A false alarm on honest work. checks-and-cases.md asks for tests that show a fault is caught "for the right reason".
- **Proposed change:** In a merge, recheck the commits it brings in (merge-base..MERGE_HEAD), and ask for a receipt only for the merge's own changes. The planted test must print "commit <id>: no review receipt", with an honest merge as its neighbour.

**N8. `git commit --amend` stops the next commit. Verdict: bears. Should change.**
- **Target:** review_receipt.py lines 80–93 and recheck_commits.py line 107.
- **Defect:** An amend of a reviewed change passes the gate with a receipt for the amendment alone. The recheck then checks the amended commit against its parent and stops the next, unrelated commit, under a heading that says the gate never saw it.
- **Grounds:** /tmp/rr/am. The amend printed "All checks passed". A later commit touching only the log printed "FAILED earlier commits the gate may not have seen / commit 7606499c6: no review receipt …/3556feeffb9fb4b7.md …" and "COMMIT STOPPED".
- **Connection:** A false alarm on an ordinary command, and the message blames the wrong commit.
- **Proposed change:** The recheck accepts any commit whose tree the gate approved (the record proposed in N1).

**N9. An environment setting named `N` changes what the gate checks. Verdict: bears. Should change.**
- **Target:** overlap_check.py line 42, `RUN_LENGTH = int(os.environ.get("N", "8"))`.
- **Defect:** The gate passes its whole environment through, so a stray `N` changes the copying check. A large value lets copied text through; a small one stops honest commits.
- **Grounds:**
  - /tmp/rr/s4n: a 12-word copied run (which fails at the default of 8) with `N=40 git commit` printed "passed copying from books … All checks passed; committing."
  - /tmp/rr/s4n2: an honest rule with `N=3` printed "FAILED copying from books" and was stopped.
  - The recheck never reruns the copying check.
- **Connection:** The copyright rule; the "full plain-word names" rule; rule 3.
- **Proposed change:** run_all_checks passes a fixed run length to the copying check. Any override for use by hand gets a full name and is ignored by the gate.

**N10. The copying and large-file checks read only some file types, and with the books absent nothing asks. Verdict: bears. Should change.**
- **Target:** overlap_check.py line 123 (.md only); run_all_checks.py line 99 (.txt only); review_receipt.py lines 128–137 and 182.
- **Defect:** Copying is checked only in .md files, and the size limit applies only to .txt files. With the books absent, which is most sessions, a file outside the reviewed folders needs no receipt, though the NOT RUN line says one is needed.
- **Grounds:**
  - /tmp/rr/s4c: 30 consecutive words of one book in drafts/notes.txt printed "passed copying from books … All checks passed; committing."
  - /tmp/rr/bk, books moved away, with generated text (not a book): a 239,613-byte drafts/big-notes.md printed "passed no book files / NOT RUN copying from books / no book text here; the review receipt must say what book text a change adds / … review receipt: not needed (no reviewed file changed) / All checks passed; committing."
- **Connection:** The CLAUDE.md copyright rule covers everything committed.
- **Proposed change:** Read every committed text file, and apply the size limit to all of them. When copying is NOT RUN, require "Book text:" for any sizeable added text anywhere.

**N11. Single words cut from registered titles can go on the allowed list. Verdict: bears. Should change.**
- **Target:** overlap_check.py line 109, where "part of" a title is accepted.
- **Defect:** Any part of a registered title is accepted, down to one word. "the", "of", "to", "story" and so on then drop out of every span.
- **Grounds:** /tmp/rr/s4.
  - 16 single words from the titles were added; `--check-allowed-list` printed "TOTAL problems: 0".
  - Book runs of 8 words or more that would then count as allowed: 164 in The Anatomy of Story (longest 12), 212 in The Anatomy of Genres, 15 in Egri, 10 in McKee.
  - A planted 12-word run printed "[12 words, allowed (title or name)] … TOTAL problem spans >= 8 words: 0". With the list as committed it printed "[12 words, PROBLEM]", exit 1.
- **Connection:** The list's own note says "a phrase from a book's text can never be allowed here".
- **Proposed change:** Allow only whole registered titles and author names. Add a planted test with "the".

**N12. The planted-fault test can call itself again without end. Verdict: bears. Should change.**
- **Target:** test_checks.py line 562 (`loosened_with_other_work`) with check_commit.py lines 162–169.
- **Defect:** The planted-fault test's gate tests commit through the gate being tested. If that gate lets the planted mixed commit through (for example after an intended relaxation), the gate in the copy runs its own planted-fault test, which does the same again, level after level.
- **Grounds:** /tmp/rr/e1: the mixed-change refusal switched off, with that test retired. After about 6 minutes, `ps` showed 9 nested test_checks.py runs about 12 s apart. I stopped them by hand, and a crashed group had left 6 /tmp/workshop-test-* folders.
- **Connection:** This is a hang, not a pass or a fail, on an honest correction of the gate.
- **Proposed change:** Set a marker setting in test_checks.py's copies, and have check_commit.py skip the planted-fault stage when it sees it. Stop the whole process group when the time limit runs out.

**N13. Claude's own tools can change the gate unasked, and some commands slip past the shell hook. Verdict: bears. Should change.**
- **Target:** protect_frozen_files.py (frozen files only); refuse_check_bypass.py lines 129–190.
- **Defect:** Claude's Edit and Write tools can change .githooks/pre-commit and every check script with no question asked.
- **Grounds:** /tmp/rr/hooktry.py.
  - Edit and Write of those files: "let through".
  - Also let through: `sed --in-place` and `perl -pi` on pre-commit; a Python one-liner writing to it; `git checkout HEAD~1 -- .githooks/pre-commit`; `bash -c`, `sh -c` or `eval` wrapping `commit -n`; `git -C "…"` or `cd "…"` quoted into the repository from /tmp; `--git-dir=`; `git commit-tree … | git update-ref`; a write to .git/workshop-checked-up-to.
  - A false alarm: `git config core.hooksPath /tmp/rr/base/.githooks`, the absolute path to the gate's own folder, is REFUSED.
- **Connection:** The note honestly says "usual spellings only", but the Edit tool is the usual way an agent changes a file, and N1 shows one word is enough.
- **Proposed change:** Return permissionDecision "ask" (so the person must approve) for edits to .githooks/*, the check scripts and .git/workshop-*. Read the quoted argument of `bash -c`, `sh -c` and `eval` as a command. Accept the absolute path to .githooks.

**N14. The frozen check reads files through local git settings and links. Verdict: bears. Should change.**
- **Target:** check_frozen_files.py lines 51–53; check_commit.py line 105; recheck_commits.py line 114.
- **Defect:** A theory's fingerprint is taken from the file as git writes it out on this machine. So a local filter, or a link to a file outside the repository, shows the check the original text while the repository holds something else.
- **Grounds:**
  - /tmp/rr/sf: a local filter (.git/config plus .git/info/attributes, never committed) writes out the original theory. An edited theory printed "passed frozen files … All checks passed". `git show HEAD:sources/bond-theory.md | tail -1` printed the added sentence. The recheck printed "TOTAL problems: 0"; with the filter removed it printed "frozen file has changed".
  - /tmp/rr/sl: the theory replaced by a link printed "passed frozen files … All checks passed"; the committed theory is a "blob of 23 bytes, content: /tmp/rr/outside-bond.md".
- **Connection:** The CLAUDE.md row says "Frozen files unedited | By itself".
- **Proposed change:** Fingerprint the committed contents (`git cat-file blob :path`, or `<commit>:path` in the recheck), and refuse a frozen path stored as a link.

**Minor findings (each bears; each minor):**
- **N15, correction notes in the log** (check_records.py lines 68 and 110–111). Correction-note lines are left out of the comparison. In /tmp/rr/cn I rewrote an existing "*Corrected in entry 28:*" note, and added two notes that wrap entry 3 in an HTML comment (`<!--`, `-->`), which hides it on screen. It printed "TOTAL problems: 0". Proposed: notes may only be added; refuse `<!--` and `-->` in the log.
- **N16, old receipts** (review_receipt.py lines 140–147). A committed receipt can be edited or deleted. In /tmp/rr/rc: "Reviewed by" changed to "the owner (changed afterwards)" and another receipt deleted printed "All checks passed". A full recheck printed "rechecked 3 commit(s) … TOTAL problems: 0". Git history keeps the originals. Proposed: .claude/reviews/ may only be added to.
- **N17, the gate's recheck report** (check_commit.py lines 136–145; check_records.py line 51).
  - On the first commit the recheck says "not checked: the commit gate is not in this history yet", but the gate shows "passed earlier commits the gate may not have seen" (/tmp/rr/first). That contradicts rule 2.
  - Problems in the staged files are printed a second time under "earlier commits …" with "rechecked 0 commit(s)" (/tmp/rr/s1a).
  - check_records.py's note says recheck_commits.py uses `--log-only`; it does not.
- **N18, owner quotes.** `"…" (from Bond, …)` and a `> …` block quote with (Bond, …) after it are not read (/tmp/rr/oq: "TOTAL problems: 0").
- **N19, Book text rule** (review_receipt.py line 115). The source register is read from disk, not from the staged files. /tmp/rr/bt: the Book-text demand ("the book texts are not here …", exit 1) disappeared after an unstaged edit of the register ("… is complete", exit 0).
- **N20, frozen files in subfolders** (check_frozen_files.py line 84). sources/revisions/bond-theory-2.md, not on the frozen list, printed "TOTAL problems: 0".
- **N21, names.** The setting `N` (see N9). kept-cases/run-kept-cases.js uses `A`, `c` and `p`, and its `args` note lists `planted` twice with two different shapes.

---

## 3. The runs asked for

- **test_checks.py** in /tmp/rr/t1 (the working copy as of 14:20) ended "ok hook: session start says the checks could not run when they are broken / TOTAL tests: 118, failed: 0", exit 0, in 16.4 s. Rerun at 14:49 in /tmp/rr/t2, a copy made after the maker's prose edits: "TOTAL tests: 118, failed: 0", exit 0.
- **run_all_checks.py** on /home/user/StoryTest (read-only; run at about 14:20 and at 14:48): "passed frozen files, maps, records, owner quotes, allowed titles, no book files, copying from books / RESULT: no check failed", exit 0, in 1.6 s. The notes were:
  - "not checked: whether the list was only added to (the list has no earlier version in HEAD)";
  - "entry 29 is new: look at each status line again";
  - "kept cases not rerun since these skills changed: character, dialogue, genre, plot, story-world".

  `git status --porcelain` was identical before and after.

## 4. Notes at the top and names

Every script under .claude/skills/*/scripts and .claude/hooks has a plain note at the top saying what it does, checked with Python's parser. So do .githooks/pre-commit, pre-merge-commit, .gitattributes, overlap-allowed.txt and frozen-files.txt. The Python scripts contain no one- or two-letter names; the shortest are the function names git, run, add and one. The exceptions are in N21.

## What I checked and found right

- The two S1 routes, S2, S3 (a) to (c), S4 (a), S5, S7, S8 and S10 to S17 are closed, with the output quoted above.
- The first-commit path. In /tmp/rr/first, a copy of the real history with the whole build staged, the gate printed "note: the commit gate is new in this commit …" and stopped only for the missing build receipt (`.claude/reviews/23656000500f0899.md`). With a receipt it committed, and the next ordinary commit printed "rechecked 1 commit(s) since 35f293956 … All checks passed".
- Removing check_commit.py to reach the first-commit path again is well guarded (/tmp/rr/fc): the maps check and 19 planted tests failed.
- A whole book sentence put in the register is caught by the copying check.
- A frozen-list line travelling with its new theory commits cleanly, as the current skill text now says.
- The recheck is fast: 60 commits in 2.5 s.
- Nothing was written to the real repository.

## What I did not check

- The hooks inside a live Claude Code session. I fed them the input a session would send, and did not try a refused command in the real project.
- Real Windows or macOS, including whether `python3` exists on Windows. Git versions other than 2.43.0, and Python other than 3.11.15.
- Checks run on GitHub; `git revert`, `git rebase` and worktrees.
- Whether a real reviewer would spot the fake receipts, which is on trust by design.
- The skills' prose, and run-kept-cases.js and book_to_text.py beyond their headers.
- I did not measure how long N12's recursion would run unchecked.
- The gate-removal route (/tmp/rr/fc) was run only to its first commit.
- Prose files changed during my review; scripts and hooks were unchanged at 14:45 UTC.

## Overall

**Not passed.** Must change: N1 and N2. Should change: N3 to N14. Minor: N15 to N21.

The review should pass once N1 and N2 are made and reviewed, each with planted tests: the gate always uses the last commit's copy of itself and records what it approved; the recheck uses the checks from its starting commit and runs the whole gate on every commit it sees. N6 to N8 and N14 are the next priority, because the same approval record puts most of them right.
