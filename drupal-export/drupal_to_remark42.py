#!/usr/bin/env python3
"""
Drupal → WordPress XML Export (parent‑child comments)

  • Pulls comments from a Drupal 10 database
  • Builds an <item> per node (post) and nests all comments inside
  • Uses <wp:comment_content> for the comment body
  • Handles anonymous / known users, email, IP, etc.
  • Pretty‑prints the output to disk
"""

from __future__ import annotations

import datetime
import re
import sys
import urllib.request
import urllib.error
from pathlib import Path
from typing import Dict, List

import mysql.connector
import xml.etree.ElementTree as ET
from xml.dom import minidom

# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def sanitize_xml_text(text: str) -> str:
    """Remove characters that are illegal in XML 1.0."""
    if not text:
        return ""
    # Keep #x9, #xA, #xD and printable characters
    return re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', "", text)


# --------------------------------------------------------------------------- #
# Data extraction
# --------------------------------------------------------------------------- #
def get_drupal_comments(db_config: Dict[str, str], site_url: str) -> List[Dict]:
    """
    Pull comments (with parent/child data) from Drupal 10.

    Returns a list of dicts.  Each dict contains all comment fields plus
    the node title and node creation timestamp – these are used later to
    build the <item> blocks.
    """
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # One query that returns comment data + node title & created
        query = """
        SELECT
            c.cid                AS comment_id,
            c.entity_id          AS node_id,
            c.uid                AS user_id,
            c.subject            AS subject,
            cb.comment_body_value AS comment_body,
            c.created            AS created_timestamp,
            c.changed            AS changed_timestamp,
            c.mail               AS email,
            c.name               AS author_name,
            c.hostname           AS ip_address,
            c.pid                AS parent_id,
            c.thread             AS thread,
            pa.alias              AS path_alias,

            -- Node data – required for the <item> header
            n.title               AS node_title,
            n.created             AS node_created
        FROM comment_field_data c
        LEFT JOIN comment__comment_body cb
               ON c.cid = cb.entity_id
        LEFT JOIN path_alias pa
               ON CONCAT('/node/', c.entity_id) = pa.path
        LEFT JOIN node_field_data n
               ON n.nid = c.entity_id
        WHERE c.status = 1
          AND c.entity_id >= 1814
        ORDER BY c.created
        """
        cursor.execute(query)
        rows = cursor.fetchall()

        comments = []

        for row in rows:
            # ---- User mapping -------------------------------------------------
            if row["user_id"] == 0:
                # Anonymous – use name/email from comment if present
                author_name = row["author_name"] or "Anonymous"
                email = row["email"] or ""
            elif row["user_id"] == 1:
                # Example: you can map user #1 to a real name/email
                author_name = "Jeff Geerling"
                email = "jeff@jeffgeerling.com"
            else:
                author_name = row["author_name"] or "Anonymous"
                email = row["email"] or ""

            # ---- URL construction ---------------------------------------------
            if row["path_alias"]:
                path = row["path_alias"] + "/"
                if not path.startswith("/"):
                    path = "/" + path
            else:
                path = f"/node/{row['node_id']}/"

            full_url = f"{site_url.rstrip('/')}{path}"

            comments.append(
                {
                    "comment_id": row["comment_id"],
                    "node_id": row["node_id"],
                    "user_id": row["user_id"],
                    "subject": row["subject"],
                    "comment_body": row["comment_body"],
                    "created_timestamp": row["created_timestamp"],
                    "changed_timestamp": row["changed_timestamp"],
                    "email": email,
                    "author_name": author_name,
                    "ip_address": row["ip_address"],
                    "parent_id": row["parent_id"],
                    "thread": row["thread"],
                    "path_alias": path,
                    "full_url": full_url,
                    # node‑level data
                    "node_title": row["node_title"] or f"Node {row['node_id']}",
                    "node_created": row["node_created"],
                }
            )

        cursor.close()
        conn.close()

        return comments

    except Exception as exc:
        print(f"Error connecting to Drupal database: {exc}", file=sys.stderr)
        sys.exit(1)


# --------------------------------------------------------------------------- #
# Build a node‑to‑comments map
# --------------------------------------------------------------------------- #
def build_node_map(comments: List[Dict]) -> Dict[int, Dict]:
    """
    Convert the flat comment list into a dict keyed by node_id.
    Each value contains node metadata and a list of comments.
    """
    node_map: Dict[int, Dict] = {}

    for c in comments:
        nid = c["node_id"]
        if nid not in node_map:
            node_map[nid] = {
                "node_title": c["node_title"],
                "node_created": c["node_created"],
                "node_link": c["full_url"],
                "comments": [],
            }
        node_map[nid]["comments"].append(c)

    return node_map


# --------------------------------------------------------------------------- #
# XML creation
# --------------------------------------------------------------------------- #
def create_wordpress_xml(node_map: Dict[int, Dict], site_url: str, output_file: str) -> None:
    """
    Build a proper WordPress export XML from a node-to-comments map.
    """
    # ----------------------------------------------------------------------- #
    # Root element
    # ----------------------------------------------------------------------- #
    rss = ET.Element(
        "rss",
        {
            "version": "2.0",
            "xmlns:wp": "http://wordpress.org/export/1.2/",
            "xmlns:content": "http://purl.org/rss/1.0/modules/content/",
            "xmlns:dc": "http://purl.org/dc/elements/1.1/",
        },
    )

    channel = ET.SubElement(rss, "channel")

    # Site info
    ET.SubElement(channel, "title").text = "Comments"
    ET.SubElement(channel, "link").text = site_url
    ET.SubElement(channel, "description").text = "Comments from Drupal site"
    ET.SubElement(
        channel, "pubDate"
    ).text = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z")
    ET.SubElement(channel, "language").text = "en-US"

    # ----------------------------------------------------------------------- #
    # Track actual exported counts
    # ----------------------------------------------------------------------- #
    exported_posts = 0
    exported_comments = 0

    # ----------------------------------------------------------------------- #
    # One <item> per node (post)
    # ----------------------------------------------------------------------- #
    for nid, node in node_map.items():
        item = ET.SubElement(channel, "item")

        # Resolve the actual URL by following redirects
        try:
            # ---- Build full URL safely ------------------------------------------- #
            node_link = node["node_link"]

            # Ensure node_link is a valid URL string
            try:
                # Parse the URL to extract components
                from urllib.parse import urlparse, urlunparse, quote

                parsed = urlparse(node_link)
                # Reconstruct the URL with properly encoded path
                encoded_path = quote(parsed.path, safe="/")
                node_link = urlunparse((
                    parsed.scheme,
                    parsed.netloc,
                    encoded_path,
                    parsed.params,
                    parsed.query,
                    parsed.fragment
                ))
            except Exception as e:
                print(f"Warning: Failed to encode URL {node_link}: {e}")
                # Proceed with original link if encoding fails
                pass

            # Create a request object
            req = urllib.request.Request(node_link)
            # Set a user agent to avoid being blocked
            req.add_header('User-Agent', 'Mozilla/5.0')

            # Try to open the URL
            response = urllib.request.urlopen(req)
            actual_url = response.geturl()

            # If we got a redirect, use the final URL
            if actual_url != node_link:
                node["node_link"] = actual_url
                print(f"Redirected {node_link} -> {actual_url}")
        except urllib.error.HTTPError as e:
            print(f"Skipping node {node['node_link']} ({e.code})")
            continue
        except urllib.error.URLError as e:
            print(f"Skipping node {node['node_link']} (URL Error: {e.reason})")
            continue
        except Exception as e:
            print(f"Skipping node {node['node_link']} (Unexpected error: {e})")
            continue

        # ---- Post meta -------------------------------------------------------
        ET.SubElement(item, "title").text = node["node_title"]
        ET.SubElement(item, "link").text = node["node_link"]

        pubdate = datetime.datetime.fromtimestamp(
            node["node_created"]
        ).strftime("%a, %d %b %Y %H:%M:%S %z")
        ET.SubElement(item, "pubDate").text = pubdate
        ET.SubElement(item, "guid").text = node["node_link"]

        # ---- Comments ---------------------------------------------------------
        for com in node["comments"]:
            wp_comment = ET.SubElement(item, "wp:comment")

            ET.SubElement(wp_comment, "wp:comment_author").text = com["author_name"]
            ET.SubElement(wp_comment, "wp:comment_author_email").text = com["email"]
            ET.SubElement(wp_comment, "wp:comment_author_url").text = ""
            ET.SubElement(wp_comment, "wp:comment_author_IP").text = com["ip_address"]

            sanitized_body = sanitize_xml_text(com["comment_body"] or "")
            ET.SubElement(wp_comment, "wp:comment_content").text = sanitized_body

            comment_date = datetime.datetime.fromtimestamp(
                com["created_timestamp"]
            ).strftime("%Y-%m-%d %H:%M:%S")
            ET.SubElement(wp_comment, "wp:comment_date").text = comment_date
            ET.SubElement(wp_comment, "wp:comment_date_gmt").text = comment_date

            ET.SubElement(wp_comment, "wp:comment_id").text = str(com["comment_id"])
            parent_id = (
                str(com["parent_id"])
                if com["parent_id"] and com["parent_id"] != 0
                else "0"
            )
            ET.SubElement(wp_comment, "wp:comment_parent").text = parent_id

            ET.SubElement(wp_comment, "wp:comment_approved").text = "1"
            ET.SubElement(wp_comment, "wp:comment_type").text = "comment"

        # ----------------------------------------------------------------------- #
        # Count this post and its comments
        # ----------------------------------------------------------------------- #
        exported_posts += 1
        exported_comments += len(node["comments"])

    # ----------------------------------------------------------------------- #
    # Write pretty-printed XML to file
    # ----------------------------------------------------------------------- #
    rough = ET.tostring(rss, encoding="utf-8")
    parsed = minidom.parseString(rough)
    pretty = parsed.toprettyxml(indent="  ", encoding="utf-8")

    Path(output_file).write_bytes(pretty)

    print(f"Exported {exported_posts} posts with {exported_comments} comments to {output_file}")



# --------------------------------------------------------------------------- #
# CLI entry point
# --------------------------------------------------------------------------- #
def main() -> None:
    # Hard‑coded connection details – change for your environment
    db_config = {
        "host": "localhost",
        "port": 3306,
        "database": "drupal",
        "user": "drupal",
        "password": "drupal",
    }

    site_url = "http://dev.jeffgeerling.com:1313"
    #site_url = "https://www.jeffgeerling.com"
    output_file = "exported-comments.xml"

    print("Extracting comments from Drupal…")
    raw_comments = get_drupal_comments(db_config, site_url)

    if not raw_comments:
        print("No comments found – aborting.")
        return

    print(f"Found {len(raw_comments)} comments across {len({c['node_id'] for c in raw_comments})} nodes")

    # Build the hierarchical structure
    node_map = build_node_map(raw_comments)

    # Create the XML
    create_wordpress_xml(node_map, site_url, output_file)


if __name__ == "__main__":
    main()
