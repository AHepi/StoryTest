# 37 Record - the revision rounds of The Long Places and Seconds

You asked: "take the data generated from all these iterations and record them. Then figure out whether they can be used to improve the process. But not the branch you're currently using. The one that was built specifically as an actual workflow." This file is the record. File 38 is the second half: what the record says about the process.

**What "these iterations" is taken to mean here.** I read it as the revision rounds of the two stories, which is my reading. The other reading takes in the iterations before those rounds too, and they are not recorded here:
- *The Long Places*' GLM pipeline (that branch's files 03 to 18);
- the first season plan's critique rounds (files 04 to 06);
- *Seconds*' plan critique rounds (files 17 to 21);
- the episode critiques (files 22 to 26).

They can be added in the same form.

## What was run, and where

Two stories were written and revised on branch `claude/story-questioning-theme-ehokf0`, outside this workshop's stages, which have not yet been run on any story.
- ***The Long Places*** is a novella of about 46,000 words. GLM 5.3 wrote it first, and Claude agents revised it.
- ***Seconds*** is a ten-episode television season. Claude's writers drafted episodes 1 to 5. GLM revised episodes 4 and 5 and wrote 6 to 10 (that branch's *Seconds* entries 26, 27 and 32).

**A round** ran:
- **Critics:** three critics, each reading the whole work through one lens (story and rules; people and meaning; continuity), and a fourth, MiMo, a model from another company.
- **A checker,** which advised on findings (*confirmed*, *quibble* or *wrong*).
- **One review by Fable 5.1** of the whole revision.
- **A ruling** by the main Claude session, saying what gets fixed and in what words.
- **Revisers** who made the changes, and the main session's word-by-word check of them.

**Who played each part:**

| Part | *The Long Places* | *Seconds* |
|---|---|---|
| Critics | Claude | GLM |
| Checker | Claude | MiMo in rounds 1 to 6, so MiMo also judged its own critiques; Claude in round 7 |
| Revisers | three Claude revisers, making exact find-and-replace edits from a plan | GLM, rewriting whole episodes |

**The rounds' own rule** was that quibbles are recorded, not fixed, and left for an audience test at the end. That is that branch's entries 20 (*The Long Places*) and 29 (*Seconds*), after your request that the rounds stop at what is "better left to an audience analysis". An audience test means five simulated readers with different tastes who read the whole work and say how it played for them.

**How each story ended:**
- ***The Long Places*:** seven rounds; copyedits and Fable's single review of the finished book; two audience tests (MiMo's readers, then Claude's); your three changes (round 8); your own critique and one focused revision (round 9).
- ***Seconds*:** seven rounds. Round 7 still confirmed one finding and Fable found four, so five mends and a wrong word followed. Then Fable's review of the finished season, one audience test, sixteen last mends, and a last review by Fable.

**How this maps onto the stages.** This workshop's `stages/how-stages-work.md`, section 12, maps the season folder's critiques onto stage 08 and its revision logs onto stage 09. By the same reading, which is mine and not written there:
- the rounds' critics are stage 08;
- the checker, the ruling and the revisions are stage 09, whose job is to "answer every finding".

The stages have no bin of quibbles held for an audience test: stage 09 answers every finding.

## What is recorded

All of it is in `iteration-data/`. Each table is plain text with commas between columns, so it opens in any spreadsheet.

| File | One row per | Rows | Made by |
|---|---|---|---|
| `findings.csv` | finding a checker weighed: story, round, the checker, every critic the checker's table names for it, the verdict, the finding in plain words (cut at 160 characters), and the file it came from | 297 | `record_iteration_data.py`, from the checker files committed on the story branch |
| `runs.csv` | workflow run (a run of Claude helper agents): when it ended, minutes, agents, tokens, and whether it finished or was stopped | 35 | the same script, from this session's run records, which Claude Code keeps outside the repository |
| `model-calls.csv` | call to an outside model, from the two call logs (GLM's log also holds 14 of MiMo's calls, labelled as MiMo's): its label, minutes and tokens | 136 | the same script, from those logs in this session's working folder |
| `rounds.csv` | round of each story: what was reviewed, how many findings the checker confirmed, how many fixes the ruling ordered, and Fable's substantive and quibble counts | 19 | by hand, from the rulings and project-story entries named in each row |
| `audience.csv` | reader in each audience test: their taste and score | 15 | by hand, from the three analyses named in each row |
| `errors.csv` | logged error in the process: who made it, what went wrong, who caught it, and its kind. A row can hold several slips of one kind from one entry; for example, one row is seven leftovers of cuts | 34 | by hand, from the story branch's project-story entries named in each row |

**Only `findings.csv` can be made again** once this session ends. The run records and the call logs lived in this session's folders, and what they held is now in `runs.csv` and `model-calls.csv`. Given only the story branch, the script remakes `findings.csv` alone.

Round 8 of *The Long Places* used a must-fix list instead of a table, so the script reads nothing from it and says so.

## The record, in short

**The rounds**, from `rounds.csv`:

| | Findings the checker confirmed | Fixes ordered | Fable's substantive findings |
|---|---|---|---|
| *The Long Places*, rounds 1 to 7 | 7, 6, 3, 2, 2, 1, 0 | 11, 8, 4, 5, 4, 4, then 4 copyedits | 3, 4, 3, 4, 2, 3, 1 |
| *The Long Places*, after the rounds | | | 2 (finished book), 1 (after your three changes), 1 (after your focused revision) |
| *Seconds*, rounds 1 to 7 | 11, 9, 6, 0, 5, 8, 1 | 18, 9, 11, 4, 8, 9, 5 | 7, 4, 6, 4, 5, 2, 4 |
| *Seconds*, after the rounds | | | 2 (finished season), 2 (mended season) |

**The critics, as the checkers judged them.** These are the findings each checker weighed, credited to every critic its table names, all rounds together, from `findings.csv`:

| Critic | *The Long Places* (Claude critics, Claude checker) | *Seconds* (GLM critics, MiMo checker until round 7) |
|---|---|---|
| story and rules | 33 weighed: 15 confirmed, 17 quibble, 1 wrong | 50 weighed: 11 confirmed, 35 quibble, 4 wrong |
| people and meaning | 21 weighed: 6 confirmed, 14 quibble, 1 wrong | 74 weighed: 9 confirmed, 63 quibble, 2 wrong |
| continuity | 33 weighed: 12 confirmed, 21 quibble, 0 wrong | 62 weighed: 17 confirmed, 41 quibble, 4 wrong |
| MiMo | 33 weighed: 1 confirmed, 6 quibble, 26 wrong | 32 weighed: 9 confirmed, 18 quibble, 5 wrong |

**The two columns measure different things:**
- *The Long Places'* checker weighed only findings a critic marked substantive. Its cells, though, sometimes also name a critic that marked the same point a quibble, and the script credits that critic too. The reviewer's recount of the substantive marks alone:
  - story 30 (14 confirmed, 15 quibble, 1 wrong);
  - continuity 28 (11, 17, 0);
  - MiMo 31 (1, 4, 26);
  - people 21, unchanged.
- *Seconds'* checker, MiMo, also weighed findings the critics had marked quibble or not marked at all. In rounds 1 to 6 it judged its own critique.

**The audience tests** (`audience.csv`):
- *The Long Places*: MiMo's readers averaged 7.9, and Claude's readers, the same five people and questions, 7.0. MiMo's readers had the whole book and quoted its last chapter, but answered briefly.
- *Seconds*: Claude's readers averaged 8.4.

**The errors** (`errors.csv`, 34 rows):
- **The main session made 17 rows.** These were mostly wording it ordered in rulings, and fixes of its own that made a new fault.
- **GLM made 7**, as reviser: changes nobody ordered, including working notes that leaked into the text.
- **MiMo made 2**, both tooling: garbled letters, and its safety filter.
- **The cuts of round 8 left 2.**
- **Twice, the limit on Claude helpers stopped a Fable review.**
- **4 rows are faults in the stories that the audience tests or your critique named.** Each of the four had been raised during the rounds, all of it or in part:
  - the grandmother's clock was raised as a quibble in round 6;
  - the shared voice was raised by Fable from round 2 on, and the rulings left it open in rounds 3, 4, 6 and 7;
  - *Seconds'* slips: five of the eight kinds were raised. "Aye" was raised from round 2 on and the rule used before it was taught in rounds 2 and 6, both as quibbles; the pencil was confirmed in round 3; Fable named "two years for seven" in round 5 and the June "birthday boy" in round 7. A search by keyword found no earlier mention of the other three (the uncle called "dad", the name never introduced, and the explanation that lost all five viewers);
  - Nilay not asking Emre to come home was confirmed in round 1 and then fixed only for the mother.

  Apart from those three *Seconds* slips, they were held back as the rounds' rule said, not missed.
- **These rows are the main session's own record of its own errors**, drawn from its own logs. The first version of this table said the four above had been "missed by every critic"; the review of this change showed otherwise, and its second look showed that three of *Seconds'* slips were, as far as a keyword search can tell, never raised.

**The cost** (`runs.csv` and `model-calls.csv`; tokens as the workflow runtime reported them; the main session's own tokens are in no record here):

| Step | Minutes | Tokens, in millions | Agents |
|---|---|---|---|
| one *Long Places* round: three critics, the checker, Fable, the plan, three revisers, and two small agents that joined chapters and started MiMo (6 runs) | 58 to 78, median 73 | 1.64 to 1.88 | 11 |
| one Fable review on its own (10 runs) | 15 to 24, median 19 | 0.22 to 0.44 | 1 |
| one Claude audience panel (2 runs) | 21 to 23 | 0.98 to 1.30 | 6 |
| your round 9: three drafters stopped at once, then the main session alone, then Fable (2 runs) | about 19 | about 0.41 | 4 |
| a GLM critique of the whole season (21 calls) or of one episode (6 calls) | medians 16.1 and 11.2 | | |
| a GLM revision of one episode in a round (50 calls), or its first writing (7 calls) | medians 2.4 and 12.4 | | |
| a MiMo critique of *The Long Places* or of *Seconds* | medians 13.3 and 31.0 | | |
| a MiMo check (7 calls) | median 15.2, longest 36.7 | | |

Round 9 had no critics: your critique served instead.

**In all**, the 35 workflow runs took 1,642 minutes between them, overlapping, so this is not the time that passed, and about 33.7 million tokens. That total is not all revision rounds:
- 781 of those minutes and 12.4 million of those tokens went on other work: the season's design and plan, the first drafting of episodes, the first Claude revision of *The Long Places*, and this workshop's own review of its stages (entry 36);
- six runs were stopped before they finished. The last was stopped because you asked me to go light on helpers. I have not restated the reasons for the other five; they are in the story branch's logs.

`runs.csv` does not include the two Fable runs that failed at the usage limit, or GLM's failed attempts, and `model-calls.csv` has no calls from *The Long Places*' GLM phase.

## Checks run on these notes

- **The script ran.** `python3 iteration-data/record_iteration_data.py --story-branch claude/story-questioning-theme-ehokf0 --workflow-records <this session's workflow records> --glm-log <GLM's call log> --mimo-log <MiMo's call log>` printed "findings.csv: 297 rows", "runs.csv: 35 rows" and "model-calls.csv: 136 rows", and the per-round and per-critic counts above.
  - The first run read "Cont. 3" (one checker's short name for the continuity critic) as a critic of its own. The script now reads it as continuity.
  - A separate count printed "rows with an unusual verdict or critic: 0".
- **The per-round counts against the logs.** The confirmed counts the script read match those logged in 13 of 14 rounds. In *Seconds* round 6, MiMo's table shows 7 confirmed rows but its numbered list says 8, and the ruling used the list; `rounds.csv` records both. This reads the same checker files twice, so it checks the reading, not the verdicts.
- **Fable's counts** in `rounds.csv` are as each ruling or project-story entry states them. Where a ruling does not state them, they come from Fable's own closing line in the run record.
- **An independent review** (the workshop's `theory-checker` role, one agent that made none of this) read the first version of this change.
  - Its verdict: "not passed", with 13 must-change, 17 should-change and 11 notes. Its report is kept with the review receipt.
  - It recounted the three script-made tables itself, read-only, and got the same rows.
  - It checked every row of `rounds.csv` and `audience.csv`, and every row of `errors.csv` against the entry it cites.
  - Its findings are answered in the receipt, one line each, and this file is rewritten from them.
  - I recounted by hand, from `runs.csv` and `model-calls.csv`, the figures taken from its report: the 781 minutes and 12.4 million tokens of other work; round 9's two runs; the medians split by task. All matched.
  - The substantive-only recount is the reviewer's. I checked the kind of cell it counts (for example round 1, row 13: "Story 10 (also Cont. 16 and MiMo 10, both marked QUIBBLE)") but did not redo it.
- **A second look** by the same reviewer, at the edits only: "passed after changes". It found all 30 earlier findings applied or answered, and 2 new must-change and 3 should-change findings, all applied, among them the three *Seconds* slips not found raised (above). I checked the two Fable quotes it cited on the story branch before accepting that one. Its report is kept with the receipt too.
- **Not run on the stages, and not rerun here:** the kept cases, since no skill or stage changed.
- **Not checked:**
  - that the token figures count each request once. This workshop's entry 35 found that one kind of session record counts a request two or three times; these figures come from the workflow runtime's own totals, a different record, not tested the same way;
  - whether each of *Seconds'* slips other than "Aye" was in GLM's first finished season (10 of the 11 "Aye"s were);
  - errors that nobody logged.
