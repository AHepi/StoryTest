# Reviews and briefs

Open this when the commit gate asks for a review receipt, when you run or answer a review, or before you send a brief to other agents.

Contents: 1 Why the gate asks for a receipt. 2 Getting a review, step by step. 3 Answering the findings. 4 A review round. 5 Checking a brief. 6 Testing the reviewers. 7 Traps.

## 1. Why the gate asks for a receipt

**Case.** After an independent check had passed a round of changes, the lead made a few more by hand and committed them in the same breath. One of them used the words "Side with" in two senses a paragraph apart. No reviewer saw that change. Trials found it later. In that round, most of the new errors the trials found had been made by changes made after a review.

**Point.** The costly errors in this workshop's history were steps that were written down and skipped, above all the independent look at a change. So the commit gate does not trust memory. A change to what the workshop says cannot be committed without a review receipt for that exact change. The receipt's name is the change's fingerprint: a short code worked out from the staged change. An edit after the review changes the fingerprint and needs its own review. Skipping the review is then no longer a silent slip; it would take a false statement in a kept file. That is also the limit of what the gate can show: it checks that a receipt exists, fits the change, is filled in, names a reviewer other than the maker and carries the reviewer's report. It cannot tell whether that reviewer really ran. The review is on trust, with a trace.

**What needs a receipt:** staged changes to anything under `.claude/skills/`, `.claude/agents/`, `.claude/hooks/`, `.githooks/` and `kept-cases/` (apart from its run record), to `.claude/settings.json`, `.gitattributes` and `CLAUDE.md`, and to numbered top-level write-ups. Records that are added to all the time do not need one: the project story, README, the questions file and the corrections file.

## 2. Getting a review, step by step

1. Stage the change: `git add ...`.
2. See what the receipt must cover: `python3 .claude/skills/error-correction/scripts/review_receipt.py fingerprint`.
3. Ask a reviewer that did not make the change:
   - **`theory-checker`** for anything a skill says about an owner theory, any owner term, any new or changed rule, rival or worked example, a brief, or a write-up for the owner;
   - **`use-tester`** for a change to a skill's procedure, table, quick version or reply step;
   - **`copy-checker`** for book-derived text, where the book text is present.

   Give the reviewer the staged change (`git diff --cached`) and say what it was for. Do not give it your own verdicts or findings. A reviewer told what you think will find what you think.
4. Answer each finding (section 3). If you change anything after the review, stage it: the fingerprint changes, so the edits need a look of their own. Give a reviewer that did not make them the edits only (the difference between what was reviewed and what is staged now) with the first review's findings. The receipt for the final fingerprint then lists the first review's findings as applied or rejected, and carries the re-review of the edits. "Passed after changes" is written only after a reviewer has seen the changes; never copy a first review's verdict onto a change it did not see.
5. Write the receipt: `review_receipt.py new` makes the form. Fill it from the reviewer's report: the change, the maker, the reviewer, each finding with applied or rejected and why (in a section "Findings answered" if there are many, with the Findings line pointing to it), the marks on new rules and rivals, and the verdict. Paste the reviewer's report under "Reviewer's report", word for word. A very long report may be kept as a file in `.claude/reviews/` beside the receipt; then give its path and copy its first lines. A report is what makes the receipt a receipt: a verdict written by the maker is a claim. Then `git add` it and commit.

**A light receipt** is for a change that alters no meaning: a typo, a link, a map row, formatting. It names the maker, says "Reviewed by: none", and gives the verdict "light (no meaning change: ...)", saying why, with the "Book text" line if the books are absent and the module draws on a book. A light receipt on a change that does alter meaning is a false record. If in doubt, get a review. The gate never takes a light receipt for a change to a check, a hook, the settings, `.gitattributes`, the frozen list or the allowed-titles list.

**A change to a check, a hook, the settings or the allowed-titles list** goes in a commit of its own (a new theory's line on the frozen list is the exception: it comes with the theory, as add-source says): the gate refuses it mixed with other work, apart from its receipt, the project story, the corrections file and the source register. It gets a full review, and the planted-fault test from the last approved commit must still pass on the changed checks. If a test from that commit no longer fits because the check was meant to change, name it in the receipt under "Tests retired", with why; the reviewer must have seen it, and any test but those of the maps and the owner quotes is retired only with the owner named first under "Reviewed by", told in plain words which guard would be lost. The changed check takes effect once a commit carrying it is approved, because the gate always runs the last approved commit's checks. A commit made straight on top of an approved commit that changes only checks, with nothing else but its receipt, is judged by its own changed machine checks, so that a wrong one can be corrected even when it stops every commit; its receipt is still checked by the last approved commit's receipt check, and its log entry follows in the next commit. A retired test is changed or removed in `test_checks.py` (or `test_the_gate.py`, for the gate's own tests) in the same commit; the gate reads retirements from every receipt added since the last approved commit, so they travel with a merge or a rebase.

**A receipt written late**, for a commit the gate did not approve, is made with `review_receipt.py new --commit <commit>` and committed afterwards. If that review does not pass, take the change back out (`git revert --no-commit <commit>`, put back any receipt the revert took out, and commit through the gate with a receipt for the withdrawal itself), and give the late receipt the verdict "not passed (withdrawn in ...)", naming where; the recheck believes it only if every line that commit added is gone, every line it removed is back, and its change can no longer be undone from the files. Never write a verdict the reviewer did not give. A receipt already committed is never changed or deleted: a correction to it is a new file that points to it. A rebase or cherry-pick that leaves a reviewed change exactly as it was keeps its receipt: the receipt's name is made from the lines the change adds and removes and the one unchanged line either side of each. So a line moved after its review, a rebase that lands next to an edit made meanwhile, or a squash that joins several changes, needs a new review; tell the reviewer where each changed line sits, since the fingerprint does not hold a place further away than that.

**A merge** needs a receipt only for its own changes, anything beyond the automatic merge of its parents (usually nothing); the commits it brings in carry theirs.

**Book text.** When the book texts are not present (most sessions), the copying check cannot run. If a changed module draws on a book (one named in the source register before or after the change), the receipt must say what book text the change adds. Normally that is "none added, because ...". Otherwise the gate refuses the commit. What the line says is the maker's word.

## 3. Answering the findings

A reviewer's finding is a criticism, and a guess. Reviewers over-reach too. In one round, reviewers proposed "only a blank desire makes a function" and credited a theory with a claim about laughter it never makes; the agents making the changes checked each finding against the sources and turned those down, with reasons (corrections file, H47).
- For each finding: does it bear? Run the error-correction loop's step 2, in proportion: its target, defect, grounds and connection, then the flip and the rival.
- Apply it, or reject it with a one-line reason. Both go in the receipt.
- A finding you reject because it rests on an input nobody gave (the owner's aim, an open question) is held if that input. Put it to the owner; do not settle it yourself.
- A finding that you apply must be answered in its content. A differently worded finding with the same point should lead to the same change. Applying a finding does not make it right.

## 4. A review round

**Proportion, and when to stop.** Weight follows the change, not the wish for certainty. A change to one passage gets one reviewer, who reads the changed lines and what they cite. A changed check gets the scripts reviewer, with the planted-fault test. Several reviewers are for a whole new part. The lead runs the planted-fault test once and hands reviewers its output; a reviewer builds a copy of the workshop only to try a route no test covers. The answers to a round get one narrow look at the lines they changed, by one agent. After two rounds, anything short of a must-change is recorded as open, and a must-change found after that goes to the owner with its cost before another round starts. A brief is checked once; a revised brief is checked only for its changed lines. The case: the build of entries 27 to 33 ran six rounds of review, with up to five reviewers each and the last briefs checked four times; the rounds and their fixes re-read about 1.4 billion tokens in eight hours (the whole build about 1.8 billion, over nine hours), while the critique it grew from cost about 40 million; the owner caught it (correction C16).

A review round (one or more reviewers over a batch of changes) is one correction, however many findings it has. Its findings are lines in the receipt, not entries in the corrections file. A finding becomes a full correction only if a tripwire fires (see the skill's "How much to do"): the error got past the stage meant to catch it. A finding on a staged change, before it is committed, is that stage working, even when the corrections file names a catch for its kind, as long as the stage that caught it is the one named for its kind. When the catch named for the kind is a check that let the error past (the planted-fault test passing while a reviewer still finds a way round), the tripwire has fired, even before commit (correction C15). Other examples of a tripwire: a finding in text already committed, or in a brief already sent.

## 5. Checking a brief

**Case.** One brief to writing agents credited "build care before the threat" to the Bond theory; it is the Anticipation theory's, and it spread into two skills. A later brief to agents making changes told them to read the villain's ladder of care turned round, against the Bond theory's own Joffrey case, and another put back a reading a reviewer had removed an hour before. A template gave every genre profile a slot headed "Guarantees", and writers filled it with promises.

**Point.** A brief is the least-checked step with the widest reach: one error in it lands in every file its readers write. So every brief to agents that write, change or check is checked by `theory-checker`, not by its author, before it goes out:
- every credit and definition is quoted from the theory, with its line;
- every reading or instruction is tied to a theory line, or labelled as the workshop's reading with its question number, and the theory's own named case is walked through it;
- every pointer ("section 5 of ...") has been opened and says what the brief claims;
- every slot in a template that assumes a distinction carries the term sheet's telling test (`owner-terms.md`);
- a brief to checkers carries no findings or verdicts from its author;
- the rows of the kinds table and of the term sheet that apply are included, so lessons reach the makers, not only the checkers;
- earlier corrections of the passages the brief touches are looked up, so a rejected reading is not brought back.

Kept cases (`kept-cases/`) are never given to agents that write or change the skills, and a brief made from a failed case gives the defect, not the case's answer.

## 6. Testing the reviewers

A reviewer is a check, and a check that has never been seen to fail tells us nothing when it passes. Now and then, give a reviewer a change with a known planted fault (for example a wrong theory credit) alongside the real work, and record in the receipt whether it was caught. A miss is a sign against that reviewer's instructions (`.claude/agents/`), worked through like any other. Every reviewer is the same kind of model as the maker, so agreement between them is weaker evidence than it looks; the owner is the only fully independent reviewer of meaning.

## 7. Traps

- **Reviewing your own change.** The receipt names the maker and the reviewer; the gate refuses them being the same unless the receipt is light.
- **Editing after the review.** The fingerprint changes; review the change again, even a one-word edit.
- **Briefing the reviewer with your conclusions.** It will find them.
- **A light receipt for a meaning change.** It is a false record in a kept file.
- **A summary for a report.** A receipt that gives the verdict and paraphrases the findings is the maker's claim. Paste the report.
- **Copying a verdict onto edits it never saw.** "Passed after changes" needs a reviewer who has seen the changes.
- **Letting the lesson stop at the checker.** Put it in the next brief to makers, through the kinds table.
