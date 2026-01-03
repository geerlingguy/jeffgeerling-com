---
nid: 2445
title: "Dump an entire database with structure only for some tables with mysqldump"
slug: "dump-entire-database-structure"
date: 2014-02-12T18:39:22+00:00
drupal:
  nid: 2445
  path: /blogs/jeff-geerling/dump-entire-database-structure
  body_format: full_html
  redirects: []
tags:
  - cli
  - database
  - export
  - mysql
  - mysqldump
  - structure
---

I typically use a MySQL GUI like <a href="http://www.sequelpro.com/">Sequel Pro</a> when I do database dumps and imports working from my Mac. GUI apps often give checkboxes that allow you to choose whether to include the structure/content/drop table command for each table in an export.

When using <code>mysqldump</code> on the command line, though, it's not as simple. You can either do a full dump and exclude a few tables entirely (using <code>--ignore-table</code>, or dump the structures of just one set of tables using the <code>-d</code> option. But you can't do both in one go with <code>mysqldump</code>.

However, you can use the power of redirection to do both commands at once to result in one dump file with all your tables, with structure only for the tables you specify:

```
mysqldump -u username -p -h hostname database \
--ignore-table=database.cache_form\
--ignore-table=database.cache_entity_node\
--ignore-table=database.cache_views_data\
--ignore-table=database.sessions\
--ignore-table=database.watchdog\
 > ~/Desktop/database-dump.sql\
 && mysqldump -u username -p -h hostname -d database \
cache_form \
cache_entity_node \
cache_views_data \
sessions \
watchdog \
 >> ~/Desktop/database-dump.sql
```

The <code>\</code> at the end of the line tells your terminal session to continue to the next line (for the sake of clarity, I don't like printing long commands one one super-long line!), and I'll explain what's happening line by line:

First, we use the mysqldump command, passing in the username (<code>username</code>, hostname (<code>hostname</code>), and database name (<code>database</code>), and password (just use the <code>-p</code> argument, so you'll be prompted for your password).

Next, we give this first command a list of tables to ignore completely—no data or structure for these tables will be included in the dump.

We direct mysqldump's output to a file named <code>database-dump.sql</code> in our Desktop folder.

Then, we give another mysqldump command (<code>&&</code> tells bash to run the following after the first command completes), and pass in the same info, except this time we add in <code>-d</code>, which tells mysqldump to exclude table data for the list of tables defined after the database (<code>database</code>).

We pass in the list of tables (just plain old text strings with spaces between each one), and redirect the output with two greater than signs (<code>>></code>)—which appends rather than replaces the contents of a file—into the same database dump we started filling up in our first mysqldump command.

If you're going to use this command a lot, you should probably put it in a shell script and pass in arguments (<code>$1</code>, <code>$2</code>, <code>$3</code>, etc.) for the parameters like the username, host, database, and output file. You could also compile the list of tables a little nicer, but that's outside the scope of this blog post.

Note that, if you're using Drupal, you should use drush's <code>skip-tables</code> and <code>structure-tables</code> configuration to do the same thing with drush sql commands, but much more easily.

Some helpful hints leading to this successful command were gleaned from <a href="http://stackoverflow.com/a/4832571/100134">this SO post</a>.
