#!/usr/bin/env python3
"""Check that every skill's map is true and every pointer in a skill lands.

What it does, for each skill folder under .claude/skills/:
1. Every file under references/ must be named, by its exact file name, in
   the SKILL.md table under the heading "Where to look, and when", and in
   the mermaid diagram (between "```mermaid" and the closing "```"). A
   longer word that merely contains the name (for example "mythic" for
   myth.md) does not count, and a mention in some other table does not
   count.
2. Every file path written in backticks in any .md file of the skill must
   exist. A full path is looked up from the repository root. A short path
   is looked up in the skill's own folder, its references and scripts
   folders, the file's own folder and the one above it, and sources/. A
   path that starts with a skill's name ("add-source/scripts/...") is
   looked up in that skill. Otherwise a short path may point into another
   skill only if that skill's name stands just before it (within the 80
   characters before the path, as in "the plot skill's `references/...`"),
   so that a pointer into the wrong skill is not passed by accident.
3. Every pointer of the form "`file.md`, section 4" or "section 4 of
   `file.md`" must land on a heading "## 4." in that file.
4. The SKILL.md front matter description must be 1,024 characters or
   fewer, which is Claude Code's limit.
5. A passage marked as shared, between
   "<!-- shared: NAME; carried by: plot/SKILL.md, genre/SKILL.md -->" and
   "<!-- /shared -->", must be word for word the same in every skill file
   that carries it, and every file the marker names must carry it. An
   opening marker without a closing one, or the reverse, is reported. A
   rule stated in several skills and changed in only one is how the skills
   came to disagree before; deleting the marker in one file would hide
   that, so the other copies name every file that must carry it.
It prints each problem in plain words and a total. It exits with code 1 if
there is any problem and 0 if there is none, so a hook can use it as a gate.

Usage: check_maps.py [REPOSITORY_ROOT]   (default: the current folder)
"""
import os
import re
import sys

PATH_IN_BACKTICKS = re.compile(r"`([A-Za-z0-9_./-]+\.(?:md|py|txt|json))`")
SECTION_NUMBERS = r"sections? ((?:\d+)(?:(?:, | and |, and )\d+)*)\b"
POINTER_FILE_THEN_SECTION = re.compile(
    r"`([A-Za-z0-9_./-]+\.md)`,? " + SECTION_NUMBERS + r"(?! of)"
)
POINTER_SECTION_THEN_FILE = re.compile(
    SECTION_NUMBERS + r" of (?:its |the |this skill's |that skill's )?`([A-Za-z0-9_./-]+\.md)`"
)
DESCRIPTION_LIMIT = 1024
MAP_HEADING = "## Where to look, and when"


def read_text(path):
    with open(path, encoding="utf-8") as text_file:
        return text_file.read()


def mermaid_blocks(text):
    return "\n".join(re.findall(r"```mermaid\n(.*?)```", text, flags=re.S))


def map_table(text):
    """The table lines under the "Where to look, and when" heading only."""
    start = text.find(MAP_HEADING)
    if start < 0:
        return ""
    rest = text[start + len(MAP_HEADING):]
    next_heading = re.search(r"^## ", rest, flags=re.M)
    section = rest[: next_heading.start()] if next_heading else rest
    return "\n".join(line for line in section.splitlines() if line.startswith("|"))


def names_exactly(text, file_name):
    """True if file_name appears in text as a whole name, not inside a longer word."""
    pattern = r"(?<![A-Za-z0-9_-])" + re.escape(file_name) + r"(?![A-Za-z0-9_-])"
    return re.search(pattern, text) is not None


def description_of(skill_text):
    match = re.match(r"---\n(.*?)\n---", skill_text, flags=re.S)
    if not match:
        return None
    description = re.search(r"^description:\s*(.*)$", match.group(1), flags=re.M)
    return description.group(1).strip().strip('"') if description else None


NEAR = 80  # characters before a path in which another skill's name must stand


def resolve(mentioned_path, line, repository_root, skill_folder, file_folder, skill_names, position=None):
    """Return the path a reader would reach, or None if it lands nowhere.

    position is where the path starts in the line; the text just before it
    is where another skill's name must stand."""
    if mentioned_path.startswith((".claude/", "sources/", "foundations/")):
        candidate = os.path.join(repository_root, mentioned_path)
        return candidate if os.path.exists(candidate) else None
    skills_folder = os.path.join(repository_root, ".claude", "skills")
    first_part = mentioned_path.split("/", 1)[0]
    if "/" in mentioned_path and first_part in skill_names:
        candidate = os.path.join(skills_folder, mentioned_path)
        return candidate if os.path.exists(candidate) else None
    local_candidates = [
        os.path.join(repository_root, mentioned_path),
        os.path.join(skill_folder, mentioned_path),
        os.path.join(skill_folder, "references", mentioned_path),
        os.path.join(skill_folder, "scripts", mentioned_path),
        os.path.join(file_folder, mentioned_path),
        os.path.join(os.path.dirname(file_folder), mentioned_path),
        os.path.join(repository_root, "sources", mentioned_path),
    ]
    for candidate in local_candidates:
        if os.path.exists(candidate):
            return candidate
    just_before = line[max(0, position - NEAR):position] if position is not None else line
    for other_skill in skill_names:
        if not names_exactly(just_before, other_skill):
            continue
        for candidate in (
            os.path.join(skills_folder, other_skill, mentioned_path),
            os.path.join(skills_folder, other_skill, "references", mentioned_path),
        ):
            if os.path.exists(candidate):
                return candidate
    return None


def numbered_headings(path):
    return set(re.findall(r"^## (\d+)\.", read_text(path), flags=re.M))


def section_list(numbers_text):
    return re.findall(r"\d+", numbers_text)


def check_skill(skill_folder, repository_root, skill_names, problems):
    skill_name = os.path.basename(skill_folder)
    skill_file = os.path.join(skill_folder, "SKILL.md")
    if not os.path.exists(skill_file):
        problems.append(f"{skill_name}: has no SKILL.md")
        return
    skill_text = read_text(skill_file)
    table_text = map_table(skill_text)
    diagram_text = mermaid_blocks(skill_text)

    description = description_of(skill_text)
    if description is None:
        problems.append(f"{skill_name}: SKILL.md has no description in its front matter")
    elif len(description) > DESCRIPTION_LIMIT:
        problems.append(f"{skill_name}: description is {len(description)} characters (limit {DESCRIPTION_LIMIT})")

    if not table_text:
        problems.append(f"{skill_name}: SKILL.md has no table under '{MAP_HEADING}'")

    references_folder = os.path.join(skill_folder, "references")
    for folder, _, file_names in os.walk(references_folder):
        for file_name in sorted(file_names):
            if not file_name.endswith(".md"):
                continue
            relative_path = os.path.relpath(os.path.join(folder, file_name), skill_folder)
            if not names_exactly(table_text, file_name):
                problems.append(f"{skill_name}: {relative_path} has no row in the '{MAP_HEADING}' table")
            if not names_exactly(diagram_text, file_name):
                problems.append(f"{skill_name}: {relative_path} has no node in the map diagram")

    for folder, _, file_names in os.walk(skill_folder):
        for file_name in sorted(file_names):
            if not file_name.endswith(".md"):
                continue
            file_path = os.path.join(folder, file_name)
            shown_file = os.path.relpath(file_path, repository_root)
            for line_number, line in enumerate(read_text(file_path).splitlines(), start=1):
                for path_match in PATH_IN_BACKTICKS.finditer(line):
                    mentioned_path = path_match.group(1)
                    if "<" in mentioned_path or "*" in mentioned_path:
                        continue
                    if resolve(mentioned_path, line, repository_root, skill_folder, folder, skill_names,
                               path_match.start()) is None:
                        problems.append(
                            f"{shown_file}:{line_number}: mentions `{mentioned_path}`, which does not exist here"
                            " (a pointer into another skill must name that skill just before the path)"
                        )
                pointers = [(match.group(1), match.group(2), match.start(1) - 1)
                            for match in POINTER_FILE_THEN_SECTION.finditer(line)]
                pointers += [(match.group(2), match.group(1), match.start(2) - 1)
                             for match in POINTER_SECTION_THEN_FILE.finditer(line)]
                for pointed_file, numbers_text, position in pointers:
                    target = resolve(pointed_file, line, repository_root, skill_folder, folder, skill_names, position)
                    if target is None:
                        continue  # already reported as a missing path
                    headings = numbered_headings(target)
                    for number in section_list(numbers_text):
                        if number not in headings:
                            problems.append(
                                f"{shown_file}:{line_number}: points to section {number} of `{pointed_file}`,"
                                " which has no heading with that number"
                            )


SHARED_OPENING = re.compile(r"<!-- shared: ([\w-]+)(?:; carried by: ([^>]*?))? -->")
SHARED_CLOSING = "<!-- /shared -->"


def check_shared_passages(repository_root, problems):
    skills_folder = os.path.join(repository_root, ".claude", "skills")
    passages, carriers = {}, {}
    for folder, _, file_names in os.walk(skills_folder):
        for file_name in sorted(file_names):
            if not file_name.endswith(".md"):
                continue
            file_path = os.path.join(folder, file_name)
            shown_file = os.path.relpath(file_path, repository_root)
            file_text = read_text(file_path)
            openings = list(SHARED_OPENING.finditer(file_text))
            closings = file_text.count(SHARED_CLOSING)
            if len(openings) != closings:
                problems.append(f"{shown_file}: {len(openings)} opening shared-passage marker(s) but {closings}"
                                " closing one(s); each shared passage needs both")
            for opening in openings:
                end = file_text.find(SHARED_CLOSING, opening.end())
                if end < 0:
                    continue
                name = opening.group(1)
                body = file_text[opening.end():end].strip("\n")
                passages.setdefault(name, []).append((shown_file, body))
                named = tuple(sorted(part.strip() for part in (opening.group(2) or "").split(",") if part.strip()))
                carriers.setdefault(name, []).append((shown_file, named))
    for name, copies in sorted(passages.items()):
        first_file, first_body = copies[0]
        for other_file, other_body in copies[1:]:
            if other_body != first_body:
                problems.append(f"{other_file}: the shared passage '{name}' differs from the one in {first_file};"
                                " change every copy together")
        lists = {named for _, named in carriers[name]}
        if len(lists) > 1:
            problems.append(f"the shared passage '{name}': its markers name different files that carry it;"
                            " make every marker's list the same")
        carrying = {os.path.relpath(shown_file, os.path.join(".claude", "skills")) for shown_file, _ in copies}
        for named in lists:
            if not named:
                problems.append(f"the shared passage '{name}': its marker does not say which files carry it"
                                " ('; carried by: plot/SKILL.md, ...')")
            for expected in named:
                if expected not in carrying:
                    problems.append(f".claude/skills/{expected}: should carry the shared passage '{name}'"
                                    " (its other copies say so) but does not")


def main():
    repository_root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
    skills_folder = os.path.join(repository_root, ".claude", "skills")
    skill_names = sorted(
        name for name in os.listdir(skills_folder) if os.path.isdir(os.path.join(skills_folder, name))
    )
    problems = []
    for skill_name in skill_names:
        check_skill(os.path.join(skills_folder, skill_name), repository_root, skill_names, problems)
    check_shared_passages(repository_root, problems)
    for problem in problems:
        print(problem)
    print(f"TOTAL problems: {len(problems)}")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
