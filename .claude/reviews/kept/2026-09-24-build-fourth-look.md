# The fourth look at the error-correction build: the three reports, 24 September 2026

What this is: the three reviewers' reports, word for word as each agent returned it. They looked at the edits answering the third look (snapshot commits 5e5564d to 018ebd6). The reviewers made no edits; every experiment ran in scratch copies. Their briefs, the check of those briefs, and the lead's plan for answering them are kept beside this file, in `2026-09-24-build-fourth-look-briefs-and-plan.md`. How each finding was answered is in the build's review receipt. No book text is quoted in them. Kept for log entry 31.

---

## 1. theory-checker

**Theory-checker, fourth look: the edits 5e5564d..018ebd6 (the answers to the third look)**

**How I worked.** I read CLAUDE.md, the term sheet, the kinds table, C1 to C15, both new kept records (the third look's reports; its briefs, brief check, known fault and plan) and the diff. For the theory passages I read the theory first:
- Gap lines 57, 59 and 64;
- Anticipation lines 15, 25, 41, 67 and 84;
- Bond lines 30 and 84.

I edited nothing in the live repository. Afterwards its HEAD was still 35f2939, `git status` still showed 30 entries, and no `/tmp/workshop-*` folders were left. Every run was in copies of 018ebd6 under `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/r4-theory-checker/`, with scripts `outside_loosening.py`, `outside_book2.py` and `checkonly_receipt.py`. The snapshot's tracked files match the live tree: `diff -rq` showed only `__pycache__` and an empty `cases/` folder in the live tree.

Line numbers below are at 018ebd6, which is the same as the live tree.

---

## Must change

**T1. A commit that changes only checks can loosen the receipt check just for itself, and then goes through with no review receipt at all.** This is new in these edits.
- **Target:** `/home/user/StoryTest/.claude/skills/error-correction/scripts/check_commit.py`, lines 248 and 263–264: `judging_scripts = staged_scripts if only_checks`, so the receipt check is taken from the staged files. The statements it breaks:
  - `/home/user/StoryTest/CLAUDE.md` line 32 ("a check cannot be loosened in the same commit as the work it would stop"), line 40 ("By itself within one commit") and line 41 ("the gate refuses the change without a review receipt");
  - `/home/user/StoryTest/.claude/skills/error-correction/SKILL.md` line 204 (a check "always get[s] a full review");
  - `/home/user/StoryTest/.claude/skills/error-correction/references/reviews-and-briefs.md` line 28 ("The gate never takes a light receipt for a change to a check");
  - `/home/user/StoryTest/.claude/skills/error-correction/references/checks-and-cases.md` line 40.
- **Defect:** the commit's own change is the check change, and its own receipt is judged by the receipt check that same commit changes.
- **Grounds:** `checkonly_receipt.py`. On top of an approved commit I staged only `review_receipt.py`, loosened so that any change touching that file needs no receipt, and added no receipt. The gate printed "note: this commit changes only checks, so its own changed checks and receipt check run on it…", then "review receipt: not needed (no reviewed file changed)", then "passed the last approved commit's planted-fault test, on the changed checks", then "All checks passed; committing." The commit is stamped "approved b217f92…".
- **At 5e5564d** the receipt check always came from the last commit: line 213 there reads `os.path.join(last_scripts, "review_receipt.py")`.
- **Connection:** the texts promise that a check change is always fully reviewed and that no check can pass its own work within one commit. Here an unreviewed check change passes and becomes the approved receipt check. The named catch, `test_checks.py`, passed it. So by SKILL.md's fifth tripwire and reviews-and-briefs.md line 48, C15's tripwire fires a fourth time.
- **Change:** judge a check-only commit's receipt with the last approved commit's receipt check, and allow the staged one only when that one fails and the owner is named. Or state this limit everywhere listed above. Either way, plant this route.
- **Verdict:** bears. **Must change.**

**T11. "Every finding of both notes is now applied" in file 26 is false a third time, and the record repeats it.**
- **Target:** `/home/user/StoryTest/26 Test - The Catch - two versions.md` line 130. Repeated in `/home/user/StoryTest/StoryTest - project story.md` line 143 ("File 26 was reworded and the findings applied").
- **Grounds:** the kept break test (`/home/user/StoryTest/.claude/reviews/kept/2026-09-24-catch-break-test.md`). These findings are still not applied:
  - N20 "holds_it" marks the ring beat **unknown**, gives a page reason for A ("A's rings 'directly across' reads correctly whichever way the camera sees"), and names the test that would settle it (block both versions with two people at a table). File 26 line 96 files it under taste, says "Nothing on the page decides", and drops the test.
  - N20 on "Why lock you up?": "A does the same job with … (A:710-711)". Not in the file.
  - N1 "rival": B's middle has more spoken rules (B:551, B:571-585, B:603-608, B:709, B:741), which partly tells the running-time rival apart. File 26 line 128 says only the owner's aim settles it.
  - N1 "direction": B:161 and B:1176 hint which draft came first, "The owner should confirm that". Neither the file nor S12 says so.
- **Connection:** the owner is told for the fourth time that every finding was applied. Kinds row 22 already records this very error twice.
- **Change:** apply these findings, or list each one not applied, with its reason, and reword line 130 and entry 30 to match.
- **Verdict:** bears. **Must change.** The file goes to the owner, and the fix costs a few lines.

---

## Should change

**T2. A check loosened in a commit made outside the gate does not stop the next commit through the gate, though several texts say it does.**
- **Target:**
  - `/home/user/StoryTest/.claude/skills/error-correction/references/checks-and-cases.md` line 36, which lists "a check loosened" among what "stops that commit until a commit puts it right";
  - the note at the top of `recheck_commits.py`, lines 13–17;
  - SKILL.md line 118 and line 228 ("whatever a commit made without the gate got wrong stops the next commit");
  - CLAUDE.md line 39;
  - `/home/user/StoryTest/27 Corrections.md` kinds row 28;
  - `/home/user/StoryTest/README.md` line 89.
- **Grounds:** `outside_loosening.py approve-first`.
  - A commit made where the gate was off made `check_records.py` skip entry 3.
  - The next commit through the gate carried only its late receipt. It printed "passed the last approved commit's planted-fault test, on the changed checks … All checks passed" and was stamped.
  - The commit after it rewrote entry 3 and printed "passed records". It was stamped too.
  - Control, `outside_loosening.py together`: with the rewrite in the first commit through the gate, it printed "FAILED records … log entry 3 has been changed".
- **Connection:** only the planted faults and the late review judge such a loosening. That is exactly the across-two-commits limit that checks-and-cases.md line 44 and CLAUDE.md line 40 state, but line 36 of the same module says the opposite.
- **Verdict:** bears. **Should change:** scope these statements to that limit.

**T3. "Apart from one honest route" understates what the texts themselves list.**
- **Target:** SKILL.md line 118; CLAUDE.md line 51 ("apart from that one honest route"); README line 89; S10 at `/home/user/StoryTest/22 Questions - meanings only you can settle.md` line 95; project story lines 12 and 75. Also checks-and-cases.md line 44, which lists three limits and then says "So the gate stops honest mistakes … by itself".
- **Grounds:** honest routes stated elsewhere in these same files:
  - CLAUDE.md line 44: copying is not seen for "a copied passage added and removed between two commits through the gate", and while the books are absent the Book-text line is only on trust;
  - CLAUDE.md line 40 and checks-and-cases line 44: across two commits, a wrong check passes the work it would have stopped;
  - T2;
  - T4.
- **Connection:** the owner is told that there is one honest gap, and the rule table on the same page shows several.
- **Verdict:** bears. **Should change.**

**T4. Notes "for a person" and "for the owner" are printed once, in the output of a commit that passes, and are then settled for good. No step carries them to the owner.**
- **Target:** checks-and-cases.md line 38 ("reported for the owner"); S10, project story line 75 and SKILL.md line 118 ("only flagged for a person"); CLAUDE.md line 44.
- **Grounds:** `outside_book2.py`.
  - A 280 KB file of invented words was added and then removed, both in commits made where the gate was off.
  - The next commit through the gate printed "note: commit c433ccd… added notes.txt, which looks like a book file … tell the owner" and "All checks passed".
  - `session_start.py` then said nothing about it.
  - The recheck's own note says settled commits are "never looked at again".
- **Connection:** "reported for the owner" claims more than the script does. U1 asked the texts to say what the person does; they still do not.
- **Verdict:** bears. **Should change:** add a step, for example "put each note in the log entry and tell the owner before committing", or say "noted once".

**T5. Use-tester's m3 is answered only in part: the check-only exception is stated too widely.**
- **Target:** checks-and-cases.md line 40 and the note at the top of `check_commit.py` ("so a wrong check can be corrected even when it stops every commit … This does not cover the gate script itself").
- **Grounds (from reading the code; not run):** `check_commit.py` line 279 always runs the recheck from `approved_scripts`, and line 309 always runs the planted-fault test from `approved_scripts`.
- **Connection:** a wrong `recheck_commits.py` or `test_checks.py` that stops every commit cannot be corrected by this route either. Only `check_commit.py` is named as the exception.
- **Verdict:** bears. **Should change:** name all three.

**T6. S10 (b)'s new "What it buys" claims more than option (b) could deliver.**
- **Target:** questions file line 95: "no edit to the gate could then happen without you seeing that it was asked for".
- **Grounds:**
  - S10's own honest route is an edit made "on GitHub, say", which Claude Code never sees.
  - The workshop's own edit hook, `/home/user/StoryTest/.claude/hooks/protect_frozen_files.py` lines 13–14, says: "It cannot see edits made by shell commands or by scripts".
- **Connection:** the owner is asked to choose between options, and one of them is misdescribed.
- **Verdict:** bears. **Should change.**

**T7. S10's "The one place you are already named" is false, and the new route for a wrong gate script asks of the owner what S10 (b) declines to ask.**
- **Target:** S10, line 95. Against it:
  - checks-and-cases.md line 48: "Only the owner may then commit the correction with the gate switched off";
  - checks-and-cases.md line 38 and the recheck's note: rewriting the history to remove a book file "is the owner's decision".
- **Connection:** S10 (b) is declined because the owner's yes "would be a click on a change you cannot review". The new route has the owner commit a change to the gate script itself, with the gate off, and nothing tells the owner how to do that.
- **Verdict:** bears. **Should change:** list these places in S10 and say what each asks of the owner.

**T8. The new receipt fingerprint ignores where a line sits, so moving a reviewed line after review keeps the old receipt.**
- **Target:**
  - `/home/user/StoryTest/.claude/skills/error-correction/references/reviews-and-briefs.md` line 25 ("If you change anything after the review … the fingerprint changes");
  - kinds row 16 ("the review receipt tied to the exact change");
  - C4 line 63 ("a change edited after its review needs a new one");
  - checks-and-cases.md line 38.
- **Grounds:** in a copy (`exp-fp`) I added one sentence to plot's `reveals-and-withholding.md`, once before "## 9. Traps" and once before "## 3. What a reveal must do". `review_receipt.py fingerprint` printed `28fab8f1142a51a3` both times.
- **Connection:** in these skills, which section a rule sits in changes its scope. The fix for U5 made this new error.
- **Verdict:** bears. **Should change:** say that the receipt covers the lines and not where they sit, or keep enough context in the fingerprint to hold the place.

**T9. The plot skill's section 1 and step 4 now limit "plant, hide, reveal" to a surprise that makes the audience reread. That contradicts section 2, which this same edit wrote.**
- **Theory first:** Gap line 57: surprise is "a gap you didn't know was there: you thought you understood and you were wrong". It carries no condition about rereading.
- **Target:**
  - `/home/user/StoryTest/.claude/skills/plot/references/reveals-and-withholding.md` line 16 ("for that kind, plant, hide, reveal");
  - `/home/user/StoryTest/.claude/skills/plot/SKILL.md` line 106 ("to make them reread what came before, plant, hide, reveal").
- **Grounds:** a rescue from nowhere, meant as a surprise, does not make the audience reread. Section 1 and step 4 then give it no planting, while line 30 says a rescue is "never exempt" and needs its set-up. At 35f2939, every surprise got "plant, hide, reveal".
- **Connection:** R7 asked for these two places to be brought into line; they now say the opposite of section 2 in the other direction. The building route (step 4) gives a writer the wrong answer.
- **Verdict:** bears. **Should change:** keep "plant, hide, reveal" for every surprise, with section 2's exemption for a bare threat's arrival.

**T10. "Buys seconds" and "lasts seconds", which C12 now calls an error, survive in two places, while C12 says the copies were brought into line.**
- **Target:**
  - plot SKILL.md line 164 ("A hidden threat buys seconds");
  - `reveals-and-withholding.md` line 16 ("It lasts seconds, as with the bomb …, unless it makes the audience reread");
  - C12 line 128.
- **Grounds:** Anticipation line 67: after *Psycho*'s early killing "no guarantee holds and every threat is real". The *Psycho* killing is a surprise in the Gap theory's words (the audience thought it understood whose story this is). It does not make anyone reread, and its effect lasts far beyond seconds. Section 2, line 30, now says the same.
- **Connection:** the theory's own case comes out wrong in two places, and the module disagrees with itself.
- **Verdict:** bears. **Should change.**

**T12. Stale "Now caught by" lines describe the old recheck.**
- **Target:** `/home/user/StoryTest/27 Corrections.md`:
  - C15 line 156: "run by the gate from the last commit … the recheck by each parent's checks";
  - C6 line 80: "and the recheck of commits the gate did not see";
  - C4 line 63: "(the gate and the recheck refuse a change or a deletion)".
- **Grounds:** the recheck's note, lines 13–17: what such commits got wrong in the files "is not judged here".
- **Connection:** these are records of what catches each error, left unchanged in corrections this diff edited.
- **Verdict:** bears. **Should change.**

**T13. Two claims have no record in the repository.**
- **Target:** entry 29, line 140, rewritten after the third look: "its other half … ran during this entry; its results wait for the write-up". Entry 30, line 143, and C15 line 155: the retirement rules were "tried by hand in a copy".
- **Grounds:** nothing under `/home/user/StoryTest/.claude/reviews/kept/` or `kept-cases/runs/` holds either run (`ls`, and a search for "trial").
- **Connection:** these are "Not run is never passed" claims without their receipts, and results kept only in scratch folders are C13's error again. Whether the half trial really ran: **does not bear yet**. Keep its record and show it.
- **Verdict:** bears, for the missing record. **Should change.**

---

## Minor (each bears unless noted)

- **T14. The jump-scare sentence cites the wrong part of the theory and uses "dread" loosely.**
  - Target: `reveals-and-withholding.md` line 30, "a jump scare works only after dread has been built (Anticipation theory, the fear ladder)".
  - Theory: the claim is Anticipation Part 2 section 7 (line 84). The ladder, line 25, says nothing about dread coming first.
  - Term sheet section 13 item 7 calls that use of "dread" loose. Q6's stopgap keeps *dread* for the rung only.
  - Fix: cite Part 2 section 7, and say "after fear has been built (the theory's 'real dread')".
- **T15. "Rests on no earlier fact" misdescribes the theory's own bomb.**
  - Gap line 59: "The story is the same; only the plot changed". The unshown bomb is an earlier fact of the story; it is only not shown.
  - Fix: write "no fact shown earlier".
- **T16. The *Psycho* clause drops "early".** Line 30 says a guarantee break "changes every threat after it". The theory (Part 2 section 5, "Break the contract early"), term sheet 1.2 and `suspense-and-fear.md` section 5 all say "early and convincingly". A late break is the workshop's separate extension, S5.
- **T17. The rescue clause, a pointer and the new example.**
  - The rescue clause extends Egri's climax rule to every rescue without saying so. Tag it as the workshop's extension of Egri *(built)*.
  - "(section 7)" after the Bond claim lands on the module's own section 7, which is Egri's jump. Write "(Bond theory, Part 2 section 7)".
  - The grandmother example is U4's own walk case. It is not a kept case: kept case 07's "grandmother" and case 09's "poisoned" are unrelated. But it confirms the fix on the case that found the fault.
  - The S13 label could name term sheet section 13, item 9.
- **T18. File 26's "weakened, not lost" (line 12) and "Weakened." (lines 48, 53 and 54) assume which version came first.**
  - "Lost" is the same word family as "loses", which C1 records as an order word.
  - "Weakened" comes from the break test's summary, "several of B's losses are weakened", the same way "still" came in. The flip test: had B come first, one would write "weaker".
- **T19. Stale or inconsistent lines in file 26.**
  - Line 9 still says "in three rounds" and "(log entries 27 and 29 …)", but four rounds are listed and entry 30 is missing.
  - Line 93 calls the recording "a second route" in A, while line 58 counts cage, ramp and recording as three. The break test's "pulls" says "a third route".
  - Line 129 says "the corrections later found" A:697 and A:706. The break test itself gave both (its lines 32 and 34).
- **T20. Records of the brief check disagree with the kept brief check.**
  - C5 is closed, but its "Put right" still says "no brief has been checked with it yet" and "nothing put right yet".
  - C5 says "nine of its findings applied". The kept briefs say "findings 1 to 11 applied".
  - Entry 30, line 141, says the two things that had to change included the test setting. The brief check's must-changes were findings 1 and 2; the setting was finding 3, a should-change.
- **T21. Small mismatches with the scripts.**
  - reviews-and-briefs.md line 30 leaves out "made straight on top of an approved commit".
  - The project story's word list (line 77) defines the last approved commit as "the most recent" such commit. The script takes the nearest one on the main line (first parents).
  - The receipt form's "Tests retired" hint says "from the last commit" and leaves out the rule that the owner is named first.
- **T22. Hook notes skip the exceptions.** The notes at the top of `/home/user/StoryTest/.claude/hooks/refuse_check_bypass.py`, `/home/user/StoryTest/.claude/hooks/git_command_reading.py` and `/home/user/StoryTest/.githooks/pre-merge-commit` say the next commit through the gate judges what such a commit got wrong. They leave out the gate's-own-files route and T2.
- **T23. The owner-objection tripwire is missing a condition.** SKILL.md line 219 fires "the owner caught it" whenever "the note came from a skill's own text", without "and the objection bears".
- **T24 (pre-existing; scripts area).** `run_all_checks.py`'s note says copying reads "every .md file". `overlap_check.py` reads every text ending in `TEXT_ENDINGS`.

---

## Marks on new or changed rules and examples

- **Exemption for a threat's arrival:** held, by keeping a bare arrival from being planted into suspense. "No earlier fact" is worded loosely (T15).
- **Jump scare needs dread first:** held (Anticipation line 84). The citation is wrong (T14).
- **A guarantee break changes every later threat:** held (line 67). "Early" has been dropped (T16).
- **S13 label:** held.
- **Rescue never exempt:** held, by a threat's arrival that also rescues, for example a bomb that kills the captors. It rests on Egri *(built)*, extended without a label.
- **Character reveal never exempt:** held (Bond line 84). Reading Bond's "earning" as a set-up is the workshop's link.
- **Section 1 "for that kind" and step 4 "to make them reread":** not held. They contradict line 30 (T9).
- **Check-only exception using its own receipt check:** fails its own claim (T1).
- **Retiring a test with the owner named first:** held if the owner accepts being asked. S10 must describe it truly (T7).
- **Typo route:** held.
- **Fingerprint from added and removed lines:** held for rebases; loose on where a line sits (T8).
- **Rivals:** none new.
- **Worked example:** the grandmother (T17).

---

## Checked and found right

- **The third theory-checker's findings, answered in content:**
  - R1 for the records check: a log rider now goes to the next commit. I confirmed the rewrite is refused in the control run.
  - R4; R5 (book files noted; the CLAUDE.md row scoped); R6 (the rule stated in three places, and the owner-name test uses startswith); R7 (label and gloss; see T9 and T10 for its copies).
  - R8; R10; R11; R12 (the two uses of "still"); R14; R15; R16; R17; R18; R19; R20 (present; see T6); R22; the R23 heading.
- **Use-tester findings:**
  - U4: scope, label and jump scare, apart from T9, T10 and T14–T16.
  - U6: the revert route is in both modules, SKILL.md and pre-merge-commit.
  - U7 (text) and U8.
  - m4 and m6; m5 (text only).
  - Stall items (b) template, (c) and (d).
- **The planting rule's other statements:** the diagnosing row "the twist came from nowhere" (line 123) and the quick version (line 154) agree with line 30.
- **The theory's own cases:**
  - Joffrey's poisoning is set up and falls under "never exempt".
  - *Chronicle of a Death Foretold* is suspense; the rule says nothing wrong about it.
  - The bomb shown first and the bomb that simply goes off are both handled.
  - "The door dilated" does not bear on this rule.
- **The quotation** "thought you understood and you were wrong" matches Gap line 57 word for word.
- **add-source Step 4.1** matches `run_all_checks.py --against` and the rule against mixing work.
- **The kept-cases README** agrees with the SKILL.md typo row.
- **Machine checks:** on a copy of 018ebd6, every check passed and copying printed NOT RUN. With `--books-from` pointing at the live `sources/raw`, "passed copying from books". That covers 8-word runs only.

## The parts the maker left undone

- **Copying not rerun on each commit the gate did not approve:** the limit is stated, but T3 contradicts it.
- **Scripts D, in part:** sound for `check_commit.py`. But the recheck and the planted-fault test are left out too (T5), and the part that was done opens T1.
- **S10 (b):** sound as the owner's choice, but it is misdescribed (T6, T7).
- **Kept-case notes:** sound to leave for the run.
- **`LARGE_RECORDS_ALLOWED`:** sound, and stated.
- **Not planted:** acceptable, but the hand try has no record (T13).
- **Other parts still open:**
  - U1's "say what the person does" (T4).
  - Stall (b): whether a light receipt will do for "answered" marks.
  - Stall (g): whether an unreviewed outside commit is a tripwire.

## Not checked

- The full `test_checks.py`, and the counts 166 and 19. The planted-fault stage ran only inside my gate runs.
- Merges, cherry-picks and GitHub.
- The hooks' code, beyond their notes.
- The screenplay line references. I checked them against the kept break test only.
- File 26's faults 2 to 5.
- Kept cases: I read only the titles, the "Aimed at" lines and one matching line each of cases 07 and 09.
- The other craft skills, beyond searches for the surprise, shock and planting rules.

## Verdict: passed after changes

- **Must change:** T1 (and record that C15's tripwire has fired again) and T11.
- **Should change:** T2–T10, T12 and T13. Several of them reach the owner, so fix them before the build is committed.

These edits then need a look of their own, by a reviewer who did not make them.

---

## 2. use-tester

# Use-tester, fourth look: the edits 5e5564d to 018ebd6, walked through the situations in Brief B

**Overall verdict: passed after changes.** I walked the brief's situations through the skill in my own copies. The main change holds for what it set out to fix: the gate now compares with the last commit it approved, and anything it finds can be put right with a new commit. The third look's U1, U2, U3, U5, U6, U7 and U8, m1 and m3 to m6 are answered in content, as are the scripts reviewer's A, C and K; D is answered in part (see F4). But walking the situations found one new must-change fault, which came in with these edits:
- **F1.** A merge commit that brings in any reviewed change to a check or hook is stopped. That covers `git merge`, and `git pull` into local work that has moved on. The printed advice then points towards retiring three of the gate's own tests.

It also found five should-change faults (F2 to F6) and seven minor ones.

**Where things are.** Every run was in copies under `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/r4-use-tester/`.
- `w0` is the live history (HEAD 35f2939) with the 018ebd6 files committed through the gate as its first gated commit: 11174d0, stamped "Workshop-gate: approved 9c67882…", passed in 36 s.
- Before building it I compared the live working tree with the snapshot, file by file, using `cmp`. All 117 tracked files are the same, and no live file is missing from the snapshot.
- `w1` to `w12`, `w4b`, `w5a`, `w5b`, `w5c` and `wfresh` are copies of `w0`.
- Each `gh*` folder is a clone with the gate never switched on. It stands in for GitHub or a machine without the gate.
- Every receipt in my copies is SIMULATED; its "report" is a stand-in paragraph that `fill.py` wrote.
- The copying check printed NOT RUN everywhere, because I copied no book text.

---

## 1. Findings

### Must change

**F1. A merge commit that brings in a reviewed check or hook change is stopped, and the advice points to retiring gate tests.**
- **Target:**
  - `check_commit.py` lines 215–216 and 304–311: the planted-fault test now runs whenever the staged checks differ from the last approved commit's, and for a merge that includes checks the merge brings in.
  - Lines 93–94, 103–105 and 365: the settings passed to the test's copies keep `GIT_REFLOG_ACTION`, which `commits_being_merged` reads at line 185.
  - The text that sends honest work this way: `checks-and-cases.md` line 46 ("merge a pull request with a merge commit"), and SKILL.md lines 118 and 227.
- **Defect:**
  - While git makes a merge commit, it hands the hook the setting `GIT_REFLOG_ACTION` ("merge hk", or the pull's own wording).
  - The gate passes that setting on to the planted-fault test. The test's own merge tests then misread their merges and fail.
  - The gate as the third look saw it (5e5564d, lines 243–262) ran this test only when the merge's own changes touched a check. So this stop is new with these edits.
- **Grounds:**
  - **Local merge (`w9`).** A one-line comment in `.claude/hooks/after_commit.py` was reviewed and approved on a branch, and the main line moved by one note. Then `git merge --no-ff -m "Merge the hook comment" hk` printed:
    - "FAILED the last approved commit's planted-fault test, on the changed checks"
    - "FAILED gate, neighbour: an honest merge of two reviewed commits goes through"
    - "FAILED gate, neighbour: a merge made with git merge -m carries the gate's stamp"
    - "FAILED gate: a merge commit runs the gate, which finds the unreviewed commit it brings in"
    - "COMMIT STOPPED"
  - **`git pull`.** `git pull --no-rebase` of the same change, from a gate-less clone into local work that had moved on, printed the same three lines and was stopped.
  - **The cause.** On that copy, `test_checks.py` with `GIT_REFLOG_ACTION="merge hk"` set printed "TOTAL tests: 166, failed: 4" (the three, plus the test that runs the real stage). Without the setting it printed "failed: 0".
  - **A second case (`w8`).** Merging an approved records correction into a main line that had moved was stopped the same way.
  - **Neighbours that stayed quiet.**
    - A merge with no check change (`w9`, `git merge -m "merge side"`) passed, and its stamp sits after a blank line.
    - A conflicted cherry-pick of a hook change, finished with `--continue` (`w12`, a6b04ce), passed.
- **Connection:**
  - This is the kinds-table row "A check or a step that stops honest work, or leaves no way through", reached by ordinary commands.
  - The printed advice ("name the test, one per line, under '## Tests retired' … with the owner named first") would have an agent ask the owner to lose three guards on merges so that an honest merge could go through.
  - Aborting and rebasing instead does get through (as `w2` shows), but no text says so.
  - No planted test merges a check change through the real stage.
- **Verdict:** bears. **Must change.**
  - Keep the git settings of the commit being made away from the test's copies.
  - Plant a merge, and a pull, that bring in a reviewed hook change, run through the real stage.

### Should change

**F2. Rebasing an approved check change that retired a planted test stops every later commit, and the printed advice cannot be followed.**
- **Target:**
  - `check_commit.py` lines 346–356: `retired_tests` reads only the receipt for this commit's own change.
  - Lines 304–311.
  - The promise that a rebase keeps its receipt: `reviews-and-briefs.md` line 32, and `checks-and-cases.md` lines 38 and 46.
- **Grounds (`w8`):**
  - The correction 567203c retired "records: a new entry over 400 characters", with the owner named. After a rebase onto a main line that had moved by one note, it became 8e70bf5, unstamped.
  - The next ordinary commit printed "FAILED records: a new entry over 400 characters … name the test … under '## Tests retired' in the review receipt", then "COMMIT STOPPED".
  - That commit changes nothing that needs a receipt, and the rebased commit's receipt, which already names the test, is committed and cannot be changed.
  - A merge instead is stopped too (F1).
  - I got through by improvising: `git reset --soft HEAD~1`, then committing again through the gate. That printed "retired in the receipt: records: a new entry over 400 characters … All checks passed" (33f7877).
- **Connection:** the text tells the agent that a rebase keeps its receipt, so the agent expects the retirement to travel with it. It does for the receipt check, but not for the planted-fault stage, and the text gives no route.
- **Verdict:** bears. **Should change.**

**F3. The flag "for a person to look at" and the book-file note last for one commit; nobody is named to act, and nothing is recorded.**
- **Target:**
  - CLAUDE.md lines 39, 44 ("a book file added without the gate is reported even after it is removed") and 51.
  - SKILL.md lines 118 and 228; `checks-and-cases.md` lines 38, 44 and 48; README.md line 89; S10 (the questions file, line 95).
  - `recheck_commits.py`: its note, items 3 and 4, and lines 181–188.
  - `session_start.py` lines 127–141.
- **Grounds:**
  - **A hook change (`w2`).**
    - Session start printed "For a person to look at: commit 1bea1d8c5 changed the gate's own files without the gate (.claude/hooks/after_commit.py)…".
    - The next ordinary commit passed, with the same line as an indented note under "passed".
    - After that, session start printed nothing about it, and the recheck printed "rechecked 0 commit(s)".
  - **A book-like file (`w10`).**
    - A 300 KB generated text was added and then removed, in two commits made outside the gate.
    - Session start printed "commit ed131f71a added notes-big.txt, which looks like a book file … tell the owner".
    - After one ordinary commit, `session_start.py | grep -c book` printed 0.
- **Defect:**
  - The flag is a printed line, settled for good by the next approved commit.
  - No text names the person, says what they do, or says that the agent must carry the flag into its reply and the next log entry.
  - The third look's U1 proposed "Say in those five places what the person does". That was not applied, and no reason was given.
- **Connection:** this flag is the only safeguard the text names for its one admitted honest route, and the only report of a book file left in the history. An owner who asks whether the gate can be trusted would be told more than holds.
- **Verdict:** bears. **Should change.**

**F4. The owner's route for a wrong gate script names nothing a non-programmer can do.**
- **Target:**
  - `checks-and-cases.md` line 48: "Only the owner may then commit the correction with the gate switched off; the next commit through the gate then needs a late review receipt for it".
  - `check_commit.py`, its note at lines 31–34.
- **Grounds (`w5a`):**
  - A one-character typo in `check_commit.py` was made on a gate-less clone and pulled in.
  - From then on, every commit printed only `File "/tmp/tmp.FL7hfwGmSu", line 342 … SyntaxError: '(' was never closed`, with no COMMIT STOPPED line and no pointer to the skill.
  - `refuse_check_bypass.py` (lines 7–23) refuses `--no-verify` and changes to where git looks for its hooks, and has no exception for the owner.
  - The correction went through only as a commit made outside the gate (a gate-less clone, as GitHub's web editor would be).
  - It then needed two late receipts: 0759c06… with "not passed (withdrawn in 0893f1b)" for the typo, and f0b696a… with "passed" for the correction.
  - Only then was a commit approved (2ea197b).
- **Connection:**
  - CLAUDE.md says the owner is not a programmer.
  - The text should say what the agent prepares, what plain steps the owner takes (for example, the edit on GitHub), and that both the broken commit and its correction need late receipts.
- **Verdict:** bears. **Should change.** This is the reason given for Scripts D left undone: sound in design, but the route cannot be used as written.

**F5. Printed commands for putting things back assume the fault is on disk or in the last commit, not in a commit the gate did not approve.**
- **Target:**
  - `check_frozen_files.py` lines 163 and 212: "(git checkout -- '<file>')".
  - `check_commit.py` line 277: "If a revert took it out, put it back: git checkout HEAD -- <receipt>".
- **Grounds:**
  - **`w1`.** After the outside commit, `git checkout -- 'sources/bond-theory.md'` changed nothing: `grep -c "Its main claim"` still printed 1. The module's `git checkout 11174d0 -- …` restored the file (0).
  - **`w11`.** After a plain `git revert` of a reviewed commit, the gate printed "put it back: git checkout HEAD -- <receipt>". Running that printed "error: pathspec … did not match any file(s) known to git". `git checkout HEAD~1 -- …` worked.
- **Connection:**
  - The gate repeats these commands on every stopped commit.
  - `checks-and-cases.md` line 46 gives the right command, but an agent reads the check's message first.
  - Two statements at odds. The gate knows the last approved commit and could print it.
- **Verdict:** bears. **Should change.**

**F6. The planting rule's exception for "a threat's arrival that rests on no earlier fact" has no telling test, and clashes with section 6 for a threat that decides the climax.**
- **Target:**
  - `plot/references/reveals-and-withholding.md` line 30: "This check is not for a threat's arrival that rests on no earlier fact … Such a turn needs no set-up".
  - Against line 77 (section 6): "Whatever the climax uses (an object, a skill, a fact) must be known earlier … How much weight a planted fact needs depends on the turn it serves: section 2".
- **Grounds, a walked case no finding produced:**
  - The writer's case: "At my fantasy's climax, as the heroine's army is winning, a flight of dragons, never mentioned before, burns it and the war is lost. I want it as a pure shock."
  - Both routes reach section 2: the diagnosing route (SKILL.md line 123 → section 2) and the building route (section 6 → section 2).
  - Section 2's exception covers the dragons: they are a threat's arrival, not a rescue or a solution, and not a reveal about a character. So the skill says "needs no set-up".
  - Section 6 says what the climax uses must be known earlier, and hands the weight question back to section 2.
  - Implied World principle 1: "Audiences assume the world works like theirs unless told otherwise" (line 20).
  - Gap theory, Part 2 section 2: "In our world a dragon attack is news; in a world full of dragons it might be weather" (line 47).
- **Connection:**
  - Read as "the audience needs no earlier fact to make sense of it", the dragons rest on a departure nobody taught the audience: a world fact, which the module's own section 1 says is scheduled. Read as "no earlier fact was shown", they are exempt.
  - The bomb that simply goes off (Gap line 59) fits either reading.
  - U4's point 2 ("no telling test") is answered for rescues and character reveals, but not for this near neighbour.
  - Whether a threat that rests on no taught fact may decide a climax is between Egri's rule (built) and the Gap theory's surprise bomb, and the module records no rival for it.
- **Verdict:**
  - Two rules at odds, and a phrase that can be read two ways: bears.
  - Which rule should govern: does not bear yet. A telling test would settle it, for example: "Would a first-time audience make sense of the arrival with no fact they were given?"
  - **Should change.**

### Minor (each bears unless noted)

**F7. Session start's "(run run_all_checks.py)" hides the rewritten entry it counted.**
- **Target:** `session_start.py` line 157; `run_all_checks.py` lines 47–49 (`--against` defaults to the last commit); `checks-and-cases.md` line 42.
- **Grounds (`w1`):**
  - Session start printed "Machine checks: FAILING: frozen files, records (run run_all_checks.py)".
  - A plain run showed only stale status lines.
  - With `--against 11174d0`, it printed "log entry 12 has been changed since 11174d0".
  - Nothing ties the failing checks to the unapproved commit.

**F8. Session start runs the checks on disk, so after an outside change to a check it reports failures the gate will not.**
- **Target:** SKILL.md line 232; `checks-and-cases.md` line 42; `session_start.py` lines 144–149.
- **Grounds (`w5c`):** a too-tight records rule was committed outside the gate. Session start printed "Machine checks: FAILING: records" for a new entry. The gate ran the approved records check, which passed it, and stopped the commit only for the missing receipt.
- **Connection:** an agent that obeys session start follows a check nobody reviewed. The recheck's note says this for the recheck only.

**F9. Putting back a log entry the way `checks-and-cases.md` line 46 says restores the whole file, and silently drops anything else the outside commit added.**
- **Grounds (`w1`):**
  - `git checkout 11174d0 -- "StoryTest - project story.md"` removed the owner's new entry 31, made on GitHub: `grep -c "^31\. "` printed 0.
  - The gate then passed the commit.

**F10. "So that a wrong check can be corrected even when it stops every commit" holds only when the owner is at hand.**
- **Target:** `checks-and-cases.md` line 40; `reviews-and-briefs.md` line 30; `check_commit.py` lines 26–30.
- **Defect:**
  - Every new check comes with its own planted test (section 3, step 3).
  - Correcting a wrong check therefore retires that test, and retirement needs the owner named first.
- **Grounds (`w5b`):**
  - A too-tight records rule with its planted test was approved (e3a81be) and then stopped the next log entry.
  - Its correction was stopped: "FAILED records: a new entry over 400 characters".
  - It passed only with "Reviewed by: the owner …" (567203c).
- **Also:**
  - `reviews-and-briefs.md` line 30 leaves out "made straight on top of an approved commit".
  - `w5c` shows that condition matters: there, the approved commit's checks judged everything.

**F11. Copies not brought into line.**
- **The typo route.** `checks-and-cases.md` line 70 does not say "before committing", nor "write the line without a fingerprint line". SKILL.md line 204 and `kept-cases/README.md` line 43 now do.
- **Cherry-picks.**
  - `.githooks/pre-merge-commit` line 5 says "Git runs no gate hook at all for … a cherry-pick", and SKILL.md line 228 lists cherry-picks among the commits the gate did not approve.
  - A conflicted cherry-pick finished with `--continue` does run the gate and is stamped (`w2` 7da2ab8, `w12` a6b04ce). This is harmless.
- **Late receipts.** `checks-and-cases.md` line 48 says "a late review receipt for it". Two are needed when the break itself came from outside (`w5a`).

**F12. A pointer that lands on the wrong part of the theory (for theory-checker to confirm).**
- **Target:** `reveals-and-withholding.md` line 30: "a jump scare works only after dread has been built (Anticipation theory, the fear ladder)".
- **Grounds:**
  - The theory says this in Part 2 section 7, the ratchet: "After real dread it works as a release valve; without dread it's just a flinch" (line 84).
  - The ladder's Shock row (line 25) says only "Nothing: it arrives without warning".
  - The pointer matches the skill's own `suspense-and-fear.md` section 2 (line 37), not the theory.

**F13. Kept cases.** I listed the files in `kept-cases/` and read only their titles and "Aimed at" lines.
- **Case 04** ("The lead shot dead in chapter three", aimed at H14):
  - The new clause "one that breaks a guarantee the audience relied on, as *Psycho* does with its apparent lead, changes every threat after it" reaches the conclusion that case protects, and the set-up route now meets it too.
  - It is the theory's own case and line ("After that, no guarantee holds and every threat is real", Anticipation line 67), already in `suspense-and-fear.md` section 5. So it does not bear as an answer key.
  - Whether case 04 still tells method from echo does not bear yet. The settling test: rerun case 04 on the committed plot skill, and grade the route the answer took.
- **The grandmother example.** It is the third look's own walked case, now written into the skill. Any later walk of it can only agree, so I used a different character reveal (the best friend, below).
- No other case's title or aim matches the changed wording.

---

## 2. The earlier findings in my area

| Item | Answered? | What I ran |
|---|---|---|
| U1 | Yes, as a stop. The "person" part is not answered (F3). | `w2`: a rebased, reviewed hook change gave a note, not a stop. The next commit passed (259c014). |
| U2 | Yes | After one approved commit, the recheck printed "rechecked 0 commit(s)" (`w2`). Late receipts took under a second (`w5a`). |
| U3 | Yes | `w4b`: withdrawal claimed, nothing withdrawn, printed "its receipt says the change was withdrawn, but it is still in .claude/skills/plot/SKILL.md", then COMMIT STOPPED. |
| U4 | Yes, for the cases it named | Jump scare, grandmother, *Psycho* and the S13 label, walked below. F6 is a residue. |
| U5 | Yes | `w2`: a rebase over a reviewed change to the same plot file found both receipts. |
| U6 | Yes | `w4`: `revert --no-commit`, two receipts, commit passed. The rule was gone (`grep -c` printed 0) and the recheck was clean. A plain revert, see F5. |
| U7 | Yes in SKILL.md and the kept-cases README; F11 for `checks-and-cases.md` | `w7`: a plot typo while plot was owed a rerun, where the refusal now says what to do; a genre typo while genre was up to date, where the fingerprint line was printed and the skill cleared. |
| U8, m5, m6 | Yes | `w6`: the search covers `.claude/skills` only. Kept case 03 was named by file and line while Q3 was being rechecked. |
| m1, K | Yes | `w9`: the `git merge -m` stamp sits after a blank line and is read as approved. |
| m3, D | In part | The gate script is now excluded; see F4 and F10. |
| m4 | Yes | The form's Verdict hint lists "not passed (withdrawn in <commit>)". |
| A | Yes | `w1`: an outside theory edit and log rewrite stopped the next commit, and a commit that put them back cleared it (19fe76b). |
| C | Yes | As U3. |

**Stall list (the third look's).**
- (a) The receipt form's hint was updated.
- (b) The template for recording an answer now exists. Not answered: the skill passages still keep "is a question put to the owner" beside "answered", and the text still does not say whether a light receipt will do.
- (c) Where a stop is written down is now answered.
- (d) An owner objecting to a note is now answered.
- (g) Whether an outside commit that got something wrong is a tripwire is still not said.

---

## 3. Stall list, per situation

**1. A GitHub commit that edits a frozen theory and rewrites entry 12 (`w1`).** Followable end to end: stopped, then put right, then approved (19fe76b). Stalls:
- F7: the hint hides the rewrite.
- F5: the frozen check's printed command does nothing.
- F9: the owner's entry 31 was lost.
- Whether this counts as a tripwire is unsaid.
- The put-right commit needs no receipt, because neither file is in the receipt's scope.

**2. Rebase, cherry-pick, squash (`w2`, `w3`, `w8`).** A rebase over the same file and a rebase of a hook change both work. Stalls:
- F3: the flag vanishes after the next commit.
- F2: a rebased retirement stops every later commit.
- A conflicted cherry-pick runs the gate and is approved; a clean one is unapproved, finds its receipt, and gets a note (F11).
- A local squash (`reset --soft`, then commit) needs a fresh review of the combined change, and the text speaks only of GitHub squashes.
- A GitHub squash after the main line moved is stopped until it gets a late receipt of its own, as stated.

**3. A late review that fails (`w4`, `w4b`).** Works as written. Stalls:
- The withdrawal "needs its own receipt", but the text does not say whether light or full.
- When the review passes part of an outside commit, taking out only the failing part is refused ("still in .claude/skills/plot/SKILL.md"). No route is stated: withdraw everything and redo the good part later, or write "passed after changes".

**4. A wrong check (`w5a`, `w5b`, `w5c`).**
- Approved by the gate: works, with the owner needed (F10).
- The gate script, committed outside: F4.
- An ordinary check, committed outside: the gate uses the approved checks and asks for a late receipt, while session start disagrees (F8).

**5. Retiring a planted test (`w5b`).** Works. It was refused with a reviewer agent named, and passed with the owner named first. Session start then listed "Planted tests retired so far (1)". Stall: the form's "Reviewed by" hint does not say the owner must come first.

**6. The owner answers Q3; typos (`w6`, `w7`).** Followable. Stalls:
- The kept-case note says "which is answered" while Q3's status is "rechecking".
- The (b) stalls above.

**7 and 8. The plot walks,** through the building route (SKILL.md line 34 → step 4 at line 106) and the diagnosing route (row at line 123 → sections 2, 3 and 7). The quick version (line 154) agrees.
- **A twist's clue (should fire).** "The narrator's brother turns out, in the last chapter, to have died years ago; readers say it came from nowhere; my clues are that he never eats and the waiter sets one place." The rule fires: the clues must be noticeable, light enough not to be guessed, and given more weight where they are easy to miss. The teller test in section 7 passes (a narrator who "will not say it"). This agrees with Gap line 57 ("you thought you understood and you were wrong") and Part 2 section 5. No stall.
- **A jump scare (the exception should fire).** "A crow smashes through the kitchen window with no warning; must I set it up?" The answer is: no set-up, but it needs dread before it. That agrees with Anticipation lines 25 and 84. Stalls: F12; and the set-up route never reaches the medium point (in prose, jump scares are "Nearly impossible", Anticipation line 98, which is in `suspense-and-fear.md` section 9).
- **A character reveal meant as a shock (the exception should stay quiet).** "The loyal best friend is revealed in the last scene to have been sleeping with the heroine's husband; I want no hints." It stays quiet: never exempt. That agrees with Bond line 84 ("It breaks when they do something that contradicts who they've been without the story earning it"). The "(section 7)" pointer lands on Egri's "Surprise without a jump", which fits.
- **A rescue from nowhere at the climax (dragons rescue the heroine).** Never exempt, so it needs a set-up. Right.
- **The same dragons deciding the climax against her:** F6.
- ***Chronicle of a Death Foretold*.** The ending is announced; "being seen is the point" fits Anticipation line 47 ("Uncertainty can also move from *whether* to *how*"). The changed text says nothing that pushes towards hiding the ending. No stall.
- **The theories' own cases, all consistent with the changed rule:**
  - The bomb, shown first (suspense) or simply going off (surprise, exempt, name labelled under S13).
  - Joffrey: the death needs no planted fact, and the later reveal of who poisoned him does. No clash with Bond line 79.
  - *Psycho*: the guarantee clause, and Norman as "Mother", a character reveal that is planted.
  - "The door dilated": emphasis given only to what pays off; the surplus is left alone.

**9. The owner asks whether the gate can be trusted.** CLAUDE.md lines 39–51, SKILL.md lines 118 and 228, and S10 would have an agent say four things. What my walks showed for each:
- **"Whatever a commit made without the gate got wrong stops the next commit until it is put right."** Held (`w1`).
- **"It stops honest mistakes and shortcuts, apart from one honest route, which is only flagged for a person."** The flag lasts one commit (F3). The gate also stops honest work, with no stated way through: merges and pulls (F1), rebased retirements (F2), and a broken gate script for a non-programmer owner (F4).
- **"A book file added without the gate is reported even after it is removed."** Reported once (`w10`).
- **"It does not stop an agent set on getting round it."** Not tested.

These claims need scoping, or F1 to F4 put right, before that answer goes to the owner.

**10. Neighbours where nothing should fire.** All stayed quiet:
- a fresh clone's first session (gate switched on, nothing flagged, 0.5 s);
- ordinary runs of commits, throughout;
- `git merge -m` with no check change.

The build's own first commit on the live history went through in `w0`, with "note: the commit gate is new in this commit" and "passed the planted-fault test brought in".

---

## 4. The maker's parts left undone
- **The copying check not rerun per unapproved commit:** sound as a stated limit. But the book-file note that stands in for it is transient (F3).
- **Scripts D, in part:** sound in design, but the route cannot be used as written (F4).
- **S10 (b):** the owner's choice; sound.
- **Case 04 and case 11 left to the rerun:** sound; see F13.
- **Scripts G, in part:** not judged; outside my area.
- **The Book-text rule reading the staged register:** I did not walk it either.
- **Counts:** on a clean copy (`w0`), `test_checks.py` printed "TOTAL tests: 166, failed: 0" in 69 s. I did not check the "19 fail on the old scripts".

## 5. Not checked
- I ran no kept cases and read no kept case beyond its title and "Aimed at" line.
- No real GitHub; no live Claude Code session. I fed the hooks nothing; the live after-commit reminder printed its text on my commands.
- The copying check (NOT RUN everywhere), and the first commit with the books present.
- The bypass hook's spellings; Windows and macOS.
- The theory content of file 26 and the corrections file.

## 6. Side effects
None in the live repository: HEAD is still 35f2939, `git status --short` shows 30 entries as at the start, and `core.hooksPath` is unchanged. No `/tmp/workshop-*` folders are left over.

## Verdict: passed after changes
- **Must change:** F1.
- **Should change:** F2, F3, F4, F5 and F6.
- **Minor:** F7 to F13.

The changes made for F1 to F6 need a look of their own, with F1's merge and pull planted through the real stage.
---

## 3. scripts and hooks

# Fourth look at the scripts and hooks (edits 5e5564d to 018ebd6), 24 September 2026

**Overall: not passed.** The maker's counts are right: 166 planted tests, all passing on the new scripts, and 19 failing on the scripts the third look saw. The main change does answer most of what it was built for:
- a commit made without the gate is now judged against the last approved commit, and putting it right clears it;
- commits are settled once a later commit is approved;
- a rebased change finds its receipt again;
- the recheck is cheap.

But three findings must change:
- **1.** The route the text gives the owner for a wrong check does not work. After the owner's commit made with the gate off, every later commit is stopped for good.
- **2.** If the main line holds no approved commit, the gate quietly goes back to the old rule. It takes its checks from the last commit and compares the files with it. GitHub's merge button, which the text recommends, leaves the main line that way. A check loosened on GitHub, together with the log rewrite it would have stopped, then passes.
- **3.** Several places tell the owner there is only "one honest route" round the gate. These runs show more.

Nine findings should change and six are minor.

**Words used below.**
- A **stamp** is the line "Workshop-gate: approved <tree>" that the gate adds to a commit it passes. `<tree>` is git's name for the commit's exact contents.
- The **main line** is the chain of first parents. For a merge commit, the first parent is the branch the merge was made on.
- The **last approved commit** is the nearest commit on the main line whose stamp matches its own contents.
- The **recheck** is `recheck_commits.py`.
- The **planted-fault test** is `test_checks.py`.
- A **check-only commit** is a commit made straight on top of an approved commit that changes only checks, plus new receipts. It is judged by its own changed checks.
- To **retire** a planted test is to name it under "Tests retired" in a receipt.
- **GIT_REFLOG_ACTION** is a setting git gives to hooks while it merges, naming what is being merged ("merge side").

**How I worked.**
- I made no edits and no commits in /home/user/StoryTest, and wrote no files there. At the end its HEAD is still 35f2939 and `git status --short` still shows 30 entries, as at the start.
- I compared the live working tree with 018ebd6 using `cmp`: 117 files, 0 differ. No untracked live file is missing from the snapshot.
- All copies are under `.../scratchpad/r4-scripts/`.
  - `base` is a clone of the live history (35f2939), with the 018ebd6 files committed through the gate as its first gated commit. The gate printed "note: the commit gate is new in this commit … passed the planted-fault test brought in … All checks passed; committing." in 42.8 s, and stamped the commit "Workshop-gate: approved cb39a7c…".
  - Each experiment, e1 to e18, is a copy of `base`.
  - Where a commit had to arrive as it would from GitHub or from a machine without the gate, I made it in the copy with the gate off for that one command (`-c core.hooksPath=/dev/null`).
- Every receipt in my copies is a **simulated** stand-in, written by my helper `fill.py`. No reviewer ran.
- `hooktry.py` feeds commands to the copy's refusal hook the way Claude Code would.
- Every run had TMPDIR pointed inside `r4-scripts`.

## The counts

- **The new test on the new scripts:** `test_checks.py` from 018ebd6 printed "TOTAL tests: 166, failed: 0" in 1 min 52 s.
- **The new test on the old scripts:** `git archive 5e5564d` with the new `test_checks.py` put in printed "TOTAL tests: 166, failed: 19" in 1 min 54 s. The 19 are:
  - the rechecking kept-case neighbour;
  - "a gate file on disk asking for the staged checks is ignored" (its expected wording changed);
  - both put-right neighbours;
  - the merge -m stamp;
  - "a check change that carries the log";
  - both rebase neighbours;
  - the settled neighbour;
  - the "withdrawn" fault;
  - the planted-stage test (the old gate names "the last commit's planted-fault test"; the output is cut at 14 lines, so I saw only that wording);
  - the two typo-route tests;
  - six of the seven new hook commands.
- **New tests that pass on the old scripts too, so they show nothing about these edits (C15):**
  - the entry-12 and last-entry rewrites;
  - the first half of the fast-forward theory test;
  - the first half of the loosened-check test;
  - the "really withdrawn" neighbour;
  - the check-only neighbour;
  - the broken-check test;
  - `rm .git/workshop-gate-passed`.

  Most of these are neighbours or guards against future loosening, so passing on both is expected.

---

## Must change

**1. The stated route for a wrong check fails wherever the check-only commit is stopped. After the owner's commit made outside the gate, every later commit is stopped, and nothing clears it. New. Bears. Must change.**
- **Target:**
  - `references/checks-and-cases.md` line 48: "If even that commit is stopped … Only the owner may then commit the correction with the gate switched off; the next commit through the gate then needs a late review receipt".
  - `check_commit.py`: lines 26–34 (the note), lines 304–315 (the last approved commit's planted-fault test runs whenever the staged checks differ from that commit's), and lines 367–375 (a test that could not run is never retired).
  - `test_checks.py` lines 451–456: `fill_receipt` finds the form only by the words "wrote … :".
- **Defect:**
  - The checks and the planted-fault test always come from the last approved commit. A commit made outside the gate is never approved, so it does not change which checks run. The owner's correction is judged, at every later commit, by the same planted-fault test that stopped it.
  - The planted-fault test also depends on the exact wording of some messages from the checks it tests. Changing that wording is therefore impossible by any route.
- **Grounds (e1):**
  1. A check-only commit reworded the message of `review_receipt.py new`, from "wrote X: fill it in…" to "a receipt form is ready at X; fill it in…". Its receipt named the owner as reviewer. The gate printed "FAILED the last approved commit's planted-fault test … FAILED receipt_tests could not run / no receipt form was written: a receipt form is ready at …", and 19 "could not plant the fault" failures. A test that could not run can never be retired.
  2. As line 48 says, I then committed the change with the gate off (d1a4d6c; its receipt came with it). The next commit changed only one log line. It printed "note: the last commit the gate approved is 2ce383549; the 1 commit(s) after it were not approved … FAILED the last approved commit's planted-fault test, on the changed checks / FAILED receipt_tests could not run".

  This repeats on every commit until the change is taken back out. That commit needs no receipt, so there is nowhere to name a retirement.
- **Connection:**
  - This is the kinds-table row "A check or a step that stops honest work, or leaves no way through".
  - The route the text gives the owner turns one change that cannot be made into a stop on every commit.
  - The maker's reason for leaving D undone in part holds only for `check_commit.py` itself: git runs the last commit's copy of it, so the owner's correction to it does take effect. It does not hold for the rest of line 48.
- **Proposed change:**
  - Let a receipt that names the owner first also retire a whole group that could not run. Or: once the owner's outside commit has a late receipt naming the owner, let it become the commit the checks come from.
  - Make `test_checks.py` find the form by its path (`.claude/reviews/<16 hex>.md`), and keep the tests within each group apart, so that one planting failure does not make the whole group "could not run".
  - Rewrite line 48 to say exactly which stops the owner's route can clear.
  - Plant both: a reworded message in a check-only commit, and the owner's route after it.

**2. With no approved commit on the main line, the gate compares the files with the last commit and takes its checks from it. A GitHub merge commit leaves the main line that way. New. Bears. Must change.**
- **Target:**
  - `check_commit.py` lines 125–137 (`last_approved_commit` follows first parents only), lines 210–212 (`approved_commit or head_commit`) and lines 230–232 (the note).
  - `recheck_commits.py` lines 99–103 and 253.
  - The advice in `checks-and-cases.md` line 46: "On GitHub, merge a pull request with a merge commit".
  - The claims this breaks:
    - CLAUDE.md row 2;
    - README line 89 ("whatever it got wrong in the files stops the next commit");
    - SKILL.md line 228;
    - `check_commit.py` lines 18–22;
    - `refuse_check_bypass.py` lines 25–29.
- **Defect:**
  - GitHub's merge commit has no stamp. Its first parent is the main line as it was before the pull request: for the first pull request, the history before the gate; later, only more of GitHub's merge commits.
  - So the gate finds no approved commit on the main line, although the approved branch commits are in the history. It then goes back to the old rule: checks from the last commit, files compared with the last commit, and no planted-fault test.
  - Whatever a web edit got wrong in the files is never seen, and the next gated commit settles it for good.
- **Grounds:**
  - **(e4)** On a branch at 35f2939, I merged the approved build commit 2ce3835 with `--no-ff` and the gate off, as the merge button does. Next came a gate-off commit rewriting log entry 5, as a web edit would, and then a record committed through the gate. That commit printed "note: no commit in the history carries the gate's stamp for its own contents, so the checks come from the last commit … passed records … rechecked 2 commit(s) the gate did not approve, since the gate came in (no commit is approved) … All checks passed; committing."
    - `grep -c` finds the rewrite still there (1).
    - Afterwards the recheck printed "rechecked 0 commit(s) … TOTAL problems: 0".
    - The note is false: 2ce3835 carries a matching stamp.
  - **(e4b)** The same history, but the web edit also switched off the log comparison in `check_records.py` and rewrote entry 7, with a late receipt. It printed "passed records … All checks passed; committing." No planted-fault test ran. This is the first round's S1 route B and the third round's M3, back again.
  - Every planted test of this case starts from a stamped single commit (`copy_repository`), so none meets a main line without a stamp.
- **Connection:**
  - This is the kinds-table row "A check that passes while the thing is wrong", reached by the route the text recommends.
  - It is also the normal shape of this repository's work: a branch per session, merged on GitHub. So the round's main claim fails on the main line.
- **Proposed change:**
  - Count as approved a merge commit that holds nothing beyond the automatic merge of its parents, when each parent is approved or from before the gate. Or take the nearest approved commit by any path.
  - Make the note name the commit it used.
  - Plant it: a main line with no stamp, a merge made the way GitHub makes one, then an outside log rewrite and an outside loosened check. Both must be stopped.

**3. The owner-facing claims of "one honest route" are wrong. Bears. Must change.**
- **Target:** CLAUDE.md line 51 ("apart from that one honest route"); README line 89; the questions file line 95 (S10: "apart from one honest route").
- **Defect:** these say an honest mistake gets past the gate only through an outside change to the gate's own files.
- **Grounds:** findings 1, 2, 4, 5, 6, 7 and 11 below are honest routes. Each is either a stop with no stated way through, or a pass while something is wrong, and each was reached with ordinary commands or settings.
- **Connection:** the kinds-table row "A claim reported without its receipt". S10 asks the owner to decide on this claim.
- **Proposed change:** put right 1 and 2 and state the rest, or list each route in these three places.

## Should change

**4. During `git merge <branch>`, GIT_REFLOG_ACTION leaks into the planted-fault test's copies. A merge that brings in a check change then fails the planted tests for merges. New in effect. Bears. Should change.**
- **Target:**
  - `check_commit.py` lines 93–94 (the settings removed for copies leave out GIT_REFLOG_ACTION) and line 365;
  - `test_checks.py` lines 42–43 (the same list);
  - the readers of the setting: `check_commit.py` lines 179–189 and `review_receipt.py` lines 85–99.
- **Defect:**
  - The planted-fault test now runs whenever the staged checks differ from the last approved commit's, and so also during a merge. Before this round it ran only on a commit's own change.
  - Git keeps the outer setting for the test's inner merges ("merge feature"), so the inner gate misreads them.
- **Grounds:**
  - **(e2, branch named `side`):** `git merge` of an approved branch carrying a check change printed "FAILED the last approved commit's planted-fault test … FAILED gate, neighbour: a reviewed hook change, rebased … FAILED gate: a merge commit runs the gate, which finds the unreviewed commit it brings in".
  - **(e2, branch named `feature`):** the same merge failed "an honest merge of two reviewed commits goes through" and "a merge made with git merge -m carries the gate's stamp".
  - **Control:** the same test run on the same merged files printed "failed: 5" with `GIT_REFLOG_ACTION="merge feature"` and "failed: 2" without it. The two failures without it are the retired maps test (finding 5) and the planted-stage test, which fails in both runs because I ran the test directly.
  - **A way through:** finishing the stopped merge with `git commit --no-edit` avoids the leak (e2-finish). No text says so.
- **Connection:** the kinds-table row "a change (a fix) that makes a new error".
- **Proposed change:** remove GIT_REFLOG_ACTION, together with the other settings, from the environment given to the copies; plant a merge that brings a check change.

**5. A retirement does not travel with a merge or a rebase, and a merge has no receipt in which to name one. New in effect. Bears. Should change.**
- **Target:**
  - `check_commit.py` lines 346–356: `retired_tests` reads only the staged change's receipt;
  - the gate's advice at lines 383–388;
  - `checks-and-cases.md` section 3, step 5.
- **Grounds (e2):**
  - On a branch, a check-only commit raised `DESCRIPTION_LIMIT` to 4096 and retired "maps: a description over the length limit", with theory-checker as reviewer; maps tests need no owner. The gate printed "retired in the receipt: maps: … All checks passed".
  - The main line then moved on by one record commit.
  - The merge, finished with `git commit`, printed "review receipt: not needed (no reviewed file changed) … FAILED maps: a description over the length limit … name the test … under '## Tests retired' in the review receipt".
  - By reading the code, a rebase is the same.
  - The branch's committed `test_checks.py` still holds the retired test, so it has to be retired again at every later change to a check.
- **Connection:** the kinds-table row "A check or a step that stops honest work, or leaves no way through".
- **Proposed change:**
  - Read "Tests retired" from the receipts of every commit since the last approved one, with the same owner rule.
  - Say that a retired test is removed or changed in `test_checks.py` in the same commit.
  - Plant a merge and a rebase of a branch that retired a test.

**6. A check-only commit may carry any file added under `.claude/reviews/`, and that file is judged by the changed checks. Bears. Should change.**
- **Target:**
  - `check_commit.py` line 206: `added_receipts` takes any added path there, kept reports included;
  - lines 213–214 and 248;
  - CLAUDE.md row 3 ("By itself within one commit").
- **Grounds:**
  - **(e10)** One commit added a 180,890-byte file, `.claude/reviews/kept/2026-09-25-long-report.md` (filler text I made up), and added that path to `LARGE_RECORDS_ALLOWED`. It printed "note: this commit changes only checks … passed no book files … passed the last approved commit's planted-fault test … All checks passed".
  - **Control (e10c):** the same file alone printed "FAILED no book files … a large text file".
  - This is the maker's own pattern for a long kept record, so an honest agent could take it.
  - From reading the code: in the same way, the receipt check that judges a check-only commit is the one that commit changes.
- **Connection:** B, reopened for the files the exception lets through.
- **Proposed change:**
  - Let a check-only commit carry only receipts, by name (`.claude/reviews/<16 hex>.md`), or run the last approved commit's checks on everything else it carries.
  - State in CLAUDE.md that the receipt check of a check-only commit is guarded only by the planted faults.
  - Plant the case of e10.

**7. Nothing checks `.claude/settings.json`. A settings change that drops the hooks the gate relies on passes. Older than these edits. Bears. Should change.**
- **Target:**
  - `check_commit.py` line 85 (settings.json counts as a check, but no check or planted test ever reads it);
  - CLAUDE.md rows 1 and 2 ("By itself: … protect_frozen_files.py before an edit"; the gate "switched on at session start");
  - README line 89.
- **Grounds (e18):** settings.json was rewritten to hold a permission list and only the after-commit hook, with its receipt. This dropped the SessionStart hook, the frozen-file hook and the refusal hook. It printed "note: this commit changes only checks … passed the last approved commit's planted-fault test … All checks passed", in 44 s.
- **What follows:** in a fresh clone nothing switches the gate on, and no Claude hook stands in front of the frozen files.
- **Connection:**
  - This is the kinds-table row "A check that passes while the thing is wrong".
  - The route is honest: the `update-config` and `fewer-permission-prompts` skills in this session write that file.
- **Proposed change:** add a check that the three hooks are registered with their matchers, with planted faults. Those tests are then protected, so only the owner could retire them.

**8. The notes "for a person to look at" and "tell the owner" vanish at the next approved commit, and nothing records that anyone looked. New. Bears. Should change.**
- **Target:**
  - `recheck_commits.py` lines 27–33 and 180–188;
  - `session_start.py` lines 127–141;
  - the claims: CLAUDE.md line 51, SKILL.md line 228, `checks-and-cases.md` line 38, README line 89, S10.
- **Grounds (e12):**
  - A reviewed hook change was rebased (it lost its stamp).
  - Session start printed "For a person to look at: commit 625aa9c7f changed the gate's own files …".
  - The next commit passed, with that note among its passing lines.
  - The next session start said nothing of it.
  - By reading, book files noted this way go through the same code and vanish the same way.
- **Connection:** U1 answered by a note that the next commit, whoever makes it, clears.
- **Proposed change:** keep such commits listed at session start until a later receipt names who looked (the owner, for the gate's files and book files). Or say plainly in all five places that the note is shown only until the next commit is approved.

**9. A withdrawal is judged by sets of lines, so a change that only reorders lines passes as "withdrawn". Part of the answer to U3 and C. Bears. Should change.**
- **Target:** `recheck_commits.py` lines 138–150.
- **Grounds (e7):**
  - A commit made with the gate off swapped steps 1 and 2 of the plot procedure.
  - A late receipt said "not passed (withdrawn in this commit)", and nothing was withdrawn.
  - The gate printed "passed earlier commits … All checks passed; committing." The swapped steps are still there, and the commit is now settled.
- **Proposed change:** test the withdrawal by whether the commit's own difference still applies in reverse to the staged files (`git apply --check -R`). Plant a reordering and a duplicated line.

**10. The fingerprint ignores where a line goes, so a reviewed line moved to another section keeps its receipt. Part of the answer to U5. Bears. Should change.**
- **Target:** `review_receipt.py` lines 7–12 (the note says the fingerprint comes from "the exact change") and lines 136–149.
- **Grounds (e6):** the same added line printed fingerprint `6816c3e2da2716d7` both under "Traps" (line 161) and under "Where to look, and when" (line 26).
- **Connection:** the note says the point of the fingerprint is to catch "a fix made after a review", and moving a line is such a fix.
- **Proposed change:**
  - Keep one unchanged line either side of each change (`--unified=1`, dropping the "@@" lines). That survives a rebase over edits elsewhere in the file. It will again fire when an edit upstream touches a line right next to the change.
  - Plant the case: a line moved after its review.

**11. An honest `git pull` that makes a merge commit is not seen as a merge, and is stopped for a receipt covering all the pulled work. Older than these edits. Bears. Should change.**
- **Target:** `check_commit.py` lines 179–189 and `review_receipt.py` lines 85–99. When git runs pre-merge-commit, the file that names the commit being merged (MERGE_HEAD) is not written yet, and under `git pull` the setting names "pull …", not "merge …".
- **Grounds (e3):**
  - A pull of two reviewed commits printed "FAILED review receipt / no review receipt .claude/reviews/08bfc7089d98c62b.md … for this change to: .claude/skills/genre/SKILL.md, .claude/skills/story-world/SKILL.md … Not committing merge".
  - `git commit --no-edit` then passed, and the merge was stamped.
  - A pull of a single reviewed commit passed only because the whole pulled change equalled that one commit, so its receipt matched. The recheck was not given the pulled commits at all.
- **Proposed change:** read pull actions too (from FETCH_HEAD), or refuse with the plain advice "finish with git commit". Plant a pull.

**12. The planted log rewrites all touch the first line of an entry. Answers I in part. Bears. Should change.**
- **Target:** `test_checks.py` lines 277–288.
- **Grounds (e9):**
  - A check-only commit made the log comparison look at each old entry's first line only. It printed "passed the last approved commit's planted-fault test … All checks passed" (45 s).
  - The next commit rewrote an indented line of old entry 29. It printed "passed records … All checks passed".
- **Proposed change:** plant a rewrite of an indented line inside an old entry that runs over several lines (entry 27, 29 or 30).

## Minor (each bears)

- **13. The kept record exempt by name can grow without any check (G, in part: the reason is not sound).**
  - **Grounds (e13):** I appended 141 KB to `kept-cases/runs/2026-09-24-before-entry-27.md` (159,768 bytes became 301,159). It printed "passed no book files / NOT RUN copying from books / no book text here; the review receipt must say what book text a change adds / review receipt: not needed". So the promise in the NOT RUN line is not kept.
  - **Why the reason fails:** the maker's reason says why the file is large, not why every later change to it is exempt. `kept-cases/runs/` is also outside the receipt's scope.
  - **Proposed change:** exempt the file by a fingerprint of its contents, so that any change to it is size-checked.
- **14. The advice after a plain revert names a command that fails.**
  - After a plain `git revert` of a reviewed commit, the gate prints "put it back: git checkout HEAD -- <receipt>".
  - Running that printed "error: pathspec '.claude/reviews/28808e76b0113094.md' did not match" (e5).
  - The command should name the last approved commit.
- **15. A commit made with the gate skipped can get a stamp, contrary to `prepare-commit-msg` lines 10–12.**
  - A `git commit` with nothing staged ran the gate, which passed and left `.git/workshop-gate-passed` behind; git stopped at "nothing to commit".
  - A later `git commit --no-verify --allow-empty` got "Workshop-gate: approved cb39a7c…" (e16).
  - I found no harm, since the contents are ones the gate passed.
- **16. Two gaps in the refusal hook.**
  - `git config core.hooksPath "/tmp/some-old-copy/.githooks"` is let through, while the same command without quotes is refused. `refuse_check_bypass.py` lines 135–138 accept any quoted path ending in `/.githooks`. This came in with the fix for F.
  - `GIT_CONFIG_PARAMETERS="'core.hookspath=/dev/null'" git commit -m x` is let through, although the note at lines 12–14 says this route is refused. The quoted value becomes its own word, so the git command is never found (`git_command_reading.py` line 41). This is older than these edits.
- **17. The Book-text rule reads the staged source register, so it can be switched off in the same commit (review_receipt.py lines 171–177).**
  - **Grounds (e17):** one commit dropped John Truby's two rows from `sources/README.md` and added a genre line naming Truby, with no "Book text" line. It printed "review receipt: … is complete".
  - **Control:** with the register as it was, it printed "say in 'Book text:' what book text the change adds", and exited with 1.
  - **Proposed change:** read the register from the last approved commit, as the allowed-titles check now does.
- **18. A refused retirement is still printed as if it had been made.** With a reviewer line "theory-checker (the owner agreed in chat)", the gate printed "retired in the receipt: records: hidden text in the log" just before "FAILED records: hidden text in the log" (e15a).

## The findings listed for me

- **A:** answered in content for the routes it named:
  - a restore after an outside edit clears the stop (planted);
  - a rebase keeps its receipt (planted);
  - the revert route is in the text;
  - commits are settled (planted). In e8, 60 reviewed outside commits were rechecked in 4.3 s with 0 problems.

  New faults came in with the answer: 1, 2 and 5.
- **B:** answered. The check change that carries the log is planted, and that test failed on the old scripts. Finding 6 is a narrower route that remains.
- **C:** answered for added and removed lines, with both cases planted. Not answered for reorders (finding 9).
- **D:** the claim is now scoped, but the stated route fails (finding 1).
- **E:** answered, but not planted.
  - e15a: a protected test retired with theory-checker as reviewer was stopped.
  - e15b: the same retirement with "the owner, with theory-checker" passed.
  - Session start lists retired tests.
- **F:** answered for its commands, all planted. Of 42 further commands I fed the hook, ordinary ones were let through: here-document commit messages, `cat .git/workshop-gate-passed 2>/dev/null`, `ls -la .githooks/ 2>&1`, `git commit -am`. Finding 16 lists what it still misses.
- **G:** answered in part (finding 13).
- **H:** answered, not planted. In e14 the gate printed "not … named in sources/README.md as it was in 2ce383549".
- **I:** answered in part (finding 12).
- **J:** answered. The stage runs for real in the new test; inside the test's own copies it prints "not run".
- **K and m1:** answered, and planted. The merge finished after `git pull` carries its stamp (e3).
- **L:** the texts are corrected (SKILL.md line 228; `checks-and-cases.md` line 46).
- **M and Q:** answered in practice, at about 70 ms per commit (e8).
- **N:** answered. The test's temporary folder was empty after my run.
- **O:** answered. The count is now 166.
- **P:** answered in part (finding 8).
- **Brief check finding 3:** found right. The recheck no longer reads the setting. `check_commit.py` still honours it only in a `workshop-test-` folder directly inside the temporary folder. The planted setting test and the planted-stage test pass.
- **U1:** answered as a note (finding 8).
- **U2:** answered (planted; e8).
- **U3:** answered in part (finding 9).
- **U5:** answered (planted), at the cost of finding 10.
- **U7:** answered. The message, the skills with no kept cases and the owed skill are planted; both tests failed on the old scripts.
- **m5:** answered (planted).

## The maker's parts left undone

- **The copying check is not rerun on each commit the gate did not approve:** sound as a stated limit. It is incomplete, though (finding 13). Where the books are present, the recheck could run the check on each commit's added lines.
- **D, in part:** sound for `check_commit.py` itself. Not sound for the rest of line 48 (finding 1).
- **S10 (b):** sound; it is the owner's choice. But the text around it overclaims (finding 3).
- **G, in part:** the reason is not sound (finding 13).
- **Not planted:** I tried the retirement rules by hand, and they work (E, above). I tried the Book-text rule reading the staged register, and it can be switched off (finding 17).
- **Counts:** confirmed (above).
- **Kept-case notes:** not my area.

## Not checked

- Real GitHub. I simulated the merge button and web edits with gate-off commits in local copies.
- `git am`, worktrees, an interactive squash, `git merge --squash` as a way through for finding 5, and an amend of a commit the gate did not approve.
- Windows and macOS.
- The hooks in a live Claude Code session. I fed them input the way a session would.
- The copying check with the real books. It printed NOT RUN in every copy.
- The prose skills beyond the lines quoted here, and the kept cases.
- Whether `test_checks.py` has other "could not run" dependencies besides `fill_receipt`.

## Side effects

- Nothing was written to the live repository.
- My temporary files are all under `r4-scripts`.
- Folders named `/tmp/workshop-*` were created at 17:51–17:52 while I was idle, so they belong to another run. I left them.

## Verdict: not passed

- **Must change:** 1 (a route for the owner that works, and a planted-fault test that does not depend on message wording); 2 (the main line without a stamp); 3 (the "one honest route" claims).
- **Should change:** 4 to 12.
- **Minor:** 13 to 18.

The edits made for these need a review of their own.
