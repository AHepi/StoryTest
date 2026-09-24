# The fifth look at the error-correction build: briefs, brief check and plan, 24 September 2026

What this is: the four briefs as sent (after the brief check's findings 1 to 13 were applied), the brief check by theory-checker word for word, and the lead's plan for answering the fifth look, written before any change and added to as each report arrived. Kept for log entry 32.

---

## 1. The briefs, as sent

# Briefs for the fifth look at the error-correction build (the edits answering the fourth look)

(Revised after the brief check by theory-checker: its findings 1 to 13 applied as it proposed. Its finding 2 led the maker to keep the trial's first half out of the repository, and its finding 9 to a change in the large-record check, both before the snapshot named below. The revised brief was not checked again.)

## Shared part (goes at the top of each brief)

You are reviewing edits you did not make. The maker is the lead agent. Your job is to find what is wrong, with reasons; the maker will apply or reject each finding, and your report will be kept word for word in the repository and pointed to from the build's review receipt. Do not read other files in the scratchpad folder than the ones named here: they hold the maker's own notes and views.

Where things are:
- The live repository is `/home/user/StoryTest`. Do not edit it, commit in it, or run anything there that writes files. Read it freely.
- A scratch snapshot repository is at `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/rereview`. Its commit `018ebd6` is what the fourth look saw; `c52f191` is now. The working tree of the live repository matches `c52f191`, apart from files git ignores (the book texts in `sources/raw/` are among those; never copy book text into anything you write).
- **The edits to review:** `git -C <snapshot> diff 018ebd6 c52f191`. The new files `.claude/reviews/kept/2026-09-24-build-fourth-look.md` (the fourth look's three reports: theory-checker T1 to T24, use-tester F1 to F13, scripts 1 to 18) and `.claude/reviews/kept/2026-09-24-build-fourth-look-briefs-and-plan.md` (the fourth look's briefs, the check of those briefs with its findings numbered 1 to 8, and the maker's plan) are records kept word for word; they hold the findings these edits were made to answer. The new file `.claude/reviews/kept/2026-09-24-hand-tries.md` is a record too. The plan's statements that a change answers a finding are the maker's claims, to be judged like any other.
- Any experiment runs in a copy you make yourself under `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/r5-<your name>/`, never in the live repository. To commit in a copy with the gate switched on, run `git config core.hooksPath .githooks` inside the copy. The live session has a hook that refuses commands which look like skipping the gate when they seem to target the live repository; use literal paths to your copies.

The main changes, in the maker's words, so you know what to look at (a description, not a claim that they work or that their premises hold): the last approved commit is now the most recent approved commit by any path, not only along first parents; the receipt check always comes from the last approved commit, also for a commit that changes only checks; every git setting (names beginning GIT_) is kept out of the planted-fault test's copies; retirements are read from every receipt added since the last approved commit; a new check makes sure the settings still register the workshop's four hooks; a claimed withdrawal must also no longer undo; a pull is read as a merge; the receipt's fingerprint keeps one unchanged line either side of each change; session start runs the last approved commit's checks; the maker's list of the honest routes the gate misses is in one place (`references/checks-and-cases.md`, section 2); whether it is complete is for you to judge.

What to look for, in your area:
1. For each finding listed for you: is it answered in content by the edits? Where the edits leave a finding not applied, or applied only in part, is the reason sound? The parts the maker left undone, with the maker's reasons, are listed next; judge them, and look for any others.
2. Do the edits themselves bring in new errors? Most new errors in this workshop's history came from fixes, and each of the last four rounds found new faults in the answers to the round before.

Parts left undone, and the maker's reasons (to be judged, not taken as right):
- A way for the owner to approve a commit by hand (scripts finding 1): not built, since a hand-typed approval is what the gate exists to refuse; instead the texts say what each route for a wrong check clears, and that past that the owner is told.
- No planted tests for the stale gate record being ignored after two minutes (scripts 15), for the Book-text rule reading the register from the last commit (scripts 17), or for the revert advice naming the last approved commit (scripts 14).
- Not tried by a planted test: the owner rule for retiring a guarded test (tried by hand; the record is kept).
- The copying check is not rerun on each commit the gate did not approve (stated as a limit).
- Claude Code asking the owner before edits to the gate's own files (owner question S10, option b): left to the owner.
- Kept-case notes (case 04 and case 11): left to the run of the kept cases on the committed build.
- Not checked by anyone but the maker: the counts in C15, entry 31 and the status line (184 tests, all passing; 16 failing on the scripts the fourth look saw).

Lessons from earlier errors that apply to all three of you (rows of the kinds-of-error table in `27 Corrections.md`):
- "A change (a fix) that makes a new error; a rule changed in one place but not its copies": search for every other statement of a changed rule.
- "A record that is stale, unfinished, or leaves out who made an error."
- "A required check skipped, or a claim reported without its receipt, with an assumed input, or with agreement between checks that were not independent."
- "A test that can only agree: cases or examples drawn from the answer, or a fix confirmed on the case that made it": the new planted tests were written for the findings they answer, and a situation that only replays a found fault shows less than a new one. Try ordinary commands and situations they do not plant.

Report: one finding at a time, in four parts: the **target** (file and line), the **defect**, the **grounds** (a theory line, a term-sheet row, or a command and what it printed), the **connection** (how the grounds show the defect in the target). Then a verdict on each: **bears**, **does not bear yet** (name the test that would settle it), or **does not bear**, and a severity: must change, should change, or minor. Say what you checked and found right, and what you did not check. End with one of: passed; passed after changes (list what must change); not passed.

## Brief A: theory-checker

Your area is what the edits say: the `error-correction` skill and its modules, the plot skill and its module `references/reveals-and-withholding.md`, add-source, the reviewer agent `.claude/agents/theory-checker.md`, `kept-cases/README.md`, `CLAUDE.md`, `README.md`, `26 Test - The Catch - two versions.md`, `27 Corrections.md` (C1, C4, C5, C6, C12, C15 and the kinds table), `22 Questions - meanings only you can settle.md` (S10, S12) and `StoryTest - project story.md` (the status lines, the word list, entries 30 and 31, neither yet committed, and the next step).

The findings listed for you: the fourth look's theory-checker T1 to T24 (as they bear on what the text says), use-tester F3 to F13 and its stall list, scripts 3 and 8, and the brief check's findings 1 to 8.

Also check:
- The plot rule in `.claude/skills/plot/references/reveals-and-withholding.md`, section 2, against the Gap, Anticipation and Bond theories (it cites the Bond theory, Part 2 section 7) and the term sheet, walking the theories' own named cases through it, and its stretch of Egri's rule to every rescue; and every other statement of the planting rule, changed or not, wherever it is: search. Among them: section 1 and section 6 of that module; the plot skill's `SKILL.md` step 4, its diagnosing-table row for a twist that came from nowhere, and its quick version; `.claude/skills/plot/references/suspense-and-fear.md` section 5, which the new sentence cites; the error-correction skill's `references/writing-rules-and-rivals.md`, section 1; C12; the plot skill's trap "Surprise by default" (changed in this diff); `.claude/skills/plot/references/structure-and-conflict.md` (Egri's rescue rule); `.claude/skills/character/references/change-and-growth.md`, section 8; and `.claude/skills/genre/references/how-genres-work.md`.
- Every statement of what the commit gate does and cannot do, wherever it is stated: search. Among them: `CLAUDE.md`, the skill, `references/checks-and-cases.md` section 2, `references/reviews-and-briefs.md`, README, C15, the kinds table, S10, the project story, and the notes at the top of `.claude/hooks/refuse_check_bypass.py`, `.claude/hooks/git_command_reading.py`, `.claude/hooks/session_start.py`, `.githooks/prepare-commit-msg`, `.githooks/pre-merge-commit` and `.githooks/pre-commit`, and the note at the top of `run_all_checks.py` (its new check that the hooks are registered). Compare each with the notes at the top of `check_commit.py` and `recheck_commits.py`. Each must claim neither more nor less than the scripts do, for honest routes as well as deliberate ones.
- Every sentence in file 26 that compares the two versions: the owner does not know which came first. And its claim that every finding of the break test is now applied: check it finding by finding against `.claude/reviews/kept/2026-09-24-catch-break-test.md` itself, not against earlier reviewers' lists.

Term-sheet rows that apply (`.claude/skills/error-correction/references/owner-terms.md`): sections 1, 6.1, 7 (dread), 9.5 (care), 10, 11.4, 12 and 13. Kinds-of-error rows that apply, beyond the shared ones: "A book rule adopted as law, failing the owner theory's own case"; "An owner term used in a neighbouring sense, or a theory narrowed or turned round (the commonest kind)"; "A claim credited to the wrong theory, book or person"; "A contradiction between skills that no single-skill review can see"; "A pointer that lands nowhere or on the wrong thing".

## Brief B: use-tester

Your area is whether the process can be followed, step by step, now that these edits are in. Walk these situations through the skill, its modules and `kept-cases/README.md` as an agent would, and run what the text tells you to run, in your own copy (build it as a history whose last commit went through the gate, so it carries a stamp):
- A commit made on GitHub (with the gate off) that edits a frozen theory and rewrites an old log entry, then the steps the text gives to put it right.
- A reviewed change rebased onto a newer main line, including one that touches a hook; a cherry-pick of a reviewed commit onto another branch; a squash of two reviewed commits.
- A change that is reviewed late and does not pass, taken back out the way the text says.
- A wrong check that stops every commit: once committed outside the gate, and once approved by the gate.
- A planted test retired because a check was meant to change.
- The owner answers a question that a kept case cites; a one-word typo in a skill whose cases are owed a rerun, and in one whose cases are not.
- A writer's question about a twist's clue, and separately about a jump scare and a character reveal meant as a shock, through the plot skill's building and diagnosing routes to `.claude/skills/plot/references/reveals-and-withholding.md`, section 2.
- The ordinary shape of this repository's work: a session's branch, its commits through the gate, then the pull request merged on GitHub with a merge commit (made in a copy with the gate off, as GitHub would), then an edit made on GitHub, then the next session's first commit.
- A rebase that lands a reviewed change right next to an edit made meanwhile; the owner's route for a wrong gate script, followed exactly as written.
- Situations no earlier reviewer walked: a new owner theory, and separately a new book, taken in through add-source (the Book-text rule now reads the register from the last commit, so a book registered in the same commit is not named there yet); two session branches, each with approved commits, merged in either order; an honest edit to `.claude/settings.json`; and a clone on Windows, where git may change line endings.
- The trial of the process (its plan is not in the repository): would anything committed in the build hand its second-half agent the answers? Read `.claude/reviews/kept/` and the records for planted problems or expected answers of a trial, and say what you find.
- The owner asks whether the gate can be trusted. Follow what the skill, `CLAUDE.md` and S10 would have an agent say.
- Near neighbours where nothing should fire: a fresh clone's first session; an ordinary run of commits through the gate; a merge made with `git merge -m`.

The findings listed for you: the fourth look's use-tester F1 to F13 and its stall list, and the scripts reviewer's 1, 2, 3, 5 and 8 as they bear on following the process.

Term-sheet rows that apply (`.claude/skills/error-correction/references/owner-terms.md`): 1 (1.2, guarantee), 6.1, 7 (dread), 10, 11.4 and 13. Kinds-of-error rows that apply, beyond the shared ones: "A check or a step that stops honest work, or leaves no way through"; "A commit that skips the gate, or arrives where it cannot see (a fast-forward, a cherry-pick, a commit made on GitHub)"; "A contradiction between skills that no single-skill review can see" (the plot routes have copies in the character and genre skills).

## Brief C: scripts and hooks

Your area is the scripts and hooks: everything under `.claude/skills/error-correction/scripts/`, `.claude/skills/add-source/scripts/`, `.claude/hooks/`, `.githooks/`, `.claude/settings.json`, `.gitattributes`, and `kept-cases/run-kept-cases.js`.

The findings listed for you: the fourth look's scripts 1 to 18, theory-checker T1, T8, T21, T22 and T24, and use-tester F1, F2, F4, F5, F7 and F8 as they bear on the scripts.

What the gate claims, and what it says it cannot do, is in `CLAUDE.md` (the table and the paragraph "What none of this can stop"), in the notes at the top of `check_commit.py` and `recheck_commits.py`, and in the notes at the top of the hooks (`refuse_check_bypass.py`, `git_command_reading.py`, `session_start.py`, `.githooks/prepare-commit-msg`); search for other statements too. Judge whether each stated limit is true and complete, for honest routes as well as deliberate ones. Look hardest for these:
- ways round that an honest or careless agent could take by accident, or with an ordinary git command (rebase, cherry-pick, revert, reset, amend, pull, a merge, a squash, a commit on GitHub) or setting;
- honest work the gate or the recheck stops, with no way through (a false alarm);
- a check that says "passed" when it did not run;
- how the new "last approved commit" behaves when there are several branches, merges, or no stamped commit at all;
- the large-record exemption bound to a fingerprint, on a copy where git changes line endings (`core.autocrlf`), since the gate takes its snapshot with `checkout-index`.

Run `test_checks.py` in a copy (it takes three or four minutes, because two tests run the gate's planted-fault stage for real). Also run the new `test_checks.py` against the scripts as the fourth look saw them (`git -C <snapshot> archive 018ebd6`, with the new test file put in), and say how many fail and which: the maker's records give counts nobody else has checked. Say which tests you ran on which scripts.

Kinds-of-error rows that apply, beyond the shared ones: "A check that passes while the thing is wrong, or can be got round"; "A check or a step that stops honest work, or leaves no way through"; "An edit to a frozen text"; "A commit that skips the gate, or arrives where it cannot see (a fast-forward, a cherry-pick, a commit made on GitHub)".

## Brief D: copy-checker

Your area is the book-derived text these edits change: the plot skill's `references/reveals-and-withholding.md` (sections 1, 2 and 6) and `SKILL.md` (step 4 and the trap "Surprise by default"), which draw on Egri, McKee and Truby. Compare the changed passages with the book texts in `/home/user/StoryTest/sources/raw/` for close paraphrase, a book's order, or its example lists, which the 8-word script cannot see. Quote no book text in your report beyond titles, names and the authors' short term names. Report in the four-part form, with a verdict on each finding and what you did not check.

## 2. The brief check (theory-checker), word for word

**Brief check, round 5** (`/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/briefs-round5.md`). I edited nothing. My only experiment ran in `scratchpad/bc5/`.

**Findings.** Each gives the target, the defect, the grounds and the connection, then a verdict.

1. **Brief B, "Situations no finding produced".** *Defect:* all three situations have already been walked. *Grounds:* the fourth look's use-tester walked the rescue at the climax (report line 525), *Chronicle* (line 527) and the first gated commit on 35f2939 (line 274). The rescue also came from the last brief check's finding 4 and from F6. *Connection:* this is last round's brief-check finding 4 coming back (kinds row "A test that can only agree"). **Bears; must change.** Add situations nobody has walked:
   - a new theory or book added through add-source. The Book-text rule now reads HEAD's register (`review_receipt.py` diff line 56), so a book registered in the same commit is not named there.
   - two session branches, each with approved commits, merged in either order;
   - an honest edit to `.claude/settings.json`;
   - a Windows clone (see finding 9).

2. **Shared part, "The new file …hand-tries-and-trial-first-half.md is a record too".** *Defect:* no brief asks whether committing this file spoils the trial. *Grounds:*
   - the file carries the planted problems, the predictions and the "true set" (lines 59–90, 180);
   - its half that uses the build "waits for the build to be committed" (line 2);
   - that half runs on "a copy of the committed build" (Conditions).

   *Connection:* the agent in that half could find the answer key in its own copy. **Does not bear yet** (test: read the trial's instructions for what its agent may read). **Must change:** give this question to Brief A or B.

3. **Brief A, the file-26 bullet.** *Defect:* it asks only for sentences that compare the two versions. *Grounds:* C1's fifth recurrence was that the claim "every finding applied" was checked against the findings reviewers named, not against the break test. File 26 line 131 still claims every finding is applied. *Connection:* this is the same route as the last five times. **Bears; should change.** Ask for line 131 to be checked finding by finding against `.claude/reviews/kept/2026-09-24-catch-break-test.md`.

4. **Brief A, the plot bullet.** *Defect:* it checks section 2 only "against the Gap and Anticipation theories", and it leaves out copies of the changed clauses.
   - *Credits:* the new sentence cites the Bond theory, Part 2 section 7 (`bond-theory.md` line 84), and stretches Egri to every rescue.
   - *Copies not named:*
     - plot `SKILL.md` line 164 ("Surprise by default", changed in this diff);
     - `plot/references/structure-and-conflict.md` line 98 (Egri's rescue rule);
     - `character/references/change-and-growth.md` section 8 (line 101);
     - `genre/references/how-genres-work.md` line 125.
   - *Rows missing:* term-sheet 9.5 (care), and the kinds row "A book rule adopted as law…". The last look's mark (line 197) says the rescue clause rests on Egri.

   **Bears; should change.**

5. **Brief B, "ending announced in the first line, as in *Chronicle*".** *Defect:* this misstates the theory's case. *Grounds:* Anticipation line 47 says *Chronicle* "announces its killing in the title". The first line belongs to *The Secret History*. **Bears; should change:** quote line 47.

6. **Brief B, kinds rows.** *Defect:* the row "A contradiction between skills that no single-skill review can see" is missing. *Grounds:* the kinds table names `use-tester` as a catch for that row. B walks plot routes whose copies sit in character and genre. **Bears; should change.**

7. **Briefs A and C, the lists of gate statements.** *Defect:* three places whose wording changed are not named:
   - `.githooks/pre-merge-commit` (its note changed, and T22 targets it);
   - `.githooks/pre-commit` (a new stop line);
   - the note in `run_all_checks.py` about the new hooks check.

   The new check is also missing from the table in `checks-and-cases.md` section 2. **Bears; minor**, since the list is open ("search").

8. **Brief C, its findings list.** *Defect:* four findings have script targets but are not listed: T21 (the form hint in `review_receipt.py`), T22, T24 and F4 (the note in `check_commit.py` and the stop line in pre-commit). **Bears; should change.**

9. **Brief C, "Look hardest for".** *Defect:* nothing points to the new fingerprint-bound exemption for large records. *Grounds:*
   - I committed that record in a scratch repository and ran `git -c core.autocrlf=true checkout-index`. The SHA-256 changed from 1d14c95d… to 40e1fcff… (935 CRs).
   - The gate takes its snapshot with `checkout-index` (`check_commit.py` line 238).
   - `.gitattributes` exempts only `sources/` and `foundations/`.

   *Connection:* a Windows clone may be stopped on every commit, the same kind of fault as C6. **Does not bear yet** (test: run the gate in a copy with autocrlf on). **Should change:** add this to Brief C.

10. **Shared part, "(a description, not a claim that they work)".** *Defect:* the words "or that its premises hold" have been dropped. They were added after last round's brief-check finding 8. "The honest routes … are listed in one place" states completeness as fact. **Bears; minor.**

11. **Shared part, "Parts left undone".** *Defect:* scripts 14 (the revert advice now names the last approved commit) is not planted, and the list does not say so. *Grounds:* grep of `test_checks.py` finds no test of that advice; its only revert is the withdrawal at line 966. **Bears; minor.**

12. **Stale lines.**
   - Brief C says "one test runs the gate's planted-fault stage for real". Two do now (`test_checks.py` lines 1136–1190; story line 149).
   - The shared part says "the last three rounds". It is four now.

   **Bears; minor.**

13. **Copying.** *Defect:* no brief asks for a copy-checker. *Grounds:* the books are present in `sources/raw/`, and the changed plot module draws on Egri, McKee and Truby. The gate's 8-word check will still run by itself at commit. **Does not bear yet** (whether any added line comes from a book); minor.

**Checked and found right**
- Commits 018ebd6 and 4430f36 exist. The live tree matches 4430f36 (`diff -rq`), apart from `__pycache__` and an empty `cases/` folder.
- The findings T1–T24, F1–F13, scripts 1–18 and brief-check 1–8 all exist.
- The corrections, S10, S12 and the parts of the project story that the brief lists are exactly the ones changed in the diff.
- The counts 183 and 16 match C15 and story lines 13 and 149.
- `checks-and-cases.md` section 2 lists the honest routes the gate misses.
- Every kinds row quoted in the briefs is word for word.
- The maker's claims are labelled as claims.
- Nothing in the briefs contradicts C5.
- Every file in the diff falls in some brief's area.

**Not checked:** whether the edits are right, beyond what is noted above; test runs; hook code; the trial's instructions to its agent; the rest of `test_checks.py`, for other answers that are not planted.

**Verdict: passed after changes.** What must change: 1 and 2. What should change: 3, 4, 5, 6, 8 and 9. Minor: 7 and 10 to 13.

## 3. The plan, written before any change

# Plan for answering the fifth look, written before any change (copy-checker and theory-checker in; use-tester and scripts still running)

## When the looking stops (decided before this round's changes)

Five looks have each found faults, several made by the round before. So:
- this round's changes are looked at once more, by fresh agents, and that sixth look covers only this round's edits (the diff from c52f191), with the fifth look's findings as its list;
- after the sixth look, nothing is changed without a further look. A must-change it finds is put right and looked at again, narrowly; anything less is recorded in the receipt and in a correction's status line as open, for a follow-up change with its own review, and is not patched unreviewed;
- the receipt's verdict follows the sixth look's words.

## Copy-checker (C1 to C6 passed; D1 to D4 side findings)

- D1 (should change): `.claude/agents/copy-checker.md` line 13: `N=6` in front of the command becomes `--run-length 6` after the script name. Search every file (kept records aside) for other copies of `N=6`.
- D2 (minor, with V4): the rescue clause loses "*(built)*"; it says Egri's case is a murder weapon, and applying it to every rescue is the workshop's reading.
- D3 (minor): section 6 says Egri calls foreshadowing a promise himself (raw line 1839); the stretch to set-ups stays the workshop's (Q7).
- D4: at the commit, the register's four overlap cells get this round's run and date (the whole tree, 8 words, all four books), run in the repository folder.

## Theory-checker (V1 to V22)

- V1 (must change): file 26 is checked against the break test's own text, item by item, not against a reviewer's list; a table of every break-test finding (N1 and N20, each field) and where it now sits, or why not, goes in the plan's appendix before the edit. The short answer takes the break test's new wording in substance, with its line references (A:554, A:285, A:590, A:616-640, B:551, B:577, B:687, B:873-875, B:480, B:502, B:161); "Almost everywhere they differ, A does the job better" becomes the direction-free "Where they differ, A more often puts a rule on screen before the moment that depends on it". A:695-701 against B:632-638 (A's Eli explains the culture at greater length), A:714 ("And the puck?") and N20's remark that the "B tells" frame steered the search go in. The checks section's claim becomes true, or lists what is left and why. Entry 31 is not rewritten: entry 32 says its claim was wrong, and C1 records the sixth time. The stage this time: the fourth look's list stood in for the break test again, after C1's fifth-time record had named that very cause; the correction puts the item-by-item table in the file's checks section, so the next reader can check each line.
- V2: step 4 in plot SKILL.md: "plant, hide, reveal, except a bare threat's arrival: `references/reveals-and-withholding.md`, section 2". C12 gains the restored copy.
- V3: section 2 defines a bare arrival by the telling test: one a first-time audience makes sense of from what it already has (the baseline, "the real world plus the habits of the genre", and what the story has shown). The unshown bomb stays a fact of the story, only not shown. Dragons from nowhere in a world like ours are a departure that needs showing. writing-rules-and-rivals' copy follows, and its case gains this error.
- V4: the climax-threat clause and the rescue clause are labelled the workshop's reading, and both point to structure-and-conflict section 7: at the climax a set-up is needed but not enough.
- V5: "apart from a loosened check" in recheck_commits.py's note, check_commit.py's note, error-correction SKILL.md's Words, CLAUDE.md row 2, README line 89, kinds row (27 Corrections line 28).
- V6: the list "What the gate cannot do" gains: close paraphrase of a book (no script sees it); receipts checked for form only (whether the reviewer ran, or judged a light receipt right, is on trust); the Book-text line is the maker's word when the books are absent; "the owner named first" is checked as a name. The places that point to it say "among them" or "listed" without claiming completeness where they now do.
- V7: texts: after a pull, rebase or cherry-pick, run `recheck_commits.py` before the next commit; a note first seen in a passed commit's output goes into the next log entry.
- V8: checks-and-cases' tripwire sentence scoped to something wrong in the files (a frozen theory edited, a log entry rewritten, a receipt deleted) or a change to a reviewed file with no review at all; SKILL.md "not tripwires" gains the matching exception.
- V9: pre-commit detects a crash, not only an exit above 1: the gate script's own stop and pass lines are recognised; if neither appears, the plain stop line prints. Planted: a gate script with a syntax error. Line 44 corrected.
- V10: S10's list gains the two places (a note on the gate's files; a wrong receipt check, recheck or planted-fault test that stops its own correction), and says that two places on it already ask the owner to accept a change reviewed only afterwards (the gate-script correction) or checked as a name (named first), the cost S10 gives against (b).
- V11: owner-answers-and-revisions: a passage marked "answered" is compared with the owner's words by theory-checker; the review can be short, but it is not a light receipt.
- V12: the trial's first half gets a trace now: a kept record of each file's fingerprint (sha256) and time, with the contents held back until the second half, and the reason. If the session ends first, the half is lost and must be rerun; said so.
- V13, V14: file 26: the stale lines (132, 125) and the neutral wording for the length rival.
- V15: copies: suspense-and-fear line 20; writing-rules line 9; add-source line 87 (the script reads every file with a text ending); reviews-and-briefs line 36 (a book registered in the same commit).
- V16: records: C15's "only receipts ride" line; C15's "not tried by a planted test" names 14 and 15 too (or they are planted); kinds rows 21-22 "seen in"; C1 line 40; C5 line 72; entry 32 says entry 31's "three of them made by my last round" was wrong.
- V17: pre-merge-commit and checks-and-cases: a revert finished after a conflict runs the gate; a clean one does not.
- V18: "newest first" becomes "first in git's order (after a merge, the approved commit the last merge brought in)".
- V19: hooks-registered: SessionStart's matcher must be empty or "*" or cover startup, resume and compact; the frozen hook must cover Edit, Write, MultiEdit and NotebookEdit where the settings have them now. Planted: a narrowed matcher.
- V20: checks-and-cases line 49 made to match line 60.
- V21: the three stall items answered in the texts: a local squash needs a fresh review (its fingerprint is new); the receipt for a withdrawal follows the rule for any change (full, since it changes meaning back); a late review that passes only part of an outside commit: withdraw the rest by a revert of the parts that did not pass, with its own receipt.
- V22: does not bear yet: recorded as untried in the checks-and-cases route, with the test that would settle it.

To keep working: all 184 planted tests; every check passing; the reply check identical in five skills; the maps.
Findings from use-tester and the scripts reviewer: added here when they arrive, before those changes are made.

## Appendix: the break test, field by field, against file 26 as it stands (read before any edit)

Read from `.claude/reviews/kept/2026-09-24-catch-break-test.md` itself, not from any reviewer's list. ✓ = in file 26 now; ✗ = missing, to apply; — = left, with the reason.

N1
- holds_it: shared spine ✓; A more often has the set-up ✓ in substance, ✗ in the short answer's wording ("Almost everywhere they differ, A does the job better", "keeps showing the rules"); links the table misses (A:535-537/B:687, A:577, A:1144-1146, A:1467, A:439) ✓; the stated reason loose, rows 1, 3, 6 and 7 simple absences ✓ (the rows say so); A's reserve set-up spoken (A:1022) ✓; A's Eli explains the culture at greater length (A:695-701 against B:632-638) ✗; swap "shows against explains" for "has the set-up against lacks it" ✗ in the short answer; remove test (only B:161 breaks; B:833, B:873-875, B:977 with B:608, B:1248-1252 weaker) ✓; the five checks' agreement ✓.
- stock_note_test: the summary needs its line references ✗.
- flip_test: the talk half does not survive; N20 praises two spoken rules ✓ (checks section; the napkin-ring item).
- facts_checked: row references ✓; B's own shown set-ups (B:873-875, B:480/B:502, B:960, B:968) ✓; some of A's set-ups are spoken (A:1022 ✓, A:571-577 ✗); row 4 overstated ✓.
- rival: running time ✓, with "about six per cent shorter" ✗; B's middle adds spoken rules ✓ (to be reworded neutrally, V14); second rival, who works a rule out, a character choice (A:590 against B:551) ✗ as a named rival (row 4 and the fix carry the substance).
- direction: order words ✓; B:161, B:1176 and the dated heading as hints, to the owner ✓.
- pulls: added weight in the slow scenes ✓; "length barely changes" gone ✓; three routes ✓.
- recommendation and new_wording: reword ✗; the short answer takes it in substance.

N20
- holds_it: paper letter held by the leaf picture and the F ✓; remove test, it makes the rule clearer but sets nothing up ✗; camera recording held, drawn like the visor's labelled-floor diagram (B:1425-1453) ✗, a further route in A ✓; napkin ring ✓; "Why lock you up?" (A:710-711, A:706 ✓, A:714 ✗); bare "Eli." (A:697 ✓, A:185 ✓ in substance); ring beat ✓; B's uncredited set-ups ✓.
- stock_note_test: three items with no reason on the page ✓ (marked taste).
- flip_test ✓ (taste line).
- facts_checked: "the best in either version" ✓; "a real question for Iona" ✓ (the phrase is gone; A:706, A:714 ✗ as above).
- rival: local polish ✓ in substance; the "B tells" frame steered the search ✗.
- direction ✓; pulls ✓; new_wording ✓ in substance (the cylinder line corrected: A plants one too, A:495).

## Added when the scripts reviewer's report arrived (before any change)

- 1 (must change; `git commit -a` and `git commit <file>`): the checks and the recheck that read the real repository get git's own staging area for this commit (GIT_INDEX_FILE, made a full path); only the scripts that make throwaway copies lose every GIT_ setting. The frozen check's advice names the most recent commit where the file still matches its line on the frozen list, not simply the last approved commit (which may already hold the edit). Planted: a frozen edit with `commit -a`, and with `commit <file>`; neighbour: a withdrawal with `commit -a` goes through.
- 2 (must change; the last approved commit after a GitHub merge): "most recent by any path" is replaced. Walking back along the main line (each commit's first parent), the last approved commit is the first that is either stamped for its own contents, or a merge made without the gate that is exactly git's automatic merge of its two parents, each of them approved in this sense or from before the gate came in (GitHub's merge button makes such a merge when there is no conflict). A merge made on GitHub with a conflict resolved by hand is not approved; the walk goes on to its first parent, so the main line's entries and checks are what count, as in a merge made through the gate. The same rule in the gate, the recheck and session start; the note counts only commits that are neither. Every text that says "by any path" changes. Planted: two approved branches merged on GitHub one after the other, without and with a conflict (the conflict resolved the natural way goes through; a rewrite of the main line's entry is stopped); a stale branch merged on GitHub after a check was tightened on main (the tightened check is used, and names the file); the round-4 tests rebuilt on a stamped base.
- 3: `.gitattributes` keeps Unix line endings for the gate's hooks and the scripts. Planted: a copy made with core.autocrlf=true commits through the gate.
- 4: the Book-text rule counts an author named in either the last approved commit's register or the staged one; the name pattern reads names like McKee. Planted: a register row and a module in one commit, with the books absent, needs the Book-text line; "Robert McKee" is read.
- 5 (with V9): the gate script leaves a result ("passed" or "stopped") where pre-commit can read it; when it is missing, pre-commit prints the plain stop line. Planted: a gate script with a syntax error, committed outside the gate, then a commit: the plain line appears.
- 6 (with V19): hooks registered fails on "disableAllHooks"; a matcher is read as Claude Code reads it (empty or "*" for all, otherwise a pattern), so ".*" passes and a narrowed one fails; SessionStart must cover startup, resume and compact. The limit (local and personal settings, which no check here reads) is stated. Planted: disableAllHooks; a narrowed matcher; neighbour ".*".
- 7: the texts give the route after a merge made on GitHub with a conflict (a branch from the last approved commit, the check corrected there as a check-only commit, then the main line merged in through the gate), planted; and the owner's real options when the receipt check, the recheck or the planted-fault test stops its own correction: edit the gate script (which runs as the last commit has it), or take the branch back to before the approved commit that brought the fault in.
- 8: a shallow copy: the gate's note says so and names `git fetch --unshallow`; listed in section 2.
- 9: a passing planted-fault test prints how many tests were not run.
- 10: the recheck's book note skips the one large record allowed by name while its fingerprint matches.
- 11: the refusal hook refuses a single-quoted '$PWD/.githooks' and a $PWD after a cd in the same command. Two hook tests.
- 12: prepare-commit-msg's note says "within two minutes".
- 13 (with V15): add-source SKILL.md and overlap_check.py say every file with a text ending.
- 14: the receipt tests run one by one, each with its own name.
- 15: session start's excerpt leaves out "skipped on request" lines.

## Added when the use-tester's report arrived (before any change)

- 1 (must change; two sessions each add the same entry number): with scripts 2's rule, a merge made on GitHub with a conflict is judged by its first parent, the main line, so keeping main's entry and renumbering your own goes through, and renumbering main's is stopped. In a merge made through the gate, the records check also protects every entry the other side added since the two lines split (by number and text), so when both sides added the same number the merge is stopped, with a plain message: abort it and rebase your branch onto the other (`git merge --abort`, `git rebase <other>`), renumbering your own entries after its. Section 2 and CLAUDE.md's row say so. Planted: GitHub merge with the conflict resolved the natural way (passes) and the reverse way (stopped); a merge through the gate where both added entry 32 (stopped, with the advice); the rebase route (passes).
- 2: as scripts 2 (the stale branch's older checks no longer take over).
- 3: as scripts 7 (the route after a merge made on GitHub with a conflict: correct the check on a branch from the last approved commit, merge the main line into that branch through the gate, and carry on from there; the other direction is stopped).
- 4: as V9 and scripts 5.
- 5: as scripts 3, and the skill fingerprints read with Windows line endings turned into Unix ones, so a copy with other line endings does not list every skill as changed.
- 6: as V8.
- 7: as V7.
- 8 (must change before the trial's second half): the trial's with-build half runs in a copy without `.claude/reviews/kept/`; before it runs, the copy is searched for the problems' own words ("villain ladder", "Q1 with option", "planted problem") and any other hit is removed from that copy. Written into the trial's procedure (C6 / the trial record) now.
- 9: as scripts 4.
- 10 (with V11): when a question is answered, each tagged passage is rewritten to state the answer (no "a question put to the owner" left beside "answered"), compared with the owner's words by theory-checker, and the skill's kept cases are rerun, since the meaning changed; the typo route is not for it.
- 11: reviews-and-briefs' copy of the withdrawal conditions gets the third.
- 12: session start's failing-check excerpt leaves out the records check's own notes (the "entry N is new" lines and the status lines).
- 13: does not bear yet; kept case 04 is rerun in run 2 and graded on whether its route goes through the theory line or echoes the trap.
- Stall items: a typo edit made on GitHub gets a light late receipt (stated); "put it back" for a frozen theory says "unless the owner meant to revise it: then the revision is a new file through add-source"; the telling test's "if not" names a fact of the world or the story, and says the genre's habits count as given (the baseline); session start does not run the planted-fault test (stated); a jump scare in prose: left open, recorded (no medium route is written for it yet).
