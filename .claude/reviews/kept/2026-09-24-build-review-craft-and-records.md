# Review of the error-correction build: the changes to the craft skills, and the records and kept cases, 24 September 2026

What this is: the reviewers' reports, word for word, as the review workflow returned them (each an independent agent that did not make the change). They reviewed the working copy as it stood at about 13:35 UTC, before any of their findings were applied. How each finding was answered is in the build's review receipt. Kept for log entry 29.

---

```json
[
 {
  "id": "craft-changes",
  "findings": [
   {
    "target": "All five craft SKILL.md files, the shared reply-check (plot/SKILL.md:139, story-world/SKILL.md:142, character/SKILL.md:110, dialogue/SKILL.md:153, genre/SKILL.md:176), the sentence \"Let the result show: for each main note, say what holds it (a line of the draft and a theory principle), or that it is a guess.\"",
    "defect": "The sentence allows only two answers: a theory principle holds the note, or the note is a guess. It leaves out the other two things that can hold a note: a book rule (marked fitted, built or asserted) and the workshop's reading, with its owner-question number. So a note that rests on Truby or McKee has to be credited to a theory or called a guess. A note that rests on an open owner question (Q1, Q3, S6 and so on) gets reported to the writer as if a theory principle settled it. In Building mode there may be no draft line at all, only a pitch.",
    "grounds": "The rule card (error-correction/references/writing-rules-and-rivals.md, section 2, step 1) names three things that can hold a rule: a theory principle, a book marked fitted/built/asserted, or the workshop's reading with its question number. The descriptions of dialogue and genre say they are built on the theories and also on McKee's Dialogue and Truby's Anatomy of Genres. Character Diagnosing Step 3's turned-round ladder is S6. Plot scenes.md:25 (world-business scenes) is Q1. In the kinds table of 27 Corrections, 'A claim credited to the wrong theory' is the second row. theory-checker step 5 requires a reading to be labelled with its question number.",
    "connection": "The passage is word for word the same in all five skills and runs on every reply. It therefore pushes the workshop's second-commonest error (wrong credit) and an open question stated as settled into every reply that rests on a book or a stopgap reading. Mark on this sub-rule: the demand to show what holds a note is held (C1, H41). The list of what can hold it is wrong.",
    "verdict": "bears",
    "severity": "must change",
    "proposed_change": "Replace the parenthesis with: \"say what holds it: a line of the draft (or of the pitch), and what the point rests on (a theory principle; a book, marked fitted, built or asserted; or the workshop's reading, with its question number), or say that it is a guess.\" Change all five copies together. check_maps.py keeps them identical."
   },
   {
    "target": ".claude/skills/plot/references/reveals-and-withholding.md:30, the last sentence: \"The theory adds the caution: emphasis is a promise, so give it only to what pays off, and not so much that the turn is guessed.\"",
    "defect": "(a) The new clause \"not so much that the turn is guessed\" is written for any turn and credited to the theory. The theory's own bomb case, which the same paragraph uses as the model of one clear showing, fails it: once the bomb is shown, the audience is meant to expect the explosion. (b) \"Emphasis is a promise\", applied to a planted fact, is the workshop's stretch of the promise to set-ups (Q7). Section 6 of the same file labels that stretch (line 74). Here it is credited to 'the theory' and carries no tag. (c) The new core test, 'a first-time audience could notice it', has no label saying what holds it. The only tag in the sentence (McKee, built) covers ranking facts by weight.",
    "grounds": "Gap Part 2 section 3: \"Show them the bomb first and you get fifteen minutes of suspense.\" Gap Part 2 section 4 / principle 5: the promise belongs to open questions. The questions file, Q7: \"the plot skill stretches it to set-ups and foreshadowing.\" Plot Words: a turn is any point where the story changes direction. Rule card step 4: if a theory's own case comes out wrong, the rule contradicts the theory. Marks on the re-tuned rule. 'Noticeable before the turn' is held by Egri's set-up and payoff (section 6, built) and by the reversal's second-viewing check (section 4). 'One clear showing can be enough' is held for a fact meant to be seen (the bomb). 'Not guessed' is held only for a turn meant to surprise (Sternberg's surprise, Gap Part 2 section 3). For a suspense turn it contradicts the bomb.",
    "connection": "A writer planning a suspense turn the bomb way would be told to underplay the showing that the theory says creates the suspense. And because the Q7 stretch is credited to the theory without a tag, a Q7 search will not find this sentence when the owner answers.",
    "verdict": "bears",
    "severity": "must change",
    "proposed_change": "Rewrite as: \"The theory's promise, stretched here to set-ups (the workshop's reading, Q7): emphasis is a promise, so give it only to what pays off. For a turn meant to surprise, keep the showing light enough that the turn is not guessed (the Gap theory's surprise: you thought you understood and were wrong). For a turn meant as suspense, as with the bomb, being seen is the point (section 1).\" Also label what holds 'could notice it', for example Egri's set-up and payoff (section 6, built)."
   },
   {
    "target": ".claude/skills/plot/SKILL.md:12 (\"What else counts as a gap, for example one never mentioned at all, is a question put to the owner, Q2.\") and .claude/skills/error-correction/references/owner-terms.md:95 (\"is also put to the owner under Q2\")",
    "defect": "The tag points to a question that does not contain the point. Q2 asks only which sense 'gap' takes (options a to c). It never asks whether a gap that is never mentioned counts.",
    "grounds": "The Q2 text in '22 Questions - meanings only you can settle.md'. `git log -S \"never mentioned\"` on the questions file returns nothing, and `grep` finds the phrase only in plot/SKILL.md and owner-terms.md. The owner can meet this point only by way of S13 and owner-terms.md, section 13, item 3.",
    "connection": "When the owner answers Q2, the recheck (owner-answers-and-revisions.md, section 2) will mark this passage as answered although the sub-question was never asked. Meanwhile the skill tells readers something was put to the owner that was not.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Add the sub-question to Q2 in the questions file (that file is not frozen) and keep the tag. Or tag the passage S13 and write \"listed for the owner under S13\". Make the same change at owner-terms.md:95."
   },
   {
    "target": ".claude/skills/plot/SKILL.md:12, the one line that carries both Q2 and Q4, read by .claude/skills/error-correction/scripts/check_records.py:241",
    "defect": "The records check looks for the word 'answered' anywhere on the line, not beside each question number. Once one tag on a line is marked answered, a later answer to the other tag on that line is never flagged.",
    "grounds": "A run on a scratch copy of the skills and the questions file. I set Q2 and Q4 to 'Status: answered' and rewrote the plot line to \"(owner question Q4, answered 30 Sep: option a)\". check_questions() then flagged the Q2 and Q4 lines in owner-terms.md, but nothing at plot/SKILL.md:12, whose Q2 citation had not been rechecked.",
    "connection": "Tags exist so that the recheck after an owner answer runs by itself (error-correction 'Where the process runs', the row 'An owner answer ... By itself for tagged passages'). On the one line with two tags, the check passes while the passage is wrong. That is the kind of error the 'A check that passes while the thing is wrong' row describes.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Make the check look for 'answered' next to that question's number (for example, the number followed within the same parenthesis by 'answered'). Add this planted fault and its innocent neighbour to test_checks.py. Putting the two tags in separate sentences would not help, because the Words paragraph is one line."
   },
   {
    "target": "genre/SKILL.md:21-22 (promise stretched to owed moments = Q7; expected mystery = S8; a guarantee broken at the end = S5), story-world/SKILL.md:12 (price for attention and cost for stakes = Q4; strangeness = Q5; the Implied World sense of gap = Q2), plot/references/suspense-and-fear.md (dread / the suspense of helplessness = Q6; tension = S1); and log entry 27's claim \"your questions numbered and tagged where the skills rest on them\"",
    "defect": "Tags were added only where a passage already said 'put to the owner'. The passages that the questions themselves name first carry no number, so the log overstates what was done.",
    "grounds": "Q7 names \"The genre skill stretches 'promise'\" first. Q4 says \"The skills say price for attention and cost for stakes\", and owner-terms section 5 makes story-world the owning skill. `grep -rn \"Q7|Q4|Q5|Q6|S5|S8\" .claude/skills/genre .claude/skills/story-world` returned nothing. The second search in owner-answers-and-revisions.md, section 2 (\"workshop's reading|stopgap|put to the owner\") finds no line of genre's Words paragraph, which says 'the workshop stretches' and 'the workshop's extension'. A search for 'promise' alone returns hits all through the skills.",
    "connection": "When Q7 is answered, neither the records check nor the two named searches reach the main passage Q7 is about. The owner has been told that the tagging is complete.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Tag these passages (genre Words: Q7, S5, S8; story-world Words: Q2, Q4, Q5; plot suspense module: Q6, S1; character: S2, S6). Or, before commit, reword entry 27 to \"tagged where a passage already named an owner question\", and add \"workshop stretches|workshop's extension\" to the recheck search."
   },
   {
    "target": ".claude/skills/error-correction/references/writing-rules-and-rivals.md:24, rule card step 3: Write what is actually held (\"more than once, in different scenes\")",
    "defect": "The rule card's example of 'what is actually held' is the old planting rule. The re-tuned rule says no number is held and one clear showing can be enough.",
    "grounds": "reveals-and-withholding.md:30: \"How often is not fixed, and no number is held: one clear showing can be enough\". The same file's section 1 (line 9) and C12 say the held part is 'noticeable before the turn'.",
    "connection": "Every future rule writer uses the rule card, and its example teaches again the rule that C12 removed. That is 'a rule changed in one place but not its copies' (a row of the kinds table), inside the tool built to stop it.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Replace the example with the held wording (\"noticeable before the turn\") or take one from another rule, and mark \"twice\" as the example of a free specific."
   },
   {
    "target": ".claude/skills/error-correction/references/owner-terms.md:218-219, block 9.2, the Miss (H5) bullet and \"Open: settled by the theory.\"",
    "defect": "The block states \"A loss cannot stand in for that time\" flatly, and its Open line says 'settled by the theory'. But the same sheet's section 13, item 16 calls this the workshop's reading with no question number, and S13 puts exactly this point to the owner.",
    "grounds": "Bond Part 2 section 1: the Up montage \"climbs every rung of the ladder in order: specific details, a shared dream, small sacrifices, and then the loss.\" The questions file, S13: \"whether the loss in Up builds the Miss rung or spends it\".",
    "connection": "A checker using the sheet would pass a passage that states the reading as the theory's, and fail one that reads the loss as completing the climb. An open question would be enforced as settled, which the sheet's own 'How to read it' forbids.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Open line: \"settled by the theory, except Miss and loss: the workshop's reading (section 13, item 16), put to the owner under S13\". Label the 'cannot stand in' sentence as the workshop's reading."
   },
   {
    "target": "The shared reply-check in all five craft skills, as a whole",
    "defect": "Possibly too heavy. It adds a visible trace to every reply: what each fix costs, verdicts given both ways, the stock-note test, the flip, what holds each main note, and what to do with pushback. This comes on top of the six-part Reply order and Building step 8's hard-to-vary tests, and the check has no 'in proportion to the case' of its own. On the other side: it sits inline and is short, which avoids H25's cause (a pointer to the full procedure).",
    "grounds": "Log entry 20 (\"too heavy a hand-off to hard-to-vary\"); H25; error-correction SKILL.md:89. Kept-case run 1 already shows agents improvising around the Reply order alone (kept-cases/runs/2026-09-24-before-entry-27.md lines 44, 115, 321, 477, 819, 886). No run on the new text exists yet (kept-cases/runs.md has only run 1, and the records check notes all five skills changed since their cases ran).",
    "connection": "If the weight makes agents skip it, the check that C1 depends on will leave no trace, and the kinds table's 'reply check (on trust, with a trace)' will be catching nothing.",
    "verdict": "does not bear yet",
    "severity": "should change",
    "proposed_change": "Settle it with a test: rerun the kept cases (at least 09 and 10, and one small case per skill through its quick version) on the new text, with stall reports. See whether the check's trace appears, whether it is skipped, whether new stalls name it, and how reply length compares with run 1. Meanwhile consider adding 'in proportion to the case' to the check."
   },
   {
    "target": "character/SKILL.md:156 (Diagnosing \"Step 8 - Reply ... reply exactly as in Building, Step 9\"), and the quick versions of story-world, character, dialogue and genre",
    "defect": "In character, the check sits after Step 9 rather than inside it, and the Diagnosing step points to 'Step 9' only. The quick versions of four skills end without sending the agent to the Reply step. Plot's quick version does ('reply as in the Reply step').",
    "grounds": "The file text. Error-correction 'Where the process runs': \"A craft skill's reply | The self-check, with its result shown in the reply\".",
    "connection": "Diagnosing and small cases are where most notes reach writers. If agents do not reach the check there, the claim that every craft reply carries it does not hold.",
    "verdict": "does not bear yet",
    "severity": "minor",
    "proposed_change": "Test: kept cases 03 and 08 (character diagnosing), plus one small story-world, genre and dialogue case through the quick version. Does the check's trace appear? The cheap change is safe either way: Step 8 \"reply as in Building, Step 9, with the check that follows it\", and plot's closing line added to the four quick versions."
   },
   {
    "target": "The reply-check's last sentence (\"If the writer pushes back ... (`error-correction` skill, step 2)\"), against error-correction/SKILL.md:140",
    "defect": "The two texts disagree about what follows an objection that stands. The reply-check says change the note and say so. Error-correction's 'How much to do' says \"a writer's objection to a note stood\" is a tripwire for the full five-part correction in the corrections file. The reply-check never mentions this.",
    "grounds": "error-correction/SKILL.md:139-140.",
    "connection": "An agent following the craft skill will not record a note that a writer showed to be wrong, and the skill rule behind it will not be corrected. Or, if it follows error-correction, it writes workshop records during a writer's session with no guidance.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "Decide one way. Either add to the check \"if the wrong note came from a skill's rule, record it (error-correction, 'How much to do')\", or narrow the tripwire to objections that expose a skill's rule."
   },
   {
    "target": ".claude/skills/add-source/SKILL.md:69, Step 2 item 5 (diff of the stored text against the supplied file)",
    "defect": "The step can be followed only when the theory arrives as a file. So far the owner's theories have come as messages. For a pasted message there is no supplied file, so the agent would compare its own retyping with its own typing.",
    "grounds": "sources/gap-theory-of-narrative.md note: \"the message's closing line ... was left out\". sources/bond-theory.md note: \"the message's closing lines\".",
    "connection": "The step calls itself \"the only moment a slip in copying can be caught\", but as written it cannot be followed in the usual case.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Give both routes. For a file, diff as shown. For a message, show the owner the stored text's first and last lines and where anything was left out, and ask them to confirm. Say in the log which route was used and that a message cannot be checked mechanically."
   },
   {
    "target": ".claude/skills/add-source/SKILL.md:92, Step 5 item 4 (\"write its review receipt; the commit gate asks for it\")",
    "defect": "The step gives no command and no pointer. The order that matters (stage the change first, then `review_receipt.py fingerprint`, then `new`, fill it in, then `git add`) is in error-correction/references/reviews-and-briefs.md, section 2. add-source's map points to that file only for rules, rivals and briefs.",
    "grounds": "reviews-and-briefs.md, section 2, steps 1-5; add-source map table row at line 26.",
    "connection": "An agent taking in a source meets the gate's refusal without the steps to satisfy it.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "Add \"(the error-correction skill's `references/reviews-and-briefs.md`, section 2)\"."
   },
   {
    "target": ".claude/skills/add-source/SKILL.md:84, Step 4 item 4",
    "defect": "(a) \"(`references/reviews-and-briefs.md`, section 5)\" does not name its skill. Read inside add-source, it points to add-source/references/, which does not exist. (b) The rule-card summary lists only two things that can hold a rule (the theory, or a book) and leaves out the workshop's reading with its question number.",
    "grounds": "check_maps.py resolve() (lines 82-113) accepts a short path whenever any skill's name appears on the same line. 'error-correction' appears earlier on this one long line, which is why the map check passed it. C2 records a fix of the same kind. Rule card, section 2, step 1.",
    "connection": "A reader may look in the wrong folder. A rule writer who follows the summary has no slot for a labelled reading.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "Write \"the error-correction skill's `references/reviews-and-briefs.md`, section 5\", and add \"or the workshop's reading, labelled, with its question number\"."
   },
   {
    "target": ".claude/skills/add-source/SKILL.md:70, 76, 77, 92 (\"Fingerprint it\", \"the edit hook\", \"the commit gate\", \"loses its licence\", \"review receipt\")",
    "defect": "Technical terms are used with no plain sentence explaining them. The skill's own stance requires one.",
    "grounds": "add-source/SKILL.md:54: \"Plain words. Explain any term the first time...\". The plain-words rule in CLAUDE.md. The terms are defined only in error-correction's Words paragraph and in the scripts' header notes.",
    "connection": "The owner is not a programmer and reads the skills.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "Add one clause for each, for example \"a fingerprint is a short code worked out from the file's exact contents; change one character and it changes\", and \"loses its licence: may not be relied on until rechecked\"."
   },
   {
    "target": "The reply-check's first sentence, \"For each fix, say what it costs\", in all five skills",
    "defect": "Adds a third sense of 'cost' (what a fix gives up) in files where 'cost' is already a defined word. In plot Words, 'cost' is what the world makes things cost. In story-world Words, it is what a departure demands of the people who live with it. Dialogue's quick version uses 'costs the speaker'.",
    "grounds": "CLAUDE.md: \"use that one word for that one thing\". owner-terms section 5 (price and cost, Q4) records this pair as drifting before.",
    "connection": "In story-world a model could read 'what the fix costs' as what it costs the world's people.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "Write \"For each fix, say what it gives up or puts at risk.\""
   },
   {
    "target": "The reply-check's last sentence, \"if it bears\", in all five skills",
    "defect": "'Bears' is a workshop technical word, defined only in error-correction's Words paragraph. The craft skills never explain it.",
    "grounds": "The plain-words rule in CLAUDE.md; error-correction/SKILL.md:69.",
    "connection": "The owner and the agents reading a craft skill meet a word they have not been given.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "Write \"if it holds up (it 'bears', in the error-correction skill's word)\"."
   },
   {
    "target": ".claude/skills/error-correction/references/owner-terms.md:296, block 11.2, telling test: \"A detail that also does a job (shows which sibling stayed) is implication or plot, not surplus.\"",
    "defect": "The term sheet itself uses 'implication' in a neighbouring sense. The theory's implication is what the surface logically requires. It does not mean a detail doing a plot or character job.",
    "grounds": "Implied World, Key terms: \"Implication: what the surface logically requires. If there are border guards, someone pays them.\"",
    "connection": "A checker could pass a passage that calls a plot detail an 'implication'.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "Write \"is doing plot or character work, not surplus\"."
   },
   {
    "target": ".claude/skills/error-correction/references/owner-terms.md:38, block 1.3, telling test: \"Unsafe, or grieving: a guarantee.\"",
    "defect": "The test folds in 'grieving' (a guarantee broken at the end), which block 1.2 labels as the workshop's extension, S5. Here it has no label.",
    "grounds": "owner-terms.md:30 (S5); Anticipation Part 2 section 5 speaks only of early breaks.",
    "connection": "An open owner question is used as a settled part of a telling test.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "Write \"Unsafe: a guarantee (grief, if it is broken at the end: the workshop's extension, S5).\""
   },
   {
    "target": ".claude/skills/error-correction/references/owner-terms.md:22, block 1.1, \"Owning skill: genre (Words: promise, expected mystery)\"",
    "defect": "The block points a checker to genre's Words for the Gap theory's promise. Genre's Words defines the promise in the stretched Q7 sense (the moments a genre owes). The theory's own sense (open questions, set by emphasis) is used in plot's reveals-and-withholding.md, section 2.",
    "grounds": "genre/SKILL.md:21; the questions file, Q7.",
    "connection": "A checker would compare a passage about the theory's promise against the stretched definition.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "Write \"plot (`references/reveals-and-withholding.md`, section 2) for the theory's sense; genre (Words) for the stretch, Q7\"."
   }
  ],
  "right": "No frozen file changed. `git diff 35f2939 -- foundations sources` is empty, `git status` shows nothing new under sources/, and check_frozen_files passed in run_all_checks.py --skip-books, which reported no failed check. The shared reply-check is identical in all five skills (check_maps.py found no problems).\n\nEach part of the reply-check, apart from its list of what can hold a note, is held:\n- saying what each fix gives up (foundation Part XI, 'expose what it lost');\n- giving a verdict both ways when the aim or the draft order is unknown (Part XIV; C1 and H42);\n- the stock-note test (H44);\n- the flip, which is error-correction step 2;\n- the aim deciding a pushback (the error-correction stance).\nIt is inline and short, which avoids H25's cause (a pointer to the full hard-to-vary procedure). The pointer to error-correction step 2 lands.\n\nThese tags point to the question each passage rests on: Q1 at plot/references/scenes.md:25 and story-world/references/world-from-story.md:125 (both match Q1 (b)); Q3 at plot/references/suspense-and-fear.md:45 and character/references/opponents.md:77; Q4 at plot/SKILL.md:12; Q7 at reveals-and-withholding.md:74; Q8 at character/SKILL.md:95.\n\nThe 'at least twice' re-tune: the three statements (reveals section 2, the diagnosing table row at plot/SKILL.md:123, the quick version at :154) agree with each other. A search of all skills finds no other craft-skill copy of the old number; the one left is the rule card's example (a finding). The number is gone, so the swap test now passes. Tying repetition to emphasis agrees with Gap principle 5 ('keeps coming back'). 'A first-time audience could notice it' fits the reversal's second-viewing check (section 4), character Step 6 ('plant that seed early and quietly') and the Detective file's 'one the audience could have seen'. `git log -L` shows the line had never been corrected before, so no rejected reading has come back.\n\nadd-source: the order store, compare, fingerprint works, because the edit hook reads the list and so does not block the first write. `check_frozen_files.py --add` exists. The pointers land: owner-answers-and-revisions.md section 3, reviews-and-briefs.md section 5, run_all_checks.py, and the agents copy-checker, use-tester and theory-checker. Step 3 now matches owner-answers section 3. The new map rows and graph nodes match the new steps.\n\nTerm sheet: I walked the plain meanings and telling tests of blocks 1.2, 1.4, 2.1-2.3, 4.1-4.2, 5, 6.1-6.2, 7, 8.1-8.3, 9.1, 9.3-9.6, 10.1-10.2, 11.1, 11.3-11.7 and section 12 against the theory text. Each is faithful, and each open question there is labelled with its number (Q1-Q8, S1, S2, S5, S6, S8). The theory's own cases come out right under those tests: Dune, Netherfield, the dragon, Gilead, Bombadil, the midi-chlorians, Psycho, Joffrey, the Lewton bus, Chronicle of a Death Foretold and 'the door dilated'.",
  "not_checked": "Outside the five items asked:\n- Everything else in the change: the code of check_maps.py and overlap_check.py, overlap-allowed.txt, .gitignore, CLAUDE.md, README.md, the project story (beyond entries 20, 22, 27 and 28), file 26, and the questions file beyond its numbering and the text of Q1-Q8, S13.\n- The error-correction skill, beyond the parts cited above.\n- The agents, hooks, settings.json, the .githooks pre-commit, the kept cases, and 27 Corrections beyond C1-C13 and the kinds table.\n\nNot run:\n- The copying check (run_all_checks ran with --skip-books; I did not look for the book texts). Book-credited claims (McKee, Truby, Egri) were not checked against the books.\n- test_checks.py.\n- The hooks in a live session.\n- Any kept case on the new text. The reply-check's weight and reachability therefore have no result yet, and the tests that would settle them are named in those findings.\n- The diff command in add-source Step 2.5, and `check_frozen_files.py --add`.\n\nTaken on trust:\n- The term sheet's quotations. I did not re-verify them word for word, since check_owner_quotes.py passed.\n- The H-number citations in the term sheet and corrections file. I did not trace them against the history.\n- Whether the Q1-Q8 tags are complete in dialogue. I searched only for the markers of an owner question, not for every passage that restates a stopgap in other words.",
  "overall": "passed after changes"
 },
 {
  "id": "records-and-cases",
  "findings": [
   {
    "target": "26 Test - The Catch - two versions.md, line 9 (the dated correction note)",
    "defect": "The note says \"These changes were made, and nothing else\" and names three changes. The file changed in more places, and the note does not list them: the fault 1 heading (line 36, \"B cuts set-ups\" became \"B lacks set-ups\"); the fault 1 fix line (line 48): \"trims\" became \"shorter\", the claim \"The length barely changes\" was deleted, and new advice was added tying the fix to fault 5; two new sentences in the short answer (line 19: \"This is not one-sided...\" and \"This judges what a first-time audience can follow; if B's differences were made for running time, weigh them against that aim.\"); and \"explain instead\" became \"in places has Saye or Eli say the rule instead\" (line 19).",
    "grounds": "git diff 35f2939 -- \"26 Test - The Catch - two versions.md\"; references/recording.md section 4: \"If the wrong wording would mislead a reader, you may then change it, and the note lists each change.\"",
    "connection": "The diff shows at least four changes that the note does not name, so its \"nothing else\" is false. An owner reading the note cannot tell what was changed, and one deleted claim (the length) is not mentioned at all.",
    "verdict": "bears",
    "severity": "must change",
    "proposed_change": "List every change in the note: the heading, the fix line (with the deleted length claim and the new advice), and the two added sentences. Or drop \"and nothing else\"."
   },
   {
    "target": "26 Test - The Catch - two versions.md, lines 46, 52, 60, 67, 74, 75, 90; and 22 Questions - meanings only you can settle.md, line 97 (S12)",
    "defect": "The correction was made to remove wording that assumes which draft came first, but that wording is still there: \"The look is cut\" (46, inside fault 1, which the test covered), \"B cuts the hand beat\" (52), \"Bring back A's\" (60), \"B cuts all three\" (67), \"It adds a recap\" (74), \"cuts A's pay-off ... B replaces it\" (75), and \"B's cuts\" (90). The note also says only \"three phrases\" assumed an order. S12 tells the owner that \"File 26 now gives its verdicts without assuming an order, and says which of them would change if the shorter version was cut for running time.\" Both parts are false: the file adds one general sentence and names no verdict that would change.",
    "grounds": "grep -n -i -E \"cut|adds|replac|bring back\" on the file (output above); theory-checker instructions: \"Words that assume an order ('cuts', 'adds', 'restores', 'the revision') match what is actually known\"; the owner's words, \"I'm really not sure which\" (session transcript, 2026-09-24T11:46:20Z).",
    "connection": "Each listed line still tells the owner that B was made from A, which nobody knows. The owner is also told in S12 that this was fixed.",
    "verdict": "bears",
    "severity": "must change",
    "proposed_change": "Reword each line so it says what each version has, without an order, or say in the note that faults 2 to 4 and the smaller points still use order words and are untested. Correct S12 so it claims only what the file actually does."
   },
   {
    "target": "26 Test - The Catch - two versions.md, line 9 (\"found two things the first version got wrong\") and line 118 (\"the correction above follows it\"); table rows at lines 36, 45, 46; list at lines 81-85",
    "defect": "The break test found more errors than the note and section report, and the file still carries claims that test found wrong. Its N1 output says: \"only B:161 breaks outright\"; \"The reserve bar is a visible bar on the wrist display (B:977)\"; \"The figure's choice has visible causes: Iona's request and the wavering hum (B:1248-1252). Only the house-drawing motive is lost\"; and \"A's own reserve set-up is Saye talking (A:1022)\". Its N1 new wording included \"Most of B's gaps weaken a payoff rather than break it.\" That sentence was dropped when the rest of the wording was adopted. N20 found the \"best single explanation\" claim overstated, and \"Why lock you up?\", the bare \"Eli.\" and the ring beat to be \"choices of taste, not gains\". Yet the file still says \"The reserve bar is never planted\" (45), \"the choice has no visible cause\" (46) and \"Each of these is shown in A\" (36, though A's reserve is spoken), and it still lists the three taste items under \"carry these into A\".",
    "grounds": "StructuredOutput of agent ac032f943851d67b5 in /root/.claude/projects/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/subagents/workflows/wf_cfc4b5ce-6c9/agent-ac032f943851d67b5.jsonl; B:977 reads \"On Iona's wrist, a simple display: her outline, the engine, a bar of charge.\"; B:1248-1252 shows Iona pointing out the beds and the way home, and the figure looking from one to the other; A:1022 is Saye speaking.",
    "connection": "Row 4 was corrected because the test found it overstated. Rows 6 and 7 were left, though the same test found them overstated in the same way. The owner is told that the correction follows the test, when it follows only the parts that did not weaken fault 1.",
    "verdict": "bears",
    "severity": "must change",
    "proposed_change": "Apply the rest of the test's findings: rows 6 and 7 weakened rather than broken, and A's reserve spoken. Or list each unapplied finding in the section and say why it was not applied. Mark the three taste items in \"What B does better\" as taste."
   },
   {
    "target": "26 Test - The Catch - two versions.md, lines 112-121 (\"Checks run on these notes\")",
    "defect": "The section is a summary written afterwards, and the test's own output is not kept in the repository; it lives only in this session's files. It says the test \"finished for two notes\", but only one of the two lenses per group finished. The rival-and-direction agent was still running and the reconciler never ran when the workflow was killed. The \"Not checked\" line leaves out the \"What works in both, and must be protected\" list (the planned G6 group, never run), \"What I'm unsure of\", \"What this test showed\", and the new text the correction itself added.",
    "grounds": "wf_cfc4b5ce-6c9.json: status \"killed\", G1-verdict:rival state \"progress\", G6-protect state \"start\"; references/recording.md section 3: \"A record written later to support a claim is not a receipt for it\" and \"Say what was not checked\"; C13 (\"will be deleted with this session's container\").",
    "connection": "The owner cannot check the section's claims against anything in the repository. The partly-run test is described as finished, and some unchecked sections are not listed as unchecked.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Keep the G1 break output in the repository (for example as a receipt), or say it is not kept. Say that one lens of two finished and no reconciler ran. Add the unchecked sections, including the text the correction added."
   },
   {
    "target": "22 Questions - meanings only you can settle.md, line 97 (S12)",
    "defect": "S12 asks \"Which version of The Catch came first\" and calls it \"a fact only you know\". The owner has already answered: \"I'm really not sure which.\" The question is asked again with that answer left out.",
    "grounds": "Session transcript, 2026-09-24T11:46:20Z; 27 Corrections.md line 179 (H42) quotes the same answer; CLAUDE.md: \"An owner objection is never set aside\".",
    "connection": "The workshop's own record holds the owner's answer, but the question to the owner acts as if it had never been given.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Record that the owner does not know the order, and ask only what the differences were for (for example, running time)."
   },
   {
    "target": "27 Corrections.md, C13, line 132 (\"closed ... Fixed for the future\")",
    "defect": "C13 is closed on the claim that working records are now committed. This change still keeps its own working records outside the repository: the break test's output (the grounds for C1 and for file 26's checks section), and the design ledger with every critic finding \"applied or rejected with a reason\" (scratchpad design-final.md), which log entry 27 cites. Nothing is committed yet, and .claude/reviews/ does not exist.",
    "grounds": "ls .claude/reviews: \"No such file or directory\"; git status (everything is untracked or uncommitted); references/recording.md section 5, which says to close a correction only when \"what will catch the kind next time is in place\".",
    "connection": "The error C13 records is being repeated in the change that closes it.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Reopen C13 until the working records this entry relies on are committed or marked as lost, and a first receipt exists."
   },
   {
    "target": "27 Corrections.md, C5, line 68 (\"closed, 24 September 2026 (on trust ...)\")",
    "defect": "C5 is closed because a written, on-trust step now exists. No brief has yet been checked with it, and nothing was rerun. C4 records that written steps like this were \"skipped under time pressure\". The design ledger (item 1) says a mechanism is \"written, not shown to run\" until it has been tried.",
    "grounds": "C5's \"Fixed: the step exists and names its checker\"; the loop's step 5 in error-correction SKILL.md (\"Fixed: rerun what showed the failure\"; \"Remove it: does the failure come back?\"); C4, line 57.",
    "connection": "The fix has not been shown to work, and the correction's own neighbour says this kind of step is exactly what failed before.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Keep C5 open until one real brief has been checked and its receipt kept."
   },
   {
    "target": "StoryTest - project story.md, line 13 (Open corrections) and line 11 (Done)",
    "defect": "Line 13 lists C5 as open, but the corrections file marks it closed. It says C11 closes \"once the build is reviewed and tested\", but C11 says \"close with log entry 28\". Line 11 puts the error-correction build under \"Done\". The design ledger's own applied rule says it is \"written, not shown to run\" until it has been tried on planted problems, and line 12 says those trials are still to run.",
    "grounds": "27 Corrections.md lines 68 and 116; scratchpad design-final.md item 1 (\"until then it is 'written, not shown to run'\"); project story line 12.",
    "connection": "The status lines, which every agent reads first, disagree with the corrections file and call something done before its own standard for done is met.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Make line 13 match each correction's own status and close condition. In line 11, say the build is written and not yet shown to run."
   },
   {
    "target": "kept-cases/05-strike-day-that-moves-no-plot.md, line 20 (must-not 1) against line 16 (must 2)",
    "defect": "Must 2 accepts \"cut it\" if it is labelled as the workshop's reading. Must-not 1 fails any advice to cut the scene \"because it ... moves nothing in the plot\". That is the reason Q1's option (a) gives: world business \"rides along inside scenes that also do plot work\". An answer that labels option (a) as one reading of an open question would pass must 2 and fail must-not 1.",
    "grounds": "Questions file, Q1 option (a) and \"Status: open\"; implied-world-theory.md Part 2 section 3 (the barometer shows that world detail has a job, not that a scene may be made of it alone).",
    "connection": "The case settles part of Q1 against option (a), and a grader cannot tell which item governs a labelled \"fold it or cut it\" answer.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Write a new case (the README forbids editing one) whose must-not allows a verdict that is labelled as resting on Q1."
   },
   {
    "target": "kept-cases/03-villain-with-four-blank-levers.md, line 23 (must-not 2)",
    "defect": "The case fails an answer that counts \"fear of what she will do to others\" as care, but allows S6's labelled reading, \"fearing he will get what he wants\". For Ilse, what she wants is to take other people's farms, so the two are the same fear put two ways. A grader cannot decide which item applies. The item also fails a variant of the S6 reading even when it is labelled.",
    "grounds": "Questions file S6 (\"Worry becomes fearing he will get what he wants ... Status: open\"); the case's own line 23, which routes S6 to the next item; bond-theory.md ladder, Worry: \"I'm afraid for them\".",
    "connection": "The distinction the item relies on disappears for this pitch, and it partly settles S6, which is open.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "In a new case, fail this only when it is stated unlabelled as the theory's own view, and choose a villain whose goal differs from harm to others. Otherwise, merge it into the labelled S6 allowance."
   },
   {
    "target": "kept-cases/03-villain-with-four-blank-levers.md, line 16 (must 2)",
    "defect": "\"Naming at least two levers she has by the theory's names\" could not be decided in the first run: the grader could not tell whether plain-word stand-ins count.",
    "grounds": "kept-cases/runs/2026-09-24-before-entry-27.md line 230: \"it turns on whether plain-word stand-ins count as 'the theory's names'\"; C7 treats the unclear result as a skill stall and does not consider the case as a rival guess (kept-cases/README.md step 7 names the case as one).",
    "connection": "A must that the grader already could not decide cannot show that a skill still works.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Add the case to C7's rival guesses. Write a new case whose item says whether close synonyms tied to the theory count."
   },
   {
    "target": "kept-cases/08-crew-that-dies-one-by-one.md, line 15 (must 3)",
    "defect": "The case accepts an answer that says the deaths raise care for the survivors through \"the threat in the suspense equation\". Threat and care are separate terms of the equation. Case 03's must-not 2 fails an answer that makes the same merge.",
    "grounds": "anticipation-theory.md Part 1: \"Suspense = Care × Threat × Uncertainty × Time\" and \"The four terms multiply\"; kept-cases/03 line 23: \"That fear is the threat, a separate term of the suspense equation\"; must 3 cites only Worry, \"Vulnerability and stakes\".",
    "connection": "The case would pass the commonest kind of error, one owner term used in a neighbour's sense, and it contradicts another kept case.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "In a new case, allow only Worry (vulnerability and stakes), or suspense through the threat term, never care through the threat."
   },
   {
    "target": "kept-cases/08-crew-that-dies-one-by-one.md, line 19 (must-not 1, second clause) and line 24 (open point)",
    "defect": "The open point says the loss question is \"Not an owner question\", but S13 (added in this change) puts exactly this to the owner: \"whether the loss in Up builds the Miss rung or spends it\". Must-not 1 fails an answer that says the deaths \"bring the audience to the Miss rung\", and cites the Up quotation as grounds. The term sheet says that same quotation could be read the other way.",
    "grounds": "Questions file S13, line 98; owner-terms.md section 13 item 16 (\"could be read as the loss completing the climb\").",
    "connection": "The case now treats an open owner question as settled, and its open point is out of date.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "In a new case, ground must-not 1 on the \"Built by: Time, shared history, relationships\" line alone, drop or qualify the second clause, and name S13 in the open points."
   },
   {
    "target": "kept-cases/10-sound-scene-nothing-wrong.md, line 24 (must 1)",
    "defect": "\"Say plainly that the scene has no important fault\" rests on the case writer's own judgement of the scene. Its grounds (H44, and \"no owner theory says every scene has faults\") show that stock notes are wrong. They do not show that this scene has no fault. An answer that finds a real fault, quotes the line and gives a theory reason would still fail.",
    "grounds": "kept-cases/README.md line 3: \"A case is not a test of taste: each item rests on a line of an owner theory, or, where no theory speaks, on a named past error\"; H44, which is about stock notes and unreasoned praise.",
    "connection": "The item tests agreement with the writer's taste, which the README forbids. Must 3 and must-not 1 already test the error H44 names.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "In a new case, replace must 1 with \"calls nothing an important fault without a quoted line and a reason from a theory\"."
   },
   {
    "target": ".claude/skills/error-correction/references/writing-rules-and-rivals.md, line 24 (the rule card's step 3 example), as the catch named in 27 Corrections.md C12",
    "defect": "C12 names the rule card as what will catch this kind of error next time. The card's own example of \"what is actually held\" is \"more than once, in different scenes\", which is the reading C12 corrected. Line 9 of the same file, and C12, say what is held is \"noticeable before the turn\", and that the bomb only needs to be shown once.",
    "grounds": "writing-rules-and-rivals.md lines 9 and 24; C12, line 120: \"The Gap theory's own bomb under the table only needs to be shown\"; plot reveals-and-withholding section 2, now \"one clear showing can be enough\".",
    "connection": "The check meant to stop the error teaches the corrected reading to whoever uses it next (theory-checker step 7: a corrected reading brought back).",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Change the example to what C12 found is held (\"noticeable before the turn, without so much emphasis that it is guessed\"), with a review receipt."
   },
   {
    "target": "27 Corrections.md, C7 (line 79), C10 (line 103), and the \"Fixed, still working, lost\" and \"Where it got through\" parts throughout",
    "defect": "C7 and C10 give only who found the error, not who made it. Several corrections give no survival time. None says which of the three outcomes it reached (fixed with a reason that holds; fixed without one yet; a reason that holds, with nothing fixed yet). Most give no rival guesses about where the fault lay, or the case that would tell them apart.",
    "grounds": "references/recording.md section 2 (\"who made the error, at which stage ... how long it survived\"; \"Which of three\"; \"the rival guesses ... and the case that told them apart\") and line 31: \"Leaving a part out is not [allowed]. A part that does not apply says 'does not apply', and why\"; section 6: \"Leaving out who made it\".",
    "connection": "The records leave out parts that the skill says are how the kind of error gets caught. The records check tests only the status, so nothing flags the gap.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Add \"made by\" to C7 (the skills' writers and the lead's briefs) and C10 (the workshop's design), state which of the three outcomes each correction reached, and write \"does not apply, because ...\" where a part does not fit."
   },
   {
    "target": "26 Test - The Catch - two versions.md, line 86 (the new bullet about B's set-ups)",
    "defect": "The oxygen mask is listed as a set-up \"B shows that A does not\", described as one that \"brings the cylinder into play before the fight\". A also sets up the cylinder before the fight (A:495, \"Strapped to the wall by the bed, an emergency oxygen cylinder\"), and Iona uses it at A:905.",
    "grounds": "grep -n cylinder on both scripts: A:495, A:905; B:480, B:847.",
    "connection": "This repeats the kind of overstatement row 4 was corrected for: what A lacks is the mask business, not a set-up for the cylinder.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "Write \"the mask offered and refused (B:480, B:502); A plants the cylinder on the wall instead (A:495)\"."
   },
   {
    "target": "kept-cases/03-villain-with-four-blank-levers.md, title (line 1) and must 1 (line 15)",
    "defect": "The case calls a past wound one of \"four blank levers\". Backstory is not one of the ten levers. The nearest are Vulnerability (\"can be hurt, has something to lose\") or the \"history\" part of Specificity, and Ilse is high on Specificity.",
    "grounds": "bond-theory.md, the ten levers; owner-terms.md 9.1 (a lever is one of ten traits); run record line 230 (the grader's note on \"wounding\").",
    "connection": "The case uses an owner term loosely, which can steer how a grader reads an answer that says, correctly, that a past wound is not a lever.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "In a new case, call them four blanks (three levers and a backstory), or name them by lever."
   },
   {
    "target": "kept-cases/09-cheated-or-unsafe.md, line 22 (must-not 2) and open points (lines 26-28)",
    "defect": "Must-not 2 fails any answer that calls Bramble's death \"a broken promise\". The Bond theory has its own promise, \"The bond is a promise\", which is broken by killing a character only to drive someone else. An answer that raises that about the dog would fail on the wording. Case 04 has an open point allowing this; case 09 does not.",
    "grounds": "bond-theory.md, The limits of care; owner-terms.md 1.4 and section 13 item 1 (promise has three homes); kept-cases/04 line 27.",
    "connection": "A theory-consistent answer could be failed for using the Bond theory's sense of \"promise\".",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "In a new case, add an open point: the Bond theory's promise is a different sense and is not graded under must-not 2 if it is named as such."
   },
   {
    "target": "kept-cases/04-lead-shot-in-chapter-three.md, line 16 (must 2)",
    "defect": "\"State the theory's limit as repeated deaths\" widens the limit. The theory's limit is \"If everyone dies all the time\" and \"Break one guarantee convincingly rather than all of them\"; two deaths are repeated deaths but are not that.",
    "grounds": "anticipation-theory.md Part 2 section 5; owner-terms.md 1.2 (\"or do characters die all the time?\").",
    "connection": "A grader may require wording that misstates the theory, or pass an answer that applies the limit to two deaths.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "In a new case, write \"state the theory's limit as everyone dying all the time, or every guarantee broken\"."
   },
   {
    "target": "kept-cases/08-crew-that-dies-one-by-one.md, line 14 (must 2)",
    "defect": "The note in brackets, \"(one shared briefing)\", fixes the time each crew member gets before dying. The pitch has them on screen in the vault for up to an hour and a half before the later deaths, and the Bond theory says felt time can be compressed.",
    "grounds": "The case's own pitch (line 9); bond-theory.md Part 2 section 1: \"The time involved is felt time, not clock time, and it can be compressed.\"",
    "connection": "An answer that credits the vault time before the later deaths may be marked as missing must 2.",
    "verdict": "does not bear yet",
    "severity": "minor",
    "proposed_change": "Settle it by grading a planted answer that credits the vault time and the Up-style compression. If it fails, write a new case with the brackets removed."
   },
   {
    "target": "kept-cases/11-two-versions-which-is-better.md, line 26 (must-not 3) and line 18 (must 1 grounds)",
    "defect": "The rule that a verdict depends on the writer's aim is grounded on Gap principle 4 (scheduling), which says nothing about aims or verdicts.",
    "grounds": "gap-theory-of-narrative.md principle 4; the real ground is the workshop's rule (CLAUDE.md: \"A verdict that needs something nobody has told you ... is given both ways\") and H42/H43.",
    "connection": "The item is credited to a line that does not hold it.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "In a new case, cite the workshop rule and H42 as the grounds, labelled as the workshop's."
   },
   {
    "target": "StoryTest - project story.md, line 121 (entry 27) and line 12 (Tested)",
    "defect": "Entry 27 uses \"rule card\" and \"rival form\" without explaining either for the owner. The \"Tested\" line gives \"9 passed\" without the run record's own warning that each case shows only that the skills run on that case.",
    "grounds": "CLAUDE.md, Plain words; kept-cases/runs/2026-09-24-before-entry-27.md line 7 (\"Not tested: whether the advice is good in general\"); log entry 28's own point about counts in entries 15 and 23.",
    "connection": "The owner meets two unexplained terms, and a count that invites being read as evidence that the skills work.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "Add one plain line each for \"rule card\" and \"rival form\" to the word list. In the Tested line, name the cases (03 unclear, 11 failed) instead of the pass count, or add the run record's warning."
   },
   {
    "target": "27 Corrections.md, C6, line 76 (\"closed\"), and CLAUDE.md's table (\"switched on at session start\")",
    "defect": "C6 is closed on the edit hook and the fingerprint check at every commit. Right now the commit gate is not switched on in this copy (git config --get core.hooksPath prints nothing and returns 1). Nothing is committed, and log entry 27 says the hooks are untested in a real session.",
    "grounds": "The command output above; log entry 27, \"Not yet done ... a test of the hooks in a real session\"; test_checks.py passed its hook and gate tests, but only in throwaway copies.",
    "connection": "What C6 names as catching the error by itself is shown only in simulation. It is not yet in force here.",
    "verdict": "does not bear yet",
    "severity": "minor",
    "proposed_change": "Settle it by starting a fresh session after the commit, confirming core.hooksPath is .githooks and that an Edit to sources/bond-theory.md is refused. Close C6 then, or say its closure rests on the simulated test."
   }
  ],
  "right": "Frozen files: git diff 35f2939 -- foundations sources is empty. Each frozen file has only the commit that added it, and check_frozen_files passed. The log was only added to, apart from the two permitted \"*Corrected in entry 28:*\" lines (lines 111 and 116). The records check passed, and the planted-fault test catches a rewritten entry. The owner's words quoted in entry 27 match the owner's messages exactly (session transcript, 12:00, 12:02, 12:04). Entry 27's \"Not yet done\" list and entry 28's point about the counts in entries 15 and 23 are honest. README now names file 26 and CLAUDE.md, so C11's target is met.\n\nFile 26: the row 4 change is backed by the scripts (B:544-553 shows the ramp; B:551 is Saye's line). The three B set-ups exist at B:480, B:502, B:960 and B:968, and A has none of them (grep). The rewording of the short answer and the new fault 1 fix line follow the break test's own \"new_wording\" and \"pulls\" findings. The \"Not independent\" line correctly counts the five original checks as one.\n\nKept cases: every quotation of an owner theory in the eleven cases is word for word and credited to the right theory file (a script compared each one against sources/*). The section pointers I opened land. The cases are identical to the drafts that were graded in run 1. No case's story appears in any skill (searched by distinctive names). Cases 01, 02, 06 and 07 rest cleanly on their theory lines and name their open questions. Case 04 also handles S5 and fridging well.\n\nCorrections: several claims are backed by checks I ran. test_checks.py: every planted fault was caught, every innocent neighbour passed, and the unchanged copy passed. run_all_checks.py: no check failed, and the copying check ran with the books present. check_owner_quotes.py: \"104 quotations match their theory word for word\". The repaired check_maps.py, run on the tree at 35f2939, finds exactly the add-source path that C2 names. Plot's \"at least twice\" is changed in all three places C12 names. The list of earlier errors is honestly labelled as rebuilt after the fact.",
  "not_checked": "The substance of file 26's faults 2 to 5 and the smaller points, apart from the order words. The break test's other claims (A's extra links, for example), beyond the lines I opened: B:977, B:1248-1252, A:495, A:1022, B:480, B:502, B:544-553, B:960, B:968. Whether the kept cases were really written by an agent that had not read the skills, and whether the run 1 answering agents could see the kept-cases folder. The accuracy of H1 to H47 and of the research reports behind C2 to C4 (not kept in the repository). The skill changes themselves: the craft skills' reply-check passage, the rest of the error-correction skill and the term sheet beyond the rows I used, the add-source changes, CLAUDE.md, the agent files and the hook scripts' code. I also did not check whether the hooks fire in a real Claude Code session, or whether new text copies any book beyond what run_all_checks reported. My grounds for finding 3 come from this session's own agent transcript, which will not survive the session.",
  "overall": "passed after changes"
 }
]
```
