#!/usr/bin/env python3
"""The commit gate's planted-fault tests, a part of test_checks.py kept in a file of its own.

test_checks.py runs these, handing over its own helpers (the throwaway
copies, the receipt forms, the gate commit); they are kept here because
test_checks.py would otherwise pass the 100,000-byte limit that the
no-book-files check sets on every text file. Each test makes a copy of the
repository, plants one fault in what a commit through the gate would see,
makes the commit, and checks that the gate stops it for the right reason;
a neighbour checks that a near miss goes through. Run test_checks.py, not
this file.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

TEXT_ENDINGS = (".md", ".txt", ".json", ".py", ".js", ".sh", ".html", ".csv", ".yaml", ".yml", ".xml", ".tex", ".rst")


def use_the_helpers(helpers):
    """Take test_checks.py's helpers and settings (copy_repository, git, edit, fill_receipt, SCRIPTS, NOT_RUN and
    the rest) as this file's own names, so the tests read the same in either file."""
    own = ("gate_tests", "more_gate_tests", "use_the_helpers", "TEXT_ENDINGS")
    globals().update({name: value for name, value in vars(helpers).items()
                      if not name.startswith("__") and name not in own})


def gate_tests(repository_root, helpers):
    use_the_helpers(helpers)
    results = []

    def one(name, prepare, arguments, expect_committed, must_print):
        copy_root = copy_repository(repository_root)
        try:
            prepare(copy_root)
            code, output = gate_commit(copy_root, "-m", "planted", *arguments)
            passed = (code == 0) == expect_committed and (not must_print or must_print in output)
        except Exception as problem:  # any failure to plant is reported, never hidden
            passed, output = False, f"could not plant the fault: {problem}"
        shutil.rmtree(copy_root, ignore_errors=True)
        results.append((name, passed, output))

    def reviewed_change(copy_root):
        add_to_traps("plot", "- A planted rule, for testing the gate.")(copy_root)
        git(copy_root, "add", "-A")
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed")

    def loosened_on_disk(copy_root):
        edit(copy_root, os.path.join(SCRIPTS, "check_records.py"),
             replace_once("def main():\n", "def main():\n    sys.exit(0)\n"))
        edit(copy_root, PROJECT_STORY, replace_once("5. **", "5. **Rewritten. "))
        git(copy_root, "add", PROJECT_STORY)

    def loosened_with_other_work(copy_root):
        edit(copy_root, os.path.join(SCRIPTS, "check_records.py"), lambda text: text + "\n# loosened\n")
        add_to_traps("plot", "- Other work in the same commit.")(copy_root)
        git(copy_root, "add", "-A")
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed")

    def reviewed_change_for_all(copy_root):
        reviewed_change(copy_root)
        git(copy_root, "reset", "-q", "--", ".claude/skills/plot/SKILL.md")

    def after_a_skipped_commit(copy_root):
        add_to_traps("plot", "- A rule committed with the gate skipped.")(copy_root)
        commit_skipping_the_gate(copy_root, "skipped")
        record_change(copy_root)

    def a_broken_check_staged_alone(copy_root):
        break_a_script(os.path.join(SCRIPTS, "run_all_checks.py"))(copy_root)
        git(copy_root, "add", "-A")
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed")

    one("gate, neighbour: a reviewed change with every check passing is committed", reviewed_change, [],
        True, None)
    one("gate: a change with no review receipt is stopped",
        lambda copy_root: (add_to_traps("plot", "- Unreviewed.")(copy_root), git(copy_root, "add", "-A")), [],
        False, "COMMIT STOPPED")
    one("gate: a change to a frozen file is stopped",
        lambda copy_root: (edit(copy_root, "sources/bond-theory.md", lambda text: text + " "),
                           git(copy_root, "add", "-A")), [], False, "frozen file has changed")
    one("gate: a check loosened on disk (not staged) cannot pass a rewritten log entry", loosened_on_disk, [],
        False, "log entry 5 has been changed")
    one("gate: a check changed together with other work is stopped", loosened_with_other_work, [],
        False, "a check is changed together with other work")
    one("gate, neighbour: `git commit -a` of a reviewed change is committed", reviewed_change_for_all, ["-a"],
        True, None)
    one("gate: a commit made with the gate skipped is caught at the next commit", after_a_skipped_commit, [],
        False, "earlier commits the gate did not approve")
    one("gate: a check that breaks, in a commit that changes only checks, is named, and the commit stopped",
        a_broken_check_staged_alone, [], False, "COULD NOT RUN")

    def disk_gate_asks_for_staged_checks(copy_root):
        edit(copy_root, ".githooks/pre-commit", replace_once('python3 "$gate_copy" --checks-from "$checks_from"',
                                                             'python3 "$gate_copy" --checks-from staged'))
        loosened_with_other_work(copy_root)
        git(copy_root, "restore", "--staged", ".githooks/pre-commit")

    def moved_test_out(copy_root):
        git(copy_root, "mv", os.path.join(SCRIPTS, "test_checks.py"), "kept-cases/old-test.py")
        add_to_traps("plot", "- Other work in the same commit.")(copy_root)
        git(copy_root, "add", "-A")
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed")

    def deleted_a_receipt(copy_root):
        reviewed_change(copy_root)
        gate_commit(copy_root, "-m", "reviewed")
        receipts = [name for name in os.listdir(os.path.join(copy_root, ".claude/reviews")) if name.endswith(".md")]
        git(copy_root, "rm", "-q", f".claude/reviews/{receipts[0]}")
        record_change(copy_root)

    def theory_as_a_link(copy_root):
        outside = tempfile.mkdtemp(prefix="workshop-other-")
        LEFT_OVER.append(outside)
        shutil.copy(os.path.join(copy_root, "sources/bond-theory.md"), os.path.join(outside, "bond.md"))
        edit(os.path.join(outside), "bond.md", lambda text: text + " An added sentence.")
        os.remove(os.path.join(copy_root, "sources/bond-theory.md"))
        os.symlink(os.path.join(outside, "bond.md"), os.path.join(copy_root, "sources/bond-theory.md"))
        git(copy_root, "add", "-A")

    def check_only_correction_of_a_wrong_check(copy_root):
        edit(copy_root, os.path.join(SCRIPTS, "check_records.py"),
             replace_once("def main():\n", "def main():\n    print('always wrong'); sys.exit(1)\n"))
        commit_skipping_the_gate(copy_root, "a wrong check, committed where the gate could not see it")
        broken = git(copy_root, "rev-parse", "HEAD").stdout.strip()
        fill_receipt(copy_root, "theory-checker", "lead agent", "not passed (withdrawn in this commit)", commit=broken)
        edit(copy_root, os.path.join(SCRIPTS, "check_records.py"),
             replace_once("def main():\n    print('always wrong'); sys.exit(1)\n", "def main():\n"))
        git(copy_root, "add", "-A")
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed")

    one("gate: a gate file on disk asking for the staged checks is ignored", disk_gate_asks_for_staged_checks, [],
        False, "the last commit has the gate, so the checks of the last approved commit are used")
    one("gate: a check moved out of its folder, with other work, is stopped", moved_test_out, [],
        False, "a check is changed together with other work")
    one("gate: deleting a review receipt already committed is stopped", deleted_a_receipt, [],
        False, "a review receipt already committed is changed or deleted")
    one("gate: a frozen theory replaced by a link to an edited copy is stopped", theory_as_a_link, [],
        False, "stored as a link")
    one("gate, neighbour: a wrong check in the last commit is corrected in a commit of its own",
        check_only_correction_of_a_wrong_check, [], True, None)

    def attempt(name, test):
        """Run one test; a test that cannot even be planted is reported as failed, by its own name."""
        try:
            outcome = test()
            if outcome is not None:
                results.extend(outcome if isinstance(outcome, list) else [outcome])
        except Exception as problem:  # any failure to plant is reported, never hidden
            results.append((name, False, f"could not plant the fault: {problem}"))

    def inline_test_10():
        outcome = []
        copy_root = copy_repository(repository_root)
        reviewed_change(copy_root)
        code, output = gate_commit(copy_root, "-m", "reviewed")
        tree = git(copy_root, "rev-parse", "HEAD^{tree}").stdout.strip()
        message = git(copy_root, "log", "-1", "--format=%B").stdout
        outcome.append(("gate, neighbour: an approved commit carries the gate's stamp for its exact contents",
                        code == 0 and f"Workshop-gate: approved {tree}" in message, output + message))
        shutil.rmtree(copy_root)
        return outcome[0]

    attempt("gate, neighbour: an approved commit carries the gate's stamp for its exact contents", inline_test_10)

    def inline_test_11():
        copy_root = copy_repository(repository_root)
        approved = git(copy_root, "rev-parse", "HEAD").stdout.strip()
        loosen_the_log_check(copy_root)
        edit(copy_root, PROJECT_STORY, replace_once("7. **", "7. **Rewritten. "))
        commit_skipping_the_gate(copy_root, "a loosened check and the work it would stop, outside the gate")
        outside = git(copy_root, "rev-parse", "HEAD").stdout.strip()
        record_change(copy_root)
        code, output = gate_commit(copy_root, "-m", "a record")
        first = ("gate: after a commit outside the gate loosens a check and rewrites the log, the next commit is"
                 " judged by the last approved commit's checks", code != 0 and "log entry 7 has been changed" in output,
                 output)
        git(copy_root, "checkout", approved, "--", os.path.join(SCRIPTS, "check_records.py"), PROJECT_STORY)
        record_change(copy_root)
        fill_receipt(copy_root, "theory-checker", "lead agent", "not passed (withdrawn in this commit)", commit=outside)
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed")
        code, output = gate_commit(copy_root, "-m", "the check and the log put right")
        second = ("gate, neighbour: once the check and the log are put right, with a late receipt, the next commit"
                  " goes through", code == 0, output)
        shutil.rmtree(copy_root)
        return [first, second]

    attempt("gate: after a commit outside the gate loosens a check and rewrites the log, the next commit is judged"
            " by the last approved commit's checks", inline_test_11)

    def inline_test_12():
        outcome = []
        copy_root = copy_repository(repository_root)
        reviewed_change(copy_root)
        gate_commit(copy_root, "-m", "reviewed")
        edit(copy_root, ".claude/skills/plot/SKILL.md", replace_once("for testing the gate.", "for testing the gate, amended."))
        git(copy_root, "add", "-A")
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed")
        code_amend, output_amend = gate_commit(copy_root, "--amend", "-m", "reviewed, amended")
        record_change(copy_root)
        code, output = gate_commit(copy_root, "-m", "a record")
        outcome.append(("gate, neighbour: after an amended reviewed commit, the next commit goes through",
                        code_amend == 0 and code == 0, output_amend + output))
        shutil.rmtree(copy_root)
        return outcome[0]

    attempt('gate, neighbour: after an amended reviewed commit, the next commit goes through', inline_test_12)

    def inline_test_13():
        outcome = []
        copy_root = copy_repository(repository_root)
        main_branch = git(copy_root, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
        git(copy_root, "checkout", "-q", "-b", "side")
        reviewed_change(copy_root)
        code_side, output_side = gate_commit(copy_root, "-m", "reviewed on a branch")
        add_to_traps("dialogue", "- A second reviewed rule, on the branch.")(copy_root)
        git(copy_root, "add", "-A")
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed")
        code_second, output_second = gate_commit(copy_root, "-m", "reviewed on a branch, again")
        code_side, output_side = max(code_side, code_second), output_side + output_second
        git(copy_root, "checkout", "-q", main_branch)
        add_to_traps("character", "- A second reviewed rule, on the main line.")(copy_root)
        git(copy_root, "add", "-A")
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed")
        code_main, output_main = gate_commit(copy_root, "-m", "reviewed on the main line")
        merge = git(copy_root, *NO_SIGNING, "merge", "--no-ff", "-m", "merge", "side", check=False)
        outcome.append(("gate, neighbour: an honest merge of two reviewed commits goes through",
                        code_side == 0 and code_main == 0 and merge.returncode == 0,
                        output_side + output_main + merge.stdout + merge.stderr))
        tree = git(copy_root, "rev-parse", "HEAD^{tree}").stdout.strip()
        stamps = git(copy_root, "log", "-1", "--format=%(trailers:key=Workshop-gate,valueonly)").stdout
        outcome.append(("gate, neighbour: a merge made with git merge -m carries the gate's stamp",
                        merge.returncode == 0 and f"approved {tree}" in stamps, stamps))
        shutil.rmtree(copy_root)
        return outcome

    attempt('gate, neighbour: an honest merge of two reviewed commits goes through', inline_test_13)

    def inline_test_0():
        copy_root = copy_repository(repository_root)
        approved = git(copy_root, "rev-parse", "HEAD").stdout.strip()
        main_branch = git(copy_root, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
        git(copy_root, "checkout", "-q", "-b", "side")
        edit(copy_root, "sources/bond-theory.md", lambda text: text + " ")
        commit_skipping_the_gate(copy_root, "theory edited on a branch")
        git(copy_root, "checkout", "-q", main_branch)
        git(copy_root, "merge", "-q", "--ff-only", "side")
        record_change(copy_root)
        code, output = gate_commit(copy_root, "-m", "a record")
        first = ("gate: a theory edit brought in by a fast-forward stops the next commit",
                 code != 0 and "bond-theory.md: frozen file has changed" in output, output)
        git(copy_root, "checkout", approved, "--", "sources/bond-theory.md")
        record_change(copy_root)
        code, output = gate_commit(copy_root, "-m", "the theory put back")
        second = ("gate, neighbour: once the theory is put back, the next commit goes through", code == 0, output)
        shutil.rmtree(copy_root)
        return [first, second]

    attempt('gate: a theory edit brought in by a fast-forward stops the next commit', inline_test_0)

    def inline_test_check_only_with_the_log():
        copy_root = copy_repository(repository_root)
        loosen_the_log_check(copy_root)
        edit(copy_root, PROJECT_STORY, lambda text: re.sub(
            r"^(12\. \*\*[^\n]*)$", lambda match: match.group(1) + " Rewritten.", text, count=1, flags=re.M))
        git(copy_root, "add", "-A")
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed")
        code, output = gate_commit(copy_root, "-m", "a loosened check with the log")
        shutil.rmtree(copy_root)
        return ("gate: a check change that carries the log is judged by the last approved commit's checks",
                code != 0 and "log entry 12 has been changed" in output, output)

    attempt("gate: a check change that carries the log is judged by the last approved commit's checks",
            inline_test_check_only_with_the_log)

    def inline_test_check_only():
        copy_root = copy_repository(repository_root)
        edit(copy_root, os.path.join(ADD_SOURCE_SCRIPTS, "check_maps.py"), lambda text: text + "\n# a comment\n")
        git(copy_root, "add", "-A")
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed")
        code, output = gate_commit(copy_root, "-m", "only a check")
        shutil.rmtree(copy_root)
        return ("gate, neighbour: a commit that changes only checks, with its receipt, is judged by its own checks",
                code == 0 and "this commit changes only checks" in output, output)

    attempt("gate, neighbour: a commit that changes only checks, with its receipt, is judged by its own checks",
            inline_test_check_only)

    def inline_test_rebased_hook_change():
        copy_root = copy_repository(repository_root)
        main_branch = git(copy_root, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
        git(copy_root, "checkout", "-q", "-b", "side")
        edit(copy_root, os.path.join(HOOKS, "after_commit.py"), lambda text: text + "\n# a reviewed comment\n")
        git(copy_root, "add", "-A")
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed")
        code_side, output_side = gate_commit(copy_root, "-m", "a reviewed hook change")
        git(copy_root, "checkout", "-q", main_branch)
        record_change(copy_root)
        code_main, output_main = gate_commit(copy_root, "-m", "a record on the main line")
        git(copy_root, "checkout", "-q", "side")
        rebase = git(copy_root, *NO_SIGNING, "rebase", "-q", main_branch, check=False)
        record_change(copy_root, "another record")
        code, output = gate_commit(copy_root, "-m", "after the rebase")
        shutil.rmtree(copy_root)
        return ("gate, neighbour: a reviewed hook change, rebased, is noted for a person and the next commit goes"
                " through", code_side == 0 and code_main == 0 and rebase.returncode == 0 and code == 0
                and "changed the gate's own files" in output,
                output_side + output_main + rebase.stdout + rebase.stderr + output)

    attempt("gate, neighbour: a reviewed hook change, rebased, is noted for a person and the next commit goes"
            " through", inline_test_rebased_hook_change)

    def inline_test_rebase_over_the_same_file():
        copy_root = copy_repository(repository_root)
        main_branch = git(copy_root, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
        git(copy_root, "checkout", "-q", "-b", "side")
        reviewed_change(copy_root)
        code_side, output_side = gate_commit(copy_root, "-m", "a reviewed rule on the branch")
        git(copy_root, "checkout", "-q", main_branch)
        edit(copy_root, ".claude/skills/plot/SKILL.md", lambda text: text + "\n- A reviewed line at the end.\n")
        git(copy_root, "add", "-A")
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed")
        code_main, output_main = gate_commit(copy_root, "-m", "a reviewed line in the same file")
        git(copy_root, "checkout", "-q", "side")
        rebase = git(copy_root, *NO_SIGNING, "rebase", "-q", main_branch, check=False)
        record_change(copy_root)
        code, output = gate_commit(copy_root, "-m", "after the rebase")
        shutil.rmtree(copy_root)
        return ("gate, neighbour: a reviewed change rebased over another change to the same file keeps its receipt",
                code_side == 0 and code_main == 0 and rebase.returncode == 0 and code == 0,
                output_side + output_main + rebase.stdout + rebase.stderr + output)

    attempt("gate, neighbour: a reviewed change rebased over another change to the same file keeps its receipt",
            inline_test_rebase_over_the_same_file)

    def inline_test_settled():
        copy_root = copy_repository(repository_root)
        outside = []
        for number in range(3):
            edit(copy_root, os.path.join(SCRIPTS, "check_records.py"),
                 lambda text, number=number: text + f"\n# an outside change, number {number}\n")
            commit_skipping_the_gate(copy_root, f"an outside check change, number {number}")
            outside.append(git(copy_root, "rev-parse", "HEAD").stdout.strip())
        for commit in outside:
            fill_receipt(copy_root, "theory-checker", "lead agent", "passed", commit=commit)
        code, output = gate_commit(copy_root, "-m", "late receipts for three outside commits")
        record_change(copy_root)
        code_next, output_next = gate_commit(copy_root, "-m", "a record")
        code_recheck, output_recheck = run(copy_root, os.path.join(SCRIPTS, "recheck_commits.py"), "--root", copy_root)
        shutil.rmtree(copy_root)
        return ("gate, neighbour: reviewed outside commits are settled once a commit through the gate is approved",
                code == 0 and code_next == 0 and code_recheck == 0 and "rechecked 0 commit(s)" in output_recheck,
                output + output_next + output_recheck)

    attempt("gate, neighbour: reviewed outside commits are settled once a commit through the gate is approved",
            inline_test_settled)

    def inline_test_withdrawn():
        results_here = []
        for really in (False, True):
            copy_root = copy_repository(repository_root)
            add_to_traps("plot", "- Show every clue at least twice.")(copy_root)
            commit_skipping_the_gate(copy_root, "an unreviewed rule, outside the gate")
            outside = git(copy_root, "rev-parse", "HEAD").stdout.strip()
            if really:
                git(copy_root, "revert", "--no-commit", outside)
                fill_receipt(copy_root, "theory-checker", "lead agent", "passed")
            else:
                record_change(copy_root)
            fill_receipt(copy_root, "theory-checker", "lead agent", "not passed (withdrawn in this commit)",
                         commit=outside)
            code, output = gate_commit(copy_root, "-m", "the withdrawal")
            shutil.rmtree(copy_root)
            if really:
                results_here.append(("gate, neighbour: a change really withdrawn (git revert --no-commit), with its"
                                     " late receipt, goes through", code == 0, output))
            else:
                results_here.append(("gate: a receipt that says 'withdrawn' while the change is still there is"
                                     " refused", code != 0 and "is still in" in output, output))
        return results_here

    attempt("gate: a receipt that says 'withdrawn' while the change is still there is refused", inline_test_withdrawn)

    def inline_test_loosened_receipt_check():
        copy_root = copy_repository(repository_root)
        edit(copy_root, os.path.join(SCRIPTS, "review_receipt.py"), replace_once(
            "def in_scope(path):\n", "def in_scope(path):\n    return False\n"))
        git(copy_root, "add", "-A")
        code, output = gate_commit(copy_root, "-m", "a receipt check loosened, with no receipt")
        shutil.rmtree(copy_root)
        return ("gate: a commit that changes only checks cannot loosen the receipt check for itself",
                code != 0 and "no review receipt" in output, output)

    attempt("gate: a commit that changes only checks cannot loosen the receipt check for itself",
            inline_test_loosened_receipt_check)

    def inline_test_large_report_with_a_check():
        copy_root = copy_repository(repository_root)
        write(copy_root, ".claude/reviews/kept/2099-01-01-long-report.md", "A made-up report line.\n" * 6000)
        edit(copy_root, os.path.join(SCRIPTS, "run_all_checks.py"), replace_once(
            "LARGE_RECORDS_ALLOWED = {", 'LARGE_RECORDS_ALLOWED = {\n    ".claude/reviews/kept/2099-01-01-long-report.md": "",'))
        git(copy_root, "add", "-A")
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed")
        code, output = gate_commit(copy_root, "-m", "a long report with a check change")
        shutil.rmtree(copy_root)
        return ("gate: a check change that carries anything but a receipt is judged by the last approved commit's"
                " checks", code != 0 and "a large text file" in output, output)

    attempt("gate: a check change that carries anything but a receipt is judged by the last approved commit's checks",
            inline_test_large_report_with_a_check)

    def inline_test_pull():
        copy_root = copy_repository(repository_root)
        main_branch = git(copy_root, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
        git(copy_root, "checkout", "-q", "-b", "side")
        reviewed_change(copy_root)
        code_side, output_side = gate_commit(copy_root, "-m", "a reviewed rule on a branch")
        add_to_traps("dialogue", "- A second reviewed rule, on the branch.")(copy_root)
        git(copy_root, "add", "-A")
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed")
        code_second, output_second = gate_commit(copy_root, "-m", "a second reviewed rule")
        git(copy_root, "checkout", "-q", main_branch)
        record_change(copy_root)
        code_main, output_main = gate_commit(copy_root, "-m", "a record on the main line")
        pull = git(copy_root, *NO_SIGNING, "pull", "-q", "--no-rebase", "--no-edit", ".", "side", check=False)
        shutil.rmtree(copy_root)
        return ("gate, neighbour: a pull of two reviewed commits that makes a merge goes through",
                code_side == 0 and code_second == 0 and code_main == 0 and pull.returncode == 0,
                output_side + output_second + output_main + pull.stdout + pull.stderr)

    attempt("gate, neighbour: a pull of two reviewed commits that makes a merge goes through", inline_test_pull)

    def inline_test_reordered():
        copy_root = copy_repository(repository_root)
        edit(copy_root, ".claude/skills/plot/SKILL.md", replace_once(
            "## Traps\n", "## Traps\n\n- First planted line.\n- Second planted line.\n"))
        git(copy_root, "add", "-A")
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed")
        gate_commit(copy_root, "-m", "two reviewed lines")
        edit(copy_root, ".claude/skills/plot/SKILL.md", replace_once(
            "- First planted line.\n- Second planted line.\n", "- Second planted line.\n- First planted line.\n"))
        commit_skipping_the_gate(copy_root, "the two lines swapped, outside the gate")
        outside = git(copy_root, "rev-parse", "HEAD").stdout.strip()
        record_change(copy_root)
        fill_receipt(copy_root, "theory-checker", "lead agent", "not passed (withdrawn in this commit)", commit=outside)
        code, output = gate_commit(copy_root, "-m", "a withdrawal claimed, nothing withdrawn")
        shutil.rmtree(copy_root)
        return ("gate: a reordering claimed as withdrawn, while the new order stands, is refused",
                code != 0 and "is still in" in output, output)

    attempt("gate: a reordering claimed as withdrawn, while the new order stands, is refused", inline_test_reordered)

    def inline_test_moved_after_review():
        copy_root = copy_repository(repository_root)
        edit(copy_root, ".claude/skills/plot/SKILL.md", replace_once("## Traps\n", "## Traps\n- A reviewed line.\n"))
        git(copy_root, "add", "-A")
        first = run(copy_root, os.path.join(SCRIPTS, "review_receipt.py"), "fingerprint", "--root", copy_root)[1]
        edit(copy_root, ".claude/skills/plot/SKILL.md", replace_once("## Traps\n- A reviewed line.\n", "## Traps\n"))
        edit(copy_root, ".claude/skills/plot/SKILL.md", replace_once("## The stance\n", "## The stance\n- A reviewed line.\n"))
        git(copy_root, "add", "-A")  # exactly the same added line, in another section
        second = run(copy_root, os.path.join(SCRIPTS, "review_receipt.py"), "fingerprint", "--root", copy_root)[1]
        shutil.rmtree(copy_root)
        return ("receipts: a reviewed line moved to another place gets a new fingerprint",
                first.split()[:1] != second.split()[:1] and bool(first.strip()), first + second)

    attempt("receipts: a reviewed line moved to another place gets a new fingerprint", inline_test_moved_after_review)

    def inline_test_retired_on_a_branch():
        outcome = []
        for how in ("merge", "rebase"):
            copy_root = copy_repository(repository_root)
            main_branch = git(copy_root, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
            git(copy_root, "checkout", "-q", "-b", "side")
            edit(copy_root, os.path.join(SCRIPTS, "check_records.py"), lambda text: text + "\n# a reviewed comment\n")
            git(copy_root, "add", "-A")
            receipt = fill_receipt(copy_root, "the owner, with theory-checker", "lead agent", "passed")
            edit(copy_root, receipt, lambda text: re.sub(r"(## Tests retired\n\n)\([^\n]*\)",
                                                         r"\1- maps: a misspelt path", text))
            git(copy_root, "add", "-A")
            code_side, output_side = gate_commit(copy_root, "-m", "a reviewed check change that retires a test")
            git(copy_root, "checkout", "-q", main_branch)
            record_change(copy_root)
            gate_commit(copy_root, "-m", "a record on the main line")
            if how == "merge":  # the merge in progress, as the gate sees it
                result = git(copy_root, *NO_SIGNING, "-c", "core.hooksPath=/dev/null", "merge", "-q", "--no-ff",
                             "--no-commit", "side", check=False)
            else:  # the rebased commit no longer matches its stamp, so it is not approved
                git(copy_root, "checkout", "-q", "side")
                result = git(copy_root, *NO_SIGNING, "-c", "core.hooksPath=/dev/null", "rebase", "-q", main_branch,
                             check=False)
            retired_names = retired_tests_for_test(copy_root)
            shutil.rmtree(copy_root)
            outcome.append((f"gate: a retirement named in a receipt on a branch is read after a {how}",
                            code_side == 0 and "maps: a misspelt path" in retired_names,
                            output_side + retired_names + str(result.stdout) + str(result.stderr)))
        return outcome

    def retired_tests_for_test(copy_root):
        """The retirements the gate would read now, asked of the copy's own gate script."""
        asking = (f"import sys; sys.path.insert(0, {os.path.join(copy_root, SCRIPTS)!r}); import check_commit; "
                  f"finder = getattr(check_commit, 'Approval', None); "
                  f"approved = finder({copy_root!r}).last_approved_commit() if finder "
                  f"else check_commit.last_approved_commit({copy_root!r}); "
                  f"print(check_commit.retired_tests({copy_root!r}, approved or 'HEAD'))")
        result = subprocess.run([sys.executable, "-c", asking], capture_output=True, text=True, check=False,
                                cwd=copy_root)
        return result.stdout + result.stderr

    attempt("gate: a retirement named in a receipt on a branch is read after a merge", inline_test_retired_on_a_branch)

    def copy_before_the_gate():
        """A copy whose main line starts before the gate (its first commit lacks the gate script), with the gate
        brought in on a branch through the gate itself, as this build was; returns the copy and the main line."""
        copy_root = copy_repository(repository_root, stamped=False)
        main_branch = git(copy_root, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
        gate_script = os.path.join(copy_root, SCRIPTS, "check_commit.py")
        with open(gate_script, encoding="utf-8") as script:
            kept = script.read()
        git(copy_root, "rm", "-q", "--cached", os.path.join(SCRIPTS, "check_commit.py"))
        git(copy_root, *NO_SIGNING, "commit", "-q", "--amend", "-m", "the workshop before the gate")
        git(copy_root, "checkout", "-q", "-b", "build")
        with open(gate_script, "w", encoding="utf-8") as script:
            script.write(kept)
        git(copy_root, "add", "-A")
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed")
        code, output = gate_commit(copy_root, "-m", "the gate brought in")
        if code != 0:
            raise AssertionError(f"the gate could not be brought in: {output}")
        git(copy_root, "checkout", "-q", main_branch)
        return copy_root, main_branch

    def inline_test_merged_on_github(also_loosen):
        if True:
            copy_root, _ = copy_before_the_gate()
            git(copy_root, *NO_SIGNING, "-c", "core.hooksPath=/dev/null", "merge", "-q", "--no-ff", "-m",
                "Merge pull request 1", "build")
            edit(copy_root, PROJECT_STORY, replace_once("5. **", "5. **Rewritten. "))
            if also_loosen:
                loosen_the_log_check(copy_root)
            commit_skipping_the_gate(copy_root, "an edit made on GitHub")
            record_change(copy_root)
            code, output = gate_commit(copy_root, "-m", "a record")
            shutil.rmtree(copy_root)
            what = "a loosened check and a log rewrite" if also_loosen else "a log rewrite"
            return (f"gate: after the gate is merged on GitHub as a merge commit, {what} made on GitHub stops the next"
                    " commit", code != 0 and "log entry 5 has been changed" in output, output)

    for also_loosen in (False, True):
        what = "a loosened check and a log rewrite" if also_loosen else "a log rewrite"
        attempt(f"gate: after the gate is merged on GitHub as a merge commit, {what} made on GitHub stops the next"
                " commit", lambda also_loosen=also_loosen: inline_test_merged_on_github(also_loosen))

    def inline_test_merge_through_the_real_stage():
        name = ("gate, neighbour: a merge bringing a reviewed hook change goes through the real planted-fault stage"
                " (outside the test's own copies)")
        if ALREADY_INSIDE:
            NOT_RUN.append(name + ": this run is itself inside the planted-fault test")
            return None
        copy_root = copy_repository(repository_root, prefix="workshop-plain-")
        environment = {name_: value for name_, value in os.environ.items()
                       if name_ != "WORKSHOP_INSIDE_PLANTED_FAULT_TEST"}
        main_branch = git(copy_root, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
        git(copy_root, "checkout", "-q", "-b", "hook-comment")
        edit(copy_root, os.path.join(HOOKS, "after_commit.py"),
             lambda text: text + "\n# a reviewed comment, for the test that merges through the real stage\n")
        git(copy_root, "add", "-A")
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed")
        git(copy_root, "config", "core.hooksPath", ".githooks")
        steps = [subprocess.run(["git", *NO_SIGNING, "commit", "-q", "-m", "a reviewed hook comment"], cwd=copy_root,
                                capture_output=True, text=True, env=environment, check=False)]
        git(copy_root, "checkout", "-q", main_branch)
        record_change(copy_root)
        steps.append(subprocess.run(["git", *NO_SIGNING, "commit", "-q", "-m", "a record"], cwd=copy_root,
                                    capture_output=True, text=True, env=environment, check=False))
        steps.append(subprocess.run(["git", *NO_SIGNING, "merge", "--no-ff", "-m", "Merge the hook comment",
                                     "hook-comment"], cwd=copy_root, capture_output=True, text=True, env=environment,
                                    check=False))
        output = "\n".join(step.stdout + step.stderr for step in steps)
        shutil.rmtree(copy_root, ignore_errors=True)
        return (name, all(step.returncode == 0 for step in steps)
                and "passed    the last approved commit's planted-fault test" in output, output)

    attempt("gate, neighbour: a merge bringing a reviewed hook change goes through the real planted-fault stage",
            inline_test_merge_through_the_real_stage)

    def inline_test_planted_stage():
        name = ("gate: the last approved commit's planted-fault test really runs on a changed check (outside the"
                " test's own copies)")
        if ALREADY_INSIDE:
            NOT_RUN.append(name + ": this run is itself inside the planted-fault test")
            return None
        copy_root = copy_repository(repository_root, prefix="workshop-plain-")
        edit(copy_root, os.path.join(ADD_SOURCE_SCRIPTS, "check_maps.py"),
             lambda text: text + "\n# a comment, for the test that runs the planted-fault stage for real\n")
        git(copy_root, "add", "-A")
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed")
        git(copy_root, "config", "core.hooksPath", ".githooks")
        environment = {name_: value for name_, value in os.environ.items()
                       if name_ != "WORKSHOP_INSIDE_PLANTED_FAULT_TEST"}
        result = subprocess.run(["git", *NO_SIGNING, "commit", "-q", "-m", "a check changed"], cwd=copy_root,
                                capture_output=True, text=True, env=environment, check=False)
        output = result.stdout + result.stderr
        shutil.rmtree(copy_root, ignore_errors=True)
        return (name, result.returncode == 0
                and "passed    the last approved commit's planted-fault test" in output, output)

    attempt("gate: the last approved commit's planted-fault test really runs on a changed check (outside the"
            " test's own copies)", inline_test_planted_stage)

    def inline_test_1():
        outcome = []
        copy_root = copy_repository(repository_root)
        main_branch = git(copy_root, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
        git(copy_root, "checkout", "-q", "-b", "side")
        add_to_traps("plot", "- A rule on a branch, never reviewed.")(copy_root)
        commit_skipping_the_gate(copy_root, "unreviewed on a branch")
        git(copy_root, "checkout", "-q", main_branch)
        record_change(copy_root)
        code, output = gate_commit(copy_root, "-m", "a record")
        merge = git(copy_root, *NO_SIGNING, "merge", "--no-ff", "-m", "merge", "side", check=False)
        outcome.append(("gate: a merge commit runs the gate, which finds the unreviewed commit it brings in",
                        code == 0 and merge.returncode != 0 and re.search(r"commit [0-9a-f]{9}: no review receipt",
                                                                           merge.stdout + merge.stderr) is not None,
                        output + merge.stdout + merge.stderr))
        shutil.rmtree(copy_root)
        return outcome[0]

    attempt('gate: a merge commit runs the gate, which finds the unreviewed commit it brings in', inline_test_1)

    def inline_test_2():
        outcome = []
        copy_root = copy_repository(repository_root)
        reviewed_change(copy_root)
        code, output = gate_commit(copy_root, "-m", "reviewed")
        code_again, output_again = run(copy_root, os.path.join(SCRIPTS, "recheck_commits.py"), "--root", copy_root)
        outcome.append(("recheck, neighbour: after a clean commit through the gate, nothing is found", code == 0
                        and code_again == 0 and "rechecked 0 commit(s) the gate did not approve" in output_again,
                        output + output_again))
        shutil.rmtree(copy_root)
        return outcome[0]

    attempt('recheck, neighbour: after a clean commit through the gate, nothing is found', inline_test_2)

    def inline_test_3():
        outcome = []
        copy_root = copy_repository(repository_root)
        git(copy_root, *NO_SIGNING, "commit", "-q", "--allow-empty", "-m", "base")
        before = last_entry_number(copy_root)
        edit(copy_root, "kept-cases/runs.md", lambda text: text + "\n" + run(copy_root, os.path.join(
            SCRIPTS, "check_records.py"), "--fingerprints", "--root", copy_root)[1])
        git(copy_root, "add", "-A")
        git(copy_root, *NO_SIGNING, "commit", "-q", "-m", "a fresh run")
        edit(copy_root, ".claude/skills/character/SKILL.md", replace_once("## Traps\n", "## Traps\n\n- A new rule.\n"))
        edit(copy_root, ".claude/skills/plot/SKILL.md", replace_once("## Traps\n", "## Traps \n"))
        code_line, line = run(copy_root, os.path.join(SCRIPTS, "check_records.py"), "--fingerprints", "plot",
                              "--root", copy_root)
        edit(copy_root, "kept-cases/runs.md", lambda text: text + "\n" + line)
        code, output = run(copy_root, os.path.join(SCRIPTS, "check_records.py"), copy_root)
        outcome.append(("records, neighbour: a typo's fingerprint line clears only its own skill",
                        before > 0 and code_line == 0 and "not rerun since these skills changed: character" in output
                        and "plot" not in output.split("skills changed:")[-1].split("(")[0], line + output))
        shutil.rmtree(copy_root)
        return outcome[0]

    attempt("records, neighbour: a typo's fingerprint line clears only its own skill", inline_test_3)

    def inline_test_owed_skill():
        copy_root = copy_repository(repository_root)
        edit(copy_root, "kept-cases/runs.md", lambda text: text + "\n" + run(copy_root, os.path.join(
            SCRIPTS, "check_records.py"), "--fingerprints", "--root", copy_root)[1])
        git(copy_root, "add", "-A")
        git(copy_root, *NO_SIGNING, "commit", "-q", "-m", "a fresh run")
        edit(copy_root, ".claude/skills/plot/SKILL.md", replace_once("## Traps\n", "## Traps\n\n- A new rule.\n"))
        git(copy_root, "add", "-A")
        git(copy_root, *NO_SIGNING, "commit", "-q", "-m", "a meaning change; the plot cases are now owed")
        edit(copy_root, ".claude/skills/plot/SKILL.md", replace_once("## Traps\n", "## Traps \n"))
        code, output = run(copy_root, os.path.join(SCRIPTS, "check_records.py"), "--fingerprints", "plot",
                           "--root", copy_root)
        code_other, output_other = run(copy_root, os.path.join(SCRIPTS, "check_records.py"), "--fingerprints",
                                       "error-correction", "--root", copy_root)
        shutil.rmtree(copy_root)
        return [("records: a typo's fingerprint line is refused for a skill already owed a rerun",
                 code == 1 and "cases were already owed a rerun" in output, output),
                ("records, neighbour: a skill with no kept cases needs no fingerprint line",
                 "has no kept cases" in output_other, output_other)]

    attempt("records: a typo's fingerprint line is refused for a skill already owed a rerun", inline_test_owed_skill)

    return results


def more_gate_tests(repository_root, helpers):
    """The tests added after the fifth look: git commit -a and <file>, a broken gate script, the way back for a
    frozen file, merges made on GitHub, two sessions' log entries, a stale branch, the route after a conflicted
    merge, Windows line endings, and the recheck's large record."""
    use_the_helpers(helpers)
    results = []

    def one(name, prepare, arguments, expect_committed, must_print):
        copy_root = copy_repository(repository_root)
        try:
            prepare(copy_root)
            code, output = gate_commit(copy_root, "-m", "planted", *arguments)
            passed = (code == 0) == expect_committed and (not must_print or must_print in output)
        except Exception as problem:  # any failure to plant is reported, never hidden
            passed, output = False, f"could not plant the fault: {problem}"
        shutil.rmtree(copy_root, ignore_errors=True)
        results.append((name, passed, output))

    def attempt(name, test):
        try:
            outcome = test()
            if outcome is not None:
                results.extend(outcome if isinstance(outcome, list) else [outcome])
        except Exception as problem:  # any failure to plant is reported, never hidden
            results.append((name, False, f"could not plant the fault: {problem}"))

    def reviewed_change(copy_root):
        add_to_traps("plot", "- A planted rule, for testing the gate.")(copy_root)
        git(copy_root, "add", "-A")
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed")

    def frozen_edit_unstaged(copy_root):  # nothing staged: git commit -a takes both changes
        edit(copy_root, "sources/bond-theory.md", lambda text: text + " ")
        edit(copy_root, PROJECT_STORY,
             lambda story: story.replace("## Word list", "## Word list\n\n- **Planted:** a record.", 1))

    one("gate: an edit to a frozen theory committed with git commit -a is stopped", frozen_edit_unstaged, ["-a"],
        False, "bond-theory.md: frozen file has changed")
    one("gate: an edit to a frozen theory committed with git commit <file> is stopped",
        lambda copy_root: edit(copy_root, "sources/bond-theory.md", lambda text: text + " "),
        ["--", "sources/bond-theory.md"], False, "bond-theory.md: frozen file has changed")

    def withdrawn_then_committed_with_a(copy_root):
        add_to_traps("plot", "- A rule committed outside the gate, then withdrawn.")(copy_root)
        commit_skipping_the_gate(copy_root, "a rule made outside the gate")
        outside = git(copy_root, "rev-parse", "HEAD").stdout.strip()
        git(copy_root, "revert", "--no-commit", outside)
        fill_receipt(copy_root, "theory-checker", "lead agent", "not passed (withdrawn in this commit)", commit=outside)
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed")
        git(copy_root, "reset", "-q", "--", ".claude/skills/plot/SKILL.md")  # left for commit -a to take

    one("gate, neighbour: a withdrawal committed with git commit -a goes through", withdrawn_then_committed_with_a,
        ["-a"], True, None)

    def broken_gate_script(copy_root):
        break_a_script(os.path.join(SCRIPTS, "check_commit.py"))(copy_root)
        commit_skipping_the_gate(copy_root, "a typo in the gate script, made on GitHub")
        record_change(copy_root)

    one("gate: a gate script broken by a typo stops the next commit with a plain line", broken_gate_script, [],
        False, "it broke before it finished")

    def inline_test_way_back_for_a_frozen_file():
        copy_root = copy_repository(repository_root)
        first = git(copy_root, "rev-parse", "HEAD").stdout.strip()
        edit(copy_root, "sources/bond-theory.md", lambda text: text + " ")
        git(copy_root, "add", "-A")
        tree = git(copy_root, "write-tree").stdout.strip()
        git(copy_root, *NO_SIGNING, "commit", "-q", SKIP_THE_GATE, "-m",
            f"a theory edit, stamped as a broken gate would stamp it\n\nWorkshop-gate: approved {tree}")
        record_change(copy_root)
        code, output = gate_commit(copy_root, "-m", "a record")
        shutil.rmtree(copy_root)
        return ("gate: a frozen theory changed in an approved commit is traced back to a commit that still has the"
                " listed text", code != 0 and f"git checkout {first[:9]} -- 'sources/bond-theory.md'" in output, output)

    attempt("gate: a frozen theory changed in an approved commit is traced back to a commit that still has the listed"
            " text", inline_test_way_back_for_a_frozen_file)

    def merge_without_the_gate(copy_root, *arguments):
        return git(copy_root, *NO_SIGNING, "-c", "core.hooksPath=/dev/null", "merge", "-q", "--no-ff", *arguments,
                   check=False)

    def finish_without_the_gate(copy_root):
        git(copy_root, *NO_SIGNING, "-c", "core.hooksPath=/dev/null", "commit", "-q", "--no-edit")

    def keep_one_side_and_renumber_the_other(copy_root, side, other_body):
        """Resolve a conflict in the log: keep one side's file (":2:" ours, ":3:" theirs), then add the other side's
        entry after it, under the next number, with every status line restamped."""
        with open(os.path.join(copy_root, PROJECT_STORY), "w", encoding="utf-8") as story:
            story.write(git(copy_root, "show", f"{side}{PROJECT_STORY}").stdout)
        add_log_entry(copy_root, True, other_body)
        git(copy_root, "add", "-A")

    def inline_test_two_sessions_merged_on_github():
        outcome = []
        for natural in (True, False):
            copy_root = copy_repository(repository_root)
            main_branch = git(copy_root, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
            number = last_entry_number(copy_root) + 1
            for branch, body in (("session-x", "Session X's entry."), ("session-y", "Session Y's entry.")):
                git(copy_root, "checkout", "-q", "-b", branch, main_branch)
                add_log_entry(copy_root, True, body)
                git(copy_root, "add", "-A")
                gate_commit(copy_root, "-m", f"an entry on {branch}")
            git(copy_root, "checkout", "-q", main_branch)
            merge_without_the_gate(copy_root, "-m", "Merge pull request 1", "session-x")
            first_merge = git(copy_root, "rev-parse", "HEAD").stdout.strip()
            merge_without_the_gate(copy_root, "-m", "Merge pull request 2", "session-y")
            if natural:
                keep_one_side_and_renumber_the_other(copy_root, ":2:", "Session Y's entry.")
            else:
                keep_one_side_and_renumber_the_other(copy_root, ":3:", "Session X's entry.")
            finish_without_the_gate(copy_root)
            record_change(copy_root)
            code, output = gate_commit(copy_root, "-m", "a record")
            shutil.rmtree(copy_root)
            if natural:
                outcome.append(("gate, neighbour: two sessions' entries merged on GitHub, the main line's entry kept"
                                " and the other renumbered after it: the next commit goes through, judged by the"
                                " main line", code == 0 and first_merge[:9] in output, output))
            else:
                outcome.append(("gate: two sessions' entries merged on GitHub, the main line's entry renumbered: the"
                                " next commit is stopped", code != 0
                                and f"log entry {number} has been changed" in output, output))
        return outcome

    attempt("gate, neighbour: two sessions' entries merged on GitHub", inline_test_two_sessions_merged_on_github)

    def inline_test_both_added_through_the_gate():
        copy_root = copy_repository(repository_root)
        main_branch = git(copy_root, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
        git(copy_root, "checkout", "-q", "-b", "session-x")
        add_log_entry(copy_root, True, "Session X's entry.")
        git(copy_root, "add", "-A")
        code_x, output_x = gate_commit(copy_root, "-m", "an entry on a branch")
        git(copy_root, "checkout", "-q", main_branch)
        add_log_entry(copy_root, True, "The main line's entry.")
        git(copy_root, "add", "-A")
        code_main, output_main = gate_commit(copy_root, "-m", "an entry on the main line")
        git(copy_root, *NO_SIGNING, "merge", "-q", "--no-ff", "-m", "merge the branch", "session-x", check=False)
        keep_one_side_and_renumber_the_other(copy_root, ":2:", "Session X's entry.")
        code, output = gate_commit(copy_root, "--no-edit")
        first = ("gate: a merge through the gate where both lines added the same log entry number is stopped, with"
                 " the advice to rebase", code_x == 0 and code_main == 0 and code != 0
                 and "both lines of work being merged added a log entry" in output, output_x + output_main + output)
        shutil.rmtree(copy_root)
        return first

    attempt("gate: a merge through the gate where both lines added the same log entry number is stopped",
            inline_test_both_added_through_the_gate)

    def inline_test_the_rebase_route():
        copy_root = copy_repository(repository_root)
        main_branch = git(copy_root, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
        git(copy_root, "checkout", "-q", "-b", "session-x")
        add_log_entry(copy_root, True, "Session X's entry.")
        git(copy_root, "add", "-A")
        gate_commit(copy_root, "-m", "an entry on a branch")
        git(copy_root, "checkout", "-q", main_branch)
        add_log_entry(copy_root, True, "The main line's entry.")
        git(copy_root, "add", "-A")
        gate_commit(copy_root, "-m", "an entry on the main line")
        git(copy_root, "checkout", "-q", "session-x")
        git(copy_root, *NO_SIGNING, "-c", "core.hooksPath=/dev/null", "rebase", "-q", main_branch, check=False)
        with open(os.path.join(copy_root, PROJECT_STORY), "w", encoding="utf-8") as story:
            story.write(git(copy_root, "show", f":2:{PROJECT_STORY}").stdout)  # in a rebase, :2: is the other line
        add_log_entry(copy_root, True, "Session X's entry.")
        git(copy_root, "add", "-A")
        rebased = git(copy_root, *NO_SIGNING, "-c", "core.hooksPath=/dev/null", "-c", "core.editor=true", "rebase",
                      "--continue", check=False)
        record_change(copy_root)
        code, output = gate_commit(copy_root, "-m", "a record after the rebase")
        shutil.rmtree(copy_root)
        return ("gate, neighbour: the rebase route: the branch rebased onto the other line, its entry renumbered"
                " after the other's, goes through", rebased.returncode == 0 and code == 0,
                rebased.stdout + rebased.stderr + output)

    attempt("gate, neighbour: the rebase route: the branch rebased onto the other line, its entry renumbered after"
            " the other's, goes through", inline_test_the_rebase_route)

    def inline_test_stale_branch_after_a_tightened_check():
        copy_root = copy_repository(repository_root)
        main_branch = git(copy_root, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
        largest = max(os.path.getsize(os.path.join(folder, name))
                      for folder, _, names in os.walk(copy_root) if "/.git" not in folder + "/"
                      for name in names if name.endswith(TEXT_ENDINGS)
                      and os.path.getsize(os.path.join(folder, name)) < 100_000)
        limit = largest + 1000
        if limit + 500 >= 100_000:
            raise AssertionError("no room below 100,000 bytes to plant a file the tightened check alone refuses")
        git(copy_root, "checkout", "-q", "-b", "stale")
        reviewed_change(copy_root)
        gate_commit(copy_root, "-m", "a reviewed rule on a branch")
        git(copy_root, "checkout", "-q", main_branch)
        edit(copy_root, os.path.join(SCRIPTS, "run_all_checks.py"), replace_once("LARGE_TEXT = 100_000",
                                                                                 f"LARGE_TEXT = {limit}"))
        git(copy_root, "add", "-A")
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed")
        code_tightened, output_tightened = gate_commit(copy_root, "-m", "a check tightened on the main line")
        merge_without_the_gate(copy_root, "-m", "Merge pull request 2", "stale")
        merged = git(copy_root, "rev-parse", "HEAD").stdout.strip()
        write(copy_root, "kept-cases/runs/planted-large.md", "word " * ((limit + 500) // 5))
        commit_skipping_the_gate(copy_root, "a large file added on GitHub")
        record_change(copy_root)
        code, output = gate_commit(copy_root, "-m", "a record")
        shutil.rmtree(copy_root)
        return ("gate: a stale approved branch merged on GitHub after a check was tightened on the main line: the"
                " tightened check is used", code_tightened == 0 and code != 0 and merged[:9] in output
                and "planted-large.md: a large text file" in output, output_tightened + output)

    attempt("gate: a stale approved branch merged on GitHub after a check was tightened on the main line",
            inline_test_stale_branch_after_a_tightened_check)

    def inline_test_route_after_a_conflicted_github_merge():
        copy_root = copy_repository(repository_root)
        main_branch = git(copy_root, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
        wrong_rule = ('    if "ZZZ" in story_text:\n'
                      '        problems.append(f"{PROJECT_STORY}: the planted wrong rule refuses ZZZ")\n')
        anchor = "    earlier_text = committed_text(git_root, against, PROJECT_STORY)\n    if earlier_text is not None and"
        edit(copy_root, os.path.join(SCRIPTS, "check_records.py"), replace_once(anchor, wrong_rule + anchor))
        git(copy_root, "add", "-A")
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed")
        steps = [gate_commit(copy_root, "-m", "a wrong check, approved")]
        git(copy_root, "checkout", "-q", "-b", "session-y")
        add_log_entry(copy_root, True, "Session Y's entry.")
        git(copy_root, "add", "-A")
        steps.append(gate_commit(copy_root, "-m", "an entry on a branch"))
        git(copy_root, "checkout", "-q", main_branch)
        add_log_entry(copy_root, True, "The main line's entry.")
        git(copy_root, "add", "-A")
        steps.append(gate_commit(copy_root, "-m", "an entry on the main line"))
        last_approved = git(copy_root, "rev-parse", "HEAD").stdout.strip()
        merge_without_the_gate(copy_root, "-m", "Merge pull request 3", "session-y")
        keep_one_side_and_renumber_the_other(copy_root, ":2:", "Session Y's entry.")
        finish_without_the_gate(copy_root)
        record_change(copy_root, "ZZZ, the owner's word")
        commit_skipping_the_gate(copy_root, "the owner's edit on GitHub")

        def correct_the_check():
            edit(copy_root, os.path.join(SCRIPTS, "check_records.py"), replace_once(wrong_rule, ""))
            git(copy_root, "add", "-A")
            fill_receipt(copy_root, "theory-checker", "lead agent", "passed")

        correct_the_check()
        code, output = gate_commit(copy_root, "-m", "the check corrected on the main line's tip")
        ready = all(code_ == 0 for code_, _ in steps)
        first = ("gate: after a merge made on GitHub with a conflict, a check corrected on the main line's tip is"
                 " judged by the wrong check", ready and code != 0 and "refuses ZZZ" in output,
                 "".join(output_ for _, output_ in steps) + output)
        git(copy_root, "reset", "-q", "--hard")
        git(copy_root, "checkout", "-q", "-b", "fix", last_approved)
        correct_the_check()
        code, output = gate_commit(copy_root, "-m", "the check corrected, on a branch from the last approved commit")
        merge = git(copy_root, *NO_SIGNING, "merge", "--no-ff", "-m", "the main line merged in", main_branch,
                    check=False)
        second = ("gate, neighbour: the check corrected on a branch from the last approved commit, then the main"
                  " line merged into it through the gate", ready and code == 0 and merge.returncode == 0,
                  output + merge.stdout + merge.stderr)
        shutil.rmtree(copy_root)
        return [first, second]

    attempt("gate: after a merge made on GitHub with a conflict, a check corrected on the main line's tip is judged"
            " by the wrong check", inline_test_route_after_a_conflicted_github_merge)

    def inline_test_windows_line_endings():
        source = copy_repository(repository_root)
        clone_root = tempfile.mkdtemp(prefix="workshop-test-")
        git(os.path.dirname(clone_root), "clone", "-q", "-c", "core.autocrlf=true", source, clone_root)
        with open(os.path.join(clone_root, ".githooks", "pre-commit"), "rb") as hook:
            windows_endings = b"\r\n" in hook.read()
        record_change(clone_root)
        code, output = gate_commit(clone_root, "-m", "a record")
        shutil.rmtree(source)
        shutil.rmtree(clone_root)
        return ("gate, neighbour: a copy that turns line endings into Windows ones still runs the gate",
                not windows_endings and code == 0 and "All checks passed" in output, output)

    attempt("gate, neighbour: a copy that turns line endings into Windows ones still runs the gate",
            inline_test_windows_line_endings)

    def inline_test_recheck_allowed_record():
        copy_root = copy_repository(repository_root)
        record = "kept-cases/runs/2026-09-24-before-entry-27.md"
        if not os.path.exists(os.path.join(copy_root, record)):
            raise AssertionError(f"{record} is not in the copy")
        git(copy_root, "rm", "-q", record)
        commit_skipping_the_gate(copy_root, "the large record removed")
        git(copy_root, "checkout", "HEAD~1", "--", record)
        commit_skipping_the_gate(copy_root, "the large record put back")
        code, output = run(copy_root, os.path.join(SCRIPTS, "recheck_commits.py"), "--root", copy_root)
        shutil.rmtree(copy_root)
        return ("recheck, neighbour: the one large record allowed by name is not noted as a book file",
                "looks like a book" not in output and "rechecked 2 commit(s)" in output, output)

    attempt("recheck, neighbour: the one large record allowed by name is not noted as a book file",
            inline_test_recheck_allowed_record)

    def before_the_gate_and_the_build():
        """A copy whose first commit lacks the gate script (from before the gate), and the gate brought in on the
        branch 'build' through the gate itself; returns the copy, the main line's name and the first commit."""
        copy_root = copy_repository(repository_root, stamped=False)
        main_branch = git(copy_root, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
        gate_script = os.path.join(copy_root, SCRIPTS, "check_commit.py")
        with open(gate_script, encoding="utf-8") as script:
            kept = script.read()
        git(copy_root, "rm", "-q", "--cached", os.path.join(SCRIPTS, "check_commit.py"))
        git(copy_root, *NO_SIGNING, "commit", "-q", "--amend", "-m", "the workshop before the gate")
        before = git(copy_root, "rev-parse", "HEAD").stdout.strip()
        git(copy_root, "checkout", "-q", "-b", "build")
        with open(gate_script, "w", encoding="utf-8") as script:
            script.write(kept)
        git(copy_root, "add", "-A")
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed")
        code, output = gate_commit(copy_root, "-m", "the gate brought in")
        if code != 0:
            raise AssertionError(f"the gate could not be brought in: {output}")
        git(copy_root, "checkout", "-q", main_branch)
        return copy_root, main_branch, before

    def inline_test_branch_from_before_the_gate():
        copy_root, main_branch, before = before_the_gate_and_the_build()
        merge_without_the_gate(copy_root, "-m", "Merge pull request 1", "build")
        git(copy_root, "checkout", "-q", "-b", "old", before)
        edit(copy_root, PROJECT_STORY, replace_once("5. **", "5. **Rewritten. "))
        commit_skipping_the_gate(copy_root, "an old branch from before the gate")
        git(copy_root, "checkout", "-q", main_branch)
        merge_without_the_gate(copy_root, "-m", "Merge the old branch", "old")
        record_change(copy_root)
        code, output = gate_commit(copy_root, "-m", "a record")
        shutil.rmtree(copy_root)
        return ("gate: a branch from before the gate, merged on GitHub, is judged: its rewrite of an old entry stops"
                " the next commit", code != 0 and "log entry 5 has been changed" in output, output)

    attempt("gate: a branch from before the gate, merged on GitHub, is judged", inline_test_branch_from_before_the_gate)

    def inline_test_two_check_changes_joined():
        copy_root = copy_repository(repository_root)
        main_branch = git(copy_root, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
        codes = []
        for branch, script in (("checks-a", os.path.join(ADD_SOURCE_SCRIPTS, "check_maps.py")),
                               ("checks-b", os.path.join(SCRIPTS, "check_owner_quotes.py"))):
            git(copy_root, "checkout", "-q", "-b", branch, main_branch)
            edit(copy_root, script, lambda text: text + f"\n# a reviewed comment on {branch}\n")
            git(copy_root, "add", "-A")
            fill_receipt(copy_root, "theory-checker", "lead agent", "passed")
            codes.append(gate_commit(copy_root, "-m", f"a reviewed check change on {branch}")[0])
        git(copy_root, "checkout", "-q", main_branch)
        merge_without_the_gate(copy_root, "-m", "Merge pull request 1", "checks-a")
        first = git(copy_root, "rev-parse", "HEAD").stdout.strip()
        merge_without_the_gate(copy_root, "-m", "Merge pull request 2", "checks-b")
        second = git(copy_root, "rev-parse", "HEAD").stdout.strip()
        asking = (f"import sys; sys.path.insert(0, {os.path.join(copy_root, SCRIPTS)!r}); import check_commit; "
                  f"print(check_commit.Approval({copy_root!r}).last_approved_commit())")
        found = subprocess.run([sys.executable, "-c", asking], capture_output=True, text=True, check=False,
                               cwd=copy_root)
        shutil.rmtree(copy_root)
        output = found.stdout + found.stderr
        return [("gate: a merge made on GitHub joining two lines that both changed the checks is not counted as"
                 " approved", codes == [0, 0] and second not in output and "Error" not in output, output),
                ("gate, neighbour: a merge made on GitHub bringing one line's check change is counted as approved",
                 codes == [0, 0] and first in output, output)]

    attempt("gate: a merge made on GitHub joining two lines that both changed the checks is not counted as approved",
            inline_test_two_check_changes_joined)

    def inline_test_old_git():
        copy_root = copy_repository(repository_root)
        main_branch = git(copy_root, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
        for branch, wording in (("x", "- A rule worded one way."), ("y", "- A rule worded another way.")):
            git(copy_root, "checkout", "-q", "-b", branch, main_branch)
            add_to_traps("plot", wording)(copy_root)
            git(copy_root, "add", "-A")
            fill_receipt(copy_root, "theory-checker", "lead agent", "passed")
            gate_commit(copy_root, "-m", f"a reviewed rule on {branch}")
        git(copy_root, *NO_SIGNING, "merge", "-q", "--no-ff", "-m", "merge x", "x", check=False)
        edit(copy_root, ".claude/skills/plot/SKILL.md",
             lambda text: re.sub(r"<<<<<<< [^\n]*\n.*?>>>>>>> [^\n]*\n", "- A third wording, never reviewed.\n",
                                 text, count=1, flags=re.S))
        git(copy_root, "add", "-A")
        stand_in = tempfile.mkdtemp(prefix="workshop-old-git-")
        LEFT_OVER.append(stand_in)
        with open(os.path.join(stand_in, "git"), "w", encoding="utf-8") as fake:
            fake.write('#!/bin/sh\nfor word in "$@"; do\n  if [ "$word" = "--write-tree" ]; then\n'
                       '    echo "fatal: unknown option --write-tree" >&2; exit 128\n  fi\ndone\n'
                       f'exec {shutil.which("git")} "$@"\n')
        os.chmod(os.path.join(stand_in, "git"), 0o755)
        # the gate is run as git would run it, but directly: git puts its own folder first on the hooks' search
        # path, which would hide the stand-in
        result = subprocess.run(["sh", os.path.join(".githooks", "pre-commit")], cwd=copy_root, capture_output=True,
                                text=True, check=False,
                                env={**os.environ, "PATH": stand_in + os.pathsep + os.environ.get("PATH", "")})
        shutil.rmtree(copy_root)
        output = result.stdout + result.stderr
        return ("gate: with a git that cannot do merge-tree --write-tree, a merge's hand-made change still needs its"
                " receipt", result.returncode != 0 and "no review receipt" in output, output)

    attempt("gate: with a git that cannot do merge-tree --write-tree, a merge's hand-made change still needs its"
            " receipt", inline_test_old_git)

    def inline_test_changed_gate_tests_run():
        name = ("gate: a commit that breaks test_the_gate.py is stopped by the changed planted-fault test (outside"
                " the test's own copies)")
        if ALREADY_INSIDE:
            NOT_RUN.append(name + ": this run is itself inside the planted-fault test")
            return None
        copy_root = copy_repository(repository_root, prefix="workshop-plain-")
        edit(copy_root, os.path.join(SCRIPTS, "test_the_gate.py"), lambda text: text + "\nthis line is not python\n")
        git(copy_root, "add", "-A")
        fill_receipt(copy_root, "theory-checker", "lead agent", "passed")
        git(copy_root, "config", "core.hooksPath", ".githooks")
        environment = {name_: value for name_, value in os.environ.items()
                       if name_ != "WORKSHOP_INSIDE_PLANTED_FAULT_TEST"}
        result = subprocess.run(["git", *NO_SIGNING, "commit", "-q", "-m", "a broken gate test"], cwd=copy_root,
                                capture_output=True, text=True, env=environment, check=False)
        output = result.stdout + result.stderr
        shutil.rmtree(copy_root, ignore_errors=True)
        return (name, result.returncode != 0 and "FAILED    the changed planted-fault test" in output, output)

    attempt("gate: a commit that breaks test_the_gate.py is stopped by the changed planted-fault test",
            inline_test_changed_gate_tests_run)

    return results
