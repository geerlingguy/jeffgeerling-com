---
nid: 2515
title: "Drupal 8 with Redis, PHP 7, Nginx, and MariaDB on Drupal VM using CentOS"
slug: "drupal-8-redis-php-7-nginx-and"
date: 2015-12-15T14:35:35+00:00
drupal:
  nid: 2515
  path: /blogs/jeff-geerling/drupal-8-redis-php-7-nginx-and
  body_format: full_html
  redirects: []
tags:
  - development
  - drupal
  - drupal 8
  - drupal planet
  - drupal vm
  - mariadb
  - nginx
  - redis
aliases:
  - /blogs/jeff-geerling/drupal-8-redis-php-7-nginx-and
---

One of the motivations behind <a href="http://www.drupalvm.com/">Drupal VM</a> is flexibility in local development environments. When you develop many different kinds of Drupal sites you need to be able to adapt your environment to the needs of the site—some sites use Memcached and Varnish, others use Solr, and yet others cache data in Redis!

Drupal VM has recently gained much more flexibility in that it now allows configuration options like:

<ul>
<li>Choose either Ubuntu or CentOS as your operating system.</li>
<li>Choose either Nginx or Apahe as your webserver.</li>
<li>Choose either MySQL or MariaDB for your database.</li>
<li>Choose either Memcached or Redis as a caching layer.</li>
<li>Add on extra software like Apache Solr, Node.js, Ruby, Varnish, Xhprof, and more.</li>
</ul>

Out of the box, Drupal VM installs Drupal 8 on Ubuntu 14.04 with PHP 5.6 (the most stable release as of December 2015) and MySQL. We're going to make a few quick changes to <code>config.yml</code> so we can run the following local development stack on top of CentOS 7:

<p style="text-align: center;">{{< figure src="./drupal-vm-centos-nginx-php7-drupal8-redis.png" alt="Drupal VM - Drupal 8 status report page showing Nginx, Redis, MariaDB, and PHP 7" width="550" height="302" >}}</p>

<h2>Configure Drupal VM</h2>

To get started, download or clone a copy of Drupal VM, and follow the <a href="https://github.com/geerlingguy/drupal-vm#quick-start-guide">Quick Start Guide</a>, but before you run <code>vagrant up</code> (step 2, #6), edit <code>config.yml</code> and make the following changes/additions:

```
# Update vagrant_box to use the geerlingguy/centos7 box.
vagrant_box: geerlingguy/centos7

# Update drupalvm_webserver to use nginx instead of apache.
drupalvm_webserver: nginx

# Make sure 'redis' is listed in installed_extras, and memcached, xhprof, and
# xdebug are commented out.
installed_extras:
  [ ... ]
  - redis

# Switch the PHP version to "7.0".
php_version: "7.0"

# Add the following variables to the end of the file to make sure the PhpRedis
# extension is compiled to run with PHP 7.
php_redis_install_from_source: true
php_redis_source_version: php7

# Add the following variables to the 'MySQL Configuration' section to make sure
# the MariaDB installation works correctly.
mysql_packages:
  - mariadb
  - mariadb-server
  - mariadb-libs
  - MySQL-python
  - perl-DBD-MySQL
mysql_daemon: mariadb
mysql_socket: /var/lib/mysql/mysql.sock
mysql_log_error: /var/log/mariadb/mariadb.log
mysql_syslog_tag: mariadb
mysql_pid_file: /var/run/mariadb/mariadb.pid
```

To make Drupal use Redis as a cache backend, you have to include and enable the Redis module on your site. The official repository on Drupal.org doesn't currently have a Drupal 8 branch, but there's a fork on GitHub that currently works with Drupal 8. We need to add that module to the <code>drupal.make.yml</code> make file. Add the following just after the line with <code>devel</code>:

```
  devel: "1.x-dev"
  redis:
    download:
      type: git
      url: https://github.com/md-systems/redis.git
      branch: 8.x-1.x
```

Run <code>vagrant up</code>, and wait for everything to install inside the VM. After a bit, you can visit http://drupalvm.dev/, and log in (username <code>admin</code> and password <code>admin</code>). Go to the 'Extend' page, and enable the Redis module.

Once the module is enabled, you'll need to follow the Redis module's installation guide to make Drupal actually <em>use</em> Redis instead of MariaDB for persistent caching. The basic steps are:

<ol>
<li>Create a new file <code>services.yml</code> inside the Drupal 8 codebase's <code>sites/default</code> folder, with the following contents:

```
services:
  cache_tags.invalidator.checksum:
    class: Drupal\redis\Cache\RedisCacheTagsChecksum
    arguments: ['@redis.factory']
    tags:
      - { name: cache_tags_invalidator }
</code></li>
<li>Open <code>sites/default/settings.php</code> and add the following to the end of the file:
<code>
$settings['redis.connection']['interface'] = 'PhpRedis';
$settings['redis.connection']['host'] = '127.0.0.1';
$settings['cache']['default'] = 'cache.backend.redis';
</code></li>
</ol>

Once you've made those changes, go to the performance page (http://drupalvm.dev/admin/config/development/performance) and click the 'Clear all caches' button. If you log into the VM (<code>vagrant ssh</code>), then run the command <code>redis-cli MONITOR</code>, you can watch Drupal use Redis in real-time; browse the site and watch as Redis reports all it's caching data to your screen.

<h2>Benchmarking Redis, PHP 7, and Drupal 8</h2>

These are by no means comprehensive benchmarks, but the results are easily reproducible and consistent. I used ApacheBench (<code>ab</code>) to simulate a single authenticated user requesting the <code>/admin</code> page as quickly as possible.

<code>
# ApacheBench command used:
ab -n 750 -c 10 -C "SESSxyz=value" http://drupalvm.dev/admin
```

With these settings, Drupal VM's CPU usage was pegged at 200%, and it reported the following results (averaged over three runs):

<table>
<thead>
<tr>
  <th>Cache location</th>
  <th>PHP version</th>
  <th>Requests/second</th>
  <th>Percent difference</th>
</tr>
</thead>
<tr>
  <td>MariaDB</td>
  <td>5.6.16</td>
  <td><strong>21.86 req/s</strong></td>
  <td>~</td>
</tr>
<tr>
  <td>Redis</td>
  <td>5.6.16</td>
  <td><strong>21.34 req/s</strong></td>
  <td>2% slower</td>
</tr>
<tr>
  <td>MariaDB</td>
  <td>7.0.0</td>
  <td><strong>30.32 req/s</strong></td>
  <td>32% faster</td>
</tr>
<tr>
  <td>Redis</td>
  <td>7.0.0</td>
  <td><strong>34.64 req/s</strong></td>
  <td>45% faster</td>
</tr>
</table>

Assuming you're using PHP 7, there's approximately a 13% performance boost using a local Redis instance rather than a local database to persist Drupal 8's cache. This falls in line with my findings in a related project, when I was <a href="https://github.com/geerlingguy/raspberry-pi-dramble/wiki/Dramble-D8-Benchmarks">building a cluster of Raspberry Pis to run Drupal 8</a> and found Redis to speed things up by about 15%!

It's odd that PHP 5.6 benchmarks showed a very slight performance <em>decrease</em> when using Redis, but I'm wondering if that's because the PhpRedis extension had some optimizations in its <code>php7</code> branch that weren't present in the older compiled versions.

It's important to run your <em>own</em> benchmarks in your <em>own</em> environment, to make sure the performance optimizations are worth the extra applications running on your infrastructure... and that they're actually helping your Drupal site run <em>better</em>, not <em>worse</em>!

<h2>Summary</h2>

I hope Drupal VM can help you build a great local development environment; I have been using it for every Drupal project I work on, and have even taken to using it as a base for building out single-server Drupal infrastructure as-needed, by removing roles and settings I don't need, and enabling the extra security settings, and it has served me well.

If there's anything you see missing from Drupal VM that would make your local Drupal development experience easier, please take a look in the issue queue and let me know what else you'd like to see!
