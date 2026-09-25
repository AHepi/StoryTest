# The sixth look at the error-correction build: the theory-checker's and the use-tester's reports, 24 September 2026

What this is: two of the four reviewers' reports, word for word as each agent returned it; the other two and the verifier's check are in `2026-09-24-build-sixth-look-scripts-copy-verifier.md`. They looked at the edits answering the fifth look (snapshot commits c52f191 to 26bf4fd); the reviewers and the verifier made no edits, and every experiment ran in their own copies. The theory-checker and the use-tester ran first; the run was stopped when the owner asked about its cost, and resumed at the owner's word with the scripts reviewer, the copy-checker and one verifier (log entry 33). The briefs, their four checks and the copy script every reviewer used are in `2026-09-24-build-sixth-look-briefs.md`. How each finding was answered is in the build's review receipt. Kept for log entry 33.

---

## 1. theory-checker

# Sixth look: theory-checker report (Brief A)

I worked from the shared part and Brief A. The live repository is `/home/user/StoryTest`; the snapshot is 26bf4fd, which matches the live tree (checked by `diff -r` against a copy made with the copy script). I read all four owner theories before the passages that cite them. Line numbers are as in the live tree.

**The theory, one line each, read first**
- **Gap line 57:** surprise is a gap you didn't know was there: "you thought you understood and you were wrong".
- **Gap line 59:** the bomb that simply goes off gives fifteen seconds of surprise. Shown first, it gives fifteen minutes of suspense.
- **Gap line 47:** in our world a dragon attack is news; in a world full of dragons it might be weather.
- **Gap line 61:** plot schedules facts about the world too (*Planet of the Apes*).
- **Gap Part 2 section 4 and principle 5:** every open question carries a promise, and emphasis sets which one.
- **Implied World lines 12, 20 and 36:** the baseline is the real world plus the genre's habits. The audience assumes the world works like theirs unless told otherwise. A fantasy that is medieval Europe with dragons rides on the genre's defaults.
- **Anticipation line 25:** Shock is a side rung. The audience knows nothing; the threat arrives without warning (the jump scare).
- **Anticipation line 84:** a jump scare after real dread works as a release valve; without dread it is a flinch.
- **Anticipation lines 67 and 69:** *Psycho* breaks a guarantee early, and after that every threat is real. Break one guarantee, not all.
- **Bond line 84:** care deepens when an unexpected act turns out to have been "in them all along". It breaks when the act contradicts who they have been "without the story earning it".

---

## Findings

**M1. Must change: "foreshadowing is a promise" is credited to the Gap theory without the Q7 label.**
- **Target:**
  - `/home/user/StoryTest/.claude/skills/plot/references/suspense-and-fear.md` line 20: "Egri's *foreshadowing* *(built)* is a promise of a coming clash (Gap principle 5)". This line was edited this round, for V15.
  - `/home/user/StoryTest/.claude/skills/plot/references/scenes.md` line 18 has the same stretch with no label: "makes a promise (a set-up to be paid off)".
- **Defect:** the workshop's reading (Q7) is credited to the theory and left unlabelled. This fault is older than this round's edits.
- **Grounds:**
  - Term sheet 1.1: stretching *promise* "to set-ups is the workshop's reading, Q7".
  - `reveals-and-withholding.md` line 74 in the same skill: "calling a set-up or a foreshadowed clash a promise is the workshop's stretch of it … (owner question Q7 is open on this)".
  - Q7 (`/home/user/StoryTest/22 Questions - meanings only you can settle.md` line 69) tells the owner: "Both are flagged as the workshop's."
  - Term sheet line 7: while a question is open, never write its stopgap as settled.
  - C12's second error was this same kind: "credited to the theory the promise's stretch to set-ups".
  - A search of the copy's history shows both lines have been there since 35f2939.
- **Connection:**
  - Two modules of the plot skill give different credit for one claim, and what the owner is told in Q7 is false.
  - If the owner answers Q7 with (b), step 2 of the owner-answer procedure searches for "Q7" and "workshop's reading". Neither search finds these lines.
- **Fix:** label both lines, for example "(Egri's word; reading it as the Gap theory's promise is the workshop's stretch, Q7)".

**M2. Must change: C1 names the wrong looks and entries for the order phrases.**
- **Target:** `/home/user/StoryTest/27 Corrections.md` line 41: "apart from three phrases the fourth and fifth looks found, each carried over from the break test's own wording and reworded (entries 31 and 32)".
- **Defect:** the looks and entries are misattributed.
- **Grounds:**
  - C1's own lines 38–40 and file 26 line 133 say: the third look (entry 30) found "still", the fourth look (entry 31) found "weakened", and the fifth look (entry 32) found "its shortness…".
  - In the snapshot, "B still shows the ramp (B" is counted 1 in 7812119 and 0 in 0f14d0a ("state after the third look's answers (entry 30)").
- **Connection:** this is a false statement in a record changed this round, and it contradicts file 26. It should read "the third, fourth and fifth looks … (entries 30, 31 and 32)".

**S1. Should change: "So does a jump scare" is stated as a category, against the telling test.**
- **Target:** `/home/user/StoryTest/.claude/skills/plot/references/reveals-and-withholding.md` line 30: "…That is the telling test. The bomb that simply goes off passes it … So does a jump scare."
- **Defect:** a way of delivering a threat is exempted as a category, though the test turns on what arrives.
- **Grounds:**
  - Anticipation line 25 defines the jump scare by the audience's knowledge ("Nothing: it arrives without warning"), not by whether it makes sense.
  - A near neighbour: in a realist drama, a ghost (or a dragon) bursts out as a jump scare, never shown before.
  - The test fails it ("nothing the audience has makes sense of them"). The sentence passes it.
- **Connection:** two sentences in one paragraph give opposite answers on one case. This is the kind of fault V3 found. Scope it, for example: "So does a jump scare by something the audience already has (a cat, the killer it knows is loose)".

**S2. Should change: the dragons example is a reviewer's own walked case, the fault C12 recorded last round.**
- **Target:**
  - reveals-and-withholding.md line 30: "Dragons that burn a village in the middle of a story whose world has seemed like ours fail it".
  - C12 (`27 Corrections.md` line 132) records "with the dragons as the case it rules out".
- **Defect:** a worked example is borrowed from a test.
- **Grounds:**
  - It is V3's walked case (from the fourth look's F6).
  - C12's fourth error lists "the example was the reviewer's own walked case" (the grandmother; fourth look F13: "Any later walk of it can only agree"). That example was dropped in entry 31.
  - The rule card's section 4 (`writing-rules-and-rivals.md` line 44) was never extended to a reviewer's walked case.
  - The kinds row "A test that can only agree".
  - This look's brief asks for exactly this case to be walked.
- **Connection:** the stage C12 named was not changed, so the fault came back. I walked near neighbours instead (below). The history in the rule card's case (line 9) is a record, so it can keep the dragons.

**S3. Should change: an agent's skipped gate is not a tripwire under line 218 but is one under line 215 (V8 answered only in part).**
- **Target:**
  - `/home/user/StoryTest/.claude/skills/error-correction/SKILL.md` line 218: "A stop that only asks for a late receipt is not one."
  - `/home/user/StoryTest/.claude/skills/error-correction/references/checks-and-cases.md` line 61, the same.
- **Defect:** for one case, the skill's two lists give opposite answers.
- **Grounds:**
  - SKILL.md line 215 says a tripwire fires when "a kind of error got past the catch that the corrections file names for it".
  - Kinds row (`27 Corrections.md` line 28): a commit that skips the gate is "never seen in the repository", and the Claude hook catches "usual spellings only".
  - CLAUDE.md rule 1 is never bent.
  - V8's fix asked for "or a change to a reviewed file with no review at all". The lead applied use-tester 6's narrower version.
- **Connection:** take an agent that commits an unreviewed skill change past the hook, using a spelling the hook misses. The next stop "only asks for a late receipt", so line 218 says no correction is recorded, while line 215 says one is. The kinds row would stay "never seen".

**m1. Minor: two climax clauses state Egri's rule without his name.**
- **Target:** reveals-and-withholding.md line 30: "since the climax must come from the characters' own acts" and "at the climax a rescue from outside fails even when it is set up".
- **Defect:** a book's rule is given without its credit. Only the pointer carries it.
- **Grounds:** `structure-and-conflict.md` line 98 credits it: "(Egri *(built)*)".
- **Connection:** a reader of section 2 takes it as settled law. Add "(Egri)".

**m2. Minor: the rereading route dropped out of section 1.**
- **Target:** reveals-and-withholding.md line 16: "A surprise on its own lasts seconds … It does more when, for instance, it breaks a guarantee early … or starts new suspense".
- **Defect:** the old "reread everything before it" route is no longer among the examples.
- **Grounds:** Gap line 61, *Planet of the Apes*, a surprise whose work is rereading; the module's own section 4 (the reversal).
- **Connection:** "for instance" keeps the list open, but the theory's own case is the one left out.

**m3. Minor: S10 was not brought into line with V20.**
- **Target:** questions file line 95: "a check loosened in one commit, which then judges the next".
- **Defect:** it keeps the wording V20 corrected.
- **Grounds:** checks-and-cases line 51 now says "once a commit carrying it is approved, the commits after are judged by the loosened check".

**m4. Minor: one break-test item is not applied, and the table misquotes another.**
- **Target:** file 26 line 93 and line 132 ("each is now applied"); `/home/user/StoryTest/.claude/reviews/kept/2026-09-24-catch-break-test-applied.md` lines 38, 41 and 55.
- **Defect:**
  - N20 holds_it: the paper letter is held by the leaf picture "and by the F on the carriage". File 26 names only the leaf picture, yet table line 38 says both sit there.
  - Table line 41 reports the test as saying "a further route". The test's holds_it and new_wording say "second route"; its pulls field says "third". The test contradicts itself here, and the file does not say so.
- **Connection:** "every field is applied" holds in substance, with this residue.

**m5. Minor; does not bear yet: four times or five?**
- **Target:** kinds row, `27 Corrections.md` line 22: "(entries 29 to 32, five times)". Against file 26 line 132: "Four earlier rounds said every finding was applied".
- **Grounds:** in the snapshot, file 26 carries the claim in four versions: 1e92459, 7812119, 0f14d0a and 4430f36 (entries 29, 29, 30 and 31).
- **Test that settles it:** list each record that made the claim. If only four exist, the row is wrong (minor).

**m6. Minor: two wording slips in the project story.**
- Entry 32 (`/home/user/StoryTest/StoryTest - project story.md` lines 153–154) says "stress test" beside "break-test", against one word for one thing.
- The status line at line 13, "209 tests, all passing, 23 of them fail: … on the scripts as the fifth look saw them", reads as a contradiction until its last clause.

**m7. Minor: C15's count of new tests that pass on the old scripts is stale.**
- **Target:** `27 Corrections.md` line 161: "three new tests pass there too".
- **Grounds:** I piped `git config core.hooksPath "$PWD/.githooks"` to c52f191's `refuse_check_bypass.py` in my copy. It let the command through both from the top folder and from `sources/` (exit 0, no deny). The live hook denies only the second.
- **Connection:** the new neighbour test (top folder, let through) passes on the old scripts too, so it is at least four. The full count is Brief C's to settle.

**m8. Minor: the refusal hook's note undercounts what is not stopped.**
- **Target:** `/home/user/StoryTest/.claude/hooks/refuse_check_bypass.py` line 30: "Two things are not stopped that way".
- **Grounds:** section 2 (lines 53–58) also lists a book file (only noted) and the other line's log entries after a conflicted GitHub merge (kept on trust).

**m9. Minor: "B's gaps" in file 26's short answer.**
- **Target:** file 26 line 29: "Most of B's gaps weaken a payoff".
- **Defect:** in a write-up to the Gap theory's owner, *gap* is used in none of the term sheet's three senses (section 3: say which sense at first use).
- **Fix:** "B's missing set-ups".

**m10. Minor; does not bear yet: the jump-scare-in-prose stall is not recorded.**
- The lead's account says this stall is "left open, recorded". Nothing in the repository outside the kept reports records it, and entry 32's "Not yet done" does not list it.
- It settles if the build's receipt records it.

**m11. Minor: the word list's "Last approved commit" is narrower than the rule.**
- **Target:** project story line 77: "a merge made on GitHub with no conflict that joins approved work".
- **Grounds:** the check_commit.py and recheck notes cover any merge made without the gate that is git's automatic merge of approved parents, or of parents "from before the gate came in".

---

## The fifth-look findings in my area

**Theory-checker**
- **V1:** answered, with the residue in m4. **V2:** answered.
- **V3:** answered, but the answer made S1 and S2. **V4:** answered, residue m1.
- **V5:** answered. I checked SKILL Words, CLAUDE.md row 2, README, the kinds row, and the notes in check_commit, recheck and the refusal hook.
- **V6:** answered: "those known so far", six items added, no text left claiming completeness. Residue m8.
- **V7:** answered.
- **V8:** in part; the missing part is S3.
- **V10:** answered. **V11:** answered. **V12:** answered: the fingerprint record exists and C13 matches it.
- **V13, V14:** answered.
- **V15:** answered, but its own line carries M1.
- **V16:** answered, apart from M2 and m5.
- **V17, V18:** answered. No "most recent" or "by any path" is left outside entry 31, which stays as written.
- **V20:** answered in checks-and-cases; S10 not brought into line (m3).
- **V21:** answered. **V22:** kept as untried, with its test (line 66).

**Use-tester**
- **6:** answered as V8, with the same residue (S3). **7, 10, 11:** answered.
- **Stall items:** genre habits as given, story facts, a frozen theory the owner meant to revise, a typo made on GitHub, and session start and the planted-fault test are all answered. The jump scare in prose is open and unrecorded (m10).

**Copy-checker D1:** answered. `--run-length 6` is accepted by overlap_check.py (line 159), and no `N=6` is left outside the kept records.

## Marks on new or changed rules
- **Bare arrival defined by the telling test:** held. It gets the theory's cases right: the unshown bomb (Gap line 59), dragons in a dragon world (Gap line 47), minimal departure (Implied World line 20), and medieval Europe with dragons carried by genre (Implied World line 36). It is held if the audience knows the genre before the arrival: "a world like ours" in the dragons example reads right only for a non-fantasy genre.
- **"So does a jump scare":** loose (S1).
- **Dragons example:** held as a case, but borrowed from a reviewer's walked case (S2).
- **Climax-threat clause:** held by F6's climax dragons, and labelled. Its "not enough" half is Egri's rule without his name (m1).
- **Rescue clause:** held, and labelled.
- **Character reveal is never exempt:** held (Bond line 84, "in them all along"; Bond's limits of care, "They believe what they see").
- **Section 1, "on its own lasts seconds":** held for the bomb (Gap line 59, Anticipation line 41); "on its own" is loose (m2).
- **Step 4 names the exemption:** held. **"Surprise by default" trap:** held.
- **Owner-answer step 3:** held (term sheet line 7; the kinds row, first line).
- **Tripwire exception:** held for a frozen edit, a rewritten entry, a deleted receipt and a loosened check. Loose on an agent's skipped gate (S3).
- **"Cannot do" list as those known so far:** held.
- **Rivals:** none new.
- **Worked examples:** none from a kept case or a trial answer. Kept case 06's dragons are about departure against breach, not planting.

## Checked and found right
- **Quotations are word for word:** "thought you understood and you were wrong" (Gap line 57), "real dread" (Anticipation line 84), "the real world plus the habits of the genre" (Implied World line 12).
- **Pointers land:** sections 1 and 6, `structure-and-conflict.md` section 7, suspense-and-fear section 5, and term sheet section 13 item 9.
- **The theory's cases, walked:** the bomb both ways, the Lewton bus, *Psycho*, Joffrey, *Chronicle*, "the door dilated", Gap lines 47 and 61, and Implied World lines 12, 20 and 36.
- **Near neighbours, walked:** a mugger or a tsunami (exempt, right); a ghost jump scare in a realist drama (S1); dragons first seen mid-story in a medieval-Europe fantasy (exempt by genre, right); a rescue at the climax (right); a character reveal (right).
- **File 26 against the break test, field by field:** I made my own list before opening the table. The sentences changed this round pass the stock-note test and the flip, and no order words were found in them.
- **Other skills:** the texts of the gate's description agree with each other and with the scripts' notes, apart from the findings above. character `change-and-growth.md` section 8 and the genre detective profile agree with the planting clauses.
- **Machine checks:** `run_all_checks.py --skip-books` in my copy printed "RESULT: no check failed", with copying NOT RUN.

## Not checked
- `test_checks.py` and `test_the_gate.py`, and the counts, beyond the $PWD neighbour (m7).
- Copying against the books.
- Kept cases, and the trial's second half.
- What the scripts do, beyond their notes and one hook run.
- Real GitHub, Windows, and a live session.
- Whether the plan came before the changes.

## What I left behind
- In `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/r6-theory-checker/`:
  - `copy1`: made by the copy script; it has no remotes, and the gate is on in that copy only;
  - `copy1.log`;
  - `snap`: an archive of 26bf4fd;
  - `oldhook`: c52f191's refusal hook and its helper.
- The `/tmp/workshop-test-*` folders are dated 19:49–20:00, before my copy finished at 21:13, so they are not mine.
- The live repository: HEAD is 35f2939, `git status --short` shows 30 entries, and `core.hooksPath` is `.githooks`. I ran nothing there that writes.

## Verdict: passed after changes
- **Must change:** M1 (label the Q7 stretch in suspense-and-fear line 20 and scenes.md line 18) and M2 (C1 line 41: "the third, fourth and fifth looks … (entries 30, 31 and 32)").
- **Should change, to record as open:** S1, S2, S3.
- **Minor:** m1 to m11.

## 2. use-tester

**Use-tester, sixth look: edits c52f191 to 26bf4fd, Brief B**

This report talks about the trial of the process. Keep it only in `.claude/reviews/kept/`, and never paste it into a receipt outside that folder: the trial's copy leaves out only `kept/`.

**Where I worked.** All work was done in `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/r6-use-tester/`.
- `base` was made with the lead's copy script. Its commit 5b8c37a was stamped and passed the planted-fault test it brought in. Its tree is the same as snapshot 26bf4fd, apart from the one simulated receipt; I compared the two with `ls-tree` and `diff`.
- Two bare repositories stand for GitHub: `github.git` and `github2.git`. Commits "made on GitHub" were made in `gh`, `gh2` and `gh3`, with hooks off.
- Every receipt is SIMULATED. My helper `fill.py` wrote them.

## Findings

**U1. GitHub's own conflict merge (and Update branch) turns the two-sessions route round, and the gate's advice then rewrites an approved entry on main without anyone seeing it.**
- **Target:**
  - `checks-and-cases.md` line 42: "Keep the main line's entries … After a merge made on GitHub, the next commit is judged against the main line, so that resolution goes through, and renumbering the main line's entries is stopped".
  - Line 61: a rewritten entry "goes back by itself: copy the entry's text from the last approved commit".
  - Line 64: the wrong-check route.
  - `check_records.py` line 150 ("put it back").
  - CLAUDE.md line 42.
  - `test_the_gate.py` lines 788–822, which model the conflicted merge with main as its first parent.
- **Defect:** GitHub's "Resolve conflicts" editor and its "Update branch" button merge main *into the session branch*, so the session branch is the first parent. If the session carries on from that branch, three things go wrong:
  - the natural resolution the text asks for is stopped;
  - both the gate and section 2 then tell the agent to copy the session's own entry over main's approved one;
  - the pull request's merge then counts as approved, so the rewrite reaches main and nothing sees it.
- **Grounds:**
  - `sB`: A's pull request was merged, then B's conflict was resolved the natural way (A keeps 33, B's entry becomes 34) in merge 8a7d362, whose first parent is b. Session start printed "FAILING: records … log entry 33 has been changed since 68c6b7dfa". The next commit printed the same, then COMMIT STOPPED.
  - `sB2`: I followed the advice (entry 33 back as B's text, A's moved to 34). It printed "All checks passed", stamped edcf9f8. I merged the pull request with the merge button (ef925f3).
  - `sNext`: `recheck_commits.py --last-approved` printed ef925f3 itself. Session start said "Machine checks: none failing". Commit 8e602ff was stamped. Main's approved entry 33 now holds B's text (checked with `git show … | grep "^33\."`).
  - `sB4`: the wrong-check route (a branch from 68c6b7d, then the session line merged in) printed "FAILED records … log entry 33 has been changed", so it is stuck in this shape too.
  - Way through, not stated for this shape: `sB3` rebased onto main and renumbered its own entry; 33067c7 was stamped. This needs a force-push.
  - Neighbour, quiet as expected: Update branch with no conflict (`sC`, d9762ba counted as approved; the next commit passed).
- **Connection:**
  - The fifth look's finding 1 ("following the gate's own advice rewrites another session's entry") is answered only for merges made through the gate and for commits on main. The missing part is this finding.
  - "Main line" is used in two senses: git's first-parent line, and GitHub's main branch.
  - The planted test confirms the fix on the shape the fifth look simulated, not the shape GitHub makes (kinds row "a test that can only agree").
- **Grade:** bears. **Must change.** Line 42 is false as an agent will read it, for GitHub's own conflict merges whenever work carries on from the branch. Say:
  - that GitHub's editor and Update branch make the session branch the first parent;
  - not to follow "put it back" there, but to rebase onto main and force-push (or not to carry on from that branch);
  - add the shape to the planted tests.
- **Not run on real GitHub:** the parent order is taken from GitHub's documented behaviour ("merges the base branch into the head branch"). Test that settles it: on a real pull request, press Update branch, then run `git log -1 --format=%P`.

**U2. An approved commit rebased with its contents unchanged keeps its stamp and settles the commits beneath it unseen. That includes the text's own route for the owner's correction to a broken gate script.**
- **Target:**
  - `checks-and-cases.md` line 36 ("a … rebase or cherry-pick that goes through without a conflict … carry no matching stamp"; the SKILL.md table at line 228 rightly adds "and changed the contents").
  - Line 38 ("a book file added, even if later removed").
  - Line 58.
  - Line 66 ("brought in with `git pull --rebase` … The next commit through the gate then needs late receipts").
  - CLAUDE.md line 44 ("A book file added without the gate is noted until the next approved commit").
  - `recheck_commits.py` lines 9–11.
- **Grounds:**
  - `v22`: local commit L1 was stamped. On GitHub came a typo in `check_commit.py` (5be916c), then the owner's correction (1dde147). After `git pull --rebase`, the rebased L1 had its old contents, kept its stamp and counted as approved. The next commit printed "rechecked 0 commit(s) … since the last approved commit, a2f4c1c9b". No late receipt was asked for, and no gate-files note appeared.
  - Then a stand-in `.epub` was uploaded and deleted on GitHub (9a34231, c28cec6) and the local work was rebased on top. `recheck_commits.py` printed "rechecked 0 … TOTAL problems: 0", and session start showed nothing.
  - Neighbour: a fresh clone of the same GitHub history (`v22ff`) printed 2 problems and 3 notes, including "commit 9a34231ae added Story craft (stand-in).epub, which looks like a book file".
- **Connection:**
  - A book file stays in GitHub's history and the owner is never told. The owner uploading a file on GitHub and deleting it is ordinary, and `pull --rebase` is the text's own new route.
  - This is beyond the c52f191 limits, which promised the note until the next approved commit. Here no gate run ever shows it.
  - The fifth look's finding 7 (V7) is answered only in part: after a fast-forward pull the note shows (`v22` session start printed "For a person to look at: commit 5be916c27 changed the gate's own files"); after such a rebase there is nothing to show.
- **Grade:** bears. **Must change.** Either bind the stamp to its parent, or recheck the commits between a stamped commit and its first approved ancestor. Or at least state this in the list, in CLAUDE.md and in line 66.

**U3. A pull request merged by "Rebase and merge" (which the text allows) and reverted on GitHub loses its log entries and receipts, and no check sees it.**
- **Target:**
  - `checks-and-cases.md` line 61 ("merge a pull request with a merge commit, or by rebasing");
  - the list at lines 48–59;
  - CLAUDE.md line 42.
- **Grounds:**
  - `sRv`: E's two reviewed commits were rebase-merged after main had moved (6694ccd, e9ab71a, both not approved), then reverted on GitHub (64e2c12) and merged (d3ba7c5).
  - Session start reported only the missing receipt for the revert, then "Machine checks: none failing". `grep -c "^3[67]\. "` printed 0, and both of E's receipts were gone.
  - After a late receipt, commit a2f098c was stamped with a *different* entry 36.
  - Neighbour: the same revert of a pull request merged with a merge commit (`sRv2`) printed "log entry 36 has been removed" and "log entry 37 has been removed".
- **Connection:** entries and receipts added and removed by commits the gate did not approve, before any approved commit, are never compared. No listed limit covers this: the only such item is about copying.
- **Grade:** bears. **Must change.** At least state it (or say to merge with a merge commit only). Better: have the recheck flag an unapproved commit that removes a log entry or a receipt.

**U4. An unlabelled stretch of the owner's term in a line this round changed.**
- **Target:** `plot/references/suspense-and-fear.md` line 20: "Egri's *foreshadowing* *(built)* is a promise of a coming clash (Gap principle 5)".
- **Grounds:**
  - `reveals-and-withholding.md` section 6 (line 74) says that calling "a foreshadowed clash a promise is the workshop's stretch … (owner question Q7 is open on this)".
  - The term sheet (1.1) says the same.
  - Walking the owner answering Q7 in `sFresh`: the records check named six lines, and not this one. Section 2's number search and label search both miss it too. So if the owner chose Q7's option (b), this line would go on crediting the stretch to Gap principle 5.
- **Connection:** kinds row "an owner term used in a neighbouring sense … a rule changed in one place but not its copies". The fault is older than this round.
- **Grade:** bears. **Must change** on the brief's scale (a workshop reading stated without its label); theory-checker should confirm. The fix is to add "the workshop's stretch, Q7".

**U5. Two siblings of step 4 still give the planting check with no exemption.**
- **Target:** plot `SKILL.md` line 123 (the diagnosing row "the twist came from nowhere") and line 154 (the quick version, "A twist that fails … From nowhere: did each fact it depends on appear before it").
- **Grounds:**
  - Walked case: "mid-book, a sniper shoots the hero's partner in a café; readers say it came from nowhere." The quick version says to plant the sniper.
  - Section 2 says this is a bare arrival (the baseline makes sense of a sniper) and needs no set-up. The complaint lies elsewhere (dread, or the time lost).
  - Gap line 59 (the bomb that simply goes off) sides with section 2.
- **Connection:** this is V2's fault in the two copies that were not touched.
- **Grade:** bears. **Should change.**

**U6. V22, now settled.**
- **Target:** `checks-and-cases.md` line 66, "(Not yet tried: …)".
- **Grounds:**
  - `v22`: plain `git pull` (git 2.43, no pull setting) printed "fatal: Need to specify how to reconcile divergent branches."
  - `git pull --no-rebase` ran the broken script and printed "COMMIT STOPPED: the commit gate's own script could not run (exit 1)" and "Not committing merge". MERGE_HEAD was left in place.
  - `v22b`: `git pull --rebase` then refused: "You have not concluded your merge (MERGE_HEAD exists)". Git's own hint (`git commit`) runs the broken gate again.
  - `git merge --abort` followed by `git pull --rebase` worked.
- **Grade:** bears. **Should change.** Replace the parenthesis with what happens, and name `git merge --abort`.

**U7. A jump scare in prose.**
- **Target:** `reveals-and-withholding.md` line 30 ("So does a jump scare … works only after fear has been built").
- **Grounds:** Anticipation line 98, "Jump scares | Nearly impossible" for prose. A prose writer on Building step 4 is told it needs no set-up and works after dread; the medium table (suspense-and-fear section 9) is never reached from there.
- **Grade:** bears. **Should change.** The lead has already recorded it as open.

**U8. A line that only names Q7 as "nearest".**
- **Target:** `owner-answers-and-revisions.md` line 20 against `owner-terms.md` line 39 ("not yet put to the owner (nearest is Q7)").
- **Grounds:** with Q7 set to answered in `sFresh`, the records check failed line 39. Step 3's "rewrite it to state the answer as the owner's meaning" does not fit a line whose own reading Q7 does not settle.
- **Grade:** bears. **Minor.**

**U9. Session start noise.**
- **Target:** `session_start.py`, `lines_under_failures`.
- **Grounds:** `sFrozen`: under "FAILING: frozen files, owner quotes" it printed "103 quotations match their theory word for word".
- **Grade:** bears. **Minor.** Fifth-look finding 12 is answered in part.

**U10. The trial's second half.**
- **Grounds:**
  - Outside `kept/`, no text names the planted problems (I searched for their words).
  - But one historical error at the end of `27 Corrections.md`, the questions file and one kept case describe the kind of error that the fifth look's finding 8 says problem 1 plants again.
  - If the build's receipt pastes the reviewers' reports outside `kept/`, the fifth look's finding 8 quotes the design ledger's line word for word.
- **Grade:** **does not bear yet.**
  - *Held if* the trial is meant to test catching a new error. If it is meant to test catching a recorded error when it happens again, that record is fair memory.
  - Test that settles it: the lead states which, then greps the trial copy (the committed build without `kept/`) for the problems' words after the receipt is written.
  - If it is meant to test a new error, the grade would be **should change**.

## Fifth-look findings in my area
- **1:** answered in part; the missing part is U1.
- **2:** answered by the main-line walk. The planted test exists (`test_the_gate.py` lines 881–906); I did not rerun it.
- **3:** answered for main; stalls in the Update-branch shape (U1, `sB4`).
- **4:** answered: `v22` printed the plain line.
- **5:** answered on Linux (a copy cloned with Windows line endings: c0559ce stamped). Not tried on Windows.
- **6:** answered (SKILL.md line 218 and line 61 agree).
- **7 and V7:** answered in part; the missing part is U2.
- **8:** answered in plan; see U10.
- **9:** answered: `book_authors` printed `['John Truby', 'Lajos Egri', 'Robert McKee']`.
- **10:** answered; see U8.
- **11:** answered (read).
- **12:** answered in part (U9).
- **13:** still does not bear yet. Test: rerun case 04. The Psycho trap now also sits in the "Surprise by default" trap.
- **V8:** answered.
- **V22:** settled; see U6.
- **Stall items:**
  - a light late receipt for a GitHub edit: works (`sD`, ac4fd77);
  - a frozen theory's way back: works (`sFrozen`: checkout from 1d2ed3c, then passed);
  - the telling test and the session-start note: in the text;
  - a jump scare in prose: open (U7).

## Marks on new or changed rules
- **The bare arrival, defined by the telling test:** held on:
  - Gap lines 47 and 59;
  - Anticipation lines 25, 41, 67 and 84;
  - Implied World lines 12, 20 and 36;
  - the dragons in a world like ours, which fail it;
  - the dragons that are weather, which pass it;
  - *Psycho* (a bare shower; the "Mother" reveal planted);
  - Joffrey (a rescue for Sansa, set up);
  - *Planet of the Apes* (a world reveal, not a threat);
  - *Chronicle* (suspense).

  Loose at a story fact explained after the arrival (an armed stranger at a wedding), and at prose (U7).
- **The climax clauses:** held if the workshop's reading (labelled) stands; no owner theory speaks of climaxes.
- **The rescue clause:** held on Egri's case; its stretch is labelled.
- **The "Surprise by default" trap:** held (Gap line 59, Anticipation lines 41 and 67).
- **The two-sessions route:** held if the merge's first parent is main (U1).
- **GitHub's conflict-free merges counted as approved:** held (`sC`, `sD`, `sNext`).
- **The stamp kept through an unchanged rebase:** loose (U2).
- **The owner-answer step 3:** held (U8 aside).

## Stall list
- **Amending a just-committed log entry:** refused ("log entry 36 has been changed since 54f5cd5…"), and no text says whether that is meant.
- **A GitHub revert of a pull request merged with a merge commit:** stopped, and by line 61 it is a tripwire, so the owner's ordinary revert needs a five-part correction. No GitHub revert route is written.
- **"Main line" in two senses:** U1.
- **An agent who has pressed Update branch has no stated way back:** U1.
- **The merge left in progress:** U6.
- **Suspense-and-fear line 20 is missed by the answer searches:** U4.

## Checked and found right
- **Squash and merge after main moved:** asked for a receipt of its own (`sSq`).
- **Rebase and merge:** both receipts were found (`sRb`).
- **The owner's edit on GitHub followed by the next pull request:** a light late receipt, then stamped (`sD`).
- **Three sessions:** the rebase route holds (`sB3`).
- **Quiet neighbours:** fast-forward pushes; ordinary commits; a fresh clone's session start (0.48 s, gate switched on, nothing flagged).
- **Named planted tests:** every one the lead names exists.
- **Kept cases:** no new wording or example tells a kept case's story or reaches its conclusion (I read only titles and "Aimed at" lines), apart from case 04 as before.

## Not tested
- Real GitHub, real Windows, or a live Claude Code session.
- `test_checks.py` runs and counts.
- A check change brought in through a merge that is not approved.
- Octopus merges, and two reviewed check changes joined on GitHub.
- Squash with main unmoved.
- A cherry-pick with contents unchanged (expected to behave as U2; not run).
- `git am`, worktrees.
- The copying check with the books present.
- No kept case was run.

## Left behind
- Only my folder above: the copies, the bare repositories, and the helpers `add_entry.py`, `fill.py`, `newclone.sh` and `clone2.sh`.
- The live repository is untouched: HEAD 35f2939, `git status --short` shows 30 entries, `core.hooksPath` is `.githooks`.
- The 20 `/tmp/workshop-test-*` folders date from 19:49–20:00, before my run, and are not mine.
- The live refusal hook refused three of my scratch commands that named `core.hooksPath` through a shell variable. That is consistent with its note; I then used full paths.

## Verdict: passed after changes
- **Must change:**
  - U1: state GitHub's parent order and the rebase route; do not follow "put it back" in that shape.
  - U2: the stamp through an unchanged rebase settles commits unseen; at least state it in the list, in CLAUDE.md and in line 66.
  - U3: state the rebase-merge-then-revert route, or allow only merge commits.
  - U4: label the stretch in suspense-and-fear line 20.
- **Should change:** U5, U6, U7 (open).
- **Minor:** U8, U9.
- **Does not bear yet:** U10, and 13.
