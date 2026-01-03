#!/usr/bin/env python3
"""
csv_to_hugo.py – Convert a Drupal‑exported CSV into Hugo markdown posts.

* Directory layout:   output_dir/YYYY/MM/slug/index.md
* Front‑matter keeps:
    nid, title, slug, date, drupal: { nid, path, body_format, redirects }, tags
* `drupal.redirects` is always a YAML list (empty list if none).
* Adds an `aliases:` list when the slug differs from the last component
  of `path` and/or when redirects are present.
* Ignores the literal string 'NULL' in the redirects column.
* If `tags` is NULL (or empty) the YAML front‑matter will contain
  `tags: []`.

The script downloads images that are referenced from
https://www.jeffgeerling.com/sites/default/files/... and rewrites the
image URLs to point at the downloaded files that live in the same folder
as the post.
"""

from __future__ import annotations

import argparse
import csv
import datetime
import json
import re
import string
import sys
import urllib.request
from pathlib import Path
from typing import List, Optional, Sequence

# ---------- Target NID (set to None to process the whole file) ----------
TARGET_NID: Optional[str] = None
# Example:  TARGET_NID = "1234"  # will only convert the row whose nid == "1234"

# ---------- Helpers ----------
def slugify(text: str) -> str:
    """Return a URL‑friendly slug for *text*."""
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"[^a-z0-9_]+", "-", text)
    text = re.sub(r"-{2,}", "-", text)
    return text.strip("-")

def parse_tags(tags_str: Optional[str]) -> List[str]:
    """Split a comma/semicolon separated tag string into a list."""
    if not tags_str:
        return []
    return [p.strip() for p in re.split(r"[;,]", tags_str) if p.strip()]

def parse_redirects(redirects_str: Optional[str]) -> List[str]:
    """Return a list of unique, slash‑prefixed URLs from the redirects column."""
    if not redirects_str:
        return []
    parts = re.split(r"[;,]", redirects_str)
    cleaned: List[str] = []
    for p in parts:
        p = p.strip()
        if not p or p.upper() == "NULL":
            continue
        if not p.startswith("/"):
            p = "/" + p
        cleaned.append(p)
    # dedupe while preserving order
    seen: set[str] = set()
    unique: List[str] = []
    for p in cleaned:
        if p not in seen:
            seen.add(p)
            unique.append(p)
    return unique

def parse_created(created_str: str) -> datetime.datetime:
    """Parse an ISO‑8601 datetime string; handles trailing 'Z'."""
    if created_str.endswith("Z"):
        created_str = created_str[:-1] + "+00:00"
    try:
        return datetime.datetime.fromisoformat(created_str)
    except ValueError as exc:
        raise ValueError(f"Invalid ISO‑8601 datetime: {created_str}") from exc

# ---------- Front‑matter generation ----------
def frontmatter(
    nid: str,
    title: str,
    slug: str,
    date: str,
    drupal_path: str,
    drupal_body_format: str,
    drupal_redirects: Sequence[str],
    tags: List[str],
    aliases: Sequence[str],
) -> str:
    """Return a YAML front‑matter block as a string."""
    title_quoted = json.dumps(title)
    slug_quoted = json.dumps(slug)

    lines = ["---"]
    lines.append(f"nid: {nid}")
    lines.append(f"title: {title_quoted}")
    lines.append(f"slug: {slug_quoted}")
    lines.append(f"date: {date}")

    lines.append("drupal:")
    lines.append(f"  nid: {nid}")
    lines.append(f"  path: {drupal_path}")
    lines.append(f"  body_format: {drupal_body_format}")

    if drupal_redirects:
        lines.append("  redirects:")
        for r in drupal_redirects:
            lines.append(f"    - {r}")
    else:
        lines.append("  redirects: []")

    if aliases:
        lines.append("aliases:")
        for a in aliases:
            lines.append(f"  - {a}")

    if tags:
        lines.append("tags:")
        for tag in tags:
            lines.append(f"  - {tag}")
    else:
        lines.append("tags: []")

    lines.append("---")
    return "\n".join(lines)

# ---------- Escape helpers for figure shortcodes ----------
def _escape_double_attr_value(val: str) -> str:
    """Return a JSON‑escaped version of *val* without the surrounding quotes."""
    return json.dumps(val)[1:-1]

# ---------- Convert <img …> tags to a Hugo figure shortcode ----------
def convert_img_tags_to_figure(body_html: str) -> str:
    """
    Convert <img> tags to Hugo figure shortcodes using a regex
    (no BeautifulSoup – avoids unwanted escaping of angle brackets).
    """
    # pattern to capture the entire <img …> tag
    img_tag_pat = re.compile(r'<img\b[^>]*>', flags=re.IGNORECASE)

    # helper to extract attribute value (quoted, double quotes only)
    attr_pat = re.compile(r'(\w+)\s*=\s*"([^"]*)"')

    def repl(match: re.Match) -> str:
        tag = match.group(0)
        attrs = dict(attr_pat.findall(tag))
        src = attrs.get("src")
        if not src:
            return tag  # nothing we can do

        parts = [f'src="{src}"']
        for key in ("alt", "width", "height", "class"):
            if key in attrs:
                parts.append(f'{key}="{_escape_double_attr_value(attrs[key])}"')

        shortcode = "{{< figure " + " ".join(parts) + " >}}"
        return shortcode

    return img_tag_pat.sub(repl, body_html)

# ---------- Image handling – download and rewrite URLs ----------
def _unescape_src(src: str) -> str:
    """Remove back‑slash escapes that were added by the Drupal CSV export."""
    return re.sub(r"\\(.)", r"\1", src)

def download_and_update_images(body: str, dir_path: Path) -> str:
    """
    Find all image URLs in the body (both <img src="…"> and markdown ![…](…)).
    Download images that live on www.jeffgeerling.com (HTTP, HTTPS or protocol‑relative)
    and rewrite the references to local files.
    """
    src_set: set[str] = set()

    # Find every src/value
    for m in re.finditer(r'src\s*=\s*["\']([^"\']+)["\']', body):
        src_set.add(m.group(1))

    for m in re.finditer(r'!\[[^\]]*\]\(([^)]+)\)', body):
        src_set.add(m.group(1))

    mapping: dict[str, str] = {}
    base_urls = ("https://www.jeffgeerling.com", "http://www.jeffgeerling.com")

    for src in src_set:
        src_clean = _unescape_src(src)

        # 1️⃣ Relative paths ("/sites/default/files/…")
        if src_clean.startswith("/sites/default/files/"):
            file_name = Path(src_clean).name
            target_path = dir_path / file_name

            if not target_path.exists():
                try:
                    urllib.request.urlretrieve("https://www.jeffgeerling.com" + src_clean, target_path)
                    print(f"📥  Downloaded {src} → {target_path}", file=sys.stderr)
                except Exception as exc:
                    print(f"⚠️  Failed to download {src}: {exc}", file=sys.stderr)
                    continue

            mapping[src] = f"./{file_name}"
            continue

        # 2️⃣ Absolute URLs (http, https, or protocol‑relative)
        if any(src_clean.lower().startswith(u) for u in base_urls):
            file_name = Path(src_clean).name
            target_path = dir_path / file_name

            if not target_path.exists():
                try:
                    urllib.request.urlretrieve(src_clean, target_path)
                    print(f"📥  Downloaded {src} → {target_path}", file=sys.stderr)
                except Exception as exc:
                    print(f"⚠️  Failed to download {src}: {exc}", file=sys.stderr)
                    continue

            mapping[src] = f"./{file_name}"
            continue

    # Replace src attributes
    def replace_src(m: re.Match) -> str:
        url = m.group(1)
        return f'src="{mapping.get(url, url)}"'

    body = re.sub(r'src\s*=\s*["\']([^"\']+)["\']', replace_src, body)

    # Replace markdown image links
    def replace_md(m: re.Match) -> str:
        alt = m.group(1)
        url = m.group(2)
        return f'![{alt}]({mapping.get(url, url)})'

    body = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replace_md, body)

    return body

# ---------- Write a post ----------
def write_post(
    out_root: Path,
    created: datetime.datetime,
    slug: str,
    front_matter: str,
    body: str,
) -> Path:
    """
    Write a single Hugo post.
    """
    year = created.strftime("%Y")
    month = created.strftime("%m")
    dir_path = out_root / year / month / slug
    dir_path.mkdir(parents=True, exist_ok=True)

    # 1️⃣ Convert <img> tags to Hugo figure shortcodes
    body = convert_img_tags_to_figure(body)

    # 2️⃣ Download images and update references
    body = download_and_update_images(body, dir_path)

    # 3️⃣ Restore block‑quote markers (in case they were escaped)
    body = re.sub(r'^\s*&gt;\s+', '> ', body, flags=re.MULTILINE)

    file_path = dir_path / "index.md"
    with file_path.open("w", encoding="utf-8") as fp:
        fp.write(front_matter)
        fp.write("\n\n")
        fp.write(body)
        fp.write("\n")

    return file_path

# ---------- CSV processing ----------
def process_csv(csv_file: Path, out_dir: Path) -> None:
    with csv_file.open(newline="", encoding="utf-8") as fp:
        reader = csv.DictReader(fp, delimiter=",")

        required_cols = {"nid", "title", "created", "body_format", "body_value"}
        missing = required_cols - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"CSV is missing required columns: {missing}")

        target_found = False

        for idx, row in enumerate(reader, start=2):
            nid = row.get("nid", "").strip()

            # If a target NID was specified, skip all rows that don't match it.
            if TARGET_NID and nid != TARGET_NID:
                continue

            try:
                title = row.get("title", "").strip()
                created_str = row.get("created", "").strip()
                body_format = row.get("body_format", "").strip().lower()
                body_value = row.get("body_value", "").strip()

                # Keep the original Drupal format for front‑matter
                original_body_format = body_format

                tags_str = row.get("tags", "").strip()
                if not tags_str or tags_str.upper() == "NULL":
                    tags_str = ""

                path = row.get("path", "").strip()
                redirects = row.get("redirects", "").strip()
                if redirects.upper() == "NULL":
                    redirects = ""

                slug = path.rstrip("/").split("/")[-1] if path else slugify(title)

                # Wrap PHP blocks in <code></code>
                body_value = re.sub(
                    r'(<\?php[\s\S]*?\?>)',
                    r'<code>\n\1\n</code>',
                    body_value,
                    flags=re.DOTALL,
                )

                # Wrap <code> blocks in <pre></pre>
                body_value = re.sub(
                    r'(?<=\n)\s*(<code>[\s\S]*?</code>)\s*(?=\n|$)',
                    r'\n<pre>\1</pre>\n',
                    body_value,
                    flags=re.DOTALL,
                )

                # Convert all pre/code wrappers to code fences
                PATTERN_START = re.compile(r'^\s*(<pre><code>)\s*$', flags=re.MULTILINE)
                PATTERN_END = re.compile(r'^\s*(</code></pre>)\s*$', flags=re.MULTILINE)
                body_value = PATTERN_START.sub('\n```', body_value)
                body_value = PATTERN_END.sub('```\n', body_value)

                created_dt = parse_created(created_str)
                tags_list = parse_tags(tags_str)

                # Build aliases
                aliases: List[str] = []
                if path:
                    last_component = path.rstrip("/").split("/")[-1]
                    if last_component and last_component != slug:
                        aliases.append(f"/{last_component}")
                redirects_list = parse_redirects(redirects)
                aliases.extend(redirects_list)

                seen: set[str] = set()
                unique_aliases: List[str] = []
                for a in aliases:
                    if a not in seen:
                        seen.add(a)
                        unique_aliases.append(a)

                fm = frontmatter(
                    nid=nid,
                    title=title,
                    slug=slug,
                    date=created_dt.isoformat(),
                    drupal_path=path,
                    drupal_body_format=original_body_format,
                    drupal_redirects=redirects_list,
                    tags=tags_list,
                    aliases=unique_aliases,
                )

                out_path = write_post(
                    out_root=out_dir,
                    created=created_dt,
                    slug=slug,
                    front_matter=fm,
                    body=body_value,
                )

                print(f"✅ Created: {out_path}")
                if TARGET_NID:
                    target_found = True
                    break  # stop after the target row

            except Exception as exc:
                print(
                    f"❌ Error processing row {idx} (nid={row.get('nid', '?')}): {exc}",
                    file=sys.stderr,
                )

        if TARGET_NID and not target_found:
            print(f"⚠️  No row with nid '{TARGET_NID}' found.", file=sys.stderr)

# ---------- Entry point ----------
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert a Drupal‑exported CSV to Hugo posts."
    )
    parser.add_argument(
        "--csv",
        dest="csv_file",
        type=Path,
        required=True,
        help="Path to the Drupal‑exported CSV file.",
    )
    parser.add_argument(
        "--out",
        dest="output_dir",
        type=Path,
        required=True,
        help="Directory where the Hugo posts will be written.",
    )

    args = parser.parse_args()

    csv_file = args.csv_file
    out_dir = args.output_dir

    if not csv_file.is_file():
        print(f"❌ {csv_file!s} does not exist or is not a file.", file=sys.stderr)
        sys.exit(1)

    out_dir.mkdir(parents=True, exist_ok=True)

    process_csv(csv_file, out_dir)

if __name__ == "__main__":
    main()
