export const meta = {
  name: 'long-places-step',
  description: 'One step of the Long Places revision rounds, with the main Claude session as final authority: revise to its ruling (if given), have Fable 5.1 review the completed revision once, then critique (three Claude critics and MiMo) and verify, and stop for the next ruling',
  phases: [
    { title: 'Plan', detail: 'plan exactly the fixes the ruling orders' },
    { title: 'Revise', detail: 'three revisers, one block each, then join the book into one document' },
    { title: 'Fable review', detail: 'one review of the completed revision, nothing else', model: 'fable' },
    { title: 'Critique', detail: 'three Claude critics and one MiMo critic mark findings substantive or quibble' },
    { title: 'Verify', detail: 'an advisory verification for the main session to rule on' },
  ],
}
// args: { review_round: R, source: folder of the version to start from, source_first: true if that folder uses the 30-chapter-NN.md layout,
//         revise_round: N (optional; revise the source into round-N using round-N/ruling.md first), fable_doc: path (optional; a completed
//         revision already joined into one document that Fable has not yet reviewed) }
const R = '/home/user/StoryTest/stories/the-long-places'
const PAD = '/tmp/claude-0/-home-user-StoryTest/265a0046-ddbf-521c-b22e-35bf4bc1a28a/scratchpad'
const ROUNDS = `${PAD}/long-places-rounds`
const MIMO_START = `${PAD}/mimo/start_long_places_critique.sh`
const JOIN = `${PAD}/mimo/join_chapters.sh`
const pad = n => String(n).padStart(2, '0')
const BLOCKS = [
  { k: 'A', chapters: 'I to V' },
  { k: 'B', chapters: 'VI to IX' },
  { k: 'C', chapters: 'X to XIV' },
]
const chapterFiles = (dir, first) => Array.from({length: 14}, (_, i) => first ? `${dir}/30-chapter-${pad(i+1)}.md` : `${dir}/chapter-${pad(i+1)}.md`)
const BASE = `You are one of at most three Claude agents working on "The Long Places", a novella first written by another AI model (GLM 5.3) and since revised by Claude agents. The owner's concept, word for word, is ${R}/01 Concept - in your words, with the villain added.md; every rule in it must hold (time travel is the very last thing revealed and is confirmed at the end; fumes, a parallel reality, a wormhole and contact with the dead each hinted almost to canon but never confirmed, the dead never said outright; the distant-future humans never provable; sharp, concise questions about belief and science; impact and consequence shown, not stated; mind-bending dissociation; a villain of Johan Liebert's quality, passive and quiet yet resourceful and formidable, and the story's own creation). Keep the book's voice, images and structure; revise, never rewrite; keep its length within ten per cent. The final authority over which findings are real and what gets changed is the main Claude session that runs these rounds, not any agent. Do not edit anything under ${R}. Do not start any other agents or workflows.`
const SEVERITY = `How to mark each finding. SUBSTANTIVE: a careful reader would notice it and it weakens the book: a plot hole or broken logic; a contradiction between chapters; a breach of the owner's concept rules (above all anything before chapter XIV that gives away time travel, or anything that confirms fumes, a parallel reality, a wormhole or the dead); a character acting without cause or against who they are; a villain who stops being formidable or stops being quiet; a scene or passage with no job; pacing that sags; confusion that does not serve the dissociation; a theme stated instead of shown; a thread that goes nowhere. QUIBBLE: it could go either way, or only an audience test could settle it: word choice or placement, sentence rhythm, the exact minute or day of an event when nothing depends on it, small matters of taste.`
const LENSES = [
  { k: 'story', p: 'STORY AND RULES: plot logic, cause and effect, the four explanations and the clue balance, the distant-future encounter, the final reveal and whether it ties every mystery, and every rule of the concept.' },
  { k: 'people', p: 'PEOPLE AND MEANING: whether we care about Nilay and the others before the strangeness bites; whether each acts from their own want and wound; whether Halden is formidable yet passive and quiet; whether the questions about belief and science are sharp and asked through events; impact and consequence; pacing and the dissociation.' },
  { k: 'continuity', p: 'CONTINUITY AND PROSE: every fact, name, date, number and object across the fourteen chapters; the seams between chapters V and VI and IX and X, where different revisers worked; repeated words and one-liners; passages that confuse without purpose.' },
]
const fablePrompt = (doc, out) => `You are giving one review of one document, and doing nothing else: do not edit any file except the one review file named below, do not start any other agents or workflows, and do not run anything that changes the story.

The document is ${doc}, a complete revision of the novella "The Long Places" in fourteen chapters. It was first written by another AI model (GLM 5.3) and has since been revised by Claude agents. The owner's concept and rules, word for word, are in ${R}/01 Concept - in your words, with the villain added.md. Read that first, then read the whole novella closely, start to finish.

Write an honest, rigorous editorial review for the owner, who is not a writer and wants plain everyday language (explain any unavoidable technical word in one plain sentence). Cover:
1. Your overall verdict in a few sentences: what the book is, what it achieves, whether it is finished.
2. How it keeps each of the owner's rules: time travel as the very last reveal, confirmed at the end and tying every mystery together; contact with the dead leaned into but never said; fumes, a parallel reality and a wormhole each hinted almost to canon and never confirmed; the distant-future humans never provable; sharp, concise questions about belief and science; impact and consequence; mind-bending dissociation; a villain of Johan Liebert's quality (passive, quiet, never show-stopping, yet resourceful and formidable).
3. What works best, with short quotations.
4. The problems, most serious first. Mark each SUBSTANTIVE (a careful reader would notice it and it weakens the book: a plot hole or broken logic, a contradiction, a broken rule, a character acting without cause, a villain who stops being formidable or quiet, a passage with no job, sagging pace, confusion that does not serve the dissociation, a theme stated instead of shown, a thread that goes nowhere) or QUIBBLE (could go either way, or only an audience could settle it: word choice or placement, rhythm, the exact timing of an event when nothing depends on it, taste). For each: chapter and passage, the problem, why it matters, and a concrete fix.
Be exact: quote the text for every claim, and do not report anything you have not checked in the text.

Write the review to ${out} in Markdown, then reply with one line: your verdict and how many SUBSTANTIVE and QUIBBLE findings you gave.`

const A = args || {}
let source = A.source
let first = !!A.source_first
let fableDoc = A.fable_doc || null
const out = {}

if (A.revise_round) {
  const n = A.revise_round
  const dir = `${ROUNDS}/round-${n}`
  const list = chapterFiles(source, first).join(', ')
  phase('Plan')
  out.plan = await agent(`${BASE}\n\nThe book is the fourteen chapter files: ${list}. The main Claude session's ruling on round ${n} is ${dir}/ruling.md. That ruling is final: it lists exactly which findings are to be fixed, and how, and which were overruled. The critiques and advisory verification in ${dir} are background only. Write ${dir}/plan.md: the revision plan for the findings the ruling orders fixed, and nothing else (never plan a change for a finding the ruling overruled or left as a quibble). Part 1, a table: each ordered finding and exactly what will change, in which chapter and passage. Part 2: for every chapter from I to XIV, a heading "Chapter N" and a numbered list of exact changes, or "No changes". Where the ruling gives wording or constraints, keep them. Keep each change as small as the problem allows, and give any shared wording exactly, so three revisers working on separate blocks stay consistent. Return a 100-word summary.`,
    {label: `r${n}-plan`, phase: 'Plan'})
  phase('Revise')
  out.revise = await parallel(BLOCKS.map(b => () => agent(`${BASE}\n\nThe revision plan is ${dir}/plan.md; follow it exactly (it carries out the main session's final ruling, ${dir}/ruling.md). Your block is chapters ${b.chapters}. For each chapter in your block, copy it from ${first ? source + '/30-chapter-NN.md' : source + '/chapter-NN.md'} to ${dir}/chapter-NN.md (NN is the two-digit chapter number), then make every change the plan lists for that chapter in the copy, and nothing else; a chapter with no changes is copied unchanged. Then write ${dir}/block-${b.k}-log.md in plain everyday language for the owner, who reads revisions closely: for each chapter, one row per planned change (done, done differently, or not done, and exactly what changed or why not). Return a one-line summary.`,
    {label: `r${n}-revise-${b.k}`, phase: 'Revise'})))
  out.join = await agent(`Run exactly this one shell command and nothing else, then reply with its output: ${JOIN} "${dir}" "${dir}/full-revision.md"`,
    {label: `r${n}-join`, phase: 'Revise', model: 'haiku', effort: 'low'})
  fableDoc = `${dir}/full-revision.md`
  source = dir
  first = false
}

if (A.final_only) {
  // The last copyedit revision: Fable gives its single review of the finished book, and no further critic round runs.
  const fdir = `${ROUNDS}/round-${A.revise_round}`
  out.fable = await agent(fablePrompt(fableDoc, `${fdir}/fable-review-of-final.md`), {label: `final-fable-review`, phase: 'Fable review', model: 'fable', effort: 'xhigh'})
  out.final_folder = source
  return out
}
const r = A.review_round
const rdir = `${ROUNDS}/round-${r}`
const list = chapterFiles(source, first).join(', ')
const fableP = fableDoc
  ? agent(fablePrompt(fableDoc, `${rdir}/fable-review.md`), {label: `r${r}-fable-review`, phase: 'Fable review', model: 'fable', effort: 'xhigh'})
  : null
phase('Critique')
out.mimo = await agent(`Run exactly this one shell command and nothing else, then reply with its output: ${MIMO_START} "${source}" ${first ? 1 : 0} "${rdir}"`,
  {label: `r${r}-start-mimo`, phase: 'Critique', model: 'haiku', effort: 'low'})
out.critics = await parallel(LENSES.map(l => () => agent(`${BASE}\n\nThe book as it stands is fourteen chapter files, in order: ${list}. You did not write or revise it. Read all fourteen, then criticise it through one lens only. ${l.p}\n${SEVERITY}\nWrite ${rdir}/critique-${l.k}.md (create the folder if needed): a numbered list, most serious first, at most 20 findings; for each the chapter and passage, the problem, why it matters, a concrete fix, and the mark SUBSTANTIVE or QUIBBLE. Only real findings. Return one line with how many of each mark you gave.`,
  {label: `r${r}-critique-${l.k}`, phase: 'Critique'})))
phase('Verify')
const v = await agent(`${BASE}\n\nThe book is the fourteen chapter files: ${list}. Three critiques of it by Claude critics are ${rdir}/critique-story.md, ${rdir}/critique-people.md and ${rdir}/critique-continuity.md. A fourth, by MiMo, a different AI model reading with fresh eyes, is ${rdir}/critique-mimo.md: weigh its findings exactly as you weigh the others. If that file is missing when you start, read the other three first and look again; if it is still missing, go on without it and say so in your summary. You wrote none of the critiques and did not revise the book. Your verdicts are advice to the main Claude session, which makes the final ruling. For every finding marked SUBSTANTIVE, check it against the book and decide: CONFIRMED (real, and substantive by the definition), QUIBBLE (real but only a quibble), or WRONG (not true of the book). Merge duplicates. Be strict both ways: taste must not pass as substantive, and a real problem must not be waved away. Quote the text that decides each verdict.\n${SEVERITY}\nWrite ${rdir}/verification.md: a table (finding in plain words, which critic, verdict, why, with the deciding quotation), then the CONFIRMED findings numbered, each with its chapter(s). Return the count, and in the summary say how many confirmed findings came from MiMo.`,
  {label: `r${r}-verify`, phase: 'Verify', schema: {type: 'object', properties: {confirmed_substantive: {type: 'integer'}, summary: {type: 'string'}}, required: ['confirmed_substantive', 'summary']}})
out.verification = v
out.fable = fableP ? await fableP : 'no completed revision to review in this step'
out.reviewed_folder = source
out.reviewed_first_layout = first
out.review_round = r
return out
