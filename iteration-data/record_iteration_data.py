#!/usr/bin/env python3
"""Record the data from the revision rounds of The Long Places and Seconds as tables.

The two stories were written and revised on branch
claude/story-questioning-theme-ehokf0, outside the stages (log entry 37 of
the workshop's project story). Each round there ran critics, a checker that
advised which of their findings were real, one review by Fable, and a ruling
by the main session. This script reads what those rounds left behind and
writes it as tables, so that the process can be judged on its record.

What it reads:
  - the checker's advice files, committed on the story branch (read with
    "git show", so nothing needs to be checked out): one row per finding the
    checker weighed, with the critic who raised it and the checker's verdict;
  - the run records of the workflows (the helper-agent runs), which this
    session's Claude Code kept outside the repository: when each run ended,
    how long it took, how many agents it used and how many tokens they read
    and wrote, as the workflow runtime reported them;
  - the call logs of the two outside models, GLM and MiMo, kept in the same
    session's working folder: one row per call, with its time and tokens.

What it writes, in the folder it lives in:
  findings.csv     one row per finding a checker weighed
  runs.csv         one row per workflow run
  model-calls.csv  one row per call to GLM or MiMo
and prints a short summary of each, which log entry 37 quotes.

A finding is credited to every critic its checker's table names, including
a critic the table says marked it a quibble; and on Seconds the checker,
MiMo, also weighed findings the critics had not marked substantive, and
weighed its own. So a critic's count is "findings the checker weighed that
name this critic", not "findings this critic marked substantive".

Only findings.csv can be made again once the session that ran the stories
has ended: the run records and the call logs lived in that session's folders.
Given only --story-branch, the script remakes findings.csv alone.

The hand-made tables beside it (rounds.csv, audience.csv, errors.csv) are
not written by this script; each row there names the file it came from.

Usage:
  python3 record_iteration_data.py --story-branch BRANCH [--workflow-records FOLDER
                                   --glm-log FILE --mimo-log FILE] [--repository PATH]
"""
import argparse
import csv
import glob
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# Which committed files hold the checker's advice for each round, by story.
CHECKER_FILES = {
    "The Long Places": ("stories/the-long-places", r"^(\d+) Round (\d+).* - the checker's advice\.md$"),
    "Seconds": ("stories/fourth-direction-season", r"^(\d+) Round (\d+).* - (?:MiMo's advice|the Claude checker's advice)\.md$"),
}


def git(repository, *arguments):
    result = subprocess.run(["git", "-C", repository, *arguments], capture_output=True, text=True)
    if result.returncode != 0:
        sys.exit(f"git {' '.join(arguments)} failed: {result.stderr.strip()}")
    return result.stdout


def plain_verdict(cell):
    """The checker's verdict, reduced to one of its three words, or the cell as written."""
    words = re.sub(r"[*_`]", "", cell).strip()
    for verdict in ("CONFIRMED", "QUIBBLE", "WRONG"):
        if words.upper().startswith(verdict):
            return verdict
    return words


def plain_critics(cell):
    """The critics named in a table cell, as short lower-case names joined by '+'."""
    words = re.sub(r"[*_`]", "", cell).lower()
    names = []
    for name in ("story", "people", "continuity", "mimo", "fable"):
        # Some tables shorten the continuity critic to "Cont. 3".
        if name in words or (name == "continuity" and re.search(r"\bcont\b", words)):
            names.append(name)
    return "+".join(names) if names else words.strip()


def read_checker_table(text):
    """Every row of the first table whose heading names a Critic and a Verdict column."""
    lines = text.splitlines()
    rows = []
    for index, line in enumerate(lines):
        if line.startswith("|") and "Critic" in line and "Verdict" in line:
            headings = [cell.strip() for cell in line.strip().strip("|").split("|")]
            critic_column = next(i for i, h in enumerate(headings) if h.startswith("Critic"))
            verdict_column = next(i for i, h in enumerate(headings) if h.startswith("Verdict"))
            finding_column = next((i for i, h in enumerate(headings) if h.startswith("Finding")), None)
            for row_line in lines[index + 2:]:
                if not row_line.startswith("|"):
                    break
                cells = [cell.strip() for cell in row_line.strip().strip("|").split("|")]
                if len(cells) <= max(critic_column, verdict_column):
                    continue
                finding = cells[finding_column] if finding_column is not None else ""
                rows.append((plain_critics(cells[critic_column]), plain_verdict(cells[verdict_column]),
                             re.sub(r"\s+", " ", finding)[:160]))
            break
    return rows


def record_findings(repository, branch):
    out_rows = []
    for story, (folder, pattern) in CHECKER_FILES.items():
        names = git(repository, "ls-tree", "--name-only", f"{branch}:{folder}").splitlines()
        for name in sorted(names):
            match = re.match(pattern, name)
            if not match:
                continue
            round_number = int(match.group(2))
            text = git(repository, "show", f"{branch}:{folder}/{name}")
            checker = "MiMo" if "MiMo's advice" in name else "Claude checker"
            table_rows = read_checker_table(text)
            if not table_rows:
                # Round 8 of The Long Places used a must-fix list, not a Critic/Verdict table: say so, never count it as zero findings.
                print(f"note: no Critic/Verdict table in {folder}/{name}; nothing read from it")
            for critics, verdict, finding in table_rows:
                out_rows.append({"story": story, "round": round_number, "checker": checker, "critics": critics,
                                 "verdict": verdict, "finding": finding, "source": f"{folder}/{name}"})
    return out_rows


def record_runs(folder):
    out_rows = []
    for path in glob.glob(os.path.join(folder, "wf_*.json")):
        with open(path, encoding="utf-8") as record_file:
            record = json.load(record_file)
        out_rows.append({"ended": record.get("timestamp", ""), "workflow": record.get("workflowName", ""),
                         "status": record.get("status", ""),
                         "minutes": round((record.get("durationMs") or 0) / 60000, 1),
                         "agents": record.get("agentCount", ""), "tokens": record.get("totalTokens", ""),
                         "run": record.get("runId", "")})
    return sorted(out_rows, key=lambda row: row["ended"])


def record_model_calls(glm_log, mimo_log):
    out_rows = []
    for path, default_model in ((glm_log, "glm-5.3"), (mimo_log, "mimo-v2.6-pro")):
        with open(path, encoding="utf-8") as log_file:
            for line in log_file:
                if not line.strip():
                    continue
                call = json.loads(line)
                usage = call.get("usage") or {}
                out_rows.append({"model": call.get("model", default_model), "label": call.get("label", ""),
                                 "attempt": call.get("attempt", ""), "seconds": call.get("seconds", ""),
                                 "prompt_tokens": usage.get("prompt_tokens", ""),
                                 "completion_tokens": usage.get("completion_tokens", ""),
                                 "refused_by_safety_filter": call.get("refused_by_safety_filter", "")})
    return out_rows


def write_table(name, rows):
    path = os.path.join(HERE, name)
    with open(path, "w", encoding="utf-8", newline="") as table_file:
        writer = csv.DictWriter(table_file, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--story-branch", required=True)
    parser.add_argument("--workflow-records")
    parser.add_argument("--glm-log")
    parser.add_argument("--mimo-log")
    parser.add_argument("--repository", default=os.path.dirname(HERE))
    arguments = parser.parse_args()
    session_sources = (arguments.workflow_records, arguments.glm_log, arguments.mimo_log)
    if any(session_sources) and not all(session_sources):
        sys.exit("give all three of --workflow-records, --glm-log and --mimo-log, or none (to remake findings.csv alone)")

    findings = record_findings(arguments.repository, arguments.story_branch)
    runs = record_runs(arguments.workflow_records) if all(session_sources) else []
    calls = record_model_calls(arguments.glm_log, arguments.mimo_log) if all(session_sources) else []
    if all(session_sources) and not runs:
        sys.exit(f"no wf_*.json run records found in {arguments.workflow_records}; nothing written")
    if all(session_sources) and not calls:
        sys.exit("the GLM and MiMo call logs hold no calls; nothing written")
    tables = [("findings.csv", findings)] + ([("runs.csv", runs), ("model-calls.csv", calls)] if all(session_sources) else [])
    for name, rows in tables:
        print(f"wrote {write_table(name, rows)}: {len(rows)} rows")
    if not all(session_sources):
        print("runs.csv and model-calls.csv left as they are: their sources were not given")

    print("\nFindings the checkers weighed, by story, round and verdict:")
    table = {}
    for row in findings:
        key = (row["story"], row["round"], row["checker"])
        table.setdefault(key, {}).setdefault(row["verdict"], 0)
        table[key][row["verdict"]] += 1
    for key in sorted(table):
        print(f"  {key[0]}, round {key[1]} ({key[2]}): {table[key]}")

    print("\nBy critic (every round together), the checker's verdicts:")
    by_critic = {}
    for row in findings:
        for critic in row["critics"].split("+"):
            key = (row["story"], critic)
            by_critic.setdefault(key, {}).setdefault(row["verdict"], 0)
            by_critic[key][row["verdict"]] += 1
    for key in sorted(by_critic):
        print(f"  {key[0]}, {key[1]}: {by_critic[key]}")

    if not runs:
        return
    print("\nWorkflow runs:", len(runs), "| minutes in all:", round(sum(r["minutes"] for r in runs), 1),
          "| tokens in all (as the runtime reported):", sum(int(r["tokens"] or 0) for r in runs))
    for model in sorted({c["model"] for c in calls}):
        these = [c for c in calls if c["model"] == model]
        print(f"{model}: {len(these)} calls, {round(sum(int(c['seconds'] or 0) for c in these) / 3600, 1)} hours,"
              f" refused by its safety filter: {sum(1 for c in these if c['refused_by_safety_filter'])}")


if __name__ == "__main__":
    main()
