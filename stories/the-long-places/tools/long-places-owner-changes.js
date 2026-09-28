// The Long Places, round 8: the owner's three changes after the audience test, run one step at a time
// (plan, revise, check, Fable review) so the main session can check each step before the next.
export const meta = {
  name: 'long-places-owner-changes',
  description: "The Long Places, round 8: carry out the owner's three changes and four slips under the main session's ruling, one step at a time (plan, revise, check, Fable review)",
  phases: [
    { title: 'Plan', detail: 'one planner turns the ruling into exact changes' },
    { title: 'Revise', detail: 'three revisers, one block each' },
    { title: 'Check', detail: 'one Claude checker, advice only' },
    { title: 'Fable review', detail: 'one review of the completed revision, nothing else', model: 'fable' },
  ],
}
// args: { step: 'plan' | 'revise' | 'check' | 'fable' }
const R = '/home/user/StoryTest/stories/the-long-places'
const PAD = '/tmp/claude-0/-home-user-StoryTest/265a0046-ddbf-521c-b22e-35bf4bc1a28a/scratchpad'
const SRC = `${PAD}/long-places-rounds/round-7`
const DIR = `${PAD}/long-places-rounds/round-8`
const pad = n => String(n).padStart(2, '0')
const srcList = Array.from({length: 14}, (_, i) => `${SRC}/chapter-${pad(i+1)}.md`).join(', ')
const newList = Array.from({length: 14}, (_, i) => `${DIR}/chapter-${pad(i+1)}.md`).join(', ')
const BASE = `You are one of at most three Claude agents working on "The Long Places", a novella of fourteen chapters first written by another AI model (GLM 5.3) and since revised by Claude agents through seven rounds. The owner's concept, word for word, is ${R}/01 Concept - in your words, with the villain added.md; every rule in it must hold (time travel is the very last thing revealed and is confirmed at the end; fumes, a parallel reality, a wormhole and contact with the dead each hinted almost to canon but never confirmed, the dead never said outright; the distant-future humans never provable; sharp, concise questions about belief and science; impact and consequence shown, not stated; mind-bending dissociation; a villain of Johan Liebert's quality, passive and quiet yet resourceful and formidable). The owner has read two audience tests and ordered three changes; the main Claude session, which is the final authority over what changes (not any agent), has turned that order into a ruling: ${DIR}/ruling.md. Read it first and follow it exactly. Background only, if you need it: the Claude readers' analysis ${R}/40 Audience test (Claude readers) - the analysis.md and their reports ${R}/40 Audience test (Claude readers) - the five readers' reports.md. Revise, never rewrite: keep the book's voice, images, structure, chapter titles and every plant that pays off later. Do not edit anything under ${R}. Do not start any other agents or workflows.`
const A = args || {}
const out = {}

if (A.step === 'plan') {
  phase('Plan')
  out.plan = await agent(`${BASE}

The book as it stands (round 7, the finished book) is the fourteen chapter files: ${srcList}. Read all of them closely, start to finish, and the ruling.

Write ${DIR}/plan.md, the exact revision plan for three revisers who will each work on one block (A: chapters I to V; B: VI to IX; C: X to XIV) without seeing each other's work. It must let them carry out the ruling consistently. Include:
1. **Word budget.** A table of each chapter's current word count, its target (from the ruling), and the planned cut in words; the block totals; and the book total, which must land between 44,500 and 46,000.
2. **The phrase ledger.** For every phrase the ruling limits, list EVERY instance in the book (chapter, the paragraph's opening words, and the sentence quoted), and mark each KEEP, CUT, or VARY (with the exact replacement words). The KEEP counts must meet the ruling's limits exactly or below. Do the same for the "three ordinary explanations" routine (which instances stay, and what the others become) and the two too-pleased lines.
3. **Chapter by chapter, I to XIV,** a heading "Chapter N" and a numbered list of exact changes: each cut named by the passage's opening and closing words and what, if anything, joins the seam; each changed line of dialogue for the plainer voices, quoted before and after; each slip fix with its exact wording; for XIII, the exact new lines where Nilay speaks to Halden (plain, her polish gone, naming only what the book has shown: the hours he kept on that hill on the fourth and fifth of September 1999, his advice that nobody go below the fourth door, her mother's twenty-six years) and his reply "You have kept excellent records."; for XIV, the new reason for striking the third sentence, the trimmed Emre speech (quote what stays), one or two new short lines of Emre as the boy he was, the removed bracketed aside, and the cut handprint line. Give all shared wording exactly, so the three blocks agree.
4. **The plant check.** A table of every plant touched by any cut, where it is set up, where it pays off, and where each part still stands after the cuts. Nothing the ruling lists may be lost.
5. **Anything in the ruling you could not plan, and why.**
Keep every change as small as the ruling allows. Return a summary of about 100 words, including the planned book total.`, {label: 'r8-plan', phase: 'Plan'})
  return out
}

if (A.step === 'revise') {
  phase('Revise')
  const BLOCKS = [{k: 'A', from: 1, to: 5, name: 'I to V'}, {k: 'B', from: 6, to: 9, name: 'VI to IX'}, {k: 'C', from: 10, to: 14, name: 'X to XIV'}]
  out.revise = await parallel(BLOCKS.map(b => () => agent(`${BASE}

The revision plan is ${DIR}/plan.md; follow it exactly (it carries out the ruling, ${DIR}/ruling.md), including its section 6, the main session's decisions, which override anything before it. Make every edit yourself from the plan; do not read or copy anything under ${PAD}/r8work (another agent's working files). Your block is chapters ${b.name}. The source chapters are ${SRC}/chapter-NN.md (NN is the two-digit chapter number, ${pad(b.from)} to ${pad(b.to)}); you may read any other source chapter for context, but change only your own. For each chapter in your block, copy it to ${DIR}/chapter-NN.md, then make every change the plan lists for that chapter in the copy, and nothing else. Where you join a seam after a cut, the joining words must be few and in the book's voice. Count each chapter's words when you finish and compare with the plan's target; if you are more than 150 words over or under, adjust within the plan's cuts (never by cutting a plant or a keeper phrase). Then write ${DIR}/block-${b.k}-log.md in plain everyday language for the owner, who reads revisions closely: for each chapter, its word count before and after, and one row per planned change (done, done differently, or not done, and exactly what changed or why not). Return a one-line summary with your block's word counts.`,
    {label: `r8-revise-${b.k}`, phase: 'Revise'})))
  return out
}

if (A.step === 'check') {
  phase('Check')
  out.check = await agent(`${BASE}

A revision has just been made under the ruling. The book before it is ${srcList}; the book after it is ${newList} (also joined as ${DIR}/full-revision.md). The plan it carried out is ${DIR}/plan.md, and the revisers' logs are ${DIR}/block-A-log.md, ${DIR}/block-B-log.md and ${DIR}/block-C-log.md. You did not plan or revise it. Your verdicts are advice to the main Claude session, which makes the final ruling.

Read the whole revised book start to finish as a reader would, then compare it with the old one where you need to. Report only real problems that this revision caused or left:
- a plant lost or weakened, or a payoff now without its set-up;
- a seam where a cut left a jump, a dangling reference ("as she had said", "the second time"), or a fact now unexplained;
- a contradiction introduced;
- a breach of the owner's concept (above all anything that now gives away time travel before the end, or confirms one of the four explanations, or makes Halden loud, punished or less formidable);
- a changed voice that no longer sounds like that character;
- a ruling order not carried out (check the phrase limits by counting, the four slips, the Halden lines, the XIV changes, the word total).
For each: chapter and passage, quoted, the problem, and the smallest fix. Mark each MUST FIX (a careful reader would notice it and it weakens the book) or QUIBBLE. Write ${DIR}/verification.md, ending with one line: MUST FIX: <number>. Return that number and a short summary.`,
    {label: 'r8-check', phase: 'Check', schema: {type: 'object', properties: {must_fix: {type: 'integer'}, summary: {type: 'string'}}, required: ['must_fix', 'summary']}})
  return out
}

if (A.step === 'fable') {
  phase('Fable review')
  const doc = `${DIR}/full-revision.md`
  out.fable = await agent(`You are giving one review of one document, and doing nothing else: do not edit any file except the one review file named below, do not start any other agents or workflows, and do not run anything that changes the story.

The document is ${doc}, a complete revision of the novella "The Long Places" in fourteen chapters. It was first written by another AI model (GLM 5.3) and has since been revised by Claude agents; this revision carries out three changes the owner ordered after an audience test (fewer repeated phrases and plainer voices for the people who are not keepers; shorter side-trips in chapters XI to XIII; one person saying to the villain's face what he did), and four small fixes. The owner's concept and rules, word for word, are in ${R}/01 Concept - in your words, with the villain added.md. Read that first, then read the whole novella closely, start to finish.

Write an honest, rigorous editorial review for the owner, who is not a writer and wants plain everyday language (explain any unavoidable technical word in one plain sentence). Cover:
1. Your overall verdict in a few sentences: what the book is, what it achieves, whether it is finished.
2. How it keeps each of the owner's rules: time travel as the very last reveal, confirmed at the end and tying every mystery together; contact with the dead leaned into but never said; fumes, a parallel reality and a wormhole each hinted almost to canon and never confirmed; the distant-future humans never provable; sharp, concise questions about belief and science; impact and consequence; mind-bending dissociation; a villain of Johan Liebert's quality (passive, quiet, never show-stopping, yet resourceful and formidable).
3. What works best, with short quotations.
4. The problems, most serious first. Mark each SUBSTANTIVE (a careful reader would notice it and it weakens the book: a plot hole or broken logic, a contradiction, a broken rule, a character acting without cause, a villain who stops being formidable or quiet, a passage with no job, sagging pace, confusion that does not serve the dissociation, a theme stated instead of shown, a thread that goes nowhere) or QUIBBLE (could go either way, or only an audience could settle it: word choice or placement, rhythm, the exact timing of an event when nothing depends on it, taste). For each: chapter and passage, the problem, why it matters, and a concrete fix.
Be exact: quote the text for every claim, and do not report anything you have not checked in the text.

Write the review to ${DIR}/fable-review.md in Markdown, then reply with one line: your verdict and how many SUBSTANTIVE and QUIBBLE findings you gave.`, {label: 'r8-fable-review', phase: 'Fable review', model: 'fable', effort: 'xhigh'})
  return out
}
return 'unknown step'