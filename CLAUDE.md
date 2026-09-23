# Working in this repository

This is a story workshop: Claude Code skills in `.claude/skills/` built on the owner's theories in `sources/`. `README.md` has the map.

- **Starting or continuing work:** read `StoryTest - project story.md` first. It has the goal, where things stand and a numbered log. Add a new numbered entry for every piece of work, failures included; never rewrite old entries.
- **Frozen files:** `foundations/claude-fable-semantics.md` and every owner theory in `sources/` (all files there except `README.md`). Never edit them, not even typos. A revision is a new file (see the `add-source` skill).
- **New material of any kind** (a theory, a revision, a book, an article) goes through the `add-source` skill.
- **Copyright:** nothing from a copyrighted book is committed. Local copies live in `sources/raw/`, which git ignores; check `git status` before each commit. Before committing anything drawn from a book, run `python3 .claude/skills/add-source/scripts/overlap_check.py sources/raw/<book>.txt .claude/skills sources foundations` and rewrite every reported run except titles, names and the author's short term names. Record the result in `sources/README.md`.
- **Craft skills** follow the owner theory they are built on and never contradict it. A book's disagreeing view is recorded as a rival, with a change to a story that would tell the two apart.
- **Maps:** every skill has a "Where to look, and when" table and graph. When you add, split or remove a module, update both in the same edit.
- **Plain words:** the owner is not a programmer. In the skills and in replies, explain a technical term once in a plain sentence, then use that one word for that one thing.
- **Scripts:** full plain-word names, and a note at the top saying what the file does.
