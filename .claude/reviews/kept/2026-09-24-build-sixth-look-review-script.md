# The sixth look at the error-correction build: the script that ran it, 24 September 2026

What this is: the script that ran the sixth look's reviewers (log entry 33), word for word as it was passed in full at 21:37:55 on 24 September (UTC), when the stopped review run `wf_14e38511-111` was resumed (session record line 8980); it is the same, byte for byte, as the copy the tool saved. The owner's "Return new script inline" and "Where is revised script?" (entries 33 and 34) may mean this script or a revised screenplay (correction C17, question S14). It holds instructions to agents that are kept nowhere else: the fourth check of the briefs and the one verifier. Earlier versions gave each reviewer that found a must-change its own verifier; after the owner's "Use one verify agent", every report whose text contains the words "must change" goes to one verifier (in this run all four did, the copy-checker's too, though it found nothing that must change). The files it names under `/tmp/` are kept, word for word, in `2026-09-24-build-sixth-look-briefs.md` (the briefs, the third brief check's report and the copy script), and the reports it produced in `2026-09-24-build-sixth-look.md` and `2026-09-24-build-sixth-look-scripts-copy-verifier.md`; the folders it names (the reviewers' copies and the snapshot repository) were this session's working files and are not kept.

```js
export const meta = {
  name: 'sixth-look',
  description: 'Recheck the revised briefs, then four independent reviewers on the fifth round\'s edits, then one agent verifying every must-change',
  phases: [
    { title: 'Brief recheck', detail: 'theory-checker rechecks the revised briefs' },
    { title: 'Review', detail: 'theory-checker, use-tester, scripts reviewer, copy-checker' },
    { title: 'Verify', detail: 'one agent tries to refute every must-change' },
  ],
}

const S = '/tmp/claude-0/-home-user-StoryTest/d4341bef-a251-5a02-b92c-5a2687b808be/scratchpad'
const BRIEFS = S + '/briefs-round6.md'

phase('Brief recheck')
const recheck = await agent(
  'You are making a narrow fourth check of briefs before they go out to reviewers (the error-correction skill\'s references/reviews-and-briefs.md, section 5). You did not write them. ' +
  'The briefs are in ' + BRIEFS + '. A third check of the previous version is in ' + S + '/brief-check-3-round6-report.md: it found 8 things, one must change (a copy made by copying the folder with its .git keeps the link to the real GitHub). ' +
  'The answer to it is a copy script the briefs now tell every reviewer to use: ' + S + '/make_review_copy.sh. Read it and try it once, making a copy under ' + S + '/r6-brief-check-4/ (it takes about four minutes; give the command a long time limit): does the copy end with no remote at all, pushing switched off, and its last commit approved by the gate, and is the live repository at /home/user/StoryTest left exactly as it was (compare its HEAD, its branch list and its .git folder\'s files before and after)? ' +
  'Then check only: (1) each of the third check\'s 8 findings is answered, or say which is not; (2) the lines changed to answer them made nothing new that is false, steers a reviewer to the lead\'s answer, narrows what a reviewer may find, or could lead a reviewer to write into the live repository, the shared snapshot repository at ' + S + '/rereview, or the real GitHub; (3) the rows quoted in the briefs still match their sources word for word. ' +
  'Never edit anything in /home/user/StoryTest or in the snapshot repository. ' +
  'In the report field, give each finding with target, defect, grounds, connection and grade (must change, should change, minor, does not bear), numbered, then what you did not check. In must_change, list one line per must-change finding (empty if none). Verdict: passed, passed after changes, or not passed.',
  {
    label: 'brief check 4',
    phase: 'Brief recheck',
    agentType: 'theory-checker',
    schema: {
      type: 'object',
      properties: {
        verdict: { type: 'string', enum: ['passed', 'passed after changes', 'not passed'] },
        must_change: { type: 'array', items: { type: 'string' } },
        report: { type: 'string' },
      },
      required: ['verdict', 'must_change', 'report'],
    },
  })

if (!recheck || recheck.must_change.length > 0) {
  log('The brief recheck found must-changes (or did not return); the reviewers were not started.')
  return { recheck, reports: null, verifications: null }
}
log('Brief recheck: ' + recheck.verdict + ', no must-change; starting the four reviewers.')

const REVIEWERS = [
  { name: 'theory-checker', brief: 'A', agentType: 'theory-checker' },
  { name: 'use-tester', brief: 'B', agentType: 'use-tester' },
  { name: 'scripts', brief: 'C', agentType: 'general-purpose' },
  { name: 'copy-checker', brief: 'D', agentType: 'copy-checker' },
]

const VERIFY_SCHEMA = {
  type: 'object',
  properties: {
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          summary: { type: 'string' },
          verdict: { type: 'string', enum: ['confirmed', 'partly', 'refuted', 'could not test'] },
          grounds: { type: 'string' },
        },
        required: ['id', 'summary', 'verdict', 'grounds'],
      },
    },
    under_graded: {
      type: 'array',
      items: { type: 'string' },
    },
  },
  required: ['findings', 'under_graded'],
}

const reports = await parallel(REVIEWERS.map(r => () => agent(
    'You are the ' + r.name + ' reviewer for the sixth look at a story workshop\'s uncommitted build. Your brief is the shared part and Brief ' + r.brief + ' in ' + BRIEFS + '. Read both first and follow them exactly, including every rule about not touching /home/user/StoryTest and working only in your own copy under ' + S + '/r6-' + r.name + '/. ' +
    'Your final message is your report, in the form the brief gives; it will be kept word for word, so write it for a reader who has not seen your working.',
    { label: 'review:' + r.name, phase: 'Review', agentType: r.agentType })))

const withMustChanges = REVIEWERS.map((r, i) => ({ name: r.name, brief: r.brief, report: reports[i] }))
  .filter(x => x.report && /must change/i.test(x.report))
let verification = null
if (withMustChanges.length > 0) {
  verification = await agent(
    'You are checking reviewers\' findings, adversarially, as the one verifier for this look. The reviewers looked at the edits in git -C ' + S + '/rereview diff c52f191 26bf4fd, under the briefs in ' + BRIEFS + '. Their reports are below. ' +
    'For each finding a report grades "must change", try to refute it: check its grounds yourself (read the files and the owner theories it cites; rerun its commands only in your own copy, made with ' + S + '/make_review_copy.sh under ' + S + '/r6-verify/, and only where reading cannot settle it). Give verdict "confirmed" if you reproduce it and it meets the brief\'s definition of must change, "partly" if it bears but less than claimed or with different grounds, "refuted" only if you show its grounds wrong, "could not test" if you cannot. ' +
    'Also list in under_graded any finding graded lower that meets the brief\'s must-change definition, with why. Never edit, stage, commit or run anything that writes in /home/user/StoryTest or in the snapshot repository. ' +
    'Identify each finding as <reviewer>:<its number>. The reports:\n\n' + withMustChanges.map(x => '=== ' + x.name + ' (Brief ' + x.brief + ') ===\n' + x.report).join('\n\n'),
    { label: 'verify (one agent)', phase: 'Verify', agentType: 'general-purpose', schema: VERIFY_SCHEMA })
}

return { recheck, reports: REVIEWERS.map((r, i) => ({ reviewer: r.name, report: reports[i] })), verification }
```
