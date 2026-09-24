# Kept cases

Short story problems, each with what a good answer **must** and **must not** do, written before any answer existed. They are rerun after a skill changes, to show that the change broke nothing the workshop already got right, and they are aimed at errors the workshop really made. (A case is not a test of taste: each item rests on a line of an owner theory, or, where no theory speaks, on a named past error.)

**Agents that write or change the skills never see this folder.** A skill that carries a case's story or its answer turns the case into an answer key. A brief made from a failed case gives the defect, not the case's must-list. The `use-tester` agent checks changed skill text against the cases' titles for the same story or conclusion.

## The cases

| File | Aimed at | Skills it tests |
|---|---|---|
| `01-danger-the-audience-sees.md` | a book rule that would cut a reveal the audience sees and the characters do not | plot |
| `02-ending-told-in-the-first-line.md` | saying that knowing the ending removes uncertainty | plot, character |
| `03-villain-with-four-blank-levers.md` | a villain judged a function for missing levers; the ladder of care turned round | character |
| `04-lead-shot-in-chapter-three.md` | calling one early death a mistake that kills care | genre, plot |
| `05-strike-day-that-moves-no-plot.md` | cutting a scene of the world at its own business | story-world, plot |
| `06-rationed-light-and-one-night.md` | calling a world's standing condition the breach | plot, genre |
| `07-invented-names-unexplained.md` | demanding a guide for every invented name | story-world, genre |
| `08-crew-that-dies-one-by-one.md` | saying the deaths build the audience's care | character, genre |
| `09-cheated-or-unsafe.md` | a cheat (a promise dropped) confused with a broken guarantee | genre, plot |
| `10-sound-scene-nothing-wrong.md` | inventing faults in a sound scene; stock notes | dialogue, character |
| `11-two-versions-which-is-better.md` | assuming which draft came first; a verdict with no aim named. **Expected to fail** until a method for comparing two drafts exists | plot, dialogue |

Each case's "Aimed at" line names a past error by its number in the list at the end of `27 Corrections.md`.

## Running them

When: after a change to a skill, run the cases that test it; before a large change is called done, run them all. Session start, and the records check, say which skills have changed since their cases last ran.

1. **Start clean.** Commit your work, so `git status` shows nothing, and note the commit (`git rev-parse --short HEAD`).
2. **Make the writer-only copies.** For each case, the answering agent gets only the part under "What the writer brings", never the must-lists. Copy that part of each case to a scratch folder outside the repository.
3. **Answer.** For each case, a fresh agent that has not seen this folder answers the writer as a Claude Code session in this repository would: it reads the skills' descriptions, chooses, and follows the chosen skill's steps. It also returns a stall report: every place it stalled, improvised, found two rules at odds, or met a record that looked stale.
4. **Grade.** The `case-grader` agent grades each answer against its case. It never reads the skills.
5. **Test the grader.** Give it at least one planted wrong answer in each batch (an answer that plainly breaks a must-not). It must fail it. If it does not, the grades from that batch cannot be relied on.
6. **Record** the run in `runs.md` as it came: the commit, which cases passed, failed or were unclear, the planted answers' grades, a line on the stalls, and the line of skill fingerprints. Put the full answers, grades and stall reports in `runs/`, one file per case (for example `runs/2026-10-01-run-2/03.md`), so no record grows past the size limit for text files. A failure is never replaced by a later pass; a rerun is added below it.
7. **Work through what it found.** A failed case goes through the error-correction loop: the skill, the case and the grading are rival guesses about where the fault is. Stalls that repeat, or that name a skill step, are signs.

`run-kept-cases.js` is the workflow script that did steps 3 to 5 for the first run. It is kept so the run can be repeated in the same way.

**The skill fingerprint line** at the end of each run in `runs.md` is written like this, one short code per skill folder:

`<!-- skill fingerprints: character=... dialogue=... genre=... hard-to-vary=... plot=... story-world=... -->`

The codes are made by the same method the records check uses: `folder_fingerprint` in `.claude/skills/error-correction/scripts/check_records.py`. After a full run, `check_records.py --fingerprints` prints the whole line for the commit you tested. After a change that alters no meaning, staged but not yet committed, `check_records.py --fingerprints <skill>` prints a line that updates only that skill, and only if its cases were up to date before; every other skill keeps its code from the last run, so a skill still owed a rerun stays listed. If the skill was already owed a rerun, it refuses: write the runs.md line without a fingerprint line. The error-correction and add-source skills have no kept cases and need no line.

## Adding a case

Write it before running anything on it. Give it: what the writer brings (under 250 words, invented, not from any skill's example or the owner's draft under test); must and must-not lists of two to five items each, decidable by a grader who quotes the answer; the grounds for each item; and the open points a grader must not grade (owner questions still open). A new or changed case needs a review receipt like any other change. Never change a case and the skill it tests in the same commit, and never change a case to make a skill pass: a changed case is a new case.
