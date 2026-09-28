export const meta = {
  name: 'fable-review-seconds',
  description: 'Fable 5.1 at extra-high effort gives one review of one completed full revision of the Seconds season, and does nothing else',
  phases: [{ title: 'Fable review', model: 'fable' }],
}
// args: { doc: the completed season joined into one document, out: where the review goes, label: short name for this version }
const W = '/tmp/claude-0/-home-user-StoryTest/265a0046-ddbf-521c-b22e-35bf4bc1a28a/scratchpad/work'
phase('Fable review')
const r = await agent(`You are giving one review of one document, and doing nothing else: do not edit any file except the one review file named below, do not start any other agents or workflows, and do not run anything that changes the story.

The document is ${args.doc}: a complete revision of "Seconds", a ten-episode television season written as scriptments (episode outlines with scenes and key dialogue). Claude's writers wrote episodes 1 to 3; another AI model, GLM 5.3, finished the season and has been revising it.

Read these first; they are the owner's rules and the season's master plan:
- ${W}/new/00-brief-2.md (the owner's brief and rules)
- ${W}/new/05-owner-feedback-2.md (the owner's second feedback; it overrides the brief where they differ: every invented law of physics from the owner's world document must be true in the story)
- ${W}/the-catch-notes.md (notes on the owner's own screenplay "The Catch"; nothing from it may be echoed)
- ${W}/new/70-plan-v3.md (the master season plan, version 3: its world rules, numbers, knowledge map and twist schedule; section 14 lists words that must never reach the screen)
Then read the whole season closely, start to finish.

Write an honest, rigorous editorial review for the owner, who is not a writer and wants plain everyday language (explain any unavoidable technical word in one plain sentence). Cover:
1. Your overall verdict in a few sentences: what the season is, what it achieves, whether it is finished.
2. How it keeps the owner's rules: the core message (a culture that never questions anything dooms its people) shown through events and never stated; mind-bending twists that are fair (planted before they land); every invented law of physics used and never broken; no echo of The Catch; no banned word or named idea on screen; not a dystopia.
3. What works best, with short quotations.
4. The problems, most serious first. Mark each SUBSTANTIVE (a careful viewer would notice it and it weakens the season: a plot hole or broken logic, a contradiction between scenes or episodes, a broken rule or law, a twist given away early or never planted, a character acting without cause, a scene with no job, sagging pace, confusion that does not serve the story, a theme stated instead of shown, a thread that goes nowhere) or QUIBBLE (could go either way, or only an audience could settle it: word choice or placement, rhythm, the exact timing of an event when nothing depends on it, taste). For each: episode and scene, the problem, why it matters, and a concrete fix.
Be exact: quote the text for every claim, and do not report anything you have not checked in the text.

Write the review to ${args.out} in Markdown, then reply with one line: your verdict and how many SUBSTANTIVE and QUIBBLE findings you gave.`, {label: `fable-review-${args.label}`, phase: 'Fable review', model: 'fable', effort: 'xhigh'})
return r
