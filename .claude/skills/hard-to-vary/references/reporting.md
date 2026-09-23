# Reporting

Open this when writing up. The aim is a report from which a reader could rerun your reasoning and reach a different view.

## The status marks

| Status | Means | Also say |
|---|---|---|
| Held | Removing it breaks a job that is not in doubt | which job or change |
| Held if | It is held only by a job that is itself in doubt, or only by a part marked loose, idle or unknown | which job or part, and what would settle it |
| Two routes | Either of two parts does the job | both parts, and whether each has a second job |
| Loose | A near neighbour would do as well | what could replace it. Loose says nothing about how it got there |
| Idle | It can go with no loss | that you tried removing it in groups |
| Unknown | No test run so far bears on it, or a relevant test could not be settled | the test that would settle it |

These statuses answer what the current test shows about a part's work. Where two parts hold a job only together and neither does it alone, each is *held, jointly with* the other, named.

Keep three other fields separate:

- **Scope:** *in test*, or *owner-fixed/outside the test*. A part the owner explicitly excludes is *not assessed*; exclusion is not evidence that it is held. A part that merely serves a job tagged fixed remains in scope unless the owner excluded the part itself.
- **Dependency:** *none named*, or *borrowed from* another explanation not tested here. Name it. Borrowing locates the support; it is not a status or provenance.
- **Provenance:** *fitted*, *built* or *asserted*, one for every part. This says where the part came from, not whether it is held.

A job's tag (*given*, *fixed*, *added*) is another list and stays with the jobs. For designs, the older words in `by-domain.md` map like this: *free* is loose and harmless; *inherited* is fitted.

For whole-explanation tests, report **result**, **N/A**, or **not settled**. Use *N/A* only when the frozen question gives the test no target, and say why. Use *not settled* when the test is relevant but the needed case, intervention or evidence is unavailable; only that can leave an affected in-scope part *unknown*. Never silently omit a test.

## How to write it up

**Case.** A table of ten candidates against twelve properties invites a total. A candidate with eleven ticks that lacks the one property everything leans on is worse than one with six that has it.

- **No totals, no ranking by count.** Report by job: what gets done, what fails, and because of which missing part.
- **Keep three things apart:** what was found, what it did to the claim, and what it could not settle.
- **Show your expectations as written beforehand,** next to what happened.
- **Carry the how-I-know tags** for every claim a verdict rests on.
- **List the parts that never met a hard case, and the findings that fit no part.**
- **If no job on the list can tell two candidates apart,** say they are the same at this level.
- **Say what was not looked at.** Then one next step.

## Traps

- Adding up marks or ticks.
- Tidying the expectations after the fact.
- Reporting what a change fixed and leaving out what it gave up.
- Presenting a loose part as a wrong one, or a held part as a true one.
