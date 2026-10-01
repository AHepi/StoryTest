*Kept for log entry 36 by the briefing session: the instructions it gave each agent, so that correction C13's lesson is followed. Sections 1 and 2 are word for word, except that any run of eight or more words shared with a book or the paper is replaced by a marker, "[quotation removed: N words of SOURCE]" (three such runs: the paper's title, one short phrase of the paper's, and one list of Truby's chapter names). Section 3 is a summary of three short follow-up messages, not word for word; the summary says what each asked.*

## 1. The brief to the maker (word for word)

# Brief: make the StoryTest workshop work like an ICM workspace, and fill it from the books

## The owner's request, word for word
"Set one more agent to branch and update the repo so that it functions more like this paper. And fill it with details from this book."
Attached: the paper "[quotation removed: 8 words of paper-icm-2603.16021]" (Van Clief and McDermott, arXiv 2603.16021v2), and three books: McKee, *Dialogue*; Truby, *The Anatomy of Story*; Truby, *The Anatomy of Genres*.

## How the request was read (say so in your log entry)
- "The repo" is the owner's story workshop as it stands on branch `claude/incomplete-job-continuation-guewwy` (entry 35). Your branch `claude/icm-story-workspace` starts from it. Another session may still be working on that branch, so change only your own branch.
- "This book" is read as the three attached books, all already registered in `sources/README.md`. If you find the owner meant one of them, say so in the log.
- "Functions more like this paper" means reorganising the workshop so that one orchestrating agent is driven by the folders, as ICM describes, while keeping everything the workshop already does well.

## Where things are
- Your working folder is the git worktree **/home/user/StoryTest-icm**, on branch `claude/icm-story-workspace`. Work only there.
- The paper as text: `/home/user/StoryTest-icm/sources/raw/paper-icm-2603.16021.txt`. Read all of it first.
- The books: `/home/user/StoryTest-icm/sources/raw/mckee-dialogue.epub`, `truby-anatomy-of-story.epub`, `truby-anatomy-of-genres.epub`. `sources/raw/` is ignored by git and must stay so. Use `.claude/skills/add-source/scripts/book_to_text.py` (or unzip) to get text.
- Read `CLAUDE.md`, `README.md`, `StoryTest - project story.md` and `27 Corrections.md` before changing anything. They carry the owner's rules. Obey them, and above all:
  - frozen files are never edited;
  - nothing from a book is committed except in the workshop's own words, checked with `overlap_check.py` and recorded in `sources/README.md`;
  - plain words for an owner who is not a programmer;
  - a new numbered log entry, quoting the owner's words, and old entries are never rewritten;
  - "not run is never passed".
- A live example of the kind of pipeline the owner runs: the TV-season work on branch `claude/story-questioning-theme-ehokf0`, folder `stories/fourth-direction-season/`. It goes brief → pitches → pitch reviews → season plan → critique rounds → revision logs → episodes, and every earlier version is kept. The owner said the revisions are the part they care about most.

## What to build (the paper's ideas, applied to this workshop)
1. **Five context layers.**
   - Layer 0 is `CLAUDE.md`: identity and a short map, kept short.
   - Layer 1 is a new root `CONTEXT.md`: task routing. What the user wants to do, and which stage or skill handles it.
   - Layer 2 is one `CONTEXT.md` per stage: the stage contract.
   - Layer 3 is reference material, stable across runs: the owner's theories in `sources/` (unmoved), the skills, and new reference files.
   - Layer 4 is working artifacts, one set per run.
2. **Numbered stage folders** for making a story, one job per stage, for example premise and brief, world, characters, plot and structure, scenes, dialogue, critique, revision. Each stage folder holds `CONTEXT.md`, a `references/` folder and an `output/` folder. You choose the exact stages. Base them on the books' own process (Truby's order of work, McKee's craft of lines and scenes) and on how the owner's season work actually runs.
3. **Stage contracts** each have four parts:
   - an **Inputs table**, naming exactly which Layer 3 files and sections, and which Layer 4 outputs of earlier stages, the stage loads;
   - **Process**;
   - **Outputs**;
   - **Verify**: which earlier stage outputs to check for consistency, and against what.
4. **Review gates.** Each stage output is a plain file the owner can open, [quotation removed: 8 words of paper-icm-2603.16021]. Say so in each contract.
5. **Configure the factory, not the product.** Add a `_config/` folder or setup questionnaire for a writer's standing preferences (voice, genre, medium, length). Keep per-run work in `output/` folders, or a runs folder with one subfolder per project.
6. **Edit-source principle, joined to the workshop's error correction.** When the owner keeps making the same kind of edit to a stage's output, that is a sign the stage contract or its references should change. Add a light way to record such edits and turn them into source changes. It should fit the existing `error-correction` skill and `27 Corrections.md`, not replace them.
7. **Traceability.** Give stage outputs light markers naming the contract section or reference file behind each part, so a problem can be traced back to its source.
8. **Keep what works.** The existing skills, hooks, commit gate, kept cases and checks stay working. If files move, update every map ("Where to look, and when" tables and graphs), every path in scripts and checks, and `README.md`. Run the workshop's own checks (`run_all_checks.py`, `check_maps.py`, `test_checks.py` and the rest) and report exactly what they printed.

## Fill it with details from the books
Each stage's `references/` gets the craft detail that stage needs, taken from the three books in the workshop's own words. It follows the owner's theories wherever they apply, and records a disagreement as a rival, in the form the `error-correction` skill gives. Before writing, compare against what the craft skills already hold, and add what is missing rather than repeating it. Useful material includes:
- **Truby's step order:** premise, the seven key steps, the 22 steps, [quotation removed: 9 words of truby-anatomy-of-story], the symbol web, plot and reveals, the scene weave, scene construction and dialogue.
- **McKee's** principles of dialogue as action and his scene design.
- **Truby's** genre beats.

Run `overlap_check.py` on every file you write, against each book's text, and rewrite every run it reports (titles and names apart). Record the results in `sources/README.md`.

## Limits
- **Work alone.** Do not start any other agents, workflows or sub-agents: the owner limits how many run at once.
- **Committing.** Commit in small steps on your branch with clear messages, using the gate. Run commits as `git -c core.hooksPath=.githooks commit ...` so the workshop's commit gate runs, and never skip it.
- **Changes that need a review receipt.** The gate refuses a change to what the workshop says unless it carries a review receipt from an agent other than its maker. You cannot honestly review your own work, and must not write a receipt that pretends otherwise. So:
  1. Commit whatever the gate accepts.
  2. Leave the rest in the working tree, staged if you like.
  3. Write a review brief for an independent reviewer to `/home/user/StoryTest-icm/REVIEW-BRIEF.md`, not committed, saying what to check.
  4. Stop. The orchestrator will run the reviewer and commit with the receipt.
- **Do not push.** The orchestrator will push after review.
- End each commit message with these two lines:
  Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_0154gfc4UktziZ56i1guynpf

## What to return
A plain-language report, under 400 words, covering:
- what you built, as a short folder map;
- what came from the paper;
- what came from each book, and the overlap-check results;
- which checks you ran, and what they printed;
- what is committed, and what is waiting for review;
- what you did not do, and what you are unsure of.

The maker's opening instruction pointed to this brief and repeated its limits (work only in the worktree, start no agents, do not push, never commit book text or edit frozen files, use the commit gate, never write a receipt for its own work, report in under 400 words).

## 2. The first-round reviewers' instructions (word for word, the script that ran them one at a time)

```
export const meta = {
  name: 'icm-review',
  description: 'Independent review of the ICM workshop change by the workshop\'s own three reviewer roles, one at a time',
  phases: [
    { title: 'Theory check' },
    { title: 'Copy check' },
    { title: 'Use test' },
  ],
}
const WT = '/home/user/StoryTest-icm'
const COMMON = `You are an independent reviewer for the owner's story workshop. You wrote none of the change you are reviewing. The change is on branch claude/icm-story-workspace in the git worktree ${WT}: one commit (915aa52) plus 37 staged files (read them with: cd ${WT} && git diff --cached). The maker's brief for reviewers is ${WT}/REVIEW-BRIEF.md; read it first, and look first at the items it says it is least sure of. Never edit, stage, commit or delete anything in ${WT} or in /home/user/StoryTest. If you need to try something that writes files, copy the worktree to a fresh scratch folder first (cp -r, then remove its .git link so nothing can reach the live repository) and work there. Do not start any other agents or workflows. Save your full report as a file in /tmp/claude-0/-home-user-StoryTest/265a0046-ddbf-521c-b22e-35bf4bc1a28a/scratchpad/icm-review/ (create the folder if needed), and return the same report as your final message.`
const ROLES = [
  {k: 'theory-checker', ph: 'Theory check', extra: 'Cover items 4 to 9 of the brief, the stage contracts and references against the owner theories and the term sheet, entry 36 and question S15 against what happened, and _config/writer.md against its sources.'},
  {k: 'copy-checker', ph: 'Copy check', extra: 'The book texts are at ' + WT + '/sources/raw/*.txt (and the paper at sources/raw/paper-icm-2603.16021.txt). Cover items 1 to 3 of the brief first, then every stages/*/references/*.md file, stages/how-stages-work.md and CONTEXT.md.'},
  {k: 'use-tester', ph: 'Use test', extra: 'Walk one small invented request (for example: a writer wants a short horror film premise and a cast) through CONTEXT.md and stages 01 and 02 exactly as an agent following the files would, in a scratch copy. Report where the contracts stall, contradict each other, point to the wrong section, or load too much or too little.'},
]
const reports = []
for (const r of ROLES) {
  phase(r.ph)
  const rep = await agent(`${COMMON}\n\nYour role: read ${WT}/.claude/agents/${r.k}.md and act exactly as that role, including its report format and final verdict line. ${r.extra} Name your report file ${r.k}.md.`, {label: r.k, phase: r.ph})
  reports.push({role: r.k, report: rep})
}
return reports```

## 3. Follow-up messages (summarised)

- **To the maker, after the first round:** the owner confirmed "These books"; then, with the three reports' paths, put right every finding or reject it with a reason, add use-tester 7 and 11 to the questions file as owner questions, record use-tester 15 as open, rerun the copying check and the checks, write one line per finding to the answers file, update entry 36, keep everything staged, write no receipt, start no agents.
- **To the second-look reviewer (a new agent, which had not reviewed before):** under section 4 of `reviews-and-briefs.md`, check every must-change answer against the staged files and a third or more of the rest; act as the copy-checker for the rewritten text of copy-checker findings 1 to 9; run the copying check at 8 words; edit nothing, start no agents; end with one of passed, passed after changes, not passed.
- **To the maker, after the second look:** fix F1 to F3 (must change) and F4 to F7 (should change), F8 to F10 if trivial; rerun the checks; add one line per finding to the answers file; report the exact changed line ranges; keep everything staged, write no receipt.
- **To the same second-look reviewer, for the final look:** read only the listed changed lines; say whether each does what its finding asked and makes nothing newly wrong; rerun the copying check and `run_all_checks.py`; anything short of a must-change is recorded as open.
