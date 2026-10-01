# The third look at the error-correction build: the three reports, 24 September 2026

What this is: the three reviewers' reports, word for word as each agent returned it. The reviewers made no edits; every experiment ran in scratch copies. Their briefs, the check of those briefs, the known fault left in for them, and the lead's plan for answering them are kept beside this file, in `2026-09-24-build-third-look-briefs-and-plan.md`. How each finding was answered is in the build's review receipt. No book text is quoted in them. Kept for log entry 30.

---

## 1. theory-checker

## Theory-checker, third round: the edits 1e92459..5e5564d (the answers to the re-review)

**How I worked.** I read CLAUDE.md, the term sheet, the kinds table, C1 to C15, the kept re-review reports and the diff. For the theory passages I read the theory first: Gap lines 24, 26, 57, 59 and 64; Anticipation lines 15, 25, 41, 47 and 67; foundation lines 373 to 391. I made no edits in the live repository. Every experiment ran in copies of the snapshot's last commit (`git archive 5e5564d`) under `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/r3-theory-checker/`, in the folders `base`, `base9`, `fresh` and `bk`.

One disclosure. The live bypass hook refused one of my scratch commands because it carried git's skip switch (`-n`). I did not get round the hook. For the "commit made where the gate is off" case, I used a fresh copy where the gate had never been switched on, as `test_checks.py`'s own copies do.

---

### Must change

**R1. A commit that changes only checks can loosen the log check and rewrite an old log entry in the same commit. The gate passes and stamps it, and the recheck never looks at it again.** This is new in these edits.
- **Target:**
  - `check_commit.py` lines 170–172 and 196–200. When `only_checks` is true, `record_scripts = staged_scripts`, and the project story, the corrections file and the register count as allowed riders.
  - The statements that claim otherwise:
    - CLAUDE.md line 32 ("so a check cannot be loosened in the same commit as the work it would stop");
    - CLAUDE.md line 40 ("By itself within one commit");
    - CLAUDE.md line 42 ("Old log entries never rewritten … By itself");
    - error-correction SKILL.md line 118 and line 227;
    - checks-and-cases.md line 29, and line 40, which says "changes only checks" without saying the log rides along;
    - `27 Corrections.md` line 23 ("by itself, within one commit");
    - the project story line 75 (word list, Commit gate) and line 45 (How the pieces fit).
- **Defect:** the new exception, added for M2, judges the log (and the corrections file and the register) with the changed checks. The first round's S1 route B is open again: a check change, a log rewrite and a receipt in one commit.
- **Grounds:** in `base9` I staged a `check_records.py` loosened to skip entry 9 (`if number == 9: continue` in `compare_logs`), a rewrite of entry 9, and a filled receipt. The gate printed:
  - "note: this commit changes only checks, so its own changed checks run on it…";
  - "passed records";
  - "passed the last commit's planted-fault test, on the changed checks";
  - "All checks passed; committing."

  The commit carries "Workshop-gate: approved f7ed398…". `recheck_commits.py` then printed "rechecked 0 commit(s) the gate did not approve … TOTAL problems: 0".

  The same try on entry 7 (`base`) was stopped only by chance: planted test 11 happens to rewrite entry 7 ("FAILED recheck: a commit outside the gate that loosens a check…").
- **Connection:** CLAUDE.md tells the owner that this rule holds "by itself" within one commit. It holds only on trust in the receipt. C15's own reopen condition ("a way round a check … that no planted fault covers, other than the limits the gate's description states") is met. By SKILL.md's fifth tripwire this is a third firing for C15, because `test_checks.py`, the named catch, passed it.
- **Change, either way:**
  - (a) in a commit that changes only checks, run the last commit's records, frozen-files, copying and allowed-titles checks on the riders; or
  - (b) state the limit in every place listed above.

  In either case, plant this route in `test_checks.py`.
- **Verdict:** bears. **Severity:** must change.

---

### Should change

**R2. The reason given for leaving N3 partly undone does not hold.**
- **Target:** the maker's reason ("the records check applies one rule to every old entry, and the existing planted rewrite tests that rule"); CLAUDE.md line 40 ("the planted faults that exist").
- **Defect:** planted faults exist to catch a changed check, and a changed check need not apply one rule to every entry.
- **Grounds:** R1's run. A check loosened to skip entry 9 passed the whole last-commit planted-fault test.
- **Connection:** the two planted rewrites (entry 5's title, test 11's entry 7) catch only loosenings aimed at those two entries. With R1's exception this becomes a route within one commit.
- **Verdict:** bears. **Severity:** should change. Plant rewrites of every old entry, or of a body line and the last entry, as N3 proposed.

**R3. "Stops honest mistakes" leaves out the honest routes the scripts' own notes admit.**
- **Target:** SKILL.md line 118 and the table row at line 228; README line 89; S10 (line 95); C15 line 151; project story lines 12 and 75.
- **Defect:** these say the gate stops honest mistakes and fails only against a deliberate agent. They leave out two routes that need no ill intent.
- **Grounds:**
  - `recheck_commits.py`'s note: a commit made outside the gate that changes the recheck "is judged by the changed version … whether or not the change was meant to loosen anything".
  - R1's route, which an honest but wrong correction to a check can also take.
  - CLAUDE.md line 51, checks-and-cases.md line 44 and kinds row 28 do state the outside-commit route.
- **Connection:** the statements disagree with each other, and five of them claim more than the scripts.
- **Verdict:** bears. **Severity:** should change.

**R4. "Report every unstamped commit they see" is more than the scripts do.**
- **Target:** CLAUDE.md line 51; checks-and-cases.md line 44.
- **Grounds:** in `bk`, two commits made where the gate was off added and then removed an ebook file.
  - The recheck printed "rechecked 2 commit(s) the gate did not approve … TOTAL problems: 0".
  - `session_start.py` printed nothing about either commit, and then "Machine checks: none failing".
  - `session_start.py` line 101 drops the "rechecked" line.
- **Connection:** the scripts judge each unstamped commit and name only the ones with problems.
- **Verdict:** bears. **Severity:** should change. Say "judge every unstamped commit, and report those with problems".

**R5. The reason for leaving N2 partly undone holds for the maps and owner-quotes checks, not for book files and copying.**
- **Target:** `recheck_commits.py`'s note ("the next commit through the gate runs them on the whole of the files as they then are"); CLAUDE.md line 44 ("No book file committed … By itself where the books are present").
- **Defect:** the copyright rule is about what is ever committed. Text added and removed between two gate runs stays in the history. The note also does not name the no-book-files check at all.
- **Grounds:** the `bk` run in R4. `grep -n -i book recheck_commits.py` finds nothing.
- **Verdict:** bears. **Severity:** should change. Either recheck each unstamped commit for book files and copying, or scope the CLAUDE.md row.

**R6. The rule for retiring a planted test is stated in no skill text, and it goes against the reason given for S10 (b).**
- **Target:**
  - `check_commit.py` lines 318–319: a protected test may be retired only if `"owner" in reviewer.lower()`.
  - The skill texts that give only "named under 'Tests retired', with why": checks-and-cases.md line 58, reviews-and-briefs.md line 30, SKILL.md line 207.
  - S10 (b) and C15 line 152.
- **Defects:**
  - The skill says less than the script.
  - S10 (b) declines "ask the owner before gate edits" because "your yes would be a click rather than a review". Yet the script names the owner as the only allowed reviewer for retiring tests that guard the frozen files, the log, the receipts and the gate.
  - From reading the code: the word "owner" anywhere in the reviewer line satisfies the test (for example "not the owner"). I did not run this.
- **Grounds:** in `base` I tried to retire the protected test "recheck: …" with "Reviewed by: theory-checker". The gate refused it ("COMMIT STOPPED"), which is right.
- **Verdict:** bears. **Severity:** should change. State the rule in the skill, square it with S10 (b), and tell the owner what being named would ask of them.

**R7. The planting rule files the Gap theory's own case of surprise under Shock, without a label.**
- **Theory first:**
  - Gap line 57: surprise is "a gap you didn't know was there: you thought you understood and you were wrong".
  - Gap line 59: the bomb that "simply goes off gives the audience fifteen seconds of surprise". Anticipation line 41 says the same.
  - Anticipation line 25: Shock, "it arrives without warning".
  - Term sheet section 13 item 9 records that the theories call this bomb *surprise*. S13 (questions file line 98) puts "'surprise' against the rung called Shock" to the owner.
- **Target:**
  - plot `references/reveals-and-withholding.md` line 30: "A turn meant only as a shock … (the Anticipation theory's Shock; the Gap theory's bomb that simply goes off), needs no set-up";
  - writing-rules-and-rivals.md line 9 ("walking the unshown bomb … a shock needs no set-up at all");
  - C12 line 126 ("a shock like that").
- **Defects:**
  - An open S13 point is settled with no label.
  - The surprise branch's gloss ("a gap you did not know was there") also covers the bomb, so the theory's own case falls under both branches, with opposite advice.
  - The copies were not brought into line. The same module's section 1 (line 16) and plot SKILL.md step 4 (line 106) still give every surprise "plant, hide, reveal".
- **Connection:** the rule card's new step 4 ("say what each case is a case of, in the theory's own words"), walked on this rule, flags it: the unshown bomb is, in the theory's own words, a case of surprise.
- **Verdict:** bears. **Severity:** should change.
  - Label the reading "the workshop's reading, S13 (term sheet section 13, item 9)".
  - Gloss the surprise branch with "you thought you understood and you were wrong".
  - Bring section 1 and step 4 into line.

**R8. The tripwire rule is stated in two places, and the two now disagree.**
- **Target:** reviews-and-briefs.md line 48 ("A finding on a staged change … is that stage working, even when the corrections file names a catch for its kind") against SKILL.md line 215 (the fifth tripwire).
- **Grounds:** C15 line 151. Its named catch, `test_checks.py`, passed ways round that a reviewer found before commit. C15 records "The tripwire fired a second time"; line 48 says it did not fire.
- **Connection:** line 48 is right for use-tester's S3 case, where the reviewer is the named catch. It is wrong when the named catch is a check that let the error past.
- **Verdict:** bears. **Severity:** should change. Add to line 48: "when the stage that caught it is the one named for its kind".

**R9. "Every finding of both notes is now applied" is still not true, and the project story says something different.**
- **Target:** file 26 line 129, against project story line 137 ("applied or listed as not applied, with reasons"). No list of unapplied findings exists.
- **Grounds:** the kept break test.
  - Line 32 (pulls): "'Why lock you up?' would displace or duplicate A's 'Like that.' (A:706)"; and the napkin ring, as a spoken line, adds a rule to the overloaded demonstration scene.
  - Line 13: more A set-ups the table misses (A:535-537, A:577, A:1144-1146, A:1467, A:439).
- **Connection:** the defect F2 named, told to the owner a second time.
- **Verdict:** bears. **Severity:** should change. List what was left, with reasons, or apply it.

**R10. File 26's new ledge-escape fix ("pick one") can remove what row 4 faults.**
- **Target:** file 26 line 57.
- **Grounds:**
  - Row 4 (line 50) faults that "In B, Iona does not work it out herself".
  - The break test's second rival (line 17) calls A:590 against B:551 "a character choice rather than a set-up".
  - Both versions show the ramp, so "adding A's cage and ramp" counts the ramp twice.
- **Connection:** "pick one" of three routes to one job can drop Iona's conclusion, which does a second job.
- **Verdict:** bears. **Severity:** should change. Pick one set-up route, and keep Iona drawing the conclusion.

**R11. The theory-checker agent still carries a closed list of order words.**
- **Target:** `.claude/agents/theory-checker.md` line 34: ("cuts", "adds", "restores", "the revision").
- **Grounds:** F1 asked for open-ended lists, and C1 line 37 says "both now say the words are only examples". This file was edited in this diff, but that line was not.
- **Connection:** a rule changed in some places and not its copy, in the one reviewer that checks write-ups.
- **Verdict:** bears. **Severity:** should change.

**R12. Order words remain in file 26, so "what remains assumes no order" overclaims a fourth time.**
- **Target:** file 26 line 12 ("now say what B still has") and line 50 ("B still shows the ramp"); the claims at line 130, C1 line 38 and project story line 137.
- **Grounds:** the phrase comes from the break test, line 16: "Row 4 overstates the change: B still shows the ramp". There, "still" is tied to "the change". Flip test: had B come first, one would write "B has" or "B does show", which lose nothing.
- **Verdict:** bears. **Severity:** should change. Given C1's history, reword both phrases, each for one word.

---

### Minor (each bears unless noted)

- **R13. Test counts.** The records say 142 tests (project story lines 13 and 138; C15 line 152). At 5e5564d, `test_checks.py` in `fresh` printed "TOTAL tests: 144, failed: 0". The two `setting_tests` came in 5e5564d, and "28 fail on the re-reviewers' scripts" was not rerun with them.
- **R14. Entry 29 misdescribes C12's error.** Project story line 133 says the bomb was used "as grounds for hiding a twist". The b2617b3 text, C12 line 126 and writing-rules line 9 all say it was grounds that "one clear showing can be enough".
- **R15. The plan part of the corrections.**
  - C6 (line 78) still has no plan part.
  - "Does not apply, because recorded before the rule existed" misstates the responses made in entry 29, after the rule existed (C4, C6, C12's second error, C13). C1 and C15 honestly say "not written before".
- **R16. S12 is unchanged.** It still says "File 26 now gives its verdicts without assuming an order", while C1 line 37 says every record that called the file clean "were corrected".
- **R17. Kinds row 22 is stale.** Its "Last seen: entry 26" should be entry 29, since F2 and F12 found this kind there.
- **R18. The after-commit reminder is shorter than the claim check.** SKILL.md line 196 says the hook repeats the claim check. The hook's text lacks "read every sentence that compares two versions".
- **R19. The receipt form does not ask for the smaller-change plan.** Its "Change" hint (`review_receipt.py` line 263) does not carry step 4's new instruction for smaller changes.
- **R20. S10 (b) gives only one side.** It gives the cost of the option, not what it buys: an edit to the gate could not then happen unseen. The owner's choice should see both.
- **R21. The reason for "Not tried" is thin.** The retiring rules can be tried by hand in a scratch copy, as R6's run shows. The reason explains why no planted test covers them, not why they were not tried.
- **R22. The open-corrections status line adds conditions.** Project story line 14 adds "kept cases" to C3 and "the process tried" to C12; neither correction's own status says so.
- **R23. File 26 leftovers.**
  - The heading "carry these into A" (line 88) now holds an "optional" napkin ring, and a mask set-up where A has its own.
  - Line 128 says the bare "Eli." carries no reason on the page, while line 95 now gives A:697.
- **R24. "Has not finished" (does not bear yet).** Project story line 12 says the trial "has not finished", while entry 29 lists it as not yet done. Settle it: was the trial started?

---

### Marks on new or changed rules

- **Planting rule, shock clause:** held by its scope job; held if S13 is read that way; unlabelled (R7).
- **Planting rule, "more weight, such as a held shot, a character's attention, or another scene":** held (noticeability). The examples are loose by design, and marked as examples. F22 is answered.
- **Plot section 6's pointer to section 2:** held (the building route).
- **Claim check, and the reply check's open lists:** held (C1's third recurrence). The example words are loose on purpose. The reply check is identical in all five skills (md5 `6a9a9dfe…`).
- **"With its question number if it has one":** held.
- **Step 4, the plan for smaller changes:** held (the list is fixed before results, Part XI). The form's hint lags (R19).
- **The mapping from marks to verdicts:** held, now labelled as the workshop's. "Two routes" and "held if unknown" are mapped.
- **The tripwire wording in SKILL.md:** held. Line 48 of reviews-and-briefs is loose against the fifth tripwire (R8).
- **Rule card step 2 ("in groups") and step 4 ("what each case is a case of"):** held.
- **The K3 wording:** held; it matches foundation line 391.
- **The typo row's fingerprint line:** held. Planted neighbour at `test_checks.py` line 840.
- **The checks-only exception:** held by M2's job for the checks themselves. Its riders are loose: they are not needed for that job, and their records job needs the old checks (R1).
- **Rivals:** none new.
- **Worked example:** SKILL.md step 4 comes from C1, not from a kept case. The new plot text tells no kept case's story; I read only the titles and "Aimed at" lines.

### Checked and found right

- **F3 to F22, answered in content:**
  - F3 (C12's note); F4 (both schedules named); F5's pointer (section 3); F6 (card step 4); F7 (a sound reading).
  - F8: C15 is relabelled "written after".
  - F9: C1, C4, C6 and C15 now match their conditions.
  - F10 and F11: taste items moved out; the note is complete.
  - F12, F13 (six places), F14, F15 (C9), F16, F17, F18 (rows 1 and 2), F19 (S4 and S7 labels match their questions), F20, F21 (C14's plan).
- **F1 and F2 in part:** four phrases reworded, and three findings applied (R9, R11, R12).
- **Use-tester S3 and S4 answered:** the frozen-list exception is stated in three places and in add-source. The word-answered minors are answered: the command for old tests, the description lagging by one commit, the section 3 pointer, section 6's route, character's route back, CLAUDE.md's detour, the tripwire wording, the promise to search, and the theory glob. The glob also fits add-source's top-level revisions.
- **Kinds row 24:** every innocent neighbour it names exists (`test_checks.py` lines 311, 546, 691, 741, 766, 840).
- **C4:** its "not passed" claim has both tests (lines 537 and 546).
- **Machine checks on `fresh`:** every check passed; copying printed NOT RUN; `check_owner_quotes` printed "104 quotations match".
- **Session start:** it now lists the open corrections (use-tester S1).
- **CLAUDE.md:** it matches the snapshot byte for byte.

### Not checked

- The other scripts' behaviour beyond R1, R4, R5 and R6: section 3 of the re-review (N1 to N21), and the claim "28 fail on the re-reviewers' scripts".
- Whether the kept re-review reports are word for word.
- The kept cases, and any run of them.
- Copying (no books).
- Faults 2 to 5 of file 26.
- The owner-named retirement path, and merges and amends by hand.
- Modules not in the diff, beyond the searches named above.

## Verdict: passed after changes

**Must change:**
- **R1:** a check loosened in a commit that changes only checks passes a rewritten log entry, and the commit is stamped. Correct the exception, or state its limit in every place listed, and plant the route.

**Should change:** R2 to R12. These edits then need a look of their own, by a reviewer who did not make them.

Main files: `/home/user/StoryTest/.claude/skills/error-correction/scripts/check_commit.py`, `/home/user/StoryTest/CLAUDE.md`, `/home/user/StoryTest/.claude/skills/error-correction/references/checks-and-cases.md`, `/home/user/StoryTest/.claude/skills/plot/references/reveals-and-withholding.md`, `/home/user/StoryTest/26 Test - The Catch - two versions.md`, `/home/user/StoryTest/27 Corrections.md`, `/home/user/StoryTest/.claude/agents/theory-checker.md`.
---

## 2. use-tester

# Use-tester, third look: the edits 1e92459 to 5e5564d, walked through situations (a) to (i)

**Overall verdict: passed after changes.** The edits answer the second round's four must-change findings (M1 to M4) in content, and S1 to S4. Walking them showed three new must-change faults, all in the recheck the M2 and M3 fixes rebuilt:
- **U1:** one honest rebase can stop every later commit, and nothing clears the stop.
- **U2:** every commit the gate did not stamp stays on the recheck's list forever. The list grows until nothing can be committed.
- **U3:** a late receipt that says "withdrawn" is believed without looking. A rejected change can stay in with every check green.

These are the kind of error the corrections file names ("a change that makes a new error"; "a step that stops honest work, or leaves no way through").

**Where things are.** All runs were in copies under `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/r3-use-tester/`.
- `w0` is the live history (HEAD 35f2939) with the 5e5564d files committed through the gate as its first gated commit (fe487cf, stamped).
- Before building it I compared all 115 tracked files with the live working tree using `cmp`. None differ, and the live tree has no untracked file that `w0` lacks.
- Every receipt in my copies is marked SIMULATED; the reviewer reports in them are stand-ins I wrote.
- On the 5e5564d files, `test_checks.py` printed "TOTAL tests: 144, failed: 0" in 38 seconds.

---

## 1. The second round's findings in my area

| Item | Answered? | What I ran |
|---|---|---|
| M1 | Yes, in content | In `wb` I set Q3 to `rechecking`: the check listed the 4 skill passages as notes, 0 problems. I marked them "answered" and closed Q3: only "note: kept-cases/03-...:28: this kept case cites Q3...", runs not searched. Committed through the gate (2e84912). |
| M2 | Yes for the route | In `wg` a late "not passed (withdrawn in this commit)" receipt was accepted, and the withdrawal commit passed (c30abda). But see U3 and U6. |
| M3 | Yes, in content | In `wm3` an outside commit loosened `review_receipt.py` and added a plot rule. The session start reported 12 problems for it, including the parent's planted-fault test failing on the loosened check. |
| M4 | Yes, for an up-to-date skill | In `we`, after a typo in plot, the records check still listed character, dialogue, genre and story-world (6c46721). See U7 for the other paths. |
| S1 | Yes | The session start lists "Open corrections (27 Corrections.md): C1, … C15". Planted test at `test_checks.py` line 929. |
| S2 | Yes | A stale stamp now fails only "records"; the earlier-commits line printed "passed … rechecked 0 commit(s)". |
| S3 | Yes | `reviews-and-briefs.md` line 48 now agrees with SKILL.md's tripwires. |
| S4 | Yes | SKILL.md line 207 and `reviews-and-briefs.md` line 30 treat the frozen list apart, which matches the scripts. |

The minor items:
- **Put right:**
  - the command for running new tests on the old check (`checks-and-cases.md` line 56);
  - the description that must follow a check in the next commit (step 5, walked);
  - the bomb pointer, now "section 3" (line 40 holds the bomb);
  - section 6 now points to section 2;
  - the hint now says `new --commit <commit>`;
  - the character route now comes back to Step 9;
  - the CLAUDE.md detour for a writer's objection is gone;
  - the tripwire wording;
  - the garbled message;
  - the `*-theory.md` glob: no copy is left outside the kept reports.
- **Not put right:** "the stop is a sign (loop, step 1)" still does not say where to write it down (stall list, c).

---

## 2. New findings

### U1. A change to the gate's own files, made without the gate, stops every later commit, and nothing clears it
- **Target:**
  - `.claude/skills/error-correction/scripts/recheck_commits.py`, lines 193 to 196, and its note at lines 30 to 31.
  - The claims about it: `references/checks-and-cases.md` line 38 ("always reported, for a person to look at") and line 44; SKILL.md line 228; CLAUDE.md line 51; README.md line 89; S10 (questions file, line 95).
  - The advice at `checks-and-cases.md` line 46: "merge a pull request with a merge commit or by rebasing".
- **Defect:**
  - The recheck counts this flag as a problem, at every run, for good. No receipt, review or owner step clears it; only a "withdrawn" receipt does (U3).
  - A commit that corrects the recheck is judged by the last commit's recheck, so it is stopped too.
  - The last way out in the text ("tell the owner") names nothing the owner can do.
- **Grounds:**
  - In `whook`, a one-line comment in `.claude/hooks/after_commit.py` went through the gate alone, with a full receipt. The last commit's planted-fault test passed on it and it was stamped (4182675).
  - The main branch moved by one reviewed genre commit, and `git rebase` made 59800f0: the same change, now unstamped.
  - The next ordinary commit printed: "FAILED earlier commits the gate did not approve / commit 59800f0fd: changes the gate's own files (.claude/hooks/after_commit.py) without the gate; a person should look at it…".
  - In `wg3`, an outside edit to `.githooks/pre-commit` got a late receipt with the verdict "passed". The commit carrying that receipt was stopped by the same line.
  - `test_checks.py` has no test with "gate's own" or "person should look" in it.
- **Connection:**
  - The kinds table row "A check or a step that stops honest work, or leaves no way through" (`27 Corrections.md` line 24) promises an innocent neighbour in `test_checks.py` for each such route. This route has none.
  - An honest rebase reaches it, and so does the rebase the skill recommends for pull requests, and so does the owner editing a hook on GitHub.
  - Five places tell the owner this is "reported for a person to look at". In fact it stops every commit, with no end.
- **Proposed change:** let a late receipt that names the owner as reviewer settle the flag (the same rule `PROTECTED_TESTS` uses). Plant the honest rebase of a reviewed hook change as a neighbour. Say in those five places what the person does.
- **Verdict:** bears. **Must change.**

### U2. The recheck never settles a commit, so outside check changes pile up until nothing can be committed
- **Target:** `recheck_commits.py`:
  - lines 13 to 18 and 245 to 248: every unstamped commit since the gate came in is looked at, every time;
  - lines 204 to 221: the parent's whole planted-fault test is rerun for each unstamped check change;
  - lines 69, 256 to 259 and 276 to 280: a 90-second limit, where running out is a failure.
  - Also `session_start.py` line 35 (a 40-second limit).
  - The version the re-reviewers saw kept a marker ("every commit since the last one it passed", 1e92459 lines 9 and 42 to 62). The edits removed it.
- **Defect:**
  - A late receipt makes an unstamped commit pass, but it is still rechecked in full at every commit and every session start, for ever.
  - Each unstamped check change costs one run of the planted-fault test, 38 seconds here.
  - Past 90 seconds the recheck prints "ran out of time" and exits 1. From then on every commit is stopped, including a correction to the recheck itself.
- **Grounds:**
  - In `wt`, three outside commits each added one comment line to `check_records.py` (each a check change on its own) and were pulled in.
  - Three late receipts with the verdict "passed" were committed through the gate (passed, 1 minute 44 seconds; 9445466).
  - The next unrelated commit, a log entry, printed "FAILED earlier commits the gate did not approve / not checked: 1 later commit(s); the recheck ran out of time".
  - The session start there printed "Recheck of earlier commits: could not run (it took too long)".
  - There is no planted test for the time limit.
- **Connection:** every exit the text offers goes through this same recheck: a late receipt, a commit that changes only checks, telling the owner. Honest outside check changes (a copy where the gate was never switched on, which README line 89 allows, or an edit on GitHub) never leave the list. How many it takes depends on the machine; the list only grows.
- **Proposed change:** settle a commit once a later commit through the gate has passed its recheck. Keep that record in the history, so a fresh clone agrees. Plant it: several late-reviewed outside check changes, then an unrelated commit goes through.
- **Verdict:** bears. **Must change.**

### U3. "Withdrawn" is taken on the receipt's word, and it also erases the flag for the gate's own files
- **Target:**
  - `recheck_commits.py` line 175 and lines 190 to 191. A receipt whose verdict says "withdrawn" ends the recheck of that commit before the gate's-own-files flag and the rule that a check change comes alone.
  - `review_receipt.py` lines 213 to 215, which check only that the word "withdrawn" is there.
  - `test_checks.py` lines 541 to 548. That neighbour is named "with the change withdrawn", withdraws nothing, and expects a pass.
  - The text: `checks-and-cases.md` line 46 and `reviews-and-briefs.md` line 32.
- **Defect:** nothing checks that the change was taken out.
- **Grounds:**
  - In `wg2`, an outside commit added "Show every clue at least twice" to `plot/SKILL.md` (C12's own error).
  - A late receipt with the verdict "not passed (withdrawn in this commit)" was committed with nothing withdrawn. The gate printed "All checks passed; committing." (c195d5d).
  - `grep -c` for the rule in `plot/SKILL.md` then printed 1. The session start printed "Machine checks: none failing" and reported no unapproved commit.
  - In `wg3`, the outside gate edit gave 2 problems. With the same "withdrawn" receipt staged and nothing reverted, the recheck printed "TOTAL problems: 0".
- **Connection:**
  - The slip is easy to make honestly. The text first says to write the late receipt "reviewed, then committed", and only then to take the change out. The planted neighbour itself writes "withdrawn in the next commit".
  - CLAUDE.md line 51 tells the owner "The gate stops honest mistakes and shortcuts".
  - This is the M2 fix making a new error.
- **Proposed change:**
  - The recheck should confirm that each file the commit changed is no longer as that commit left it, in the commit the receipt names or in HEAD.
  - Keep the gate's-own-files flag whatever the verdict.
  - Plant "withdrawn claimed, nothing withdrawn" as a fault, and correct the neighbour at lines 541 to 548.
- **Verdict:** bears. **Must change.**

### U4. The plot skill's new shock clause: two rules at odds, and wrong on two of the theories' own cases
- **Target:** `.claude/skills/plot/references/reveals-and-withholding.md` line 30, from "A turn meant only as a shock". Its copies are in `writing-rules-and-rivals.md` line 9 and `27 Corrections.md` line 126.
- **Defect:**
  1. **An open point written as settled.** The clause puts the Gap theory's bomb that "simply goes off" under the Anticipation theory's Shock, with no label. The Gap theory calls that case surprise. `owner-terms.md` section 13, item 9 records this very clash as open, under S13. The module's own section 1 (line 16) says a surprise is "plant, hide, reveal. It lasts seconds…". So the theory's own case now gets two rules: plant it (as a surprise), and give it no set-up (as a shock).
  2. **Scoped by intent, with no telling test.** Which turns the clause covers depends on what the writer "means", so a character reveal meant "as a pure shock" is excused from the set-up check.
  3. **"Buys seconds" is loose.** It is true of the bomb (Gap line 59; Anticipation line 41) and false of *Psycho*.
- **Grounds:** the walked cases.
  - **Twist clue (the check should fire; the clause should stay quiet).** "The housekeeper is the victim's daughter; she hums his lullaby once, in chapter 4." The building route (map row, line 34; section 6 now points to section 2) and the diagnosing route (row at line 123, sections 2, 3 and 7) both reach the rule. It gives: noticeable, light enough not to be guessed, more weight if it is easy to miss. The clause stays quiet. This agrees with Gap lines 57 and 64. Right.
  - **Jump scare (the clause should fire).** The clause gives "no set-up", which fits Anticipation line 25 ("Nothing: it arrives without warning | The jump scare"). But Anticipation line 84 says: "A jump scare on its own is a reflex, not fear. After real dread it works as a release valve; without dread it's just a flinch". The clause should say its "set-up" means a planted fact, not preparation.
  - **Near neighbour (should stay quiet; it fires).** "In chapter 20 the gentle grandmother is revealed as the poisoner. I want a pure shock, no clues." Meant only as a shock, and not meant to be seen on a second look, so the clause applies: "needs no set-up … this check is not for it". Bond theory line 84: "It breaks when they do something that contradicts who they've been without the story earning it." The same module's section 7 (line 93) and its rivals (line 101) say the opposite for this case, so both routes meet two rules at odds.
  - **The theories' own case, *Psycho*.** By term sheet 11.4's telling test ("get no warning at all (shock, the side rung)") the shower murder is a shock, so the clause says "buys seconds". Anticipation line 67: "After that, no guarantee holds and every threat is real". The plot skill's own `suspense-and-fear.md` line 59 says the same.
- **Connection:** the rule card's step 4 (line 25, edited this round) says to name what each theory case is a case of, in the theory's words, and then walk it. The Gap theory's words for the unshown bomb are "fifteen seconds of surprise". Walked that way, the clause renames that case, and gives the grandmother twist and *Psycho* the wrong answer. This passage (C12) has already carried two errors, both from fixes.
- **Proposed change:**
  - Scope the clause by what the turn does: a turn that depends on no planted fact and reveals nothing about who a character is (a threat's arrival).
  - Label the bomb's name as S13, item 9.
  - Drop "buys seconds", or add "unless it breaks a guarantee" (pointing to *Psycho* in `suspense-and-fear.md`).
  - Say that a jump scare still wants dread before it.
  - Change the rule card example and C12 to match.
- **Verdict:** bears. **Should change.** The theory-checker should confirm the S13 labelling.

### U5. An honest rebase fires when the same file changed upstream
- **Target:**
  - `review_receipt.py` lines 136 to 143. The fingerprint hashes `git diff --full-index`, which includes the files' internal names in git (they change whenever the file's contents change) and the line numbers of each change.
  - SKILL.md line 228 and `checks-and-cases.md` line 38 ("a cherry-pick or rebase whose contents changed").
  - `checks-and-cases.md` line 46 (merge a pull request "by rebasing").
- **Defect:** after a rebase with no conflict, a reviewed change whose file was edited elsewhere upstream gets a new fingerprint. Its receipt is no longer found, and every commit is stopped until a new review of a change already reviewed.
- **Grounds:**
  - `wrb`: upstream changed only the genre skill, and the rebase passed ("TOTAL problems: 0").
  - `wrb2`: upstream added a sentence elsewhere in `plot/SKILL.md`. The recheck printed "commit bcfabb22e: no review receipt .claude/reviews/282e840658905c2d.md … make one with review_receipt.py new --commit bcfabb22e after an independent review", and the next commit was stopped.
- **Connection:** the brief lists an honest rebase as a neighbour where nothing should fire. The text leads the agent to expect this only when the change itself changed, and it gives no light route, such as pointing to the original receipt.
- **Proposed change:** fingerprint only the lines added and removed. Or allow a late receipt that names the original when those lines are identical. Plant both neighbours.
- **Verdict:** bears. **Should change.**

### U6. How to take a change back out is not said, and `git revert` makes a new ungated commit
- **Target:**
  - `checks-and-cases.md` line 46 and `reviews-and-briefs.md` line 32 ("take the change back out").
  - The lists of what git runs no hook for (SKILL.md line 228; `.githooks/pre-merge-commit` line 5) leave out revert. No skill text mentions revert.
- **Defect:** `git revert` runs no pre-commit hook and leaves no stamp. The text does not say to use `git revert --no-commit` and then commit through the gate. Nor does it say the withdrawal needs a receipt of its own.
- **Grounds:**
  - `wrev`: `git revert --no-edit HEAD` on the outside gate edit made 7641278, unstamped. The recheck then printed 4 problems; two were for the revert itself, one of them the gate's-own-files flag (made permanent by U1).
  - `wg`: the withdrawal commit was first stopped with "no review receipt .claude/reviews/51c89f90051dd59d.md … .claude/skills/plot/SKILL.md". It went through only with a second, full receipt.
- **Connection:** situation (g) done with ordinary git adds a new unstamped commit, and there is a step the text never mentions.
- **Verdict:** bears. **Should change.**

### U7. The typo route: the refusal gives the wrong advice, depends on commit order, and is not planted
- **Target:** `check_records.py` lines 392 to 416 (it compares the skill as it is in HEAD with the last run, and says "rerun its kept cases"). Also SKILL.md line 204, `checks-and-cases.md` line 70 and `kept-cases/README.md` line 43.
- **Defect:**
  1. **Wrong advice when the skill was already owed.** The table says "No kept-case rerun"; the script says "rerun its kept cases". Neither says the honest record: a runs.md line with no fingerprint line, and the skill stays listed. All five craft skills are owed now, so the next typo in any of them hits this.
  2. **Order.** The table reads "Make it; let the gate check it … add a line". Commit first, then ask for the line, and it refuses with a false cause ("it had already changed since its cases last ran"), because it treats the last commit as "before".
  3. **Not planted.** With the refusal replaced by `if False:`, `test_checks.py` printed "TOTAL tests: 144, failed: 0" (`snap-norefuse`).
  4. **Untracked skills.** For the error-correction or add-source skill it prints "error-correction: no such skill", exit 1. The text does not say those skills need no line.
- **Grounds:**
  - In `we`, with plot owed: the refusal as quoted, exit 1.
  - Once plot was up to date, the one-commit route worked.
  - A second typo, committed first: the same refusal.
- **Connection:** M4 is answered for the case it named. The route around it has two rules at odds, a misleading message, and a promise ("refuses if…") that no planted fault holds.
- **Verdict:** bears. **Should change.**

### U8. The owner-answer steps show kept cases to the agent that changes the skills
- **Target:**
  - `owner-answers-and-revisions.md` lines 17 and 18 (grep `kept-cases`, "read each hit") and line 21 (the same agent writes the new case).
  - Against these: `kept-cases/README.md` line 5 (edited this round: "Agents that write or change the skills never see this folder"), `reviews-and-briefs.md` line 63, and `checks-and-cases.md` lines 62 and 91.
- **Defect:** two rules at odds.
- **Grounds:** running step 2's own command in `wb` printed line 28 of kept case 03 (an open-point line, with part of what an answer must do) and a grader's note at `kept-cases/runs/2026-09-24-before-entry-27.md` line 230. I saw these only by following the step, and did not use them.
- **Connection:** the next skill change is then made by an agent that has seen the answer, so the case turns into an answer key.
- **Proposed change:** search `.claude/skills` only. Take kept cases from the records check's file-and-line notes. Give the new case to an agent that has not read the skills.
- **Verdict:** bears. **Should change.**

### Minor (each bears)
- **m1. Clean merges are not stamped.** `.githooks/prepare-commit-msg` line 17: on a merge commit with no conflict, the stamp lands on the line under the subject with no blank line, so git does not read it as a stamp.
  - In `wmerge`, the message was "merge side2\nWorkshop-gate: approved e1841f…", and the recheck counted it as "the gate did not approve".
  - It is harmless for now (0 problems), but it is a false record and it adds to U2's list. The planted merge test (`test_checks.py` lines 765 to 768) checks only that the merge goes through.
- **m2. Stale counts.** The project story line 13 and `27 Corrections.md` line 152 say the planted-fault test "runs 142". It runs 144. The two tests added in 5e5564d, and that commit's changes to `check_commit.py` and `recheck_commits.py`, are in neither entry 29 nor C15.
- **m3. The "changes only checks" exception is stated too widely.** `checks-and-cases.md` line 40 and `check_commit.py` lines 15 to 20 say it lets a wrong check "be corrected even when it stops every commit". That holds only for the checks `run_all_checks.py` runs. The receipt check, the recheck, the rule against mixing and the gate itself still come from the last commit (`check_commit.py` lines 197, 213 and 226). U1 and U2 are exactly the stops it cannot lift. Should change.
- **m4. The receipt form.** The form `new --commit` writes offers only passed, passed after changes or light (`review_receipt.py` line 270). "not passed (withdrawn in …)" appears only in the modules.
- **m5. Kept cases during rechecking.** `owner-answers-and-revisions.md` line 17 says kept cases are listed "always as notes". While a question is `rechecking`, none is listed (`wb`; `check_records.py` lines 210 to 215).
- **m6. Owner terms go stale.** `owner-terms.md` line 7, "Those questions are open", is wrong from the first answer.

---

## 3. The parts the maker left undone
- **N2, in part: sound.** The session start runs the machine checks on the current files ("Machine checks: none failing" in every run I made). The next commit through the gate runs maps, owner quotes and copying on the whole staged tree.
- **N3, in part: sound.** `compare_logs` applies one rule to every old entry. This round's new rules have their own planted tests (`test_checks.py` lines 316 to 320).
- **N13, in part: sound as an owner choice.** S10 (b) sets it out with its cost. But S10 and CLAUDE.md misdescribe what happens now (U1), and that should be put right before the owner decides.
- **Retiring a planted test, and the Book-text rule:** not judged. I did not walk them.

## 4. Kept cases (titles and "Aimed at" lines only)
- **The shock clause against case 04** ("calling one early death a mistake that kills care"): it carries no answer from the case. But "buys seconds" for an unwarned early death pulls against what case 04 protects. Does not bear yet; the settling test is to rerun case 04 on the changed plot skill.
- **The "(section 3)" pointer against case 01:** does not bear.
- **The reply check's sentence on order words against case 11** ("assuming which draft came first"): it now says more of that case's target in all five skills. PW10 stays does not bear yet. The settling test is to rerun case 11 and grade whether a pass comes from method or from echoing the check's words.

## 5. Stall list
- **(a)** Followable. Two small stalls:
  - Step 4 puts the plan in the receipt's Change line, but the form's hint says "(one line…)".
  - After a re-review, it is not said whether both reports go under "Reviewer's report". I put both.
- **(b)** Walked end to end. Stalls:
  - U8, m5 and m6.
  - There is no template for where the answer goes (I wrote "**Answer (date):**").
  - "is a question put to the owner" goes stale beside "answered". I rewrote it and used a full receipt; nothing says whether a light one would do.
- **(c)** Walked: restamped, committed. It is still not said where "the stop is a sign (step 1)" is written down.
- **(d)** Followable. When the owner brings their own story and objects to a craft note, CLAUDE.md line 20 (an owner objection goes to error-correction, and "the owner caught it" is a tripwire) and the reply check both apply. Nothing says which governs.
- **(e)** U7. The route for an up-to-date skill works.
- **(f)**
  - A mixed commit was refused, and the check alone followed by its description in the next commit passed (`wf`, 68d112e and 0558df5).
  - The command for running new tests on the old check works.
  - Stalls: m3, and "tell the owner" names nothing the owner can do (U1, U2).
- **(g)**
  - U3 and U6, m4, plus whether an unreviewed outside commit is a tripwire is still unsaid.
  - The honest merges, with and without a conflict, passed (m1 aside).
  - An amend followed by an unrelated commit passed (`wam`).
  - Open corrections are listed at session start.
- **Neighbours**
  - A fresh clone's first session is quiet, with the gate on (`wfresh`).
  - A rebase over an unrelated file passed.
  - A rebase over the same file fires (U5).
  - A rebase of a reviewed hook change stops everything for good (U1).
  - Cherry-pick was not run.
- **(h)** The twist clue is sound on both routes. The shock case: U4.
- **(i)** Following CLAUDE.md lines 36 to 51, SKILL.md lines 118 and 225 to 240 and S10, an agent would tell the owner four things:
  - by itself, the gate stops honest mistakes within one commit;
  - outside commits are judged afterwards by their parent's checks;
  - a change to the gate's files is flagged for a person to look at;
  - only S10 (a) or the owner catches everything.

  My walks contradict three parts: U3 (an honest slip passes with every check green), U1 (the "flag" is a stop nobody can clear) and U2 (outside check changes pile up until nothing can be committed). Those claims need scoping, or U1 to U3 put right, before that answer goes to the owner.

## 6. What I did not check
- I ran no kept cases.
- The copying check printed NOT RUN in my copies.
- I did not run a cherry-pick, or anything on GitHub itself: I reasoned from the local rebase.
- I did not check line endings, the bypass hook's spellings, the hooks in a live Claude Code session, retiring a planted test, or the Book-text rule reading the staged register.
- I did not judge the theory content of the other edits beyond (h).
- The times are this machine's.

**Side effects.** None in the live repository: HEAD is still 35f2939, `git status` shows 30 entries as before, and no cache files were written. The live after-commit reminder hook printed its text on my commands. `test_checks.py` made and removed its own copies in the system's temporary folder.

**Verdict: passed after changes.**
- **Must change:** U1, U2, U3.
- **Should change:** U4 to U8, and m3.

These edits need a re-review of their own.
---

## 3. scripts and hooks

# Third review of the scripts and hooks (edits 1e92459 to 5e5564d), 24 September 2026

**Overall: not passed.** Two findings must change. Both are new errors that came in with the fixes:
- **A.** A problem the recheck finds can never be put right with a new commit. After ordinary commands such as `git revert` or `git rebase`, every later commit is stopped for good.
- **B.** A commit that changes only checks is judged by its own changed checks, and it may carry the log with it. So a loosened records check and the log rewrite it lets through went into one commit. That reopens the first round's S1 route B.

Eight findings should change and seven are minor. Most of the re-review's items (N1 to N21, and M2, M3, M4, S1 and S2 as they touch the scripts) are answered in content; see "Checked and found right".

**How I worked.** I made no edits and no commits in /home/user/StoryTest. At the end, `git status --short` there still shows 30 entries, as at the start.
- Every experiment ran in copies under `.../scratchpad/r3-scripts/`.
- The main copy is `base`: the live repository's 28 commits, plus the working tree as it is now (checked file by file with `cmp`: identical to the live tree). It was committed through the gate as the gate's first commit. The gate printed "note: the commit gate is new in this commit … All checks passed; committing." in 41.8 s, and the commit carries the stamp "Workshop-gate: approved e19b34f…".
- Each experiment (`e1` to `e10`, `r2`) starts from a copy of `base`. Where a commit had to arrive the way a commit made on GitHub would, I made it in the copy with the gate skipped.
- Helpers: `fill.py` fills in a receipt form, with a 45-word filler "report"; `hooktry.py` feeds commands to the Claude hook that refuses ways round the gate.
- Two terms used throughout: a **stamp** is the line "Workshop-gate: approved <tree>" that the gate adds to a commit's message. The **recheck** (`recheck_commits.py`) looks again at every commit without a matching stamp.

---

## Must change

**A. The recheck judges each unstamped commit against its own parent, every time, for ever. Nothing it finds can be put right with a new commit. Ordinary commands then stop every later commit, with no way through. Bears. Must change.**
- **Target:**
  - `recheck_commits.py` lines 176–196 (frozen, records, receipts-only-added and gate-own checks for each unstamped commit) and lines 247–266 (every commit since the gate came in, on every run; there is no longer a record of what was already rechecked).
  - What the text promises instead:
    - `checks-and-cases.md` line 46: "put it right with a new commit: … a log entry or a frozen file restored".
    - `session_start.py` line 105: "put them right with a new commit".
    - CLAUDE.md line 39.
- **Defect:** a commit's difference from its parent never changes. So a later commit that puts things right does not clear the report, and the gate stops every later commit because of it. The one way out, a late receipt with "not passed (withdrawn…)", clears only the mixed-change, gate-own-files and planted-fault parts (line 190). It never clears the frozen, log or deleted-receipt parts.
- **Grounds:**
  - (e1) A theory edited in a commit made with the gate skipped (as on GitHub), then restored exactly as line 46 says, with `git checkout HEAD~1 -- sources/bond-theory.md`. The restoring commit printed "FAILED earlier commits the gate did not approve / commit 66001dc5e, frozen files: sources/bond-theory.md: frozen file has changed … COMMIT STOPPED".
  - (e8) A reviewed hook change was committed through the gate on a branch. The main line moved on, and I ran `git rebase` (which re-creates the branch's commits on top of newer work, so their contents no longer match their stamps). The recheck printed "commit f1607cc2c: changes the gate's own files (.claude/hooks/session_start.py) without the gate; a person should look at it", exit 1, 32 s. Nothing the person can do clears it.
  - (e8) Then `git revert --no-edit HEAD` (a revert is a new commit that undoes an earlier one). Git ran no gate for it (0 s), and the revert deleted the original commit's receipt ("delete mode 100644 .claude/reviews/135c9727c8f38f7f.md"). The recheck printed "commit bfb9efc88: changes or deletes a review receipt already committed", plus a missing receipt and gate-own-files lines: "TOTAL problems: 4", 61 s. Any revert of any reviewed commit deletes that commit's receipt, because the commit added it.
  - (e3) Four reviewed check-only commits, each passed by the gate, then an ordinary `git rebase` onto a newer main line. The recheck ran the parent's planted-fault test on each one: "not checked: 1 later commit(s); the recheck ran out of time … TOTAL problems: 0", exit 1, 113 s. The next unrelated record commit printed "FAILED earlier commits the gate did not approve … TOTAL problems: 0 … COMMIT STOPPED" after 101 s, and it will do so on every commit from then on.
- **Connection:** the gate stops these commits by itself, and the fix the text prescribes does not work. The routes are the commands an honest agent or the owner would use:
  - `git revert`, to take a change back out;
  - `git rebase` or `git pull --rebase`;
  - GitHub's "rebase" merge, which line 46 recommends;
  - a web edit on GitHub.

  The only ways through are rewriting shared history, getting round the gate, or writing a false "not passed (withdrawn)" receipt. This is M2's complaint again ("the only way the text leaves open is a false record").
- **Proposed change:**
  1. A committed, only-added-to list, reviewed like any change, where a reported commit is marked as put right by a named later commit or receipt. The recheck reads that list from the last stamped commit.
  2. Stamp the approved change's `git patch-id` as well as its tree. A patch-id is git's fingerprint of a change itself, so a rebased or cherry-picked commit with the same change keeps its approval.
  3. Remember commits already rechecked and passed, so each planted-fault run happens once, not before every commit.
  4. Say in checks-and-cases.md to take a change back out with `git revert --no-commit`, then restore its receipt, then commit through the gate.
  5. Plant each case: restore after an outside edit; rebase; revert.

**B. A commit that changes only checks may carry the log, the corrections file and the source register, and all of them are judged by its own changed checks. Bears. Must change.**
- **Target:**
  - `check_commit.py` lines 69–70 (the files allowed alongside a check change), 173 and 197 (`record_scripts = staged_scripts` when only checks change).
  - The claims it breaks:
    - CLAUDE.md line 32 ("a check cannot be loosened in the same commit as the work it would stop") and rows 40 ("By itself within one commit") and 42 ("Old log entries never rewritten … By itself");
    - `checks-and-cases.md` line 29.
- **Defect:** the exception added for M2 (so that a wrong check can be corrected) runs every `run_all_checks` check from the staged files, and the log travels with the check change. A loosened records check therefore passes the log rewrite it would stop, in one commit. The last commit's planted-fault test does not catch it, because every planted log rewrite changes a title line.
- **Grounds:**
  - (e2) `check_records.py` was made to skip entry 12, and entry 12 was rewritten, with a receipt, in one commit. It printed "note: this commit changes only checks, so its own changed checks run on it … passed records … passed the last commit's planted-fault test, on the changed checks … All checks passed; committing." (For entry 7 the planted test `inline_test_11` did catch it; it rewrites entry 7.)
  - (e2b) A loosening applied the same way to every entry: compare only each entry's title. Together with a rewrite of the body of entry 20, the gate printed "passed the last commit's planted-fault test … All checks passed; committing." The commit is stamped, so the recheck will never look at it.
- **Connection:** this is the first round's S1 route B ("the check change, the entry 7 rewrite and a receipt in one commit"), closed at 1e92459 and reopened by the exception.
- **Proposed change:** run the last commit's checks on the files that travel with a check change (the log, the corrections file, the register), and use the staged checks only on the checks themselves. Or allow only the receipt alongside, and let the log entry follow in the next commit, as the check's description already does. Plant it: the title-only loosening with a body rewrite, which must be stopped.

---

## Should change

**C. "not passed (withdrawn in …)" is taken on the receipt's word. Bears. Should change.**
- **Target:**
  - `review_receipt.py` lines 213–215;
  - `recheck_commits.py` lines 175 and 190;
  - `test_checks.py` line 546 (the neighbour test for this rule withdraws nothing, so it can only agree).
- **Defect:** nothing checks that the change was withdrawn. The recheck then skips the mixed-change, gate-own-files and planted-fault checks for that commit.
- **Grounds:** (e5) An unreviewed plot rule was committed with the gate skipped. A late receipt "not passed (withdrawn in the next commit)" went through the gate ("All checks passed; committing."). The rule is still in `plot/SKILL.md` (`grep -c` printed 1), and the recheck printed "TOTAL problems: 0".
- **Connection:** a check that passes while the thing is wrong, reached by an honest slip: writing the receipt first and forgetting the withdrawal.
- **Proposed change:** for "not passed", require that the reviewed files the commit touched are, at the last commit, as they were before it. Plant both: withdrawn, and not withdrawn.

**D. "A wrong check can be corrected even when it stops every commit" holds only for the checks `run_all_checks.py` runs. Bears. Should change.**
- **Target:** `check_commit.py` lines 15–20; `checks-and-cases.md` line 40.
- **Defect:** the receipt check, the recheck, the planted-fault test and the gate itself always come from the last commit. A wrong one of these stops its own correction. M2's own example, a wrong receipt check, is still stuck.
- **Grounds:** (e7) Outside the gate, `SHORTEST_REPORT` was set to 4000 words. The correction, alone, with a proper receipt and a late "not passed (withdrawn in this commit)" receipt for the broken commit, printed "FAILED review receipt … a verdict alone is not a receipt … COMMIT STOPPED".
- **Connection:** the claim covers less than it says. Line 48 does say to stop and tell the owner. But the owner's only route is a commit outside the gate, which A then reports for ever.
- **Proposed change:** scope the claim to the checks it covers, and give the owner a stated route that A's put-right list would accept.

**E. The rules for retiring a planted test can be met by a line saying the owner did not review. Bears. Should change.**
- **Target:** `check_commit.py` line 71 (`PROTECTED_TESTS`) and lines 318–319 (`"owner" not in reviewer.lower()`).
- **Defect:**
  - The owner rule is a search for the word "owner" anywhere in the "Reviewed by" line.
  - The protected list misses log guards ("records: hidden text in the log", "records: a correction note under an old entry changed"), the hook tests and the setting tests. The gate's own message says "a test guarding … the log … or the gate is retired only with the owner named as reviewer".
  - N4's proposal that session start list the retirements is neither built nor listed as left undone.
- **Grounds:** (r2) Switching off the log comparison failed 5 planted tests. With "Reviewed by: theory-checker (the owner was not asked)" and those 5 named under "Tests retired", the gate printed "retired in the receipt: records: an old log entry rewritten … gate: … recheck: … All checks passed; committing."
- **Connection:** N4 answered in part. The maker's note that these rules were "not tried" is now answered by this run.
- **Proposed change:** require the reviewer line to begin with "the owner"; protect every log test and every hook and setting test; list retirements at session start; plant each.

**F. The hook's new reading of wrapped commands, and its new gate-records rule, refuse honest commands. Bears. Should change.**
- **Target:**
  - `git_command_reading.py` lines 42–49 (`WRAPPED_COMMAND` searches inside quoted text);
  - `refuse_check_bypass.py` lines 169–172 (any redirection counts as writing, with no check that the path is in this repository) and the note at lines 19–23.
- **Defect:** the hook's note says it lets through "text that only mentions these words (a commit message, a note being written)" and "anything done in another repository". It no longer does either reliably.
- **Grounds (hooktry, on a copy):**
  - REFUSED `git commit -m "fix: eval 'git commit -n' is refused now"`
  - REFUSED `echo "run: bash -c 'git commit -n -m x' to skip" > notes.md`
  - REFUSED `ls .git/workshop-* 2>/dev/null` and `cat .git/workshop-gate-passed 2>&1`, both read-only, with the message "would remove, empty or overwrite the commit gate's own files in .githooks/"
  - REFUSED `ls <other copy>/.git/workshop-gate-passed 2>/dev/null`, while `cd <other copy> && git commit -n -m x` was let through
  - REFUSED `bash -c 'cd /tmp && git commit -n -m x'`
  - REFUSED `git config core.hooksPath "$PWD/.githooks"`
  - Let through: `bash -lc 'git commit -n -m x'`
  - The live session's hook also refused one of my own scratch commands for the `ls … 2>/dev/null` part.
- **Connection:** a fix that brought in new errors. The false alarms stop honest work, and the refusal message sends the agent to the wrong files.
- **Proposed change:** read `bash -c` and `eval` only where they stand outside quotes; count only writing redirections into a gate record inside the project; give the gate records their own message; plant each neighbour.

**G. The size limit exempts two folders, and a file outside the receipt's scope needs no receipt. With the books absent, N10's route is open again. Bears. Should change.**
- **Target:**
  - `run_all_checks.py` lines 54 and 105–107 (`kept-cases/runs/` and `.claude/reviews/kept/` are exempt);
  - `review_receipt.py` line 236 (the Book-text line is asked for only for staged skill modules, never for late receipts);
  - the claims in CLAUDE.md row 44 and `checks-and-cases.md` line 50.
- **Grounds:** (e6) A 266,654-byte generated text in `.claude/reviews/kept/` printed "passed no book files / NOT RUN copying from books … the review receipt must say what book text a change adds / review receipt: not needed … All checks passed; committing."
- **Connection:** N10's second half ("require 'Book text:' for any sizeable added text anywhere") is neither applied nor listed as left undone.
- **Proposed change:** apply the size limit everywhere and name the kept files that may exceed it; when the copying check is NOT RUN, ask for "Book text:" for any large added text, and on late receipts too.

**H. A book phrase can be allowed by putting it in the source register and on the allowed list in one commit. Bears. Should change. (This route is older than these edits.)**
- **Target:** the note at the top of `overlap-allowed.txt` ("a phrase from a book's text can never be allowed here"); `overlap_check.py` lines 19–25; `run_all_checks.py` lines 139–143 (the allowed list is checked against the staged register).
- **Grounds:** (e9) An invented 13-word "book" sentence (made-up words, in an ignored `sources/raw/` file of the copy only) was added under the register's "Other titles" and to the allowed list, with a receipt. The gate printed "passed allowed titles … passed copying from books … All checks passed". The register itself needs no receipt.
- **Connection:** the N11 edit repeats the "never", but only the reviewer of the allowed-list change stands in the way, which is on trust.
- **Proposed change:** check the allowed list against the register as it was in the last commit, so a new register title is copy-checked with the old list first. Or say the limit.

**I. The reason for N3's part left undone is not sound. Bears. Should change.**
- **Target:** the maker's reason ("the records check applies one rule to every old entry, and the existing planted rewrite tests that rule"); `test_checks.py`, whose planted rewrites change only the title lines of entries 5 and 7.
- **Grounds:** e2b above. A check that applies one rule to every entry, comparing titles only, passes every planted log test.
- **Connection:** the planted faults are meant to catch a *changed* check. One title-line rewrite cannot tell a whole-entry comparison from a title-only one.
- **Proposed change:** plant a body-line rewrite, a rewrite of the last old entry, and a rewrite of an entry other than 5 and 7.

**J. No planted test ever runs the gate's planted-fault stage; the log's "Not tried" list understates this. Bears. Should change.**
- **Target:** `test_checks.py` line 40, which switches the setting on for every copy; log entry 29, line 138.
- **Defect:** the setting switches off the planted-fault stage in every test copy. So none of the 144 tests covers:
  - the last commit's test running on a check change;
  - the "there is no such test" failure (N5);
  - retirement (N4);
  - the recheck's run of the parent's planted-fault test.
- **Grounds:** the reasoning above, from reading `check_commit.py` lines 242–266. My runs outside the test copies show the stage does work now: e2b; r2; and `plain-named`, which printed "passed the last commit's planted-fault test" in 29 s. Nothing would notice if it stopped working.
- **Proposed change:** in one planted test, run the gate in a copy named otherwise, with the setting cleared, on a small check change. Also list these in "Not tried".

---

## Minor (each bears)

- **K. A merge made with `git merge -m` never counts as approved.** The stamp is glued to the subject line, so git does not read it as a trailer (a "Name: value" line at the end of a commit message that git can read back). Grounds (e4): the message was "merge side⏎Workshop-gate: approved c0cbe4e…" with no blank line between. The recheck printed "rechecked 1 commit(s) the gate did not approve". A file with no final newline reproduces it with `git interpret-trailers`. The cost is small, because merges return early in the recheck. But CLAUDE.md row 39 ("the gate stamps each commit it passes") is untrue for these merges, and `inline_test_13` checks only exit codes. Fix: in `prepare-commit-msg` line 18, add a newline first if the file lacks one.
- **L. A squash keeps a matching stamp.** `git rebase -i` with "squash" (e4) kept "Workshop-gate: approved 9b7893a…", which equals the new tree, so the commit was passed over. `recheck_commits.py` line 10, `checks-and-cases.md` lines 38 and 46 and SKILL.md line 228 say a squash has no matching stamp. The content is harmless (the sum of changes each approved), but the statements are wrong.
- **M. Session start gives the recheck only 40 s** (`session_start.py` line 35). One unstamped check commit costs about 30 s. Grounds (e8): "Recheck of earlier commits: could not run (it took too long)". That is honest, not "passed". The stopped recheck left its `workshop-recheck-*` folders behind in /tmp.
- **N. Each run of `test_checks.py` leaves a copy of an owner theory in /tmp.** `theory_as_a_link` (line 665) never removes its `workshop-other-*` folder, which holds an edited `bond.md`. I found about 45 such folders from this afternoon's runs.
- **O. A stale record.** Log entry 29 (status line 13 and line 138) says the planted-fault test has 142 tests. My run printed "TOTAL tests: 144, failed: 0", after 5e5564d added two setting tests.
- **P. N2's part left undone.** The reason (the next gate commit rereads the whole files) holds for maps and owner quotes. It does not hold for copying where the books are absent, and late receipts need no Book-text line (G). It does not hold for a book file added in one unstamped commit and removed in the next: it stays in git's history, and nothing looks. The recheck's note does not mention the book-file check.
- **Q. The recheck's own 90-second limit** (`TIME_LIMIT`) is checked only between commits, while one planted-fault run inside it may last up to 600 s.

---

## The maker's other parts left undone

- **N13 in part** (no "ask" before edits to the gate's own files): the reason is sound. It is the owner's choice, set out in S10 (b). An accidental edit is shown at session start ("Commit gate: switched on, BUT its files on disk differ from the last commit (.githooks/pre-commit)", seen in e4), and the unstamped commit is reported afterwards. But by A, that report can then never be cleared.
- **"Not tried"** (retirement rules; the Book-text rule reading the staged register): I tried retirement (E). The list is incomplete (J).

## The setting WORKSHOP_INSIDE_PLANTED_FAULT_TEST

**Found right, with one boundary.** It skips the planted-fault stage only in a folder whose name begins `workshop-test-` directly inside the temporary folder. The TMPDIR setting moves the temporary folder.
- With the setting on and TMPDIR pointed at my scratch folder, a copy named `workshop-test-named` printed "not run   the planted-fault tests (this commit is made inside the planted-fault test itself…)" and committed. It said "not run", never "passed".
- A copy named `plain-named`, with the same setting and TMPDIR, ran the stage and printed "passed the last commit's planted-fault test".
- The live repository's folder, StoryTest, can never match.
- Inside the test's own copies the setting works as intended. Its side effect is J.

## Checked and found right

- **Planted-fault test:** `test_checks.py` in copy `t1` printed "TOTAL tests: 144, failed: 0", in 24 s.
- **N1:** the gate file on disk asking for the staged checks is ignored (planted test); session start names gate files that differ on disk (e4).
- **N2 and M3 in the main:**
  - unstamped commits are judged by their parent's checks (e1 found the theory edit; planted test `inline_test_11`);
  - check-changing commits get the parent's planted-fault test (e3, e8);
  - the recheck no longer repeats the staged problems (use-tester S2, seen in e1's output).
- **N5:** `--no-renames` is used. From reading only: a missing test is FAILED.
- **N6 and N7:**
  - a merge needs a receipt only for its own changes;
  - an honest merge went through (e4, and `inline_test_13`);
  - the planted merge test now requires "commit …: no review receipt".
- **N8 to N12, N14 to N17, N20, N21:** answered as proposed, each with a passing planted test where one was asked for.
- **N12 (recursion):** stopping the whole group of processes works. The new planted-fault test run on the old 1e92459 scripts recursed: about 44 nested processes after roughly 10 minutes, which I stopped. The new scripts finish in 24 s.
- **N18:** the "(from Bond, …)" form is caught; I did not test block quotes.
- **Stamps:** correct for `git commit`, `git commit -a` and `git commit -- <path>` (e4); a skipped-gate commit gets none (e1, e5).
- **Cost of stamped commits:** the recheck over 500 stamped commits took 2.4 s (e10).
- **M4:** covered by `inline_test_3`, which passed; I did not try it further.
- **Use-tester S1:** session start lists "Open corrections (27 Corrections.md): C1 … C15" (e4).

## Not checked

- The maker's claim that 28 tests fail on the re-reviewed scripts: my run of the new test on them recursed without end, so I have no count.
- Real GitHub merges (squash, rebase, merge button), `git pull`, worktrees, Windows and macOS.
- The hooks in a live Claude Code session; I fed them input as a session would.
- Block-quoted owner quotes (N18); the filter route of N14 (reading only); N19 (reading only).
- The prose skills, beyond the lines quoted above.

## Side effects

- Nothing was written to the live repository.
- My runs made `/tmp/workshop-*` folders. I deleted those dated after 15:48, which I believe were all from my own runs: my stopped recursion run, the stopped rechecks, and the theory copies of N. Any folder a parallel reviewer made in that window would have gone too. Five older folders (15:32 to 15:44) were left alone.

## Verdict: not passed

Must change:
1. **A:** let a reported commit be put right (a committed list of commits put right; stamps that survive a rebase; rechecked commits remembered; the revert route in the text; planted cases).
2. **B:** judge the files that travel with a check change by the last commit's checks, or refuse them alongside a check change; plant the title-only loosening.

C to J should change. The edits made for A and B need a review of their own.