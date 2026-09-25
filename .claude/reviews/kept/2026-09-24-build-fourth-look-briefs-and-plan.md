# The fourth look at the error-correction build: briefs, their check, and the plan, 24 September 2026

What this is, in order: the three reviewers' briefs, as revised after they were checked; the check of those briefs by theory-checker, word for word; and the lead's plan for answering the reports, written before any change, in three parts as the reports arrived (17:42, 17:57 and 18:01 UTC). No known fault was left in for the reviewers this time. The reports are in `2026-09-24-build-fourth-look.md`. Kept for log entry 31.

---

## 1. The briefs, as sent

# Briefs for the fourth look at the error-correction build (the edits answering the third look)

(Revised after the brief check by theory-checker: its findings 1 to 8 applied as it proposed. The revised brief was not checked again.)

## Shared part (goes at the top of each brief)

You are reviewing edits you did not make. The maker is the lead agent. Your job is to find what is wrong, with reasons; the maker will apply or reject each finding, and your report will be kept word for word in the repository and pointed to from the build's review receipt. Do not read other files in the scratchpad folder than the ones named here: they hold the maker's own notes and views.

Where things are:
- The live repository is `/home/user/StoryTest`. Do not edit it, commit in it, or run anything there that writes files. Read it freely.
- A scratch snapshot repository is at `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/rereview`. Its commit `5e5564d` is what the third look saw; `018ebd6` is now. The working tree of the live repository matches `018ebd6`, apart from files git ignores (the book texts in `sources/raw/` are among those; never copy book text into anything you write).
- **The edits to review:** `git -C <snapshot> diff 5e5564d 018ebd6`. The two new files `.claude/reviews/kept/2026-09-24-build-third-look.md` (the third look's three reports: theory-checker R1 to R24, use-tester U1 to U8 and m1 to m6, scripts A to Q) and `.claude/reviews/kept/2026-09-24-build-third-look-briefs-and-plan.md` (the third look's briefs, the check of those briefs with its findings numbered 1 to 12, a known fault left in for those reviewers, and the maker's plan) are records kept word for word; they hold the findings these edits were made to answer. The plan's statements that a change answers a finding are the maker's claims, to be judged like any other.
- Any experiment runs in a copy you make yourself under `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/r4-<your name>/`, never in the live repository. To commit in a copy with the gate switched on, run `git config core.hooksPath .githooks` inside the copy. The live session has a hook that refuses commands which look like skipping the gate when they seem to target the live repository; use literal paths to your copies.

The main change, in the maker's words, so you know what to look at (a description, not a claim that it works or that its premises hold): the commit gate now takes its checks from, and compares the files with, the last commit it approved (the nearest commit on the main line whose stamp matches its own contents), instead of the last commit; the recheck of commits the gate did not approve now looks only at what the maker takes to be the things the history alone can show (receipts, a claimed withdrawal, book files, changes to the gate's own files); a commit that changes only checks, made straight on top of an approved commit, may carry nothing but new receipts, and is then judged by its own changed checks.

What to look for, in your area:
1. For each finding listed for you: is it answered in content by the edits? Where the edits leave a finding not applied, or applied only in part, is the reason sound? The parts the maker left undone, with the maker's reasons, are listed next; judge them, and look for any others.
2. Do the edits themselves bring in new errors? Most new errors in this workshop's history came from fixes, and each of the last three rounds found new faults in the answers to the round before.

Parts left undone, and the maker's reasons (to be judged, not taken as right):
- The copying check is not rerun on each commit the gate did not approve. Reason: it needs the books, and the gate reads the files as they are at each commit; stated as a limit in `CLAUDE.md` and the recheck's note.
- Scripts D, in part: the exception for a commit that changes only checks does not reach the gate script itself (`check_commit.py`). Reason: that script always comes from the last commit; a wrong one is the owner's to correct, by a route stated in `references/checks-and-cases.md` section 2.
- Claude Code asking the owner before edits to the gate's own files (owner question S10, option b): left to the owner.
- Use-tester's kept-case notes (case 04 against the shock clause; case 11): left to the run of the kept cases on the committed build.
- Scripts G, in part: one kept record (`kept-cases/runs/2026-09-24-before-entry-27.md`) is still exempt from the size limit, by name (`LARGE_RECORDS_ALLOWED` in `run_all_checks.py`). Reason: it was written before the limit covered kept records; later runs are to be kept one file per case.
- Not tried by a planted test: the Book-text rule reading the staged register. The rules for retiring a planted test were tried by hand, not by a planted test.
- Not checked by anyone but the maker: the counts in C15, entry 30 and the status line (166 tests, all passing; 19 failing on the scripts the third look saw).

Lessons from earlier errors that apply to all three of you (rows of the kinds-of-error table in `27 Corrections.md`):
- "A change (a fix) that makes a new error; a rule changed in one place but not its copies": search for every other statement of a changed rule.
- "A record that is stale, unfinished, or leaves out who made an error."
- "A required check skipped, or a claim reported without its receipt, with an assumed input, or with agreement between checks that were not independent."
- "A test that can only agree: cases or examples drawn from the answer, or a fix confirmed on the case that made it": the new planted tests were written for the findings they answer, and a situation that only replays a found fault shows less than a new one. Try ordinary commands and situations they do not plant.

Report: one finding at a time, in four parts: the **target** (file and line), the **defect**, the **grounds** (a theory line, a term-sheet row, or a command and what it printed), the **connection** (how the grounds show the defect in the target). Then a verdict on each: **bears**, **does not bear yet** (name the test that would settle it), or **does not bear**, and a severity: must change, should change, or minor. Say what you checked and found right, and what you did not check. End with one of: passed; passed after changes (list what must change); not passed.

## Brief A: theory-checker

Your area is what the edits say: the `error-correction` skill and its modules, the plot skill and its module `references/reveals-and-withholding.md`, add-source, the reviewer agent `.claude/agents/theory-checker.md`, `kept-cases/README.md`, `CLAUDE.md`, `README.md`, `26 Test - The Catch - two versions.md`, `27 Corrections.md` (C1, C4, C5, C6, C12, C13, C15 and the kinds table), `22 Questions - meanings only you can settle.md` (S10, S12) and `StoryTest - project story.md` (the status lines, the parts table, the word list, entries 29 and 30, neither yet committed, and the next step).

The findings listed for you: the third look's theory-checker R1 to R24 (as they bear on what the text says), use-tester U4, U6, U7, U8, m2 to m6 and the stall list, and the brief check's findings 1 to 12.

Also check:
- The plot rule in `.claude/skills/plot/references/reveals-and-withholding.md`, section 2, against the Gap and Anticipation theories and the term sheet, walking the theories' own named cases through it; and every other statement of the planting rule, changed or not, wherever it is: search. Among them: section 1 and section 6 of that module; the plot skill's `SKILL.md` step 4, its diagnosing-table row for a twist that came from nowhere, and its quick version; `.claude/skills/plot/references/suspense-and-fear.md` section 5, which the new sentence cites; the error-correction skill's `references/writing-rules-and-rivals.md`, section 1; and C12.
- Every statement of what the commit gate does and cannot do, wherever it is stated: search. Among them: `CLAUDE.md`, the skill, `references/checks-and-cases.md` section 2, `references/reviews-and-briefs.md`, README, C15, the kinds table, S10, the project story, and the notes at the top of `.claude/hooks/refuse_check_bypass.py`, `.claude/hooks/git_command_reading.py`, `.claude/hooks/session_start.py` and `.githooks/prepare-commit-msg`. Compare each with the notes at the top of `check_commit.py` and `recheck_commits.py`. Each must claim neither more nor less than the scripts do, for honest routes as well as deliberate ones.
- Every sentence in file 26 that compares the two versions: the owner does not know which came first.

Term-sheet rows that apply (`.claude/skills/error-correction/references/owner-terms.md`): sections 1, 6.1, 7 (dread), 10, 11.4, 12 and 13. Kinds-of-error rows that apply, beyond the shared ones: "An owner term used in a neighbouring sense, or a theory narrowed or turned round (the commonest kind)"; "A claim credited to the wrong theory, book or person"; "A contradiction between skills that no single-skill review can see"; "A pointer that lands nowhere or on the wrong thing".

## Brief B: use-tester

Your area is whether the process can be followed, step by step, now that these edits are in. Walk these situations through the skill, its modules and `kept-cases/README.md` as an agent would, and run what the text tells you to run, in your own copy (build it as a history whose last commit went through the gate, so it carries a stamp):
- A commit made on GitHub (with the gate off) that edits a frozen theory and rewrites an old log entry, then the steps the text gives to put it right.
- A reviewed change rebased onto a newer main line, including one that touches a hook; a cherry-pick of a reviewed commit onto another branch; a squash of two reviewed commits.
- A change that is reviewed late and does not pass, taken back out the way the text says.
- A wrong check that stops every commit: once committed outside the gate, and once approved by the gate.
- A planted test retired because a check was meant to change.
- The owner answers a question that a kept case cites; a one-word typo in a skill whose cases are owed a rerun, and in one whose cases are not.
- A writer's question about a twist's clue, and separately about a jump scare and a character reveal meant as a shock, through the plot skill's building and diagnosing routes to `.claude/skills/plot/references/reveals-and-withholding.md`, section 2.
- Situations no finding produced: a rescue from nowhere at the climax; a story told with its ending announced in the first line, as in *Chronicle of a Death Foretold*; and the build's own first commit through the gate on the live history (last commit `35f2939`, where no commit is approved yet), walked in a copy.
- The owner asks whether the gate can be trusted. Follow what the skill, `CLAUDE.md` and S10 would have an agent say.
- Near neighbours where nothing should fire: a fresh clone's first session; an ordinary run of commits through the gate; a merge made with `git merge -m`.

The findings listed for you: the third look's use-tester U1 to U8, m1 to m6 and the stall list; and the scripts reviewer's A, C, D and K as they bear on following the process.

Term-sheet rows that apply (`.claude/skills/error-correction/references/owner-terms.md`): 1 (1.2, guarantee), 6.1, 7 (dread), 10, 11.4 and 13. Kinds-of-error rows that apply, beyond the shared ones: "A check or a step that stops honest work, or leaves no way through"; "A commit that skips the gate, or arrives where it cannot see (a fast-forward, a cherry-pick, a commit made on GitHub)".

## Brief C: scripts and hooks

Your area is the scripts and hooks: everything under `.claude/skills/error-correction/scripts/`, `.claude/skills/add-source/scripts/`, `.claude/hooks/`, `.githooks/`, `.claude/settings.json`, `.gitattributes`, and `kept-cases/run-kept-cases.js`.

The findings listed for you: the third look's scripts A to Q, the brief check's finding 3 (the setting WORKSHOP_INSIDE_PLANTED_FAULT_TEST), and use-tester U1, U2, U3, U5, U7, m1 and m5 as they bear on the scripts.

What the gate claims, and what it says it cannot do, is in `CLAUDE.md` (the table and the paragraph "What none of this can stop"), in the notes at the top of `check_commit.py` and `recheck_commits.py`, and in the notes at the top of the hooks (`refuse_check_bypass.py`, `git_command_reading.py`, `session_start.py`, `.githooks/prepare-commit-msg`); search for other statements too. Judge whether each stated limit is true and complete, for honest routes as well as deliberate ones. Look hardest for these:
- ways round that an honest or careless agent could take by accident, or with an ordinary git command (rebase, cherry-pick, revert, reset, amend, pull, a merge, a squash, a commit on GitHub) or setting;
- honest work the gate or the recheck stops, with no way through (a false alarm);
- a check that says "passed" when it did not run;
- how the new "last approved commit" behaves when there are several branches, merges, or no stamped commit at all.

Run `test_checks.py` in a copy (it takes a minute or two, because one test runs the gate's planted-fault stage for real). Also run the new `test_checks.py` against the scripts as the third look saw them (`git -C <snapshot> archive 5e5564d`, with the new test file put in), and say how many fail and which: the maker's records give counts nobody else has checked. Say which tests you ran on which scripts.

Kinds-of-error rows that apply, beyond the shared ones: "A check that passes while the thing is wrong, or can be got round"; "A check or a step that stops honest work, or leaves no way through"; "An edit to a frozen text"; "A commit that skips the gate, or arrives where it cannot see (a fast-forward, a cherry-pick, a commit made on GitHub)".

---

## 2. The check of the briefs (theory-checker)

**Brief check: /tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/briefs-round4.md**

**Findings (target; defect; grounds; connection; verdict)**

1. **Brief A, "Also check", bullet 2, and Brief C, "What the gate claims".** *Defect:* the list of places that state what the gate does is closed, and it leaves out the notes at the top of the hooks. *Grounds:* grep finds `refuse_check_bypass.py` lines 25–27 and `git_command_reading.py` lines 23–25 ("The real safety net is the recheck of every commit the gate did not see"). It also finds `session_start.py` lines 13–18 and `.githooks/prepare-commit-msg` lines 6–10. All four files changed between 5e5564d and 0f14d0a. *Connection:* under the new design the gate judges what unapproved commits got wrong, not the recheck. A closed list steers both checkers away from these copies (kinds row: "a rule changed in one place but not its copies"). **Bears.** Add these notes, and add "wherever else it is stated: search".

2. **Brief A, the plot bullet ("its copies: section 1, step 4, writing-rules section 1, C12").** *Defect:* it lists only the copies that changed. It leaves out statements of the planting rule that did not change: the diagnosing-table row "the twist came from nowhere" (plot `SKILL.md` line 123), quick-version item 2 (line 154), and `suspense-and-fear.md` section 5, which the new sentence cites for *Psycho*. *Grounds:* grep; C12's own target names "the diagnosing table and the quick version". *Connection:* C12 has recurred three times, each time through copies. Also, `references/writing-rules-and-rivals.md` belongs to error-correction but sits among plot paths (the same fault as last round's finding 10). **Bears.**

3. **Term-sheet rows, Briefs A and B.** *Defect:* section 7 (dread, Q6) is missing from both briefs, and section 1 (1.2 guarantee) is missing from B. *Grounds:* the new sentence at `reveals-and-withholding.md` line 30 says "a jump scare works only after dread has been built" and names a broken guarantee (*Psycho*). Term-sheet section 13 item 7 notes that the theory uses "dread" loosely at exactly that jump-scare line (Anticipation line 84). Brief B walks a jump scare. *Connection:* `reviews-and-briefs.md` section 5 requires every row that applies. **Bears.** Brief B should also carry the row "A commit that skips the gate, or arrives where it cannot see", since it walks GitHub commits, rebases, cherry-picks and squashes (minor).

4. **Brief B, the situations.** *Defect:* most situations replay the found faults. The jump scare and the character reveal are U4's cases; the rebased hook change is U1's; the withdrawal is U3's and U6's; the merge with `-m` is K's. No situation is added that the findings did not suggest, and last round's warning that a replay shows less has been dropped. *Grounds:* the kinds row "A test that can only agree…", which the shared part applies only to planted tests. *Connection:* this steers the use-tester towards confirming the fixes. **Bears.** Add situations the findings did not produce: a turn that rests on no earlier fact and is not a threat (a rescue from nowhere); *Chronicle of a Death Foretold*; and the real next step, the build's first commit through the gate on the live history (35f2939), where no commit is approved yet.

5. **Shared part, "Parts left undone".** *Defect:* the list is incomplete. (a) Scripts finding G was applied only in part: `run_all_checks.py` lines 16–17 and 62 (`LARGE_RECORDS_ALLOWED`) still exempt one kept record from the size limit. (b) The Book-text rule reading the staged register is still "not tried" (C15). Last round's brief listed it (kept brief, line 31). *Connection:* "listed next" invites the checker to judge the list rather than search for more. **Bears.** Seen in passing: `CLAUDE.md` line 44 says "A text file over 100 KB is refused anywhere".

6. **No brief asks anyone to confirm the counts.** C15, entry 30 and the status line say 166 tests, all passing, and 19 failing on the scripts the third look saw. *Grounds:* R13 found last round's counts stale, and its "28 fail" had not been rerun. *Connection:* the claim has no receipt, and Brief C runs `test_checks.py` only at 0f14d0a. **Bears.** Ask Brief C to run the new tests against 5e5564d's scripts, or list the counts as unchecked.

7. **Labels "B1 to B12" (shared part, Brief A) and "the brief check's B3" (Brief C).** *Defect:* these labels exist nowhere. The kept file numbers the findings 1 to 12, and "B3" collides with scripts finding B. *Grounds:* grep of the repository finds only story-world diagram nodes. **Bears; minor.** Write "brief-check finding 3 (the setting WORKSHOP_INSIDE_PLANTED_FAULT_TEST)".

8. **Shared part, "the main change" and "the findings these edits answer".** *Defect:* mild steering. "What the history alone can show" states the design's premise as fact. "These edits answer" assumes the outcome. Section 4 of the kept plan file carries the maker's verdicts ("the simpler design above answers them", line 206), and the brief does not mark them as claims to judge. The summary also leaves out the condition "made straight on top of an approved commit". *Grounds:* section 5, "no findings or verdicts from its author". **Bears; minor.**

**Checked and found right**
- The live tree matches 0f14d0a (cmp on every tracked file; no extra files on either side apart from ignored ones).
- The commits exist, and the third look saw 1e92459..5e5564d.
- Both kept files contain all seven scratch originals in full, with spacing collapsed.
- The labels R1–R24, U1–U8, m1–m6, A–Q, the stall list and the kept-case notes exist.
- Every file in the diff falls in some brief's area.
- Brief A's list of corrections, its S10 and S12, and the parts of the project story match the diff hunks.
- `checks-and-cases.md` section 2 states the owner's route. `CLAUDE.md` line 44 and the recheck note (lines 43–46) state the copying limit. `test_checks.py` has the test that runs for real. The bypass hook lets `core.hooksPath .githooks` through.
- Every quoted kinds row is word for word.
- Nothing contradicts C5 or C1: the file-26 bullet is open-ended.

**Not checked**
- Whether the edits are right, beyond what I noted in passing.
- Whether a known fault has been planted this round.
- No commits or test runs; hook code beyond its notes.
- Whether the plan came before the changes. The only evidence is file times: `plan-round3.md` at 16:33:41, `fix_hooks_round3.py` at 16:40.

**Verdict: passed after changes.** Change 1 to 6 before the briefs go out; 7 and 8 are minor.
---

## 3. The lead's plan, written before any change

# Plan for answering the fourth look, written before any change (theory-checker's report in; use-tester and scripts still running)

To put right (theory-checker T1 to T24):
- T1: the receipt check always comes from the last approved commit, also for a commit that changes only checks; only the machine checks come from the staged files there. A wrong receipt check that stops every commit goes to the owner's route, stated with the gate script's. Plant: a check-only commit that loosens the receipt check and carries no receipt is stopped. C15 records the fourth firing.
- T11, T18, T19: file 26: apply or list each break-test finding still left (the ring beat's settling test, A:710-711, the spoken-rule count in B's middle, the direction hints B:161 and B:1176 as a question for the owner), reword "weakened, not lost" and "Weakened.", fix the stale lines; S12 gains the direction hints as something the owner could confirm.
- T2, T3, T5, T22: every statement of what the gate stops is scoped: a check loosened outside the gate is judged only by the planted faults and its late review (the two-commit limit); the honest routes are listed, not counted as one; the check-only exception names what it does not reach (the gate script, the receipt check, the recheck, the planted-fault test).
- T4: notes for a person go into the log entry of the commit that shows them, and to the owner in the report; the texts say so, and that they are shown once.
- T6, T7: S10 (b) described truly on both sides; the places the owner is already asked are listed with what each asks.
- T8: say the receipt covers the lines a change adds and removes, not where they sit; a move after review within a module keeps the receipt, so the reviewer is told to read the lines in place. (Keeping context in the fingerprint would bring back U5.)
- T9, T10, T14, T15, T16, T17: plot: "plant, hide, reveal" for every surprise, with section 2's exemption for a bare threat's arrival; "lasts seconds" and "buys seconds" scoped (unless it breaks a guarantee early, or makes the audience reread); the jump-scare citation and "dread"; "no fact shown earlier"; "early"; the rescue clause tagged as the workshop's extension of Egri; the Bond pointer; S13 item 9.
- T12, T20, T21, T23: records and small mismatches.
- T13: keep the hand try of the retiring rules and the trial's first half as records in the repository.
- T24: run_all_checks' note.
To keep working: all 166 planted tests; every check passing; the reply check identical in five skills.
Findings from use-tester and the scripts reviewer: added here when they arrive, before those changes are made.

## Added when the scripts reviewer's report arrived (before any change)

- 1 (the owner's route fails; a group crash cannot be retired): the planted-fault test finds a receipt form by its path, not its message, and each receipt and gate test runs on its own, so one failure names one test; the texts say exactly which stops each route clears, and that past that there is no route inside the workshop: tell the owner. No new owner-approval mechanism.
- 2 (GitHub's merge button leaves the main line unstamped): the last approved commit becomes the most recent approved commit by any path, not only along first parents; the same in the gate, the recheck and session start. Planted: an unstamped main line, a merge made as GitHub makes one, then an outside log rewrite and an outside loosened check, both stopped.
- 3 ("one honest route"): the honest routes the gate misses are listed in one place (checks-and-cases.md section 2), and the other places point to it rather than counting them.
- 4: GIT_REFLOG_ACTION removed from the copies' settings; planted merge bringing a check change.
- 5: retirements read from the receipts of every commit since the last approved one, with the same owner rule; planted merge of a branch that retired a test.
- 6: a check-only commit may carry only receipts named by a fingerprint; planted.
- 7: a check that the four Claude hooks are registered in the settings, with planted faults.
- 8 (with T4): notes are shown until the next approved commit; the texts say to copy each into that commit's log entry and tell the owner.
- 9: a withdrawal also needs the commit's own change to no longer apply in reverse; planted reorder.
- 10 (with T8): the fingerprint keeps one unchanged line either side of each change; planted move after review. (A rebase over an edit right next to the change then needs a new review; said so.)
- 11: a pull that makes a merge is read from FETCH_HEAD; planted.
- 12 (with R2): a planted rewrite of an indented line inside an old entry.
- 13: the one large record exempt only while its contents match a fingerprint; 14: the revert advice names the last approved commit; 15: the gate's record is ignored when older than two minutes; 16: the quoted hooksPath must be this project's; a quoted GIT_CONFIG_PARAMETERS is read; 17: the Book-text rule reads the register from the last commit; 18: a refused retirement is printed as refused.

## Added when the use-tester's report arrived (before any change)

- F1 (with scripts 4): every setting git gives a hook (names beginning GIT_) is removed from the copies the planted-fault test makes; planted: a merge bringing a reviewed hook change, through the real planted-fault stage.
- F2 (with scripts 5): retirements read from every receipt since the last approved commit.
- F3 (with scripts 8, T4): texts.
- F4: pre-commit prints a plain stop line when the gate script itself cannot run; checks-and-cases.md says what the agent prepares, what the owner does (the edit made on GitHub), and that both the broken commit and the correction need late receipts.
- F5 (with scripts 14): the frozen check's advice names the commit it compares with; the gate's revert advice names the last approved commit.
- F6: the shock exemption excludes a threat that decides the climax (section 6), with a telling test: would a first-time audience make sense of it with no fact they were given?
- F7, F8: session start runs the last approved commit's checks, not the ones on disk, against that commit, and prints the first lines of what fails.
- F9: the text says to put back only the changed entry, not the whole file.
- F10, F11, F12, F13: texts (the owner is needed to retire a guarded test when correcting a wrong check; the typo route in checks-and-cases.md; a conflicted cherry-pick runs the gate; two late receipts; the jump-scare citation; the grandmother example dropped, since it was a walk case).
