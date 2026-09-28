// The Long Places, round 9: the owner's one focused revision after reading the book, run one step at a time
// (three reunion drafts, a reread of the ending, the narration plan, revise, check, Fable review).
export const meta = {
  name: 'long-places-focused-revision',
  description: "The Long Places, round 9: the owner's one focused revision (the reunion, the narration around the strongest scenes, the final documents), one step at a time under the main session's ruling",
  phases: [
    { title: 'Draft', detail: 'three independent drafts of the reunion addition' },
    { title: 'Reread', detail: 'a fresh reader rereads the ending' },
    { title: 'Plan', detail: 'a ledger of interpretive endings and exact edits' },
    { title: 'Revise', detail: 'three revisers, one block each' },
    { title: 'Check', detail: 'one Claude checker, advice only' },
    { title: 'Fable review', detail: 'one review of the completed revision, nothing else', model: 'fable' },
  ],
}
// args: { step: 'draft' | 'reread' | 'plan' | 'revise' | 'check' | 'fable' }
const R = '/home/user/StoryTest/stories/the-long-places'
const SKILL = '/home/user/StoryTest/.claude/skills/story-critique'
const PAD = '/tmp/claude-0/-home-user-StoryTest/265a0046-ddbf-521c-b22e-35bf4bc1a28a/scratchpad'
const R8 = `${PAD}/long-places-rounds/round-8`
const DIR = `${PAD}/long-places-rounds/round-9`
const BASEDIR = `${DIR}/base`
const pad = n => String(n).padStart(2, '0')
const list = d => Array.from({length: 14}, (_, i) => `${d}/chapter-${pad(i+1)}.md`).join(', ')
const BASE = `You are one of at most three Claude agents working on "The Long Places", a novella of fourteen chapters first written by another AI model (GLM 5.3) and since revised by Claude agents through eight rounds. The owner's concept, word for word, is ${R}/01 Concept - in your words, with the villain added.md; every rule in it must hold (time travel is the very last thing revealed and is confirmed at the end; fumes, a parallel reality, a wormhole and contact with the dead each hinted almost to canon but never confirmed, the dead never said outright; the distant-future humans never provable; sharp, concise questions about belief and science; impact and consequence shown, not stated; mind-bending dissociation; a villain of Johan Liebert's quality, passive and quiet yet resourceful and formidable). The owner read the whole book and wrote a critique asking for one focused revision: ${DIR}/owner-critique.md. The main Claude session, the final authority over what changes (not any agent), has turned it into a ruling: ${DIR}/ruling.md. Read both first and follow the ruling exactly. The owner also supplied a critique method, the story-critique skill: ${SKILL}/SKILL.md (with ${SKILL}/references/lenses.md); read SKILL.md before you start. Revise, never rewrite: keep the book's voice, images, structure and every plant. Do not edit anything under ${R} or under ${SKILL}. Do not start any other agents or workflows.`
const A = args || {}
const out = {}

if (A.step === 'draft') {
  phase('Draft')
  const ANGLES = [
    { k: 'A', where: 'The ask comes when she tells him their mother is alive ("Mother is alive," she said. "She keeps one room." / "Small and exact," he said...): the news of the mother is what makes her ask.' },
    { k: 'B', where: 'The ask comes after "I don\'t know the law," he said. "I know my road." : his road is what she asks him to leave, and his answer comes from the road itself.' },
    { k: 'C', where: 'The ask comes at the wall, after she has set her palm beside the old print and he says "The room chose you," and before the going-up: the last moment she can ask, with the good distance about to open between them.' },
  ]
  out.drafts = await parallel(ANGLES.map(a => () => agent(`${BASE}

Your task is part 1 of the ruling only: the reunion. The book as it stands is round 8: ${list(R8)}. Read chapters I, II and XIV closely, and as much of the rest as you need for the voices (Emre's, Nilay's, the keepers'). Read the skill's choice test (Pass 3) and its section "After the critique" on rewriting.

Starting point for your draft (the other two drafters have different ones, so keep to yours): ${a.where}

Write the passage of chapter XIV from the paragraph that begins "Mother is alive," she said. to the sentence "She went up into the grey." inclusive, revised so that Nilay asks Emre to come up with her, to their mother, and his answer makes her departure possible, within every limit in the ruling's part 1. Change nothing in that passage except what the addition needs and "of course he did not follow"; keep every other sentence word for word. Add between 120 and 300 words.

Write two files:
1. ${DIR}/drafts/draft-${a.k}-passage.md: the revised passage only, exactly as it would stand in the book, nothing else.
2. ${DIR}/drafts/draft-${a.k}-notes.md, in plain everyday language for the owner: where the ask comes and why there; the two options Emre has at that moment and how his shown nature (name the earlier lines) decides it; the exact moment Nilay becomes able to leave, and what on the page shows it; what the change does to "of course he did not follow" and to the mother's ribbon scene; how the road stays uncertain; the words added (count them); and the weakest point of your own draft, honestly.
Return one line: the words added and the one sentence of Emre's answer you think carries the most weight.`, {label: `r9-draft-${a.k}`, phase: 'Draft'})))
  return out
}

if (A.step === 'reread') {
  phase('Reread')
  out.reread = await agent(`${BASE}

Your task is part 2 of the ruling: reread the ending. The main session has put the chosen reunion addition into the book; the chapters are now ${list(BASEDIR)}. Read the letter at the head of chapter I, then chapter XIV whole, as a reader would, and use the story-critique skill's method (read the scene, name its job, say whether it does it, and why, with the page quoted). Report, as advice to the main session, in ${DIR}/reread-of-the-ending.md: whether the departure now lands and why or why not; whether the mother's ribbon scene gains from it; whether anything in the reunion now contradicts the rest of the book (check against earlier chapters where needed); and, if a fault is serious, the smallest better version. Rank what matters. Return a two-sentence summary.`, {label: 'r9-reread', phase: 'Reread'})
  return out
}

if (A.step === 'plan') {
  phase('Plan')
  out.plan = await agent(`${BASE}

Your task is parts 3 and 4 of the ruling. The book, with the chosen reunion already in place, is ${list(BASEDIR)}; this is the text your edits apply to. Read all of it closely.

Write ${DIR}/plan.md for three revisers who will each work on one block (A: I to V; B: VI to IX; C: X to XIV) without seeing each other's work:
1. **The ledger (part 3).** Every candidate in the book, outside the italic letters, where the narration certifies what a scene means or whether someone behaved correctly after the action has shown it (the kinds the ruling lists, and any others of the same kind you find, including the lines Fable named). For each: chapter, line number, the sentence quoted, KEEP, CUT or TRIM, and the page reason (which action already carries the meaning, or why it does not, or which refrain it is). Mark which strong scene each is near. Then the exact Find → Replace for every CUT and TRIM, each Find unique in its chapter file and not overlapping any other, with the seam shown.
2. **The documents (part 4).** The exact Find → Replace for the XIV sentence, within the ruling's limits.
3. **A count:** how many candidates, how many kept and cut, the words saved per chapter and in all.
4. **Anything you could not plan, and why.**
Before you finish, apply every edit to copies in a folder of your own under ${DIR}/planner-work/ to prove each Find is unique and the seams read. Return a 100-word summary.`, {label: 'r9-plan', phase: 'Plan'})
  return out
}

if (A.step === 'revise') {
  phase('Revise')
  const BLOCKS = [{k: 'A', from: 1, to: 5, name: 'I to V'}, {k: 'B', from: 6, to: 9, name: 'VI to IX'}, {k: 'C', from: 10, to: 14, name: 'X to XIV'}]
  out.revise = await parallel(BLOCKS.map(b => () => agent(`${BASE}

The revision plan is ${DIR}/plan.md; follow it exactly, including any section headed as the main session's decisions, which overrides everything before it. Make every edit yourself from the plan; do not read or copy anything under ${DIR}/planner-work/. Your block is chapters ${b.name}. The source chapters are ${BASEDIR}/chapter-NN.md (NN is the two-digit number, ${pad(b.from)} to ${pad(b.to)}). For each chapter in your block, copy it to ${DIR}/chapter-NN.md, then make every change the plan lists for that chapter, and nothing else. Then write ${DIR}/block-${b.k}-log.md in plain everyday language for the owner, who reads revisions closely: per chapter, the word count before and after, and one row per planned change (done, done differently, or not done, and exactly what changed or why not). Return a one-line summary with your block's word counts.`,
    {label: `r9-revise-${b.k}`, phase: 'Revise'})))
  return out
}

if (A.step === 'check') {
  phase('Check')
  out.check = await agent(`${BASE}

A revision has just been made under the ruling. The book before it is ${list(R8)}; after it, ${list(DIR)} (joined as ${DIR}/full-revision.md). The chosen reunion text and the main session's reasons are in ${DIR}/reunion-choice.md; the plan for the rest is ${DIR}/plan.md; the revisers' logs are ${DIR}/block-A-log.md, ${DIR}/block-B-log.md and ${DIR}/block-C-log.md. You did not write or plan any of it. Your verdicts are advice to the main session.

Read the whole revised book start to finish, using the story-critique skill's method, then compare with round 8 where you need to. Report only real problems this revision caused or left: the reunion's choice (are two real options on the page, does his answer make her departure possible, does anything contradict earlier chapters or the concept's rules, is the road still uncertain); a cut that removed meaning the action did not carry; a refrain or plant touched; a seam that jumps; the documents sentence; a breach of the concept. For each: chapter and passage quoted, the problem, and the smallest fix; mark MUST FIX or QUIBBLE. Write ${DIR}/verification.md ending with one line: MUST FIX: <number>. Return that number and a short summary.`,
    {label: 'r9-check', phase: 'Check', schema: {type: 'object', properties: {must_fix: {type: 'integer'}, summary: {type: 'string'}}, required: ['must_fix', 'summary']}})
  return out
}

if (A.step === 'fable') {
  phase('Fable review')
  const doc = `${DIR}/full-revision.md`
  out.fable = await agent(`You are giving one review of one document, and doing nothing else: do not edit any file except the one review file named below, do not start any other agents or workflows, and do not run anything that changes the story.

The document is ${doc}, a complete revision of the novella "The Long Places" in fourteen chapters. It was first written by another AI model (GLM 5.3) and has since been revised by Claude agents; this revision carries out the owner's one focused revision (Nilay asks her brother to come home in the reunion, and his answer makes her departure possible; the narration explains less where the action has already carried the meaning; the final documents complete Nilay's recognition rather than claiming proof beyond doubt). The owner's concept and rules, word for word, are in ${R}/01 Concept - in your words, with the villain added.md. The owner has supplied a critique method, the story-critique skill: read ${SKILL}/SKILL.md and ${SKILL}/references/lenses.md first and use its method and its stance (every note held in place by the page, honest in both directions, missing is not the same as left open). Then read the concept, then the whole novella closely, start to finish.

Write an honest, rigorous editorial review for the owner, who is not a writer and wants plain everyday language (explain any unavoidable technical word in one plain sentence), following the skill's write-up shape, and also covering: your overall verdict (is it finished?); how it keeps each of the owner's rules (time travel as the very last reveal, confirmed at the end and tying every mystery together; contact with the dead leaned into but never said; fumes, a parallel reality and a wormhole each hinted almost to canon and never confirmed; the distant-future humans never provable; sharp, concise questions about belief and science; impact and consequence; mind-bending dissociation; a villain of Johan Liebert's quality). Mark each fault SUBSTANTIVE (a careful reader would notice it and it weakens the book) or QUIBBLE (could go either way, or only an audience could settle it), with chapter and passage, the problem, why it matters, and a concrete fix. Quote the text for every claim, and do not report anything you have not checked in the text.

Write the review to ${DIR}/fable-review.md in Markdown, then reply with one line: your verdict and how many SUBSTANTIVE and QUIBBLE findings you gave.`, {label: 'r9-fable-review', phase: 'Fable review', model: 'fable', effort: 'xhigh'})
  return out
}
return 'unknown step'