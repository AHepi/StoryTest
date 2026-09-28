# 38 Findings - what the revision rounds say about the process

This is the second half of your request (entry 37): whether the data from the rounds on *The Long Places* and *Seconds* (file 37, `iteration-data/`) can improve the process. **The short answer is yes, in six places, each a proposed change to how stage 08 (critique) or stage 09 (revision) works.** One of the six rests on one case, and one cannot yet tell its two explanations apart.

**None of them has been made.** Changing a stage's contract changes what the workshop says. That goes through the `error-correction` skill, with a reviewer who did not make the change (`CLAUDE.md`, rule 1; question S15). So each proposal below is for you to choose, and then for that process to carry out.

**How each proposal is marked.** The marks are the `hard-to-vary` skill's, in its sense. It is "a way of criticising, not a truth-meter".
- A proposal is ***held*** when a job it does is named and taking it away would lose that job.
- It is ***held if*** it holds only if a doubtful input holds, such as your aim or an untested fact.
- ***Loose*** marks a part that a near neighbour would do as well (for example "two rounds" where "three" would serve).
- ***Unknown*** marks what no test here has settled, with the missing test named.
- ***Two routes*** means two explanations the data cannot yet tell apart.

For each proposal:
- the error it answers, with the rows of `iteration-data/` that show it;
- what in stages 08 and 09 already does part of the job;
- what it would add in cost;
- its mark.

## What the data can and cannot show

- **One run per story, and no comparison run.** Nothing was run twice under different rules.
- **The two stories differ in many things at once.** They had different critic models (Claude, GLM), different checkers (Claude; MiMo, which judged its own critiques in rounds 1 to 6), different revisers (Claude making exact edits; GLM rewriting whole episodes), and different forms and lengths. So no difference between them can be put down to one of these alone.
- **A checker's verdict is advice, not the truth.** The main session re-read and sometimes overruled it. The readers in the audience tests are simulated.
- **The stories ran outside the stages.** The rounds had parts the stages lack: a bin of quibbles held for an audience test at the end, a separate checker, and a ruling by the lead. So the findings carry over to the stages by analogy, not directly.
- **The error table is the main session's own record of its own errors.** It holds only what was logged, and the first version of it was wrong about four rows (file 37).
- **Only the revision rounds are recorded.** The iterations before them are not (file 37).

## 1. Check that each accepted change is really in the new version

**The error.** In *Seconds* round 7, a ruling ordered a line changed "wherever it repeats". The reviser missed one repeat, and the main session's word-by-word check did not notice (`errors.csv`, *Seconds* entry 52). The check compared what had changed against the order. It never asked whether everything ordered had changed.

That story branch's entry 52 then adopted the missing half ("From now on I check both"), and entry 53 used it.

**What already does part of the job.** Stage 09's revision log asks each row for "What changed, and where … so the writer can find each change in the new version" (its reference, section 1, item 3). On the changes themselves, its Verify checks only "the new version differs from the old only where the log says". That compares with the reviser's own log, not with what was ordered.

**The proposal.** Stage 09's Verify also opens each place the log names and confirms the change is there. For an order of the form "every place where X", it searches the new version for X and shows the search.

**Cost.** One more check by whoever verifies, and no extra agent.

**Mark:** *held*, by the job of catching an ordered change that was not made, on one case. *Loose*: whether "show the search" or "point to each place" is the better form.

(*The Long Places* round 9's missed sentences, entry 49, are not a second case. That pass worked by judgement, and the sentences were never listed.)

## 2. Have someone who did not write it read the reviser's own new wording against the whole work, before it goes in

**The error.** Ten rows of `errors.csv` are faults the main session put in through the words it ordered:
- **Five "ruling wording" rows**, where the ordered wording was itself wrong. Examples: "nine and a half seconds", which beat the record the season toasts; "I never felt a thing"; "twenty-six years".
- **Five "a fix made a fault" rows**, where a fix was right in its own place and broke something elsewhere. Examples: a handprint "beside" the old one; a doorway in the ceiling someone "bends to"; a witness statement that lost its noun.

**When they were caught:**
- two within their own round: *The Long Places* entries 30 and 44;
- three by the next round's review;
- five two or more rounds later.

**The two cases where someone read the wording before the revision:**
- **A catch.** In *The Long Places* round 4, the planner flagged three slips in the ruling's wording while planning (entry 30). Nothing stopped the revision to act on it, so they went in and were put right in the next ruling (entry 31).
- **A miss, and a wording that kept a lost noun.** In round 8, the planner defended "twenty-six years", which the checker caught after the revision (entry 44). In round 4, the ruling's own wording dropped a noun ("No instruments deployed." became "None of mine deployed."), and the planner's suggested wording, "None deployed by me", kept that loss (entry 38's row).

**What already does part of the job.** The workshop's brief check (the error-correction skill's `reviews-and-briefs.md`, section 5) looks at a brief's credits, readings and pointers. It does not check whether a brief's new facts agree with the work, and the rounds did not run it.

**The proposal.** In stage 09, any wording the reviser writes itself, rather than moving or cutting, is read against the whole work by someone who did not write it. That covers every number, name, date and "who knows what". Anything found is put right before any reviser starts.

**Cost.** One reader per round: one agent, within your limit of two at a time.

**Mark:** *held if* a reader at that point catches most such faults. The record has one catch and one miss. The test would be to give a fresh reader the ten orders with the text as it stood, and count. That is *unknown* until run. Nine of the ten rows are in the proposal's scope. The witness statement's lost noun came from a rewording that cut words, which the proposal leaves out.

## 3. Do not hold raised points for an audience test at the very end

**The error, restated after review.** The first version of this file said the audience tests found faults "every critic missed". That was wrong: each of the four rows had faults raised during the rounds (file 37). On *Seconds*, five of the eight kinds of slip were raised; a keyword search found no earlier mention of the other three (the uncle called "dad", the name never introduced, and the explanation that lost all five viewers).
- **Raised as quibbles and held for the audience test:**
  - the grandmother's clock (round 6);
  - "Aye" in Essex mouths (from round 2 on);
  - the rule used before it was taught (rounds 2 and 6);
  - the shared voice (Fable, from round 2 on; left open in rounds 3, 4, 6 and 7).
- **Raised by Fable and left as they were:** "two years for seven" (round 5) and the June "birthday boy" (round 7).
- **Confirmed, fixed only in part, then held:** Nilay never asking Emre to come home. It was confirmed in round 1, fixed then only for the mother, and raised again as a quibble in round 3.

The readers then named several of these among what bothered them most: the voice, which all five named, and the "Aye"s, which all five noticed. They passed over others, such as the fine arithmetic the last rounds spent their time on.

**What already does part of the job.** The stages have no bin of quibbles to hold, because stage 09 answers every finding, accepted or rejected. A stage 09 would have had to decide each of these points when it was raised, though it could have rejected them.

**The proposal:**
- **(a)** A point raised by two critics, or in two rounds, goes to you as a choice at once, not to a bin. This joins 4(b).
- **(b)** Optionally, a reader panel on an early version, to sort which held points readers notice.

**Cost.** (a) costs nothing extra. (b) is a panel: 21 to 23 minutes and about 1 to 1.3 million tokens in the tests (`runs.csv`), with six agents. The tests already ran two at a time, so these figures stand under your limit.

**Mark:**
- (a) is *held* by the job of stopping raised points being put off. It is *held if* you would rather be asked than have the lead settle them, and its "two" is *loose*.
- (b) is *held if* your aim is to settle quibbles while they are cheap to fix. Whether an early panel sorts them as the final ones did is *unknown*. The test is to run one on an early version and compare.
- The first version's reason for (b), that critics cannot see what readers see, did not survive the review for most of the faults: the record fits "the critics saw them, and the quibble rule held them back" better. The three *Seconds* slips not found raised are the only basis left for it, and a small one; the search for them was by keyword, so an earlier mention in other words may have been missed.
- Its guard, that readers must quote the last chapter, would not have caught MiMo's thin readings. MiMo's readers had the whole book and quoted it, but answered in 2,347 to 7,107 tokens. A guard on the depth of an answer is untested.

## 4. Stop by the kind of finding, not by a count

**The pattern.**
- **On *The Long Places*, the checker's confirmed findings fell fast:** 7, 6, 3, 2, 2, 1, 0. On *Seconds* they did not: 11, 9, 6, 0, 5, 8, 1.
- **Fable's fresh full reading found substantive points every time:** 19 reviews, none empty. *The Long Places*: 3, 4, 3, 4, 2, 3, 1, 2, 1, 1. *Seconds*: 7, 4, 6, 4, 5, 2, 4, 2, 2.
- **Several later fixes mended earlier ones** (the five "a fix made a fault" rows).

What ended the rounds was:
- a cap on rounds;
- one confirmation round;
- after the last review, fixing only what that round broke, or a plain contradiction.

**What already does part of the job.** Stage 08 already limits rounds to the number `_config/writer.md` sets (question 11), "then the result goes to the writer", and stage 09's review stop says the same.

**The proposal.**
- **(a)** The only new part is the rule for after the last review: fix only what the last round broke, or a plain contradiction, and put everything else to the writer as a choice.
- **(b)** A point an independent reviewer has raised in two rounds, which the ruling left open, goes to the writer at once as a question. The cases:
  - the shared voice, raised from round 2 and left open four times;
  - the reunion, raised in rounds 1 and 3;
  - the seven reversed calls from which the rounds drew their own rules: *The Long Places* entry 29, "when a point keeps coming back and costs a clause to settle, settle it the first time", and *Seconds* entry 38, "a point that keeps coming back and costs a line gets settled".

**Cost.** None beyond the writer's time to answer.

**Mark:**
- (a) is *held if* your aim is a finished work rather than a flawless one. A flawless one never arrived in 19 fresh reviews.
- (b) is *held* by the job of stopping a repeated point being put off, and *held if* you want to be asked rather than have the lead settle it. "Two rounds" is *loose*. The rival rule is entry 29's own, which settles small points the first time without asking.

## 5. Keep each critic's record, and replace one whose findings are mostly judged wrong

**The pattern** (`findings.csv`; see file 37 for what the counts measure):
- **MiMo as a critic of *The Long Places*:** 1 confirmed and 26 wrong, out of 33. Its one confirmed finding came in round 1, shared with the Claude story critic. It repeated one wrong point, that Halden is not frightening, in six rounds.
- **MiMo on *Seconds*:** 9 confirmed out of 32. It was judging itself in rounds 1 to 6. Its first critique found the two worst places where the season broke your rules, which no other critic found (story branch, entry 46).
- **MiMo's cost:** a critique took a median of 13.3 minutes on *The Long Places* and 31.0 on *Seconds*. Its safety filter blocked it three times (entry 46; the call log flags one).

**What already does part of the job.** Nothing records a critic's record across rounds.

**The proposal.** Each round's project-log entry records each critic's confirmed, quibble and wrong counts from the checker. A critic more than half of whose findings the checker has judged wrong, after two rounds, is replaced. A quibble does not count against it: counted by confirmed findings alone, every critic in the data would be replaced, since none had half its findings confirmed (the best was *The Long Places* story critic, 15 of 33).

**Cost.** A count, and no extra agent.

**Mark:**
- *held*, by the job of replacing a critic with a poor record. On *The Long Places*, dropping MiMo after round 2 would have lost no confirmed finding.
- *held if* the checker is independent of the critic, which it was not for MiMo on *Seconds*.
- "After two rounds" and "more than half" are *loose*: MiMo on *The Long Places* had 3 of 5 judged wrong after round 1 and 6 of 9 after round 2, so after one round or three, and at a third or a half, it is dropped just the same. No other critic comes near: the most any other had judged wrong was MiMo on *Seconds*, 5 of 32.
- Keeping a fresh-eyes critic from another model in round 1 rests on one case: MiMo's first *Seconds* critique.

## 6. Write local changes as exact edits, applied by a script

**The pattern.**
- **GLM, revising *Seconds* by rewriting whole episodes,** made changes nobody ordered in seven revisions, including working notes and a placeholder line that leaked into the text (the "reviser discipline" rows).
- **Every *Long Places* round used exact edits** (a piece of text to find, and its replacement), each checked to match exactly one place, and was revised by Claude.
- **Changes nobody ordered found there:** none, apart from round 8's two quotation marks, which the reviser logged.
- **What found GLM's changes** was the main session's word-by-word check against its ruling. That is a check like stage 09's "only the logged changes", but made against the order, not the reviser's log. A change the reviser logs with a reason would pass stage 09's version.

**What already does part of the job.** Stage 09's "only the logged changes" check, with that gap.

**The proposal.** In stage 09, an accepted change that alters words in place is written as an exact edit, and made by a script that refuses an edit matching anything but one place. The new version is compared with the order, not only with the reviser's log.

**Cost.** A script, and no extra agent.

**Mark:** *unknown*, with *two routes*. The only contrast is GLM rewriting against Claude making exact edits, so the method and the model are not told apart. The test is the same model revising one round each way.

## Also noted, with no change proposed

- **The limit on Claude helpers stopped a Fable review twice** (`errors.csv`), and you have since set a limit of two helpers at a time. Each proposal's cost is given above against that limit.
- **Your round 9 used far fewer helpers than a full round, though it is not like for like:**
  - round 9: two runs, 4 agents (three drafters stopped at once, then Fable), about 19 minutes and 0.41 million tokens;
  - a full round: 11 agents, a median of 73 minutes, and 1.6 to 1.9 million tokens;
  - round 9 had no critics, since your critique served;
  - the main session's own tokens are in no record.
- **Your critique of *The Long Places* found again a point critics had raised in rounds 1 and 3,** which the round-1 ruling fixed only in part: Nilay never asks Emre to come home.
  - Your critique came after seven rounds of critics and nine of Fable's reviews.
  - Your critique asks "Let her ask him to come". Tying that to the story-critique method's choice test is the workshop's reading (from the round-9 changes, file 48), not something your critique says.
  - Stage 08 already makes `story-critique` lead a whole-work critique when your account has it, and the rounds first used it in round 9.
  - This workshop's `README.md` still says `story-critique` is "not in this repository". It is now committed on the story branch (`.claude/skills/story-critique/`), exactly as you supplied it. Bringing it here goes through the `add-source` skill, with a review.

## Checks run on these notes

- **Figures.** Every figure comes from `iteration-data/` or from the story-branch entries cited, counted from the tables. The figures first found by the review I checked myself before committing:
  - the timing of the ten wording faults, row by row in `errors.csv`;
  - MiMo's one confirmed finding on *The Long Places* (`findings.csv`, row 8, round 1);
  - the split medians, by hand from `model-calls.csv`.
- **Story-branch entries.** Every entry cited was read before being cited.
- **What already does each job.** Stages 08 and 09 were read: `stages/08-critique/CONTEXT.md` and its reference, section 1; `stages/09-revision/CONTEXT.md` and its reference, section 1.
- **An independent review** (the workshop's `theory-checker` role) read the first version and did not pass it. This version answers its findings, and one narrow look at the changes follows before commit.
- **Not checked:**
  - whether each proposal would really have caught its errors. That is argued from the record, not re-run: the *unknown* marks above name the tests;
  - the proposals against the kept cases.
