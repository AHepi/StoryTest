#!/usr/bin/env python3
"""Have GLM 5.3, at its deepest thinking, carry on writing the Seconds episodes.

What it does: Claude's writers finished episodes 1 to 3 and started 4 and 5.
GLM picks up each episode from the stage it had reached:
  episode 4: revise Claude's draft using Claude's critique;
  episode 5: critique Claude's draft, then revise it;
  episodes 6 to 10: draft, critique, revise;
then GLM checks the whole season for continuity and fixes what it finds.
Every answer, its thinking and its token counts are saved in this folder.

Usage: python3 glm_seconds_pipeline.py
The API key is read from a private file outside the repository.
"""
import concurrent.futures
import json
import os
import time

import requests

FOLDER = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(os.path.dirname(FOLDER), "work")
KEY_FILE = os.path.join(os.path.dirname(FOLDER), ".glm_key")
ENDPOINT = "https://api.z.ai/api/coding/paas/v4/chat/completions"
MODEL = "glm-5.3"
LOG_FILE = os.path.join(FOLDER, "calls-log.jsonl")
TITLES = ["Straight", "The Assayer's Wife", "Making Weight", "The Other Bank", "Delivered",
          "Ten Seconds", "Two Counts", "The Laundry", "The Deep", "Paper"]
SYSTEM_PROMPT = (
    "You are a television writer of great craft, continuing a season that other writers began. "
    "Write in English. Follow the task exactly, and write only what the task asks for, in Markdown, "
    "with no preamble and no closing remarks."
)


def path(name):
    return os.path.join(FOLDER, name)


def read(file_path):
    with open(file_path, encoding="utf-8") as handle:
        return handle.read()


def write(file_path, text):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as handle:
        handle.write(text)


def ask_glm(label, prompt, output_name):
    """Send one prompt to GLM with streaming; save the answer and its thinking; return the answer."""
    if os.path.exists(path(output_name)):
        print(f"[{label}] already done", flush=True)
        return read(path(output_name))
    key = read(KEY_FILE).strip()
    body = {"model": MODEL, "messages": [{"role": "system", "content": SYSTEM_PROMPT},
                                          {"role": "user", "content": prompt}],
            "thinking": {"type": "enabled"}, "reasoning_effort": "max",
            "max_tokens": 128000, "stream": True}
    for attempt in range(1, 7):
        started = time.time()
        answer, thinking, usage = [], [], {}
        try:
            with requests.post(ENDPOINT, json=body, stream=True, timeout=(30, 900),
                               headers={"Authorization": f"Bearer {key}"}) as response:
                if response.status_code != 200:
                    raise RuntimeError(f"status {response.status_code}: {response.text[:300]}")
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
            write(path(output_name), text + "\n")
            write(path(os.path.join("thinking", output_name)), "".join(thinking))
            with open(LOG_FILE, "a", encoding="utf-8") as log:
                log.write(json.dumps({"label": label, "output": output_name, "attempt": attempt,
                                      "seconds": round(time.time() - started), "usage": usage}) + "\n")
            print(f"[{label}] done in {round(time.time() - started)}s", flush=True)
            return text
        except Exception as problem:
            wait = min(60 * attempt, 300)
            print(f"[{label}] attempt {attempt} failed: {problem}; waiting {wait}s", flush=True)
            time.sleep(wait)
    raise RuntimeError(f"[{label}] gave up")


def rules():
    return f"""THE OWNER'S BRIEF AND RULES (obey them exactly):

{read(os.path.join(WORK, 'new', '00-brief-2.md'))}

THE OWNER'S SECOND FEEDBACK (overrides the brief where they differ):

{read(os.path.join(WORK, 'new', '05-owner-feedback-2.md'))}

NOTES ON THE OWNER'S OWN SCREENPLAY "THE CATCH" (nothing from it may be echoed):

{read(os.path.join(WORK, 'the-catch-notes.md'))}

THE MASTER SEASON PLAN, VERSION 3 (it wins over everything else; its numbers are exact; section 14 lists the words that must never reach the screen):

{read(os.path.join(WORK, 'new', '70-plan-v3.md'))}
"""


def final_name(number):
    return f"episode-{number:02d}-final.md"


def claude_final(number):
    return os.path.join(WORK, "new", f"82-episode-{number:02d}-final.md")


def finished_before(number):
    parts = []
    for earlier in range(1, number):
        source = claude_final(earlier) if earlier <= 3 else path(final_name(earlier))
        if os.path.exists(source):
            parts.append(read(source))
    return "\n\n".join(parts) or "(none)"


FORMAT = ("FORMAT: a scriptment. Start with '# Episode N: Title' and the one-line pitch. Then the cold open and the acts, "
          "each broken into numbered scenes headed 'Scene N. Place, time.' Action in present-tense prose; dialogue as "
          "NAME: line, with the lines that matter written in full. 6,000 to 8,000 words. End with a short section "
          "'Plants and payoffs' listing what this episode plants for later and pays off from earlier.")

CRITIQUE_TASK = ("Criticise it, most serious first, at most 15 findings, each with the scene, the problem, why it matters "
                 "and a concrete fix. Check: (1) fidelity to the plan's beats, numbers, knowledge map and twist plants for "
                 "this episode, nothing revealed early and no plant missing; (2) the physics and every law it uses, against "
                 "the plan's rules; (3) the owner's rules, above all no echo of The Catch and no banned word or named idea on "
                 "screen; (4) craft: does each scene do at least two jobs, do we care before the threat, does dialogue act "
                 "rather than explain, is anything preachy, does the episode end higher than it began; (5) continuity with "
                 "the finished earlier episodes.")


def draft(number):
    prompt = f"""{rules()}

THE FINISHED EARLIER EPISODES (keep their voice and continuity exactly):

{finished_before(number)}

YOUR TASK: write episode {number}, "{TITLES[number - 1]}", following the plan's episode {number} beat for beat (section 8), its law ledger rows for this episode (section 4), the knowledge map (section 10) and the twist schedule (section 9). {FORMAT}"""
    return ask_glm(f"ep{number:02d}-draft", prompt, f"episode-{number:02d}-draft.md")


def critique(number, draft_text):
    prompt = f"""{rules()}

THE FINISHED EARLIER EPISODES:

{finished_before(number)}

EPISODE {number} DRAFT (by another writer):

{draft_text}

YOUR TASK: you did not write this draft. {CRITIQUE_TASK}"""
    return ask_glm(f"ep{number:02d}-critique", prompt, f"episode-{number:02d}-critique.md")


def revise(number, draft_text, critique_text):
    prompt = f"""{rules()}

THE FINISHED EARLIER EPISODES:

{finished_before(number)}

EPISODE {number} DRAFT:

{draft_text}

A CRITIQUE OF THE DRAFT, BY ANOTHER WRITER:

{critique_text}

YOUR TASK: check each finding against the plan and the draft; reject any that are wrong or would make things worse. Write the complete revised episode (same format as the draft). Then, after a line containing only ===LOG===, write the revision log in plain everyday language for the owner, who reads revisions closely: a table with one row per finding (the finding in plain words; accepted, accepted in part or rejected; exactly what changed or why not), then any other change you made and why."""
    raw = ask_glm(f"ep{number:02d}-revise", prompt, f"episode-{number:02d}-revise-raw.md")
    episode, _, log = raw.partition("===LOG===")
    write(path(final_name(number)), episode.strip() + "\n")
    write(path(f"episode-{number:02d}-revision-log.md"), log.strip() + "\n")


def season_check():
    season = "\n\n".join(read(claude_final(n)) if n <= 3 else read(path(final_name(n))) for n in range(1, 11))
    prompt = f"""{rules()}

ALL TEN FINAL EPISODES, IN ORDER (episodes 1 to 3 by Claude's writers, 4 to 10 finished by GLM):

{season}

YOUR TASK: read them as one season. Find every continuity error between episodes (names, numbers, dates, who knows what when, objects, injuries, plants never paid off, payoffs never planted, a twist given away early, a character acting on knowledge they do not yet have), every breach of the plan's or the owner's rules, and anything that reads differently across episodes (voice, a character's manner; watch the seam between episodes 3 and 4, where the writers change). Write a table with one row per finding: episode and scene, the problem, must-fix or should-fix, and the smallest exact fix. Then, for each episode from 1 to 10, a heading "Episode N" and the rows that apply to it (or "Nothing")."""
    return ask_glm("season-check", prompt, "season-check.md")


def apply_fixes(number, check_text):
    source = claude_final(number) if number <= 3 else path(final_name(number))
    prompt = f"""{rules()}

THE WHOLE-SEASON CHECK:

{check_text}

EPISODE {number} AS IT STANDS:

{read(source)}

YOUR TASK: apply every must-fix and should-fix finding the check lists for episode {number}, and nothing else, with the smallest changes that do the job. Write the complete episode. Then, after a line containing only ===LOG===, one row per finding in plain words: accepted or rejected, and exactly what changed. If the check lists nothing for episode {number}, write only the line NO CHANGES."""
    raw = ask_glm(f"ep{number:02d}-season-fix", prompt, f"episode-{number:02d}-season-fix-raw.md")
    if raw.strip().startswith("NO CHANGES"):
        return
    episode, _, log = raw.partition("===LOG===")
    write(path(f"episode-{number:02d}-after-season-check.md"), episode.strip() + "\n")
    write(path(f"episode-{number:02d}-season-check-log.md"), log.strip() + "\n")


def main():
    os.makedirs(path("thinking"), exist_ok=True)
    claude_draft_4 = read(os.path.join(WORK, "new", "80-episode-04-draft.md"))
    claude_critique_4 = read(os.path.join(WORK, "new", "81-episode-04-critique.md"))
    claude_draft_5 = read(os.path.join(WORK, "new", "80-episode-05-draft.md"))
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        episode_4 = pool.submit(revise, 4, claude_draft_4, claude_critique_4)
        critique_5 = pool.submit(critique, 5, claude_draft_5)
        episode_4.result()
        critique_text_5 = critique_5.result()
    revise(5, claude_draft_5, critique_text_5)
    for number in range(6, 11):
        draft_text = draft(number)
        critique_text = critique(number, draft_text)
        revise(number, draft_text, critique_text)
    check_text = season_check()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        list(pool.map(lambda n: apply_fixes(n, check_text), range(1, 11)))
    print("=== finished ===", flush=True)


if __name__ == "__main__":
    main()
