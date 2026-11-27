#!/usr/bin/env python3
"""Apply exact logged edits to a stage output and measure prose story text only.

This script replaces whole-file rewriting for local draft edits in stage 09
and provides one shared story-text counter for stages 01 and 09 (prose drafts).

What it guarantees (by script, without trusting an agent's summary):
1. Never overwrites an existing file or symlink: refuses if the target path
   exists (including dangling symlinks) or resolves to the same file as source.
2. Every edit must carry an id (matching its revision-log row), refuse no-op
   edits (find == replace), and match exactly one place by default
   ("match": "one"); zero matches or more than one match stops the run before
   anything is written.
3. For "match": "all", refuses on zero matches, checks expected_count if given,
   and checks that zero stray occurrences of the replaced text remain at the
   end (reporting the zero-repeat status explicitly in the receipt, including
   NOT RUN if disabled or if replacement still contains find).
4. Runs script checks on the resulting text before writing:
   - forbidden_patterns (literal or regex, on story text or the whole file);
   - sacred_lines (exact story line or paragraph match by default, never
     matched inside '## Verify' or header notes; or first/last story line
     compared verbatim against a reference file such as draft-v1);
   - untouched_sections (markdown '##' sections that must remain identical to
     the source file or a named reference file, preserving duplicate headings
     and matching exact headings before boundary-aware prefixes).
5. Prints a complete receipt: applied edits with line numbers and zero-repeat
   status, check results, story-text-only counts (excluding markdown headings,
   leading file-header italic notes, [from: ...] markers, scene breaks, and
   trailing '## Verify' sections), and the line-by-line diff.

Usage:
  python3 stages/09-revision/scripts/apply_exact_edits.py --edits order.json [--dry-run] [--long-para 60] [--no-diff]
  python3 stages/09-revision/scripts/apply_exact_edits.py --count file1.md [file2.md ...] [--long-para 60] [--section "## 5."]
"""
import argparse
import difflib
import json
import os
import re
import sys

HEADING_LINE = re.compile(r"^#{1,6}\s+")
H2_LINE = re.compile(r"^##\s+")
VERIFY_HEADING = re.compile(r"^##\s+Verify(?:\s*\[from:[^\]]*\])?\s*$", flags=re.IGNORECASE)
SCENE_BREAK = re.compile(r"^\s*(?:[-*_]\s*){3,}$")
INLINE_MARKER = re.compile(r"\s*\[from:[^\]]*\]")

HELP_EPILOG = """Edit-order JSON format:
{
  "source": "draft-v1.md",
  "target": "draft-v2.md",
  "edits": [
    {"id": "F1", "find": "exact old text", "replace": "new text"},
    {"id": "F2", "find": "old term", "replace": "new term", "match": "all", "expected_count": 3}
  ],
  "checks": {
    "forbidden_patterns": [
      {"pattern": "\\"", "regex": false, "scope": "story", "label": "straight double quotes"}
    ],
    "sacred_lines": [
      "Exact story line or paragraph that must remain verbatim.",
      {"text": "Substring if explicitly needed", "match": "substring"},
      {"file": "draft-v1.md", "position": "last_story_line"}
    ],
    "untouched_sections": [
      "## 1. Opening",
      {"section": "## 2.", "file": "draft-v1.md"}
    ]
  }
}
"""


def read_text(path):
    with open(path, "r", encoding="utf-8", newline="") as handle:
        return handle.read()


def split_sections_by_h2(text):
    """Return ordered list of (heading_line_or_None, body_text) split on '## ' headings."""
    lines = text.splitlines(keepends=True)
    sections = []
    current_heading = None
    current_lines = []
    for line in lines:
        if H2_LINE.match(line):
            sections.append((current_heading, "".join(current_lines)))
            current_heading = line.strip()
            current_lines = [line]
        else:
            current_lines.append(line)
    sections.append((current_heading, "".join(current_lines)))
    return sections


def heading_matches_selector(heading, selector):
    """Return 'exact', 'prefix', or None for a markdown '##' heading against a selector."""
    sel = selector.strip()
    if heading == sel:
        return "exact"
    if not heading.startswith(sel):
        return None
    if len(heading) == len(sel):
        return "exact"
    next_char = heading[len(sel)]
    # Boundary-aware prefix: avoid '## Chapter 1' matching '## Chapter 10' or '## Act I' matching '## Act II'.
    if sel[-1].isalnum() and next_char.isalnum():
        return None
    return "prefix"


def match_h2_sections(sections, selector):
    """Find matching (heading, body) tuples from split_sections_by_h2 output.

    Exact heading matches take precedence over boundary-aware prefix matches,
    and duplicate headings are all preserved so ambiguity is caught.
    """
    exact = []
    prefix = []
    for heading, body in sections:
        if heading is None:
            continue
        kind = heading_matches_selector(heading, selector)
        if kind == "exact":
            exact.append((heading, body))
        elif kind == "prefix":
            prefix.append((heading, body))
    return exact if exact else prefix


def is_single_asterisk_italic(text):
    """True for '*...*' italic notes, False for '**...**' bold lines."""
    return (
        len(text) >= 2
        and text.startswith("*")
        and text.endswith("*")
        and not text.startswith("**")
        and not text.endswith("**")
    )


def extract_story_paragraphs(text, section_prefixes=None):
    """Return (paragraphs, matched_headings) for story text only.

    Skips markdown headings, leading file-header italic notes, italic workshop
    notes with [from: ...] markers, standalone marker lines, scene breaks, and
    any trailing '## Verify' section.

    Each paragraph entry is (start_line, cleaned_paragraph_text, cleaned_lines)
    where start_line is 1-indexed and cleaned_lines holds each non-empty line in
    that paragraph with inline [from: ...] markers stripped.
    """
    lines = text.splitlines()
    # Drop trailing ## Verify section if present.
    story_end = len(lines)
    for idx, line in enumerate(lines):
        if VERIFY_HEADING.match(line):
            story_end = idx
            break
    lines = lines[:story_end]

    # When section filtering is requested, decide which headings match using exact-first rules.
    allowed_headings = None
    matched_headings = []
    if section_prefixes is not None:
        sections = split_sections_by_h2("\n".join(lines))
        allowed_headings = set()
        for sel in section_prefixes:
            for heading, _ in match_h2_sections(sections, sel):
                allowed_headings.add(heading)
                if heading not in matched_headings:
                    matched_headings.append(heading)

    seen_story_content = False
    in_selected_section = section_prefixes is None
    paragraphs = []
    current_lines = []
    current_start = None

    def flush():
        nonlocal current_lines, current_start
        if current_lines:
            cleaned_lines = [INLINE_MARKER.sub("", part.strip()).strip() for part in current_lines]
            cleaned_lines = [part for part in cleaned_lines if part]
            joined = " ".join(cleaned_lines).strip()
            if joined:
                paragraphs.append((current_start, joined, cleaned_lines))
            current_lines = []
            current_start = None

    for idx, raw in enumerate(lines, start=1):
        stripped = raw.strip()
        if not stripped:
            flush()
            continue

        if H2_LINE.match(stripped):
            flush()
            seen_story_content = True
            if section_prefixes is not None:
                in_selected_section = stripped in allowed_headings
            continue

        if HEADING_LINE.match(stripped):
            flush()
            continue

        if not in_selected_section:
            continue

        if SCENE_BREAK.match(stripped):
            flush()
            continue

        # Strip inline marker to detect workshop italic notes with markers inside or right after '*'.
        without_marker = INLINE_MARKER.sub("", stripped).strip()
        has_marker = "[from:" in stripped
        if not without_marker:
            flush()
            continue

        if (not seen_story_content and is_single_asterisk_italic(without_marker)) or (
            has_marker and is_single_asterisk_italic(without_marker)
        ):
            flush()
            continue

        seen_story_content = True
        if current_start is None:
            current_start = idx
        current_lines.append(stripped)

    flush()
    return paragraphs, matched_headings


def count_story_text(text, long_para=60, section_prefixes=None):
    paragraphs, matched_headings = extract_story_paragraphs(text, section_prefixes=section_prefixes)
    para_word_counts = [len(p.split()) for _, p, _ in paragraphs]
    total_words = sum(para_word_counts)
    total_paras = len(para_word_counts)
    mean_words = (total_words / total_paras) if total_paras else 0.0
    long_count = sum(1 for count in para_word_counts if count >= long_para)
    story_joined = "\n".join(p for _, p, _ in paragraphs)
    straight_double_quotes = story_joined.count('"')
    italic_runs = len(re.findall(r"(?<!\*)\*(?!\s)[^*\n]+(?<!\s)\*(?!\*)", story_joined))
    return {
        "words": total_words,
        "paragraphs": total_paras,
        "mean_words_per_paragraph": round(mean_words, 1),
        "long_paragraphs": long_count,
        "long_para_cutoff": long_para,
        "straight_double_quotes": straight_double_quotes,
        "asterisk_italic_runs": italic_runs,
        "matched_headings": matched_headings,
    }


def line_number_at_offset(text, offset):
    return text.count("\n", 0, offset) + 1


def find_all_offsets(text, needle):
    offsets = []
    start = 0
    while True:
        pos = text.find(needle, start)
        if pos == -1:
            break
        offsets.append(pos)
        start = pos + len(needle)
    return offsets


def apply_edits_in_memory(source_text, edits):
    """Apply ordered exact edits sequentially; return (new_text, applied_records, errors)."""
    current = source_text
    records = []
    errors = []
    absent_checks = []

    if not isinstance(edits, list) or not edits:
        return current, records, ["Edit order must include a non-empty 'edits' list."]

    for index, edit in enumerate(edits, start=1):
        if not isinstance(edit, dict):
            errors.append(f"Edit #{index}: must be a JSON object.")
            continue
        edit_id = edit.get("id")
        find_text = edit.get("find")
        replace_text = edit.get("replace")
        match_mode = edit.get("match", "one")
        expected_count = edit.get("expected_count")

        if not isinstance(edit_id, str) or not edit_id.strip():
            errors.append(f"Edit #{index}: missing non-empty 'id'.")
            continue
        if not isinstance(find_text, str) or not find_text:
            errors.append(f"Edit {edit_id}: 'find' must be a non-empty string.")
            continue
        if not isinstance(replace_text, str):
            errors.append(f"Edit {edit_id}: 'replace' must be a string.")
            continue
        if find_text == replace_text:
            errors.append(f"Edit {edit_id}: 'replace' is identical to 'find' (no-op edit refused).")
            continue
        if match_mode not in ("one", "all"):
            errors.append(f"Edit {edit_id}: 'match' must be 'one' or 'all', got {match_mode!r}.")
            continue
        if expected_count is not None and (
            isinstance(expected_count, bool) or not isinstance(expected_count, int) or expected_count < 1
        ):
            errors.append(f"Edit {edit_id}: 'expected_count' must be a positive integer.")
            continue
        if "verify_absent" in edit and not isinstance(edit["verify_absent"], bool):
            errors.append(f"Edit {edit_id}: 'verify_absent' must be a boolean.")
            continue

        offsets = find_all_offsets(current, find_text)
        count = len(offsets)

        if match_mode == "one":
            if expected_count is not None and expected_count != 1:
                errors.append(f"Edit {edit_id}: match='one' conflicts with expected_count={expected_count}.")
                continue
            if count == 0:
                errors.append(f"Edit {edit_id}: 'find' text matched 0 places.")
                continue
            if count > 1:
                lines = [line_number_at_offset(current, pos) for pos in offsets]
                errors.append(
                    f"Edit {edit_id}: 'find' text matched {count} places (lines {lines}); "
                    "match='one' requires a unique match."
                )
                continue
            pos = offsets[0]
            line_no = line_number_at_offset(current, pos)
            current = current[:pos] + replace_text + current[pos + len(find_text):]
            records.append(
                {"id": edit_id, "match": "one", "count": 1, "lines": [line_no], "zero_repeat": None}
            )
        else:
            if count == 0:
                errors.append(f"Edit {edit_id}: match='all' matched 0 places.")
                continue
            if expected_count is not None and count != expected_count:
                errors.append(
                    f"Edit {edit_id}: match='all' matched {count} places, expected {expected_count}."
                )
                continue
            # Record line numbers in current text at the moment this sequential edit matches.
            lines = [line_number_at_offset(current, pos) for pos in offsets]
            current = current.replace(find_text, replace_text)
            default_verify = find_text not in replace_text
            verify_flag = edit.get("verify_absent", default_verify)
            if verify_flag:
                zero_repeat_status = "pending"
                absent_checks.append((len(records), edit_id, find_text))
            elif "verify_absent" in edit and edit["verify_absent"] is False:
                zero_repeat_status = "NOT RUN (disabled by order)"
            else:
                zero_repeat_status = "NOT RUN (replacement contains find)"
            records.append(
                {
                    "id": edit_id,
                    "match": "all",
                    "count": count,
                    "lines": lines,
                    "zero_repeat": zero_repeat_status,
                }
            )

    if not errors:
        for rec_idx, edit_id, find_text in absent_checks:
            remaining = find_all_offsets(current, find_text)
            if remaining:
                rem_lines = [line_number_at_offset(current, pos) for pos in remaining]
                errors.append(
                    f"Edit {edit_id}: post-edit search found {len(remaining)} remaining "
                    f"occurrence(s) of replaced text at lines {rem_lines}."
                )
            else:
                records[rec_idx]["zero_repeat"] = "0 remaining"

    return current, records, errors


def resolve_input_path(path_value, base_dir, prefer_base_dir=True):
    """Resolve an input file path: prefer base_dir (order file's folder), then CWD."""
    if os.path.isabs(path_value):
        return path_value, False
    base_candidate = os.path.abspath(os.path.join(base_dir, path_value))
    cwd_candidate = os.path.abspath(path_value)
    if prefer_base_dir:
        if os.path.exists(base_candidate):
            return base_candidate, True
        if os.path.exists(cwd_candidate):
            return cwd_candidate, False
        return base_candidate, True
    if os.path.exists(cwd_candidate):
        return cwd_candidate, False
    return base_candidate, True


def run_deterministic_checks(source_text, target_text, checks, base_dir):
    """Run forbidden_patterns, sacred_lines, and untouched_sections checks.

    Returns (passed_notes, errors).
    """
    passed_notes = []
    errors = []
    if checks is None:
        return passed_notes, errors
    if not isinstance(checks, dict):
        return passed_notes, ["'checks' must be a JSON object."]

    story_paras, _ = extract_story_paragraphs(target_text)

    # 1. Forbidden patterns
    forbidden_list = checks.get("forbidden_patterns", [])
    if not isinstance(forbidden_list, list):
        errors.append("'forbidden_patterns' must be a list.")
        forbidden_list = []
    for idx, rule in enumerate(forbidden_list, start=1):
        if isinstance(rule, str):
            pattern = rule
            use_regex = False
            scope = "story"
            label = rule
        elif isinstance(rule, dict):
            pattern = rule.get("pattern", "")
            use_regex = bool(rule.get("regex", False))
            scope = rule.get("scope", "story")
            label = rule.get("label", pattern)
        else:
            errors.append(f"forbidden_patterns[{idx}]: must be a string or JSON object.")
            continue
        if not isinstance(pattern, str) or not pattern:
            errors.append(f"forbidden_patterns[{idx}]: empty or non-string pattern.")
            continue
        if scope not in ("story", "all"):
            errors.append(f"forbidden_patterns[{idx}] ({label}): scope must be 'story' or 'all'.")
            continue

        compiled = None
        if use_regex:
            try:
                compiled = re.compile(pattern)
            except re.error as exc:
                errors.append(f"forbidden_patterns[{idx}] ({label}): invalid regex ({exc}).")
                continue

        hits = []
        if scope == "story":
            for line_no, para, _ in story_paras:
                matched = compiled.search(para) if compiled else (pattern in para)
                if matched:
                    hits.append(line_no)
        else:
            for line_no, line in enumerate(target_text.splitlines(), start=1):
                matched = compiled.search(line) if compiled else (pattern in line)
                if matched:
                    hits.append(line_no)

        if hits:
            errors.append(
                f"Forbidden pattern '{label}' ({scope}) found on line(s) {hits[:10]}"
                + ("..." if len(hits) > 10 else "")
            )
        else:
            passed_notes.append(f"forbidden pattern '{label}' ({scope}): 0 matches")

    # 2. Sacred lines (story text only; exact paragraph or exact story line match by default)
    sacred_list = checks.get("sacred_lines", [])
    if not isinstance(sacred_list, list):
        errors.append("'sacred_lines' must be a list.")
        sacred_list = []
    story_exact_entries = set()
    for _, para, para_lines in story_paras:
        story_exact_entries.add(para)
        for line in para_lines:
            story_exact_entries.add(line)

    for idx, item in enumerate(sacred_list, start=1):
        if isinstance(item, str):
            if item.strip() in story_exact_entries:
                passed_notes.append(f"sacred line #{idx} (story exact): present verbatim")
            else:
                errors.append(
                    f"Sacred line #{idx} not present as an exact story line/paragraph: {item!r}"
                )
        elif isinstance(item, dict) and "text" in item:
            text_val = item.get("text")
            match_kind = item.get("match", "exact")
            if not isinstance(text_val, str) or not text_val:
                errors.append(f"Sacred line #{idx}: 'text' must be a non-empty string.")
                continue
            if match_kind == "exact":
                found = text_val.strip() in story_exact_entries
            elif match_kind == "substring":
                found = any(text_val in para for _, para, _ in story_paras)
            else:
                errors.append(f"Sacred line #{idx}: 'match' must be 'exact' or 'substring'.")
                continue
            if found:
                passed_notes.append(f"sacred line #{idx} (story {match_kind}): present verbatim")
            else:
                errors.append(f"Sacred line #{idx} ({match_kind}) missing from story text: {text_val!r}")
        elif isinstance(item, dict) and "file" in item:
            file_val = item.get("file")
            position = item.get("position")
            if not isinstance(file_val, str) or not file_val:
                errors.append(f"Sacred line #{idx}: 'file' must be a non-empty string.")
                continue
            ref_path, _ = resolve_input_path(file_val, base_dir)
            if not os.path.exists(ref_path):
                errors.append(f"Sacred line #{idx}: reference file not found: {ref_path}")
                continue
            ref_paras, _ = extract_story_paragraphs(read_text(ref_path))
            if not ref_paras or not story_paras:
                errors.append(f"Sacred line #{idx}: no story paragraphs found to compare.")
                continue
            if position == "first_story_line":
                expected = ref_paras[0][1]
                actual = story_paras[0][1]
            elif position == "last_story_line":
                expected = ref_paras[-1][1]
                actual = story_paras[-1][1]
            else:
                errors.append(
                    f"Sacred line #{idx}: position must be 'first_story_line' or 'last_story_line'."
                )
                continue
            if actual == expected:
                passed_notes.append(f"sacred {position} (vs {os.path.basename(ref_path)}): exact match")
            else:
                errors.append(
                    f"Sacred {position} changed (vs {os.path.basename(ref_path)}):\n"
                    f"  expected: {expected!r}\n  actual:   {actual!r}"
                )
        else:
            errors.append(
                f"Sacred line #{idx}: must be a string, {{\"text\": ...}}, or {{\"file\": ..., \"position\": ...}}."
            )

    # 3. Untouched sections (list-based to preserve duplicate headings; exact match before prefix)
    untouched_list = checks.get("untouched_sections", [])
    if not isinstance(untouched_list, list):
        errors.append("'untouched_sections' must be a list.")
        untouched_list = []
    source_sections = split_sections_by_h2(source_text)
    target_sections = split_sections_by_h2(target_text)
    for idx, item in enumerate(untouched_list, start=1):
        if isinstance(item, str):
            heading_selector = item
            ref_sections = source_sections
            ref_label = "source"
        elif isinstance(item, dict) and isinstance(item.get("section"), str) and item["section"]:
            heading_selector = item["section"]
            if "file" in item:
                if not isinstance(item["file"], str) or not item["file"]:
                    errors.append(f"Untouched section #{idx}: 'file' must be a non-empty string.")
                    continue
                ref_path, _ = resolve_input_path(item["file"], base_dir)
                if not os.path.exists(ref_path):
                    errors.append(f"Untouched section '{heading_selector}': file not found: {ref_path}")
                    continue
                ref_sections = split_sections_by_h2(read_text(ref_path))
                ref_label = os.path.basename(ref_path)
            else:
                ref_sections = source_sections
                ref_label = "source"
        else:
            errors.append(f"Untouched section #{idx}: must be a heading string or {{\"section\": ...}}.")
            continue

        ref_matches = match_h2_sections(ref_sections, heading_selector)
        tgt_matches = match_h2_sections(target_sections, heading_selector)
        if len(ref_matches) != 1:
            errors.append(
                f"Untouched section '{heading_selector}': matched {len(ref_matches)} section(s) in {ref_label}."
            )
            continue
        if len(tgt_matches) != 1:
            errors.append(
                f"Untouched section '{heading_selector}': matched {len(tgt_matches)} section(s) in target."
            )
            continue
        if ref_matches[0][1] == tgt_matches[0][1]:
            passed_notes.append(f"untouched section '{ref_matches[0][0]}' (vs {ref_label}): identical")
        else:
            errors.append(
                f"Untouched section '{ref_matches[0][0]}' differs from {ref_label}."
            )

    return passed_notes, errors


def run_edits_command(args):
    order_path = os.path.abspath(args.edits)
    base_dir = os.path.dirname(order_path)
    try:
        with open(order_path, "r", encoding="utf-8") as handle:
            order = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: could not read edit order {order_path}: {exc}", file=sys.stderr)
        return 1

    if not isinstance(order, dict):
        print("ERROR: edit order root must be a JSON object.", file=sys.stderr)
        return 1

    for required in ("source", "target", "edits"):
        if required not in order:
            print(f"ERROR: edit order missing required field '{required}'.", file=sys.stderr)
            return 1
    if not isinstance(order["source"], str) or not order["source"]:
        print("ERROR: 'source' must be a non-empty path string.", file=sys.stderr)
        return 1
    if not isinstance(order["target"], str) or not order["target"]:
        print("ERROR: 'target' must be a non-empty path string.", file=sys.stderr)
        return 1

    source_raw = order["source"]
    target_raw = order["target"]
    source_path, resolved_via_base = resolve_input_path(source_raw, base_dir, prefer_base_dir=True)
    if os.path.isabs(target_raw):
        target_path = target_raw
    elif os.path.isabs(source_raw) or resolved_via_base:
        target_path = os.path.abspath(os.path.join(base_dir, target_raw))
    else:
        target_path = os.path.abspath(target_raw)

    if not os.path.exists(source_path):
        print(f"ERROR: source file does not exist: {source_path}", file=sys.stderr)
        return 1
    if os.path.realpath(source_path) == os.path.realpath(target_path):
        print("ERROR: target path must differ from source path (never overwrite).", file=sys.stderr)
        return 1
    if os.path.lexists(target_path):
        print(
            f"ERROR: target path already exists (never overwrite earlier versions or symlinks): {target_path}",
            file=sys.stderr,
        )
        return 1

    source_text = read_text(source_path)
    target_text, applied_records, edit_errors = apply_edits_in_memory(source_text, order["edits"])
    if edit_errors:
        print("STOPPED: edit application failed; target file was NOT written.", file=sys.stderr)
        for err in edit_errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    passed_notes, check_errors = run_deterministic_checks(
        source_text, target_text, order.get("checks"), base_dir
    )
    if check_errors:
        print("STOPPED: script checks failed; target file was NOT written.", file=sys.stderr)
        for err in check_errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    if not args.dry_run:
        parent = os.path.dirname(target_path)
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(target_path, "w", encoding="utf-8", newline="") as handle:
            handle.write(target_text)

    src_counts = count_story_text(source_text, long_para=args.long_para)
    tgt_counts = count_story_text(target_text, long_para=args.long_para)
    target_bytes = len(target_text.encode("utf-8"))

    mode_label = "DRY RUN (target not written)" if args.dry_run else "WRITTEN"
    print(f"STATUS: {mode_label}")
    print(f"Source: {source_path}")
    print(f"Target: {target_path} ({target_bytes} bytes)")
    if target_bytes >= 100_000:
        print(
            "WARNING: target is 100,000 bytes or larger; split it by act, episode or chapter "
            "(stages/how-stages-work.md, section 4).",
            file=sys.stderr,
        )
    print("\nApplied edits (applied sequentially; line numbers are when each edit matched):")
    for rec in applied_records:
        line_str = ", ".join(str(n) for n in rec["lines"])
        zr = f", zero-repeat={rec['zero_repeat']}" if rec["zero_repeat"] is not None else ""
        print(f"  - {rec['id']}: mode={rec['match']}, count={rec['count']}, matched at line(s)={line_str}{zr}")

    if passed_notes:
        print("\nScript checks (all passed):")
        for note in passed_notes:
            print(f"  - {note}")

    word_delta = tgt_counts["words"] - src_counts["words"]
    para_delta = tgt_counts["paragraphs"] - src_counts["paragraphs"]
    print(f"\nStory-text-only counts (long paragraph cutoff: {args.long_para} words):")
    print(
        f"  source: {src_counts['words']} words, {src_counts['paragraphs']} paragraphs "
        f"(mean {src_counts['mean_words_per_paragraph']}, >={args.long_para}w: {src_counts['long_paragraphs']}, "
        f"straight quotes: {src_counts['straight_double_quotes']}, italic runs: {src_counts['asterisk_italic_runs']})"
    )
    print(
        f"  target: {tgt_counts['words']} words ({word_delta:+d}), {tgt_counts['paragraphs']} paragraphs ({para_delta:+d}) "
        f"(mean {tgt_counts['mean_words_per_paragraph']}, >={args.long_para}w: {tgt_counts['long_paragraphs']}, "
        f"straight quotes: {tgt_counts['straight_double_quotes']}, italic runs: {tgt_counts['asterisk_italic_runs']})"
    )

    if not args.no_diff:
        diff_lines = list(
            difflib.unified_diff(
                source_text.splitlines(keepends=True),
                target_text.splitlines(keepends=True),
                fromfile=os.path.basename(source_path),
                tofile=os.path.basename(target_path),
                n=2,
            )
        )
        print("\nDiff (source -> target):")
        if diff_lines:
            sys.stdout.writelines(diff_lines)
            if not diff_lines[-1].endswith("\n"):
                print()
        else:
            print("  (no textual difference)")

    return 0


def run_count_command(args):
    section_prefixes = args.section if args.section else None
    total_words = 0
    total_paras = 0
    total_long = 0
    total_quotes = 0
    total_italics = 0
    seen_per_selector = {sel: 0 for sel in (section_prefixes or [])}

    for path in args.count:
        if not os.path.exists(path):
            print(f"ERROR: file not found: {path}", file=sys.stderr)
            return 1
        text = read_text(path)
        if section_prefixes:
            file_sections = split_sections_by_h2(text)
            for sel in section_prefixes:
                seen_per_selector[sel] += len(match_h2_sections(file_sections, sel))
        counts = count_story_text(
            text, long_para=args.long_para, section_prefixes=section_prefixes
        )
        total_words += counts["words"]
        total_paras += counts["paragraphs"]
        total_long += counts["long_paragraphs"]
        total_quotes += counts["straight_double_quotes"]
        total_italics += counts["asterisk_italic_runs"]
        sec_note = ""
        if section_prefixes is not None:
            matched_str = ", ".join(counts["matched_headings"]) if counts["matched_headings"] else "none"
            sec_note = f" [sections: {matched_str}]"
        print(
            f"{path}{sec_note}: {counts['words']} words, {counts['paragraphs']} paragraphs, "
            f"mean {counts['mean_words_per_paragraph']}, >={args.long_para}w: {counts['long_paragraphs']}, "
            f"straight quotes: {counts['straight_double_quotes']}, italic runs: {counts['asterisk_italic_runs']}"
        )

    if section_prefixes:
        unmatched = [sel for sel, count in seen_per_selector.items() if count == 0]
        if unmatched:
            for sel in unmatched:
                print(f"ERROR: --section {sel!r} matched 0 sections across input files.", file=sys.stderr)
            return 1

    if len(args.count) > 1:
        mean_all = round(total_words / total_paras, 1) if total_paras else 0.0
        print(
            f"TOTAL: {total_words} words, {total_paras} paragraphs, mean {mean_all}, "
            f">={args.long_para}w: {total_long}, straight quotes: {total_quotes}, italic runs: {total_italics}"
        )
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Apply exact logged edits to a stage output or count prose story text only.",
        epilog=HELP_EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--edits", help="Path to a JSON edit-order file.")
    group.add_argument("--count", nargs="+", help="Count prose story text only in one or more markdown files.")
    parser.add_argument("--dry-run", action="store_true", help="Check edits and print diff without writing target.")
    parser.add_argument("--no-diff", action="store_true", help="Omit diff output.")
    parser.add_argument("--long-para", type=int, default=60, help="Word-count cutoff for long paragraphs (default: 60).")
    parser.add_argument(
        "--section",
        action="append",
        help="With --count, limit counts to '##' sections matching this heading or prefix (repeatable; errors if 0 match).",
    )
    args = parser.parse_args(argv)
    if args.edits:
        return run_edits_command(args)
    return run_count_command(args)


if __name__ == "__main__":
    sys.exit(main())
