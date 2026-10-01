#!/usr/bin/env python3
"""After a commit, remind the agent of the check before any claim reaches the owner.

Claude Code runs this by itself after every shell command (see
.claude/settings.json). When the command ran git commit, it adds a short
reminder to what the agent knows: the moment after a commit is when work
is usually reported, and the workshop's worst misses were claims reported
without being checked. For any other command it does nothing. It reads the
command with git_command_reading.py, so a note that merely mentions a
commit does not count.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from git_command_reading import git_commands  # noqa: E402

REMINDER = (
    "Before telling the owner or a writer about this work (error-correction skill, 'Before any claim"
    " reaches the owner'): every 'checked', 'fixed', 'works' or 'passed' points to what was run and what it"
    " printed; 'not found' says where you looked, and a cut-off output proves nothing; say what was not"
    " checked. A verdict that needs an aim or a value only the owner or the writer can give is 'held if' that"
    " aim: give it both ways and ask. One that needs a fact nobody has checked or told you (such as which draft"
    " came first) does not bear yet: name the test or the question, and if a note must go out now, give it both"
    " ways. Words that assume an order must match what is known: no list of words catches them all, so read every"
    " sentence that compares two versions. Checks that read the same page through the"
    " same frame count as one. Each 'because' must survive the flip (would you be as sure of the opposite?) and"
    " the swap (would it fit any story?)."
)


def main():
    try:
        hook_input = json.load(sys.stdin)
        command = (hook_input.get("tool_input") or {}).get("command") or ""
        if any(subcommand == "commit" for _, subcommand, _ in git_commands(command)):
            json.dump({"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": REMINDER}},
                      sys.stdout)
        return 0
    except Exception as problem:
        print(f"after_commit hook could not run ({problem})", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
