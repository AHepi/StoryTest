# StoryTest - project story

## The goal

A story workshop: a set of Claude Code skills that help build and test stories. The skills stand on four theories of narrative written by the owner, use a test for whether each choice in a story is doing real work ("hard to vary"), and add detail from four craft books, always in the workshop's own words and never copying the books.

## Where things stand

*Updated 23 September 2026, entry 11.*

- **Done:** the foundation and the hard-to-vary skill; the four owner theories, stored and frozen; the source register; the intake skill (`add-source`) with its two scripts; a guide to the repository (`README.md`) and rules for future agents (`CLAUDE.md`).
- **Under way:** reading the four books into own-words notes, then writing the five craft skills (`story-world`, `plot`, `character`, `dialogue`, `genre`).
- **Not started:** checking the craft skills for copying, faithfulness to the theories, and loose parts.

## How the pieces fit

A concrete case first. A writer asks, "My villain feels flat. Why?"

1. The `character` skill takes it. Its frame is the owner's Bond theory: audiences care because of the relationship a story builds, and for a villain the enemy is indifference, not dislike.
2. It checks the villain against the theory's ten levers, and against ideas from Egri and Truby on building a cast, written in the workshop's words.
3. Each suggested fix is tested with the `hard-to-vary` skill: if the villain's backstory could be swapped for any other and nothing in the story changed, it is doing no work.
4. If the fix is in how the villain talks, the `dialogue` skill takes over; if it is in when the audience learns what the villain wants, the `plot` skill does.

The parts, what each does, and what it hands on:

| Part | What it does | Hands on to |
|---|---|---|
| Foundation (`foundations/`) | The owner's formal theory of what makes an explanation good | The `hard-to-vary` skill |
| `hard-to-vary` skill | Tests whether each part of an explanation, or each choice in a story, is held in place by a job | Every craft skill uses it |
| Owner theories (`sources/`) | Implied World, Gap, Anticipation, Bond: why worlds, plots, suspense and characters work | Each is the frame of one or more craft skills |
| Source register (`sources/README.md`) | Lists every source: stored theories and registered (not stored) books | The owner, to check where any idea came from |
| `add-source` skill | The one way in for any new source; turns an ebook into text and checks for copying | Owner theories, the register, the craft skills |
| Craft skills | Build and diagnose one area each: world, plot, character, dialogue, genre | Each other, where a question crosses areas |

## Word list

- **Skill:** a folder of instructions that Claude Code loads when a request matches it. Each has a main file (`SKILL.md`) and optional extra files it opens only when needed.
- **Module (reference file):** one of those extra files, covering one part of a skill in depth.
- **Map:** the table and diagram near the top of each skill that says which module to open when. A module missing from the map can never be reached.
- **Owner theory:** one of the four theories the owner wrote. The primary source for a craft skill.
- **Frozen source:** a stored text that is never edited. A changed version is added as a new file, called a revision.
- **Foundation:** the owner's formal theory of explanation ("Claude Fable Semantics"), which the hard-to-vary skill puts to work.
- **Craft skill:** a skill for one area of storytelling (world, plot, character, dialogue, genre).
- **Craft book:** a published book on writing. Registered and used in own words, never stored.
- **Register:** the list of sources in `sources/README.md`.
- **Own words:** written fresh from notes, not copied or reworded line by line from a book.
- **Overlap check:** a script that lists every run of 8 or more words in a row that the workshop shares with a book. The rule is zero, apart from titles, names and short terms.
- **Hard to vary:** a choice is hard to vary when changing it would break something the story needs. A choice you could swap for any other is doing no work.
- **Rival:** a book's view that differs from an owner theory, recorded beside the theory with a way to tell the two apart, never used to overrule it.
- **Commit:** a saved snapshot of the files, with a note saying what changed. **Push:** sending commits to GitHub. **Branch:** a separate line of work. **Pull request:** a request to fold a branch into the main line, where changes can be reviewed.
- **Agent:** a separate Claude worker given one job. **Workflow:** a script that runs many agents to a plan.

## Log

Entries 1 to 7 are from the previous session. Its own copy of this file was not in the repository, so these entries are rebuilt from its saved work (the commit notes). If you have that session's copy, upload it and I will merge the two.

1. **Foundation and hard-to-vary installed.** The formal theory (revision 1) went into `foundations/`, and the hard-to-vary skill into `.claude/skills/`, both exactly as supplied.
2. **Implied World theory stored**, frozen, as the future primary source of the story-world skill.
3. **Gap theory of narrative stored**, frozen. Its closing offer line was left out as not part of the theory, and the note says so.
4. **Anticipation theory stored**, frozen, as a future module of the plot skill.
5. **Hard-to-vary brought into line with revision 1** of the foundation: one changed claim (about parts fitted to past cases) carried through four files. Two older disagreements between the skill and the foundation were found and left for the owner to decide.
6. **Copying guard added.** `sources/raw/` set as a local folder that is never saved to GitHub, and the overlap check script written.
7. **Bond theory stored**, frozen, as the future primary source of the character skill, with Egri's book noted as to be registered and used in own words only. **The previous session stopped here**, before the register, the intake skill or any craft skill existed.
8. **Picked up the job (this session).** The previous session's conversation was not visible. The plan was rebuilt from what it left: its commit notes name a register, an intake skill, and story-world, plot and character skills. The four uploaded books were identified: Egri, *The Art of Dramatic Writing*; McKee, *Dialogue*; Truby, *The Anatomy of Story* and *The Anatomy of Genres*.
9. **Books turned into text.** Wrote `book_to_text.py`, which turned all four ebooks into plain text in `sources/raw/` (about 490,000 words in all); git ignores them, as checked. Gave the overlap check plain-word names; its output on the same inputs is identical before and after, as checked.
10. **Register and intake skill written**, then saved to GitHub and a draft pull request opened (#1). The overlap check found only book titles in the register, which the rule allows.
11. **Reading the books.** Split the books into 33 chunks and started one reading agent per chunk, each writing own-words notes tied to the four theories. The first attempt ran 2 agents at a time (the machine's default limit); it was stopped after about five minutes and restarted as three batches of 2, because the machine was nearly idle. The two unfinished readers' work was lost and redone.

## Next step

Finish the reading, then write the five craft skills from the notes.
