# Recording a correction

Open this when a tripwire has fired and the correction goes in the corrections file, when you write a log entry about a correction, or when an old record needs correcting.

Contents: 1 Where things are recorded. 2 The record: five parts and a status line. 3 Receipts. 4 Correcting an old record. 5 Closing. 6 Traps.

## 1. Where things are recorded

**Case.** Log entry 22 recorded two misreadings of the owner's theories and corrected them. It did not say that both came from the lead's own brief. So the lesson went nowhere: the next brief was not checked either.

**Point.** Each thing has one home, and the others point to it.
- **The corrections file** (`27 Corrections.md`, top level) holds three things: the kinds of error seen here, with what catches each; every full correction, open or closed, in the form in section 2; and, at the end, the errors from before the file existed.
- **The project story's log** tells the owner what was done, in plain words. A log entry about a correction is short and cites the correction's number ("see C4"). The full record is not copied into it.
- **A review receipt** (`.claude/reviews/`) holds one review's findings, each applied or rejected with its reason, and the reviewer's own report, pasted in. A review round is recorded there, not as many corrections.
- **The questions file** (`22 Questions - meanings only you can settle.md`) is the only home for what waits on the owner. A correction that waits on the owner points to the question's number.

## 2. The record: five parts and a status line

Each full correction in the corrections file has five parts and a status line:

```
### C<number>. <what was wrong, in a few plain words>
- **Made by, found by:** who made the error, at which stage (a brief, a writer, a fix, the lead's own edit); who or what found it; how long it survived (from its commit to the finding).
- **Criticism:** the target (file, lines, commit); the defect; the grounds; the connection. Verdict: bears / does not bear yet (and the test that would settle it) / does not bear.
- **Where it got through, and the response:** the stage that should have caught it; the rival guesses about where the fault lay (the thing, the rig, the inputs) and the case that told them apart; re-tune or new part. For a new part, its witness: what it is and what it ties together; who made it, in which commit; what it was made from; and which decisive step came from outside the workshop (the owner's diagnosis, question or instruction).
- **Plan, then put right, still working, lost:** the plan as it was written before the change (to put right; to keep working; the inputs), and beside it what happened: what now holds, with its receipt; what was rerun to show everything on the keep-working list still works, with receipts (anything on that list that now fails is broken, not lost, and the correction is not closed); what else changed or was given up. The route: what ran, and in what order, from the change to what now passes, and what came back when the change was removed, alone and in groups. Which of three: put right through the reason (the change was made by using the reason, and the route shows it); put right without a reason that holds yet (and the number of the correction opened on the reason); a reason that holds, with nothing put right yet. A change beside a correct reason that did not produce it is the second and third together.
- **Now caught by:** the check, kept case, step or rule that will catch this kind next time, with its path; or "on trust, because ...". What would reopen this correction.
- **Status:** open (and the next action) / closed, <date>.
```

"In proportion" is allowed: a part may be one line. Leaving a part out is not, and that includes the status line. A part that does not apply says "does not apply", and why.

The kinds table at the top of the file has one row per kind of error. It gives what the kind is, the corrections and log entries where it was seen, when it was last seen, what catches it now, and whether that catch runs by itself or on trust. When a kind gets past its catch, the catch itself becomes the target of a new correction.

## 3. Receipts

- A receipt points to events, each with what it is taken to show: the command, what it printed, and what that means; a commit hash; a file and line; a reviewer's report; the owner's own words. Paste the lines that matter; do not paraphrase them.
- Tag how you know each thing, as hard-to-vary does: *seen* (you ran or read it), *claimed* (someone says so), *recalled* (memory), *worked out* (follows from the others).
- A record made from the claim, rather than from the event, is not a receipt for the claim, whenever it was written. A review receipt that pastes the reviewer's report is one; a verdict the maker writes from the result wanted is not. A later copy of an event is the same witness, not a second one. Records rebuilt afterwards, like log entries 1 to 7 and the list of past errors, say that they were rebuilt, and from what.
- "Not found" says where you looked. A cut-off output proves nothing about what was cut off (log entry 25).
- Say what was not checked, and say "not run" for a check that could not run. Never write "passed" for it.

## 4. Correcting an old record

**Case.** Log entry 26 says *The Catch*'s Final4 "cuts set-ups". Nobody knew which draft came first.

**Point.** Old records are never rewritten. Editing one to match what is known now destroys the evidence of what was known then. Instead:
- **The log.** Add a new entry that says what the old one got wrong and what is right. You may also add one line under the old entry, beginning `*Corrected in entry N:*`, pointing forward. The records check allows that line and nothing else.
- **A write-up for the owner** (a test or critique). Put a dated note at the top saying what was wrong and what changed. If the wrong wording would mislead a reader, you may then change it, and the note lists each change. The earlier text stays in the git history.
- **A frozen text** is never edited, not even with a note. See `owner-answers-and-revisions.md`, section 4.

## 5. Closing

Closing a correction is a decision, not a proof. Close it when what was to be put right holds, what was to keep working still works, and what will catch the kind next time is in place, or is honestly marked on trust. Write the date and what would reopen it (for example: "reopen if a kept case for the character skill fails on a villain's ladder"). A correction that cannot be closed stays open with its next action; the session-start hook lists open corrections, so it is not forgotten.

## 6. Traps

- **Two homes for one record.** The log entry copies the correction in full, the two drift, and nobody knows which is right. Cite the number.
- **Leaving out who made it.** The stage that made the error is how its kind gets caught. Log entry 22 left out that the lead's brief made two misreadings, so the brief step was never changed.
- **A plan written after the results.** The keep-working list chosen once the results are known can leave off the case that failed and call it lost. Write the plan first, and show it beside what happened.
- **A receipt that is a summary.** "Checks pass" is a claim. Paste what the check printed.
- **Closing because the symptom went away.** Say the route. Then remove the change, alone and together with any other change made for the same failure. A change is not shown to have done nothing until it has been removed in groups: two changes that each stop the failure are two routes, and both are credited.
