#!/usr/bin/env python3
"""
hugo_file_refs_dl.py

Recursively walks the ../content folder (one level up from where the script
resides), finds all index.md files, extracts links to /sites/default/files
pointing to the allowed extensions, downloads the files into the same folder
as the index.md, and rewrites the links to relative ones.

Usage:
    hugo_file_refs_dl.py [--dry-run]

Options:
    --dry-run    Run without touching the filesystem (default: False)
"""

import argparse
import os
import re
import sys
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests

# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #

# Base URL to resolve relative links (fixed, no CLI override)
BASE_URL = "https://www.jeffgeerling.com"

# Allowed file extensions
ALLOWED_EXTS = {'.swf', '.aif', '.mp3', '.m4r', '.mp4', '.m4a', '.pdf',
                '.txt', '.zip', '.ai', '.eps'}

# Regexes
HTML_A_LINK_RE = re.compile(
    r'<a\s+[^>]*href\s*=\s*["\']([^"\']+)["\']',
    flags=re.IGNORECASE | re.MULTILINE
)

# Markdown links – negative lookbehind so we ignore image links ![...](...)
MD_LINK_RE = re.compile(
    r'(?<!\!)\[(?P<text>[^\]]+)\]\((?P<url>[^)]+)\)',
    flags=re.IGNORECASE | re.MULTILINE
)

# --------------------------------------------------------------------------- #
# Helper functions
# --------------------------------------------------------------------------- #

def is_allowed_file(url: str) -> bool:
    """Return True if URL ends with an allowed file extension."""
    _, ext = os.path.splitext(urlparse(url).path)
    return ext.lower() in ALLOWED_EXTS


def resolve_full_url(link: str) -> str:
    """Return an absolute URL (adds BASE_URL if link is relative)."""
    if urlparse(link).scheme:   # already absolute
        return link
    return urljoin(BASE_URL, link)


def download_file(url: str, dest_path: Path, dry_run: bool) -> bool:
    """Download a file to dest_path. Return True if the file was (or would be) written."""
    if dest_path.exists():
        print(f"SKIP  (already exists)  {dest_path}")
        return False

    if dry_run:
        print(f"DRYRUN DOWNLOAD  {url} -> {dest_path}")
        return True

    try:
        resp = requests.get(url, stream=True, timeout=30)
        resp.raise_for_status()
        with open(dest_path, 'wb') as f:
            for chunk in resp.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"DOWNLOADED  {url} -> {dest_path}")
        return True
    except Exception as exc:
        print(f"ERROR  downloading {url}: {exc}")
        return False


def process_index_md(index_path: Path, dry_run: bool, script_dir: Path) -> bool:
    """
    Process a single index.md file.

    Returns True if any downloadable files were found (and therefore
    the file was modified / files downloaded).  If no relevant links are
    found, the file is left untouched and False is returned.
    """
    content = index_path.read_text(encoding='utf-8')
    replacements = {}

    # ---- Find <a href="..."> links --------------------------------------- #
    for m in HTML_A_LINK_RE.finditer(content):
        orig_href = m.group(1)
        if '/sites/default/files' not in orig_href:
            continue
        if not is_allowed_file(orig_href):
            continue

        filename = os.path.basename(urlparse(orig_href).path)
        if not filename:
            continue

        new_href = f"./{filename}"
        abs_url = resolve_full_url(orig_href)
        dest = index_path.parent / filename
        download_file(abs_url, dest, dry_run)
        replacements[orig_href] = new_href
        print(f"REPLACE HTML  {orig_href} -> {new_href}")

    # ---- Find Markdown links ----------------------------------------------- #
    for m in MD_LINK_RE.finditer(content):
        link = m.group('url')
        if '/sites/default/files' not in link:
            continue
        if not is_allowed_file(link):
            continue

        filename = os.path.basename(urlparse(link).path)
        if not filename:
            continue

        new_link = f"./{filename}"
        abs_url = resolve_full_url(link)
        dest = index_path.parent / filename
        download_file(abs_url, dest, dry_run)
        replacements[link] = new_link
        print(f"REPLACE MD    {link} -> {new_link}")

    # ---- If we found any files, print PROCESS line and apply replacements --- #
    if replacements:
        # Print PROCESS line once, relative to the script directory
        rel_path = os.path.relpath(index_path, script_dir)
        print(f"\nPROCESS   {rel_path}")

        # Build a regex that matches any of the old URLs (escaped)
        escaped_old = [re.escape(k) for k in replacements.keys()]
        pattern = re.compile('|'.join(escaped_old))

        def repl(match: re.Match) -> str:
            return replacements[match.group(0)]

        new_content = pattern.sub(repl, content)

        if dry_run:
            print(f"DRYRUN: would write updated {index_path}")
        else:
            index_path.write_text(new_content, encoding='utf-8')
            print(f"WROTE     {index_path}")

        return True
    else:
        return False


def walk_and_process(base_dir: Path, dry_run: bool, script_dir: Path) -> None:
    """Recursively walk through base_dir and process every index.md."""
    for root, dirs, files in os.walk(base_dir):
        # skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        if 'index.md' in files:
            index_path = Path(root) / 'index.md'
            # We only print a PROCESS line if the file actually contains
            # downloadable links. That is handled inside process_index_md.
            process_index_md(index_path, dry_run, script_dir)


# --------------------------------------------------------------------------- #
# Main entry point
# --------------------------------------------------------------------------- #

def main() -> None:
    parser = argparse.ArgumentParser(description="Hugo file reference downloader")
    parser.add_argument('--dry-run', action='store_true',
                        help='Do not touch the filesystem (default: False)')
    args = parser.parse_args()

    # Path to ../content relative to the script's location
    script_dir = Path(__file__).resolve().parent
    content_dir = script_dir.parent / 'content'

    if not content_dir.is_dir():
        print(f"ERROR: Content directory not found: {content_dir}")
        sys.exit(1)

    print(f"Starting on content directory: {content_dir}")
    print(f"Base URL          : {BASE_URL}")
    if args.dry_run:
        print("=== DRY RUN MODE ===")

    walk_and_process(content_dir, args.dry_run, script_dir)
    print("\nDone.")


if __name__ == "__main__":
    main()
