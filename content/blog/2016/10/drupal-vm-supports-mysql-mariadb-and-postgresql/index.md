---
nid: 2702
title: "Drupal VM supports MySQL, MariaDB, and PostgreSQL"
slug: "drupal-vm-supports-mysql-mariadb-and-postgresql"
date: 2016-10-01T18:52:49+00:00
drupal:
  nid: 2702
  path: /blog/2016/drupal-vm-supports-mysql-mariadb-and-postgresql
  body_format: markdown
  redirects: []
tags:
  - database
  - drupal
  - drupal 8
  - drupal planet
  - drupal vm
  - postgresql
---

<p style="text-align: center;"><a href="https://www.postgresql.org/">{{< figure src="./Postgresql_elephant.png" alt="PostgreSQL elephant transparent PNG" width="200" height="206" class="insert-image" >}}</a><br>
<em>The <a href="https://wiki.postgresql.org/wiki/Logo">PostgreSQL logo</a>. Same family as <a href="http://php.net/elephpant.php">PHP's mascot</a>!</em></p>

For the past few years, I've been intending to kick the tires of PostgreSQL, an open source RDBMS (Relational DataBase Management System) that's often used in place of MySQL, MariaDB, Oracle, MS SQL, or other SQL-compliant servers. Drupal 7 worked with PostgreSQL, but official support was a bit lacking. For Drupal 8, [daily automated test builds](https://www.drupal.org/node/3060/qa) are finally being run on MySQL, SQLite, and PostgreSQL, so many of the more annoying bugs that caused non-MySQL database engines to fail have finally been fixed!

With [Drupal VM](https://www.drupalvm.com/), one of my goals is to be able to replicate almost any kind of server environment locally, supporting _all_ of the most popular software. Developers have already been able to choose Apache or Nginx, Memcached, or Redis, Varnish, Solr or Elasticsearch, and many other options depending on their needs. Today I finally had the time to nail down PostgreSQL support, so now developers can choose which database engine they'd like—MySQL, MariaDB, PostgreSQL, or even SQLite!

As of [Drupal VM 3.3.0](https://github.com/geerlingguy/drupal-vm/releases/tag/3.3.0), all four are supported out of the box, though for [MariaDB](http://docs.drupalvm.com/en/latest/extras/mariadb/) or [PostgreSQL](http://docs.drupalvm.com/en/latest/extras/postgresql/), you need to adjust a couple settings in your `config.yml` before provisioning.

If you want to build a VM running Drupal 8 on PostgreSQL, the process is pretty simple:

  1. [Download Drupal VM](https://www.drupalvm.com/) and follow the [Quick Start Guide](https://github.com/geerlingguy/drupal-vm#quick-start-guide).
  2. Before running `vagrant up`, create a `config.yml` file with the contents:

```
---
drupalvm_database: pgsql
```

  3. Run `vagrant up`.

After a few minutes, you should have a new Drupal 8 site running on top of PostgreSQL!

<p style="text-align: center;">{{< figure src="./postgresql-db-engine-drupal-status-report.png" alt="PostgreSQL database engine Drupal 8 status report page" width="400" height="157" class="insert-image" >}}</p>

## A few caveats

You should note that, just like with support for Apache vs. Nginx<sup>1</sup>, there are far fewer Drupal sites running on PostgreSQL than on MySQL (or MariaDB), so if you choose to use PostgreSQL, you'll likely encounter a bump in the road at some point. For example, to get PostgreSQL working at all with Drupal, the database has to use an older PostgreSQL default output method that uses ASCII instead of hex (the default since PostgreSQL 9.0) for transmission.

If you're planning on digging deeper in to PostgreSQL with Drupal (especially if you need to support things like spatial and geographic objects, or full-text search, and don't want to add on Apache Solr or something like it), you should read through this meta issue for Drupal 8: [[meta] Remaining Drupal 8 PostgreSQL issues](https://www.drupal.org/node/2564307).

## Learn More

  - [Drupal VM docs - using PostgreSQL](http://docs.drupalvm.com/en/latest/extras/postgresql/)
  - [Drupal VM issue - add PostgreSQL support](https://github.com/geerlingguy/drupal-vm/issues/146)
  - [PostgreSQL documentation](https://www.postgresql.org/docs/)
  - [[meta] Remaining Drupal 8 PostgreSQL issues](https://www.drupal.org/node/2564307)

<hr>

<sup>1</sup> _Historically_, Apache was used by the vast majority of Drupal sites, so many Drupal features, documentation, and hosting providers assume Apache and either don't consider Nginx configuration, or give it 'second-class' status. That's not to say it's _not_supported... just that you often need to do some of your own due diligence to get everything working smoothly and securely when not using the default option!
