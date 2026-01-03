---
nid: 2358
title: "MySQL General Errors on MAMP/WAMP/XAMPP"
slug: "mysql-general-errors"
date: 2011-08-16T14:57:16+00:00
drupal:
  nid: 2358
  path: /blogs/jeff-geerling/mysql-general-errors
  body_format: filtered_html
  redirects: []
tags:
  - drupal
  - drupal 7
  - drupal planet
  - mysql
aliases:
  - /blogs/jeff-geerling/mysql-general-errors
---

I've been getting errors like <code>General error: Can't create/write to file</code>, <code>Error 2006: MySQL server has gone away</code>, and other similar PDOExceptions and errors from time to time while developing on my Mac using MAMP Pro (this seems to happen more often with Drupal 7 sites than Drupal 6, for reasons I know not). I've noticed a few other developers are getting these errors too, and almost always on local environments as opposed to live servers.

I found that the easiest way to deal with them is by giving MySQL a nice buffer of memory via the <code>max_allowed_packet</code> and <code>innodb_buffer_pool_size</code> settings. Just bump those up to 256M or higher, and the errors above should go away. (In MAMP Pro, just go to File > Edit Templates > my.cnf, and search for those variables. Uncomment the innodb_buffer_pool_size variable if it's commented out.

Typically this only happens if you're working with rather large databases, or if you're doing things like clearing all caches with a low max_allowed_packet size. Some people drop the entire database and reimport, but that seems like overkill to me—especially since I can always throw more RAM at a problem!

Further reading: <a href="http://dev.mysql.com/doc/refman/5.0/en/gone-away.html">MySQL has gone away</a> [MySQL Reference Manual]
