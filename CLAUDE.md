# Working in this repository

This is a story workshop: Claude Code skills in `.claude/skills/` built on the owner's theories in `sources/`. `README.md` has the map.

- **Starting or continuing work:** read `StoryTest - project story.md` first. It has the goal, where things stand and a numbered log. Add a new numbered entry for every piece of work, failures included; never rewrite old entries. Then read `22 Questions - meanings only you can settle.md` for points the owner has not yet decided; until they do, keep each skill's labelled stopgap reading. Open corrections are in `27 Corrections.md`.
- **Taking a request from the owner:** before acting, say it back in one line (what is asked, what is not, and the nearest other reading, if there is one) and name anything you are adding to it. Quote the owner's words at the start of the log entry. Then carry on; do not wait unless your reading is in doubt. It is in doubt, among other times, when the owner's words have more than one plain reading that leads to different work (a word that makes sense as written but could be a slip for another, as "Return" for "Rerun"; a word with two senses, as "script" for a screenplay or a program), or when you would add "if you meant something else, tell me". Then ask which is meant, and do nothing risky, costly or hard to undo on any of the readings until the owner answers; a cheap reply on one reading may go now, with the question (correction C17).
- **Frozen files:** `foundations/claude-fable-semantics.md` and every owner theory in `sources/` (every file there other than `README.md`). Never edit them, not even typos. A revision is a new file (see the `add-source` skill). A hook (a small program Claude Code runs by itself before every file edit) refuses edits to them, and a fingerprint check catches any other route.
- **New material of any kind** (a theory, a revision, a book, an article) goes through the `add-source` skill.
- **Copyright:** nothing from a copyrighted book is committed. Local copies live in `sources/raw/`, which git ignores. Before committing anything drawn from a book, run `python3 .claude/skills/add-source/scripts/overlap_check.py sources/raw/<book>.txt .` in the repository folder and rewrite every reported run except titles, names and the author's short term names. Record the result in `sources/README.md`.
- **Craft skills** follow the owner theory they are built on and never contradict it. A book's disagreeing view is recorded as a rival, with a change to a story that would tell the two apart (the rival form in the `error-correction` skill).
- **Maps:** every skill has a "Where to look, and when" table and graph. When you add, split or remove a module, update both in the same edit.
- **Plain words:** the owner is not a programmer. In the skills and in replies, explain a technical term once in a plain sentence, then use that one word for that one thing.
- **Scripts:** full plain-word names, and a note at the top saying what the file does.

## Error correction

Error correction is how work here proceeds; hard to vary is how its judgements are measured. Use the `error-correction` skill whenever anything may be wrong:
- a check fails or a commit is stopped;
- a reviewer, kept case or trial finds a problem;
- the owner objects, or asks whether something was done (a writer's objection to a note is answered in the craft skill's reply check);
- you doubt your own work.

Use it also before you call anything fixed or done, before a critique or report goes to the owner, before a brief goes to other agents, before you write a skill's rule or a rival, and when an owner question is answered.

Three rules are never bent:
1. **Nobody grades their own work.** A change to what the workshop says is reviewed by an agent that did not make it. The commit gate will not take it without that review's receipt.
2. **Not run is never passed.** Every "checked", "put right" or "works" points to what was run and what it printed. Say what was not checked.
3. **A failing check is a sign, never an obstacle.** Put right what it found, or correct the check in a commit of its own. Never get round it.

What the owner values is an input: never rank or overrule it. An owner objection is never set aside; if it seems not to bear, ask the question that would settle it. A verdict that needs an aim only the owner or a writer can give is *held if* that aim: give it both ways, and ask. A verdict that needs a fact nobody has checked or told you, such as which draft came first, *does not bear yet*: ask, and if a note must go now, give it both ways.

A few words used below. *Staged* means marked with `git add` to go into the next commit. The *commit gate* is the set of checks git runs by itself before every commit (`.githooks/pre-commit`); it runs the checks as they were in the last commit it approved, so a check cannot be loosened in the same commit as the work it would stop. `--no-verify` is a switch that would make git skip the gate. *By itself* means a program does it with no one choosing to; *on trust, with a trace* means an agent must do it, and leaves a record someone can check.

What enforces each rule:

| Rule | Enforced by |
|---|---|
| Frozen files unedited | By itself: `.claude/hooks/protect_frozen_files.py` before an edit (the checks make sure the settings still register it), and the fingerprint check at every commit |
| Checks pass before a commit | By itself: `.githooks/`, switched on at session start. The gate stamps each commit it passes and compares the files with the last commit it approved (found by walking back along the main line; a merge made on GitHub with no conflict counts as approved, with the exceptions in the error-correction skill's references/checks-and-cases.md, section 2), so what a commit made without it got wrong in the files stops the next commit until it is put right (a loosened check apart: see the next row). A Claude hook refuses the usual ways of skipping the gate (the usual spellings only). At session start and before each commit, `recheck_commits.py` looks at the commits since the last approved one for their review receipts, a claimed withdrawal, book files and changes to the gate's own files; the last two are notes, shown until the next approved commit, and acting on them is on trust |
| A check is corrected in its own commit, and cannot pass the work it would stop | By itself within one commit: the gate runs the last approved commit's checks and receipt check, refuses a check change mixed with other work, and runs that commit's planted-fault test whenever the checks differ from its own. Across two commits, on trust: the loosening commit's review, and the planted faults that exist; the same for a check loosened in a commit made without the gate |
| A change to what the workshop says is independently reviewed | On trust, with a trace: the gate refuses the change without a review receipt (`.claude/reviews/`) that names a reviewer other than the maker and carries the reviewer's report; it cannot tell whether that reviewer really ran |
| Old log entries never rewritten; write-ups list the checks run on them | By itself: the records check at every commit, against the last approved commit and, in a merge through the gate, the other side's new entries too. After a merge made on GitHub with a conflict, the other line's entries are kept on trust; GitHub's conflict editor and "Update branch" put the session's branch first, and a rebase-merged pull request reverted on GitHub is never compared (see the list named below) |
| Status lines current | On trust, with a trace: a new entry forces a new stamp on each line and prints them all; what the second look finds is on trust |
| No book file committed; copying checked | By itself where the books are present, on the files as they are at each commit through the gate; otherwise the review receipt must say what book text a change to a skill adds. A text file over 100 KB is refused anywhere, apart from one kept record named in the check, and only while its contents are unchanged. A book file added without the gate is noted until the next approved commit. Not seen: a copied passage added and removed between two commits through the gate, and small text outside the skills while the books are absent |
| A skill's rules and rivals measured when written | On trust, with a trace in the review receipt |
| Briefs checked before they go out | On trust; a trace only when the brief is kept |
| Kept cases rerun after a skill changes | On trust, with a trace: session start lists skills changed since their cases last ran |
| A full correction recorded when a tripwire fires | On trust, with a trace: the records check reads `27 Corrections.md` |
| Saying a request back; claims checked before they reach the owner | On trust; a hook repeats the claim check after every commit |

What none of this can stop: an agent set on getting round the gate. The gate is made of files in this repository: git runs `.githooks/pre-commit` from the disk, and that runs the gate script as it is in the last commit, so whoever edits them can switch it off. It also misses some honest routes; those known are listed in the error-correction skill's references/checks-and-cases.md, section 2, "What the gate cannot do", among them a change to the gate's own files made outside it, a check loosened across two commits, close paraphrase and some other copying, what a receipt says beyond its form, notes that are shown only until the next approved commit, and some routes on the way to or from GitHub (its conflict merges, a rebase that settles commits unseen, a rebase-merged pull request reverted there, a build landed on a main branch that has moved on). Only a check that runs outside the repository (question S10) or the owner can catch everything. The gate stops most honest mistakes and shortcuts, which is what the workshop's history needed.
