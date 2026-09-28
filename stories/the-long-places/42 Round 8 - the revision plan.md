# 42 Round 8 - the revision plan

*The planner's exact plan for your three changes: 254 find-and-replace edits, a ledger of every repeated phrase, the word budget and the check of every clue. Section 6 holds my decisions on it, which override the rest.*

---


This plan carries out the round 8 ruling (`round-8/ruling.md`) and nothing else: the owner's three changes (say the repeated things less often and let people sound different; shorten the side-trips; one person says to Halden's face what he did) and the four slips. It was written after reading all fourteen round-7 chapters, the ruling, the concept (file 01), and, for background, the Claude readers' analysis and reports (file 40).

**How this plan was made and checked.** Every change below is an exact Find → Replace on a round-7 chapter file. I applied all 254 of them to copies of the round-7 files and then:
- checked that every Find occurs exactly once in its round-7 chapter, and that no two Finds overlap, so the edits can be made in any order;
- checked that every line number given is the line of the round-7 file where the Find begins;
- counted the words of every result (the numbers in section 1 are counts of those copies, not estimates);
- counted every limited phrase in the result (the KEEP totals in section 2 are what the revised text actually contains);
- read every seam in place.

## Rules for the revisers

- **Source.** Work from the round-7 files: `long-places-rounds/round-7/chapter-NN.md`. Line numbers are those files' line numbers as they stand now. Copy each chapter into the round-8 folder (or wherever your own task says) and make the changes there. Do not edit the round-7 files, the ruling, or anything under `/home/user/StoryTest/stories/the-long-places`.
- **Exactness.** Make only the changes listed for your chapters, exactly as written, character for character. Do not touch any other sentence, even one that looks improvable. The files use straight apostrophes (`'`) and straight double quotes (`"`); the dash is the em dash (—); italics are asterisks. Where a Find begins with a space, so does its Replace; the space is part of the text.
- **Quoting.** In this plan « » only mark where a quoted text begins and ends; they are not part of it. `¶` marks a paragraph break (a blank line between paragraphs). An ellipsis inside « » (…) never appears in a Find: long cuts are given by their first and last words, and you cut everything from the first word shown to the last word shown, inclusive.
- **Seams.** When a cut is replaced by nothing, the plan shows how the seam reads; check that yours reads the same. Where a whole paragraph goes, remove it and one of the blank lines around it, so that exactly one blank line separates the paragraphs that remain.
- **Order.** The edits within a chapter are numbered in the order they occur. Because no two overlap and each Find is unique in the round-7 text, the order in which you apply them does not matter.
- **The letters.** The italic letters change only where this plan says, and every such change is a phrase-limit change (or slip 2). The letter at the head of I and its copy at the end of XIV (XIV:133–159) must stay word-for-word identical; neither is touched.
- **Melek and Halden** speak exactly as now. No line of theirs is changed. (XI.13 changes a line of narration inside Melek's confession, not her words.)
- **Counting.** Word counts in this plan use the ruling's method: the text split on white space, which counts a spaced em dash as a word (it gives the ruling's 50,094 for round 7). `wc -w` in this environment (a UTF-8 locale) does not count a lone em dash, so its figures run about 0.8% lower; both are given in section 1. (In a C locale `wc -w` gives the ruling's figures.)

## Shared wording (the three blocks must agree)

These texts are fixed. They appear only where listed.

- **Slip 1, the grandmother's watch** (blocks A and C).
  - I:57 (I.3, I.4): «Melek told the watch story, meaning nothing by it. Her grandmother had kept a pocket watch, a wedding piece, and carried it down with her. Every time the old woman came up from a night below, the watch was an hour behind.» and «An old watch, an old woman, a bell». The saying «*a clock is a donkey, you beat it and it walks.*» stays word for word.
  - III:95 (III.20): «Nilay told the watch story then, to change the subject — Melek's grandmother, the pocket watch, *a clock is a donkey, you beat it and it walks* —».
  - IV:115 (IV.15): «an hour-behind watch,».
  - XIII:47 (XIII.11): «*The keeper's watch retards one hour upon each night below; she sets it by the church bell; a clock is a donkey, she says; you beat it and it walks. Nothing to record.*» (only «clock» → «watch» in the first clause).
  - After the round, the words «wall clock», «clock story», «hour-behind clock» and «keeper's clock» occur nowhere in the book.
- **Slip 2** (XI:17, XI.4): «was hers for sixty years before it was mine». Melek's «forty winters» / «Forty years» at the niche (XI:61–73) are a different thing and stay.
- **Slip 4, "Nine"** (V:43, V.7), at its first use only: «Fatma Nine — *Nine* is the village's word for a grandmother — waking from a doze,». "Nine" is explained nowhere else.
- **Change 3.** XIII:110 (XIII.21) carries Nilay's two spoken sentences and leaves Halden's existing reply, «"You have kept excellent records," he said.» (XIII:112), untouched. XIV:115 (XIV.20) gives the new reason for striking the third sentence. The words «accusations want a court» then occur once in the book, at XIII:102, where the ruling leaves them.

**Cross-block dependencies.** Some cuts remove a repeat because the first telling stays elsewhere. Each reviser must leave the first telling alone (it is not in anyone's list of changes):

| This cut | relies on this staying unchanged |
|---|---|
| III.2 (Márton scolding the tractor), III.18 (Yusuf's tripod introduction) | I:67 |
| III.5 (the plans agreeing on the treads) | II:31 |
| IV.12 and XIII.13 ("typescripts and hands … never varied by a word") | III:73 |
| IV.13 ("backdating, the least mysterious practice") | I:59 |
| VII.19 ("politely, the way institutions ask") | VI:47 |
| XI.26 ("her nails were a committee where Melek's had been a decision") | IX:77 (Márton's version) |
| XIII.7 ("grayer by nothing, dated and sound, the age of good paper") | IV:51 |
| XIII.23 (giving her name at the mouth) | XIV:15 |
| XIII.24 ("like a doorman who knows the step") | IX:79 |
| XIV.6 ("The vigil was not announced. It was announced by being kept.") | XI:43 |
| XIV.15 ("like a coal in both hands") | VIII:115 |

The phrase limits are book-wide, so each block must make exactly its own ledger entries (section 2) and no others; the totals only come out right if all three do.

## 1. Word budget

"Now" is round 7. "Planned" is the count of the round-7 text with every change in this plan applied. The ruling's count is the governing one; the `wc -w` columns are for revisers who check with `wc`.

| Chapter | Now (ruling's count) | Now (`wc -w`) | Ruling's target | Planned | Planned (`wc -w`) | Planned cut | Planned against target | Where the cut comes from |
|---|---|---|---|---|---|---|---|---|
| I | 3,025 | 3,008 | 2,900 | **3,002** | 2,985 | -23 | +102 | phrase pass; slip 1 |
| II | 3,047 | 3,015 | 2,950 | **2,950** | 2,920 | -97 | +0 | phrase pass; the explanations routine (II:33) |
| III | 3,215 | 3,195 | 2,700 | **2,713** | 2,702 | -502 | +13 | the gravity numbers and tables |
| IV | 3,624 | 3,603 | 3,300 | **3,366** | 3,347 | -258 | +66 | the first half of Malta |
| V | 3,376 | 3,347 | 3,100 | **3,223** | 3,197 | -153 | +123 | the gas figures around the scenes |
| **Block A** | **16,287** | 16,168 | **14,950** | **15,254** | 15,151 | **-1,033** | **+304** | |
| VI | 3,227 | 3,198 | 2,950 | **2,992** | 2,963 | -235 | +42 | the viral-post stretch and the view counts |
| VII | 4,169 | 4,124 | 3,850 | **3,967** | 3,922 | -202 | +117 | phrase pass (the breach stays whole) |
| VIII | 4,030 | 3,997 | 3,500 | **3,455** | 3,426 | -575 | -45 | the committee and the lab results |
| IX | 3,553 | 3,518 | 3,200 | **3,212** | 3,186 | -341 | +12 | Marques's physics halved; the solstice set-up |
| **Block B** | **14,979** | 14,837 | **13,500** | **13,626** | 13,497 | **-1,353** | **+126** | |
| X | 3,341 | 3,319 | 3,150 | **3,262** | 3,240 | -79 | +112 | phrase pass |
| XI | 3,692 | 3,666 | 3,200 | **3,191** | 3,172 | -501 | -9 | Recep's price list; the traffic correlation; the routine |
| XII | 3,186 | 3,157 | 2,500 | **2,629** | 2,606 | -557 | +129 | the consultancy emails |
| XIII | 3,529 | 3,503 | 2,800 | **3,006** | 2,990 | -523 | +206 | the List and the drowned chapel; change 3 |
| XIV | 5,080 | 5,031 | 4,700 | **4,820** | 4,778 | -260 | +120 | slip 3; Emre's speech; the aside; phrase pass |
| **Block C** | **18,828** | 18,676 | **16,350** | **16,908** | 16,786 | **-1,920** | **+558** | |
| **Book** | **50,094** | 49,681 | **44,800** | **45,788** | **45,434** | **-4,306** | **+988** | |

**The book lands at 45,788 words by the ruling's count (45,434 by `wc -w`): inside 44,500–46,000 by either count, and 8.6% shorter.**

The planned total is above the sum of the suggested chapter targets (44,800) by about a thousand words, and the blocks are above their suggested totals by more than the 200 words the ruling lets me move. I have kept every change as small as the ruling allows, and I could not reach the suggested figures without cutting what the ruling protects. Where the gap comes from:

- **I, II, VII, X ("phrase pass")**: the ordered phrase changes save few words, because most of them vary a phrase rather than delete a sentence. I added no other cuts to I or X. II reaches its target only because the explanations routine at II:33 goes (II.2). VII has trims only outside the breach.
- **XIII (+206)**: the List is down to three lines and the drowned chapel to the boat and the founder's letter. What remains is the photograph of 1949, the Vigil of the Sealed Hour and its margin, the 1924 note (slip 1), the sampling note, the keepership sheet (paid off in XIV), the tin box and wax (used in XIV), the confrontation the ruling leaves in place, the fourth hinge with the new lines, and Halden's closing question. All are plants or protected.
- **XIV (+120)**: the heart of the book (the reunion, the ribbon, the loop, the certificate and the fingerprint note, the coda letter) is untouched except as ordered.
- **V (+123), IV (+66), III (+13), VI (+42), VIII (−45), IX (+12), XI (−9), XII (+129)**: the named sources are cut. The rest of each chapter is plants, loved scenes, or the four explanations the concept needs.

If the main session wants the book nearer 44,800, section 5 lists the next cuts I would make, in order. They are **not** part of this plan.

## 2. The phrase ledger

Every instance in round 7 of every phrase the ruling limits is listed, with its decision. "Ch:line" is the round-7 line. "Paragraph opens" gives the paragraph's first words. The sentence is quoted from round 7; a very long sentence is clipped (…) around the phrase. For CUT and VARY, the edit number points to section 3, where the exact Find and Replace are; for VARY the exact replacement words are also shown here. A KEEP whose sentence is touched by another edit is marked so; the phrase itself stays.

**How the limits are counted.** For three phrases my count differs slightly from the ruling's, and the KEEP totals meet the limits under either count:
- "to the knuckle" / "first knuckle": the ruling's 17 is "to the knuckle" alone. I count both forms together (17 + 9 = 26) and keep 8 in all: the lamp rules (I:11 and its copy XIV:141), the song (XI:49), XIV (XIV:25, XIV:81), and three narrative instances where a new person first takes up the rule (I:43 Melek, IX:77 Márton's last night, XI:103 Nilay's first round).
- "follow past the lamp": the ruling's 5 is the exact phrase. With "follow him / her past the lamp" (III:23, V:21) the family is 7. I keep 3 of the 7 (II:21, V:21, VII:21), so the exact phrase stands twice.
- "past the name, nothing" and variants: I count 12 (the ruling 11), including XIV:15 "past the breaths said nothing". I keep 6. The separate sentence "To speak past the name is how the shamed were treated once" (I:19, II:11, XIV:49, XIV:149) is a different line and is not counted; nor is XII:7 "nothing asked past it". All of those stay.

**Summary**

| Phrase | Now | At most | Planned KEEP (counted in the revised text) |
|---|---|---|---|
| "the whole of" | 31 | 12, and never more than once in a chapter except XIV (2) | **12** |
| "I never do" | 7 | 3 before XIV, plus Emre's in XIV | **3** |
| "follow past the lamp" (and "follow him/her past the lamp") | 7 | 3 (counted with the him/her variants, so that the whole sentence family is 3) | **3** |
| "two breaths" | 19 | 8 | **8** |
| "to the knuckle" / "first knuckle" | 26 | 8 (both forms counted together) | **8** |
| "past the name, nothing" and its variants | 12 | 6 | **6** |
| "flat on the palm" | 3 | 2 | **2** |
| "manners" | 20 | 12 | **12** |
| "the moon's laundry" | 2 | 1 (the first) | **1** |
| the "the way X does Y" simile ("the way the / a / it / she / he …") | 60 | 40 (two thirds of 60) | **37** |
| "which was" | 44 | 29 or fewer (a third cut) | **19** |

"The whole of" is then once each in I, II, IV, V, VII, VIII, X, XI, XII and XIII, and twice in XIV (XIV:89 and the coda copy XIV:155). "I never do" stands twice before XIV (V:21 and VII:21, both in letters) and then in Emre's mouth at XIV:81, where it "sounded like quotation, because it was". The "two breaths" ritual is named in the IV letter and in Malta, glossed by Yusuf (VI:39), and then named only where it weighs most (VII:59, the breach; VIII:111, Leyla's vigil; IX:77, Márton's last descent; XI:89, the returned phrase; XIV:15, the vigil); elsewhere the knock is done without being named. "Which was" is cut from 44 to 19, first in XI (9 → 2), X (7 → 2) and VII (7 → 3); many go inside passages cut for length. "The way X does Y" goes from 60 to 37, first in XIV (13 → 4).


### "the whole of"

Now 31. Limit: 12, and never more than once in a chapter except XIV (2). **KEEP: 12.** (Counted in the revised text by the same pattern: 12.)

| # | Ch:line | Paragraph opens | Sentence (round 7) | Decision | Edit and exact replacement |
|---|---|---|---|---|---|
| 1 | I:25 | *At the third lamp her | If you want the whole of teaching in one sentence: fear spends itself where it is allowed to.* | **KEEP** |  |
| 2 | I:35 | She had spent nineteen summers | That was the whole of it. | **CUT** | I.1 |
| 3 | II:25 | *To the one who keeps | That is the whole of what I know about doors.* | **KEEP** |  |
| 4 | II:39 | And under the stamp, the | And under the stamp, the whole of it, the way it had been the whole of it for twenty-six years: *Male, thirteen. | **VARY** | II.3: «And under the stamp, all of it, as it had been all of it for twenty-six years:» |
| 5 | II:39 | And under the stamp, the | And under the stamp, the whole of it, the way it had been the whole of it for twenty-six years: *Male, thirteen. | **VARY** | II.3: «And under the stamp, all of it, as it had been all of it for twenty-six years:» |
| 6 | III:71 | In the second week he | It was a letter copied out by hand, the whole of it, in a sloping clerk's hand — he checked it against Nilay's March letter at the dig-house table, and … | **VARY** | III.17: «It was a letter copied out by hand, every line of it, in a sloping clerk's hand» |
| 7 | IV:51 | He opened the door at | Gray was the whole of him; he had the age of good paper, dated and sound; his voice had been poured and allowed to set. | **KEEP** |  |
| 8 | V:27 | In ninety-one caves on three | That was the whole of her position, and she held it the way you hold a tool you were fitted for: bad air pooled, … | **CUT** | V.2 |
| 9 | V:45 | It had not rained since | That was the whole of the season in one sentence, and she would spend the rest of the summer being forgiven for it. | **KEEP** |  |
| 10 | VII:11 | *They keep to the edge | That is the whole of the kinship between the near keeping and the far one, and it has always been enough.* | **KEEP** |  |
| 11 | VII:57 | There were two of them | That was the whole of it, she thought, standing there: not ambush, not accident — a house that had been told. | **CUT** | VII.12 |
| 12 | VIII:29 | *To the one who keeps | *To the one who keeps the lamps after me: the grandparents dug upward, all the days of the wall, and the house is here, and the lamps are trimmed, and that is the whole of the record, and it is enough.* | **KEEP** |  |
| 13 | VIII:93 | The file holds four statements | That was the whole of her commentary. | **CUT** | VIII.5 |
| 14 | VIII:115 | Nilay sat the stranger's vigil | That was the whole of the institution, if it was an institution: an economy of sitting, run by women, for debts that no tribunal had ever priced. | **CUT** | VIII.16 |
| 15 | IX:33 | Melek read the sky over | "You knock softly now," she said, and took up her oil can, and that was the whole of the blessing. | **VARY** | IX.5: «and that was all the blessing.» |
| 16 | X:15 | *We have always buried the | That is the whole of the reason, and it has always been enough, and it is not for saying, and I have half said it, which will be forgiven, the wall being long.* | **KEEP** |  |
| 17 | X:27 | Priska Vogel had stood at | Guilt had given her a profession, and a mercy to hand out with it, and the two had always arrived together, which was the whole of her luck and most of her character. | **CUT** | X.1 |
| 18 | X:29 | Melek found him, because the | And at the step, having reported the whole of it: "I did not touch him. | **VARY** | X.2: «And at the step, having reported it all:» |
| 19 | X:57 | He heard her out with | He heard her out with the whole of his attention, which was the most disquieting thing about him, and then he asked, presently, whether the thirteenth bore of her canton was still closed for lining. | **VARY** | X.8: «He heard her out with all his attention — the most disquieting thing about him — and then he asked,» |
| 20 | XI:9 | *It is not given back, | It is set down, and someone after sets it going again, and that is the whole of the manner. | **VARY** | XI.1: «and that is all the manner there is.» |
| 21 | XI:19 | *To the one who keeps | That is the whole of the teaching. | **KEEP** |  |
| 22 | XI:73 | They buried her by the | Halime stood at the edge of the graveside, where the women had put her by putting her nowhere, and Nilay stood beside her for the whole of it, and neither of them asked the other anything, and the burial went on. | **VARY** | XI.15: «and Nilay stood beside her all through it,» |
| 23 | XI:77 | No document had handed Nilay | The office had come to her by refusal, which was how offices moved there: what is given can be resented, and what is refused must be taken up, and the taking up is the whole of the training. | **VARY** | XI.18: «The office had come to her by refusal, as offices moved there: what is given can be resented, and what is refused must be taken up, and the taking up is the training.» |
| 24 | XII:11 | *I said that for years | If you want the whole of this teaching in one sentence: a belief is a keeping, kept.* | **KEEP** |  |
| 25 | XIII:11 | *You will want to ask | Nothing in the manner distinguishes them, and the manner is the whole of what I know. | **KEEP** |  |
| 26 | XIII:29 | Nilay closed the site register | She read it back once, could not fault it, and could not sign it quickly either, and between those two facts lay the whole of her year. | **CUT** | XIII.4 |
| 27 | XIV:7 | Priska came up on the | At the table Nilay gave her the whole of the protocol and none of the reason, and Priska received both portions without comment, warming the Registrar's wax, gone dark red with age, over the stove. | **VARY** | XIV.2: «At the table Nilay gave her all of the protocol and none of the reason,» |
| 28 | XIV:13 | "Then it will hold," Priska | "Then it will hold," Priska said, and pressed her initials into the seal, which is the whole of what a witness owns. | **VARY** | XIV.3: «and pressed her initials into the seal, which is all a witness owns.» |
| 29 | XIV:89 | "Then what happened below is | "Then what happened below is yours," Priska said, and poured, and that was the whole of the interview, and it was the correct whole. | **KEEP** |  |
| 30 | XIV:105 | Seher nodded, at the inside | Seher nodded, at the inside of her own eyelids, and settled, and the mat kept her, and that was the whole of the colloquy. | **CUT** | XIV.19 |
| 31 | XIV:155 | *At the third lamp her | If you want the whole of teaching in one sentence: fear spends itself where it is allowed to.* | **KEEP** |  |

### "I never do"

Now 7. Limit: 3 before XIV, plus Emre's in XIV. **KEEP: 3.** (Counted in the revised text by the same pattern: 3.)

| # | Ch:line | Paragraph opens | Sentence (round 7) | Decision | Edit and exact replacement |
|---|---|---|---|---|---|
| 1 | III:23 | *He left in the morning, | I never do.* | **CUT** | III.1 |
| 2 | V:21 | *She stays the while a | I never do. | **KEEP** |  |
| 3 | VI:19 | *He went up into the | I never do. | **CUT** | VI.2 |
| 4 | VII:21 | *Do not fear them, and | I never do.* | **KEEP** |  |
| 5 | IX:17 | *Understand me: the one who | I never do.* | **CUT** | IX.2 |
| 6 | XI:15 | *She slept by the lamps. | I never do.* | **CUT** | XI.3 |
| 7 | XIV:81 | At the head of the | "I never do," he said, and it sounded like quotation, because it was. | **KEEP** |  |

### "follow past the lamp" (and "follow him/her past the lamp")

Now 7. Limit: 3 (counted with the him/her variants, so that the whole sentence family is 3). **KEEP: 3.** (Counted in the revised text by the same pattern: 3.)

| # | Ch:line | Paragraph opens | Sentence (round 7) | Decision | Edit and exact replacement |
|---|---|---|---|---|---|
| 1 | II:21 | *When the grey came in | … once the wind has finished its argument, and she went up into the grey, and I did not follow past the lamp. | **KEEP** |  |
| 2 | III:23 | *He left in the morning, | I did not follow him past the lamp. | **CUT** | III.1 |
| 3 | V:21 | *She stays the while a | Then she goes, and going out she weeps, every year, in the manner of a person given exactly the thing she came for, and I do not follow her past the lamp. | **KEEP** |  |
| 4 | VI:19 | *He went up into the | *He went up into the morning and the sun went with him, small in the daylight and no less his for that, and I did not follow past the lamp. | **CUT** | VI.2 |
| 5 | VII:21 | *Do not fear them, and | When they go down, they go down, and I do not follow past the lamp. | **KEEP** |  |
| 6 | IX:17 | *Understand me: the one who | I did not follow past the lamp. | **CUT** | IX.2 |
| 7 | XI:15 | *She slept by the lamps. | In the morning she ate a little, and was carried up into the grey, and I did not follow past the lamp. | **CUT** | XI.3 |

### "two breaths"

Now 19. Limit: 8. **KEEP: 8.** (Counted in the revised text by the same pattern: 8.)

| # | Ch:line | Paragraph opens | Sentence (round 7) | Decision | Edit and exact replacement |
|---|---|---|---|---|---|
| 1 | IV:13 | *Company comes. This is what | Knock twice, with the flat of the hand, on the sounding stone, and then wait the length of two breaths, which is longer than any want. | **KEEP** |  |
| 2 | IV:37 | "And this," she said, laying | Two breaths' worth." | **KEEP** |  |
| 3 | V:35 | The lamp round done, the | Melek rose, laid the flat of her hand on the sounding stone, and knocked twice, softly, and then stood in the waiting, two breaths entire, and the waiting was the rite, if it was a rite; Priska had stopped deciding which parts were. | **CUT** | V.6 |
| 4 | VI:29 | The crossed-out forty-one in the | … the head of the deep stair with the flat of his hand, twice, softly, and waited out the two breaths, every time, though nothing had ever answered him and he would have said he did it for the bit. | **CUT** | VI.3 |
| 5 | VI:39 | "Listen. It's not a mystery, | The two breaths are latency." | **KEEP** |  |
| 6 | VI:61 | He sat with the phone | … walking through the middle gallery without giving a name at the mouth, without knocking, without waiting out the two breaths, and the rooms receiving them anyway, the way stone receives rain. | **CUT** | VI.11 |
| 7 | VII:45 | They went down on the | Yusuf gave his name at the mouth before anyone asked, and knocked at the head of the deep stair with the flat of his hand, twice, softly, and waited out the two breaths, as he always did, for the bit, he would once have said. | **CUT** | VII.10 |
| 8 | VII:45 | They went down on the | … the same — two, with the flat of the hand, on the cut stone — and stood the two breaths entire, and past the two breaths she went in first, with the lamp, so that the rooms would meet her … | **VARY** | VII.11: «and stood out the waiting, and then she went in first,» |
| 9 | VII:45 | They went down on the | … flat of the hand, on the cut stone — and stood the two breaths entire, and past the two breaths she went in first, with the lamp, so that the rooms would meet her before they met the light. | **VARY** | VII.11: «and stood out the waiting, and then she went in first,» |
| 10 | VII:59 | Melek did not cross herself | After a while — Yusuf said two breaths; Nilay, later, could not make it shorter than the length of a drummed finger — the elder on the far … | **KEEP** |  |
| 11 | VIII:111 | The women asked Melek for | … hand on the sounding stone beside the answering niche and knocked twice, softly, for her, and stood the two breaths entire, and the waiting was the mourning. | **KEEP** |  |
| 12 | IX:49 | The women were sitting the | … of the deep stair he knocked with the flat of his hand, twice, softly, and waited out the two breaths, having watched the boy do it all summer and having no opinion left about why he copied him. | **CUT** | IX.14 |
| 13 | IX:77 | Then he filled the tin | At the head of the deep stair he knocked with the flat of his hand, twice, softly, and waited out the two breaths entire, and nothing answered, and the nothing had room in it. | **KEEP** |  |
| 14 | XI:27 | Recep was Melek's nephew, her | The etiquette itself he gave away free, and it had survived the internet intact: two knocks with the flat of the hand, and two breaths of waiting. | **VARY** | XI.6: «on the flat stone below the mulberries, out of his aunt's sightline; in April he had the list laminated. The etiquette he gave away free: two knocks with the flat of the hand, and the wait.» |
| 15 | XI:81 | She gave her name at | At the head of the deep stair she knocked with the flat of her hand, twice, softly, and stood the two breaths entire, and nothing answered. | **VARY** | XI.21: «and stood out the waiting, and nothing answered.» |
| 16 | XI:89 | She stood the two breaths. | She stood the two breaths. | **KEEP** |  |
| 17 | XII:85 | His body did the learned | … and he knocked on that, twice, with the flat of his hand, softly — and waited out the two breaths. | **CUT** | XII.12 |
| 18 | XII:103 | He gave his name at | He knocked twice on the frame, with the flat of his hand, and waited out the two breaths, and nothing answered. | **VARY** | XII.14: «He knocked twice on the frame, and waited, and nothing answered. The oil went to the joint of his own thumb and no further — his thumb, the only one the rule had now. The second pinch stood true. The …» |
| 19 | XIV:15 | Before dark she went down. | … stopped watch, wax down — and knocked twice with the flat of her hand, softly, and stood the two breaths entire, and past the breaths said nothing, there being nothing in the manner that wanted words. | **KEEP** | (sentence touched by XIV.6; the phrase stays) |

### "to the knuckle" / "first knuckle"

Now 26. Limit: 8 (both forms counted together). **KEEP: 8.** (Counted in the revised text by the same pattern: 8.)

| # | Ch:line | Paragraph opens | Sentence (round 7) | Decision | Edit and exact replacement |
|---|---|---|---|---|---|
| 1 | I:11 | *The oil goes to the | *The oil goes to the first knuckle of the thumb and no further. | **KEEP** |  |
| 2 | I:43 | Melek Yılmaz was at the | She filled each small lamp to the first knuckle of her thumb, no further, from a tin can that smelled of the press and of some older oil than this year's. | **KEEP** |  |
| 3 | II:7 | *I did not hurry. Hurry | I finished the lamp I was at — oil to the knuckle, wick pinched true — and then I took the light along, and there was a weeping ahead of me, … | **VARY** | II.1: «I finished the lamp I was at — oil measured, wick pinched true —» |
| 4 | IV:117 | Melek finished the round and | Melek finished the round and did not hand Nilay the lamp so much as let her arrive at it — the ninth, filled to the knuckle, the wick pinched true. | **CUT** | IV.16 |
| 5 | V:31 | After the wheat came in | The sitting nights, the women called them: each household took one, and a woman who had buried people kept her mat where her people had sat, and Melek led, and the round came first, oil to the knuckle, wicks pinched. | **CUT** | V.4 |
| 6 | VI:17 | *Was I afraid of him? | For one breath the house felt long — longer than my keeping of it — and then the breath passed, and I filled the lamp, and oil to the knuckle settles more than a wick.* | **VARY** | VI.1: «and I filled the lamp, and measured oil settles more than a wick.*» |
| 7 | VII:73 | Melek rose at last in | Melek rose at last in her own time, and topped the niche-lamp to the knuckle of her thumb, and pinched the wick true, and left it burning, which is the way you leave a house that is not empty. | **CUT** | VII.17 |
| 8 | VII:87 | At dusk Nilay found Melek | At dusk Nilay found Melek at the wicks, doing the round of nine, oil to the knuckle, pinching each flame true. | **CUT** | VII.24 |
| 9 | VII:93 | Below the village, under three | … had left burning was burning, or had burned out, or would be burning; the oil had gone in to the knuckle; the house was keeping its evening. | **CUT** | VII.25 |
| 10 | VIII:21 | *They knocked loudly, with iron | When they had gone up, the basin was full, and the oil was to the knuckle, and the mark was cut.* | **VARY** | VIII.1: «the basin was full, and the oil was at its measure, and the mark was cut.*» |
| 11 | VIII:111 | The women asked Melek for | The round was done, oil to the knuckle, wicks pinched true, and then Melek laid the flat of her hand on the sounding stone beside the answering … | **CUT** | VIII.15 |
| 12 | IX:15 | *Both filled to the knuckle. | *Both filled to the knuckle. | **VARY** | IX.1: «*Both filled to the measure. The room leaned once,» |
| 13 | IX:49 | The women were sitting the | The women were sitting the middle gallery on the night of the twenty-first, eleven of them, lawful, lamps to the knuckle; the sitting ran its ledger two rooms away, and he passed it going down, and nodded, and was nodded … | **VARY** | IX.13: «eleven of them, lawful, and he passed them going down, and nodded, and was nodded to.» |
| 14 | IX:77 | Then he filled the tin | Then he filled the tin lamp himself, from Melek's can, to the first knuckle of his thumb and no further. | **KEEP** |  |
| 15 | X:51 | When the site was released, | … took the round down as far as the law allowed and filled the lamp at the fourth door to the knuckle of her thumb and pinched the wick true, because a house that has had a death in it keeps … | **CUT** | X.7 |
| 16 | XI:11 | *I filled it for her, | *I filled it for her, to the first knuckle of her thumb, because hers was the knuckle the rule had been measured on, and she watched the oil with the attention of a woman counting change she did not doubt. | **VARY** | XI.2: «*I filled it for her, by her own thumb, because hers was the knuckle» |
| 17 | XI:49 | *Fill to the knuckle, pinch | *Fill to the knuckle, pinch to the true;* | **KEEP** |  |
| 18 | XI:65 | "The name of the room." | She filled the ninth lamp to the knuckle. | **CUT** | XI.13 |
| 19 | XI:103 | Nilay kept her first round | The oil went to the first knuckle of her own thumb and no further, and her knuckle was not Melek's knuckle, and the difference was millimeters, and the difference was everything. | **KEEP** |  |
| 20 | XII:103 | He gave his name at | The oil went to the first knuckle of his thumb and no further — his knuckle, the only one the rule had now. | **VARY** | XII.14: «He knocked twice on the frame, and waited, and nothing answered. The oil went to the joint of his own thumb and no further — his thumb, the only one the rule had now. The second pinch stood true. The …» |
| 21 | XIII:132 | She gave her name at | The oil went to the first knuckle of her own thumb and no further. | **CUT** | XIII.25 |
| 22 | XIV:15 | Before dark she went down. | She kept the round first, all nine, oil to the knuckle of her own thumb; the trial was the keeping, and the keeping came first. | **VARY** | XIV.5: «She kept the round first, all nine; the trial was the keeping, and the keeping came first. Then, at the answering niche, she laid the tin box» |
| 23 | XIV:25 | The round came with the | He topped the lamp to the first knuckle of his thumb and no further. | **KEEP** |  |
| 24 | XIV:81 | At the head of the | "Fill to the knuckle. | **KEEP** |  |
| 25 | XIV:127 | That winter she rendered the | … start of her first notebook all along: a keeper, teaching a child to tend a lamp — oil to the knuckle, wick pinched true, the dark taken a spoonful at a time. | **VARY** | XIV.25: «a keeper, teaching a child to tend a lamp — the oil measured, the wick pinched true,» |
| 26 | XIV:141 | *The oil goes to the | *The oil goes to the first knuckle of the thumb and no further. | **KEEP** |  |

### "past the name, nothing" and its variants

Now 12. Limit: 6. **KEEP: 6.** (Counted in the revised text by the same pattern: 6.)

| # | Ch:line | Paragraph opens | Sentence (round 7) | Decision | Edit and exact replacement |
|---|---|---|---|---|---|
| 1 | I:19 | *If company comes, you say | *If company comes, you say the name of the room, and then nothing. | **KEEP** |  |
| 2 | II:11 | *I set the lamp down | *I set the lamp down where she could see it if she chose to see it, and I said the name of the room, once, and after the name, nothing. | **KEEP** |  |
| 3 | V:13 | *Then water. She sets a | Past the name, nothing. | **KEEP** |  |
| 4 | V:23 | *To the one who keeps | *To the one who keeps the lamps after me: fill the lamp before her season; answer the once, and past the name, nothing; do not follow her into the morning. | **VARY** | V.1: «answer the once, and no more; do not follow» |
| 5 | VII:11 | *They keep to the edge | They give the name of their room — and it is a name you will not know, being from a part of the house you have not walked — and past the name, nothing. | **VARY** | VII.1: «being from a part of the house you have not walked — and say no more. Our rule,» |
| 6 | VII:25 | *To the one who keeps | Say the name of the room, and past the name, nothing. | **VARY** | VII.2: «Say the name of the room, once. They keep» |
| 7 | XI:65 | "The name of the room." | Past the name, nothing." | **KEEP** |  |
| 8 | XI:89 | She stood the two breaths. | Then she answered, once, because that is the etiquette, and past the answer, nothing: "The singing room." | **CUT** | XI.23 |
| 9 | XIV:15 | Before dark she went down. | … — and knocked twice with the flat of her hand, softly, and stood the two breaths entire, and past the breaths said nothing, there being nothing in the manner that wanted words. | **CUT** | XIV.6 |
| 10 | XIV:31 | She said, "Emre," once — | … measured doors, or had heard its grandmother, or its grandchild — because the manners are the manners, and past the name, nothing, and then he broke the office for the first time in twenty-seven of her years: | **KEEP** |  |
| 11 | XIV:57 | "We know her," he said. | Past the name, nothing." | **CUT** | XIV.14 |
| 12 | XIV:149 | *If company comes, you say | *If company comes, you say the name of the room, and then nothing. | **KEEP** |  |

### "flat on the palm"

Now 3. Limit: 2. **KEEP: 2.** (Counted in the revised text by the same pattern: 2.)

| # | Ch:line | Paragraph opens | Sentence (round 7) | Decision | Edit and exact replacement |
|---|---|---|---|---|---|
| 1 | VI:49 | And before the file had | She offered him his exits the way she offered everything, flat on the palm: wet plaster doubles; a low lamp stands a man's shadow up; a boy who has been alone in bad air sees company. | **KEEP** | (sentence touched by VI.7; the phrase stays) |
| 2 | X:71 | "Neither does it hang one," | "Neither does it hang one," Nilay said, and laid the two drafts side by side, flat on the palm. | **CUT** | X.10 |
| 3 | XIV:75 | Some of it re-keyed itself | She laid those flat on the palm and left them where they lay. | **KEEP** |  |

### "manners"

Now 20. Limit: 12. **KEEP: 12.** (Counted in the revised text by the same pattern: 12.)

| # | Ch:line | Paragraph opens | Sentence (round 7) | Decision | Edit and exact replacement |
|---|---|---|---|---|---|
| 1 | I:37 | The permit had come in | She noticed the *in advance*, and liked the letter's manners, and forgot it. | **VARY** | I.2: «and liked the letter's courtesy, and forgot it.» |
| 2 | I:59 | In the second week of | Some remembered good manners. | **CUT** | I.5 |
| 3 | II:19 | *Near morning she came closer | Comfort that lays hold of you is only weather with manners.* | **KEEP** |  |
| 4 | V:69 | And they worked. On twenty-two | The village's manners cooled by exactly one degree, which was the temperature of a courtesy observed: a child on a wall clicked its tongue at her, pump-fashion, and ran; Havva, recovered, patted her hand at the bread queue and said, "You fixed the air, dear. | **VARY** | V.13: «The village cooled by exactly one degree, the temperature of a courtesy observed:» |
| 5 | V:71 | For the report she took | The village, she understood, would have written it as the manners. | **KEEP** |  |
| 6 | VI:29 | The crossed-out forty-one in the | … going down, having watched the women do it and been told by Seher, the schoolteacher, that it was manners; he knocked at the head of the deep stair with the flat of his hand, twice, softly, and waited out the … | **KEEP** |  |
| 7 | VII:19 | *The elder of them, the | … the weave of it repeated nowhere — I looked, being young, and my eyes were better than my manners — and I have not seen the like since, not on the living. | **KEEP** |  |
| 8 | VII:59 | Melek did not cross herself | … hand out, European, grave, at the level of a handshake; the hand went out and hung with its manners on, and nothing took it, and nothing refused it, and he repossessed it slowly, like a man who has offered his … | **VARY** | VII.14: «the hand went out and hung there, courteous, and nothing took it,» |
| 9 | VII:85 | Kaya Bey came up the | He said it comfortably, and it fit — the wraps, the water, the tidy ash, the manners, even the teeth, which he did not count — it fit everything but the parts that fit nothing, which is why it would never die. | **VARY** | VII.22: «the tidy ash, the courtesy, even the teeth,» |
| 10 | VIII:87 | They keep the edges | > They keep the edges of the light, which is manners. | **KEEP** |  |
| 11 | VIII:87 | They keep the edges | They had the names already, which is also manners. | **KEEP** |  |
| 12 | VIII:111 | The women asked Melek for | Nilay gave her own name at the mouth before the lamps, first, unasked; the manners had arrived in her by roads she had stopped auditing. | **VARY** | VIII.14: «the custom had arrived in her by roads she had stopped auditing.» |
| 13 | XI:69 | "The village gave me a | "If it was him, he kept his manners. | **KEEP** |  |
| 14 | XI:79 | On the ninth day she | The order still stood — no one below the second door, pending everything — but orders accrete manners the way hills accrete paths. | **VARY** | XI.19: «but orders accrete customs the way hills accrete paths.» |
| 15 | XI:93 | At the dig house she | A second time would have been asking, and she had been thirteen months in that country and knew the manners by heart. | **VARY** | XI.25: «and knew the etiquette by heart.» |
| 16 | XII:7 | *I have never seen them. | Manners travel farther than people do. | **KEEP** |  |
| 17 | XII:7 | *I have never seen them. | That is what manners are for.* | **KEEP** |  |
| 18 | XII:85 | His body did the learned | And because the manners were in his body now and made no objection to absurdity, he knocked — there was nothing to knock on but … | **KEEP** |  |
| 19 | XIV:31 | She said, "Emre," once — | … room, from a woman who measured doors, or had heard its grandmother, or its grandchild — because the manners are the manners, and past the name, nothing, and then he broke the office for the first time in twenty-seven of … | **KEEP** | (sentence touched by XIV.8; the phrase stays) |
| 20 | XIV:31 | She said, "Emre," once — | … woman who measured doors, or had heard its grandmother, or its grandchild — because the manners are the manners, and past the name, nothing, and then he broke the office for the first time in twenty-seven of her years: | **KEEP** | (sentence touched by XIV.8; the phrase stays) |

### "the moon's laundry"

Now 2. Limit: 1 (the first). **KEEP: 1.** (Counted in the revised text by the same pattern: 1.)

| # | Ch:line | Paragraph opens | Sentence (round 7) | Decision | Edit and exact replacement |
|---|---|---|---|---|---|
| 1 | III:47 | The residual sat under the | The residual sat under the deep rooms and past them, farther down than the plans went, below the fourth door and beyond the last mapped floor: a gravity deficit of thirty-four microgal, give or take the moon's laundry. | **KEEP** |  |
| 2 | VII:29 | The coring had been on | … floors all summer like a guest who will neither leave nor explain itself — twenty-nine microgal, minus the moon's laundry — and the Ministry's annex, countersigned twice in the slope, permitted the sounding of it in the first dry week … | **CUT** | VII.3 |

### the "the way X does Y" simile ("the way the / a / it / she / he …")

Now 60. Limit: 40 (two thirds of 60). **KEEP: 37.** (Counted in the revised text by the same pattern: 37.)

| # | Ch:line | Paragraph opens | Sentence (round 7) | Decision | Edit and exact replacement |
|---|---|---|---|---|---|
| 1 | I:27 | *The oil is measured. The | Before, it is dark the way it always was, and after, it is dark the same way, and between the two there will have been light for as long as my knuckles hold out, and after that for as long as yours.* | **KEEP** |  |
| 2 | I:71 | At the mouth of Kırk | … same figure: eighteen minutes, and eighteen again, obedient to nothing anyone had ever identified, keeping its own time the way the sea keeps the moon's. | **KEEP** |  |
| 3 | I:75 | The warmth came against her | The warmth came against her right shoulder the way a cat commits itself: suddenly, entirely, with weight. | **KEEP** |  |
| 4 | II:5 | *The water came at the | *The water came at the land in the night, and the land took it loudly, the way it always has. | **KEEP** |  |
| 5 | II:19 | *Near morning she came closer | In the end she slept against my side, entirely, all at once, the way the tired pay down a debt they have carried too long. | **KEEP** |  |
| 6 | II:39 | And under the stamp, the | And under the stamp, the whole of it, the way it had been the whole of it for twenty-six years: *Male, thirteen. | **VARY** | II.3: «And under the stamp, all of it, as it had been all of it for twenty-six years:» |
| 7 | II:53 | The storm came on the | She went at dusk, before the rain, taking the tin lamp from the niche at the mouth without asking, and she filled it herself, past any knuckle, greedily, the way the frightened do. | **KEEP** |  |
| 8 | II:59 | She cried in the dark | She cried in the dark with her whole body, the way she had not permitted herself in front of anyone since the fourth, and when the crying was spent the warmth … | **KEEP** |  |
| 9 | II:59 | She cried in the dark | … permitted herself in front of anyone since the fourth, and when the crying was spent the warmth arrived, the way it had arrived all her life at the mouths of rooms: suddenly, entirely, with weight, at her right side. | **VARY** | II.4: «the warmth arrived, as it had arrived all her life» |
| 10 | II:77 | The first night rain of | … the crossed-out count, one problem laid on another, and turned off the light, and the tune came back the way it always came back, at its own pace, pausing where the words would be. | **CUT** | II.5 |
| 11 | III:11 | *He came to the end | *He came to the end and had a number, and was pleased with it, and I was pleased that he was pleased, and then — because they always do it — he went back along the way he had come, counting again.* | **KEEP** |  |
| 12 | III:21 | *He wanted to know why | If he had stayed thirty years, and kept the lamps, and eaten at my fire, one morning the why would have arrived whole, without words, the way the round arrives; and he would have stopped asking, without ever having been answered. | **KEEP** |  |
| 13 | III:67 | The singing room he found | He hummed, the way a man hums who is alone and testing, and found the note where the walls stood up behind his voice … | **VARY** | III.15: «He hummed, as a man hums who is alone and testing,» |
| 14 | IV:11 | *One room sings, and I | There is a note — the chest finds it before the throat does, the way a door knows your weight before you knock — and when you give the note to the room, the room does not keep it. | **KEEP** |  |
| 15 | IV:55 | She asked about the letters, | He said it the way a man states a filing practice, and reached for a cloth, and wiped the desk where the teapot had stood, because the water had marked it, thirty years ago, and he was still keeping that from happening again. | **KEEP** |  |
| 16 | V:31 | After the wheat came in | Priska asked leave to bring her meter down and set it in the corner of the middle gallery, and Melek considered the pump the way she had considered Márton's gravimeter. | **VARY** | V.5: «and Melek considered the pump as she had considered Márton's gravimeter.» |
| 17 | V:31 | After the wheat came in | It was not quiet; it clicked, six strokes to the minute; the women folded it into the night the way a household folds a clock. | **KEEP** |  |
| 18 | VI:15 | *He slept by the lamps | The sun in his hand went dark when he slept, as suns do not, and from that I learned it was his, the way the lamp is mine: a thing that keeps his hours and not the world's. | **KEEP** |  |
| 19 | VI:49 | And before the file had | She offered him his exits the way she offered everything, flat on the palm: wet plaster doubles; a low lamp stands a man's shadow up; a boy who has been alone in bad air sees company. | **KEEP** |  |
| 20 | VI:63 | At the mouth of Kırk | … same figure: nineteen minutes, and nineteen again, obedient to nothing anyone had ever identified, keeping its own time the way the sea keeps the moon's. | **KEEP** |  |
| 21 | VII:9 | *You will know them before | When they are on the road, the flame leans toward the deep rooms, the way a plant leans at a window, and there is no draft to blame, and you do not go looking for one. | **KEEP** |  |
| 22 | VII:13 | *The oldest keepers call them | *The oldest keepers call them the far lamplighters, and the name is exact, though not the way the young first take it. | **KEEP** |  |
| 23 | VII:43 | That was the Thursday. It | … saved whole on sacking to be returned to its socket, and Melek put her conditions under the ministry's the way she put everything under everything: her first, down; names given at the mouth; and no counting below. | **VARY** | VII.7: «and Melek put her conditions under the ministry's, as she put everything under everything:» |
| 24 | VII:75 | Nilay climbed out last. At | She bagged it with the ash, procedure reasserting itself the way a soldier polishes boots, and gave the ordinary accounts their turn on the climb: a heritage mill's paper bag in somebody's pocket; a cuff; a joke with a mortar. | **CUT** | VII.18 |
| 25 | VII:79 | The cards asked to be | Recovery ground all night and handed up one frame in the morning: the print of a woven sandal, human, right foot, mid-stride, in the flour-fine dust, going the way the deep road went. | **KEEP** |  |
| 26 | VIII:19 | *A man came alone on | … trimmed day with a glass finger in his coat, and stood a long while before the first marks, the way the poor stand before bread, and then he took a finger's cup of the wall's blood into the glass, and … | **KEEP** |  |
| 27 | VIII:109 | Leyla Hanım died in her | Nilay had known her the way she knew all of them, as a face at the bread queue with a whole hydrology under it, and had never once asked. | **VARY** | VIII.13: «Nilay had known her as she knew all of them,» |
| 28 | VIII:113 | Nothing came. The air moved | The air moved along the duct, the fan turned on its mended bearing, the masks did their work, and the dark was present the way a full room is present. | **KEEP** |  |
| 29 | IX:9 | *I did not know that | She read the leaning to me, which has no words, and handed me the oil, and called it her decision, the way the surface calls things, where things can still be changed.* | **KEEP** |  |
| 30 | IX:39 | She spent her coldest hour | He watched it take the note out of her the way it took it out of everyone — sternum first, her chest finding the low A before any decision had been … | **VARY** | IX.9: «He watched it take the note out of her as it took it out of everyone» |
| 31 | IX:57 | Twice is a result. He | … never once obliged him, and at 06:12, entering the column, he wept at the laptop — without drama, the way it comes to old men, at a desk, over arithmetic — and let it have its ten minutes, and logged … | **KEEP** |  |
| 32 | IX:59 | Priska, before she drove to | At the door she said, "Wear the mask below the second door," and he said, "The body is the oven, Priska; I am keeping the oven honest," and she looked at him the way she looked at a gradient she could not instrument, and left. | **KEEP** |  |
| 33 | IX:71 | The Registrar came up the | He looked once at the whiteboard, the way he looked at everything, as if it had already been filed, and did not look at it again. | **CUT** | IX.22 |
| 34 | IX:75 | Halden asked nothing about watches, | The Registrar went down the hill the way he had come, and the grey closed over him at the mulberries. | **KEEP** |  |
| 35 | IX:79 | Down past the second door | … where the lamps go, and laid his hand flat on his knee, and let the stillness have him the way the women let it, Priska's meter left on its nail by the dig-house door; tonight the witness was to be … | **KEEP** |  |
| 36 | X:55 | She laid her case out | She laid her case out in three sentences, the way she built a column. | **KEEP** |  |
| 37 | X:83 | Priska moved her office to | The stone was warm by ten and her tables behaved in daylight, and part of her — she noted it the way she noted everything — was simply glad to be out from under the hill, and she let the note stand without a column. | **VARY** | X.13: «she noted it as she noted everything» |
| 38 | XI:13 | *Then she asked for the | I walked her the length of it, slow, and she read the lines with her finger held a finger's width off the stone, touching nothing, the way the taught read, and at the far end, among the oldest cuts, she stood a long time. | **KEEP** |  |
| 39 | XI:41 | At the end of May, | At the end of May, Melek went down the way a keel goes down — no ceremony, all at once, in her kitchen, between the stove and the door. | **KEEP** |  |
| 40 | XI:71 | She died in the third | She had put the oil can into Nilay's hands two days before, with both hands, the way she poured tea. | **KEEP** |  |
| 41 | XI:83 | The singing room took the | The singing room took the song the way it took everything, sternum first. | **VARY** | XI.22: «The singing room took the song as it took everything, sternum first.» |
| 42 | XI:105 | She came up at full | … same figure: twenty minutes, and twenty again, obedient to nothing anyone had ever identified, keeping its own time the way the sea keeps the moon's. | **KEEP** |  |
| 43 | XII:33 | The Registrar's letter had arrived | He laid the two dates side by side, the way he laid everything now. | **CUT** | XII.3 |
| 44 | XIII:11 | *You will want to ask | The wall begins in ignorance, the way the day does, and it is right that it end there also, and I have not been paid the ignorance, and the not-being-paid is what the hesitation is.* | **KEEP** |  |
| 45 | XIII:27 | The dig closed the way | The dig closed the way the season closed in that country: by letter, in the last week of August. | **VARY** | XIII.1: «The dig closed as the season closed in that country:» |
| 46 | XIII:45 | Then he brought her the | Then he brought her the volume, from the inner shelf, the way a sexton brings a key. | **KEEP** |  |
| 47 | XIII:104 | He supplied it himself, as | He supplied it himself, as a courtesy, the way a clerk supplies a folio number. | **KEEP** |  |
| 48 | XIV:3 | The fourth of September came | … came up the hill clear and dry, two days ahead of the frost, and the village kept it the way it had kept it for twenty-seven years, which was by not keeping it: bread as usual, the argument at the … | **VARY** | XIV.1: «and the village kept it as it had kept it for twenty-seven years, by not keeping it:» |
| 49 | XIV:15 | Before dark she went down. | … the women called generous and a forecast sheet would have called pooled — and the dark was present the way a full room is present. | **VARY** | XIV.7: «and the dark was present as a full room is present.» |
| 50 | XIV:35 | He set out water for | He went in far enough to be brave, and then one door more; the land cleared its throat, the way it did all that year, and a stone he had not marked came home in its socket, and the brave was finished. | **VARY** | XIV.9: «the land cleared its throat, as it did all that year,» |
| 51 | XIV:43 | "There was a girl behind | Crying with her whole body, the way the tired pay down a debt they have carried too long. | **KEEP** |  |
| 52 | XIV:43 | "There was a girl behind | I sat where the wall lets a body sit and hummed the way the keepers hummed for me — the tune everyone's mother used, the one nobody owns, with nothing in it to follow but the going on." | **VARY** | XIV.12: «and hummed like the keepers hummed for me» |
| 53 | XIV:65 | He looked at the flame | He looked at the flame while he answered, the way the office answers. | **CUT** | XIV.16 |
| 54 | XIV:67 | "You've had it backwards. It | A place that's kept long enough stops being in only one of its times — it's in all of them, the way a road is in all its miles. | **CUT** | XIV.17 (the clause goes with the halved speech) |
| 55 | XIV:107 | The ribbon had lain all | … still in the pocket, and watched her daughter go out with the oil can to the evening round, the way she had once watched a boy go out in house slippers, and did not call anything after her. | **KEEP** |  |
| 56 | XIV:117 | On the fourteenth of September, | … behind the bound-in annual lines, scored it once with the little knife from Melek's oilcloth, one line, low, the way the wall is cut, and under the line wrote: | **CUT** | XIV.22 |
| 57 | XIV:123 | At the mouth of Kırk | … same figure: eighteen minutes, and eighteen again, obedient to nothing anyone had ever identified, keeping its own time the way the sea keeps the moon's. | **KEEP** |  |
| 58 | XIV:125 | In October the Ministry's report | Then she took her water bottle and wet one exposed stone, the way she had wetted a thousand carved surfaces for the light a camera needs — and stopped, halfway through, her hand … | **VARY** | XIV.23: «as she had wetted a thousand carved surfaces» |
| 59 | XIV:127 | That winter she rendered the | That winter she rendered the wall's two new lines, and then the old ones, notebook after notebook, the way she had rendered them for six years without reading them — half transcription, half what the hand did while the … | **VARY** | XIV.24: «notebook after notebook, as she had rendered them for six years» |
| 60 | XIV:157 | *The oil is measured. The | Before, it is dark the way it always was, and after, it is dark the same way, and between the two there will have been light for as long as my knuckles hold out, and after that for as long as yours.* | **KEEP** |  |

### "which was"

Now 44. Limit: 29 or fewer (a third cut). **KEEP: 19.** (Counted in the revised text by the same pattern: 19.)

| # | Ch:line | Paragraph opens | Sentence (round 7) | Decision | Edit and exact replacement |
|---|---|---|---|---|---|
| 1 | II:77 | The first night rain of | She lay in the dark of the dig house, not sleeping, listening to the hill drink, which was a sound, only a sound, the weather moving in the stone. | **KEEP** |  |
| 2 | III:7 | *He was polite, which the | … body sit, and he ate little and drank much, and talked all through the meal about the rope, which was knotted, he said, at the length of his own forearm, one knot to a forearm, and the forearm, he said, … | **KEEP** |  |
| 3 | III:15 | *He stood at the mouth | … heads of children he is afraid of loving too much, and he came back with a third number, which was the second number, and not the first.* | **KEEP** |  |
| 4 | III:31 | Dr. Márton Kállai wore three | At conferences, when the watches drew the question, he said, "They keep one another honest," which was a joke, and also the nearest thing to the truth he permitted himself in public. | **KEEP** |  |
| 5 | III:59 | Priska arrived for the refraction | … candles lay down at knee height on schedule, on demand, at printed times — her anomalies kept appointments, which was the whole difference between her science and his. | **CUT** | III.11 |
| 6 | III:81 | Everybody laughed, and nobody entirely, | Everybody laughed, and nobody entirely, and the sheets went into the archive box between her air maps and his triangle, which was where the summer kept everything it could not spend. | **KEEP** |  |
| 7 | V:69 | And they worked. On twenty-two | The village's manners cooled by exactly one degree, which was the temperature of a courtesy observed: a child on a wall clicked its tongue at her, pump-fashion, and ran; Havva, recovered, patted her hand at the bread queue and said, "You fixed the air, dear. | **VARY** | V.13: «The village cooled by exactly one degree, the temperature of a courtesy observed:» |
| 8 | VI:57 | The post traveled. By Friday | By Friday noon it had forty thousand views, which was more than everything he had made in four years, together. | **CUT** | VI.10 |
| 9 | VI:57 | The post traveled. By Friday | … the people who said leaf; the people who said proof; the people who said *a person walked past*, which was true, and settled nothing, being the caption he had almost written. | **CUT** | VI.10 |
| 10 | VII:17 | *When I was new I | She was a long time answering, which was her way of saying the answer was worth carrying slow. | **KEEP** |  |
| 11 | VII:37 | She sounded it with the | The lamp went down burning evenly, which was a fact about the air, and came up warm, which was another, and riding on it, in a September that had not rained, was the smell of rain on dust. | **KEEP** |  |
| 12 | VII:37 | She sounded it with the | The lamp went down burning evenly, which was a fact about the air, and came up warm, which was another, and riding on it, in a September that had not rained, was the smell of rain on dust. | **KEEP** |  |
| 13 | VII:39 | "Rock at three meters does | He disliked all three equally, which was how she knew he had already checked them. | **VARY** | VII.5: «He gave the table three explanations himself and disliked all three equally; that was how she knew he had already checked them.» |
| 14 | VII:43 | That was the Thursday. It | The loss of the instrument went into the incident book, and incident books want recovering, and the annex — read generously, which was the only way Kaya Bey's ministry ever read anything — permitted investigation of the void by entry. | **CUT** | VII.6 |
| 15 | VII:59 | Melek did not cross herself | She set her lamp in the empty niche at the basin's head, which was where a lamp went, and then she laid the flat of her hand against the polished wall and held it … | **CUT** | VII.13 |
| 16 | VII:71 | The rest of the hour | … his hand above it and said "cold," and took up in a sample bag what a spatula holds, which was most of what there was, the ceiling above it wearing no smoke at all. | **CUT** | VII.15 |
| 17 | VIII:107 | It was that night, past | She photographed the notebook page, printed it, and stapled it into the annex beside the statement, contradicting herself in the record, which was the only honest thing the record could hold, and went to bed with the light on longer than she would have admitted. | **KEEP** |  |
| 18 | VIII:125 | It did not answer the | The room was satisfied all the same, without anyone being able to say by what, and Seher's minute recorded the exchange as *resolved,* which was accurate in every respect but the ones that count. | **CUT** | VIII.18 |
| 19 | IX:51 | The three watches rode down | … day had left in them, and Priska's spare meter clicked at his hip, six strokes to the minute, which was company, a fact he declined to log. | **KEEP** |  |
| 20 | IX:59 | Priska, before she drove to | … could not exclude — and left the page square on his table where he could not miss it, which was the tenderest thing anyone did for him all winter. | **KEEP** |  |
| 21 | X:27 | Priska Vogel had stood at | Guilt had given her a profession, and a mercy to hand out with it, and the two had always arrived together, which was the whole of her luck and most of her character. | **CUT** | X.1 |
| 22 | X:27 | Priska Vogel had stood at | She had never once stood at a cave mouth in the position she held on the last morning of December, which was the position of a chemist whose instrument had just been asked to acquit a hill. | **CUT** | X.1 |
| 23 | X:43 | Marques came in January, as | The closure kept her above the second door and she did not argue with it, which was the first thing the hill had ever made her accept. | **CUT** | X.4 |
| 24 | X:57 | He heard her out with | He heard her out with the whole of his attention, which was the most disquieting thing about him, and then he asked, presently, whether the thirteenth bore of her canton was still closed for lining. | **VARY** | X.8: «He heard her out with all his attention — the most disquieting thing about him — and then he asked,» |
| 25 | X:59 | He did not answer her | And she had nothing, and he knew she had nothing, and there was no cruelty anywhere in the knowing, which was the worst of it. | **KEEP** |  |
| 26 | X:73 | They sat with that, and | "Goodnight, Doctor," Nilay said at the door, and the title went in cold where the name had been, and Priska sat a long time with the two drafts and could not merge them, which was, she supposed, the finding. | **VARY** | X.11: «and could not merge them. That, she supposed, was the finding.» |
| 27 | X:83 | Priska moved her office to | The meter clicked at her hip, six strokes to the minute, above a shut hill, in the best air in the province — on her own evidence, which was indicative. | **KEEP** |  |
| 28 | XI:7 | *She had kept this house | Now she was old past the arguing with, and she had come down the stair one last time to do what she had been meaning to do for a lifetime, which was to set the lamp down.* | **KEEP** |  |
| 29 | XI:31 | Nilay listed the explanations: the | And the village's own account, which Havva Nine delivered at the bread queue, without patting anyone's hand, which was the message entire: "Tell your Doctor the grandparents are restless. | **VARY** | XI.8: «The village had its own account, and Havva Nine delivered it at the bread queue, without patting anyone's hand:» |
| 30 | XI:41 | At the end of May, | When Nilay went north two days later she saw the transfer authorization, and saw its date, which was the day before the kitchen floor, and Sungur's sentence came up with it, and neither the paper nor the sentence would say which had been first. | **CUT** | XI.12 |
| 31 | XI:71 | She died in the third | "It chose me sixty years ago and I argued for a month, which was a month wasted. | **KEEP** |  |
| 32 | XI:73 | They buried her by the | The women sang her song, badly, twice, and Nilay's mother's mouth moved with it, which was memory or which was the village, and there had never been a test that could tell those apart. | **VARY** | XI.14: «and Nilay's mother's mouth moved with it, from memory or from the village,» |
| 33 | XI:73 | They buried her by the | The women sang her song, badly, twice, and Nilay's mother's mouth moved with it, which was memory or which was the village, and there had never been a test that could tell those apart. | **VARY** | XI.14: «and Nilay's mother's mouth moved with it, from memory or from the village,» |
| 34 | XI:73 | They buried her by the | Yusuf came up from Derinkuyu and stood at the back and left before the bread, which was its own attendance. | **VARY** | XI.17: «and left before the bread, its own kind of attendance.» |
| 35 | XI:77 | No document had handed Nilay | The office had come to her by refusal, which was how offices moved there: what is given can be resented, and what is refused must be taken up, and the taking up is the whole of the training. | **VARY** | XI.18: «The office had come to her by refusal, as offices moved there: what is given can be resented, and what is refused must be taken up, and the taking up is the training.» |
| 36 | XI:79 | On the ninth day she | He passed her with the gravity of a boy holding his whole duty in one sentence, and she went down unlawful and appointed, in the same body, which was, she supposed, the definition of a keeper that the county had arrived at. | **VARY** | XI.20: «in the same body: the county's definition of a keeper, she supposed.» |
| 37 | XII:81 | Layered. The color the hill | The color the hill was at that hour, which was the color everything was at that hour; he took that explanation at once, gratefully, and held it. | **KEEP** |  |
| 38 | XII:91 | Kemal's mother gave him the | In the grey he walked up to take the Derinkuyu road past the mouth, which was the direct road, and only that. | **KEEP** |  |
| 39 | XIII:35 | Valletta at dusk was stone | The pharmacy's green cross had lit itself, the stair smelled of eucalyptus, and at the top the door stood ajar at the hour of her arrival, which was the previous courtesy with the bookkeeping left showing. | **CUT** | XIII.6 |
| 40 | XIII:35 | Valletta at dusk was stone | … red with age, and she noticed them the way one notices the cloth folded at the desk's corner, which was still keeping a thirty-year-old ring from happening again. | **VARY** | XIII.8: «and she noticed them as she noticed the cloth folded at the desk's corner, still keeping a thirty-year-old ring from happening again.» |
| 41 | XIII:98 | "The calibration memorandum," she said. | None of them had ever once required a villain, which was the property of the thing she minded most about it. | **VARY** | XIII.20: «None of the explanations for that one had ever once required a villain, and that was what she minded most about it.» |
| 42 | XIV:3 | The fourth of September came | … ahead of the frost, and the village kept it the way it had kept it for twenty-seven years, which was by not keeping it: bread as usual, the argument at the co-op as usual, and at every gate half a … | **VARY** | XIV.1: «and the village kept it as it had kept it for twenty-seven years, by not keeping it:» |
| 43 | XIV:83 | She came out at the | She came out at the mouth at first light on the fifth of September, twenty-seven years and a day, and Priska was at the watcher's stone with the thermos, at the hour she had chosen, which was her way of attending. | **KEEP** |  |
| 44 | XIV:97 | Later that day, at the | … instead — whose label said *viewed: no* and would go on saying it, one problem laid on another, which was how that drawer kept things. | **KEEP** |  |

### The "three ordinary explanations" routine

I count as the routine every place where, after a strange event or record, a character lays out a list of ordinary explanations (or "builds the forks") and files the thing unresolved. There are 27 such places. The ruling keeps the first (IV, the Saflieni shoe) and at most three others, "chosen for weight". The ruling calls IV the first time; three instances in I and II come earlier, and I have treated them as the routine too (see section 5).

**Kept whole (4):**

| Ch:line | Where | Why this one |
|---|---|---|
| IV:75 | "Three ways to hold it": the Saflieni shoe (duplicate accession number; a stray of the old excavations; a cautious surveyor) | The ruling's first instance. |
| II:69 | The humming in 1999: Halime or any of the mothers; a mind building a mother; "There was a third way to hold that night." | The book's first hint of the dead, which the concept needs, and the source of IV's "ways to hold it". |
| V:57 | Priska builds the forks at her father's cough (the stone ticking; a drip; the lamp; her own chest) | The fumes against the dead at their sharpest; "the half-second in which she had not wanted it to survive". All five readers chose this scene. |
| IX:59 | Priska's forks column for Márton (thermal, firmware, reference, "the fourth fork being himself") | A plant: the page is found "square on the table … the fourth fork unresolved" at X:73. |

**Cut, or reduced to one clause (23):**

| Ch:line | The list (round 7) | Decision | Edit |
|---|---|---|---|
| I:61 | the count of forty-one: a red-eye; a bin or blind alcove; shelves of smoke | One clause: «The shelves of smoke, she decided, had made the openings lie.» | I.6 |
| II:33 | the two plans: the '24 surveyor tired; the '98 office in Ankara; the ceiling shut and cleared | The three sentences go; the existing clause «There was nothing in any of it that a tired surveyor and an Ankara office could not account for between them.» stays as the one clause. | II.2 |
| III:49 | the hollow: water table; drift; density tables | One clause: «and he put it to every test the hill allowed» | III.7 |
| VI:31 | Yusuf's forty-ones: a bin in cold smoke; his stride; shelves of dead air | One clause: «he made the excuses for those mornings himself before anyone could make them for him.» | VI.4 |
| VI:47 | the sandal frame: a villager; a herder; a hoax; a leaf; the bracket's shadow | One clause: «and every one of them stood up nicely.» | VI.6 |
| VI:49 | the reflection: wet plaster; a low lamp; a boy alone in bad air | One clause: «flat on the palm, and he took none of them out loud.» | VI.7 |
| VI:55 | the letter: the Trust's young woman; a clerk; a guess | One account: «The Trust's young woman with the clipboard, seen in April, scarf or no scarf, could still be in the country with a courier's bag.» | VI.9 |
| VII:39 | the smell of rain: summer heat; the aquifer; wet rock | One clause: «He gave the table three explanations himself and disliked all three equally» | VII.5 |
| VII:75 | the flour: a mill's paper bag; a cuff; a joke with a mortar | Cut. Kaya Bey's «flour, he said, travels in pockets» (VIII:119) keeps the ordinary account on the page. | VII.18 |
| VIII:105 | the tritium zero: fossil water; pre-war cisterns; (Márton) the half-life | One clause for the ordinary account, «Priska called it fossil water, the commonest water on earth.»; Kaya Bey's cisterns go; Márton's note (the time plant) stays. | VIII.10 |
| VIII:107 | her own statement: typed from memory; amended at the keyboard; the truer memory | One clause: «She had typed from memory, she supposed, and slipped.» | VIII.11 |
| VIII:109 | Leyla's silence: a quarrel; the walk; being last | The list goes; «The village had three explanations for that, and she had furnished none of them.» stays. | VIII.12 |
| IX:29 | Márton's counter-readings: stratification; settlement; tuff dust | The list goes; «he had dismissed, in writing, his own counter-readings with the courtesy of a man dismissing relatives.» | IX.4 |
| XI:31 | the knock answered: the shaft's tide; the tuff; boys; the hermits | Cut. The village's account (Havva: "the grandparents are restless") stays. | XI.8 |
| XI:33 | Priska's recording: the shaft's tide; the tuff; the fan bearing | One clause: «She gave the explanations two honest days, and none of them confessed.» Her shaft timing (twenty against eighteen) stays. | XI.9 |
| XI:35 | Kaya Bey's traffic correlation | Cut, whole paragraph (ordered). | XI.10 |
| XI:37 | why the answers thinned: the company leaving; the courtesy cheapening; the season | Cut. | XI.11 |
| XI:91 | the returned phrase: the room returns notes; the ear fed; the batteries; a young woman | One clause: «She built the explanations on the climb, methodically, and none of them would carry the weight, and none of them would break.» | XI.24 |
| XII:37 | the April letter: a directorate; a registry with friends; the young woman | One clause: «He spent an evening on the ordinary accounts, and under them found the other reading, the one that warmed:» | XII.4 |
| XII:97 | the old print: old dust; co-op sandals; undatable | One clause: «Old dust under an overhang holds marks for weeks, he told himself.» | XII.13 |
| XIII:81 | the chapel: kept faithfully and gone quiet, or kept to the money's edge | Cut, whole paragraph. | XIII.17 |
| XIII:94 | the inked-out item: an accomplice; the founder's retrieval; a deposit never made; a hoax | Cut. | XIII.18 |
| XIII:98 | the calibration memo: a filing failure; a service covering itself; a registry | One clause: «None of the explanations for that one had ever once required a villain, and that was what she minded most about it.» | XIII.20 |

**Not the routine, and unchanged: the book's own explanations, which the concept needs on the page.** The fumes: V:27 (Priska's position), V:53, V:67 ("The fumes were canon now"), X:39, X:47, XIV:77. The parallel build: VI:33 ("Suppose instead two good maps"), VI:39 (server lag), VI:45 ("different build?"), VII:81 ("The other instance. It loaded us."). The wormhole: III:89 ("a hole through everything"), IX:43 (halved, not removed: negative energy, the Casimir effect, "Show me the machine"), IX:47 (the fuel bill), IX:61 (the whiteboard). The dead: II:69, V:53, V:55–59, XI:31 (Havva), XI:61–69 (Melek), X:47 ("Not to the grandparents"). The three together: X:47 ("the death belonged to nobody"), VIII:127 (the Registrar's annex: "the air's, the geometry's, or the mischief of men"), XIV:77 ("Some of it re-keyed itself"). Also unchanged: the single ordinary accounts that are not lists (VII:85 Kaya Bey's hermits; I:75 the cat and the warm stone; IV:41 Mrs. Vella's workmen).

### The two too-pleased lines

| Ch:line | Round 7 | Decision | Edit |
|---|---|---|---|
| V:81 | "… and now it installs with a fan. Oxygen debt writes sermons, Priska. The theology is finished; the fumes remain." | CUT; the line is made plain Márton at the same time: «"So. Your air warms a grandmother, answers a knock, stops my clocks," he said, "and now it gets a fan. Good. The fumes stay, Priska. The theology is finished."» | V.18 |
| III:89 | "One referee used the word *wishful*, in a footnote, which is where wounds are legally inflicted." | CUT: «One referee used the word *wishful*, in a footnote.» The rest of the confession is untouched. | III.19 |
| IX:65 | "the referee's report with its footnote and its word, *wishful*, standing where wounds are legally inflicted;" (the same line, repeated) | CUT: «the referee's report with its footnote and its word, *wishful*;» | IX.20 |

"The moon's laundry" is in the phrase ledger above (III:47 KEEP, VII:29 CUT).

## 3. Chapter by chapter

Each change gives its number, the round-7 line, its kind, why, and the change in words; then the exact Find and Replace. Kinds: *phrase limit* (a ledger entry in section 2); *explanations routine*; *plainer voice*; *length cut* (a cut for change 2, or a repeat of a line told in full elsewhere); *slip*; *change 3*; and the XIV items.

### Chapter I

File: `round-7/chapter-01.md`. 6 changes. 3,025 → **3,002** words (-23; `wc -w` 3,008 → 2,985).

Phrase pass and slip 1. The letter (I:3–29) is not touched: its copy closes XIV and the two must stay identical. The Göbekli heresy (I:41), the 1924 inventory with item fifty-one (I:63), the 1999 permit line (I:65), the forty-one (I:61) and the shaft's eighteen minutes (I:71) all stay.

1. **I.1** — line 35 (phrase limit: the whole of: cut; -6 words)
   - Find: «by avoiding it. That was the whole of it. The strangeness»
   - Replace with: «by avoiding it. The strangeness»
2. **I.2** — line 37 (phrase limit: manners: vary; +0 words)
   - Find: «and liked the letter's manners, and forgot it.»
   - Replace with: «and liked the letter's courtesy, and forgot it.»
3. **I.3** — line 57 (slip 1 (watch): slip 1; +6 words)
   - Find: «Melek told the clock story, meaning nothing by it. Her grandmother had kept a wall clock, a wedding piece. Every time the old woman came up from a night below, the clock was an hour behind.»
   - Replace with: «Melek told the watch story, meaning nothing by it. Her grandmother had kept a pocket watch, a wedding piece, and carried it down with her. Every time the old woman came up from a night below, the watch was an hour behind.»
4. **I.4** — line 57 (slip 1 (watch): slip 1; +0 words)
   - Find: «An old clock, an old woman, a bell»
   - Replace with: «An old watch, an old woman, a bell»
5. **I.5** — line 59 (phrase limit: manners: cut; -4 words)
   - Find: «Some remembered a clipboard. Some remembered good manners. One man»
   - Replace with: «Some remembered a clipboard. One man»
6. **I.6** — line 61 (explanations routine: routine: one clause; -19 words)
   - Find: «She had flown in on a red-eye; she had counted a bin or a blind alcove that the far direction didn't return; the shelves of smoke made the openings lie.»
   - Replace with: «The shelves of smoke, she decided, had made the openings lie.»

### Chapter II

File: `round-7/chapter-02.md`. 5 changes. 3,047 → **2,950** words (-97; `wc -w` 3,015 → 2,920).

Phrase pass, and the explanations routine at II:33 (the ruling's change 1). Every reader loved this chapter; nothing else in it changes. II:69 ("a third way to hold that night") is a routine instance kept whole. The present-tense slip at II:67 ("Nilay has never asked her directly") was noticed by one reader but is not in the ruling, and stays.

1. **II.1** — line 7 (phrase limit: to the knuckle: vary (letter); -2 words)
   - Find: «I finished the lamp I was at — oil to the knuckle, wick pinched true —»
   - Replace with: «I finished the lamp I was at — oil measured, wick pinched true —»
2. **II.2** — line 33 (explanations routine: routine: the list goes; the one clause 'There was nothing in any of it that a tired surveyor and an Ankara office could not account for between them.' stays; -85 words)
   - Cut the passage from «The '24 surveyor had tired — twice in his inventory the same» to «cleared it since; tuff closes and opens like a poor man's purse.» (85 words).
   - Replace with: nothing. The seam reads «…equally for a morning, then forgave both equally. On Thursday she went and looked. The gallery…».
3. **II.3** — line 39 (phrase limit: the whole of x2; the way it; -3 words)
   - Find: «And under the stamp, the whole of it, the way it had been the whole of it for twenty-six years:»
   - Replace with: «And under the stamp, all of it, as it had been all of it for twenty-six years:»
4. **II.4** — line 59 (phrase limit: the way it; -1 words)
   - Find: «the warmth arrived, the way it had arrived all her life»
   - Replace with: «the warmth arrived, as it had arrived all her life»
5. **II.5** — line 77 (phrase limit: the way it; -6 words)
   - Find: «and the tune came back the way it always came back, at its own pace,»
   - Replace with: «and the tune came back, at its own pace,»

### Chapter III

File: `round-7/chapter-03.md`. 20 changes. 3,215 → **2,713** words (-502; `wc -w` 3,195 → 2,702).

The gravity numbers and tables go; Márton, the watches (III:31, III:69, left wrist), the Carpathian confession (III:89, only its too-pleased clause goes), the register remark and 1,142.6 (III:55, untouched), the hollow of twenty-nine microgal, the eleven-centimeter triangle and his refusal to average (III:59) all stay. "The moon's laundry" keeps its first and only place (III:47), and III.4 keeps the moon in the washing of readings so that the phrase still has something to point at. Márton's banter is made dry (III.9, III.12); Priska is made flat (III.8).

1. **III.1** — line 23 (phrase limit: follow past the lamp / I never do: cut (letter); -10 words)
   - Find: « I did not follow him past the lamp. I never do.*»
   - Replace with: «*»
2. **III.2** — line 33 (length cut: repeats I; -9 words)
   - Find: «up the last stretch of hill himself, having scolded Kemal's tractor into obedience short of it, and he let nobody»
   - Replace with: «up the last stretch of hill himself, and he let nobody»
3. **III.3** — line 33 (length cut: gravity detail; -10 words)
   - Find: «and put his stakes in around the mouth and down the middle gallery and along the deep stair to the threshold of the fourth door.»
   - Replace with: «and put his stakes in from the mouth to the threshold of the fourth door.»
4. **III.4** — line 43 (length cut: gravity numbers; keeps the moon for 'the moon's laundry'; -46 words)
   - Cut the passage from «He worked mornings, when the hill was still honest with its heat.» to «and he trusted no figure that had not been. Then he built» (74 words).
   - Replace with: «He worked mornings, and every reading was washed before it was kept: every number he had ever loved had first been cleaned of the moon. Then he built»
5. **III.5** — line 43 (length cut: repeats II; -26 words)
   - Find: « A century apart, agreeing to the millimeter on seven worn treads and a set of bins, and differing by one entire room in the middle gallery. He asked»
   - Replace with: « He asked»
6. **III.6** — line 47 (length cut: gravity numbers; -10 words)
   - Find: « It was a hollow of some thousands of cubic meters.»
   - Replace with: nothing. The seam reads «…the way old men convert everything, into buildings. A nave's worth of absence, deeper than the…».
7. **III.7** — line 49 (explanations routine: routine + gravity tables: one clause; -107 words)
   - Cut the passage from «He was rigorous about hating it, which is how he loved things.» to «sat down from thirty-four microgal to twenty-nine and refused to go lower.» (142 words).
   - Replace with: «He was rigorous about hating it, which is how he loved things, and he put it to every test the hill allowed; it sat down from thirty-four microgal to twenty-nine and refused to go lower.»
8. **III.8** — line 51 (plainer voice: Priska plain; -4 words)
   - Find: «"Groundwater," Priska said over his shoulder. "Or your tables. Or — forgive me, Professor — your faith."»
   - Replace with: «"Groundwater," Priska said over his shoulder. "Or your tables. Or your faith, Professor."»
9. **III.9** — line 53 (plainer voice: Márton banter plain; -6 words)
   - Find: «"Your air," he said, "is the least interesting fluid on earth and the most guilty one."»
   - Replace with: «"Air," he said. "Most boring fluid on earth. Always guilty."»
10. **III.10** — line 57 (length cut: gravity numbers; -50 words)
   - Find: « Three tripods, three corner prisms — one at the stair head, one at the far niches, one past the sooted lamps — and the laser ranger on a crate he had carried from Uppsala for the purpose. A hundred paces of perimeter. Each side measured three times, forward and back.»
   - Replace with: nothing. The seam reads «…the two plans had quarreled, out of spite. And the triangle would not close: eleven centimeters…».
11. **III.11** — line 59 (length cut: gravity numbers; keeps 'refused to average'; -135 words)
   - Cut the passage from «Priska arrived for the refraction verdict with her stratification maps rolled under» to «air like a held note, the closure came back ten point eight,» (194 words).
   - Replace with: «Priska arrived for the refraction verdict with her stratification maps rolled under her arm like warrants. Air bends light, she said; layered air bends it in layers; his beam was crossing a lasagna. They ran the generator to churn the air, and the triangle stayed eleven centimeters short. On a still night the closure came back ten point eight,»
12. **III.12** — line 63 (plainer voice: Márton banter plain; -3 words)
   - Find: «"Your socks, Priska, have never once been asked to close. If they were, you would buy better socks, and I would lose my only honest colleague."»
   - Replace with: «"Nobody asks your socks to close, Priska. If they did, you would buy better socks, and I would lose my one honest colleague."»
13. **III.13** — line 65 (length cut: trim; -22 words)
   - Find: «for fifteen years, in corridors at conferences from Vienna to Reykjavík, and neither had ever once yielded the other an inch in public or missed a session where the other spoke.»
   - Replace with: «for fifteen years, at conferences from Vienna to Reykjavík.»
14. **III.14** — line 65 (length cut: trim; -16 words)
   - Find: «The cruelty between them was a way of keeping faith, and both of them knew it, and neither had ever said so, there being no need.»
   - Replace with: «The cruelty between them was a way of keeping faith.»
15. **III.15** — line 67 (phrase limit: the way a; -1 words)
   - Find: «He hummed, the way a man hums who is alone and testing,»
   - Replace with: «He hummed, as a man hums who is alone and testing,»
16. **III.16** — line 67 (length cut: trim; -27 words)
   - Find: « So he carried his instruments down in the mornings and up in the evenings, like a man who takes his dog to work and calls it fieldwork.»
   - Replace with: nothing. The seam reads «…"and not a night past the first cloud." The watches agreed. That was the humiliation of…».
17. **III.17** — line 71 (phrase limit: the whole of: vary; +0 words)
   - Find: «It was a letter copied out by hand, the whole of it, in a sloping clerk's hand»
   - Replace with: «It was a letter copied out by hand, every line of it, in a sloping clerk's hand»
18. **III.18** — line 83 (length cut: repeats I; -12 words)
   - Find: «who pulled the year out of him — Yusuf, who introduced people and tripods in the same breath, and who put the camera up»
   - Replace with: «who pulled the year out of him: he put the camera up»
19. **III.19** — line 89 (too-pleased line: too-pleased line; -7 words)
   - Find: «One referee used the word *wishful*, in a footnote, which is where wounds are legally inflicted.»
   - Replace with: «One referee used the word *wishful*, in a footnote.»
20. **III.20** — line 95 (slip 1 (watch): slip 1; +0 words)
   - Find: «Nilay told the clock story then, to change the subject — Melek's grandmother, the wall clock,»
   - Replace with: «Nilay told the watch story then, to change the subject — Melek's grandmother, the pocket watch,»

### Chapter IV

File: `round-7/chapter-04.md`. 16 changes. 3,624 → **3,366** words (-258; `wc -w` 3,603 → 3,347).

The first half of Malta is thinned (hotel, Paola, the stone, Mrs. Vella's polish). The "list of sites that reads like a museum placard" is not in IV; it is the List in XIII, and it is cut there (XIII.14). Everything from Halden's door onward stays except IV.12–IV.16: the Register and the margin "4–5.ix. Kept the hours. A.H.", the two leaves of 6.ix and 7.ix.1999, the phial, the Saflieni shoe and "Three ways to hold it", the founder's slip and Melek's half of the rule. Mrs. Vella is not on the ruling's list of voices; only her travelogue lines are trimmed, and her story of the school party and the Trust's reply ("The Trust does not correct what it did not record") stay, because XIII pays them off.

1. **IV.1** — line 23 (length cut: first half of Malta; -21 words)
   - Find: «A licensee is owed her sponsor's file; a registry that copies its letters by hand has a file worth the flight. »
   - Replace with: nothing. The seam reads «…of the twins that she wrote to Valletta. And in the drawer at the dig house…».
2. **IV.2** — line 27 (length cut: first half of Malta; -5 words)
   - Find: «seven-forty in the morning, an hour and twenty minutes before the first public admission,»
   - Replace with: «seven-forty in the morning, before the first public admission,»
3. **IV.3** — line 27 (length cut: first half of Malta; -32 words)
   - Find: « She noted it, in the way of her trade, as a stratum, and read the stratum as: institutions a century old keep keys for one another. That was all. That, and nothing.»
   - Replace with: nothing. The seam reads «…the licensee. She had asked for no courtesy. That night she looked the name up, because…».
4. **IV.4** — line 31 (length cut: travelogue; -35 words)
   - Find: «Paola on a Monday was a working town doing its working — bread, buses, a church squared up against the sky with the hypogeum crouching at its flank like something the church was keeping an eye on. Mrs. Vella met her at the ticket desk»
   - Replace with: «In Paola Mrs. Vella met her at the ticket desk»
5. **IV.5** — line 33 (length cut: travelogue; -35 words)
   - Cut the passage from «It was not her stone. It was honey where her tuff is» to «broken in by accident, cistern-cutters after water; everything since had been apology.» (71 words).
   - Replace with: «It was not her stone, but the ceilings were rounded as her rooms were rounded, and over the wall niches the black had depth, layer under layer, the same archive nobody had ever needed to open.»
6. **IV.6** — line 41 (length cut: travelogue; -22 words)
   - Find: « She smiled the smile of a woman who has watched ten visitors a day, eighty a day, make noise for thirty years.»
   - Replace with: nothing. The seam reads «…the point, dear. Anyone can make a noise." "It has answered me twice in my life,…».
7. **IV.7** — line 43 (length cut: trim; -19 words)
   - Find: «a moment longer than the experiment required, in the manner of her trade and of one or two other trades she did not name to herself.»
   - Replace with: «a moment longer than the experiment required.»
8. **IV.8** — line 47 (length cut: travelogue; -14 words)
   - Find: «On the way up, in the empty top room where the light was being persuaded to come on, Mrs. Vella told her the story,»
   - Replace with: «On the way up Mrs. Vella told her the story,»
9. **IV.9** — line 47 (length cut: travelogue; -24 words)
   - Find: «The archives burned in the bombing, so nothing can be checked, and nothing ever has been found, and nothing ever will be. We don't tell it on the tours now. It frightens, and fright sells, and the two have ruined enough between them."»
   - Replace with: «The archives burned in the bombing, so nothing can be checked. We don't tell it on the tours now."»
10. **IV.10** — line 47 (length cut: Mrs. Vella's polish; travelogue; -13 words)
   - Find: «wanting it struck off the record or put on it — one or the other, you understand; a person can live with either. They answered»
   - Replace with: «wanting it struck off the record or put on it. They answered»
11. **IV.11** — line 47 (length cut: Mrs. Vella's polish; -9 words)
   - Find: «I've kept the letter half a lifetime, and it has kept me curious exactly as long."»
   - Replace with: «I've kept the letter half a lifetime."»
12. **IV.12** — line 57 (phrase limit: repeats III; -15 words)
   - Find: «and read, page after page, one line, in typescripts and hands that aged down the stack and never varied by a word: *Nothing to record.*»
   - Replace with: «and read, page after page, one line: *Nothing to record.*»
13. **IV.13** — line 69 (length cut: repeats I; -8 words)
   - Find: « (April; the meeting they preceded, June; backdating, the least mysterious practice in either country)»
   - Replace with: « (April; the meeting they preceded, June)»
14. **IV.14** — line 95 (plainer voice: Márton banter plain; -3 words)
   - Find: «"The cloud," he said, "is a meteorological fact. My hollow is a geophysical one. One of us will still be there in September."»
   - Replace with: «"The cloud is weather," he said. "My hollow is geology. We will see which one is still there in September."»
15. **IV.15** — line 115 (slip 1 (watch): slip 1; +0 words)
   - Find: «an hour-behind clock,»
   - Replace with: «an hour-behind watch,»
16. **IV.16** — line 117 (phrase limit: to the knuckle: cut; -3 words)
   - Find: «the ninth, filled to the knuckle, the wick pinched true.»
   - Replace with: «the ninth, filled, the wick pinched true.»

### Chapter V

File: `round-7/chapter-05.md`. 21 changes. 3,376 → **3,223** words (-153; `wc -w` 3,347 → 3,197).

The gas figures around the scenes are thinned; Havva, the father's cough at 05:40, Seher and the masks stay whole. The sitting-night tally keeps its one full statement at V:69 (twenty-two nights, fifteen events; twenty-six, two), which XIV:77 quotes; the earlier copy at V:43 goes. Slip 4 is here (V.7). Kaya Bey (V.11), Seher (V.16, V.17) and Márton (V.18) are made plainer.

1. **V.1** — line 23 (phrase limit: past the name: vary (letter); -2 words)
   - Find: «answer the once, and past the name, nothing; do not follow»
   - Replace with: «answer the once, and no more; do not follow»
2. **V.2** — line 27 (phrase limit: the whole of: cut; -3 words)
   - Find: «That was the whole of her position, and she held it»
   - Replace with: «That was her position, and she held it»
3. **V.3** — line 27 (length cut: gas figures; -29 words)
   - Find: « Give her a flue and a fan and six hours, and the company went out with the air. A chemistry you can pipe outdoors is a kind of mercy.»
   - Replace with: nothing. The seam reads «…of the light, a voice under a knock. She had watched the word *hypercapnia* do, in…».
4. **V.4** — line 31 (phrase limit: to the knuckle: cut; -6 words)
   - Find: «, and Melek led, and the round came first, oil to the knuckle, wicks pinched.»
   - Replace with: «, and Melek led, and the round came first.»
5. **V.5** — line 31 (phrase limit: the way she; -1 words)
   - Find: «and Melek considered the pump the way she had considered Márton's gravimeter.»
   - Replace with: «and Melek considered the pump as she had considered Márton's gravimeter.»
6. **V.6** — line 35 (phrase limit: two breaths: cut; -3 words)
   - Find: «and then stood in the waiting, two breaths entire, and the waiting was the rite»
   - Replace with: «and then stood in the waiting, and the waiting was the rite»
7. **V.7** — line 43 (slip 4 (Nine): slip 4; +10 words)
   - Find: «Fatma Nine, waking from a doze,»
   - Replace with: «Fatma Nine — *Nine* is the village's word for a grandmother — waking from a doze,»
8. **V.8** — line 43 (length cut: ordinary account inside the scene; -15 words)
   - Find: «her mother's soap — the co-op still sold it; every mother in the room had used it — arrived whole»
   - Replace with: «her mother's soap, arrived whole»
9. **V.9** — line 43 (length cut: gas figures; the tally stays in V:69; -28 words)
   - Find: «both books balanced: twenty-two sitting nights so far, fifteen such events, every one of them below the second door, every one on a still night, when her forecast sheets — her candles lay down at printed times, at appointed places — had pooled the gallery in dead air like a held note.»
   - Replace with: «both books balanced: every event below the second door, every one on a still night, in air her forecast sheets had marked as dead.»
10. **V.10** — line 49 (length cut: gas figures; -5 words)
   - Find: «four point zero percent. Forty thousand parts per million.»
   - Replace with: «four point zero percent.»
11. **V.11** — line 67 (plainer voice: Kaya Bey plain; +3 words)
   - Find: «Institutions prefer a cause they can mandate, he said pleasantly, and here, Doctor, was a cause.»
   - Replace with: «The Ministry needed a cause it could put in an order, he said pleasantly, and here, Doctor, was one.»
12. **V.12** — line 67 (length cut: gas figures; -6 words)
   - Find: «and scrubber masks, soda-lime canisters of the mine-rescue kind, below the second door»
   - Replace with: «and scrubber masks below the second door»
13. **V.13** — line 69 (phrase limit: manners; which was; -3 words)
   - Find: «The village's manners cooled by exactly one degree, which was the temperature of a courtesy observed:»
   - Replace with: «The village cooled by exactly one degree, the temperature of a courtesy observed:»
14. **V.14** — line 71 (length cut: trim; -9 words)
   - Find: «twenty-seven accounts, at kitchen tables, over tea she was sorry about by the third.»
   - Replace with: «twenty-seven accounts, at kitchen tables.»
15. **V.15** — line 71 (length cut: trim; -14 words)
   - Find: «She kept a checklist, and the checklist never once cleared: a maiden name, a debt, a document, a buried thing, a date, a fact that could be checked and would stand. No presence, in twenty-seven kitchens, had ever produced one.»
   - Replace with: «She kept a checklist, and it never once cleared: no presence, in twenty-seven kitchens, had ever produced a fact that could be checked and would stand.»
16. **V.16** — line 79 (plainer voice: Seher plain; -2 words)
   - Find: «It is not talk that is missing, Doctor."»
   - Replace with: «It isn't talk that's missing, Doctor."»
17. **V.17** — line 79 (plainer voice: Seher plain; +4 words)
   - Find: «The papers decline. You decline too, Doctor — kindly."»
   - Replace with: «The papers won't say. You won't say either, Doctor. You're kind about it."»
18. **V.18** — line 81 (too-pleased line: too-pleased line cut; Márton banter plain; -6 words)
   - Find: «"Your guilty air has warmed a grandmother, answered a knock, and stopped my clocks," he said, "and now it installs with a fan. Oxygen debt writes sermons, Priska. The theology is finished; the fumes remain."»
   - Replace with: «"So. Your air warms a grandmother, answers a knock, stops my clocks," he said, "and now it gets a fan. Good. The fumes stay, Priska. The theology is finished."»
19. **V.19** — line 87 (length cut: gas figures; -15 words)
   - Find: «could not be located in the service's files for the relevant quarter; that the service's accreditation for that quarter had lapsed, for administrative reasons; that readings»
   - Replace with: «could not be located for the relevant quarter, and that readings»
20. **V.20** — line 87 (length cut: trim; -17 words)
   - Find: « Her canon kept its stamp, and the number it stood on had become a story about paperwork.»
   - Replace with: nothing. The seam reads «…restored certificate is a certificate with a biography. Someone had read her report more closely than…».
21. **V.21** — line 87 (length cut: trim; -6 words)
   - Find: « — only the number's provenance — and the splinter was exactly splinter-sized, and she sat»
   - Replace with: « — only the number's provenance — and she sat»

### Chapter VI

File: `round-7/chapter-06.md`. 11 changes. 3,227 → **2,992** words (-235; `wc -w` 3,198 → 2,963).

The viral-post stretch and the view counts go (VI.10); "four million" stays, because X, XII and XIII use it. Halden's letter to Yusuf dated the Tuesday (VI:53) and Yusuf's arithmetic (VI:55) stay; only the ordinary accounts shrink. The server-lag theory (VI:39), the tea (VI:45), the sandal frame, the doubled reflection and the ninety-seven percent (VI:47–49) stay. The letter's "two nights" (VI:15) is left, as the ruling says.

1. **VI.1** — line 17 (phrase limit: to the knuckle: vary (letter); -2 words)
   - Find: «and I filled the lamp, and oil to the knuckle settles more than a wick.*»
   - Replace with: «and I filled the lamp, and measured oil settles more than a wick.*»
2. **VI.2** — line 19 (phrase limit: follow past the lamp / I never do: cut (letter); -11 words)
   - Find: «small in the daylight and no less his for that, and I did not follow past the lamp. I never do. The day's mark»
   - Replace with: «small in the daylight and no less his for that. The day's mark»
3. **VI.3** — line 29 (phrase limit: two breaths: cut; -4 words)
   - Find: «and waited out the two breaths, every time, though nothing had ever answered him»
   - Replace with: «and waited, every time, though nothing had ever answered him»
4. **VI.4** — line 31 (explanations routine: routine: one clause; -24 words)
   - Find: «himself before anyone could make them for him: a bin counted as a room in cold smoke; his stride shortening at the far turn; the shelves of dead air making openings lie.»
   - Replace with: «himself before anyone could make them for him.»
5. **VI.5** — line 33 (plainer voice: Priska plain; -7 words)
   - Find: «"Your rooms drift in my weather," she said. "Everything on this hill drifts in it. If I am the control variable of this circus, I want it minuted that I object."»
   - Replace with: «"Your forty-ones fall on my pooled-air days," she said. "If my air is the control variable here, I want it minuted that I object."»
6. **VI.6** — line 47 (explanations routine: routine: one clause; -30 words)
   - Find: «He made the excuses in the chat's voice before the chat could: a villager in grandmother-woven sandals, and the co-op did know a family that still wove them, out of the thorn side; a herder; a hoax, meaning him; a leaf; the lamp bracket's shadow. All five stood up nicely.»
   - Replace with: «He made the excuses in the chat's voice before the chat could, and every one of them stood up nicely.»
7. **VI.7** — line 49 (explanations routine: routine: one clause; 'flat on the palm' KEEP; -21 words)
   - Find: «flat on the palm: wet plaster doubles; a low lamp stands a man's shadow up; a boy who has been alone in bad air sees company. He took none of them out loud.»
   - Replace with: «flat on the palm, and he took none of them out loud.»
8. **VI.8** — line 55 (length cut: trim; -6 words)
   - Find: «He kept a changelog of his own posts; he had always kept changelogs; the changelog said»
   - Replace with: «He kept a changelog of his own posts; it said»
9. **VI.9** — line 55 (explanations routine: routine: one account; -32 words)
   - Find: «He turned the ordinary accounts over: the Trust's young woman with the clipboard, seen in April, scarf or no scarf, still in the country with a courier's bag; a clerk who thanked everybody for everything; a guess, made by someone who had watched four years of his evenings and knew his habits better than he did.»
   - Replace with: «The Trust's young woman with the clipboard, seen in April, scarf or no scarf, could still be in the country with a courier's bag.»
10. **VI.10** — line 57 (length cut: viral-post stretch and view counts; -94 words)
   - Cut the passage from «The post traveled. By Friday noon it had forty thousand views, which» to «almost written. And they did not need him to name the place.» (118 words).
   - Replace with: «The post traveled. By Saturday night it was past four million and had stopped being his. And nobody needed him to name the place.»
11. **VI.11** — line 61 (phrase limit: two breaths: cut; -4 words)
   - Find: «without knocking, without waiting out the two breaths, and the rooms»
   - Replace with: «without knocking, without waiting, and the rooms»

### Chapter VII

File: `round-7/chapter-07.md`. 25 changes. 4,169 → **3,967** words (-202; `wc -w` 4,124 → 3,922).

Phrase pass. The breach itself (VII:45–75) stays whole: inside it only phrase-limit changes, the ordered cut of the second "Nobody counted twice" (VII.16), and the flour routine (VII.18). The camera found upright and wiped (VII:49), "Is the fire mountain awake?" (VII:67), the woman's forearm, the teeth, the three hours and forty minutes (VII:77), the woven print (VII:79) and the word šumašar (VII:83) all stay. Kaya Bey is made plainer (VII.21, VII.23).

1. **VII.1** — line 11 (phrase limit: past the name: vary (letter); -1 words)
   - Find: «being from a part of the house you have not walked — and past the name, nothing. Our rule,»
   - Replace with: «being from a part of the house you have not walked — and say no more. Our rule,»
2. **VII.2** — line 25 (phrase limit: past the name: vary (letter); -4 words)
   - Find: «Say the name of the room, and past the name, nothing. They keep»
   - Replace with: «Say the name of the room, once. They keep»
3. **VII.3** — line 29 (phrase limit: moon's laundry: cut; trim; -14 words)
   - Find: «had sat under the deep floors all summer like a guest who will neither leave nor explain itself — twenty-nine microgal, minus the moon's laundry — and»
   - Replace with: «had sat under the deep floors all summer — twenty-nine microgal — and»
4. **VII.4** — line 33 (length cut: trim; -17 words)
   - Find: «in orderly lengths, tuff and tuff and a hand's depth of the hard blue band the old wells spoke of, and Melek sat»
   - Replace with: «in orderly lengths, and Melek sat»
5. **VII.5** — line 39 (explanations routine: routine: one clause; which was; -26 words)
   - Find: «He gave the table his explanations himself: retained heat of the summer, sunk and stored; the aquifer, breathing through the floor; wet rock making its own weather, which he had seen in mines. He disliked all three equally, which was how she knew he had already checked them.»
   - Replace with: «He gave the table three explanations himself and disliked all three equally; that was how she knew he had already checked them.»
6. **VII.6** — line 43 (phrase limit: which was; -2 words)
   - Find: «read generously, which was the only way Kaya Bey's ministry ever read anything»
   - Replace with: «read generously, the only way Kaya Bey's ministry ever read anything»
7. **VII.7** — line 43 (phrase limit: the way she; -1 words)
   - Find: «and Melek put her conditions under the ministry's the way she put everything under everything:»
   - Replace with: «and Melek put her conditions under the ministry's, as she put everything under everything:»
8. **VII.8** — line 43 (length cut: trim; -18 words)
   - Find: « Nobody asked on whose authority. The annex held the Ministry's, and Melek's was older, and both were satisfied.»
   - Replace with: nothing. The seam reads «…given at the mouth; and no counting below. At the mulberries, meanwhile, two cars from Ankara…».
9. **VII.9** — line 43 (length cut: trim; -19 words)
   - Find: « At the mulberries, meanwhile, two cars from Ankara had come and gone, filming the mouth, served tea by children.»
   - Replace with: nothing. The seam reads «…and Melek's was older, and both were satisfied. They went down on the Sunday, in the…».
10. **VII.10** — line 45 (phrase limit: two breaths: cut; ritual not renamed; -12 words)
   - Find: «and knocked at the head of the deep stair with the flat of his hand, twice, softly, and waited out the two breaths, as he always did,»
   - Replace with: «and knocked at the head of the deep stair, and waited, as he always did,»
11. **VII.11** — line 45 (phrase limit: two breaths x2: vary; -4 words)
   - Find: «and stood the two breaths entire, and past the two breaths she went in first,»
   - Replace with: «and stood out the waiting, and then she went in first,»
12. **VII.12** — line 57 (phrase limit: the whole of: vary; -3 words)
   - Find: «That was the whole of it, she thought, standing there:»
   - Replace with: «That was it, she thought, standing there:»
13. **VII.13** — line 59 (phrase limit: which was; -2 words)
   - Find: «at the basin's head, which was where a lamp went,»
   - Replace with: «at the basin's head, where a lamp went,»
14. **VII.14** — line 59 (phrase limit: manners: vary; -2 words)
   - Find: «the hand went out and hung with its manners on, and nothing took it,»
   - Replace with: «the hand went out and hung there, courteous, and nothing took it,»
15. **VII.15** — line 71 (phrase limit: which was; -2 words)
   - Find: «what a spatula holds, which was most of what there was,»
   - Replace with: «what a spatula holds, most of what there was,»
16. **VII.16** — line 71 (ordered cut: doubled 'Nobody counted twice': second cut; -3 words)
   - Find: «there were others behind it. Nobody counted twice. The room was one room,»
   - Replace with: «there were others behind it. The room was one room,»
17. **VII.17** — line 73 (phrase limit: to the knuckle: cut; -6 words)
   - Find: «and topped the niche-lamp to the knuckle of her thumb, and pinched the wick true,»
   - Replace with: «and topped the niche-lamp, and pinched the wick true,»
18. **VII.18** — line 75 (explanations routine: routine: cut (Kaya Bey's 'flour travels in pockets' in VIII keeps the ordinary account); the way a; -31 words)
   - Find: «She bagged it with the ash, procedure reasserting itself the way a soldier polishes boots, and gave the ordinary accounts their turn on the climb: a heritage mill's paper bag in somebody's pocket; a cuff; a joke with a mortar. The stairs»
   - Replace with: «She bagged it with the ash, procedure reasserting itself. The stairs»
19. **VII.19** — line 79 (phrase limit: repeats VI:47; -5 words)
   - Find: «The cards asked to be formatted that evening, both of them, politely, the way institutions ask.»
   - Replace with: «The cards asked to be formatted that evening, both of them.»
20. **VII.20** — line 83 (length cut: trim; -14 words)
   - Find: « She did not trust the feeling. She was asleep before any reply could come, and none had come by morning.»
   - Replace with: « She did not trust the feeling.»
21. **VII.21** — line 85 (plainer voice: Kaya Bey plain; -3 words)
   - Find: «"Cappadocia kept hermits in its caves into living memory; a community could keep a lower house, and keep its own counsel, and keep it clean."»
   - Replace with: «"Cappadocia had hermits in its caves within living memory. A community could live down there, keep to itself, keep the place clean."»
22. **VII.22** — line 85 (phrase limit: manners: vary; +0 words)
   - Find: «the tidy ash, the manners, even the teeth,»
   - Replace with: «the tidy ash, the courtesy, even the teeth,»
23. **VII.23** — line 85 (plainer voice: Kaya Bey plain; -1 words)
   - Find: «"The chamber goes in the file," he said, "and the file goes up, and until it comes down, the block stays in its socket under the Ministry's wire and lead."»
   - Replace with: «"The chamber goes in the file," he said. "The file goes up. Until it comes down, the block stays in its socket, under Ministry wire and a lead seal."»
24. **VII.24** — line 87 (phrase limit: to the knuckle: cut; -4 words)
   - Find: «doing the round of nine, oil to the knuckle, pinching each flame true.»
   - Replace with: «doing the round of nine, pinching each flame true.»
25. **VII.25** — line 93 (phrase limit: to the knuckle: cut; -8 words)
   - Find: «or would be burning; the oil had gone in to the knuckle; the house was keeping its evening.»
   - Replace with: «or would be burning; the house was keeping its evening.»

### Chapter VIII

File: `round-7/chapter-08.md`. 22 changes. 4,030 → **3,455** words (-575; `wc -w` 3,997 → 3,426).

The committee and the lab results. The four statements (VIII:39–91) are untouched, including Márton's "Instruments: none deployed by me." In the committee, the Ministry's question "who elected the Trust?" and the Trust's reply go (VIII.18); the Registrar's annex (VIII:127), the closure dated the fourteenth (VIII:129), Márton's solstice application (VIII:131) and the coin and its foam (VIII:133–139) stay. In the lab results, the ash's preliminary line goes (its final is in X:49); the herbarium grain, the hair that matches every population a little, and the tritium zero with Márton's half-life note stay. Demircioğlu's letter keeps *you-who-are* and "late, and wrong, or early, and right". Leyla Hanım's death and vigil stay; only the village's list of explanations goes.

1. **VIII.1** — line 21 (phrase limit: to the knuckle: vary (letter); +0 words)
   - Find: «the basin was full, and the oil was to the knuckle, and the mark was cut.*»
   - Replace with: «the basin was full, and the oil was at its measure, and the mark was cut.*»
2. **VIII.2** — line 33 (plainer voice: Kaya Bey plain; -10 words)
   - Find: «per the incident annex — "so that the record will have what the hour had," he said, "four rooms of it, and no corridors between."»
   - Replace with: «per the incident annex. "Four people, four statements," he said. "No conferring. Sign every page."»
3. **VIII.3** — line 35 (length cut: trim; -21 words)
   - Find: «a queue of queries at the co-op, a drone that stood over the cemetery wall at dusk until a boy brought it down with a hose of water, and a man from Kayseri»
   - Replace with: «a queue of queries at the co-op and a man from Kayseri»
4. **VIII.4** — line 37 (length cut: trim; -29 words)
   - Find: «Nilay compiled the annexes herself, because she was the registrar of her own dig and there was no one to delegate to who did not already have a version of the hour in them. The statements»
   - Replace with: «Nilay compiled the annexes herself. The statements»
5. **VIII.5** — line 93 (plainer voice: Priska plain; the whole of: cut; -21 words)
   - Find: «and said, "Four honest people. Memory is not an instrument, which is why the procedure wants two witnesses to everything, and we supplied four witnesses to nothing." That was the whole of her commentary.»
   - Replace with: «and said, "Four honest people. Four different hours. Memory is not an instrument."»
6. **VIII.6** — line 99 (length cut: trim; -18 words)
   - Find: « Hittite has been dead three thousand years and owes us no consistency; the debt runs the other way.»
   - Replace with: nothing. The seam reads «…and right. I decline to choose for you. You were my most confident student and my…».
7. **VIII.7** — line 99 (length cut: trim; -17 words)
   - Find: « You were my most confident student and my best questioner, which is a warning, not a compliment.»
   - Replace with: nothing. The seam reads «…no consistency; the debt runs the other way. Do not build on this. — Dem.* The…».
8. **VIII.8** — line 101 (length cut: lab results (the ash's final stays in X); -16 words)
   - Find: «The laboratory's lines were shorter. Bag 1, ash: *preliminary counts irregular; the laboratory asks for the sample's history; report to follow.* Bag 2:»
   - Replace with: «The laboratory's lines were shorter. Bag 2:»
9. **VIII.9** — line 101 (length cut: lab results; -24 words)
   - Find: «annotated by the laboratory as contamination (mixed sample); see attached notes*; the notes were not attached, and a letter about them would be answered in the fullness of whoever answers such letters. And the water,»
   - Replace with: «annotated by the laboratory as contamination (mixed sample).* And the water,»
10. **VIII.10** — line 105 (explanations routine: routine + lab results: one clause; -81 words)
   - Cut the passage from «Priska read the zero and shrugged it upward into sense: fossil aquifer» to «the room from Ankara nodded at whichever they had heard last. Márton» (92 words).
   - Replace with: «Priska called it fossil water, the commonest water on earth. Márton»
11. **VIII.11** — line 107 (explanations routine: routine: one clause; -45 words)
   - Find: «She built the forks methodically, because building forks was how she kept her hands still: she had typed from memory and slipped; she had amended at the keyboard without noticing the amending; the amendment was the truer memory and she had refused it on the night and it had taken the file by force.»
   - Replace with: «She had typed from memory, she supposed, and slipped.»
12. **VIII.12** — line 109 (explanations routine: routine: one clause; -52 words)
   - Cut the passage from «The village had three explanations for that, and she had furnished none» to «is an office, and no one who holds it comes out unbruised.» (66 words).
   - Replace with: «The village had three explanations for that, and she had furnished none of them.»
13. **VIII.13** — line 109 (phrase limit: the way she; -1 words)
   - Find: «Nilay had known her the way she knew all of them,»
   - Replace with: «Nilay had known her as she knew all of them,»
14. **VIII.14** — line 111 (phrase limit: manners: vary; +0 words)
   - Find: «the manners had arrived in her by roads she had stopped auditing.»
   - Replace with: «the custom had arrived in her by roads she had stopped auditing.»
15. **VIII.15** — line 111 (phrase limit: to the knuckle: cut; -7 words)
   - Find: «The round was done, oil to the knuckle, wicks pinched true, and then Melek»
   - Replace with: «The round was done, and then Melek»
16. **VIII.16** — line 115 (phrase limit: the whole of: cut; -3 words)
   - Find: «That was the whole of the institution, if it was an institution:»
   - Replace with: «That was the institution, if it was an institution:»
17. **VIII.17** — line 117 (length cut: committee; -14 words)
   - Find: «Melek did not come — the lamps do not sit on committees — and the village sent her half the tea afterward all the same.»
   - Replace with: «Melek did not come; the lamps do not sit on committees.»
18. **VIII.18** — line 119 (length cut: committee: the Ministry's question and the Trust's reply (VIII:119-125) go; the Registrar's annex (VIII:127) stays; -194 words)
   - Cut the passage from «The statements were tabled and not read aloud, their contradictions standing in» to «*resolved,* which was accurate in every respect but the ones that count.» (216 words).
   - Replace with: «The statements were tabled and not read aloud. Kaya Bey restated the hermits for the record; flour, he said, travels in pockets.»
19. **VIII.19** — line 127 (length cut: seam after VIII.18: with the question and reply gone, 'too' has nothing to refer to; -1 words)
   - Find: «and Kaya Bey read that too, more slowly, because it was the only document»
   - Replace with: «and Kaya Bey read that aloud, slowly, because it was the only document»
20. **VIII.20** — line 129 (plainer voice: Kaya Bey plain; -5 words)
   - Find: «"Then you were anticipated, Doctor. The Ministry manages it for all of us eventually."»
   - Replace with: «"Then the Ministry got there first, Doctor. Next item."»
21. **VIII.21** — line 135 (plainer voice: Kaya Bey plain; -9 words)
   - Find: «Kaya Bey observed that boxes grow lighter between provinces, and that a box which had held four million views' worth of nothing was a box with a market.»
   - Replace with: «Kaya Bey said that things go missing from boxes between provinces, and that anything from this site would sell.»
22. **VIII.22** — line 135 (plainer voice: Márton banter plain; -7 words)
   - Find: «"I left the house a lamp," he said, "and was paid for it at the going rate. I have been robbed in four countries, Doctor, and this was the first transaction of my life that ran the other way."»
   - Replace with: «"I left the house a lamp," he said, "and I was paid for it. I have been robbed in four countries, Doctor. This is the first time it went the other way."»

### Chapter IX

File: `round-7/chapter-09.md`. 23 changes. 3,553 → **3,212** words (-341; `wc -w` 3,518 → 3,186).

Marques's wormhole physics is cut by half (IX.11) and she is made blunt (IX.8, IX.10, IX.12, IX.17); the throat, negative energy, the Casimir effect, "Show me the machine", the fuel bill and the whiteboard stay, so the wormhole stays hinted, almost canon, never confirmed. The solstice set-up is thinned (IX.7, IX.8, IX.13). The Ministry's grant dated the twenty-eighth (IX:31), the forty nanoseconds twice (IX:53–55), Priska's forks column (IX:59), the parcel, the acquittal and "For your peace" (IX:65–67), Halden's visit and the cello (IX:71–75) stay. **Márton's last descent (IX:77–79) is not touched**: it is his death scene's first half, and it holds three kept phrases ("first knuckle", "two breaths", and "On his right wrist").

1. **IX.1** — line 15 (phrase limit: to the knuckle: vary (letter); +0 words)
   - Find: «*Both filled to the knuckle. The room leaned once,»
   - Replace with: «*Both filled to the measure. The room leaned once,»
2. **IX.2** — line 17 (phrase limit: follow past the lamp / I never do: cut (letter); -10 words)
   - Find: «and wanting is a surface thing, and she went up. I did not follow past the lamp. I never do.*»
   - Replace with: «and wanting is a surface thing, and she went up.*»
3. **IX.3** — line 29 (length cut: trim; -34 words)
   - Find: «The dig went down to its winter skeleton — Nilay cataloguing in the dig house with a stove that drew badly, Priska above ground among her ducts and thresholds, Yusuf gone to his mother's people in Derinkuyu for the frost weeks — and Márton stayed,»
   - Replace with: «The dig went down to its winter skeleton, and Márton stayed,»
4. **IX.4** — line 29 (explanations routine: routine: one clause; -24 words)
   - Find: «obedient as a mule, re-run once in December from a different vertex order with the same deficit; and he had dismissed, in writing, his own counter-readings — winter stratification, tripod settlement, tuff dust on the returns — with the courtesy»
   - Replace with: «obedient as a mule; and he had dismissed, in writing, his own counter-readings with the courtesy»
5. **IX.5** — line 33 (phrase limit: the whole of: vary; -2 words)
   - Find: «and that was the whole of the blessing.»
   - Replace with: «and that was all the blessing.»
6. **IX.6** — line 35 (length cut: trim; -13 words)
   - Find: «and drank it when she chose, which gave her the advantage over every other visitor the site had had.»
   - Replace with: «and drank it when she chose.»
7. **IX.7** — line 35 (length cut: trim; -23 words)
   - Find: «She had read the numbers — he had written in October, stripped of story, the triangle, the residual, the twenty-nine microgal, as one professional posts figures to another — and she had also, it emerged, read the withdrawn preprint»
   - Replace with: «She had read the numbers he sent in October, and also, it emerged, the withdrawn preprint»
8. **IX.8** — line 37 (plainer voice: Marques plain; solstice set-up; -26 words)
   - Cut the passage from «"Two clocks," she said, "is an anecdote. Three are a committee, you» to «internet had decided the solstice mattered; the internet is not told otherwise.» (82 words).
   - Replace with: «"Two clocks is an anecdote," she said. "Three is a committee, you wrote me once. Fine. Wear them on your wrist and your body heat votes for all three." She walked the hill with him in the flat light, stood at the mouth while he explained the duct, and ignored the solstice-watchers along the cemetery wall.»
9. **IX.9** — line 39 (phrase limit: the way it; -1 words)
   - Find: «He watched it take the note out of her the way it took it out of everyone»
   - Replace with: «He watched it take the note out of her as it took it out of everyone»
10. **IX.10** — line 39 (plainer voice: Marques plain; +4 words)
   - Find: «"Resonance," she said. "Rooms sing. Cathedrals sing better. Geometry is not hospitable, Professor."»
   - Replace with: «"Resonance," she said. "A room with a good mode. Cathedrals do it better. It means nothing, Professor."»
11. **IX.11** — line 43 (plainer voice: wormhole physics halved; Marques plain; -52 words)
   - Cut the passage from «"A throat wants negative energy," Marques said. "Negative energy is real —» to «the room once, professionally, a suspect's tidy kitchen. "Show me the machine."» (108 words).
   - Replace with: «"To hold a throat open you need negative energy," Marques said. "It exists — the Casimir effect, between two plates, very small. To keep open anything a cat could walk through you would need a planet's worth. Nobody has ever shown me where that comes from." She looked around the room once. "Show me the machine."»
12. **IX.12** — line 47 (plainer voice: Marques plain; -10 words)
   - Cut the passage from «"Then it has a fuel bill," Marques said, "and somebody is paying» to «noise, write to me. They will not. Send the logs either way."» (79 words).
   - Replace with: «"Then it has a fuel bill," Marques said, "and somebody is paying it. Find the bill and I'll come and look." At the mouth, before the hired car turned, she gave him her prescription through the car window: "Leave your watches down one night. All three together, same temperature, not on your wrist. If they disagree by more than noise, write to me. They won't. Send the logs anyway."»
13. **IX.13** — line 49 (phrase limit: to the knuckle: cut; solstice set-up; -17 words)
   - Find: «eleven of them, lawful, lamps to the knuckle; the sitting ran its ledger two rooms away, and he passed it going down, and nodded, and was nodded to, in the economy of it.»
   - Replace with: «eleven of them, lawful, and he passed them going down, and nodded, and was nodded to.»
14. **IX.14** — line 49 (phrase limit: two breaths: cut; ritual not renamed; -12 words)
   - Find: «at the head of the deep stair he knocked with the flat of his hand, twice, softly, and waited out the two breaths, having watched the boy»
   - Replace with: «at the head of the deep stair he knocked, and waited, having watched the boy»
15. **IX.15** — line 51 (length cut: trim; -7 words)
   - Find: «logging against the satellites when the sky permitted, which, in a valley, is a philosophy.»
   - Replace with: «logging against the satellites when the sky permitted.»
16. **IX.16** — line 53 (length cut: trim; -14 words)
   - Find: «before anyone could do it for him: it existed, it described sporadic excursions of tens of nanoseconds in units that had undergone a synchronization transition during cold soak; his had undergone no transition below; and the advisory went into the log anyway,»
   - Replace with: «before anyone could do it for him; it covered excursions of tens of nanoseconds, under conditions his watches had not met, and it went into the log anyway,»
17. **IX.17** — line 57 (plainer voice: Marques plain; -22 words)
   - Cut the passage from «*Find the heat you are missing. Correlated excursions are not in the» to «will come in January and we will be unlucky together. — I.M.*» (63 words).
   - Replace with: «*Find the heat you're missing. Correlated excursions aren't in the advisory. I checked. Engineers write annexes to please whoever is asking. Two nights is an anecdote with a witness. I'll come in January and we can be unlucky together. — I.M.*»
18. **IX.18** — line 59 (plainer voice: Priska plain; -2 words)
   - Find: «"Your clocks came back changed," she said. "Mine only breathe. I do not like it, Professor, and I am not required to."»
   - Replace with: «"Your clocks came back changed," she said. "My meters don't. I don't like it, Professor, and I don't have to."»
19. **IX.19** — line 59 (plainer voice: Márton banter plain; -1 words)
   - Find: «"The body is the oven, Priska; I am keeping the oven honest,"»
   - Replace with: «"The body is the oven, Priska. I keep the oven honest,"»
20. **IX.20** — line 65 (too-pleased line: too-pleased line; -6 words)
   - Find: «and its word, *wishful*, standing where wounds are legally inflicted;»
   - Replace with: «and its word, *wishful*;»
21. **IX.21** — line 67 (length cut: trim; -29 words)
   - Find: « It was, like everything in that country, both clean and unclean: an annex is a document written by men who had never met his clocks, and engineers please whoever is asking; he knew all that; he stood with it anyway.»
   - Replace with: « He knew what annexes were worth; he stood with it anyway.»
22. **IX.22** — line 71 (phrase limit: the way he; -6 words)
   - Find: «He looked once at the whiteboard, the way he looked at everything, as if it had already been filed,»
   - Replace with: «He looked once at the whiteboard, as if it had already been filed,»
23. **IX.23** — line 73 (length cut: trim; -34 words)
   - Find: « The frost: Halden thought it would hold through January; the village thought not; both sides cited the same mulberry. The founder, who had held a teacup all his life and drunk none, liking what holding does. The co-op stove, which drew badly, and how a stove's character is fixed by its first winter.»
   - Replace with: « The frost. The founder, who had held a teacup all his life and drunk none, liking what holding does.»

### Chapter X

File: `round-7/chapter-10.md`. 14 changes. 3,341 → **3,262** words (-79; `wc -w` 3,319 → 3,240).

Phrase pass. The death scene (X:29–37: the right wrist, the watches stopped at 03:12 and 05:41, the third still agreeing with the sky) and the inquest (X:45: 1,142.5, and the elimination prints taken at the co-op table) are untouched. Marques (X.3, X.5), Kaya Bey (X.6), Priska (X.9) and Seher (X.12) are made plainer; Seher's "I am thirty-four. What am I supposed to do now?" stays word for word. The title stays, as the ruling says.

1. **X.1** — line 27 (phrase limit: the whole of: cut; which was x2; -38 words)
   - Cut the passage from «Guilt had given her a profession, and a mercy to hand out» to «a chemist whose instrument had just been asked to acquit a hill.» (70 words).
   - Replace with: «She had never once stood at a cave mouth in the position she held on the last morning of December: a chemist whose instrument had just been asked to acquit a hill.»
2. **X.2** — line 29 (phrase limit: the whole of: vary; -2 words)
   - Find: «And at the step, having reported the whole of it:»
   - Replace with: «And at the step, having reported it all:»
3. **X.3** — line 41 (plainer voice: Marques plain; -6 words)
   - Find: «*Correlated stopping is not in the advisory, Doctor; neither is dying. I am sorry. Send the rest either way. — I.M.*»
   - Replace with: «*Correlated stopping isn't in the advisory. I'm sorry, Doctor. Send the rest anyway. — I.M.*»
4. **X.4** — line 43 (phrase limit: which was; -2 words)
   - Find: «and she did not argue with it, which was the first thing the hill had ever made her accept.»
   - Replace with: «and she did not argue with it: the first thing the hill had ever made her accept.»
5. **X.5** — line 43 (plainer voice: Marques plain; -3 words)
   - Find: «"A dead man's three are a grief. I am sorry, Doctor Vogel; grief is not a witness."»
   - Replace with: «"Three on a dead man's wrist is grief, not data. I'm sorry, Doctor Vogel."»
6. **X.6** — line 49 (plainer voice: Kaya Bey plain; -2 words)
   - Find: «Kaya Bey, for the record, aloud, observed that produce raised under oil-fired glass reads exactly this way — fossil carbon, he said, is the modern weather, and vegetables live in it — and the sentence fitted,»
   - Replace with: «Kaya Bey said, for the record, that greenhouse produce grown with oil-fired heating reads exactly this way — old carbon in the air, he said, gets into the vegetables — and the sentence fitted,»
7. **X.7** — line 51 (phrase limit: to the knuckle: cut; -6 words)
   - Find: «and filled the lamp at the fourth door to the knuckle of her thumb and pinched the wick true,»
   - Replace with: «and filled the lamp at the fourth door and pinched the wick true,»
8. **X.8** — line 57 (phrase limit: the whole of; which was; -2 words)
   - Find: «He heard her out with the whole of his attention, which was the most disquieting thing about him, and then he asked,»
   - Replace with: «He heard her out with all his attention — the most disquieting thing about him — and then he asked,»
9. **X.9** — line 69 (plainer voice: Priska plain; +2 words)
   - Find: «"The plain word doesn't certify a hill for sitting."»
   - Replace with: «"The plain word doesn't make the hill safe to sit in."»
10. **X.10** — line 71 (phrase limit: flat on the palm: cut; -4 words)
   - Find: «and laid the two drafts side by side, flat on the palm.»
   - Replace with: «and laid the two drafts side by side.»
11. **X.11** — line 73 (phrase limit: which was; +0 words)
   - Find: «and could not merge them, which was, she supposed, the finding.»
   - Replace with: «and could not merge them. That, she supposed, was the finding.»
12. **X.12** — line 77 (plainer voice: Seher plain; +0 words)
   - Find: «Or it comes, and I can no longer tell it from weather."»
   - Replace with: «Or it comes, and I can't tell it from weather any more."»
13. **X.13** — line 83 (phrase limit: the way she; -1 words)
   - Find: «she noted it the way she noted everything»
   - Replace with: «she noted it as she noted everything»
14. **X.14** — line 83 (length cut: trim; -15 words)
   - Find: « — she had watched the women since August; she knew what an office was —»
   - Replace with: nothing. The seam reads «…repeated office proves the thing it is about and it steadied her for the dark anyway,…».

### Chapter XI

File: `round-7/chapter-11.md`. 26 changes. 3,692 → **3,191** words (-501; `wc -w` 3,666 → 3,172).

Recep's price list (XI.6), the traffic correlation (XI.10) and the explanations routine (XI.8, XI.9, XI.11, XI.24) go. Slip 2 is here (XI.4). The knock first answered, Priska's recording on the ninth of June at 21:41 with the shaft timed at twenty against eighteen (XI:33), "five stars, finally an explanation", Melek's collapse, the transfer authorization dated the day before (XI:41), the ward, the lamp set down, the song, the confession, the burial, the notebook, the gate boy, the returned phrase, Seher's "It costs the question" and Nilay's first round all stay. Melek's words are untouched; XI.13 changes only the narration after her line. Recep's one spoken line ("Both. Inside is extra.") goes with the price list; the gate boy's speech is already everyday and is not changed.

1. **XI.1** — line 9 (phrase limit: the whole of: vary (letter); +0 words)
   - Find: «and that is the whole of the manner.»
   - Replace with: «and that is all the manner there is.»
2. **XI.2** — line 11 (phrase limit: first knuckle: vary (letter); -3 words)
   - Find: «*I filled it for her, to the first knuckle of her thumb, because hers was the knuckle»
   - Replace with: «*I filled it for her, by her own thumb, because hers was the knuckle»
3. **XI.3** — line 15 (phrase limit: follow past the lamp / I never do: cut (letter); -11 words)
   - Find: «and was carried up into the grey, and I did not follow past the lamp. I never do.*»
   - Replace with: «and was carried up into the grey.*»
4. **XI.4** — line 17 (slip 2 (sixty): slip 2; +0 words)
   - Find: «was hers for forty years before it was mine»
   - Replace with: «was hers for sixty years before it was mine»
5. **XI.5** — line 25 (length cut: trim; -21 words)
   - Find: « The frame had stopped being news by then and become infrastructure. The pin on the map was a fixture with reviews.»
   - Replace with: nothing. The seam reads «…two languages saying nothing either of them meant. Weekends put candles in jars along the mulberries,…».
6. **XI.6** — line 27 (length cut: Recep's price list; two breaths: cut; -41 words)
   - Cut the passage from «on the flat stone below the mulberries, politely, out of his aunt's» to «knocks with the flat of the hand, and two breaths of waiting.» (77 words).
   - Replace with: «on the flat stone below the mulberries, out of his aunt's sightline; in April he had the list laminated. The etiquette he gave away free: two knocks with the flat of the hand, and the wait.»
7. **XI.7** — line 29 (length cut: trim; -17 words)
   - Find: «and a clip of one of them did numbers that were a little sister to four million, and the fence»
   - Replace with: «and the fence»
8. **XI.8** — line 31 (explanations routine: routine: cut; which was; -57 words)
   - Cut the passage from «Nilay listed the explanations: the shaft's own tide, which breathed on a» to «the bread queue, without patting anyone's hand, which was the message entire:» (76 words).
   - Replace with: «The village had its own account, and Havva Nine delivered it at the bread queue, without patting anyone's hand:»
9. **XI.9** — line 33 (explanations routine: routine: one clause; -22 words)
   - Find: «She gave the explanations two honest days: the shaft's tide, which kept its own hours; the tuff letting go of the day's heat; the fan's mended bearing, which had form. None of them confessed.»
   - Replace with: «She gave the explanations two honest days, and none of them confessed.»
10. **XI.10** — line 35 (length cut: the traffic correlation: whole paragraph; -135 words)
   - Cut the passage from «Kaya Bey came up with a folder. He had tabulated the young» to «as a thing provoked, one reading the hill as a thing reported.» (135 words, and the blank line before it).
   - Replace with: nothing (the whole paragraph goes). The paragraph before ends «…she did not pretend otherwise in either direction.»; the next begins «By midsummer Recep's boy worked two tellings: the…».
11. **XI.11** — line 37 (explanations routine: routine: cut; -33 words)
   - Find: « What had done it — the company leaving with the courtesy, the courtesy cheapening past use, or the season turning — neither the file nor the queue said, and both had stopped asking.»
   - Replace with: nothing. The seam reads «…one another. The answers thinned the same season. The queue stood outside the fence and the…».
12. **XI.12** — line 41 (phrase limit: which was; -2 words)
   - Find: «and saw its date, which was the day before the kitchen floor,»
   - Replace with: «and saw its date: the day before the kitchen floor,»
13. **XI.13** — line 65 (phrase limit: to the knuckle: cut (narration; Melek's words unchanged); -3 words)
   - Find: «She filled the ninth lamp to the knuckle.»
   - Replace with: «She filled the ninth lamp.»
14. **XI.14** — line 73 (phrase limit: which was x2; -2 words)
   - Find: «and Nilay's mother's mouth moved with it, which was memory or which was the village,»
   - Replace with: «and Nilay's mother's mouth moved with it, from memory or from the village,»
15. **XI.15** — line 73 (phrase limit: the whole of: vary; -2 words)
   - Find: «and Nilay stood beside her for the whole of it,»
   - Replace with: «and Nilay stood beside her all through it,»
16. **XI.16** — line 73 (length cut: trim; -20 words)
   - Find: « The other sentence went round the graveside after, arriving everywhere like carried water: the room chooses the one who stays.»
   - Replace with: nothing. The seam reads «…the other anything, and the burial went on. Yusuf came up from Derinkuyu and stood at…».
17. **XI.17** — line 73 (phrase limit: which was; +0 words)
   - Find: «and left before the bread, which was its own attendance.»
   - Replace with: «and left before the bread, its own kind of attendance.»
18. **XI.18** — line 77 (phrase limit: which was; the whole of; -5 words)
   - Find: «The office had come to her by refusal, which was how offices moved there: what is given can be resented, and what is refused must be taken up, and the taking up is the whole of the training.»
   - Replace with: «The office had come to her by refusal, as offices moved there: what is given can be resented, and what is refused must be taken up, and the taking up is the training.»
19. **XI.19** — line 79 (phrase limit: manners: vary; +0 words)
   - Find: «but orders accrete manners the way hills accrete paths.»
   - Replace with: «but orders accrete customs the way hills accrete paths.»
20. **XI.20** — line 79 (phrase limit: which was; -7 words)
   - Find: «in the same body, which was, she supposed, the definition of a keeper that the county had arrived at.»
   - Replace with: «in the same body: the county's definition of a keeper, she supposed.»
21. **XI.21** — line 81 (phrase limit: two breaths: vary; -1 words)
   - Find: «and stood the two breaths entire, and nothing answered.»
   - Replace with: «and stood out the waiting, and nothing answered.»
22. **XI.22** — line 83 (phrase limit: the way it; -1 words)
   - Find: «The singing room took the song the way it took everything, sternum first.»
   - Replace with: «The singing room took the song as it took everything, sternum first.»
23. **XI.23** — line 89 (phrase limit: past the name (variant): cut; -5 words)
   - Find: «Then she answered, once, because that is the etiquette, and past the answer, nothing: "The singing room."»
   - Replace with: «Then she answered, once, because that is the etiquette: "The singing room."»
24. **XI.24** — line 91 (explanations routine: routine: one clause; -97 words)
   - Cut the passage from «She built the explanations on the climb, methodically. The room returns notes;» to «of them would carry the weight, and none of them would break.» (119 words).
   - Replace with: «She built the explanations on the climb, methodically, and none of them would carry the weight, and none of them would break.»
25. **XI.25** — line 93 (phrase limit: manners: vary; +0 words)
   - Find: «and knew the manners by heart.»
   - Replace with: «and knew the etiquette by heart.»
26. **XI.26** — line 103 (length cut: repeats IX:77; -16 words)
   - Find: «The wick she pinched with her nails, pinched and never cut; her nails were a committee where Melek's had been a decision, but the third pinch stood true.»
   - Replace with: «The wick she pinched with her nails; the third pinch stood true.»

### Chapter XII

File: `round-7/chapter-12.md`. 14 changes. 3,186 → **2,629** words (-557; `wc -w` 3,157 → 2,606).

The consultancy emails are cut to what "Four million includes the state" needs (XII.2): a consultancy asks for his files, offers to buy the recovered footage, and thanks a directorate in Ankara in a footer. The first email's date (the ninth of April, XII:33) stays, so Halden's letter of the tenth still arrives a day after it. "GNSS-denied environments" and the per diem go. Gülce, the channel taken down, the fourteen seconds ("recovered: 14 sec. watched: 0." and "*viewed: no*"), the figure measuring the threshold with its forearm, the woven print that reads old, and the lamp in Derinkuyu all stay. The gate boy's line (XII:95) and Kemal's mother (who has no spoken line) are unchanged.

1. **XII.1** — line 25 (length cut: trim; -13 words)
   - Find: «in a school notebook because his uncle distrusted any arithmetic that could not be checked by hand, and the phone stayed dark,»
   - Replace with: «in a school notebook, and the phone stayed dark,»
2. **XII.2** — line 27 (length cut: the consultancy emails, cut to what 'Four million includes the state' needs; -228 words)
   - Cut the passage from «The first came in April and the second in May, and they» to «hand: *received 9.iv; received 12.v; received 3.vi; received, paper, 19.vii; answered: 0.*» (297 words).
   - Replace with: «The first came in April, from a consultancy that was two surnames and an ampersand, Ankara and Düsseldorf, asking for his raw files and his logs at standard rates. In June they offered to buy the recovered footage outright, and thanked, in smaller type beneath the signature, a directorate in Ankara for its continued interest. In July one came on paper, to the house. He answered none of them.»
3. **XII.3** — line 33 (phrase limit: the way he; -6 words)
   - Find: «He laid the two dates side by side, the way he laid everything now.»
   - Replace with: «He laid the two dates side by side.»
4. **XII.4** — line 37 (explanations routine: routine: one clause; -32 words)
   - Find: «He spent an evening on the ordinary accounts, and they were good ones: a directorate in Ankara that talked, as directorates do, to whoever wrote to it by hand; a registry with friends; the Trust's young woman, still in the country. And under those, the other reading, the one that warmed:»
   - Replace with: «He spent an evening on the ordinary accounts, and under them found the other reading, the one that warmed:»
5. **XII.5** — line 37 (length cut: trim; -17 words)
   - Find: « He stopped needing to choose between them, and noticed that he had stopped, and filed the noticing.»
   - Replace with: nothing. The seam reads «…and both a kindness, and both something else. Some things you sign in April and only…».
6. **XII.6** — line 41 (length cut: trim; -13 words)
   - Find: «unsent since the Monday and Tuesday he had drafted it, a loaded thing in a drawer of a house with four million windows.»
   - Replace with: «unsent since the Monday and Tuesday he had drafted it.»
7. **XII.7** — line 47 (length cut: trim; -21 words)
   - Find: «He thought, before typing it, of gülce's column — four years of two o'clock, a ward or a bakery somewhere — and typed a second line after it,»
   - Replace with: «He typed a second line after it,»
8. **XII.8** — line 49 (length cut: trim; -23 words)
   - Find: « The platform had learned, at the end, to write like the Registrar — final, quiet, promising paperwork — without any of the reasons.»
   - Replace with: nothing. The seam reads «…undone. Your data will be prepared for download.* Fourteen days later, to the Tuesday, the link…».
9. **XII.9** — line 51 (length cut: trim; -16 words)
   - Find: «an uploading he had never asked for; error-checking keeps what memory loses, which is the whole difference between a server and a person.»
   - Replace with: «an uploading he had never asked for.»
10. **XII.10** — line 53 (length cut: trim (the dialogue at XII:67 keeps the tiebreaker); -73 words)
   - Cut the passage from «He did not play it. He sat with his finger over it» to «Tuesday, in the mood of an algorithm. There was the basin besides,» (82 words).
   - Replace with: «He did not play it. There was the basin,»
11. **XII.11** — line 77 (length cut: trim; -40 words)
   - Find: « Above the gate the duct's fan turned, six strokes to the minute, somewhere between a clock and a breeze; the spare meter had clicked like that at his hip all one season, and he had liked it, company being company.»
   - Replace with: nothing. The seam reads «…and the plan had an hour to spend. Inside the fence, on the flat by the…».
12. **XII.12** — line 85 (phrase limit: two breaths: cut; -4 words)
   - Find: «softly — and waited out the two breaths.»
   - Replace with: «softly — and waited.»
13. **XII.13** — line 97 (explanations routine: routine: one clause; -40 words)
   - Find: « Old dust under an overhang holds marks for weeks; the co-op wove those sandals; the age of a print in old dust was nothing a boy could date and nothing Yusuf could either — he had watched a wall of marks for a season and never once caught one admitting its age.»
   - Replace with: « Old dust under an overhang holds marks for weeks, he told himself.»
14. **XII.14** — line 103 (phrase limit: two breaths; first knuckle; the ritual done without being named in full; -31 words)
   - Cut the passage from «He knocked twice on the frame, with the flat of his hand,» to «and not pushed; near, and wait; and the wick came to it.» (83 words).
   - Replace with: «He knocked twice on the frame, and waited, and nothing answered. The oil went to the joint of his own thumb and no further — his thumb, the only one the rule had now. The second pinch stood true. The flame he carried cupped and low, and the wick came to it.»

### Chapter XIII

File: `round-7/chapter-13.md`. 26 changes. 3,529 → **3,006** words (-523; `wc -w` 3,503 → 2,990).

The List is cut to three lines (Saflieni, Dowth, Ayios Nikandros) and the drowned chapel to its strongest pieces: the lamp rowed out by boat (XIII:59, untouched) and the founder's unsent letter (XIII:73–79, untouched). The 1949 photograph (XIII:61–69), the Vigil of the Sealed Hour and its margin (XIII:83–92), the 1924 note (slip 1, XIII.11) and the sampling note "Was sorry" (XIII:47), the keepership sheet (XIII:39), and the passage where she stops at the closure and he supplies the hospital (XIII:100–108) all stay. **Change 3** is XIII.21, at the fourth hinge (XIII:110): Nilay says it, plainly, in two sentences that name only what the book has shown — the hours he kept on that hill on the fourth and fifth of September 1999 (the margin at IV:57), his advice that nobody go below the fourth door (the leaf of 7.ix.1999 at IV:71), and her mother's twenty-six years (the count the book uses until the anniversary; the Valletta evening is in the first days of September 2026, before the fourth). She adds no new fact and no guess about what he knew of Emre's fate; "the night my brother went down" is the ruling's own wording. Halden answers with the existing line, "You have kept excellent records," (XIII:112, untouched) and nothing else; the paragraph about the sentence's weight (XIII:114) stays as it is. "Nothing in that room had happened" (XIII:124) stays and still holds: nothing did.

1. **XIII.1** — line 27 (phrase limit: the way the; -1 words)
   - Find: «The dig closed the way the season closed in that country:»
   - Replace with: «The dig closed as the season closed in that country:»
2. **XIII.2** — line 27 (length cut: trim; -22 words)
   - Find: « The Ministry thanked the licensee in a paragraph, continued its order about the second door pending everything, and wished the village well.»
   - Replace with: nothing. The seam reads «…by letter, in the last week of August. Kemal's tractor took the last crates down on…».
3. **XIII.3** — line 27 (length cut: trim; -26 words)
   - Find: « Yusuf was in Derinkuyu, the phone dark; the stick slept on in the drawer with the two plans and the crossed-out count and the Ministry's letter.»
   - Replace with: nothing. The seam reads «…winter the duct was short and asked nothing. Nilay closed the site register herself, at the…».
4. **XIII.4** — line 29 (phrase limit: the whole of: cut; -3 words)
   - Find: «and between those two facts lay the whole of her year.»
   - Replace with: «and between those two facts lay her year.»
5. **XIII.5** — line 31 (length cut: ritual retold; -11 words)
   - Find: «off the Wall, and the pinch stood true on the second try most nights, and the gate boy,»
   - Replace with: «off the Wall, and the gate boy,»
6. **XIII.6** — line 35 (phrase limit: which was; -2 words)
   - Find: «at the hour of her arrival, which was the previous courtesy with the bookkeeping left showing.»
   - Replace with: «at the hour of her arrival: the previous courtesy, with the bookkeeping left showing.»
7. **XIII.7** — line 35 (length cut: repeats IV:51; -13 words)
   - Find: « He was grayer by nothing, dated and sound, the age of good paper.»
   - Replace with: nothing. The seam reads «…the previous courtesy with the bookkeeping left showing. He poured the tea with both hands and…».
8. **XIII.8** — line 35 (phrase limit: which was; -3 words)
   - Find: «and she noticed them the way one notices the cloth folded at the desk's corner, which was still keeping a thirty-year-old ring from happening again.»
   - Replace with: «and she noticed them as she noticed the cloth folded at the desk's corner, still keeping a thirty-year-old ring from happening again.»
9. **XIII.9** — line 39 (length cut: trim; -29 words)
   - Find: « Three institutions at one mouth of a hill, and none of them owning it — that, the sheet implied without saying, was the condition the Trust existed to preserve.»
   - Replace with: nothing. The seam reads «…the village's; the line to remain the Trust's. At the foot, where a date goes, the…».
10. **XIII.10** — line 45 (length cut: trim; -32 words)
   - Find: « She had expected the founder's hand and got it — the hard hand of the slip in her pocket — page after page of it, an old man's inventory of an idea.»
   - Replace with: nothing. The seam reads «…and above the words, small, the shelf-mark: *0*. The Kırk Oda notes of 1924 came first,…».
11. **XIII.11** — line 47 (slip 1 (watch): slip 1 (ruling's wording); +0 words)
   - Find: «*The keeper's clock retards one hour upon each night below;»
   - Replace with: «*The keeper's watch retards one hour upon each night below;»
12. **XIII.12** — line 47 (length cut: trim; -31 words)
   - Find: « Melek's grandmother, Melek's story, Melek's voice over the wicks — and under all of them, a century down, the founder's pen, which had heard it first and filed it as furniture.»
   - Replace with: nothing. The seam reads «…beat it and it walks. Nothing to record.* She turned the page, and there was the…».
13. **XIII.13** — line 49 (the List and the chapel: repeats III and IV; -12 words)
   - Find: «one to a page, forty and more, typescripts and hands aging down the stack, never varying by a word. And before them,»
   - Replace with: «one to a page, forty and more. And before them,»
14. **XIII.14** — line 51 (the List and the chapel: the List: the placard lines go; -15 words)
   - Find: «> *Newgrange — no lamp after 1974.*
> *Derinkuyu — date unknown; rock cannot testify.*»
   - Replace with: nothing. The seam reads «…line, some in the hard hand, some later: > *Ħal Saflieni — lower level, 1940: do…».
15. **XIII.15** — line 57 (the List and the chapel: the drowned chapel, cut to the boat; -46 words)
   - Cut the passage from «She was on the next site before she felt the page's temperature.» to «stopped mid-column, unreconciled, the way lines stop when whoever keeps them stops.» (99 words).
   - Replace with: « Ayios Nikandros had a folder: a drowned chapel, taken by the reservoir in '55; the founder's remittance counterfoils, ceasing in 1949; and the water authority's summer wage-lines, 1955 through 1961 — *fetched the lamp; set the lamp; paid* — paid by nobody the page named, and stopping mid-column after the summer of '61.»
16. **XIII.16** — line 71 (length cut: trim; -19 words)
   - Find: «The room accepted this the way rooms accepted him, without anyone being able to say afterward what had shifted. She read the letter instead,»
   - Replace with: «She read the letter instead,»
17. **XIII.17** — line 81 (the List and the chapel: the drowned chapel: routine paragraph; -93 words)
   - Cut the passage from «The keeping had continued — the List said *kept nightly*, and the» to «to. She could not choose between the two, and did not try.» (93 words, and the blank line before it).
   - Replace with: nothing (the whole paragraph goes). The paragraph before ends «…way to ask it whether it was satisfied.*»; the next begins «One thing more in the volume, and he…».
18. **XIII.18** — line 94 (explanations routine: routine: cut; -31 words)
   - Find: « She tried the explanations because her hands wanted work: an accomplice; the founder's own retrieval; a deposit never made where the depositor believed; a hoax with a timetable and excellent handwriting.»
   - Replace with: nothing. The seam reads «…seventy years. It would hold for seventy more. The annals did not record the item's name,…».
19. **XIII.19** — line 96 (length cut: trim; -27 words)
   - Find: «She had brought her own matters as one brings a purse into a market, meaning to spend carefully, and she found she had already taken them out.»
   - Replace with: nothing (the whole paragraph goes). The paragraph before ends «…comma, and the comma was the cruelest part.»; the next begins «"The calibration memorandum," she said. "Priska's certificate surfaced…».
20. **XIII.20** — line 98 (explanations routine: routine: one clause; which was; -39 words)
   - Cut the passage from «The explanations for that one stood in a row, worn smooth from» to «which was the property of the thing she minded most about it.» (61 words).
   - Replace with: « None of the explanations for that one had ever once required a villain, and that was what she minded most about it.»
21. **XIII.21** — line 110 (change 3: change 3; +21 words)
   - Find: «She knew it by heart. She set it down nowhere, and he did not pick it up, and between them, on the desk, it took up no room at all.»
   - Replace with (¶ = paragraph break, a blank line; the first part stays in the same paragraph as the words before it): «She knew it by heart, and this time she set it down.» ¶ «"You kept the hours on that hill on the fourth and fifth of September 1999, the night my brother went down. Then you wrote that nobody should go below the fourth door, and my mother has waited twenty-six years."»
22. **XIII.22** — line 130 (length cut: trim; -29 words)
   - Find: « The schoolteacher's mat was where the order allowed it, at the mouth, and the schoolteacher was on it. The gate boy came up with the key on its bootlace.»
   - Replace with: nothing. The seam reads «…its own silence with the mulberries going early. And inside the fence, along the second rail,…».
23. **XIII.23** — line 132 (length cut: the ritual is told again, in full, in XIV:15; -11 words)
   - Find: «She gave her name at the mouth, aloud, to nobody, first, and went down past the second door»
   - Replace with: «She went down past the second door»
24. **XIII.24** — line 132 (length cut: repeats IX:79; -15 words)
   - Find: «, past the Ninth Room's note finding her sternum like a doorman who knows the step,»
   - Replace with: «,»
25. **XIII.25** — line 132 (phrase limit: first knuckle: cut; -14 words)
   - Find: « The oil went to the first knuckle of her own thumb and no further.»
   - Replace with: nothing. The seam reads «…the nine niches and the black above them. The lamps were hers on trial, until they…».
26. **XIII.26** — line 132 (length cut: trim; -20 words)
   - Find: « The lamps were hers on trial, until they were not, and later, on the table above, the parcel would lie under the oilcloth notebook while the hill kept its evening.»
   - Replace with: « The lamps were hers on trial, until they were not.»

### Chapter XIV

File: `round-7/chapter-14.md`. 25 changes. 5,080 → **4,820** words (-260; `wc -w` 5,031 → 4,778).

Slip 3 (XIV.18), Emre's speech halved (XIV.17), one short paragraph of the boy (XIV.10), the bracketed aside removed (XIV.8), the new reason for the struck third sentence (XIV.20), and the phrase pass (the "the way" similes cluster here: 13 → 4). The ribbon, the reunion ("You filled the lamp badly, that night", "Nilay."), "I have never once had shoes", the grey man who took the light, the mother folding the ribbon, the certificate and the fingerprint note, "time travel" named and given back, Book Zero, the shaft's eighteen minutes, Göbekli and the rendering all stay. The sealed box's two sheets are left, as the ruling says. The coda letter (XIV:133–159) is not touched.

**The XIV items in full.**

- **The recognition moment (XIV.8).** The long bracketed aside about the name — «— three syllables, the middle one long; she had heard it twice before, once in the dark without knowing it, and once, knowing it, in a polished room, from a woman who measured doors, or had heard its grandmother, or its grandchild —» — is removed. The short aside before it ("she had said it once into another dark, and the humming had not changed") stays, because it is the echo of II:61–63 that the moment turns on. The beat now reads: «She said, "Emre," once — she had said it once into another dark, and the humming had not changed — and he said the name of the room first, because the manners are the manners, and past the name, nothing, and then he broke the office for the first time in twenty-seven of her years:» ¶ «"Nilay."»
- **The boy (XIV.10)**, a new paragraph after "I have never once had shoes, in all of it. The house never minded.": «Then he grinned, and for a moment the grin was thirteen. "Mother's going to kill me about the slippers. Did the kid ever come in?"» Both lines come from what the book has shown (the house slippers, II:47 and XIV:35; the kid that had not come in with the evening flock). The question is left unanswered, so nothing new is added about the kid. His next line ("I went up the first winter") follows unchanged. His "Mother" comes before Nilay tells him their mother is alive (XIV:51); that is deliberate: the reflex of a boy.
- **Emre's speech (XIV.17)**, from 133 words to 79. What stays, exactly: «"You've had it backwards. It isn't a door to anywhere. It's a road that's long instead of far. A place kept long enough is in all of its times at once. I never left, Nilay. I've been here since the summer I fell; it's only been longer for me. The ones below keep too, from farther than I've been, and not the way you're going. And you'll go farther back than any of us. The wall already says so."» It keeps "a road that's long instead of far" and the confirmation of time travel (a place "in all of its times at once"; "it's only been longer for me"; "you'll go farther back than any of us"). It keeps the far-future hint unprovable ("from farther than I've been, and not the way you're going"). It drops the lore ("Keeping is the thread. The rooms come when they're kept.", "From where, I couldn't tell you.", "We never asked each other; it isn't asked. I don't think any of us ever met anyone but each other."). His "I don't know the law … I know my road" and the naming of *time travel* (XIV:69–73) stay.
- **The handprint (XIV.18).** Cut «, which had always been hers, and which she would press, in her own farthest keeping, before there was a Wall to press it on» so that XIV:77 reads «She wet her right hand in the bowl and set her palm on the stone above the first marks, over the old print. The two prints sat together at the head of the counting, a thing and its shadow, and neither of them was first.» The certificate (XIV:109) and the fingerprint note (XIV:111) stay word for word, and the paper does the work.
- **The third sentence (XIV.20).** «She wrote a third, with two dates in it, the fourth and the fifth of September 1999, and struck it through, because she had said it once, to his face, and paper would only give him something to file.» Only the reason changes.
- **Also cut in XIV**, as repeats of lines told in full elsewhere: the niche described again (XIV.5), "The vigil was not announced. It was announced by being kept." (XIV.6, first at XI:43), the gloss "The office said what the office said …" (XIV.11), Emre's "asking is a lamp you hold up on somebody …" (XIV.13, from the II letter), "like a coal in both hands" (XIV.15, first at VIII:115), and the List's details in the post to Valletta (XIV.21; the chapel's payoff, "whatever keeping weighed, and whatever its ceasing had cost, was hers now to carry up the hill with the oil", stays).

1. **XIV.1** — line 3 (phrase limit: the way it; which was; -3 words)
   - Find: «and the village kept it the way it had kept it for twenty-seven years, which was by not keeping it:»
   - Replace with: «and the village kept it as it had kept it for twenty-seven years, by not keeping it:»
2. **XIV.2** — line 7 (phrase limit: the whole of: vary; -1 words)
   - Find: «At the table Nilay gave her the whole of the protocol and none of the reason,»
   - Replace with: «At the table Nilay gave her all of the protocol and none of the reason,»
3. **XIV.3** — line 13 (phrase limit: the whole of: vary; -3 words)
   - Find: «and pressed her initials into the seal, which is the whole of what a witness owns.»
   - Replace with: «and pressed her initials into the seal, which is all a witness owns.»
4. **XIV.4** — line 13 (plainer voice: Priska plain; -1 words)
   - Find: «"A witness's whole duty is the hour," she said,»
   - Replace with: «"The witness writes down the hour," she said,»
5. **XIV.5** — line 15 (phrase limit: to the knuckle: cut; the niche not re-described; -32 words)
   - Find: «She kept the round first, all nine, oil to the knuckle of her own thumb; the trial was the keeping, and the keeping came first. Then, at the shelf cut at the height of a heart, its back sooted black and shining, the stone to its left worn smooth to the height of hands, she laid the tin box»
   - Replace with: «She kept the round first, all nine; the trial was the keeping, and the keeping came first. Then, at the answering niche, she laid the tin box»
6. **XIV.6** — line 15 (phrase limit: past the name (variant): cut; repeats XI:43; -14 words)
   - Find: «and stood the two breaths entire, and past the breaths said nothing, there being nothing in the manner that wanted words. The vigil was not announced. It was announced by being kept. She sat»
   - Replace with: «and stood the two breaths entire, and said nothing, there being nothing in the manner that wanted words. She sat»
7. **XIV.7** — line 15 (phrase limit: the way a; -1 words)
   - Find: «and the dark was present the way a full room is present.»
   - Replace with: «and the dark was present as a full room is present.»
8. **XIV.8** — line 31 (bracketed aside: the bracketed aside removed; -43 words)
   - Find: «and he said the name of the room first — three syllables, the middle one long; she had heard it twice before, once in the dark without knowing it, and once, knowing it, in a polished room, from a woman who measured doors, or had heard its grandmother, or its grandchild — because the manners are the manners,»
   - Replace with: «and he said the name of the room first, because the manners are the manners,»
9. **XIV.9** — line 35 (phrase limit: the way it; -1 words)
   - Find: «the land cleared its throat, the way it did all that year,»
   - Replace with: «the land cleared its throat, as it did all that year,»
10. **XIV.10** — line 39 (Emre as the boy: Emre as the boy he was; +25 words)
   - Find: «"I have never once had shoes, in all of it. The house never minded."»
   - Replace with (¶ = paragraph break, a blank line; the first part stays in the same paragraph as the words before it): «"I have never once had shoes, in all of it. The house never minded."» ¶ «Then he grinned, and for a moment the grin was thirteen. "Mother's going to kill me about the slippers. Did the kid ever come in?"»
11. **XIV.11** — line 41 (length cut: explains the echo; -26 words)
   - Find: « The office said what the office said, through whoever held the oil; there was no test that could tell them apart, and there had never been.»
   - Replace with: nothing. The seam reads «…been Melek's, at the wicks, the June before. "There was a girl behind a stone once,"…».
12. **XIV.12** — line 43 (phrase limit: the way the; -1 words)
   - Find: «and hummed the way the keepers hummed for me»
   - Replace with: «and hummed like the keepers hummed for me»
13. **XIV.13** — line 57 (length cut: Emre plainer; -21 words)
   - Find: « We don't ask what's new, and we don't ask the year — asking is a lamp you hold up on somebody, and the dark down here has enough light put to it.»
   - Replace with: « We don't ask what's new, and we don't ask the year.»
14. **XIV.14** — line 57 (phrase limit: past the name: cut; -4 words)
   - Find: «The answer is the name of the room. Once. Past the name, nothing." He considered the flame.»
   - Replace with: «The answer is the name of the room. Once." He considered the flame.»
15. **XIV.15** — line 61 (length cut: repeats VIII:115; -15 words)
   - Find: « And Nilay carried that the rest of the way like a coal in both hands.»
   - Replace with: nothing. The seam reads «…believed it before I had a right to." Near the end — the lamp low, the…».
16. **XIV.16** — line 65 (phrase limit: the way the; -5 words)
   - Find: «He looked at the flame while he answered, the way the office answers.»
   - Replace with: «He looked at the flame while he answered.»
17. **XIV.17** — line 67 (Emre's speech: Emre's speech halved; -54 words)
   - Cut the passage from «"You've had it backwards. It isn't a door to anywhere. It's a» to «go farther back than any of us. The wall already says so."» (133 words).
   - Replace with: «"You've had it backwards. It isn't a door to anywhere. It's a road that's long instead of far. A place kept long enough is in all of its times at once. I never left, Nilay. I've been here since the summer I fell; it's only been longer for me. The ones below keep too, from farther than I've been, and not the way you're going. And you'll go farther back than any of us. The wall already says so."»
18. **XIV.18** — line 77 (slip 3 (handprint): slip 3: the narrated handprint line cut; -24 words)
   - Find: «over the old print, which had always been hers, and which she would press, in her own farthest keeping, before there was a Wall to press it on. The two prints»
   - Replace with: «over the old print. The two prints»
19. **XIV.19** — line 105 (phrase limit: the whole of: cut; -8 words)
   - Find: «and the mat kept her, and that was the whole of the colloquy.»
   - Replace with: «and the mat kept her.»
20. **XIV.20** — line 115 (change 3: change 3 in XIV: the new reason; +8 words)
   - Find: «and struck it through, because accusations want a court, and she had a hill.»
   - Replace with: «and struck it through, because she had said it once, to his face, and paper would only give him something to file.»
21. **XIV.21** — line 115 (length cut: trim: the List details go; the chapel's payoff (the cost of keeping is hers now) stays; -28 words)
   - Find: « The keepership sheet went in the same post, its date filled in; and with the lamps had come the List, and with the List its quiet line — kept nightly, quiet since 1961 — and the wage-line that stopped mid-column; whatever keeping weighed, and whatever its ceasing had cost, was hers now to carry up the hill with the oil.»
   - Replace with: « The keepership sheet went in the same post, its date filled in; whatever keeping weighed, and whatever its ceasing had cost, was hers now to carry up the hill with the oil.»
22. **XIV.22** — line 117 (phrase limit: the way the; -6 words)
   - Find: «one line, low, the way the wall is cut, and under the line wrote:»
   - Replace with: «one line, low, and under the line wrote:»
23. **XIV.23** — line 125 (phrase limit: the way she; -1 words)
   - Find: «the way she had wetted a thousand carved surfaces»
   - Replace with: «as she had wetted a thousand carved surfaces»
24. **XIV.24** — line 127 (phrase limit: the way she; -1 words)
   - Find: «notebook after notebook, the way she had rendered them for six years»
   - Replace with: «notebook after notebook, as she had rendered them for six years»
25. **XIV.25** — line 127 (phrase limit: to the knuckle: vary; +0 words)
   - Find: «a keeper, teaching a child to tend a lamp — oil to the knuckle, wick pinched true,»
   - Replace with: «a keeper, teaching a child to tend a lamp — the oil measured, the wick pinched true,»
## 4. The plant check

Every plant that any change in this plan touches is listed, first the ones the ruling names, then the others. "Touched by" gives the edits in or next to the passages that carry the plant. "Where it stands" says where each part of it is after the cuts. Nothing the ruling lists is lost.

**The plants the ruling names**

| Plant | Set up | Pays off | Touched by | Where it stands after the cuts |
|---|---|---|---|---|
| The air shaft's timing (18, 19, 20, back to 18) | I:71 (eighteen) | VI:63 (nineteen); XI:33 (Priska times twenty against Nilay's eighteen) and XI:105 (twenty); XIV:123 (eighteen) | XI.9 (the list earlier in XI:33) | All four refrain paragraphs untouched. XI:33 keeps "twenty minutes out, twenty in … said eighteen … did not average them". |
| 1,142.6 against 1,142.5 | III:55 | X:45 | III.10, III.11 (the triangle passages after it) | III:55 and X:45 untouched. |
| The three watches and where they are worn | III:31 (left wrist, "where the artery is closest"), III:69 | IX:51–57 (forty nanoseconds, twice), IX:79 (right wrist), X:35 (right wrist; 03:12 and 05:41; the third still agreeing with the sky), X:81 | III.18, IX.8, IX.16, X.3, X.5 | III:31, III:69, IX:55, IX:79, X:35 and X:81 untouched. IX:53 keeps 40.1 ns and the advisory in shorter form. Marques still names the committee of three (IX.8). |
| The margin note "4–5.ix. Kept the hours. A.H." | IV:57 | XIII:110 (now spoken by Nilay), XIV:37 ("It was in a margin in Valletta, with the date"), XIV:115 | IV.12 (same sentence, earlier clause only), XIII.21 | The margin note and "the only page in the volume with a day on it" untouched. XIV:37 and XIV:115 untouched. |
| The gendarmerie leaf of 6.ix and 7.ix.1999 | II:37 ("correspondence, Valletta, 7.ix.1999, 1 leaf — not reproduced"), IV:23 | IV:71 (both leaves), XIII:110 (the fourth hinge, now spoken), XIV:115 (the struck third sentence) | IV.1, XIII.21, XIV.20 | II:37 and IV:71 untouched. IV:23 keeps "a gendarmerie file listed a leaf from Valletta, of September 1999, and did not reproduce it". XIII:110 and XIV:115 carry the new wording. |
| The pigment phial | I:63 (item fifty-one), IV:73 | VIII:19 (the letter's "glass finger"), XIII:47 ("Took a finger's cup … Was sorry."), XIV:109 (the certificate), XIV:111 (the chit) | XIII.12, XIV.18 | IV:73, VIII:19, XIV:109 and XIV:111 untouched. XIII:47 keeps the sampling note and "Item fifty-one had been sorry". |
| The Saflieni shoe | IV:47 (the school party of 1940; "The Trust does not correct what it did not record."), IV:75–77 | IV:81–83; XIII:51–57 ("Ħal Saflieni — lower level, 1940: do not correct" and the guide's voice); XIV:39 ("never once had shoes") | IV.8–IV.11, XIII.13–XIII.15 | IV:75–83 untouched. IV:47 keeps the school party, "no list", and the Trust's reply. XIII keeps the Saflieni line and the guide's voice. |
| The coin and its foam | VIII:51 (Márton's statement) | VIII:133–139 (the circle in the foam empty); XIV:77 ("a coin paid for a lamp and gone from its foam") | VIII.21, VIII.22 | VIII:51, VIII:133, VIII:139 and XIV:77 untouched. VIII:135 keeps the stair-head lamp, the coin "cold as a key", and "either very worn or very new". |
| The camera found upright and wiped | VII:41 | VII:49; VIII:95 ("the camera standing wiped on its foot"); VIII:133 | none | Untouched. |
| Yusuf's fourteen seconds | VI:49 (the upload "from the copy the app had kept" failed at ninety-seven percent) | XII:51–69 (RECOVERABLE, 0:14, "recovered: 14 sec. watched: 0.", "*viewed: no*"); XIV:97 (the stick, put back unplayed) | XII.2 (the ninety-seven percent is no longer cited in the emails), XII.9, XII.10, XIII.3 | VI:49 untouched. XII:51 keeps the servers holding what the card had lost. XII:53 keeps the not-playing and "watched: 0". XII:57–69 and XIV:97 untouched. |
| The woven footprint | VI:47 (the recovered frame: "a sandal. Woven.") | VII:79 (the print of a woven sandal); XII:93–97 (the print at the threshold that reads old); XIV:39 ("woven things, boot-shaped") | VI.6, VII.19, XII.13 | VI:47 keeps the frame; VII:79, XII:93 and XIV:39 stand. XII:97 keeps "Rain deletes … He could not make the print read new". |
| The 1949 photograph | XIII:61 | XIII:63–69 ("The Trust has had two registrars." / "It does not record the recorders."); XIV:121 | XIII.15 (the chapel sentence before it), XIII.16 | XIII:61–69 untouched. |
| The Vigil of the Sealed Hour and its margin | XIII:83–92 | XIV:5–21 and XIV:85–97 | XIII.18 (after the margin) | XIII:83–92 untouched, including "[inked out]". XIV keeps the protocol step by step; only phrase changes (XIV.3–XIV.7). |
| The fourth hinge (7 September 1999) | IV:71 | XIII:110 | XIII.21 | "There was a fourth hinge, the oldest, in the same slope, dated the seventh of September 1999. She knew it by heart" stays; Nilay now speaks it. |
| The ribbon | II:51, II:65 | XIV:19 ("until the ribbon"), XIV:27, XIV:107 | none | Untouched. |
| "I have never once had shoes" | II:47 (house slippers), IV:75–77 (the child's shoe) | XIV:39 | XIV.10 (a new paragraph after it) | The line is untouched; the new boy lines follow it. |
| "The grandparents dug upward" | VIII:9, VIII:29 | the far keepers and the wall's marks (XIV:77, XIV:127) | VIII.1 (one phrase in the same letter) | VIII:9–13 and VIII:29 untouched. |
| Every italic letter that answers a scene; the early-dated letters | all fourteen letters | their scenes, before and after | only the phrase-limit edits II.1, III.1, V.1, VI.1, VI.2, VII.1, VII.2, VIII.1, IX.1, IX.2, XI.1–XI.3, and slip 2 (XI.4) | Every letter stays and none loses a sentence that answers a scene. The early-dated documents in the story also all stay: the consents dated April (I:59), Halden's letter to Yusuf dated the Tuesday (VI:53), the closure dated the fourteenth (VIII:129), the solstice grant dated the twenty-eighth (IX:31), the transfer dated the day before (XI:41), and Halden's letter of the tenth of April (XII:33). |
| The forty and forty-one rooms | I:61 | II:33 (1998's chamber), IV:113 ("say forty"), VI:31–45, the drawer (II:77, XII:69, XIV:97) | I.6, II.2, VI.4, VI.5 | I:61 keeps the crossed-out forty-one. VI:31 keeps the except-whens in pooled-air windows and the count in a mask. VI:33 keeps fourteen microgal. VI:43 keeps the forty-one on camera. |
| The humming | II:15 (the letter), II:59 | II:63, II:77, XIV:43–49 | II.4, II.5, XIV.12 (phrase changes only) | All stand. |

**Other plants touched by the cuts**

| Plant | Set up | Pays off | Touched by | Where it stands |
|---|---|---|---|---|
| The grandmother's watch (slip 1) | I:57 | III:95, IV:115, XIII:47 | I.3, I.4, III.20, IV.15, XIII.11 | A pocket watch she carried down, in all four places. |
| Márton refuses to average | III:59 | XI:33 ("having learned that from a better man") | III.11 | Kept inside III.11's replacement. |
| Room 9, the singing room, the low A | III:67, the IV letter | IV:45 (the same note in Malta), IV:111–113, IX:39, IX:79, XI:83 | III.15, III.16, IX.9, IX.10, XI.22, XIII.24 | III:67 keeps Room 9 and the hertz. IV:45 untouched. IX:79 keeps "like a doorman who knows the step" (XIII's repeat goes). |
| The tripod below the fourth door | III:67 ("not a night past the first cloud") | IV:93–103 | III.16 (the sentence after it) | Melek's condition and IV:93–103 untouched. |
| Priska's forks column | IX:59 | X:73 | none (a kept instance of the routine) | Untouched. |
| The calibration splinter | V:87 | X:39 ("Considered indicative"), XIII:98 | V.19–V.21, XIII.20 | V:87 keeps the Trust's page, "*considered indicative*", and "Someone had read her report more closely than the Ministry had … only the number's provenance". X:39 untouched. XIII:98 keeps the memorandum and "never once required a villain". |
| The Hittite word | VII:63 (three syllables; "not calling; naming") | VIII:99 (*you-who-are*; "late, and wrong, or early, and right"); XIV:31 (the aside) | VIII.6, VIII.7, XIV.8 | VII:63 untouched. VIII:99 keeps both hints. The XIV aside goes, as ordered; the tie between the word and "the name of the room" now rests on VII:63 and the VII letter ("They give the name of their room"). |
| Márton's solstice application | VIII:131 | IX:31 | VIII.18 (just before it) | Both untouched. |
| Seher's minutes | VIII:117 | IX:31 ("Seher's minute had recorded the intention") | VIII.17, VIII.18 | VIII:117 keeps "Seher took the minutes". |
| The monk who kept the undercroft | III:89 | IX:67 (the stringer's note) | III.19, IX.21 | Both stand. |
| "For your peace" | IX:67 | X:73 | IX.21 | Both untouched. |
| Göbekli and the oldest open question | I:41 | XIII:79 ("one buried hill"), XIV:109, XIV:125 | none | Untouched. |
| The drowned chapel | XIII:57–59 | XIII:79 (the founder's letter), XIV:115 | XIII.15, XIII.17, XIV.21 | The boat (XIII:59) and the letter stand. XIV keeps "whatever keeping weighed, and whatever its ceasing had cost, was hers now to carry up the hill with the oil". |
| The lamp-jars along the mulberries | XI:25 | XIII:130 (the grey figure sets one upright) | XI.5, XIII.22 | Both stand. |
| "Before first frost" | XI:75 | XIII:31, XIII:132, XIV:3 | XIII.5, XIII.26 | All stand. |
| The consents dated April | I:59 | IV:69; XII:37 ("Some things you sign in April and only find out in June.") | I.5, IV.13, XII.4 | All stand. |
| The Trust's young woman | I:59 | VI:55, XII:37 | VI.9, XII.4 | Stands at I:59 and VI:55 (as the one ordinary account); XII:37 no longer names her. |
| The two leaves copied on the plane | IV:115 | VIII:121 | VIII.18 | The VIII echo goes with the committee exchange; IV:115 stands. (Section 5.) |
| The stick in the drawer | XII:69 | XIV:97 | XIII.3 (a mention between them) | Both stand. |
| Kaya Bey's hermits | VII:85 | VIII:119 | XI.8, XI.24 (later mentions) | VII:85 and VIII:119 stand. |
| The answering niche | V:35 | VIII:111, XIII:89 ("the niche that answers"), XIV:15 | XIV.5 | XIV:15 now says "at the answering niche" instead of describing it again. |
| The Trust's founding, 1923 | VIII:123 (the reply) | XIII:39 ("since 1923") | VIII.18 | XIII:39 stands on its own; I:37 ("a foundation older than the republic") still dates the Trust. |

## 5. What I could not plan exactly as the ruling suggests, and why

1. **The suggested chapter targets.** The book lands at 45,788 words (45,434 by `wc -w`), inside the ordered range of 44,500–46,000 and 8.6% shorter. That is about a thousand words above the suggested targets (44,800), and each block is over its suggested total by more than the 200 words the ruling lets me move (A +304, B +126, C +558). Section 1 says where the gap comes from. In short: the phrase-pass chapters give little, and XIII and XIV are mostly plants and protected passages. I preferred the smallest changes that meet the ordered range. If the main session wants the book nearer 44,800, these are the next cuts I would make, in this order. None is in the plan, and together they come to about 450 words (the book would then be about 45,340):
   - R1. XIV:129, «she had known that for six years and had never before had to know what it meant» (17).
   - R2. IX:65, «though he had a memory of feeding that preprint to a wastebasket in Uppsala — the wastebasket had evidently been emptied into an archive; everything is, eventually» (27).
   - R3. VIII:99, Demircioğlu's first sentence, «Of your four spellings … introduced to each other prematurely.» (24).
   - R4. VII:83, «The word had a family feeling she could not place, chalk and grammar, a lecture hall with the windows open. She did not trust the feeling.» (26).
   - R5. XIII:73, the founder's salutation paragraph (31).
   - R6. III:79–81, Yusuf's "Forty years of nothing" line and "Everybody laughed…" (59).
   - R7. XII:41, from «He had held the channel for four years.» to «either shut or open.» (59).
   - R8. X:83, from «Each evening at the same hour» to «every evening, at the same hour.» (54).
   - R9. V:71, the paragraph of twenty-seven accounts (71). This would take one "manners" KEEP with it, leaving 11.
   - R10. VI:29, Yusuf's and Seher's disagreement about who first said the low way was older (81). This is a last resort: it is one of the parallel-build hints.
2. **IV's "list of sites that reads 'like a museum placard'."** There is no such list in IV. The reader (file 37) meant the Trust's List in XIII (Newgrange, Dowth, Derinkuyu). It is cut there (XIII.14), and IV's cut comes from the first half of Malta alone.
3. **The explanations routine starts before IV.** The ruling calls IV (the Saflieni shoe) the first time, but the same routine is already at I:61, II:33 and II:69. I kept II:69 as one of the three "other places": it is the first hint of the dead, and the concept needs it. I reduced I:61 to one clause and cut the list at II:33, where the chapter's existing clause ("There was nothing in any of it that a tired surveyor and an Ankara office could not account for between them") already does the work. II:33 is therefore a small content cut in a chapter the ruling marks "phrase pass only". I judged it part of change 1 (the routine), not a new cut. If the main session disagrees, restoring II.2 adds 85 words and makes II the one chapter with two kept routines before IV.
4. **The committee exchange in VIII (VIII.18).** Cutting the Ministry's question "who elected the Trust?" and the Trust's reply is the largest judgment call in the plan. The ruling names the committee as VIII's cut, and this is the committee's longest stretch. The Registrar's annex (VIII:127) stays as the Trust's one voice there. The cost is a good Halden reply ("the record is the mandate") and the small VIII echo of the two leaves copied on the plane. If the main session wants the exchange kept, drop VIII.18 and VIII.19 (+195 words; the book is then 45,983, still inside the range, but only just).
5. **Change 3's wording.** "The night my brother went down" is the ruling's own phrase. If it reads as a guess that Emre went below, which the book confirms only in XIV, the safe alternative is "the night my brother went missing". "Twenty-six years" is right for the evening in Valletta: it falls in the first days of September 2026, before the twenty-seventh anniversary on the fourth, and XIV's "twenty-seven" comes after it. The two sentences add no fact and no guess about what Halden knew. Halden's answer and manner are unchanged.
6. **Counting three of the limits.** For "to the knuckle" / "first knuckle", "follow past the lamp" and "past the name, nothing", my counts differ slightly from the ruling's (section 2 explains how). The planned KEEPs meet the limits under either count.
7. **Voices with nothing to change.** Nilay's mother (already short and tart), the gate boy (his one line is already everyday), and Kemal's mother (who has no spoken line) are unchanged. Recep's one line goes with the price list. Two speakers are not on the ruling's list: Mrs. Vella (IV) is trimmed only as travelogue, and her story and the Trust's reply stay; Demircioğlu (VIII) loses two sentences for length. Márton's confession (III:87–93) keeps everything but the too-pleased clause, and his last descent and death (IX:77–79, X:29–37) are untouched.
8. **Side effects on leftovers the critics flagged.** Two ordered cuts happen to remove two old leftovers: V.9 removes the first copy of the sitting-night tally (the full statement stays at V:69), and XII.2 removes the XII sentence whose verb had no object. Neither was a target. Everything else the ruling leaves is left: the chapter titles; the "two nights" letter; the wrists and stopped times; the sealed box's two sheets; Halden's nature; naming "time travel"; the early-dated letters; Leyla Hanım's death. So are two small things readers noticed that the ruling did not order: the present tense at II:67 ("Nilay has never asked her directly") and "the little knife from Melek's oilcloth" at XIV:117.

## 6. The main session's decisions on this plan (these override everything above)

The main Claude session, the final authority, checked this plan before any reviser started. It counted every phrase limit, the protected plants and the word total in a copy with every edit applied, and read every larger cut and every new line in context. The plan stands, with three changes. Revisers make these exactly, as if they were in section 3.

1. **VIII.18 and VIII.19 are NOT made.** The Ministry's question "who elected the Trust?" and the Trust's reply stay. They are the one place the book asks the Trust's authority to account for itself, and the reply ("the record is the mandate") and the room's satisfaction show Halden's institution at its most untouchable, which the concept needs.
   - Instead make only this, as **VIII.18a** (line 119): Find «The statements were tabled and not read aloud, their contradictions standing in the file like a survey that refused to close.» Replace with «The statements were tabled and not read aloud.»
   - Everything else from «Kaya Bey restated the hermits» to «*resolved,* which was accurate in every respect but the ones that count.» stays word for word. VIII:127's «and Kaya Bey read that too, more slowly,» stays as it is, because "too" again has something to refer to.
   - The phrase ledger gains back one "which was" (20 in all, within the limit of 29) and nothing else.
2. **XIII.21: "went down" becomes "went missing".** The planner rightly flagged that "the night my brother went down" could read as a guess about where Emre went, which the book confirms only in XIV. Nilay's line is therefore: «"You kept the hours on that hill on the fourth and fifth of September 1999, the night my brother went missing. Then you wrote that nobody should go below the fourth door, and my mother has waited twenty-six years."»
3. **One of the optional cuts in section 5 is made, R1, as XIV.R1** (line 129). This keeps the book safely inside the range with the committee exchange restored. Find «half what the hand did while the eye counted; she had known that for six years and had never before had to know what it meant.» Replace with «half what the hand did while the eye counted.»
   - R2 is **not** made. The wastebasket in Uppsala "emptied into an archive" is the Trust's reach into Márton's past, and it stays.
   - No other optional cut is made.

**The book then comes to 45,953 words by the ruling's count, 8.3% shorter** (counted in a copy with every edit applied).

The main session also accepts:
- the cut of the explanations list at II:33 (section 5, point 3);
- the planner's counting of the three phrase families (point 6);
- its handling of the voices that had nothing to change (point 7).
