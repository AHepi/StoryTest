#!/usr/bin/env python3
"""Tests for stages/09-revision/scripts/apply_exact_edits.py.

Verifies normal exact-edit application and refusal guards, including planted
faults for every review finding:
- unique match succeeds and writes a new file without touching the source;
- zero matches, ambiguous (>1) matches, and no-op edits (find == replace) fail
  without writing target;
- match='all' replaces every occurrence, enforces expected_count, prints
  explicit zero-repeat status (including NOT RUN when disabled), and catches
  reintroduced occurrences;
- existing target file, target == source, and dangling symlink targets are
  refused (never overwrites);
- literal sacred_lines match story text only (refusing Verify-section echo and
  appended-text bypasses), plus explicit substring mode and first/last line vs
  reference file;
- untouched_sections preserves duplicate headings (never overwrites via dict),
  matches exact headings before prefixes (## Chapter 1 vs ## Chapter 10), and
  supports reference files;
- --count --section reports matched headings and exits non-zero on 0 matches;
- story-text extraction handles drafts without ## headings (keeping full-italic
  story paragraphs and bold lines), header notes with external [from: ...]
  markers, and chapters titled '## Verify the Alibi';
- relative paths prefer order.json's directory over CWD; bad JSON/regex/types
  exit 1 cleanly without tracebacks; --dry-run writes nothing; --help shows
  the edit-order schema.
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "apply_exact_edits.py")

SAMPLE_DRAFT = """# Sample Story: draft 1

*Brought in at stage 01. [from: 01 step 3; request]*

## 1. Opening

First story line stays exact.

She walked across the yard. The wind rattled the gate. [from: 06 step 3]

---

## 2. Middle

He said "wait" twice and he said "wait" again.

The watchman checked the lock. The watchman checked the lock again.

Last story line stays exact.

## Verify

- Against the brief: agrees.
"""


def run_cli(*args, cwd=None):
    return subprocess.run(
        [sys.executable, SCRIPT, *args],
        capture_output=True,
        text=True,
        check=False,
        cwd=cwd,
    )


class TestApplyExactEdits(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.src = os.path.join(self.tmpdir.name, "draft-v1.md")
        with open(self.src, "w", encoding="utf-8") as handle:
            handle.write(SAMPLE_DRAFT)

    def tearDown(self):
        self.tmpdir.cleanup()

    def write_order(self, order, folder=None):
        directory = folder or self.tmpdir.name
        path = os.path.join(directory, "order.json")
        with open(path, "w", encoding="utf-8") as handle:
            json.dump(order, handle)
        return path

    def test_unique_and_all_edits_succeed_with_checks_and_zero_repeat_receipt(self):
        tgt = os.path.join(self.tmpdir.name, "draft-v2.md")
        order_path = self.write_order(
            {
                "source": self.src,
                "target": tgt,
                "edits": [
                    {
                        "id": "F1",
                        "find": "The watchman checked the lock.",
                        "replace": "The guard tried the latch.",
                    },
                    {
                        "id": "F2",
                        "find": '"wait"',
                        "replace": "\u201cwait\u201d",
                        "match": "all",
                        "expected_count": 2,
                    },
                ],
                "checks": {
                    "forbidden_patterns": [
                        {"pattern": '"', "label": "straight double quotes", "scope": "story"},
                        {"pattern": "TODO_LEAK", "label": "placeholder leak", "scope": "all"},
                    ],
                    "sacred_lines": [
                        "First story line stays exact.",
                        {"text": "wind rattled the gate", "match": "substring"},
                        {"file": self.src, "position": "first_story_line"},
                        {"file": self.src, "position": "last_story_line"},
                    ],
                    "untouched_sections": [
                        "## 1. Opening",
                        {"section": "## 1. Opening", "file": self.src},
                    ],
                },
            }
        )
        res = run_cli("--edits", order_path)
        self.assertEqual(res.returncode, 0, msg=res.stderr + res.stdout)
        self.assertTrue(os.path.exists(tgt))
        self.assertIn("STATUS: WRITTEN", res.stdout)
        self.assertIn("- F1: mode=one, count=1", res.stdout)
        self.assertIn("zero-repeat=0 remaining", res.stdout)
        self.assertIn("Diff (source -> target):", res.stdout)
        with open(tgt, "r", encoding="utf-8") as handle:
            content = handle.read()
        self.assertIn("The guard tried the latch.", content)
        self.assertNotIn('"wait"', content)
        with open(self.src, "r", encoding="utf-8") as handle:
            self.assertEqual(handle.read(), SAMPLE_DRAFT)

    def test_dry_run_writes_nothing(self):
        tgt = os.path.join(self.tmpdir.name, "draft-v2.md")
        order_path = self.write_order(
            {
                "source": self.src,
                "target": tgt,
                "edits": [{"id": "F1", "find": "the yard", "replace": "the lane"}],
            }
        )
        res = run_cli("--edits", order_path, "--dry-run")
        self.assertEqual(res.returncode, 0, msg=res.stderr + res.stdout)
        self.assertIn("STATUS: DRY RUN", res.stdout)
        self.assertFalse(os.path.exists(tgt))

    def test_refuses_zero_matches_and_ambiguous_and_noop(self):
        tgt = os.path.join(self.tmpdir.name, "draft-v2.md")
        for edit, expected_err in [
            ({"id": "F1", "find": "nonexistent sentence", "replace": "x"}, "matched 0 places"),
            ({"id": "F1", "find": "The watchman", "replace": "The guard"}, "matched 2 places"),
            ({"id": "F1", "find": "the yard", "replace": "the yard"}, "no-op edit refused"),
            ({"id": "F1", "find": "The watchman", "replace": "The guard", "match": "all", "expected_count": 3}, "expected 3"),
        ]:
            order_path = self.write_order({"source": self.src, "target": tgt, "edits": [edit]})
            res = run_cli("--edits", order_path)
            self.assertEqual(res.returncode, 1)
            self.assertFalse(os.path.exists(tgt))
            self.assertIn(expected_err, res.stderr)

    def test_verify_absent_disabled_prints_not_run(self):
        tgt = os.path.join(self.tmpdir.name, "draft-v2.md")
        order_path = self.write_order(
            {
                "source": self.src,
                "target": tgt,
                "edits": [
                    {"id": "F1", "find": "The watchman", "replace": "The guard", "match": "all", "verify_absent": False},
                    {"id": "F2", "find": "the yard", "replace": "the yard where The watchman waited"},
                ],
            }
        )
        res = run_cli("--edits", order_path)
        self.assertEqual(res.returncode, 0, msg=res.stderr + res.stdout)
        self.assertIn("zero-repeat=NOT RUN (disabled by order)", res.stdout)

    def test_refuses_overwrite_existing_file_and_dangling_symlink(self):
        tgt = os.path.join(self.tmpdir.name, "draft-v2.md")
        with open(tgt, "w", encoding="utf-8") as handle:
            handle.write("existing")
        order_path = self.write_order(
            {"source": self.src, "target": tgt, "edits": [{"id": "F1", "find": "the yard", "replace": "the lane"}]}
        )
        res = run_cli("--edits", order_path)
        self.assertEqual(res.returncode, 1)
        self.assertIn("already exists", res.stderr)

        symlink_tgt = os.path.join(self.tmpdir.name, "dangling-v2.md")
        outside = os.path.join(self.tmpdir.name, "nonexistent-target.md")
        os.symlink(outside, symlink_tgt)
        order_path2 = self.write_order(
            {"source": self.src, "target": symlink_tgt, "edits": [{"id": "F1", "find": "the yard", "replace": "the lane"}]}
        )
        res2 = run_cli("--edits", order_path2)
        self.assertEqual(res2.returncode, 1)
        self.assertFalse(os.path.exists(outside))
        self.assertIn("already exists", res2.stderr)

    def test_literal_sacred_line_blocks_verify_bypass_and_appended_text_bypass(self):
        tgt = os.path.join(self.tmpdir.name, "draft-v2.md")
        # Bypass attempt 1: delete sacred line from story, quote it in ## Verify.
        order1 = self.write_order(
            {
                "source": self.src,
                "target": tgt,
                "edits": [
                    {"id": "F1", "find": "Last story line stays exact.", "replace": "Rewritten ending."},
                    {"id": "F2", "find": "- Against the brief: agrees.", "replace": "- Sacred: Last story line stays exact."},
                ],
                "checks": {"sacred_lines": ["Last story line stays exact."]},
            }
        )
        res1 = run_cli("--edits", order1)
        self.assertEqual(res1.returncode, 1)
        self.assertFalse(os.path.exists(tgt))

        # Bypass attempt 2: append text onto sacred line.
        order2 = self.write_order(
            {
                "source": self.src,
                "target": tgt,
                "edits": [
                    {"id": "F1", "find": "Last story line stays exact.", "replace": "Last story line stays exact. Then he explained why."}
                ],
                "checks": {"sacred_lines": ["Last story line stays exact."]},
            }
        )
        res2 = run_cli("--edits", order2)
        self.assertEqual(res2.returncode, 1)
        self.assertFalse(os.path.exists(tgt))

    def test_untouched_sections_handles_exact_chapter_prefix_and_duplicate_headings(self):
        # Chapter 1 vs Chapter 10 must not collide.
        ch_src = os.path.join(self.tmpdir.name, "chapters.md")
        ch_tgt = os.path.join(self.tmpdir.name, "chapters-v2.md")
        with open(ch_src, "w", encoding="utf-8") as handle:
            handle.write("# Book\n\n## Chapter 1\n\nOne.\n\n## Chapter 10\n\nTen.\n")
        order_ch = self.write_order(
            {
                "source": ch_src,
                "target": ch_tgt,
                "edits": [{"id": "F1", "find": "Ten.", "replace": "Ten revised."}],
                "checks": {"untouched_sections": ["## Chapter 1"]},
            }
        )
        res_ch = run_cli("--edits", order_ch)
        self.assertEqual(res_ch.returncode, 0, msg=res_ch.stderr + res_ch.stdout)
        self.assertIn("untouched section '## Chapter 1' (vs source): identical", res_ch.stdout)

        # Count --section "## Chapter 1" counts ONLY Chapter 1 (1 word), not Chapter 10.
        res_cnt = run_cli("--count", ch_src, "--section", "## Chapter 1")
        self.assertEqual(res_cnt.returncode, 0, msg=res_cnt.stderr)
        self.assertIn("[sections: ## Chapter 1]: 1 words, 1 paragraphs", res_cnt.stdout)

        # Unmatched --section must fail with exit 1.
        res_missing = run_cli("--count", ch_src, "--section", "## Chapter 99")
        self.assertEqual(res_missing.returncode, 1)
        self.assertIn("matched 0 sections", res_missing.stderr)

        # Duplicate headings must NOT silently pass when the first is mutated.
        dup_src = os.path.join(self.tmpdir.name, "dup.md")
        dup_tgt = os.path.join(self.tmpdir.name, "dup-v2.md")
        with open(dup_src, "w", encoding="utf-8") as handle:
            handle.write("# Book\n\n## Interlude\n\nFirst interlude.\n\n## Interlude\n\nSecond interlude.\n")
        order_dup = self.write_order(
            {
                "source": dup_src,
                "target": dup_tgt,
                "edits": [{"id": "F1", "find": "First interlude.", "replace": "Mutated interlude."}],
                "checks": {"untouched_sections": ["## Interlude"]},
            }
        )
        res_dup = run_cli("--edits", order_dup)
        self.assertEqual(res_dup.returncode, 1)
        self.assertFalse(os.path.exists(dup_tgt))
        self.assertIn("matched 2 section(s)", res_dup.stderr)

    def test_post_edit_absent_check_catches_reintroduced_phrase(self):
        tgt = os.path.join(self.tmpdir.name, "draft-v2.md")
        order_path = self.write_order(
            {
                "source": self.src,
                "target": tgt,
                "edits": [
                    {"id": "F1", "find": "The watchman", "replace": "The guard", "match": "all"},
                    {"id": "F2", "find": "the yard", "replace": "the yard where The watchman stood"},
                ],
            }
        )
        res = run_cli("--edits", order_path)
        self.assertEqual(res.returncode, 1)
        self.assertFalse(os.path.exists(tgt))
        self.assertIn("remaining occurrence(s)", res.stderr)

    def test_story_extraction_no_h2_external_marker_and_verify_chapter_title(self):
        # Draft with no ## headings, header note with external marker, italic story line, bold slugline.
        path = os.path.join(self.tmpdir.name, "no-h2.md")
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(
                "# Short Piece\n\n"
                "*Revised at stage 09.* [from: 09 step 4]\n\n"
                "**EXT. HARBOUR - NIGHT**\n\n"
                "*Secret italic paragraph.*\n\n"
                "Plain closing line.\n"
            )
        res = run_cli("--count", path)
        self.assertEqual(res.returncode, 0, msg=res.stderr)
        # 3 story paragraphs: bold slugline (4w) + italic para (3w) + closing (3w) = 10w
        self.assertIn("10 words, 3 paragraphs", res.stdout)
        self.assertIn("italic runs: 1", res.stdout)

        # Forbidden italics must catch *Secret italic paragraph.* even with no ## headings.
        tgt = os.path.join(self.tmpdir.name, "no-h2-v2.md")
        order = self.write_order(
            {
                "source": path,
                "target": tgt,
                "edits": [{"id": "F1", "find": "Plain closing line.", "replace": "Still plain closing line."}],
                "checks": {
                    "forbidden_patterns": [
                        {"pattern": r"(?<!\*)\*(?!\s)[^*\n]+(?<!\s)\*(?!\*)", "regex": True, "label": "italics", "scope": "story"}
                    ]
                },
            }
        )
        res_forb = run_cli("--edits", order)
        self.assertEqual(res_forb.returncode, 1)
        self.assertIn("Forbidden pattern 'italics'", res_forb.stderr)

        # Chapter titled '## Verify the Alibi' must NOT be truncated.
        alibi = os.path.join(self.tmpdir.name, "alibi.md")
        with open(alibi, "w", encoding="utf-8") as handle:
            handle.write("# Mystery\n\n## Verify the Alibi\n\nThree story words.\n\n## Verify\n\n- Agrees.\n")
        res_alibi = run_cli("--count", alibi)
        self.assertEqual(res_alibi.returncode, 0, msg=res_alibi.stderr)
        self.assertIn("3 words, 1 paragraphs", res_alibi.stdout)

    def test_relative_paths_prefer_order_dir_over_cwd_hijack(self):
        cwd_dir = os.path.join(self.tmpdir.name, "cwd_decoy")
        ord_dir = os.path.join(self.tmpdir.name, "order_dir")
        os.makedirs(cwd_dir)
        os.makedirs(ord_dir)
        with open(os.path.join(cwd_dir, "draft-v1.md"), "w", encoding="utf-8") as handle:
            handle.write("## 1. Decoy\n\nThe decoy yard.\n")
        with open(os.path.join(ord_dir, "draft-v1.md"), "w", encoding="utf-8") as handle:
            handle.write("## 1. Real\n\nThe real yard.\n")
        order_path = self.write_order(
            {"source": "draft-v1.md", "target": "draft-v2.md", "edits": [{"id": "F1", "find": "real yard", "replace": "real lane"}]},
            folder=ord_dir,
        )
        res = run_cli("--edits", order_path, cwd=cwd_dir)
        self.assertEqual(res.returncode, 0, msg=res.stderr + res.stdout)
        self.assertTrue(os.path.exists(os.path.join(ord_dir, "draft-v2.md")))
        self.assertFalse(os.path.exists(os.path.join(cwd_dir, "draft-v2.md")))

    def test_bad_inputs_return_clean_errors_without_traceback(self):
        tgt = os.path.join(self.tmpdir.name, "draft-v2.md")
        bad_orders = [
            {"source": self.src, "target": tgt, "edits": [{"id": "F1", "find": "the yard", "replace": "x", "expected_count": True}]},
            {"source": self.src, "target": tgt, "edits": ["not-a-dict"]},
            {
                "source": self.src,
                "target": tgt,
                "edits": [{"id": "F1", "find": "the yard", "replace": "the lane"}],
                "checks": {"forbidden_patterns": [{"pattern": "[bad", "regex": True, "label": "bad"}]},
            },
            {
                "source": self.src,
                "target": tgt,
                "edits": [{"id": "F1", "find": "the yard", "replace": "the lane"}],
                "checks": {"sacred_lines": [{"position": "last_story_line"}]},
            },
        ]
        for bad in bad_orders:
            order_path = self.write_order(bad)
            res = run_cli("--edits", order_path)
            self.assertEqual(res.returncode, 1)
            self.assertNotIn("Traceback", res.stderr)

    def test_help_includes_edit_order_schema(self):
        res = run_cli("--help")
        self.assertEqual(res.returncode, 0)
        self.assertIn("Edit-order JSON format:", res.stdout)
        self.assertIn("untouched_sections", res.stdout)


if __name__ == "__main__":
    unittest.main()
