---
nid: 3356
title: "Fixing nginx Error: Undefined constant PDO::MYSQL_ATTR_USE_BUFFERED_QUERY"
slug: "fixing-nginx-error-undefined-constant-pdomysqlattrusebufferedquery"
date: 2024-03-12T04:57:08+00:00
drupal:
  nid: 3356
  path: /blog/2024/fixing-nginx-error-undefined-constant-pdomysqlattrusebufferedquery
  body_format: markdown
  redirects: []
tags:
  - cli
  - drupal
  - errors
  - mysql
  - php
---

I install a _lot_ of Drupal sites day to day, especially when I'm doing dev work.

In the course of doing that, sometimes I'll be working on infrastructure—whether that's an Ansible playbook to configure a Docker container, or testing something on a fresh server or VM.

In any case, I run into the following error every so often in my Nginx `error.log`:

```
"php-fpm" nginx Error: Undefined constant PDO::MYSQL_ATTR_USE_BUFFERED_QUERY
```

The funny thing is, I _don't_ have that error when I'm running CLI commands, like `vendor/bin/drush`, and can even install and manage the Drupal site and database on the CLI.

The problem, in my case, was that I had applied `php-fpm` configs using Ansible, but in my playbook I hadn't restarted `php-fpm` (in my case, on Ubuntu 22.04, `php8.3-fpm`) after doing so. So FPM was running with outdated config and didn't know that the MySQL/MariaDB drivers were even present on the system.

There are tons of forum posts, Drupal Answers posts, etc. saying the resolution to the issue was installing `php8.3-mysql` or the like, but if you're using PHP-FPM, make sure you have the MySQL ini added to the PHP config (use `php -i` to check your config paths), and make sure you've restarted PHP-FPM. Same thing with restarting Apache if you're using the built-in PHP support there.

Why did I post this blog post? Because after the fourth time I've run into this—spending on average like 30 minutes each time diagnosing the issue—I figured I'd write my own blog post so I find the solution I needed more quickly next time :)
