#!/usr/bin/env python3
"""Refuse an edit to a frozen file before it happens.

Claude Code runs this by itself before every file edit (the Edit, Write,
MultiEdit and NotebookEdit tools; see .claude/settings.json). It reads the
file the tool is about to change and, if that file is on a frozen list
(.claude/skills/error-correction/frozen-files.txt), refuses the edit and
says why in plain words. It looks at two lists: the one in the repository
the edited file belongs to, and the one in the session's own project
folder, so an edit made from a scratch copy is still caught. Any other
edit goes ahead untouched.

It cannot see edits made by shell commands or by scripts; the fingerprint
check (check_frozen_files.py, run before every commit) catches those. If
this script itself goes wrong, it lets the edit through and prints a
notice, so that a fault here never stops ordinary work.
"""
import json
import os
import re
import subprocess
import sys

LIST_PATH = os.path.join(".claude", "skills", "error-correction", "frozen-files.txt")
LIST_LINE = re.compile(r"^([0-9a-f]{64})\s+(.+?)\s+added\s+\S.*$")


def frozen_paths(repository_root):
    """The frozen files listed in this repository, as real paths; empty if it has no list."""
    list_file = os.path.join(repository_root, LIST_PATH)
    if not os.path.exists(list_file):
        return set()
    paths = set()
    with open(list_file, encoding="utf-8") as frozen_list:
        for line in frozen_list:
            match = LIST_LINE.match(line.strip())
            if match:
                paths.add(os.path.realpath(os.path.join(repository_root, match.group(2))))
    return paths


def repository_of(folder):
    while folder and not os.path.isdir(folder):
        folder = os.path.dirname(folder)
    return subprocess.run(["git", "-C", folder or ".", "rev-parse", "--show-toplevel"],
                          capture_output=True, text=True, check=False).stdout.strip()


def main():
    try:
        hook_input = json.load(sys.stdin)
        working_folder = hook_input.get("cwd") or os.getcwd()
        tool_input = hook_input.get("tool_input") or {}
        target = tool_input.get("file_path") or tool_input.get("notebook_path")
        if not target:
            return 0
        if not os.path.isabs(target):
            target = os.path.join(working_folder, target)
        target = os.path.realpath(target)
        roots = {root for root in (repository_of(os.path.dirname(target)), os.environ.get("CLAUDE_PROJECT_DIR"),
                                   repository_of(working_folder)) if root}
        for repository_root in roots:
            if target in frozen_paths(repository_root):
                reason = (
                    f"{os.path.relpath(target, repository_root)} is a frozen file: the owner's own text, never"
                    " edited, not even a typo. A changed version is added as a new revision file through the"
                    " add-source skill (step 3). If you think the frozen text itself is wrong, record it as a"
                    " correction and ask the owner (error-correction skill,"
                    " references/owner-answers-and-revisions.md, section 4); do not edit it."
                )
                json.dump({"hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": reason,
                }}, sys.stdout)
                return 0
        return 0
    except Exception as problem:  # a fault here must never block ordinary work
        print(f"protect_frozen_files hook could not run ({problem}); the edit was not checked", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
