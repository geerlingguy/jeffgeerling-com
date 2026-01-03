#!/usr/bin/env python3
"""
hugo_drupal_path_to_aliases.py

Recursively scans project_root/content/blog for every `index.md` file.
If a front‑matter block contains a `drupal.path` that does **not** match
the pattern `/blog/YYYY/<something>`, the script appends that value to
the page’s `aliases` list **without discarding any existing aliases**.

All other formatting – key order, indentation, blank lines,
trailing new‑lines – is left untouched.
"""

import re
import sys
from pathlib import Path

import frontmatter  # pip install python-frontmatter

ROOT_DIR = Path(__file__).resolve().parents[1]
CONTENT_BLOG_DIR = ROOT_DIR / "content" / "blog"
INDEX_FILE_NAME = "index.md"
BLOG_YEAR_RE = re.compile(r"^/blog/\d{4}/.+$")

# -----------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------
def inline_yaml_list(values):
    """Return a YAML‑style inline list, e.g. [a, b, c]."""
    return "[" + ", ".join(repr(v) for v in values) + "]"


def _parse_yaml(header_text: str):
    """Parse header_text with frontmatter, but replace tabs with spaces."""
    cleaned = header_text.replace("\t", "  ")
    try:
        return frontmatter.loads(cleaned)
    except Exception:
        return {}


def _fallback_path(header_text: str):
    """Fallback for odd indentation / tab issues."""
    lines = header_text.splitlines()
    in_drupal = False
    for line in lines:
        if in_drupal:
            m = re.match(r"^\s*path:\s*([^\s]+)", line)
            if m:
                return m.group(1)
        if re.match(r"^\s*drupal:\s*$", line):
            in_drupal = True
    return None


def extract_drupal_path(header_text: str) -> str | None:
    """Try to obtain the `drupal.path` value."""
    meta = _parse_yaml(header_text)
    path = meta.get("drupal", {}).get("path")
    if path:
        return path
    return _fallback_path(header_text)


# -----------------------------------------------------------------------
# Main logic
# -----------------------------------------------------------------------
def process_file(md_path: Path) -> None:
    txt = md_path.read_text(encoding="utf-8-sig")
    lines = txt.splitlines(True)  # keep line breaks

    # Find front‑matter delimiters
    try:
        start_idx = next(
            i for i, l in enumerate(lines) if l.strip() in ("---", "...")
        )
    except StopIteration:
        return  # no front‑matter

    try:
        end_idx = next(
            i
            for i in range(start_idx + 1, len(lines))
            if lines[i].strip() in ("---", "...")
        )
    except StopIteration:
        return  # malformed front‑matter

    header_lines = lines[start_idx + 1 : end_idx]
    if not header_lines:
        return  # empty front‑matter

    header_text = "".join(header_lines)

    # ---------- Get the drupal.path value ----------
    drupal_path = extract_drupal_path(header_text)
    if not drupal_path:
        return  # nothing to do

    # Skip if the path already matches the allowed pattern
    if BLOG_YEAR_RE.match(drupal_path):
        return
    else:
        print(f"'{drupal_path}' in {md_path} does NOT match the allowed pattern")

    # ---------- Parse the header into a dict ----------
    metadata = _parse_yaml(header_text)

    # ---------- Update aliases ----------
    aliases = metadata.get("aliases") or []
    if not isinstance(aliases, list):
        print(f"WARNING: Non‑list aliases in {md_path}; skipping.")
        return

    if drupal_path in aliases:
        return  # nothing to change

    aliases.append(drupal_path)

    # ---------- Re‑create the header while keeping the original order ----------
    # Find existing aliases block (inline or multiline)
    alias_start = None
    for idx, line in enumerate(header_lines):
        if line.lstrip().startswith("aliases:"):
            alias_start = idx
            break

    if alias_start is not None:
        key_line = header_lines[alias_start]
        key_indent = key_line[: key_line.find("aliases:")]
        after_colon = key_line[key_line.find(":") + 1 :].strip()

        if after_colon == "":
            # Multiline block – find its end
            j = alias_start + 1
            while j < len(header_lines):
                l = header_lines[j]
                stripped = l.lstrip()
                if stripped == "":
                    j += 1
                    continue
                if stripped.startswith("-"):
                    # first list item – record its indentation
                    item_indent = l[: l.find("-")]
                    break
                else:
                    # no list items – treat as empty block
                    item_indent = l[: l.find("-")] if "-" in l else ""
                    break

            # Find the block end (first line that is less indented)
            block_end = j + 1
            while block_end < len(header_lines):
                l = header_lines[block_end]
                if l.strip() == "" or l.lstrip().startswith("#"):
                    block_end += 1
                    continue
                if len(l) - len(l.lstrip()) <= len(item_indent):
                    break
                block_end += 1

            # Append new alias before block_end
            # Ensure the alias is indented two spaces
            new_line = f"{item_indent or '  '} - {drupal_path}\n"
            header_lines = (
                header_lines[:block_end] + [new_line] + header_lines[block_end:]
            )
        else:
            # Inline list – convert to multiline (keep existing items)
            # Parse the inline list
            try:
                inline_items = frontmatter.loads(f"aliases:{after_colon}")["aliases"]
            except Exception:
                inline_items = []
            inline_items.append(drupal_path)

            # Build multiline block
            new_block = [f"{key_indent}aliases:\n"]
            for alias in inline_items:
                new_block.append(f"  - {alias}\n")
            header_lines = (
                header_lines[:alias_start]
                + new_block
                + header_lines[alias_start + 1 :]
            )
    else:
        # No aliases key – insert a new multiline block before the closing delimiter
        new_block = ["aliases:\n"]
        for alias in aliases:
            new_block.append(f"  - {alias}\n")
        header_lines = header_lines + new_block

    # ---------- Build new file content ----------
    new_file_lines = (
        lines[: start_idx + 1]  # opening delimiter line
        + header_lines
        + lines[end_idx:]  # closing delimiter + rest of the file
    )
    new_txt = "".join(new_file_lines)

    # ---------- Write back only if something changed ----------
    if new_txt != txt:
        md_path.write_text(new_txt, encoding="utf-8-sig")
        print(f"Updated aliases in {md_path}")


def main() -> None:
    if not CONTENT_BLOG_DIR.is_dir():
        print(f"ERROR: Expected directory {CONTENT_BLOG_DIR} does not exist.")
        sys.exit(1)

    for md_path in CONTENT_BLOG_DIR.rglob(INDEX_FILE_NAME):
        if md_path.is_file():
            process_file(md_path)


if __name__ == "__main__":
    main()
