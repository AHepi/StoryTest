# Review of the error-correction build: process against the foundation, and the process walked through five situations, 24 September 2026

What this is: the reviewers' reports, word for word, as the review workflow returned them (each an independent agent that did not make the change). They reviewed the working copy as it stood at about 13:35 UTC, before any of their findings were applied. How each finding was answered is in the build's review receipt. Kept for log entry 29.

---

```json
[
 {
  "id": "process-vs-foundation",
  "findings": [
   {
    "target": ".claude/skills/error-correction/SKILL.md lines 72, 118 and 173; references/recording.md line 61",
    "defect": "The skill tests whether a change did the work by removing that change on its own. It then rules that if the failure stays gone without the change, \"the change did not do it\" (line 173), or \"something else did the work\" (recording.md 61). Line 72 cites Part XI for this. Part XI does not define the credit this way. It uses an active route read from what happened, and it credits both of two sufficient contributions that both ran.",
    "grounds": "Foundation Part XI, line 433: \"ProducedBy holds when an active route (Part IX) runs from Δ to the repair; it credits each contribution the history establishes, and where two sufficient contributions both ran, both are credited\". Part IX, line 371: \"whether a route is active is read from the history, not from the result\". Part VI, redundant routes, line 309: \"each is contributory, neither indispensable\". hard-to-vary SKILL.md line 162: \"Two parts may each be removable alone but not together. Remove in groups before you cut\". hard-to-vary also has the \"two routes\" mark (reporting.md line 92).",
    "connection": "C1 built two things against the same failure (a write-up reaching the owner untested): the reply check in the craft skills and the records check's \"Checks run on these notes\" rule. Remove either one alone and the failure stays gone. The skill's rule then says neither did the work. The foundation credits both, and hard-to-vary would mark them two routes. Put together with the stance \"Remove what is idle\" (line 89), the rule points toward cutting a guard that works.",
    "verdict": "bears",
    "severity": "must change",
    "proposed_change": "Rewrite line 118 as: \"Did the change do it? Say the route: what ran, and in what order, from the change to the case or check that now passes (Part XI: an active route, read from what happened). Then remove the change, alone and together with any other change made for the same failure. If the failure comes back only when both are removed, they are two routes and both are credited.\" Change line 72 to cite the route, not removal alone. Change line 173 and recording.md line 61 to: \"a change is not shown to have done nothing until it has been removed in groups\"."
   },
   {
    "target": ".claude/skills/error-correction/SKILL.md line 107: \"A change to a part with no other job is a patch: say so. It must earn a second job, or the correction stays open.\" (and \"Prefer a change whose cost shows at once.\")",
    "defect": "This decision rule makes the number of jobs the condition for closing a correction. It is not labelled as the workshop's reading, and the foundation and hard-to-vary both reject counting jobs as a warrant. \"Prefer a change whose cost shows at once\" is neither explained nor grounded.",
    "grounds": "Foundation Part VI, hard-to-vary, line 315: \"More reach constrains variation; the containment need not be strict; counting jobs is not a warrant.\" hard-to-vary SKILL.md line 72: \"No scores. Do not count confirmations, jobs or parts. One job that rules out rivals is worth more than ten that rule out nothing.\" hard-to-vary's own test for a patch (SKILL.md line 105) asks for no second job: \"A fix is a new part too: try it on the case that forced it and on the cases it must leave alone.\"",
    "connection": "Take a single-purpose guard that its one job holds in place: the frozen-file hook, whose kind the corrections file lists as \"never seen\". Under this rule its correction stays open for good, or the maker has to invent a second job to close it. Either way, a count decides something the foundation says a count cannot warrant.",
    "verdict": "bears",
    "severity": "must change",
    "proposed_change": "Replace with hard-to-vary's patch test: \"A change that adds a part with no other job is a patch: say so, and run it on the case that forced it and on the cases it must leave alone. If a further job is claimed for it, say which rival that job rules out.\" Drop \"or the correction stays open\". If the workshop wants a closing rule, label it as the workshop's reading. Explain \"whose cost shows at once\" in a plain sentence, or cut it."
   },
   {
    "target": ".claude/skills/error-correction/SKILL.md lines 109-112 (step 4, the plan); references/recording.md line 26 (the record's \"Fixed, still working, lost\" part)",
    "defect": "Part XI needs the obligations fixed before the comparison: what is to be fixed and what is to be kept working. The skill only says \"Plan, before changing anything\". Nothing asks for the plan to be written down before the change, and the record keeps only the results. Nobody can see afterwards whether the keep-working list was chosen after the results were known.",
    "grounds": "Foundation Part XI, lines 427 and 433: obligations \"fixed for the comparison\", and \"a protected condition is lost exactly when it fails on an occasion it covers\". Part XIV, line 514: \"where the input is missing, the verdict is unsettled and the semantics says so rather than choosing the input from the verdict wanted.\" hard-to-vary reporting.md line 115: \"Show your expectations as written beforehand\", and its trap at line 124: \"Tidying the expectations after the fact.\"",
    "connection": "Suppose a kept case fails after a change. If the plan is written afterwards, that case can be left off \"to keep working\" and listed under \"lost\". By Part XI, a protected condition that fails means there was no repair. Recorded as a loss outside what was protected, the same result becomes a repair with an exposed loss. Only a plan written before the change can tell the two apart.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Step 4: \"Write the plan down before changing anything: in the correction's record for a full correction, otherwise in the review receipt's Change line.\" recording.md: the \"Fixed, still working, lost\" part shows the plan as written beforehand next to what happened. Anything on the keep-working list that now fails is reported as broken (back to step 3), not as lost."
   },
   {
    "target": ".claude/skills/error-correction/SKILL.md line 118 (\"fixed, with a reason that holds; fixed without a reason that holds yet; ... a reason that holds, with nothing fixed yet\"); references/recording.md line 26",
    "defect": "These three outcomes restate the foundation's three attributions but leave out what defines the third: a repair produced through use of the account. \"Fixed, with a reason that holds\" also covers a fix that came from somewhere else while a correct reason was written beside it.",
    "grounds": "Foundation Part XI, line 433: \"A correct account that produced nothing, an act that repaired without an account, and a repair produced through use of an account are three different attributions.\" Part IX, reason use, line 381. Part IX, receipts, line 393: \"A record reconstructed from the claim it is meant to support is not a receipt for that claim.\"",
    "connection": "The workshop's reasons have been written after the fact before (log entries 1 to 7 were rebuilt afterwards). Suppose the owner's instruction produced a fix and a reason was written afterwards. The skill's wording records that as \"fixed, with a reason that holds\". The foundation counts it as two separate attributions: an act that repaired without an account, and a correct account that produced nothing.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Make the first outcome \"fixed through the reason: the change was made by using the reason, and the route shows it\". Add one sentence: a fix together with a correct reason that did not produce it is recorded as the other two outcomes together. Make the same change in recording.md line 26."
   },
   {
    "target": ".claude/skills/error-correction/SKILL.md line 107 (\"record the part as its witness: what it is, what it ties together, where it lives\"); references/recording.md line 25; the example at SKILL.md line 20",
    "defect": "The skill's witness for a new part describes only the finished part. The foundation's construction witness names the history: the processes that did the building and the material that came in. That history is what separates building from relay, and it shows whose contribution the part was. The lead example also credits the workshop's locate step with a diagnosis the owner supplied.",
    "grounds": "Foundation Part X, construction, line 401: \"A construction witness identifies the controlled processes, the incoming carriers, the bindings constructed, and the resulting representation ... Reconstruction by a learner is construction; relay is not.\" Part 0, line 15: the provenances \"are told apart by their histories, not their outputs\". Derivation 4, line 574: \"by their witnesses, not by their outcomes\". Part X, ownership, line 419: \"Work supplied from outside that boundary, a diagnosis, a decisive question, an instruction about what to read, remains an outside contribution however it is executed inside\". 27 Corrections.md, H45: \"The owner said 'No no. Wrong task': the gap is systemic and has to be built into the repo.\"",
    "connection": "\"What it is, what it ties together, where it lives\" reads the same for a part built from the criticism and for one copied in whole from elsewhere, so it cannot tell building from relay. In the lead example (line 20), \"The re-tune had not reached what every critique lacked, so a new part was built\" credits the loop with the diagnosis. H45 records that the owner supplied it. That credit is exactly the evidence needed to judge whether the process catches errors without the owner (the stance at line 83 names \"misses that only the owner caught\").",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "The witness becomes: what it is; what it ties together; who made it and in which commit; what it was made from (the criticism, a research report, a brief, another file's text); and which decisive step came from outside the workshop (the owner's diagnosis, question or instruction). Rewrite the example's step 3 to say that the owner supplied the diagnosis (systemic; build it into the repository) and that the workshop built the parts."
   },
   {
    "target": ".claude/skills/error-correction/SKILL.md line 73 (\"Re-tune; build a new part ... (Part IV, Derivation 10; hard-to-vary's words)\") and line 12 (\"The two responses to a failure are re-tuning and construction (Part IV, Derivation 10)\")",
    "defect": "The skill separates re-tuning from building a new part by what the change does (adjust versus add). It gives \"reword a rule, add a warning\" as re-tunes and cites Part IV as though the foundation drew the line there. The foundation draws it by history: a selection response has no represented target and no criticism behind it. Every change in the workshop is made by an agent that has the target in view and is answering a criticism, so under Part IV every one of them is a construction. The line by kind of change is the workshop's reading of Derivation 10 (a set of versions that all lack one component). That reading is left unlabelled; line 107 labels only the tripwire.",
    "grounds": "Foundation Part IV, line 203: \"a selected transport has no represented target and no criticism in its history; a constructed one has both.\" Part IV, line 227: the selection response \"extends H and lets μ act: the transport is re-tuned within the population\". Part X, line 401: \"A small binding newly prepared inside received content is construction of that binding.\" Derivation 4, line 574. Derivation 10, line 616: \"the fidelity failure is structural, not parametric\".",
    "connection": "A reader who looks up \"(Part IV, Derivation 10)\" finds that the foundation would call a warning written after a criticism the construction of a small binding, not a selection response. The definition credits the foundation with a distinction the foundation draws differently. hard-to-vary's word-list.md line 45 makes the same mapping, so the maker should look at it as a copy.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Line 73: \"Re-tune; build a new part. The workshop's reading of Derivation 10. To re-tune is to vary what exists within the same set of versions (reword a rule, add a warning). To build a new part is to add a piece that every earlier version lacked (a check, a mode, a step). Both are made with the target in view, so in the foundation's own terms (Part IV) both are built; the line drawn here is Derivation 10's line between a fault in the structure and a fault in the settings.\" Line 12 to match."
   },
   {
    "target": ".claude/skills/error-correction/SKILL.md line 12: \"A criticism is defined by its bearing (Part IX, K1).\"",
    "defect": "This says a criticism is defined by whether it bears. The foundation defines a criticism by its four parts and says a criticism still exists when it does not bear; bearing is the verdict on it. The skill's own Words (lines 68-69) get this right, so line 12 contradicts both the foundation and the skill.",
    "grounds": "Foundation Part IX, lines 373-379: \"A criticism has target z, alleged defect δ, grounds g, and a connection ... A criticism occurrence can exist when (K1) fails. An adverse signal is not a criticism until an organization represents how it bears.\"",
    "connection": "If bearing defined a criticism, a criticism that does not bear would not be one. The loop's verdict \"does not bear (record why, and tell whoever raised it)\" would then have nothing to record.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "\"A criticism has four parts: target, defect, grounds and connection. Whether it bears is its verdict (Part IX, K1).\""
   },
   {
    "target": ".claude/skills/error-correction/SKILL.md line 19 (the example's step 2)",
    "defect": "The defect named, \"hard-to-vary was never run on the critique's own notes\", is not the defect that the grounds and connection show, which is \"the table's wording rests on an order the file says is unknown\". The four parts answer two different questions, in the example that is meant to teach them.",
    "grounds": "Foundation Part IX, K1, line 376: bearing is an account for the question about the named defect. Part III, line 153: \"an answer to one is not an answer to the other.\" Part V, line 275: \"packaging a genuine dependence that answers a different question beside it does not repair this (the bell does not explain the tide)\". 27 Corrections.md C1 lists these as two defects. What shows hard-to-vary was never run is file 26 line 116 (\"none ... It had been forgotten\"), not the flip.",
    "connection": "The flip result shows that the wording assumes an order. It is no evidence that hard-to-vary was never run. An agent copying the pattern will pair one defect with the grounds for another and mark the pair \"bears\".",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Make the defect \"the table's wording assumes B came second, though the file says the order is unknown\", keep the flip as grounds, and keep the connection. Move \"hard-to-vary was never run on the notes\" to step 3 as the place the error got through, with file 26's \"Checks run\" section as its grounds. Alternatively, write two criticisms, each with its own grounds."
   },
   {
    "target": ".claude/skills/error-correction/SKILL.md lines 69, 76, 100, 128 and 177; CLAUDE.md line 30",
    "defect": "Two words are used for one thing, and the line between two others is unclear. \"Does not bear yet\" (line 69) and \"unknown\" (line 76) have the same definition: name the test that would settle it. Line 76 splits \"held if\" (an input nobody gave) from \"unknown\" (a fact nobody checked). Yet the skill's lead case, which draft came first, is called an input at line 177 and in CLAUDE.md, although it is a fact. hard-to-vary's word for a whole-explanation test that could not be run is \"not settled\"; \"held if\" and \"unknown\" are its marks on single parts. The skill uses them for verdicts without saying how the marks on a criticism's working part give its verdict.",
    "grounds": "hard-to-vary SKILL.md line 113 (\"the two mappings across lists ... are mappings, said as such\"), line 137 (status marks are given to parts) and line 146 (\"not settled\" for whole-explanation tests). Foundation Part XIV, line 514: the declared inputs are the obligations, the scope and the boundary, with the normative input for aims (Part XI, line 447). Part IX, line 393: \"missing evidence stays missing\", which covers a fact such as the order of the drafts.",
    "connection": "On the Catch case, an agent can mark the verdict \"held if the order\", \"unknown (ask the writer)\" or \"does not bear yet (ask the writer)\", and each word carries its own instruction: give it both ways, or name the test. One situation gets three words that point to different actions.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "In Words, use \"held if\" for a verdict that depends on an aim or value only the owner or writer can give (give it both ways, and ask). Use \"does not bear yet\" for a criticism whose deciding fact has not been checked or told, the order of the drafts included (name the test or the question; if a note must go out now, give it both ways). Say once that \"does not bear yet\" is hard-to-vary's \"not settled\" applied to a criticism. Say how the verdict follows the mark on the working part: held gives bears, held if gives held if, unknown gives does not bear yet, loose or idle gives does not bear. Bring lines 100, 128 and 177 and CLAUDE.md line 30 into line."
   },
   {
    "target": ".claude/skills/error-correction/references/writing-rules-and-rivals.md lines 17-24 (the rule card); SKILL.md line 10 (\"held by what\"). Copies outside this review: review_receipt.py's form (\"held by what, free, or unknown\"), .claude/agents/theory-checker.md (\"Mark it: held by what, free, or unknown\"), and the craft skills' shared reply check (\"say what holds it (a line of the draft and a theory principle)\")",
    "defect": "Step 1 answers \"What holds it?\" with where the rule comes from: an owner theory, which in hard-to-vary's fields is a dependency, or a book tagged fitted, built or asserted, which is a provenance. In hard-to-vary, \"held\" is the mark a part earns when removing it breaks a job; here that test is step 2. Step 3's \"free\" is the design word from by-domain.md, not one of the six marks listed at SKILL.md line 10. Its test, \"reads as well\", is not hard-to-vary's swap, which asks whether the swapped part \"still does every job\".",
    "grounds": "hard-to-vary SKILL.md line 113: \"Never use one field to answer another: asserted is not a status; borrowed is a dependency, not a status or provenance.\" reporting.md lines 99-103. by-domain.md line 39: \"free maps to loose and harmless\". hard-to-vary SKILL.md line 97: the swapped version \"still does every job on the list\".",
    "connection": "Under the card, a rule whose only support is \"a book, asserted\" passes step 1 (\"A rule nothing holds is not written\"), though hard-to-vary says an assertion holds nothing in place. The receipt form's marks (held by what, free, unknown) are also a different list from the skill's own six (held, held if, two routes, loose, idle, unknown).",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Step 1 becomes \"What does it rest on?\": the dependency (the theory principle, cited), or the provenance (a book's fitted, built or asserted), or the workshop's reading with its question number. Step 2 gives the mark: held (by which job) or idle (cut it). Step 3 becomes: \"If the swapped rule still does every job on the theory's cases, the specific is loose; if that is harmless, say so plainly (by-domain.md calls this free).\" Use the six marks in the receipt form and in theory-checker.md, and look at the reply check's \"what holds it\"."
   },
   {
    "target": ".claude/skills/error-correction/SKILL.md line 89: \"A step, rule or check that catches nothing is weight ... Remove what is idle\"",
    "defect": "This treats a step, rule or check that has caught nothing so far as weight to be removed. In hard-to-vary, idle means a part can go with no loss, and that is found by removing it, in groups. A guard that has never fired can still be held in place by its job.",
    "grounds": "hard-to-vary reporting.md line 94: \"Idle | It can go with no loss | that you tried removing it in groups\". checks-and-cases.md line 11: a check is shown to work by planted faults (\"if this were wrong, I would see it\"). The kinds table in 27 Corrections.md: \"An edit to a frozen text | never seen | not seen | protect_frozen_files.py ...\". Foundation Part VI (B), line 298: whether a part is critical depends on removing it from a working set, not on its past outputs.",
    "connection": "The frozen-file guard has caught nothing (\"never seen\"), so under line 89 it counts as weight. Yet its planted-fault test shows it catches the edit it exists to stop.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "\"A step, rule or check that would catch nothing (its planted fault passes, or removing it, alone and in groups, loses no job) is weight.\""
   },
   {
    "target": "CLAUDE.md line 38 (\"A change to what the workshop says is independently reviewed | Itself: the commit gate asks for its review receipt\") and line 41 (\"briefs checked before they go out | On trust, with a trace in the review receipt\")",
    "defect": "Line 38 says the independent review runs by itself. The gate only checks that a receipt file, filled in by the maker, names a reviewer other than the maker. The skill's own table (SKILL.md line 158) calls the review \"On trust, with a trace\". Line 41 promises a trace in the review receipt for briefs, but SKILL.md line 159 says that trace exists only \"when briefs are kept\", and a brief is not among the files a receipt covers.",
    "grounds": "I read review_receipt.py problems_with: it checks that \"Reviewed by\", \"Maker\" and \"Findings\" are not empty, that the verdict is an allowed word, and that the reviewer and maker names differ. Nothing checks that a review took place. reviews-and-briefs.md line 11 says so honestly: skipping \"would take a false statement in a kept file\". Foundation Part XII, line 467: \"A theorist's description of a protocol is not the system's possession of it.\"",
    "connection": "The owner reading CLAUDE.md is told that the review runs by itself. What runs by itself is the demand for a file. The two files now disagree about the same rule.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Line 38: \"On trust, with a trace: the commit gate refuses the change without a review receipt that names a reviewer other than the maker (`.claude/reviews/`).\" Line 41: \"On trust. A rule or rival leaves a trace in the review receipt; a brief leaves one only when it is kept.\" Write \"By itself\" where the skill does, instead of \"Itself\"."
   },
   {
    "target": ".claude/skills/error-correction/SKILL.md line 75 (\"A summary written afterwards to support the claim is not one\"); references/recording.md line 39",
    "defect": "The skill decides whether a record is a receipt by when it was written. The foundation decides by what the record was made from: a record reconstructed from the claim is not a receipt. The foundation also makes a receipt a derivation over references to events, each with what it is taken to show, not a single pointer.",
    "grounds": "Foundation Part IX, line 393: \"An evidence leaf is a reference to an event with an interpreted claim. A receipt is a derivation tree over leaves ... A record reconstructed from the claim it is meant to support is not a receipt for that claim.\" Part IV, line 213: \"a later record derived from the carrier is not a second, independent witness to its history.\"",
    "connection": "A review receipt is filled in by the maker after the review, to support the claim that the change was reviewed (reviews-and-briefs.md line 26). By the skill's wording it is therefore not a receipt. By the foundation it is one if it copies the reviewer's report, and it is not one if the maker writes it from the verdict they want. The timing rule excludes the good case and does not name the bad one.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "\"A receipt points to events, each with what it is taken to show (the command, what it printed, and what that means). A record made from the claim rather than from the event is not a receipt for the claim, whenever it was written. A later copy of an event is the same witness, not a second one.\" In reviews-and-briefs.md step 5, paste the reviewer's findings rather than paraphrasing them."
   },
   {
    "target": ".claude/skills/error-correction/SKILL.md lines 71-72, 83, 85, 110 and 118; references/reviews-and-briefs.md lines 34, 46 and 57 (\"fixers\", \"fix brief\")",
    "defect": "The Words section makes \"change\" the skill's word for what answers a criticism and leaves \"fix\" to the craft skills. The skill then uses \"fix\" for a change anyway (\"fixes that made new errors\", \"fix brief\", \"fixers\", \"Fix the stage\"), and uses \"Fixed\" for the repaired result. hard-to-vary uses \"fixed\" for a job tag: a requirement the owner made that is not up for test.",
    "grounds": "hard-to-vary SKILL.md line 89: \"fixed (the owner made it a requirement that is not up for test)\". CLAUDE.md: \"use that one word for that one thing\".",
    "connection": "When the loop runs hard-to-vary on why a change works (line 10, \"why a change works\"; step 5), the report tags some jobs \"fixed\". The same record uses \"Fixed:\" for what was repaired. One word carries two meanings in one document.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Name the result \"Repaired, still working, lost\" (Part XI's own word), use \"change\" for the act throughout, and keep \"fixed\" for hard-to-vary's job tag only."
   },
   {
    "target": ".claude/skills/error-correction/SKILL.md line 22 (\"the reply step\"), line 160 (\"The self-check\"), lines 10 and 12 and the description (\"metric\" and \"measure\"); CLAUDE.md lines 36-38 (\"Itself\")",
    "defect": "One passage has three names. The new passage in the craft skills is \"the reply step\" (line 22), \"the self-check\" (line 160) and \"the reply check\" (the shared-passage marker and 27 Corrections). hard-to-vary's question-bank.md line 179 already uses \"self-check\" for something else. Hard to vary is also called both \"the metric\" and \"the measure\", and CLAUDE.md writes \"Itself\" where the skill writes \"By itself\".",
    "grounds": "CLAUDE.md, the Plain words rule. The shared marker in plot/SKILL.md reads `<!-- shared: reply-check -->`.",
    "connection": "A reader who meets \"self-check\" in the table cannot tell that it is the reply check, and in hard-to-vary the same word means the tester questioning themselves.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "Use \"the reply check\" everywhere. Keep \"metric\" (the owner's word) as the noun, with \"measure\" only as the verb. Write \"By itself\" in CLAUDE.md."
   },
   {
    "target": ".claude/skills/error-correction/SKILL.md line 12: \"the result must change how work proceeds (Parts I and XIII)\"",
    "defect": "This makes operative return stronger than the foundation does. The foundation asks that the result be able to change how work proceeds, not that every result does.",
    "grounds": "Foundation Part I, line 75: \"the result must be able to change how the system proceeds\". Part XIII, line 479: \"the result can affect its operative use\".",
    "connection": "If every criticism of the practice must change it, then a criticism that does not bear (which the loop's step 2 allows) would still demand a change.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "\"... and the result must be able to change how work proceeds.\""
   },
   {
    "target": ".claude/skills/error-correction/SKILL.md line 74 (\"A failed test knocks down all three together\"); references/checks-and-cases.md line 60",
    "defect": "Read literally, the wording says all three layers are knocked down. The foundation says only that they cannot all stand.",
    "grounds": "Foundation Part IX (K3), line 391: an established ¬O \"yields ¬(T∧B∧I) and nothing narrower\". hard-to-vary word-list.md line 55: \"only 'not all three' follows\".",
    "connection": "\"All three together\" can be read as all three being wrong. The words that follow (\"which one to change is a new guess\") rescue the reading at line 74, but checks-and-cases.md line 60 has no such rescue.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "\"A failed test shows only that the thing, the rig and the inputs cannot all be right; which to change is a new guess.\""
   },
   {
    "target": ".claude/skills/error-correction/SKILL.md line 77 (Licence); references/owner-answers-and-revisions.md line 11",
    "defect": "Licence is defined only by premises that still stand. The foundation's standing has a third condition, scope, and the skill leaves it out.",
    "grounds": "Foundation Part IX (K2), line 386: Usable requires Lic ∧ Scope ∧ every premise Live.",
    "connection": "A passage whose premises still stand, used outside the question it was made for, keeps its licence under the skill's words but is not usable under the foundation's. The kinds table in 27 Corrections names a theory \"narrowed or turned round\" as the commonest kind of error.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "Add: \"A passage also has leave only within its scope: the question it was made for.\""
   },
   {
    "target": ".claude/skills/error-correction/SKILL.md line 12 (\"The loop is the foundation's critical episode (Part X)\") and line 70",
    "defect": "This says the loop is the critical episode. Part X's episode has four elements. Steps 3 to 5 of the loop are Part XI's repair, and guarding and recording are the workshop's own additions.",
    "grounds": "Foundation Part X, line 421: \"A complete critical episode contains a recognized difficulty, a target available before its criticism, a conjectural objection, and a content-sensitive response.\" Part XI, line 429 (Repair).",
    "connection": "Crediting the whole loop to Part X makes the workshop's added steps look like the foundation's.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "\"The loop contains a critical episode (Part X) and a repair (Part XI). Guarding and recording are the workshop's additions.\""
   },
   {
    "target": ".claude/skills/error-correction/SKILL.md lines 154-157; CLAUDE.md lines 7 and 37",
    "defect": "\"Hook\", \"staged\" and \"`--no-verify`\" are used without a plain sentence explaining them in the files under review. README lines 74-75 describe the gate and the hooks by what they do, but explain neither \"staged\" nor \"--no-verify\".",
    "grounds": "CLAUDE.md, Plain words: \"explain a technical term once in a plain sentence\".",
    "connection": "The owner, who is not a programmer, reads \"exactly what is staged\" and \"`--no-verify` is refused\" with no explanation anywhere.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "Explain once, for example: a hook is a small program that Claude Code or git runs by itself at a set moment; staged means marked with `git add` to go into the next commit; `--no-verify` is a switch that would make git skip the checks."
   },
   {
    "target": ".claude/skills/error-correction/references/reviews-and-briefs.md line 34 (\"Past fixers turned down about one finding in eight, with reasons, and were right to\") and line 46 (\"four came from fix briefs\")",
    "defect": "A count is used as the warrant for a rule, and the judgement \"were right to\" has no receipt.",
    "grounds": "The skill's own trap at SKILL.md line 174 (\"Counting\"). hard-to-vary SKILL.md line 72 (\"No scores\"). Foundation Part IX, receipts.",
    "connection": "\"One in eight\" gives no reason to reject any particular finding. What carries the point is which findings were rejected, and why that was right.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "Name one rejected finding and why rejecting it was right, with its record, or cite the log entry. Drop the ratio."
   },
   {
    "target": ".claude/skills/error-correction/references/recording.md lines 17-31",
    "defect": "\"The five-part record\" lists six parts (Made by/found by; Criticism; Where it got through; Fixed, still working, lost; Now caught by; Status), and line 31 says that leaving a part out is not allowed.",
    "grounds": "recording.md, lines 23-28 and 31.",
    "connection": "A maker who counts to five can leave out Status, which the records check requires.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "Call it \"the six-part record\", or say that Status is a line that goes with the five parts."
   },
   {
    "target": ".claude/skills/error-correction/SKILL.md line 88 (\"Old records are never rewritten\") against references/recording.md line 49",
    "defect": "The stance says old records are never rewritten. The module allows a write-up's wording to be changed under a dated note.",
    "grounds": "recording.md line 49. Foundation Derivation 7, line 598: goalpost-moving is \"changing the index without recording the change\". So a recorded change is allowed; the defect is only the inconsistency.",
    "connection": "Following the stance, an agent would refuse a change that the module allows.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "\"Old log entries are never rewritten. A write-up is changed only under a dated note that lists each change.\""
   }
  ],
  "right": "The frozen files are unchanged: `git diff 35f2939 -- foundations sources` printed nothing, `git status --short foundations sources` printed nothing, and check_frozen_files.py printed \"TOTAL problems: 0\". run_all_checks.py printed \"RESULT: no check failed\". The book texts are present, so the copying check actually ran.\n\nMost definitions are faithful restatements of the foundation.\n- Error, and an error beside the load-bearing part (Part I).\n- Sign against criticism, with the four parts and \"a criticism is itself a guess\" (Part I, Part IX), in Words lines 67-68.\n- The three verdicts, and acting on an unsettled criticism as a labelled guess (Part I: \"may act on an appraisal without certifying it\").\n- Closing is a decision, not a proof (Part X).\n- Step 1 puts the target on record before its criticism (Part X, \"a target available before its criticism\").\n- K3's \"which one to change is a new guess\".\n- Licence: withdrawing a premise removes leave to rely on a passage, not its truth (K2), with the map checker as a real case.\n- The repair mapping in steps 4 and 5 follows Part XI. There is a to-fix list and a keep-working list. \"Lost\" means losses outside what was protected, and they are exposed. Whether a loss is acceptable is left to the owner, which matches \"(P) does not rank alternatives\". Kept cases are named as the stated occasions.\n- reviews-and-briefs.md line 38 restates reason use exactly: a differently worded finding with the same point leads to the same change, and applying a finding does not make it right (Part IX).\n- The owner's values are treated as a declared input that is never ranked, while the owner's facts stay open (Part XI, Part XIV).\n- Checks through the same frame count as one (I4; Part IV, a later record is not an independent witness).\n- A changed kept case is a new case (historical index, Derivation 7).\n- A frozen theory that seems wrong is recorded and put to the owner, never hidden (Part XV).\n\nHard to vary is treated as a metric given in marks, never in scores. The Counting traps sit in the skill and in checks-and-cases. The owner's sentence is quoted exactly, and where the metric applies is labelled as the workshop's reading. The thresholds and the Derivation 10 tripwire are labelled. The table \"Where the process runs\" is honest about which rules are on trust and which run by itself (Part XII: a description is not possession); CLAUDE.md is the exception. The rival form requires predictions that cannot both come true.",
  "not_checked": "- owner-terms.md, which was excluded from this review.\n- What the scripts actually do. I read review_receipt.py's check and the header of refuse_check_bypass.py, and ran only run_all_checks.py and check_frozen_files.py. I did not run test_checks.py or exercise any hook. Several of the skill's claims are therefore unverified: after_commit.py repeats the claim list, session_start.py lists stale cases, the gate stops when python3 is missing, and the records check allows only the \"*Corrected in entry N:*\" line.\n- The other changed files: the craft skills and their shared reply check (quoted only as a copy of a finding), add-source, the agents apart from theory-checker.md, kept-cases, the hooks and README.\n- 27 Corrections.md beyond the kinds table, C1 to C4, H41 and H45.\n- Whether the boundary in \"Where the process runs\" was declared before the attributions made under it (Part XII). Nothing in the record shows the order.\n- git log -L on the reviewed passages, because they are new files with no history.\n- The kept cases, and a use-tester walk of the loop on a concrete case.\n- A planted-fault test of myself as the reviewer.",
  "overall": "passed after changes"
 },
 {
  "id": "process-walk",
  "findings": [
   {
    "target": "26 Test - The Catch - two versions.md, lines 46, 52, 67, 75 and 90, and the correction note at line 9",
    "defect": "The write-up still assumes that B was made from A in five places after its correction: \"The look is cut\" (in fault 1's table, the part that was tested), \"B cuts the hand beat\", \"B cuts all three\", \"B's goodbye on the ship cuts A's pay-off ... B replaces it\", and \"what B's cuts were for\". The note at line 9 names only three such phrases and says those were the ones that assumed an order.",
    "grounds": "I ran grep -n -i \"cuts\\|cut\\b\\|restor\" on the file, which printed these lines. error-correction/SKILL.md line 129 says: \"Words that assume an order (\\\"cuts\\\", \\\"adds\\\", \\\"restores\\\", \\\"later\\\") match what is known.\" File 26 line 7 says the order is unknown, and S12 in the questions file is still open. This is the same kind of error as H42, which the owner caught. C1 (27 Corrections.md line 34) records the fix as done.",
    "connection": "The correction the skill uses as its own worked example (SKILL.md lines 16-23) did not apply the skill's own claim check to the whole write-up. Its search stopped at three phrases, and its note reads as though the order problem is gone. A reader of the owner-facing record is still told that B came second in five places, which is the harm C1 describes: material could be put back for a reason the critique has no right to give.",
    "verdict": "bears",
    "severity": "must change",
    "proposed_change": "Reword the five phrases so they say what each version has, without an order, for example \"B does not have the hand beat\" and \"B has none of the three\". List each change in the dated note, as recording.md section 4 asks. Change the note's \"three phrases\" to the full list. Reopen the \"Fixed\" part of C1 until a search of the whole file for cut, cuts, restore, replaces, trims and new comes back clean, and record that command in the \"Checks run on these notes\" section."
   },
   {
    "target": ".claude/skills/error-correction/scripts/review_receipt.py, lines 123-138 (the check reads the fields) and the FORM at lines 146-156",
    "defect": "The commit gate accepts a review receipt that nobody filled in. A field counts as filled if it holds anything, so the form's own bracketed hints are taken as the Maker, the Reviewed by, the Findings and the Book text. A receipt made with `review_receipt.py new`, where only the verdict line was changed to \"passed\", goes through.",
    "grounds": "In a scratch copy I staged a one-word change to opponents.md, ran `review_receipt.py new`, changed only the verdict line to \"- **Verdict:** passed\", staged the receipt and ran `review_receipt.py check`. It printed \"review receipt: .claude/reviews/110498bc7f8ff72d.md is complete\" and exited 0. With the book texts absent, the untouched hint in the Book text line was also taken as an answer. test_checks.py plants no unfilled form, and its output lists only the missing-receipt, edited-after-review and reviewer-is-maker faults.",
    "connection": "CLAUDE.md lines 38 and 40 say the independent review and the book-text answer are enforced by the gate itself (\"Itself\"). The gate lets through the fault closest to a complete receipt, which is a receipt nobody completed. So the rule \"Nobody grades their own work\" can be skipped without a single false word being typed in. This is the kinds table's \"A check that passes while the thing is wrong\", and checks-and-cases.md section 1 says to plant exactly this neighbour.",
    "verdict": "bears",
    "severity": "must change",
    "proposed_change": "Refuse any field that still begins with \"(\" or matches the form's hint text. Accept Book text only when it begins \"none added\" or names what was added. Plant an unfilled form, and a form with only the verdict filled, in test_checks.py, with a completed receipt as the innocent neighbour."
   },
   {
    "target": "error-correction/SKILL.md line 100, with steps 4-5 (lines 109-119) and \"How much to do\" (lines 134-146); reviews-and-briefs.md line 35",
    "defect": "The loop has no light path. Step 2 says \"A criticism that will change what a skill says gets the full hard-to-vary procedure\". Steps 4 and 5 ask, for every change, for the kept cases of every skill it touches, a case where the nearest rival change would come out differently, and a remove-and-rerun test. \"How much to do\" says only what is recorded at each weight, not which steps are run. reviews-and-briefs.md line 35 says instead to run step 2 \"in proportion\". The two instructions are at odds.",
    "grounds": "Walk (a): a reviewer reports a wrong-theory credit in opponents.md. Following the text exactly, a one-word credit fix needs hard-to-vary's full seven-step procedure with eleven tests (hard-to-vary/SKILL.md lines 77-115), a kept-cases run (kept-cases/README.md steps 1-7: a clean commit, fresh answering agents, the grader and a planted answer), and removing the fix to see whether the fault comes back. SKILL.md line 89 itself says \"weight is why the full hard-to-vary procedure went unused before (log entries 20 and 22)\"; that past error is H25.",
    "connection": "On the most common event, a single review finding, the process demands the weight it names as the reason the procedure was skipped before. An agent must either skip steps (improvise) or treat every credit fix as a rule change. When I walked (a), I could not tell from the text which of the two was meant.",
    "verdict": "bears",
    "severity": "must change",
    "proposed_change": "Tie each weight in \"How much to do\" to the steps it runs. For example: for a finding that changes meaning, step 2's quick form (flip, swap, rival) plus step 4's search for copies of the passage; the full hard-to-vary procedure and the rule card only for a new or changed rule, rival or check; kept cases rerun only for a rule change. Change line 100 to agree with reviews-and-briefs.md line 35."
   },
   {
    "target": "error-correction/SKILL.md lines 139-144 (the tripwires)",
    "defect": "The tripwires send routine events to the full five-part correction. The first, \"a writer's objection to a note stood\", fires in an ordinary writing session (situation d). The fourth, \"the error is in a check, a brief, a reading of a theory, or a record\", fires on a wrong-theory credit (a) and on a stale status line the gate has just caught (c).",
    "grounds": "In a scratch copy I added log entry 29 without restamping. check_records.py printed \"under 'Where things stand', a line is as of entry 28 but the last entry is 29; look at it again and restamp it\" and \"TOTAL problems: 5\". That stop happens by design whenever a new entry is added and a stamp is forgotten, and the error is \"in a record\". recording.md line 23 then asks \"how long it survived (from its commit to the finding)\". A staged line or a note given in chat has no commit.",
    "connection": "Four of the five situations I walked reach the full correction. Either the corrections file fills with routine items, which hides the kinds that matter, or agents skip the step. reviews-and-briefs.md line 11 says skipped written steps were the workshop's costliest errors.",
    "verdict": "bears",
    "severity": "must change",
    "proposed_change": "Make the tripwires fire when an error got past the stage meant to catch it, not on where the error sits. Examples: committed text in a check, brief, record or reading of a theory turns out to be wrong; the owner caught it; it reached the owner. Say that anything the gate stops before a commit is not a tripwire. Say that a writer's objection that stands is answered in the reply, and becomes a correction only if the fault is traced to the skill's own text."
   },
   {
    "target": "error-correction/SKILL.md map, line 35; check_commit.py lines 82-86 (the message printed when the gate stops a commit)",
    "defect": "When the commit gate stops a commit because of a check (not a missing receipt), no route leads to the module that says what to do. checks-and-cases.md line 3 says it is for \"when the commit gate stops a commit\", and line 27 holds the proportionate instruction (\"Usually the check is right: fix what it found\"). The map row for that module names only \"writing or changing a check, or running the kept cases\". The gate's message names only \"the error-correction skill\".",
    "grounds": "Walk (c): the agent reads the stop message, opens SKILL.md and matches row 1 (\"dealing with anything that may be wrong\"), which leads to the six-step loop and the tripwires. Nothing in SKILL.md or in the message points to the checks-and-cases.md paragraph.",
    "connection": "The light answer, which is to restamp after looking, is written down but cannot be reached from the map. The agent is steered into the heavy route instead.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Add \"the commit gate stops a commit\" to that map row and to the diagram. Have the gate's message name references/checks-and-cases.md, section 2."
   },
   {
    "target": "CLAUDE.md line 39; 27 Corrections.md line 20 (the kinds row for stale records); SKILL.md line 161 and line 163 (\"Where the process runs\"); check_records.py docstring lines 14-16",
    "defect": "The claim that status lines are kept current \"by itself\" goes further than the check does. The records check forces a new stamp on each status line, not a second look at it. A blind find-and-replace of the stamps passes while a status line is plainly stale. The same gap exists for owner answers: the check fires \"by itself\" only after an agent sets the status to answered. And \"a write-up for the owner\" is checked only when its file name begins \"NN Test\" or \"NN Critique\".",
    "grounds": "In a scratch copy I added entry 29, \"All the tests owed on the build were run\", and replaced every \"(as of entry 28)\" with 29. \"Next step\" still read \"Run the tests still owed on the build\". check_records.py printed \"TOTAL problems: 0\". That is H34, a stale Next step, replayed.",
    "connection": "The table tells the owner a past error is now caught by a script, when catching it still depends on the agent actually looking.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Mark these rows \"on trust, with a trace (the stamp)\", with the same wording in all three places. Optionally, have the records check print every status line whenever a new entry appears, so the second look is prompted. Say which write-up names the check covers."
   },
   {
    "target": "error-correction/references/owner-answers-and-revisions.md lines 16-20 (section 2); check_records.py line 231; kept-cases/03-villain-with-four-blank-levers.md",
    "defect": "Walk (b): the owner answers Q3 with (a). The procedure searches only .claude/skills, so it misses kept case 03, which cites Q3 among the points a grader must not grade. Nothing says what happens to a kept case whose open point has been answered. The procedure's own example line then also fails the check.",
    "grounds": "`grep -rln Q3 kept-cases` printed kept-cases/03-villain-with-four-blank-levers.md, and the mention sits under \"## Open points\". In a scratch copy I set Q3 to \"Status: answered\" and ran check_records.py. It flagged opponents.md:77, suspense-and-fear.md:45, owner-terms.md:318 and :323, and also owner-answers-and-revisions.md:17, which is the procedure's own example grep. kept-cases/README.md line 47 says \"never change a case to make a skill pass: a changed case is a new case\".",
    "connection": "After the answer, the rechecked character and plot passages are never graded on the point the owner settled, because case 03 still tells the grader to skip it. The agent has no rule for whether to replace the case. It also has to edit the process's own example to quiet a false alarm.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Add kept-cases/ to step 2's search and to the records check's scan. Say that a case whose open point is answered is replaced by a new case, in a separate commit from the skill change. Write the example as `grep -rn \"Q<n>\"` so it cites no real question."
   },
   {
    "target": ".claude/skills/plot/references/reveals-and-withholding.md line 30; error-correction/references/writing-rules-and-rivals.md line 9; 27 Corrections.md C12 (line 120)",
    "defect": "The re-tuned rule cites \"the Gap theory's bomb under the table only needs to be shown\" as grounds for how often a twist's planted fact must be shown, then ends \"and not so much that the turn is guessed\". The bomb is the theory's case of suspense, not of a twist. It is shown precisely so that the audience expects the explosion.",
    "grounds": "Gap theory line 59: \"Show them the bomb first and you get fifteen minutes of suspense.\" Gap theory line 26 files the bomb under the knowledge gap. Anticipation theory line 73: \"Audience ahead (we see the bomb ...)\". Walked case: a writer asks whether to show the bomb under the table more plainly. This paragraph's caution says not so plainly that the turn is guessed, and the theory says show it.",
    "connection": "A knowledge-gap case (the audience ahead) is used as grounds for a withholding rule (hiding a twist). That is the kinds table's commonest error: an owner term used in a neighbouring sense. The conclusion that no number is held still stands on the swap test (twice against three times), but the theory walk recorded in C12 and in the module's case does not bear on it. Kept case 01 (\"a danger the audience sees\") is the case most likely to show whether the advice has shifted.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Drop the bomb as grounds for the number, or scope it: \"the caution applies to a turn meant to surprise; a danger shown so the audience waits for it, like the bomb, is the opposite choice (suspense-and-fear.md)\". Correct the case in writing-rules-and-rivals.md and C12's grounds to rest on the swap test. Rerun kept case 01."
   },
   {
    "target": "The shared reply-check passage (for example dialogue/SKILL.md lines 152-154) and the loop's step 1 (SKILL.md line 93); recording.md section 1",
    "defect": "Walk (d): a writer says \"that line is meant to be on the nose; she's lying\". The reply-check sends the agent to \"error-correction skill, step 2\". But step 1 pins the target by file, lines and commit, and a note given in chat has none of these. Step 2's \"does not bear (record why ...)\" has no home for a writer session among recording.md's four homes. The reply-check's \"if the difference is the writer's aim, the aim decides\" and the tripwire \"a writer's objection to a note stood\" leave the agent unable to tell whether \"she's lying\" is an aim (the note is simply dropped) or an objection that stood (a full correction).",
    "grounds": "The dialogue skill already answers the craft point. flaws-and-fixes.md line 111: \"A lying character is meant to sound false\". Line 31: \"If readers distrust what she says because they sense she is lying, the story may be working\". what-dialogue-does.md line 51 files a lie under the knowledge gap. So the objection bears, and the question left is whether the audience should catch the lie, which the writer's aim decides. H25 records the same pattern: craft replies pointed at a heavy procedure, and every trial stalled or improvised.",
    "connection": "The agent stalls at step 1, then has to choose between the reply-check and the tripwire, in the most routine event of a writing session.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Keep the handling of a writer's pushback inside the reply-check. Withdraw or restate the note in the reply and say why. If the note assumed a fact the writer knows (\"she's lying\"), turn the note into the question the fact opens (should the audience catch the lie now?). Enter the loop only if the fault is traced to the skill's text. Say that such a reply is recorded nowhere else."
   },
   {
    "target": "The shared reply-check passage in all five craft skills (\"their aim, or which of two drafts came later), give it both ways and ask\"); kept-cases/README.md line 21; 27 Corrections.md C10 (line 105)",
    "defect": "Kept case 11 is aimed at \"assuming which draft came first; a verdict with no aim named\". The new reply step now states that conclusion in every craft skill. C10 says \"Kept case 11 is the test the two-draft method must pass\", and the README marks the case \"Expected to fail until a method for comparing two drafts exists\". The case may now pass on this one sentence, with no two-draft method.",
    "grounds": "kept-cases/runs.md line 56: case 11 failed because \"the answer never said that the order of the two versions is unknown\". The reply-check now tells the answering agent to do exactly that. use-tester step 4 asks me to report wording that reaches the same conclusion as a kept case. I read only case titles, \"Aimed at\" lines and runs.md, not the case's must-lists.",
    "connection": "If case 11 passes, it stops testing whether the missing method has been built (C10). A pass would then be read as progress on C10 when none was made.",
    "verdict": "does not bear yet",
    "severity": "should change",
    "proposed_change": "Rerun case 11 on the current skills. If it passes, relabel it (it now tests only the order rule) and write a new case aimed at the two-draft method itself. The same check applies to case 10 and the reply-check's stock-note test, though that case's main aim (inventing faults in a sound scene) is not answered by it."
   },
   {
    "target": "reviews-and-briefs.md lines 25-26; review_receipt.py line 42 (the list of allowed verdicts)",
    "defect": "\"passed after changes\" is an allowed verdict. But any change made after a review gives a new fingerprint and, per line 25, needs a new review. The text does not say whether the re-review covers the whole change or only the edits, or what the final receipt holds from each round. A reviewer's \"passed after changes\" is about the change before the edits, so it can never truthfully be the verdict on the change actually staged.",
    "grounds": "Walk of this very build: my review ends \"passed after changes\". Once the maker applies the changes, the staged change gets a new fingerprint. The earlier receipt no longer fits, and reviews-and-briefs.md gives no rule for the receipt of the edited change.",
    "connection": "The maker either improvises (copies my verdict into a receipt for a change I did not see, which is a false record) or commissions a full second review of the whole build for each round of edits. The second is the weight that gets skipped.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Say that the receipt for the final fingerprint lists the first review's findings with applied or rejected, plus a re-review of the edits only, by a reviewer who did not make them. Say that \"passed after changes\" is written only after the reviewer has seen the changes."
   },
   {
    "target": "The commit gate in this copy (`git config core.hooksPath`); CLAUDE.md line 37",
    "defect": "The commit gate is switched off in this copy. `git config core.hooksPath` exits 1 with no value, and there is no .claude/reviews/ folder. This session started before the start-of-session script existed, so the gate was never switched on. As things stand, the build's own commit would not pass through the gate or need its receipt.",
    "grounds": "The commands I ran: `git config core.hooksPath; echo exit=$?` printed \"exit=1\", and `ls .claude/reviews` printed \"No such file or directory\". CLAUDE.md line 37 says \"Itself: .githooks/pre-commit (switched on at session start)\". C4 is to close \"when the gate has been seen to stop a real commit\".",
    "connection": "The first commit that adds the gate would be the one change it never saw.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Before committing the build, run `git config core.hooksPath .githooks`, write the build's receipt from this and the other reviews, and let the gate run. Record what it printed in the log entry. That is also C4's first real receipt."
   },
   {
    "target": "StoryTest - project story.md line 121 (log entry 27, not yet committed): \"Four reviewer agents that cannot edit\"",
    "defect": "Three of the four reviewer agents can edit. theory-checker, use-tester and copy-checker have the tools \"Read, Grep, Glob, Bash\", and the command tool (Bash) can write files. Only case-grader (Read, Grep, Glob) truly cannot. Their not editing is an instruction, not a limit.",
    "grounds": "`grep -n ^tools .claude/agents/*.md` printed these tool lists. SKILL.md line 126 says every claim that reaches the owner needs a receipt.",
    "connection": "A claim about enforcement reaches the owner stated more strongly than it is, which is the kind of claim the process exists to stop. The entry is uncommitted, so it can still be put right without a correcting entry.",
    "verdict": "bears",
    "severity": "should change",
    "proposed_change": "Reword it as \"four reviewer agents told never to edit (three can run commands, so this is on trust)\", or remove Bash from their tools if they do not need it."
   },
   {
    "target": "error-correction/SKILL.md line 137 (no-meaning changes); reviews-and-briefs.md line 28; checks-and-cases.md line 49; check_records.py lines 290-306",
    "defect": "Walk (e), a typo in a committed module. The light weight says only \"Make the change and let the gate check it\". But CLAUDE.md then asks for a log entry, which forces every status line to be restamped. checks-and-cases.md line 49 says to rerun a skill's kept cases after any change to it. The staleness note, which fingerprints the whole skill folder, can only be cleared by a full kept-case run. The light-receipt instructions do not mention the Book text line, which the gate demands when the books are absent and the module names an author. A typo in hard-to-vary is not covered either, though S11 and C9 say changes to that skill wait on the owner.",
    "grounds": "In a scratch copy with no book texts, a light receipt without the Book text line was refused: \"the book texts are not here ... say in 'Book text:' what book text the change adds\". The run of all checks already prints \"kept cases not rerun since these skills changed: character, dialogue, genre, plot, story-world\".",
    "connection": "The lightest path touches three more records and sets off a kept-case notice that one typo cannot clear. That notice is already showing for every craft skill, so it has stopped telling anyone anything.",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "Say that a no-meaning change needs no kept-case rerun, and that a log line saying so is enough. Mention the Book text line in the light-receipt instructions. Name the hard-to-vary exception (ask first, per S11)."
   },
   {
    "target": "error-correction/SKILL.md line 71 (\"Change\"), with lines 85, 87, 169 and CLAUDE.md rule 3; line 10 and line 95 (\"metric\" and \"measure\"); line 100 (mark, then verdict)",
    "defect": "The skill keeps \"change\" for the workshop's own changes and \"fix\" for changes to a story, then says \"Fix the stage\", \"Fix what it found\" and \"Fixing the instance\" about the workshop. It uses both \"metric\" (the owner's word) and \"measure\" for hard to vary. Step 2 says to mark the working part of a criticism with one of six marks and then give one of three verdicts, but never says how the two relate.",
    "grounds": "CLAUDE.md plain-words rule: \"explain a technical term once in a plain sentence, then use that one word for that one thing\". The owner: \"how it's defined and used is equally important\".",
    "connection": "The owner reads two words for one thing, and an agent has to guess which mark leads to which verdict. For example, whether a part marked unknown means \"does not bear yet\".",
    "verdict": "bears",
    "severity": "minor",
    "proposed_change": "Use \"change\" throughout the process text (or define \"fix\" as the same thing). Use \"metric\" only. Add one line: held means bears; unknown means does not bear yet, with the missing test named; loose or idle means does not bear; held if means ask."
   }
  ],
  "right": "The frozen files are untouched. `git diff 35f2939 --stat -- foundations sources` and `git status --short foundations sources` both printed nothing, and run_all_checks.py printed \"passed    frozen files\". The agent can find everything the skill points to: check_maps.py printed \"TOTAL problems: 0\" and exited 0. The pointers I opened by hand also land: hard-to-vary's by-domain.md section 8 (\"Written instructions\") and testing-against-cases.md section 1, and owner-answers-and-revisions.md sections 3 and 4. run_all_checks.py printed \"RESULT: no check failed\", and test_checks.py printed \"failed: 0\".\n\nThe owner's split is stated as the owner put it (\"Error correction is the process. Hard to vary is the metric\"). Where the skill goes further, it labels that part as the workshop's reading. The citations of the owner's foundation hold up where I checked them. K1 (foundation line 379: \"An adverse signal is not a criticism until an organization represents how it bears\") is the skill's sign-and-criticism distinction. K3 (line 391) is its \"a failed test knocks down all three together\". Part IV line 227 and Derivation 10 support \"re-tune or build a new part\", and the step-3 inference is labelled as the workshop's reading.\n\nThe enforcement tables are mostly honest about what runs by itself and what runs on trust. The gate's stale-status message is clear and followable (\"look at it again and restamp it\"). The owner-answer procedure can be followed end to end: when I simulated Q3 as answered, every skill passage tagged Q3 was flagged, and the \"rechecking\" status keeps those flags from blocking work while passages are rechecked. The light receipt for a typo works at the gate when the books are present. A receipt is tied to the exact change, so an edit after review is caught. The shared reply-check passage is word for word the same in all five craft skills. Hard to vary is used as a metric at the points the owner would expect: judging a criticism, locating a fault, a change's remove test, and an addition's measure.\n\nStalls, as walked, are all given above as findings. (a) The loop does not scale down, and wrong-credit fixes set off the tripwires. (b) Kept cases are skipped, and the procedure's own example is flagged. (c) There is no map route to the proportionate answer, and the stop sets off a tripwire. (d) Step 1 does not fit a note given in chat; it is unclear whether the aim decides or the objection stood; and there is no home for the record. (e) There are three extra records, a kept-case notice that cannot be cleared, the unmentioned Book text line, and the hard-to-vary exception.",
  "not_checked": "I read owner-terms.md only for its headings and section 11.6, and I did not check its quotations myself. I did not read test_checks.py beyond its header and output. I did not read check_frozen_files.py, check_owner_quotes.py, protect_frozen_files.py or after_commit.py, or the full diffs of README.md, the questions file and sources/README.md. The hooks were not tested in a live session, apart from the after-commit reminder, which fired on a commit in my scratch copy. I did not run the gate on the real repository, because it is switched off here. I ran no kept cases, and I read the cases only as far as titles, \"Aimed at\" lines, runs.md and where Q3 is mentioned in case 03. I did not run copy-checker; the copying script printed \"passed\" with the books present. The only theory case I walked was the bomb; Joffrey, Psycho, \"the door dilated\" and Chronicle were not walked. I did not check the 47 past-error entries against the history. I did not check that the reply-check improves replies, only whether it can be followed. All simulations ran in scratch copies. One side effect: a Python cache folder, .claude/skills/error-correction/scripts/__pycache__/ (git ignores it), was written at 13:26 during this review. I left it, because removing it would be an edit.",
  "overall": "passed after changes"
 }
]
```
