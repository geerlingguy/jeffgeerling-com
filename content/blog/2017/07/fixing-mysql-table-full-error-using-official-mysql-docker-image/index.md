---
nid: 2792
title: "Fixing MySQL 'The table is full' error using the official MySQL Docker image"
slug: "fixing-mysql-table-full-error-using-official-mysql-docker-image"
date: 2017-07-05T17:34:27+00:00
drupal:
  nid: 2792
  path: /blog/2017/fixing-mysql-table-full-error-using-official-mysql-docker-image
  body_format: markdown
  redirects: []
tags:
  - database
  - docker
  - import
  - mysql
---

Recently I had to test importing some very large databases with lots of giant log tables (e.g. 5+ GB tables), and when I tried doing an import into a local docker MySQL container instance, I got `ERROR 1114: The table is full`. Here are the commands I used:

```
# Run a MySQL container locally to test a large file import.
$ docker run --name mysql-import-test -p 3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=database_name -d mysql:latest

# Import a database .sql file and monitor progress with pv.
$ pv ~/database.sql | mysql -u root -proot -h 127.0.0.1 --port 32774 database_name
ERROR 1114 (HY000) at line 93898: The table 'xyz' is full
```

I found that—likely due to some Docker filesystem defaults—the MySQL import would fail every time when there was a database table containing more than 1GB of data. Now, this could be related to the way the database was exported, and I also found some issues where people were using memory tables that got exported and wouldn't import cleanly.

But in my particular case, to overcome this problem I just mounted a local directory into the container at `/var/lib/mysql`, and that seems to have cleared up the problem:

```
$ docker run --name mysql-import -v `(pwd)`/mysql:/var/lib/mysql:rw,delegated -p 3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=magento -d mysql:latest
```

So, if you ever see "The table 'x' is full", check into whether the filesystem supports file sizes at least as large as your largest MySQL database table. There are likely other ways you can work around this issue, but this fix worked for me, so I thought I'd post it here in case anyone else ever ran into the same issue.
