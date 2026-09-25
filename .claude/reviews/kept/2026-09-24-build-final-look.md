# The narrow look at the answers to the sixth look, 24 September 2026

What this is: the report of the one agent that looked at the changes answering the sixth look (snapshot commits 26bf4fd to 2a7c252), word for word as it returned it. Its four must-changes were then made in the words it gave, with the record fixes it named that the workshop's own rules require; no further look saw them, since the owner asked that the work be finished. Everything else it found is recorded as open in the build's review receipt. Kept for log entry 33.

---

**Narrow look at the answers to the sixth look (snapshot 26bf4fd to 2a7c252)**

I read the diff, the two kept reports, the lead's account and the two test outputs. I did not rerun the test suite or the machine checks. I made no copy of the workshop. One point I checked by experiment: a tiny made-up git history in my scratch folder (not a copy of the workshop), on which I called only the `Approval` class of each version of `check_commit.py`.

## Must change

**N1. Scripts finding 1 is only half answered, and the new rule widens the half left open.**
- **Target:**
  - `check_commit.py` and `recheck_commits.py`: `automatic_merge_of_approved` and `last_approved_commit`.
  - `checks-and-cases.md` line 29, and the section 2 list, "What the gate cannot do".
  - The account's line "Scripts 1 … put right".
- **Defect:**
  - The scripts reviewer's finding 1 had two shapes, e2 and e4. For e4 it proposed a change to the walk and asked for an e4 planted test. Only e2 is answered: a branch from before the gate that comes in as the *second* parent.
  - The e4 shape is untouched: the main line's walk runs into history from before the gate, finds no approved commit, and falls back to comparing with the last commit.
  - The new rule adds the ordinary case to that shape. The build merged on GitHub, with no conflict, into a main branch that gained commits after the build split off (all from before the gate) is no longer counted as approved.
- **Grounds:**
  - My made-up history: a commit from before the gate; a branch that brings in a stamped gate; main moves on by one commit before the gate; the branch is merged with the gate off; then one commit is made "on GitHub".
    - The old rule (26bf4fd) printed the merge as the last approved commit.
    - The new rule (2a7c252) printed `None`.
    - With main not moved on, both printed the merge.
  - By reading `main()`: with no approved commit, the gate says "the checks come from the last commit and the files are compared with it". So a frozen-theory edit or a log rewrite made on GitHub after the landing becomes the base it is compared with, and it is stamped in. The recheck does not catch either: `sources/` and the log are outside the receipt's scope.
  - The only such fallback that section 2 lists is a shallow clone (a copy made with its history cut short).
  - The fifth round's planted landing test (`copy_before_the_gate`, test_the_gate.py around line 514) keeps main unmoved, so it can only agree. The verifier did not run e4.
- **Connection:**
  - This is CLAUDE.md's "Frozen files unedited: by itself", on the build's own landing route.
  - It applies if GitHub's default branch has any commit the build lacks, for example an earlier pull request merged there with a merge commit. I could not check that.
- **Smallest fix (text only):**
  - Say in section 2 that before the build's pull request is merged, the main branch is merged into the build branch through the gate. The main side is then inside the approved side, and the landing counts.
  - List the limit.
  - Correct the account.
  - Or make the reviewer's walk change, with an e4 test.

**N2. Use-tester finding U2: the false text the verifier named first is still there.**
- **Target:** `checks-and-cases.md` line 36: "a `git revert`, rebase or cherry-pick that goes through without a conflict … carry no matching stamp".
- **Defect:** A rebase that leaves a commit's contents unchanged keeps a matching stamp. The new item at line 58 of the same section now says exactly that, so the section contradicts itself.
- **Grounds:**
  - The verifier's U2: "Three texts are therefore false. (1) checks-and-cases.md line 36…".
  - SKILL.md line 228 and the note in `recheck_commits.py` both say "and changed the contents".
- **Fix:** add "and changes the contents" to line 36.

**N3. The case in the new rule "Proportion, and when to stop", and in C16, gives numbers that are false or disagree with entry 33.**
- **Target:**
  - `reviews-and-briefs.md` section 4: "six rounds, with up to four reviewers each … re-read about 1.4 billion tokens in eight hours".
  - C16: "six rounds of up to four agents".
- **Grounds:**
  - Entry 29: "Five agents that had not made the build reviewed it", so the first round had five reviewers.
  - Entry 33 and C16 say the build "took over nine hours" and re-read about 440 million tokens (design and first build) plus about 1.4 billion (the six rounds). The rule gives the whole build 1.4 billion and eight hours.
  - I checked only whether the texts agree with each other, not the measurements.
- **Fix:** "up to five reviewers", and say that the 1.4 billion is the six rounds' figure (the whole build about 1.84 billion, over nine hours).

**N4. The answer to finding m9 leaves a copy of the same fault.**
- **Target:** file 26, line 131, in "Checks run on these notes": "most of B's gaps weaken a payoff rather than break it".
- **Defect:** This is the same everyday sense of *gap* that m9 (graded must change by the verifier) removed at line 29. The new line-20 note now says *gap* "is the Gap theory's own term, with its own senses", while line 131 keeps the everyday sense.
- **Grounds:**
  - The term sheet, section 3: "say which sense at first use".
  - The kinds row "a rule changed in one place but not its copies".
  - Line 104 ("reads as a gap, not a deliberate open question") may be a third sense. Worth a look.
- **Fix:** "most of what B lacks weakens a payoff".

## Should change

- **S-a. Squash merges have the U3 hole, and the U3 item is too wide.**
  - Section 2, line 63, still offers GitHub's "Squash and merge". A squash made after main moved on, then reverted on GitHub, leaves both commits unapproved, and the files are never compared: the same hole as U3 (by reading).
  - Line 59's "neither side was approved" holds only after the main branch moved on. Otherwise the rebased commits keep their trees and their stamps.
  - The same wide claim is in CLAUDE.md's log row.
  - Fix: "with a merge commit only (not rebase or squash)", and add "after the main branch moved on".
- **S-b. Entry 33's "three rare routes GitHub makes" understates what the owner is told.**
  - U2's rebase is made locally by `git pull --rebase`, not by GitHub. CLAUDE.md's "three routes GitHub makes" has the same slip.
  - "Rare" is not supported: the use-tester called U2's trigger ordinary, and "Update branch" is a standard GitHub button. Entry 33 goes to the owner.
- **S-c. C15 owes a record of its sixth time.**
  - The sixth look found ways round the gate while the planted-fault test passed 209 of 209. By section 4's last paragraph (C15's own rule), that is a tripwire.
  - C15 has no "sixth time" entry. Its status line (line 163) still waits on "the sixth look". The kinds row still says "C15 (five times)".
  - The project story's "(the sixth look still found five, now put right)" matches no list. Scripts 1–4 and U1–U3 make seven, and U2 and U3 are listed as limits, not put right.
- **S-d. C16's response changes a different place from the stage it names.** C16 names the stage as "How much to do", but only `reviews-and-briefs.md` changed, and "How much to do" does not point to the new paragraph. This is C1's own lesson: "A cause named is not a stage changed."
- **S-e. The account cites an owner request with no words behind it.**
  - The account says "the owner asked that the gate not be hardened further". No owner words in entry 33 or elsewhere in the log say this.
  - Does not bear yet: quote the owner's words, or call it the lead's reading, before it goes into the receipt.
- **S-f. Part of scripts finding 2 is neither answered nor listed as open.** Section 3, step 3 (line 78) still says to "put the new `test_checks.py` into it". The scripts reviewer graded this should change. The account does not answer it and does not list it as open.
- **S-g. One sentence in C15 misses an exception it states itself.**
  - C15's "Still working" sentence says the tests that fail on the old scripts are new ones, apart from the real-stage tests.
  - The same paragraph says that in round 3, one test failed "only because a message's wording changed" (entry 30). The sentence should allow for that.

## Minor

- **Test 2's neighbour does not show anything.** It reads the same answer as its fault test, so it fails on the old scripts although nothing is wrong there. Asking `Approval(...).approved(first)` directly would pass on both versions. The lead disclosed this.
- **The old-git text is incomplete.**
  - It does not say that each GitHub merge then asks for a late receipt for its whole change, because the receipt comparison falls back to the first parent.
  - It does not say that a merge through the gate that brings in a check change together with other work is refused as mixed.
  - No plain line names the git version, which was the reviewer's proposal. This environment has git 2.43.
- **Project story slips.**
  - The "Tested" status line repeats its "(in earlier rounds …)" parenthesis.
  - "Written…" says "(entries 27 and 29 to 32)"; entry 33 is left out.
- **Answer to S1:** "as the dragons do" points ahead to the next sentence.
- **C1:** "three phrases the third, fourth and fifth looks found" is true only if read as three phrasings ("still", "weakened", "its shortness…"). Name them, as the verifier asked.
- **U2 item and route:**
  - The line-58 example "a change to the gate's own files made there, is never noted" holds only for a change that was undone before the pull.
  - Line 68's "a rebase settles the commits it lands on unseen" is too general; it errs toward caution.
- **U1 not planted:** the stated bar ("needs GitHub's own parent order") is weak, since the verifier simulated that order in a copy. The fix is text only.
- **Duplicate helper:** `before_the_gate_and_the_build` repeats `copy_before_the_gate` almost line for line.

## Checked and found right

- **M1 and U4:** both lines now carry "the workshop's stretch" and "Q7", so the owner-answer search for "Q7" finds them.
- **M2:** C1 now names the third, fourth and fifth looks and entries 30 to 32.
- **U1:** the paragraph matches the verifier's walk and uses "main branch" for GitHub's branch.
- **Lower findings put right:**
  - S1 is scoped.
  - m5's kinds row ("four times, … entries 29 to 31") matches the verifier's four versions and file 26's "Four earlier rounds".
  - m8's hook note is fixed.
  - m9 is fixed at line 29.
  - C15 names the six new tests that pass on the old scripts, as the verifier listed them.
- **The four script changes:**
  - The approval code is the same in `check_commit.py` and `recheck_commits.py` (the same list of check files; both refuse when git cannot make its automatic merge).
  - The fallback in `automatic_merge` is the same in the gate and `review_receipt.py`.
  - The changed-test rule covers both test files, and `test_checks.py` (lines 734–735) imports `test_the_gate.py` from its own folder, so the staged copy is the one that runs.
- **The five new tests, as the runs say:** each plants the fault it names and fails on the old scripts for that reason, in `test-run-25-old.txt`:
  - the records check passed and the commit went through;
  - the second merge was printed as approved;
  - "review receipt: not needed";
  - no changed-test stage ran;
  - the neighbour fails as disclosed.
  - All 214 pass in `test-run-25.txt`.
- **No way round found, by reading:**
  - The rule for two check changes held against merges in sequence, the "Update branch" direction, a rebased side, and identical changes on both sides.
  - The rule for a branch from before the gate as the second parent: that parent counts only when it is inside the approved one, and then the merge's tree is the approved one's.
- **Entry 33 counts:** eleven confirmed must-changes (2+1+3+4+1), and four under-graded findings (m7 is folded into scripts 5).
- **Source register:** its cells agree with the copy-checker's whole-tree runs.

## Not checked

- The test suite and the machine checks: I used the lead's outputs, not a rerun.
- The inner cause of the two real-stage failures: `test-run-25-old.txt` cuts that output off. I accepted the lead's reason, as in earlier rounds.
- Every measurement in entry 33 and C16 (tokens, hours, steps, 24 agents, 126 copies, each brief check finding a way). I checked only whether the texts agree.
- GitHub's real default branch, which decides whether N1 hits this build's landing.
- The claimed effects of the scripts 3 change (the next commit runs the planted-fault test; a correction goes through): by reading only, and no test covers them.
- A real old git, Windows, real GitHub.
- The lead's reading of "Return" as "Rerun".
- The kept reports: not judged, as briefed.

## Left behind

- In `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/r7-narrow/`:
  - `new/` and `old/`: `check_commit.py` extracted from 2a7c252 and 26bf4fd, with `__pycache__`;
  - `landing.sh`;
  - `land-yes/` and `land-no/`: the tiny made-up histories, with no remotes.
- `.../scratchpad/ttg-new.py`: an extract of `test_the_gate.py`.
- The snapshot: I ran only `git show`, `git diff` and `git grep` there.
- The live repository: I ran only read-only git commands (branch, log, merge-base, rev-parse, `status --short`). `git status` may refresh git's index timestamps; no content was written.
- I did nothing on GitHub.

## Verdict: passed after changes

The must-changes are N1 to N4. All four can be answered in text; N1 can also be answered in code. Under the new rule "Proportion, and when to stop", a must-change found after two rounds goes to the owner with its cost before another round starts.
