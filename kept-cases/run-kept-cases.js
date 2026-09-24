export const meta = {
  name: 'run-kept-cases',
  description: 'Run kept story cases against the skills at a given copy of the repository, then grade each answer against its must and must-not lists',
  phases: [{ title: 'Answer' }, { title: 'Grade' }],
}

// args: { root: path to the repository copy whose skills are tested,
//         cases: [{file, writerFile, caseFile}],
//         planted: [{case, caseFile, answerFile}],
//         label: 'before' | 'after' }
const runArguments = args
const ANSWER_SCHEMA = {
  type: 'object',
  properties: {
    skills_chosen: { type: 'array', items: { type: 'string' } },
    files_opened: { type: 'array', items: { type: 'string' } },
    answer_to_writer: { type: 'string' },
    stalls: { type: 'array', items: { type: 'object', properties: {
      where: { type: 'string' }, what: { type: 'string', description: 'where you stalled, improvised, found two rules at odds, or met a record that looked stale' } },
      required: ['where', 'what'] } },
  },
  required: ['skills_chosen', 'files_opened', 'answer_to_writer', 'stalls'],
}
const GRADE_SCHEMA = {
  type: 'object',
  properties: {
    items: { type: 'array', items: { type: 'object', properties: {
      list: { type: 'string', enum: ['must', 'must not'] },
      item: { type: 'string' },
      verdict: { type: 'string', enum: ['met', 'broken', 'unclear'] },
      evidence: { type: 'string', description: 'the words of the answer that show it, quoted, or "nothing in the answer" ' } },
      required: ['list', 'item', 'verdict', 'evidence'] } },
    result: { type: 'string', enum: ['pass', 'fail', 'unclear'], description: 'fail if any must is broken or any must-not is broken; unclear if any item is unclear and none broken' },
    notes: { type: 'string' },
  },
  required: ['items', 'result', 'notes'],
}

function writerPart(caseText) {
  const start = caseText.indexOf('## What the writer brings')
  const end = caseText.indexOf('## Must')
  return caseText.slice(start + '## What the writer brings'.length, end).trim()
}

const answerPrompt = (writerFile) => `You are Claude Code, working in the story workshop at ${runArguments.root} (a set of Claude Code skills for building and testing stories). A writer has sent the message in the file named at the end. Answer it the way a Claude Code session in this repository would: first read the descriptions (the front matter) of the skills in ${runArguments.root}/.claude/skills/*/SKILL.md and choose the skill or skills whose description fits; then follow the chosen skill's procedure as written, opening only the modules and theory passages its map and steps send you to, and reply to the writer as its reply step says.

Rules for this run: apart from the writer's message file named at the end, read files ONLY under ${runArguments.root} (it sits inside a scratch folder; that is expected). Do not open any other folder or file (in particular not /home/user/StoryTest, nothing else in any scratchpad, and no folder named kept-cases, cases-draft or case-run other than that one file). Do not edit any file. Do not ask the writer anything; if something is missing, do what the skill says to do when facts are missing.

Besides the answer, report honestly every place where you stalled, had to improvise because the skill did not say what to do, found two rules at odds, or met a record that looked stale. An empty list is fine if there were none.

THE WRITER'S MESSAGE is in the file ${writerFile}. Read that file first (it is the only file outside ${runArguments.root} you may open).`

const gradePrompt = (caseFile, answer) => `You are grading one answer from a story workshop against a test case whose expectations were written before the answer existed. Do not open the workshop's skills; judge only the answer against the lists. Read the case (its Must and Must not lists, and its Open points, which say what may be left unsettled and what not to grade). For each item, decide met, broken or unclear, and quote the words of the answer that show it (or say "nothing in the answer"). A must is met only if the answer actually does it; a must not is broken only if the answer actually does the forbidden thing. Be strict and literal; do not reward length. Result: fail if any must is broken or any must-not is broken; unclear if any item is unclear and none is broken; otherwise pass.

THE CASE is in the file ${caseFile}. Read it in full first. Do not open any other file, except an answer file if one is named below.

THE ANSWER TO GRADE:
${answer}`

const results = await pipeline(
  runArguments.cases,
  async (keptCase) => {
    const caseFile = keptCase.file
    const ans = await agent(answerPrompt(keptCase.writerFile), { label: `answer:${caseFile}`, phase: 'Answer', schema: ANSWER_SCHEMA })
    return { caseFile, ans }
  },
  async ({ caseFile, ans }, keptCase) => {
    if (!ans) return { caseFile, error: 'no answer' }
    const grade = await agent(gradePrompt(keptCase.caseFile, ans.answer_to_writer), { label: `grade:${caseFile}`, phase: 'Grade', schema: GRADE_SCHEMA })
    return { caseFile, label: runArguments.label, answer: ans, grade }
  },
)

const planted = await parallel((runArguments.planted || []).map(plantedAnswer => async () => {
  const grade = await agent(gradePrompt(plantedAnswer.caseFile, 'The answer is in the file ' + plantedAnswer.answerFile + '; read it. It is the answer to grade.'), { label: `grade-planted:${plantedAnswer.case}`, phase: 'Grade', schema: GRADE_SCHEMA })
  return { planted: true, caseFile: plantedAnswer.case, expected: 'fail', grade }
}))

return { label: runArguments.label, root: runArguments.root, results, planted }
