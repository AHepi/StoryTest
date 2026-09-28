export const meta = {
  name: 'fable-review-long-places-19',
  description: 'Fable 5.1 at extra-high effort gives one review of the completed Claude revision of The Long Places (file 19), and does nothing else',
  phases: [{ title: 'Fable review', model: 'fable' }],
}
const R = '/home/user/StoryTest/stories/the-long-places'
const OUT = '/tmp/claude-0/-home-user-StoryTest/265a0046-ddbf-521c-b22e-35bf4bc1a28a/scratchpad/long-places-rounds/round-1/fable-review.md'
phase('Fable review')
const r = await agent(`You are giving one review of one document, and doing nothing else: do not edit any file except the one review file named below, do not start any other agents or workflows, and do not run anything that changes the story.

The document is ${R}/19 The Long Places - revised by Claude, final.md, a complete novella of fourteen chapters. It was first written by another AI model (GLM 5.3) and has since been revised by Claude agents. The owner's concept and rules, word for word, are in ${R}/01 Concept - in your words, with the villain added.md. Read that first, then read the whole novella closely, start to finish.

Write an honest, rigorous editorial review for the owner, who is not a writer and wants plain everyday language (explain any unavoidable technical word in one plain sentence). Cover:
1. Your overall verdict in a few sentences: what the book is, what it achieves, whether it is finished.
2. How it keeps each of the owner's rules: time travel as the very last reveal, confirmed at the end and tying every mystery together; contact with the dead leaned into but never said; fumes, a parallel reality and a wormhole each hinted almost to canon and never confirmed; the distant-future humans never provable; sharp, concise questions about belief and science; impact and consequence; mind-bending dissociation; a villain of Johan Liebert's quality (passive, quiet, never show-stopping, yet resourceful and formidable).
3. What works best, with short quotations.
4. The problems, most serious first. Mark each SUBSTANTIVE (a careful reader would notice it and it weakens the book: a plot hole or broken logic, a contradiction, a broken rule, a character acting without cause, a villain who stops being formidable or quiet, a passage with no job, sagging pace, confusion that does not serve the dissociation, a theme stated instead of shown, a thread that goes nowhere) or QUIBBLE (could go either way, or only an audience could settle it: word choice or placement, rhythm, the exact timing of an event when nothing depends on it, taste). For each: chapter and passage, the problem, why it matters, and a concrete fix.
Be exact: quote the text for every claim, and do not report anything you have not checked in the text.

Write the review to ${OUT} in Markdown, then reply with one line: your verdict and how many SUBSTANTIVE and QUIBBLE findings you gave.`, {label: 'fable-review-19', phase: 'Fable review', model: 'fable', effort: 'xhigh'})
return r