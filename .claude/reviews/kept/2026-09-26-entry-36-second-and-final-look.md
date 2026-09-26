*Kept for log entry 36 by the briefing session. Word for word as the agent wrote it, except that every run of eight or more words shared with a book or with the paper was replaced by a marker, "[quotation removed: N words of SOURCE]", so that no source text is committed (CLAUDE.md, copyright rule). The removal script and its run are recorded in entry 36's receipt.*

# Second look: the answers to review round 1, stages of log entry 36

**Reviewer:** an independent agent. I wrote none of this change and did not review it in round 1. I took the one narrow look that `reviews-and-briefs.md` section 4 allows after a round of fixes. I edited, staged, committed or deleted nothing in `/home/user/StoryTest-icm` or `/home/user/StoryTest`. The only commands I ran there were reads (`git --no-optional-locks` diff, show, ls-files and cat-file; the overlap check; the `review_receipt.py fingerprint` read). Everything else ran in my own scratch folder, `scratchpad/second-look/`.

**Target:** branch `claude/icm-story-workspace` in `/home/user/StoryTest-icm`: commit `915aa52` plus the staged change. I exported the staged change from the index to `second-look/staged/`. The worktree has no unstaged edits to these files; only `REVIEW-BRIEF.md` is untracked.

**How I found the edits.** The use-tester's scratch copy (`scratchpad/usetest-copy`, made at 20:50) matches the round-1 reviewers' line numbers. For example, `dialogue-passes.md` lines 19 to 23, cast sheet line 45 and `how-stages-work.md` line 82 read exactly as the reports quote them. I therefore used it as the reviewed state and diffed it against the staged export. That covered 27 changed files; README and eight output READMEs are unchanged.

**Read:** the three round-1 reports; `answers-round-1.md`; `reviews-and-briefs.md` section 4; `.claude/agents/copy-checker.md`. Every changed line in the diff, and every staged file under `stages/`, `_config/` and `CONTEXT.md` in full. The theory passages the fixes cite (Bond principles and limits of care; Implied World Part 2 and "What it predicts"; Gap Part 2 section 4 and writer's question 2). The skill sections the new pointers name. The book passages behind copy-checker findings 1 to 10, 17, 18 and 28, and the paper's sections 3.1, 3.2, 6.1 and 6.3. The season branch `claude/story-questioning-theme-ehokf0` at its current tip `e130ef1`.

---

## 1. The answers, checked against the staged files

### Must-change findings: is each answer true?

**Theory-checker 1 to 13**
- **TC 1: true.** Cast sheet section 2 (staged lines 33 to 44) now says a harmful act puts Side with at risk, not care. Allegiance is held by alignment (principle 2) or balance (principle 4), or "meant to lose it here". "Act by act, in the same stretch" is labelled the workshop's reading and points to `building-a-character.md` section 4, "The price" (it is there). The stage 02 Verify (line 53) and Inputs (Bond principles 2, 4 and 6 and the limits of care; Diagnosing step 3) match. I checked the Bond wording against `bond-theory.md` lines 25 to 29 and 86 to 88.
- **TC 2: true.** Stage 01 Verify, line 66, now reads "keeps ... or twists how the promise is kept (section 11 there), never drops it", with the guest-genre exception and named guarantees. The Inputs load genre-file sections 10 and 11; every genre file's section 11 is "Twisting it".
- **TC 3: true.** World worksheet section 2 splits the two kinds of shorthand. The quote "Worlds with many departures need a guide" matches `implied-world-theory.md` line 76 word for word, and "The door dilated" is at line 50. `voice.md` section 4 does hold "Shared background". The stage 03 and stage 07 Verify items agree, and entry 36 is corrected.
- **TC 4: true.** Scene weave line 24 and stage 05 Verify line 43 add emphasis, *Lost* and a later-season slot, which Gap lines 64, 66 and 78 bear out.
- **TC 5: true.** `how-stages-work.md` section 8 has "When one edit is enough" (line 87); `revision-log.md` section 5 opens with the same route. "Three runs in a row" is credited to the paper, which matches its section 6.3.
- **TC 6: true.** `CLAUDE.md` rule 1 (line 28) and the table row (line 43) are qualified, and entry 36 records the error-correction skill's row as owed. See finding F7 for one gap left.
- **TC 7: true.** There is a clause in `CLAUDE.md` line 7, and `how-stages-work.md` section 11 has the matching paragraph.
- **TC 8: true.** I confirmed each part:
  - `git cat-file -s` gives 91,576, 99,968 and 99,836 bytes at `c9429dd`, `d4d3cea` and `0ad292a`.
  - The committed Tested line reads "214 tests, all passing" at both `d4d3cea` and `0ad292a`.
  - The maker's outputs end "failed: 0" at `c9429dd` and "failed: 4" at `d4d3cea`.
  - `test_the_gate.py` (lines 549 to 580) makes both "outside" tests require "passed the last approved commit's planted-fault test", which runs the whole test inside. So entry 36's new "they fail whenever another test does" is borne out.
  - The Open corrections line now names the owed correction.
- **TC 9: true** as to the other reading and why it was not taken. But the same bullet keeps a claim that its source has since corrected: see finding F1.
- **TC 10: true.** Both quotes in `writer.md` question 4 match `07 Owner feedback 1`, line 7. The narrow and wide readings are both put, and "shown by what happens" is credited to the season session.
- **TC 11 (a) to (e): true when written.** "Feature" is gone. "Try something other than Dystopia." is quoted exactly. Three and four helpers are both recorded. Two rounds are credited to the season plan. Item (d) has since been overtaken: see finding F2.
- **TC 12: true when written, and the re-credits are true.** All five sources lines now say "the Fourth Direction season project's practice". The "planned, not done" wording has since been overtaken: see finding F2.
- **TC 13: true.** Premise worksheet section 5 (line 65) gives both cases with their costs. The "second rival in section 9" is "Is theme always moral?", as claimed.

**Copy-checker must-changes: 1 to 10, 15, 17, 18, 19, 21, 22, 23, 28, 30, 32, 38**
- **CC 1 to 9:** true. Read again as the copy-checker in part 2.
- **CC 10: mostly true.** The wish-list examples and the cost detail are gone. But the list of what repeats ("a kind of person, a kind of story, a subject, a voice", line 13) has moved, reordered, into the paragraph the first reader passed. Verdict: does not bear yet (four ordinary categories, reordered).
- **CC 15, 17, 18, 19, 21, 22, 23, 30, 32 and 38:** true.
- **CC 28: reworded, and needed for a rival.** "Weigh the hero's actions, and the choice itself, against their own lives" still follows the shape of his closing sentence. Verdict: does not bear yet. Separately, "unresolved" stands in for his "ambiguous"; see finding F9.

**Use-tester 1 to 6, 8 to 10, and 12 to 14 and 16 at low weight**
- **All true.** Every contract loads all of `how-stages-work.md`, and each Process step 1 records edits. `opponents.md` section 9 is loaded. The last rival in `building-a-cast.md` section 12 is the point-of-view one, with its test in section 11. Stage 01 now loads the genre skill's "Built on" passages word for word as `genre/SKILL.md` line 16 lists them, with the Horror and Fantasy additions. Critique and revision files are named by target in stages 01, 08 and 09, their references, the output READMEs and section 12. The project log comes first everywhere. hard-to-vary is loaded in stages 02 to 07.
- **UT 16(c)** opened a new route that stage 08 does not yet fit: see finding F5.
- **UT 7 and UT 11:** true. S16 and S17 are put to the owner, with labelled stopgaps in stage 01 step 1, `_config/` and the cast sheet.
- **UT 15:** true. It is recorded as open in entry 36, with its test.

**The maker's checks, rerun where allowed**
- `overlap_check.py` at 8 and 6 words: the same results the maker reports (part 3).
- The maker's pointer script on my export: "checked 348 path mentions and 297 section numbers in 32 files, TOTAL problems: 0".
- `run_all_checks.py` on my export: "RESULT: no check failed". Copying was not run there because the export has no book text; I ran it separately.
- `review_receipt.py fingerprint`: "fa05c7bc3a85acd5, covers: CLAUDE.md". This matches the maker's report.
- I did not rerun `test_checks.py`, as the rules ask.

### Should-change findings: sample

I checked more than a third of each list:
- **Theory-checker 14 to 24: all 11 true.** Truby's side is labelled *built* and scored on "cheated" only, with its home owed. The labels in TC 15, 17 and 18 are in place. TC 16 has no *promise*. TC 19 uses the full rule. TC 20 adds the `_config/` exception. TC 21 fixes the Inputs. TC 22 is fixed in S15. TC 23 now reads "mysteries". For TC 24, the sizes check out at characters divided by four: `CLAUDE.md` about 2,713 tokens, `CONTEXT.md` about 1,377, contracts about 929 to 2,162.
- **Copy-checker 11, 12, 13, 16, 20, 24, 26, 29, 31, 33 and 39: all 11 checked, all true.**
- **Use-tester's low-weight 12, 13, 14 and 16: all true,** except the draft route in finding F5.

### New findings from this look

**F1. A record of the owner's words that its own source now contradicts**
- **Target:** entry 36, "How it was read" (`StoryTest - project story.md`, staged line 192): "the briefing session asked, and you answered: 'These books'". The bullet was rewritten in this round (TC 9, CC 38).
- **Defect:** the claim is now known to be false.
- **Grounds:** the season session is the briefing session. Its log was corrected at 21:16 (commit `e130ef1`, `Fourth Direction season - project story.md` line 103): "Correction to entry 9: I wrote that I asked which book you meant. I didn't ask; you told me without being asked."
- **Connection:** once committed, entry 36 would be a kept record that is wrong about an exchange with the owner. That is a tripwire ("a record ... turns out to be wrong after it was committed"). Fixing it now takes one clause, for example "you then said, without being asked: 'These books'".
- **Verdict:** bears (must change).

**F2. "Not yet in" is now false: the season's second attempt has reported, and its result bears on the design**
- **Target:**
  - premise worksheet section 3, staged line 32: "That second attempt's results are not yet in";
  - `how-stages-work.md` section 12, line 117: "(planned in the second attempt; not yet run when this was written)";
  - `_config/writer.md` question 10, line 21: "they had not finished when this was written".
- **Defect:** a present-tense claim that is now false. It is used as the reason for stage 01's method of writing rivals from different kinds of story. The two dated clauses also bring back the problem use-tester stall 12 named, a dated status line inside a rules file. The fix round took one out of section 8 and added two.
- **Grounds:** season branch commit `906c2df` (21:16), log entries 10 to 12 and files 10, 11 and 12:
  - three pitches, each from a different kind of story (crime, coming-of-age, detective);
  - three independent reviews;
  - the owner chose *Seconds* ("First is best").
  - The originality review found all three still echoing the dropped first attempt: B and C take Caraway's ending (file 11, line 20), and even A's "engine of the doom is Caraway's Fast" (line 65).
- **Connection:** the worksheet cites the season as its reason and says the test has not come back. It has, and it partly cuts against the claim that different starting points keep rivals apart. "Not shown to work" still holds; "not yet in" does not.
- **Change:**
  - The worksheet: say what the reviews found, and keep "not shown to work".
  - Section 12: map files 10, 11 and 12, and drop the dated clause.
  - Question 10: say what the second attempt did, and that the owner chose its first pitch.
- **Verdict:** bears (must change) for the worksheet sentence. The other two go in the same edit.

**F3. The rewritten references send stage agents to book text that is not committed and that no Inputs table loads**
- **Target:** seven places, all rewritten this round for copy-checker findings 1 to 6 and 10:
  - premise worksheet line 11 ("Use them as he describes them"), line 53 ("Use it from the book") and line 73 ("follow it from the book");
  - cast sheet line 11 ("use his list from the book") and line 33 ("Use the steps from the book");
  - `dialogue-passes.md` line 19 ("Use his list from the book");
  - `critique-rounds.md` line 38 ("read it there").
- **Defect:** a fix that breaks something else. Each place tells the stage agent to work from the book. But:
  - `sources/raw/` is git-ignored (`.gitignore`), and `reviews-and-briefs.md` line 36 says the book texts are absent in "most sessions";
  - no Inputs table names a book;
  - `how-stages-work.md` section 2, line 29 says a stage "loads exactly the files and sections its Inputs table names, and no others";
  - section 10, line 101 says "A craft book's ideas arrive through the references, already in the workshop's own words".

  So the instruction contradicts the shared rules in every session, and cannot be followed in most.
- **Grounds:** the files and lines above. The first round treated the same kind of stall as a must-change (UT 10: a step that sends the agent to files its Inputs do not load).
- **Connection:** where a reference has its own fallback, a run only loses some detail. Dialogue section 2 falls back to the dialogue skill's Building steps and the scene card; premise section 7 to `structure-and-conflict.md` section 2; critique section 4 has its own questions; the cast sheet's section 1 has its own columns. Two core steps have no fallback:
  - the moral line (cast sheet section 2, stage 02 step 5, and S17's "every step");
  - the change at the centre (premise section 4, which says "Use it from the book").

  There an agent without the book either skips the step or rebuilds Truby's list from memory. The second is a copying and fidelity risk in the output.
- **Change (no book text needed):**
  - One rule in `how-stages-work.md`, in section 1's exception or section 10: when a reference points into a book, read the named passage in `sources/raw/` if it is present, as an input beyond the Inputs table, and never copy from it into an output. If it is absent, work from the reference's own description and the skills it names, and record "book not present" in the Verify (not a pass).
  - For the moral line and the change at the centre, one line each saying what to do without the book.
- **Verdict:** bears (must change).

**F4. Section labels left stale by the renames**
- **Target:**
  - stage 08 contract line 18 ("the second-viewing lens"; the section is now "The ending-backwards lens");
  - stage 06 contract line 19 ("action first, the chain under each beat") and line 31 ("running the chain under each beat to its fourth link"). The reference now calls its sections "Action now, talk in stage 07" and "McKee's five steps, divided between two stages", and no longer speaks of a chain or links.
- **Defect:** the Inputs "For" column and a Process step name sections that no longer exist under those names.
- **Grounds:** `critique-rounds.md` line 36; `drafting-scenes.md` lines 9 and 19.
- **Connection:** an agent can still find them. This is the kind of drift the pointer script cannot see.
- **Verdict:** bears (low; should change).

**F5. The new "bring your own draft" route meets a stage 08 that needs a premise**
- **Target:** stage 01 step 5, staged line 44 (a draft is saved as `draft-v1.md` with "a one-line brief"); `CONTEXT.md` lines 15 and 21; stage 08 contract line 13 (reads `premise-vN.md` "when the target is not the pitches").
- **Defect:** a brought-in draft has no premise, so stage 08's Inputs name a file that does not exist. Step 5's "write a one-line brief" also sits oddly with step 4, which has already written a full brief.
- **Grounds:** the lines above.
- **Connection:** the route that UT 16(c) and (a) asked for ends one step short.
- **Change:** "and `premise-vN.md` when one exists"; and say that step 4's brief may be one line for a brought-in draft.
- **Verdict:** bears (low; should change).

**F6. The review counts in entry 36 do not match the report they summarise**
- **Target:** entry 36, "Reviewed", staged line 196: "nine passages followed a book's list in its order and too near its wording, and three the paper's".
- **Defect:** the copy-checker's report asks for rewrites of 8 book passages at "bears" and 9 at "bears (minor)". It names four places that keep the paper's expression (findings 8, 30, 32 and 38).
- **Grounds:** `copy-checker.md`, "Answers to the brief's items 1 to 3", item 3, and its verdict list.
- **Connection:** the owner reads this bullet as the account of the review.
- **Change:** drop the numbers or use the report's.
- **Verdict:** bears (low; should change).

**F7. `how-stages-work.md` is left out of the qualified rule 1**
- **Target:** `CLAUDE.md` line 28 and the line 43 table row ("the stage contracts and references and `CONTEXT.md`"); S15 (the same list, and option (a)).
- **Defect:** `stages/how-stages-work.md`, the rules every stage loads in full, is neither a contract nor a reference. It is also outside the gate, but the qualified sentence does not name it, and S15's option (a) as worded would leave it out.
- **Grounds:** `review_receipt.py` scope (`stages/` is not listed); `how-stages-work.md` line 3.
- **Change:** "everything under `stages/` except the outputs", or name the file.
- **Verdict:** bears (low; should change).

**F8. The edit record names its categories differently from section 8**
- **Target:** `stages/owner-edits.md` line 5: "*one-off* (a touch only you could add ...)", with "cut the opening" as its first example of a kind.
- **Defect:** section 8 now calls this category "A change only you could make" and dropped "cutting the opening" (CC 8). The record's key still uses the old name and example.
- **Grounds:** `how-stages-work.md` lines 82 and 83; `CLAUDE.md` "Plain words" (one word for one thing).
- **Connection:** this is not a copying problem (three or four ordinary words). It is two names for one thing.
- **Verdict:** does not bear yet (a light edit).

**F9. The rival's book side should keep Truby's own word**
- **Target:** `critique-rounds.md` line 49: "leave its moral argument unresolved".
- **Defect:** Truby's word is "ambiguous". An ambiguous argument supports more than one reading; an unresolved one is not settled. A rival should state the other side's claim exactly, and one word is not copying.
- **Grounds:** `truby-anatomy-of-story.txt` line 3713, "Make the moral argument ambiguous".
- **Verdict:** does not bear yet.

**F10. Two book pointers are slightly off**
- **Target:** `drafting-scenes.md` line 21 ("his chapter on dialogue design"); cast sheet line 29 ("his chapter on the parts of desire").
- **Defect:** "Dialogue Design" is McKee's Part Four. The five steps and "The Complex of Desire" are sections of its chapter 12, "Story/Scene/Dialogue".
- **Grounds:** `mckee-dialogue.txt` line 2623 (contents).
- **Verdict:** does not bear yet (readers will find them).

No fix I checked misreads an owner theory or brings back a rejected reading. The cast sheet, the world worksheet and the scene weave now each walk their theory's own case (*Psycho* and Walter White; "the door dilated"; *Lost*) the way the theory does.

---

## 2. Copy-check of the rewritten text for copy-checker findings 1 to 9

Book text present: `ls sources/raw/*.txt` lists all four texts. For each passage I read the new text beside the book passage the first reader cited. I also ran:
- the overlap check at 8 and 6 words;
- a one-word-swap scan at 7 and 6 words, using the first reader's `near_runs.py`, which only reads, on the eight rewritten files.

The swap scan found only ordinary phrases, plus the items noted below.

1. **Target:** `dialogue-passes.md` section 2, lines 17 to 21, and line 3.
   - **Defect:** none left. His questions and his order are gone, and a pointer with the workshop's proportion rule remains. Asking before, during and after writing is his idea, reworded. (He actually says "on every beat", "in the middle", and "for a third time".)
   - **Grounds:** `mckee-dialogue.txt` lines 2492 to 2516, "Key Questions".
   - **Connection:** no list, no order, no glosses.
   - **Verdict:** does not bear.

2. **Target:** `drafting-scenes.md` section 2, lines 19 to 25.
   - **Defect:** none. The step names are his term names, four words or fewer each, used only as labels mapped to scene-card fields. His glosses are gone, and the aphorism is quoted and attributed.
   - **Grounds:** `mckee-dialogue.txt` lines 1428 to 1437, "Five Steps of Behavior".
   - **Verdict:** does not bear. (Pointer precision: finding F10.)

3. **Target:** cast sheet section 2, lines 31 to 44.
   - **Defect:** none. A one-sentence pointer to his "basic strategy"; the care plan and its table are the workshop's own.
   - **Grounds:** `truby-anatomy-of-story.txt` lines 1150 to 1163.
   - **Verdict:** does not bear.

4. **Target:** premise worksheet section 7, lines 71 to 76.
   - **Defect:** none. A pointer, then three additions of the workshop's own. "Rough list of the story's events" lightly echoes his "some rough order" (three words).
   - **Grounds:** `truby-anatomy-of-story.txt` lines 485 to 506.
   - **Verdict:** does not bear.

5. **Target:** premise worksheet section 4, lines 51 to 59.
   - **Defect:** "the one action at the middle of the story" matches six of seven words of his gloss for A ("action in the middle of the story"). It is a one-line description of his term, attributed with his letters. The method's steps, his "best able to force" and "remain who he is" are gone; the check is reworded ("has nothing to push against").
   - **Grounds:** `truby-anatomy-of-story.txt` line 263, "[quotation removed: 9 words of truby-anatomy-of-story]".
   - **Verdict:** does not bear.

6. **Target:** `critique-rounds.md` section 4, lines 36 to 44.
   - **Defect:** none. One line on his chapter and a pointer. The four questions come from the Gap theory's reading backwards and the plot skill, not from his list of techniques.
   - **Grounds:** `truby-anatomy-of-story.txt` lines 3702 to 3716.
   - **Verdict:** does not bear.

7. **Target:** world worksheet section 2, lines 24 to 30, and `dialogue-passes.md` section 3, line 25.
   - **Defect:** none. One sentence and a pointer to `voice.md` section 4. His order of points, his contrast of cultures, "close-knit" and the retold *Godfather* example are gone. The dialogue line no longer says "shorthand ... outsiders".
   - **Grounds:** `mckee-dialogue.txt` lines 1390 to 1396.
   - **Verdict:** does not bear.

8. **Target:** `how-stages-work.md` section 8, lines 81 to 89.
   - **Defect:** line 83 keeps the paper's two-part contrast (output helps this run, source helps later ones). That contrast is the registered idea itself, and the wording is the first reader's own suggested fix. "A touch", "a turn of phrase" and "cutting the opening" are gone, replaced by the workshop's own examples. Line 89, "the same kind of edit turns up in one stage's output in three separate runs", now shares "stage's output" with the paper, a shade closer than the reviewed wording. It sits in a sentence that credits the paper and names its "three runs in a row".
   - **Grounds:** `paper-icm-2603.16021.txt` line 907, "Editing the output fixes this run"; line 926, "in the same stage's output three runs".
   - **Verdict:** does not bear for line 83; does not bear yet for line 89 (a light reword is optional). The leftover "cut the opening" and "a touch" in `owner-edits.md` are finding F8.

9. **Target:** plot worksheet section 3, lines 30 to 39.
   - **Defect:** the efficient/effective pairing and the battle-and-war clause are gone, and tactics and strategy appear as term names with a pointer. "Campaign" is his word too ("a larger campaign"), used here as the first reader proposed. Line 34 still has "(what sequence of actions would win the goal)", the phrase the first reader named ("sequence of actions ... overall goal").
   - **Grounds:** `truby-anatomy-of-genres.txt` lines 757 to 761.
   - **Verdict:** does not bear yet (slight). Rewording the parenthesis, for example "what order of moves would win it", would settle it.

**Result of the copy-check:** none of findings 1 to 9 still bears. Two light rewords are optional: plot worksheet line 34, and `how-stages-work.md` line 89.

---

## 3. `overlap_check.py` at 8 words on `stages/`, `_config/` and `CONTEXT.md`

Run from `/home/user/StoryTest-icm` as `python3 .claude/skills/add-source/scripts/overlap_check.py sources/raw/<source>.txt stages _config CONTEXT.md`:

```
######## mckee-dialogue
TOTAL problem spans >= 8 words: 0
exit code: 0
######## truby-anatomy-of-story
TOTAL problem spans >= 8 words: 0
exit code: 0
######## truby-anatomy-of-genres
TOTAL problem spans >= 8 words: 0
exit code: 0
######## paper-icm-2603.16021
TOTAL problem spans >= 8 words: 0
exit code: 0
```

**Also run on my staged export.** Adding `CLAUDE.md`, README, the project story, the questions file and `sources/README.md` gave 0 problem spans against each source; only two spans marked "allowed (title or name)" were printed. At 6 words, which is not required, the only problem span is `plot-worksheet.md`, "the hero and the main opponent", against *The Anatomy of Story*: the span the maker reports and the first reader found does not bear.

---

## What I did not check

- The kept cases: not read.
- `test_checks.py`: not rerun, as the rules ask.
- The `.epub` files: I used the `.txt` copies.
- The use-tester's walk: not run again.
- The four theories: read only at the passages the fixes cite, not in full.
- TC 9's stated reason (the gate, the map check and the kept cases finding the skills by where they are): judged plausible, not traced through the scripts.
- Whether `REVIEW-BRIEF.md` is kept out of the commit: it is untracked now.
- The copy-check was done by eye and by script on the rewritten text of findings 1 to 9. Other book-derived passages were covered only through the should-change sample above.

## Verdict

**Passed after changes.** What must change:
1. **F1.** Entry 36, "How it was read": replace "the briefing session asked, and you answered" with wording that matches the season log's correction (the owner said "These books" without being asked).
2. **F2.** Premise worksheet section 3: replace "That second attempt's results are not yet in" with what the reviews found. All three pitches still echoed the dropped first attempt, two of them in its ending, and the owner chose *Seconds*. Keep "not shown to work". In the same edit, bring `how-stages-work.md` section 12's row and `_config/writer.md` question 10 up to date and drop their "when this was written" clauses.
3. **F3.** Add one rule to `how-stages-work.md` on how a stage treats a reference's pointer into a book:
   - if the book is present in `sources/raw/`, read the named passage as an input beyond the Inputs table, never copying it into an output;
   - if it is absent, work from the reference and the skills it names, and record "book not present" in the Verify;
   - give the moral line (cast sheet section 2) and the change at the centre (premise section 4) one line each on what to do without the book.

Should change, and recorded as open if not done: F4, F5, F6 and F7. Optional: F8, F9 and F10, and the two rewords in part 2.

**Cost and route.** Each of the three must-changes is one or two sentences. None touches `CLAUDE.md`, so the review fingerprint (`fa05c7bc3a85acd5`) is unchanged by them. Under section 4, the edits for them need one more narrow look at those lines only. If this look counts as the second round, the rule is that these go to the owner with that cost before another round starts.

---

# Final narrow look

**Scope.** I looked only at the lines the maker changed in answer to findings F1 to F10 and the two optional rewords, as listed under "Second look" in `answers-round-1.md`. I exported the index again with read-only git commands to `scratchpad/second-look/staged2/` and diffed it against my earlier export (`second-look/staged/`). Exactly the 15 files and lines the coordinator listed have changed, and nothing else. The worktree has no unstaged edits; only `REVIEW-BRIEF.md` is untracked. I edited nothing in either repository and started no agents.

## Each changed line

- **F1: fixed. Entry 36, line 192.**
  - **Target:** entry 36, "How it was read".
  - **Change:** it now reads "you then said, without being asked: 'These books'".
  - **Grounds:** this matches the season log's correction (`e130ef1`, line 103).
  - **Newly wrong:** nothing.
- **F2: fixed. Premise worksheet line 32, `how-stages-work.md` lines 118, 119 and 124, `_config/writer.md` line 21.**
  - **Change:** the result is now given and dated "as of 26 September 2026": three pitches from crime, coming-of-age and detective; independent reviews; the owner chose *Seconds*; and all three still echo the first attempt, two of them in its ending. The worksheet keeps "not shown to keep them apart". Section 12 maps files 10, 11 and 12, and both dated "when this was written" clauses are gone.
  - **Grounds:** I checked the new claims against the season branch at `e130ef1`:
    - "reaching for the same source material" matches file 11's "What all three share", "The same source items" (line 19);
    - "First is best" matches file 12, line 8;
    - file 12's title matches the section 12 row.
  - **Newly wrong:** nothing. The date makes each claim true as a record of that day, not a status that goes stale.
- **F3: fixed. `how-stages-work.md` lines 23 and 24, 31 and 103; premise worksheet line 53; cast sheet line 33.**
  - **Change:**
    - Section 1 has "A second exception". A book present in `sources/raw/` is read as an input beyond the Inputs table and never copied into an output. When absent, the agent works from the reference and the skills it names, and writes "book not present" in the Verify, which is not a pass.
    - Section 2 step 2 names both exceptions, and section 10 agrees.
    - Each of the two core steps has a line for working without the book. The moral line's fallback holds to `premise-and-theme.md` sections 6 and 7, which stage 02 already loads.
  - **Newly wrong:** nothing of weight. One small point: section 10's "never copied or quoted at length" could be read as allowing short copying, while section 1 says plainly "never copy from it into an output". This is optional and does not need a fix.
- **F4: fixed.**
  - Stage 08, line 18: now "the ending-backwards lens".
  - Stage 06, lines 19 and 31: now the reference's new section names and "the first four of McKee's five steps", which matches `drafting-scenes.md` section 2.
- **F5: fixed.**
  - Stage 08, line 13: `premise-vN.md` "when one exists", with the draft case named.
  - Stage 01, line 44: step 4's brief may be "a line or two" for a brought-in draft. This agrees with the `CONTEXT.md` row "writes a short brief".
- **F6: fixed. Entry 36, line 196.** The counts are dropped; it now reads "a number of passages ... and some kept the paper's phrasing". This is true to the report.
- **F7: fixed, with one side effect that comes from my own suggested wording.**
  - **Change:** `CLAUDE.md` lines 28 and 43, S15 (line 106) and README line 80 now say `CONTEXT.md` and "everything under `stages/` apart from the outputs".
  - **Side effect:** that phrase also takes in `stages/owner-edits.md`. That file is a record that gains a row every run, and `how-stages-work.md` section 1 says it is "read as a record, as data". So rule 1's "there the review rests on trust" now seems to ask for an independent review of each row. S15's option (a), if carried out as worded, would make the gate ask for a receipt for each row. The workshop's own rule exempts records that are added to all the time (`reviews-and-briefs.md` section 1).
  - **Verdict:** does not bear yet, and not a must-change. S15 is still an open question for the owner, and carrying out option (a) would be a reviewed change of its own. Record as open: "apart from the outputs and the edit record".
- **F8: fixed. `owner-edits.md` line 5.** It now says "a change only you could make", and its example kinds match section 8 ("cut a speech in half"; "cut the opening" is gone).
- **F9: fixed. `critique-rounds.md` line 49.** It now says "ambiguous", Truby's word.
- **F10: fixed.**
  - `drafting-scenes.md` line 21 now says "his chapter 'Story/Scene/Dialogue'".
  - Cast sheet line 29 now says "'The Complex of Desire', in his chapter 'Story/Scene/Dialogue'".
  - Both match the book's contents (`mckee-dialogue.txt` line 2623).
- **Optional rewords: done, and both settle the point.**
  - Plot worksheet line 34 now reads "the course that would win the goal"; "sequence of actions" is gone.
  - `how-stages-work.md` line 91 now reads "in the work of one stage in three separate runs"; "stage's output" is gone.

## Checks

**`overlap_check.py` at 8 words** on the 15 changed files, against each of the three books and the paper. I ran it both on my export and in the worktree; the files are byte-identical.
```
######## mckee-dialogue
TOTAL problem spans >= 8 words: 0
exit code: 0
######## truby-anatomy-of-story
TOTAL problem spans >= 8 words: 0
exit code: 0
######## truby-anatomy-of-genres
TOTAL problem spans >= 8 words: 0
exit code: 0
######## paper-icm-2603.16021
TOTAL problem spans >= 8 words: 0
exit code: 0
```

**`run_all_checks.py` on my read-only export of what is staged** (`second-look/staged2`):
```
passed    frozen files
passed    maps
passed    records
passed    owner quotes
passed    allowed titles
passed    no book files
passed    hooks registered
NOT RUN   copying from books
          no book text here; the review receipt must say what book text a change adds
RESULT: no check failed
```
- It also printed three notes. Two say what could not be checked in a copy without git history (whether the frozen list was only added to; whether old log entries were rewritten). The third is the standing note that kept cases have not been rerun since the five craft skills changed.
- Copying was not run because the export holds no book text. The overlap run above covers it.

**Other reads:**
- `review_receipt.py fingerprint` gives `ceec8814fab18303`, covering `CLAUDE.md`, as the maker says. The receipt must be made for this fingerprint.
- The maker's one-off pointer script on my export reports one problem: "`sources/raw/` does not exist". That is only because the export has no git-ignored book folder, and the new text itself says the folder is present in some sessions only. In the worktree the folder exists. This is a limit of the script, not a fault in the text.

## Is anything a must-change?

No. Every change does what its finding asked, and none misreads an owner theory or a source. The only new problem is the F7 side effect above, which is short of a must-change. Under section 4 it is recorded as open, not fixed.

Recorded as open:
1. `CLAUDE.md` rule 1, its table row, S15 and README say "everything under `stages/` apart from the outputs"; this should also except the edit record, `stages/owner-edits.md`.
2. Optional: section 10's "never copied or quoted at length" could be tightened to match section 1's "never copy".

Before committing, the maker's usual step still applies: entry 36's status line and its "Committed, and waiting" bullet should record this second look and its result.

## Verdict

**passed**
