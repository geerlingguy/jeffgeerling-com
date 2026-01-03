#!/usr/bin/env python3
"""
Export Drupal blog posts to a CSV file.

Usage:
    python drupal_export.py  >  blog_export.csv
or
    python drupal_export.py  output_file.csv

The script prints a header row, then one CSV row per node.
Fields containing newlines, commas, or quotes are correctly quoted.
"""

import sys
import csv
import pymysql
import os
from contextlib import closing

# ------------------------------------------------------------------
# 1. Configuration – edit these values for your environment
# ------------------------------------------------------------------
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_USER = os.getenv("DB_USER", "drupal")
DB_PASS = os.getenv("DB_PASS", "drupal")
DB_NAME = os.getenv("DB_NAME", "drupal")

# ------------------------------------------------------------------
# 2. The SQL you already have – keep it exactly as you wrote it
# ------------------------------------------------------------------
SQL_QUERY = """
SELECT
    n.nid,
    nf.title,
    FROM_UNIXTIME(nf.created,'%Y-%m-%dT%TZ') AS created,
    u.name,
    b.body_format,
    b.body_value,
    GROUP_CONCAT(DISTINCT t_tag.name ORDER BY t_tag.name SEPARATOR ', ') AS tags,
    pa.alias AS path,
    GROUP_CONCAT(DISTINCT r.redirect_source__path ORDER BY r.rid SEPARATOR ', ') AS redirects
FROM node AS n
LEFT JOIN node__body b
          ON b.entity_id = n.nid AND b.deleted = 0
LEFT JOIN node_field_data nf
          ON nf.nid = n.nid
LEFT JOIN users_field_data u
          ON u.uid = nf.uid
LEFT JOIN node__field_tags tntg
          ON tntg.entity_id = n.nid
LEFT JOIN taxonomy_term_field_data t_tag
          ON t_tag.tid = tntg.field_tags_target_id
LEFT JOIN path_alias pa
          ON pa.path = CONCAT('/node/', n.nid)
LEFT JOIN redirect r
          ON r.redirect_redirect__uri = CONCAT('internal:/node/', n.nid)
WHERE n.type = 'blog_post'
  AND nf.status = 1
  AND (nf.title NOT LIKE '%Photo: %')
GROUP BY n.nid
ORDER BY nf.created;
"""

# ------------------------------------------------------------------
# 3. Helper: build the CSV writer
# ------------------------------------------------------------------
def get_csv_writer(f):
    """
    Return a csv.writer that:
    * uses UTF‑8
    * escapes commas, newlines, and quotes
    * does **not** add an extra newline on Windows
    """
    return csv.writer(
        f,
        delimiter=",",
        quotechar='"',
        quoting=csv.QUOTE_MINIMAL,
        lineterminator="\n",  # csv module uses \n on all platforms
    )

# ------------------------------------------------------------------
# 4. Main routine
# ------------------------------------------------------------------
def main(output_path=None):
    # 4a. Connect to MariaDB
    conn = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,  # we want column names
    )

    # 4b. Prepare the output file/stream
    out_stream = open(output_path, "w", encoding="utf-8", newline="") if output_path else sys.stdout

    writer = get_csv_writer(out_stream)

    # 4c. Write header
    # We can get the header from the cursor description or hard‑code it
    header = [
        "nid",
        "title",
        "created",
        "author",
        "body_format",
        "body_value",
        "tags",
        "path",
        "redirects",
    ]
    writer.writerow(header)

    # 4d. Execute the query and stream rows
    with conn.cursor() as cur:
        cur.execute(SQL_QUERY)
        # fetchmany() can reduce memory usage; 1000 rows per batch is typical
        batch_size = 1000
        while True:
            rows = cur.fetchmany(batch_size)
            if not rows:
                break
            for row in rows:
                # Map to the header order
                writer.writerow(
                    [
                        row.get("nid"),
                        row.get("title"),
                        row.get("created"),
                        row.get("name"),            # author
                        row.get("body_format"),
                        row.get("body_value"),
                        row.get("tags"),
                        row.get("path"),
                        row.get("redirects"),
                    ]
                )

    # 4e. Close everything
    out_stream.close()
    conn.close()


# ------------------------------------------------------------------
# 5. Entry point
# ------------------------------------------------------------------
if __name__ == "__main__":
    # Accept an optional output filename
    if len(sys.argv) > 1:
        out_file = sys.argv[1]
    else:
        out_file = None  # write to stdout

    try:
        main(out_file)
    except Exception as exc:
        sys.stderr.write(f"❌ Error: {exc}\n")
        sys.exit(1)
