# StoryTest - project story

## The goal

A story workshop: a set of Claude Code skills that help build and test stories. The skills stand on four theories of narrative you wrote, use a test for whether each choice in a story is doing real work ("hard to vary"), and add detail from four craft books, always in the workshop's own words and never copying the books.

## Where things stand

*Updated 23 September 2026, entry 24.*

- **Done:** the foundation and the hard-to-vary skill; your four theories, stored and frozen; the source register, with all four books registered and checked for copying; the intake skill (`add-source`) with its three scripts; the five craft skills (`story-world`, `plot`, `character`, `dialogue`, `genre`), each written from your theories and the books, reviewed three ways and fixed; a guide to the repository (`README.md`) and rules for future agents (`CLAUDE.md`).
- **Tested:** four small story problems were run through the skills, fixed, and run again (entries 20 and 23).
- **Waiting on you:** questions only you can settle, in `22 Questions - meanings only you can settle.md`. The skills work without the answers; each open point carries a clearly labelled stopgap reading until you decide.

## How the pieces fit

A concrete case first. A writer asks, "My villain feels flat. Why?"

1. The `character` skill takes it. Its frame is your Bond theory: audiences care because of the relationship a story builds, and for a villain the enemy is indifference, not dislike.
2. It checks the villain against the theory's ten levers, and against ideas from Egri and Truby on building a cast, written in the workshop's words.
3. Each suggested fix is tested with the `hard-to-vary` skill: if the villain's backstory could be swapped for any other and nothing in the story changed, it is doing no work.
4. If the fix is in how the villain talks, the `dialogue` skill takes over; if it is in when the audience learns what the villain wants, the `plot` skill does.

The parts, what each does, and what it hands on:

| Part | What it does | Hands on to |
|---|---|---|
| Foundation (`foundations/`) | Your formal theory of what makes an explanation good | The `hard-to-vary` skill |
| `hard-to-vary` skill | Tests whether each part of an explanation, or each choice in a story, is held in place by a job | Every craft skill uses it |
| Owner theories (`sources/`) | Implied World, Gap, Anticipation, Bond: why worlds, plots, suspense and characters work | Each is the frame of one or more craft skills |
| Source register (`sources/README.md`) | Lists every source: stored theories and registered (not stored) books | You, to check where any idea came from |
| `add-source` skill | The one way in for any new source; turns an ebook into text and checks for copying | Owner theories, the register, the craft skills |
| Craft skills | Build and diagnose one area each: world, plot, character, dialogue, genre | Each other, where a question crosses areas |

## Word list

- **Skill:** a folder of instructions that Claude Code loads when a request matches it. Each has a main file (`SKILL.md`) and optional extra files it opens only when needed.
- **Module (reference file):** one of those extra files, covering one part of a skill in depth.
- **Map:** the table and diagram near the top of each skill that says which module to open when. A module missing from the map can never be reached.
- **Owner theory:** one of the four theories you wrote (Implied World, Gap, Anticipation, Bond). The skills call them this. The primary source for a craft skill.
- **Frozen source:** a stored text that is never edited. A changed version is added as a new file, called a revision.
- **Foundation:** your formal theory of explanation ("Claude Fable Semantics"), which the hard-to-vary skill puts to work.
- **Craft skill:** a skill for one area of storytelling (world, plot, character, dialogue, genre).
- **Craft book:** a published book on writing. Registered and used in own words, never stored.
- **Register:** the list of sources in `sources/README.md`.
- **Own words:** written fresh from notes, not copied or reworded line by line from a book.
- **Overlap check:** a script that lists every run of 8 or more words in a row that the workshop shares with a book. The rule is zero, apart from titles, names and short terms.
- **Hard to vary:** a choice is hard to vary when changing it would break something the story needs. A choice you could swap for any other is doing no work.
- **Rival:** a book's view that differs from one of your theories, recorded beside the theory with a way to tell the two apart, never used to overrule it.
- **Commit:** a saved snapshot of the files, with a note saying what changed. **Push:** sending commits to GitHub. **Branch:** a separate line of work. **Pull request:** a request to fold a branch into the main line, where changes can be reviewed.
- **Agent:** a separate Claude worker given one job. **Workflow:** a script that runs many agents to a plan.

## Log

Entries 1 to 7 are from the previous session. Its own copy of this file was not in the repository, so these entries are rebuilt from its saved work (the commit notes). If you have that session's copy, upload it and I will merge the two.

1. **Foundation and hard-to-vary installed.** The formal theory (revision 1) went into `foundations/`, and the hard-to-vary skill into `.claude/skills/`, both exactly as supplied.
2. **Implied World theory stored**, frozen, as the future primary source of the story-world skill.
3. **Gap theory of narrative stored**, frozen. Its closing offer line was left out as not part of the theory, and the note says so.
4. **Anticipation theory stored**, frozen, as a future module of the plot skill.
5. **Hard-to-vary brought into line with revision 1** of the foundation: one changed claim (about parts fitted to past cases) carried through four files. Two older disagreements between the skill and the foundation were found and left for you to decide.
6. **Copying guard added.** `sources/raw/` set as a local folder that is never saved to GitHub, and the overlap check script written.
7. **Bond theory stored**, frozen, as the future primary source of the character skill, with Egri's book noted as to be registered and used in own words only. **The previous session stopped here**, before the register, the intake skill or any craft skill existed.
8. **Picked up the job (this session).** The previous session's conversation was not visible. The plan was rebuilt from what it left: its commit notes name a register, an intake skill, and story-world, plot and character skills. The four uploaded books were identified: Egri, *The Art of Dramatic Writing*; McKee, *Dialogue*; Truby, *The Anatomy of Story* and *The Anatomy of Genres*.
9. **Books turned into text.** Wrote `book_to_text.py`, which turned all four ebooks into plain text in `sources/raw/` (about 490,000 words in all); git ignores them, as checked. Gave the overlap check plain-word names; its output on the same inputs is identical before and after, as checked.
10. **Register and intake skill written**, then saved to GitHub and a draft pull request opened (#1). The overlap check found only book titles in the register, which the rule allows.
11. **Reading the books.** Split the books into 33 chunks and started one reading agent per chunk, each writing own-words notes tied to the four theories. The first attempt ran 2 agents at a time (the machine's default limit); it was stopped after about five minutes and restarted as three batches of 2, because the machine was nearly idle. The two unfinished readers' work was lost and redone.
12. **Reading finished.** All 33 readers completed with no errors, writing about 545,000 words of notes in their own words (kept outside the repository, never committed). Each note says how the idea stands to your four theories: agrees, extends, conflicts, or no link. Example of a conflict found: Egri wants a play to hold only what its premise needs, which would cut the purposeless world detail the Implied World theory says makes a world feel real.
13. **Craft skills written.** 21 writing agents produced the five craft skills: `story-world` (5 files), `plot` (8), `character` (5), `dialogue` (6) and `genre` (14, including one profile per genre for twelve genres). To save time, writing started skill by skill as soon as the notes each one needed were ready, while other chunks were still being read.
14. **A naming clash settled.** "Horror" is both a genre and the top rung of your fear ladder. Rule adopted: capital-H Horror for the genre, "the horror rung" for the ladder step.
15. **Every skill reviewed and fixed.** Three separate reviewers read each skill: one for faithfulness to your theories, one for copying, and one for loose parts and whether it works in use. A fixer then checked each finding and applied or rejected it. In all: 11 blocking findings, 243 should-fix and 116 small ones; 277 changes applied and 47 turned down with reasons. Examples of what was caught:
    - The plot skill had adopted Truby's rule that a reveal which changes no decision should be cut. That would have cut your Gap theory's own example, the bomb shown to the audience only.
    - The character skill said knowing an event removes uncertainty. Your Anticipation theory says the uncertainty moves from whether to how.
    - The genre skill warned against "anyone can die at any moment", which is the effect your Anticipation theory says one early break is meant to create.
    - Several passages followed Truby's wording or order too closely even though the copying script found no runs of 8 words. They were rewritten.
    - One mistake was mine. My brief to the writers credited "build care before the threat" to the Bond theory; it is in the Anticipation theory, and a fixer corrected it.
16. **A second copying guard added to the intake skill.** Because reviewers found close paraphrase in most first drafts that the script had passed, `add-source` now requires a second reader to compare passages with the book by eye.
17. **Map checker written and tested.** `check_maps.py` checks that every module is in its skill's map table and diagram, that every file path a skill mentions exists, and that descriptions fit Claude Code's length limit. Tested on a copy with a planted orphan module and a misspelt link: both caught. On the real repository it reports zero problems.
18. **One rule for promises and guarantees.** The genre profiles had drawn the line between a promise (what a genre owes, from your Gap theory) and a guarantee (a protection the audience relaxes into, from your Anticipation theory) in different places. The rule is now settled in one file, `how-genres-work.md`, and a final pass is applying it to all twelve profiles.
19. **Register completed.** Copying check for all four books: 0 runs of 8+ words anywhere in the repository, apart from book and film titles.
20. **Final check and four trial runs.** One agent read all five skills together: no broken links, but one blocking contradiction (the plot skill would cut a scene that shows the world at its own business, which the Implied World theory values) and about twenty mismatched terms and hand-offs. Four agents then ran small story problems through the skills: a flat villain, a generic Horror-Western, stiff dialogue, and a thriller whose middle sags. The right skill was chosen every time and every pointer worked. The skills improved the answers moderately, not dramatically. Example: for the flat villain, the character skill stopped the agent from agreeing with the writer's own fix (give him scenes alone), because time in a villain's head can make readers side with him. The trials also found four gaps shared by all five skills: no fallback when the writer gives only a pitch, too heavy a hand-off to hard-to-vary, unclear routing for small cases, and no set shape for the reply.
21. **Promise and guarantee pass finished** (begun in entry 18): all twelve genre profiles now draw the line the same way.
22. **Fixes, and the questions file.** The four shared gaps were fixed with matching wording in all five skills, along with the consistency problems. A checking agent then found about a dozen remaining problems, and I fixed those by hand. Two of them misread your theories: the reason given for keeping world-only scenes stretched the Gap theory, and the villain's ladder of care had been turned round wrongly. Wrote `22 Questions - meanings only you can settle.md`: eight main questions and a few smaller ones, each with options, the skills' current reading and my recommendation.
23. **Trials run again.** The same four problems were run on the fixed skills, checking each earlier stall. 31 of 38 were resolved, 5 partly resolved, and 2 not: this file's stale "next step", fixed now; and the dialogue skill's worked example, which resembles one test scene by coincidence of the test and was left alone. The reruns found about fifteen smaller new problems, most introduced by the fixes themselves (for example, "Side with" used in two senses a paragraph apart).
24. **Last small pass** on those fifteen, one fixer per skill. It also defines a "small case" (one scene, one character, one choice or one named symptom), and adds to every reply which choices are free and which are held in place. This pass was checked by the copying and map scripts, but the four trials were not run a third time.

## Next step

Bring the workshop one real problem from a story of your own: a pitch, a scene, or a character who isn't working. That is the test the four trial runs could only imitate.
