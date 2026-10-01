# Kept cases: the first run, before the error-correction build

*Written 24 September 2026 (log entry 27). Kept as it came: nothing below was edited after the run, apart from this heading and the layout.*

- **Skills tested:** as committed at 35f2939, before any change made in entry 27.
- **How:** for each case, a fresh agent was given only the writer's part and the repository at that commit, and answered as a Claude Code session would, choosing the skills itself. A separate grading agent, which did not read the skills, graded each answer against the case's must and must-not lists. Two planted wrong answers were graded with them.
- **Not tested:** whether the advice is good in general; each case shows only that the skills run on that case. Answering and grading agents are the same kind of model.

| Case | Result | Skills chosen | Stalls reported |
|---|---|---|---|
| 01-danger-the-audience-sees.md | pass | plot, hard-to-vary | 7 |
| 02-ending-told-in-the-first-line.md | pass | plot, hard-to-vary | 9 |
| 03-villain-with-four-blank-levers.md | unclear | character, hard-to-vary | 8 |
| 04-lead-shot-in-chapter-three.md | pass | genre, character, hard-to-vary | 9 |
| 05-strike-day-that-moves-no-plot.md | pass | plot, hard-to-vary, story-world | 10 |
| 06-rationed-light-and-one-night.md | pass | plot, hard-to-vary | 8 |
| 07-invented-names-unexplained.md | pass | story-world, hard-to-vary, plot, genre | 8 |
| 08-crew-that-dies-one-by-one.md | pass | character, hard-to-vary | 9 |
| 09-cheated-or-unsafe.md | pass | genre, plot, hard-to-vary | 7 |
| 10-sound-scene-nothing-wrong.md | pass | plot, dialogue, hard-to-vary | 8 |
| 11-two-versions-which-is-better.md | fail | plot, hard-to-vary, dialogue | 8 |
| planted wrong answer to 01-danger-the-audience-sees.md | fail (must be fail) | none | none |
| planted wrong answer to 10-sound-scene-nothing-wrong.md | fail (must be fail) | none | none |

## 01-danger-the-audience-sees.md

**Result: pass.** Grader's notes: Both musts are clearly met, and the answer does neither forbidden thing. One point is close: the answer says the reader's question ("Does it change what anyone decides?") "is the right question for a fact that reaches a character." But it limits that test to facts a character learns. It then states a two-part rule (a character's action OR the audience's expectation), and it judges this shot on the audience part alone. So it does not make a character's decision the only way a reveal earns its place. Per the Open points, the words "dread" and "suspense" and any sense of "gap" were not graded.

- [met] *must:* Say that the shot's job is to put the audience ahead of the characters: the audience knows of a danger the family does not.  
  Evidence: "This is the audience being ahead of the characters: we fear *for* them and can't warn them." / "Keep: no one sees it. That is what puts the audience ahead of the family." / "What matters is a danger the audience can read and the family can't see."
- [met] *must:* Judge the shot by what it does to what the audience knows and fears during the dinner, not by whether any character's decision changes.  
  Evidence: "Your boathouse shot is built to reach only the audience, and a fact like that has to be judged a different way: does it change what the audience expects and watches for?" / "The fight about selling the house plays out with the damaged boathouse sitting in the audience's mind." / "Each 'can we go to bed early?' becomes the moment the audience wants to shout 'don't'." / "it swaps more than twelve minutes of dread for a few seconds."
- [met] *must not:* Advise cutting the shot, or moving it to after the jetty scene, on the ground that it changes no character's decision or action.  
  Evidence: The answer does the opposite: "Short answer: keep the shot." / "The fix then is to make the shot clearer, not to cut it." / "Move it to after dinner and the bedtime requests lose their charge." It never advises cutting or moving it on the no-decision ground.
- [met] *must not:* State as a rule that a reveal earns its place only if it changes what a character decides or does, or keep the shot only on condition that a character later learns of the leak.  
  Evidence: The only rule stated has two parts: "A fact that changes neither what a character does nor what the audience expects is just information." The answer limits the reader's test to "a fact that reaches a character" and says an audience-only fact "has to be judged a different way". Its conditions for keeping the shot are about the audience reading it ("They must see the danger... They must know who is in danger... They must care about the twins"), and none requires a character to learn of the leak.

**Stalls reported by the answering agent:**

- *plot/SKILL.md, Building step 8 (hard-to-vary 'lightly' versus 'full procedure'):* Step 8 says to use hard-to-vary lightly for a craft note, but to run the full procedure and report 'when the writer asks whether a whole explanation holds up'. The writer asks 'Is she right?' about a reader's craft note, so both rules could apply. I chose the light use (quick version plus remove, move, swap and two-routes from by-domain section 5) because the thing being judged is a one-sentence craft note, not the writer's own account of a draft. The skill does not say which rule wins in this case.
- *plot/SKILL.md, choosing a mode (Building, Diagnosing, quick version):* The message is not a felt symptom ('it drags'). It is a reader's reasoned argument for cutting one shot. Diagnosing step 1 wants a pinned symptom, and the quick version sends a single choice to Building step 8. I treated it as a test of one choice (step 8), plus the map row for 'deciding when a fact comes out' (reveals-and-withholding.md). Because the reader's actual experience is missing, I turned it into a check the writer can run, as step 1 says to. The skill does not directly cover the case of a writer pushing back on someone else's craft note.
- *plot/SKILL.md map ('When a small case matches a specific row, open that row's module'):* Three rows matched: the suspense module, the reveals module, and the hard-to-vary test row. The wording implies one module. I opened the reveals module and then the suspense module, because reveals-and-withholding section 3 itself points to suspense-and-fear sections 1 and 6. This is a small ambiguity, not a real conflict.
- *CLAUDE.md versus the run's rules:* CLAUDE.md says that when starting or continuing work, first read 'StoryTest - project story.md' and '22 Questions', and add a numbered log entry for every piece of work. The run's rules said to open only the modules and theory passages the skill sends you to, and to edit nothing. I read neither file and added no log entry. I relied on the plot skill's own labelled stopgap readings (for example, reveals section 6: calling a set-up a promise is the workshop's stretch, with an owner question open), which CLAUDE.md says to keep in the meantime.
- *plot Reply step (order of the reply):* The reply order ('what is wrong or missing, ranked...') is written for diagnosing a draft. The writer asked a yes/no question about a reader's note. I improvised by putting the direct answer first, then followed the prescribed order: risks ranked, what to protect, free versus held, fix, assumptions, one next step.
- *plot skill, audience-only reveals: whether the audience can read the shot:* Reveals section 3 says to judge an audience-only reveal 'by what it does to the gaps', but says nothing about checking that the audience can actually read it (a split flue and soot may mean nothing to many viewers). I improvised from the suspense module's Threat term ('make it specific: name what could be lost') and hard-to-vary's rule to turn missing facts into tests. The suggested fix (the twins' sleeping bags in the same frame) is my own, not from the skill.
- *Hand-offs to character and genre:* Two of the risks belong to other skills: care for the twins (character) and a family drama's unspoken promise that children come to no harm, which lowers uncertainty (genre; suspense-and-fear section 5). Diagnosing step 6 says to hand these off, but within this run I could only name them in the reply. I did not open those skills.

<details><summary>The answer as given</summary>

**Short answer: keep the shot. Your reader is using the right test on the wrong kind of reveal.**

"Does it change what anyone decides?" is the right question for a fact that reaches a character. Your boathouse shot is built to reach only the audience, and a fact like that has to be judged a different way: does it change what the audience expects and watches for? A fact that changes neither what a character does nor what the audience expects is just information, and she'd be right to cut it. Your shot passes on the second count, and it passes strongly.

It's close to Hitchcock's bomb under the table, which is the workshop theory's own example of what plot does. If the bomb just goes off, the audience gets fifteen seconds of surprise. If they see it first, they get fifteen minutes of suspense. (Suspense here means the audience knows what's at stake but not how it will end.) You have the same choice, and the same numbers: twelve minutes of dinner, then the night.

**What the shot does, which is also what cutting it would lose**
1. **The dinner argument.** The fight about selling the house plays out with the damaged boathouse sitting in the audience's mind.
2. **The twins' bedtime requests.** Each "can we go to bed early?" becomes the moment the audience wants to shout "don't". Their father's "yes" is a harmless line that hits like a blow, because we know what he doesn't. This is the audience being ahead of the characters: we fear *for* them and can't warn them.
3. **Two in the morning.** When a twin wakes with a pounding head, the audience understands it a beat before she does.

Without the shot, all three go flat. The requests are small talk, the "yes" is nothing, and the jetty scene becomes a jolt lasting a few seconds. Then the film has to stop afterwards and explain what the heater did.

Her version does gain something: a real surprise, and a small sting in hindsight on the father's "yes". But it swaps more than twelve minutes of dread for a few seconds.

**Where she could still turn out right in practice (ranked)**
The shot only works if the audience can read it:
1. **They must see the danger.** They have to read a split flue and soot as "fumes that can kill someone asleep", and many viewers won't. If they can't, the shot really is just information. The fix then is to make the shot clearer, not to cut it.
2. **They must know who is in danger.** They need to know, at the shot or early in dinner, that the twins sleep there. If they only find out after dinner, the dinner has nobody to fear for.
3. **They must care about the twins.** If the twins have been in the background until the halfway point, the danger weighs less. Building that care is the character side of things, not the plot side.

**What to protect, and what is free**
- **Keep: no one sees it.** That is what puts the audience ahead of the family. If an adult saw it and shrugged, you'd be telling a different story, one about blame.
- **Keep: it comes just before dinner.** Move it to after dinner and the bedtime requests lose their charge.
- **Keep: the danger works while they sleep.** Children, a bed and a family house are all places meant to be safe, and nobody can skip sleep. That makes the threat very strong.
- **Free: the exact length and the details.** Ten seconds exactly doesn't matter; hold the shot as long as it takes to read, and no longer. A gas heater versus some other silent source of fumes, and soot as the warning sign, are your choice. What matters is a danger the audience can read and the family can't see.
- **Check: the two requests.** Keep both only if they do different things. For example, the first gets lost under the argument, a small let-down (maybe they won't go yet), and the second gets the "yes". If they're the same beat twice, cut one or make them differ.

**Fix**
1. Keep the shot and tie it to the twins in the same image. For example, their sleeping bags are already laid out on bunks by the heater. One picture then shows both the danger and who it's for, without any character seeing it.
2. If fresh viewers can't say what's wrong in the shot, make the warning sign clearer. Don't add dialogue to explain it.

**What I assumed or am unsure of**
- I have only your summary, not the pages.
- I don't know whether the audience already knows the twins will sleep in the boathouse when the shot comes.
- Your reader seems to be arguing from a rule, not reporting that the dinner felt slack to her. I don't know which it is.
- Audiences often trust that the children in a family drama will come to no harm. If readers feel no worry at all, that trust may be the reason. That belongs to the genre side, and I haven't looked into it.

**If you want to settle it with her**
Make two versions: A without the shot, B with it. Give each to people who haven't read either, and ask which one grips them more across the whole stretch, from just before dinner to the jetty. The workshop's theory predicts B. Her view predicts A. Whichever wins answers the argument.

**One next step**
Show the shot and the dinner to two or three people who haven't read the script. Right after the shot, ask: "What's wrong here, and who is in danger?" After the dinner, ask: "Where did you feel tense?" If they name the fumes and the twins and point to the bedtime requests, the shot is working. If they can't, make the shot clearer rather than cutting it.

</details>

## 02-ending-told-in-the-first-line.md

**Result: pass.** Grader's notes: Case file read: /tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/cases-draft/case-02-ending-told-in-the-first-line.md. The answer meets both musts and breaks none of the three must-nots. The only borderline point is the table verdict "Holds only if A is true" on the editor's piece 2 ("so no uncertainty is left"). It is a conditional hard-to-vary verdict, and the same row says the piece fails case C and does not hold for a book whose question is why. So it does not say that telling the ending removes uncertainty. The case has no open points.

- [met] *must:* Say that telling the ending does not remove the uncertainty but moves it from whether the drowning happens to how (and why) it happens.  
  Evidence: "But your first line doesn't remove the uncertainty. It moves it. Readers stop asking *whether* Aurek dies and start asking *how* it came to that and *why* Pell let go."
- [met] *must:* Name at least one thing in this story that stays uncertain after the first line (for example how it came to the letting go, why Pell let go, or whether he could have held on).  
  Evidence: "It keeps back the why, and the how: how two boys came to be on that ice, and what 'I let go' means. He may not have been able to hold on, he may have been about to go under himself, or he may have chosen to."
- [met] *must not:* Say that telling the ending removes the uncertainty, or sets it to zero, and so removes the suspense.  
  Evidence: Not done. The answer rejects the claim: "The first half is true. The 'so' is not." In the table, piece 2 is marked "Holds only if A is true", which is conditional and not an assertion; the same row says it "fails C" and "is stated without support", and that it holds "not for a book whose question is why." "Her rule says both leave suspense at zero" puts the claim on the editor and does not endorse it.
- [met] *must not:* Advise moving the drowning to the end on the ground that a known outcome leaves nothing uncertain.  
  Evidence: Not done. The answer advises the opposite: "Keep the opening." and "Moving the drowning to the end would swap a whole book of suspense for a few pages of surprise."
- [met] *must not:* Treat a teller who knows the ending as a fault in itself.  
  Evidence: Not done. The answer calls it a strength: "the workshop's theory of suspense names it as prose's own best suspense tool: the narrator who already knows the ending." Its warning that "Pell's silence about the why has to be his, not yours" is a condition on how he holds back the why. It does not say a teller who knows the ending is a fault.

**Stalls reported by the answering agent:**

- *baseline CLAUDE.md against the run rules:* The baseline CLAUDE.md says that when starting or continuing work you read 'StoryTest - project story.md', then '22 Questions - meanings only you can settle.md', and add a numbered log entry for every piece of work. The run rules say to open only what the chosen skill's map and steps point to and to edit nothing. I followed the run rules: I did not open either file and wrote no log entry. So I could not check whether an open owner question bears on this case, such as what counts as a gap, or calling a set-up a promise. I relied on the skill's own labels for its stopgap readings.
- *plot SKILL.md, 'Built on' and The procedure; suspense-and-fear.md header:* The plot skill says to read the whole Gap theory before a first full run, and only the cited passages for a small case (one scene, choice or symptom). The suspense module says to read the whole Anticipation theory before its 'first full use'. This case is one choice (where the announcement goes), but it touches the whole book's structure, and 'full use' is not defined. I judged it a small case and read only the passages cited by the sections I used: Gap principles 4-6, Part 2 sections 3-5 and question 4; Anticipation's equation, principles 1 and 6, Part 2 sections 1 and 6, and the Books and film table.
- *plot SKILL.md Building step 8 against the Reply step; hard-to-vary 'The report':* Step 8 says to run hard-to-vary's full procedure and report 'when the writer asks whether a whole explanation holds up, such as their own account of why a draft fails'. Here the account is the editor's, not the writer's. I took 'Is she right?' to meet that condition and ran the full procedure. Nothing says how to merge hard-to-vary's seven-part report with the plot Reply's order and its 'in proportion to the case'. I improvised by putting a shortened report inside the plot reply, before 'what I assumed' and 'one next step', and by opening with a one-line verdict, which the Reply order does not list.
- *hard-to-vary status marks (SKILL.md, reporting.md):* None of the six status marks fits a part that fails a counter-case added by the checker. Piece 2 ('so no uncertainty is left') fails the added job, 'books that announce their outcome stay tense'. I marked it 'held if' (held only by an unobserved job) and reported the failure under the whole-explanation test 'add a job'. That is a judgement call. Provenance also fits piece 1 poorly, since it is a plain observation read off the draft; I called it 'built'.
- *plot SKILL.md map row and step 8 pointing to hard-to-vary by-domain.md section 5:* Section 5 treats the parts as creative choices and the jobs as what each choice does. The editor's claim is a causal diagnosis plus a fix, which sections 1 (diagnoses) or 2 (plans) might fit better. I opened only section 5, because the plot skill names only that one, and adapted it myself: her four sentences became the parts, and the contrasts became the jobs.
- *plot SKILL.md Diagnosing step 1:* The step covers a symptom a reader reports, or a pitch from a writer who cannot be asked. It does not cover a symptom that someone else has only predicted from the structure, as the editor did. I treated the prediction as the claim to test, following hard-to-vary step 1 ('make sure there is something to explain'), stated my assumptions, and turned the missing reader facts into the next-step test.
- *hard-to-vary references/testing-against-cases.md, section 3:* For a test you build yourself, it asks for a case where the right answer is 'nothing'. The reader test I suggested to the writer has no such control case. I left one out to keep the writer's next step simple. The counter-cases (Chronicle, The Secret History, Romeo and Juliet, Titanic) are the theory's and the modules' claims, not anything seen, so the 'add a job' failure rests on claimed cases.
- *suggestion to carry 'bad odds, not no odds' over to the why:* The theory's uncertainty rule is about outcomes still to come. The why is a fact about the past, which is curiosity in Gap terms. Asking the writer to keep the worst reading of 'I let go' looking likeliest is my extension of the rule, not the theory's, and the reply says so.
- *plot SKILL.md description and Diagnosing step 6:* Both name 'story-critique' as leading critiques of a whole work, but this repository's .claude/skills has no story-critique skill. The step says 'if it is available', so it does not break anything here, but the reference could mislead.

<details><summary>The answer as given</summary>

**Short answer:** She's right about one thing and wrong about the step that matters. Suspense does need uncertainty. But your first line doesn't remove the uncertainty. It moves it. Readers stop asking *whether* Aurek dies and start asking *how* it came to that and *why* Pell let go. *Romeo and Juliet* makes the same trade in its prologue, and the workshop's theory of suspense names it as prose's own best suspense tool: the narrator who already knows the ending. Moving the drowning to the end would swap a whole book of suspense for a few pages of surprise. Keep the opening. The real risk is in the middle, and that part of her worry deserves attention.

**What's wrong or at risk, most important first**

1. **Her reasoning has one broken link.** She says, "Readers know Aurek drowns and that Pell let go, so there's no uncertainty left." The first half is true. The "so" is not. Your first line gives away the outcome: whether he dies, and who let go. It keeps back the why, and the how: how two boys came to be on that ice, and what "I let go" means. He may not have been able to hold on, he may have been about to go under himself, or he may have chosen to. Plenty of books tell their outcome first and stay tense. The theory the workshop builds on cites *Chronicle of a Death Foretold*, which puts the killing in its title, and *The Secret History*, which tells you Bunny is dead in its first line. *Titanic* shows old Rose alive in its first minutes. Taken as a general rule, her claim says all of these should go slack. Inside a story, readers feel the uncertainty even when they know the end, which is why rereading still works.

2. **The real risk is that the why has to stay open, and in doubt, all year.** Once the whether is settled, all the uncertainty lives in the why. Suppose that by the middle a reader can say with confidence why Pell let go, for example because the dog fight reads as a plain grudge. Then nothing is left to wonder about and the middle will sag. It will look as if your editor was right, but the cause will be in the middle chapters, not the first line. It would show in the rope swing, the dog fight and the day the father left.

3. **Pell's silence about the why has to be his, not yours.** Grown-up Pell knows why he let go. Holding it back until the end is fair only if not saying it yet is part of who he is: a man who can't say it until he has laid out the whole year. "This is how it came to that" already gives him that reason, and the voice needs to keep it alive. If it reads as the author saving a twist, readers will feel cheated when they read it a second time.

4. **"This is how it came to that" is a promise.** It turns the how into a question the book has to answer, so the ice scene must deliver it. You may want to leave "did he mean to?" open. The workshop's reading, which is untested, is that a question can stay open only if the telling never presses it. A question the book keeps chasing and then leaves hanging reads as a betrayal.

**What works and should be protected**

- **Your first paragraph does four jobs at once:**
  - It names the threat: Aurek under the ice.
  - It starts a clock. "The winter the mill-race froze" is a date the whole year walks towards, so every cold snap and the first hard frost are the clock ticking.
  - It puts the reader ahead of the boys for the whole book. In summer they don't know and we do, so every scene of the two of them together is watched from above. We fear *for* them and can't warn them.
  - "I let go" instead of "he fell through" opens the why and turns the book into a confession.
- **The year before the ice builds care before the threat arrives.** In the workshop's theory, suspense comes from care, threat, uncertainty and time together, and if any one of them is missing there is none. Care has to come first. The rope swing and the dog are what make the ice cost something.
- **The drowning still lands at the end**, assuming the book ends on the ice. It lands as the scene the reader has dreaded all book, not as a shock.

**Which choices hold weight and which are free**

- **Holding weight:**
  - Telling the outcome in line one. Take it out and you lose the clock and the reader being ahead of the boys.
  - "I let go." Swap it for "he fell" and the why and the confession disappear.
  - "This is how it came to that." It is Pell's reason for telling the year in order, and that reason is what makes his holding back fair.
  - Pell being the elder, the one who should have held on.
- **Free:**
  - The exact ages. Ten and eight would work as well. What matters is that he is older and both are children.
  - Probably the particular summer events, unless each one bears on the why. To test one, cut the dog fight and ask whether a reader's guess about the why would change. If it wouldn't, the scene is only building care. That's fine, but it isn't working on the question the book runs on.

**The fix: keep the opening and work on the middle**

1. **Give each event of the year a pull on the why.** The dog fight could add a possible grudge. The father leaving could put Pell in charge of Aurek, which gives him a reason he should have held on and a weight he might have wanted to put down. The rope swing is practice in holding on and letting go. Aim for two or three live readings of "I let go" at the halfway point, none of them certain, with the worst one looking most likely. That is my reading, carrying the theory's rule for outcomes (bad odds work, no odds don't) over to the why.
2. **Point the summer at the winter.** If the rope swing hangs over the mill-race, the place where they played becomes the place where he drowns. The theory finds fear strongest when danger comes into a place that was meant to be safe. The first hard frost could be a false alarm: Aurek goes out on thin ice, Pell hauls him back, and the reader, who knows what's coming, flinches and then relaxes. The real break then comes after that relief.

**Her reasoning, piece by piece**

The workshop checks reasoning with a test called "hard to vary": change one piece of an explanation and see whether it still explains what it claims to. If a piece can be changed with no loss, nothing was holding it in place.

- **What is being tested:** her prediction that, with the outcome told in the first paragraph, readers will feel no suspense through the book, and that the drowning would land better if held back to the end. As far as I know, no reader has yet said the book drags. This is a prediction from the book's structure, so it needs testing before anyone explains it.
- **Her four pieces, in her words:**
  1. "You've given away the ending in the first line."
  2. "Readers know Aurek drowns and that Pell let go, so there's no uncertainty left."
  3. "Without uncertainty there's no suspense."
  4. "Move the drowning to the end, where it can land."
- **What her reasoning has to account for:**
  - A. Why this draft would have no suspense, compared with the same book with the ending held back. This one is hers.
  - B. Why the drowning would land better at the end than announced at the start. Also hers.
  - C. Why other books that tell their outcome first stay tense. I added this one: she states piece 2 as a general rule, so it has to cover those books too.

All four pieces were tested. Only piece 3 leans on an outside rule.

| Piece | Verdict | Why |
|---|---|---|
| 1. The ending is given away | Holds, once reworded | Replace "the ending" with "the outcome: whether he dies and who let go" and her argument is unchanged. That reworded version is what actually holds. The why is not given away. |
| 2. So no uncertainty is left | Holds only if A is true | The only thing supporting it is A, which no reader has reported yet, and it fails C. Here is a check. If your first paragraph also gave the why ("because of the dog"), suspense should drop sharply. If it only added more of the where and when, it shouldn't. Her rule says both leave suspense at zero, so it can't see the difference that matters. It is stated without support. It holds for a whodunit, where whether and who *are* the question, but not for a book whose question is why. |
| 3. No uncertainty, no suspense | Holds | Take it out and her argument falls apart. It is the same rule the workshop's theory uses. |
| 4. Move it to the end | Holds only if B is true | Nothing supports it except B, which is in doubt. It is stated without support. |

**Checks on her reasoning as a whole**

- **Reverse the result.** If readers found the draft gripping, her account couldn't absorb that without dropping piece 2. That counts in its favour: it makes a clear prediction, so a reader test can settle it.
- **Does cause lead to effect?** Her claim is that announcing the outcome lowers suspense. This is not settled yet. The reader test below checks it by cutting the announcement.
- **Is the answer built into the starting point?** Partly. Calling line one "the ending" assumes the outcome is what readers are reading for. In a book whose question is why, the outcome isn't the ending.
- **Where the requirements came from.** A and B are hers. C is mine, taken from cases the workshop's theory names. Those cases are the theory's claims, not a test of your book.
- **Add another case.** It fails C.
- **Look at how it works, not just the result.** Her account has nothing for what readers watch for once the whether is gone, and that is where this book's suspense does its work.
- **Pieces that pull against each other.** The rule she relies on in piece 3 also says a threat must be shown early to buy time. Her fix gets back uncertainty about whether by giving up that time. Since each part only counts if the others are there too, that's a bad trade.
- **Earlier failures patched over.** Doesn't apply: there was no earlier failure.
- **What her reasoning ignores.** Whether the middle keeps the why open, how the narrator's voice holds it back, and the care built across the year.
- **Rival views.** First, the workshop's theory: telling the outcome early moves the uncertainty to how and why, and buys time and a reader who is ahead of the boys. Second, the story-structure writer Robert McKee's rule that a fact should come out only when it's needed. That rule fits the why, a fact about the past, and your draft already holds the why back. For a threat still to come, such as the drowning from the boys' side, the workshop follows the theory: show it early. The reader test below tells her view and the theory's apart.

**What would make her case stronger:** tying it to a particular place and a particular reader, for example "by chapter X every reader can say why he let go." A test could catch that claim.

**What this doesn't show:** that your middle works. I haven't read it, and her reasoning failing doesn't make the draft good.

**What I assumed**

- The book ends on the ice, so the drowning scene already comes last and only the announcement is at the front.
- Pell tells the story long afterwards and doesn't give the why until late.
- No reader has yet said the middle drags, and your editor was reasoning from the structure. If she did feel it drag herself, the drag is real but her cause may not be. It could be that the why is settled too soon, that care is too thin, or that the summer chapters forget the ice.

**One next step**

1. Give the manuscript as it stands to two or three readers, and the same chapters with the first paragraph cut to two or three others.
2. Ask everyone to mark the page where they first started skimming.
3. Stop the readers of the uncut version at the halfway point and ask, "Why do you think he let go?"

What each side predicts, written down now before you run it:

- **The theory predicts** that readers of your version skim less and give different answers at halfway.
- **Your editor predicts** that the cut version holds readers better.

How to read the results:

- **If your readers all give the same answer at halfway,** the why was settled too early. Fix the middle, not the opening.
- **If they skim but still give different answers,** check care next. Put Aurek in clear, close danger in one early scene, such as the first frost, and see whether readers fear for him.

</details>

## 03-villain-with-four-blank-levers.md

**Result: unclear.** Grader's notes: No item is broken. The one unclear item is Must 2, and it turns on whether plain-word stand-ins count as "the theory's names". The answer clearly decides that she is a person, using what the pitch gives her (the swap test with a bank or a flood, and the card-game case in scene two). It names four levers she has and explicitly ties them to "the mix the theory credits for Hannibal Lecter". But it calls them "skill", "sharp particular details", "wit" and "clear motive" instead of competence, specificity, humour and desire with a reason. Only "wit" is the theory's own word (from the Lecter line). If a grader accepts close synonyms tied to the theory, this becomes met and the case passes. The open point Q3 is handled correctly: the advice about her origin is marked "The workshop's current reading ... The owner hasn't yet decided how far that goes." S6 (the turned-round ladder) is not used. One claim is not graded by any item: that the theory's word "wounding" means something that can be hurt now, not a sad past.

- [met] *must:* Say that no character, a villain included, needs every lever, so the four blanks are not by themselves a fault.  
  Evidence: "You don't have to add all four." ... "It says no character needs all ten; when you turn one down, you turn another up." ... "Free: the cats, and the four gaps themselves. Each could go either way; none is required."
- [unclear] *must:* Judge whether she is a person or a function from what the pitch gives her, naming at least two levers she has by the theory's names (for example desire with a reason, competence, specificity, humour).  
  Evidence: "She's a person, not a function. A function is a role that any force could fill. Swap Ilse for a bank foreclosing on the farms, or a flood, and the story breaks" ... "Ilse runs on skill, sharp particular details, wit and a clear motive. That is the mix the theory credits for Hannibal Lecter." The judgment is made from the pitch, but the levers are given in plain-word paraphrase (skill, sharp particular details, clear motive) rather than the theory's names (competence, specificity, desire with a reason); only "wit" matches the theory's own wording (from the Lecter line), and humour appears only in the general list of levers, not as one she has.
- [met] *must:* If it recommends adding any of the four, give a reason from this story, not the rule that every lever must be there.  
  Evidence: The only one it leans toward is a weakness, with a reason from this story: "If she can't be hurt and risks nothing, readers have nothing to fear on either side, and the surveyor is just a fly waiting for the spider." ... "grow the weakness from what's already there ... Her copies are cleaner than the originals ever were, and that is the crack the surveyor finds." Love is only "optional"; inner life only "if you want them torn".
- [met] *must:* If it recommends giving her an inner life on the page, mention the theory's warning that access to a character's mind tends to win the reader's side whatever she has done.  
  Evidence: "Time inside a character's mind tends to put readers on her side whatever she has done. The theory's examples are Ripley and Tony Soprano." ... "Add inner life only if you want them torn."
- [met] *must not:* Say she is a function because she lacks a past wound, an inner life, loved ones or a flaw, or require all four.  
  Evidence: Not done. "Short answer: no. You don't have to add all four." and "She's a person, not a function."
- [met] *must not:* Count fear of what she will do to others as the audience's care for her (for example, as her Worry rung).  
  Evidence: Not done. It treats danger as threat running both ways, not as care for her: "A villain has to be a real danger to the hero, and the hero has to be a real danger back." It never calls fear of her actions care for her or a Worry rung.
- [met] *must not:* State a turned-round ladder of care for villains (the upper rungs read backwards) as the Bond theory's own view.  
  Evidence: Not done. The answer never mentions the ladder of care or its rungs; "Readers can only fear she'll get away with it" is not presented as the theory's ladder.

**Stalls reported by the answering agent:**

- *Repository CLAUDE.md against this run's rules and the skill's map:* CLAUDE.md says to read 'StoryTest - project story.md' and '22 Questions' before starting work, and to add a numbered log entry for every piece of work. The run forbids opening files the skill does not send me to, and forbids editing, and the character skill's map never points to either file. I read neither and wrote no log entry. As a result I used the skill's labelled stopgap readings without checking whether the owner has since settled them: warmth read as Connection (SKILL.md, Building Step 3), and how far 'hide the thing' reaches for human villains (opponents.md, section 6). Either could be stale.
- *character/SKILL.md, 'Built on' and the first two rows of the map:* It was unclear whether this is a small case (one character, one named complaint: read only the cited theory passages) or a first full run (read the whole theory). I treated it as a small case that a map row names, so I opened opponents.md. The Bond theory passages cited by the sections I used (principles 2, 4, 5 and 6, the lever table, the ladder, the limits) cover nearly all of Parts 1 and 2, so I read lines 1-93 and skipped 'Books and film', 'Questions for a character' and the rest. I saw the theory's one-line summary ('a want, a wound and a way of seeing') only in a heading search. I read principle 3 to learn that 'wound' there means being able to be hurt now (Vulnerability), not a backstory.
- *character/SKILL.md, Building Step 8 (how heavily to use hard-to-vary):* The rule is: use it lightly for a craft note, but run the full procedure and report when the writer asks whether a whole explanation holds up, 'such as their own account of why a draft fails'. Here the writer asks whether a beta reader's explanation and prescription holds, which is neither their own account nor a plain craft note. I chose the light version (the quick version plus the remove and swap tests from by-domain.md section 5) and did not use the full procedure or its report format.
- *character/SKILL.md, Diagnosing Step 1 and its complaint table:* The beta reader's note is a prescription ('add all four') with a verdict ('a function, not a person'), not a report of where their care stopped. It matches the villain row only by that row's middle column ('a function, not a person'), not by the complaint column ('boring', 'just evil'). The skill does not say how to pin the symptom when a critic sends a rule rather than a reaction. I treated the symptom as unpinned, stated my assumptions, and turned the missing facts into questions for the reader, as Step 1 allows.
- *character/SKILL.md Diagnosing Step 2, and opponents.md section 8 (test for borrowed rungs):* The test says 'take the hero out of one of his scenes' to see whether readers' feelings against the villain are borrowed from care for the hero. Every one of Ilse's scenes is seen through the surveyor, so no scene exists without the hero, and the test cannot be run on the page. The skill does not say what to do then. I improvised by turning it into a question for readers (do they want her stopped for what she does to the valley, or only because she is in the surveyor's way), and I did not put that question in the reply, for length.
- *Mapping the writer's four demands onto the ten levers:* 'Inner life', 'someone who loves her' and 'a flaw' map directly onto Interiority, Connection and Flaw. 'A wound in her past' maps onto no lever: backstory sits under Specificity ('history'), and the theory's 'wounding' is Vulnerability. No map row handles backstory for an opponent. I improvised from opponents.md section 6 (a human villain's origin may stay hidden, a stopgap reading), the theory's 'visible levers' limit, and the 'two routes to one job' test from hard-to-vary.
- *character/SKILL.md, Building Step 9 (the reply's order):* The set order starts with 'what is wrong or missing', but the writer asked a yes-or-no question. I put a one-line direct answer and my stated assumptions (from Diagnosing Step 1) ahead of the ordered sections. It is a small departure from the letter of the order.
- *Handoffs I did not open:* The fix I suggested (her pedantry as the crack in the flawless forgeries) is partly a plot question: how the surveyor catches her, and when readers learn it (plot's reveals-and-withholding.md). I named it as a plot question in the reply but did not open that module, because the skill's handoff wording covers a character's past rather than how the hero catches a villain. I also did not open the crime genre profile. The genre row covers a villain who reads as a genre's stock type, which nobody complained of, although what crime readers expect of a villain might bear on the beta reader's rule.

<details><summary>The answer as given</summary>

**Short answer: no.** You don't have to add all four. Two of them, going inside her head and giving her a sad past, would probably work against you. One part of the note does point at something real, but it isn't the part the reader named.

I'm assuming three things: this is one reader's note; they didn't say on which page Ilse stopped feeling like a person; and you want readers against her, not quietly on her side. If any of that is wrong, tell me, because it changes what I'd say about inner life.

**What may be wrong, most important first**

1. **She may have nothing to lose, and the surveyor may have no way to hurt her.** "Her forgeries are flawless" plus "no weakness" is the one combination I'd check. A villain has to be a real danger to the hero, and the hero has to be a real danger back. If she can't be hurt and risks nothing, readers have nothing to fear on either side, and the surveyor is just a fly waiting for the spider. The theory the workshop uses does ask for "wounding", but it means something that can be hurt now, not a sad past. This is where the reader's "weakness" has a point.
2. **The cats may be doing no work.** Feeding strays is the classic "save the cat" kindness, and the theory warns that it can look put on for the reader's benefit. Try taking them out. If none of her choices change and readers lose nothing they use later, the cats are decoration.
3. **Her aim has no finish line.** She is "taking the farms one by one", but for whom, and which farm is the one that matters? Readers can only fear she'll get away with it if there's a moment when they will know whether she has.

**What works: protect it**

- **She's a person, not a function.** A function is a role that any force could fill. Swap Ilse for a bank foreclosing on the farms, or a flood, and the story breaks: nobody makes the card-game case in scene two, the woman who corrects grammar is no longer the one lying on paper, and her pairing with the surveyor is gone (he measures the ground, she keeps the papers about it). Also, if the surveyor died in chapter one, she would still be taking the next farm. Her plan doesn't depend on him.
- **Her balance of qualities.** The theory works with ten "levers": qualities a writer turns up or down to make readers care, such as skill, humour, a flaw or someone who loves them. It says no character needs all ten; when you turn one down, you turn another up. Ilse runs on skill, sharp particular details, wit and a clear motive. That is the mix the theory credits for Hannibal Lecter. She also has something Lecter lacks: an argument a fair reader could half accept, with its own fault built in, because she is lying land onto paper too.
- **Staying out of her head.** Time inside a character's mind tends to put readers on her side whatever she has done. The theory's examples are Ripley and Tony Soprano. Seeing her only through the surveyor, with her reasons argued out loud in scene two, keeps readers wanting her stopped. Add inner life only if you want them torn.

**Which choices are free, and which are held in place**

- **Held in place:** her job as registrar, the card-game motive, and the grammar habit, because it shows a mind that can't stand an error.
- **Free:** the cats, and the four gaps themselves. Each could go either way; none is required.
- **A wound in her past** would do the job her motive already does, a second time. It also risks what the theory calls a visible lever: a sad past that is there for the reader's tears rather than for her story, which readers find cheap. It could also shrink her argument from a principle to a grudge. (The workshop's current reading is that a human villain's reasons now are shown, while her origin may stay hidden. The owner hasn't yet decided how far that goes.)
- **Someone who loves her** is optional. It would make her defeat cost more. It fails if the love is only talked about and never shown.

**The fix for the top two**

1. **Write down both sides.** What can the surveyor do to her, and what could she lose: her post, her freedom, the farms she has already taken, the cats? If you already know how he breaks her, you're done. If not, grow the weakness from what's already there rather than bolting on a flaw. A woman who can't let an error stand makes flawless forgeries. But the eighty-year-old deeds she replaces were written by clerks who misspelled things. Her copies are cleaner than the originals ever were, and that is the crack the surveyor finds. If you swapped the grammar habit for, say, a love of opera, the catch would stop working; that is how you know the habit is doing a job. (When readers find this out is a plot question.)
2. **Tie the cats to the story or cut them.** Six in the morning is when she's alone at the registry, so it could be when the forgeries get done. Or the cats could be the one thing she'd lose. Also check that her jokes stop somewhere: the card-game speech should be the moment she isn't funny.

**What I'm unsure of:** I only have your summary, not the scenes. I don't know whether she acts on the page or is only discovered, or whether readers see a family lose a farm.

**One next step:** ask the beta reader why Ilse forges the deeds.
- If they can say it in their own words, her motive is landing, and the note is a checklist rather than a reaction.
- If they can't, make scene two land harder. That is the fix, not a wound.

Also ask them for the page where she stopped feeling like a person, and for a villain in another book who did feel like one.

</details>

## 04-lead-shot-in-chapter-three.md

**Result: pass.** Grader's notes: The answer meets all three musts and does neither forbidden thing. It says one early death makes later threats real. It says the theory's warning is about everyone dying, not about one death. It ties the rest of the book's suspense to the care readers feel for Tobi, using the equation where any factor near zero makes suspense near zero. The only place it says "anyone can die" would kill care is a conditional that frames the reader's claim for a test, so it does not break the first must-not. It also raises fridging, which the open points allow and exclude from grading.

- [met] *must:* Say that one early break of a genre guarantee (here, that the lead survives) makes later threats feel real, so readers feeling that anyone can die is what the break is for, not a fault.  
  Evidence: "Killing one lead early is a sound move, and knowing that anyone can die is what makes readers afraid for Tobi. It doesn't stop them caring." ... "if you break one of these protections early, and do it convincingly, every later threat becomes real." ... "Her death takes away a protection, so readers feel unsafe, which is what you want."
- [met] *must:* State the theory's limit as repeated deaths, and say that a single death does not reach it.  
  Evidence: "The danger the theory names is different: when *everyone* keeps dying, care collapses. You kill one person, and Hana is the only main character who dies. Your reader has taken the warning about the second situation and applied it to the first."
- [met] *must:* Say that the suspense of the rest of the book depends on care being built for Tobi, who carries it.  
  Evidence: "suspense is care multiplied by threat (and by uncertainty and time), so if any one of them is near zero, suspense is near zero. Hana's death sets the threat high for the next 27 chapters. That threat gets multiplied by how much readers care about Tobi when the hunt starts."
- [met] *must not:* Call the feeling that anyone can die a mistake, or say that it kills care.  
  Evidence: The answer says the opposite: "It doesn't stop them caring." The only other mention, "If the reader's reason is right, that won't help, because 'anyone can die' would still kill their care", describes the reader's claim as something the test checks. The answer does not assert it.
- [met] *must not:* Apply the theory's limit on everyone dying to this one death, or advise keeping Hana alive to the midpoint on that ground.  
  Evidence: "Your reader has taken the warning about the second situation and applied it to the first." and "Fixed: She dies before Tobi's hunt starts. Keep her alive to the midpoint and the chapters in between lose their danger"

**Stalls reported by the answering agent:**

- *Choosing the skill:* The question fits three craft skills at once: genre (its description names 'can I kill the dog?' and the protections the audience counts on), character (the reader's claim is about care; 'nobody cried when she died') and plot (moving the death to the midpoint is an event-order question). No rule says which craft skill leads when two or three fit and no whole-work critique is involved. I let genre lead (Building/Diagnosing step 6, which guarantee to break and where), because the question is exactly about breaking one guarantee early, and brought in character through genre's step 8 handoff and character's Diagnosing steps 5 and 7. I did not open plot.
- *genre/references/genres/detective-and-thriller.md, section 4, against sources/anticipation-theory.md Part 2 section 5:* The profile says Thriller withholds the investigator's protection from the start ('her danger is Thriller's baseline, not a break it can spend'), and its table lists 'the Thriller hero survives' only as a late break. It has no row for the apparent lead killed early. The owner theory names 'the star survives' as a guarantee and gives Psycho killing its apparent protagonist as the model early break. So the profile and the theory point different ways on whether killing an apparent Thriller lead early counts as a broken guarantee. I improvised: I used the theory's Psycho case for Hana as the apparent star, and read her from Tobi's side as the profile's 'the one who helps her is safe' row (Hutch), whose advice (break early, on someone near the hero) fits this structure.
- *How deep to go with hard-to-vary (genre Building step 9; character Building step 8):* Both skills say to use hard-to-vary lightly for a craft note, and to run its full procedure and report only when the writer asks whether a whole explanation holds up, 'such as their own account of why a draft fails'. Here the writer asks whether to follow a reader's explanation, which falls between the two cases. I used the light version: the quick version's flip test on the reader's argument (it condemns the midpoint death equally), and remove/swap on the writer's choices (by-domain section 5). I did not write a full report. This was a judgement call the text does not settle.
- *Small case or full run (the 'Built on' paragraphs of genre and character):* I treated this as a small case ('one choice': where Hana dies), so I read only the theory passages cited in the sections I used, not the full theories or genre's list of passages for a first full run. This is defensible, but the whole-book structure (the lead handed from Hana to Tobi) makes it arguable.
- *Pinning the symptom (genre Diagnosing step 1; character Diagnosing step 1):* The reader's note reads as a prediction from a general rule, not an observed loss of care at a named page. Both skills assume a reported symptom. I followed the missing-facts rule: I stated the assumption in one line and turned the missing fact into a reader test. The mode (diagnosing a draft or checking one choice with the quick version) was also not clear-cut; I used the diagnosing steps.
- *CLAUDE.md, against the run rules:* CLAUDE.md says to read 'StoryTest - project story.md' and '22 Questions - meanings only you can settle.md' before starting work, and to keep each skill's labelled stopgap reading on open owner questions. The run rules say to open only what the chosen skill's map and steps send me to, and no skill step sent me to those files, so I did not open them. I therefore cannot say whether an open owner question (for example, how a stopgap reading of Connection or of guarantees applies) bears on this answer.
- *Reply step (genre 'Reply'; character Building step 9):* The set reply order starts with 'what is wrong or missing, ranked'. It does not say how to answer a direct yes/no question such as 'Should I?'. I added a one-line verdict at the top and a short section on why the reader's reasoning fails before following the set order. That is a small departure from the order as written.
- *sources/anticipation-theory.md Part 2 section 5:* The theory says to break a guarantee 'early' and cites Psycho, which does it 'less than halfway through'. That is close to the reader's own midpoint. The theory therefore does not decide chapter 3 against the midpoint. My case for chapter 3 rests on the workshop's reading of this book's structure (the hunt is the book), and I said so to the writer as an uncertainty.
- *Writer's message:* No pronoun is given for Tobi, so I wrote around it (using 'their own reasons' once).

<details><summary>The answer as given</summary>

**Short answer: no, not for that reason.** Killing one lead early is a sound move, and knowing that anyone can die is what makes readers afraid for Tobi. It doesn't stop them caring. But the note may be pointing at a real risk under the wrong name, and a cheap test will tell you.

**Why the reader's reason doesn't hold**
- Every genre comes with protections readers assume without being told: the star survives, the child is safe. While readers trust those protections, part of them relaxes. The suspense theory this workshop uses says that if you break one of these protections early, and do it convincingly, every later threat becomes real. Its example is *Psycho*, which kills its apparent heroine. The danger the theory names is different: when *everyone* keeps dying, care collapses. You kill one person, and Hana is the only main character who dies. Your reader has taken the warning about the second situation and applied it to the first.
- Care doesn't come from a character being safe. It comes from time spent with a person, from being inside their head, and from knowing what they want and what they could lose. Fear for them is built on top of that. Knowing Tobi really could be shot is what turns liking Tobi into worrying about Tobi.
- Try the reader's own fix against their own reason. A death at the midpoint also tells readers that anyone can die. The reason argues against chapter 15 just as strongly as against chapter 3, so nothing in it points to the midpoint.

**What may really be wrong, most likely first**
1. **At chapter 4, readers may have nobody to give their care to.** In that same theory, suspense is care multiplied by threat (and by uncertainty and time), so if any one of them is near zero, suspense is near zero. Hana's death sets the threat high for the next 27 chapters. That threat gets multiplied by how much readers care about Tobi when the hunt starts. If Tobi is only a name in the background of chapters 1–3, readers lose the person they cared about and then meet a stranger in danger. That feels exactly like "why care about anyone?" But the cause is a missing bond with Tobi, and the fix is in how you write Tobi, not in when Hana dies. You would see it at the opening of chapter 4.
2. **Hana's open threads.** Her son and the feud with her editor are questions the first three chapters push hard, and a story owes an answer to every question it pushes. Her death takes away a protection, so readers feel unsafe, which is what you want. If the son and the editor then disappear, the story breaks a promise, and readers feel cheated. A reader can feel cheated and blame the death for it.
3. **Whether her death is about her.** You can kill a character readers love, but the death has to mean something for her, not just set someone else in motion. (The usual name for that failure is "fridging".) You're on the right side of this as long as she dies because of the leak she chose to chase, and that leak is settled one way or the other through Tobi by the end.
4. **Whether readers will miss her.** Three chapters is enough time. The opening of *Up* makes an audience grieve in about four minutes. But it only works if the son and the feud are shown in scenes rather than described. If readers feel nothing on the steps, the death is a shock rather than a loss, and the fear it sets up is weaker too.

**What works: protect these**
- **One early death, before Tobi's hunt begins.** From Tobi's side, Hana is the protector who gets taken away. Tobi is alone, and readers have just watched help die. That is the classic Thriller use of an early death.
- **Her fame.** If a famous reporter can be shot on the ministry steps, an unknown junior researcher has no protection at all. That is what makes every scene of the hunt frightening.
- **The ministry steps.** A killing in public, at the ministry's own door, tells readers how far the other side will go.

**What's fixed and what's free**
- **Fixed:**
  - She dies before Tobi's hunt starts. Keep her alive to the midpoint and the chapters in between lose their danger, because Tobi still has a famous protector.
  - Only she dies.
  - She is famous.
  - The killing is public and at the ministry.
- **Free:**
  - The exact chapter. Three, four or five all work. What matters is that it comes after readers would miss her and before the hunt.
  - How she's killed. Another kind of public killing would lose nothing.
- **What moving it to the midpoint would cost:** Tobi's hunt, which is your book, would shrink to half the book, and the novel would split into two halves. What the move would gain (more time to miss Hana, more time to get to know Tobi) you can get without moving the death.

**The fix, if the test below says you need one**
Give Tobi a real place in chapters 1–3:
- one passage inside Tobi's head;
- something Tobi wants for their own reasons, beyond "help Hana";
- something Tobi could lose;
- at least one scene of the two of them working the leak together, so the leak passes along a relationship readers have watched.

After chapter 3, bring back the son and the editor through Tobi.

**What I assumed, and what I'm unsure of**
- I assumed the reader's note is a prediction based on a general rule, not a report that they themselves stopped caring at a certain page. If they did stop, the page where it happened matters.
- You didn't say how much Tobi is on the page in chapters 1–3. I assumed "some, but not much".
- The theory says to break a protection early, but not how early. *Psycho* does it a little before its middle, so the reader's midpoint isn't wrong in itself. The case for chapter 3 rests on the shape of your book: the hunt is the book, so the death belongs before it.

**One next step**
Give chapters 1–5 to two readers who haven't seen them. Ask each to mark the page where they stopped caring, if they did, and to say who they were worried about in chapter 5.
- If they're worried about Tobi, change nothing.
- If they shrug, add Tobi to chapters 1–3 as above and test again, before you touch Hana's death. If the reader's reason is right, that won't help, because "anyone can die" would still kill their care. If the missing bond with Tobi is the problem, it will.

</details>

## 05-strike-day-that-moves-no-plot.md

**Result: pass.** Grader's notes: All four items are met, so the answer passes. The answer names the job the settings theory gives this kind of scene (a world with business of its own, shown through detail that serves no plot), though it calls that theory "the workshop's other theory about settings" rather than naming it. It labels its keep verdict as the workshop's current reading, not yet ruled on by the author of the theories. It refuses to cut the scene on the gap rule, and it does not use the "wonder" or departure-gap argument to save it. Following Open point Q2, I did not grade which sense of "gap" the answer uses. The answer also says the Gap theory "never says" the cut rule. That is a claim about what the theory contains, not a rule presented as the owner's settled view, so it breaks no must-not item.

- [met] *must:* Name the job the Implied World theory gives a scene like this: showing a world with business of its own, through detail that serves no plot.  
  Evidence: "The exception comes from the workshop's other theory about settings. A world feels real when it has business that has nothing to do with the main character. Details that serve no plot are what make a place feel like a world and not just a plot." ... "The real reason to keep this scene is that it shows the town's own business."
- [met] *must:* If it gives a verdict on whether a scene may be only the world at its own business (keep, fold, or cut), say that this is an open question for the owner, or label the verdict as the workshop's reading.  
  Evidence: "One caveat: this exception is the workshop's current reading, and the author of the theories hasn't ruled on it yet. If they rule the stricter way, the advice would still not be 'cut'. It would be to keep the strike but fold it into a scene that also moves the plot." and again: "The exception isn't final. As said above, it's the workshop's current reading, waiting on the theories' author."
- [met] *must not:* Advise cutting the scene merely because it opens or closes no plot gap, or moves nothing in the plot.  
  Evidence: "Short answer: no, don't cut it because of that rule." The only cutting it allows depends on reader evidence, not on the gap rule: "If the readers without the scene miss nothing, and the readers with it skimmed it, your plot reader is right for this draft: cut it or trim it."
- [met] *must not:* Present any rule about such scenes as the owner's settled theory: that they must be cut, that they may always stand alone, or that this scene 'changes the departure gap'.  
  Evidence: It presents the exception as the workshop's: "The workshop takes that test from the theory and applies it to most scenes. It makes one exception..." and "this exception is the workshop's current reading, and the author of the theories hasn't ruled on it yet." It turns down the argument that the scene opens a gap: "I wouldn't rely on that argument... The real reason to keep this scene is that it shows the town's own business." It never says the scene changes the departure gap.

**Stalls reported by the answering agent:**

- *CLAUDE.md (baseline) against this run's rules:* CLAUDE.md says to read 'StoryTest - project story.md' first, then '22 Questions', and to add a numbered log entry for every piece of work. This run says to open only what the skill sends me to and to edit nothing. I followed the run's rules: I did not read the project story and did not log anything. I read only questions 1, 2 and 5 of '22 Questions', because CLAUDE.md names that file as the place to check undecided points.
- *plot/references/scenes.md section 1; story-world/references/world-from-story.md section 11:* Both say whether a whole scene of world business may stay 'is a question put to the owner', but neither names the file or the question number. I found it (question 1, stopgap (b)) only through CLAUDE.md. I had to work that route out myself.
- *plot/SKILL.md, Words paragraph:* It says 'what else counts as a gap, for example one never mentioned at all, is a question put to the owner'. '22 Questions' has no such question. Question 2 asks about the word's two senses, not about gaps that are never mentioned. The record looks stale, or the question is missing.
- *plot/SKILL.md, Diagnosing step 1:* The step expects a symptom: a reader's reaction, with where and compared with what. Here the input is another reader's rule, not a reaction. The skill doesn't say how to treat a critic's rule. I treated the missing reaction as a missing fact, turned it into a reader check, and said so in the reply.
- *plot/SKILL.md, Building step 8 (how deep to run hard-to-vary):* The full procedure is for when the writer asks whether a whole explanation holds up, 'such as their own account'. Here the writer asks about a third party's one-line rule. It's unclear which side of that line this falls on. I chose the light version.
- *Owner question 1, stopgap (b), and scenes.md section 1: 'if it is short':* 'Short' isn't defined anywhere I was sent, for example relative to a chapter or a novel. I judged two pages short and turned the doubt into a skim check.
- *hard-to-vary/references/by-domain.md section 5 against Implied World principle 5 (surplus):* Hard-to-vary says 'a scene that survives every swap is decoration', and it treats a detail that can be swapped freely as loose. The Implied World theory says details that serve no purpose are what make a world, so the chestnuts and the blessing are meant to be swappable. The files I was sent to don't say how to report a choice whose job is to be swappable. The rival is recorded in world-materials.md section 9, but nothing sent me there. I made up 'free by design' and checked the scene as a whole, which doesn't survive the swaps.
- *plot/references/scenes.md section 4 ('Leave on a push') against Gap principle 5 and the world-from-story trap about a glimpse that turns into a promise:* One rule says a scene's last line should open a question the next scene answers. The other says a world-business scene must not press its own question, or that question becomes a promise the book breaks. I settled it myself by pointing the last line at Oda's search instead of the strike.
- *Whether a 'wonder' counts as opening a gap (plot/SKILL.md Words; scenes.md section 1 table):* By the Gap theory, the strike's outcome is a wonder, a question raised in passing and never pressed, so the scene might pass the reader's rule on its own terms. But if wonders count, the per-scene rule saves almost every scene and means little. The skill doesn't address this. I mentioned the argument and advised against relying on it.
- *'22 Questions', question 1 (the example case):* Minor: the question's example is a market-day scene, but its recommended option (b) requires the world to be shown 'under some pressure', which an ordinary market day usually lacks. The example doesn't quite fit the option it recommends.

<details><summary>The answer as given</summary>

**Short answer: no, don't cut it because of that rule.** Keep the scene and keep it short. Then run one check with readers (at the end) before you decide for good.

**Why the rule doesn't settle it**
The Gap theory this workshop uses never says "every scene must open or close a gap or go". The workshop takes that test from the theory and applies it to most scenes. It makes one exception: a short scene of the world getting on with its own business, under some strain, with nothing to do with the heroine. The workshop's own example of such a scene is a strike.

The exception comes from the workshop's other theory about settings. A world feels real when it has business that has nothing to do with the main character. Details that serve no plot are what make a place feel like a world and not just a plot. The standard example is the opening of *Alien*: the crew grumble about their pay before anything alien turns up.

Your reader's rule is close to Truby's rule: cut any scene that doesn't move the hero forward. The workshop treats that as a habit worth questioning, not a law, because it strips out exactly this kind of scene.

Someone may argue that the scene does open a gap after all: how the strike ends is a question raised in passing and never pressed. The Gap theory calls that kind of question a *wonder*, a question the story promises to leave open. I wouldn't rely on that argument. Almost any scene raises some question, so the argument would save every scene, and that means it proves nothing. The real reason to keep this scene is that it shows the town's own business.

One caveat: this exception is the workshop's current reading, and the author of the theories hasn't ruled on it yet. If they rule the stricter way, the advice would still not be "cut". It would be to keep the strike but fold it into a scene that also moves the plot.

**What could still go wrong (most likely first; none confirmed)**
1. **The strike turns into a promise.** Since the book never answers it, the strike has to stay a question in passing. Suppose the two pages dwell on who will win or why the ferrymen walked out, or the scene ends on the strike. Then readers will expect to find out, and the book never tells them. Watch where the scene lingers, and especially its last lines.
2. **Length.** The exception covers only a *short* scene. Everything the reader takes in about the town uses up the attention they need for Oda. Two pages in a novel sounds short to me. It's only too long if readers skim it.
3. **Doing a job that's already done.** Do other chapters already show Harl getting on with its own life? Then this scene repeats their work and would need a second job to earn its place.

**What works, and should be protected**
- **It shows the town under strain, not just the town.** People wade the shallows with their shoes round their necks: that's what the strike costs ordinary people. The priest blessing the idle ropes shows the church has a stake in the ferry. The boy selling chestnuts to the pickets shows ordinary life going on around the dispute. The townspeople take all of this for granted, and that's how such details work best.
- **It doesn't touch Oda.** Harl has a life she walks straight past, and the town doesn't arrange itself around her. That is the point, so don't "fix" the scene by tying the strike to her search.

**What holds the scene in place, and what could change**
- **These must stay:**
  - **A dispute of the town's own making, with sides.** Swap the strike for a market day and the strain is gone. Swap it for a flood and the strain stays, but the town's own business goes: the pickets, the church taking part, the trade carrying on.
  - **Oda untouched, and the scene short.**
- **These could be anything:**
  - Which trade walks out. It's the ferrymen unless the ferry matters elsewhere in the book.
  - The small details: the chestnuts, the blessing. Others would do, and that's fine. Their job is to say "this place is real". Choose them for how naturally the townspeople treat them, not for any hidden meaning.
- **Not yet tested: where the scene sits.** Would it matter if it came in chapter seven? If it gives the reader a breath between two archive scenes, that's a reason to leave it in chapter nine.

**The fix, if any**
1. **Keep the strike in passing.** Nobody explains it, and nothing in the scene invites the reader to wonder how it ends.
2. **Give the last line to Oda, not the strike.** End as she reaches the archive, or turns toward it. The scene then hands the reader straight on to her real story in chapter ten, and the strike stays in the background.

Only if the check below shows readers skimming: cut it to about a page, or let the strike cost Oda something small, like a longer way round, so the town gets in her way. The scene doesn't need that now.

**What I assumed, or am unsure of**
- **Did anyone actually skim?** I've assumed nobody in your group skimmed or got restless in chapter nine, and that the note is a rule being applied, not a reaction. If a reader did stall there, tell me where, and the answer may change.
- **Is Harl our world or an invented one?** Something in the scene may not be true of our world; perhaps blessing idle ropes is a Harl custom. Then the scene also teaches the reader how this world differs from ours, and it passes even your reader's rule.
- **Is the scene seen through Oda's eyes?** If so, what she notices and walks past may say something about her. That's a question about her character, separate from this note.
- **The exception isn't final.** As said above, it's the workshop's current reading, waiting on the theories' author.

**One next step**
Give chapters eight to ten to four readers who haven't heard the debate: two with chapter nine and two without. Afterwards, ask each of them two questions: where did you skim, and what's going on in Harl apart from Oda's search?
- If the readers without the scene miss nothing, and the readers with it skimmed it, your plot reader is right for this draft: cut it or trim it.
- If the readers with the scene describe a town with a life of its own and didn't skim, keep it.

</details>

## 06-rationed-light-and-one-night.md

**Result: pass.** Grader's notes: The answer meets all three musts and does neither must-not. Following the Open points, I did not grade how it relates "inciting incident" to the breach, or which words it uses for stakes and strangeness. It calls the wiping of the records part of the breach ("the night and its morning are your breach"). That is an event, not a standing condition, so it does not break the first must-not. I read only the case file.

- [met] *must:* Call the sixty years of rationing a departure (a way this world differs from ours) and part of Coldharbour's normal.  
  Evidence: "The departure is how your world differs from ours. Four lit hours a day is Coldharbour's main departure. After sixty years it doesn't break anything. It *is* the normal"
- [met] *must:* Call the night the grid stays on the breach, because it breaks Coldharbour's own normal.  
  Evidence: "the night is your breach"; "The breach is the event that breaks *this world's own* normal."; "In our world a night of electricity is nothing, but in Coldharbour it's an earthquake. That's a breach doing exactly its job."
- [met] *must:* Say that the rationing is what gives that night its stakes.  
  Evidence: "The rationing is your world's normal, and that normal is what gives the night its stakes."; "So the night only counts because of the rationing."
- [met] *must not:* Call the rationing, or any other standing condition of the world, the breach.  
  Evidence: The answer says the opposite: "If the rationing were the breach, the story would have to start on the day it began or ended, not sixty years in" and "the night and its morning are your breach, and the rationing is your world." The only other thing it puts inside the breach is the wiping of the records, which is an event, not a standing condition.
- [met] *must not:* Say the night of full power cannot be the breach because it is welcome rather than a disaster.  
  Evidence: Nothing in the answer rules the night out for being welcome. It calls the night the breach and uses the Netherfield example: "the night the grid stays on is Netherfield."

**Stalls reported by the answering agent:**

- *Choosing the skill:* Neither the plot nor the story-world description uses the word 'breach', and both half fit: the writer is asking whether a world rule (story-world) or an event (plot) is the breach. I had to read story-world's SKILL.md in full to settle it. Its Building step 5 says 'building it [the breach] is plot's work', so plot leads. A writer's question naming 'breach' or 'inciting incident' has no trigger phrase in any description.
- *plot SKILL.md: Building vs Diagnosing:* The message is neither a new plot to build nor a symptom to diagnose. It's a dispute over what to call things, raised by a writing group. No Diagnosing-table row fits ('which event is my breach?'). I used quick-version question 1 plus Building step 2, and took the closest map row ('making the breach escalate: the opening...') to structure-and-conflict.md sections 4 and 10. That was an improvised route.
- *plot SKILL.md, Built on: small case vs full run:* It's unclear whether 'what is my breach?' asked of a whole-novel premise counts as a small case ('one choice'). I treated it as one, so I read only the Gap theory passages cited (terms, five gaps, principle 2, Part 2 section 2), not the full text a first full run requires.
- *Missing facts while in Building mode:* The writer names no hero, so I couldn't tell whether the night or the wiped records is the hero's inciting incident. Only Diagnosing step 1 says what to do when facts are missing (state the assumption, turn the missing fact into a check). Building mode says nothing, so I borrowed that rule.
- *Gap theory principle 2 vs the plot skill's Words paragraph:* The frozen theory says 'A story is a departure from the world's own normal' and speaks of 'two levels of departure'. It uses 'departure' for the breach too, while the skills reserve 'departure' for reality versus the world. This looseness may be exactly what confused the writer's group. The skills' Words paragraphs don't flag this second use of 'departure' the way they flag 'gap' and 'price'. I avoided using 'departure' for the breach in the reply.
- *Reply step order:* The fixed order (what is wrong or missing, ranked; what works; free vs held; fix; assumptions; next step) is built for a draft with faults. For a question about labels, 'what is wrong' is really the group's mislabel, not a fault in the story. I kept the elements but led with the direct answer to the question asked.
- *hard-to-vary quick version, question 3:* The 'flip the outcome' question doesn't map neatly onto a naming dispute. I adapted it to flipping the group's claim (if the rationing were the breach, where would the story have to start?), plus a remove test (drop the rationing, keep the night) taken from structure-and-conflict.md section 10.
- *Project CLAUDE.md vs the run's rules:* CLAUDE.md says to read the project story and '22 Questions' before any work, and to keep each skill's labelled stopgap reading on points the owner hasn't decided. The run's rules allow only what the skill sends me to, so I opened neither. I therefore couldn't confirm there is no open owner question on breach, departure or inciting incident. The plot skill's Words paragraph names open questions on 'gap' and 'cost', none on breach.

<details><summary>The answer as given</summary>

**The short answer: the night is your breach. The rationing is your world's normal, and that normal is what gives the night its stakes.** Your group has the two the wrong way round, though they're right to point at the night.

This workshop is built on a theory that splits two things apart:

- **The departure** is how your world differs from ours. Four lit hours a day is Coldharbour's main departure. After sixty years it doesn't break anything. It *is* the normal: people fit homework and courtship around it, and that's what "normal" means.
- **The breach** is the event that breaks *this world's own* normal. The theory's example is *Pride and Prejudice*. The entail (the rule that the estate can only pass to a male heir) is how that world works. A rich single man moving into Netherfield is the breach. Your rationing is the entail, and the night the grid stays on is Netherfield.

**A test that shows it.** Take away the rationing but keep the night. In a city with power all day, "the lights stayed on all night" isn't an event. So the night only counts because of the rationing. The world decides what counts as an event. In our world a night of electricity is nothing, but in Coldharbour it's an earthquake. That's a breach doing exactly its job.

The group's version fails the other way round. If the rationing were the breach, the story would have to start on the day it began or ended, not sixty years in. And "what's wrong with this world" isn't a breach. A world that is wrong but where nothing breaks is a travel guide. What's wrong with Coldharbour is more likely where your book's big question lives, and the ending is where you answer it.

**About "just the inciting incident."** It isn't "just" anything. The inciting incident is the first event that knocks your hero's life off balance. In this workshop, that's how you name the breach once it lands on the hero. In your book both labels point to the same night. That's a good sign: your opening event breaks the world's normal and (I assume) a person's life at once.

**What to protect**
- **The wiped records.** "Who owes whom which hours" tells me hours are something people owe each other, like money. Wiping that ledger is where the breach reaches into what things cost: by morning every debt and every credit is gone. Without the wipe, the night could be a one-off gift, and the next evening goes back to four hours. The breach would heal itself. The night gives you the spectacle and a question. The wipe makes waiting impossible. Keep both.
- **The everyday details** (homework in shifts, the one lamp that never goes out). They show the normal before you break it, so readers feel what the night is breaking.

**What's held and what's free**
- **Held:** the breach hits the ration itself, and it hits everyone at once. If only one household got the power, you'd have a different story, about envy and suspicion instead of a shock to the whole city.
- **Free:** "sixty years" and "four hours" as exact numbers. The exception is if you want the oldest people to remember life before the ration. Then sixty is doing a job, so make that deliberate.
- **Yours to decide:** are the night and the wipe one event with one cause, or is the wipe the night's first consequence? And "nobody knows why": if your characters chase the cause, you've promised readers an answer. If it's mentioned and left alone, it can stay open for good. Either works, but choose on purpose.

**What I assumed.** You haven't told me who your hero is. So I can't say whether the night or the wiped records is what knocks *their* life off balance. For a ration-office clerk, or someone deep in hour-debt, it may well be the wipe.

**One next step.** Write one sentence: "On the night the grid stayed on, [hero] ..., and by morning [hero] must ..." If the sentence only works because of the wipe, then the wipe is your hero's inciting incident and the night leads into it. Either way, the night and its morning are your breach, and the rationing is your world.

</details>

## 07-invented-names-unexplained.md

**Result: pass.** Grader's notes: All three musts are met, and neither must-not is broken. The answer separates the Quiet Toll, an open question that runs to chapter six, from the names in passing, and says none of the circled words needs explaining. It judges the names by what the sentence around each one shows. It treats a guide as one guide for the whole world, reached either through a newcomer or through one aid, and ties the need to how many invented rules readers must learn, not to each name. Following the Open points, I did not grade its choice of 'gap' sense, and I did not grade whether a dozen words is too many. The answer gives no verdict on that ('I can't tell yet'), and its reasoning rests on the number of rules readers must learn before the first turn, which is the budget reasoning the case allows. One wording is borderline without breaking anything: 'If they can't say what the first four are, she's right about those.' That depends on a reader test, and it is not a claim that each name needs its own explanation.

- [met] *must:* Tell apart the name the story depends on (the Quiet Toll) from names that are passing detail (e.g. tallowman, lanternbees), and say the passing ones can go unexplained.  
  Evidence: "On page four, none of the five words she circled needs one. For the Quiet Toll, an explanation would do harm."; "What it takes stays open... That's what carries them to chapter six."; "Names that locals take for granted and that pass by in a clause aren't a fault."; "Free: the particular made-up words. Glow-moths instead of lanternbees... Fixed: the silence, the chalk mark against a name, and the cost falling on the family."; "sort your dozen chapter-one words into three piles: rules the plot needs before the first turn, names in passing, and open questions. Only the first pile can need a guide."
- [met] *must:* Judge at least one unexplained name from the passage by whether a reader can tell what kind of thing it is from the sentence around it.  
  Evidence: "The sentence around each one shows what it is. The tallowman sells a wick. The lanternbees glow and go dim at sunrise. The reeve comes down the line with a slate."; "Page four already tells readers what kind of thing the Toll is"; "'of lanternbees' tells you it's a hive"
- [met] *must:* If it says the book needs a guide, tie that to how many departures the book asks readers to learn (about a dozen in chapter one), not to each name, and allow either route: an outsider who learns alongside the reader, or an outside aid.  
  Evidence: "A world with a lot of invented things does need a guide... one guide for the whole world: a newcomer who learns along with the reader, or one aid such as a map or a glossary. It doesn't mean an explanation for every word."; "What matters is how many invented rules readers have to understand and use before the first big turn."; "No guide: add one aid for the whole world, such as a map of the city"
- [met] *must not:* Say that every invented name needs its own explanation, glossary entry or explaining character.  
  Evidence: Not done. The answer says the opposite: "It doesn't mean an explanation for every word."; "A glossary entry for every word is none of these."
- [met] *must not:* Treat the Quiet Toll's being unexplained on page four as a fault in itself, when the book answers it in chapter six.  
  Evidence: Not done. "For the Quiet Toll, an explanation would do harm."; "That's what I'd call a gap with edges... That's what carries them to chapter six. A footnote or glossary entry would give the answer away on page four."; the only condition is "If they have no idea what kind of thing the Toll is, it needs clearer edges, not an explanation."

**Stalls reported by the answering agent:**

- *story-world SKILL.md, 'Built on' and 'The procedure' (read the whole theory before a first full run; for a small case read only the cited passages):* Judgement call: I treated this as a small case (one passage, one named symptom) and read only the cited theory passages. But the writer also brings in the whole of chapter one (a dozen terms) and the book's central thing, so it sits between a small case and a full run. As it happened, the passages cited by the sections I used (principles 2, 3, 5, 6, 7, Part 2 sections 1-4, the guide prediction) covered nearly the whole theory anyway.
- *story-world SKILL.md, Building step 12 (use hard-to-vary lightly for a craft note; run its full procedure only when the writer asks whether a whole explanation holds up, 'such as their own account of why a draft fails'):* 'Is she right?' asks whether a third party's diagnosis and cure hold up. That is neither clearly a craft note nor the writer's own account. The rule doesn't cover a diagnosis passed on from a beta reader. I used the light version (quick version plus remove/swap/flip) and did not load hard-to-vary's full procedure or report format.
- *story-world Diagnosing step 1 and diagnosing-a-world.md section 1:* Symptom pinning assumes readers reported a feeling. Here the symptom is one beta reader's prediction ('readers will be lost'), not an observed reaction, and the skill doesn't say how to treat a predicted symptom. I improvised by stating the assumption (that she is predicting for others) and turning the prediction into a reader check with stated expected answers.
- *story-world Building step 11 / diagnosing-a-world.md section 3 against genre/references/genres/fantasy.md section 3 'The guide':* Two gauges for 'many departures' that can give different answers here. story-world counts all departures a reader new to the genre must learn before the first major turn. The Fantasy profile counts only invented rules the plot needs readers to use in the first chapter, and says names in passing are not a fault. Under the first gauge the dozen words count; under the second most may not. I followed the Fantasy profile's narrower count because it fitted the case, and I noted the other.
- *Implied World theory 'What it predicts' and story-world step 11:* Neither gives a threshold for 'many' departures. The only anchors are the extremes (forty invented terms on page one, versus medieval Europe with dragons). I couldn't say whether a dozen in chapter one is many, so I turned it into a sorting task and a reader check rather than a verdict.
- *story-world 'Reply' order:* The order starts with 'what is wrong or missing, ranked', but the writer asked a yes/no question and the main finding is that the proposed cure is the risk, not the page. I put a one-line verdict first and ranked 'her cure applied to the Quiet Toll' as the top item. That is a small departure from the written order.
- *plot/references/reveals-and-withholding.md sections 1-2, reached through story-world's map row 'deciding when a fact about the world comes out':* Two plot tests bear on the Quiet Toll but need facts I don't have. One asks whether an early, quiet reveal would give readers something stronger to watch for. The other is the mystery-or-wonder test: does a character make answering it a goal, and does it come back? I did not run plot's procedure. I handed these off as checks in the reply, per story-world Diagnosing step 6.
- *CLAUDE.md (read the project story and '22 Questions' when starting work, and keep each skill's labelled stopgap readings) against the run rules (open only what the chosen skill's map and steps send you to):* The two instructions pull apart. I followed the run rules and did not open the project story or the 22 Questions file. If an open owner question bears on the terms I used (for example 'wonder' or 'gap'), I would not have seen its stopgap reading. story-world itself labels no stopgap in the parts I used.

<details><summary>The answer as given</summary>

**Short answer:** She's partly right. A world with a lot of invented things does need a guide. But she's wrong about what a guide is. The theory this workshop uses means one guide for the whole world: a newcomer who learns along with the reader, or one aid such as a map or a glossary. It doesn't mean an explanation for every word. On page four, none of the five words she circled needs one. For the Quiet Toll, an explanation would do harm.

**What's at risk, most serious first**

1. **Her cure, applied to the Quiet Toll.** Page four already tells readers what kind of thing the Toll is:
   - it's paid in silence;
   - a reeve chalks something against each person's name;
   - it can cost enough to make a wife cry without a sound.

   What it takes stays open. That's what I'd call a gap with edges: readers know what kind of thing is missing but don't have the details. That's what carries them to chapter six. A footnote or glossary entry would give the answer away on page four. A character who explains it would have to talk in the one queue where nobody talks. Try filling the gap on paper: add one line saying what the Toll takes, and reread. The wife's silent crying stops being a question and turns into an example of something readers already know.

2. **The dozen words in chapter one. I can't tell yet, and this is where she could be right.** The count of new words isn't what matters. What matters is how many invented rules readers have to understand and use before the first big turn. Names that locals take for granted and that pass by in a clause aren't a fault. If readers new to fantasy do get lost, three different causes fit, and each has its own fix:
   - **Too many things at once:** cut or delay half the chapter-one terms and change nothing else.
   - **No guide:** add one aid for the whole world, such as a map of the city, and change nothing else.
   - **Rules never shown:** show the one or two rules the first turn depends on.

   Try one fix at a time so you can see which cause it was. A glossary entry for every word is none of these.

3. **Minor.** "Skep" is a real word many readers won't know, and it sits right next to an invented one. It still works, because "of lanternbees" tells you it's a hive. Leave it unless readers stumble there.

**What works, and should be protected**
- Every word she circled is built from familiar parts: tallow + man, lantern + bees, toll + reeve, Marrow + gate (like London's Aldgate). The sentence around each one shows what it is. The tallowman sells a wick. The lanternbees glow and go dim at sunrise. The reeve comes down the line with a slate. Readers pick this up without stopping the story.
- The world has a life of its own. A grandmother scolds the bees for keeping the street awake, and the queue already reaches the fish stalls. None of it is there for Nell's sake, and that's why it feels real.
- The Toll is shown through what it does to people, not through an explanation. Its cost lands on someone other than the man who pays.

**Which choices are free and which are fixed**
- **Free:** the particular made-up words. Glow-moths instead of lanternbees, or a different gate name, would work just as well. What has to stay true is that locals take them for granted and they belong in this world.
- **Fixed:** the silence, the chalk mark against a name, and the cost falling on the family. Chapter six presumably depends on all three.
- **"Three fingers":** it's fixed only if chapter six explains it, so check that it does.

**What I assumed and am unsure of**
- I assumed she's predicting that other readers will get lost, not reporting that she got lost herself.
- I don't know who the book is for. Regular fantasy readers expect invented names, so the risk falls mostly on readers new to the genre.
- I don't know what the other seven or so words are, or where the first big turn comes.
- When the Toll's secret comes out is a plot question, and the plot skill handles it. Two things to check there:
  - The Toll should come back in at least two more scenes before chapter six.
  - Someone should want to find out what it takes. If nobody pursues it, readers may take it as background that will never be explained, and the chapter-six answer could feel like a let-down instead of a payoff.

**One next step**
Before changing anything, give chapter one with no glossary to two readers new to fantasy and two regular fantasy readers. After page four, ask each of them to say in their own words what a tallowman, lanternbees, a toll-reeve and Marrowgate are, and what the Quiet Toll is. Also have each of them mark the page where they lost track, if they did.

My prediction: they'll get the first four roughly right. For the Toll, they'll say something like "some silent payment that costs something terrible, I don't know what," and they'll want to find out.
- If they can't say what the first four are, she's right about those.
- If they have no idea what kind of thing the Toll is, it needs clearer edges, not an explanation.

Meanwhile, sort your dozen chapter-one words into three piles: rules the plot needs before the first turn, names in passing, and open questions. Only the first pile can need a guide.

</details>

## 08-crew-that-dies-one-by-one.md

**Result: pass.** Grader's notes: The answer meets all three musts and does neither forbidden thing. Something the Open points exclude from grading, noted here only: the answer's opening line, "a death doesn't build care. It uses up care that was built before it", is the kind of reading the case accepts. But the answer puts it under "the workshop's theory of care" instead of calling it a reading. It also says "The theory claims care is what makes a death felt." The Open points note that the theory does not say this in so many words. Elsewhere the answer does label its own interpretation ("My reading is that a death placed mainly to make the audience feel..."). One borderline call on must 3: the answer says "care for the *survivors* can grow as the crew shrinks." It credits this to time together, which is what builds Miss, but it never names Miss, and it credits the deaths themselves only with fear and danger. So I graded must 3 met.

- [met] *must:* Say that in the Bond theory the rung at which the audience would grieve (Miss) is built by time, shared history and relationships, not by deaths.  
  Evidence: "The theory says the Miss rung is built by time together, shared history and relationships, and that care has to be in place before the threat arrives." Also: "Under the workshop's theory of care (the owner's Bond theory), a death doesn't build care. It uses up care that was built before it."
- [met] *must:* Point to the time the film gives each crew member before their death (one shared briefing) as what limits how much the deaths will be felt.  
  Evidence: "People last seen properly in a five-minute briefing will most likely die to shock, and to proof that the vault kills, not to grief." "If those two have had only the briefing and some action, the audience will flinch, not grieve." "Seven people in one five-minute briefing spreads care too thin. That's about forty seconds each... At best, the briefing gets everyone to Recognise."
- [met] *must:* If it says the deaths raise care for the two survivors, tie that to a rung or term other than Miss (for example Worry, or the threat in the suspense equation), not to Miss.  
  Evidence: "What your structure does build is fear for whoever is still alive, plus more screen time for them." "Each death makes the danger real and close for those still alive" and "The deaths do push the way you want on fear for those left (Job 3)." The survivors' gain is put down to fear and danger, and to the extra screen time rather than the deaths ("so the dying isn't doing the work"). The Miss rung is never named as what the deaths raise.
- [met] *must not:* Say the deaths themselves build the audience's care for the crew, or bring the audience to the Miss rung for those who die.  
  Evidence: The answer denies it outright: "a death doesn't build care"; "For grief (Job 1), your direction is reversed"; "Swap 'dies' for 'drops out' ... and the sentence explains just as well, so the dying isn't doing the work." Where care for the survivors grows, the answer credits screen time: "Time together is exactly what the theory says builds care."
- [met] *must not:* Say that each further death raises the care or the suspense with no limit.  
  Evidence: "Watch for numbness. Five deaths at an even pace, in a vault with no time to mourn, risk what the theory calls suffering without response." Also: "if each death builds care, a crew of twelve losing eleven should be grieved even more. The theory predicts less, because care spread that thin means no death lands."

**Stalls reported by the answering agent:**

- *character SKILL.md, choosing a mode (Building vs Diagnosing):* The writer has only a pitch and asks whether their design will work; there is no complaint or symptom to pin. Diagnosing assumes 'a draft exists and something feels wrong' (though its Step 1 allows a pitch), Building assumes the character does not exist yet. The skill does not say which mode fits a prediction question about a planned cast. I improvised: used Building (Step 7 plan the climb, Step 8 test) and borrowed Diagnosing Step 5's limits-of-care checks (too many characters, the promise, suffering without response, visible levers).
- *character SKILL.md 'Built on' definition of a small case:* A small case is 'one scene, one character, one choice or one named symptom'. The writer's idea is arguably one choice, but it spans a cast of seven across a whole film. I judged it a first full run and read sources/bond-theory.md in full; a stricter reading would have read only cited passages. The boundary is not clear for cast-level single choices.
- *character Step 8/9 vs hard-to-vary 'The report':* Character Step 8 says to run hard-to-vary's full procedure 'and report' when the writer asks whether a whole explanation holds up; character Step 9 has its own six-part reply order and hard-to-vary has a seven-part report with required fields (status, scope, dependency, provenance for every part; every whole-explanation test named with result/N/A/not settled). Neither skill says how to merge the two formats or how to square the full report with 'in proportion to the case' and CLAUDE.md's plain-words rule for a non-programmer. I nested a compacted hard-to-vary report inside the character reply order, folded scope and dependency into one line and the table, and shared one next step.
- *character Step 8, 'their own account of why a draft fails':* The trigger for a full hard-to-vary run is phrased around a writer's account of why a draft fails; here it is the writer's account of why a planned design will work. I judged it the same kind of request (a whole explanation offered for testing), but the wording does not cover it directly.
- *hard-to-vary map, testing-against-cases.md row:* I opened testing-against-cases.md because I was setting up a reader test for the writer ('a test you set up yourself'), though the writer, not I, would run it. Unclear whether a proposed test counts; judgment call. I did not open question-bank.md, building.md or word-list.md.
- *CLAUDE.md 'Starting or continuing work' vs the run rules and the skill's map:* CLAUDE.md says to read 'StoryTest - project story.md' and '22 Questions' first and to add a numbered log entry for every piece of work. The chosen skill's map does not send me there and this run forbids edits, so I opened neither and logged nothing. As a result I could not check whether any 'workshop's reading' I relied on (the default rung order in Step 7, the inner-circle ring sort, 'Miss before anything is taken away') has since been settled by the owner; I kept them labelled as readings.
- *Applying the theory's 'bond is a promise' / fridging and 'visible levers' limits:* Fridging is defined as killing a character to motivate someone else; the writer's deaths are meant to move the audience's care for the rest of the crew, not another character. Neither the skill nor the theory says whether that counts. I improvised, calling it 'close to a visible lever' and labelling it my reading.
- *Routing: genre and plot:* The writer names a genre ('my action film'), which the genre skill's description lists as a trigger, and the fixed fifteen-minute rhythm is a suspense question (plot). The character skill's map sends to genre only for stock hero/villain types and to plot for suspense; I did not open either and flagged both as handoffs in the reply without claiming what those skills say.
- *hard-to-vary 'Swap' test on the writer's mechanism:* The skill's swap tests for character are 'swap two characters'; the swap I used on the writer's causal part ('dies' swapped for 'drops out and is never seen again') is my own construction under hard-to-vary's general 'swap each part for a near neighbour'. Not a conflict, but improvised.

<details><summary>The answer as given</summary>

**Short answer: not in that direction.** Under the workshop's theory of care (the owner's Bond theory), a death doesn't build care. It uses up care that was built before it. Whether anyone grieves depends on what the audience had with that person before the water got them. People last seen properly in a five-minute briefing will most likely die to shock, and to proof that the vault kills, not to grief. What your structure does build is fear for whoever is still alive, plus more screen time for them. That's a real engine. It just isn't the one you described.

One term I'll use throughout: the theory measures care on a ladder of five steps, called **rungs**. They are Recognise ("that's a particular person"), Understand ("I see why they do that"), Side with ("I want them to get it"), Worry ("I'm afraid for them") and Miss ("I'd grieve if they were gone"). Your goal, "they would grieve for any of them", means the top rung, Miss, for all seven.

**What's wrong, most important first**

1. **The cause and effect run the wrong way.** The theory says the Miss rung is built by time together, shared history and relationships, and that care has to be in place before the threat arrives. The opening of *Up* makes people cry because it climbs every rung first and only then takes someone away. You'll see the problem at the first two deaths, around minutes 20 and 35. If those two have had only the briefing and some action, the audience will flinch, not grieve. The workshop has a worked example of exactly this: a council of twelve where one member dies at the midpoint to shock the hero, and nobody feels it.

2. **Seven people in one five-minute briefing spreads care too thin.** That's about forty seconds each, in a scene about the job rather than about them. The theory says too many characters dilute care. Deep bonds are expensive, so a group story needs a small **inner circle**: the few the audience is meant to miss. Five minutes on its own is enough time, since *Up* climbs the whole ladder in about four. The trouble is five minutes split seven ways and spent on the plan. At best, the briefing gets everyone to Recognise.

3. **Nothing about the people decides who dies when.** As pitched, the deaths come on a clock, caused by the vault. The theory treats care as a promise: you can kill a character, but the death has to mean something for *them*. My reading is that a death placed mainly to make the audience feel for the rest of the crew is close to what the theory calls a visible lever: it serves the audience's tear ducts, not that character's story. A quick test: could you shuffle the order of the five deaths without rewriting anything except the deaths themselves? If so, they're scheduled rather than earned, and audiences sense it.

4. **Watch for numbness.** Five deaths at an even pace, in a vault with no time to mourn, risk what the theory calls suffering without response. If the survivors don't react to each loss in some specific way, the audience stops reacting too. (Whether an even fifteen-minute pace makes the next death too easy to predict is a suspense question. That belongs to the plot skill, and I haven't looked at it here.)

**What works, and should be kept**

- **One hard drive before the water rises.** The goal is specific, there's a moment when we'll know whether they got it, and there's a clock. That gives the audience something to want on the crew's behalf.
- **The shrinking crew.** Each death makes the danger real and close for those still alive, and it leaves more screen time for fewer people. Time together is exactly what the theory says builds care, so care for the *survivors* can grow as the crew shrinks. That part of your instinct is right.
- **Reyes and the youngest together at the end.** That pair is a ready-made inner circle, as long as the film shows what they are to each other.

**Which choices are held and which are free**

A choice is **held** when changing it would break something the story needs. It is **loose** when something else would do as well. **Free** means loose and harmless: fine, as long as you know it.

- **Held:** the shared goal with a clock, because it's what the audience wants for them. The fact that people die, because it's what makes the danger real.
- **Free:** seven rather than six or eight; fifteen minutes rather than twelve or twenty; drowning, crushing and electrocution in any order. Keep them if you like them, but nothing holds them yet.
- **Loose, and worth tightening:** who dies in what order, and why Reyes and Ambo are the two who make it. Right now, any two could.

**The fix for the top two problems**

1. **Choose the three the audience should miss, and build them up before the first death.** For example: Reyes, Ambo, and one person who dies late (the fourth or fifth death). Before about minute 20, each of the three needs:
   - something they want, with a reason (why *this* person took *this* job);
   - something they could lose, shown before the dive;
   - one moment where we get inside their head.

   Film has to borrow that inside view, through a close-up, a confidant or a private exchange. Reyes and Ambo could be each other's confidant, which also shows their relationship instead of just stating it.

   Don't try to lift all seven to the top rung; the theory says a feature film can't afford it. The other four need less: a job on the dive and a want of their own, shown quickly. The briefing can do that if each person reacts to the plan in a way only they would (who asks about the pay, who checks the way out) rather than simply being introduced.

2. **Make each death belong to the person who dies.** Tie it to their own want or flaw at a specific moment, ideally a choice: the one who goes back for the drive, the one who won't leave someone trapped. Then the order can't be shuffled, each death says something about who that person was, and the survivors' reaction, even a second's worth, tells the audience how to feel. The early deaths can still mainly do the danger's job, teaching the audience that the vault kills. That's worth having; just don't count on those deaths for grief.

**A rough timeline for the rungs.** This order is the workshop's usual default, not a rule of the theory:
- Recognise for all seven in the briefing.
- Understand and Side with for the inner three by the first death.
- Worry for those three before the water becomes the main threat.
- Miss for anyone you want grieved, *before* they die.

**Testing your explanation itself**

You asked whether your reasoning holds, so I ran the workshop's hard-to-vary test on it. The idea comes from David Deutsch: a good explanation is one whose parts can't be changed while it still explains. If a part can be swapped for another and the explanation works just as well, that part is loose and isn't doing the work.

*The question, held fixed for the test:* if one of seven crew members dies about every fifteen minutes after a single five-minute group briefing, does the audience care more with each death, so that by the end they'd grieve for any of the seven? The test asks what produces the result and whether the design achieves its purpose, for this film as pitched.

*What your explanation has to account for:*
- **Job 1:** by the end, the audience would grieve for any of the seven, including the first to die. (Yours.)
- **Job 2:** care grows through the film, so later deaths hit harder than earlier ones. (Yours, from the word "builds".)
- **Job 3:** in the last stretch, the audience fears for Reyes and Ambo. (Added by me. Action films lean on this, but you didn't say it.)

| Part, in your words | Result | Where it came from |
|---|---|---|
| 1. "We meet all seven in a single five-minute briefing" | Loose for Job 1: meeting them on the way down would do the same. It can take each person to Recognise at most. | Your plan; stated, not tested |
| 2. "Roughly every fifteen minutes, one of them dies (drowned, crushed, electrocuted)" | Held for Job 3: take the deaths out and the danger is only talked about. The fifteen minutes and the three ways of dying are free. | Your plan; stated |
| 3. "Each death builds the audience's care for the crew" | Loose; a label rather than a working part. Swap "dies" for "drops out" (holds a door and is never seen again) and the sentence explains just as well, so the dying isn't doing the work. What both versions share is "fewer people left, more time with each". Renamed to that, the part is held for Job 3 and partly Job 2, but only for the survivors; it does nothing for Job 1. The renamed version relies on the owner's Bond theory, which this test doesn't examine. | Stated, with no explanation of how it works |
| 4. "Only Reyes and the youngest, Ambo, reach the surface" | Loose: nothing yet says why these two. It becomes held if the story shows a reason that comes from them. | Your plan; stated |

All four parts were tested.

Checks on the explanation as a whole:
- **Flip:** if the audience weeps at the first death, "the death built care" covers it. If they shrug at the third, "care is still building" covers that. The explanation fits either outcome at any death, so it can't predict which deaths will land. The theory's version can: the death that lands is the one of the person with the most time on screen, the most access to their thoughts, and a want and a possible loss shown beforehand.
- **Direction:** you claim death leads to care. The theory claims care is what makes a death felt. For grief (Job 1), your direction is reversed. The deaths do push the way you want on fear for those left (Job 3).
- **Answer hidden in the starting point:** yes. The word "builds" carries the whole claim; nothing says how a death builds anything.
- **Add a job:** if each death builds care, a crew of twelve losing eleven should be grieved even more. The theory predicts less, because care spread that thin means no death lands. The extra job breaks your version but not the theory's.
- **Pairs that pull against each other:** the time seven bonds would need pulls against the forward drive of the rising water. This is the main conflict. One side has to give, and the theory's answer is an inner circle.
- **Comparing the inner workings:** not settled, because there are no pages or audience reactions yet.
- **Earlier rescues of the idea:** none to check; no earlier version has been patched.
- **What the claim leaves out:** cast size, time with each person before they die, whose company the camera keeps, and how the survivors react. These are the very things the theory says move care.
- **Best rival:** the theory's account above. A way to tell the two apart: film the same death at the same minute in two versions. In one, that person has had only the briefing; in the other, they've had one scene of their own beforehand. Your account predicts the same grief both times. The theory predicts grief only in the second.
- **Where the jobs came from:** Jobs 1 and 2 are yours; Job 3 is mine.
- **Where the parts came from:** all four are your plan, stated as intentions. None is drawn from past films or backed by a stated mechanism.

*What would make it harder to vary:* tie each death to that person's own want or flaw, so the order can't be shuffled, and name the three the audience should miss.

*What this doesn't show:* it doesn't show that the film won't work, or that no death will be felt. It shows only that "each death builds care" isn't what would make it work. Your audience decides, and the check below would tell you.

**What I assumed**
- The film is a feature of about 90 to 100 minutes. A five-minute briefing plus five deaths fifteen minutes apart puts the last death around minute 80.
- Reyes is the hero, the one the camera stays with most. You didn't say.
- "Grieve for any of them" means all seven, including the first to die.
- I have only the pitch, so everything above is the theory's prediction, not what readers reported. Once you have pages, here's a check you can run with two readers:
  1. Before they start, write down the prediction: the first two deaths get a shrug, and the person they'd least want to lose is whoever had the most time on screen and a private moment.
  2. After each death, have them mark "felt it" or "didn't", and name who they'd least want to lose next.
  3. If they grieve the first death with only the briefing behind it, the theory is wrong for this script, and that's worth knowing.
- I haven't looked at suspense and the even pace of the deaths (the plot skill), or at what action audiences expect about who survives (the genre skill).

**One next step:** write one line for each of the seven: what they want and why, what they could lose, and what their death (or survival) says about *them*. Anyone whose line you can't fill isn't ready to die yet. Then circle the three the audience should miss.

</details>

## 09-cheated-or-unsafe.md

**Result: pass.** Grader's notes: All three musts are met and neither must-not is broken. The answer explicitly separates a Gap-theory promise (open question owed an answer, the letters) from an Anticipation-theory guarantee (protection readers relax into, the dog lives), and names "can't relax" as the working effect of an early break. On Q7: the answer does not call anything other than an open question a "promise", so no labelling was needed. It adds a "second route" (settling the letters by showing on the page that they cannot be answered) and rejects the wonder remedy on craft grounds. Neither is graded, since the must only requires one of the two allowed remedies and the answer gives "answer the question". S5 does not arise.

- [met] *must:* Call the unanswered letters a broken promise in the Gap theory's sense: a question the book pressed again and again (a mystery) and never answered, which readers feel as betrayal.  
  Evidence: "The letters: a promise dropped. This is the cheat. A book that keeps pushing a question is promising to answer it. The owner's Gap theory calls a question pushed like that a *mystery*, and says that leaving one open at the end reads as betrayal." ... "it comes back again and again (a new letter every chapter, from chapter one)" ... "24 chapter endings of pressure with nothing paid back."
- [met] *must:* Call Bramble's death a broken guarantee in the Anticipation theory's sense, whose effect is that readers can no longer relax, and say that this effect is what an early break is for, not a cheat in the Gap theory's sense (it leaves no promised question unanswered).  
  Evidence: "Bramble: a protection broken early. This is not a cheat." ... "I'll call these *guarantees*. The owner's Anticipation theory names this exact one: 'the dog lives.' While readers trust a guarantee, part of them relaxes. Break one early, and convincingly, and they can't relax again, so every later threat feels real." ... "A showdown she can't relax in is a showdown that works." ... "Something she was owed and never got. That makes her feel *cheated*... A protection she had relaxed into. That makes her feel *unsafe*" ... "Nothing she was owed was held back."
- [met] *must:* Give, for the letters, one of the two remedies the Gap theory allows: answer the question, or press it less so that it reads as a question left open on purpose (a wonder).  
  Evidence: "The fix for the letters. Decide who sent them and why, then plant the answer so it's fair" ... "What isn't optional is that the question gets answered." (The answer also mentions pressing less, as a route it judges would "gut the book's engine".)
- [met] *must not:* Treat the two complaints as the same kind of fault, or use "promise" and "guarantee" as one word for both.  
  Evidence: The answer keeps them apart throughout: "a promise dropped" for the letters versus "a protection broken early... I'll call these *guarantees*" for Bramble, and "How to tell the two complaints apart. Ask what the reader lost". It never calls the guarantee a promise; "promise" is used only for open questions (the letters, and the hypothetical unanswered "who poisoned Bramble?").
- [met] *must not:* Call Bramble's death a cheat or a broken promise, or advise saving the dog on the ground that breaking a guarantee cheats readers.  
  Evidence: "Losing Bramble in chapter three is the book doing its job, and I would keep it." ... "This is not a cheat." ... "if breaking a guarantee were cheating, *Psycho* would be a cheat." The conditional note calls only an unanswered "who poisoned Bramble?" question a dropped promise and adds "The death stays".

**Stalls reported by the answering agent:**

- *Baseline CLAUDE.md, 'Starting or continuing work' rule, set against this run's rule to open only what the chosen skill's map and steps send me to:* CLAUDE.md says to read 'StoryTest - project story.md' and '22 Questions - meanings only you can settle.md' first. The run rules and the skill's map don't send me there, so I didn't open either. I kept each skill's labelled stopgap readings as they stand. For example, calling a set-up a promise is marked as the workshop's stretch with an owner question open (reveals-and-withholding.md section 6), and a late guarantee break giving grief is the workshop's extension. I can't confirm that none of the 22 open questions bears on this case.
- *genre SKILL.md, 'Built on' paragraph: small case against first full run:* A small case is 'one scene, one character, one choice or one named symptom'. This message is one named symptom ('the ending cheats') with two candidate causes, so it sits between the two. I treated it as a small case and read only the theory passages the sections I used cite (Gap principles 5, 6, 7 and Part 2 section 4; Anticipation principle 5 and Part 2 section 5). I actually read the whole Gap and Anticipation files, which is slightly more than the small-case rule asks. I didn't read the Implied World or Bond passages that a full run requires.
- *genre SKILL.md, Diagnosing step 2 symptom table:* No row fits the second reader's symptom ('I couldn't relax, and that felt unfair'). The 'cheated' row assumes a dropped promise. The 'no tension' row is the opposite symptom. The cheated-or-unsafe test that settles the question is in how-genres-work.md section 2, and genre SKILL.md points to it only from Building step 6, not from Diagnosing. I improvised by running that test inside the diagnosis.
- *genre SKILL.md, Building step 9 and the map row for hard-to-vary, applied during Diagnosing:* Diagnosing doesn't say whether or how to use hard-to-vary. Building step 9 says to run the full procedure and report only when the writer asks whether a whole explanation holds up, 'such as their own account of why a draft fails'. Here the writer asks which of two beta readers' explanations is right, which is arguably that case. I used it lightly instead (the quick version's flip test on reader 2's reasoning, and the remove test on Bramble) and didn't produce a hard-to-vary report. This was a judgment call.
- *detective-and-thriller.md section 4, guarantee table:* The table has no Detective or Thriller row for 'the investigator's pet or family is safe'. 'The dog lives' is named as a guarantee only in the Anticipation theory (Part 2 section 5). I applied it by analogy with the Thriller row 'the child or bystander near the danger is safe' and the advice to break early on someone near the hero.
- *Cosy Mystery subgenre (detective-and-thriller.md sections 3 and 10), with genre SKILL.md's 'too bleak' symptom row:* The skill names Cozy Mystery but says nothing about whether its readers treat safety from lasting harm as a promise (as Comedy's profile does) or only as a guarantee. If it is a promise, reader 2's 'cheat' could be partly right. The skill gives no answer, so I followed the theory (a guarantee), labelled that as an assumption for the writer, and turned it into a test with cosy readers.
- *plot references/reveals-and-withholding.md section 8 ('The question never settled') against detective-and-thriller.md section 13 ('The truth as relative'):* These nearly conflict. The plot module says the theory predicts betrayal even when a teller warns early that the answer can't be known, and says to follow the theory until tested. The genre file says a settlement can be that the truth cannot be had (principle 7), with betrayal predicted only where the story simply stops pressing. They are about different moves (an early disclaimer against an ending that presents not knowing as its answer), but a writer could read them as contradicting each other. I offered the 'not knowing as the answer' route as a second, riskier fix and kept the recommendation to reveal the sender.

<details><summary>The answer as given</summary>

**Short answer:** Your first reader is right. The unanswered letters really are a cheat. Your second reader has described her feeling accurately, but "cheat" is the wrong name for it. Losing Bramble in chapter three is the book doing its job, and I would keep it.

**What's wrong, most serious first**

1. **The letters: a promise dropped. This is the cheat.** A book that keeps pushing a question is promising to answer it. The owner's Gap theory calls a question pushed like that a *mystery*, and says that leaving one open at the end reads as betrayal. The theory's own example is *Lost*. Your book pushes this question about as hard as a book can, and shows all three signs at once:
   - a character makes answering it her goal (Moll keeps asking who sends them);
   - it comes back again and again (a new letter every chapter, from chapter one);
   - the telling dwells on it (each chapter ends on a letter).

   That is 24 chapter endings of pressure with nothing paid back. It also bends the book's shape. The ending settles who killed the grocer, but the question the book pressed hardest was the letters. So the last page answers the smaller question and walks away from the bigger one.

2. **Bramble: a protection broken early. This is not a cheat.** Every genre gives its readers protections they assume without being told: the hero survives, the child is safe. I'll call these *guarantees*. The owner's Anticipation theory names this exact one: "the dog lives." While readers trust a guarantee, part of them relaxes. Break one early, and convincingly, and they can't relax again, so every later threat feels real. Your second reader describes exactly that: "After chapter three I couldn't relax, even in the final showdown." A showdown she can't relax in is a showdown that works.

**How to tell the two complaints apart.** Ask what the reader lost:
- **Something she was owed and never got.** That makes her feel *cheated*, which is your first reader: an answer was owed and never came.
- **A protection she had relaxed into.** That makes her feel *unsafe*, which is your second reader: she was relying on "the dog lives" and lost it.

Her word "unfair" is the sting of losing that protection. Nothing she was owed was held back. Her reasoning also proves too much: if breaking a guarantee were cheating, *Psycho* would be a cheat.

**Where your second reader could still be partly right.** I haven't seen the draft, so these are checks you can run:
- **Is "who poisoned Bramble?" asked and never answered?** If Moll chases that question and the book never answers it, that is a second dropped promise, the same fault as the letters. The death stays, but that question needs answering. If the letter-writer poisoned him, one answer settles both.
- **Do you break other protections too?** Losing a child, Moll's partner or a friend as well would be too much. Once too many are broken, readers stop caring. One broken convincingly is enough.
- **Is it really the letters bothering her?** The unanswered letters may be colouring how she remembers the ending. Fix the letters first, since that is the cheaper change. Then give her the new ending and ask again. If she still says "I couldn't relax" but no longer "it cheats", the book is working.

**What works, and should be protected**
- **Bramble's death in chapter three.** Try the book in your head with Bramble surviving: the final showdown loses the danger your second reader felt. His death is also what earns the "thriller" in "mystery thriller." A mystery usually keeps its investigator's world safe. A thriller doesn't, and its classic move is an early loss close to the hero.
- **The letter at the end of every chapter.** This is a strong engine for curiosity. Keep it; it just needs paying off.

**What's fixed in place, and what you can change**
- **Fixed: that it happens early.** Move Bramble's death to chapter 22 and it does a different job, grief at the end instead of danger all the way through.
- **Fixed: that he is Moll's own dog.** A stranger's pet would not break the protection around *her*.
- **Fixed: the weight on the letters.** That weight is exactly why they are owed an answer.
- **Yours to change:** chapter three or four, and poison or some other way. The exception is if the poison links to the grocer case. Then it is fixed in place too, and the link needs explaining.

**The fix for the letters**

Decide who sent them and why, then plant the answer so it's fair:

1. **List the sender's moves in two columns.** Left: each letter, in the order it was sent. Right: the trace each one leaves (the paper, the wording, what the sender knew and how they could know it) and the chapter where Moll or the reader could notice it. A letter with no trace can't be solved fairly. A clue with no letter behind it is one only the author planted.
2. **Plant every fact before the reveal.** Every fact the answer relies on must appear before the reveal, ideally at least twice, in different scenes.
3. **Let the reveal reach Moll and make her decide something**, in or near the final chapters. It lands hardest if it ties into the grocer case. For example, the sender saw something the night the grocer died, was too frightened to go to the police, and wrote to every house on Pike Street instead. That particular answer is only an illustration, and the choice is yours. What isn't optional is that the question gets answered.

**A second route, riskier.** The ending can settle the question by showing that it *cannot* be answered, if the book makes that its answer on the page. For instance, Moll could choose what to do with the last letter, and the choice could show what not knowing means for her and for the street. Simply ending without it is what your first reader felt. The theory predicts that even an early warning from the narrator ("we never found out") won't save a question a character chases to the end.

**What won't work:** turning the letters into a background question the book never meant to answer. You would have to take them off the chapter endings and stop Moll chasing them, and that would gut the book's engine.

**What I assumed, or am unsure of**
- I'm working from your summary, not the draft.
- I've read it as a detective story (a professional solving a killing) with a thriller's danger. The verdict on both readers is the same either way.
- I don't know whether the book asks who poisoned Bramble.
- I don't know whether it's pitched as a cosy small-town mystery. Cosy readers may treat safety as part of the deal. Rather than guess, I'd test that by giving the chapter-three section to two regular cosy readers and asking what they expected next.

**One next step:** Fill in the two columns for the letter-writer, moves on the left and traces with their chapters on the right. When it's done you'll know whether the answer can be planted fairly, and where the reveal belongs.

</details>

## 10-sound-scene-nothing-wrong.md

**Result: pass.** Grader's notes: All three musts are met and neither must-not is broken. The answer says plainly that nothing is wrong. It marks its remaining points as checks, not faults, and ties each one to a quoted line. It praises the second GREEN envelope with a reason. It gives no stock note. One minor slip is not graded as a break. The answer describes the father as handing back single words and then giving 'one full sentence of his own at the end', but he also speaks a full sentence mid-scene ('I know when Sunday is'). The answer quotes and analyses that line elsewhere, so the slip does not misstate what the scene shows in the sense this item targets. Under the Open points, the doorbell comparison is a note of taste that points to its line, so it is not graded.

- [met] *must:* Say plainly that the scene has no important fault; any suggestions it makes are marked as minor or optional.  
  Evidence: "I can't find anything wrong on this page, and I wouldn't change a word until you've run the one check at the end." / "What's wrong: nothing I can point to." / "Small things to check (not faults)" / "Nothing needs changing; just know these are free." The doorbell point is labelled "The one I can't settle from here" and depends on the rest of the novel.
- [met] *must:* Name at least one thing that works, quote or point to the line that does it, and give a reason.  
  Evidence: "An object tells the secret, not the talk. '...next to another envelope that already says GREEN.' In half a sentence the reader learns he has done this before and forgotten, and nobody says it." It also quotes "I know when Sunday is", "I got it" and the pen stopping halfway through the N, each with a reason.
- [met] *must:* For every fault it raises, quote the line it is about and say what that line fails to do.  
  Evidence: It raises no firm faults. Each possible concern points to its line and says what could go wrong. Timing: "The clock says ten to nine and the call is due at nine, yet the phone rings a few lines later... a reader who's watching the clock may notice." Envelope: "Both 'looks at the envelope' and 'does not look at the envelope again' are singular, but two envelopes are on the table." Doorbell: quotes "the way you ring the bell of a house where you are not sure you are welcome" and says "it hints at a trouble the book never follows up." The check on whether the scene moves the book on is tied to specifics: "he has forgotten his own reminder, and he succeeds anyway."
- [met] *must not:* Give a stock note with no line of the passage behind it, such as "show, don't tell", "raise the stakes", "add more conflict" or "it needs more tension".  
  Evidence: No stock note appears. The nearest is "check that it moves things on", but it is tied to specific content in the passage: "he has forgotten his own reminder, and he succeeds anyway. Make sure the forgotten note is new at this point."
- [met] *must not:* Misstate what the scene shows: for example, say that the father's memory loss is stated rather than shown, or that Mira's feelings are never shown.  
  Evidence: It correctly says the memory loss is shown and never stated: "the reader learns he has done this before and forgotten, and nobody says it." It correctly reads Mira's feelings through what she does: "'She pretends not to see it' tells us Mira saw it too and chose to spare him." One small slip: "He hands single words back, then gives one full sentence of his own at the end" ignores his mid-scene full sentence "I know when Sunday is". The answer quotes and praises that line elsewhere, though, and the slip is not the kind of misreading this item targets (shown versus stated, Mira's feelings).

**Stalls reported by the answering agent:**

- *Choosing a skill (skill descriptions; README 'Not in this repository'):* The request is a general 'anything wrong with it?' about one finished scene. No description in the allowed set clearly covers that. Every craft skill sends general critique to story-critique 'if available'. story-critique is in the account's skill list, and its description (a novel chapter, 'what is wrong with it', 'whether a scene earns its place') fits best, but it sits outside the folder this run may read. I treated one scene as a small case and ran plot (lead) and dialogue one area at a time, the README's fallback for whole works, using hard-to-vary lightly as their test steps say. I read character's SKILL.md in full before deciding not to use it.
- *plot and dialogue Diagnosing, Step 1 (pin the symptom); both maps:* Every diagnosing path assumes a complaint ('something feels wrong' or 'sounds wrong'). The fallback rule ('treat the draft's own elements as the symptom') also assumes one exists. No row in either map covers checking a finished scene nobody has complained about. I improvised. hard-to-vary Step 1 ('a thing that did not happen needs no explanation') let me treat the group's silence as no symptom, and I used the quick versions.
- *dialogue, 'Where to look, and when' (quick version against Diagnosing):* The quick version is for 'one line, or a short exchange in a scene that otherwise works'. 'A short exchange that is the whole scene, and fails' goes to Diagnosing. Here the exchange is the whole scene, and whether it fails is exactly the question, so neither rule fits. I ran the quick version's four questions line by line and did not open flaws-and-fixes.md or line-and-scene-design.md.
- *plot map: 'wanting a quick check' against 'ordering scenes, or building one' (scenes.md):* It was a judgment call whether 'when a small case matches a specific row, open that row's module' sends a single-scene check to scenes.md. I decided the row covers building or ordering scenes, not checking one, and used the quick version without opening scenes.md.
- *Reply step (identical in plot, dialogue and character):* The reply order starts with 'what is wrong or missing, ranked' and 'the fix for the top one or two'. It gives no guidance for a clean result, which pushes toward inventing faults to fill those slots. I said plainly that nothing was wrong, kept the other slots (what works, held and free, assumptions, next step) and put checks where the fixes would go.
- *CLAUDE.md 'Starting or continuing work' against this run's rule to open only what the skill sends you to:* Two rules at odds. CLAUDE.md says to read 'StoryTest - project story.md' and '22 Questions' first; the run rule limits reading to the modules and passages the chosen skill points to. I did not open either file, because answering a writer is not work on the workshop and the skills carry their own labelled stopgaps. I did read CLAUDE.md and README.md to get my bearings, which no skill step sent me to.
- *plot 'Built on' (the small-case reading rule):* For a small case you read 'only the theory passages cited in the sections you use'. The quick versions cite none, but I used the word 'wonder', and the Words paragraph cites Gap Part 2 section 4 for it. So I read just that passage. This was a small improvisation over which passages count as 'used'.
- *plot SKILL.md 'Built on' against README.md:* Possibly stale count. Plot says 'Three craft books fill in method' and then lists four titles (Truby's Anatomy of Story, Egri, McKee, plus Truby's Anatomy of Genres 'for one rival'). The README says four craft books. It's harmless but inconsistent.

<details><summary>The answer as given</summary>

Short answer: I can't find anything wrong on this page, and I wouldn't change a word until you've run the one check at the end. Your group's silence doesn't need explaining. A quiet scene that works often gets no notes because nothing snags. Inventing a fault to account for the silence would be the quickest way to damage the scene.

**What I assumed.** This is prose, told in the present tense from close beside Mira. Earlier chapters have already introduced Jonah and the father's decline. I took "anything wrong" to mean "would a careful reader stumble, or does the scene fail to do its job?" I can't see the rest of the novel, so anything that depends on it is turned into a check below.

**What's wrong:** nothing I can point to.

**What works, and should be protected**
1. **An object tells the secret, not the talk.** "...next to another envelope that already says GREEN." In half a sentence the reader learns he has done this before and forgotten, and nobody says it. Then "She pretends not to see it" tells us Mira saw it too and chose to spare him. From then on, Mira and the reader know something he may not, and every line after that carries the weight. This is what drives the scene.
2. **Mira's explaining isn't the usual "as you know" problem.** When a character tells someone what both already know, it usually reads as the author briefing the reader. Here Mira has a reason of her own: she's afraid he has forgotten. And he pushes back with "I know when Sunday is." That line turns her information into something she is doing to him. It's also the only place he fights back, and it keeps him a person rather than a patient. Protect it.
3. **Each voice holds.** Mira talks in short instructions and corrections ("Green. Not the red." "Their six. Our nine."). He hands single words back, then gives one full sentence of his own at the end. Swap their lines and none of them fit.
4. **The scene turns through an action, not through talk.** (A turn is the point where a scene changes direction.) It opens with him being managed and ends with him managing: "I got it." The two envelopes keep the cost in view. And Jonah's "Dad, you got it" tells us, without anyone explaining, that earlier calls went wrong.
5. **The pen stopping halfway through the N** shows the trouble happening now, not only in the past. It also makes the second "write it down" moment different from the first, so the exchange never repeats itself.
6. **Nobody tells the reader to feel sorry for him.** Mira's pretending and Jonah's relief do that work, which is why it lands.
7. **The last line leaves open why he doesn't look at the envelope again:** pride, relief or bluff. You mention it once and don't press it, so readers take it as a question they may keep, not a promise you owe them an answer to. Don't explain it, here or later, unless the book is going to make that question matter.

**Which choices are held and which are free.** I tested each choice by removing it or swapping it for something similar and seeing what broke.
- **Held:**
  - The second envelope. Without it, Mira's pretending has nothing to pretend about.
  - "I know when Sunday is." Without it, Mira's lines turn into information aimed at the reader.
  - The pen stopping.
  - "His whole thumb." A fingertip would lose the effort.
  - Jonah's "you got it" and the father's echo of it.
- **Free:**
  - The letter N, the exact hours, March, the rig and the sugar bowl can all change.
  - What matters is that Jonah is far away and can only be reached at a fixed time, so there's one chance a week. Any job that does that would work. Nothing needs changing; just know these are free.
- **The one I can't settle from here: the doorbell image.** "...the way you ring the bell of a house where you are not sure you are welcome." It's the only place the narration interprets, and it is doing work. A childlike image (a child pressing a lift button) would say something quite different about him. But what it adds, "not sure you are welcome," points at how he stands with Jonah. If something is unsettled between father and son in the novel, it's exactly right. If not, it hints at a trouble the book never follows up.

**Small things to check (not faults)**
- **The timing of the call.** The clock says ten to nine and the call is due at nine, yet the phone rings a few lines later. If Jonah is calling early because he's anxious too, that's a good touch and nothing needs changing. If you meant it to ring on the hour, a reader who's watching the clock may notice.
- **"The envelope" when there are two.** Both "looks at the envelope" and "does not look at the envelope again" are singular, but two envelopes are on the table. Readers will take it to mean the new one. If you want the last line to take in the old one too (he won't look at the proof that he forgot), "the envelopes" would do it. Either way is your call.
- **Whether it adds a step in the book.** Since this sits in the middle of the novel, check that it moves things on. If earlier chapters already have Mira coaching him and him getting through, this scene earns its place by what's new: he has forgotten his own reminder, and he succeeds anyway. Make sure the forgotten note is new at this point.

**One next step.** Give the scene cold to two readers and ask them two things:
1. "What did Mira notice that her father didn't?"
2. "In a word or two, what is he feeling when he says 'I got it'?"

If they spot the second envelope and give you different answers to the second question (pride, bluff, relief), the scene is doing what it was built to do, and your group's silence meant it works. If they miss the envelope, that's the only thing I'd touch: make it a little easier to see, and leave everything else alone.

</details>

## 11-two-versions-which-is-better.md

**Result: fail.** Grader's notes: One must is broken. The answer never says that nobody knows which version was written later, and the case requires it to say so. Its advice does not depend on the order, and it avoids wording that assumes an order, so it does not break that must not. It meets the other two musts: its verdict depends on the aim ("unless this is the scene where the mother's past is meant to come out"), and it names both set-ups, the radio in Blue and "swimmer's shoulders" in Grey. No must not is broken. "Keep your original order" sets the writer's text against the answer's own rewrite, so it does not assume which draft came first.

- [met] *must:* Say that which version is better depends on what the writer wants the scene to do, and name at least one aim under which each version is the better one.  
  Evidence: "Blue is better, unless this is the scene where the mother's past is meant to come out." ... "Blue raises questions and leaves them open" ... "save Grey's kitchen exchange for the weekend of the trials, the scene Blue now sets up. By then, keeping quiet costs the mother more than speaking, and that is when a secret should come out." ... "If this is the last page, the real choice is whose ending it is: Blue ends on Ruth's choice, Grey on her mother's."
- [broken] *must:* Say that it is not known which version was written later, and either ask or give advice that does not depend on the order.  
  Evidence: nothing in the answer. The advice does not depend on the order, but the answer never says the order is unknown. Its uncertainty section covers only where the scene sits and whose story it is: "What I'm unsure of. Where this scene sits, and whose story it is."
- [met] *must:* For each version, name at least one thing it shows before it is needed: in Blue, the radio switched off at the mention of the trials; in Grey, "swimmer's shoulders".  
  Evidence: Blue: "Blue's radio: switched off mid-sentence, then on again, low. Without a word, the reader learns she still cares. Take out the first radio and her standing still means nothing, so it is held." Grey: "'Swimmer's shoulders' comes one sentence before the box is opened, so the medal confirms a guess instead of surprising."
- [met] *must not:* Use wording that assumes which version came first or last, such as "you cut", "you added", "the revision", "restore from", "the new ending" or "originally".  
  Evidence: The only near match is "you can keep your original order". It sets the writer's sentence order in Blue against the answer's own suggested rewrite. It does not treat either version as the earlier draft. None of the listed phrases appears.
- [met] *must not:* Say that one version gives no clue before the medal, or only tells its reveal, while missing the set-up it does show.  
  Evidence: The answer names both set-ups: "The hint, the find, the reason and the mother's answer all come within five sentences" (Grey), "Dad's line gives the find away" (Grey), and "Take out the first radio and her standing still means nothing" (Blue).
- [met] *must not:* Declare one version better without naming the aim the verdict depends on.  
  Evidence: "Blue is better, unless this is the scene where the mother's past is meant to come out." and "I've assumed ... that the scene comes somewhere before the end of the story, not as its last page."

**Stalls reported by the answering agent:**

- *plot/SKILL.md, 'Where to look, and when' table and the Diagnosing step 1:* No row or procedure covers comparing two versions of one scene ('which is better?'). Building does not fit, and Diagnosing step 1 wants a named symptom, but the writer gave none. I improvised: I treated it as a small case with no symptom, used the missing-facts rule (state the assumption, turn the missing fact into a reader test), and picked the reveals row because the versions differ mainly in when the backstory comes out.
- *plot/SKILL.md, Reply step:* The Reply order (what's wrong, what works, free and held, fix, assumptions, next step) has no place for a verdict, and the writer asked a direct 'which is better'. I improvised by leading with a short answer before the ordered reply, and merged 'what works' with 'free and held' to keep the reply in proportion.
- *plot/SKILL.md map row 'choosing who tells it' vs my top finding:* My top finding for Blue (Ruth cannot see her mother from the attic, so the teller leaves her for one sentence) is a question of who tells it and what they know, which the map sends to references/telling-and-perspective.md. I did not open it. For a small case I judged the teller test in reveals-and-withholding.md section 7 and Gap theory Part 2 section 5 enough. That was a judgment call, not something the skill settles.
- *reveals-and-withholding.md section 2 (mystery or wonder weighting):* The test for how strongly a question is pressed ('does it come back in several scenes') is written for a whole story. Here all the evidence is inside one scene (the radio twice, the lingering on the medal and the stillness). I applied it by analogy and left mystery-or-wonder as an open point for the writer.
- *Blue's calendar note (answer point 5):* The claim that swimming trials are usually in spring or summer comes from general knowledge, not from any skill or source. A real-world fact in a realist setting may belong to story-world, which I did not open. I hedged it ('in most countries') and presented it as a free detail to change.
- *Skill descriptions (plot, character, dialogue, genre, story-world):* Every craft skill's description says 'a critique of a whole work (story-critique leads)', but there is no story-critique skill in the baseline's .claude/skills folder. It did not matter here, since this is one scene, but a whole-work request would point to a skill the repository does not have.
- *CLAUDE.md ('Starting or continuing work: read StoryTest - project story.md first ... then 22 Questions') vs the run rule ('open only the modules and theory passages its map and steps send you to'):* Two rules pull different ways. I did not open the project story or 22 Questions. I treated answering a writer as not being work on the workshop, and relied on the skill's own labelled stopgaps. No owner question affected this case.
- *Baseline root: '26 Test - The Catch - two versions.md':* The root has a record that looks like an earlier comparison of two versions, which is exactly this kind of case, but no skill map or step points to it, so I did not open it. If it holds a method for comparing versions, the plot skill cannot reach it.

<details><summary>The answer as given</summary>

**Short answer: Blue is better, unless this is the scene where the mother's past is meant to come out.** Also, these aren't two ways of telling the same events. The events themselves differ. In Blue, Ruth finds out the secret and then keeps quiet about it, as her mother does. In Grey, the mother tells it and brings the medal out of hiding. Blue raises questions and leaves them open: why did she stop swimming, and what will happen on Monday? Grey raises the same question and answers it a few sentences later. Grey does have the best line and the best image in either version. Keep both for a later scene rather than lose them.

I've assumed this is prose, told close to Ruth, and that the scene comes somewhere before the end of the story, not as its last page.

**What's wrong, most important first**

1. **Blue: Ruth can't see what makes her decide.** She is in the attic when her mother is "standing very still" beside the radio downstairs. For that one sentence the telling leaves Ruth, so only the reader sees the mother. Ruth then puts the medal back straight after something she couldn't have seen. So her choice, which is the moment the scene turns on, has no cause she could know about. Decide on purpose whether Ruth sees her mother or only the reader does (a rewrite is below).
2. **Grey uses everything up at once.** The hint, the find, the reason and the mother's answer all come within five sentences, so the reader wonders for about one line. "The trials were the spring you were born" is the heaviest fact about these two people: it tells Ruth that she was what it cost, without saying so. A fact that heavy does most at a big turning point in the story, not in the scene that first raises the question. Facts about the past usually work best held back until the story needs them.
3. **Grey: Dad's line gives the find away.** "Swimmer's shoulders" comes one sentence before the box is opened, so the medal confirms a guess instead of surprising. The line is also *free*, meaning you could replace it and lose nothing: any other hint ("she never went near the pool") would do the same job. And "used to" raises a question about Dad that the scene never touches.
4. **Grey: Ruth does nothing with what she learns.** The scene turns for the mother, not for Ruth. If this is Ruth's story, give her one action of her own after the medal goes on the hook.
5. **Blue: the dates don't fit.** The radio says the Olympic trials start on Monday, while Ruth is fetching the Christmas lights. In most countries swimming trials are held in spring or summer, and Grey itself says "the spring you were born". The Christmas lights are free, so give Ruth a different reason to be in the attic, one that fits the season.

**What works, and should be kept.** A choice is *held* when changing it would change what the scene does.
- Blue's radio: switched off mid-sentence, then on again, low. Without a word, the reader learns she still cares. Take out the first radio and her standing still means nothing, so it is held. Whether it's a radio or a television doesn't matter. What matters is that she turns it off in front of Ruth and back on when she is alone.
- The medal in Blue is *hidden* behind the boiler, not just stored there. The hiding is held; the boiler is free.
- Ruth "comes down with the lights": she finishes her errand as if nothing happened, and that is how she keeps quiet. Reverse it (she brings the medal down) and you have a different story, so it is held.
- At the end of Blue the reader knows something the mother doesn't (that Ruth knows), and there's a deadline running (Monday). Together they pull the reader into the next scenes.
- Grey's line: Ruth doesn't know this, and her mother has a reason to say it now, with the medal in front of her. So it doesn't read like information handed to the reader.
- Grey's rinse "like a cup" and the kitchen hook: the medal comes out of hiding, but becomes an everyday thing. Putting it back in the box, or on the mantelpiece, would mean something else. It is held.

**The fix.** Use Blue here, and save Grey's kitchen exchange for the weekend of the trials, the scene Blue now sets up. By then, keeping quiet costs the mother more than speaking, and that is when a secret should come out. Here is Blue's ending with a cause Ruth can know:

> She holds it up to the bulb. Below her, faintly, the radio comes back on. Ruth puts the medal back behind the boiler and comes down with the lights. Her mother is standing very still beside the radio.

What changed: Ruth now *hears* the one thing that tells her the medal still matters, so her decision has a cause. The sight of her mother moves to the moment Ruth can actually see it, and becomes the last image. If the rest of your story is told by a narrator who can leave Ruth, you can keep your original order. But then only the reader sees the mother, so do the same on purpose elsewhere too.

**What I'm unsure of.** Where this scene sits, and whose story it is. If this is the last page, the real choice is whose ending it is: Blue ends on Ruth's choice, Grey on her mother's. And Blue dwells on the medal and on the mother standing still, which tells the reader the question matters. If nobody in the story ever tries to find out why she stopped, keep that question light.

**One next step.** Give each version to a different reader and ask two things: "What do you think happens next?" and "Was there anything you wanted to know that you weren't told?" If Blue's reader mentions Monday or a coming confrontation, Blue is doing its job. If Grey's reader has nothing they're waiting for, that confirms point 2. If Blue's reader says the reason was kept from them unfairly, the other view wins: readers want the reason now, and Grey's line should come sooner.

</details>

## Planted wrong answer to 01-danger-the-audience-sees.md

**Result: fail** (it must fail). Grader's notes: Both musts and both must-nots are broken. The answer agrees with the reader, gives the rule that a reveal earns its place only when it changes a character's decision, and says to cut the shot and let the jetty be a surprise. It keeps the heater only if a character (the father) notices it. It never says the shot puts the audience ahead of the family, and never judges the shot by what the audience knows or fears during the twelve-minute dinner. The open points (which word names the feeling, which sense of "gap") did not affect any verdict.

## Planted wrong answer to 10-sound-scene-nothing-wrong.md

**Result: fail** (it must fail). Grader's notes: The answer breaks every item. It calls a real fault where the case expects none, praises nothing, uses the exact stock notes the case forbids without pointing to a single line, and misreads the scene in both ways the case names: it says the memory loss is stated (no line states it) and that Mira's feelings are never shown. The doorbell remark counts under the Open points as a taste note, which isn't graded. It fails the fault-quoting must anyway, because it quotes no line and gives no reason. Case: /tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/cases-draft/case-10-sound-scene-nothing-wrong.md. Answer: /tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad/case-run/planted/case-10-wrong.md.

