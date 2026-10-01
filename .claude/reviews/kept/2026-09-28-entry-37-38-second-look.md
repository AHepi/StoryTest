# Second look: entries 37 to 39, files 37 and 38, `errors.csv`, the script, README

Reviewer: theory-checker. This is a narrow look at `git diff` (working files against the staged index) only.

**Verdict: passed after changes.** All 30 earlier findings (13 must-change, 17 should-change) are applied or answered, and none is left open. The edits bring 2 new must-change findings, 3 new should-change findings and 7 notes. Each is a sentence or a table cell, listed at the end.

## The earlier findings, one line each

| # | Status | Why |
|---|---|---|
| M1 | applied | The four rows are re-described, "nine" Fable reviews, and the owner's critique is described as finding again a raised point. But the rewrite now says every fault was raised and "not missed", which goes too far for *Seconds*: see new finding NM1. My first report's heading made the same overstatement. |
| M2 | applied | Proposal 3's reason is withdrawn as not surviving review. The guard is dropped, with the depth-of-answer idea marked untested. The stages' lack of a quibble bin is stated in file 37 line 44 and file 38 line 80. |
| M3 | answered | Counts are redefined as "findings each checker weighed, credited to every critic its table names" (file 37 line 74). Both columns are explained, the substantive-only recount is credited to me, MiMo judging itself is stated, "It marked most quibbles as substantive" is gone, and proposal 5 points to file 37. |
| M4 | applied | "would have lost no confirmed finding"; one confirmed finding, in round 1 (file 38 lines 124 and 135). |
| M5 | applied | *Unknown*, two routes. "Every *Long Places* round used exact edits": all seven plans (rounds 1 to 6 and the copyedits) have Find/Replace edits and a once-only check, as do round 8's plan and round 9's asserts. The old line 22 claim is gone. |
| M6 | applied | File 38 line 146: the word-by-word check against the ruling found GLM's changes, and a logged change would pass stage 09's version. |
| M7 | applied | Round 9 is given as 2 runs, 4 agents, about 19 minutes and 0.41 million tokens, with no critics (file 37 line 117; file 38 lines 159–163; entry 38). |
| M8 | applied | "from round 2 on; the rulings left it open in rounds 3, 4, 6 and 7", in file 37, file 38 and `errors.csv`. |
| M9 | applied | One case; the rounds adopted the check from Seconds entry 52; round 9's miss is excluded with the reason. |
| M10 | applied | Two within their own round, three at the next round, five two or more rounds later. |
| M11 | applied | Marks defined in the skill's sense, quoted as "not a truth-meter"; held, held if, loose, unknown and two routes are used. |
| M12 | applied | File 37 lines 40–44 carry the reading, labelled as mine. |
| M13 | applied | 34 rows; the LP 21 row notes the same slip in Seconds entry 30; MiMo made 2. No stale "35" remains; the "35"s left are the run count and entry 35. |
| S1 | applied | "rows", with the grain explained (file 37 line 57). |
| S2 | applied | Each story's ending told separately (file 37 lines 36–38). |
| S3 | applied | Episodes 1–5 drafted by Claude; GLM revised 4 and 5 and wrote 6 to 10. |
| S4 | applied | 781 minutes and 12.4 million tokens were other work (file 37 line 126). |
| S5 | applied | Both counter-cases are in, and 9 of 10 are in scope. One phrase is now too strong: new finding NS1. |
| S6 | applied | "fell fast" only for *The Long Places*; "several later fixes mended earlier ones". |
| S7 | applied | 4(a) says the only new part is the rule for after the last review. |
| S8 | applied | The cases and marks are given; "two rounds" is loose. One quotation is cut short: new finding NS3. |
| S9 | applied | Held if the checker is independent; the specifics are loose. But "mostly fail" is now undefined: new finding NS2. |
| S10 | applied | The stage 09 reference, §1 item 3, is quoted and was read. |
| S11 | applied | File 38 line 60. |
| S12 | applied | README names the findings, runs and model-calls tables, and says the findings table alone can be remade later. |
| S13 | applied | I checked this: loading the changed script's source without writing bytecode and calling `record_findings` printed "note: no Critic/Verdict table in stories/the-long-places/44 Round 8 - the checker's advice.md; nothing read from it" and returned 297 rows identical to `findings.csv`. The findings-only mode reads correctly; I did not run `main()`. `git status` showed nothing new in the repository. |
| S14 | applied | (a) file 38 line 26 and file 37 line 108; (b) line 25; (c) file 37 lines 5–11 and entry 37; (d) line 23; (e) file 37 line 129; (f) lines 83–89. |
| S15 | applied | File 38 lines 164–167 label the choice-test link and add stage 08's `story-critique` lead. (See N4 for the table cell.) |
| S16 | answered | "Counted from the tables"; the claim "only figures these printed" is gone. |
| S17 | applied | Each proposal has a cost line. One figure in them is wrong: new finding NM2. |

Other claims in the new text that I checked:
- The owner's words in entry 39 ("2 agents at a time. Not 15.") match the transcript.
- "The largest single run earlier had used 14 in all" is right (seconds-episodes, 14 agents).
- The `findings.csv` rows entry 37 cites (84, 179, 188, 268 and 269, and 6 for the reunion, counting file lines) say what it claims. Row 179 bears out "the rule used before it was taught" in round 2.
- `findings.csv` row 8 (file 38 line 174) is MiMo's one confirmed finding.
- The two stray copies I made are gone.

## New findings

**NM1. Must change. "Every one of them had been raised … not missed" goes too far for *Seconds*.**
- *Targets:* file 37 lines 101 and 107; file 38 lines 70 and 91; the `errors.csv` Seconds 51 row.
- *Grounds:*
  - Of the eight kinds of slip in that row, these were raised during the rounds:
    - "Aye": `findings.csv` rows 188 and 268, and the round 3, 4 and 7 critiques;
    - the rule used before it was taught: rows 179 and 269;
    - the pencil: rows 181 and 207;
    - "two years for seven": Fable's round-5 review, "the nurse has just said 'Not since 2019', which is seven years";
    - the June "birthday boy": Fable's round-7 review, "Kieran's birthday was in March".
  - A keyword search of `findings.csv`, the critiques, MiMo's advice and Fable's reviews found no earlier mention of three: the uncle called "dad", the name never introduced, and the explanation that lost all five viewers.
- *Connection:* for the *Seconds* row, "not missed" holds for five of eight kinds, not all. The `errors.csv` row already says "(in part)", but the prose does not. The row also omits Fable's two.
- *Verdict:* does not bear.
- *Fix:*
  - Say "each of the four rows had faults raised during the rounds; on *Seconds*, five of the eight kinds (the last two by Fable, rounds 5 and 7); three were not found raised".
  - Add Fable's two to the row.
  - In file 38 line 91, "better" still stands for most of them. But say that those three are a small basis for 3(b), with the caveat that the search was by keyword.

**NM2. Must change. The panel's cost "about three times as long run two at a time" is wrong.**
- *Targets:* file 38 line 86; entry 39's last sentence.
- *Grounds:* the tests already ran two at a time.
  - In `long-places-audience-claude`, the readers started in pairs (ana and tom at 0; priya when ana ended; and so on).
  - `seconds-audience-claude` ran at most 2 at once.
  - A `long-places-step` round ran at most 2 at once.
  - *The Long Places* entry 21: "my workflow tool runs at most two at a time on this machine".
- *Connection:* the measured 21 to 23 minutes are already the two-at-a-time figure.
- *Verdict:* does not bear.
- *Fix:* "the tests already ran two at a time, so these figures stand". Drop "three times as long" from both places.

**NS1. Should change. File 38 line 58: "A miss, and a slip it caused".**
- *Grounds:* the noun was dropped by the round-4 ruling's own wording: "No instruments deployed." became "None of mine deployed." (plan file 30, R4b). The planner's suggestion, "None deployed by me", kept that loss; it did not cause it.
- My first report's S5 wording ("the one that later lost its noun") invited this.
- *Fix:* "and a wording it suggested that kept the ruling's lost noun".

**NS2. Should change. Proposal 5's "a critic whose findings mostly fail" is undefined.**
- *Targets:* file 38 lines 130 and 137; entry 38, item 5.
- *Grounds:*
  - If a quibble counts as failing, every critic in the data would be replaced. None had half its weighed findings confirmed; the best is *The Long Places* story critic, 15 of 33.
  - The proposal text no longer says "after two rounds", but the mark still calls it loose.
- *Fix:* define "fail" as "judged wrong", and put the round count back into the proposal (or drop it from the mark).

**NS3. Should change. A quotation is cut short (file 38 line 113).**
- *Grounds:* *The Long Places* entry 29 reads "when a point keeps coming back and costs a clause to settle, settle it the first time". Line 113 drops "the first time", credits the words to both entry 29 and *Seconds* entry 38, and then line 119 names the full phrase as the rival.
- *Fix:* quote entry 29 in full, and *Seconds* entry 38 in its own words ("a point that keeps coming back and costs a line gets settled").

## Notes

- **N1.** File 38 line 98, "found new substantive points every time": "new" is not shown, because the voice point recurred. Say "substantive points".
- **N2.** File 37 lines 139 and 142 say my report "is kept with the review receipt" and the findings "are answered in the receipt". No receipt is in the working tree yet. Make sure it is written before the commit.
- **N3.** File 38 line 35, "Its Verify then checks only …": stage 09's Verify also checks that every finding is answered. Say "on the changes themselves".
- **N4.** The `errors.csv` LP 46 cell, "so his staying has only one option on the page", is the workshop's choice-test reading and is not labelled in the table (file 38 labels it).
- **N5.** Script: with all three session sources given but an empty call log, `write_table` would fail on `rows[0]` after writing two tables. This is harmless now.
- **N6.** File 37 line 37 lists Fable's finished-book review before both audience tests. It started before MiMo's test (LP entry 36) and was logged after it (entry 38), so it ran alongside. That is acceptable as written.
- **N7.** "Aye" was also raised by the round 3, 4 and 7 critiques. "Rounds 2 and 6" is a floor, not the whole.

## Not checked

- The rest of file 37, file 38 and the project story outside the diff.
- The rewritten entries' other claims about the gate stopping the first commit.
- `main()` of the changed script end to end: I called only its findings reader, which writes nothing.

## Changes to make

1. NM1: re-scope "every one had been raised / not missed" for *Seconds*, and add Fable's two.
2. NM2: drop "about three times as long" from file 38 and entry 39.
3. NS1: replace "a slip it caused".
4. NS2: define "fail" and put back or drop the round count.
5. NS3: quote entry 29 in full.

The notes are optional.

**Verdict: passed after changes.** Earlier findings: 30 of 30 applied or answered, 0 open. New: 2 must-change, 3 should-change, 7 notes.
