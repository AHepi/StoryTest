# Hand tries of the retiring rule, 24 September 2026

What this is: a record that until now lived only in the session's scratch files (the fourth look's theory-checker, finding T13): the output of a hand try of the rule for retiring a planted test that guards the workshop, run twice in scratch copies with the gate switched on, once on the scripts after the third look's answers (entry 30) and once on the scripts after the fourth look's (entry 31). In each try a records check was loosened so that one guarded planted test ('records: hidden text in the log') failed, and the receipt retired that test, with three different 'Reviewed by' lines. The first half of the trial of the process is not kept here yet: its record holds the planted problems and the answers written before it ran, and its second half runs on a copy of the committed build, where that record would hand the answers to the agent being tried. It is kept, with the second half, once the trial has run (entry 31). Kept for log entry 31.

---

## After the third look's answers (entry 30)

```
--- Reviewed by: theory-checker  ->  exit 1
FAILED    the last approved commit's planted-fault test, on the changed checks
          retired in the receipt: records: hidden text in the log
          FAILED  records: hidden text in the log
          not run  gate: the last approved commit's planted-fault test really runs on a changed check (outside the test's own copies): this run is itself inside the planted-fault test
--- Reviewed by: theory-checker (the owner was not asked)  ->  exit 1
FAILED    the last approved commit's planted-fault test, on the changed checks
          retired in the receipt: records: hidden text in the log
          FAILED  records: hidden text in the log
          not run  gate: the last approved commit's planted-fault test really runs on a changed check (outside the test's own copies): this run is itself inside the planted-fault test
--- Reviewed by: the owner  ->  exit 0
passed    the last approved commit's planted-fault test, on the changed checks
          retired in the receipt: records: hidden text in the log
All checks passed; committing.
```

## After the fourth look's answers (entry 31)

```
--- Reviewed by: theory-checker  ->  exit 1
FAILED    the last approved commit's planted-fault test, on the changed checks
          NOT retired (it guards the workshop, so the owner must be named first as reviewer): records: hidden text in the log
          FAILED  records: hidden text in the log
          not run  gate, neighbour: a merge bringing a reviewed hook change goes through the real planted-fault stage (outside the test's own copies): this run is itself inside the planted-fault test
          not run  gate: the last approved commit's planted-fault test really runs on a changed check (outside the test's own copies): this run is itself inside the planted-fault test
--- Reviewed by: theory-checker (the owner was not asked)  ->  exit 1
FAILED    the last approved commit's planted-fault test, on the changed checks
          NOT retired (it guards the workshop, so the owner must be named first as reviewer): records: hidden text in the log
          FAILED  records: hidden text in the log
          not run  gate, neighbour: a merge bringing a reviewed hook change goes through the real planted-fault stage (outside the test's own copies): this run is itself inside the planted-fault test
          not run  gate: the last approved commit's planted-fault test really runs on a changed check (outside the test's own copies): this run is itself inside the planted-fault test
--- Reviewed by: the owner  ->  exit 0
passed    the last approved commit's planted-fault test, on the changed checks
          retired in a receipt: records: hidden text in the log
All checks passed; committing.
```
