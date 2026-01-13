#!/usr/bin/env python3
"""
Drupal to Remark42 Comment Export Script with Parent-Child Relationships
Exports Drupal comments in WordPress XML format for Remark42 import
"""

import xml.etree.ElementTree as ET
from xml.dom import minidom
import mysql.connector
import datetime
import sys
from typing import Optional, Dict, List

def get_drupal_comments(db_config: dict, site_url: str) -> list:
    """
    Extract comments from Drupal 10 database with parent-child relationships.

    Args:
        db_config: Database connection parameters
        site_url: Base URL of your site

    Returns:
        List of comment dictionaries
    """

    # Connect to Drupal database
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # Query to get comments with their associated node information and parent relationships
        # Using Drupal 10 table structure with separate path_alias table and comment_body table
        query = """
        SELECT
            c.cid as comment_id,
            c.entity_id as node_id,
            c.uid as user_id,
            c.subject as subject,
            cb.comment_body_value as comment_body,
            c.created as created_timestamp,
            c.changed as changed_timestamp,
            c.mail as email,
            c.name as author_name,
            c.hostname as ip_address,
            c.pid as parent_id,
            c.thread as thread,
            pa.alias as path_alias
        FROM comment_field_data c
        LEFT JOIN comment__comment_body cb ON c.cid = cb.entity_id
        LEFT JOIN path_alias pa ON CONCAT('/node/', c.entity_id) = pa.path
        WHERE c.status = 1
            AND c.entity_id >= 1814
        ORDER BY c.created
        """

        cursor.execute(query)
        comments = cursor.fetchall()

        # Process comments to get proper URLs and handle user mapping
        processed_comments = []
        for comment in comments:
            # Handle user mapping
            if comment['user_id'] == 0:
                # If user_id is 0, use author_name from comment or fallback to Anonymous
                author_name = comment['author_name'] if comment['author_name'] else 'Anonymous'
                email = comment['email'] if comment['email'] else ''
            elif comment['user_id'] == 1:
                author_name = 'Jeff Geerling'
                email = 'jeff@jeffgeerling.com'  # You can adjust this email as needed
            else:
                author_name = comment['author_name'] or 'Anonymous'
                email = comment['email'] or ''

            # Get the path alias or construct URL
            if comment['path_alias']:
                path = comment['path_alias']
                if not path.startswith('/'):
                    path = '/' + path
            else:
                # Fallback to node path
                path = f'/node/{comment["node_id"]}'

            # Construct full URL
            full_url = f"{site_url}{path}"

            processed_comments.append({
                'comment_id': comment['comment_id'],
                'node_id': comment['node_id'],
                'user_id': comment['user_id'],
                'subject': comment['subject'],
                'comment_body': comment['comment_body'],
                'created_timestamp': comment['created_timestamp'],
                'changed_timestamp': comment['changed_timestamp'],
                'email': email,
                'author_name': author_name,
                'ip_address': comment['ip_address'],
                'parent_id': comment['parent_id'],
                'thread': comment['thread'],
                'path_alias': path,
                'full_url': full_url
            })

        cursor.close()
        conn.close()

        return processed_comments

    except Exception as e:
        print(f"Error connecting to Drupal database: {e}")
        sys.exit(1)

def create_wordpress_xml(comments: list, site_url: str, output_file: str):
    """
    Create WordPress XML format for Remark42 import with parent-child relationships

    Args:
        comments: List of comment dictionaries
        site_url: Base URL of your site
        output_file: Output XML file path
    """

    # Create root element
    rss = ET.Element('rss', {'version': '2.0'})

    # Add namespace declaration properly
    channel = ET.SubElement(rss, 'channel')

    # Site info
    ET.SubElement(channel, 'title').text = 'Comments'
    ET.SubElement(channel, 'link').text = site_url
    ET.SubElement(channel, 'description').text = 'Comments from Drupal site'
    ET.SubElement(channel, 'pubDate').text = datetime.datetime.now().strftime('%a, %d %b %Y %H:%M:%S %z')
    ET.SubElement(channel, 'language').text = 'en-US'

    # Add comments in order, handling parent-child relationships
    for comment in comments:
        item = ET.SubElement(channel, 'item')

        # Comment metadata
        ET.SubElement(item, 'title').text = comment['subject'] or 'Comment'
        ET.SubElement(item, 'link').text = comment['full_url']
        ET.SubElement(item, 'pubDate').text = datetime.datetime.fromtimestamp(
            comment['created_timestamp']
        ).strftime('%a, %d %b %Y %H:%M:%S %z')

        # Comment content
        content = ET.SubElement(item, 'content:encoded')
        content.text = comment['comment_body'] or ''

        # Comment author info - using standard WordPress fields
        author_name = ET.SubElement(item, 'wp:comment_author')
        author_name.text = comment['author_name'] or 'Anonymous'

        author_email = ET.SubElement(item, 'wp:comment_author_email')
        author_email.text = comment['email'] or ''

        author_url = ET.SubElement(item, 'wp:comment_author_url')
        author_url.text = ''

        author_ip = ET.SubElement(item, 'wp:comment_author_IP')
        author_ip.text = comment['ip_address'] or ''

        # Comment ID and parent info
        comment_id = ET.SubElement(item, 'wp:comment_id')
        comment_id.text = str(comment['comment_id'])

        # Set parent ID - if parent_id is 0 or None, it's a top-level comment
        parent_id = str(comment['parent_id']) if comment['parent_id'] and comment['parent_id'] != 0 else '0'
        comment_parent = ET.SubElement(item, 'wp:comment_parent')
        comment_parent.text = parent_id

        comment_type = ET.SubElement(item, 'wp:comment_type')
        comment_type.text = 'comment'

        comment_status = ET.SubElement(item, 'wp:comment_status')
        comment_status.text = 'approved'

    # Convert to string and format properly
    rough_string = ET.tostring(rss, encoding='unicode')

    # Parse and pretty print to avoid namespace issues
    try:
        reparsed = minidom.parseString(rough_string)
        pretty_xml = reparsed.toprettyxml(indent="  ")

        # Write to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(pretty_xml)

        print(f"Exported {len(comments)} comments to {output_file}")
    except Exception as e:
        print(f"Error creating XML: {e}")
        # Fallback to basic XML without pretty printing
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(rough_string)
        print(f"Exported {len(comments)} comments to {output_file} (basic format)")

def main():
    # Hardcoded configuration for Drupal 10
    db_config = {
        'host': 'localhost',
        'port': 3306,
        'database': 'drupal',
        'user': 'drupal',
        'password': 'drupal'
    }

    site_url = "https://www.jeffgeerling.com"
    output_file = "comments.xml"

    print("Extracting comments from Drupal...")
    comments = get_drupal_comments(db_config, site_url)

    print(f"Found {len(comments)} comments")

    if not comments:
        print("No comments found to export")
        return

    # Sort comments by creation timestamp to maintain proper order
    comments.sort(key=lambda x: x['created_timestamp'])

    print("Creating WordPress XML export with parent-child relationships...")
    create_wordpress_xml(comments, site_url, output_file)

    print("Export complete!")

if __name__ == '__main__':
    main()
