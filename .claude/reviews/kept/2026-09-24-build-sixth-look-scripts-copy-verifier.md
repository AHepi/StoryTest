# The sixth look at the error-correction build: the scripts and copy-checker reports, and the verifier, 24 September 2026

What this is: the other two reviewers' reports, word for word, and the one verifier's check of every finding the four reports graded must change (its structured answer, set out as text, word for word); the first two reports are in `2026-09-24-build-sixth-look.md`. They looked at the edits answering the fifth look (snapshot commits c52f191 to 26bf4fd); the reviewers and the verifier made no edits, and every experiment ran in their own copies. The theory-checker and the use-tester ran first; the run was stopped when the owner asked about its cost, and resumed at the owner's word with the scripts reviewer, the copy-checker and one verifier (log entry 33). The briefs, their four checks and the copy script every reviewer used are in `2026-09-24-build-sixth-look-briefs.md`. How each finding was answered is in the build's review receipt. Kept for log entry 33.

---

## 3. scripts and hooks (a general-purpose agent)

**Sixth look, scripts and hooks (Brief C): report**

I made no changes to `/home/user/StoryTest`. At the end its HEAD was still 35f2939, `git status --short` still listed 30 entries, and `.git` had no `workshop-*` files. Everything below ran in copies under `.../scratchpad/r6-scripts/`. Every review receipt in those copies is a stand-in written by my `tools/fill_receipt.py`: no reviewer read any of those changes.

**Words used below**
- The **stamp** is the line "Workshop-gate: approved <tree>" that the gate adds to a commit it passes.
- The **last approved commit** is the commit the gate takes its checks from and compares the files with.
- A **GitHub merge** is a merge commit made with the gate off, the way GitHub makes one.
- A **branch from before the gate** is a line of work that split off before the commit that brought the gate in.
- The **planted-fault test** is `test_checks.py` together with `test_the_gate.py`.
- A **check-only commit** is a commit that changes only checks and receipts, made straight on top of an approved commit.

**Copies:**
- `base` was made with the lead's copy script at 21:32 by an earlier start of this review that stopped; its log is `base-make.log`, its commit 51354c9 is stamped "approved b8d3628…", and it has no remotes. I compared every tracked file in the snapshot at 26bf4fd with `base` and with the live tree using `cmp`: none differ.
- `e1` to `e9` are clones of `base` with their remote removed. `github.git` is my stand-in for GitHub.

## The counts (brief item 1)
- **New tests on the current scripts** (`cnt-new`, from `git archive 26bf4fd`): "TOTAL tests: 209, failed: 0", in 4 min 42 s.
- **New tests on the old scripts** (`cnt-old`: c52f191 with the new `test_checks.py` and `test_the_gate.py` put in): "TOTAL tests: 209, failed: 23".
  - I reran the gate groups with the full output shown (`tools/full_output.py`, saved in `old-gate-full.txt`).
  - 21 of the 23 fail for the fault each plants.
  - The 2 that run the real planted-fault stage fail only because the test they run inside themselves fails. That inner run printed "TOTAL tests: 207, failed: 21, not run: 2".
- **The old test on the old scripts** (`cnt-c52`): "TOTAL tests: 184, failed: 0". Two of its tests were renamed in the new file ("after a merge made as GitHub makes one…" became "after the gate is merged on GitHub as a merge commit…").
- **Six tests with new names pass on the old scripts too.** The lead's account and C15 say three.
  - The three the lead lists: the two renamed "gate merged on GitHub" tests, and the rebase route.
  - Three more, not listed:
    - "gate, neighbour: the check corrected on a branch from the last approved commit, then the main line merged into it through the gate";
    - "gate: after a merge made on GitHub with a conflict, a check corrected on the main line's tip is judged by the wrong check";
    - "hook: the gate folder named by $PWD from the project's top folder is let through".
  - No test fails on the old scripts for a reason other than its planted fault.

## Must change

**1. A branch from before the gate is counted as settled. What its commits got wrong in the files is never judged, and the gate and the recheck disagree about those commits. New in this round.**
- **Target:**
  - `check_commit.py` lines 16 and 190;
  - `recheck_commits.py` lines 7–11, 148 and 306–310;
  - `checks-and-cases.md` line 29;
  - the same rule in CLAUDE.md line 39 and SKILL.md line 118.
- **Defect:** a merge made without the gate counts as approved when either parent is "from before the gate". That parent's own new commits are then never compared with an approved commit.
- **Grounds:**
  - **e2.**
    - On a branch from 35f2939 I rewrote log entry 5 and committed with the gate off, then merged it with the gate off. The merge had no conflict.
    - `recheck_commits.py --last-approved` printed the merge itself.
    - The next commit through the gate printed "passed records … All checks passed; committing." and was stamped "approved 4ea5e84…", with entry 5 rewritten.
  - **e2c (control).** The same rewrite on a branch from 51354c9 (after the gate) printed "FAILED records … log entry 5 has been changed since 2ed4601c9…".
  - **e4.**
    - A main line that moved on before the gate: an edit to the "Next step" paragraph.
    - The build merged into it with a conflict, resolved by hand, with entry 5 also rewritten.
    - The next commit printed "note: walking back along the main line, no commit is approved by the gate, so the checks come from the last commit…" and was stamped with the rewrite.
    - Under the c52f191 rule, `git log --topo-order` lists 51354c9 (the stamped build) first, so that rule would have caught the rewrite. That conclusion is by reading only.
  - **e2b.**
    - The same shape as e2, with a skill line changed instead of the log.
    - The gate's own rule found the merge (HEAD) as the last approved commit, so it counted zero commits since then.
    - Yet the recheck printed "rechecked 1 commit(s) the gate did not approve, since the last approved commit, 4448f925b" and "commit f3c26c9e6: no review receipt…".
    - So the recheck's note "every commit an approved commit reaches back to is settled, and is never looked at again" (line 11) is false here. The recheck leaves out only the history before the stamped commits and the commit before the gate (line 306), not everything before an approved merge.
- **Connection:**
  - Kinds row "a commit that … arrives where it cannot see".
  - This covers every branch that exists when the build lands. It also covers the build's own merge, if GitHub's main has moved on in a way that conflicts.
  - None of it is in the list of what the gate cannot do, either at c52f191 or now.
- **Proposed change:**
  - Count a parent from before the gate as settled only when it is an ancestor of the other parent.
  - When the main-line walk reaches the history from before the gate, take the approved parent of the merge that brought the gate in.
  - Have the recheck list what the gate lists (`rev-list HEAD ^<last approved>`, less the approved commits).
  - Plant tests for e2 and e4.
- **Grade: must change.**

**2. The gate never runs a changed `test_the_gate.py`. A typo in it goes in stamped, and then stops every later check change, its own correction included. New in this round (the split).**
- **Target:**
  - `check_commit.py` line 399 runs the staged test only when `test_checks.py` itself changed;
  - the claims "and the changed test too" at `check_commit.py` line 68 and `checks-and-cases.md` line 34;
  - `checks-and-cases.md` line 76 (section 3, step 3), "put the new `test_checks.py` into it", which now leaves the gate's tests out.
- **Grounds:**
  - **e1.**
    - I added a function with a syntax error to `test_the_gate.py` alone and committed it as a check-only commit.
    - It printed "passed the last approved commit's planted-fault test … (2 test(s) not run inside it) … All checks passed", stamped "approved b9a89ae…".
    - A harmless comment added to `run_all_checks.py` then printed "FAILED gate_tests could not run / invalid syntax (test_the_gate.py, line 996)", and the same for more_gate_tests. A test that could not run is never retired.
    - The commit putting `test_the_gate.py` back was stopped the same way.
  - By reading: the approved copy is the one that runs, because `test_checks.py` imports `test_the_gate.py` from its own folder, which is the archive of the last approved commit. So no staged or on-disk copy can be run in its place.
- **Connection:**
  - This is a false statement in a script note and in a skill text.
  - It is also the kind "a check that passes while the thing is wrong": a gate test is committed that has never run.
  - The way out is the owner's route.
- **Proposed change:**
  - Run the staged test whenever `test_checks.py` or `test_the_gate.py` differs.
  - Plant a typo in `test_the_gate.py` alone.
  - Section 3, step 3: put both files in.
- **Grade: must change.** The section 3 wording on its own would be a should change.

**3. Two reviewed check changes joined by a GitHub merge. The limit added in this round is not a true limit, and it costs more than it says. New in this round.**
- **Target:**
  - `check_commit.py` lines 182–190 (the same code in `recheck_commits.py`);
  - `checks-and-cases.md` line 52.
- **Grounds:**
  - **e9.** I made two check-only commits, each on its own branch:
    - A renamed `field` to `field_value` in `review_receipt.py`;
    - B added one new call to `field(…)` in `problems_with`.
  - Each printed "passed the last approved commit's planted-fault test … All checks passed".
  - Both were merged with the gate off, with no conflict (6de9f06, then 830f5ec). `--last-approved` printed 830f5ec.
  - The next ordinary commit printed "COULD NOT RUN review_receipt.py (exit 1): … NameError: name 'field' is not defined".
  - The check-only correction printed the same stop, because the receipt check always comes from the last approved commit. Only the owner's route is left.
  - By reading, the c52f191 rule would have taken B's working checks and run B's planted-fault test on the joined checks, so an ordinary correcting commit would have gone through.
- **Connection:**
  - A changed check takes effect without the planted-fault test ever running on it.
  - Two ordinary pull requests end at the owner's route.
- **Why it is not a true limit:** the gate could decline to count as approved a merge whose two sides both changed check files since they split. The next commit would then run the planted-fault test on the joined checks, at the cost of one run.
- **Proposed change:** that rule, with a planted test in the shape of e9.
- **Grade: must change.**

**4. With git older than 2.38 (no `merge-tree --write-tree`), a merge's own changes need no receipt. Older than these edits.**
- **Target:**
  - `check_commit.py` lines 245 and 281;
  - `review_receipt.py` lines 79, 116 and 123.
- **Grounds:**
  - **e7.**
    - A conflicted merge through the gate, resolved by hand with a third, unreviewed wording of a plot `SKILL.md` line.
    - With the real git (2.43), the gate printed "FAILED review receipt … no review receipt … for this change to: .claude/skills/plot/SKILL.md".
    - With my stand-in for an older git (`tools/oldgit/git`, which refuses `--write-tree` the way an older git refuses an unknown option), the gate printed "passed review receipt … not needed (no reviewed file changed) … All checks passed; committing."
  - The failed command gives an empty name for the merge's own contents, and every comparison against that name finds nothing.
  - By reading, the recheck has the same gap for a merge made on GitHub with a conflict.
  - Ubuntu 22.04 ships git 2.34. I did not try a real older git.
- **Connection:** a fail-open (the check lets the commit through when it cannot run), and not listed as a limit.
- **Proposed change:** when `merge-tree` fails for any reason other than a conflict, stop the commit with a plain line saying git 2.38 or newer is needed. Plant it with a stand-in.
- **Grade: must change.**

**5. C15 miscounts the tests that pass on the old scripts.**
- **Target:** `27 Corrections.md` line 161: "three new tests pass there too (…)".
- **Grounds:** the counts above. Six tests with new names pass on the old scripts, three of them not named.
- **Grade:** must change under the brief's rule for a false statement in a record. It is a one-line correction.

## Should change

**6. The Book-text rule misses a book whose author goes by one name.**
- **Target:** `review_receipt.py` line 189. The pattern needs two capitalised words.
- **Grounds:**
  - **e5.** I added a register row "| Aristotle, *Poetics* …" and a module naming only Aristotle, and left the Book-text line as the form's hint.
  - The check printed "review receipt: … is complete".
  - `book_authors` returned `['John Truby', 'Lajos Egri', 'Robert McKee']`.
- **Connection:** the same reader as fifth-look findings scripts 4 and use-tester 9. No book registered today is affected.
- **Proposed change:** accept names of one word or more.

## Minor
- **7. The refusal hook's rule for `$PWD` holds.** I fed 11 commands to the copy's hook. None that would switch the gate off was let through. Four honest spellings are refused, but plain `.githooks` always works:
  - `"$PWD"/.githooks`;
  - `$PWD/.githooks` with no quotes (refused before this round too);
  - a `cd` placed after the setting;
  - `cd ..` placed before it.
- **8. A misleading stop message in `.githooks/pre-commit`.** When `mktemp` fails (a temporary folder that does not exist), the hook says the gate script "is in neither the last commit nor the staged files". Seen in my first try; older than these edits.
- **9. An octopus merge through the gate** (one that joins three or more branches): the changes of the third branch are counted as the merge's own and need a receipt again (`check_commit.py` line 281). By reading only.
- **10. A local `git merge --squash`** let the other side's log entry 33 be reworded, and the commit was stamped (03c4e56). It is not a merge, so the other side's entries are not kept.

## The fifth-look findings in my area
- **Scripts 1: answered.** I also tried five more commit forms: `--include`, `--only`, `--amend -a`, `--amend -- <file>` and `--pathspec-from-file`. Each printed "FAILED frozen files … bond-theory.md: frozen file has changed". Honest changes made with `--only` and `--amend -a` passed and were stamped.
- **Scripts 2: answered in part.**
  - Merges of approved branches work: the tests are planted and they fail on the old scripts.
  - In e6, a pull through the gate that dropped the other side's entry 33 printed "log entry 33, which the commit being merged (1abda9d5a) added, has been changed or removed". The plain pull passed and was stamped.
  - Not answered: findings 1 and 3.
- **Scripts 3: answered** on a clone with Windows line endings (`e8crlf`): skill files CRLF, hooks LF, skill fingerprints identical to the LF copy, and the same kept-case note. Windows itself was not tried.
- **Scripts 4: answered for two-word names.** One-word names remain (finding 6).
- **Scripts 5, 6, 10, 11 and 15: answered.** Each is planted, and each fails on the old scripts.
- **Scripts 7: answered.** Both route tests pass on the old scripts too, so they show the route works, not a change.
- **Scripts 8: answered.** By reading.
- **Scripts 9: answered.** Seen as "(2 test(s) not run inside it)".
- **Scripts 12: answered.** The stamp note now says "in the last two minutes".
- **Scripts 13: answered.** A search found no wording left that says the copying check reads only `.md` files.
- **Scripts 14: answered.** Each receipt test now runs under its own name.
- **V9 and use-tester 4: answered.**
- **V16, the counts:** 209, and 23 failing (21 plus 2), are confirmed. The "three" is wrong (finding 5). The "not tried by a planted test" list now names the fourth look's scripts 14 and 15.
- **V19: answered.**
- **Use-tester 5: answered.**
- **Use-tester 9: answered in part** (finding 6).
- **Use-tester 12: answered.**

## Marks on new or changed rules
- **The staging area for this commit is passed to the checks:** held. Two planted tests, plus five commit forms and two honest neighbours in e5.
- **An automatic merge of approved parents counts as approved:**
  - held for approved parents (planted, and e6);
  - loose for a parent from before the gate (finding 1) and for check changes on both sides (finding 3).
- **The other side's log entries in a merge through the gate:** held (e6). Loose only for a squash (finding 10).
- **The result file that pre-commit reads:** held (the planted typo test). By reading, it is written only at the gate's end, and no test runs the gate script directly.
- **The hooks check:** held (four planted tests). Local settings are a stated limit.
- **The Book-text register read before and after:** held for two-word names; loose for one-word names.
- **The refusal hook's `$PWD` rule:** held.
- **The frozen check's way back:** held (planted).
- **The split of the planted-fault test:** two routes. The approved `test_the_gate.py` is the one that runs, but a changed one never runs (finding 2).
- **Line endings (`.gitattributes` and fingerprints):** held on Linux.

## Checked and found right
- `check_commit.py` and `recheck_commits.py` hold the same approval class; I compared the text line by line. The only difference is which commits the recheck lists (finding 1).
- Session start asks the recheck on disk with `--last-approved`.
- The gate runs the approved `test_the_gate.py` in every case.
- No wording is left that says the copying check reads only `.md` files.

## Not checked
- Real GitHub, Windows, macOS, a real git older than 2.38, and a live Claude Code session. The hooks were fed JSON input the way Claude Code would send it.
- The GitHub situations in Brief B.
- The owner-named retirement of a test.
- An octopus merge, by test.
- The recheck's time limit.
- The unchanged hooks `after_commit.py` and `protect_frozen_files.py`.
- The texts outside the lines cited here.
- Whether the old rule's outcomes in findings 1 and 3 really happen: by reading only.

## Left behind
- **In `r6-scripts/`, made by this run:**
  - folders: `cnt-new`, `cnt-old`, `cnt-c52`, `e1`, `e2`, `e2b`, `e2c`, `e4`, `e5`, `e6`, `e6b`, `e7`, `e8crlf`, `e9`, `github.git`, `tmpdir-*`, `tools`, `tmp`;
  - output files: `count-*.txt`, `old-gate-full.txt`, `n-*.txt`, `e1-commit*.txt`, `e5-pathspec.txt`.
- **From the earlier, stopped start of this review** (not used): `old`, `snap-new`, `snap-old`, `t-new`, `tmp-new`, `tmp-old`, `run-new.txt`, `run-old.txt`. The same start made `base`, which I did use.
- **Not mine:** twenty `/tmp/workshop-test-*` folders dated 19:49 to 20:00, from before this run.

## Verdict: passed after changes
- **Must change:** 1 to 5. Findings 1 and 3 are the same function (`automatic_merge_of_approved`), so one change can answer both.
- **Should change:** 6.
- **Minor:** 7 to 10.

The changes for these need their own narrow look.

## 4. copy-checker

## Copy-checker report: sixth look (Brief D)

**Verdict: passed.** I found nothing that must change. The one finding that bears is minor, and it is older than this round. My report quotes no book text: it names places in the books by line number and describes them in my own words.

I made no changes to the repository at `/home/user/StoryTest`. Everything I ran, I ran in my own copy, made with the lead's copy script: `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/r6-copy-checker/copy`. It has no remotes.

**What I looked at.** The four books are present in `sources/raw/`: Egri, *The Art of Dramatic Writing*; McKee, *Dialogue*; Truby, *The Anatomy of Story*; and Truby, *The Anatomy of Genres*. I compared all 35 changed files: each is the same in my copy, the snapshot at 26bf4fd and the live tree. Seven lines of book-derived text changed:
- the rule card, `writing-rules-and-rivals.md` line 9
- plot `SKILL.md` lines 106 and 164
- `reveals-and-withholding.md` lines 16, 30 and 74
- `suspense-and-fear.md` line 20

### What the overlap script printed
- **8 words, all 35 changed files, each book:** 0 problem spans, exit 0.
- **6 words, same files:** 0 problem spans for Egri, McKee and *The Anatomy of Story*. *The Anatomy of Genres* gave 1 problem span (finding 1). The only other spans were the film title *Once Upon a Time in the West*, marked allowed.
- **8 words, the whole tree, each book:** 0 problem spans. The allowed spans are that film title, plus the books' own titles in `sources/README.md` and the allowed list.
- **5 and 4 words, the seven new lines only:** common word strings and one title (finding 2).

### Findings
1. **Target:** `/home/user/StoryTest/27 Corrections.md` line 126. **Defect:** a 6-word run. **Grounds:** *The Anatomy of Genres*, one shared everyday phrase ("this is the first use of"). The line was already there at c52f191. **Connection:** it is the workshop's sentence about its own rule card; no idea from the book is in it. **Grade:** does not bear.
2. **Target:** the new lines on plot `SKILL.md` lines 106 and 164 and `reveals-and-withholding.md` line 30. **Defect:** 4- and 5-word runs. **Grounds:**
   - A 9-word span against *The Anatomy of Genres* is four separate short runs joined together. They come from unrelated places (a western, raw line 3439; *Arrival*, raw line 2317). No book has a dragon passage like the workshop's.
   - The 4-word run shared with *The Anatomy of Story* around *Psycho* (raw line 1598) is about a different point, a family's hidden secrets.
   - Egri's matching run (raw line 2478) is about dialogue.
   - **Connection:** none of these is the books' distinctive wording. **Grade:** does not bear.
3. **Target:** `/home/user/StoryTest/.claude/skills/plot/references/reveals-and-withholding.md` line 74, the new sentence that Egri calls foreshadowing a promise *(built)*. **Defect looked for:** close paraphrase, and a wrong credit. **Grounds:** Egri raw line 1839 says this in one short clause (promising conflict), after his *Thirty Seconds over Tokyo* example (raw lines 1836-1840). He argues it from the audience's waiting at raw line 1849. **Connection:** the claim is his and is credited to him in different words. The grade "built" is defensible, and the stretch of the Gap theory's promise is still labelled as the workshop's reading (Q7). **Grade:** does not bear.
4. **Target:** same file, line 30: "Egri's case is a murder weapon, and applying it to every rescue is the workshop's reading". **Defect looked for:** a wrong credit or a wrong label. **Grounds:** Egri raw lines 2474-2475 give the nail-file weapon in a murder play; he never mentions rescues. **Connection:** true, and labelled correctly; the old "(built)" is gone. **Grade:** does not bear.
5. **Target:** same file, line 30, the new climax clauses ("a set-up is needed but not enough"; "a rescue from outside fails even when it is set up"), both pointing to `structure-and-conflict.md` section 7. **Defect looked for:** a credit the book does not hold. **Grounds:** at raw line 226 Egri rules out an accident or an illness as an ending that comes from outside the play; the end must come from the character's own acts. At raw line 2475 the weapon must be found in a way true to the character, not by chance. **Connection:** section 7's Egri credit covers both clauses. "A rescue from outside" is not a case Egri names, but it applies his own category. **Grade:** does not bear.
6. **Target:** same file, line 30. This part of the line has not changed since c52f191. **Defect:** "Egri's set-up and payoff" names a term as his when he does not use it. **Grounds:** grep of Egri found 0 uses of "payoff". His two uses of "set-up" (raw lines 367 and 1855) mean something else. His idea is preparing for coming events (raw line 2474). **Connection:** the idea is rightly credited to Egri, but a writer looking for this term in his book would not find it. A possible rewording: "Egri's rule that what a coming event needs is prepared (section 6)". **Grade:** minor.
7. **Target:** `/home/user/StoryTest/.claude/skills/plot/references/suspense-and-fear.md` line 20. **Defect looked for:** close paraphrase. **Grounds:** the only change is "the same bomb as". The Egri sentence on the same line has not changed; I read it beside Egri raw lines 1836-1840. **Connection:** it keeps Egri's one example, credited, but reverses his order (the rule first, then the example) and uses new wording. It shares his idea, not his expression. **Grade:** does not bear.
8. **Target:** `reveals-and-withholding.md` line 16, and plot `SKILL.md` lines 106 and 164. **Grounds:**
   - The new wording comes from the owner theories: *Psycho* and the broken guarantee are in the Anticipation theory, Part 2 section 5.
   - "Or starts new suspense (below)" points to McKee's *narrative drive*, which McKee supports at raw lines 194 and 177 (ranking facts).
   - *Speed* is the workshop's own example; McKee's "Speed" at raw line 272 is a heading word.
   - Line 106 adds only a pointer.
   - Truby's *Psycho* passages make other points.
   - **Grade:** does not bear.
9. **Target:** the rule card, `writing-rules-and-rivals.md` line 9, and the baseline and dragons sentences on line 30. **Grounds:**
   - Line 9 is the workshop's own history.
   - The baseline is quoted exactly from `implied-world-theory.md` line 12.
   - The dragons case comes from the owner theories (Gap line 47; Implied World line 36).
   - No book has a dragon case: Egri, McKee and *The Anatomy of Story* have none, and *The Anatomy of Genres* has three mentions, all in lists.
   - No book tells Hitchcock's bomb.
   - **Grade:** does not bear.
10. **Target:** `/home/user/StoryTest/.claude/skills/add-source/SKILL.md` line 88, and the note inside `overlap_check.py`. **Defect looked for:** a false statement. **Grounds:** the script's list of text endings, and `run_all_checks.py` lines 262-265, which run the script on "." (the whole folder). **Connection:** "as the commit gate does" is true. **Grade:** does not bear.

### The fifth look's findings in my area
- **C1 to C6 still hold.**
  - C1: I reran the search on the rewritten line 16. No book has plant, hide (or conceal) and reveal within 40 words: 0 in all four books.
  - C2: nothing in the books matches the telling test or the dragons case on the rewritten line 30.
  - C3: the new clause on line 106 is a pointer only.
  - C4: rechecked (finding 8).
  - C5 and C6: the lines have not changed. C6's point that a broken promise is the workshop's idea, not Egri's, still holds: at raw line 1849 Egri speaks of waiting for the promise to be kept, never of breaking it.
- **D1 answered.** Line 13 of `/home/user/StoryTest/.claude/agents/copy-checker.md` now says `--run-length 6` after the script's name. Run that way, the script printed 6-word totals. A search found `N=6` nowhere outside `.git` and the kept records.
- **D2 answered** (finding 4). The rest of D2 is still unchanged: section 6 and the sources line read Egri's rule as being about the climax. That narrows a rule which covers every coming event, so it is still true. D2 itself said the rule need not change.
- **D3 answered** (finding 3).
- **D4 does not bear yet.** The register cells, `/home/user/StoryTest/sources/README.md` lines 40-43, still read 23 Sep 2026, and today's runs show they still describe the tree. The lead's promise to update them at the commit can only be checked then.

### Marks on the changed credits
- Egri calling foreshadowing a promise *(built)*: held by Egri raw line 1839.
- Egri's case of a murder weapon: held by raw line 2475.
- Applying it to every rescue, labelled the workshop's reading: the label is right.
- The climax clauses: held through section 7's Egri credit (raw lines 226 and 2475).

### The script used
You asked for any new script inline. The one I wrote was used only for the C1 recheck, run once through a pipe and not saved:
```
import re,glob
for b in sorted(glob.glob('/home/user/StoryTest/sources/raw/*.txt')):
    w=re.findall(r"[a-z']+", open(b,encoding='utf-8').read().lower())
    hits=0
    for i in range(0,len(w)-40,10):
        win=w[i:i+40]
        if any(x.startswith('plant') for x in win) and any(x.startswith(('hide','hid','conce')) for x in win) and any(x.startswith('reveal') for x in win):
            hits+=1
    print(b.split('/')[-1], hits)
```

### What I did not check
- Side by side with the books: the other 28 changed files (scripts, records, kept reports). The 8- and 6-word runs covered them.
- The unchanged plot sections 3-5 and 7-9 against Truby and McKee, and *The Anatomy of Genres* beyond word searches.
- The dialogue skill's `flaws-and-fixes.md` line 78, which D2 named.
- Whether the rules are right as craft or as theory; that belongs to the theory-checker and the use-tester.
- The paraphrase judgements are by reading; no tool measures close paraphrase.

### What I left behind
Everything is in `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/r6-copy-checker/`:
- `copy/`: the review copy. Its last commit, a968307, went through the gate with the copy script's stand-in review receipt.
- `make-copy-output.txt`
- `changed-files.txt`
- `changed-lines.md`
- `overlap-*.out`: the script's output for each run

Verdict: passed

## 5. The verifier (one general-purpose agent)

Findings the verifier checked (each reviewer's must-changes), with its verdict and grounds, word for word:

**theory-checker:M1: confirmed.** suspense-and-fear.md line 20 (edited this round) credits Egri's 'foreshadowing is a promise' to Gap principle 5 without the Q7 label. scenes.md line 18 states set-ups as promises with no label either.

Grounds: Read the diff c52f191..26bf4fd for suspense-and-fear.md: this round added only 'the same bomb as' to line 20. It kept 'Egri's *foreshadowing* *(built)* is a promise of a coming clash (Gap principle 5)'. reveals-and-withholding.md line 74 says calling 'a foreshadowed clash a promise is the workshop's stretch' (Q7 open). Term sheet 1.1 'Open' says the same. Q7 (questions file lines 67-71) tells the owner 'Both are flagged as the workshop's'. C12 (corrections line 129) recorded this same kind of error: 'credited to the theory the promise's stretch to set-ups'. I ran the owner-answer step-2 searches in the live tree (read only). grep -rn Q7 .claude/skills lists six lines (owner-terms 21, 22, 39; genre SKILL 20; reveals-and-withholding 30, 74), not these two. The label search ('workshop's reading|stopgap|put to the owner|workshop stretches|workshop's extension') matched neither line (count 0). So if the owner answers Q7 with (b), these lines stay. The scenes.md half is weaker and older: it has no explicit '(Gap principle 5)'. But it puts 'makes a promise (a set-up to be paid off)' in the Withholding row of the Gap theory's five-gaps table, unlabelled. Both meet must change: a workshop reading stated without its label, credited to the theory. No script written for this.

**theory-checker:M2: confirmed.** C1's put-right line (corrections line 41, added this round) says only the fourth and fifth looks (entries 31 and 32) found order phrases after entry 29's reading. The third look (entry 30) found some too.

Grounds: Line 41 at 26bf4fd, added this round: 'what remains assumes no order (entry 29), apart from three phrases the fourth and fifth looks found ... (entries 31 and 32)'. C1 lines 38-40 and file 26 line 133 say the third look (entry 30) found two uses of 'still' after the entry-29 reading. The fourth (entry 31) found 'weakened', the fifth (entry 32) found 'its shortness'. In the snapshot, 'B still shows the ramp (B' counts 1 at 1e92459 and 7812119 (entry 29) and 0 at 0f14d0a (third look's answers, entry 30). So the sentence leaves out phrases that were left after entry 29. Caveat on the fix: 'three' can also be read as the fourth look's two phrases ('weakened, not lost', 'Weakened.') plus the fifth look's one. Read that way the looks are named right, but the sentence still leaves out the third look's 'still' uses. It is false either way. The fix should add the third look (entry 30) and recount, not just rename the looks. No script written.

**use-tester:U1: confirmed.** When GitHub's conflict editor (or Update branch) merges main into a session branch, the session branch becomes the first parent. The gate then stops the natural renumbering, its advice renumbers main's approved entry, and that rewrite reaches main unseen.

Grounds: Walked in my copy r6-verify/u1. My base copy came from the copy script (798e136 stamped). A bare repository stood for GitHub, and GitHub's merges were made with the gate off. What printed: (1) Sessions a and b each stamped their own entry 33 (6bb14df, bd4f8d2). (2) 'GitHub merged A's pull request: 55fc183 parents 798e136 6bb14df'. (3) The conflict editor's merge of main into b, resolved the natural way (A keeps 33, B's becomes 34): 'b117145 parents bd4f8d2 55fc183'. (4) The next commit on b printed 'the last commit the gate approved ... is bd4f8d29d' and 'log entry 33 has been changed since bd4f8d29d... put it back', then COMMIT STOPPED. (5) I followed that advice (B's text back at 33, A's moved to 34): 'All checks passed', stamped 7ce47ea. (6) 'GitHub merged B's pull request: c6c6015 parents 55fc183 7ce47ea'. (7) Next session: last approved was c6c6015 itself, 'rechecked 0 commit(s)', 'TOTAL problems: 0', 'Machine checks: none failing'. Entry 33 on main went from 'Entry 33 as session a wrote it' (after A's merge) to 'Entry 33 as session b wrote it'. By reading, check_commit.py line 190 counts c6c6015 as approved: 55fc183 is an ancestor of 7ce47ea, so merge-tree gives 7ce47ea's tree. checks-and-cases.md line 42 ('so that resolution goes through, and renumbering the main line's entries is stopped') is false in this shape. The limit added at line 55 ('kept word for word on trust') does not cover it, because here the gate itself directs the renumbering of main's approved entry. Neither c52f191's limits nor the current ones name it. Not checked: GitHub's real parent order, which is taken from GitHub's documentation as the finding says; the rebase way through. Scripts written (new, inline). The shared helpers newclone.sh and fill_receipt.py are used by every walk below:
----- newclone.sh -----
#!/bin/sh
# Verifier's helper: clone the verifier's base copy into a new folder, remove its remote, set a user and switch the
# gate on there. Usage: newclone.sh <new folder>
set -e
V=/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/r6-verify
git clone -q --no-local "$V/base" "$1"
git -C "$1" remote remove origin
git -C "$1" config user.name verifier; git -C "$1" config user.email verifier@example.com
git -C "$1" config commit.gpgsign false; git -C "$1" config core.hooksPath .githooks

----- fill_receipt.py -----
#!/usr/bin/env python3
"""Verifier's helper, for its own scratch copies only: write a SIMULATED review receipt for what is staged in the
copy named by the first argument (the same filling the lead's copy script uses), and stage it. No review ran."""
import re, subprocess, sys
root = sys.argv[1]
made = subprocess.run([sys.executable, ".claude/skills/error-correction/scripts/review_receipt.py", "new", "--root", "."],
                      cwd=root, capture_output=True, text=True)
found = re.search(r"\.claude/reviews/[0-9a-f]{16}\.md", made.stdout + made.stderr)
if not found:
    print("no receipt made:", (made.stdout + made.stderr).strip()[:300])
    sys.exit(0)
path = f"{root}/{found.group(0)}"
text = open(path, encoding="utf-8").read()
answers = {"Change": "SIMULATED receipt (verifier's scratch copy); no review ran", "Maker": "lead agent",
           "Reviewed by": "SIMULATED stand-in (no reviewer)", "Findings": "none (simulated)",
           "Book text": "none added (simulated)", "Verdict": "passed"}
for name, answer in answers.items():
    text = re.sub(r"(\*\*" + re.escape(name) + r":\*\*)[^\n]*", lambda m: m.group(1) + " " + answer, text, count=1)
text = re.sub(r"(## Reviewer's report\n\n)\([^\n]*\)", r"\1SIMULATED. Written by the verifier's helper in a scratch copy so that a planted situation can be walked through the commit gate in that copy only. No reviewer read the change for it, and nothing it says is a finding. It exists only in the verifier's own scratch copy, never in the live repository, and it stands for the review a real change would need.", text)
text = re.sub(r"\n## Tests retired\n.*?(?=\n## |\Z)", "\n", text, flags=re.S)
open(path, "w", encoding="utf-8").write(text)
subprocess.run(["git", "-C", root, "add", found.group(0)], check=True)
print("receipt", found.group(0))

----- set_log.py -----
#!/usr/bin/env python3
"""Verifier's helper, for its own scratch copies only: write the project story in the copy named by the first argument
as the file given by the second argument (a path, or '-' to keep the copy's own), with the extra entries given after
it as NUMBER=LABEL (added before "## Next step"), and every status stamp moved on to the last of them."""
import re, sys
root, source, extras = sys.argv[1], sys.argv[2], sys.argv[3:]
path = f"{root}/StoryTest - project story.md"
text = open(path if source == "-" else source, encoding="utf-8").read()
for extra in extras:
    number, label = extra.split("=", 1)
    text = text.replace("\n## Next step", f"\n{number}. **{label}.** A planted piece of work in a scratch copy.\n\n## Next step", 1)
    text = re.sub(r"\(as of entry \d+\)", f"(as of entry {number})", text)
open(path, "w", encoding="utf-8").write(text)

----- run_u1.sh -----
#!/bin/sh
# Verifier's walk for use-tester finding U1: two sessions each add log entry 33; A's pull request is merged on
# "GitHub" first; B's conflict is resolved the way GitHub's conflict editor does it (the main line merged into B's
# branch, so B's branch is the first parent); B's session carries on from that branch, then its pull request merges.
V=/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/r6-verify
C=$V/u1; G=$V/u1-github.git; W=$V/u1-gh; L="StoryTest - project story.md"
sh $V/tools/newclone.sh $C
git init -q --bare $G
cd $C; main=$(git rev-parse --abbrev-ref HEAD); X=$(git rev-parse HEAD)
git remote add github $G; git push -q github $main 2>/dev/null
for s in a b; do
  git checkout -q -b $s $X
  python3 $V/tools/set_log.py $C - "33=Entry 33 as session $s wrote it"
  git commit -qam "session $s: entry 33 (verifier)" 2>&1 | tail -1
  echo "$s: $(git log -1 --format='%h stamp: %(trailers:key=Workshop-gate,valueonly)')"
  git push -q github $s 2>/dev/null
done
git clone -q -b $main $G $W; cd $W; git config user.name github; git config user.email github@example.com
git fetch -q origin a b
git -c core.hooksPath=/dev/null merge -q --no-ff --no-edit origin/a && PA=$(git rev-parse HEAD) && echo "GitHub merged A's pull request: $(git log -1 --format='%h parents %p')"
git push -q origin $main 2>/dev/null
git checkout -q -b b origin/b
git -c core.hooksPath=/dev/null merge -q --no-edit $main > /dev/null 2>&1; echo "conflict editor: merge of the main line into b stopped: $(git diff --name-only --diff-filter=U | tr '\n' ' ')"
git show $PA:"$L" > $V/u1-main-log.md
python3 $V/tools/set_log.py $W $V/u1-main-log.md "34=Entry 33 as session b wrote it"
git add "$L"; git -c core.hooksPath=/dev/null commit -q --no-edit
echo "resolved the natural way (A keeps 33, B's becomes 34): $(git log -1 --format='%h parents %p')"
git push -q origin b 2>/dev/null
cd $C; git checkout -q b; git pull -q --ff-only github b
echo "--- B's session carries on from its branch: the next commit through the gate"
git commit --allow-empty -m "next commit on b (verifier)" 2>&1 | grep -i "log entry\|All checks\|STOPPED\|note: the last" | cut -c1-240
echo "--- following the gate's advice: entry 33 back as the last approved commit has it, A's entry after it"
git show b~0:"$L" > /dev/null
Bc=$(git log --format=%H --grep="session b: entry 33" -1); git show $Bc:"$L" > $V/u1-b-log.md
python3 $V/tools/set_log.py $C $V/u1-b-log.md "34=Entry 33 as session a wrote it"
git commit -qam "entries put back as the gate asked (verifier)" 2>&1 | grep -i "All checks\|STOPPED" 
echo "E: $(git log -1 --format='%h stamp: %(trailers:key=Workshop-gate,valueonly)')"
git push -q github b 2>/dev/null
cd $W; git checkout -q $main; git fetch -q origin b; git -c core.hooksPath=/dev/null merge -q --no-ff --no-edit origin/b && echo "GitHub merged B's pull request: $(git log -1 --format='%h parents %p')"
git push -q origin $main 2>/dev/null
cd $C; git checkout -q $main; git pull -q --ff-only github $main
echo "--- the next session on the main line"
echo "last approved: $(python3 .claude/skills/error-correction/scripts/recheck_commits.py --last-approved 2>&1 | tail -1)  (B's pull request merge: $(git rev-parse HEAD))"
python3 .claude/skills/error-correction/scripts/recheck_commits.py 2>&1 | tail -2
echo "entry 33 on the main line after A's merge: $(git show $PA:"$L" | grep '^33\. ' | cut -c1-60)"
echo "entry 33 on the main line now:            $(grep '^33\. ' "$L" | cut -c1-60)"
printf '{"cwd": "%s", "hook_event_name": "SessionStart"}' "$C" | CLAUDE_PROJECT_DIR=$C python3 .claude/hooks/session_start.py 2>&1 | grep -i "machine checks\|commits the gate\|problem"


**use-tester:U2: confirmed.** An approved commit rebased with its contents unchanged keeps a matching stamp, so the commits beneath it are settled unseen. This happens on the text's own route for the owner's correction to the gate script.

Grounds: Walked in r6-verify/u2. Local work L1 went through the gate: '6f3bdfe tree ca2bc51... stamp: approved ca2bc51...'. On the stand-in GitHub, with the gate off: 3280021 (a typo in check_commit.py) and d5c7745 (the owner's correction, restoring it). After 'git pull --rebase github <branch>': L1 became 3d14708 with 'tree ca2bc51... stamp: approved ca2bc51...', so the stamp still matches. recheck --last-approved printed 3d14708. The recheck printed 'rechecked 0 commit(s) ... TOTAL problems: 0'. Session start showed only 'Commit gate: on' and 'Machine checks: none failing'. No late receipt was asked for the two GitHub commits, and no note said they changed the gate's own files. prepare-commit-msg never strips a stamp, and rebase runs no pre-commit. Three texts are therefore false. (1) checks-and-cases.md line 36: a rebase 'that goes through without a conflict' carries 'no matching stamp'. c52f191 said 'whose contents changed', which was true, and recheck_commits.py lines 12-13 still say that. (2) Line 66: 'The next commit through the gate then needs late receipts'. (3) Line 38: 'a note is shown only until a commit through the gate is approved'. Here the note is never shown. Must change holds on the false-statement ground. Whether this is also a way round beyond c52f191's limits is arguable, since c52f191's limit 'A note ... is shown only until the next approved commit' covers part of it. Not run: the .epub variant; a cherry-pick with contents unchanged. Script written (new, inline; it uses newclone.sh and fill_receipt.py, given under use-tester:U1):
----- run_u2.sh -----
#!/bin/sh
# Verifier's walk for use-tester finding U2: an approved local commit, then on "GitHub" (a bare repository in the
# verifier's folder) a typo in the gate script and the owner's correction of it, brought in with git pull --rebase.
V=/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/r6-verify
C=$V/u2; G=$V/u2-github.git; W=$V/u2-gh
sh $V/tools/newclone.sh $C
git init -q --bare $G
cd $C; main=$(git rev-parse --abbrev-ref HEAD)
git remote add github $G; git push -q github $main
git clone -q -b $main $G $W; git -C $W config user.name owner-on-github; git -C $W config user.email owner@example.com
cd $W
S=.claude/skills/error-correction/scripts/check_commit.py
sed -i '1a this line is a typo made on github' $S; git -c core.hooksPath=/dev/null commit -qam "typo in the gate script, made on GitHub"
git show HEAD~1:$S > $S; git -c core.hooksPath=/dev/null commit -qam "the owner's correction, made on GitHub"
git push -q origin $main
echo "github: $(git log --oneline -3 | tr '\n' ' ')"
cd $C
printf '\nA line added by the verifier in an approved local commit.\n' >> README.md
git add README.md && python3 $V/tools/fill_receipt.py $C
git commit -q -m "local work L1 (verifier)" 2>&1 | tail -1
echo "L1: $(git log -1 --format='%h tree %T stamp: %(trailers:key=Workshop-gate,valueonly)')"
git pull -q --rebase github $main 2>&1 | tail -2
echo "after pull --rebase: $(git log --oneline -4 | tr '\n' ' ')"
echo "L1': $(git log -1 --format='%h tree %T stamp: %(trailers:key=Workshop-gate,valueonly)')"
echo "--- recheck --last-approved:"; python3 .claude/skills/error-correction/scripts/recheck_commits.py --last-approved 2>&1 | tail -2
echo "--- recheck:"; python3 .claude/skills/error-correction/scripts/recheck_commits.py 2>&1 | tail -4
echo "--- session start (as Claude Code would run it):"
printf '{"cwd": "%s", "hook_event_name": "SessionStart"}' "$C" | CLAUDE_PROJECT_DIR=$C python3 .claude/hooks/session_start.py 2>&1 | grep -i "commit\|note\|approved\|problem" | head -8


**use-tester:U3: confirmed.** A pull request merged by 'Rebase and merge' after main moved, then reverted on GitHub, loses its log entry and receipt, and no check sees it.

Grounds: Walked in r6-verify/u3. Main moved on through the gate (Y cdb3cd0, stamped). Pull request E was made from 798e136 through the gate (a437485, stamped): entry 33, a plot SKILL.md line, and its receipt 39c9350e6cbfc273.md. I rebase-merged it on the stand-in GitHub as a cherry-pick with the gate off: '967fa8f tree efc8ecb... stamp: approved a452bd5...'. The stamp does not match, so the commit is not approved. I then reverted it there (20518b9). After a fast-forward pull, entry 33 was gone (0 lines) and E's receipt file was gone. recheck --last-approved printed cdb3cd0. The recheck and session start reported only 'commit 20518b9bf: no review receipt ... for this change to: .claude/skills/plot/SKILL.md', then 'Machine checks: none failing'. run_all_checks against cdb3cd0 printed 'passed records'. By reading: the files are compared only with Y, which never had the entry or the receipt. find_receipt (review_receipt.py line 211) finds E's receipt in 967fa8f's own tree. The project story is outside the receipt's scope (review_receipt.py lines 59-62), so even the revert's late receipt need not show the removed entry. Neither c52f191's list nor the current one names this, and checks-and-cases.md line 61 says 'or by rebasing'. Not run: the merge-commit neighbour. Scripts written (new, inline; they use newclone.sh and fill_receipt.py, given under use-tester:U1):
----- add_entry.py -----
#!/usr/bin/env python3
"""Verifier's helper, for its own scratch copies only: add log entry N (the second argument) to the project story in
the copy named by the first argument, just before "## Next step", and move every status stamp on to that entry."""
import re, sys
root, number = sys.argv[1], int(sys.argv[2])
path = f"{root}/StoryTest - project story.md"
text = open(path, encoding="utf-8").read()
text = text.replace("\n## Next step", f"\n{number}. **An entry added by the verifier's walk ({number}).** It records a planted piece of work in a scratch copy.\n\n## Next step", 1)
text = re.sub(r"\(as of entry \d+\)", f"(as of entry {number})", text)
open(path, "w", encoding="utf-8").write(text)

----- run_u3.sh -----
#!/bin/sh
# Verifier's walk for use-tester finding U3: a reviewed pull request (log entry 33, a skill line, its receipt) merged
# on "GitHub" by rebasing after the main line moved, then reverted there; then the next session in the local copy.
V=/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/r6-verify
C=$V/u3; G=$V/u3-github.git; W=$V/u3-gh
sh $V/tools/newclone.sh $C
git init -q --bare $G
cd $C; main=$(git rev-parse --abbrev-ref HEAD); X=$(git rev-parse HEAD)
git remote add github $G
printf '\nA line on the main line, added by the verifier through the gate.\n' >> README.md
git commit -qam "main moves on: Y (verifier)" 2>&1 | tail -1
git push -q github $main 2>/dev/null
echo "Y: $(git log -1 --format='%h stamp: %(trailers:key=Workshop-gate,valueonly)')"
git checkout -q -b pr-e $X
python3 $V/tools/add_entry.py $C 33
S=.claude/skills/plot/SKILL.md; line=$(grep -n "Surprise by default" $S | head -1 | cut -d: -f1)
sed -i "${line}s/\$/ (pull request E, verifier)/" $S
git add -A && python3 $V/tools/fill_receipt.py $C
git commit -q -m "pull request E: entry 33 and a skill line (verifier)" 2>&1 | tail -1
E=$(git rev-parse HEAD); echo "E: $(git log -1 --format='%h stamp: %(trailers:key=Workshop-gate,valueonly)') files: $(git show --name-only --format= HEAD | tr '\n' ' ')"
git push -q github pr-e 2>/dev/null
git clone -q -b $main $G $W; cd $W; git config user.name github; git config user.email github@example.com
git fetch -q origin pr-e
git -c core.hooksPath=/dev/null cherry-pick $E > /dev/null 2>&1 && echo "rebase-merged as $(git log -1 --format='%h tree %T stamp: %(trailers:key=Workshop-gate,valueonly)')"
git -c core.hooksPath=/dev/null revert --no-edit HEAD > /dev/null 2>&1 && echo "reverted on GitHub: $(git log -1 --format='%h %s')"
git push -q origin $main 2>/dev/null
cd $C; git checkout -q $main; git pull -q --ff-only github $main
echo "local now: $(git log --oneline -4 | tr '\n' ' ')"
echo "entry 33 lines now: $(grep -c '^33\. ' 'StoryTest - project story.md'); E's receipt present: $(git show --name-only --format= $E | grep -c reviews/ | xargs -I{} sh -c "ls $(git show --name-only --format= $E | grep reviews/) 2>/dev/null | wc -l")"
echo "--- recheck --last-approved: $(python3 .claude/skills/error-correction/scripts/recheck_commits.py --last-approved 2>&1 | tail -1)"
echo "--- recheck:"; python3 .claude/skills/error-correction/scripts/recheck_commits.py 2>&1 | cut -c1-220 | tail -6
echo "--- session start:"; printf '{"cwd": "%s", "hook_event_name": "SessionStart"}' "$C" | CLAUDE_PROJECT_DIR=$C python3 .claude/hooks/session_start.py 2>&1 | grep -v "Next step\|Open corrections\|Owner questions" | cut -c1-220
echo "--- machine checks against the last approved commit:"
python3 .claude/skills/error-correction/scripts/run_all_checks.py --against $(python3 .claude/skills/error-correction/scripts/recheck_commits.py --last-approved 2>/dev/null | tail -1) . 2>&1 | grep -i "records\|RESULT\|removed" | cut -c1-200


**use-tester:U4: confirmed.** Same line as theory-checker:M1. suspense-and-fear.md line 20 credits the Q7 stretch to Gap principle 5 without a label.

Grounds: Same grounds as theory-checker:M1. Line 20 was touched this round and keeps '(Gap principle 5)' on Egri's foreshadowing-as-promise. reveals-and-withholding.md line 74 and term sheet 1.1 call that stretch the workshop's (Q7). The step-2 Q7 search lists six lines, not this one, and the label search finds nothing on it (both run read-only in the live tree). The fix is one label on the line, 'the workshop's stretch, Q7'. One change answers both findings.

**scripts:1: confirmed.** A merge made without the gate counts as approved when one parent is from before the gate, so what that branch got wrong in the files is never judged. This is new in this round.

Grounds: Walked in r6-verify/e2 with run_e2.sh <folder> 35f2939. On a branch from 35f2939 I rewrote log entry 5 with the gate off, then merged it with the gate off: 'merge: 4a31d44 parents 798e136 1237743'. recheck --last-approved printed 4a31d44 (the merge itself). The next commit through the gate printed 'passed records', 'review receipt: not needed', 'rechecked 1 commit(s) ... since the last approved commit, 4a31d4401', 'All checks passed', and was stamped 'approved 32e26f44...' with entry 5 still rewritten. Control (e2c, the same walk from the approved 798e136): 'FAILED records ... log entry 5 has been changed since 798e1360c...', COMMIT STOPPED. By reading: check_commit.py line 190 accepts 'approved(parent) or before_the_gate(parent)'. c52f191's rule was 'most recent approved commit by any path', which would have compared with 798e136. Neither list of limits names this. The recheck also looked at a commit behind an approved merge ('rechecked 1'), so its own note (lines 10-11, 'every commit an approved commit reaches back to is settled') is false too. Not run: e4 (main moved on before the gate). Script written (new, inline; it uses newclone.sh, given under use-tester:U1):
----- run_e2.sh -----
#!/bin/sh
# Verifier's walk for scripts finding 1: log entry 5 rewritten on a branch made from <start> with the gate off,
# merged with the gate off (as GitHub's merge button would), then one ordinary commit through the gate.
# Usage: run_e2.sh <folder> <start commit>
V=/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/r6-verify
C=$1
sh $V/tools/newclone.sh $C
cd $C
main=$(git rev-parse --abbrev-ref HEAD)
git checkout -q -b side $2
python3 - <<'PY'
p = "StoryTest - project story.md"; t = open(p, encoding="utf-8").read()
t = t.replace("5. **Hard-to-vary brought into line with revision 1**", "5. **REWRITTEN BY THE VERIFIER: hard-to-vary brought into line with revision 1**", 1)
open(p, "w", encoding="utf-8").write(t)
PY
git -c core.hooksPath=/dev/null commit -qam "entry 5 rewritten, gate off (verifier)"
git checkout -q $main
git -c core.hooksPath=/dev/null merge --no-edit side 2>&1 | tail -2
echo "merge: $(git log -1 --format='%h parents %p')"
echo "--- recheck --last-approved:"; python3 .claude/skills/error-correction/scripts/recheck_commits.py --last-approved 2>&1 | tail -3
echo "--- next commit through the gate:"
git commit --allow-empty -m "ordinary commit through the gate (verifier)" 2>&1 | grep -v "^ *$" | head -40
echo "exit $?"
git log -1 --format='%h stamp: %(trailers:key=Workshop-gate,valueonly)'
echo "entry 5 now: $(git show HEAD:'StoryTest - project story.md' | grep -n '^5\. \*\*' | cut -c1-80)"


**scripts:2: confirmed.** The gate never runs a changed test_the_gate.py, so a typo in it goes in stamped. After that, every later check change is stopped, including the typo's own correction.

Grounds: Walked in r6-verify/e1. Commit 1 changed only test_the_gate.py, adding a syntax error, as a check-only commit. It printed 'passed the last approved commit's planted-fault test, on the changed checks (2 test(s) not run inside it)', 'All checks passed', and was stamped 83f2ece 'approved b524013...'. Commit 2 added a harmless comment to run_all_checks.py. It printed 'FAILED gate_tests could not run / invalid syntax (test_the_gate.py, line 996)', the same for more_gate_tests, 'TOTAL tests: 153, failed: 2', COMMIT STOPPED. Commit 3 put test_the_gate.py back and was stopped the same way. By reading: check_commit.py line 399 runs the staged test only when test_checks.py itself changed. test_checks.py lines 734-735 import test_the_gate from their own folder, which is the archive of the last approved commit. So 'and the changed test too' is false for this file, at check_commit.py line 68 and checks-and-cases.md line 34. Section 3 step 3 (line 76) also speaks only of putting in the new test_checks.py. The only way out is the owner's route. Script written (new, inline; it uses newclone.sh and fill_receipt.py, given under use-tester:U1):
----- run_e1.sh -----
#!/bin/sh
# Verifier's walk for scripts finding 2: a typo in test_the_gate.py alone, committed through the gate as a
# check-only commit; then a harmless check change; then the typo taken back out.
V=/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/r6-verify
C=$V/e1
sh $V/tools/newclone.sh $C
cd $C
T=.claude/skills/error-correction/scripts/test_the_gate.py
printf '\n\ndef a_typo_planted_by_the_verifier(:\n    pass\n' >> $T
git add $T && python3 $V/tools/fill_receipt.py $C
echo "=== commit 1: typo in test_the_gate.py alone"
git commit -m "typo in test_the_gate.py alone (verifier)" 2>&1
echo "exit $?"
git log -1 --format='%h stamp: %(trailers:key=Workshop-gate,valueonly) tree %T'
echo "=== commit 2: a harmless comment in run_all_checks.py"
R=.claude/skills/error-correction/scripts/run_all_checks.py
printf '\n# a harmless comment added by the verifier\n' >> $R
git add $R && python3 $V/tools/fill_receipt.py $C
git commit -m "harmless comment (verifier)" 2>&1
echo "exit $?"
git log -1 --format='%h %s'
echo "=== commit 3: the typo taken back out"
git reset -q --hard HEAD
git checkout HEAD~1 -- $T 2>/dev/null
git show HEAD~1:$T > $T
git add $T && python3 $V/tools/fill_receipt.py $C
git commit -m "typo taken out (verifier)" 2>&1
echo "exit $?"
git log -1 --format='%h %s'


**scripts:3: confirmed.** Two reviewed check changes joined by a GitHub merge with no conflict take effect untested, then stop every commit, including the check-only correction. The limit added this round for this is not a true limit.

Grounds: Walked in r6-verify/e9a and e9b, each cloned from my base copy. Side A renamed field to field_value in review_receipt.py. Side B added one call field('', 'Verdict') at the top of problems_with. Each side printed 'passed the last approved commit's planted-fault test ... All checks passed' and was stamped (0b10048, d259f52). I merged them with the gate off and no conflict: '96cdd6d parents d259f52 0b10048'. recheck --last-approved printed 96cdd6d. An empty commit through the gate printed 'COULD NOT RUN review_receipt.py (exit 1): ... NameError: name 'field' is not defined', COMMIT STOPPED. The check-only correction (B's call taken out) printed the same stop, even though 'passed the last approved commit's planted-fault test'. That is because the receipt check always comes from the last approved commit (check_commit.py, approved_scripts). My judgement: checks-and-cases.md line 52 is not a true limit. The gate could decline to count as approved a merge whose two sides both changed check files since they split. Then the next commit's staged checks would differ from the first parent's, and its planted-fault test would run on the joined checks. The line also leaves out the cost: every commit is stopped, and only the owner's route clears it. Scripts written (new, inline; they use newclone.sh and fill_receipt.py, given under use-tester:U1):
----- run_e9_side.sh -----
#!/bin/sh
# Verifier's walk for scripts finding 3, one side: a reviewed check-only commit on its own clone.
# Usage: run_e9_side.sh a|b
V=/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/r6-verify
C=$V/e9$1
sh $V/tools/newclone.sh $C
cd $C
R=.claude/skills/error-correction/scripts/review_receipt.py
if [ "$1" = a ]; then
  sed -i 's/\bfield(/field_value(/g' $R          # side A: rename field to field_value everywhere
else
  python3 - "$R" <<'PY'
import sys
p = sys.argv[1]; t = open(p).read()
t = t.replace('def problems_with(root, commit=None):\n', 'def problems_with(root, commit=None):\n    field("", "Verdict")  # side B: one new call (verifier)\n', 1)
open(p, 'w').write(t)
PY
fi
git diff --stat
git add $R && python3 $V/tools/fill_receipt.py $C
git commit -m "check-only change, side $1 (verifier)" 2>&1
echo "exit $?"
git log -1 --format='%h stamp: %(trailers:key=Workshop-gate,valueonly) tree %T'

----- run_e9_join.sh -----
#!/bin/sh
# Verifier's walk for scripts finding 3, the join: side A (clone e9a) merged into side B (clone e9b) with the gate
# off, as GitHub's merge button would; then an ordinary commit, then a check-only correction, both through the gate.
V=/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/r6-verify
cd $V/e9b; main=$(git rev-parse --abbrev-ref HEAD)
git fetch -q $V/e9a $main
git -c core.hooksPath=/dev/null merge --no-edit FETCH_HEAD 2>&1 | tail -1
echo "merge: $(git log -1 --format='%h parents %p')"
echo "--- recheck --last-approved:"; python3 .claude/skills/error-correction/scripts/recheck_commits.py --last-approved 2>&1 | tail -2
echo "--- an ordinary commit through the gate:"
git commit --allow-empty -m "ordinary commit (verifier)" 2>&1 | grep -i "receipt\|COULD NOT\|All checks\|STOPPED\|note:" | cut -c1-300
echo "--- the check-only correction (side B's call taken out):"
R=.claude/skills/error-correction/scripts/review_receipt.py
sed -i '/# side B: one new call (verifier)/d' $R
git add $R && python3 $V/tools/fill_receipt.py $V/e9b
git commit -m "correction of the joined checks (verifier)" 2>&1 | grep -i "receipt\|COULD NOT\|All checks\|STOPPED\|note:\|planted" | cut -c1-300
git log -1 --format='HEAD now %h %s'


**scripts:4: confirmed.** With a git older than 2.38 (no 'merge-tree --write-tree'), a merge's own hand-made changes need no review receipt. The check fails open, and no text states a git version.

Grounds: Walked in r6-verify/e7. Branches x and y each reworded the same plot SKILL.md line through the gate (4b86bc2 and 24a3bf5, both stamped). The merge of x into y stopped on the conflict, and I resolved it by hand with a third, unreviewed wording. I then ran .githooks/pre-commit twice. With the real git 2.43 it printed 'FAILED review receipt / no review receipt .claude/reviews/8a80bf920302ce5e.md ... for this change to: .claude/skills/plot/SKILL.md', COMMIT STOPPED. With PATH led by my stand-in (it fails on --write-tree as an old git does, 'fatal: unknown rev --write-tree', exit 128) it printed 'passed review receipt / review receipt: not needed (no reviewed file changed) / All checks passed; committing.' By reading: review_receipt.py automatic_merge (line 79) returns '' when merge-tree fails. comparison (line 116) then runs 'git diff --cached ""', which fails; I ran that command and it printed 'fatal: ambiguous argument'. So no file is found to need a receipt. check_commit.py line 281 has the same path. A search found no '2.38' or git version stated anywhere outside the kept records. This is older than the round, and graded the same. Not run: a real git older than 2.38; the recheck's path for a conflicted GitHub merge. Scripts written (new, inline; they use newclone.sh and fill_receipt.py, given under use-tester:U1):
----- oldgit/git -----
#!/bin/sh
# Verifier's stand-in for a git older than 2.38, which has no merge-tree --write-tree: it refuses that option the
# way such a git fails on it (an unknown revision, exit 128), and passes everything else to the real git.
for argument in "$@"; do
  if [ "$argument" = "--write-tree" ]; then echo "fatal: unknown rev --write-tree" >&2; exit 128; fi
done
exec /usr/bin/git "$@"

----- run_e7.sh -----
#!/bin/sh
# Verifier's walk for scripts finding 4: a merge through the gate whose conflict is resolved by hand with a third,
# unreviewed wording of a plot SKILL.md line; the gate's hook run once with the real git and once with the stand-in.
V=/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/r6-verify
C=$V/e7
sh $V/tools/newclone.sh $C
cd $C
main=$(git rev-parse --abbrev-ref HEAD)
S=.claude/skills/plot/SKILL.md
line=$(grep -n "Surprise by default" $S | head -1 | cut -d: -f1)
for side in x y; do
  git checkout -q -b $side $main
  sed -i "${line}s/\$/ (wording $side, verifier)/" $S
  git add $S && python3 $V/tools/fill_receipt.py $C
  git commit -q -m "wording $side (verifier)" 2>&1 | tail -1
  git log -1 --format="$side: %h stamp: %(trailers:key=Workshop-gate,valueonly)"
done
git -c core.hooksPath=/dev/null merge --no-edit x 2>&1 | tail -1
sed -i "${line}s/.*/- **Surprise by default.** A THIRD WORDING, NEVER REVIEWED (verifier)./" $S
git add $S
echo "=== the hook with the real git"; sh .githooks/pre-commit 2>&1 | grep -i "receipt\|All checks\|STOPPED\|FAILED\|note:"
echo "=== the hook with the stand-in for an older git"; PATH=$V/tools/oldgit:$PATH sh .githooks/pre-commit 2>&1 | grep -i "receipt\|All checks\|STOPPED\|FAILED\|note:"
rm -f "$(git rev-parse --git-path workshop-gate-passed)"


**scripts:5: confirmed.** C15 says three new tests pass on the old scripts. Six do.

Grounds: I ran the new test_checks.py and test_the_gate.py (from 26bf4fd) on c52f191's scripts, in r6-verify/old (made with git archive from the snapshot). It printed 'TOTAL tests: 209, failed: 23'. c52f191's own test on c52f191 (r6-verify/oldold) printed 'TOTAL tests: 184, failed: 0'. Comparing the names (compare_counts.py below): 27 names are new, 21 of them fail on the old scripts, and these 6 pass: the two renamed 'after the gate is merged on GitHub as a merge commit' tests; the rebase route; 'after a merge made on GitHub with a conflict, a check corrected on the main line's tip is judged by the wrong check'; 'the check corrected on a branch from the last approved commit, then the main line merged into it through the gate'; and 'hook: the gate folder named by $PWD from the project's top folder is let through'. The other 2 failures carry old names: the two tests that run the real stage. So C15 (corrections line 161) 'three new tests pass there too' is false. So is its 'in each round, the tests that fail on the old scripts are the new ones'. Commands: cd r6-verify/old && python3 .claude/skills/error-correction/scripts/test_checks.py; cd r6-verify/oldold && python3 .claude/skills/error-correction/scripts/test_checks.py; python3 tools/compare_counts.py count-new-on-old.txt count-old-on-old.txt. Not checked: 209 on the current scripts (not rerun); whether each failure is for its planted fault. Script written (new, inline):
----- compare_counts.py -----
#!/usr/bin/env python3
"""Verifier's helper: from two outputs of test_checks.py (the new tests run on the old scripts, and the old tests run
on the old scripts), list the tests whose names are new and that pass on the old scripts, and count the failures."""
import re, sys
def results(path):
    found = {}
    for line in open(path, encoding="utf-8"):
        match = re.match(r"^(ok|FAILED)\s+(.*\S)\s*$", line)
        if match:
            found[match.group(2)] = match.group(1)
    return found
new_on_old, old_on_old = results(sys.argv[1]), results(sys.argv[2])
new_names = [name for name in new_on_old if name not in old_on_old]
print(f"tests in the new file: {len(new_on_old)}; in the old file: {len(old_on_old)}; names new: {len(new_names)}")
print(f"failing on the old scripts: {sum(1 for r in new_on_old.values() if r == 'FAILED')}")
print("names new that pass on the old scripts:")
for name in new_names:
    if new_on_old[name] == "ok":
        print("  ", name)
print("names in the old file gone from the new:", [n for n in old_on_old if n not in new_on_old])

Left behind by this verification: only /tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/r6-verify/ (the copies base, e1, e2, e2c, e7, e9a, e9b, u1, u2, u3; the bare stand-ins for GitHub and their clones; old and oldold; tools/; the logs). One /tmp/workshop-test-* folder left by a run I stopped was removed. The twenty from 19:49-20:00 are not mine. The live repository is untouched: HEAD 35f2939, 30 entries in git status --short, core.hooksPath .githooks.

Findings graded lower that the verifier judged to meet the must-change definition:

- theory-checker:m7 (graded minor) is the same false count as scripts:5. C15 line 161 says 'three new tests pass there too', and my run shows six. The brief makes a false statement in a record a must change.
- theory-checker:m5 (graded minor, does not bear yet). I ran the test it names: the claim 'every finding ... applied' is in four earlier versions of file 26 (1e92459 and 7812119 in entry 29, 0f14d0a in entry 30, 4430f36 in entry 31). That matches file 26 line 132's 'Four earlier rounds', while the kinds row (corrections line 22, changed this round) says 'entries 29 to 32, five times'. 'Five' holds only if the sixth round's own 'each is now applied' is also wrong, which file 26 says it is not. So either the row or file 26 line 132 is a false statement in a record changed this round: must change.
- theory-checker:m8 (graded minor). The refusal hook's note (refuse_check_bypass.py lines 29-33) says 'Two things are not stopped that way' by the next commit's comparison. More are not stopped: a book file added and later removed (only noted); the other line's entries after a conflicted GitHub merge (on trust); and, in my walks, a pre-gate branch's rewrite (scripts:1), a revert after a rebase-merge (U3) and gate-file commits settled under a rebased stamp (U2). This is a false statement in a hook note. It is older than this round but in a file this round changed, and it is the part of V6 left unanswered: must change.
- theory-checker:m9 (graded minor). File 26 line 29, the short answer rewritten this round from the break test's wording, says 'Most of B's gaps weaken a payoff'. That uses the Gap theory's own central term in an everyday sense (missing set-ups), none of the term sheet's three senses (section 3: 'say which sense at first use'). The brief grades an owner term used in a neighbouring sense must change. The context makes the meaning plain, but the definition does not depend on that.
- theory-checker:S1 (graded should change), borderline. 'So does a jump scare' (reveals-and-withholding.md line 30, written this round) says a jump scare passes the telling test. By that same sentence's test, a jump scare by something the audience does not already have (a ghost in a realist drama) fails it, just as the dragons do. So as written it is a false statement in a line the lead wrote, which the brief grades must change. If it is read as meaning only a typical jump scare, it is merely loose. One clause of scope fixes it.
