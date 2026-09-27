#!/usr/bin/env python3
"""Run GLM 5.3, at its deepest thinking, through a story in stages.

What it does: each stage is one job. It reads the files that earlier stages
wrote, asks GLM to do its job, and writes its own files into this folder.
Several GLM calls run at once where a stage has independent parts. Every
call's answer, its thinking and its token counts are saved, so nothing
is lost and every revision can be traced.

Usage: python3 glm_story_pipeline.py STAGE
Stages, in order: designs, judge, design-critiques, design-revision,
chapters, draft-critiques, revision-plan, revise-chapters, final-check.

The API key is read from the file named in KEY_FILE and is never written
into any output.
"""
import concurrent.futures
import json
import os
import re
import sys
import time

import requests

FOLDER = os.path.dirname(os.path.abspath(__file__))
KEY_FILE = os.path.join(os.path.dirname(FOLDER), ".glm_key")
ENDPOINT = "https://api.z.ai/api/coding/paas/v4/chat/completions"
MODEL = "glm-5.3"
MAX_OUTPUT_TOKENS = 128000
AT_ONCE = 3
LOG_FILE = os.path.join(FOLDER, "calls-log.jsonl")

SYSTEM_PROMPT = (
    "You are a novelist of great range and daring, working on one stage of a story. "
    "Write in English. Follow the task exactly, and write only what the task asks for, "
    "in Markdown, with no preamble and no closing remarks."
)


def read(name):
    with open(os.path.join(FOLDER, name), encoding="utf-8") as handle:
        return handle.read()


def write(name, text):
    with open(os.path.join(FOLDER, name), "w", encoding="utf-8") as handle:
        handle.write(text)


def exists(name):
    return os.path.exists(os.path.join(FOLDER, name))


def ask_glm(label, prompt, output_name):
    """Send one prompt to GLM with streaming, save the answer and its thinking, and return the answer."""
    if exists(output_name):
        print(f"[{label}] already done: {output_name}", flush=True)
        return read(output_name)
    key = open(KEY_FILE).read().strip()
    body = {
        "model": MODEL,
        "messages": [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": prompt}],
        "thinking": {"type": "enabled"},
        "reasoning_effort": "max",
        "max_tokens": MAX_OUTPUT_TOKENS,
        "stream": True,
    }
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
            write(output_name, text + "\n")
            write(os.path.join("thinking", output_name), "".join(thinking))
            record = {"label": label, "output": output_name, "attempt": attempt,
                      "seconds": round(time.time() - started), "usage": usage}
            with open(LOG_FILE, "a", encoding="utf-8") as log:
                log.write(json.dumps(record) + "\n")
            print(f"[{label}] done in {record['seconds']}s, usage {usage}", flush=True)
            return text
        except Exception as problem:  # network cut, rate limit, server error
            wait = min(60 * attempt, 300)
            print(f"[{label}] attempt {attempt} failed: {problem}; waiting {wait}s", flush=True)
            time.sleep(wait)
    raise RuntimeError(f"[{label}] gave up after 6 attempts")


def run_at_once(jobs):
    """Run several (label, prompt, output_name) jobs at once, at most AT_ONCE at a time."""
    with concurrent.futures.ThreadPoolExecutor(max_workers=AT_ONCE) as pool:
        futures = [pool.submit(ask_glm, *job) for job in jobs]
        return [future.result() for future in futures]


CONCEPT = lambda: read("00-concept.md")


def stage_designs():
    prompt = f"""{CONCEPT()}

YOUR TASK: design this story completely, as the blueprint a writer will follow chapter by chapter. It is a novella of about 35,000 to 45,000 words in 12 to 16 chapters. The blueprint must contain:
1. Title, and a one-paragraph premise that does NOT reveal the time travel.
2. Point of view and narrative form, and how the form itself will produce the reader's "mind bending dissociation".
3. The places: which ancient sites, where, how old, what happens in them, and the physical texture of each.
4. The characters: who they are, what each believes about the places (fumes, parallel reality, wormhole, the dead, or none), what each wants, what each loses.
5. The four explanations (toxic fumes, parallel reality, wormhole, contact with the dead): for each, the evidence planted for it, where, how close it comes to being "established as canon", and what keeps it from being confirmed. Contact with the dead must be leaned into without ever being said outright.
6. The encounter with humans from the astronomically distant future: what the characters experience, what they make of it, and why no reader can ever be confident what happened.
7. The final reveal: exactly how time travel is confirmed at the very end, and how it retroactively ties every earlier mystery together. List every earlier clue and what it turns out to have been.
8. The theme of impact and consequence: which actions ripple, and how.
9. The sharp, concise questions the story asks about belief, spirituality and society, and whether science can replace belief: where each is asked, by whom or by what event.
10. A chapter-by-chapter outline: for each chapter, what happens, whose point of view, which clues are planted, which explanation it tilts toward, and what the reader should feel.
11. A clue ledger: a table of every clue, the chapter it appears in, the explanations it seems to support, and what it really is.
12. The rules the writer must never break (above all: nothing confirms time travel before the final reveal; nothing ever confirms the other explanations).
13. The villain: who they are, what they want, how they act through others without being seen to act, what makes them remarkably resourceful and a formidable threat while staying passive and quiet, how the reader slowly learns to fear them, how they relate to the places and the time travel, and what the reader never learns about them."""
    run_at_once([(f"design-{letter}", prompt, f"10-design-{letter}.md") for letter in "ABC"])


def stage_judge():
    designs = "\n\n".join(f"=== DESIGN {letter} ===\n{read(f'10-design-{letter}.md')}" for letter in "ABC")
    prompt = f"""{CONCEPT()}

Three writers each designed this story independently. Their blueprints follow.

{designs}

YOUR TASK, in two parts, written as one Markdown document:
PART 1, JUDGEMENT: judge the three designs honestly against the concept: which best keeps the time travel hidden until the very end while making it tie everything together; which best leans into the dead without saying it; which keeps all four explanations nearly canon but unconfirmed; which handles the distant-future encounter best; which asks the sharpest questions about belief and science; which best produces dissociation; which has the villain of the quality the owner asked for (quiet, passive, resourceful, formidable); which is most original. Choose one as the base and name exactly which ideas from the others you graft in, and which you reject and why.
PART 2, THE BLUEPRINT: write the complete merged blueprint, with every one of the thirteen sections the designers were given (title and premise; point of view and form; the places; the characters; the four explanations with their evidence; the distant-future encounter; the final reveal with every earlier clue explained; impact and consequence; the questions about belief; the chapter-by-chapter outline; the clue ledger; the rules never to break; the villain). Make it complete and exact: a writer will follow it chapter by chapter."""
    ask_glm("judge", prompt, "20-judgement-and-blueprint-v1.md")


CRITIC_LENSES = {
    "mystery": "THE MYSTERY'S DISCIPLINE: does anything confirm time travel before the final reveal, or confirm any other explanation at all? Is each explanation (fumes, parallel reality, wormhole, the dead) hinted strongly enough to feel almost canon? Does the final reveal truly tie every clue together, with none left dangling or contradicted? Is the distant-future encounter kept so uncertain that no reader can be confident? Check the clue ledger clue by clue.",
    "questions": "THE QUESTIONS AND THE THEME: are the questions about belief, spirituality, society and whether science can replace belief sharp and concise, asked through events and people rather than lectures? Does the story avoid answering them too neatly? Is impact and consequence felt in what happens, not stated? Where is it preachy, where is it thin?",
    "craft": "CRAFT AND DISSOCIATION: will a reader care about these people before the strangeness bites; does each chapter end higher than it began; where would a reader be bored, confused in the wrong way, or ahead of the story; does the form really produce mind-bending dissociation, and where could it go further; what is derivative of well-known books or films, and how could it be made its own? And THE VILLAIN: is the villain of the quality the owner asked for (the quality of Johan Liebert in Monster: passive, quiet, never show-stopping, yet remarkably resourceful and a formidable threat), and is the villain this story's own creation rather than a copy of Johan?",
}


def stage_design_critiques():
    blueprint = read("20-judgement-and-blueprint-v1.md")
    jobs = []
    for name, lens in CRITIC_LENSES.items():
        prompt = f"""{CONCEPT()}

Below is the blueprint for this story (with the judgement that produced it). You did not write it.

{blueprint}

YOUR TASK: criticise the blueprint through one lens only. {lens}
Write a numbered list of findings, most serious first. For each: where, the problem, why it matters, and a concrete fix. At most 15 findings, only real ones."""
        jobs.append((f"design-critique-{name}", prompt, f"30-design-critique-{name}.md"))
    run_at_once(jobs)


def stage_design_revision():
    critiques = "\n\n".join(f"=== CRITIQUE: {name} ===\n{read(f'30-design-critique-{name}.md')}" for name in CRITIC_LENSES)
    prompt = f"""{CONCEPT()}

The blueprint (version 1):

{read('20-judgement-and-blueprint-v1.md')}

Three critiques of it:

{critiques}

YOUR TASK: produce two documents, separated by a line containing only ===SPLIT===.
DOCUMENT 1, THE REVISION LOG: one table per critique, with one row per finding: the finding in a few words; accepted, accepted in part, or rejected; and exactly what changed, or why it was rejected. Then a short section "Changes made to keep it coherent" and a section "Still unresolved". Write it plainly: the owner reads it closely and cares most about the revisions.
DOCUMENT 2, THE BLUEPRINT (version 2): the complete revised blueprint with all thirteen sections, standing on its own (not a list of changes)."""
    text = ask_glm("design-revision", prompt, "40-design-revision-raw.md")
    if "===SPLIT===" not in text:
        raise SystemExit("design revision: the split line is missing; read 40-design-revision-raw.md")
    log, blueprint = text.split("===SPLIT===", 1)
    write("41-design-revision-log.md", log.strip() + "\n")
    write("42-blueprint-v2.md", blueprint.strip() + "\n")


def chapter_count(blueprint):
    numbers = [int(n) for n in re.findall(r"(?im)^\W*chapter\s+(\d+)", blueprint)]
    return max(numbers) if numbers else 14


def stage_chapters():
    blueprint = read("42-blueprint-v2.md")
    total = int(os.environ.get("CHAPTERS", chapter_count(blueprint)))
    for number in range(1, total + 1):
        name = f"50-chapter-{number:02d}-draft.md"
        so_far = "\n\n".join(read(f"50-chapter-{n:02d}-draft.md") for n in range(1, number))
        prompt = f"""{CONCEPT()}

THE BLUEPRINT (follow it; it wins over your own ideas unless it plainly breaks the concept):

{blueprint}

THE STORY SO FAR:

{so_far or '(nothing yet: this is the first chapter)'}

YOUR TASK: write Chapter {number} of {total} in full, as finished prose, following the blueprint's outline for this chapter, its clue ledger and its rules. Match the voice and continuity of the story so far exactly. Start with the chapter heading. Aim for about {int(os.environ.get('WORDS_PER_CHAPTER', 3000))} words. Write only this chapter."""
        ask_glm(f"chapter-{number:02d}", prompt, name)


def full_draft(kind):
    names = sorted(n for n in os.listdir(FOLDER) if re.fullmatch(rf"\d\d-chapter-\d\d-{kind}\.md", n))
    return "\n\n".join(read(n) for n in names), len(names)


DRAFT_LENSES = {
    "mystery": CRITIC_LENSES["mystery"],
    "questions": CRITIC_LENSES["questions"],
    "prose": "PROSE, CHARACTER AND CONTINUITY: continuity errors between chapters; flat or repetitive sentences; dialogue that explains instead of acts; characters who change without cause; chapters that sag; places where the dissociation becomes mere confusion; any line that states a theme outright; and whether the villain stays quiet, passive and formidable on the page, frightening through what others do and find, never through speeches or displays.",
}


def stage_draft_critiques():
    draft, _ = full_draft("draft")
    jobs = []
    for name, lens in DRAFT_LENSES.items():
        prompt = f"""{CONCEPT()}

THE BLUEPRINT:

{read('42-blueprint-v2.md')}

THE COMPLETE FIRST DRAFT:

{draft}

YOUR TASK: criticise the draft through one lens only. {lens}
Write a numbered list of findings, most serious first. For each: the chapter and passage, the problem, why it matters, and a concrete fix. At most 20 findings, only real ones."""
        jobs.append((f"draft-critique-{name}", prompt, f"60-draft-critique-{name}.md"))
    run_at_once(jobs)


def stage_revision_plan():
    draft, count = full_draft("draft")
    critiques = "\n\n".join(f"=== CRITIQUE: {name} ===\n{read(f'60-draft-critique-{name}.md')}" for name in DRAFT_LENSES)
    prompt = f"""{CONCEPT()}

THE BLUEPRINT:

{read('42-blueprint-v2.md')}

THE COMPLETE FIRST DRAFT ({count} chapters):

{draft}

THREE CRITIQUES OF THE DRAFT:

{critiques}

YOUR TASK: write the revision plan and log, as one Markdown document with two parts.
PART 1, THE LOG: one table per critique, one row per finding: the finding in a few words; accepted, accepted in part, or rejected; and what will change, in which chapter, or why it is rejected. Write it plainly: the owner cares most about the revisions.
PART 2, THE PLAN BY CHAPTER: for every chapter from 1 to {count}, a heading "Chapter N" and a numbered list of exact changes to make in that chapter (or "No changes"), specific enough that a reviser who sees only the whole draft and this plan can make them."""
    ask_glm("revision-plan", prompt, "70-revision-plan-and-log.md")


def stage_revise_chapters():
    draft, count = full_draft("draft")
    plan = read("70-revision-plan-and-log.md")
    jobs = []
    for number in range(1, count + 1):
        prompt = f"""{CONCEPT()}

THE BLUEPRINT:

{read('42-blueprint-v2.md')}

THE COMPLETE FIRST DRAFT:

{draft}

THE REVISION PLAN:

{plan}

YOUR TASK: write the revised Chapter {number} in full, making every change the plan lists for Chapter {number} and nothing that would break the other chapters. Keep everything that works. Then, after a line containing only ===NOTES===, list in plain words each change you made and any planned change you could not make, and why."""
        jobs.append((f"revise-{number:02d}", prompt, f"80-chapter-{number:02d}-revised-raw.md"))
    run_at_once(jobs)
    for number in range(1, count + 1):
        raw = read(f"80-chapter-{number:02d}-revised-raw.md")
        chapter, _, notes = raw.partition("===NOTES===")
        write(f"80-chapter-{number:02d}-revised.md", chapter.strip() + "\n")
        write(f"81-chapter-{number:02d}-change-notes.md", notes.strip() + "\n")


def stage_final_check():
    story, _ = full_draft("revised")
    prompt = f"""{CONCEPT()}

THE FINISHED STORY:

{story}

YOUR TASK: be the last reader before publication, checking only the concept's hard rules. Answer each with evidence (chapter and quoted phrase):
1. Is time travel the very last plot point revealed? Is anything before the ending enough to confirm it?
2. Are toxic fumes, parallel reality, wormholes and contact with the dead each hinted and nearly canon, yet never confirmed? Is contact with the dead ever said outright?
3. Does the ending confirm time travel and tie every earlier mystery together? List any mystery left untied.
4. Is the distant-future encounter present, and is there never enough evidence to be confident what happened?
5. Are the questions about belief, spirituality and science asked sharply and concisely?
6. Is impact and consequence the theme, shown rather than stated?
7. Is the main villain passive, quiet and never show-stopping, yet remarkably resourceful and a formidable threat, and the story's own creation rather than a copy of Johan Liebert?
End with PASS or FAIL for each rule, and for each FAIL the smallest exact fix."""
    ask_glm("final-check", prompt, "90-final-check.md")


STAGES = {
    "designs": stage_designs, "judge": stage_judge, "design-critiques": stage_design_critiques,
    "design-revision": stage_design_revision, "chapters": stage_chapters,
    "draft-critiques": stage_draft_critiques, "revision-plan": stage_revision_plan,
    "revise-chapters": stage_revise_chapters, "final-check": stage_final_check,
}

if __name__ == "__main__":
    os.makedirs(os.path.join(FOLDER, "thinking"), exist_ok=True)
    for stage in sys.argv[1:]:
        print(f"=== stage {stage} ===", flush=True)
        STAGES[stage]()
    print("=== finished ===", flush=True)
