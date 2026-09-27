#!/usr/bin/env python3
"""Revise the whole Seconds season with GLM 5.3, round after round, until only quibbles are left.

What it does, each round:
  1. Three GLM critics read the whole season, each through one lens, and mark every
     finding SUBSTANTIVE (a real problem a viewer would notice) or QUIBBLE (word
     placement, the exact timing of an event, taste: better left to an audience test).
  2. A GLM verifier checks every SUBSTANTIVE finding and keeps only the real ones.
  3. If none are confirmed, the rounds stop.
  4. Otherwise GLM writes a revision plan by episode, and GLM revisers rewrite each
     episode that needs changes, three at a time, each with a plain log.
At most MAX_ROUNDS rounds. Every file of every round is kept in round-N folders.

Usage: python3 glm_seconds_rounds.py   (run after glm_seconds_pipeline.py has finished)
"""
import concurrent.futures
import os
import re

from glm_seconds_pipeline import ask_glm, claude_final, path, read, rules, write

MAX_ROUNDS = 6
SEVERITY = """HOW TO MARK EACH FINDING:
SUBSTANTIVE means a careful viewer would notice it and it weakens the season: a plot hole or broken logic; a contradiction between scenes or episodes; a breach of the owner's rules or the plan's physics (an echo of The Catch, a banned word or named idea on screen, a secret new rule, a twist revealed early or unplanted); a character acting without cause or against who they are; a scene with no job; pacing that sags; confusion that does not serve the story; a theme stated instead of shown.
QUIBBLE means it could go either way, or only an audience test could settle it: word choice or placement, sentence rhythm, the exact minute or day of an event when nothing depends on it, small matters of taste."""

LENSES = {
    "story": "STORY AND RULES: plot logic, cause and effect, twists and their plants, the plan's physics and numbers, and the owner's rules.",
    "people": "PEOPLE AND FEELING: whether we care before the threat, whether each character acts from their want and wound, the suspense ratchet, the genre's promises, the villain and pursuer, and whether any theme is spoken instead of shown.",
    "continuity": "CONTINUITY AND VOICE: every fact, name, number, date, injury and object across all ten episodes; who knows what when; plants never paid off and payoffs never planted; the seams where the writers change (between episodes 3 and 4); and each character's voice staying their own.",
}


def starting_episode(number):
    """The latest version of each episode before the rounds begin."""
    after_check = path(f"episode-{number:02d}-after-season-check.md")
    if os.path.exists(after_check):
        return read(after_check)
    return read(claude_final(number)) if number <= 3 else read(path(f"episode-{number:02d}-final.md"))


def season_text(episodes):
    return "\n\n".join(episodes[n] for n in range(1, 11))


def confirmed_count(verification):
    match = re.search(r"CONFIRMED SUBSTANTIVE FINDINGS:\s*(\d+)", verification)
    if not match:
        raise SystemExit("the verifier did not end with the count line")
    return int(match.group(1))


def run_round(number, episodes):
    folder = f"round-{number}"
    season = season_text(episodes)
    jobs = []
    for name, lens in LENSES.items():
        prompt = f"""{rules()}

THE WHOLE SEASON AS IT STANDS:

{season}

YOUR TASK: you did not write this season. Criticise it through one lens only: {lens}
{SEVERITY}
Write a numbered list of findings, most serious first, at most 20. For each: the episode and scene, the problem, why it matters, a concrete fix, and the mark SUBSTANTIVE or QUIBBLE. Only real findings."""
        jobs.append((f"r{number}-critique-{name}", prompt, f"{folder}/critique-{name}.md"))
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        critiques = list(pool.map(lambda job: ask_glm(*job), jobs))
    all_critiques = "\n\n".join(f"=== CRITIQUE: {name} ===\n{text}" for name, text in zip(LENSES, critiques))
    verification = ask_glm(f"r{number}-verify", f"""{rules()}

THE WHOLE SEASON:

{season}

THREE CRITIQUES OF IT:

{all_critiques}

YOUR TASK: you are the verifier. For every finding marked SUBSTANTIVE, check it against the season and the plan, and decide: CONFIRMED (a real problem, and substantive by the definition below), QUIBBLE (real but only a quibble), or WRONG (not true of the season). Merge duplicates. Be strict in both directions: do not let a matter of taste pass as substantive, and do not wave away a real problem.
{SEVERITY}
Write a table: the finding in plain words, which critic, your verdict, and why. Then list the CONFIRMED findings again, numbered, each with the episode(s) it touches. End with exactly one line: CONFIRMED SUBSTANTIVE FINDINGS: <number>""", f"{folder}/verification.md")
    count = confirmed_count(verification)
    if count == 0:
        return episodes, 0
    plan = ask_glm(f"r{number}-plan", f"""{rules()}

THE WHOLE SEASON:

{season}

THE VERIFIED FINDINGS:

{verification}

YOUR TASK: write the revision plan for the CONFIRMED findings only (leave quibbles alone; they are for an audience test). Part 1, a table: each confirmed finding, and exactly what will change in which episode and scene. Part 2: for every episode from 1 to 10, a heading "Episode N" and a numbered list of exact changes, or "No changes". Keep each change as small as the problem allows.""", f"{folder}/plan.md")
    revised = dict(episodes)

    def revise(episode_number):
        section = re.search(rf"(?ims)^#+\s*Episode {episode_number}\b(.*?)(?=^#+\s*Episode \d+\b|\Z)", plan)
        if section and re.search(r"(?i)no changes", section.group(1)) and len(section.group(1).strip()) < 40:
            return episode_number, episodes[episode_number]
        raw = ask_glm(f"r{number}-revise-{episode_number:02d}", f"""{rules()}

THE WHOLE SEASON:

{season}

THE REVISION PLAN:

{plan}

YOUR TASK: rewrite episode {episode_number} in full, making every change the plan lists for Episode {episode_number} and nothing that would break the other episodes. Keep everything that works and keep the format. Then, after a line containing only ===LOG===, list in plain everyday words each change you made and any planned change you could not make, and why. If the plan lists no changes for Episode {episode_number}, write only the line NO CHANGES.""", f"{folder}/episode-{episode_number:02d}-raw.md")
        if raw.strip().startswith("NO CHANGES"):
            return episode_number, episodes[episode_number]
        text, _, log = raw.partition("===LOG===")
        write(path(f"{folder}/episode-{episode_number:02d}.md"), text.strip() + "\n")
        write(path(f"{folder}/episode-{episode_number:02d}-log.md"), log.strip() + "\n")
        return episode_number, text.strip() + "\n"

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for episode_number, text in pool.map(revise, range(1, 11)):
            revised[episode_number] = text
    return revised, count


def main():
    episodes = {n: starting_episode(n) for n in range(1, 11)}
    history = []
    for number in range(1, MAX_ROUNDS + 1):
        episodes, count = run_round(number, episodes)
        history.append(f"Round {number}: {count} confirmed substantive findings")
        print(history[-1], flush=True)
        if count == 0:
            break
    else:
        history.append(f"Stopped at the cap of {MAX_ROUNDS} rounds with substantive findings still open.")
    for n in range(1, 11):
        write(path(f"final/episode-{n:02d}.md"), episodes[n])
    write(path("final/rounds-summary.md"), "# Revision rounds\n\n" + "\n".join(f"- {line}" for line in history) + "\n")
    print("=== finished ===", flush=True)


if __name__ == "__main__":
    main()
