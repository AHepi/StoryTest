# Critique, draft round 1: density of the middle, and continuity

*Stage 08, round 1. One critic, one kind of problem: whether the middle (chapters 5 to 9) is lighter to read in draft 2, and whether the cuts and additions keep the story continuous and its plot unchanged. Written by an agent that did not make draft 2. Compared: `stages/07-dialogue/output/unseen-orchard/draft-v1-part1..3.md` against `draft-v2-part1..3.md`, against `stages/01-brief-and-premise/output/unseen-orchard/brief-v1.md` and `request.md`. [from: 08; brief-v1; draft-v1; draft-v2]*

## Overall judgement

The middle is shorter (chapters 5 to 9: 5,409 words in draft 1, 4,795 in draft 2, an 11% cut; chapter 7 grew by 153 words) and some of it does read lighter, chiefly the bargaining scene in chapter 5 and the household scene in chapter 6. But the cuts took many of the small human beats that let a reader breathe, while most of the terms and procedure stayed, and four new "felt presence" passages were added to chapters 6 to 9. So the middle is shorter, but in places no lighter.
Two cuts in chapter 9 removed facts that chapter 10 still depends on. The additions bring in one broken world rule and one contradiction. No event, decision or outcome of the plot has changed.

How the comparison was made: both drafts read in full; chapter word counts by a short script (`awk` over the chapter headings); `diff` run on chapters 10 to 12 and part 1 to see exactly what was added there; `grep` for the terms and repeated images named below. Not checked: the revision log that draft 2's header points to (`stages/09-revision/output/unseen-orchard/revision-log-draft-round-1.md`). **That file does not exist**: the folder holds only `feedback-1.md`. Also not checked: `world-v1`, the world document draft 2 cites, so where a finding may come from it, it says so.

## Findings, most important first

### 1. The cuts took the breathing beats; the procedure stayed

- **Target:** chapters 5, 6 and 8 of draft 2. Still there, for example: ch. 5, "His branch would name the expedition's commander. Orra would keep her title and the household duties that came with it" / "Those duties include the guarantees" / "They belong to the head of the House"; ch. 5, the new one-sentence list "direct wages for every worker on a lot; inspection rights in her own name; a first extension on the guarantee that depended on accepted deliveries, not on any military result"; ch. 6, "The Berth Council had admitted the Serrat agents, and its fabrication owners had won recognition of property claims disputed for years. The guards now carried both sets of instructions." Cut: ch. 5, "The attendant moved her tool case without asking, and she made him move it back"; ch. 6, "You'd think I'd know how wide a door was", "Nessa pulled the needle through", "By evening the irregular knock in the pipes had stopped"; ch. 8, the chair Nessa holds and then lets go, and the trolley wheel squeaking in the corridor.
- **What is wrong:** the reader still has to hold the same runs of institutional terms, but has lost the light, concrete beats that broke them up. And the chapter 5 terms have been packed into one long sentence, which is denser to read than the dialogue it replaced.
- **Grounds:** the writer's words, "The middle is too dense" (request.md), which ask for a lighter read, not only a shorter one. Implied World theory, principle 2, attention budget (`sources/implied-world-theory.md`): every term spends the attention plot and character need. Principles 4 and 5, indifference and surplus: details like the trolley wheel or the mended shirt are what make the world feel lived in, and they cost the reader almost no effort.
- **Suggested fix:** in ch. 5, cut the House succession exchange down to the offer and Orra's refusal ("He offered to pay for everything if his branch could name the commander. Orra said no, in writing, while he watched"), and drop "household duties", "head of the House" and "My father accepted them with command". Give back two of the bargaining lines as speech ("Direct wages." / "Inspection rights. For me.") and drop the guarantee-extension clause, which no later chapter uses directly. In ch. 6, drop the Berth Council sentence down to "The guards now carried two sets of instructions." Restore two or three of the cut beats: the door joke, the needle, the chair. **Cost:** about 60 words back in; the uncle's branch politics go (no later chapter uses them); the theme of succession duties goes thinner.
- **Standing:** bears.
- **Where it came from:** this output only (stage 09, round 1).
- **Reply check:** flip: I would not be as sure that cutting the beats and keeping the terms made it lighter. Swap: names this draft's own lines. Survives both.

### 2. "The shop" and its spare rigs: cut in ch. 9, still relied on in chs. 9 to 11

- **Target:** ch. 9, draft 2. Draft 1's "Surety had eight more rigs, in the shop they were trying to capture" is cut, but draft 2 still has "The woman with the yellow cord moved two names from the shop party to the junction party. 'Then we don't stop at the racks.'" Ch. 10 still reasons from it: "Her inspection survey showed the shop three compartments farther in, beyond the portable frame's steering reach even empty."
- **What is wrong:** the reader is never told that the shop is a target or why it matters (spare rigs: the means to bring more people across), so "shop party", "the racks" and the chapter 10 reasoning have nothing to stand on until chapter 11 explains the shop after the event.
- **Grounds:** Implied World theory, the medium corollary: "In a book, nothing exists until it's named." Draft 1, ch. 9, set this up; brief-v1, A1, allows cuts to pay for the lore, not cuts that a later passage needs.
- **Suggested fix:** put back one sentence before the junction paragraph: "Surety carried eight more rigs, in the cartridge shop; take the shop and Nearbank could send people instead of messages." **Cost:** about 20 words in the middle.
- **Standing:** bears.
- **Where it came from:** this output only.
- **Reply check:** flip: no; the line is dangling as written. Swap: specific. Survives.

### 3. The drone rescue course: its setup cut in ch. 9, still used in ch. 10

- **Target:** ch. 10 (unchanged from draft 1): "The night pilot brought up the alternative drone course and then closed it. He had seen the same result she had." Draft 1, ch. 9, set it up: "Their small drones could not make the rendezvous in anything like the same time, even before carrying a person became the question." Draft 2, ch. 9, cuts that and keeps only "Twenty kilometres. Wren could cover it; they had stored a course when the outstation was established."
- **What is wrong:** at the story's main decision the reader meets an "alternative drone course" never mentioned before. Its quick dismissal used to be a closed door the reader had already seen; now it is a puzzle in the middle of the climax.
- **Grounds:** draft 1, ch. 9, and the medium corollary, as in finding 2. Chapter 10 is the decision the whole story turns on (brief-v1: the plot stays), so a reader caught on an unexplained option there is the costliest place to lose one.
- **Suggested fix:** restore the draft 1 sentence after "Wren could cover it": "Their small drones could not, and none could carry a person." **Cost:** about 12 words.
- **Standing:** bears.
- **Where it came from:** this output only.
- **Reply check:** survives both.

### 4. *Patience* breaks the story's own crossing rule

- **Target:** ch. 7, draft 2 (new): the pilot's account of *Patience*, "where the receiving bay had filled before its people arrived. They had come through into rock and into the hull's own frame."
- **What is wrong:** chapter 3 sets the rule that "the frame would test for obstructing mass before settling on either side" and take its abort point if the space has filled, and chapter 7 has just shown that rule saving Nessa ("OBSTRUCTED... Her frame had taken the plotted abort"). People arriving inside rock contradicts it, two pages after the rule worked.
- **Grounds:** Implied World theory, principle 3, ripple, and the story's own ch. 3 and ch. 7. A rule the reader has just watched work cannot fail silently in the next scene without some reason given. Brief-v1: lore may give a moment a second meaning but not change what happens, and here the lore changes what the frame can do.
- **Suggested fix:** one clause that keeps the rule: "from the years before frames checked for mass", or "their abort points had filled too". **Cost:** about 8 words; the horror stays, and it gains history (this is how the check came to exist).
- **Standing:** bears.
- **Where it came from:** this output only, unless `world-v1` sets *Patience* up this way (not checked).
- **Reply check:** flip: I would not be as sure that the rule allows it. Swap: specific. Survives.

### 5. Four presence passages in four chapters of the middle

- **Target:** draft 2, ch. 6, "as if it had been opened from a side and someone were looking in at all of it together"; ch. 7, the long "She saw herself" passage; ch. 8, "of being turned, gently, by something that did not touch her, until she could see the side of herself she had kept towards the wall"; ch. 9, "the sense of the galley door open from a side she could not face, and all twelve of them in view at once". Chapter 9 also gains a new gravimeter-log scene. Chapter 10's passage then lists them all again: "as it had been in the field, and in the assay room, and at the galley door".
- **What is wrong:** the middle the writer called dense now carries a recurring passage in nearly every chapter, written in the same words each time ("from a side", "at once", "nothing in front of anything else"; "at once" goes from 3 uses in draft 1 to 6). That adds a new kind of density, and it weakens the chapter 7 and chapter 10 peaks by repeating them in advance.
- **Grounds:** request: the spiritual element is "particularly announced" in despair, uncertainty and quiet decisions with loud consequences. The writer asked for these moments, but how often they come is the writer's call. Implied World theory, principle 2 (attention budget) and principle 6 (iceberg ratio: depth comes from what is sensed, not from how much is shown).
- **Suggested fix:** keep ch. 6 (a quiet decision with loud consequences) and ch. 7 (despair). Cut the ch. 8 passage (Dema's question already does that work) and cut the ch. 9 galley passage down to one sentence ("She heard herself say it."). Chapter 10's list then becomes "as it had been in the field, and in the assay room". **Cost:** about 110 words out of the middle; the presence comes up twice rather than four times before the climax.
- **Standing:** held if the writer wants the presence quiet and rare. If the writer wants it felt at every hard choice, keep all four, but vary the wording so that each passage reads as new. Writer: which?
- **Where it came from:** this output, or `world-v1` if it fixes how often the presence appears (not checked).
- **Reply check:** flip: I would not be as sure of the opposite (that four times is right), but that depends on an aim, so it is held. Swap: names this draft's own passages. Survives.

### 6. "Move the drum": one drum, where the story has four

- **Target:** ch. 8, draft 2: "Nearbank's tugs would move the drum, all four reception axes at once". Draft 1 had "Sava pointed to the four drum tracks."
- **What is wrong:** Nearbank has four drums (ch. 2, "a spindly tug turning between four larger structures"; ch. 11, "chosen by the drums' emergency meetings"; ch. 12, "the dark curve of a drum"), but the new sentence describes one drum with four axes.
- **Grounds:** draft 2's own chapters 2, 11 and 12; draft 1, ch. 8.
- **Suggested fix:** "Nearbank's tugs would move all four drums at once, and every arrival the occupiers had plotted would become a bad guess." **Cost:** none.
- **Standing:** bears.
- **Where it came from:** this output only.
- **Reply check:** survives both.

### 7. The gravimeter log holds a reading it could not have taken

- **Target:** ch. 9, draft 2 (new scene): the log is "Wren's own interior: a list of times, each with a small mass and a place on the ship where nothing stood", yet it includes one entry "from the dispatch station on Nearbank... the minute she had selected Tomas's list".
- **What is wrong:** Wren's gravimeter cannot log a mass inside Nearbank's dispatch station, and nothing says why Nearbank's station records would hold gravimeter readings or how the pilot came to have them. A second, smaller slip: in ch. 2 the gravimeter "had nothing left to measure" while the mass they had come to survey was still there.
- **Grounds:** draft 2, ch. 9, the scene's own first sentence; ch. 1 and ch. 2 (the gravimeter measures masses outside the hull).
- **Suggested fix:** either drop the Nearbank entry (the ch. 2 entry, "a little behind her chair", is enough to make the point), or say the pilot had asked Nearbank's station for its own instrument record and added it to his list. In ch. 2, "which had nothing left to measure" can become "which had been idle since the crossing". **Cost:** the first option loses the link to her decision in ch. 6; the second adds about 15 words.
- **Standing:** bears.
- **Where it came from:** this output only.
- **Reply check:** survives both.

### 8. Linet is not placed in the ch. 7 common room

- **Target:** ch. 7, draft 2. Draft 1's "Linet followed with a box of repaired instruments" and "Nessa followed Linet and Dema towards the packed tables" are cut. Linet first appears in the chapter as "By the time she freed it Linet was beyond the next bend with Dema and the instrument box".
- **What is wrong:** the reader does not know Linet was in the room, and "the instrument box" has no box introduced before it. Yet the chapter's emotional hinge is the two of them being separated ("Linet," she said eventually. / "No word.").
- **Grounds:** draft 1, ch. 7; the medium corollary.
- **Suggested fix:** restore "Linet followed with a box of repaired instruments" in the opening paragraph. **Cost:** 7 words.
- **Standing:** bears.
- **Where it came from:** this output only.
- **Reply check:** survives both.

### 9. Chapter 6 cuts left three loose ends

- **Target:** ch. 6, draft 2: "Her daughter waited outside the partition" (the partition is never introduced: draft 1's "Through a transparent partition, a young man rotated an insert" is cut); "'They do,' said the purchaser" (draft 1's "Nessa sat beside the shipment purchaser" is cut); "That does not qualify her as a witness" now follows the adjudicator's own action, not Dema's "She's free. Her parents were free.", so it answers nothing.
- **What is wrong:** a reader has to guess who the purchaser is and what the adjudicator is replying to.
- **Grounds:** draft 1, ch. 6; the medium corollary.
- **Suggested fix:** give back "Nessa sat beside the shipment purchaser" (6 words); change "outside the partition" to "outside the glass"; put back Dema's "She's free. Her parents were free." before the adjudicator's line (7 words). **Cost:** about 15 words.
- **Standing:** bears.
- **Where it came from:** this output only.
- **Reply check:** survives both.

### 10. Two words used for a second thing, and a quote-mark slip

- **Target:** (a) ch. 10, "Tomas on his stopped frame": the story's "frame" means the crossing rig, so this reads as Tomas standing on a rig, not as a paused picture. (b) ch. 10, "Turned people had planted it": the story's word for this is "reversed" (ch. 3, "Her return had reversed her"). (c) ch. 2, the new Linet lines use straight quote marks ("Drift. It does that after a crossing.") where every other line uses curly ones.
- **What is wrong:** (a) and (b) give one thing two names, or one name two meanings, in passages a reader takes slowly. (c) is a visible typing slip.
- **Grounds:** draft 1's consistent use of "frame" and "reversed"; `grep` found "turned people" only in the ch. 10 addition, and straight quotes only in ch. 2, lines 171 to 175 of part 1.
- **Suggested fix:** "Tomas, still on the paused screen"; "Reversed people had planted it"; curly quotes throughout. **Cost:** none, unless "turned" is meant as the crossers' own slang. In that case one line should show it as slang, such as Linet's "Looked at" in ch. 3.
- **Standing:** bears (b is held if "turned" is meant as the crossers' slang).
- **Where it came from:** this output only.
- **Reply check:** survives both.

### 11. Nessa's one protest before she signs is cut

- **Target:** ch. 6, draft 2. Cut: Nessa's "You accepted her berth guarantee", the adjudicator's "This is testimony", and Dema's "Whose consent did she need to be born?"
- **What is wrong:** in draft 1 Nessa pushes back once before giving in; in draft 2 she says nothing until her wage question, so she reads as more complicit. Chapters 8 and 10 then show her refusing and choosing, and they mean more if chapter 6 has already shown her trying and failing. The cut also loses the chapter's sharpest line. In draft 2's ch. 5 the agreement already gives "direct wages for every worker on a lot", so her ch. 6 wage question now confirms something the reader has just been told, where in draft 1 it was a small act of securing.
- **Grounds:** brief-v1, the plot stays: no decision may change, and Nessa still signs, so this does not break the plot. But it changes how her decision reads, and that is the writer's to choose. Request: "The plot is fine."
- **Suggested fix:** restore the three lines (about 25 words); in ch. 5, write "direct wages" without "for every worker on a lot". **Cost:** 25 words back into the densest chapter.
- **Standing:** held if the writer wants Nessa's slide in ch. 6 to be one of silent compliance (keep draft 2) or of resistance that fails (restore). Writer: which?
- **Where it came from:** this output only.
- **Reply check:** flip: held, since it depends on the writer's aim. Swap: specific. Survives.

### 12. How does a Nearbank guard know the pilot?

- **Target:** ch. 12, draft 2 (new): "The guard had said something about him; Nearbank had a word for men like that."
- **What is wrong:** the pilot is a home-side contract hand taken on at Surety (ch. 5), and his search took place three crossings away. Nothing shows how a Nearbank guard would know of him.
- **Grounds:** draft 2, ch. 5 and ch. 7; nothing in chapters 8 to 11 puts the pilot on Nearbank.
- **Suggested fix:** make it general: "The guard had said something about pilots who went looking; Nearbank had a word for men like that." **Cost:** none.
- **Standing:** does not bear yet. If `world-v1` makes the pilot known at Nearbank (not checked), the line stands as it is.
- **Where it came from:** this output, or `world-v1`.
- **Reply check:** survives both.

## Dropped in the reply check

- *The ch. 7 hold is longer than the 18-second field allowance.* Dropped. The text says the hold was "longer than any crossing she had made", and a crossing uses six seconds, so it fits inside the rule. I would be about as sure of the opposite reading.
- *The blue cup "set at the empty place" (ch. 7) that the child then carries out.* Dropped. It reads as a deliberate second meaning (the child taking the empty place's cup), not as a slip. I could not say it was wrong.
- *Draft 2 cuts the shipping intermediary's exemption (ch. 6), an event.* Dropped as a plot change. Cutting a minor event that nothing later relies on changes no outcome, and the brief allows cuts in the middle. Noted here so that the writer can see it went.

## Plot check

Every event, decision and outcome in chapters 1 to 12 was compared, and none differs. Rin is stopped; Nessa signs the lot, selects Tomas's list, refuses Orra's exceptions, holds the entrance and refuses the rescue; Tomas surrenders and is held for a hearing; the guarantee is called. These facts all still arrive where later chapters need them: frames A and B; the four-minute cooling; B waiting at Nearbank; the attendant transferred; the twelve boarders; the access agreement and inspection rights; the households; Rin; Dema; the mended shirt; the orchard motor; the junction's physical cut. The two exceptions are those in findings 2 and 3.
