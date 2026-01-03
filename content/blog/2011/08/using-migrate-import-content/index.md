---
nid: 2331
title: "Using Migrate to Import Content from a Legacy Database"
slug: "using-migrate-import-content"
date: 2011-08-26T15:34:02+00:00
drupal:
  nid: 2331
  path: /blogs/jeff-geerling/using-migrate-import-content
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal 7
  - drupal planet
  - flocknote
  - migrate
  - migrate extras
aliases:
  - /blogs/jeff-geerling/using-migrate-import-content
---

Since a few people who missed <a href="http://groups.drupal.org/node/169659">last night's St. Louis Drupal meetup</a> wanted to hear more about <a href="http://drupal.org/project/migrate">Migrate module</a> and my notes from a recent content migration for flockNote, I thought I'd post my observations and some tips here.

<h2>Migrate Module, v2</h2>

My prior experience with Migrate was on version 1.x, along with <a href="http://drupal.org/project/tw">Table Wizard</a>, for Drupal 6 (I used it in tandem with a bunch of CSV files that were used to import organizational data into the <a href="http://archstl.org/">Archdiocese of St. Louis'</a> website). A lot has changed in the process of Migrate upgrading from 1.x to 2.x... especially with Drupal 7!

Whereas in Drupal 6/Migrate 1.x, I had to define table relationships and definitions via Table Wizard + Views (which in itself was slightly tedious), and had to have all the tables in the same database as the Drupal site (making for a very bloated database), with Migrate 2.x, there are no dependencies—you can perform the entire Migration process with Drupal core and Migrate module (if you'd like). I'd highly recommend the <a href="http://drupal.org/project/migrate_extras">Migrate Extras</a> module as well, though, as it helps with a ton of non-core field types and features.

Migrate 2 is entirely object-oriented in its design (which is a very good thing!), but this means that when you add your own migrations in a custom module, you need to identify any files you have extending the Migration classes in your module's .info file. Also, as of yet, there is no way to define migration mappings in the interface (like there was in 6.x-1.x), so everything needs to be done in code (this is being worked on: <a href="http://drupal.org/node/1123538">UI for defining migrations</a>). There is a UI to monitor migration progress, import, rollback, and reset migrations, but drush is the preferred way to do all of these processes.

I'm not going to get in all the nitty-gritty details of Migrate in this post; I defer to the already thorough <a href="http://drupal.org/node/415260">documentation for Migrate on drupal.org</a>.

<h2>Migrating flockNote</h2>

<a href="http://www.flocknote.com/">flockNote</a> is a communication tool/resource specifically for Catholic parishes and organizations, and currently has thousands of nodes, many thousands of members (users), and over a hundred thousand other data points in the legacy database (many of which were able to be filtered out pre-migrate as they contained duplicate or expired data). I needed to get all that data into a new Drupal site I had been working on over the past few months, and a lot of the migration process involved handling interesting content relationships, taming data that had changed schemas from time to time, and many different types of data.

<p style="text-align: center;">{{< figure src="./migration-final.png" width="600" height="366" >}}
Image of the results of the full Migration of flockNote data. Only took a few hours!</p>
For each migration (migrating pictures, then files, then users, then userprofiles (in tandem with <a href="http://drupal.org/project/profile2">Profile2</a>), node types, private messages (in tandem with <a href="http://drupal.org/project/privatemsg">Privatemsg</a>) and comments), I created a separate 'fn_migrate.TYPE.inc' file in my custom fn_migrate module. Each file began with my own class (for example, UserMigration) extending the Migration class. Inside this new class definition, each migration is basically the same, and is simple from a high-level perspective:

<ol>
	<li>In the construct() method:

<ol>
	<li>Describe the migration.</li>
	<li>Define the source of the migration (in my case, a database table, so I just used Database::getConnection() to connect to a copy of the old database). You can import from databases, CSV files, XML files, or other sources.</li>
	<li>Define the destination of the migration (in the case of a user, MigrateDestinationUser).</li>
	<li>Make sure your source and destination will have primary keys (for rollback operations, speed of import, etc.), and map those using MigrateSQLMap.</li>
	<li>Define field mappings (simple: $this-&gt;addFieldMapping('new_field', 'old_field); – though you can also define default values or other source migrations in this part of the process.</li>
</ol></li>
	<li>In the prepareRow() method:

<ol>
	<li>Preprocess any rows that might need to be changed or fixed to fit your new data schema. For example, on the new site, link fields that don't have a value are NULL. In the incoming data, empty links actually had a value of 'http://' - so in prepareRow(), I emptied out the value of a link field if it had 'http://' as its value.</li>
</ol></li>
	<li>In the complete() method:

<ol>
	<li>Operate on the final record/object that was imported - for example, you could take a $node object and do something with it for another bit of custom functionality.</li>
</ol></li>
</ol>

That's a pretty simple high-level overview of a migration definition. There are more methods than these, but almost every migration I defined implemented those three methods (most of the work was done in construct() and prepareRow()).

<h2>Migrate Tips</h2>

<ul>
	<li><strong>Referencing content of the same type:</strong> For one content type ('Lists'), the content could reference other nodes of the same content type... this could present a problem if, during the migration, a node referenced another node that hadn't been imported yet. What do we do? Migrate handles this pretty easily, by creating a 'Stub' node that it will reference, then import later in the process. Read <a href="http://drupal.org/node/1013506">Chickens and eggs: using stubs</a> for more info. (Basically, you implement a createStub() method and tell Migrate how to create the stub node - Migrate handles the rest).</li>
	<li><strong>Mapping data from old to new:</strong> Migrate keeps a map of all the old data to the new data (it's important to have a primary key in the old data so you can track things easily!), and while importing, if you have a field that needs to be mapped to your new data (for example, the author of a node should be mapped using an earlier User Migration, just define the field mapping thusly: $this-&gt;addFieldMapping('uid', 'old_author_id')-&gt;sourceMigration('User');</li>
	<li><strong>Can't handle a specific field mapping?</strong> <a href="http://drupal.org/project/migrate_extras">Migrate Extras</a> provides field handlers for tons of contrib Field types and other data (like Privatemsg messages). It's still being tidied up, and many fields don't have proper mappings yet, but you can usually hack something together to get a migration working for things like the <a href="http://drupal.org/project/cck_phone">Phone</a> fields and other structured fields. In my case, (with the help of <a href="http://drupal.org/user/36598">joelstein</a>), I used a 'JeffFieldHandler' that extended&nbsp;MigrateFieldHandler, for fields of type 'link_field', 'phone_number', and 'addressfield' (since those three field types have similar data structures).</li>
	<li><strong>Use the UI for a quick reference:</strong> Keep checking in with the UI to quickly view Migrate messages and warnings, and click on a migration name to view field mapping data (especially handy for seeing which fields you haven't mapped yet, or extra fields you should specify as unneeded).</li>
	<li><strong>Use drush for everything else:</strong> Drush is powerful... and Drush and Migrate are powerful when you're migrating. Here's a handy <a href="http://cyrve.com/import">reference of Migrate Drush commands</a> (a little out of date as of this writing).</li>
</ul>

<h2>Migration Speed/Performance Optimizations</h2>

Migration is a very demanding process on any system, as MySQL and PHP are typically doing a lot of things. Migration can be especially slow if your environment is not configured very well. One small change, tweaking the amount of memory (memory_limit) available to php-cli (from 256 MB to 1 GB), reduced the Migrate time by about 25%, because memory limits were hit less often.

Additionally, you may want to tweak my.cnf to disable some InnoDB row logging and caching during the migration, in order to speed up inserts. (Have a look-see at MySQL's <a href="http://dev.mysql.com/doc/refman/5.0/en/innodb-tuning.html">InnoDB Performance Tuning tips</a>).

Finally, if you can possibly do migration processes (especially one large batch import, like I did at the end for flockNote) on a super-fast machine with an SSD, and then push the database to your live server, that's a good way to avoid a super-long migration process. What took about 4 hours on my MacBook Pro with a 6G SSD (which has very fast seek/write times) took about 8-10 hours on our production server (because of it's measly little RAID array with spinning disks). It was a lot faster doing the import on my Mac, then uploading the gzipped sql dump to the server (using drush sql-sync).

<h2>Feeds vs. Migrate</h2>

A lot of people seem to think that <a href="http://drupal.org/project/feeds">Feeds</a> and Migrate are opposed to each other, but I beg to differ. On one site, I'm actually using both at the same time for different purposes. Migrate is used to import a continuously changing dataset for an organizational directory for an old MSSQL database, and Feeds is used to aggregate RSS feeds from some other sites into the site.

Feeds can be used for content import/migration, but in my opinion, it's better suited for smaller/simpler migrations, or continuous migration (updating content from RSS feeds, XML files, etc.), whereas Migrate is built more for large (or insanely large) content or data migrations from old sites to new sites, or from entirely different schemas, with minimal hassle and maximum speed.

The truth is, Feeds was built as a way to import 'feeds'—XML, RSS, ATOM, etc.—and that's what it does best. Migrate was built to move legacy content into Drupal... and that's what <em>it</em>&nbsp;does best. I'm not one to try stretching one module into every use case I can find. Just use the right module for the job :-)

<em>I hope to write up a case study for drupal.org regarding flockNote soon (there are a lot of great things to show!)... just need more time for writing!</em>
