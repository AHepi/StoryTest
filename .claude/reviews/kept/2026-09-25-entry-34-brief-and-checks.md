# Log entries 34 and 35: the reviewer's brief, its three checks, and the instructions of the runs, 25 September 2026

What this is: the brief the one reviewer worked under, as it went out; the three checks of it by `theory-checker` (the first of the whole brief, the second and third of its changed lines only, as `references/reviews-and-briefs.md` section 4 says), each word for word as the agent returned it; and the scripts that ran the checks, the review and the three looks after it, word for word, since the instructions they give the agents are kept nowhere else. The review of the change and the looks after it are in `2026-09-25-entry-34-reviews.md`; the receipt that answers them is the one made for this change in `.claude/reviews/`.

## 1. The brief, as it went out

````markdown
# Brief: review of the change for log entry 34 (one reviewer, under the proportionate review rule)

You are reviewing a staged change to the story workshop at `/home/user/StoryTest`. You did not make it; the lead agent did. The owner is not a programmer, and wrote of the work so far: "this whole process on a the scripts I uploaded has taken 12 hours and tons of tokens." So this review is kept in proportion (`.claude/skills/error-correction/references/reviews-and-briefs.md`, section 4, the paragraph "Proportion, and when to stop"): read the changed lines and what they cite, and, for check 2, wherever the same rule is stated. Do not make a copy of the workshop and do not run the planted-fault test; no check or hook is changed.

## The change

`git -C /home/user/StoryTest diff --cached` (three files: `CLAUDE.md`, `27 Corrections.md`, `StoryTest - project story.md`). What it is for: it records, as correction C17, what the lead takes to be its misreading of the owner's message at session-record line 8968. It changes CLAUDE.md's line on taking a request from the owner, and the kinds-table row for that kind of error; it adds log entry 34; it restamps and changes the status lines of the project story; and it closes correction C13.

## What the change rests on (the events)

The session's record is `/root/.claude/projects/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be.jsonl`, a very large file. Read it only at the lines named here or found by the command below; times are UTC (the record's "Z"). To see a line, `sed -n '8968p' <file> | cut -c1-2000`; to see a line's time, `sed -n '8980p' <file> | grep -o '"timestamp":"[^"]*"'`.

The owner's messages, word for word:
- line 1416, 24 Sep 11:14: [two screenplay files attached] "Here. Try these two"
- line 1572, 11:46: "I'm really not sure which. Is the hard to vary method for testing added? Or was it forgotten?"
- line 1612, 12:00: [a file attached] "No no. Wrong task. Hard to vary and error correction need to be built into the repo itself. So you will need to add it wherever it makes sense. Which will require a bit of research."
- line 1657, 12:02: "Error correction is essential. And how it's defined and used is equally important. So don't skim. Metabolise the source to understand how to apply it properly."
- line 1710, 12:04: "Hard to vary is a metric. Error correction is a process."
- line 8487, 20:10: "Why is there a file limit?"
- line 8822, 21:25: "Use one verify agent. This single review has taken a lot of tokens. After the review, I want you to figure out why and see if it can optimised somehow"
- line 8894, 21:27: "No I meant this whole process on a the scripts I uploaded has taken 12 hours and tons of tokens."
- line 8968, 21:36: "Return new script inline. And if you're making changes to the repo, finish up. That's different."
- line 9530, 25 Sep 01:02: "Where is revised script?"

How this list was drawn up, so you can test that it is complete: this read-only command prints every message of the owner's from line 1400 on (the first message of entry 26 is at line 1416), leaving out tool results, task notifications, stop-hook messages, messages from other agents, loaded skills, system reminders, local command output and the summaries written when the conversation was continued; an interruption or a command the owner typed is printed, and a message with no text is printed as "[no text]":

```
python3 - <<'EOF'
import json
path = "/root/.claude/projects/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be.jsonl"
skip = ("This session is being continued", "Stop hook feedback", "<task-notification>", "Another Claude session sent a message", "Base directory for this skill", "<system-reminder>", "Caveat:", "<local-command")
for number, line in enumerate(open(path), 1):
    if number < 1400: continue
    record = json.loads(line)
    if record.get("type") != "user" or record.get("isMeta"): continue
    content = record["message"]["content"]
    if isinstance(content, list):
        if any(isinstance(part, dict) and part.get("type") == "tool_result" for part in content): continue
        text = " ".join(part.get("text", "") for part in content if isinstance(part, dict) and part.get("type") == "text")
    else:
        text = content
    text = text.strip()
    if not text.startswith(skip): print(number, record["timestamp"][:19], repr(text[:120]) if text else "[no text]")
EOF
```

The lead's two replies around line 8968, word for word, are in `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/entry34-lead-replies.txt` (session-record lines 8961 and 8971). At line 8980 the lead resumed the review run `wf_14e38511-111` with a script passed in full (the run was first launched at about 20:58 and stopped before line 8961); its record is `/root/.claude/projects/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/subagents/workflows/wf_14e38511-111/journal.jsonl`, where records 1 to 9 are the first launch and records 10 to 15 the resumed part. The lead's report to the owner that ended entry 33 is at line 9524. The lead's reply to line 9530, with a script in it, is at line 9630. The script passed at line 8980 is also in the tool's own saved copy, `/root/.claude/projects/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/workflows/scripts/sixth-look-wf_14e38511-111.js`, and in the lead's copy, `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/sixth-look-as-run.js`.

The owner's two uploaded screenplays are `/root/.claude/uploads/d4341bef-a251-5a02-b92c-5a2687b808be/65e1e528-The-Catch.txt` and `/root/.claude/uploads/d4341bef-a251-5a02-b92c-5a2687b808be/a64e4837-The-Catch-Final4.txt` (read only their first lines).

The machine checks were run by the lead after the change was made: `/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/checks-entry-34.txt`.

## Check

1. **The records.** Is every statement in C17, entry 34, the kinds row, the status lines and C13's new status true to the events above and to the repository (a commit, a file, a count)? Does C17 have every part of the form in `.claude/skills/error-correction/references/recording.md`, section 2, and does C13's closing meet section 5 of that file? Are the owner's words quoted exactly? Is any status line under "Where things stand" out of date? Is what the owner meant at lines 8968 and 9530 read fairly?
2. **The changed line in CLAUDE.md.** Measure it with the rule card (`.claude/skills/error-correction/references/writing-rules-and-rivals.md`, section 2, steps 2 to 4; the line is in CLAUDE.md, not a skill, but it is a rule agents follow): for each of its signs, give a mark (held, held if, two routes, loose, idle, unknown) and the job that holds it, or none. Walk every owner message above through the line yourself: which does it stop, which does it let through, and is either wrong? Does it contradict anything else in CLAUDE.md or in the error-correction skill, and is the same rule stated anywhere else that was not changed with it?
3. **Words.** Is any term new, or used in a second sense beside an existing one (CLAUDE.md, "Plain words")?

The kinds-table rows that apply (from `27 Corrections.md`; the first is changed by this change, so read it there):
- "The owner's request misread, or a local patch for a fault in the workshop's stages"
- "A record that is stale, unfinished, or leaves out who made an error"
- "A change (a fix) that makes a new error; a rule changed in one place but not its copies"
- "A required check skipped, or a claim reported without its receipt, with an assumed input, or with agreement between checks that were not independent"

## Report

Number each finding, with its target (file and line), defect, grounds and connection, and your verdict on it: bears, does not bear yet (with the test or the owner's answer that would settle it, and the question to put to the owner if one is needed), or does not bear. Grade each that bears: **must change** (a false statement in the change, the owner's words misquoted, a part of the form missing, a line that fails to stop the case it answers or stops a plain owner request, a contradiction with another rule), **should change**, or **minor**. Then: the marks for the line's signs; what you checked and found right; what you did not check. End with one verdict: passed, passed after changes, or not passed.

## Rules

Never edit, stage, commit or run anything that writes in `/home/user/StoryTest`; never touch GitHub. Read only. Your final message is your report; it will be kept word for word in the review receipt, so write it for a reader who has not seen your working.
````

## 2. The first check of the brief (whole brief)

````
Verdict: passed after changes

Must change:
Finding 1: at entry34-brief.md line 7, take the lead's verdicts out of the statement of what the change is for. Replace "it records a mistake of the lead's that the owner caught, as the workshop's rules require" with, for example, "it records, as correction C17, what the lead takes to be its misreading of the owner's message at line 8968". Replace "C17, with its five parts and a status line" with "C17". Replace "restamped and brought up to date" with "restamped and changed". Grounds: reviews-and-briefs.md section 2 step 3, section 5 ("a brief to checkers carries no findings or verdicts from its author") and section 7 ("Briefing the reviewer with your conclusions").

The brief is /tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/entry34-brief.md. I checked only the brief; I did not review the change itself.

FINDINGS

1. Must change. Target: brief line 7, the sentences on what the change is for.
Defect: they state as fact the lead's answers to questions that check 1 (lines 28 to 29) asks the reviewer to settle:
- "it records a mistake of the lead's that the owner caught, as the workshop's rules require". This is C17's own "Verdict: bears", plus a claim that the rules require a full correction.
- "C17, with its five parts and a status line". Check 1 asks whether C17 has every part of the form.
- "the status lines ..., restamped and brought up to date". Check 1 asks whether any status line is still out of date.
Grounds: reviews-and-briefs.md section 2 step 3 ("Do not give it your own verdicts or findings. A reviewer told what you think will find what you think."); section 5 ("a brief to checkers carries no findings or verdicts from its author"); section 7, trap "Briefing the reviewer with your conclusions". The brief's own evidence also leaves the reading open:
- Line 8894 calls the owner's uploads "the scripts I uploaded", and line 1416 shows those uploads were screenplays. So what "new script" (line 8968) and "revised script" (line 9530) meant is for the reviewer to judge, not a given.
Connection: a reviewer told that a mistake happened, that the form is complete and that the status lines are current is steered toward confirming all three.
Fix: "it records, as correction C17, what the lead takes to be its misreading of the owner's message at line 8968". Drop "with its five parts". Change "brought up to date" to "changed".

2. Should change. Target: brief line 3, "read the changed lines and what they cite, and nothing else".
Defect: the paragraph it cites (reviews-and-briefs.md line 48) says only "reads the changed lines and what they cite". "And nothing else" is the lead's addition. It also clashes with:
- the brief's own check 2 ("anything else in CLAUDE.md or in the error-correction skill");
- the kinds row the brief itself includes ("a rule changed in one place but not its copies");
- theory-checker's standing search of the other skills for copies of a changed rule.
Grounds: reviews-and-briefs.md line 48.
Connection: taken literally, the phrase stops the search for copies that the included row exists for. The harm is small for now: my search (grep for "say it back", "in doubt", "do not wait" and "request" across the skills, agents and README) found no other statement of this rule outside CLAUDE.md.
Fix: drop "and nothing else", or add "and, for check 2, wherever the same rule is stated".

3. Should change. Target: brief lines 11 to 25 and check 1 (line 28).
Defect: check 1 asks whether every statement in C17 and entry 34 is true "to the events above and to the repository". Some of those statements rest on events the brief gives no pointer to, while it limits reading of the session record to the named lines:
- C17: "the report that ended entry 33 did not include the script". No line is given for that report.
- C17: "workflow run wf_14e38511-111". No pointer.
- Entry 34: "It is now in my reply to you, exactly as it ran; the copy the tool saved is in this session's working files". No pointer, although scratchpad/sixth-look-as-run.js (and sixth-look-original.js) exist.
Grounds: the staged diff (27 Corrections.md, the new C17; the project story's entry 34) set against the brief's pointer list.
Connection: the reviewer can only mark these statements unchecked, or break the brief's reading limit.
Fix: give the session-record line of entry 33's closing report and the path of the as-run script. Or tell the reviewer these cannot be checked.

4. Should change. Target: brief line 11 ("read only those lines") together with line 30 ("Walk every owner message above through the line").
Defect: the brief supplies exactly the ten messages that the change counts, and forbids reading other lines. The change's claims "the owner's ten messages from 'Here. Try these two' to 'Where is revised script?'" (C17) and "your ten messages since entry 26, it stops only this one" (entry 34) therefore rest on the lead's own list. The reviewer cannot test whether that list is complete.
Grounds: the brief's own wording; the staged C17 and entry 34.
Connection: this narrows what the reviewer can find. A missing owner message would never be walked through the new line.
Fix: give a one-line read-only filter that prints the line number and the first characters of every owner message between lines 1416 and 9530. Or say how the list was drawn up.

5. Should change. Target: brief lines 33 to 36 (the kinds-table rows that apply).
Defect: the row "A required check skipped, or a claim reported without its receipt, with an assumed input, or with agreement between checks that were not independent" is missing. It applies:
- Entry 34 is addressed to the owner and reports claims: "Walked through your ten messages ... it stops only this one", and "Checked. ... one reviewer read the changed lines ...; the report is in this change's receipt".
- C17's defect rests on a reading of what the owner meant.
Grounds: reviews-and-briefs.md section 5 ("the rows of the kinds table ... that apply are included"); 27 Corrections.md kinds table.
Connection: without that row, the reviewer is not pointed at the claims to the owner or at the assumed input.
The three rows the brief does name exist under exactly those names.

6. Should change. Target: brief line 40 (report form and the grades).
Defect: the brief asks for a grade (must / should / minor) but not the verdict on each finding that theory-checker's own form requires (.claude/agents/theory-checker.md line 38: bears / does not bear yet / does not bear). Its must-change list also has no place for a finding that rests on an input only the owner can give.
Grounds:
- CLAUDE.md: "A verdict that needs a fact nobody has checked or told you ... does not bear yet: ask".
- reviews-and-briefs.md section 3: a finding that rests on the owner's aim is "held if" that aim; put it to the owner.
Connection: here the events turn on what the owner meant by a word, so such findings are likely. Without a place for them, they would be graded "should change" and not put to the owner.
Fix: ask for the verdict beside the grade, with the question for the owner where one is needed.
On point (4) of my task: section 4 of reviews-and-briefs.md does not define "must change". It uses the term only as the threshold after two rounds, and for what goes to the owner with its cost. The brief's definition is therefore the lead's own. It does not conflict with section 4: it keeps "must change" for a false record, a misquotation, a missing part, a line that fails its case, and a contradiction, which suits a proportionate first round.

7. Minor. Target: brief line 3, "has said the work so far cost far too much".
Defect: this puts in the owner's mouth a judgement stronger than the owner's words. Not a quotation, but reported speech.
Grounds: line 8822, "This single review has taken a lot of tokens"; line 8894, "this whole process on a the scripts I uploaded has taken 12 hours and tons of tokens".
Fix: quote line 8894, or drop the clause. Section 4's proportion rule stands without it.

8. Minor. Target: brief line 11, the example command (sed -n '8968p' piped to cut -c1-2000).
Defect: for line 8980, whose time the brief gives (21:37:55), the timestamp sits at character 14330 of a line 14686 characters long. The same command would not show it. The brief also does not say that its times are UTC (the record's "Z").
Grounds: character positions measured in the named lines only.
Fix: suggest sed -n '8980p' piped to grep -o '"timestamp":"[^"]*"', and say "UTC".

CHECKED AND FOUND RIGHT
- Owner quotations: all ten are word for word against session-record lines 1416, 1572, 1612, 1657, 1710, 8487, 8822, 8894, 8968 and 9530. The only difference is trailing spaces the brief dropped at 1710, 8822, 8894 and 8968. Every date and time the brief gives matches the record's timestamp. The bracketed notes on the attachments at 1416 and 1612 are accurate.
- Lead replies: scratchpad/entry34-lead-replies.txt matches lines 8961 and 8971 exactly, with the right timestamps.
- Line 8980: it is the lead's call at 21:37:55.057 that starts the review run (script named 'sixth-look').
- The change: the staged change is the three files the brief names. No check or hook is changed, and nothing is left unstaged. All six parts the brief lists are present in the diff: C17, the CLAUDE.md line, the kinds row, entry 34, the status lines, and C13 closed.
- Machine checks: checks-entry-34.txt exists. It was written at 01:10:34.598, after the last edit to the three files (01:10:33), and prints "RESULT: no check failed".
- Section pointers: reviews-and-briefs.md section 4, paragraph "Proportion, and when to stop"; recording.md section 2 (five parts and a status line) and section 5 (Closing); writing-rules-and-rivals.md section 2, steps 2 to 4; CLAUDE.md "Plain words". All exist and say what the brief says they say, apart from finding 2. The brief's six marks match the rule card. Its move of step 4 from the theory's cases to the owner's messages is stated openly, and fits a rule in CLAUDE.md.
- Term sheet: no row applies, since the change uses no owner theory term, so leaving them out is right.
- Point (5): the brief says plainly "Never edit, stage, commit or run anything that writes in /home/user/StoryTest; never touch GitHub. Read only.", and forbids a copy and the planted-fault test. Every command it suggests is read-only. Nothing in it points toward GitHub.

For the lead (the owner's current question, line 9530, "Where is revised script?"): if "script" means the review workflow script, the version as run (one verifier) is /tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/sixth-look-as-run.js, and the version before it is sixth-look-original.js in the same folder. I did not check that either file matches the script passed inline at line 8980.

NOT CHECKED
- Whether the ten owner messages are all of the owner's messages in that span. As told, I read the session record only at the lines the brief names (1416, 1572, 1612, 1657, 1710, 8487, 8822, 8894, 8961, 8968, 8971, 8980, 9530).
- Any other line of the session record, including entry 33's closing report and anything the lead wrote between lines 8971 and 8980.
- The workflow run id.
- The change itself: whether C17, entry 34, the CLAUDE.md line, the kinds row and the status lines are true and complete. That is the reviewer's job.
- Nothing was copied and no test was run. Nothing was edited or staged.
````

## 3. The second check (changed lines)

````
Verdict: passed after changes

Must change:
Finding 1: brief line 47, 'The lead's reply to line 9530, which showed the owner a script, is not yet in the record (it is part of the current turn)': the reason is false, since the current turn is already in the record (9869 lines, and no owner message after line 9530), and whichever way the facts fall one of the two claims is false. Search the record after line 9530 for the lead's reply. If it is there, give its line. If not, say that the lead has not yet replied, so entry 34's 'showed it, exactly as it ran' cannot be checked now. Grounds: reviews-and-briefs.md section 5 ('a brief to checkers carries no findings or verdicts from its author') and section 2 step 3.

Narrow check of the revised brief /tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/entry34-brief.md, changed lines only. I did not review the staged change. I confirmed that entry34-brief-changes.diff is exactly the difference between entry34-brief-first.md and entry34-brief.md.

(1) THE FIRST CHECK'S 8 FINDINGS
- F1 (must change): answered. Line 7 now uses the proposed wording ('what the lead takes to be its misreading'); 'five parts' is gone; 'brought up to date' became 'changes'. Check 1 (line 55) drops 'still' and adds 'Is what the owner meant at lines 8968 and 9530 read fairly?'. Line 49 points to the screenplays. New finding 1 below is a fresh case of the same kind, on a new line.
- F2: answered. Line 3: 'and, for check 2, wherever the same rule is stated'. Line 56 adds the question about copies of the rule.
- F3: answered in part. Line 9524 is right. The run id is loosely described (finding 3). The as-run script is right (finding 4). The statement about the reply to line 9530 is finding 1.
- F4: answered at lines 25 to 45, with a gap (finding 2). I ran the listing once. It printed exactly lines 1416, 1572, 1612, 1657, 1710, 8487, 8822, 8894, 8968 and 9530, with the brief's times.
- F5: answered. The line 63 row is word for word at 27 Corrections.md line 22.
- F6: answered. Line 67 asks for bears / does not bear yet / does not bear, with the owner's question where one is needed.
- F7: answered. Line 3 quotes line 8894's words exactly (a shortened quote, leaving out 'No I meant').
- F8: answered. Line 11 says the times are UTC. The timestamp command prints "timestamp":"2026-09-24T21:37:55.057Z".

(2) and (3): NEW FINDINGS

1. Must change.
Target: line 47, 'The lead's reply to line 9530, which showed the owner a script, is not yet in the record (it is part of the current turn)'.
Defect: the reason given is false, and one of the two claims in the sentence is false whichever way the facts fall.
Grounds:
- wc -l gives 9869 lines, last written at 01:19.
- The brief's own listing reads to the end of the file and finds no owner message after line 9530. So lines 9531 to 9869 are the current turn, and it is being written to the record as it goes.
- If the lead has already shown the script, that reply is in the record, and 'not yet in the record' is false.
- If it has not, 'which showed the owner a script' is false.
Connection:
- The staged entry 34 says 'I ... showed it, exactly as it ran', and check 1 asks the reviewer to test every statement in entry 34.
- The brief gives the lead's own claim as an event and tells the reviewer it cannot be found. That steers the reviewer and closes the way to test the claim.
- Rules: reviews-and-briefs.md section 5, 'a brief to checkers carries no findings or verdicts from its author'; section 2 step 3.
Verdict: bears. Which half is false does not bear yet. Test that settles it: search the record after line 9530 for an assistant text containing a line of the as-run script (for example 'one agent tries to refute every must-change'). I did not run it, because I was told to read the record only at the named lines.
Fix: if the reply is in the record, give its line and drop 'not yet in the record'. If not, write 'the lead has not yet replied to line 9530; entry 34's "showed it" describes a reply still to come and cannot be checked now'.

2. Should change.
Target: line 25 ('leaving out tool results, task notifications, stop-hook messages, messages from other agents, loaded skills and the summaries'), against the skip list on line 31 and 'if text' on line 43.
Defect: the code leaves out more than the text says. That includes two kinds of owner action:
- '[Request interrupted' (the owner stopping the lead);
- '<command-' (a slash command the owner typed).
It also drops any owner message with no text, such as an image alone.
Grounds: the skip tuple and the 'if text' test in the brief's own command.
Connection: the listing exists so the reviewer can test that the ten messages are complete (the answer to F4). An owner interruption between lines 8968 and 8980, or between 8894 and 8961, would bear on C17's 'acted on without waiting'. The command would hide it, while the text says every owner message is printed.
Verdict: the mismatch bears. Whether any such record exists in the span does not bear yet: run the listing with those two prefixes removed from the skip list.
Fix: remove '[Request interrupted' and '<command-' from the skip list, or name them in line 25 as left out.

3. Minor.
Target: line 47, 'The review the lead then started was launched at line 8980; its run is wf_14e38511-111, whose record is in .../wf_14e38511-111/journal.jsonl'.
Defect: at line 8980 the lead resumed a stopped run; it did not start a new one. The journal holds both launches.
Grounds:
- Line 8980's Workflow input has resumeFromRunId = wf_14e38511-111.
- Journal records 1 to 9 ('launched', then brief check 4, whose agent metadata is from 20:58, and the first reviewers) belong to the first launch, stopped before line 8961.
- Records 10 to 15 come after 21:37.
- Line 8971 itself says 'the two finished reviews are reused, not rerun'.
Connection: C17 and entry 34 say the lead 'reran the review'. A reviewer reading the journal from the top would count the first launch as part of the review started at 8980. The counter-evidence is in front of it, hence minor.
Fix: 'At line 8980 the lead resumed run wf_14e38511-111 (first launched about 20:58, stopped before line 8961); in its journal, records 1 to 9 are the first launch, 10 to 15 the resumed part.'

4. Minor.
Target: line 47, 'the script it showed, as the lead says it ran, is .../sixth-look-as-run.js, and the version before it is sixth-look-original.js'.
Defect: the first half is right and can be stated without the hedge. The copy the tool saved, which entry 34 names, is not given. 'The version before it' is inexact.
Grounds:
- sixth-look-as-run.js is byte for byte the script passed at line 8980 (diff).
- It also equals the tool's saved copy, /root/.claude/projects/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/workflows/scripts/sixth-look-wf_14e38511-111.js, saved 21:37:56.
- sixth-look-original.js labels its brief check 'brief recheck' and has a different brief-check prompt ('16 findings').
- The first launch of wf_14e38511-111 ran an agent labelled 'brief check 4' (journal record 2), so original.js is not what that run first ran. Its label matches the journal of the earlier run wf_10fb627b-e22.
- The tool's copy for that earlier run (workflows/scripts/sixth-look-wf_10fb627b-e22.js, saved 21:26:35) already uses one verifier. It differs from the as-run script only in its lines 3 and 7, the description strings.
Connection:
- A reviewer comparing original.js with as-run.js to see 'the revision' will also see an unrelated brief-check change.
- It cannot test entry 34's 'the copy the tool saved is in this session's working files' from the lead's own copy (made 01:03:58, after line 9530).
Fix: give the tool's copy, say that as-run.js matches line 8980 exactly, and either drop 'the version before it' or say what that file is.

CHECKED AND FOUND RIGHT (changed lines)
- Line 7 still describes the staged change: C17 added, CLAUDE.md's request line changed, the kinds row changed, entry 34 added, status lines restamped and changed, C13 closed. The three staged files were rewritten at 01:18:49, after the first check.
- Line 51: checks-entry-34.txt was written at 01:18:51, after that rewrite, and prints 'RESULT: no check failed'. Dropping 'once' is right, since the file was rewritten after the first check's 01:10:34.
- Line 47, replies: entry34-lead-replies.txt holds the exact text of lines 8961 and 8971. Line 8980 is the Workflow call at 21:37:55.057 with script name 'sixth-look'.
- Line 47, report: line 9524 is the lead's report at 23:09:41, starting 'The error-correction work is finished, saved and uploaded to GitHub.'
- Line 49: both upload files exist and are screenplays ('= THE CATCH', 'FADE IN:'; the second reads 'An original short screenplay' and 'Revised screenplay — 22 September 2026').
- Lines 3, 11, 25, 49, 51, 55, 56, 63 and 67 add no verdict or finding of the lead's about the change.
- Every command in the brief only reads. Nothing points the reviewer at GitHub. Line 9524's text contains a pull-request link, but the brief's Rules forbid touching GitHub.

NOT CHECKED
- Whether the lead's reply to line 9530 is in the record (finding 1's test).
- Whether the skip list hides any owner record in the span (finding 2's test).
- Session-record lines other than 8961, 8971, 8980, 9524 and the ten listed.
- Whether an owner message of entry 26 comes before line 1400, where the listing starts.
- The staged change itself. Seen in passing only: the staged entry 34's 'Checked.' part now describes this recheck and the coming review as done, and the brief gives the reviewer no pointer to test it. That is for the reviewer and the lead; I did not weigh it.
- The brief's unchanged lines.
- No test was run and no copy made. Nothing in /home/user/StoryTest was edited or staged. I wrote two comparison files in the scratchpad: verify-diff-entry34.txt and check8980-script.js.
````

## 4. The third check (lines changed since the second)

````
Verdict: passed

This is a narrow check of the revised brief /tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/entry34-brief.md. I checked only its changed lines, which are 25, 31, 43 and 47. First I made sure that entry34-brief-changes-2.diff is exactly the difference between entry34-brief-second.md and entry34-brief.md: `diff` of the two files, compared with `cmp`, printed SAME. I did not review the staged change.

(1) THE SECOND CHECK'S 4 FINDINGS
- Finding 1 (must change): answered. Line 47 no longer says "not yet in the record (it is part of the current turn)" or "which showed the owner a script". It now says "The lead's reply to line 9530, with a script in it, is at line 9630." Session-record line 9630 is an assistant text at 2026-09-25T01:06:03.090Z. It begins "The script is below." and holds a fenced js block that opens with the sixth-look meta. The listing prints no owner message after 9530, so 9630 falls in the lead's turn answering 9530. The wording is neutral: it does not repeat entry 34's "exactly as it ran", so the reviewer can still test that claim.
- Finding 2 (should change): answered.
  - Line 31 drops "[Request interrupted" and "<command-" from the skip list.
  - Line 43 now prints a message with no text as "[no text]".
  - Line 25 now says interruptions and typed commands are printed, and now names system reminders and local command output among what is left out.
  - I ran the command once, exactly as the brief gives it. It printed exactly lines 1416, 1572, 1612, 1657, 1710, 8487, 8822, 8894, 8968 and 9530, with the times the brief gives. So no interruption, typed command or message with no text is hidden in the span, and the ten-message list matches the command's output.
- Finding 3 (minor): answered, almost word for word with the proposed fix.
  - Line 8980's Workflow input has a full `script` and `resumeFromRunId: wf_14e38511-111`.
  - The journal has 15 records. Records 2 to 9 name agents that ran from 20:58:01 to 21:34:26 (brief check 4 started at 20:58:01.584Z). All of that is before line 8961 at 21:34:49, which says "I've stopped the run."
  - The agents of records 10, 11 and 14 first write at 21:37:56 or later, and records 12, 13 and 15 are their results.
  - So "first launched at about 20:58 and stopped before line 8961" and "records 1 to 9 ... records 10 to 15" are right.
- Finding 4 (minor): answered.
  - The hedge "as the lead says it ran" is gone, and so is "the version before it" (sixth-look-original.js).
  - The tool's saved copy is now given. The script I pulled from line 8980's input, the tool's copy workflows/scripts/sixth-look-wf_14e38511-111.js (6375 bytes, saved 21:37:56) and the scratchpad's sixth-look-as-run.js are byte for byte the same (`cmp` passed on both pairs).
  - The tool-copy path is the same one line 9630 names.

(2) AND (3): FINDINGS ON THE CHANGED LINES

1. Minor. Verdict: does not bear yet.
Target: line 25, "(the first message of entry 26 is at line 1416)".
Defect: I could confirm only half of the claim. Line 1416 exists: it is the owner's upload of the two screenplays with "Here. Try these two" (listing output, 11:14:20). Entry 26 in the project story opens "You supplied two versions of your screenplay", which fits. But the word "first" needs to know that no earlier owner message belongs to entry 26, and "Here." reads like an answer to an earlier exchange.
Grounds: the listing starts at line 1400, and I was allowed to read the session record only at the named lines. Neither entry 26 nor the opening of `26 Test - The Catch - two versions.md` quotes an earlier request.
Connection: if an earlier owner request opened entry 26, the listing would miss it. Check 2 asks the reviewer to walk every owner message through the CLAUDE.md line. Little rests on it, because C17 is about lines 8822 to 9530, and the "12 hours" start (the upload) is at 1416 either way.
Test that would settle it: print the last owner message before line 1416 (the same command, reading lines 1 to 1415) and see whether it belongs to entry 25 or to entry 26.
Cheap fix: "(the owner's upload of the screenplays for entry 26 is at line 1416)", which I checked and found true.

No other finding. The changed lines state events, not the lead's view of the change. They add no finding or verdict of the lead's. They do not steer the reviewer or narrow what it may find. Dropping sixth-look-original.js removes a pointer the second check found inexact; the reviewer still has lines 8961 and 8971, the journal and both copies of the script. Every new path is read-only: the session record, the journal, the tool's saved copy and the scratchpad copy. The listing command only reads. Nothing new points at writing into /home/user/StoryTest or at GitHub, and the unchanged Rules section still forbids both.

WHAT I DID NOT CHECK
- Session-record lines other than 8961, 8980, 9530 and 9630, and the ten printed by the listing. So I did not check whether an earlier assistant text sits between 9531 and 9629 (it would not make line 25 or 47 false). Nor did I check whether the script shown at 9630 is the whole as-run script; that is entry 34's claim, left to the reviewer.
- Whether the skip list or the isMeta test on line 35 hides an owner message in the span. For example, a record that begins with a system reminder and carries the owner's words after it would be hidden. Testing this would need a changed command; the "<\system-reminder>", "Caveat:" and isMeta skips were already there when the second check read the brief.
- Finding 1's test above.
- The brief's unchanged lines and the staged change itself.

I made no copy of the workshop and ran no test. Nothing in /home/user/StoryTest was edited, staged or committed. I wrote two comparison files to the scratchpad: verify-diff-entry34-2.txt and check8980-script-2.js.
````

## 5. The scripts that ran them

### entry-34-35-final-look-wf_b00177ed-c72.js

````js
export const meta = {
  name: 'entry-34-35-final-look',
  description: 'The one short look the owner agreed to: the edits since the last look, for log entries 34 and 35',
  phases: [
    { title: 'Final look', detail: 'theory-checker reads only the lines changed since the last look' },
  ],
}

const SCRATCHPAD = '/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad'

phase('Final look')
const report = await agent(
  'You are giving one short, final look at edits to a staged change in the story workshop at /home/user/StoryTest. You did not make the change or the edits; the lead agent did. The owner agreed to this one look ("And yes", session record line 10242) after the lead put the cost to them, as the workshop\'s proportion rule requires (/home/user/StoryTest/.claude/skills/error-correction/references/reviews-and-briefs.md, section 4, "Proportion, and when to stop"). Anything short of a must-change you find will be recorded as open; so look only for must-changes, and list anything smaller in one line each. ' +
  'The edits made since the last look are exactly ' + SCRATCHPAD + '/entry34-changes-since-last-look.diff. The last look\'s report is ' + SCRATCHPAD + '/entry34-last-look-report.md; the lead\'s account of how its findings were answered is the section "The last look\'s findings" at the end of ' + SCRATCHPAD + '/entry34-findings-answered.md (every statement in it is the lead\'s claim, to check). The edits also add log entry 35 and the owner\'s answer to question S14. ' +
  'What entry 35 describes: the owner wrote "No. The screenplay. The latestest revision" (session record line 10114). The lead then made a revised screenplay from the owner\'s Final4: the original is /root/.claude/uploads/d4341bef-a251-5a02-b92c-5a2687b808be/a64e4837-The-Catch-Final4.txt, the undated version is /root/.claude/uploads/d4341bef-a251-5a02-b92c-5a2687b808be/65e1e528-The-Catch.txt, the revision is "' + SCRATCHPAD + '/revision/35 The Catch - workshop revision of Final4.txt", made by ' + SCRATCHPAD + '/revision/make_revision.py, with its list of edits in "' + SCRATCHPAD + '/revision/35 The Catch - the 50 edits and their reasons.txt". The notes it applies are in /home/user/StoryTest/26 Test - The Catch - two versions.md. The session record is /root/.claude/projects/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be.jsonl, a very large file: read it only at lines 10114 and 10242. ' +
  'Check only: (1) each of the last look\'s must-changes (A to E) is answered as the account says; (2) every statement the edits add (entry 35, S14\'s answer, the status lines, the line on saving these records) is true to those files and those two owner messages, quotes the owner exactly, and contradicts nothing else in the change or in CLAUDE.md; in particular, test entry 35\'s counts (50 edits, about 7 per cent longer, about the length of the undated version) and its list of the main edits against the revision and the edit list. You may run read-only commands (diff, wc, grep, python that only reads). Do not judge the screenplay\'s craft; that is the owner\'s call. ' +
  'Must change means: a false statement, a misquote, a missing part of a correction\'s form (references/recording.md, section 2), a contradiction. Give each finding with target, defect, grounds, grade and verdict; then what you checked and found right, and what you did not check. End with one verdict: passed, passed after changes, or not passed. ' +
  'Never edit, stage, commit or run anything that writes in /home/user/StoryTest or in the scratchpad; never touch GitHub. Your final message is your report; it will be kept word for word in the review receipt.',
  { label: 'final look', phase: 'Final look', agentType: 'theory-checker' })

return { report }
````

### entry-34-last-look-wf_fd59ac0d-7d8.js

````js
export const meta = {
  name: 'entry-34-last-look',
  description: 'One last narrow look, by one agent, at the edits answering the narrow look of entry 34',
  phases: [
    { title: 'Last look', detail: 'theory-checker reads only the lines changed since the narrow look' },
  ],
}

const SCRATCHPAD = '/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad'

phase('Last look')
const report = await agent(
  'You are giving one last narrow look at edits to a staged change in the story workshop at /home/user/StoryTest. You did not make the change or the edits; the lead agent did. Under the workshop\'s proportion rule (/home/user/StoryTest/.claude/skills/error-correction/references/reviews-and-briefs.md, section 4, "Proportion, and when to stop") this is past the second round: anything short of a must-change you find will be recorded as open, and a must-change goes to the owner with its cost before any further round. So look only for must-changes in the edits, and list anything smaller briefly. ' +
  'The narrow look\'s report is ' + SCRATCHPAD + '/entry34-narrow-look-report.md. The edits made since it are exactly ' + SCRATCHPAD + '/entry34-changes-since-narrow-look.diff. The lead\'s account of how each of its findings was answered is the section "The narrow look\'s findings" at the end of ' + SCRATCHPAD + '/entry34-findings-answered.md: every statement in it is the lead\'s claim, to check. The brief the earlier reviewers worked under, with its events and sources, is ' + SCRATCHPAD + '/entry34-brief.md; its rules apply to you: read only, no copy of the workshop, no tests. The machine checks, run by the lead after the edits: ' + SCRATCHPAD + '/checks-entry-34.txt. ' +
  'Check only: (1) is each finding answered as the account says, and is anything in that section false? (2) do the edits add anything false, misquote the owner, contradict another line of the change or of CLAUDE.md, or leave a part of a correction\'s form (references/recording.md, section 2) missing? ' +
  'Must change means: a false statement, a misquote, a missing part, a line that fails the case it answers or stops a plain owner request, a contradiction. Give each finding with target, defect, grounds, grade and verdict (bears, does not bear yet, does not bear); then what you checked and found right, and what you did not check. End with one verdict: passed, passed after changes, or not passed. ' +
  'Never edit, stage, commit or run anything that writes in /home/user/StoryTest; never touch GitHub. Your final message is your report; it will be kept word for word in the review receipt.',
  { label: 'last look', phase: 'Last look', agentType: 'theory-checker' })

return { report }
````

### entry-34-narrow-look-wf_9aa10876-aa2.js

````js
export const meta = {
  name: 'entry-34-narrow-look',
  description: 'One narrow look, by one agent, at the edits made to answer the review of entry 34',
  phases: [
    { title: 'Narrow look', detail: 'theory-checker reads only the lines changed since the review' },
  ],
}

const SCRATCHPAD = '/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad'

phase('Narrow look')
const report = await agent(
  'You are giving one narrow look at edits to a staged change in the story workshop at /home/user/StoryTest, as its proportion rule says (/home/user/StoryTest/.claude/skills/error-correction/references/reviews-and-briefs.md, section 4, "Proportion, and when to stop": the answers to a round get one narrow look at the lines they changed, by one agent). You did not make the change or the edits; the lead agent did. ' +
  'The review of the change is ' + SCRATCHPAD + '/entry34-review-report.md; the brief it worked under is ' + SCRATCHPAD + '/entry34-brief.md (its events and sources apply to you too, and so do its rules: read only, no copy of the workshop, no tests). ' +
  'The edits made since that review are exactly ' + SCRATCHPAD + '/entry34-changes-since-review.diff, plus one new file, /home/user/StoryTest/.claude/reviews/kept/2026-09-24-build-sixth-look-review-script.md. The lead\'s account of how each finding was answered is ' + SCRATCHPAD + '/entry34-findings-answered.md: every statement in it is the lead\'s claim, to check. The whole staged change is git -C /home/user/StoryTest diff --cached; read only the lines the edits touch, and what they cite. The machine checks, run by the lead after the edits: ' + SCRATCHPAD + '/checks-entry-34.txt. ' +
  'Check only: (1) is each finding answered as the account says, and is anything in the account false? (2) do the edits add anything false, misquote the owner, use a word in a second sense, or leave a part of a correction\'s form missing (references/recording.md, section 2)? (3) the changed line in /home/user/StoryTest/CLAUDE.md (the line on taking a request from the owner): give each of its signs and steps a mark with the rule card (references/writing-rules-and-rivals.md, section 2), walk the ten owner messages through it again, and say whether it now stops any plain request it should not, or contradicts another line of CLAUDE.md or the error-correction skill; (4) the new kept file: is it the script as the session record shows it at line 8980, and is its note true? ' +
  'Grade each finding: must change (a false statement, a misquote, a missing part, a line that fails its case or stops a plain request, a contradiction), should change, or minor, with target, defect, grounds, connection and verdict (bears, does not bear yet, does not bear). This is the second round: after it, only must-changes will be put right; the rest will be recorded as open. Then give what you checked and found right, and what you did not check. End with one verdict: passed, passed after changes, or not passed. ' +
  'Never edit, stage, commit or run anything that writes in /home/user/StoryTest; never touch GitHub. Your final message is your report; it will be kept word for word in the review receipt.',
  { label: 'narrow look', phase: 'Narrow look', agentType: 'theory-checker' })

return { report }
````

### entry-34-review-2-wf_def3a5e2-211.js

````js
export const meta = {
  name: 'entry-34-review-2',
  description: 'A narrow check of the brief\'s changed lines, then one reviewer of the staged change for log entry 34',
  phases: [
    { title: 'Brief recheck', detail: 'theory-checker checks only the brief\'s changed lines' },
    { title: 'Review', detail: 'one theory-checker reads the changed lines of the workshop' },
  ],
}

const SCRATCHPAD = '/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad'
const BRIEF = SCRATCHPAD + '/entry34-brief.md'

phase('Brief recheck')
const brief_recheck = await agent(
  'You are making a narrow check of a revised brief before it goes out to a reviewer, as the story workshop\'s rules say (/home/user/StoryTest/.claude/skills/error-correction/references/reviews-and-briefs.md, section 5, and section 4\'s paragraph "Proportion, and when to stop": a revised brief is checked only for its changed lines). You did not write it; the lead agent did. ' +
  'The revised brief is ' + BRIEF + '; its first version is ' + SCRATCHPAD + '/entry34-brief-first.md; the changed lines are in ' + SCRATCHPAD + '/entry34-brief-changes.diff; the first check\'s report, with its 8 findings, is ' + SCRATCHPAD + '/entry34-brief-check-report.md. ' +
  'Check only: (1) each of the 8 findings is answered by the changed lines, or say which is not; (2) the changed lines add nothing false, no finding or verdict of the lead\'s about the change, nothing that steers the reviewer or narrows what it may find, and nothing that could lead it to write into /home/user/StoryTest or touch GitHub; (3) every new pointer (a file, a line of the session record, a run) exists and says what the brief claims, reading the session record only at the lines named; you may run the brief\'s listing command once, since it only reads. ' +
  'Do not review the staged change itself; that is the reviewer\'s job. Do not make a copy of the workshop or run any test. Never edit, stage or commit anything. ' +
  'In the report field, give each finding numbered, with target, defect, grounds and grade (must change, should change, minor), then what you did not check. In must_change, one line per must-change finding (empty if none). Verdict: passed, passed after changes, or not passed.',
  {
    label: 'brief recheck',
    phase: 'Brief recheck',
    agentType: 'theory-checker',
    schema: {
      type: 'object',
      properties: {
        verdict: { type: 'string', enum: ['passed', 'passed after changes', 'not passed'] },
        must_change: { type: 'array', items: { type: 'string' } },
        report: { type: 'string' },
      },
      required: ['verdict', 'must_change', 'report'],
    },
  })

if (!brief_recheck || brief_recheck.must_change.length > 0) {
  log('The brief recheck found a must-change (or did not return), so the reviewer was not started.')
  return { brief_recheck, review: null }
}
log('Brief recheck: ' + brief_recheck.verdict + ', no must-change; starting the one reviewer.')

phase('Review')
const review = await agent(
  'You are the one reviewer of a staged change to the story workshop at /home/user/StoryTest. Your brief is ' + BRIEF + '. Read it first and follow it exactly, including its rules: read only, no copy of the workshop, no tests. ' +
  'Your final message is your report, in the form the brief gives; it will be kept word for word in the review receipt.',
  { label: 'review', phase: 'Review', agentType: 'theory-checker' })

return { brief_recheck, review }
````

### entry-34-review-3-wf_a5ecad8b-2da.js

````js
export const meta = {
  name: 'entry-34-review-3',
  description: 'A last narrow check of the brief\'s newly changed lines, then one reviewer of the staged change for log entry 34',
  phases: [
    { title: 'Brief recheck', detail: 'theory-checker checks only the lines changed since the second check' },
    { title: 'Review', detail: 'one theory-checker reads the changed lines of the workshop' },
  ],
}

const SCRATCHPAD = '/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad'
const BRIEF = SCRATCHPAD + '/entry34-brief.md'

phase('Brief recheck')
const brief_recheck = await agent(
  'You are making a narrow check of a revised brief before it goes out to a reviewer, as the story workshop\'s rules say (/home/user/StoryTest/.claude/skills/error-correction/references/reviews-and-briefs.md, section 5, and section 4\'s paragraph "Proportion, and when to stop": a revised brief is checked only for its changed lines). You did not write it; the lead agent did. ' +
  'The brief is ' + BRIEF + '. The version the second check saw is ' + SCRATCHPAD + '/entry34-brief-second.md; the lines changed since are in ' + SCRATCHPAD + '/entry34-brief-changes-2.diff; the second check\'s report, with its 4 findings, is ' + SCRATCHPAD + '/entry34-brief-recheck-report.md. ' +
  'Check only: (1) each of those 4 findings is answered by the changed lines, or say which is not; (2) the changed lines add nothing false, no finding or verdict of the lead\'s about the change, nothing that steers the reviewer or narrows what it may find, and nothing that could lead it to write into /home/user/StoryTest or touch GitHub; (3) every new pointer (a line of the session record, a record of the run\'s journal, a file) exists and says what the brief claims; read the session record only at the lines named; you may run the brief\'s listing command once, since it only reads. ' +
  'Do not review the staged change itself, and do not recheck lines the earlier checks saw. Do not make a copy of the workshop or run any test. Never edit, stage or commit anything. ' +
  'In the report field, give each finding numbered, with target, defect, grounds and grade (must change, should change, minor), then what you did not check. In must_change, one line per must-change finding (empty if none). Verdict: passed, passed after changes, or not passed.',
  {
    label: 'brief recheck 2',
    phase: 'Brief recheck',
    agentType: 'theory-checker',
    schema: {
      type: 'object',
      properties: {
        verdict: { type: 'string', enum: ['passed', 'passed after changes', 'not passed'] },
        must_change: { type: 'array', items: { type: 'string' } },
        report: { type: 'string' },
      },
      required: ['verdict', 'must_change', 'report'],
    },
  })

if (!brief_recheck || brief_recheck.must_change.length > 0) {
  log('The last brief recheck found a must-change (or did not return). Under the proportion rule this goes to the owner with its cost; the reviewer was not started.')
  return { brief_recheck, review: null }
}
log('Brief recheck: ' + brief_recheck.verdict + ', no must-change; starting the one reviewer.')

phase('Review')
const review = await agent(
  'You are the one reviewer of a staged change to the story workshop at /home/user/StoryTest. Your brief is ' + BRIEF + '. Read it first and follow it exactly, including its rules: read only, no copy of the workshop, no tests. ' +
  'Your final message is your report, in the form the brief gives; it will be kept word for word in the review receipt.',
  { label: 'review', phase: 'Review', agentType: 'theory-checker' })

return { brief_recheck, review }
````

### entry-34-review-wf_8c48984f-01f.js

````js
export const meta = {
  name: 'entry-34-review',
  description: 'One check of the brief, then one reviewer of the staged change for log entry 34 (the proportionate review rule)',
  phases: [
    { title: 'Brief check', detail: 'theory-checker checks the brief once' },
    { title: 'Review', detail: 'one theory-checker reads the changed lines' },
  ],
}

const SCRATCHPAD = '/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad'
const BRIEF = SCRATCHPAD + '/entry34-brief.md'

phase('Brief check')
const brief_check = await agent(
  'You are checking a brief before it goes out to a reviewer, as the story workshop\'s rule for briefs says (/home/user/StoryTest/.claude/skills/error-correction/references/reviews-and-briefs.md, section 5, and the paragraph "Proportion, and when to stop" in section 4: a brief is checked once). You did not write it; the lead agent did. ' +
  'The brief is ' + BRIEF + '. Check only the brief, in proportion: (1) every pointer it gives (a file, a section, a line of the session record, a time) exists and says what the brief claims; read the session record only at the lines the brief names, never the whole file, since it is very large; (2) every quotation of the owner is word for word; (3) it carries no finding or verdict of the lead\'s about the change, and does not steer the reviewer toward an answer or narrow what the reviewer may find; (4) it includes the kinds-table rows that apply, and its definition of must change fits section 4 of that file; (5) nothing in it could lead the reviewer to write into /home/user/StoryTest or touch GitHub. ' +
  'Do not review the change itself; that is the reviewer\'s job. Do not make a copy of the workshop or run any test. Never edit, stage or commit anything. ' +
  'In the report field, give each finding numbered, with target, defect, grounds and grade (must change, should change, minor), then what you did not check. In must_change, one line per must-change finding (empty if none). Verdict: passed, passed after changes, or not passed.',
  {
    label: 'brief check',
    phase: 'Brief check',
    agentType: 'theory-checker',
    schema: {
      type: 'object',
      properties: {
        verdict: { type: 'string', enum: ['passed', 'passed after changes', 'not passed'] },
        must_change: { type: 'array', items: { type: 'string' } },
        report: { type: 'string' },
      },
      required: ['verdict', 'must_change', 'report'],
    },
  })

if (!brief_check || brief_check.must_change.length > 0) {
  log('The brief check found a must-change (or did not return), so the reviewer was not started.')
  return { brief_check, review: null }
}
log('Brief check: ' + brief_check.verdict + ', no must-change; starting the one reviewer.')

phase('Review')
const review = await agent(
  'You are the one reviewer of a staged change to the story workshop at /home/user/StoryTest. Your brief is ' + BRIEF + '. Read it first and follow it exactly, including its rules: read only, no copy of the workshop, no tests. ' +
  'Your final message is your report, in the form the brief gives; it will be kept word for word in the review receipt.',
  { label: 'review', phase: 'Review', agentType: 'theory-checker' })

return { brief_check, review }
````
