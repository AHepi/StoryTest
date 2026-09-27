#!/usr/bin/env python3
"""Revise the whole Seconds season with GLM 5.3, round after round, until only quibbles are left,
with Claude (the main session) as the final authority on what gets fixed.

Each time it runs, it does the next step and stops:
  review   Three GLM critics read the whole season, each through one lens, and a MiMo critic
           (a different model, MiMo v2.6 Pro) reads it with fresh eyes. Each marks every
           finding SUBSTANTIVE (a real problem a viewer would notice) or QUIBBLE (word
           placement, the exact timing of an event, taste: better left to an audience test).
           A MiMo verifier checks every SUBSTANTIVE finding and gives its advice.
           The season as reviewed is saved as one document. Then it stops.
  (wait)   Claude reads the critiques, the advice and Fable's review, checks them against the
           season, and writes round-N/ruling.md: which findings are real and must be fixed,
           ending with "RULING: FIX <n>" or "RULING: DONE". Nothing is changed without it.
  revise   GLM writes a plan for exactly what the ruling orders, and GLM revisers rewrite each
           episode that needs changes, five at a time, each with a plain log. The full revised
           season is saved as one document (for Fable 5.1's single review). Then it stops.
When a ruling says DONE, the final season is written to final/. At most MAX_ROUNDS rounds.
Every file of every round is kept in round-N folders.

Usage: python3 glm_seconds_rounds.py   (run after glm_seconds_pipeline.py has finished; run again after each step)
"""
import concurrent.futures
import json
import os
import re
import time

import requests

from glm_seconds_pipeline import LOG_FILE, ask_glm, claude_final, path, read, rules, write

MIMO_ENDPOINT = "https://token-plan-sgp.xiaomimimo.com/v1/chat/completions"
MIMO_MODEL = "mimo-v2.6-pro"
MIMO_KEY_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".mimo_key")
# MiMo's maker runs a safety filter that sometimes blocks an answer about this crime story and sends this sentence instead.
MIMO_REFUSAL = re.compile(r"request was rejected because it was considered high risk", re.I)
FICTION_NOTE = ("This is a work of fiction under editorial review: a television drama about a family of thieves. "
                "Your task is purely literary: judging the writing, its logic and its craft.\n\n")


class MimoRefused(RuntimeError):
    """MiMo's safety filter blocked the answer three times running."""


def ask_mimo(label, prompt, output_name):
    """Send one prompt to MiMo with deep thinking and streaming; save answer and thinking; return the answer."""
    if os.path.exists(path(output_name)):
        print(f"[{label}] already done", flush=True)
        return read(path(output_name))
    key = read(MIMO_KEY_FILE).strip()
    body = {"model": MIMO_MODEL, "messages": [{"role": "user", "content": prompt}],
            "thinking": {"type": "enabled"}, "max_tokens": 128000, "stream": True}
    refusals = 0
    for attempt in range(1, 13):
        started = time.time()
        answer, thinking, usage = [], [], {}
        try:
            with requests.post(MIMO_ENDPOINT, json=body, stream=True, timeout=(30, 900),
                               headers={"Authorization": f"Bearer {key}"}) as response:
                if response.status_code != 200:
                    raise RuntimeError(f"status {response.status_code}: {response.text[:300]}")
                response.encoding = "utf-8"  # MiMo's server does not name its alphabet, so accented letters came out garbled
                for line in response.iter_lines(decode_unicode=True):
                    if not line or not line.startswith("data:"):
                        continue
                    data = line[5:].strip()
                    if data == "[DONE]":
                        break
                    chunk = json.loads(data)
                    if chunk.get("error"):
                        raise RuntimeError(str(chunk["error"])[:300])
                    usage = chunk.get("usage") or usage
                    for choice in chunk.get("choices", []):
                        delta = choice.get("delta", {})
                        if delta.get("reasoning_content"):
                            thinking.append(delta["reasoning_content"])
                        if delta.get("content"):
                            answer.append(delta["content"])
            text = "".join(answer).strip()
            if not text:
                raise RuntimeError("empty answer")
            if MIMO_REFUSAL.search(text) and len(text) < 400:
                refusals += 1
                with open(LOG_FILE, "a", encoding="utf-8") as log:
                    log.write(json.dumps({"label": label, "model": MIMO_MODEL, "output": output_name, "attempt": attempt,
                                          "refused_by_safety_filter": True, "usage": usage}) + "\n")
                if refusals >= 3:
                    raise MimoRefused(f"[{label}] MiMo's safety filter refused the answer three times")
                raise RuntimeError("MiMo's safety filter refused the answer")
            write(path(output_name), text + "\n")
            write(path(os.path.join("thinking", output_name)), "".join(thinking))
            with open(LOG_FILE, "a", encoding="utf-8") as log:
                log.write(json.dumps({"label": label, "model": MIMO_MODEL, "output": output_name, "attempt": attempt,
                                      "seconds": round(time.time() - started), "usage": usage}) + "\n")
            print(f"[{label}] done in {round(time.time() - started)}s", flush=True)
            return text
        except MimoRefused:
            raise
        except Exception as problem:
            wait = 20 if "safety filter" in str(problem) else min(60 * attempt, 300)
            print(f"[{label}] attempt {attempt} failed: {problem}; waiting {wait}s", flush=True)
            time.sleep(wait)
    raise RuntimeError(f"[{label}] gave up after 12 attempts")

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


def version(number):
    """The season after round `number` (version 0 is the season before any round)."""
    episodes = {n: starting_episode(n) for n in range(1, 11)}
    for done in range(1, number + 1):
        for n in range(1, 11):
            revised = path(f"round-{done}/episode-{n:02d}.md")
            if os.path.exists(revised):
                episodes[n] = read(revised)
    return episodes


def confirmed_count(verification):
    match = re.search(r"CONFIRMED SUBSTANTIVE FINDINGS:\s*(\d+)", verification)
    if not match:
        raise SystemExit("the verifier did not end with the count line")
    return int(match.group(1))


def review(number, episodes):
    folder = f"round-{number}"
    season = season_text(episodes)
    write(path(f"{folder}/season-as-reviewed.md"), season + "\n")
    jobs = []
    for name, lens in LENSES.items():
        prompt = f"""{rules()}

THE WHOLE SEASON AS IT STANDS:

{season}

YOUR TASK: you did not write this season. Criticise it through one lens only: {lens}
{SEVERITY}
Write a numbered list of findings, most serious first, at most 20. For each: the episode and scene, the problem, why it matters, a concrete fix, and the mark SUBSTANTIVE or QUIBBLE. Only real findings."""
        jobs.append((ask_glm, f"r{number}-critique-{name}", prompt, f"{folder}/critique-{name}.md"))
    fresh_prompt = f"""{rules()}

THE WHOLE SEASON AS IT STANDS:

{season}

YOUR TASK: you did not write this season, and you come to it fresh. Criticise it as a whole: story and rules, people and feeling, continuity and voice.
{SEVERITY}
Write a numbered list of findings, most serious first, at most 20. For each: the episode and scene, the problem, why it matters, a concrete fix, and the mark SUBSTANTIVE or QUIBBLE. Only real findings."""
    jobs.append((ask_mimo, f"r{number}-critique-mimo", FICTION_NOTE + fresh_prompt, f"{folder}/critique-mimo.md"))
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        critiques = list(pool.map(lambda job: job[0](*job[1:]), jobs))
    names = list(LENSES) + ["mimo (fresh eyes, a different model)"]
    all_critiques = "\n\n".join(f"=== CRITIQUE: {name} ===\n{text}" for name, text in zip(names, critiques))
    verify_prompt = f"""{rules()}

THE WHOLE SEASON:

{season}

FOUR CRITIQUES OF IT:

{all_critiques}

YOUR TASK: you are the verifier. Your verdicts are advice to Claude, who makes the final ruling. For every finding marked SUBSTANTIVE, check it against the season and the plan, and decide: CONFIRMED (a real problem, and substantive by the definition below), QUIBBLE (real but only a quibble), or WRONG (not true of the season). Merge duplicates. Be strict in both directions: do not let a matter of taste pass as substantive, and do not wave away a real problem. Quote the words from the season that decide each verdict.
{SEVERITY}
Write a table: the finding in plain words, which critic, your verdict, and why. Then list the CONFIRMED findings again, numbered, each with the episode(s) it touches. End with exactly one line: CONFIRMED SUBSTANTIVE FINDINGS: <number>"""
    try:
        verification = ask_mimo(f"r{number}-verify", FICTION_NOTE + verify_prompt, f"{folder}/verification.md")
    except MimoRefused:
        write(path(f"{folder}/verifier-note.md"), "MiMo's safety filter refused to give the verifier's answer three times, so GLM gave the advice instead. "
              "Claude, the final authority, weighs it knowing GLM wrote the season.\n")
        verification = ask_glm(f"r{number}-verify-glm", verify_prompt, f"{folder}/verification.md")
    print(f"Round {number} reviewed: the verifier advises {confirmed_count(verification)} confirmed substantive findings. "
          f"Waiting for Claude's ruling in {folder}/ruling.md", flush=True)


def revise_to_ruling(number, episodes, ruling):
    folder = f"round-{number}"
    season = season_text(episodes)
    plan = ask_glm(f"r{number}-plan", f"""{rules()}

THE WHOLE SEASON:

{season}

THE FINAL RULING, BY CLAUDE, WHO HAS THE LAST WORD ON WHAT GETS FIXED:

{ruling}

YOUR TASK: write the revision plan for exactly the findings the ruling orders fixed, and nothing else (never plan a change for a finding the ruling overruled or left as a quibble; quibbles are for an audience test). Where the ruling gives wording or constraints, keep them. Part 1, a table: each ordered finding, and exactly what will change in which episode and scene. Part 2: for every episode from 1 to 10, a heading "Episode N" and a numbered list of exact changes, or "No changes". Keep each change as small as the problem allows.""", f"{folder}/plan.md")

    def revise(episode_number):
        section = re.search(rf"(?ims)^#+\s*Episode {episode_number}\b(.*?)(?=^#+\s*Episode \d+\b|\Z)", plan)
        if section and re.search(r"(?i)no changes", section.group(1)) and len(section.group(1).strip()) < 40:
            return episode_number, episodes[episode_number]
        raw = ask_glm(f"r{number}-revise-{episode_number:02d}", f"""{rules()}

THE WHOLE SEASON:

{season}

THE REVISION PLAN (it carries out Claude's final ruling):

{plan}

YOUR TASK: rewrite episode {episode_number} in full, making every change the plan lists for Episode {episode_number} and nothing that would break the other episodes. Keep everything that works and keep the format. Then, after a line containing only ===LOG===, list in plain everyday words each change you made and any planned change you could not make, and why. If the plan lists no changes for Episode {episode_number}, write only the line NO CHANGES.""", f"{folder}/episode-{episode_number:02d}-raw.md")
        if raw.strip().startswith("NO CHANGES"):
            return episode_number, episodes[episode_number]
        text, _, log = raw.partition("===LOG===")
        if not log:
            # GLM sometimes marks its notes with a bare line of "===" instead; never let notes leak into an episode.
            loose = re.search(r"(?m)^={3,}\s*$", raw)
            if loose:
                text, log = raw[:loose.start()], raw[loose.end():]
        write(path(f"{folder}/episode-{episode_number:02d}.md"), text.strip() + "\n")
        write(path(f"{folder}/episode-{episode_number:02d}-log.md"), log.strip() + "\n")
        return episode_number, text.strip() + "\n"

    revised = dict(episodes)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        for episode_number, text in pool.map(revise, range(1, 11)):
            revised[episode_number] = text
    write(path(f"{folder}/full-season.md"), season_text(revised) + "\n")
    write(path(f"{folder}/revision-complete.txt"), "The full revision for this round is finished.\n")
    print(f"Round {number} revision complete: {folder}/full-season.md is ready for Fable's review and the next round.", flush=True)


def main():
    """Do the next step of the rounds, then stop."""
    for number in range(1, MAX_ROUNDS + 1):
        folder = f"round-{number}"
        if not os.path.exists(path(f"{folder}/verification.md")):
            review(number, version(number - 1))
            return
        if not os.path.exists(path(f"{folder}/ruling.md")):
            print(f"Waiting for Claude's ruling in {folder}/ruling.md", flush=True)
            return
        ruling = read(path(f"{folder}/ruling.md"))
        if re.search(r"RULING:\s*DONE", ruling):
            final = version(number - 1)
            for n in range(1, 11):
                write(path(f"final/episode-{n:02d}.md"), final[n])
            write(path("final/full-season.md"), season_text(final) + "\n")
            write(path("final/rounds-summary.md"), f"# Revision rounds\n\nClaude ruled the season finished after round {number}'s review: only quibbles remain.\n")
            print("=== finished: Claude ruled only quibbles remain ===", flush=True)
            return
        if not re.search(r"RULING:\s*FIX\s*\d+", ruling):
            raise SystemExit(f"{folder}/ruling.md does not end with RULING: FIX <n> or RULING: DONE")
        if not os.path.exists(path(f"{folder}/revision-complete.txt")):
            revise_to_ruling(number, version(number - 1), ruling)
            return
    print(f"Reached the cap of {MAX_ROUNDS} rounds; Claude decides what happens next.", flush=True)


if __name__ == "__main__":
    main()
