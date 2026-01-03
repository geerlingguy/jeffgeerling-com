---
nid: 2417
title: "Reclaim Your Hard Drive - Saving Tons of Space with MySQL InnoDB tables"
slug: "reclaim-your-hard-drive-saving"
date: 2012-08-11T17:58:21+00:00
drupal:
  nid: 2417
  path: /blogs/jeff-geerling/reclaim-your-hard-drive-saving
  body_format: full_html
  redirects: []
tags:
  - database
  - drupal
  - drupal 7
  - drupal planet
  - innodb
  - mysql
aliases:
  - /blogs/jeff-geerling/reclaim-your-hard-drive-saving
---

Drupal 7 <a href="http://drupal.org/node/301362">uses InnoDB tables</a>. InnoDB provides many benefits, but can cause some unexpected headaches. One headache for me is that, by default, MySQL tells InnoDB to create one file on your system, called <code>ibdata1</code>, to hold ALL the data from EVERY InnoDB table you have on your MySQL server. This file <strong>never shrinks in size</strong>; it only expands to contain new data. If you delete something from MySQL or drop a table, the space that table was using is reallocated for other new data. This isn't a bad thing, especially for those who have a lot of drive space, and not many databases that are altered or dropped quite frequently.

I develop a lot of sites on my little MacBook Air (with a 128GB SSD), so I often download database snapshots from live and testing environments, empty out the tables on my local environment, then import the database dumps. Can you spot the problem here?

Using <a href="http://daisydiskapp.com/">Daisy Disk</a> I just noticed that my <code>ibdata1</code> file had grown to more than 10 GB, and my Air's drive only had about 5 GB free space!

So, after reading through MySQL's <a href="http://dev.mysql.com/doc/refman/5.0/en/innodb-storage-engine.html">InnoDB Engine documentation</a> and <a href="http://stackoverflow.com/a/3456885/100134">this answer</a> on Stack Overflow, I found that it's not too hard to change MySQL to keep data tables in their own files, and delete the files after the tables are deleted (thus saving me a ton of space). It just takes a little time and annoyance.

Here's how to do it, roughly:

<ol>
	<li><strong>Export/dump all your databases.</strong> (In my case, I didn't do this, since I could just grab them all from production or development servers.) If you have a good backup and restoration system in place, you shouldn't need to fret too much about this part, but if you don't, you'll probably need to spend a bit of time dumping each database or writing a script to do this for you.</li>
	<li><strong>Drop (delete) all databases</strong>, except for the mysql database, and information_schema, if it exists.</li>
	<li><strong>Shut down MySQL.</strong></li>
	<li><strong>Delete the <code>ibdata1</code> file and any <code>ib_logfile</code> log files</strong> (I just had <code>ib_logfile0</code> and <code>ib_logfile1</code>).</li>
	<li><strong>Add <code>innodb_file_per_table</code></strong> under the [mysqld] heading in your my.cnf file.</li>
	<li><strong>Start MySQL.</strong></li>
	<li><strong>Import all your databases.</strong></li>
</ol>

After doing this, my 'mysql' directory with all my databases only took up about 3 GB (there are a few large databases I regularly work with... but +/-3 GB is a lot less painful than 10+ GB!

I also took this opportunity to flush out some other testing databases that I had on my local computer for Drupal 4.7 (really!), 5, 6, 7 and 8 testing. It's easy enough to create a new database when the need arises, and with drush, it's easier than ever to create and sync databases and files for my Drupal sites.

On most of the production servers I manage, I don't worry about setting innodb_file_per_table, because there are often only one, two or three databases, and they aren't constantly changing like on my local computer—they only grow over time, so the ever-increasing size of the ibdata1 file isn't concerning to me.
