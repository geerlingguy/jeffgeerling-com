---
nid: 2412
title: "Quickly resetting a local MySQL database from the command line [Updated]"
slug: "quickly-resetting-local-mysql"
date: 2013-06-25T04:17:01+00:00
drupal:
  nid: 2412
  path: /blogs/jeff-geerling/quickly-resetting-local-mysql
  body_format: full_html
  redirects: []
tags:
  - database
  - drupal
  - drupal planet
  - drush
  - mysql
  - shell
---

[<strong>Update</strong>: And, as quickly as I finished writing this post, I thought to myself, "surely, this would be a good thing to have drush do out-of-the-box. And... it already does, making my work on this shell script null and void. I present to you: <a href="http://drush.ws/#sql-drop"><code>drush sql-drop</code></a>! Oh, well.]

When I'm creating or updating an installation profile/distribution for Drupal, I need to reinstall Drupal over and over again. Doing this requires a few simple steps: drop/recreate the database (or drop all db tables), then <a href="https://drupal.org/documentation/install/developers"><code>drush site-install</code></a> (shortcut: <code>si</code>) with the proper arguments to install the site again.

In the past, I've often had <a href="http://www.sequelpro.com/">Sequel Pro</a> running in the background on my Mac, and I'd select all the database tables, right-click, choose 'Delete Tables', then have to click again on a button to confirm the deletion. This took maybe 10-20 seconds, depending on whether I already had Sequel Pro running, and how good my mouse muscles were working.

I created a simple shell script that works with MAMP/MAMP Pro on the Mac (but can easily be modified to work in other environments by changing a few variables), which simply drops all tables for a given database:

```
#!/bin/bash
#
# Drop all tables from a given database.
#

# Some variables.
MYSQL=/Applications/MAMP/Library/bin/mysql
AWK=$(which awk)
GREP=$(which grep)
USER="valid-username-here"
PASSWORD="your-password-here"

# Database (argument provided by user).
DATABASE="$1"

# Require the database argument.
[ $# -eq 0 ] && {
  echo "Please specify a valid MySQL database: $0 [database_goes_here]" ;
  exit 1;
}

# Drop the given database with mysql on the commind line.
TABLES=$($MYSQL -u $USER -p$PASSWORD $DATABASE -e 'show tables' | $AWK '{ print $1}' | $GREP -v '^Tables')
for TABLE in $TABLES
do
  # echo "Deleting $TABLE table from $DATABASE..."
  $MYSQL -u $USER -p$PASSWORD $DATABASE -e "DROP TABLE $TABLE"
done
```

I named the script wipe-db.sh, and you can call it like so: <code>$ /path/to/wipe-db.sh database-name</code>. I added a symlink to the script inside my /usr/local/bin folder so I can just type in 'wipe-db' in the Terminal instead of entering the full path. To add the symlink:

```
$ ln -s /path/to/wipe-db.sh /usr/local/bin/wipe-db
```

Now I can wipe the database tables within a couple seconds, since I always have Terminal running, and I never have to reach for the mouse!
