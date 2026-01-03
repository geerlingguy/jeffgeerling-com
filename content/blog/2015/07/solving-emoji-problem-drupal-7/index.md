---
nid: 2501
title: "Solving the Emoji/character encoding problem in Drupal 7"
slug: "solving-emoji-problem-drupal-7"
date: 2015-07-21T17:39:42+00:00
drupal:
  nid: 2501
  path: /blogs/jeff-geerling/solving-emoji-problem-drupal-7
  body_format: full_html
  redirects: []
tags:
  - database
  - drupal
  - drupal planet
  - mysql
  - utf8
  - utf8mb4
aliases:
  - /blogs/jeff-geerling/solving-emoji-problem-drupal-7
---

<blockquote><strong>Update</strong>: As of Drupal 7.50, Emoji/UTF-8 mb4 is now supported for MySQL (and other databases) in core! See the documentation page here for more information on how to configure it: <a href="https://www.drupal.org/node/2754539">Multi-byte UTF-8 support in Drupal 7</a>. <em>This blog post exists for historical purposes only—please see the Drupal.org documentation for the most up-to-date instructions, and see my newer blog post here: <a href="/blog/2016/getting-emoji-and-multibyte-characters-on-your-drupal-7-site-750-??">Getting Emoji and multibyte characters on your Drupal 7 site with 7.50 ??</a>!</em></blockquote>

On many Drupal 7 sites, I have encountered issues with Emoji (mostly) and other special characters (rarely) when importing content from social media feeds, during content migrations, and in other situations, so I finally decided to add a quick blog post about it.

Have you ever noticed an error in your logs complaining about incorrect string values, with an emoji or other special character, like the following:

```
PDOException: SQLSTATE[HY000]: General error: 1366 Incorrect string value: '\xF0\x9F\x98\x89" ...' for column 'body_value' at row 1: INSERT INTO {field_data_body} (entity_type, entity_id, revision_id, bundle, delta, language, body_value, body_summary, body_format) VALUES (:db_insert_placeholder_0, :db_insert_placeholder_1, :db_insert_placeholder_2, :db_insert_placeholder_3, :db_insert_placeholder_4, :db_insert_placeholder_5, :db_insert_placeholder_6, :db_insert_placeholder_7, :db_insert_placeholder_8); Array ( [:db_insert_placeholder_0] => node [:db_insert_placeholder_1] => 538551 [:db_insert_placeholder_2] => 538550 [:db_insert_placeholder_3] => story [:db_insert_placeholder_4] => 0 [:db_insert_placeholder_5] => und [:db_insert_placeholder_6] => <p>?</p> [:db_insert_placeholder_7] => [:db_insert_placeholder_8] => filtered_html ) in field_sql_storage_field_storage_write() (line 514 of /drupal/modules/field/modules/field_sql_storage/field_sql_storage.module).
```

To fix this, you need to switch the affected MySQL table's encoding to <code>utf8mb4</code>, and also switch any table columns ('fields', in Drupal parlance) which will store Emojis or other exotic UTF-8 characters. This will allow these special characters to be stored in the database, and stop the PDOExceptions.

Using Sequel Pro on a Mac, this process is relatively quick and painless:

<ol>
<li>Open the affected tables (in the above case, <code>field_data_body</code>, and the corresponding revision table, <code>field_revision_body</code>), and click on the 'Table info' tab.</li>
<li>In the 'Encoding' menu, switch from "UTF-8 Unicode (utf8)" to "UTF-8 Unicode (utf8mb4)". This will take a little time for larger data sets.</li>
<li>Switch over to the 'Structure' tab, and for each field which will be storing data (in our case, the <code>body_value</code> and <code>body_summary</code> fields), choose "UTF-8 Unicode (utf8mb4)" under the 'Encoding' column. This will take a little time for larger data sets.</li>
</ol>

After converting the affected tables, you will also need to patch Drupal 7 to make sure the MySQL connection uses the correct encoding. Apply the latest patch from the issue <a href="https://www.drupal.org/node/2488180">Drupal 7 MySQL does not support full UTF-8</a>, and add the following keys to your default database connection settings:

```
<?php
$databases = array(
  'default' => array(
    'default' => array(
      'database' => 'database',
      'username' => 'username',
      'password' => 'password',
      'host' => '127.0.0.1',
      'driver' => 'mysql',
      // Add default charset and collation for mb4 support.
      'charset' => 'utf8mb4',
      'collation' => 'utf8mb4_general_ci',
    ),
  ),
);
?>
```

That issue is actually a child issue of <a href="https://www.drupal.org/node/1314214">MySQL driver does not support full UTF-8</a>, which has already been fixed in Drupal 8 (which now requires MySQL 5.5.3 or later as a result). It may take a little time for the problem to get an 'official' fix in Drupal 7, since it's a complicated problem that requires a delicate touch—we don't want a bunch of people's sites to go belly up because some contributed modules are using large VARCHAR columns, or because their hosting provider is running an old version of MySQL!

There's also a handy <a href="https://github.com/stovak/table_converter">table_converter</a> module for Drupal 7, which helps you automate the process of converting tables to the new format. It still requires the core patch mentioned above, but it can help smooth out the process of actually converting the tables to the new format.

Finally, if you want to write an update function to convert the tables yourself during a deployment (instead of manually converting tables using something like table_converter), you can use a function like the following in a custom module's <code>mymodule.install</code> file:

```
<?php
/**
 * Convert the `body` field to utf8mb4.
 */
function mymodule_update_N(&$sandbox) {
  db_query("ALTER TABLE {field_data_body} MODIFY body_value longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci");
  db_query("ALTER TABLE {field_data_body} MODIFY body_summary longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci");
  db_query("ALTER TABLE {field_revision_body} MODIFY body_value longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci");
  db_query("ALTER TABLE {field_revision_body} MODIFY body_summary longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci");
  field_cache_clear(TRUE);
}
?>
```

Once you've fixed the issue, you won't be quite as annoyed next time you see one of these guys: ?
