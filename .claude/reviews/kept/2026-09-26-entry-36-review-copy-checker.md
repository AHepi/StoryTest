*Kept for log entry 36 by the briefing session. Word for word as the agent wrote it, except that every run of eight or more words shared with a book or with the paper was replaced by a marker, "[quotation removed: N words of SOURCE]", so that no source text is committed (CLAUDE.md, copyright rule). The removal script and its run are recorded in entry 36's receipt.*

# Copy-checker report: the stages of log entry 36

Reviewer: copy-checker (`.claude/agents/copy-checker.md`), an independent agent that wrote none of this change. Read-only: nothing in `/home/user/StoryTest-icm` or `/home/user/StoryTest` was edited, staged, committed or deleted. The only file written is this report, plus one throwaway script in the same scratch folder (`near_runs.py`, described below).

Target: branch `claude/icm-story-workspace`, commit `915aa52` plus the 37 staged files. Covered by eye: the brief's items 1 to 3 first, then all nine `stages/*/references/*.md`, `stages/how-stages-work.md` and `CONTEXT.md`. Compared against `sources/raw/mckee-dialogue.txt`, `truby-anatomy-of-story.txt`, `truby-anatomy-of-genres.txt` and `paper-icm-2603.16021.txt`.

## What was run

- **Book text present:** `ls sources/raw/*.txt` lists all four texts.
- **`overlap_check.py`, 8 words,** on `stages`, `_config` and `CONTEXT.md` against each of the four sources: 0 problem spans each (exit 0).
- **Same at 6 words:** 0 against McKee, *Genres* and the paper. One span against *The Anatomy of Story*: `plot-worksheet.md`, "the hero and the main opponent" (finding 27).
- **Same at 5 words, as an aid only:** the hits were mostly common phrases. One is a McKee aphorism (finding 19).
- **A one-word-swap scan** (my own throwaway script, `near_runs.py`, run in the scratch folder): 7-word and 6-word runs that match a source with any one word changed. It found:
  - "only the parts of a program that changed" against the paper's "…of the program…" (finding 32);
  - "editing the output mends this run" (finding 8);
  - a few ordinary phrases.
- **The other changed files at 8 words** (`CLAUDE.md`, `README.md`, project story, 22 Questions, `sources/README.md`): 0 problem spans. **At 6 words:** entry 36 holds a 7-word run from the paper's abstract (finding 38), plus spans that are allowed or ordinary.
- **By eye:** for each passage drawn from a book, I found the book's passage on the same idea by searching its key terms, and read the two side by side.

**What the verdicts mean:**
- **bears:** the passage should be rewritten or cut to a pointer before commit.
- **bears (minor):** the same, but a small fix will do.
- **does not bear yet:** there is a real likeness, but it is slight. A light reword is advised, not required.
- **does not bear:** I checked it and the likeness is only in ideas or in ordinary wording.

## Answers to the brief's items 1 to 3

1. **Lists in the author's order: the wording is not far enough from the books.**
   - **Moral line** (cast sheet, section 2) and **chain under each beat** (drafting-scenes, section 2): each step's gloss paraphrases the author's own gloss, not just his order. Cut both to pointers. The author's step names are term names of four words or fewer, so they may stay. Keep what the workshop adds: the care plan in the first; which stage writes which link in the second.
   - **Premise worksheet:** the section 3 card is mostly pointers and passes. Sections 4 and 7 do not pass:
     - Section 4 is a close paraphrase of Truby's premise step 8.
     - Section 7 is his seven-steps exercise item by item, in his order, with his numbers. The brief calls these sections "reordered and merged", but section 7 is not reordered, and the file's own sections follow his premise chapter's step order (finding 13).
2. **McKee's questions** (dialogue-passes, section 2) are the clearest copying in the change. The "four groups in the workshop's order" follow his "Key Questions" list in his own order: the fourth group is exactly his "final step" group. Several questions differ from his only in the pronoun. Cut to a pointer.
3. **The paper's phrasing.** Most of `how-stages-work.md` and all of `CONTEXT.md` use the paper's ideas in the workshop's own words, with attribution, and pass. Four places keep the paper's expression and need a reword:
   - the edit-source line in section 8 (finding 8);
   - the layer-question column in section 1 (finding 30);
   - the "parts of a program that changed" sentence in section 7 (finding 32);
   - entry 36's "one agent, reading the right files" (finding 38).

## Findings

Ranked, the most serious first.

1. **Target:** `stages/07-dialogue/references/dialogue-passes.md`, lines 19-23 (section 2).
   - **Defect:** a list in the author's order and close to his wording. The text says "Grouped in the workshop's order", but the four groups follow McKee's list in his sequence:
     - background desires, object of desire, scene intention, motivation;
     - scene driver, antagonism, values, turning point;
     - subtext, beats, action or reaction, progression;
     - his "final step" group (text, exposition, characterization), unchanged.
   - Some questions differ from his only in the pronoun: "what they would say to get what they want", "whether it is an action or a reaction", "too early or too late", "what they cannot yet do or say", "what they tell themselves they want". The places resistance comes from are his three examples in his order. Line 19 also keeps his instructions to ask three times, and from every character's side.
   - **Grounds:** `mckee-dialogue.txt`, lines 2492-2516, chapter 19, "Key Questions": "Is it an action or a reaction?"
   - **Connection:** about 15 of his roughly 20 questions, in his order, reworded mainly by changing "he" to "they". That pronoun change is why the 6-word and 8-word runs miss it.
   - **Verdict:** bears.
   - **Fix:** a pointer to his "Key Questions". Keep the workshop's own parts: one pass with the driver in a small scene, how much to do (the dialogue skill's step 7), and the note of questions that changed a scene. If a checklist is wanted, write the workshop's own questions keyed to the scene card fields (`scenes.md`, section 2), in the card's order.

2. **Target:** `stages/06-scenes/references/drafting-scenes.md`, lines 19-26 (section 2).
   - **Defect:** a list in the author's order, where each item paraphrases his definition of that step:
     - item 1 is his "scene intention" (what the character wants right now, as a step toward the larger want; granting it ends the scene);
     - item 2: "rightly or wrongly" is his "realistic or mistaken";
     - item 4: "physical or spoken" is his "physical or verbal";
     - item 5: "if the act needs any" is his "[quotation removed: 9 words of mckee-dialogue]".
   - The lead-in keeps his slow-motion and chain images, and line 26 keeps "an earlier link".
   - **Grounds:** `mckee-dialogue.txt`, lines 1428-1437, chapter 12, "Five Steps of Behavior": "these five steps in slow-motion detail". Also lines 1384-1386, "Scene Intention".
   - **Connection:** the order is his idea, as the brief says, but the glosses are his too.
   - **Verdict:** bears.
   - **Fix:** keep his five step names, which are term names and allowed ([quotation removed: 8 words of mckee-dialogue], expression), with a pointer. Then say only the workshop's use: which links this stage writes, which stage 07 writes, and the scene-card field each one fills.

3. **Target:** `stages/02-characters/references/cast-sheet-and-moral-line.md`, lines 31-40 (section 2).
   - **Defect:** a list in the author's order, with some of his wording. Steps 1 to 8 follow his "Basic Strategy" items in sequence:
     - values and moral weakness;
     - first immoral action;
     - immoral actions, with criticism, the ally's attack and justification;
     - obsessive drive ("win at almost any price", his "do almost anything to succeed");
     - worse actions, more criticism, more justification;
     - battle;
     - final action against the opponent (his "moral or immoral" becomes "right or wrong");
     - self-revelation and a decision "between two courses".
   - **Grounds:** `truby-anatomy-of-story.txt`, lines 1150-1163, "Moral Argument: Basic Strategy": "[quotation removed: 8 words of truby-anatomy-of-story]".
   - **Connection:** his 15 items merged into 8, with none reordered.
   - **Verdict:** bears.
   - **Fix:** a pointer to his basic strategy. Keep what the workshop adds (lines 42-46): the care plan beside each moral step (which rung, which lever pays, principle 4), and "the story's question need not be moral". If the sheet needs steps, make them columns of the care plan: act, who objects, rung, lever.

4. **Target:** `stages/01-brief-and-premise/references/premise-worksheet.md`, lines 73-80 (section 7).
   - **Defect:** follows the book's exercise item by item, in its order and with its numbers:
     - events in one sentence each, at least five, ten or more better;
     - a rough order that will change;
     - start from the self-revelation, then the need and the desire;
     - both kinds of weakness, one hurting only the hero and one hurting others, several of each;
     - the problem growing out of the weakness;
     - an opponent after the same goal who is good at attacking the weakness.
   - **Grounds:** `truby-anatomy-of-story.txt`, lines 485-506, the seven-steps writing exercise: "[quotation removed: 9 words of truby-anatomy-of-story]".
   - **Connection:** six items in sequence. Some glosses track his closely: "a knack for striking the hero's weakness" is his "[quotation removed: 8 words of truby-anatomy-of-story]". The section is not reordered.
   - **Verdict:** bears.
   - **Fix:** point to `structure-and-conflict.md`, section 2, and the plot skill's Building steps. Keep only the workshop's additions: events as the Gap theory's story, the start from the settlement when the hero does not change, and the detail left to stage 02.

5. **Target:** `premise-worksheet.md`, lines 53-61 (section 4).
   - **Defect:** a close paraphrase of one passage, point by point in its order:
     - the one basic action;
     - the action best able to force the hero to face their weaknesses;
     - the start and the end as opposites of that action;
     - several options;
     - the warning that a start like the action only deepens it.
   - **Grounds:** `truby-anatomy-of-story.txt`, lines 259-298, premise step 8, character change: "the one action best able to force".
   - **Connection:**
     - "the action most likely to force them to face what is wrong with them" tracks "[quotation removed: 11 words of truby-anatomy-of-story]";
     - "who they are at the start / at the end" tracks "who your hero is at the beginning … who he is at the end";
     - "only confirms who the hero is" tracks "remain who he is".
   - The invented lighthouse case (line 59) and "How it stands" (line 63) are the workshop's own and pass.
   - **Verdict:** bears.
   - **Fix:** one sentence with a pointer (his W, A and C are term letters and may stay). Keep the invented case and the check in the workshop's words. Drop the four-step gloss.

6. **Target:** `stages/08-critique/references/critique-rounds.md`, lines 37-42 (section 4).
   - **Defect:** the book's items in its order, each closely paraphrased:
     - an ending reveal that sends the audience back;
     - a surprising change in an opponent or a minor character;
     - background details that come forward on a later viewing;
     - texture in character, moral argument, symbol and world that gains once the twist and the hero's change are known (his own example list, kept);
     - the storyteller's changed relation to the others.
   - Line 49 then uses his last item.
   - **Grounds:** `truby-anatomy-of-story.txt`, lines 3702-3716, his closing chapter on the never-ending story: "details in the background … move to the foreground".
   - **Connection:** five of his six techniques, as five questions in his order. "Details in the background that move to the front" is almost his wording. The brief does not flag this passage.
   - **Verdict:** bears.
   - **Fix:** keep the lens idea in one line and the Gap theory link (line 44), point to his closing chapter, and ask the critic's questions from the Gap theory's reading backwards, not from his list.

7. **Target:** `stages/03-world-and-symbols/references/world-and-symbols-worksheet.md`, line 26 (section 2).
   - **Defect:** follows McKee sentence by sentence and retells his example:
     - a shared history and shared beliefs let much go unsaid;
     - a few words carry the rest;
     - mixed backgrounds make people explain;
     - so the culture decides how much is text and how much subtext;
     - "close-knit" is his word;
     - then the crime-family man who says a phrase the family understand and explains it to the outsider he loves. This is his *Godfather* example with the names taken out.
   - **Grounds:** `mckee-dialogue.txt`, lines 1390-1396, chapter 12, "Background Desires" (high-context and low-context cultures): "[quotation removed: 9 words of mckee-dialogue]".
   - **Connection:** his order, his contrast and his example.
   - **Verdict:** bears.
   - **Fix:** one sentence naming the idea, with a pointer ("high-context" and "low-context" are term names). Drop the retold example or invent one. Keep lines 28 and 30, which are the workshop's own. `dialogue-passes.md`, line 29 repeats "close-knit … shorthand … outsiders": reword it in the same edit.

8. **Target:** `stages/how-stages-work.md`, lines 81-86 (section 8).
   - **Defect:** keeps the paper's expression in runs of fewer than 8 words, and its argument order:
     - line 82, "Editing the output mends this run; changing the source mends every later run", is the paper's two-sentence line with three words swapped;
     - line 81 keeps "a turn of phrase" (the paper's example of an edit that belongs in the output) and "a touch", from its "human touch";
     - line 82's first example, "always cutting the opening", is the paper's own example;
     - line 86, "the same kind of edit … in the same stage in three different runs", tracks "[quotation removed: 12 words of paper-icm-2603.16021]".
   - **Grounds:** `paper-icm-2603.16021.txt`, lines 906-926, section 6.3, the edit-source principle: "Editing the output fixes this run."
   - **Connection:** the one-word-swap scan found "editing the output mends this run". The idea is registered for use; this wording is the paper's.
   - **Verdict:** bears for line 82's sentence. Does not bear yet for lines 81 and 86 (short, attributed, ordinary examples).
   - **Fix:** say it in the workshop's terms, for example: an edit to an output helps this project only, and a change to the contract or reference helps every project after it. Replace "a turn of phrase" and "cutting the opening" with examples of the workshop's own.

9. **Target:** `stages/04-plot/references/plot-worksheet.md`, lines 32 and 34 (section 3).
   - **Defect:** follows the book's paragraph point by point and keeps its distinctive pairing:
     - tactics as the right response in the moment, strategy as the right sequence toward the whole goal;
     - heroes good at the first and not the second;
     - "win each fight and lose the war";
     - "acting efficiently rather than effectively", his "acting efficiently at the cost of acting effectively";
     - at line 34, "sequence of actions" and "campaign" are his words.
   - **Grounds:** `truby-anatomy-of-genres.txt`, lines 749-761, the Action chapter, "Strategy vs. Tactics": "known as acting efficiently".
   - **Connection:** "tactics" and "strategy" are term names and allowed. The efficient/effective pairing and the battle-and-war framing are his expression. The questions at lines 35-39 are the workshop's own and pass.
   - **Verdict:** bears.
   - **Fix:** define the two levels in the workshop's own words ("campaign" and "moves", already used at line 34, would do). Drop the efficient/effective pairing and the fight-and-war clause.

10. **Target:** `premise-worksheet.md`, lines 11-15 (section 1).
    - **Defect:** his example lists in his order, and his three instructions squeezed into one phrase:
      - "characters, twists, lines … kinds of story, subjects, periods" is his wish-list examples (characters, plot twists, lines of dialogue, themes, genres);
      - "unsorted, nothing ruled out for cost" is his "don't organize", "don't reject anything" and his cost example;
      - "Lay the two side by side and mark what turns up on both" tracks "lay them out … repeat themselves on both lists", followed by his list of what repeats.
    - **Grounds:** `truby-anatomy-of-story.txt`, lines 130-134, premise step 1: "Banish thoughts like 'That would cost too much money.'"
    - **Verdict:** bears (minor).
    - **Fix:** name his two lists ("wish list" and "premise list" are term names) with a pointer, and drop the example lists and the cost detail. Line 17 is the workshop's own and passes.

11. **Target:** `premise-worksheet.md`, line 34.
    - **Defect:** his two techniques in his order, the first closely glossed: "what must happen if that promise is kept" is his "[quotation removed: 8 words of truby-anatomy-of-story]". Then "what if", asked repeatedly.
    - **Grounds:** `truby-anatomy-of-story.txt`, lines 137-142, premise step 2: "[quotation removed: 8 words of truby-anatomy-of-story]".
    - **Verdict:** does not bear yet. Two ordinary ideas, attributed; a light reword of the promise gloss is enough.

12. **Target:** `premise-worksheet.md`, line 71.
    - **Defect:** keeps his image: "beyond the writer and their family" is his "you and your immediate family".
    - **Grounds:** `truby-anatomy-of-story.txt`, lines 307-309, premise step 10.
    - **Verdict:** does not bear yet. "Beyond the writer's own circle" would settle it.

13. **Target:** `premise-worksheet.md` as a whole (sections 1 and 3 to 7, and the card at lines 38-49).
    - **Defect:** the section order is Truby's premise chapter step order:
      - step 1: the two lists;
      - step 2: possibilities;
      - steps 7 and 8: basic action and change;
      - step 9: the moral choice;
      - step 10: audience appeal;
      - then his next chapter's exercise.
    - The card keeps his exercise's order, apart from moving "problems" down.
    - **Grounds:** `truby-anatomy-of-story.txt`, lines 312-323, the premise writing exercise.
    - **Connection:** the brief's "reordered and merged" overstates the difference.
    - **Verdict:** does not bear yet on its own: the headings are ordinary craft terms and the card is mostly pointers. It resolves once findings 4, 5 and 10 are fixed.

14. **Target:** `premise-worksheet.md`, line 67 (section 5).
    - Paraphrases his step 9 at the level of the idea, in the workshop's own "A over B" form.
    - **Verdict:** does not bear.

15. **Target:** `cast-sheet-and-moral-line.md`, lines 11-24 (the section 1 table).
    - **Defect:** the first seven columns are the measures of his character comparison, nearly in his order: weaknesses, need, desire, values, power, and each one's answer to the moral problem. In the glosses:
      - the Job column keeps his example list in order ("hero, main opponent, ally", with his fake ally reworded);
      - Power keeps "status" (and ability becomes "skill");
      - Want keeps his question of when the audience knows the goal is won or lost.
    - **Grounds:** `truby-anatomy-of-story.txt`, lines 945-962, character writing exercise 3: "Power, status, and ability".
    - **Verdict:** bears (minor).
    - **Fix:** put the columns in the workshop's own order (its answer and its levers first, say) and drop the glosses that track his. The Levers and Never-says columns are the workshop's own.

16. **Target:** `cast-sheet-and-moral-line.md`, lines 50-52 (section 3, steps 1 to 3).
    - **Defect:** three items of the same exercise, in his order:
      - start with the hero and the main opponent;
      - the self-revelation first, then the need;
      - each opponent attacks the weakness in a different way.
    - **Grounds:** the same exercise, lines 954-962: "[quotation removed: 10 words of truby-anatomy-of-story]".
    - **Verdict:** does not bear yet. Attributed and mostly pointers; small once finding 15 is fixed.

17. **Target:** `cast-sheet-and-moral-line.md`, line 27.
    - **Defect:** follows three sentences of McKee in order, with his wording:
      - the want against the inner "hunger" (his "emotional hunger");
      - "tell themselves they want" (his "tell himself he wants");
      - the hunger is generic, while the object makes the story original;
      - would getting the object satisfy the need?
    - **Grounds:** `mckee-dialogue.txt`, lines 1379-1382, chapter 12, "The Complex of Desire": "[quotation removed: 8 words of mckee-dialogue]".
    - **Verdict:** bears (minor).
    - **Fix:** use his term names ("object of desire" and "super-intention" are allowed) with a pointer. Keep the workshop's check (a want that could move to another story unchanged is not yet a want) without "hunger".

18. **Target:** `drafting-scenes.md`, line 11 (section 1).
    - **Defect:** two close paraphrases:
      - "letting what the characters do tell the story" is Truby's "Let the characters' actions tell the story";
      - "talk is the final layer of a scene, and until the writer knows what each person wants and does, they cannot know how that person would speak" joins McKee's "talk is the final result" to his "[quotation removed: 9 words of mckee-dialogue] … until".
    - **Grounds:** `truby-anatomy-of-story.txt`, line 3687, "Scenes Without Dialogue"; `mckee-dialogue.txt`, lines 1436 and 1460.
    - **Verdict:** bears (minor).
    - **Fix:** say the order in the workshop's own words (action first, talk after), with both attributions and without the glosses.

19. **Target:** `drafting-scenes.md`, line 26.
    - **Defect:** a five-word McKee aphorism, word for word and with no quotation marks: "dialogue problems are story problems".
    - **Grounds:** `mckee-dialogue.txt`, lines 444 and 1104 (chapter 9, "Design Flaws"): "Dialogue problems are story problems."
    - **Verdict:** bears (minor).
    - **Fix:** put it in quotation marks as a short attributed quotation, or reword it.

20. **Target:** `drafting-scenes.md`, line 28.
    - "The value at stake in each scene, and its charge at the start and at the end" is his "Scene value(s)" question.
    - **Grounds:** `mckee-dialogue.txt`, line 2504.
    - **Verdict:** does not bear yet. One attributed idea, in his standard terms.

21. **Target:** `dialogue-passes.md`, lines 11-15 (section 1), and the sources line (line 3).
    - **Defect:** Truby's dialogue exercise items in his order, with his glosses:
      - "What they are doing" is his story dialogue, "about what the characters are doing";
      - "What they believe" and "argue what is right" are his moral dialogue ("right or wrong", "what the characters believe");
      - "words, lines and sounds" is his "words, phrases, tagline, and sounds";
      - "Voices" is his "Unique Voices".
    - **Grounds:** `truby-anatomy-of-story.txt`, lines 3687-3693: "Rewrite each scene using only story dialogue".
    - **Verdict:** bears (minor).
    - **Fix:** his three track names are term names and allowed, and the pass order can stay with a pointer to `line-and-scene-design.md`, section 6. Change the headings "What they are doing" and "What they believe", and "words, lines and sounds", to the workshop's own. The item bodies, tied to stages 02, 03 and 06, are mostly the workshop's already.

22. **Target:** `stages/05-scene-weave/references/scene-weave-worksheet.md`, line 22.
    - **Defect:** a close paraphrase following one sentence:
      - "three to five" strands;
      - "no strand has room for the long list of steps, but each must still get the seven core jobs done" is his "you can't cover the twenty-two steps … but each must cover the seven";
      - "or it reads as filler" is his "the audience will find it unnecessary".
    - **Grounds:** `truby-anatomy-of-story.txt`, lines 3122-3124, the television multistrand plot: "[quotation removed: 9 words of truby-anatomy-of-story]".
    - **Verdict:** bears (minor).
    - **Fix:** the line says the rule is already in `scenes.md`, section 7, so cut it to that pointer.

23. **Target:** `scene-weave-worksheet.md`, line 13.
    - **Defect:** his steps for reworking a scene list, in his order: reorder the large blocks, then neighbouring scenes; merge; cut, then add where there is a gap; and "not by the clock", his "structure, not chronology".
    - **Grounds:** `truby-anatomy-of-story.txt`, lines 3049-3052: "Order the scenes by structure, not chronology."
    - **Verdict:** bears (minor).
    - **Fix:** the line already points to `scenes.md`, section 6; keep only the pointer.

24. **Target:** `scene-weave-worksheet.md`, line 11.
    - "One line naming its single core action" is his "describe each scene in one line … single essential action".
    - **Grounds:** `truby-anatomy-of-story.txt`, lines 3038-3041.
    - **Verdict:** does not bear yet.

25. **Target:** `scene-weave-worksheet.md`, line 25.
    - "keeps putting its people to moral decisions" is his "constantly challenged by moral decisions". It is attributed, in the workshop's own wording, and does not copy his list of shows.
    - **Grounds:** `truby-anatomy-of-genres.txt`, line 583.
    - **Verdict:** does not bear.

26. **Target:** `plot-worksheet.md`, lines 11 and 15.
    - **Defect:** the first two items of his plot exercise, in order: the plot must track the designing principle and the theme ("tracks" kept), and a story symbol the plot should express ("enact"). Line 15, "list the reveals on their own", is his "List the reveals separately".
    - **Grounds:** `truby-anatomy-of-story.txt`, lines 2943-2947, plot writing exercise 7: "[quotation removed: 8 words of truby-anatomy-of-story]."
    - **Verdict:** does not bear yet. Short and attributed; the rest of the order of work is the workshop's own (the teller moves after the reveals).

27. **Target:** `plot-worksheet.md`, line 14, the one 6-word span: "for the hero and the main opponent".
    - **Verdict:** does not bear. Two common craft terms joined by "and"; nothing distinctive.

28. **Target:** `critique-rounds.md`, line 49 (the book's side of the rival).
    - **Defect:** keeps his sentence's shape and some of its words: "make its moral argument ambiguous, or … what the hero decides at the final choice, so that the audience goes on weighing the choice".
    - **Grounds:** `truby-anatomy-of-story.txt`, lines 3715-3716: "[quotation removed: 8 words of truby-anatomy-of-story]".
    - **Verdict:** bears (minor).
    - **Fix:** a rival needs the claim stated exactly, so use a short quotation in quotation marks with attribution, or reword. Whether this is a straw rival is for the theory-checker; I have not judged it.

29. **Target:** `critique-rounds.md`, line 30.
    - "Which instruction, reference or earlier output produced it" is the paper's "instruction, reference file, or previous stage output".
    - **Grounds:** `paper-icm-2603.16021.txt`, line 856, section 6.2.
    - **Verdict:** does not bear yet. A natural three-item list; the three-way sort that follows is the workshop's own.

30. **Target:** `how-stages-work.md`, lines 11-17 (the section 1 table).
    - **Defect:** the "question it answers" column is the paper's Figure 1 labels, in order:
      - two word for word: "Where am I?" and "Where do I go";
      - the rest nearly so: "What rules … apply?", "What am I working …?", and "What does this stage do?" for "What do I do?".
    - The column heading "Changes between runs?" is a row label from the paper's Table 2.
    - **Grounds:** `paper-icm-2603.16021.txt`, lines 229-232 (Figure 1) and 285 (Table 2): "Where am I?" "Where do I go?"
    - **Verdict:** bears (minor).
    - **Fix:** reword the question column in the workshop's own terms, or drop it; the "Where it lives here" column carries the table.

31. **Target:** `how-stages-work.md`, line 19.
    - Follows the paper's sentences in order:
      - "read as rules to follow" and "material to work on" track its "internalized as constraints" and "processed as input";
      - "separate folders tell the agent which is which" tracks its "separating them in the folder structure";
      - "set the factory up once, and each run makes a new product" tracks its "set up once … each run".
    - **Grounds:** `paper-icm-2603.16021.txt`, lines 265, 270-272 and 323.
    - **Verdict:** does not bear yet. "Factory" and "product" are term names; the rest is short and idea-level. A reword of the last clause would settle it.

32. **Target:** `how-stages-work.md`, line 76 (section 7).
    - **Defect:** the first two sentences follow one sentence of the paper (the Inputs table names what a stage reads, so a change there may leave its output stale). The last sentence has two runs that are almost the paper's:
      - "only the parts of a program that changed" (the paper has "the program": 7 of 8 words match);
      - "Only the stages that read the changed file need it" (the paper: "[quotation removed: 11 words of paper-icm-2603.16021]").
    - **Grounds:** `paper-icm-2603.16021.txt`, lines 837-841, section 6.1: "[quotation removed: 9 words of paper-icm-2603.16021]".
    - **Verdict:** bears (minor).
    - **Fix:** reword the last sentence and the compiler aside.

33. **Target:** `how-stages-work.md`, line 47.
    - An attributed report of the paper's finding, with its caveat. "Where the direction is set" and "brought into line with earlier decisions" track its "direction-setting" and "aligning output with earlier decisions".
    - **Grounds:** `paper-icm-2603.16021.txt`, line 643.
    - **Verdict:** does not bear yet.

34. **Target:** `how-stages-work.md`, lines 28-29, 49, 60-65 and 70 (a run, a stop inside a stage, markers, Verify).
    - The paper's ideas, attributed where they come from it, in the workshop's own words.
    - "Exactly the files and sections its Inputs table names" lightly echoes the paper's "exactly which files … and which sections".
    - **Verdict:** does not bear.

35. **Target:** `CONTEXT.md`, line 6.
    - "One job" comes from the paper's principle name, a term name.
    - "What it reads, does and writes" and "edit what it made before anything else runs" track "what it reads (inputs), what it does" and "before the next stage runs".
    - **Grounds:** `paper-icm-2603.16021.txt`, line 477, section 3.3.
    - **Verdict:** does not bear. An ordinary description; the routing table, the stage table and the graph are the workshop's own.

36. **Target:** `world-and-symbols-worksheet.md`, lines 11-21 (section 1).
    - The first three steps follow Truby's story-world order (designing principle, arena, opposed values). Each step is a pointer into the story-world skill, mixed with the Implied World theory's steps.
    - **Grounds:** `truby-anatomy-of-story.txt`, lines 1402-1407.
    - **Verdict:** does not bear.

37. **Target:** `stages/09-revision/references/revision-log.md`, the whole file.
    - The workshop's own practice; the paper's idea appears only in the sources line, in the workshop's words.
    - **Verdict:** does not bear.

**Outside my assigned list, noted in passing:**

38. **Target:** `StoryTest - project story.md`, line 192 (entry 36, "How it was read").
    - "one agent, reading the right files at each step" keeps 7 words of the paper's abstract.
    - **Grounds:** `paper-icm-2603.16021.txt`, line 11: "[quotation removed: 10 words of paper-icm-2603.16021]".
    - **Verdict:** bears (minor). Reword.

39. **Target:** `_config/questionnaire.md`, line 3.
    - "Set the workshop up once with the writer's standing preferences" is the paper's "set up once with the user's preferences".
    - **Grounds:** `paper-icm-2603.16021.txt`, line 270.
    - **Verdict:** does not bear yet. Attributed, one sentence.

40. **Target:** `sources/README.md`, the note under the paper's row.
    - "is open source under the MIT licence" is a statement of fact about the licence.
    - **Verdict:** does not bear.

## What I did not check

- **Not read by eye:**
  - the nine stage contracts (`stages/*/CONTEXT.md`);
  - the `output/README.md` files;
  - `stages/owner-edits.md`;
  - `_config/writer.md`;
  - most of `_config/questionnaire.md`;
  - the changed parts of `CLAUDE.md`, `README.md`, `22 Questions - meanings only you can settle.md` and `sources/README.md`.

  These went through the script only, at 8, 6 and 5 words, plus the one-word-swap scan. A search showed that none of the contracts, output READMEs or `_config/writer.md` names a book or the paper. Of entry 36, I read only the lines the scripts pointed to.
- **Not read in full:** the books. For each passage I found the matching book passage by searching its key terms. A passage drawn, without attribution, from a part of a book I did not search could be missed.
- **Not checked:**
  - whether the passages repeat what the skills already hold, or whether each pointer names the right section (brief item 8);
  - the theory readings, the rule labels, or whether the rival is sound (brief items 4 to 7). Those are the theory-checker's.
- **Not compared:** the `.epub` files. I used the `.txt` copies and assumed they match.
- **The planted-fault test:** not rerun, as the brief asked.

## Verdict

**passed after changes.** Before commit, these must be rewritten or cut to pointers:
- `stages/07-dialogue/references/dialogue-passes.md`, section 2 (finding 1) and section 1's headings (finding 21);
- `stages/06-scenes/references/drafting-scenes.md`, section 2 (finding 2), line 11 (finding 18) and line 26 (finding 19);
- `stages/02-characters/references/cast-sheet-and-moral-line.md`, section 2 (finding 3), the section 1 table's order and glosses (finding 15), and line 27 (finding 17);
- `stages/01-brief-and-premise/references/premise-worksheet.md`, section 7 (finding 4), section 4 (finding 5) and section 1 (finding 10);
- `stages/08-critique/references/critique-rounds.md`, section 4 (finding 6) and line 49 (finding 28);
- `stages/03-world-and-symbols/references/world-and-symbols-worksheet.md`, section 2 (finding 7), with the matching line 29 of `dialogue-passes.md`;
- `stages/how-stages-work.md`, line 82 (finding 8), the question column in section 1 (finding 30) and line 76 (finding 32);
- `stages/04-plot/references/plot-worksheet.md`, section 3 (finding 9);
- `stages/05-scene-weave/references/scene-weave-worksheet.md`, lines 13 and 22 (findings 22 and 23);
- entry 36 in `StoryTest - project story.md`, line 192 (finding 38).

After the rewrite, rerun `overlap_check.py` at 8 words, and have a second reader look again at the new text of findings 1 to 9.
