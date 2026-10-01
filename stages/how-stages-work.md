# How the stages work

*Sources: Van Clief and McDermott, the Interpretable Context Methodology paper (registered in `sources/README.md`), in the workshop's own words; the workshop's own error-correction practice (`.claude/skills/error-correction/SKILL.md`); and the Fourth Direction season project's practice (brief, rival pitches, a plan, rounds of critique, revision logs, every version kept), as recorded on branch `claude/story-questioning-theme-ehokf0`. Every stage contract points here for the rules they all share, so each rule has one home. Every stage loads this whole file.*

Contents: 1 The five layers. 2 A run. 3 Review stops. 4 Versions and the handed-over copy. 5 Markers. 6 Verify. 7 Stale outputs. 8 Your edits, and when they should change a stage. 9 Helper agents. 10 What never goes in an output. 11 The project log, and the workshop's own records. 12 How the season work maps onto the stages.

## 1. The five layers

The paper's central idea: one agent can do a long piece of work well if, at each step, it reads only the files that step needs, in a set order. The folders decide what it reads. Five layers, from the most general to the most particular:

| Layer | What it holds | Where it lives here | Same for every run? |
|---|---|---|---|
| 0 | what this repository is, and where to look next | `CLAUDE.md` | yes |
| 1 | which stage or skill takes a request | `CONTEXT.md` at the top of the repository | yes |
| 2 | one stage's job: what it reads, does, writes and checks | each stage's `CONTEXT.md` (its *contract*) | yes |
| 3 | the rules and craft to follow | the owner's theories in `sources/`, the skills in `.claude/skills/`, each stage's `references/`, this file, and the writer's settings in `_config/` | yes, apart from `_config/`, which the writer changes whenever they like; everything else changes only through the workshop's own process |
| 4 | this run's own material | each stage's `output/<project>/` | no: every run makes its own |

Layer 3 is followed; Layer 4 is worked on. Keeping them in separate folders tells the agent which is which. (The paper's names for the two are *the factory* and *the product*: what is prepared once and used again, and what each run makes new.) One file sits between them: `stages/owner-edits.md` gains rows every run and is read as a record, as data about the writer's edits, not as a rule.

**One exception to reading only what a stage lists.** Several skills ask for passages of the owner theories to be read in full once per conversation before a first full run (for example `.claude/skills/plot/SKILL.md` and `.claude/skills/genre/SKILL.md`, "Built on"). That rule wins over the paper's scoping: a stage that uses such a skill reads those passages in full the first time in a conversation, then only the passages its Inputs table names.

**A second exception: a reference that points into a book.** Some references say to use a list or a method from a craft book rather than restate it. The books are local copies in `sources/raw/`, which git ignores, so they are present in some sessions only. If the book is present, read the passage the reference names, as an input beyond the Inputs table, and never copy from it into an output (section 10). If it is absent, work from the reference's own description and the skills it names, and write "book not present" in the Verify section; that is not a pass.

## 2. A run

A *run* is one project going through the stages: a film, a novel, a season, a short story. Give it a short name in lower case with hyphens (`fourth-direction`). Each stage writes into its own `output/<project>/` folder, so several projects can run side by side without mixing.

For each stage, the agent:
1. reads the project log (section 11), to see where the run stands and which versions are current, then that stage's `CONTEXT.md`;
2. loads exactly the files and sections its Inputs table names, and no others, apart from the two exceptions in section 1;
3. compares each earlier output it reads with the copy that was handed over, and records any edits the writer made (section 8); a handed-over copy counts as part of the input the contract names, so it may be read even where the Inputs table does not list it;
4. works through its Process, in order;
5. writes its Outputs, with markers (section 5) and the Verify sections its contract names (section 6);
6. stops for review (section 3), and adds an entry to the project log.

The numbers give the usual order. The critique and revision stages (08 and 09) can be pointed at the output of any earlier stage, and usually are: the season project ran critique rounds on its plan, long before any episode existed. Which stage runs next is always your call at a review stop; nothing runs on to a later stage by itself.

## 3. Review stops

The paper calls these *review gates*. Here they are **review stops**, so they are never confused with the commit gate (the checks git runs before every commit).

After every stage the agent stops, names the files it wrote, and says what it is least sure of. You can then:
- **edit** any output in place and save it: the next stage starts from the file as you left it, your changes included;
- **go on** to the next stage;
- **rerun** this stage, with a note on what to change;
- **go back** to an earlier stage;
- **stop** the run.

The paper's practitioners said they changed most at the first stage, choosing what the work is about, and at the last, checking the result against what was decided earlier, and least in between *(their own reports, not measured)*. If the same holds here, most of your time will go on the brief and premise, and on the critique and revision rounds; nobody has measured it yet.

**A stop inside a stage.** Write the line `**Stop for review after this step.**` under any Process step in a contract, and the agent stops there, shows what it has, and waits. Take the line out when you no longer need it.

## 4. Versions and the handed-over copy

- **The agent never overwrites a file.** Each output file carries a version number: `premise-v1.md`, `premise-v2.md`. A new version is a new file; every earlier version is kept.
- **Which version a stage reads:** the highest number, unless the project log says otherwise.
- **Your edits are made in place**, in the file you were handed. To see what you changed, the agent needs the copy it handed over. If your settings (`_config/writer.md`, question 12) say story work is committed to git, the agent commits each file as it hands it over, and git holds that copy. Otherwise, including while question 12 has no answer, the agent saves an untouched copy in `output/<project>/handed-over/` when it hands the file over.
- **Keep each file under 100,000 bytes** (about 15,000 words). The workshop's checks refuse any larger text file, because that is how they catch a copied book. Split a long draft by act, episode or chapter.

## 5. Markers

A marker is a short note in square brackets at the end of a heading or a paragraph, saying which step of which contract, and which reference, produced that part:

`[from: 04 step 3; plot skill, structure-and-conflict.md §2]`

- It names the stage number and Process step, then the Layer 3 file and section that part rests on. Name the owner theory where the part rests on one (`gap-theory §2 principle 2`). Where a part rests on your own words, name the file (`brief-v2 rule 3`). Where it rests on nothing but the writer's own choice, write `[from: 04 step 3; own choice]`.
- It is not a footnote for readers; skip it when you read. It is there so that when something is wrong, the critique and revision stages can follow it back to the contract step or reference that produced it, and change that rather than only the output (section 8). The paper proposes something like this for tracing a fault back to its source; it did not build it, and the workshop's version is this plain one.
- A final draft can be cleaned of markers when it leaves the workshop; the versions kept in `output/` keep theirs.

## 6. Verify

Each output that a contract's Verify list names ends with a section headed `## Verify`. It lists each check, and for each: what was compared with what, and the result, one of *agrees*, *disagrees* (say where, and what was done), or *not run* (say why). Not run is never passed. The checks compare this stage's output with earlier stages' outputs and with the references, so that a fault is caught at the stage where it appears, before you review, not three stages later. This follows the paper's proposal for a Verify section in every contract, which it had not yet built.

The Verify section is the stage checking its own work for consistency. It is not a review: the workshop's rule is that nobody grades their own work, so judging whether the work is good belongs to the critique stage, run by an agent that did not write it (section 9).

## 7. Stale outputs

Each contract's Inputs table says which files the stage reads. So when one of those files changes, the stage's output may no longer fit it. Examples: you edit the premise after the characters are done; a craft skill's module changes; a revision round makes `plot-v2`. The agent then lists, in the project log, every later output that read the changed file, and marks each *stale*. A stale output is not wrong, but it cannot be relied on until its stage's Verify is run again against the new file, or the stage is rerun. A stage that read nothing that changed is left as it is. (The paper likens this to a compiler that rebuilds only what depends on a changed file.)

## 8. Your edits, and when they should change a stage

When you edit an output, there are two kinds of edit, and the paper's point is to tell them apart.
- **A change only you could make**: a detail from your own life, a line you hear and the workshop did not, a choice of taste. It belongs in the output, and nothing else needs to change.
- **An edit that points back to a stage**: you keep making the same kind of change to the same stage's output, run after run (always making one character less articulate, always moving a reveal later, always cutting a speech in half). That is a sign the stage's contract, or one of its references, is producing the fault. An edit to an output helps this project only; a change to the contract or reference helps every project after it.

**How it is recorded.** Before a stage runs, the agent compares each earlier output it reads with the copy handed over (section 4). For each change you made, it adds one row to `stages/owner-edits.md`: the date, the project, the stage, the file, a few words on the kind of edit, and the marker on the passage you changed, which says which contract step or reference produced it. It does not ask you to explain; it asks only if it cannot tell what you changed.

**When one edit is enough.** An edit or a critic's finding that shows by itself that a contract or reference is wrong (it misreads an owner theory, gives a wrong rule, or points to the wrong place) is a sign for the `error-correction` skill at once, not a row to watch. The rule below is for edits of taste and kind, where no single one shows the source to be wrong.

**When a pattern becomes a proposal.** When the same kind of edit turns up in the work of one stage in three separate runs, the agent stops at the next review stop and proposes a change to that stage's contract or reference, quoting the rows. "Three" is a rule of thumb taken from the paper, which speaks of three runs in a row, not a measured number; what matters is that the edit recurs across runs, not within one. A pattern you point out yourself counts at once.

**How the change is made.** A proposed change to a contract or reference is a change to what the workshop says, so it goes through the `error-correction` skill like any other: its "How much to do" table decides how much review it needs, and whether one of its tripwires has fired (one of them is "the owner caught it"), in which case the full correction goes in `27 Corrections.md`. The row in `stages/owner-edits.md` then points to the correction, or to the commit that made the change. If the corrections file has no room for a new correction, the project story's "Open corrections" line says what must be done first.

## 9. Helper agents

One agent runs the stages. It may hand a job to a helper agent (for example three rival pitches, or three critics), and when it does, the stage contract is the helper's brief: the helper gets the Process step it is to carry out and the files that step needs, as the contract names them. The number of helpers working at once is set in `_config/writer.md`. Two of the workshop's rules apply:
- **Nobody grades their own work.** A critique (stage 08) is written by an agent that did not write what it criticises.
- **Briefs are checked before they go out**, as the error-correction skill's `references/reviews-and-briefs.md`, section 5, says, in proportion to the job.

## 10. What never goes in an output

- **Text from a book.** Stage outputs are the writer's story and the workshop's notes. A craft book's ideas arrive through the references, already in the workshop's own words, or, where a reference points into a book that is present, from the book read as section 1 says; either way they are never copied or quoted at length in an output.
- **Changes to a frozen file.** The owner's theories and the foundation are read, never edited.
- **A claim with no receipt.** "Checked", "agrees" or "works" in an output points to what was run (section 6).

## 11. The project log, and the workshop's own records

Each project keeps a numbered log at `stages/01-brief-and-premise/output/<project>/project-log.md`, started as soon as the request is saved (stage 01, step 3). One entry per stage run, critique round, revision round or piece of your feedback: what ran, which files it read and wrote, what it was least sure of, and anything marked stale. Quote your words where you gave any. Old entries are never rewritten; a later entry corrects an earlier one. Every stage reads it first (section 2).

**A story run and the workshop's own records.** `CLAUDE.md` asks anyone starting work to read the workshop's project story (`StoryTest - project story.md`) and questions file first, and to add an entry to the workshop's log for every piece of work. For a story run through the stages, that is read this way: the run's own record is its project log, and it reads the workshop's records only when it changes the workshop itself (a contract, a reference, a skill). The workshop's log gets one entry when a project starts and one when it ends or is set aside, each pointing to the project log, and an entry for any change the run makes to the workshop.

## 12. How the season work maps onto the stages

| In the Fourth Direction season folder (branch `claude/story-questioning-theme-ehokf0`) | Here |
|---|---|
| 01 Brief; 08 Brief 2 | stage 01: `brief-vN.md` |
| 02 Pitches A, B and C; 10 Pitches A, B and C of the second attempt, each written separately | stage 01: rival premises, `pitches-vN.md` |
| 11 Pitch reviews, one per reviewer, each looking for one kind of problem | stage 08, pointed at stage 01's pitches: `critique-pitches-round-N-<kind>.md` |
| 03 Judgement: which pitch won and why | stage 01: `premise-vN.md`, with its reasons |
| 03, 05 Season plan, versions 1 and 2 | stages 02 to 05 together: cast, world, plot, scene weave (the plan) |
| 04, 06 Critique rounds, one critic per kind of problem | stage 08: `critique-plan-round-N-<kind>.md`, one file per critic per round |
| 05 Revision log: every finding, accepted or not, and what changed | stage 09: `revision-log-plan-round-N.md`, and the new versions it makes |
| 07 Owner feedback: why Caraway was dropped; 12 Owner feedback 2: *Seconds* chosen, every law in | stage 09: your feedback recorded in full, and whatever it changes (a new brief; a rebuilt plan) |
| Episodes, each drafted, critiqued and revised | stages 06 and 07, then 08 and 09, one file per episode |
