---
nid: 2670
title: "Getting Emoji and multibyte characters on your Drupal 7 site with 7.50"
slug: "getting-emoji-and-multibyte-characters-on-your-drupal-7-site-750"
date: 2016-07-08T15:43:50+00:00
drupal:
  nid: 2670
  path: /blog/2016/getting-emoji-and-multibyte-characters-on-your-drupal-7-site-750
  body_format: markdown
  redirects:
    - /blog/2016/getting-emoji-and-multibyte-characters-on-your-drupal-7-site-750-??
aliases:
  - /blog/2016/getting-emoji-and-multibyte-characters-on-your-drupal-7-site-750-??
tags:
  - drupal
  - drupal 7
  - drupal planet
  - emoji
  - mysql
  - utf8
  - utf8mb4
---

> Edit: Updated blog post title to remove the Emoji (??) since it was breaking Drupal.org's Planet aggregator... hopefully once Drupal.org is upgraded to 7.50 I won't have to do that again :)
>
> Also note that you don't _have_ to enable utf8mb4 support if you get a warning on your Drupal 7 site's status page; it's just a helpful suggestion. Everything besides emoji/special character support still works fine whether your convert your database or not!

Almost exactly a year ago, I wrote a blog post titled [Solving the Emoji/character encoding problem in Drupal 7](http://www.jeffgeerling.com/blogs/jeff-geerling/solving-emoji-problem-drupal-7).

Since writing that post, Drupal 7 bugfixes and improvements have started to pick up steam as (a) many members of the community who were focused on launching Drupal 8 had time to take a breather and fix up some long-standing Drupal 7 bugs and improvements that hadn't yet been backported, and (b) there are [two new D7 core maintainers](https://groups.drupal.org/node/512271). One of the patches I've been applying to many sites and hoping would get pulled into core for a long time was [adding support for full UTF-8](https://www.drupal.org/node/2761183), which allows the entry of emojis, Asian symbols, and mathematical symbols that would break Drupal 7 sites running on MySQL previously.

My old blog post had a few steps that you could follow to make your Drupal 7 site 'mostly' support UTF-8, but there were some rough edges. Now that support is in core, the process for converting your existing site's database is more straightforward:

  1. Back up your database (and perform this process in a test environment before on your production site if at all possible).
  2. Prepare MySQL by making sure the following three settings are in `my.cnf` (then restart MySQL). You need to have MySQL > 5.5 to do this:

        [mysqld]
        innodb_large_prefix=true
        innodb_file_format=barracuda
        innodb_file_per_table=true

  3. Install the drush command to convert your site's databases: `drush @none dl utf8mb4_convert-7.x`
  4. Convert your site's databases, one Drupal site/settings.php at a time (run this command from a site's docroot): `drush --uri=http://www.example.com/ utf8mb4-convert-databases`
  5. Add `charset` and `collation` settings to each database in your site settings.php:

        $databases['default']['default'] = array(
          'database' => 'databasename',
          ...
          'charset' => 'utf8mb4',
          'collation' => 'utf8mb4_general_ci',
        );

  6. Upgrade your Drupal codebase to 7.50.
  7. Run database updates to make sure everything is correct.

Once that's done, you'll be able to add whatever characters you'd like, like the smiling pile of poo: ?

I was testing the 'alpha2' release of the utf8mb4_convert Drush command and found some issues with converting really old Drupal 5->6->7 databases, but those have since been resolved (<a href="https://www.drupal.org/node/2762599">thanks, stefan.r!</a>), and a new era of emojification is upon us!
