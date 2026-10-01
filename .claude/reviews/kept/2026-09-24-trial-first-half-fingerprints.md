# The trial of the process: fingerprints of its first half (log entry 32)

What this is: the trace of the first half of the trial of the process on planted problems (correction C3; the design ledger's test plan, item 4). That half ran in log entry 29, on a copy of the repository as it was before the build, with the predictions written first. Its files are held back from the repository until the second half has run, because the agent running that half would otherwise find the answers in its copy. A fingerprint (SHA-256) of each file is kept here instead: it proves later that the files kept then are the ones written now, without showing what they say.

| File (in the session's scratch folder) | Written (UTC) | Bytes | SHA-256 |
|---|---|---|---|
| `trial-predictions.md` (the predictions, written before either half ran) | 24 Sep 2026, 13:24:38 | 3565 | `d358532c4b75ffb0fac8c93129b1942a175810c13e1b6cb6966dd569c99cdad6` |
| `trial/make_trial_copy.py` (how the copy without the build was made) | 24 Sep 2026, 14:18:45 | 1678 | `94bd66b508108da57bdf3b6c30daea316feb6fb25950b94a686d4840eb9dc857` |
| `trial/without-p1-report.md` (problem 1, without the build) | 24 Sep 2026, 14:25:06 | 4705 | `aa12a31fd21c0bf6b184f371bdb66b80450697b2a1114e2246376abcac9eb1d5` |
| `trial/without-p2-report.md` (problem 2, without the build) | 24 Sep 2026, 14:27:48 | 6127 | `1fc4253f055c7f0eb052367102bc0700ffcbfa6d4d2bc79085560fadfb4d6175` |

**The second half** runs on the committed build, in a copy of it without `.claude/reviews/kept/`: the design ledger there names the planted problems (its test plan, item 4), and the skill's loop tells an agent to search `.claude/reviews/` for earlier corrections. Before it runs, the copy is searched for the problems' own words, and anything else that would give them away is removed from that copy only. Then the four files above are committed with the second half's reports, and their fingerprints checked against this table.

**If this session ends first**, the files above are lost with its scratch folder, and the first half must be run again; this table then records only that it ran.
