# The Long Places - project story

## The goal

A story written by GLM 5.3, another company's AI model (from Z.ai), with its thinking turned to the maximum. You wanted to see what it does when let loose on your concept:
- **The places.** Man-made places kept for immense spans of time (shrines, caves, temples, ritual sites) gain a quality that lets the people in them travel through time.
- **The last reveal.** Time travel is the very last plot point revealed, and it ties every mystery together.
- **The four theories.** Contact with the dead is leaned into but never said outright. Toxic fumes, a parallel reality and a wormhole are each hinted and almost canon, but none is ever confirmed.
- **The distant future.** An encounter with humans from the astronomically distant future, which nobody can ever be sure about.
- **The questions.** Sharp, short questions about belief, spirituality and whether science can replace belief.
- **The theme and the feeling.** Impact and consequence; a mind-bending sense of dissociation.
- **The villain.** Your addition: of the quality of Johan Liebert in *Monster*, meaning passive, quiet, never show-stopping, but resourceful and formidable.

As with the other story, every stage and every revision is kept.

## Where things stand

- **Two finished versions, both kept:**
  - GLM 5.3's own, revised once by GLM (file 10);
  - the same book revised by three Claude agents from an independent reading (file 19, about 49,150 words).
- **The Claude revision:**
  - Halden is now dangerous on the page from chapter IV.
  - Nilay makes one real move toward her brother in the middle.
  - The time-travel clues are thinner, and the parallel-reality thread is stronger.
  - The far-future visitors are stranger.
  - Emre's line about them is only a guess.
  - The slips are fixed.
- **How it was checked:** a fresh reader checked the Claude revision and found 11 small problems (2 must-fix). All were fixed, and its verdict is "the book reads as one; with these edits it is ready".

## How the pieces fit

| Piece | What it does | What it hands on |
|---|---|---|
| The concept (01) | Your words, plus the villain you added | Every stage reads it first |
| Designs (02, 03) | Three separate GLM writers each design the whole story | The judge |
| Judgement and blueprint (04) | GLM judges the designs, picks a base and merges the best into one blueprint | The critics |
| Blueprint critiques (05) | Three GLM critics: the mystery's discipline, the questions and theme, craft and the villain | The reviser |
| Revised blueprint and log (06) | Every finding: accepted or not, and what changed | The chapter writers |
| First draft (07) | Fourteen chapters, written in order, each writer seeing everything before it | The draft critics |
| Draft critiques (08) | Three GLM critics on the whole draft: the mystery, the questions, prose and continuity | The revision plan |
| Revision plan and log (09) | Every finding, accepted or not, and exact changes, chapter by chapter | The chapter revisers |
| The finished story (10) | All fourteen revised chapters in one file | You |
| Change notes (11) | Each chapter reviser's own list of what it changed, and what it could not | You |
| Final check (12) | GLM checks the finished story against your seven rules, with quotations | You |
| Independent reading (13) | A fresh Claude reader's honest view of GLM's version | The Claude revision plan |
| Claude revision plan (16) | One shared plan for the three Claude revisers, chapter by chapter | The revisers |
| Revised, before the check (17) | The three revisers' chapters as first finished, and their change logs | The continuity check |
| Continuity check (18) | A fresh reader on the revised book: seams, rules, slips | The final fixes |
| Revised by Claude, final (19) | The book after every check finding was applied | You |
| Pipeline program (`tools/`) | Runs GLM through the stages. It reads your key from a private file outside the repository, and the key is in no file here | Everything above |

## Words used here

- **GLM 5.3:** the AI model from Z.ai that wrote this story. **Maximum thinking** means it reasons at length before each answer. Its reasoning is saved separately from its answers.
- **Blueprint:** GLM's master plan for the story: the places, people, four theories, clues, chapter outline, villain and rules.
- **Clue ledger:** the blueprint's table of every clue, where it appears, what it seems to support, and what it really is.
- **Keeper interlude:** the short, undated passage that opens each chapter, in the voice of someone tending the lamps.
- **Pipeline:** the program that runs the stages in order, several at once where parts are independent.
- **MiMo v2.6 Pro:** an AI model from Xiaomi. Here it is a fresh-eyes critic in the revision rounds and runs the audience test at the end.
- **Substantive finding / quibble:** a problem a careful reader would notice and that weakens the story, versus a point only an audience test could settle (word choice, rhythm, the exact timing of an event when nothing depends on it).
- **Audience test:** five simulated readers with different tastes read the finished story and report how it played for them.
- **Ruling:** my written decision at the end of each round's review: which findings are real and must be fixed, which are overruled, and why. Nothing is changed without one.
- **Fable 5.1:** Anthropic's Fable model. It gives one review of each finished revision, at extra-high effort, and does nothing else.

## Log

1. **The concept, and GLM reached** (file 01).
   - You asked for GLM 5.3 at full thinking and gave an API key (a password for the service).
   - I found GLM 5.3 listed and its deepest thinking setting, "max". Your key works only through GLM's coding-plan address: the general address reported no balance. So this draws on your coding plan.
   - One small test call worked: it wrote two sentences about a cave shrine at dusk, in 5 seconds.
   - I stored the key in a private file outside the repository, readable only by the machine's owner account. No output or repository file contains it; I searched every file here for it.
2. **First designs, stopped for the villain** (files 02).
   - Three GLM designers wrote whole-story designs at the same time. Each took six to seven minutes and 25,000 to 29,000 tokens.
   - Just then you added the villain: "of the same quality as Johan Liebert from the anime Monster. Passive, quiet, non show stopping, but remarkably resourceful and a formidable threat."
   - The villain belongs in the design from the start, so I stopped the run and kept those three designs here as the "before the villain" version.
   - My way of stopping it also stopped my own command; nothing was lost, since the designs had already been saved.
   - I added your words to the concept, with one note of mine: "of the same quality" means working the way Johan works on a reader, but as this story's own creation, not a copy of him.
3. **Three new designs, with the villain** (files 03). Every stage's instructions now ask about the villain: the designs, the judge, the critics and the final check.
4. **Judgement and blueprint, version 1** (file 04). GLM judged the three designs, chose a base, and merged the best of the others into one blueprint.
5. **Blueprint critiques** (files 05). Three GLM critics:
   - the mystery's discipline: nothing confirmed early;
   - the questions about belief and the theme;
   - craft, dissociation and the villain.
6. **Blueprint version 2, with its revision log** (files 06).
7. **The first draft** (file 07).
   - Fourteen chapters, written in order at maximum thinking. Each writer saw the blueprint and every earlier chapter.
   - Each chapter took between about 5 and 11 minutes. Most of each answer is GLM thinking before it writes: 17,000 to 46,000 thinking tokens per chapter, against 3,700 to 5,300 tokens of prose. The thinking grew as the story did: chapter 1 took the least, chapter 14 the most.

8. **The draft criticised** (files 08). Three GLM critics each read the whole draft:
   - the mystery's discipline;
   - the questions about belief;
   - prose, continuity and the villain on the page.
9. **The revision plan and log** (file 09). GLM listed every finding, accepted or not, and wrote exact changes for each chapter.
10. **The revised story** (file 10).
    - Fourteen revisers worked three at a time. Each saw the whole draft and the plan and revised one chapter.
    - Each took between 1.5 and 6.5 minutes. The story ended at about 49,000 words, close to the draft's length.
11. **The change notes** (file 11): each reviser's own list of what it changed.
12. **GLM's final check** (file 12).
    - All seven rules pass, with quotations: time travel last; four theories hinted but none confirmed; the dead never said outright; the ending ties the mysteries together; the far-future encounter left unprovable; sharp questions about belief; the villain passive but formidable.
    - It lists the loose ends it left on purpose, among them what the Trust and Halden really are, a vanished school party, and a cave breath timed at eighteen, then nineteen, then twenty minutes in different chapters.
13. **My own reading** (no file).
    - **Read:** chapter I, chapter VII and the whole of chapter XIV. **Not read closely:** the other eleven chapters.
    - **Chapter I** is strong literary writing: the keeper's lamp lesson, a count of rooms that won't stay at forty, a letter from the villain thanking Nilay "in advance", and a warmth against her shoulder that could be a cat, a draught or someone she lost.
    - **Chapter VII** is the encounter below. The strangers have perfect prosthetic-like teeth but have never been near a clinic. They carry grain from a wheat that no longer grows anywhere. One asks "Is the fire mountain awake?". Every camera file comes back empty, which keeps it impossible to say whether they came from the deep past or the far future.
    - **Chapter XIV** lands the reveal cleanly and very late. Nilay wakes somewhere else holding a letter in her own hand dated tomorrow. Her brother, lost in 1999, has been keeping the lamps "along the road" ever since. The oldest handprint on the wall, over 10,000 years old, is her own.
    - **Doubts:**
      - The prose is dense and oblique, and some readers may find it hard going.
      - I haven't checked the middle chapters to see whether the villain feels like a real threat or only an unsettling presence.
      - The eighteen, nineteen and twenty minutes may be a continuity slip that GLM has called deliberate.

14. **An independent reading** (file 13).
    - A fresh Claude reader that wrote none of the story read all fourteen chapters as a first-time reader.
    - **Best:** the keeper-letter frame; chapters V, XI and XIV; and evidence that stays honestly balanced between the explanations. The questions about belief are the book's strongest area.
    - **Weakest:**
      - Halden is an unsettling presence rather than a formidable threat. The harm he causes is large when added up (a death, the women's vigils ended, the keeper removed the day before she collapses), but it all comes wrapped as kindness, and the book half shares his view.
      - The middle chapters are all one tone, with a passive heroine and repeated words.
      - Time travel is heavily signalled, so a genre-savvy reader may guess "time" by chapter IX, though the exact twist still surprises.
      - The far-future visitors speak a worn-down Turkish, so they never feel astronomically far off.
    - **Its three suggested changes:** make Halden dangerous on the page early; cut the repetition and give Nilay one active move; rebalance the clues.
    - **Slips found:**
      - two wrong weekdays: 4 September 1999 was a Saturday, not a Sunday, and 4 September 2025 was a Thursday, not a Friday (the second is my own find);
      - "tourches";
      - a fan-repair log dated before the breakdown;
      - Márton's years given as both 27 and 28.
    - **Checked by me:** the weekday slips, the typo, the breathing times (18, 20, 19, 20, 20, 18, which looks deliberate) and the repeated words. The reader's judgements on the villain and pacing rest on its reading, not mine.

15. **Three Claude agents revise it** (files to come).
    - You said: "Set 3 if your own agents on the revision. And let GLM continue work on the other story."
    - So this revision is by Claude, not GLM, working from the independent reading.
    - One agent writes a shared plan covering:
      - Halden as a visible threat by chapter IV;
      - one active move by Nilay toward Emre in the middle;
      - fewer "dated before its cause" clues, so time can't be guessed by chapter IX;
      - a stronger parallel-reality thread;
      - stranger far-future visitors;
      - Emre's line about them softened to a guess, while time travel is still confirmed at the end;
      - less repetition, and loose threads tied or cut;
      - every slip fixed.
    - Three agents then each revise a block of chapters (I-V, VI-IX, X-XIV), keeping GLM's voice and length. A fresh reader checks the seams and the rules, and each block fixes what the reader finds.
    - Never more than three at once. Every change is logged.

16. **The Claude revision plan** (file 16). About 13,000 words, settling each question once for the whole book:
    - **Halden's aim:** the sites kept by one keeper at a time, unknown, and the people this costs never recorded.
    - **His chosen harm:** in 1999 he answered the police in a way that was literally true, "The Trust holds no survey of any chamber below the fourth door", and it quietly ended the search for Nilay's brother.
    - **Nilay's move:** in chapter VII she picks the drill site over the room she searched in 1999.
    - **The clues:** only three "dated before its cause" moments are kept. Márton's gravity readings now match Yusuf's 41-room mornings, and the visitors are stranger.
17. **Three Claude revisers** (files 17). Each revised one block: chapters I-V, VI-IX and X-XIV. Every change is logged in plain words: done, done differently or not done, and why.
18. **A fresh continuity check** (file 18).
    - It found 11 small problems. The 2 must-fix: a log entry timed at the very minute another character was awake at the same spot, and "nobody had knocked" where someone had.
    - All were fixed, and the earlier chapter versions are kept in file 17.
    - Verdict: "the book reads as one; with these edits it is ready."
19. **The revised book** (file 19). About 49,150 words, against GLM's 48,980.
    - **My own check:** I read the new Halden scene in chapter IV; it lands as a real, chosen harm done through paperwork and courtesy.
    - **Not read by me:** the rest of the revision.
    - **Correction to entry 14:** I said chapter XIV's "Friday" was a slip. It isn't. That chapter is set in 2026, a year after the dig, and 4 September 2026 was a Friday. The planner caught it. A note is added to file 13.

20. **Revision rounds until only quibbles are left** (files to come).
    - You said: "Do more revision passes on both until the only critiques are just word placements or quibbles over the exact timing of events."
    - The rounds start from the Claude revision (19), with Claude agents as you set: three critics, one verifier and, if real problems remain, one planner and three revisers. Never more than three at once.
    - A finding is **substantive** if a careful reader or viewer would notice it and it weakens the story: a plot hole, a contradiction, a broken rule of yours, a character acting without cause, a scene with no job, sagging pace, confusion that serves nothing, a theme stated instead of shown.
    - A finding is a **quibble** if only an audience test could settle it: word choice or placement, sentence rhythm, the exact minute or day of an event when nothing depends on it, taste.
    - A separate verifier confirms each substantive finding, marks it a quibble, or rejects it. Only confirmed ones are fixed, and the rounds stop when a round confirms none.
    - Quibbles are recorded, not fixed.
    - At most six rounds. If the cap is reached, I'll say so.

21. **MiMo joins as a third opinion, and how many helpers can run at once** (programs in `tools/`).
    - You asked me to find a use for MiMo (MiMo v2.6 Pro, Xiaomi's AI model), and how many agents I can run at once, since MiMo and GLM can each run 5.
    - **How many at once:**
      - *My own Claude helpers:* you set a limit of three. In practice my workflow tool runs at most two at a time on this machine: it allows two fewer than the machine's four processors.
      - *GLM and MiMo:* they run on their makers' computers, not this one. This machine only sends the question and waits, so five of each at once costs it almost nothing. The programs use up to five.
    - **What MiMo does now:**
      1. *A fourth critic in every round, on both stories.* It is a different model from the ones that wrote and revise each story, so it reads with genuinely fresh eyes. Its findings are weighed exactly like the others.
      2. *The verifier for GLM's rounds on* Seconds, *so GLM's work is never cleared by GLM alone.*
      3. *The audience test at the end.* Five simulated readers, each with different tastes, read each finished story at the same time and say where they were gripped, lost, bored or moved. MiMo then writes the audience analysis. The five: a nurse who reads literary fiction, an engineer who checks every rule, a film student, a retired bus driver who reads a thriller a week, and a philosophy teacher who goes to church.
    - **What I tested:**
      - *Finding the right door.* Only MiMo's Singapore address accepts your key; the two others refuse it.
      - *Thinking depth.* Its deep-thinking mode works; its "max" setting is refused, so "high" is used.
      - *A whole book at once.* One critique of the entire Claude revision took 9 minutes 37 seconds. MiMo read all 62,000 tokens (a token is roughly three-quarters of a word) and thought through about 18,000 more before writing.
    - **What MiMo found in round 1:** 15 findings; it marked 4 substantive:
      - Halden reads as elegant rather than frightening.
      - Márton's last descent alone has no visible moment of decision.
      - The parallel-reality theory has no adult champion.
      - The far-future visitors are too faint to be read as people from very far away.
      A Claude verifier will now check these alongside the three Claude critics.
    - **A slip, caught and fixed:** MiMo's first critique came back with garbled accented letters ("MÃ¡rton" for "Márton"). Its server doesn't say which alphabet it uses, and the program guessed wrong. I set it explicitly, repaired the file (nothing was lost; it was a display error only), and tested again: "Márton — Kırk Oda — café" now comes back intact. GLM's files were checked and never had the problem.
    - **Because a MiMo critique takes almost ten minutes,** it is started in the background at the start of each round, while the three Claude critics read. The verifier waits for it.

22. **I am the final authority, and Fable 5.1 reviews each finished revision once** (programs in `tools/`).
    - You said: "You are the final authority. Not any of the agents." And: "When a full revision has been written, get Fable 5.1 on Xhigh effort to do a single review on that one document. Nothing else. And only when a revision has been completed."
    - **What changed:**
      - *Before:* the verifier's count decided on its own what was fixed, and the rounds ran unattended.
      - *Now:* each round stops after the verifier. Its verdicts are only advice. I read the four critiques, the verifier's advice and Fable's review, and check the disputed points against the book myself. Then I write a ruling (`ruling.md` in each round's folder): which findings are real and must be fixed, which I overrule, and why. The planner and revisers work only from my ruling. Only I can declare the book finished.
    - **Fable 5.1:** Anthropic's Fable model at "extra-high" effort, meaning it thinks longer and harder than usual before answering. It gives one review of each finished full revision, joined into one document, and does nothing else: it doesn't critique mid-round, verify, plan or revise. It runs only once a revision is complete.
      - The first finished revision is file 19, the version round 1 is reading, so Fable is reviewing it now.
      - After that, each round's revision is joined into one document as soon as all fourteen chapters are done, and Fable reviews it while the next round's critics read.
    - **Round 1's first run** was allowed to finish its critiques and verification. It is stopped the moment the verifier is done, before any planning, so nothing in the book changes until I have ruled.

23. **Round 1: four critics, Fable's review, the checker's advice and my ruling** (files 23).
    - **What read the book (file 19):**
      - three Claude critics, each through one lens;
      - MiMo with fresh eyes;
      - Fable 5.1, once.
    - **Fable's verdict:** "finished as a story and keeps every owner's rule", with 3 substantive problems and 9 quibbles. Its three problems:
      - Nilay's mother never appears after the reunion.
      - Nilay's printed statement in chapter VIII says "two" figures, while the narration says her filed statement says "three".
      - Chapters VI and VII give the same Monday evening two different pictures.
    - **The checker** (a Claude agent) weighed the four critiques and advised that 7 findings were real. It did not see Fable's review. It judged MiMo's three other substantive findings wrong, and Fable agrees on two of them.
    - **My checks:** I checked each disputed point against the book myself. For example:
      - The "two/three" slip goes back to GLM's first draft. GLM's master plan never meant the file to change by itself, so it is a slip, not a planted clue.
      - The weekdays in VI and VII really do collide: 1 September 2025 was a Monday.
    - **My ruling: fix 11, correct 6 small errors of fact.**
      - I upheld the checker's 7.
      - I overruled it 4 times: on the "two/three" statement (it had called it deliberate), on Priska's meter on the night Márton died, and on chapter XII explaining its own meaning. I also added Fable's VI/VII finding, which the checker had never seen.
      - The 6 small errors include a spring that should be summer, a fence mentioned before it is built, and a watch stopped at twenty past nine on a descent made "before dark".
    - **Two fixes are there because the book broke your rules:**
      - One sentence in XIV confirmed the fumes theory.
      - Another said time travel did *not* account for three mysteries, though your rule is that it ties them all together.
    - **Everything I overruled is listed in the ruling, with the reason.** All quibbles are recorded and left for the audience test.
    - **A timing note:** the first run was stopped the moment the checker finished. Its planner had just started and was stopped before writing anything, so no plan was made from the checker's count alone.

24. **Round 1's fixes made** (files 24).
    - A planner turned my ruling into exact changes, and three revisers made them, one block of chapters each. Every change is logged in plain words.
    - **I checked every change against my ruling, word by word.** All were made as ordered. The one piece of new wording I had to check was the reviser's sentence on Priska's air: its figures (4.0 percent at the fourth door; 15 events in 22 nights, 2 in 26) are all figures chapter V already gives.
    - **The new moment for Nilay's mother** (141 words): she finds the ribbon on the table by the bread oven, asks nothing, folds it on its old creases, and keeps smoothing the top fold "long after there was nothing left to smooth". At dusk she watches her daughter go out with the oil can, "the way she had once watched a boy go out in house slippers, and did not call anything after her."
    - The book is now about 49,330 words.

25. **Round 2: reviews and my ruling** (files 25).
    - **Fable's review of the round-1 version:** "a finished, tightly built literary mystery that keeps every one of the owner's rules and has a villain worthy of the brief; it needs a short polish pass, not a rewrite", with 4 substantive problems and 10 quibbles.
    - **The checker advised 6 real problems.** MiMo's three substantive findings were all judged wrong; two of them repeat points already settled in round 1.
    - **My ruling: fix 8.**
      - I upheld the checker's 6. Among them:
        - When Nilay wakes, the wax reads as the lid of the tin box, though the ritual seals only the letter.
        - The sheet from tomorrow is dated "tomorrow" on the very morning it describes.
        - Priska, who made everyone wear her air meter, lets Nilay sit a still-air night below without one.
      - I added 2 of Fable's: Nilay writes an accusation against the Registrar and strikes it through, so accepting the keepership from him visibly costs her something; and a plain slip where the oil can is handed to Nilay twice.
      - I left 4 of Fable's as quibbles, with reasons. One example: "the whole hour" on the meter strip is the book's own name for the event, not sixty minutes.
    - **Protected on purpose:** Fable warned that the sealed-box proof has a deliberate hole: Nilay breaks the seal alone, below. My ruling forbids anyone from "strengthening" it.
    - **The trend:** round 1 had 11 fixes, several of them real plot problems. Round 2 has 8, all small (a clause or a sentence each). The problems are getting smaller.

26. **Round 2's fixes made** (files 26). I checked all eleven changes word by word against my ruling, and all were made as ordered. The book is now about 49,440 words.

27. **Round 3: reviews and my ruling** (files 27).
    - **The critics found far less.** Substantive findings fell to 1 (story), 1 (people), 3 (continuity) and 4 (MiMo). The checker confirmed 3; it judged three of MiMo's four wrong and the fourth a quibble.
    - **Fable's review of the round-2 version:** "a finished, rule-keeping novella that needs one polish pass … not re-plotting", with 3 substantive problems and 12 quibbles.
    - **My ruling: fix 4, and correct one garbled phrase.**
      - *The masks.* In real chemistry, dust masks and filter cartridges don't stop carbon dioxide. Only a chemical scrubber (soda lime) or piped air does. Yet the book's air scientist prescribed dust masks against it. That handed an informed reader a reason to throw out the fumes theory, which your rule says must stay almost canon. The masks are now named once as soda-lime scrubber masks.
      - *The ribbon.* The letter from the next day says "I did not cry until the ribbon", and the book never shows her crying. One sentence now shows it.
      - *Two plain errors:* a summary that misquotes one of the four statements, and Priska's father's cough lasting twelve years and then thirty.
    - **Two of my own earlier calls, corrected:**
      - In round 1 I left the ribbon line alone, calling it restraint. Fable's argument changed my mind: it is the one prediction on the sheet, so it must come true on the page.
      - In round 1 I also filed the cough slip among the quibbles, which was wrong. It is a plain error.
    - **Left for the audience test:** Fable's two bigger points.
      - *Voice:* every character talks in the same wise, aphoristic voice.
      - *Pace:* chapter XIII is dense just before the climax.
      These are matters of taste and pace, the voice is the book's own, and a "voice pass" over 49,000 words would be a rewrite. The five simulated readers can tell us whether they tire of it, and then it becomes your call.
    - **The trend:** fixes per round have gone 11, 8, 4, and each is now a word or a sentence.

28. **Round 3's fixes made** (files 28). I checked all five changes word by word against my ruling, and all were made as ordered. The book is now about 49,470 words.

29. **Round 4: reviews and my ruling** (files 29).
    - **Fable's review of the round-3 version:** "finished in structure and nearly finished in text — it keeps every one of the owner's rules, with a Johan-quality villain and a genuinely earned last reveal; four small sentence-level fixes stand between it and done."
    - **The checker confirmed 2.** It judged seven of MiMo's eight substantive findings wrong and the eighth a quibble.
    - **My ruling: fix 5, each a clause or a sentence, and correct 3 slips of wording.**
      - Nothing on the page stops anyone going back to the polished chamber for four months. One clause now says the Ministry has sealed it.
      - The second handprint Nilay presses at the climax is never accounted for when she studies the wall that winter. One sentence now says there is one print, and she cannot tell which of the two it is.
      - The fingerprint match, the book's one hard proof, now shows how the 1924 photograph reached the technician: the Trust sent it, "as a courtesy".
      - Priska's air meter ticks six times a minute, so its paper strip is also a clock. One sentence now reads its length: it agrees with the watches, three hours and thirty-seven minutes. The lost time was the party's alone.
      - "The two dates side by side" now says plainly which two Julys it means.
    - **Four of these reverse my own earlier calls.** I had left the chamber, the fingerprint's route, the meter strip and the two Julys as quibbles or "inferable". Each came back from a different reviewer with a better argument, and each costs a clause. The lesson I've written into the ruling: when a point keeps coming back and costs a clause to settle, settle it the first time.
    - **Where I overruled Fable:** it said a keeper's letter in chapter XI contradicts Melek, "forty years" against "sixty". The book's own text answers it. Melek was chosen for the keepership sixty years ago and kept the niche for forty winters; she says both in the same chapter.
    - **The trend:** fixes per round have gone 11, 8, 4, 5. The last two rounds are all single sentences, and Fable now calls the book nearly done.

30. **Round 4's fixes made** (files 30). I checked all nine changes word by word. They were made as ordered, but the planner rightly flagged three slips in my own round-4 wording:
    - I had Priska "not average" two figures in September, though chapter XI says she learned that later, from Márton.
    - I used Márton's times (three hours thirty-seven) where Priska's give three hours forty.
    - I wrote "None of mine deployed" for Márton, though Yusuf used Márton's heat gun.

    All three are corrected in round 5.

31. **Round 5: reviews and my ruling** (files 31).
    - **Fable's review of the round-4 version:** "a near-finished, genuinely successful novella that keeps every one of the owner's rules", with 2 substantive problems and 10 quibbles. The checker confirmed 2 more.
    - **My ruling: fix 4, and correct my own 3 slips.**
      - *Emre's confession.* He says he answered his sister in the dark with the room's name, but she remembers only humming. The book had already planted the answer: the lullaby "paused where the words would be", and she "never once let herself wonder what the words were". Now the name was in the pause, and a contradiction becomes a payoff.
      - *The drowned chapel.* The page about it gets one plain sentence, because the ending's cost rests on it: someone rowed a lamp out to a drowned church every summer night for six years, unpaid, then stopped, and the place went quiet.
      - *Melek's rain rule.* The drilling now starts two days after the first rain, not the morning after, which Melek's own rule forbids. The fix is one phrase.
      - *The handprint.* At the climax she now presses her hand *over* the old print, not beside it, so the wall shows one print, as it always has. My round-4 fix had caused this.
    - **The trend:** fixes per round have gone 11, 8, 4, 5, 4, and all are now phrases or single sentences. Round 6 is the last round under the cap I set in entry 20.

32. **Round 5's fixes made** (files 32). I checked all seven changes word by word, and all were made as ordered. The planner rightly wrote "seven years" of summers on the drowned chapel where my example said six: 1955 to 1961 is seven. The book is now about 49,630 words.

33. **Round 6: reviews and my ruling** (files 33).
    - **The critics are nearly done finding things.** They marked 1, 1, 4 and 1 findings substantive, and the checker confirmed only 1.
    - **Fable's review of the round-5 version:** "a strong, finished-in-logic novella that keeps every one of the owner's rules", with 3 substantive findings and 9 quibbles.
    - **My ruling: fix 4, and correct 2 slips from round 5.**
      - *The boy at the first dawn.* Why didn't he follow the grey man up? Chapter II shows the stone opens at grey even in that corridor. Now: "in the morning, while I slept, he went up and took the light with him." This reverses my round-1 call, which had rested on a reading chapter II contradicts.
      - *Márton and Melek's rule.* Did he break her "not one past the first cloud"? One sentence now says his sky held when he went down.
      - *The tall woman.* She no longer "bends to" a doorway that is in the chamber's ceiling; she rises until it is at her shoulder. My own round-1 fix had caused this.
      - *Marques.* She no longer speaks Márton's private joke as her own; she quotes what he once wrote to her.
    - **Left for the audience test, again:** Fable's point about the shared wise voice, now raised three times, and its point about chapter XIII's density. Both would mean a pass over the book's voice or cutting its texture, not a clause. The five-reader panel is the right judge.
    - **The cap.** This is round 6, the last under the cap I set in entry 20. After these fixes I am running one more review with the same critics, checker and Fable, only to confirm. If it confirms nothing substantive, the book is done, and the audience test comes next.
    - **The trend:** fixes per round have gone 11, 8, 4, 5, 4, 4. The checker's confirmed findings have gone 7, 6, 3, 2, 2, 1.

## Next step

After each round's review, rule on the findings myself, then have the fixes I order made. When I rule that only quibbles remain, run MiMo's audience test on the final book, add every round's critiques (MiMo's included), verification, plan and logs here with the final book and the audience analysis, and tell you how many rounds it took.
