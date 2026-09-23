# Sources

This folder holds the owner's theories, frozen, and the register of every outside work the workshop draws on. The craft skills in `.claude/skills/` are built from these sources. The sources never change to suit a skill.

## Three kinds of source, kept three ways

| Kind | Example | Kept how |
|---|---|---|
| **The owner's own theory** | `bond-theory.md` | Stored here word for word, under a heading and a note saying where it came from. Frozen: never edited. A revised version is added as a new file with a revision number. |
| **The foundation** | `../foundations/claude-fable-semantics.md` | Stored word for word in `foundations/`, frozen the same way. The `hard-to-vary` skill is its working form. |
| **Someone else's copyrighted work** | Egri, *The Art of Dramatic Writing* | Registered in the table below, **never stored**. Its ideas go into the craft skills in the workshop's own words. A local copy may sit in `sources/raw/` while it is being read; git ignores that folder, so it is never committed. |

To add a source of any kind, use the `add-source` skill (`.claude/skills/add-source/SKILL.md`).

## The owner's theories

All four were supplied on 23 September 2026. Each builds on the one before.

| File | Central claim, in one line | Builds on | Primary source of |
|---|---|---|---|
| `implied-world-theory.md` | A fictional world is never on the page; the audience infers it from what is shown. | nothing | `story-world` skill |
| `gap-theory-of-narrative.md` | A narrative is a stack of five gaps that open and close over time. | Implied World | `plot` skill |
| `anticipation-theory.md` | Suspense and fear come from what the audience expects might happen. | Implied World, Gap | `plot` skill, suspense module |
| `bond-theory.md` | Audiences care about a character because of the relationship the story builds, not the character's traits. | Anticipation | `character` skill |

The `dialogue` and `genre` skills have no owner theory of their own yet. They are built on what the four theories already say about talk and about genre, and they say so at the top.

## The foundation

| File | What it is | Used by |
|---|---|---|
| `../foundations/claude-fable-semantics.md` | The owner's formal theory of explanation, revision 1 (file 11), 22 September 2026. | `hard-to-vary` skill, which every craft skill uses to test whether a choice is doing work |

## Registered works (not stored)

"Overlap check" is the result of `.claude/skills/add-source/scripts/overlap_check.py`, which lists every run of 8 or more words in a row that the workshop's files share with the book. The rule is zero runs, apart from names, titles and the author's own short term names.

| Work | Edition read | Supplied | Feeds | Overlap check |
|---|---|---|---|---|
| Lajos Egri, *The Art of Dramatic Writing: Its Basis in the Creative Interpretation of Human Motives* | Touchstone ebook of the 1960 revised edition (© 1942, 1946, 1960) | 23 Sep 2026, with the Bond theory, "for more detail on developing characters in general" | `character`; also `plot` (premise, conflict) and `dialogue` | *pending* |
| John Truby, *The Anatomy of Story: 22 Steps to Becoming a Master Storyteller* | ebook, 2011 (first published 2007) | 23 Sep 2026, with the request to finish the job | `plot`, `character`, `story-world`, `dialogue` | *pending* |
| John Truby, *The Anatomy of Genres: How Story Forms Explain the Way the World Works* | Picador ebook, 2022 (ISBN 9780374722814) | 23 Sep 2026, with the request to finish the job | `genre`; also `story-world` | *pending* |
| Robert McKee, *Dialogue: The Art of Verbal Action for Page, Stage, and Screen* | Grand Central ebook, 2016 (ISBN 9781455591923) | 23 Sep 2026, with the request to finish the job | `dialogue`; also `character` (voice) | *pending* |

Where a book disagrees with an owner theory, the skill follows the theory and records the book's view as a rival, with the change that would tell the two apart. The book never quietly corrects the theory.

## Revisions

An owner theory is never edited in place. A revision is added as a new file (for example `bond-theory-revision-1.md`) with a note saying what changed. Then every skill that restates the changed claim is checked and brought into line in the same piece of work, the way `hard-to-vary` was brought into line with revision 1 of the foundation.
