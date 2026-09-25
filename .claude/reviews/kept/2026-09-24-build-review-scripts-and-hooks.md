# Review of the error-correction build: the scripts and hooks, 24 September 2026

What this is: the reviewer's report, word for word, as the review workflow returned it, with one change: a run of 21 words the reviewer quoted from a book, to show the copying check let it through, is left out, because the book's text is never committed. The reviewer tested each finding in scratch copies of the repository. How each finding was answered is in the build's review receipt. Kept for log entry 29.

---

```json
[
 {
  "id": "scripts-and-hooks",
  "findings": [
   {
    "target": ".claude/skills/error-correction/scripts/check_commit.py lines 49, 57 and 68 (and run_all_checks.py lines 98, 100 and 101)",
    "defect": "The commit gate takes the checks, the receipt check and the planted-fault test from the working copy, not from the last commit. (\"Working copy\" means the files on disk now, including changes not yet staged. \"Staged\" means marked for the next commit.) Only the map check and the copying check are taken from the staged files. So a check can be loosened in the same commit as the work it would block, or loosened on disk and never staged, and the loosened check then passes that work. Nothing enforces \"correct the check in its own commit\".",
    "grounds": "Scratch copy /tmp/review/g2. I staged a rewrite of log entry 5. The gate as written stopped it with \"log entry 5 has been changed since HEAD\". I then changed check_records.py on disk so it always passes, and did not stage that change. The same commit printed \"passed records ... All checks passed; committing.\" After I restored the check, the next commit also passed, so the rewrite stays in for good. Scratch copy /tmp/review/g3 had one commit holding three things: check_records.py changed to skip entry 7, a rewrite of entry 7, and a receipt naming theory-checker. The gate printed \"passed  the checks' own planted-fault test (a check changed)\" and made the commit.",
    "connection": "CLAUDE.md rule 3 and check_commit.py's own note (lines 15-17) say a wrong check is corrected in its own commit. The owner asked for error correction built into the repository. A gate whose checks come from the files being changed lets a change certify itself. The planted-fault test cannot see a loosening it has no planted fault for, and it is taken from the working copy too.",
    "verdict": "bears",
    "severity": "must change",
    "proposed_change": "Take every check, the receipt check and test_checks.py from the last commit, copied out of HEAD into the scratch folder, so a changed check takes effect from the next commit. On a first commit, print plainly that the checks come from the staged files. Refuse a commit that changes a check, hook, list or settings file together with anything else except its receipt and the log. Add both routes above to test_checks.py as planted faults."
   },
   {
    "target": ".claude/skills/error-correction/scripts/check_frozen_files.py lines 47-57 (read_list) and 92-97 (the only-added-to comparison)",
    "defect": "When a path is on the frozen list twice, the later line wins. The \"only added to\" rule allows new lines. So one added line with a new fingerprint lets an edited theory pass.",
    "grounds": "Scratch copy /tmp/review/g1. After I added a sentence to sources/bond-theory.md, the check printed \"frozen file has changed\". I then added one line with the new fingerprint for the same path, and the check printed \"TOTAL problems: 0\". The commit went through the gate with a light receipt (\"Reviewed by: none\", \"Verdict: light (a list line only)\"). The gate printed \"passed  frozen files ... passed  the checks' own planted-fault test ... All checks passed; committing.\"",
    "connection": "The script's note (lines 14-17) says a file re-listed with a new fingerprint is refused. It is refused only when the old line is removed. 27 Corrections.md C6 is closed with \"Reopen if a frozen file changes\", and a frozen file has now changed in a copy with every check passing.",
    "verdict": "bears",
    "severity": "must change",
    "proposed_change": "Report any path listed more than once. Compare each frozen file with the fingerprint its path had in the last commit's list, not with the last matching line. Add this planted fault to test_checks.py. Reopen C6 until both are done."
   },
   {
    "target": ".claude/skills/error-correction/scripts/review_receipt.py line 79 (field) and lines 123-137; CLAUDE.md line 38",
    "defect": "The gate checks the receipt's form, not that a review took place, and the form check has holes. (a) The field reader runs past the end of its line, so an empty Maker, Reviewed by or Findings field takes the next line as its value. (b) The form's own bracketed hints count as answers, so a form left blank except for \"Verdict: passed\" counts as complete. (c) A light receipt (\"Reviewed by: none\") is accepted for any change, including a change to a check or a list.",
    "grounds": "Scratch copy /tmp/review/g4. Receipt form untouched except the verdict \"passed\": the check printed \"review receipt: .claude/reviews/fbd3b22e87724294.md is complete\" and exited 0. Same receipt with Maker, Reviewed by and Findings left empty: none of the three was reported, only the book-text line. Scratch copy /tmp/review/g1: a light receipt carried the frozen-list line that let an edited theory in. SKILL.md line 75 says \"A summary written afterwards to support the claim is not one\". reviews-and-briefs.md step 5 has the maker fill the receipt in afterwards, and the form has no place for the reviewer's own words.",
    "connection": "CLAUDE.md's enforcement table says independent review is enforced by the gate itself (\"Itself\"). By the skill's own definition, a review receipt is a summary the maker writes afterwards, so the gate enforces that a form exists, not that someone else looked. The owner said how error correction is defined and used matters as much as having it. Here the definition and the enforcement claim disagree.",
    "verdict": "bears",
    "severity": "must change",
    "proposed_change": "Read each field to the end of its own line only. Refuse any field that still holds the form's bracketed hint. For a full receipt, require the reviewer's report pasted word for word, or kept in a file beside the receipt, so it counts as a receipt by the skill's definition. Refuse a light receipt for any change to a check, a hook, the settings file, the frozen list or the allowed-titles list. Until then, change the CLAUDE.md row to \"On trust, with a trace: the gate asks for the receipt but cannot tell whether the named reviewer ran\". Add (a), (b) and (c) to test_checks.py as planted faults."
   },
   {
    "target": ".claude/skills/add-source/scripts/overlap_check.py lines 58-72 (is_allowed); overlap-allowed.txt; run_all_checks.py lines 117-123",
    "defect": "Three gaps in the copying check. (a) A span counts as allowed if, once titles and names are taken out, no single remaining piece reaches 8 words. So a long copied run passes when a title sits in its middle. (b) Any phrase can go on the allowed list, and the list is read from the files being committed, so a book phrase and the text that copies it can arrive in one commit. (c) The gate's copying run reads only .claude, sources, foundations, kept-cases and the top-level .md files, so a new top-level folder is never read.",
    "grounds": "Books were present in this session. Scratch copy /tmp/review/p1: a line holding 21 consecutive words of The Anatomy of Genres, 14 of them outside the film title. The check printed \"[21 words, allowed (title or name)] [a run of 21 words copied from a book, left out here: the book's text is never committed]\" and exited 0. Scratch copy /tmp/review/p3: a copied sentence made the check print \"FAILED  copying from books\". After two lines of that sentence were added to overlap-allowed.txt, it printed \"passed  copying from books\". Scratch copy /tmp/review/p2: a 30-word copied sentence in drafts/notes.md, and run_all_checks printed \"passed  copying from books\".",
    "connection": "CLAUDE.md says to rewrite every reported run \"except titles, names and the author's short term names\". The 14 copied words are none of these. The allowed list is meant for titles and names only, but only a comment inside the list says so. Copyright is the one rule here with outside consequences.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Allow a span only if the words outside titles and names, counted together, stay under a small number such as 3, not counted piece by piece. Refuse an allowed entry that is not a title or author named in the sources/README.md register (give the film title its own line there). Require a full review, never a light receipt, for any change to overlap-allowed.txt. Read every .md file in the staged copy, not a fixed set of folders. Add all three as planted faults."
   },
   {
    "target": "the working copy's git setting core.hooksPath (/home/user/StoryTest), before this change is committed",
    "defect": "The commit gate is not switched on in the real repository now, so the commit that brings in this whole change would not be checked by it.",
    "grounds": "`git -C /home/user/StoryTest config --get core.hooksPath` printed nothing and exited 1. .claude/settings.json is new and untracked, so the session-start hook that switches the gate on has not run in this session. The shell-command hooks are live: the claim reminder appeared after my commands, and my `-c core.hooksPath=...` command in a scratch copy was refused.",
    "connection": "This commit carries every check and hook, so it most needs the gate. A later log line such as \"committed through the gate\" would be untrue unless the gate is switched on first.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Run `git config core.hooksPath .githooks` before committing. Commit through the gate with a review receipt, and paste the gate's printed output into the log entry. If the commit is made any other way, the log must say it was not checked by the gate."
   },
   {
    "target": ".githooks/ (only pre-commit exists); check_commit.py note lines 4-5; check_records.py line 146 and review_receipt.py, which compare only with the last commit",
    "defect": "Git does not run the pre-commit hook for a merge without conflicts, a fast-forward, a cherry-pick or a rebase, nor for a commit made elsewhere (on GitHub, or on a machine where the gate is off). What arrives that way is not checked. Records and receipts compare only with the last commit, so a log rewrite or an unreviewed skill change that arrives this way is never caught later either. Frozen-file edits are caught at the next ordinary commit.",
    "grounds": "Scratch copy /tmp/review/g7: a theory edit on a branch, merged with `git merge --no-ff`, exited 0 with no gate output, and check_frozen_files reported the change only afterwards. Scratch copy /tmp/review/g7b: `git cherry-pick` of a theory edit exited 0 with no gate output. Scratch copy /tmp/review/g8: a rewrite of log entry 7 arrived by fast-forward. run_all_checks then printed \"passed  records\", and the rewritten words are in the file.",
    "connection": "The note says \"Git runs this by itself before every commit\", and the skill's table says \"Every commit\". That holds only for `git commit` on a copy where the gate is switched on.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Add .githooks/pre-merge-commit, which runs the same gate. Have the session-start hook check every commit since the last one the gate saw (the records against that commit, and `review_receipt.py check --commit` on each), keeping the last checked commit in a file. Say in the note which commits the gate cannot see. A check that runs on GitHub for every push would close the made-elsewhere route."
   },
   {
    "target": ".claude/skills/error-correction/scripts/test_checks.py lines 36-47; check_commit.py lines 67-76",
    "defect": "For `git commit -a` and `git commit <file>`, git gives the gate the full path of the file where it keeps the list of what is about to be committed, in a setting called GIT_INDEX_FILE. The planted-fault test's throwaway copies inherit that setting. Their `git add` and `git commit` then write into the real commit's list, the first copy's commit fails, and the test stops with a Python error. The gate prints a bare FAILED with no reason.",
    "grounds": "A test hook that printed its settings showed GIT_INDEX_FILE=/tmp/review/envtest/.git/index.lock for `commit -a`, a temporary list for `commit <file>`, and the short \".git/index\" for a plain commit. Scratch copy /tmp/review/g17: a comment added to check_records.py, the receipt filled in, then `git commit -a`. The gate printed \"FAILED  the checks' own planted-fault test (a check changed)\" and \"COMMIT STOPPED\", with no reason. Running test_checks.py by hand with that setting ended in \"CalledProcessError: Command '[... 'commit', '-q', '-m', 'copy']' returned non-zero exit status 1\".",
    "connection": "This is a false alarm with no plain reason, on a common way of committing. While it runs, the test writes into the real commit's list. The plain `git commit` works only because the short path happens to point into each copy's own folder.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Remove GIT_INDEX_FILE, GIT_DIR, GIT_WORK_TREE and GIT_OBJECT_DIRECTORY from the settings of every git command test_checks.py runs in its copies, and when check_commit.py starts it. Print the error output of every script the gate runs. Add a gate test that commits with -a."
   },
   {
    "target": ".claude/hooks/session_start.py lines 83-92; check_commit.py lines 53 and 73-76; overlap_check.py lines 87-88",
    "defect": "A check that cannot run is sometimes shown as passing, or the commit stops with no reason. Session start prints \"Machine checks: none failing\" when run_all_checks.py cannot run at all. The gate prints only the scripts' normal output, so when run_all_checks.py or test_checks.py crashes, the commit stops with no reason. The copying check skips a file or folder that does not exist and prints \"0 problem spans\" with exit 0 (the version at 35f2939 stopped with an error instead).",
    "grounds": "Scratch copy /tmp/review/g11: I added a broken line to run_all_checks.py. session_start.py printed \"- Machine checks: none failing\", and a commit printed only \"passed  review receipt\" then \"COMMIT STOPPED\". `overlap_check.py sources/raw/truby-anatomy-of-genres.txt .claude/skils` (a misspelt folder) printed \"TOTAL problem spans >= 8 words: 0\" and exited 0. The version from 35f2939 printed \"FileNotFoundError\".",
    "connection": "CLAUDE.md rule 2 says \"Not run is never passed\". checks-and-cases.md section 3 says a check \"prints each problem as a sentence the owner could follow\". CLAUDE.md's own by-hand copying command names folders, so a typo there gives a clean pass.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "In session_start.py, when run_all_checks.py exits non-zero with no FAILED line, or runs out of time, print \"Machine checks: could not run\". In check_commit.py, print each script's error output and name the script that could not run. In overlap_check.py, treat a missing file or folder as NOT RUN (exit 3) and name it. Add a planted fault for each."
   },
   {
    "target": ".claude/hooks/refuse_check_bypass.py lines 21-26; CLAUDE.md line 37 (\"`--no-verify` is refused\")",
    "defect": "The hook recognises only some spellings. Missed: short options run together (`git commit -nam`), a shortened option (`--no-veri`), the setting name in lower case (`core.hookspath`), a ; or & inside the message, the usual multi-line message with the option after it, `-C \"folder with space\"`, `env git ...`, git settings passed through the environment, and deleting .githooks/pre-commit. False alarms: a commit message that mentions --no-verify or \" -n \", the read-only question `git config core.hooksPath || echo off`, and setting hooks in any other repository.",
    "grounds": "/tmp/review/hooktest.py printed \"let thru\" for every missed spelling and \"REFUSED\" for both messages and the question. Scratch copy /tmp/review/g6: `git commit --no-veri`, `git -c core.hookspath=/dev/null commit` and `git commit -nam` each committed a theory edit with no gate output. My own `git config core.hooksPath hooks` in a separate scratch repository was refused.",
    "connection": "The note says the hook refuses \"the commands that would skip or switch off that gate\", and CLAUDE.md lists it as enforcement. In fact it reminds, with gaps. Its stop message tells someone asking a read-only question that the command \"would skip or switch off\" the gate, which is untrue.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Say in the note and in CLAUDE.md that the hook catches the usual spellings only, and point to the later recheck proposed in the merge finding as the real safety net. Match the setting name in any letter case. Refuse any group of short options after commit that contains n, and any shortened form of --no-verify. Do not refuse `git config core.hooksPath` with no value, or settings in other repositories. Keep the missed spellings and the false alarms as planted cases."
   },
   {
    "target": ".claude/skills/error-correction/scripts/check_frozen_files.py lines 42-44 and 98-106; no .gitattributes in the repository",
    "defect": "A fingerprint is worked out from a file's exact bytes on disk. Where git writes Windows line endings when it checks files out (the setting core.autocrlf=true, which the Git for Windows installer normally sets), every frozen file's fingerprint differs and every commit is stopped. The printed advice, \"restore it (git checkout -- '<path>')\", writes the same bytes again.",
    "grounds": "Scratch copy /tmp/review/g10 with core.autocrlf=true and the frozen files checked out again. `file` showed \"with CRLF line terminators\". The check printed \"frozen file has changed\" for all five files, and a commit of one line in README.md was stopped with the same lines.",
    "connection": "This is a false alarm that blocks all work on such a machine, and its advice does not fix it. It matters if the owner or a session ever works from Windows.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Add .gitattributes with `sources/*.md -text` and `foundations/** -text`, so git never changes those files' line endings. Or fingerprint the committed contents rather than the bytes on disk. Add a planted test with autocrlf switched on."
   },
   {
    "target": ".claude/hooks/protect_frozen_files.py lines 35-38",
    "defect": "The hook reads the frozen list of the repository the session is standing in, not the repository the edited file belongs to.",
    "grounds": "I fed the hook an edit of /tmp/review/g4/sources/bond-theory.md. With the session folder at /tmp/review/g4 or /tmp, it refused. With the session folder at /tmp/review/g5, another repository, it allowed the edit.",
    "connection": "The workshop's own practice is to work in scratch copies. From one of them, an edit to the real theory goes through. The fingerprint check still catches it at the next commit.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "Find the repository from the edited file's own folder, and also check the file against the list in CLAUDE_PROJECT_DIR."
   },
   {
    "target": "check_frozen_files.py lines 56, 66 and 81-83; protect_frozen_files.py line 28",
    "defect": "Three small gaps. The list is read by splitting at spaces, so a frozen file whose name has a space is read as a shorter name that does not exist, and the edit hook does not protect it. Only .md files in sources/ must be frozen, while CLAUDE.md says all files there except README.md. On a first commit the \"only added to\" comparison is skipped with no \"not checked\" line.",
    "grounds": "Scratch copy /tmp/review/g9: after `--add \"sources/my new theory.md\"`, the check printed \"sources/my: frozen file is missing\" and \"sources/my new theory.md: should be frozen but is not on the list\". The edit hook allowed an edit to that file.",
    "connection": "add-source names theory files in lower case with hyphens (SKILL.md line 65), so the space case is unlikely. The .md-only rule is narrower than CLAUDE.md's frozen rule.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "Read the fingerprint from the start of each line and \"added ...\" from its end, leaving the path whole, or separate the parts with tabs. Freeze every file in sources/ except README.md. On a first commit, print \"not checked: the list has no earlier version\"."
   },
   {
    "target": ".claude/skills/error-correction/scripts/check_owner_quotes.py line 40, and the note at lines 13-14",
    "defect": "Only text in curly quotes is read, so a made-up quotation in straight quotes, with a theory named after it, is never checked.",
    "grounds": "Scratch copy /tmp/review/g12: I added `\"The bond is a contract, signed in blood.\" (Bond, The limits of care)` to owner-terms.md. The check printed \"TOTAL problems: 0\".",
    "connection": "The note says \"so no quotation slips past unchecked\".",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "Also read straight-quoted text that has a theory's name in brackets after it, or refuse straight quotes in the term sheet. Add this as a planted fault."
   },
   {
    "target": ".claude/skills/add-source/scripts/check_maps.py lines 184-199",
    "defect": "A copy of a shared passage is compared only while it keeps its opening marker. Delete that marker in one skill and the copy there can drift. A closing marker with no opening one is not reported.",
    "grounds": "Scratch copy /tmp/review/g14: I removed `<!-- shared: reply-check -->` from plot/SKILL.md and changed the passage. The check printed \"TOTAL problems: 0\".",
    "connection": "The note gives the reason for this check: \"A rule stated in several skills and changed in only one is how the skills came to disagree before.\"",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "Report an opening marker without a closing one, and the reverse. Compare the list of files that carry each passage with the last commit, or keep a list of which files should carry it."
   },
   {
    "target": ".claude/skills/error-correction/scripts/review_receipt.py lines 58-61",
    "defect": "git writes a file name with an accented letter in quotes, with number codes for the letter. That name does not begin with \".claude/skills/\", so the change needs no receipt.",
    "grounds": "Scratch copy /tmp/review/g5: I staged a new module, .claude/skills/plot/references/café.md. `git diff --cached --name-only` printed `\".claude/skills/plot/references/caf\\303\\251.md\"`, and the receipt check printed \"review receipt: not needed (no reviewed file changed)\".",
    "connection": "Files in .claude/skills/ are meant to need a receipt. Later edits to such a file would need none.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "Run git with `-c core.quotePath=false` and `-z` in review_receipt.py and check_commit.py, and add this as a planted fault."
   },
   {
    "target": ".claude/skills/error-correction/scripts/check_records.py lines 53 and 83-93",
    "defect": "Any line in the log that starts with a number and a full stop is taken as a new entry. So a numbered list inside an entry is reported as \"log entry 1 appears 2 times\", which points at the wrong place. The entry number in a \"*Corrected in entry N:*\" note is never checked to exist.",
    "grounds": "Scratch copy /tmp/review/g13: a new entry holding the lines \"1. read the file;\" and \"2. fixed the row.\" The check printed \"log entry 1 appears 2 times\" and \"log entry 2 appears 2 times\".",
    "connection": "checks-and-cases.md section 3 says each problem should be a sentence the owner can follow. This one sends the reader to entries 1 and 2.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "Count as entries only numbers that follow on from the entry before. Otherwise print \"a numbered line inside entry N: indent it\". Check that N in a correction note exists and is later than the entry it sits under."
   },
   {
    "target": "test_checks.py (lambda names c, t, l); check_frozen_files.py line 120 (l); check_maps.py lines 169-170 (m)",
    "defect": "Some names inside the scripts are single letters.",
    "grounds": "CLAUDE.md: \"Scripts: full plain-word names, and a note at the top saying what the file does.\"",
    "connection": "Every script's file name is in full plain words and every script has a note at the top. Whether the rule also covers names inside a script is for the owner to say.",
    "verdict": "does not bear yet",
    "severity": "minor",
    "proposed_change": "Ask the owner whether \"full plain-word names\" covers names inside scripts. If it does, rename c to copy_root, t to text, l to line and m to match."
   }
  ],
  "right": "No frozen file changed. `git diff --stat 35f2939 -- foundations sources` printed nothing. Each of the five listed fingerprints matches the file as it was in the commit that added it, as it was at 35f2939, and as it is now (I checked each one with sha256sum against git show).\n\n`python3 .claude/skills/error-correction/scripts/run_all_checks.py`, run on the working copy with the four books present, printed passed for frozen files, maps, records, owner quotes, no book files and copying from books, then \"RESULT: no check failed\", in 1.4 seconds. I also ran overlap_check.py against each book myself. The only spans it found were labelled \"allowed (title or name)\" (the registered book titles and the film title).\n\n`python3 .claude/skills/error-correction/scripts/test_checks.py` printed ok on every line and exited 0 in 11 seconds. `git status` showed the same entries before and after, so it works only on throwaway copies.\n\nWhere the gate runs, it does what it says for the plain cases. In /tmp/review/g2 it stopped a rewritten log entry with a plain reason naming the entry, and in copies it stopped a frozen-file edit. A first commit prints \"not checked\" for the log comparison rather than passed. A worktree and a detached state both work. Without books, the copying check prints NOT RUN, never passed.\n\nCompared with 35f2939, the repaired map check and copying check are real improvements. Matching exact names, reading only the map table, checking section pointers, and returning a failure code all hold up under the planted-fault test. The review receipt's fingerprint does change with any edit made after a review.\n\nThe shell-command hooks are wired and live. The claim reminder appeared after my commit commands, and a `-c core.hooksPath=` command was refused.\n\nEvery Python script, the hooks and .githooks/pre-commit have plain-word file names and a note at the top. So do the two lists, and each note says what the file is for.",
  "not_checked": "I did not test whether the edit hook for Edit and Write is wired in a live session, because I would not risk an edit to a real frozen file. I did not start a new session, so the session-start hook was run only as a script in copies.\n\nI did not test on real Windows or macOS. The Windows line-ending case was simulated on Linux with core.autocrlf. I tested only git 2.43. The newer `git config set` / `git config unset` forms (git 2.46 and later) were judged from reading the hook, not run.\n\nI did not review kept-cases/run-kept-cases.js beyond its header. I did not read the skills' prose, the reviewer agents, the kept cases, or most of 27 Corrections.md, apart from its \"Now caught by\" lines, the gate descriptions in CLAUDE.md, README.md, SKILL.md and references/checks-and-cases.md, and the receipt steps in references/reviews-and-briefs.md.\n\nI did not look for every way a determined agent could get round the hooks, only the spellings listed. I did not test speed on a much larger repository.\n\nThe working copy was still being edited during my review: run_all_checks.py changed once, and I re-read it. At 13:34 it matched my snapshot in /tmp/review/snap, so later edits are not covered.",
  "overall": "not passed"
 }
]
```
