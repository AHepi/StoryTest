# The fifth look at the error-correction build: the four reports, 24 September 2026

What this is: the four reviewers' reports, word for word as each agent returned it. They looked at the edits answering the fourth look (snapshot commits 018ebd6 to c52f191); the copy-checker looked only at the plot passages that draw on books. The reviewers made no edits; every experiment ran in scratch copies. Their briefs, the check of those briefs, and the lead's plan for answering them (written before any change, with the break test's fields laid against file 26) are kept beside this file, in `2026-09-24-build-fifth-look-briefs-and-plan.md`. How each finding was answered is in the build's review receipt. The copy-checker's report names places in the books by line and describes them in its own words; it quotes no book text. Kept for log entry 32.

---

## 1. theory-checker

**Theory-checker, fifth look: the edits 018ebd6..c52f191, which answer the fourth look**

**How I worked**
- I read `CLAUDE.md`, the term sheet, the kinds table, corrections C1 to C15, the brief (its shared part and Brief A only), the diff, and the three new kept records.
- For each theory passage I read the theory before the change.
- I edited nothing in the live repository. Afterwards its HEAD was still 35f2939, `git status --short` still showed 30 entries, and `core.hooksPath` was as I found it. The live `CLAUDE.md` is the same as c52f191's (checked with `diff`).
- Every experiment ran in copies under `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/r5-theory-checker/`.
- Line numbers are at c52f191, which matches the live tree.

**The theory, read first (one line each)**
- Gap line 57: surprise is a gap you didn't know was there: you thought you understood and you were wrong. It carries no condition about rereading or planting.
- Gap line 59: the bomb that simply goes off gives fifteen seconds of surprise; shown first, it gives fifteen minutes of suspense. Only the plot changed.
- Gap line 47: in a world full of dragons, a dragon attack might be weather.
- Anticipation line 25: Shock is a side rung. The audience knows nothing, and the threat arrives without warning (the jump scare).
- Anticipation line 41: the bomb stands for the time term: seconds of surprise against minutes of suspense.
- Anticipation lines 67 and 69: *Psycho* kills its apparent lead early, and after that every threat is real. Break one guarantee convincingly, not all of them.
- Anticipation line 84: a jump scare on its own is a reflex. After real dread it works as a release valve; without dread it is a flinch.
- Bond line 84: care deepens when a character does something unexpected that was in them all along. It breaks when they contradict who they have been without the story earning it.
- Implied World line 20: audiences assume the world works like theirs unless told otherwise.

---

## Must change

**V1. File 26 still says every break-test finding is applied, and checked against the break test itself, it is not.**
- **Target:**
  - `/home/user/StoryTest/26 Test - The Catch - two versions.md` line 131;
  - repeated in `/home/user/StoryTest/27 Corrections.md` line 39 ("the four findings applied") and in `/home/user/StoryTest/StoryTest - project story.md` line 148.
- **Defect:** break-test findings are left unapplied, with no reason given.
- **Grounds** (`/home/user/StoryTest/.claude/reviews/kept/2026-09-24-catch-break-test.md`, note N1):
  - Its stock-note test says: "The summary names none of them, so it needs its line references to be held by this page." The short answer (file 26 line 28) still names no line reference. The test's own new wording names eleven (A:554, A:285, A:590, A:616-640, B:551, B:577, B:687, B:873-875, B:480, B:502, B:161).
  - It says "A's Eli explains the culture at greater length than B's (A:695-701 against B:632-638)". `grep -c` on file 26 finds A:695 0 times and B:632 0 times.
  - Its recommendation ("reword") replaces "Almost everywhere they differ, A does the job better" with "Where they differ, A more often puts a rule on screen…". Line 28 keeps the first-draft sentence word for word (`git show fa9d675`, line 17), although the test held N1 only "in direction".
  - Also missing: A:714, and N20's remark that the "B tells" frame steered the search.
- **Connection:**
  - C1's fifth-time record names the cause: the claim "was checked against the findings the reviewers named, not against the break test itself". This round applied exactly the fourth look's four items and repeated that cause.
  - The owner is told a fifth time that every finding was applied.
- **Verdict:** bears. **Must change.** Apply these findings (at least the line references), or list each one left undone with its reason. Reword line 131, C1 and entry 31 to match, and record this as the sixth time for C1.

## Should change

**V2. Step 4 brings back the fault the third look's R7 found.**
- **Target:** `/home/user/StoryTest/.claude/skills/plot/SKILL.md` line 106: "*surprise* (…: plant, hide, reveal)", with no exemption.
- **Grounds:**
  - The edit restored 35f2939's wording word for word.
  - R7 (`/home/user/StoryTest/.claude/reviews/kept/2026-09-24-build-third-look.md`) named exactly this wording: step 4 "still give[s] every surprise 'plant, hide, reveal'".
  - The fourth look's T9 asked for "plant, hide, reveal" for every surprise, "with section 2's exemption for a bare threat's arrival". The maker's plan says the same.
  - Section 1 (`/home/user/StoryTest/.claude/skills/plot/references/reveals-and-withholding.md` line 16) now carries the exemption. Step 4 does not.
- **Connection:**
  - Walk the theory's own cases down the building route: the bomb that simply goes off (Gap line 59) and the jump scare (Anticipation line 25). Step 4 tells the writer to plant them; section 2 exempts them.
  - This is C12's recorded stage again: a copy was restored without walking the theory's cases through it.
- **Verdict:** bears (a reading corrected before, now back). **Should change.** Add: "except a bare threat's arrival: `references/reveals-and-withholding.md`, section 2".

**V3. The exemption's definition and its telling test give opposite answers.**
- **Target:**
  - reveals-and-withholding.md line 30: "a bare threat's arrival, one that rests on no fact shown earlier…". Then: "The telling test: would a first-time audience make sense of the arrival with no fact they were given? If not, it rests on a fact about the world that needs showing."
  - The copy at `/home/user/StoryTest/.claude/skills/error-correction/references/writing-rules-and-rivals.md` line 9 gives the definition alone.
- **Grounds:**
  - Take the fourth look's F6 dragons away from the climax: dragons never mentioned burn a village in the middle of a story whose world has seemed like ours.
  - They rest on no fact shown earlier, so the definition exempts them. They fail the telling test, so the test does not.
  - Implied World line 20 and Gap line 47 side with the test.
  - F6 named both readings. T15's fix ("no fact shown earlier") took the reading F6 warned against, and F6's own fix added the other as the test.
- **Connection:** two fixes from two reviewers were applied together, and they now contradict each other in one paragraph. A reader who stops at the definition, as the writing-rules copy does, exempts the dragons.
- **Verdict:** bears. **Should change.** Define the bare arrival by the test: one a first-time audience makes sense of from what it already has (the baseline, "the real world plus the habits of the genre", and what the story has shown). Keep T15's point that the unshown bomb is a fact of the story, only not shown.

**V4. The climax clauses stretch Egri's rule without a label, and the skill's own statement of Egri's climax rule says a set-up is not enough.**
- **Target:** reveals-and-withholding.md line 30:
  - "a threat that decides the climax is something the climax uses, which needs its set-up (section 6)";
  - the rescue clause, "needs its set-up like anything the climax uses".
- **Grounds:**
  - Section 6 (line 77) states Egri's rule as "Whatever the climax uses (an object, a skill, a fact) must be known earlier", which means things the characters use.
  - `/home/user/StoryTest/.claude/skills/plot/references/structure-and-conflict.md` line 98 says: "The climax comes from the characters' own acts (Egri *(built)*). An accident, an illness or a rescue from outside proves nothing". Its trap at line 145 says the same.
  - No owner theory speaks of climaxes.
- **Connection:**
  - Calling an outside threat "something the climax uses" is the workshop's stretch, like the rescue stretch beside it. Only the rescue stretch is labelled.
  - Walk a planted outside rescue, or planted dragons that decide the climax. Section 2 is satisfied, while structure-and-conflict says the climax still proves nothing.
  - The diagnosing route for "came from nowhere" (SKILL.md line 123 → sections 2, 3 and 7) never reaches structure-and-conflict section 7.
- **Verdict:** bears. **Should change.** Label the threat stretch as the workshop's reading. Point both climax clauses to structure-and-conflict section 7: a set-up is needed, and at the climax it is not enough.

**V5. The fourth look's T2 is answered only in part: several places still say that anything a commit made without the gate got wrong in the files stops the next commit.**
- **Target:**
  - `/home/user/StoryTest/.claude/skills/error-correction/scripts/recheck_commits.py` note, lines 13–17. It lists "a check loosened" among what "stops every commit until a commit puts it right". T2 named these lines, and they are unchanged.
  - error-correction `SKILL.md` line 118;
  - `/home/user/StoryTest/CLAUDE.md` line 39;
  - `/home/user/StoryTest/README.md` line 89 ("whatever it got wrong in the files stops the next commit");
  - kinds row, `27 Corrections.md` line 28;
  - `check_commit.py` note, lines 20–24.
- **Grounds:**
  - `/home/user/StoryTest/.claude/skills/error-correction/references/checks-and-cases.md` lines 36, 49 and 60, the SKILL.md table (line 228) and CLAUDE.md line 40 now say that a loosened check is judged only by the planted-fault test and its late review.
  - T2's run showed exactly that.
- **Connection:** CLAUDE.md rows 2 and 3 now contradict each other, and the owner-facing README claims more than the scripts do.
- **Verdict:** bears. **Should change.** Add "apart from a loosened check (section 2)" in each place.

**V6. The list "What the gate cannot do" is presented as complete, and it is not.**
- **Target:**
  - checks-and-cases.md lines 46–52;
  - the claims that it is complete: SKILL.md line 118 ("what it does not stop is listed"), CLAUDE.md line 51 ("each listed"), README line 89, S10 at `/home/user/StoryTest/22 Questions - meanings only you can settle.md` line 95 ("the ones they miss are listed"), and the project story line 12.
- **Grounds:** honest mistakes the gate passes, stated elsewhere in the same files but missing from the list:
  - close paraphrase of a book, which no script sees even with the books present (kinds row, line 15; H4 and H19);
  - the receipt is checked for its form only (CLAUDE.md line 41), and an honestly misjudged light receipt passes (reviews-and-briefs line 28);
  - where the books are absent, the Book-text line is the maker's word (CLAUDE.md line 44);
  - a guarded test "retired only with the owner named first" is checked as a name. The kept hand try passed with that line typed by the maker.
- **Connection:** the fourth look (T3, scripts 3) found the same overclaim in the form "one honest route". The owner is again told that a list holds everything the gate misses.
- **Verdict:** bears. **Should change.** Add these items, or write "among them".

**V7. A note can first appear in the output of the very commit it tells the agent to record it in.**
- **Target:** recheck_commits.py lines 36–38 ("copies each into that commit's log entry"); checks-and-cases.md line 38; SKILL.md line 228.
- **Grounds:**
  - In `check_commit.py` lines 294–305, recheck notes print under a "passed" line and never stop the commit. The fourth look's F3 and scripts 8 saw the note under a passing commit, and gone at the next session start.
  - A commit made without the gate that arrives mid-session (a pull of a GitHub edit, a rebase, a cherry-pick) is not shown at session start.
- **Connection:** for such a commit the note is first seen after the commit is already made. "That commit's log entry" is then impossible, and nothing shows the note again.
- **Verdict:** bears, by reading the code and the fourth look's runs; I did not rerun it. **Should change.** Say: after a pull, rebase or cherry-pick, run `recheck_commits.py` before the next commit; a note first seen in a passed commit's output goes into the next log entry.

**V8. The new tripwire sentence contradicts the skill, and it fires on where a stop comes from, not on an error.**
- **Target:** checks-and-cases.md line 54: "If the stop comes from a commit the gate did not approve, that commit put something wrong into the history, which is a tripwire (the skill's 'How much to do')".
- **Grounds:**
  - The section it points to, SKILL.md line 218, says: "These are not tripwires: Anything the gate stops before a commit."
  - The tripwires at SKILL.md lines 209–214 fire when "an error got past the stage meant to catch it".
  - The texts' own honest routes stop for a late receipt: a GitHub squash whose stamp no longer matches (line 54 itself), and a rebase that lands next to an edit made meanwhile (line 40; reviews-and-briefs line 33).
- **Connection:** the skill and the module give opposite answers to the question the fourth look left open (stall (g)). And as worded, an honest squash of reviewed work would need a five-part correction.
- **Verdict:** bears. **Should change.** Scope the sentence to something wrong in the files (a frozen theory edited, a log entry rewritten, a receipt deleted) or a change to a reviewed file with no review at all, and make the matching exception in SKILL.md line 218.

**V9. The plain stop line for a broken gate script never fires in the fourth look's own case.**
- **Target:** checks-and-cases.md line 44 ("if the gate script itself cannot run, pre-commit says so in a plain line"); `/home/user/StoryTest/.githooks/pre-commit` lines 29–31 (`if [ $status -gt 1 ]`).
- **Grounds:**
  - Python exits with code 1 on a syntax error, an uncaught error and a missing module. Three one-line scripts in my folder each printed `exit=1`.
  - In `r5-theory-checker/gatecopy`, a clone of c52f191, I committed a `check_commit.py` with a syntax error while the gate was off, switched the gate on, and tried an ordinary commit.
  - `git commit` exited 1 and printed only the traceback ("SyntaxError: invalid syntax"). `grep -c "COMMIT STOPPED"` on the output printed 0.
- **Connection:** the fourth look's F4 case (a typo that makes a SyntaxError) still gets no pointer to the owner's route, while the text says there is one. The fix was not tried even on the case that found it.
- **Verdict:** bears. **Should change.** Detect a crash (the gate's own result line is missing, or a traceback appears), plant that case, and correct line 44.

**V10. S10's list of where the owner is already asked is incomplete, and does not say that two of those places carry the cost S10 gives against option (b).**
- **Target:** questions file line 95, "Where you are already asked, whatever you choose".
- **Grounds:**
  - Two places that ask the owner are missing from S10's list:
    - checks-and-cases line 38: the owner "decides what to do: look at a change to the gate's files";
    - line 58: when a wrong receipt check, recheck or planted-fault test stops its own correction, "there is no route inside the workshop… tell the owner".
  - S10 turns down (b) because "your yes would be a click on a change you cannot review". Yet its own list has the owner commit a gate-script change that the agent prepared and that is reviewed only afterwards (line 59).
  - "Named first" is checked as a name only (V6).
- **Connection:** the fourth look's T7 asked for these places, and for what each asks of the owner. The owner is choosing between options on this description.
- **Verdict:** bears. **Should change.**

**V11. A light receipt for an "answered" mark leaves the maker alone to judge that a passage follows the owner's answer.**
- **Target:** `/home/user/StoryTest/.claude/skills/error-correction/references/owner-answers-and-revisions.md` line 20, a new sentence.
- **Grounds:**
  - Term sheet line 7: once a question is answered, "the answer governs".
  - Kinds row, line 11: drift from the owner's meaning is the workshop's commonest error.
  - CLAUDE.md rule 1: nobody grades their own work.
  - reviews-and-briefs line 28: a light receipt on a change that alters meaning is a false record.
  - Once the mark is written, the records check stops flagging the passage.
- **Connection:**
  - Whether a stopgap "already follows the answer" is a judgement of meaning. After the mark, the passage reads as the owner's settled meaning.
  - The sentence also rewards leaving "a question put to the owner" beside "answered", which is the fourth look's stall (b) complaint.
- **Verdict:** bears. **Should change.** Have theory-checker compare each marked passage with the owner's words. The review can be short.

**V12. The first half of the trial leaves no trace in the repository.**
- **Target:** project story line 140 (entry 29: "ran during this entry"); line 149; `/home/user/StoryTest/.claude/reviews/kept/2026-09-24-hand-tries.md` line 3.
- **Grounds:** `ls .claude/reviews/kept/ kept-cases/runs/` shows no trial record. The reason for keeping the contents out (the second-half agent would find the answers in its copy) is sound.
- **Connection:**
  - Until the record is kept, "ran" has no receipt.
  - The record lives only in scratch files, which will be lost with the session (C13's error).
  - A fingerprint of the record committed now would prove it later without revealing it.
- **Verdict:** bears for the missing trace; the reason for withholding the contents is sound. **Should change.**

## Minor (each bears unless noted)

**V13. File 26 line 132 is stale.**
- It says "All four rounds' changes are listed", but the note lists five rounds.
- Its account stops at the fourth round and leaves out the fourth look's "weakened", found after its "What remains… assume no order" was written.
- Line 125 still says the section was completed in entry 29, though entries 30 and 31 changed it.

**V14. File 26 line 101: "so its shortness did not come from saving talk".**
- The frame comes from the break test's rival ("a deliberate trim… it did not save talk"). It is the same route by which "still" and "weakened" came in (C1, fourth and fifth times).
- Flip: had A come later, one would write about A's extra length instead.
- Neutral wording: "the difference in length does not lie in the talk of those scenes".

**V15. Copies of changed rules not brought into line.**
- `/home/user/StoryTest/.claude/skills/plot/references/suspense-and-fear.md` line 20: "a surprise buys seconds", unscoped, while section 5 of the same module has *Psycho*.
- writing-rules-and-rivals line 9: "needs no set-up at all", with no climax clause. Its account also stops at the third error.
- `/home/user/StoryTest/.claude/skills/add-source/SKILL.md` line 87: the copying check "reads every .md file". The fourth look's T24 was fixed only in `run_all_checks.py`; `overlap_check.py` reads every file with one of its text endings.
- reviews-and-briefs line 36: "Otherwise the gate refuses the commit" is not true for a book registered in the same commit, since the register is now read from HEAD.

**V16. Records with errors.**
- C15 line 157 and entry 31: "only receipts named by a fingerprint ride with a check change". Under the mixing rule (`check_commit.py` lines 90–91 and 221–222; reviews-and-briefs line 30), the project story, the corrections file, the source register and any file under `.claude/reviews/` may still come with a check change. Only the check-only exception is limited to receipts.
- C15 line 158, "Not tried by a planted test", leaves out scripts 14 and 15. A grep of `test_checks.py` finds no test for either.
- Kinds rows 21 and 22 are out of date in "Seen in".
- C1 line 40 still says "what remains assumes no order (entry 29)", two failures later.
- C5 line 72 says each brief check found "things that had to change (among them, a way round the gate)". In the third brief check the way round was finding 3, a should-change (kept third-look record, line 94).
- Entry 31 line 147 says "three of them made by my last round". The reviewers marked all four faults as new.

**V17. Git behaviour slightly misstated.**
- `.githooks/pre-merge-commit` lines 5–7 and checks-and-cases line 36 list "a plain revert" among commands that run no gate.
- In a scratch repository (git 2.43.0, with a pre-commit hook that logs each run):
  - a revert that stopped for a conflict and was finished with `--continue` printed "PRE-COMMIT RAN";
  - `rebase --continue` after a conflict did not run it;
  - neither a clean revert nor a clean cherry-pick ran it.
- This is harmless.

**V18. "Most recent" means first in git's topological order, not newest.**
- In a scratch repository, A1 (dated 3 January) was merged first and B1 (dated 2 January) second. `git log --topo-order` listed B1 first.
- `check_commit.py` line 131 says "newest first". Say "the one the last merge brought in".

**V19. The hooks-registered check lets narrowed settings through (by reading only).**
- `run_all_checks.py` lines 74–79 and 143 accept any SessionStart matcher, and require only Edit and Write for the frozen-file hook.
- A SessionStart matcher of "resume", or one without MultiEdit, would pass.
- That runs against the check's note (line 20) and CLAUDE.md line 38.

**V20. Checks-and-cases line 49, "the next commit is then judged by the loosened check".** For a loosening made outside the gate, it is the commit after the next approved one; line 60 says this correctly.

**V21. Stall items not answered, with no reason given (use-tester, fourth look, section 3, items 2 and 3):**
- a local squash, which needs a fresh review;
- whether the receipt for a withdrawal may be light;
- no route when a late review passes only part of an outside commit.

**V22. Does not bear yet.** Line 59's "editing the file on GitHub and pulling it in" may be stopped: if the local history has a commit that GitHub lacks, the pull makes a merge, and that merge runs the broken gate script. Settle it by pulling an owner's correction into a local branch that has moved on.

---

## Marks on new or changed rules
- **Section 1, "Plant, hide, reveal" for every surprise, with a pointer to the exemption:** held (Gap line 57 sets no rereading condition).
- **Section 1, "lasts seconds unless it makes the audience reread or breaks a guarantee early":** loose. The module's next paragraph (a surprise that starts new suspense, *Speed*) is a third route. What is held: the unshown bomb (Gap line 59, Anticipation line 41) and *Psycho* (Anticipation line 67).
- **Exemption for a bare arrival:** held for the unshown bomb and the jump scare. Its definition is loose against its own test (V3).
- **Telling test:** held (Gap line 47, Implied World line 20).
- **Climax-threat clause:** held by F6's dragons. It is an unlabelled stretch of Egri *(built)* (V4).
- **Jump scare needs dread first:** held (Anticipation line 84).
- **Guarantee broken early and convincingly:** held (Anticipation lines 67 and 69).
- **Rescue never exempt:** held by an unshown threat's arrival that rescues. For other rescues the main rule already applies, so "every" is harmless.
- **Character reveal never exempt:** held (Bond line 84). Reading the theory's "earning" as a set-up is still the workshop's link, unlabelled.
- **Step 4:** not held on the unshown bomb (V2).
- **The "Surprise by default" trap:** held.
- **Light receipt for "answered":** held if the maker's judgement is right, which is the judgement this workshop has most often got wrong (V11).
- **The tripwire for a stop from an unapproved commit:** loose in scope (V8).
- **The "cannot do" list as complete:** loose (V6).
- **Fingerprint with one neighbouring line:** held for a moved line, with its limit stated.
- **Rivals:** none new.
- **Worked examples:** none new. The grandmother example was dropped. Nothing drawn from a kept case or a trial answer: I searched `kept-cases/` for the new wording; "dragon" appears only in case 06, on departure against breach.

## The earlier findings
- **T1:** answered in text (checks-and-cases, reviews-and-briefs line 30, CLAUDE.md line 40), and C15 records the fourth firing.
- **Answered in part:** T2 (V5), T7 (V10), T9 (V2), T11 (V1), F4 (V9).
- **T3:** answered as pointers, but to a list claimed complete (V6).
- **T4:** answered in text, but not followable mid-session (V7).
- **Answered, with a new fault:** T15 (V3), F6 (V3, V4).
- **Answered, with a copy missed:** T10 (V15), T19 (V13), T24 (V15).
- **Answered:** T5, T6, T8, T12, T13 (hand try kept; the trial is V12), T14, T16, T17, T18, T20 (with a minor point, V16), T21, T22, T23.
- **Use-tester:** F3 as in V7; F5, F7 to F12 answered in text; F13 sound to leave for the rerun.
- **Stall list:** (b) now has a rule, but see V11; (g) is answered in one place only (V8); the rest as in V21.
- **Scripts 3 and 8:** as V6 and V7.
- **Brief check 1 to 8:** all applied in the briefs as sent (kept record lines 23, 34–36, 53–57, 69, 75, 81, 83 and 89).

## The parts the maker left undone
- **No owner approval by hand (scripts 1):** sound, but S10 is incomplete (V10).
- **No planted tests for scripts 14, 15 and 17:** acceptable, but C15 states only 17 (V16).
- **The retirement rule tried by hand:** the record is kept; the gate checks a name only (V6).
- **Copying not rerun on each unapproved commit:** sound as a stated limit.
- **S10 (b):** sound as the owner's choice.
- **Kept-case notes:** sound to leave for the rerun.
- **Counts:** I did not check them.

## Checked and found right
- **Quotations and pointers:**
  - "thought you understood and you were wrong" (Gap line 57) and "real dread" (Anticipation line 84) are word for word.
  - Anticipation Part 2 section 7 (line 79), Bond Part 2 section 7 (line 83), suspense-and-fear section 5 and term sheet section 13 item 9 all land.
  - "Early and convincingly" is restored.
- **The theory's cases, walked through section 2:**
  - the bomb, both ways;
  - the jump scare (exempt, with dread before it);
  - *Psycho*;
  - Joffrey (his death needs no plant; the reveal of the poisoner is a solution and needs its set-up);
  - *Chronicle of a Death Foretold* ("being seen is the point");
  - the Lewton bus (a false alarm, neither a rescue nor a threat's arrival; it passes);
  - "the door dilated" (surplus, not a turn).
- **Agreement with other skills:** the character-reveal clause agrees with character `change-and-growth.md` section 8 and genre `how-genres-work.md` line 125.
- **Machine checks:** `run_all_checks.py --skip-books` on my copy of c52f191 printed "RESULT: no check failed", with the copying check NOT RUN.

## Not checked
- `test_checks.py` and the counts 184 and 16.
- Copying against the book texts.
- Kept cases.
- Real GitHub, Windows, and the hooks in a live Claude Code session.
- The scripts, beyond the lines named above.
- Whether the plan came before the changes.
- The screenplay line references, beyond the kept break test.
- File 26's faults 2 to 5.
- V7 and V19 were checked by reading only.
- A cherry-pick finished after a conflict: I relied on the fourth look's run.

## Side effects
- Nothing written to the live repository.
- My folders under `r5-theory-checker/`: `snap`, `gatecopy` (it holds the broken-gate commit, with the gate switched on inside that copy only), `hooktest`, `topo` and `topo2`, plus three tiny `.py` files and `gate-out.txt`.
- The gate's own temporary copies were removed, and no `/tmp/workshop-*` folders are left.

## Verdict: passed after changes
- **Must change:** V1.
- **Should change:** V2 to V12. V5, V6 and V10 reach the owner.
- **Minor:** V13 to V21. V22 does not bear yet.

These edits then need a look of their own, by a reviewer who did not make them.

## 2. use-tester

# Use-tester, fifth look: edits 018ebd6 to c52f191, walked through the situations in Brief B

**Verdict: passed after changes.** Most of the fourth look's findings are now answered: I walked F1, F2, F5, F7, F8, F9, F11 and F12 and each held. But walking the brief's new situations found honest routes that go beyond the limits the texts state. C15 cannot close while they stand. There are two must-changes:
- the trial's planted problems are in a kept record the build will commit;
- the owner-facing account of what the gate cannot do misses the routes in findings 1, 2 and 5.

**Where things are.** Everything ran in copies under `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/r5-use-tester/`. Full outputs are in its `o-*.txt` files.
- **`base`** is a clone of the live history (HEAD 35f2939) with the c52f191 files committed through the gate. Commit 30fae7f is stamped "approved 4556f36…", printed "passed the planted-fault test brought in", and took 49 s.
- **Before building it,** I compared all 120 tracked snapshot files with the live tree using `cmp`: none differ, and no live file is missing from the snapshot.
- **`w2` to `w20`, `w2p` and `wfresh`** are copies of `base`. GitHub commits, merge-button merges and web edits were simulated with `git -C <copy> -c core.hooksPath=/dev/null …`.
- **Every receipt is SIMULATED,** filled by my helper `fill.py`. No reviewer ran.
- **The copying check** printed NOT RUN everywhere.

---

## 1. Findings

**1. Two sessions that each add a log entry (the same entry number).**
- **Target:**
  - `check_commit.py` lines 130–142 and 225: the checks run against one approved commit only.
  - `check_records.py`: its message "put it back, add a new entry that corrects it".
  - `checks-and-cases.md` line 54: "A rewritten log entry goes back by itself: copy the entry's text from the last approved commit…".
  - The claims:
    - CLAUDE.md line 42: "Old log entries never rewritten … By itself: the records check at every commit";
    - `checks-and-cases.md` lines 46–52, which do not list this route.
- **Defect:**
  - Two sessions branch from the same approved commit, and each adds entry 32.
  - The natural resolution is stopped: keep main's entry 32 and renumber your own. The printed advice ("put it back") would then overwrite the other session's approved entry.
  - The reverse resolution passes, and it rewrites an approved entry already on main.
  - After merges on GitHub, whether the next commit is stopped depends only on which pull request was merged last.
  - A rebase gets through, but no text says so.
- **Grounds:**
  - **Merging main in, natural resolution (`w10`).** Session A's pull request was merged the way the merge button would, then `git merge main` on B, with A kept at 32 and B at 33. It printed "FAILED records … log entry 32 has been changed since 0fd08d8…", then COMMIT STOPPED.
  - **Reverse resolution.** B kept at 32 and A at 33 printed "All checks passed". It was stamped 86bbde4. After B's merge on GitHub, the next session's commit 9a88d8a passed, and main's entry 32 now holds B's text.
  - **Resolved on GitHub (`w12`).** The conflict was resolved on GitHub, A at 32 and B at 33. The next session's first commit printed "note: the last commit the gate approved is 0fd08d8e6 … FAILED records … log entry 32 has been changed since 0fd08d8…".
  - **Rebase (`w12`).** `git rebase` of B, resolved the natural way, then the next commit printed "last commit the gate approved is 55390e837 … passed records", stamped e84115b.
- **Connection:** this is the kinds row "A check or a step that stops honest work, or leaves no way through". It is also a pass while wrong, on a rule CLAUDE.md says is enforced by itself. Following the gate's own advice rewrites another session's entry.
- **Verdict:** bears. **Must change**, at least the claims. Either make the records comparison cover every approved commit that is not an ancestor of the one chosen, or state the route: rebase a session branch onto main when both have added entries. Then list the route in section 2 and scope CLAUDE.md line 42.

**2. An older approved branch merged last takes over the checks.**
- **Target:**
  - `check_commit.py` lines 11–15 and 130–142, with the same logic in `recheck_commits.py` and `session_start.py`.
  - `checks-and-cases.md` line 29: "after a merge made on GitHub … it is the approved commit the merge brought in".
  - CLAUDE.md line 39: "the most recent approved commit by any path".
- **Defect:** "most recent by any path" in `--topo-order` means the tip of the pull request merged last. That tip can be older than the main line's own approved commits. For the next commit, the main line's newer approved checks are skipped, and so are its comparisons: an entry or theory added on main counts as "new".
- **Grounds:**
  - `w11`: `log --topo-order` after two merge-button merges lists B's tip before A's merge. `last_approved_commit` printed 4ca2c87.
  - `w17`: main carried an approved records rule (titles over 60 characters refused). An older approved branch (250a71b) was merged on GitHub afterwards.
  - An entry that rule refuses then printed "note: the last commit the gate approved is 250a71bbc … passed records … All checks passed", stamped 47ed549.
  - `git show HEAD:…check_records.py | grep -c "over 60 characters"` printed 1.
- **Connection:** with parallel sessions this is an honest merge order. It is not among the stated limits, and the stated "loosened check across two commits" does not describe it.
- **Verdict:** bears. **Should change** (one commit's window). Pick the approved commit whose checks are newest, or run every approved tip's comparisons. Otherwise state it. This is mainly the scripts reviewer's area, so I note the connection.

**3. Correcting a wrong machine check, in the ordinary shape of the work.**
- **Target:**
  - `checks-and-cases.md` line 57: "made straight on top of the last approved commit";
  - line 42, and `reviews-and-briefs.md` line 30;
  - `check_commit.py` lines 226–227.
- **Defect:**
  - In the ordinary shape, a session starts on a GitHub merge commit, which is never approved. So a check-only correction on the session branch does not get the exception, and is judged by the wrong check.
  - The route that works is not stated: branch from the last approved commit, correct there, then merge main *into that branch*.
  - The other merge direction is stopped too, because a merge in progress finds the last approved commit only in HEAD's own history.
- **Grounds (`w17`):**
  1. A too-tight rule was approved on a session branch (f09311e, planted-fault test passed) and merged on GitHub. Then the owner added a long-titled entry on GitHub.
  2. Session start printed "FAILING: records … entry 32's title is over 60 characters".
  3. The correction committed on the session branch printed "note: the last commit the gate approved is f09311ef2 … FAILED records … entry 32's title…".
  4. On a branch from f09311e the correction passed as check-only (50e7523). `git merge main` into it passed (a1b5479).
  5. `git merge 50e7523` from the session branch printed "FAILED records … over 60", then COMMIT STOPPED.
- **Connection:** this is the kinds row "leaves no way through" as written. The gate does print the last approved commit's name, which is the only clue.
- **Verdict:** bears. **Should change.** Say how to make the commit on top of the last approved commit when the last commit is not approved, and which way to merge.

**4. The new plain stop line in pre-commit does not appear for a broken gate script.**
- **Target:**
  - `.githooks/pre-commit` line 29 (`if [ $status -gt 1 ]`);
  - `checks-and-cases.md` line 44: "if the gate script itself cannot run, pre-commit says so in a plain line".
- **Defect:** Python exits with code 1 both for a syntax error and for an uncaught exception, so the line never prints for the usual breakages.
- **Grounds:**
  - My probe scripts printed "syntax error exit=1" and "uncaught exception exit=1".
  - `w5`: a one-character typo in `check_commit.py`, committed on GitHub. The next commit printed only `SyntaxError: '(' was never closed`. There was no COMMIT STOPPED line and no pointer, and HEAD was unchanged.
- **Connection:** this is F4's own case, and the plan's answer ("pre-commit prints a plain stop line") does not reach it. The rest of the owner's route works as written: `w5`'s two late receipts, "not passed (withdrawn in 29eca9a)" and "passed", then 9535eb0 stamped.
- **Verdict:** bears. **Should change.** Detect a crash (Python's own report, or no final line from the gate) rather than relying on the exit code.

**5. A clone where git changes line endings (Windows).**
- **Target:**
  - `.gitattributes`, which covers only `sources/**` and `foundations/**`;
  - `session_start.py` lines 97–103 ("Commit gate: on");
  - `check_records.py` lines 362–371 (`folder_fingerprint` reads raw bytes);
  - `checks-and-cases.md` section 2 and the kept-cases README, which say nothing of this.
- **Grounds (`w14`, cloned with `core.autocrlf=true`):**
  - `.githooks/pre-commit` has CRLF line endings. Every commit printed "fatal: cannot exec '.githooks/pre-commit': No such file or directory", with HEAD unchanged, while session start said "Commit gate: on".
  - All six skill fingerprints differ from the LF copy's (both lines printed), and session start lists `hard-to-vary` as owed a rerun. So the typo route can never print a line on such a clone, and a runs.md line written there makes every skill look changed elsewhere.
  - Run directly, the Python checks all passed. Only the shell hooks and the fingerprints break.
- **Verdict:**
  - Bears for a clone with `autocrlf=true`.
  - Does not bear yet for real Git for Windows. The test that would settle it: clone on Windows with the installer's default line endings, make one commit, and run `check_records.py --fingerprints`.
  - **Should change:** `.githooks/* text eol=lf`, and fingerprints read with line endings normalised.

**6. The new tripwire sentence is at odds with the skill.**
- **Target:** `checks-and-cases.md` line 54 ("If the stop comes from a commit the gate did not approve, that commit put something wrong into the history, which is a tripwire…") against SKILL.md lines 217–218 ("These are not tripwires: Anything the gate stops before a commit").
- **Grounds:**
  - `w8`: the owner's one-comma edit on GitHub was stopped for a missing receipt, and a light late receipt cleared it (27b8626).
  - `w8`: a reviewed change rebased next to an edit made meanwhile was stopped for a missing receipt; the recheck printed "no review receipt .claude/reviews/84a188563eb28b70.md".
  - By line 54, each of these needs a full five-part correction. By SKILL.md it is the gate doing its job, and the "How much to do" tripwire list names neither.
- **Connection:** this is the kinds row "a contradiction … no single-skill review can see", and also the trap "Adding process for its own sake". Every honest rebase would become a recorded error.
- **Verdict:** bears. **Should change.** Scope line 54 to what such a commit got wrong in the files: a frozen edit, a rewritten entry, a loosened check.

**7. The instruction to copy each note into "that commit's log entry" cannot be followed as written.**
- **Target:** SKILL.md line 228; `checks-and-cases.md` line 38; the `recheck_commits.py` note, lines 36–38.
- **Grounds:**
  - `w2`: after a mid-session rebase of a reviewed hook change, the note "commit 85f55f066 changed the gate's own files…" first appears inside the passing output of the commit that settles it (`o-w2-rb.txt` lines 23–27). By then that commit's log entry is already staged.
  - The next session start showed nothing: `grep -c "For a person"` printed 0.
- **Verdict:** bears. **Minor.** Say to run `recheck_commits.py` before committing after a rebase, pull or merge, or else to copy the note into the next entry.

**8. The trial's answers are in the build.**
- **Target:** `.claude/reviews/kept/2026-09-24-design-ledger.md` line 52, committed since 1e92459 (entry 29), together with SKILL.md line 164, which tells the loop to search `.claude/reviews/` for earlier corrections.
- **Defect:** the line says: "Problem 1: the reversed villain ladder re-planted, with one restatement elsewhere, and the owner's sign 'the villain ladder reads the theory backwards'. Problem 2: the owner answers Q1 with option (a)". It hands the second-half agent three things:
  - that the problems are planted;
  - where the answer is ("one restatement elsewhere");
  - both inputs.
- **Grounds:** the hand-tries note (line 3) kept the first half out of the repository for exactly this reason. A search for "planted problem" and "Q1 with option" finds only this record.
- **Verdict:** bears. **Must change before the trial's second half runs.** The record is kept word for word, so give the trial agent a copy without `.claude/reviews/kept/`, or run it from a commit that lacks this file.

**9. The Book-text rule's reader misses McKee.**
- **Target:** `review_receipt.py` line 190: `^\| ([A-Z][a-z]+ [A-Z][a-z]+),`.
- **Grounds:** `book_authors` printed `['John Truby', 'Lajos Egri']`. "Robert McKee" does not match.
- **Connection:** today every skill file naming McKee also names Truby or Egri (my search printed none naming McKee alone), so nothing slips through now. A module drawing on McKee alone would. This is older than these edits.
- **Verdict:** bears. **Minor.**

**10. Owner answers: the "answered" mark leaves passages that contradict themselves.**
- **Target:** `owner-answers-and-revisions.md` line 20.
- **Grounds (`w19`, Q3 answered):**
  - Following the text left "is a question put to the owner (Q3, answered 24 Sep: option b)" in two modules, and "**Open:** Q3 (answered 24 Sep: option b; …)" in the term sheet.
  - All of it went through on a light receipt (57df04e).
  - The same step also says "the kept cases for its skill are rerun", which disagrees with the typo route for a change said to alter no meaning.
- **Verdict:** bears. **Minor.**

**11. A copy not brought into line.**
- **Target:** `reviews-and-briefs.md` line 32 gives two of the three withdrawal conditions. It lacks "can no longer be undone from the files", which `checks-and-cases.md` line 54 and the recheck have.
- **Verdict:** bears. **Minor.**

**12. Session start prints noise as failures.**
- **Target:** `session_start.py` lines 170–174.
- **Grounds:** `w17` and `w20`: after "FAILING: records …" it prints "*Updated 24 September 2026.*" and the status lines. These are the "entry N is new" note's own lines, not failures.
- **Verdict:** bears. **Minor.**

**13. Kept case 04.**
- **Target:** the Psycho guarantee wording, now in three places: `reveals-and-withholding.md` line 16 (new) and line 30, and the SKILL.md trap at line 164 (new).
- **What it matches:** case 04, "The lead shot dead in chapter three", aimed at H14 ("if anyone can die at any moment, care collapses"). The wording tells the same story (the apparent lead killed early) and reaches the conclusion the case protects ("broken early and convincingly … makes every later threat real").
- **Why it is not simply an answer key:** it is the theory's own case and words (Anticipation line 67, "After that, no guarantee holds and every threat is real"; line 69, "Break one guarantee convincingly"; term sheet 1.2). The new part is that it now sits in the SKILL.md trap, which every plot session reads.
- **Verdict:** does not bear yet. The test that would settle it: rerun case 04 on the committed plot and genre skills, and grade whether the answer's route goes through the theory line or echoes the trap. **Minor.**

---

## 2. The earlier findings in my area

| Item | Answered? | What I ran |
|---|---|---|
| F1 | Yes | `w2` `git merge --no-ff -m` of a reviewed hook change: "passed the last approved commit's planted-fault test", stamped 35eef3e. `w2p` `git pull --no-rebase`: passed, stamped 405c0da. |
| F2 | Yes, rebase included | `w18`: a retirement plus the changed test (1 m 48 s); rebased; the next commit printed "retired in a receipt: maps: …", stamped fe6b8ec. |
| F3 | In text only | Finding 7. |
| F4 | In part | Finding 4. The route itself works (`w5`). |
| F5 | Yes | `w20`: session start printed `git checkout 30fae7fb… -- …`. |
| F6 | Yes | Walked below. |
| F7, F8 | Yes | `w20` and `w16`: the approved checks are compared with the approved commit. Noise: finding 12. |
| F9 | Yes | `w20`: entry 12 restored and the owner's entry 32 kept (`grep -c` printed 1); stamped 32b25af. |
| F10 | Yes, in text | Finding 3 is a residue. |
| F11 | Yes | Finding 11 is a new drift. |
| F12 | Yes | Anticipation Part 2 section 7, line 84. |
| F13 | See finding 13 | The grandmother example is gone (`grep` found nothing). |
| Scripts 1 | Yes for the gate-script route (`w5`) | Finding 4. |
| Scripts 2 | Yes (`w8`) | New residues: findings 1 and 2. |
| Scripts 3 | In part | The list omits findings 1, 2 and 5. |
| Scripts 5 | Yes (`w18`) | |
| Scripts 8 | In text | Finding 7. |

**The fourth look's stall items:**
- The owner-first hint in the form: answered.
- The kept-case note says "which is answered" while Q3 is "rechecking": still there (`w19`).
- Whether a withdrawal's own receipt may be light: still unsaid.
- How to withdraw only the failing part of an outside commit: still no route.
- A jump scare in prose: still not reached from the set-up route.

---

## 3. Stall list, per situation

1. **A GitHub edit to a frozen theory and to entry 12 (`w20`).**
   - Followable, and stamped.
   - Finding 6: whether this is a tripwire.
   - If the owner meant to revise their own theory, the text says only "put it back". Only the printed message mentions add-source.
2. **Rebase, cherry-pick, squash (`w2`, `w8`).**
   - A rebase of a hook change is fine, apart from finding 7.
   - A rebase next to an edit needs a new review, as stated.
   - `git merge --squash` asked for a receipt for the combined change, consistent with the text.
   - `git rebase --continue` after a conflict ran no gate, which is consistent (the text names only cherry-pick and merge).
   - The cherry-pick itself was not run separately.
3. **A late review that fails (`w8`).** Works (734a387). The withdrawal receipt's weight, light or full, is unsaid.
4. **A wrong check.**
   - Put back after an outside break (`w16`): works (8969975). Session start said "none failing" although the next commit would fail the planted-fault test.
   - Approved: finding 3.
   - The gate script: findings 4 and 6.
5. **Retiring a test:** works.
6. **The owner answers Q3; typos:** followable (`w19`), with finding 10. The genre typo line updated only genre. The plot refusal said what to do.
7. **Plot walks** (building route: step 4 to section 1 to section 2; diagnosing route: the row "the twist came from nowhere" to sections 2, 3 and 7):
   - **A twist's clue** ("my mentor-cop planted the evidence against her father; readers say it came from nowhere; my only clue is that he always volunteers for the evidence room"). The rule fires: this is a character reveal, which is never exempt, so it needs a set-up the story has earned; keep the showing light. This agrees with Bond line 84: "It breaks when they do something that contradicts who they've been without the story earning it". Character skill section 8 agrees.
   - **A jump scare** (a cat from a wardrobe). The exemption fires: no set-up, but fear first. This agrees with Anticipation line 84. Stalls:
     - SKILL.md step 4 now says "plant, hide, reveal" for every surprise, and the exemption is only in the module;
     - the medium point (prose) is not reached.
   - **Near neighbour:** an avalanche that kills the villain at the climax, "a pure shock". Stays quiet, since it is a rescue or solution, never exempt. Right.
   - **The telling test.** Its "If not" branch names only a world fact; a story fact (a jilted man arriving) is covered only by the general check. Whether genre knowledge counts as "a fact they were given" is not said.
   - **The climax clause.** "a threat that decides the climax is something the climax uses" stretches Egri's rule, but only the rescue stretch is labelled as the workshop's reading. For theory-checker. Walking Gap line 59's unshown bomb at a climax, a light set-up can keep the surprise, so I found no contradiction with a theory line.
   - **The theories' own cases, all consistent:** the bomb, shown or not; Joffrey (a rescue for Sansa, and the poison is planted); *Psycho* (the shower is bare, "Mother" is planted); *Chronicle* ("being seen is the point", Anticipation line 47); "the door dilated". Every pointer lands: Bond Part 2 section 7 (line 84) and Anticipation Part 2 section 7 (line 84).
8. **The ordinary shape (`w8`).**
   - The session branch was stamped.
   - The GitHub merge commit (2492f3e) carries no stamp. Session start found c5633ff through it.
   - The web edit needed a light late receipt, and the next commit was stamped (27b8626).
   - Stalls: finding 6, and the typo route cannot be used for an edit already committed on GitHub.
9. **A rebase next to an edit; the owner's gate-script route:** as above.
10. **Situations nobody walked before.**
    - A new owner theory in one commit: works (28a20de).
    - A new book: the Book-text line is demanded anyway, because every craft file names Truby, Egri or McKee, so reading the register from the last commit opens no reachable gap today (see finding 9).
    - Two sessions' branches: findings 1 and 2.
    - A settings edit adding a permission list: check-only, 59 s, stamped.
    - Windows: finding 5.
11. **The trial:** finding 8.
12. **The owner asks whether the gate can be trusted.** CLAUDE.md line 51, SKILL.md line 118, section 2 and S10 would have an agent answer:
    - it stops most honest mistakes;
    - it misses five listed routes;
    - only S10 or the owner catches everything.

    Before that goes to the owner it must add findings 1, 2 and 5, and drop section 2's "pre-commit says so in a plain line" (finding 4).
13. **Near neighbours, all quiet:**
    - a fresh clone's session start: 0.47 s, gate on, nothing flagged;
    - ordinary commits throughout;
    - `git merge -m` of two note branches: stamped b17f594.

## Not tested
- Real GitHub, real Windows, or a live Claude Code session.
- `test_checks.py` counts (Brief C's).
- The bypass hook's spellings.
- A gate script approved by the gate and then found wrong.
- `git am`, worktrees.
- The copying check with the books present.
- No kept case was run; I read only their titles and "Aimed at" lines.

## Side effects
None in the live repository. HEAD is 35f2939, `git status --short` shows 30 entries as at the start, `core.hooksPath` is unchanged, and there are no `/tmp/workshop-*` folders.

## Verdict: passed after changes
- **Must change:**
  - 8: keep the design ledger's trial line out of the trial agent's copy.
  - 1: put right, or state in section 2 and in CLAUDE.md line 42, the parallel-entry route. Also state findings 2 and 5 in section 2 before the owner is told the gate can be trusted.
- **Should change:** 2 to 6.
- **Minor:** 7 and 9 to 12.
- **Does not bear yet:** 13, and 5 on real Windows.

## 3. scripts and hooks (a general-purpose agent)

# Fifth look at the scripts and hooks (edits 018ebd6 to c52f191), 24 September 2026

**Overall: not passed.** The maker's counts are right: 184 planted tests, all passing on the new scripts, and 16 failing on the scripts the fourth look saw. Most of the fourth look's findings are answered in content, and I tried several of them through the real gate. There are two must-changes:
- **1.** A commit made with `git commit -a` or `git commit <file>` lets an edit to a frozen theory through, and the commit gets the gate's stamp. This is older than these edits, but no earlier reviewer found it.
- **2.** After a merge made on GitHub that joins two approved branches, the gate compares everything with the merged-in branch's side. That stops honest work, it accepts a rewrite of a log entry already on the main line, and it drops a check the main line had tightened and approved. This came in with these edits.

Five findings should change and eight are minor.

**Words used below.**
- A **stamp** is the line "Workshop-gate: approved <tree>" that the gate adds to a commit it passes.
- The **last approved commit** is the commit the gate takes its checks from and compares the files with.
- The **staging area** is what `git add` marks for the next commit. Git calls it the index.
- A **check-only commit** is a commit made straight on top of an approved commit that changes only checks, plus receipts.
- The **planted-fault test** is `test_checks.py`, and the **recheck** is `recheck_commits.py`.
- A **GitHub merge** is a merge commit made on GitHub, which has no gate. I made these in copies with the gate off.

**How I worked.**
- I read the brief's shared part and Brief C, the fourth look's kept reports and plan, and the diff. I read no other scratchpad file.
- I made no edits and no commits in `/home/user/StoryTest`. At the end its HEAD was still 35f2939, `git status --short` still showed 30 entries, and there were no `/tmp/workshop-*` folders.
- All copies are under `.../scratchpad/r5-scripts/`.
  - `base` is a clone of the live history with the c52f191 files committed through the gate. That commit printed "the planted-fault test brought in … All checks passed" and is stamped "approved d981267…". I checked beforehand with `diff -rq`: the live tree matches c52f191 apart from an empty `cases/` folder.
  - `e1` to `e15` are copies of `base`, made with `mk.sh`.
- Every receipt in my copies is a **simulated** stand-in written by my `fill.py`. No reviewer ran.
- TMPDIR pointed inside `r5-scripts`. No book text was copied.

## The counts (tests I ran, on which scripts)

- **New `test_checks.py` on the c52f191 scripts** (`t-new`, from `git archive c52f191`): "TOTAL tests: 184, failed: 0", in 280 s. No test was listed as not run.
- **New `test_checks.py` on the 018ebd6 scripts** (`t-old`, `git archive 018ebd6` with the new test file put in): "TOTAL tests: 184, failed: 16", in 269 s. The 16:
  - both "hooks registered" faults;
  - the large record once its contents change;
  - the check-only commit loosening the receipt check;
  - the check change carrying anything but a receipt;
  - the pull neighbour;
  - the reordering claimed as withdrawn;
  - the moved line;
  - the retirement after a merge, and after a rebase;
  - both GitHub-merge tests;
  - the merge through the real stage;
  - the planted-stage test;
  - the two new hook commands.
- Three new tests pass on the old scripts too, so they show nothing about these edits: the entry-29 indented rewrite, the hooks neighbour, and the Windows line-endings neighbour. All three are guards or neighbours.
- So I confirm the maker's counts in C15, entry 31 and the status line.

## Must change

**1. With `git commit -a` or `git commit <file>`, the frozen check reads the wrong staging area. An edit to a frozen theory passes and is stamped. A real withdrawal is stopped. Older than these edits.**
- **Target:**
  - `check_commit.py` lines 106–110: `environment_for_copies` drops every GIT_ setting, GIT_INDEX_FILE included.
  - `check_commit.py` lines 268–273 and 297–299: `run_all_checks.py` and the recheck get that environment.
  - `run_all_checks.py` passes `--index`, so `check_frozen_files.py` lines 104–107 and 159–165 read the frozen files from git's staging area.
  - The same cause in `recheck_commits.py` line 78, with lines 142–166 (a claimed withdrawal is compared with the staging area).
  - The claims this breaks: CLAUDE.md line 38 ("the fingerprint check at every commit"), and `checks-and-cases.md` line 54 ("A frozen file goes back as the last approved commit has it").
- **Defect:**
  - For `commit -a` or `commit <file>`, git builds the commit in a temporary staging area, and tells hooks where it is through GIT_INDEX_FILE.
  - The gate's copy of the files uses that area. The frozen check and the recheck run without it, so they read the ordinary staging area, which does not hold the change.
- **Grounds:**
  - **e1.** `sed` added " (edited)" to line 3 of `sources/bond-theory.md`, then `git commit -a`. It printed "passed frozen files … All checks passed; committing.", and the commit was stamped "approved 0d569fb…".
  - **Control (e1c).** The same edit staged with `git add` printed "FAILED frozen files … frozen file has changed".
  - **e1p.** `git commit -m … -- sources/bond-theory.md` also passed, and was stamped.
  - **The next commit in e1** printed "FAILED frozen files … put it back as 8c2666066 has it (git checkout 8c2666066 -- 'sources/bond-theory.md')". 8c2666066 is the approved commit that holds the edit. Running that command changed nothing, and the next try printed the same stop. Session start prints the same advice.
  - **e7.** `git revert --no-commit` of a commit made outside the gate, plus a late receipt "not passed (withdrawn in this commit)", then `git commit -a`. It printed "FAILED earlier commits … its receipt says the change was withdrawn, but it is still in .claude/skills/plot/SKILL.md; take it out (git revert --no-commit 753044a01…)". The same files staged with `git add` passed.
  - **On the 018ebd6 scripts (`old-a`)**, the `-a` frozen edit also passed and was stamped "approved 96f55b3…".
- **Connection:**
  - Kinds rows "An edit to a frozen text" and "A check that passes while the thing is wrong", reached with the most ordinary git command.
  - Once stamped, the edit sits in the last approved commit, so the printed way back restores the edited text.
  - The withdrawal case is the row "A check or a step that stops honest work".
- **Proposed change:**
  - Give `run_all_checks.py` and the recheck the commit's own staging area (GIT_INDEX_FILE made absolute, or an explicit option), or have the frozen check read the gate's copy.
  - When an approved commit already holds a changed frozen file, name a commit where the file still matches its list line.
  - Plant `commit -a` and `commit <file>`, both for a frozen edit and for a withdrawal.
- **Verdict:** bears. **Must change.**

**2. After a GitHub merge of two approved branches, the gate takes the merged-in side as the last approved commit, whatever its age. New in these edits.**
- **Target:**
  - `check_commit.py` lines 130–142: `git log --topo-order`, and the first stamped commit wins.
  - `check_commit.py` lines 244–251: the note.
  - The same choice in `recheck_commits.py` lines 102–107 and `session_start.py` lines 67–78.
  - The claims:
    - `check_commit.py` lines 11–24: "most recent"; "a changed check takes effect only once a commit carrying it has been approved"; "whatever they got wrong … stops this commit";
    - CLAUDE.md line 39;
    - SKILL.md line 118;
    - `checks-and-cases.md` line 29;
    - the project story's word list, line 77 ("the most recent commit, by any path").
- **Defect:**
  - In git's topological order (children before parents), after a merge, the commits of the branch merged in (the second parent) are listed first. So the reference is whatever approved commit that side holds, and the main line's approved commits count as "not approved".
  - Two effects follow:
    - log entries renumbered when a conflict is resolved are judged against that side only;
    - checks tightened and approved on the main line are not used.
- **Grounds:**
  - **e3.**
    - Sessions X and Y each added entry 32 on their own branch, and each commit was approved.
    - On main, with the gate off as on GitHub, I merged X, then Y. I resolved the conflict the natural way: X's entry stays 32, Y's becomes 33.
    - The next gated commit printed "note: the last commit the gate approved is f3f88e980 [Y1]; the 3 commit(s) after it were not approved by the gate", although X1 among them is approved. It then printed "FAILED records … log entry 32 has been changed since f3f88e98…".
    - A check-only commit there got no check-only note, and the same stop.
    - The only way through I found was to rewrite main's entry 32 so that Y's text is 32 and X's is 33. Then the gate printed "All checks passed; committing." It had accepted a rewrite of an entry that approved X1 had put on the main line.
  - **e8.**
    - Y1 was approved on a branch from the base. On main, a check-only commit A1 lowered `LARGE_TEXT` to 90,000 and was approved (51 s).
    - Then came a GitHub-style merge of Y, and a web edit adding a 95,040-byte text under `kept-cases/runs/`.
    - The next gated commit printed "note: the last commit the gate approved is 7c0d5cb72 [Y1]; the 4 commit(s) after it were not approved", then "passed no book files" (Y1's 100,000 limit).
    - It then printed "FAILED the last approved commit's planted-fault test … TOTAL tests: 182, failed: 26, not run: 2", with the advice to name tests under "## Tests retired".
    - The large file is never named at the top. The stop happens only because each planted copy carries it.
  - The planted test for this change ("after a merge made as GitHub makes one…") starts from `copy_repository(stamped=False)`, so it has only one approved side.
- **Connection:**
  - Kinds rows "A check that passes while the thing is wrong" and "A check or a step that stops honest work, or leaves no way through".
  - "Most recent" is false: Y1 was made before A1.
  - Scripts finding 2 is answered for one session at a time; this is the new error its fix made.
- **Proposed change:**
  - For the log: every entry of every approved commit the merge joins must survive word for word, and an entry added on one side may be renumbered after the other side's.
  - Take the checks from the side with the newest approved checks, and name it in the note.
  - Count only unapproved commits in "N commit(s) after it".
  - Plant two approved session branches merged on GitHub, in either order, and a stale branch merged after a check was tightened on main.
  - Until then, list this in section 2.
- **Verdict:** bears. **Must change.**

## Should change

**3. On a copy where git changes line endings (`core.autocrlf=true`, the Git for Windows default), the gate's shell scripts cannot run, and every commit is stopped. Older than these edits.**
- **Target:** `.gitattributes` lines 1–5 keep line endings only under `sources/` and `foundations/`; the three `.githooks/` scripts; section 2 of `checks-and-cases.md`, which is silent on this.
- **Grounds:**
  - **e5** is a clone made with `-c core.autocrlf=true`. `git commit` printed only "fatal: cannot exec '.githooks/pre-commit': No such file or directory", and no commit was made. The file's first line reads `#!/bin/sh\r`.
  - Run through `sh`, the same file printed `Syntax error: "elif" unexpected (expecting "then")`, exit 2.
  - With only the hooks kept to Unix line endings (a local `.git/info/attributes` line), the same commit passed.
  - On that copy, the large record was 160,703 bytes with Windows line endings, and `allowed_large_record` returned True. So the exemption bound to a fingerprint holds, as the brief asked me to check.
  - Only on that copy, the kept-case note also listed hard-to-vary, because skill fingerprints are read from disk bytes.
  - Not tried on Windows itself.
- **Connection:** "A check or a step that stops honest work, or leaves no way through". Session start switches the gate on, and no text names the cause.
- **Proposed change:** add `.githooks/** text eol=lf` (and consider the scripts and skills) to `.gitattributes`, and plant an autocrlf copy.
- **Verdict:** bears. **Should change.**

**4. The fix for scripts 17 exempts a book registered in the same commit, which is the add-source skill's own "one commit per source" path.**
- **Target:** `review_receipt.py` lines 180–191; add-source SKILL.md lines 43 and 95.
- **Grounds:**
  - **e11.** One staged change registers "Marian Placeholder, *A Made-Up Book on Endings*" and adds a plot module crediting Placeholder. The receipt's Book text still holds its hint, and the books are absent.
    - The new `review_receipt.py check` printed "review receipt: … is complete".
    - 018ebd6's `review_receipt.py check` on the same files printed "say in 'Book text:' what book text the change adds".
  - Also, on the real register `book_authors` returns only ['John Truby', 'Lajos Egri']. The pattern `[A-Z][a-z]+ [A-Z][a-z]+` cannot read "Robert McKee" (line 190; older). This is hidden today only because every file naming McKee also names Egri or Truby.
- **Connection:** "A change (a fix) that makes a new error". The maker left 17 unplanted. A neighbour planted for add-source's path would have caught this.
- **Proposed change:** count an author named in either the last approved commit's register or the staged one; let the pattern read names like McKee; plant both.
- **Verdict:** bears. **Should change.**

**5. The new plain stop line in pre-commit never appears for a broken gate script, which is F4's own case.**
- **Target:** `.githooks/pre-commit` lines 29–31 (`[ $status -gt 1 ]`); `checks-and-cases.md` line 44 ("if the gate script itself cannot run, pre-commit says so in a plain line").
- **Grounds:**
  - **e2.** A one-character typo in `check_commit.py` was committed outside the gate. The next `git commit` printed only "SyntaxError: '(' was never closed", with exit 1 and no plain line.
  - Python exits 1 for any uncaught error, the same code as a failed check.
  - `test_checks.py` holds no test for this line.
- **Connection:** the text now claims more than the script does. `checks-and-cases.md` section 3 asks for planted faults for every new check.
- **Proposed change:** print the line whenever the gate's output lacks its own final line, or holds a Python error report; plant a broken gate script.
- **Verdict:** bears. **Should change.**

**6. The new "hooks registered" check passes when all hooks are switched off.**
- **Target:** `run_all_checks.py` lines 130–149 and its note (lines 20–25); CLAUDE.md line 38 ("the checks make sure the settings still register it").
- **Grounds:** I called `hooks_not_registered` directly on edited copies of `settings.json`:
  - `"disableAllHooks": true` added: passes;
  - the edit hook's matcher set to `.*` (a pattern covering every tool) or `Edit.*|Write`: "no PreToolUse for Edit hook runs …", a false alarm;
  - a permission list added: passes, which is right.
- **Connection:**
  - "A check that passes while the thing is wrong". `disableAllHooks` is one of Claude Code's settings, and the update-config skill could write it on an honest request.
  - `.claude/settings.local.json` and the user's own settings can do the same, where no check in the repository looks. That limit is not stated.
- **Proposed change:** fail on `disableAllHooks`; read the matcher as a pattern; state the local-settings limit; plant `disableAllHooks`.
- **Verdict:** bears. **Should change.**

**7. The routes for a wrong check: the check-only route cannot be taken after a GitHub merge, and "tell the owner" leaves the owner nothing to do.**
- **Target:** `check_commit.py` lines 226–228 (the last commit itself must be approved); `checks-and-cases.md` lines 56–60.
- **Grounds:**
  - e3, above: after GitHub merges, the check-only commit was judged by the old checks.
  - By reading: the receipt check, the recheck and the planted-fault test always come from the last approved commit, and a commit made outside the gate never becomes one. So if one of them stops every commit, an owner's commit on GitHub changes nothing. Only two things help:
    - the owner editing `check_commit.py` itself;
    - taking the branch back to before the approved commit that brought the fault in, which loses later work.
  - A way through for the check-only route exists, but no text gives it. It is untried: branch from the last approved commit, correct the check there, merge main into that branch through the gate, then fast-forward.
- **Connection:** on the parts left undone, the reason for building no hand approval is sound. The text past "tell the owner" is not: every new session starts after a GitHub merge, which closes the route the text gives first.
- **Proposed change:** state the owner's real options and the route after a GitHub merge. Or count a GitHub merge that holds nothing beyond the automatic merge of approved parents as approved.
- **Verdict:** bears. **Should change.**

## Minor (each bears)

- **8. Shallow clones.** A clone of depth 1 whose tip is a GitHub merge printed "no commit in the history carries the gate's stamp" (e9), and the old rule applied. Section 2 does not list this. The live repository is not shallow (`--is-shallow-repository` printed false).
- **9. A "passed" that hides tests not run.** On a pass, the gate's "passed … planted-fault test" line hides the two tests left out inside it. The count "not run: 2" shows only on a failure (e8 against e10).
- **10. The recheck's book note ignores the allowed large record** (`recheck_commits.py` lines 169–176). A rebased or squashed build commit would be reported to the owner as "looks like a book file". By reading only.
- **11. Refusal hook gaps** (`refuse_check_bypass.py` lines 140–143). `git config core.hooksPath '$PWD/.githooks'` in single quotes (git keeps "$PWD" as written, so no hooks run) is let through, and so is `cd .claude && git config core.hooksPath "$PWD/.githooks"`. My 50 commands, fed through `hooktry.py`, gave no new false refusal compared with 018ebd6.
- **12. The stamp note overclaims.** `prepare-commit-msg` lines 51–52 say "gets no stamp". Within two minutes of a gate run that made no commit, `git commit --no-verify --allow-empty` got "approved d981267…"; after 3 minutes it got none (e12). The contents were the same, so no harm, but the note should say "within two minutes".
- **13. The old ".md" wording remains beside T24's fix.** add-source SKILL.md line 87 and `overlap_check.py` line 120 still say the copying check reads ".md" files. T24's fix changed only `run_all_checks.py`'s note.
- **14. The receipt tests are still one group** (`test_checks.py` line 509). A planting failure there still reads "receipt_tests could not run" and can never be retired. The plan said each test would run on its own. Finding the form by its path removes only the case e1 found.
- **15. Session start's excerpt of a failing check** includes "skipped on request (--skip-books)" as if it were part of the failure (e1).

## The findings listed for me

- **Scripts 1:** answered in part. The form is found by its path, and the texts say what each route clears. See 7 and 14.
- **Scripts 2:** answered for one session at a time (planted, and the test fails on old); the new fault is 2.
- **Scripts 3:** section 2's list is incomplete. It lacks 1, 2, 3, 8 and the local-settings part of 6.
- **Scripts 4 and F1:** answered. In e10 a gated merge that brought in a check change printed "passed the last approved commit's planted-fault test" and was stamped.
- **Scripts 5 and F2:** answered through the real gate (e10). After a rebase, and after a merge, it printed "retired in a receipt: maps: a description over the length limit".
- **Scripts 6:** answered (planted).
- **Scripts 7:** answered in part (6).
- **Scripts 8:** answered as text, on trust.
- **Scripts 9:** answered for reorders; see 1 for `commit -a`.
- **Scripts 10 and T8:** answered. One paragraph placed in three sections gave three fingerprints.
- **Scripts 11:** answered (e6).
  - A pull of a reviewed commit passed and was stamped.
  - A pull of an unreviewed web edit printed "no review receipt … review_receipt.py new --commit 6214fbc75".
- **Scripts 12:** answered (planted).
- **Scripts 13:** answered; it holds with Windows line endings too.
- **Scripts 14:** answered, not planted. In e14 the printed `git checkout 0cc57a863 -- <receipt>` worked.
- **Scripts 15:** answered, not planted (12).
- **Scripts 16:** answered, with two more gaps (11).
- **Scripts 17:** answered for dropping a row; a new hole (4).
- **Scripts 18:** answered. e15 printed "NOT retired (it guards the workshop, so the owner must be named first as reviewer): records: hidden text in the log".
- **T1:** answered (planted, fails on old).
- **T21:** the form's hint is fixed; "most recent" is still not what the code does (2).
- **T22:** answered.
- **T24:** answered in `run_all_checks.py`; the copy elsewhere is not (13).
- **F4:** not answered for its own case (5).
- **F5:** answered, except after a `-a` commit (1).
- **F7 and F8:** answered. Session start ran the approved commit's checks, and printed the failing line (e1).

## The maker's parts left undone

- **No hand approval:** the reason is sound, but the text is incomplete (7).
- **No planted tests for 14, 15 and 17:** I tried all three by hand. 14 and 15 work. 17 made finding 4, so the reason for leaving it unplanted does not hold.
- **The owner rule for retiring a guarded test:** I tried the refusal side (e15), and it works.
- **The copying check not rerun on each unapproved commit:** sound as a stated limit.
- **S10 (b):** the owner's choice.
- **Kept-case notes:** not my area.
- **Counts:** confirmed.

## Not checked

- Real GitHub, Windows, macOS, and a live Claude Code session. I fed the hooks JSON input the way Claude Code would.
- The copying check with real books; it printed NOT RUN everywhere.
- `git am`, octopus merges, a `git pull --rebase` that stops for a conflict, and `git merge --squash`.
- The owner-named retirement on the passing side (the maker's hand try, not rerun).
- The unchanged files: `after_commit.py`, `protect_frozen_files.py`, the add-source scripts and `run-kept-cases.js`.
- The way through proposed in 7.

## Side effects

- Nothing was written to the live repository.
- The old-scripts test run left four `workshop-test-*` folders in `r5-scripts/tmp-old`.

## Verdict: not passed

- **Must change:** 1 (the `commit -a` and `commit <file>` staging area) and 2 (the last approved commit after a GitHub merge of two approved branches).
- **Should change:** 3 to 7.
- **Minor:** 8 to 15.

The edits made for these need a review of their own.

## 4. copy-checker

Copy-checker report: fifth look, the plot skill's book-derived text (Brief D)

What I looked at. The edits are `git -C <snapshot> diff 018ebd6 HEAD -- .claude/skills/plot/`, with HEAD at c52f191. They are two hunks in each of two files. Both files match the live repository (checked with diff -q).
- /home/user/StoryTest/.claude/skills/plot/references/reveals-and-withholding.md, line 16 (section 1, the Surprise bullet) and line 30 (section 2, the set-up paragraph).
- /home/user/StoryTest/.claude/skills/plot/SKILL.md, line 106 (step 4) and line 164 (the trap "Surprise by default").

Section 6 did not change in this range, although the brief names it. I read it against Egri anyway, because the new line 30 now leans on it.

The book text is present: `ls sources/raw/*.txt` listed Egri, *The Art of Dramatic Writing*; McKee, *Dialogue*; and Truby, *The Anatomy of Story* and *The Anatomy of Genres*.

Runs and what they printed:
- **8 words and 6 words:** both changed files against all four books, run in the snapshot. Every run printed "TOTAL problem spans ... 0", exit 0. The 6-word runs used `--run-length 6`, because the `N=6` form does not work (see D1).
- **5 and 4 words, changed lines only:** the lines were fed to the script through a pipe, so no file was written.
  - One 5-word string of everyday words, shared with Egri. It sits in the unchanged part of step 4.
  - Three 4-word strings of common words, shared with the two Truby books.
  - None of these is distinctive wording.
- **Whole snapshot tree, 8 words:** `overlap_check.py <book> .` for all four books printed 0 problem spans each. Every reported span was marked allowed (a title).

Copying findings (step 2, the side-by-side reading)

C1.
- Target: reveals-and-withholding.md line 16, the rewritten Surprise bullet.
- Defect looked for: close paraphrase, or a book's order of points.
- Grounds:
  - The bullet's sources are the owner theories: gap-theory-of-narrative.md lines 57 and 59, and anticipation-theory.md Part 2 section 5 (line 67), which has *Psycho* and the broken guarantee.
  - The only book that uses *Psycho* is Truby, *The Anatomy of Genres*, Horror chapter (raw line 310), and it uses it for a different point: the killer as the central character.
  - A search of 40-word windows found no passage in any of the four books that has plant, hide (or conceal) and reveal together. It printed 0 for each book.
- Connection: the new wording follows the owner theories, not a book.
- Verdict: does not bear.

C2.
- Target: reveals-and-withholding.md line 30, the changed sentences: the bare arrival, the "telling test", the dread, the *Psycho* guarantee, the rescue clause, and the character reveal.
- Defect looked for: close paraphrase.
- Grounds:
  - "Real dread" is from the Anticipation theory, Part 2 section 7 (line 84). The guarantee is from its section 5 (line 67).
  - The character-reveal clause is from the Bond theory, Part 2 section 7 (line 84). It is close to the owner's own sentence, but that is the owner's theory, not a book, and it is cited.
  - The nearest book passage is Egri, chapter 9, Transition (raw line 2065), on Nora. It argues something else (gradual transition), and the workshop's text does not follow it.
  - The telling test has no counterpart that I found in any of the books.
- Connection: none of the changed text follows a book.
- Verdict: does not bear.

C3.
- Target: SKILL.md line 106 (step 4).
- Defect looked for: any copying.
- Grounds: the change only removes a clause. "Plant, hide, reveal" was already there at 018ebd6, and no book has the triad (see C1).
- Verdict: does not bear.

C4.
- Target: SKILL.md line 164, the trap "Surprise by default".
- Defect looked for: close paraphrase.
- Grounds:
  - The additions are "usually" and the *Psycho* parenthetical, both from the Anticipation theory (line 67).
  - The Truby clause did not change. Truby's passage on the reveals plot (*The Anatomy of Story*, raw lines 2346-2348) uses different words.
- Verdict: does not bear.

C5.
- Target: reveals-and-withholding.md line 77, section 6, the "Set-up and payoff" bullet. It did not change; I read it because the brief names section 6.
- Defect looked for: a book's example list and order of points.
- Grounds: Egri, Part IV chapter 3, Dialogue (raw line 2475), the nail-file example.
- Connection:
  - This is the closest paraphrase in the area. It keeps Egri's single example, both of its conditions, and his two further points (not by chance; from the character).
  - But it reverses the order, putting the general rule first, words everything anew, and credits the example as "Egri's case".
  - What it shares is the example's idea, not its expression.
- Verdict: does not bear.

C6.
- Target: reveals-and-withholding.md line 76, section 6, the Foreshadowing bullet. It did not change.
- Defect looked for: a book's order of points.
- Grounds: Egri, chapter 7, Foreshadowing Conflict (raw lines 1826-1845).
- Connection:
  - Its three short points follow Egri's order, but that is simply the natural order: what it is, what it does, what it promises.
  - None of Egri's examples is used.
  - The third point, a promise that is broken, is the workshop's, not Egri's.
- Verdict: does not bear.

Side findings (not copying; for the maker and the theory-checker)

D1.
- Target: /home/user/StoryTest/.claude/agents/copy-checker.md line 13.
- Defect: a rule changed in one place but not in its copies. The line tells the copy-checker to put `N=6` in front of the command. The script has not read that setting since commit 7812119 (entry 29), which replaced it with `--run-length`.
- Grounds: `N=6 python3 .claude/skills/add-source/scripts/overlap_check.py <Egri> .claude/skills/plot/SKILL.md` printed "TOTAL problem spans >= 8 words: 0". `git show 7812119` shows the `os.environ.get("N", "8")` line removed. Outside the kept records, grep found that one line as the only copy of `N=6`.
- Connection: a checker who follows the line runs the 8-word check twice and could report a 6-word pass that never ran. That breaks rule 2: not run is never passed. This is outside the diff under review.
- Verdict: bears; should change. Fix: write `--run-length 6` after the script name.

D2.
- Target: reveals-and-withholding.md line 30, the new clause "stretching Egri's set-up and payoff from the climax to every rescue is the workshop's reading *(built)*".
- Defect: the clause puts the workshop's stretch in the wrong place, and its label is mixed.
- Grounds:
  - Egri's nail-file point sits in Part IV chapter 3, Dialogue (raw lines about 2474-2475). It comes under a general rule about preparing coming events, and concerns the crime in a murder play.
  - His chapter 10, Crisis, Climax, Resolution (raw lines 2258-2378), has no point about preparing what the climax uses. A search for preparation words there printed one hit, and it is unrelated.
  - Egri never uses "payoff": grep printed 0 hits.
  - The rule card at /home/user/StoryTest/.claude/skills/add-source/SKILL.md line 86 grades a book's claim fitted, built or asserted. A workshop reading is instead labelled as such, with its question number.
- Connection:
  - The workshop already reads Egri's rule as being about "the climax". That reading also appears at section 6 line 77, the sources line (line 3), and /home/user/StoryTest/.claude/skills/dialogue/references/flaws-and-fixes.md line 78.
  - Egri's own general rule arguably already reaches a rescue. So the workshop's reading starts at "the climax", not at "every rescue".
  - "*(built)*" is a book's grade attached to a workshop reading, with no question number.
- Verdict: bears; minor. The rule itself need not change.

D3.
- Target: reveals-and-withholding.md line 74 (section 6, did not change). It says that calling "a foreshadowed clash a promise is the workshop's stretch".
- Defect: a book's support is left uncredited.
- Grounds: Egri, chapter 7, Foreshadowing Conflict (raw line 1839), calls foreshadowing a promise himself.
- Connection: stretching the Gap theory's principle 5 is still the workshop's reading. But the foreshadowing half has a book behind it, which bears on owner question Q7.
- Verdict: bears; minor.

D4.
- Target: /home/user/StoryTest/sources/README.md lines 40-43, the Overlap check cells.
- Defect: a record that could go stale. All four cells are dated 23 Sep 2026, and entry 31 records no copying run.
- Connection: the live build is not yet committed (live HEAD is 35f2939). So the CLAUDE.md duty to record the result falls due at that commit.
- Verdict: does not bear yet. It is settled by the register line written at the commit.

Checked and found right:
- The four books are present.
- The overlap runs above: 8 and 6 words on the changed files, 5 and 4 words on the changed lines, and 8 words on the whole tree.
- The owner-theory citations in the changed text are right: Bond Part 2 section 7, and Anticipation Part 2 sections 5 and 7.
- The dropped "grandmother" example and the dropped "reread" clause in step 4 are removals only.

Not checked:
- The unchanged sections 3-5 and 7-9 against Truby and McKee: Truby's four slots, the revelations sequence, and McKee's exposition rules.
- McKee's *Dialogue* side by side: no changed sentence draws on McKee. I searched it only for surprise and bomb terms.
- *The Anatomy of Genres* beyond its *Psycho* passage and word counts.
- The other 26 files in the full diff, beyond the whole-tree 8-word run.
- Whether the edits are right as craft or as theory.
- The paraphrase judgements are by reading; no tool measures close paraphrase.

Verdict: passed. No changed book-derived passage bears as copying. Recommended, but not a condition of the copying check: D1 (should change), D2 and D3 (minor), and D4 at the commit.
