#!/usr/bin/env python3
"""Check that every skill's map is true and every file path it mentions exists.

What it does, for each skill folder under .claude/skills/:
1. Every file under references/ must be named in the SKILL.md map table
   (a line starting with "|") and in the mermaid diagram (between
   "```mermaid" and the closing "```").
2. Every file path written in backticks in any .md file of any skill,
   and every path the map table points to, must exist. Paths are tried
   relative to the repository root and to the skill's own folder.
3. The SKILL.md front matter description must be 1,024 characters or
   fewer, which is Claude Code's limit.
It prints each problem and a total; zero problems is the rule.

Usage: check_maps.py [REPOSITORY_ROOT]   (default: the current folder)
"""
import os
import re
import sys

PATH_IN_BACKTICKS = re.compile(r"`([A-Za-z0-9_./-]+\.(?:md|py|txt|json))`")
DESCRIPTION_LIMIT = 1024


def read_text(path):
    with open(path, encoding="utf-8") as text_file:
        return text_file.read()


def mermaid_blocks(text):
    return "\n".join(re.findall(r"```mermaid\n(.*?)```", text, flags=re.S))


def map_table_lines(text):
    return "\n".join(line for line in text.splitlines() if line.startswith("|"))


def description_of(skill_text):
    match = re.match(r"---\n(.*?)\n---", skill_text, flags=re.S)
    if not match:
        return None
    description = re.search(r"^description:\s*(.*)$", match.group(1), flags=re.M)
    return description.group(1).strip().strip('"') if description else None


def path_exists(mentioned_path, repository_root, skill_folder, file_folder):
    """True if the path resolves from any place a reader would look from.

    A full path is tried from the repository root. A short path is also
    tried from the skill's folder, its references folder, the file's own
    folder and the folder above it, from sources/, and from every other
    skill's folder, because the skills write "hard-to-vary's
    references/by-domain.md" and similar.
    """
    skills_folder = os.path.join(repository_root, ".claude", "skills")
    candidates = [
        os.path.join(repository_root, mentioned_path),
        os.path.join(skill_folder, mentioned_path),
        os.path.join(skill_folder, "references", mentioned_path),
        os.path.join(file_folder, mentioned_path),
        os.path.join(os.path.dirname(file_folder), mentioned_path),
        os.path.join(repository_root, "sources", mentioned_path),
    ]
    if not mentioned_path.startswith((".claude", "sources", "foundations")):
        for other_skill in os.listdir(skills_folder):
            candidates.append(os.path.join(skills_folder, other_skill, mentioned_path))
            candidates.append(os.path.join(skills_folder, other_skill, "references", mentioned_path))
    return any(os.path.exists(candidate) for candidate in candidates)


def check_skill(skill_folder, repository_root, problems):
    skill_name = os.path.basename(skill_folder)
    skill_file = os.path.join(skill_folder, "SKILL.md")
    if not os.path.exists(skill_file):
        problems.append(f"{skill_name}: no SKILL.md")
        return
    skill_text = read_text(skill_file)
    table_text = map_table_lines(skill_text)
    diagram_text = mermaid_blocks(skill_text)

    description = description_of(skill_text)
    if description is None:
        problems.append(f"{skill_name}: SKILL.md has no description in its front matter")
    elif len(description) > DESCRIPTION_LIMIT:
        problems.append(f"{skill_name}: description is {len(description)} characters (limit {DESCRIPTION_LIMIT})")

    references_folder = os.path.join(skill_folder, "references")
    for folder, _, file_names in os.walk(references_folder):
        for file_name in sorted(file_names):
            if not file_name.endswith(".md"):
                continue
            relative_path = os.path.relpath(os.path.join(folder, file_name), skill_folder)
            if file_name not in table_text:
                problems.append(f"{skill_name}: {relative_path} has no row in the map table")
            if file_name not in diagram_text and file_name.replace(".md", "") not in diagram_text:
                problems.append(f"{skill_name}: {relative_path} has no node in the map diagram")

    for folder, _, file_names in os.walk(skill_folder):
        for file_name in file_names:
            if not file_name.endswith(".md"):
                continue
            file_path = os.path.join(folder, file_name)
            for mentioned_path in PATH_IN_BACKTICKS.findall(read_text(file_path)):
                if "<" in mentioned_path or "*" in mentioned_path:
                    continue
                if not path_exists(mentioned_path, repository_root, skill_folder, folder):
                    shown_file = os.path.relpath(file_path, repository_root)
                    problems.append(f"{shown_file}: mentions `{mentioned_path}`, which does not exist")


def main():
    repository_root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
    skills_folder = os.path.join(repository_root, ".claude", "skills")
    problems = []
    for skill_name in sorted(os.listdir(skills_folder)):
        skill_folder = os.path.join(skills_folder, skill_name)
        if os.path.isdir(skill_folder):
            check_skill(skill_folder, repository_root, problems)
    for problem in problems:
        print(problem)
    print(f"TOTAL problems: {len(problems)}")


if __name__ == "__main__":
    main()
