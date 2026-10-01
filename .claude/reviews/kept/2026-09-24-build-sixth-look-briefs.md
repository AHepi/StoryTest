# The sixth look at the error-correction build: briefs, their four checks, and the copy script, 24 September 2026

What this is: the briefs as sent, the four checks of them by theory-checker (each word for word; the reviewers were started only when a check found no must-change), and the script every reviewer used to make a safe copy of the workshop. Kept for log entries 32 and 33.

---

## 1. The briefs, as sent

# Briefs for the sixth look (the last full look at the build), revised after the brief check

## Shared part (every brief begins with this)

You are reviewing work in a story workshop: Claude Code skills in `/home/user/StoryTest/.claude/skills/`, built on the owner's theories in `/home/user/StoryTest/sources/`. The owner is not a programmer. CLAUDE.md in the repository gives the rules; you get it at start. You did not make any of this work: the lead agent did. Nobody grades their own work, so your report is the review.

**What you are looking at.** A build that puts error correction (a process) and hard to vary (a metric) into the workshop: the `error-correction` skill, a commit gate (checks git runs by itself before every commit), review receipts, and records. It is not yet committed. It has had five looks by independent agents; each found faults, and many were made by the answers to the look before. This sixth look starts from the edits that answered the fifth look. A fault older than these edits that you meet while checking them is reported and graded the same way: the fifth look's worst fault was older than its diff.

- The edits: `git -C /tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/rereview diff c52f191 26bf4fd` (35 files; a snapshot repository whose commit 26bf4fd matches the live tree at `/home/user/StoryTest`). Three small changes in it were made while these briefs were being checked, and answer no fifth-look finding, so the lead's account below does not cover them: the rule card's case in `writing-rules-and-rivals.md`, section 1; the plot trap "Surprise by default" in plot `SKILL.md`; and the refusal hook's rule for a hooks folder named with `$PWD` (`.claude/hooks/refuse_check_bypass.py`), with two planted tests in `test_checks.py` (`git -C /tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/rereview diff aab01cd 26bf4fd` shows these, and the counts in `27 Corrections.md` and the project story that follow from the two new tests). That snapshot repository is shared by four reviewers at once: read it, or clone it into your own folder; never commit, check out or change anything in it.
- What the fifth look found, word for word: `/home/user/StoryTest/.claude/reviews/kept/2026-09-24-build-fifth-look.md`. The plan for answering it, written before any change: section 3 of `/home/user/StoryTest/.claude/reviews/kept/2026-09-24-build-fifth-look-briefs-and-plan.md`.
- The lead's account of how each finding was answered: `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/findings-answered-round5.md`. Every statement in it is the lead's claim, to check, not a fact: "applied", "does not bear yet", "passed; no change", "answered by", the reasons given for what was not done, and the counts.
- The workshop's record of its own errors: `/home/user/StoryTest/27 Corrections.md` (the kinds table at the top; C1, C5, C12, C13 and C15 changed in this round), and the log's new entry 32 and the status lines in `/home/user/StoryTest/StoryTest - project story.md`.
- These briefs are in `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/briefs-round6.md`. Apart from them, the lead's account named above, the shared snapshot `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/rereview` (read only), the copy script named below, and your own folder `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/r6-<the name your brief gives>/`, read no other file in the scratchpad folder: it holds the lead's working notes, other reviewers' old copies and the trial's held-back files.

**The kinds of error this workshop has made**, each with what the kinds table in `27 Corrections.md` says catches it now (look for each in your area; where the catch is a reviewer, that reviewer may be you; where each was seen, and when last, is in the table itself):
- **An owner term used in a neighbouring sense, or a theory narrowed or turned round (the commonest kind).** Caught now by: `theory-checker` with the term sheet (`references/owner-terms.md`), whose review receipt the commit gate demands (on trust, with a trace); kept cases 02, 06 and 07, and 04, 08 and 09 once their defects are replaced (C14)
- **A claim credited to the wrong theory, book or person.** Caught now by: `theory-checker`, reading the theory before the change; the term sheet's "Who said it" table; `check_owner_quotes.py` for the sheet itself (by itself)
- **A book rule adopted as law, failing the owner theory's own case.** Caught now by: the rule card in `references/writing-rules-and-rivals.md` (on trust, with a trace in the receipt); kept cases 01, 03
- **A rival that misstates a side or cannot tell the two views apart.** Caught now by: the rival form in `references/writing-rules-and-rivals.md`; `theory-checker` (on trust, with a trace)
- **Close paraphrase of a book that the 8-word script cannot see.** Caught now by: `copy-checker` where the books are present; the receipt's "Book text" line where they are not (on trust, with a trace); 8-word runs by `overlap_check.py` (by itself where the books are present)
- **A change (a fix) that makes a new error; a rule changed in one place but not its copies.** Caught now by: the review receipt tied to the exact change, which the commit gate demands (on trust, with a trace: the reviewer's report is pasted in); the shared-passage check in `check_maps.py` (by itself); the search for restatements in the loop's step 4 (on trust)
- **A brief that carries an error to many agents; a lesson that reaches the checkers but not the makers.** Caught now by: the brief check by `theory-checker` in `references/reviews-and-briefs.md`, with this table and the term sheet in every brief (on trust)
- **A contradiction between skills that no single-skill review can see.** Caught now by: `theory-checker`'s search of the other skills for the changed rule; `use-tester` (on trust, with a trace); kept case 05
- **A pointer that lands nowhere or on the wrong thing.** Caught now by: `check_maps.py` for paths, map rows and section numbers, and `check_records.py` for README (by itself); what a section says is not checked by any script
- **A record that is stale, unfinished, or leaves out who made an error.** Caught now by: `check_records.py`: the log only added to, numbered files with their entries (by itself); status lines stamped "(as of entry N)" and printed whenever a new entry appears (on trust, with a trace: the stamp forces a look, not what it finds); the "made by" part of a correction (on trust)
- **A test that can only agree: cases or examples drawn from the answer, or a fix confirmed on the case that made it.** Caught now by: kept cases written by an agent that had not read the skills, and never given to writers or fixers; `use-tester` compares a change with them (on trust)
- **A required check skipped, or a claim reported without its receipt, with an assumed input, or with agreement between checks that were not independent.** Caught now by: the "Checks run on these notes" section every write-up needs (by itself, `check_records.py`); the reply check in every craft skill (on trust, with a trace in the reply); the after-commit hook's reminder (by itself, but advisory)
- **A check that passes while the thing is wrong, or can be got round.** Caught now by: `test_checks.py`, which plants each fault, the ways round each check, and an innocent neighbour, and runs the gate's own planted-fault stage for real once; the last approved commit's copy of it is run by the commit gate whenever the checks differ from that commit's, and a check change must come alone (by itself, within one commit; across commits, on trust: the receipt, plus the planted faults). An agent set on getting round the gate is beyond it (S10)
- **A check or a step that stops honest work, or leaves no way through.** Caught now by: an innocent neighbour in `test_checks.py` for each (by itself); `use-tester` walking the process through everyday situations (on trust, with a trace in its report)
- **Acting on cut-off or missing evidence.** Caught now by: the claim check in the skill and the after-commit hook (on trust; the hook is advisory)
- **The owner's request misread, or a local patch for a fault in the workshop's stages.** Caught now by: saying the request back (CLAUDE.md, on trust); the loop's step 3, "where did it get through?" (on trust)
- **An edit to a frozen text.** Caught now by: `.claude/hooks/protect_frozen_files.py` and `check_frozen_files.py` at every commit, reading the contents as committed and comparing them with the last approved commit, so an edit made outside the gate stops the next commit until it is put back (by itself)
- **A commit that skips the gate, or arrives where it cannot see (a fast-forward, a cherry-pick, a commit made on GitHub).** Caught now by: the gate's stamp, which names the exact contents it approved; the gate, which compares the files with the last approved commit (found by walking back along the main line, where a merge made on GitHub with no conflict counts as approved, so such a merge does not hide it), so what such a commit got wrong in the files stops the next commit until it is put right, apart from a check it loosened, which only the planted-fault test and its late review judge; and `recheck_commits.py`, which asks each commit since then for its review receipt, checks a claimed withdrawal against the files, and reports book files and changes to the gate's own files (by itself, but after the fact); a Claude hook refusing the usual ways of skipping (usual spellings only). A commit made outside the gate that changes the gate's own files, or a stamp typed by hand, is beyond it: only a check outside the repository (S10) or the owner would see those

**How to grade each finding.** The stopping rule, decided before this round's changes: after this look, a must-change is put right and looked at again, narrowly; anything less is recorded as open (in the build's review receipt and the correction's status line), for a later change with its own review, and the build is committed with it open. So:
- **must change:** a way round the gate beyond the limits its description stated before this round (`references/checks-and-cases.md`, section 2, "What the gate cannot do", as it was at c52f191; a limit added in this round counts only if you judge it a true limit, and say so); an honest route with no way through; a false statement in any text in the change that the lead wrote or changed (a skill, a record, CLAUDE.md, README, file 26, an agent's definition, the notes in scripts and hooks; a false claim inside a kept reviewer's report is reported, not changed, since the record is kept word for word); a text that contradicts an owner theory, uses an owner term in a neighbouring sense, narrows, widens or turns round what a theory says, credits a claim to the wrong theory, book or person, or states a workshop reading without labelling it as one; copied or closely paraphrased book text; a fifth-look finding the lead says is answered that is not answered at all (one answered only in part: give the missing part its own grade on this scale);
- **should change:** anything else that bears and would mislead or stall someone using the workshop;
- **minor:** bears, but misleads no one (a stale word, a pointer that still lands);
- **does not bear:** say why;
- **does not bear yet:** needs a fact nobody has. Run the test that would settle it in your copy if you can; if you cannot, name the test and say which grade the finding would take if it bears.
End with one verdict for your area: **passed** (no must-change), **passed after changes** (passed once the must-changes you list are made), or **not passed**.

**How to report.** For each finding: target (file and line), defect, grounds (a theory line, a case, or a command and what it printed), connection, and grade. Then: the fifth-look findings in your area, each answered, answered in part, or not; the marks on any new or changed rule (held, held if, two routes, loose, idle, unknown, with what holds it); what you checked and found right; what you did not check.

**Rules while you work.**
- Never edit, stage, commit or switch branches in `/home/user/StoryTest`, never change its git settings, and run nothing there that writes files, `.git` included. The gate's script writes a record into `.git` of whatever repository it runs in, and a commit made within two minutes of it can be stamped: so never run `check_commit.py`, `test_checks.py` or any git command that writes with the live repository as its folder.
- Make every copy of the workshop with the lead's copy script: `sh /tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/make_review_copy.sh /tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/r6-<the name your brief gives>/<a new folder name>`. It clones the live history, removes every remote and switches pushing off, copies in the live files as they are now (not the books), and commits them through the gate in the copy, so the copy's last commit is approved as the build would be; that commit takes about three and a half minutes. Never make a copy another way, and never copy the live folder with its `.git`: a copied `.git` keeps the live repository's link to the real GitHub. To make a further copy of your own copy, clone it with `git clone --no-local`, and then remove the clone's remote (`git -C <new copy> remote remove origin`) unless you mean it to stand for GitHub. If you ever work in a copy made otherwise, first run `git -C <copy> remote -v` and remove every remote it lists.
- Play GitHub with a bare repository inside your own folder (`git init --bare <your folder>/github.git`, added to your copies as a remote named `github`), and always name that remote when you push or pull (never a bare `git push` or `git pull`). Never push into `/home/user/StoryTest` or the shared snapshot, never add either as a remote, and never touch the real GitHub: no push to it, no `gh`, no GitHub tools.
- Your shell may go back to `/home/user/StoryTest` before each command. The workshop's scripts (`check_commit.py`, `recheck_commits.py`, `run_all_checks.py`, `test_checks.py`, `review_receipt.py` and the checks they run) take their repository from the folder they run in, and run the checks beside them: so start every command that runs one with `cd <your copy> &&`, and run your copy's own script, never the live repository's. Use `git -C <your copy>` or full paths for everything else. To switch the gate on in a copy: `git -C <copy> config core.hooksPath .githooks` (the copy script does this). To make a commit there as GitHub would, with no gate: `git -C <copy> -c core.hooksPath=/dev/null commit ...`.
- The hooks read their folders from their input instead: the two that guard commands and edits take the working folder from the JSON's `"cwd"` and the project from `CLAUDE_PROJECT_DIR`, and session start falls back to `CLAUDE_PROJECT_DIR`. Try a hook only by piping the JSON Claude Code would send to your copy's hook script, run with `cd <your copy> &&`, with `CLAUDE_PROJECT_DIR` set to your copy and `"cwd"` set to your copy or any folder inside it, never `/home/user/StoryTest`: never by running the command the hook guards.
- `test_checks.py` takes about three and a half minutes, and so does a commit through the gate in a copy that brings in or changes checks (the gate runs the planted-fault test inside it); when `test_checks.py` itself changes, the gate runs both the old and the changed test, about seven minutes. Give those a longer time limit than the usual two minutes, or run them in the background.
- Say at the end what you left behind.
- Never copy book text (the books are in `/home/user/StoryTest/sources/raw/`, which git ignores) into anything you write.
- Plain words: the owner reads the results through the lead. Name a technical thing once in plain words.
- Read the owner theory before the passage that cites it. The term sheet is `/home/user/StoryTest/.claude/skills/error-correction/references/owner-terms.md`.
- Where a list below names places to check, it is a starting point: search the whole repository (outside `.claude/reviews/kept/` and `kept-cases/runs/`) for every other statement of the same thing.

## Brief A: theory-checker

Your area: what the texts say. Name: `theory-checker`.

**Term sheet rows for your area, word for word:**
> ### 1.1 Promise
> **Owner:** Gap theory (`gap-theory-of-narrative.md`), principle 5 Promise; Part 2 section 4.
> - **Own words:** “Every open question carries a promise, and emphasis is what sets it.” (Gap, Part 2 section 4)
> - **In plain words:** an open question the story presses (lingers on, has characters chase, keeps bringing back) is promised an answer; one mentioned in passing and never pressed is promised to stay open. Breaking either promise feels like betrayal (principle 5).
> - **Not to be confused with:** a guarantee (1.2); an expectation (1.3); the Bond theory's promise (1.4).
> - **Telling test:** If it went, would the audience feel *cheated* (a promise) or *unsafe* (a guarantee)? And where did it come from: set by emphasis inside this story (the theory's promise), or brought by the genre before page one (the workshop's stretch)?
> - **Open:** for open questions, settled by the theory. Stretching *promise* to the moments a genre owes and to set-ups is the workshop's reading, Q7. The name *expected mystery* is S8.
> - **Owning skill:** plot (`plot/references/reveals-and-withholding.md`, section 2) for the theory's own sense, open questions set by emphasis; genre (Words: *promise*, *expected mystery*) for the workshop's stretch to the moments a genre owes, Q7. The cheated-or-unsafe test is the workshop's, in `genre/references/how-genres-work.md` section 2.

> ### 1.2 Guarantee (and the theory's "contract")
> **Owner:** Anticipation theory (`anticipation-theory.md`), principle 5 Broken contract; Part 2 section 5.
> - **Own words:** “Genres carry unspoken guarantees: the star survives, the child is safe, the dog lives.” (Anticipation, Part 2 section 5)
> - **In plain words:** a protection the audience assumes, so part of it relaxes. The principle's name, *contract*, means this set of protections: “Fear needs the audience to believe the genre's usual protections are gone.” (Anticipation, principle 5). It is not a promise to answer anything. Break one early and convincingly and every later threat is real.
> - **Not to be confused with:** a promise (1.1); the bond as a promise (1.4).
> - **Telling test:** cheated or unsafe, as in 1.1. A second test catches the reading turned round (H14): after the break, *could* anyone die (the aim of the principle), or *do* characters die all the time? Only the second makes care collapse: “Break one guarantee convincingly rather than all of them.” (Anticipation, Part 2 section 5)
> - **Open:** early breaks, settled by the theory. A guarantee broken at the end giving weight or grief is the workshop's extension, S5.
> - **Owning skill:** genre (Words: *guarantee*).

> ### 2.1 Departure (and the baseline)
> **Owner:** Implied World theory (`implied-world-theory.md`), Key terms; principle 1 Minimal departure. The Gap theory's departure gap (reality against the world) is the same difference seen as a layer.
> - **Own words:** “any way the fictional world differs from the baseline” (Implied World, Key terms, Departure)
> - **In plain words:** a standing difference from the baseline, which is “what the audience assumes by default” (Implied World, Key terms, Baseline): a magic system, a political order, a ruined climate, a slang. It is true on an ordinary day before the story starts.
> - **Not to be confused with:** the breach (2.2); pressure (2.3). The Gap theory calls the breach a second level of departure (2.2); on its own, *departure* means the first level, the world against reality.
> - **Telling test:** Is it true on an ordinary day before anything happens (a departure), or does it happen against that day's normal (a breach)? *Dune*'s shortage of water is a departure; a rich single man moving into Netherfield is a breach. A dragon attack is a breach in our world; in a world full of dragons it might be weather. A water shortage or overpopulation does not become the breach by being dramatic (H16).
> - **Open:** settled by the theory. That a scene of the world at its own business "changes the departure gap" is the workshop's reading, Q1 (b); never state it as the theory's (H27).
> - **Owning skill:** story-world (Words: *baseline*, *departure*); genre (Words).

> ### 2.2 Breach (and the world's own normal)
> **Owner:** Gap theory, principle 2 Breach; the five gaps table; Part 2 section 2.
> - **Own words:** “A story is a departure from the world's *own* normal.” (Gap, principle 2)
> - **In plain words:** what happens that breaks the normal of the fictional world, departures included. The normal is the world's (“what's possible, normal and valued” (Gap, Terms, World)), not the audience's baseline. The breach produces stakes and a reason to tell the story.
> - **Not to be confused with:** a departure; a broken guarantee (the Anticipation theory's broken contract); a broken promise.
> - **Telling test:** Measured against what? Against the audience's real world plus the genre's habits: a departure. Against the fictional world's own everyday: a breach.
> - **Open:** settled by the theory.
> - **Owning skill:** plot (Words: the five gaps).

> ## 7. Dread, the suspense of helplessness, dread by proxy (Q6)
> 
> **Owners:** Anticipation theory, the fear ladder and principle 6 (Part 2 section 6); Gap theory, the five gaps table (Knowledge row).
> - **Own words:**
>   - The dread rung: “Something is wrong, but not what” (Anticipation, the fear ladder, Dread row)
>   - What the knowledge gap produces: “Dramatic irony, dread” (Gap, the five gaps table, Knowledge row), with Hitchcock's bomb, where the audience is ahead.
>   - Audience ahead: “suspense of helplessness. We fear *for* the character” (Anticipation, Part 2 section 6)
>   - Audience behind: “(the character sees something we can't): dread by proxy” (Anticipation, Part 2 section 6)
>   - Audience level: “shared terror. We fear *with* the character” (Anticipation, Part 2 section 6)
> - **Not to be confused with:** each other; the terror rung (8.1); shock (11.4).
> - **Telling test:** Who knows more? Nobody knows what the threat is: the dread rung. The audience knows and the character doesn't: the suspense of helplessness (the Gap table's *dread*). The character knows and the audience doesn't: dread by proxy. Both know the same: shared terror. Change one thing: show the audience the killer in the closet, and a dread-rung scene becomes the suspense of helplessness.
> - **Nearby:** *residue*, the ladder's last row and principle 8: “Fear outlasts the story when the threat could exist in the audience's own world” (Anticipation, principle 8). Whether a monster meets this through what it stands for is S4.
> - **Open:** Q6 (now (a): *dread* for the rung only; *the suspense of helplessness* for the audience ahead). Write *dread by proxy* in full for the audience behind.
> - **Owning skill:** plot (`references/suspense-and-fear.md` sections 2 and 6; the plot Words paragraph does not define these).

> ### 10.1 Tension (S1)
> **Owner:** Anticipation theory, principle 7 The ratchet; Part 2 section 7. The theory does not define it.
> - **Own words:** “Tension should rise in steps with partial releases” (Anticipation, principle 7)
> - **In plain words:** the workshop's reading: the felt level of suspense or fear at a moment, the thing the ratchet raises and eases.
> - **Not to be confused with:** suspense in the equation (10.2); pressure (2.3); stakes (cost, 5).
> - **Telling test:** Would a false alarm lower it? The Lewton bus eases tension for a moment and leaves the threat where it was; the real threat arrives in that release.
> - **Open:** S1.
> - **Owning skill:** plot (`references/suspense-and-fear.md` section 7; not in the Words paragraph).

> ### 10.2 Suspense: three uses
> **Owners:** Gap theory, Part 2 section 3 (Sternberg), and the Withholding row of the five gaps table; Anticipation theory, the suspense equation and the fear ladder.
> - **Own words:** “a gap about the future” (Gap, Part 2 section 3); “Suspense = Care × Threat × Uncertainty × Time” (Anticipation, the suspense equation); “What the threat is, but not how it ends” (Anticipation, the fear ladder, Suspense row)
> - **In plain words:** Sternberg's suspense is any open question about the future; the equation's suspense needs all four terms above zero; the suspense rung is one step of the fear ladder.
> - **Not to be confused with:** each other; curiosity (a gap about the past); surprise (11.4); tension (10.1).
> - **Telling test (H12, H15):** Tell the audience the ending. Suspense does not fall to zero: “Uncertainty can also move from *whether* to *how*.” (Anticipation, Part 2 section 1). A claim that knowing the outcome removes uncertainty turns the theory round.
> - **In use:** write *the suspense rung* when the rung is meant (genre, Words).
> - **Open:** settled by the theories.
> - **Owning skill:** plot (Words mention Sternberg's sense; `references/suspense-and-fear.md` sections 1 and 2).

> ### 11.4 Surprise, three times
> **Owners:** Gap theory, Part 2 section 3 (Sternberg); Anticipation theory, the fear ladder (Shock); Bond theory, principle 7.
> - **Own words:** “you thought you understood and you were wrong” (Gap, Part 2 section 3); “Nothing: it arrives without warning” (Anticipation, the fear ladder, Shock row); “Care grows when a character does something unexpected that still makes sense for them.” (Bond, principle 7)
> - **Telling test:** Did the audience think it understood and turn out wrong (the Gap theory's surprise), get no warning at all (shock, the side rung), or see a character do something unexpected that still fits them (the Bond theory's surprise)? If the act does not fit and the story has not earned it, the audience calls it “out of character” (Bond, Part 2 section 7), and the bond breaks.
> - **Open:** settled, but two uses overlap (section 13). **Owning skill:** plot (`references/reveals-and-withholding.md`; `references/suspense-and-fear.md`); character (`references/change-and-growth.md`).

> ## 12. Who said it
> 
> Claims that were credited to the wrong theory before, or easily could be.
> 
> | Claim | Belongs to | Not to |
> |---|---|---|
> | Care has to be built before the threat arrives | Anticipation, Part 2 section 1 | Bond or Gap (H6) |
> | The world decides what things cost; without a world, nothing sets the price | Gap, principle 2 and Part 2 section 2 | Implied World (H20) |
> | Care is what makes the gaps worth closing | Bond, How it fits with the others | Gap (H20) |
> | A character is a desire the world has shaped, chasing what the world resists | Gap, Part 2 section 2 | Bond |
> | The world shouldn't care about the hero, but the audience must | Bond, How it fits (turning Implied World principle 4 round) | Implied World |
> | The Worry rung is the equation's care term | Bond, under the ladder | Anticipation |
> | Ahead, level, behind (the knowledge positions) | Anticipation, principle 6 (the gap itself is Gap's) | Gap |
> | The threat's rules work like mysteries, its nature like wonders | Anticipation, Part 2 section 3 (using Gap's distinction) | Gap alone |
> | Horror as a world whose rules turn against its people | Anticipation, Part 2 section 4 (framed in Implied World terms) | Implied World's own text |
> | Characters' reactions cue ours | Carroll, used by Anticipation (Part 2 section 6) and Bond (Part 2 section 5) | |
> | Minimal departure | Ryan, used by Implied World | |

And from section 13, its opening and item 9:

> ## 13. Where the theories themselves leave a term unclear
> 
> All of these are put to the owner together under S13 in the questions file; an item that is also a question of its own gives that number.
> 
> 9. **Surprise:** both theories call Hitchcock's bomb that simply goes off a surprise, “fifteen seconds of surprise” (Gap, Part 2 section 3) and “you get seconds of surprise” (Anticipation, Part 2 section 1), yet the Anticipation theory's side rung for a threat that “arrives without warning” (Anticipation, the fear ladder, Shock row) is Shock. The Bond theory uses *surprise* for a third thing (principle 7).

**The fifth-look findings to check in your area:** theory-checker V1 to V8, V10 to V18, V20 to V22 (their texts); use-tester 6, 7, 10 and 11 and its stall items (the texts); copy-checker D1 (`.claude/agents/copy-checker.md`).

1. **The plot rule and its copies.** Start from `/home/user/StoryTest/.claude/skills/plot/references/reveals-and-withholding.md` sections 1, 2 and 6; plot `SKILL.md` step 4, the diagnosing table's row for a twist that came from nowhere, the quick version's "A twist that fails", and the traps (including "Surprise by default"); `references/suspense-and-fear.md`; and the rule card's case in `.claude/skills/error-correction/references/writing-rules-and-rivals.md`, section 1. Then search for every other statement of the planting rule and its exemption. Walk cases through the new wording, among them: the theories' own (the bomb shown and unshown; the jump scare; *Psycho*; Joffrey; the Lewton bus; Gap line 47, a dragon attack that in a world full of dragons "might be weather"; Implied World lines 12 and 20, the baseline and minimal departure, and line 36, medieval Europe with dragons riding on the genre's defaults; Gap line 61, *Planet of the Apes*, a reveal about the world) and the fifth look's (dragons from nowhere mid-story in a world like ours; dragons that decide the climax; a rescue at the climax; a character reveal). Are the workshop's readings labelled as such, and does each credit go to the right theory or book?
2. **File 26 against the break test.** First read the break test itself (`/home/user/StoryTest/.claude/reviews/kept/2026-09-24-catch-break-test.md`), field by field, and write your own list of what each field asks of file 26 (`/home/user/StoryTest/26 Test - The Catch - two versions.md`), before you open the lead's table (`.claude/reviews/kept/2026-09-24-catch-break-test-applied.md`). Then check file 26 against your list, and the table against both. Run the write-up checks on the sentences changed in this round: the stock-note test (would it fit any script?), the flip (would you be as sure of the opposite? For example: had the other version had the line, would the note praise it; had the other draft come first, would the same evidence read the other way?), and a verdict given both ways where it needs an input nobody gave. Read every sentence that compares the two versions for words that assume which came first.
3. **What the gate does and cannot do.** Start from `references/checks-and-cases.md` section 2 (rewritten as a whole) and section 3; the error-correction skill's Words, its list of what is not a tripwire, and its tables; `references/reviews-and-briefs.md` sections 2 and 4; CLAUDE.md's table and closing paragraph; README; the notes at the top of `check_commit.py`, `recheck_commits.py`, `run_all_checks.py`, `.githooks/pre-commit`, `pre-merge-commit`, `prepare-commit-msg`, `.claude/hooks/session_start.py` and `refuse_check_bypass.py`; the project story's word list ("Last approved commit"); and the kinds rows in `27 Corrections.md`. Then search for others. Do they agree with each other, and with what the scripts do? Does any still claim to be complete?
4. S10 in `22 Questions - meanings only you can settle.md`, and section 2, step 3 of `references/owner-answers-and-revisions.md` (the steps for an owner answer).
5. **The records:** C1, C5, C12, C13 and C15, the kinds rows, entry 32 and the status lines. Is each claim true, and does each say who made the error and what caught it?

## Brief B: use-tester

Your area: walking situations through the changed procedures, in scratch copies, to find advice an owner theory would reject, steps that stall, and routes with no way back. Name: `use-tester`.

**Term sheet rows for your area, word for word:**
> ### 2.1 Departure (and the baseline)
> **Owner:** Implied World theory (`implied-world-theory.md`), Key terms; principle 1 Minimal departure. The Gap theory's departure gap (reality against the world) is the same difference seen as a layer.
> - **Own words:** “any way the fictional world differs from the baseline” (Implied World, Key terms, Departure)
> - **In plain words:** a standing difference from the baseline, which is “what the audience assumes by default” (Implied World, Key terms, Baseline): a magic system, a political order, a ruined climate, a slang. It is true on an ordinary day before the story starts.
> - **Not to be confused with:** the breach (2.2); pressure (2.3). The Gap theory calls the breach a second level of departure (2.2); on its own, *departure* means the first level, the world against reality.
> - **Telling test:** Is it true on an ordinary day before anything happens (a departure), or does it happen against that day's normal (a breach)? *Dune*'s shortage of water is a departure; a rich single man moving into Netherfield is a breach. A dragon attack is a breach in our world; in a world full of dragons it might be weather. A water shortage or overpopulation does not become the breach by being dramatic (H16).
> - **Open:** settled by the theory. That a scene of the world at its own business "changes the departure gap" is the workshop's reading, Q1 (b); never state it as the theory's (H27).
> - **Owning skill:** story-world (Words: *baseline*, *departure*); genre (Words).

> ### 1.2 Guarantee (and the theory's "contract")
> **Owner:** Anticipation theory (`anticipation-theory.md`), principle 5 Broken contract; Part 2 section 5.
> - **Own words:** “Genres carry unspoken guarantees: the star survives, the child is safe, the dog lives.” (Anticipation, Part 2 section 5)
> - **In plain words:** a protection the audience assumes, so part of it relaxes. The principle's name, *contract*, means this set of protections: “Fear needs the audience to believe the genre's usual protections are gone.” (Anticipation, principle 5). It is not a promise to answer anything. Break one early and convincingly and every later threat is real.
> - **Not to be confused with:** a promise (1.1); the bond as a promise (1.4).
> - **Telling test:** cheated or unsafe, as in 1.1. A second test catches the reading turned round (H14): after the break, *could* anyone die (the aim of the principle), or *do* characters die all the time? Only the second makes care collapse: “Break one guarantee convincingly rather than all of them.” (Anticipation, Part 2 section 5)
> - **Open:** early breaks, settled by the theory. A guarantee broken at the end giving weight or grief is the workshop's extension, S5.
> - **Owning skill:** genre (Words: *guarantee*).

> ## 7. Dread, the suspense of helplessness, dread by proxy (Q6)
> 
> **Owners:** Anticipation theory, the fear ladder and principle 6 (Part 2 section 6); Gap theory, the five gaps table (Knowledge row).
> - **Own words:**
>   - The dread rung: “Something is wrong, but not what” (Anticipation, the fear ladder, Dread row)
>   - What the knowledge gap produces: “Dramatic irony, dread” (Gap, the five gaps table, Knowledge row), with Hitchcock's bomb, where the audience is ahead.
>   - Audience ahead: “suspense of helplessness. We fear *for* the character” (Anticipation, Part 2 section 6)
>   - Audience behind: “(the character sees something we can't): dread by proxy” (Anticipation, Part 2 section 6)
>   - Audience level: “shared terror. We fear *with* the character” (Anticipation, Part 2 section 6)
> - **Not to be confused with:** each other; the terror rung (8.1); shock (11.4).
> - **Telling test:** Who knows more? Nobody knows what the threat is: the dread rung. The audience knows and the character doesn't: the suspense of helplessness (the Gap table's *dread*). The character knows and the audience doesn't: dread by proxy. Both know the same: shared terror. Change one thing: show the audience the killer in the closet, and a dread-rung scene becomes the suspense of helplessness.
> - **Nearby:** *residue*, the ladder's last row and principle 8: “Fear outlasts the story when the threat could exist in the audience's own world” (Anticipation, principle 8). Whether a monster meets this through what it stands for is S4.
> - **Open:** Q6 (now (a): *dread* for the rung only; *the suspense of helplessness* for the audience ahead). Write *dread by proxy* in full for the audience behind.
> - **Owning skill:** plot (`references/suspense-and-fear.md` sections 2 and 6; the plot Words paragraph does not define these).

> ### 10.2 Suspense: three uses
> **Owners:** Gap theory, Part 2 section 3 (Sternberg), and the Withholding row of the five gaps table; Anticipation theory, the suspense equation and the fear ladder.
> - **Own words:** “a gap about the future” (Gap, Part 2 section 3); “Suspense = Care × Threat × Uncertainty × Time” (Anticipation, the suspense equation); “What the threat is, but not how it ends” (Anticipation, the fear ladder, Suspense row)
> - **In plain words:** Sternberg's suspense is any open question about the future; the equation's suspense needs all four terms above zero; the suspense rung is one step of the fear ladder.
> - **Not to be confused with:** each other; curiosity (a gap about the past); surprise (11.4); tension (10.1).
> - **Telling test (H12, H15):** Tell the audience the ending. Suspense does not fall to zero: “Uncertainty can also move from *whether* to *how*.” (Anticipation, Part 2 section 1). A claim that knowing the outcome removes uncertainty turns the theory round.
> - **In use:** write *the suspense rung* when the rung is meant (genre, Words).
> - **Open:** settled by the theories.
> - **Owning skill:** plot (Words mention Sternberg's sense; `references/suspense-and-fear.md` sections 1 and 2).

> ### 11.4 Surprise, three times
> **Owners:** Gap theory, Part 2 section 3 (Sternberg); Anticipation theory, the fear ladder (Shock); Bond theory, principle 7.
> - **Own words:** “you thought you understood and you were wrong” (Gap, Part 2 section 3); “Nothing: it arrives without warning” (Anticipation, the fear ladder, Shock row); “Care grows when a character does something unexpected that still makes sense for them.” (Bond, principle 7)
> - **Telling test:** Did the audience think it understood and turn out wrong (the Gap theory's surprise), get no warning at all (shock, the side rung), or see a character do something unexpected that still fits them (the Bond theory's surprise)? If the act does not fit and the story has not earned it, the audience calls it “out of character” (Bond, Part 2 section 7), and the bond breaks.
> - **Open:** settled, but two uses overlap (section 13). **Owning skill:** plot (`references/reveals-and-withholding.md`; `references/suspense-and-fear.md`); character (`references/change-and-growth.md`).

**The fifth-look findings to check in your area:** use-tester 1 to 13 and its stall items; theory-checker V7, V8 and V22.

Build your copies with the copy script (shared part), and play GitHub with your own bare repository, committing there with the gate switched off, as the shared part says.

1. **Situations nobody has walked yet** (most of your time goes here):
   - GitHub's "Update branch" button, which merges the main line into a session's branch, so the merge's first parent is the session branch;
   - the next pull request merged on GitHub after an owner's edit made there, so one parent of the merge is not approved;
   - "Squash and merge" and "Rebase and merge" on GitHub;
   - three sessions at once, each adding a log entry, merged in different orders;
   - a revert made on GitHub;
   - the owner's correction to a broken gate script brought in with a plain `git pull` into a local branch that has moved on (the test that settles V22), and with `git pull --rebase`;
   - any other ordinary shape of work you think of.
2. **Quiet neighbours, where nothing should fire:** a fast-forward; an ordinary run of commits through the gate; a fresh clone's first session.
3. **The fixes, only where no planted test covers them.** The lead's account names planted tests; before you skip a case, confirm the named test exists in `test_checks.py` or `test_the_gate.py` and plants that case. Then walk: the owner answers a question (section 2, step 3 of `references/owner-answers-and-revisions.md`); session start after a pull brings a note; the route for a wrong check after a merge made on GitHub with a conflict, walked as an agent would read it in section 2.
4. **The plot changes, walked as a writer would:** a jump scare in a film and in prose; dragons from nowhere mid-story; dragons that decide the climax; a rescue at the climax; a twist about a character; and a near neighbour where the exemption should apply.
5. **The trial's second half:** read `/home/user/StoryTest/.claude/reviews/kept/2026-09-24-trial-first-half-fingerprints.md`. Could that half's agent, working in a copy without `.claude/reviews/kept/`, still find the planted problems or their answers? Search the rest of the repository for anything that would give them away (do not open the scratchpad's trial files).

## Brief C: scripts and hooks (a general-purpose agent)

Your area: the scripts and hooks changed in this round, and their planted tests. Name: `scripts`.

**The fifth-look findings to check in your area:** scripts 1 to 15; theory-checker V9, V16 (the counts) and V19; use-tester 4, 5, 9 and 12.

Files: `check_commit.py`, `recheck_commits.py`, `run_all_checks.py`, `check_records.py`, `check_frozen_files.py`, `review_receipt.py`, `test_checks.py` and the new `test_the_gate.py` (in `/home/user/StoryTest/.claude/skills/error-correction/scripts/`); `overlap_check.py` (add-source); `.githooks/pre-commit`, `prepare-commit-msg`, `pre-merge-commit`; `.gitattributes`; `.claude/hooks/session_start.py` and `refuse_check_bypass.py`; and `references/checks-and-cases.md` section 3.
1. Confirm the counts in C15 and entry 32: `test_checks.py` on the current scripts (in a copy made with the copy script, or a plain file copy of its working tree), and on the scripts as the fifth look saw them (`git -C <snapshot> archive c52f191 | tar -x -C <your folder>/old`, with the two new test files put in; run it there with `cd <your folder>/old &&`). Which new tests pass on the old scripts too, and does any fail on the old scripts for a reason other than the fault it plants?
2. Try to get round each new rule:
   - the last approved commit, found along the main line, with a merge made without the gate counted as approved when it is exactly git's automatic merge of approved parents: look for merges it wrongly counts or wrongly refuses (an octopus merge, a parent from before the gate, git without `merge-tree --write-tree`, a merge whose first parent is the session branch, a merge of two reviewed check changes);
   - git's staging area passed for `commit -a` and `commit <file>` (and `--include`, `--only`, `--amend -a`);
   - the result file pre-commit reads;
   - the other side's log entries in a merge through the gate;
   - the hooks check;
   - the Book-text register read before and after;
   - the refusal hook's `$PWD` rule;
   - the frozen check's way back;
   - the split of the planted-fault test: does the gate run the last approved commit's `test_the_gate.py`, or could a staged or on-disk copy be run instead?
3. Check that `recheck_commits.py` and `check_commit.py` apply the same approval rule, and that session start gets it from the recheck.

## Brief D: copy-checker

Your area: copying from the books, and whether each book is credited only for what it says. Name: `copy-checker`.

**The fifth-look findings to check in your area:** copy-checker C1 to C6 (still true after the edits) and D1 to D4.

1. The plot passages changed in this round: `git -C /tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/rereview diff c52f191 26bf4fd -- .claude/skills/plot/`, and the rule card's case in `.claude/skills/error-correction/references/writing-rules-and-rivals.md`. The new sentences credit Egri (foreshadowing called a promise; his case of the murder weapon) and restate the Implied World theory's baseline.
2. Run the overlap script against every book at 8 words and at 6 (`python3 /home/user/StoryTest/.claude/skills/add-source/scripts/overlap_check.py --run-length 6 <book> <files>`, the run length right after the script's name), on the changed files, from your copy.
3. Read the changed lines against the books for close paraphrase: a passage that follows an author's sentence order, or a list in the author's order and wording.
4. Check each credit to a book against the book: does the book say it, and is the label right (fitted, built or asserted for a book's claim; "the workshop's reading" for the workshop's own)?
Report each finding with target, defect, grounds, connection and grade, then what you ran and what it printed, and what you did not check.

## 2. First check (theory-checker)

**Brief check, round 6: `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/briefs-round6.md`**

**Verdict: passed after changes.** Findings 1 to 3 must change before the briefs go out. Three of them are must-changes, so a short second check of the revised briefs would be sensible. The fifth look's brief says its revised version was never checked again.

I edited nothing in `/home/user/StoryTest` or in the snapshot repository. My only files are in `scratchpad/r6-brief-check/snap/`: an archive of aab01cd, extracted for comparison, which can be deleted. Line numbers below are lines of the briefs file.

## Must change

**1. The grading rule, with the stopping rule, lets the workshop's commonest errors into the commit.**
- **Target:** lines 14–17.
- **Defect:** "Must change" covers only a way round the gate, an honest route with no way through, a false statement, a text that *contradicts* a theory, and a finding claimed as applied that is not. It leaves out:
  - a term used in a neighbouring sense;
  - a theory narrowed, widened or turned round;
  - a claim credited to the wrong theory;
  - a workshop reading left unlabelled;
  - close paraphrase of a book.
- **Grounds:**
  - The first kinds row calls the neighbouring sense and the narrowed theory "the commonest kind".
  - CLAUDE.md says craft skills "follow the owner theory"; that asks for more than not contradicting it.
  - CLAUDE.md also says "nothing from a copyrighted book is committed".
  - The stopping rule (line 14) sends everything below must-change into the commit, recorded as open.
- **Connection:** a narrowed theory or a paraphrased Egri line, graded "should change", would ship in the skills writers use.
- **Also:** say what happens to "does not bear yet". Reviewers should run the settling test in their copy where they can, and otherwise say which grade the item would take if it bears. Align "a way round the gate" with C15's closing words, "beyond the limits the gate's description states".
- **Verdict:** must change.

**2. Instructions that can change the live repository.**
- **Target:** line 54 ("try to get round … the refusal hook's `$PWD` rule"); lines 21–22.
- **Defect:** nothing says to test the refusal hook by feeding commands to its script inside a copy. Running the commands for real is the risk. And round 5's "or run anything there that writes files" has been dropped.
- **Grounds:**
  - A reviewer's shell goes back to `/home/user/StoryTest` before every command.
  - The command being tried, `git config core.hooksPath '$PWD/.githooks'`, would switch off the live gate if the hook failed to refuse it. The fifth look tested it safely, through a helper (kept report, line 748).
  - `check_commit.py` line 410 writes `.git/workshop-gate-passed` in whatever repository it runs in. `prepare-commit-msg` line 16 stamps any commit within two minutes whose contents match that record.
- **Connection:** "never change its git settings" does not cover the second route, and a slip on the first is the very thing under test.
- **Fix:** add "test hook commands only by piping them to the hook script inside your copy; always use `git -C <copy>` or full paths; run nothing in the live repository that writes files, `.git` included."
- **Verdict:** must change.

**3. Brief B replays the cases that made the fixes, and has no new situations and no near neighbours.**
- **Target:** lines 38–48.
- **Defect:**
  - Items 1–5, 8 and 9 each repeat a fifth-look finding's own case.
  - `findings-answered-round5.md` lines 29–34, 42 and 45 name a planted test for almost every one of them.
  - Round 5's "situations no earlier reviewer walked" and "near neighbours where nothing should fire" are both gone.
- **Grounds:**
  - Kinds row "A test that can only agree: … a fix confirmed on the case that made it".
  - Round-4 brief check, finding 4, and round-5 brief check, finding 1 (graded must change). This is the third time.
  - The fifth look's must-changes came from situations nobody had walked, and one was older than its diff.
- **Connection:** the last full look is aimed at confirming the fixes.
- **Fix:** add situations nobody has walked. Examples:
  - GitHub's "Update branch" button, which makes a merge whose first parent is the session branch;
  - the next pull request merged on GitHub after an owner's edit made there, so one parent is not approved;
  - "Squash and merge" and "Rebase and merge" on GitHub;
  - three sessions at once;
  - a revert made on GitHub;
  - quiet neighbours: a fast-forward, an ordinary run of commits through the gate, a fresh clone's first session.
- **Verdict:** must change.

## Should change

**4. No kinds rows and no term-sheet rows in any brief.**
- **Target:** all four briefs. Line 12 and line 25 only point to the files.
- **Grounds:**
  - `reviews-and-briefs.md` section 5, and C5's catch ("with this file's kinds table and the term sheet put into every brief").
  - Round-4 brief check, finding 3; round-5 brief check, finding 6.
  - The use-tester's standing instructions and a general-purpose agent carry neither file.
- **Connection:** the new wording rests on the baseline, and term-sheet 2.1 gives exactly this case: "A dragon attack is a breach in our world".
- **Rows to add:**
  - Brief A: 2.1, 2.2, 1.1/1.2, 7, 10.1, 11.4, 12, 13 item 9.
  - Brief B: 2.1, 1.2, 7, 11.4.
  - Every brief: the kinds rows for its own area.
- **Verdict:** should change.

**5. Brief A's case list reads as closed and leaves out the theories' own dragon and baseline cases.**
- **Target:** line 30.
- **Grounds:**
  - Gap line 47: in a world full of dragons, an attack "might be weather".
  - Implied World lines 12 and 20 (the baseline; minimal departure) and line 36 (medieval Europe with dragons, riding on the genre's defaults).
  - Gap line 61 (*Planet of the Apes*), a reveal about the world.
- **Connection:** the new definition of a bare arrival turns on "the habits of the genre". It is walked here only with the case that produced it.
- **Fix:** write "among them" and add these cases.
- **Verdict:** should change.

**6. The lists of places to check are closed; no brief says "search".**
- **Target:** lines 30 and 32.
- **Omitted statements of what the gate does:**
  - `reviews-and-briefs.md`;
  - the error-correction SKILL.md list of what is not a tripwire, and its new exception (V8's other half);
  - the notes at the top of `pre-merge-commit` (V17), `prepare-commit-msg`, `session_start.py`, `refuse_check_bypass.py` and `run_all_checks.py`;
  - the project story's word-list entry "Last approved commit".
- **Omitted copies of the plot rule:** plot SKILL.md lines 123, 154 and 164; `suspense-and-fear.md` line 126.
- **Grounds:** this is the third time (round-4 brief check, findings 1 and 2; round 5, finding 7).
- **Verdict:** should change.

**7. Changes and findings no brief covers.**
- **Changes with no reviewer:**
  - `reviews-and-briefs.md`: the Book-text line (V15), the withdrawal's third condition (use-tester 11), the squash (V21);
  - `.claude/agents/copy-checker.md` (D1);
  - `checks-and-cases.md` section 3.
- **Findings with no reviewer:** only Brief C is given a list of fifth-look findings to check (line 56). So use-tester 11 and 13, the stall items, V17's note, and D1–D4 fall between the briefs.
- **Fix:** give each brief its list of fifth-look findings, as round 5 did.
- **Verdict:** should change.

**8. Brief A item 2 hands over the lead's table as the tool for the check.**
- **Target:** line 31.
- **Defect:** C1's recorded cause, six times over, is a claim checked against a list instead of against the break test itself.
- **Fix:**
  - Read the break test field by field first, and write your own list, before opening the table.
  - Also run the write-up checks on the new sentences: the stock-note test, the flip, and a verdict given both ways where it needs an input nobody gave.
- **Verdict:** should change.

**9. The brief says only C1, C12, C13 and C15 changed; C5 changed too.**
- **Target:** lines 12 and 34.
- **Grounds:** the word diff of `27 Corrections.md` shows C5's "put right" line rewritten ("third, fourth and fifth looks … marked should change in the third look's brief check").
- **Verdict:** should change. The statement is false.

**10. "Covers only the edits" may keep older faults from being reported.**
- **Target:** line 7.
- **Grounds:** the fifth look's first scripts must-change was "older than these edits" (kept report, lines 614–615).
- **Fix:** say that a fault older than these edits, met while checking them, is reported and graded the same way.
- **Verdict:** should change.

**11. Missing working instructions, and one shared resource left unprotected.**
- **Missing:**
  - how to switch the gate on and off in a copy (`git config core.hooksPath .githooks`; `git -C <copy> -c core.hooksPath=/dev/null …`);
  - that `test_checks.py` takes about 3½ minutes (`test-run-20-time.txt`), longer than the 2-minute default command timeout;
  - the plain pull into a local branch that has moved on, which is the test that settles V22 and sits next to item 6 of Brief B.
- **Unprotected:** nothing forbids changing the shared snapshot `rereview`, which four reviewers read at the same time.
- **Verdict:** should change.

**12. Round 5's rule "read no other scratchpad files" has been dropped.**
- **Grounds:** the scratchpad holds the lead's plans, fix scripts, earlier brief checks, and the trial's first-half files (`trial-predictions.md`, `trial/`).
- **Connection:** reviewers can be steered by the lead's own notes.
- **Verdict:** should change.

## Minor

**13. Only "applied" is marked as the lead's claim.**
- **Target:** line 11.
- **Defect:** the lead's account also carries verdicts: "does not bear yet" (V22, use-tester 13), "passed; no change", "answered by scripts 2", its reasons for what was not done, and the counts.
- **Fix:** mark every statement there as a claim to check.
- **Verdict:** minor.

**14. The grading scale leaves reviewers guessing in places.**
- **Target:** lines 15–19.
- **Defect:**
  - "should change" and "minor" have no line between them;
  - there is no "does not bear";
  - "answered in part" is not placed on the scale;
  - "passed after changes" is unclear when only must-changes will be made;
  - the brief does not say where open items get recorded.
- **Verdict:** minor.

**15. Brief D.**
- **Target:** line 60.
- **Defect:**
  - "Report as before" means nothing to a fresh agent;
  - the path is shortened to `.../rereview`;
  - Brief A asks whether Egri is credited only for what his book says, but that needs the book, and last time the copy-checker found D2 and D3. Give that check to D too.
- **Verdict:** minor.

**16. Brief C does not list the test split among the new rules to try to get round.**
- **Target:** line 54.
- **Detail:** the gate's own tests now sit in `test_the_gate.py`, which `test_checks.py` imports from its own folder (lines 732–736). Whether the gate runs the approved copy or the staged one is worth trying to break.
- **Verdict:** minor.

## Seen in passing (not for the briefs, since a brief to checkers carries no findings)

- `writing-rules-and-rivals.md` line 9 says walking the dragons "showed … that a threat deciding the climax needs its set-up". Plot section 2 labels that rule as the workshop's reading.
- Plot SKILL.md line 164 still gives one "unless" (*Psycho*). Section 1 now gives open examples and a third route.

## Checked and found right

- **The snapshot:** aab01cd matches the live tree (`diff -rq`), apart from an empty `cases/` folder.
- **The kept fifth-look report:** it holds every non-empty line of the four scratch reports (`grep -xF`, 0 missing each).
- **The trial fingerprints:** all four SHA-256 values and sizes match the scratch files. I did not open those files.
- **The plan's timing:** `plan-round5.md` was last written at 19:32:40, and the earliest changed live file at 19:34:56. That fits "written before any change", but it rests on file times only.
- **Pointers:** every path in the briefs exists, and the named lines and sections are the changed ones.
- **Two claims in the briefs:**
  - `merge-tree --write-tree` is really used (`check_commit.py` 186, `recheck_commits.py` 144).
  - No planted test runs `git pull --rebase`, which fits "never tried before".
- **Brief C's file list:** it names every changed script and hook.
- **No leaks:** there is no book text in the briefs, and no kept case's answer. Case 06 is about departure against breach; I read its title only.

## Not checked

- Whether the edits themselves are right, beyond the two notes seen in passing.
- Any test run.
- Whether the kept plan is the same as `plan-round5.md`.
- The trial's own instructions to its agents.
- The lead's claims in `findings-answered-round5.md`.
- The file-26 table, line by line.

## 3. Second check (theory-checker)

Recheck of the revised briefs, /tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/briefs-round6.md, against the first brief check (brief-check-round6-report.md, 16 findings). I edited nothing in /home/user/StoryTest or in the snapshot `rereview`. My files are only in scratchpad/r6-brief-recheck/ (listed at the end). Line numbers below are lines of the briefs file.

== (3) Word-for-word checks ==
- Term sheet: every quoted line in Brief A (61-146) and Brief B (161-198), with its `> ` taken off, appears as a whole line in owner-terms.md (`grep -qxF` on each line). Each chosen row is complete, with no line missing. Brief A has 1.1, 1.2, 2.1, 2.2, 7, 10.1, 11.4, 12 and 13 item 9; Brief B has 2.1, 1.2, 7 and 11.4. Only one quoted line is not from the sheet: line 145, "From section 13 (where the theories themselves leave a term unclear):" (see finding 7).
- Kinds: the 18 kinds on lines 16-33 match the Kind column of the table in 27 Corrections.md (lines 11-28) exactly (`diff` printed nothing). Only the Kind column is given (see finding 11).

== Findings ==

1. MUST CHANGE. Target: line 202 (Brief B, "Build your copy ... a clone of the live history") and lines 204-211 (the GitHub situations). The shared rules are lines 46-47. Defect: a clone of /home/user/StoryTest has the live repository as `origin`. Brief B's new situations ("Update branch", pull requests merged on GitHub, a plain `git pull`) need a stand-in for GitHub, and nothing forbids pushing to `origin`. The shared rules forbid writes "there" and git commands "with the live repository as its folder". A push made from a copy is neither, yet it writes into the live `.git`. Grounds: the fifth look's base clone has `origin /home/user/StoryTest` (`git -C r5-use-tester/base remote -v`). The live repository has a second local branch that is not checked out, `claude/story-repo-structure-31ayeb` (`for-each-ref`), and `receive.denyCurrentBranch` is unset. In scratch (r6-brief-recheck/pushdemo) a clone's `git push origin HEAD:other` into its source's non-checked-out branch printed "accepted", and the source's log showed the new commit. Neither briefs-round5.md nor briefs-round6.md says anything about push, remote or origin (grep found nothing). This session also has a GitHub tool server, and the owner's `origin` is https://github.com/AHepi/StoryTest. Connection: the revision's own new situations make a push the natural move, and nothing stops it landing in the live repository. The real-GitHub route is does not bear yet: it depends on whether the reviewer agents get GitHub tools. The local route bears. Fix: see must_change.

2. MUST CHANGE. Target: line 47 ("always use `git -C <your copy>` or full paths") and line 48 ("with CLAUDE_PROJECT_DIR set to your copy"), used by Brief B item 3 ("session start after a pull brings a note") and Brief C item 2. Defect: the workshop's scripts take their repository from the folder they are run in, not from the script's path or CLAUDE_PROJECT_DIR. Grounds:
- check_commit.py line 275: `root = git(os.getcwd(), "rev-parse", "--show-toplevel")`; lines 409-413 then write `.git/workshop-gate-passed`.
- recheck_commits.py line 285 works the same way.
- session_start.py lines 105-106 use the working folder first, and CLAUDE_PROJECT_DIR only as a fallback.
- test_checks.py and run_all_checks.py default to `.`.
- refuse_check_bypass.py takes the working folder from the JSON's "cwd".
- Test in scratch: from folder cwdrepo, with CLAUDE_PROJECT_DIR=envrepo, session_start.py printed "Last log entry: 1. Entry in cwdrepo."
Connection: the reviewer's shell goes back to /home/user/StoryTest before each command. So `CLAUDE_PROJECT_DIR=<copy> python3 <copy>/.claude/hooks/session_start.py` checks the live repository and reports it as the copy, which would be a false finding in the last full look. Running check_commit.py by its full path in the same way writes the gate's record into the live `.git`, the very thing line 46 forbids. Fix: see must_change.

3. SHOULD CHANGE. Target: line 36, must change "a way round the gate beyond the limits its own description states". Defect: that list is under review, and six of its limits were added in this round. The c52f191 list had five bullets; now there are ten: two reviewed check changes joined on GitHub, close paraphrase, what a receipt says, the other line's entries after a conflicted GitHub merge, a shallow clone, settings kept outside. A way round that falls under a new limit is graded below must change, although listing it was the lead's answer to fifth-look findings (V6, and part of use-tester 1). Grounds: `git show c52f191:.../checks-and-cases.md` against the current section 2. The lead's account for V6 ("gains ..."), and for use-tester 1 alongside the new "other line's log entries" bullet. C15's status line ties its closing to the same limits. Connection: the grading scale takes the lead's answer as its yardstick, and the same line also calls "a finding the lead says is answered and is not" a must change, so the two clauses pull against each other. Fix: measure against the limits as they stood at c52f191. A limit added in this round counts only if the reviewer judges it a true limit, and says so.

4. SHOULD CHANGE. Target: line 36 ("a statement in a skill or a record that is false; a skill text that contradicts ..."). Defect: this leaves out CLAUDE.md (loaded into every session), the notes in hooks and .githooks (outside .claude/skills), .claude/agents/copy-checker.md (D1), file 26 (a write-up for the owner) and README. Grounds: reviews-and-briefs.md line 13 treats records, numbered write-ups, CLAUDE.md, .claude/agents/, .claude/hooks/ and .githooks/ as separate groups, and names only the project story, README, the questions file and the corrections file as records. Connection: a false line in CLAUDE.md's enforcement table (the fifth look's V5 area), or a narrowed theory in file 26, would be graded should change, and under the stopping rule it would be committed. Fix: "any text in the change".

5. SHOULD CHANGE. Target: line 151, Brief A item 2: "the flip (would the same evidence read the other way if the other draft came first?)". Defect: this narrows the workshop's flip to a second check on draft order, which the same item already asks for twice (order words; verdicts given both ways). Grounds: after_commit.py: "would you be as sure of the opposite?". theory-checker.md line 34: "would the writer be as sure of the opposite?". The break test's own flip was of that kind: "the flip test found the critique praising spoken rules in B where it liked them" (file 26 line 130). Connection: this steers the reviewer away from the kind of flip that found the critique's loose half. Fix: use the workshop's wording, with draft order as one case of it.

6. SHOULD CHANGE (bundled with 2 in the fix). Target: line 48. Defect: in hook JSON copied from what Claude Code sends, "cwd" is /home/user/StoryTest. With CLAUDE_PROJECT_DIR set to the copy, the refusal hook treats commands aimed at the live folder as "another repository" and lets them through. Grounds: refuse_check_bypass.py main(): working_folder = hook_input "cwd", and reason_to_refuse skips targets outside project_root. Connection: a reviewer could report a false way round the `$PWD` rule (Brief C item 2).

7. SHOULD CHANGE. Target: lines 145-146. Defect: item 9 of section 13 is quoted without the section's opening line, "All of these are put to the owner together under S13 ...". In its place is a framing line in quote marks that is not in the sheet. Grounds: owner-terms.md lines 355-357. The kinds row and C12 record "the unshown bomb filed under Shock without its open-question label" (entry 29). Connection: the brief drops the very label whose loss was an earlier correction. Fix: quote the opening line, and put the brief's own framing outside the quote.

8. MINOR. Target: lines 60-146. Defect: row 10.2 (Suspense: three uses) is missing, though the plot rule turns on "meant to surprise or to be waited for". c561651, made after the first check, adds "or starts new suspense" (plot SKILL.md line 164). Grounds: owner-terms.md lines 272-281. Connection: an owner term in the changed text has no row in the brief.

9. MINOR. Target: lines 7 and 9. Defect: the diff includes two edits made after the first brief check (aab01cd to c561651: writing-rules-and-rivals.md line 9 and plot SKILL.md line 164). No fifth-look finding and no entry in the lead's account lies behind them, yet the brief calls the edits "the edits that answered the fifth look". Grounds: `git -C rereview diff --stat aab01cd c561651`. Connection: reviewers will look for an account of these two edits that does not exist. Say so, without passing on the checker's notes.

10. MINOR. Target: line 213 (Brief B item 3, "only where no planted test covers them (planted tests are named in the lead's account)"). Defect: what gets skipped rests on the lead's claim. Fix: confirm that each named test exists and plants that case before skipping it.

11. MINOR. Target: lines 15-33. Defect: kind names only, while reviews-and-briefs.md section 5 asks for "the rows". Grounds: reviews-and-briefs.md line 60. Connection: the "Caught now by" column, which says what each reviewer is relied on for, is missing.

12. MINOR. Target: line 49 and line 202. Defect: the time warning names only test_checks.py. A commit through the gate in a copy that brings in or changes checks runs the same test inside the commit. Grounds: check_commit.py lines 395-406, "the planted-fault test brought in". Connection: building the copy "the way the fifth look did" can pass the 2-minute limit mid-commit.

13. MINOR. Target: line 36, "(grade the missing part)". Defect: it is unclear whether a partly answered finding is always a must change, or takes the missing part's own grade.

14. MINOR. Target: line 153 and line 213, "step 3 of references/owner-answers-and-revisions.md". Defect: that file has two step 3s. The changed one is in section 2 (diff hunk at line 20).

15. MINOR. Target: line 150. Defect: the quick version's "A twist that fails" (plot SKILL.md line 154), a copy of the plot rule, is still not named. The search rule on line 54 covers it.

== (1) The 16 first-check findings ==
Every one is answered.
- 1: answered. Line 36 widened; does not bear yet handled on line 40; the C15 wording used. New problems: findings 3, 4 and 13.
- 2: answered. Lines 46-48. New gaps: findings 1, 2 and 6.
- 3: answered. Lines 204-214.
- 4: answered. The rows match word for word. See findings 7, 8 and 11.
- 5: answered. The added theory lines (Gap 47 and 61, Implied World 12, 20 and 36) land on the passages named.
- 6: answered, in substance. See finding 15.
- 7: answered. Each brief has its list; reviews-and-briefs, copy-checker.md and checks-and-cases section 3 are covered.
- 8: answered. See finding 5.
- 9: answered. The hunks in 27 Corrections.md fall in C1, C5, C12, C13 and C15.
- 10 to 16: answered (line 7; lines 9 and 47-49; lines 13, 11, 35-41; Brief D items 1-4; Brief C item 2's last bullet).

== Checked and found right ==
- Of the claims I checked (list below), none is false.
- 35 files in the diff.
- c561651 matches the live tree (`diff -rq`); the only difference is the empty `cases/` folder.
- Entry 32; the word-list entry "Last approved commit"; the plan's section 3 and its stopping rule.
- The gate writes a record into `.git`, and the 2-minute stamp (prepare-commit-msg).
- The Approval rule matches Brief C's description (check_commit.py lines 182-190).
- A copy of the refusal hook lets through both of the brief's copy commands and refuses the same command with no `-C`.
- The overlap script only reads files.
- The book texts are present.
- The Egri credits in the plot diff match Brief D item 1.
- No verdicts from the lead, and no kept-case answers, appear in the briefs.

== Not checked ==
- Whether the edits themselves are right.
- Any run of test_checks.py or of the gate.
- Whether the reviewer agents will have GitHub tools.
- The lead's claims in findings-answered-round5.md, and whether the planted tests it names exist.
- The file-26 table.
- The trial files (not opened).
- Brief C's other rule descriptions, beyond the approval rule.

== Side effects and what I left behind ==
- In the live repository I ran only reads (status, log, remote, branch, config --get, for-each-ref, grep, sed). `git status` may refresh the index's cache in the live `.git` and in `rereview`.
- I left scratchpad/r6-brief-recheck/ (the c561651 archive, the cwdrepo, envrepo and pushdemo test repositories, and text files from the comparisons). All of it can be deleted.

Verdict: passed after changes.

## 4. Third check (theory-checker)

Third check of /tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/briefs-round6.md, checked against the 15 findings of brief-recheck-round6-report.md. Line numbers are lines of the current briefs file.

== Findings ==

1. MUST CHANGE.
- Target: line 48 ("A clone of /home/user/StoryTest has the live repository as its remote origin. Before anything else in a clone, run ... remote remove origin"). Line 47 says only "Work in a copy".
- Defect: the step that removes the remote covers clones only. A copy made by copying the folder, .git included (for example with cp -a), keeps the live repository's settings. Its remote origin is the real GitHub, and its checked-out branch tracks the owner's real branch. A plain `git push` in such a copy writes to the owner's GitHub; a plain `git pull` reads from it. The brief never says so, so a reviewer who copied instead of cloning would think the removal step does not apply.
- Grounds:
  - The live repository's settings, read with `git config --get-regexp`: remote.origin.url is https://github.com/AHepi/StoryTest; branch.claude/incomplete-job-continuation-guewwy.remote is origin, and that branch is checked out; push.default is unset, so git's default ("simple") pushes the current branch to its upstream.
  - This has already happened in this workflow: scratchpad/tc-copy/.git/config, a folder copy made earlier, has exactly this remote and tracking.
- Connection: the recheck's finding 1 is answered for clones only. The part left open leads to the real GitHub, one of the three places the task says must never be written to.
- Not tested: whether GitHub would accept such a push. I must not try it.
- Fix: see must_change.

2. SHOULD CHANGE.
- Target: line 47 ("The workshop's scripts and hooks (... session_start.py and the rest) take their repository from the folder they run in, not from their own path or CLAUDE_PROJECT_DIR").
- Defect: this is false for the hooks.
- Grounds:
  - refuse_check_bypass.py lines 237-240: it takes its working folder from the JSON's "cwd", and its project from CLAUDE_PROJECT_DIR first.
  - protect_frozen_files.py lines 52 and 60: it takes the JSON's "cwd", and adds CLAUDE_PROJECT_DIR to the repositories it guards.
  - session_start.py lines 105-106: it falls back to CLAUDE_PROJECT_DIR when the folder it runs in is not in a repository.
- Connection: line 49 then tells reviewers to set CLAUDE_PROJECT_DIR for hooks, which contradicts line 47. Brief C's reviewer, whose area includes both hooks, is given a wrong picture of how they choose their repository. For the scripts themselves the claim is true: check_commit, recheck_commits, review_receipt, run_all_checks, test_checks, check_frozen_files, check_records, check_owner_quotes and check_maps all default to the folder they run in.
- Fix: say "scripts". Say that the two hooks that guard commands and edits read the JSON's "cwd" and CLAUDE_PROJECT_DIR, as in the next rule.

3. SHOULD CHANGE.
- Target: line 49 ("with both "cwd" in the JSON and CLAUDE_PROJECT_DIR set to your copy").
- Defect: this narrows what the Brief C reviewer can try on "the refusal hook's $PWD rule" (line 258). Read literally, "cwd" must be the copy's top folder, so a working folder inside the copy is ruled out. That is exactly where the rule matters, because Claude Code's cwd can be a subfolder after an earlier `cd`.
- Grounds: in scratch (r6-brief-check-3/hooktry), a copy of the hook was given `git config core.hooksPath "$PWD/.githooks"`, with CLAUDE_PROJECT_DIR set to the test repository. It printed nothing and exited 0 (let through) in both cases:
  - "cwd" set to the repository's top folder;
  - "cwd" set to its subfolder `sources`. There $PWD/.githooks is sources/.githooks, which is not the gate folder.
  I did not run the resulting commit. My own session's refusal hook stopped that command, and I did not try to get round it.
- Connection: the new wording steers the reviewer away from the case that tells.
- Fix: "cwd" may be the copy or any folder inside it, never /home/user/StoryTest.
- Note: this is also a possible defect in the build. It is for the lead to handle as a finding of its own. Do not put it in the brief, because a brief to checkers carries no findings from its author.

4. MINOR.
- Target: line 13 ("Apart from them and the lead's account named above, read no other file in the scratchpad folder").
- Defect: the list of exceptions now leaves out two things inside the scratchpad folder that reviewers must use: the shared snapshot `rereview`, which line 9 tells them to read, and the reviewer's own folder r6-<name>/, which line 47 tells them to work in.
- Grounds: both paths are under scratchpad/.
- Connection: a literal reader is barred from its own copy.
- Fix: add both to the exceptions.

5. MINOR.
- Target: line 36 ("a false statement in any text in the change").
- Defect: the change includes kept word-for-word reviewer reports, for example .claude/reviews/kept/2026-09-24-build-fifth-look.md (943 lines). A false statement in them is the earlier reviewer's, and the record cannot be edited.
- Grounds: `git diff --stat c52f191 c561651`.
- Connection: graded must change, such a finding would stall the stopping rule.
- Fix: say "text the lead wrote or changed"; a false claim in a kept report is reported, not changed.

6. MINOR.
- Target: line 50 ("so does a commit through the gate ... that brings in or changes checks").
- Defect: when test_checks.py itself changes, the gate runs both the last approved commit's copy of the planted-fault test and the changed one, so about seven minutes.
- Grounds: check_commit.py lines 396-402.
- Connection: a reviewer who sets five minutes has the commit killed partway. The build commit is not affected: the live HEAD (35f2939) has no gate, so it runs the test once (lines 403-405).

7. MINOR.
- Target: line 47 ("start every command that runs one with cd <your copy> &&").
- Defect: the line does not say to run the copy's own script. A script run by its full path in the live repository uses the live repository's sibling files: run_all_checks.py runs checks from HERE (line 76), and test_checks.py imports test_the_gate.py. It also writes Python bytecode into the live __pycache__ folders (git ignores them, but line 46 says nothing that writes).
- Connection: in Brief C item 1 (the c52f191 scripts), running the live repository's run_all_checks.py would test the wrong scripts.

8. MINOR.
- Target: lines 15-33.
- Defect: the "Seen in" and "Last seen" columns are still left out. Section 5 of reviews-and-briefs.md asks for "the rows".
- Grounds: the "Seen in" column holds C12's "the unshown bomb filed under Shock without its open-question label", which Brief A item 1 walks.
- Connection: the recheck's finding 11 is answered in substance (the "Caught now by" column is in). Line 12 sends reviewers to the table, so this misleads no one.

== (1) The 15 recheck findings ==
- 1: answered in part (line 48, clones only). The missing part is my finding 1.
- 2: answered (line 47, cd <copy> &&). The statement about hooks is false (my finding 2).
- 3: answered (line 36, limits as at c52f191). The pointer lands: at c52f191, section 2 has the "What the gate cannot do" paragraph (line 46).
- 4: answered (line 36). CLAUDE.md, README, file 26, copy-checker.md, the scripts and the hooks are all in the diff. See my finding 5.
- 5: answered (line 167). It uses the workshop's own words, "would you be as sure of the opposite?" (after_commit.py line 28; error-correction SKILL.md line 135), with draft order given as one example.
- 6: answered (line 49). The new wording narrows (my finding 3).
- 7: answered (lines 156-162). The framing is outside the quote; heading, opening line and item 9 match owner-terms.md lines 355, 357 and 367.
- 8: answered (10.2 at lines 122-130 and 210-218).
- 9: answered (line 9). `git diff --stat aab01cd c561651` shows only those two files. The copy-checker's C4 in the fifth look targeted the trap but did not bear, so "answer no fifth-look finding" holds.
- 10: answered (line 239).
- 11: answered in substance (my finding 8).
- 12: answered (line 50). See my finding 6.
- 13: answered (line 36).
- 14: answered (lines 169 and 239). Section 2 step 3 is the step the diff changes (hunk at line 20).
- 15: answered (line 166). "A twist that fails" is at plot SKILL.md line 154.

== (2) Other checks on the changed lines ==
- No verdicts from the lead and no kept-case answers appear in the briefs.
- Nothing I read steers a reviewer to the lead's answer.
- Commits made with `git -C <copy>` run the copy's hooks. .githooks has no absolute paths, and check_commit takes its repository from the folder git runs it in.
- The snapshot has no remotes.
- c561651 still matches the live tree: `diff -rq`, apart from the empty cases/ folder.

== (3) Word for word ==
- Kinds: all 18 lines on 15-33 equal "- **<Kind>.** Caught now by: <Caught now by>", built from the table in 27 Corrections.md (lines 11-28). A script compared every line and found every one identical.
- Term sheet: every quoted block in Brief A (1.1, 1.2, 2.1, 2.2, 7, 10.1, 10.2, 11.4, 12) and Brief B (2.1, 1.2, 7, 10.2, 11.4) matches owner-terms.md line for line, in order and complete. For example, 10.2 is lines 272-280 and 7 is lines 156-169; each block ends where the sheet has a blank line and then the next heading or ---. The section 13 excerpt matches lines 355, 357 and 367.

== Not checked ==
- Whether the build's edits are right.
- Any run of test_checks.py or of the gate.
- Whether a push to the real GitHub would be accepted.
- The resulting commit for finding 3 (my session's refusal hook stopped the command).
- Whether the planted tests named in the lead's account exist.
- Whether each brief's choice of term-sheet rows is complete beyond 10.2 (for example, Brief B has no 1.1 or 2.2).
- Brief C's other rule descriptions.
- The trial files.

== Side effects ==
- In the live repository and the snapshot I only read: log, diff (GIT_OPTIONAL_LOCKS=0 for the live diff), cat-file, config reads, branch -a, remote -v, archive, show.
- I left scratchpad/r6-brief-check-3/: the c561651 archive and hooktry/ (a scratch repository, copies of two hook scripts, in.json). All of it can be deleted.

## 5. Fourth check (theory-checker)

Fourth check of /tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/briefs-round6.md. It covers the answers to the 8 findings in brief-check-3-round6-report.md and the copy script make_review_copy.sh. Line numbers are those of the current briefs file.

== The copy script, run once ==
Command: sh make_review_copy.sh .../scratchpad/r6-brief-check-4/copy. It exited 0 and printed "remotes left: 0" and "last commit bc7ef7b, stamp: approved b8d36289...". It took 51 seconds in all (real 0m51.377s).
- No remote at all: `git remote -v` in the copy prints nothing. The local config has no branch.* or remote.* entries, so the branch tracks nothing. A bare `git push` prints "fatal: No configured push destination" (exit 128), and a bare `git pull` prints "There is no tracking information" (exit 1).
- Pushing switched off: push.default=nothing. Commit signing is off, and the gate is on (core.hookspath=.githooks).
- Last commit approved: the stamp names HEAD's own tree (b8d36289f92a...). The copy's own recheck_commits.py printed "rechecked 0 commit(s) ... since the last approved commit, bc7ef7b8d". Approval(".").last_approved_commit() returned bc7ef7b8d.
- Files: the copy's committed files are exactly the live working tree plus the simulated receipt. I compared sha256 of every file and git ls-files against the live file list. Snapshot 26bf4fd has the same tree minus the receipt (ls-tree blob hashes compared). The simulated receipt says plainly that no review ran.
- Live repository left exactly as it was: before the run, after it, and again at the end of my work, these were identical: HEAD (35f2939, on claude/incomplete-job-continuation-guewwy), all refs, `branch -a`, the local config, the sha256 and time of all 324 files in .git, the sha256 of every working-tree file, and the __pycache__ files. The snapshot still has HEAD 26bf4fd and no remotes.

== Findings ==

1. SHOULD CHANGE.
- Target: line 49, "The workshop's scripts (check_commit.py, ...) take their repository from the folder they run in, and run the checks beside them". This clause is new in the answer to the third check's finding 7.
- Defect: it is false for check_commit.py, the gate itself.
- Grounds: check_commit.py line 323 unpacks (git archive) the last approved commit's scripts into a temporary folder. Lines 327 and 332 use the staged scripts instead, only when the gate is new or the commit changes only checks. Line 340 runs run_all_checks.py from those, never from beside the gate script. .githooks/pre-commit line 17 runs the gate script itself from a temporary copy taken from HEAD.
- Connection: Brief C item 2, last bullet (line 261), asks the scripts reviewer whether the gate runs the last approved commit's test_the_gate.py or could run a staged or on-disk copy. The shared part now asserts the on-disk answer, a false claim from the brief's author about the question the reviewer must settle, and it goes to four agents. The practice line 49 prescribes (cd <copy> &&, run the copy's own script) is right and should stay.
- Fix: drop "and run the checks beside them", or narrow it: run_all_checks.py runs the checks beside it, and test_checks.py and recheck_commits.py load their neighbours.

2. SHOULD CHANGE.
- Target: line 47, "Make every copy of the workshop with the lead's copy script ... Never make a copy another way". This is new.
- Defect: it contradicts line 9 ("read it, or clone it into your own folder") and Brief C item 1, line 251 ("or a plain file copy of its working tree"; "git -C <snapshot> archive c52f191 | tar -x -C <your folder>/old").
- Grounds: the script can only copy the live tree on top of the live history (lines 8, 17 and 23 of the script). It cannot make the c52f191 copy that item 1 needs.
- Connection: a literal reader either breaks line 47 or drops item 1's run on the old scripts, which narrows what the scripts reviewer can find. A reader who clones the snapshot per line 9 may not count that clone as "a copy made otherwise", and so may keep the shared snapshot as its origin. Line 48's ban on pushing there still guards this, so it is not a hole.
- Fix: say "every copy of the live repository"; say that a clone of the snapshot has its origin removed at once; allow an archive or a plain copy of a working tree (no .git).

3. MINOR.
- Target: line 47 ("that commit takes about three and a half minutes"), line 51 ("and so does a commit through the gate in a copy that brings in or changes checks ... about seven minutes") and line 6 of the script. Line 51's second half is new in the answer to finding 6.
- Defect: the figures for a commit through the gate are about four times too long.
- Grounds: the whole script, including a commit through the gate that brings in checks, took 51 s. test_checks.py alone took 3m27.9s (209 tests, 0 failed), so line 51's first claim is true. Run as the gate runs it (WORKSHOP_INSIDE_PLANTED_FAULT_TEST=1), it took 44.2 s (207 run, 2 not run). test_the_gate.py lines 559-560 and 592-593 skip the two tests that run the gate for real.
- Connection: a commit through the gate takes about a minute, and about two when test_checks.py itself changes. That last case, and the "changes checks" case, I inferred from check_commit.py lines 396-405 and did not time. The error is on the long side, so it harms no one.

4. MINOR.
- Target: Brief D item 2, line 271, which names /home/user/StoryTest/.claude/skills/add-source/scripts/overlap_check.py by full path.
- Defect: line 49 now says "run your copy's own script, never the live repository's".
- Grounds: overlap_check.py imports only os, re and sys, and every open() in it reads (lines 39-41, 68, 92, 175, 184). So running it writes nothing into the live repository. The allowed list it reads beside itself is the same in the copy.
- Connection: this is a contradiction only; there is no write and the result is the same. Fix: use <your copy>/.claude/skills/add-source/scripts/overlap_check.py, with the books still read from /home/user/StoryTest/sources/raw/ (the copy has no books).

5. MINOR.
- Target: line 47 ("switches pushing off") and line 48 ("always name that remote when you push or pull").
- Defect: naming the remote alone does not push.
- Grounds: in the copy, with a bare repository added as `github`, `git push github` printed "fatal: You didn't specify any refspecs to push, and push.default is "nothing"" (exit 128). `git push github HEAD` worked. I then removed the remote.
- Connection: a one-command stall, and git's message explains it. Fix: "name the remote and the branch".

6. MINOR.
- Target: line 50 ("with CLAUDE_PROJECT_DIR set to your copy and "cwd" set to your copy or any folder inside it").
- Defect: it still narrows what a reviewer may try a little.
- Grounds: refuse_check_bypass.py lines 241-244 have a path for when CLAUDE_PROJECT_DIR is unset. Line 215 has a path for a target outside the project. The hook only runs `git rev-parse` in "cwd", so a "cwd" outside the copy writes nothing.
- Connection: the safety reason excludes only the live repository and the snapshot. Keep "run with cd <your copy> &&". Allow "cwd" anywhere but those two, and allow CLAUDE_PROJECT_DIR to be unset.

7. MINOR (carried).
- Target: lines 15-33, answering the third check's finding 8.
- Defect: the "Seen in" and "Last seen" columns are still left out. Line 15 now points to the table for them.
- Grounds: reviews-and-briefs.md section 5 asks that "the rows of the kinds table ... are included".
- Connection: answered by a pointer. It misleads no one.

8. MINOR.
- Target: line 49 (the recipe `git -C <copy> -c core.hooksPath=/dev/null commit ...` and "full paths").
- Defect: the line does not say why full paths matter. A reviewer's own session hook reads the command as written.
- Grounds: I piped both forms to the copy's refusal hook. With the full path it was let through. Written as `C=<path>; git -C $C -c core.hooksPath=/dev/null commit -m x`, it was refused. My own session refused a command that only read settings: a clone, then `config --local --get-regexp '...'`, then `config --local --get core.hooksPath`. The same command was refused when piped to the copy's hook.
- Connection: Brief B's use-tester will make many commits with the gate off. Fix: "write the copy's full path, never a shell variable, in any command that names core.hooksPath".
- Note for the lead only, not for the brief: config_moves_hooks returns True for a quoted `git config` key whenever "hookspath" appears anywhere in the command. That may be a build finding (a check that stops honest work).

Does not bear:
- Commit signing in further clones: the global config has commit.gpgsign=true, but a commit in a plain scratch clone succeeded (no signature). No stall.
- The script copies files in over a checkout and never deletes, so a tracked file deleted in the live tree would survive in the copy. Today the live tree deletes nothing (the copy's commit equals the live tree plus the receipt). This would bear only if a tracked file were deleted in the live tree before a reviewer runs the script.
- The script does not stop a destination inside the snapshot. The brief names r6-<name>/.
- The simulated receipt passes the gate with its Marks line left as the placeholder. review_receipt.py line 221 requires only Change, Maker, Reviewed by, Findings and Verdict, and the Marks line is on trust by design.

== (1) The third check's 8 findings ==
- 1: answered. The script, run and checked above; line 47 bans copying .git and says to remove every remote in any other copy; line 48 bans a bare push or pull. In a scratch clone, `git remote remove origin` also cleared the branch's tracking settings.
- 2: answered. Line 50 matches refuse_check_bypass.py lines 241-244, protect_frozen_files.py lines 52 and 60, and session_start.py lines 105-106. after_commit.py reads no folder. The new clause on line 49 is my finding 1.
- 3: answered (line 50). The small narrowing left is my finding 6.
- 4: answered (line 13). No folder r6-theory-checker, r6-use-tester, r6-scripts or r6-copy-checker exists yet.
- 5: answered (line 36). Kept cases are not in this round's diff (git diff --stat c52f191 26bf4fd lists 35 files, as line 9 says).
- 6: answered (line 51). The figures are too long: my finding 3.
- 7: answered (line 49). The leftover in Brief D is my finding 4.
- 8: answered by a pointer: my finding 7.

== (2) Other checks on the changed lines ==
- Line 9 now names 26bf4fd. `diff --stat aab01cd 26bf4fd` shows 6 files: the two earlier ones, plus refuse_check_bypass.py, test_checks.py (two new planted tests), 27 Corrections.md and the project story. The counts moved from 207 to 209 tests, and from 22 to 23 failing on the old scripts, as line 9 says. The line carries no finding or verdict. No stale commit name is left, and c52f191, aab01cd and 26bf4fd all exist in the snapshot.
- Nothing in the changed lines steers a reviewer to the lead's answer, apart from finding 1, which steers away from it.
- Nothing in the changed lines leads a reviewer to write into /home/user/StoryTest, the snapshot or the real GitHub.

== (3) Word for word ==
A script (r6-brief-check-4/compare_rows.py) compared them:
- All 18 kinds lines (16-33) equal "- **Kind.** Caught now by: <cell>", built from the live 27 Corrections.md table.
- Every term-sheet block in Brief A (1.1, 1.2, 2.1, 2.2, 7, 10.1, 10.2, 11.4, 12) and Brief B (2.1, 1.2, 7, 10.2, 11.4) equals owner-terms.md and is complete, for example 10.2 at lines 272-280.
- The section 13 excerpt equals owner-terms.md lines 355-358 and 367.

== Not checked ==
- Whether the build's edits are right, and the lead's account.
- The timing of a gate commit that changes checks or changes test_checks.py (inferred from the code, not timed).
- Four reviewers running the script at once.
- Brief lines not changed in this revision, beyond the quoted rows; whether each brief's choice of rows is complete.
- Whether GitHub would accept a push.
- Why my session's hook refused beyond the one line I read.

== What I left ==
Everything is in scratchpad/r6-brief-check-4/: copy/, further/ (a clone with its remote removed), signtest/, github.git/, the before/after/final state records, compare_rows.py, hookprobe.py and cmd-*.txt. All of it can be deleted. I added nothing to the system temporary folder (20 old workshop-test- folders before, 20 after). In the live repository and the snapshot I only read. My session's refusal hook stopped one command. I did not get round it: I dropped the core.hooksPath read and ran only the remote-removal test.

## 6. The copy script

#!/bin/sh
# Make a safe copy of the workshop for a reviewer: a clone of the live history with every remote removed and pushing
# switched off, the live files as they are now copied in (not the books, not .git), and those files committed through
# the gate in the copy, so the copy's last commit is approved as the build would be. The live repository is only read.
# Usage: make_review_copy.sh <folder that does not exist yet>
# The commit through the gate runs the planted-fault test brought in, about three and a half minutes.
set -e
live=/home/user/StoryTest
dest="$1"
if [ -z "$dest" ] || [ -e "$dest" ]; then
  echo "give a folder that does not exist yet" >&2
  exit 1
fi
case "$(realpath -m "$dest")" in
  "$live"|"$live"/*) echo "the copy must be outside $live" >&2; exit 1 ;;
esac
git clone -q --no-local "$live" "$dest"
for remote in $(git -C "$dest" remote); do git -C "$dest" remote remove "$remote"; done
git -C "$dest" config push.default nothing
git -C "$dest" config user.name reviewer
git -C "$dest" config user.email reviewer@example.com
git -C "$dest" config commit.gpgsign false
(cd "$live" && tar --exclude=./.git --exclude=./sources/raw --exclude='__pycache__' -cf - .) | (cd "$dest" && tar -xf -)
git -C "$dest" config core.hooksPath .githooks
cd "$dest"
git add -A
# The gate asks for a review receipt for the build; this copy gets a SIMULATED one, so that its last commit is approved
# as the build's will be. No review ran for it, and it says so. It exists only in this copy.
receipt=$(python3 .claude/skills/error-correction/scripts/review_receipt.py new --root . | grep -o '\.claude/reviews/[0-9a-f]\{16\}\.md' | head -1)
python3 - "$receipt" <<'FILL'
import re, sys
path = sys.argv[1]
text = open(path, encoding="utf-8").read()
answers = {"Change": "SIMULATED receipt, made by make_review_copy.sh for a reviewer's copy only; no review ran",
           "Maker": "lead agent", "Reviewed by": "SIMULATED stand-in (no reviewer)", "Findings": "none (simulated)",
           "Book text": "none added (simulated; the real receipt says what was checked)", "Verdict": "passed"}
for name, answer in answers.items():
    text = re.sub(r"(\*\*" + re.escape(name) + r":\*\*)[^\n]*", lambda m: m.group(1) + " " + answer, text, count=1)
text = re.sub(r"(## Reviewer's report\n\n)\([^\n]*\)", r"\1SIMULATED. This receipt was written by make_review_copy.sh so that a reviewer's copy of the workshop can hold the build as an approved commit. No reviewer read the change for it, and nothing it says is a finding. The real receipt for the build, with every reviewer's report, is written in the live repository after the review.", text)
text = re.sub(r"\n## Tests retired\n.*?(?=\n## |\Z)", "\n", text, flags=re.S)
open(path, "w", encoding="utf-8").write(text)
FILL
git add "$receipt"
git commit -q -m "the build as it stands in the live folder, committed through the gate in this copy (simulated receipt)"
echo "copy ready: $dest"
echo "remotes left: $(git -C "$dest" remote | wc -l)"
git -C "$dest" log -1 --format='last commit %h, stamp: %(trailers:key=Workshop-gate,valueonly)'
