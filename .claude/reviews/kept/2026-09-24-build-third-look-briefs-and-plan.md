# The third look at the error-correction build: briefs, their check, the known fault, and the plan, 24 September 2026

What this is, in order: the three reviewers' instructions (briefs), as revised after they were checked; the check of those briefs by theory-checker, word for word (correction C5); the record of the known fault left in for the reviewers (reviews-and-briefs.md, section 6), with its timestamps; and the lead's plan for answering the reports, written before any change, in three parts as the reports arrived (16:07, 16:23 and 16:33 UTC). The reports themselves are in `2026-09-24-build-third-look.md`. Kept for log entry 30.

---

## 1. The briefs, as sent

# Briefs for the third look at the error-correction build (the edits answering the re-review)

(Revised after the brief check by theory-checker: its findings 1 to 11 applied as it proposed. The revised brief was not checked again.)

## Shared part (goes at the top of each brief)

You are reviewing edits you did not make. The maker is the lead agent. Your job is to find what is wrong, with reasons; the maker will apply or reject each finding, and your report will be pasted word for word into the build's review receipt.

Where things are:
- The live repository is `/home/user/StoryTest`. Do not edit it, commit in it, or run anything there that writes files. Read it freely.
- A scratch snapshot repository is at `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/rereview`, with four commits: `b2617b3` (what the first reviewers saw), `1e92459` (after the first round's answers; what the re-reviewers saw), `7812119` (the answers to the re-review), `5e5564d` (now: a few more edits made after the brief check). The working tree of the live repository matches `5e5564d`, apart from files git ignores.
- **The edits to review:** `git -C <snapshot> diff 1e92459 5e5564d`. The new file `.claude/reviews/kept/2026-09-24-build-rereview.md` in that diff is a word-for-word copy of the re-review's reports. It holds the findings these edits answer: section 1 (theory-checker, F1 to F22), section 2 (use-tester, M1 to M4, use-tester S1 to S4, minors), section 3 (scripts, N1 to N21). (Section 3 also mentions the first round's S1 to S17, which are different items.)
- Any experiment runs in a copy you make yourself under `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/r3-<your name>/`, never in the live repository.

What to look for, in your area:
1. For each finding listed for you: is it answered in content by the edits? Where the edits leave a finding not applied, or applied only in part, is the reason sound? The parts the maker left undone, with the maker's reasons, are listed next; judge them, and look for any others.
2. Do the edits themselves bring in new errors?

Parts left undone, and the maker's reasons (to be judged, not taken as right):
- N2, in part: the recheck does not rerun the maps, owner-quotes and copying checks on each commit the gate did not approve. Reason: the next commit through the gate runs them on the whole of the files as they then are. (Written in the note at the top of `recheck_commits.py`.)
- N3, in part: no new planted rewrites of other log entries. Reason: the records check applies one rule to every old entry, and the existing planted rewrite tests that rule.
- N13, in part: Claude Code does not ask the owner before an edit to the gate's own files. Reason: in C15 and in owner question S10 (b).
- Not tried: the rules for retiring a planted test, and the Book-text rule reading the staged register, because they run only outside the planted-fault test (said in C15).

Lessons from earlier errors that apply to all three of you (rows of the kinds-of-error table in `27 Corrections.md`):
- "A change (a fix) that makes a new error; a rule changed in one place but not its copies": most new errors in this workshop's history came from fixes. Search for every other statement of a changed rule.
- "A record that is stale, unfinished, or leaves out who made an error."
- "A required check skipped, or a claim reported without its receipt, with an assumed input, or with agreement between checks that were not independent."

Report: one finding at a time, in four parts: the **target** (file and line), the **defect**, the **grounds** (a theory line, a term-sheet row, or a command and what it printed), the **connection** (how the grounds show the defect in the target). Then a verdict on each: **bears**, **does not bear yet** (name the test that would settle it), or **does not bear**, and a severity: must change, should change, or minor. Say what you checked and found right, and what you did not check. End with one of: passed; passed after changes (list what must change); not passed.

## Brief A: theory-checker

Your area is what the edits say: the `error-correction` skill and its modules, the craft skills (plot, character, genre, dialogue, story-world), add-source, the reviewer agents `.claude/agents/theory-checker.md` and `.claude/agents/use-tester.md`, `kept-cases/README.md`, `CLAUDE.md`, `README.md`, `26 Test - The Catch - two versions.md`, `27 Corrections.md` (every correction from C1 to C15 changed, and the kinds table), `22 Questions - meanings only you can settle.md` (S10; S12 is unchanged in this diff, though F1 named it) and `StoryTest - project story.md` (the status lines, the "How the pieces fit" table, the word list, log entries 27 and 29, neither yet committed, and the next step).

The findings listed for you: section 1, F1 to F22; and from section 2, use-tester S3 and S4 and the minor items answered in words rather than scripts.

Also check:
- The statements of what the commit gate cannot do (in `CLAUDE.md`, the skill, `references/checks-and-cases.md` section 2, C15, the kinds table and S10). Compare each with what the scripts' own notes say they do (the notes at the top of `check_commit.py` and `recheck_commits.py`). Each must claim neither more nor less than the scripts do, for honest routes as well as deliberate ones.
- Every order word in file 26 against what is known: the owner does not know which draft came first. No list of words catches them all; read every sentence that compares the two versions.

Term-sheet rows that apply (`.claude/skills/error-correction/references/owner-terms.md`): sections 1 (promise, guarantee, expectation), 6.1 (mystery and wonder), 10 (tension and suspense), 11.4 (surprise, three times), 12 (who said it) and 13 (where the theories leave a term unclear). Kinds-of-error rows that apply, beyond the shared ones: "An owner term used in a neighbouring sense, or a theory narrowed or turned round (the commonest kind)"; "A claim credited to the wrong theory, book or person"; "A contradiction between skills that no single-skill review can see" (the reply check is copied into five craft skills; the tripwire rule is stated in two places); "A pointer that lands nowhere or on the wrong thing".

## Brief B: use-tester

Your area is whether the process can be followed, step by step, now that these edits are in. Walk these situations through the skill, its modules and `kept-cases/README.md` as an agent would, and run what the text tells you to run, in your own copy:
- (a) A reviewer finds a claim credited to the wrong theory in a staged change, before commit.
- (b) The owner answers a question that a kept case and a kept run record both cite.
- (c) The gate stops a commit because the status lines were not restamped for a new log entry.
- (d) A writer objects to a note a craft skill gave.
- (e) A one-word typo is corrected in one craft skill, while the other four skills are owed a kept-case rerun.
- (f) A check is found wrong and corrected: first an ordinary correction; then the case where a check in the last commit stops every commit, so the correction goes in a commit that changes only checks.
- (g) A commit made where the gate was off arrives; its late review does not pass, and the change is taken back out.
- (g) An honest merge of two reviewed commits; an amended reviewed commit followed by an unrelated commit; a session start with corrections open.
- Near neighbours where nothing should fire: an honest rebase or cherry-pick of reviewed commits (the stamp may no longer match), and a fresh clone's first session.
- (h) A writer's question about a clue for a twist, and separately about a turn meant as a shock, taken through the plot skill's building route and its diagnosing route to the rule in `.claude/skills/plot/references/reveals-and-withholding.md`, section 2 ("Mystery or wonder").
- (i) The owner asks whether the gate can be trusted. Follow what the skill, `CLAUDE.md` and S10 would have an agent say.

The findings listed for you: section 2 of the kept re-review report, M1 to M4, use-tester S1 to S4 and the minor items.

Term-sheet rows that apply (`.claude/skills/error-correction/references/owner-terms.md`): 6.1 (mystery and wonder), 10 (tension and suspense), 11.4 (surprise, three times) and 13. Kinds-of-error rows that apply, beyond the shared ones: "A check or a step that stops honest work, or leaves no way through" (an answered question that could never be closed, a late review that did not pass and could not be written down, an honest merge stopped, an amended commit stopping the next one, a typo's record clearing every skill's kept-case notice); "A test that can only agree: cases or examples drawn from the answer, or a fix confirmed on the case that made it" (these situations are the ones that found the faults; a situation that only replays a found fault shows less than a new one).

## Brief C: scripts and hooks

Your area is the scripts and hooks: everything under `.claude/skills/error-correction/scripts/`, `.claude/skills/add-source/scripts/`, `.claude/hooks/`, `.githooks/` (including the new `prepare-commit-msg`), `.claude/settings.json`, `.gitattributes`, and `kept-cases/run-kept-cases.js`.

The findings listed for you: section 3 of the kept re-review report, N1 to N21; and from section 2, M2, M3, M4, use-tester S1 and use-tester S2 as they bear on the scripts.

What the gate now claims, and what it says it cannot do, is in `CLAUDE.md` (the table and the paragraph "What none of this can stop") and in the notes at the top of `check_commit.py` and `recheck_commits.py`. Judge whether each stated limit is true and complete, for honest routes (a commit made on GitHub, an ordinary command) as well as deliberate ones. Look hardest for these:
- ways round that an honest or careless agent could take by accident, or with an ordinary command or setting;
- honest work the gate or the recheck stops (a false alarm);
- a check that says "passed" when it did not run.

One setting to test in particular: `WORKSHOP_INSIDE_PLANTED_FAULT_TEST`. `test_checks.py` sets it so that commits in its own copies do not start the planted-fault test again; the gate and the recheck then skip that test. Whether the setting can skip anything outside those copies is yours to find out.

Run `test_checks.py` in a copy. Say which tests you ran on which scripts.

Kinds-of-error rows that apply, beyond the shared ones: "A check that passes while the thing is wrong, or can be got round"; "A check or a step that stops honest work, or leaves no way through"; "A test that can only agree: cases or examples drawn from the answer, or a fix confirmed on the case that made it" (the new planted tests were written for the findings they answer); "An edit to a frozen text"; "A commit that skips the gate, or arrives where it cannot see (a fast-forward, a cherry-pick, a commit made on GitHub)".

---

## 2. The check of the briefs (theory-checker)

**Brief check: `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/briefs-round3.md`**

**Result: passed after changes.** Findings 1 and 2 must change before the briefs go out. Findings 3 to 9 should change, and 10 to 12 are minor.

**Findings (target; defect; grounds; connection; verdict)**

1. **Line 57 (Brief C).** *Defect:* the brief tells the reviewer that a way round already named in the stated limits is a finding only if the limit is misstated. *Grounds:* the maker's reason for not fully applying N13 is exactly "the limit is stated in CLAUDE.md" (`findings-answered-round2.md`). The recheck's own note names a limit that honest people can hit too: an outside commit, for example one made on GitHub, that changes the recheck "is judged by the changed version". The brief calls all of these "an agent set on getting round the gate". *Connection:* this settles item 1 for N13 and M3 before the review starts, and steers the reviewer away from honest routes. **Bears; must change.**

2. **The areas at lines 26 and 53.** *Defect:* four files in the diff fall in no brief's area: `.claude/agents/theory-checker.md`, `.claude/agents/use-tester.md`, `kept-cases/README.md` (it now holds the rule answering M4) and `kept-cases/run-kept-cases.js` (a script, and N21 names it). *Grounds:* `git diff --name-status 1e92459 7812119`. *Connection:* nobody reviews those edits. **Bears; must change.**

3. **Line 62.** *Defect:* the brief gives `WORKSHOP_INSIDE_PLANTED_FAULT_TEST` only as a tip for running the tests. *Grounds:* when that setting is on, `check_commit.py` (lines 224 and 234–236) prints "not run" for the planted-fault test on a check change and does not stop the commit; `recheck_commits.py` (lines 184–187) does the same. No hook mentions the setting (I searched `.claude/hooks` and `.githooks`). It is a close neighbour of N9. *Connection:* the reviewer is steered away from a possible way round that ordinary commands give. I did not run such a commit. **Bears; should change:** list it as something to test.

4. **Line 14, item 1 ("is the reason they give sound?").** *Defect:* the brief does not say where those reasons are written. *Grounds:* the part of N2 left undone (the maps, owner-quotes and copying checks are not run on unseen commits) appears in no edited file I searched. It appears only in the scratch file `findings-answered-round2.md`. *Connection:* the question cannot be answered as the brief stands. **Bears; should change:** give the not-applied parts with their reasons, and leave out the "applied" claims.

5. **Line 26 (Brief A's list of corrections).** *Defect:* the list gives C1, C4, C6, C9 and C12 to C15. But every correction from C1 to C15 changed (F8's plan parts). The project story's "How the pieces fit" row (line 44) and "Next step" (line 143) also changed and are not listed. S12 is listed, but it is unchanged in this diff. *Grounds:* the `git diff -U0` line ranges. *Connection:* the checker is steered away from C2, C3, C5, C7, C8, C10 and C11. **Bears; should change.** Add "S12 is unchanged here; F1 named it".

6. **Lines 17–20, 35, 49 and 64 (kinds-table rows).** *Defect:* three rows that apply are missing:
   - "A test that can only agree … a fix confirmed on the case that made it", for B and C. B's situations are the ones that found the faults, and the 28 new tests were written for those findings.
   - "A contradiction between skills…", for A: the reply check is copied into five craft skills, and the tripwire rule is stated twice.
   - "A pointer that lands nowhere…", for A.

   *Grounds:* the table in `27 Corrections.md`, and section 5 of `reviews-and-briefs.md`. **Bears; should change.**

7. **Brief B (term-sheet rows).** *Defect:* Brief B lists no term-sheet rows, although situation (h) turns on surprise, suspense and shock. Term-sheet section 6.1 (mystery and wonder, the promise of open questions) applies to A and B, because the rule sits in "Mystery or wonder". *Grounds:* section 5 of `reviews-and-briefs.md`. **Bears; should change.**

8. **Lines 39–45 (Brief B's situations).** *Defect:* situations (a), (c), (d) and (f) are left out, although S3 (a), S2 (c) and the minor items in (a), (d) and (f) are listed for B. The check-only commit is new: it is judged by its own changed checks (`check_commit.py`, top note). There is no everyday neighbour where nothing should fire, such as an honest rebase or cherry-pick of reviewed commits (the stamp no longer matches), or a fresh clone. *Grounds:* re-review section 2, lines 120–129, and the use-tester's own instruction to include a near neighbour. **Bears; should change.**

9. **Line 33, the "Also check" bullet on the plot rule.** *Defect:* it pairs the one sentence about shock with term-sheet sections 11.4 and 13. That is where the known fault recorded in `reviewer-test-round3.md` lies (section 13, item 9). *Grounds:* F4, F5 and F22 already send the checker to that paragraph. *Connection:* a catch now shows less about the reviewer (reviews-and-briefs section 6). **Bears; should change:** cut the bullet back, or record in the reviewer-test note that the brief pointed there. The bullet also names no theory lines or cases. The ones to name are Gap line 59 (the bomb, both schedules) and Anticipation line 25 (the Shock row).

10. **Line 33 (pointer).** *Defect:* section 2 is titled "Mystery or wonder", not "surprise, suspense and shock"; the rule is at line 30. The path is plot's, but it is written as `references/…`, next to error-correction's `references/owner-terms.md`. **Bears; minor.**

11. **Lines 28, 47 and 55 (labels).** *Defect:* "S1 to S4" also names the first-round findings in section 3 of the kept report (S1 to S17) and the owner questions (S10, S12). **Bears; minor:** write "use-tester S1" and so on.

12. **Line 10.** The claim "word-for-word copy" is true: after collapsing spacing, each of the three `rereview-*.md` reports appears in full inside the kept file. **Does not bear.**

**Checked and found right**
- Every tracked file in the live tree matches `7812119` (cmp run on each).
- The three snapshot commits exist.
- The kept file's sections and labels (F1–F22, M1–M4, S1–S4, N1–N21) match what the brief says.
- Every quoted kinds row is word for word.
- The term-sheet section numbers and titles match.
- `checks-and-cases.md` section 2 has "What the gate cannot do"; the CLAUDE.md paragraph and both scripts' top notes exist; `test_checks.py` line 40 sets the setting.
- Entries 27 and 29 are uncommitted (entry 28 is too).
- Apart from findings 1 and 3, no verdicts of the author's are carried. The brief's line to theory-checker that no word list catches every order phrase is consistent with C1; nothing in it contradicts C5.

**Not checked**
- Whether the edits answer any finding.
- The theory claims in the edits.
- No commit or test run; hook code beyond searches.
- The kept first-round reports.

**Other notes**
- Seen in passing, not part of the brief: in `CLAUDE.md` the "What none of this can stop" paragraph sits inside the rule table, leaving three rows below it.
- Keep this report in `.claude/reviews/kept/`: that is C5's condition for closing. Do not give it to the round-3 reviewers, because finding 9 names the known fault.

**Verdict: passed after changes.**
- Must change: 1 and 2.
- Should change: 3 to 9.
- Minor: 10 and 11.
---

## 3. The known fault left in for the reviewers

# Known fault left in for the round-3 reviewers (reviews-and-briefs.md section 6)

Noticed by the lead before the round-3 briefs went out. Not planted on purpose: it is a real fault in the round-2 edits, left in unchanged so the review can show whether it is caught. It is put right after the review whatever the result.

Target: .claude/skills/plot/references/reveals-and-withholding.md, section 2, the sentence "A turn meant only as a shock, one that arrives with no warning (the Anticipation theory's Shock; the Gap theory's bomb that simply goes off), needs no set-up and buys seconds; this check is not for it."

Defect: both theories call the bomb that simply goes off a *surprise* ("fifteen seconds of surprise", Gap Part 2 section 3; "you get seconds of surprise", Anticipation Part 2 section 1). Filing it under "shock" settles, without a label, the overlap the term sheet lists as open (owner-terms.md section 13, item 9; S13). It should be labelled as the workshop's reading, with S13.

Caught by: theory-checker, third round, finding R7 (should change): it named the sentence, both theories' lines, term-sheet section 13 item 9 and S13, and also found the copies in writing-rules-and-rivals.md line 9 and C12, and two places (section 1, plot SKILL.md step 4) not brought into line. Weaker evidence than a catch with no pointer: the brief listed term-sheet 11.4 and 13 (see below). use-tester: caught it too, finding U4 (should change), by walking the theories' own cases; it also found the clause wrong on Psycho and on a character reveal meant as a pure shock. The scripts reviewer: its area did not include the plot skill.

Added 15:46 UTC, before the briefs went out: the brief check (its finding 9) noted that the first draft of Brief A pointed straight at this sentence with term-sheet 11.4 and 13. That bullet was cut. The revised briefs still list term-sheet sections 11.4 and 13 among the rows that apply (the brief rule requires it), and Brief B's situation (h) names section 2 of the module. So a catch shows less about the reviewer than it would have with no pointer.

---

## 4. The lead's plan, written before any change

# Plan for answering the third look, written before any change (theory-checker's report in; use-tester and scripts reports still running)

To put right (theory-checker R1 to R24):
- R1: a commit that changes only checks may carry nothing else but new review receipts; the log, the corrections file and the register then come in the next commit (judged by the changed checks from the last commit). A check change that carries the log is an ordinary check commit, judged by the last commit's checks. Planted: a check-only loosening with a rewritten entry 9 is stopped. Texts: check_commit.py note, checks-and-cases.md sections 2 and 3, reviews-and-briefs.md section 2, SKILL.md.
- R2: plant rewrites of a body line of a middle entry and of the last committed entry.
- R3 and R4: every statement of the gate's limits says it also misses honest outside commits that change the recheck or gate, and that the recheck judges every unstamped commit and reports those with problems.
- R5: the recheck also looks for book files (sources/raw/ paths, large text files) in each unstamped commit; the note and CLAUDE.md say copying is not rerun per commit.
- R6: state the retiring rule in the skill texts; the owner named for protected tests means the owner agrees, in plain words, to lose a named guard; tighten "owner" matching; say so in S10.
- R7: label the shock reading (S13, term sheet 13 item 9); gloss surprise in Gap's words; bring section 1, plot SKILL.md step 4, writing-rules line 9 and C12 into line.
- R8: reviews-and-briefs section 4: a staged finding is the stage working when the stage that caught it is the one named for its kind.
- R9, R10, R12, R23: file 26: list what the break test found and was not applied, with reasons; the ledge fix keeps Iona drawing the conclusion; reword "still" twice; the heading and the "Eli." line.
- R11: theory-checker.md order words open-ended.
- R13: test counts rerun at the end, and the count failing on the re-reviewers' scripts rerun.
- R14, R15, R16, R17, R20, R22, R24: records: C12 description in entry 29; plan parts in C4, C6, C12, C13; S12; kinds row "A required check skipped"; S10 (b) both sides; open-corrections line; trial half-run.
- R18, R19: after-commit reminder and receipt form hint.
- R21: try the retiring rules by hand in a scratch copy.
To keep working: all 144 planted tests; every check passing on the live files; the reply check identical in five skills.
Findings from use-tester and the scripts reviewer: added to this plan when they arrive, before those changes are made.

## Added when use-tester's report arrived (before any change)

The three must-change findings (U1, U2, U3) and one I found while reading them (a frozen-file edit or a log rewrite that arrives in a commit made outside the gate can never be cleared: the recheck judges that commit alone, forever, so restoring the file in a later commit does not help) share one cause: the recheck judges each unapproved commit on its own and never lets it settle. Patching each would add parts to the piece every round has found faults in. The plan is to make it simpler instead:

- The gate's starting point becomes the last approved commit (the nearest commit in the history carrying the gate's stamp for its own contents), not simply the last commit. The gate takes its checks from it and compares with it: the log only added to, the frozen list only added to, receipts only added to, and the planted-fault test run whenever the checks differ from its checks. Normally the last approved commit is the last commit, and nothing changes. After commits made outside the gate, anything they got wrong is judged in the files as they are now, so a later commit that puts it right clears it (and a commit that still has it wrong is stopped).
- The recheck shrinks to what only history can show, for the commits since the last approved one: each needs a review receipt (late, or the original found by a fingerprint that survives a rebase, U5), or a withdrawal the recheck verifies (each file the commit changed is back as it was, U3); book files added anywhere in those commits are reported (R5; they cannot be put right by a new commit, only by rewriting history, so they are reported, not a stop); a change to the gate's own files is reported for a person, never a stop that nothing clears (U1).
- Once a commit through the gate is stamped, everything before it is settled (U2); the record is the stamp, which is in the history, so a fresh clone agrees.
- The mixing rule applies to the commit's own change. A commit that changes only checks may carry nothing else but new receipts (R1).
- Merge stamps placed where git reads them (m1).
Planted tests: a rebased reviewed hook change goes through with its original receipt; several reviewed outside check changes, then an unrelated commit goes through quickly; "withdrawn" with nothing withdrawn is stopped, and a real withdrawal passes; a frozen edit arriving outside, then restored, passes, and not restored, is stopped; a rebase over a same-file upstream change finds its receipt; the check-only commit with a log rider is judged by the last approved commit's checks; R2's rewrites.

Also: U4 with R7 (the shock clause: scope by what the turn does, label S13, drop "buys seconds" or add the guarantee exception, jump scares want dread first, copies brought into line); U6 (say how to take a change back out: `git revert --no-commit`, then commit through the gate with its receipt); U7 (the typo route's message and order, planted; skills with no kept cases need no line); U8 (the owner-answer search looks in `.claude/skills` only; kept cases come from the records check's notes; a new case is written by an agent that has not read the skills); m3 (state the check-only exception's reach); m4 (the form lists "not passed (withdrawn in ...)" for late receipts); m5 (kept cases listed during rechecking); m6 (owner-terms "those questions are open" line); stall (c): say where the sign of a gate stop is written (nowhere unless it is a tripwire: the fix is the record); stall (d): which governs when the owner objects to a note on their own story.
To keep working: everything listed above, and every earlier planted test that still describes the right behaviour; tests whose expected output names the old recheck are rewritten to the new route, and each rewrite is named in the receipt.

## Added when the scripts reviewer's report arrived (before any change)

Its must-change A and B are the same faults as U1-U3 and R1, found separately; the simpler design above answers them. Details settled now:
- The last approved commit (A) is the nearest commit on the main line of the history whose stamp matches its contents. The gate's own script still comes from the last commit (the stated limit, and the owner's route for correcting the gate itself); every check, the receipt check, the recheck and the planted-fault test come from A. The files are compared with A.
- A commit that changes only checks (with nothing else but new receipts), when the last commit is approved, is judged by its own changed checks and receipt check, and A's planted-fault test must pass on them (D, in part). A wrong gate script: the owner's route, stated.
- Settled: commits reachable from an approved commit. The recheck covers only the rest, since the gate came in: receipts (fingerprint made from the added and removed lines only, so a rebase keeps it: U5), withdrawal verified line by line (C, U3), book files noted (P), gate's own files noted (U1).
- E: the owner rule needs the reviewer line to begin with "the owner"; every records, hook and setting test protected; retirements listed at session start.
- F: bash -c and eval read only outside quotes, and with flag clusters such as -lc; redirections count only when their target is a gate record or gate file in this project; a quoted hooksPath ending in .githooks is let through; the wrapped command's own cd is followed.
- G: no size exemption for kept folders; the Book-text line asked for on late receipts too; the claim scoped for small text outside the skills.
- H: the allowed list is checked against the register as it was in A.
- I: planted rewrites of a body line, of the last old entry, and of entry 12.
- J: one planted test runs the gate's planted-fault stage for real, in a copy not named as a test copy (skipped when already inside the test, so it cannot call itself without end).
- K: a newline before the stamp; L: the squash statements corrected; M, Q: the recheck is now cheap, and its folders are removed if it is stopped; N: the planted test removes its outside folder; O: counts.
