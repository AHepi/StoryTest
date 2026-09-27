# Fourth Direction season - project story

## The goal

Write a full TV season, about ten episodes, built from your document "The Fourth Direction": a world stacked in leaves, where crossing between them can turn you into your own mirror image.

- **The core message:** a culture that never questions anything always dooms its people to suffering and eventual death. It must be shown by what happens, never said.
- **What you want from it:** mind-bending, full of twists, and nothing like your screenplay *The Catch*.
- **The part you care about most:** the revisions. Every critique, every change and every earlier version is kept and logged.

## Where things stand

- **The first attempt, Caraway, is dropped.** You said it was too close to *The Catch*, presented religion in a stock way, referred to the theory of explanation, named ideas outright and was a dystopia. Its files are kept as history (01 to 06). Why it was dropped is in 07.
- **The second attempt produced three pitches and three independent reviews** (08 to 11).
- **You chose the first pitch, *Seconds*,** an Essex family of thieves who step through walls. You asked for every invented law of *The Fourth Direction* to be true in it (12).
- **The *Seconds* plan is on version 3** (16 to 20), after two rounds of three critics each. Round 1 raised 49 findings and round 2 raised 52; none was thrown out entirely. I checked version 3 myself (21), and it passes your rules.
- **All ten episodes are written** (episodes 1 to 3 by Claude's writers, 4 to 10 by GLM), with GLM's whole-season check applied (file 32). Now: Fable's single review and GLM's revision rounds, with me ruling on what gets fixed.
- **Separate job, finished:** the workshop reorganised to work like the paper you sent. It is reviewed, committed through your commit gate, and pushed to its own branch, with its own draft pull request: https://github.com/AHepi/StoryTest/pull/3.

## How the pieces fit

| Piece | What it does | What it hands on |
|---|---|---|
| The brief (01, then 08) | Tells the writers what you asked, your rules, and what to avoid | Everything below starts from it |
| Pitches (02, and the new ones) | Rival versions of the whole season, written separately | The judge picks one and borrows from the others |
| Pitch reviews (11) | Independent checks of the pitches: originality, your rules, use of *The Fourth Direction* | The judge's decision |
| Judgement and season plan (03, and the new ones) | The master document every episode writer follows | The critics |
| Critiques (04, 06, and the new ones) | Separate critics, each hunting one kind of problem | The reviser |
| Revision logs (05, and the new ones) | Every finding: accepted or rejected, why, and exactly what changed | The next version of the plan, and you |
| Your feedback (07, 12) | The biggest revisions: why an attempt was dropped, which pitch you chose, and what else you asked for | The next brief or rebuild |
| Episodes (to come) | Each drafted, critiqued and revised, with its own log | The season |

## Words used here

- **Leaf:** one of the stacked worlds. Ours is one leaf.
- **Crossing:** leaving your leaf for a few seconds, through the fourth direction.
- **Turned:** coming back from a crossing as your own mirror image. A turned body can't use ordinary food.
- **Pitch:** a short version of a whole season, used to compare ideas before writing it in full.
- **Season plan:** the master document, with the world, the characters and every episode's events.
- **Critique:** a critic's list of problems, each with a suggested fix.
- **Revision log:** a record of what each critic found, whether it was accepted, and what changed.
- **Twist:** a reveal that makes you see what came before differently.
- **Plant:** an earlier detail that makes a later twist fair.
- **Helper agent:** a separate copy of Claude given one job. Never more than three work at once, as you asked.
- **GLM 5.3:** an AI model from Z.ai. It is finishing *Seconds* from episode 4 on.
- **MiMo v2.6 Pro:** an AI model from Xiaomi. Here it is a fresh-eyes critic and the verifier in GLM's revision rounds, and it runs the audience test at the end.
- **Substantive finding / quibble:** a problem a careful viewer would notice and that weakens the season, versus a point only an audience test could settle (word choice, rhythm, the exact timing of an event when nothing depends on it).
- **Audience test:** five simulated viewers with different tastes read the finished season and report how it played for them.
- **Ruling:** my written decision at the end of each round's review: which findings are real and must be fixed, which are overruled, and why. Nothing is changed without one.
- **Fable 5.1:** Anthropic's Fable model. It gives one review of each finished revision, at extra-high effort, and does nothing else.

## Log

1. **Brief written** (file 01). Your request, both attachments, your four story theories and your hard-to-vary test went to the writers. So did a starting idea of mine: a walled city, twins, and a mint test. Looking back, that starting idea steered the result towards *The Catch*.
2. **Three pitches written** (02). Two built on my starting idea, and one different story, "The Kept".
3. **Judged and merged into season plan version 1** (03). Pitch A was the base, with pieces grafted from B and C.
4. **Round 1 criticism** (04). Three critics looked at logic, theme and craft, and found 50 problems between them.
5. **Round 1 revision** (05). All 50 were accepted, six of them only in part. Version 2 of the plan and a full log.
6. **Round 2 criticism, stopped** (06). Three more critics finished their reports and a version 3 was written. It was stopped before its log was written, because your feedback arrived.
7. **Your feedback: Caraway dropped** (07).
   - You said it was a rip of *The Catch*, that its religion was presented in a stock way, that it must never refer to the theory of explanation, that it should use far more of *The Fourth Direction*, that it named ideas outright, and that it should not be a dystopia.
   - On checking, I found seven close overlaps with *The Catch*, including the name Nell, the mint reveal, backwards writing and germs nothing will eat.
   - Everything kept, nothing deleted.
8. **Second brief written, and the second attempt started** (08).
   - The brief carries your six rules, what to avoid, and a long list of *The Fourth Direction*'s unused ideas.
   - The theory file was taken out of the writers' reach.
   - Your craft skills were added as guidance.
   - Three pitches in three kinds of story are being written, then reviewed independently, merged, and criticised twice.

9. **A separate job started: the workshop reorganised like the paper you sent** (no file in this folder; it lives on its own branch).
   - You said: "Set one more agent to branch and update the repo so that it functions more like this paper. And fill it with details from this book."
   - The paper is "Interpretable Context Methodology: Folder Structure as Agent Architecture". It describes running AI work through numbered stage folders, each with a plain file saying what that stage reads, does and writes, and a pause after each stage so a person can check and edit.
   - One agent is working alone on a new branch, `claude/icm-story-workspace`. The branch starts from your newest workshop branch.
   - The three books (McKee's *Dialogue*, Truby's *The Anatomy of Story* and *The Anatomy of Genres*) are in a folder git never commits. Only the agent's own wording goes in.
   - Your workshop's rule is that nobody reviews their own work. So anything needing review will wait for an independent reviewer before it is committed and pushed.
   - This makes four agents at once while the three story writers are busy. I took "one more agent" to mean you allowed that.
   - Settled afterwards: I asked which book "this book" meant. You said: "These books". So it means all three, which is how the agent was already briefed. The agent was told, so its own log can quote your answer.

10. **Three new pitches written** (file 10).
    - ***Seconds***: an Essex family of thieves who step through walls and boast they always come back unturned. The lead kind of story is crime.
    - ***Honest Weight***: a 1911 prairie town whose wonder-wheat grew beside a stone that fell from nowhere. It is a coming-of-age story.
    - ***Slack Water***: a present-day Highland loch town that cures turned people at slack tide. It is a detective story.
    - One writer's run broke partway and restarted by itself, so the third pitch arrived about an hour after the other two.
11. **Three independent pitch reviews** (file 11).
    - *Seconds* was judged the most original and the strongest on the message, and the closest to ready.
    - *Honest Weight* had the richest material but leaned towards Caraway and ended where Caraway ended.
    - *Slack Water* was judged not original enough: under it sat Caraway's mechanism and ending.
12. **Your feedback 2: *Seconds* chosen, and every invented law in** (file 12).
    - You said: "First is best. Now I want to see what happens if you incorporate ALL of the fake laws of physics from "the fourth direction" attachment. Sorry, changed my mind".
    - A judge was merging the three pitches when this arrived. It was stopped before writing anything, so there is no file for it.
    - I read "all the fake laws" in the widest sense, so no reading is missed:
      - all seven laws, clause by clause;
      - the four things the page marks as made up;
      - its seven theorems;
      - its smaller consequences;
      - its plot examples wherever they fit.
    - Two of these the pitch had deliberately left untrue: that life next door is mirror-handed, and that moving there cures a turned person. Both are now true.
    - A turned body's germs being mirror-life must now appear too, used in a way unlike *The Catch*'s dishes and Caraway's mould.
    - A writer is rebuilding *Seconds* into a season plan with a table showing where each law does its work, then two rounds of criticism, all logged.
13. **The workshop job: built, reviewed, being fixed** (no file in this folder).
    - The agent built nine numbered stages, from brief and premise to revision. Each has a plain file saying what it reads, does, writes and checks, plus reference notes from the three books in the workshop's own words. Your copying check found one 8-word run, which was rewritten, then none.
    - Following your workshop's rule, three reviewers who did not build it checked it: the theory-checker, the copy-checker and the use-tester. All three said "passed after changes":
      - 24 findings on how your theories are read;
      - passages that follow the books' order too closely;
      - a walk-through that found where the stage files stall.
    - The builder is now fixing each finding, or recording why not. A reviewer will then take one narrow look at the answers before anything is committed or pushed.
    - Correction to entry 9: I wrote that I asked which book you meant. I didn't ask; you told me without being asked.
    - Correction to entry 10: I wrote that one writer's run "broke partway and restarted by itself". I checked afterwards and the records don't show that. All they show is that the third pitch took about an hour longer than the other two. The reason is unknown.

14. **The workshop job finished and pushed** (no file in this folder; branch `claude/icm-story-workspace`, draft pull request 3).
    - The builder answered all 80 first-round findings.
    - A fourth reviewer, new to the job, checked every must-fix answer and a third of the rest. Every answer was true. It found three more must-fixes. One was a knock-on from my own mistake: the workshop's entry had copied my wrong claim that I'd asked which book you meant.
    - After those were fixed, a final look at only the changed lines passed it. Two small points are recorded as open, as your workshop's rules require after two rounds.
    - The reviewers' reports are kept word for word in the workshop's reviews folder, apart from short book quotations they used as evidence. Those were replaced with a marker, because your copying check refuses any committed book text.
    - A record of every instruction I gave each agent is kept too.
    - Committed through your commit gate: every check passed, and the receipt was complete.
    - Your planted-fault test still shows 4 of 214 failing. The same four failed before this work began, since your workshop's entry 34.

15. **Why the third pitch was late, found** (no file).
    - Entry 10's correction said the reason was unknown. It is now known: this machine has four processors, and the tool that runs the helper agents runs at most two at once on a machine that size.
    - So the third pitch writer waited its turn, and so do the third critic in each round. Nothing broke.
16. **The rebuild of *Seconds* with every law: version 1 written** (the file will be copied here with its critiques and logs when the round finishes).
    - The plan is about 110 KB. Its first round of three critics is running:
      - one checks every law, item by item;
      - one checks craft;
      - one checks the message and originality.

17. ***Seconds* critique round 1** (files 17). The three critics raised 49 findings between them. The biggest:
    - two turned people holding hands could cure one of them for free;
    - Liam was "fridged": he appeared only to die;
    - the finale quietly borrowed the second pitch's ending.
18. **Round 1 revision: version 2 and its log** (files 18). 39 findings were accepted as proposed and 10 in part; none was rejected outright.
    - Holding hands now costs the hand that held on.
    - Liam is on screen from episode 1.
    - Rosie owns her lie.
    - Smell and taste proofs were swapped for meters, so nothing echoes the mint.
    - Nine points were left open.
19. ***Seconds* critique round 2** (files 19). 52 findings, among them:
    - a live scale reading of an unseen visitor, which copied *The Catch*'s needle;
    - a taste test in disguise (Terry's marmalade);
    - a "spare" that looked like *The Catch*'s reserve bar;
    - a spot where the physics ran backwards: digging out the Hill should make the scales read heavier, not lighter.
20. **Round 2 revision: version 3 and its log** (files 20). All 52 were accepted, some in part or with a different fix, and every *Catch* echo was removed. The "spare" became "the bite", a brass tab with no light or gauge. The lying scale now comes from the neighbours digging under Grays. Ten choices are left for you, each with a default.
21. **My own check of version 3** (file 21). I searched it for banned words, *Catch* echoes and dystopia signs, and found none that reach the screen. I read all ten episodes, checked the sums for Liam's and Frank's deaths by hand, and listed the ten open choices plainly. It goes to the episode writers on its defaults.

22. **Episode 1, "Straight"** (files 22): draft, critique by another writer, final version and revision log. About 8,200 words.
23. **Episode 2, "The Assayer's Wife"** (files 23): the same four files. About 7,900 words.
24. **Episode 3, "Making Weight"** (files 24): the same four files. About 7,100 words.
25. **The machine restarted mid-run** (no file).
    - The restart stopped the episode run while episode 4 was being revised and episode 5 critiqued. Nothing already written was lost: the drafts and critiques were on disk, and the run's own record of its finished steps survived.
    - I restarted the run from that record, so finished steps are reused rather than redone.
    - The three finished episodes were copied here straight away, so another restart can't lose them.

26. **A second run of episodes 1 to 3, and Claude's last drafts** (files 26).
    - **My mistake:** in entry 25 I wrote that restarting the run would reuse finished steps rather than redo them. It didn't, because the three writing lanes don't keep the same order on a restart, so the saved record no longer matched.
    - So the run revised episodes 1 and 2 a second time (same drafts and critiques), critiqued and revised episode 3 a second time, and drafted episode 4 afresh.
    - Both versions of each are kept: the first run in files 22 to 24, the second in files 26.
    - The second-run versions are the ones later episodes build on, because they are what the next writers see.
    - Also kept: Claude's draft and critique of episode 4, and Claude's draft of episode 5.
27. **GLM takes over *Seconds*** (no file yet; its program is in `tools/`).
    - You said: "Set 3 of your own agents on the revision. And let GLM continue work on the other story."
    - I took that as a swap: three Claude agents now revise *The Long Places*, and GLM 5.3, at maximum thinking, continues *Seconds* from wherever each episode had reached.
    - GLM will revise Claude's episode 4 draft using Claude's critique; critique and revise Claude's episode 5 draft; draft, critique and revise episodes 6 to 10 itself; then check the whole season and fix what it finds, logging every change.
    - The Claude run on *Seconds* was stopped to keep to three Claude agents at once.
    - GLM gets the same brief, your rules, the notes on *The Catch* and plan version 3. It does not get the theory of explanation.

28. **GLM's servers failed, and the run was made sturdier** (programs in `tools/`).
    - GLM finished episodes 4, 5 and 6 (revised, each with a log).
    - Then its servers kept answering "internal network failure" on episode 7.
    - I raised the program's retries from 6 to 12 and wrapped it in a runner that restarts after a failure, skipping anything already finished. No finished work was lost.
29. **Revision rounds until only quibbles are left** (files to come).
    - You said: "Do more revision passes on both until the only critiques are just word placements or quibbles over the exact timing of events. You know, stuff that is better left to an audience analysis."
    - When GLM has finished all ten episodes and its season check, it runs rounds on the whole season: three GLM critics, a GLM verifier and, if real problems remain, a GLM plan and GLM revisers.
    - A finding is **substantive** if a careful reader or viewer would notice it and it weakens the story: a plot hole, a contradiction, a broken rule of yours, a character acting without cause, a scene with no job, sagging pace, confusion that serves nothing, a theme stated instead of shown.
    - A finding is a **quibble** if only an audience test could settle it: word choice or placement, sentence rhythm, the exact minute or day of an event when nothing depends on it, taste.
    - A separate verifier confirms each substantive finding, marks it a quibble, or rejects it. Only confirmed ones are fixed, and the rounds stop when a round confirms none.
    - Quibbles are recorded, not fixed.
    - At most six rounds. If the cap is reached, I'll say so.

30. **MiMo joins as a third opinion, and how many helpers can run at once** (programs in `tools/`).
    - You asked me to find a use for MiMo (MiMo v2.6 Pro, Xiaomi's AI model), and how many agents I can run at once, since MiMo and GLM can each run 5.
    - **How many at once:** my own Claude helpers stay within your limit of three (my workflow tool runs at most two at a time on this machine). GLM and MiMo run on their makers' computers, so five of each at once costs this machine almost nothing, and the programs use up to five.
    - **What changed in GLM's rounds on *Seconds*** (entry 29):
      - *The critics:* the three GLM critics are joined by a fourth, MiMo, reading the whole season with fresh eyes.
      - *The verifier:* it is now MiMo, not GLM, so GLM's work is never cleared by GLM alone.
      - *The revisers:* GLM revises up to five episodes at once instead of one at a time.
    - **The audience test at the end:** five simulated viewers with different tastes watch the finished season on paper, all at once, and MiMo writes the audience analysis. This is where the quibbles the rounds leave alone get settled.
    - **Tested:** MiMo's working address, its deep thinking, and a full-book critique of *The Long Places* (9 minutes 37 seconds). A garbled-letters slip in MiMo's replies was found and fixed (details in *The Long Places* project story, entry 21).
    - **Not yet tested on *Seconds*:** the rounds program with MiMo in it. It starts only after GLM finishes episodes 7 to 10, and GLM's servers are still failing on episode 7.

31. **I am the final authority, and Fable 5.1 reviews each finished revision once** (programs in `tools/`).
    - You said: "You are the final authority. Not any of the agents." And: "When a full revision has been written, get Fable 5.1 on Xhigh effort to do a single review on that one document. Nothing else. And only when a revision has been completed."
    - **What changed in GLM's rounds:**
      - *Before:* MiMo's verifier decided on its own what GLM fixed, and the rounds ran unattended.
      - *Now:* the program does one step and stops.
        1. *Review:* four critics read the season, and MiMo's verifier gives advice.
        2. *Ruling:* I check the findings against the season and write a ruling: what is real and must be fixed, and what is overruled.
        3. *Revision:* GLM plans and revises exactly what the ruling orders.
      - Only I can declare the season finished.
    - **Fable 5.1:** it gives one review, at extra-high effort, of each finished full version of the season, joined into one document, and does nothing else.
      - The first will be GLM's completed season, once all ten episodes and the whole-season check are done. A watcher tells me the moment that document exists.
      - After that, Fable reviews each round's revision once it is complete.
    - **Tested:** a practice run of the new step-by-step program, with stand-in answers instead of real GLM and MiMo calls. It reviewed, waited for my ruling, changed only the episode my ruling named, reviewed the result, and stopped when I ruled it done.
    - **Not yet run for real:** GLM's servers are still failing on episode 7.

32. **GLM finished the season** (files 32).
    - GLM's servers recovered after about 40 minutes of failures on episode 7. The run picked up where it stopped, and no finished work was lost.
    - **What GLM did:**
      - revised Claude's episode 4 draft;
      - critiqued and revised Claude's episode 5 draft;
      - drafted, critiqued and revised episodes 6 to 10, each critique a separate call that had not written the draft;
      - read all ten episodes as one season.
      Each episode took GLM about 30 to 40 minutes of thinking and writing.
    - **GLM's whole-season check found 18 problems.** One example: in episode 4 we see Danny take about ten tubs of food, and the next morning Maggie says "twenty-odd". It gave each problem the smallest fix. Episodes 1 to 3 needed none. Episodes 4 to 10 were fixed, and every change is logged.
    - **I checked that nothing was cut short.** Every fixed episode is within a few dozen words of its earlier length and ends with its "Plants and payoffs" list.
    - **The whole season is about 74,000 words**, saved as one document (file 32). This is the first finished full version, so Fable 5.1 is now giving it its single review.
    - At the same time, GLM's first revision round has started on its own: three GLM critics, a MiMo critic and MiMo's advice. It will stop and wait for my ruling.
    - **Not yet read by me:** the new episodes themselves. I'll read the passages at stake in each finding when I rule, as I have for *The Long Places*.

33. **Fable's single review of the finished season** (file 33): "a complete, well-built season that keeps every one of the owner's rules and needs only a continuity pass, not a rewrite", with 7 substantive findings, all at the level of a line or a number, and 11 quibbles.

34. **Round 1: four critiques, MiMo's advice, and my ruling** (files 34).
    - **The critics:** three GLM critics, each through one lens, and MiMo with fresh eyes.
    - **A setback, fixed:** MiMo's first try at advice was blocked by its maker's safety filter. The answer read "The request was rejected because it was considered high risk", probably because the season is about a family of thieves. The program wrongly took that sentence for real advice.
      - I changed both programs so a blocked answer counts as a failure.
      - MiMo now gets up to three tries, with a note that this is fiction under editorial review. If it still refuses, GLM gives the advice instead, and a note records that.
      - I tested this with a stand-in MiMo that always refuses.
      - The second real try went through first time: MiMo's advice was 11 real problems.
    - **I checked every finding I ruled on against the script myself**, quotation by quotation.
    - **My ruling: fix 18, and correct 3 slips of wording.** Every fix is a line, a clause or one short exchange; no new scenes. The groups:
      - *Breaches of the plan's rules* (4):
        - A "cylinder" behind the TV scientist; the plan bans oxygen cylinders as an echo of *The Catch*.
        - The weighbridge printer chattering live as Ray vanishes; the plan bans any instrument reacting live to an unseen crosser.
        - Terry crossing in the finale with no rig on him.
        - Rosie holding a breath she never took.
      - *Who knows what* (3): Tess quoting a boast of Danny's she never heard, Rosie telling the family what only Maggie told Tess, and Tess quoting a line Maggie never said.
      - *The season's own numbers* (3): Lee's weights breaking the kilos-to-seconds rule; Tess offering a ten-second cure to two people who can't stay in the black ten seconds; and an investigator misdescribing the raid we watched.
      - *Rules said and then broken without a word* (3): Shaun's second trip against "never go back twice"; Rosie skipped when Peg tests everyone who crossed; and the twenty-year law for stepping out, never charged.
      - *Plants and payoffs* (5): why Rosie can't fire her field in the sea, now planted in episode 1; Tess's 61.7 reading, now used; Rosie's secret that she taught Liam to starve, now said; the unmarked two-week gap, now captioned; and a line about a step five hours in the future, now put in the future.
    - **Where I overruled:**
      - *People 1, Aoife "fridged":* the brief's craft notes do say "no fridging", but Aoife is built as a person through her absence, and her death drives her mother's story, not a man's.
      - *Fable's "tingle came early" point* (Fable 6): left, because the plan intends that clue.
      - *Most of the people critic's other points:* left, because they would add material rather than mend a fault.
    - **One change I made myself, to the plan:** the episodes lean on the tingle starting about two seconds before a crosser's time runs out, and the plan never declared it. Your rule is that every invented rule is declared once, so I added those words in two places (file 34, before and after).
    - **Now:** GLM is planning and revising to my ruling. When it finishes, Fable reviews the revised season once, and round 2's critics start.

35. **Round 1's fixes made by GLM** (files 35).
    - GLM wrote a plan from my ruling and revised the seven episodes it touched (1, 2, 6, 7, 8, 9, 10), five at a time. Each took it between about 1 and 6 minutes.
    - **I checked every change word by word against the earlier season.** All 18 fixes and the 3 corrections were made as ordered. Among them:
      - Lee's weights now run from 64 down to 52 kilos in February, which gives him 9.6 seconds by the rule.
      - Danny's boast now happens at the family table, with Tess there.
      - Terry is buckled into his rig at the fence.
      - The cylinder and the live printer are gone.
      - Rosie says, at last: "Nan put the plate in front of him. I'm the one taught him to be hungry for it."
    - **GLM also changed three small things I did not order,** all harmless: "set into the lino" became "set flush in the lino", "draws out the painting" became "draws the painting out", and "he is falling" became "he's falling".
    - **GLM added two small things to make the fixes work:**
      - In episode 7, a history for Aoife's six-second vault ("October '19. The Mynors run. Six and a quarter"), so Tess's "you said" is true.
      - In episode 10, a two-line lead-in to Rosie's confession.
      Both fit the season.
    - **Now:** Fable is giving the revised season its single review, and GLM's round 2 critics are reading it.

36. **Round 2: Fable's review, four critiques, MiMo's advice and my ruling** (files 36).
    - **Fable's single review of the season after round 1:** "nearly finished — a complete, coherent, well-made season that keeps every owner rule", with 4 substantive findings and 18 quibbles.
    - **MiMo's advice:** 9 real problems. This time it went through first try.
    - **My checks:** I tested each claim against the script and the plan. Six of MiMo's nine held up, and three did not:
      - *Ray's "59.0" page "never fires":* it does. The audience sees the same weight on Joe's ticket in episode 6, and again in episode 9.
      - *Kieran's graph is "incoherent":* it isn't. The wobble starts after the April quake chips the check weight, and episode 9 names its cause.
      - *The plan says "three bodies" at the depot:* it never does.
    - **My ruling: fix 9**, each a line, a clause or a short exchange. For example:
      - "It's still printing" becomes "It printed all night". Your plan bans any instrument reacting live to an unseen body, as an echo of *The Catch*.
      - Joe no longer "hears" something land from inside the black, where no sound crosses.
      - Maggie's graph no longer marks "nothing happened" with the same tick as "came back straight".
      - The ferry timetable is no longer in Maggie's bag and Tess's coat at once.
      - Maggie now says why she sent her invitation through the Marlows' safe: she rang the house once and got a dial tone.
      - Rosie now owns what her lie cost: "Something took hold of me. That's Con."
    - **A mistake of mine, corrected:** my round-1 ruling kept Lee's job at "nine and a half seconds". That beats Rosie's 9.4, which the season toasts as "the longest job a Marlow's ever done". Fable caught it, and Lee's job is now a nine, with his weights adjusted to match the rule.
    - **One change I made myself, to the plan:** the plan said a weigh-wall feels a body within four metres, but it also has the Mayfair wall log Joe, six metres away. That contradiction was in the plan itself. I corrected it to ten metres, and episode 3's line will match.
    - **Left for the audience test:** Peg and Tess never speak after Tess is put out. Their reconciliation is shown in what they do at the station. Whether it also needs words is a matter of taste.
    - **The trend:** round 1 had 18 fixes, round 2 has 9. GLM is making them now.

## Next step

When GLM finishes the season, have Fable review it and rule on round 1's findings myself. After each round, rule again. When I rule that only quibbles remain, run MiMo's audience test on the final season, add every episode, critique, verification, plan and log here with the audience analysis, and read the seam between episodes 3 and 4.
