#!/usr/bin/env python3
"""Jobs for MiMo v2.6 Pro (Xiaomi), with deep thinking, on the two stories.

What it does:
  critique  - MiMo reads a whole book or season with fresh eyes and writes findings,
              each marked SUBSTANTIVE (a real problem) or QUIBBLE (better left to an
              audience test). Used as a fourth critic, beside three Claude or GLM critics.
  audience  - five simulated readers or viewers, each with a different taste, read the
              finished story at once and report how it played for them; MiMo then
              writes the audience analysis that settles the quibbles critics leave.

Usage:
  python3 mimo_tasks.py critique TEXT_LIST_FILE CONCEPT_FILE OUTPUT_FILE
      TEXT_LIST_FILE lists, one per line, the files that make up the story, in order.
  python3 mimo_tasks.py audience TEXT_LIST_FILE CONCEPT_FILE OUTPUT_FOLDER KIND
      KIND is "novella" or "tv season".

The API key is read from a private file outside the repository.
"""
import concurrent.futures
import json
import os
import sys
import time

import requests

HERE = os.path.dirname(os.path.abspath(__file__))
KEY_FILE = os.path.join(os.path.dirname(HERE), ".mimo_key")
ENDPOINT = "https://token-plan-sgp.xiaomimimo.com/v1/chat/completions"
MODEL = "mimo-v2.6-pro"
LOG_FILE = os.path.join(HERE, "calls-log.jsonl")

SEVERITY = """HOW TO MARK EACH FINDING:
SUBSTANTIVE means a careful reader or viewer would notice it and it weakens the story: a plot hole or broken logic; a contradiction between parts; a breach of the owner's rules in the concept; a character acting without cause or against who they are; a scene or passage with no job; pacing that sags; confusion that does not serve the story; a theme stated instead of shown; a thread that goes nowhere.
QUIBBLE means it could go either way, or only an audience test could settle it: word choice or placement, sentence rhythm, the exact minute or day of an event when nothing depends on it, small matters of taste."""

PANEL = [
    ("Ana, 34, nurse, reads literary fiction on night shifts",
     "loves character and feeling, impatient with puzzles for their own sake"),
    ("Tom, 52, engineer, watches every crime and science fiction series",
     "checks the logic of every rule, notices every inconsistency, hates cheats"),
    ("Priya, 23, film student",
     "watches for structure, twists and what each scene is doing; bored by repetition"),
    ("Joe, 67, retired bus driver, reads a thriller a week",
     "wants to know what happens next; gets lost when a story is too clever"),
    ("Lena, 41, philosophy teacher and churchgoer",
     "cares most about what the story says about belief, meaning and consequence"),
]


def read(file_path):
    with open(file_path, encoding="utf-8") as handle:
        return handle.read()


def write(file_path, text):
    os.makedirs(os.path.dirname(os.path.abspath(file_path)), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as handle:
        handle.write(text)


def ask_mimo(label, prompt, output_file):
    """Send one prompt to MiMo with deep thinking and streaming; save the answer and thinking; return it."""
    if os.path.exists(output_file):
        return read(output_file)
    key = read(KEY_FILE).strip()
    body = {"model": MODEL, "messages": [{"role": "user", "content": prompt}],
            "thinking": {"type": "enabled"}, "max_tokens": 128000, "stream": True}
    for attempt in range(1, 9):
        started = time.time()
        answer, thinking, usage = [], [], {}
        try:
            with requests.post(ENDPOINT, json=body, stream=True, timeout=(30, 900),
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
            write(output_file, text + "\n")
            write(output_file + ".thinking.txt", "".join(thinking))
            with open(LOG_FILE, "a", encoding="utf-8") as log:
                log.write(json.dumps({"label": label, "output": output_file, "attempt": attempt,
                                      "seconds": round(time.time() - started), "usage": usage}) + "\n")
            print(f"[{label}] done in {round(time.time() - started)}s", flush=True)
            return text
        except Exception as problem:
            wait = min(30 * attempt, 180)
            print(f"[{label}] attempt {attempt} failed: {problem}; waiting {wait}s", flush=True)
            time.sleep(wait)
    raise RuntimeError(f"[{label}] gave up")


def story_text(list_file):
    return "\n\n".join(read(line.strip()) for line in read(list_file).splitlines() if line.strip())


def critique(list_file, concept_file, output_file):
    prompt = f"""THE OWNER'S CONCEPT AND RULES:

{read(concept_file)}

THE STORY AS IT STANDS:

{story_text(list_file)}

YOUR TASK: you did not write this story, and you come to it fresh, as a different model from the ones that wrote and criticised it. Criticise it as a whole: story logic and the owner's rules, the people and what we feel for them, continuity and prose.
{SEVERITY}
Write a numbered list of findings, most serious first, at most 20. For each: where (chapter or episode and scene), the problem, why it matters, a concrete fix, and the mark SUBSTANTIVE or QUIBBLE. Only real findings. Markdown, no preamble."""
    ask_mimo("critique", prompt, output_file)


def audience(list_file, concept_file, output_folder, kind):
    story = story_text(list_file)

    def panellist(person):
        who, taste = person
        name = who.split(",")[0].lower()
        prompt = f"""You are {who}. Your taste: {taste}. You have just finished this {kind}.

{story}

YOUR TASK: report honestly, in your own voice, how it played for you, as a member of an audience research panel would. Say:
1. Where you were gripped, and where your attention drifted (be specific: chapter or episode and moment).
2. What confused you, and whether that confusion felt deliberate and rewarding or just unclear.
3. What you guessed before the story told you, and when.
4. Which characters you cared about, which you did not, and why.
5. Which lines or moments you will remember, and any wording or timing that jarred.
6. What you think it was about, in a sentence or two.
7. A score out of 10, and whether you would recommend it and to whom.
Markdown, no preamble."""
        return name, ask_mimo(f"audience-{name}", prompt, os.path.join(output_folder, f"panel-{name}.md"))

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        reports = list(pool.map(panellist, PANEL))
    joined = "\n\n".join(f"=== {name.upper()} ===\n{text}" for name, text in reports)
    summary_prompt = f"""THE OWNER'S CONCEPT:

{read(concept_file)}

FIVE AUDIENCE PANEL REPORTS ON THE FINISHED {kind.upper()}:

{joined}

YOUR TASK: write the audience analysis for the owner, who is not a writer, in plain everyday language. Cover: where the panel agreed and disagreed; the moments that worked for nearly everyone; where attention drifted; what was guessed early; which confusions paid off and which did not; which small wording and timing points (the quibbles critics leave to an audience) actually bothered readers, and which nobody noticed; the scores; and the three changes the panel's reactions most support, if any. Markdown, no preamble."""
    ask_mimo("audience-summary", summary_prompt, os.path.join(output_folder, "audience-analysis.md"))


if __name__ == "__main__":
    job = sys.argv[1]
    if job == "critique":
        critique(*sys.argv[2:5])
    elif job == "audience":
        audience(*sys.argv[2:6])
    else:
        raise SystemExit(__doc__)
