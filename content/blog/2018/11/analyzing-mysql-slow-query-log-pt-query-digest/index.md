---
nid: 2892
title: "Analyzing a MySQL slow query log with pt-query-digest"
slug: "analyzing-mysql-slow-query-log-pt-query-digest"
date: 2018-11-29T16:02:22+00:00
drupal:
  nid: 2892
  path: /blog/2018/analyzing-mysql-slow-query-log-pt-query-digest
  body_format: markdown
  redirects: []
tags:
  - database
  - drupal
  - drupal planet
  - infrastructure
  - magento
  - mysql
  - performance
  - slow
  - tuning
  - tutorial
---

There are times when you may notice your MySQL or MariaDB database server getting very slow. Usually, it's a very stressful time, as it means your site or application is _also_ getting very slow since the underlying database is slow. And then when you dig in, you notice that logs are filling up—and in MySQL's case, the slow query log is often a [canary in a coal mine](https://en.wikipedia.org/wiki/Sentinel_species) which can indicate potential performance issues (or highlight active performance issues).

But—assuming you have the slow query log enabled—have you ever grabbed a copy of the log and dug into it? It can be extremely daunting. It's literally a list of query metrics (time, how long the query took, how long it locked the table), then the raw slow query itself. How do you know which query takes the longest time? And is there one sort-of slow query that is actually the worst, just because it's being run hundreds of times per minute?

You need a tool to sift through the slow query log to get those statistics, and Percona has just the tool for it: [pt-query-digest](https://www.percona.com/doc/percona-toolkit/LATEST/pt-query-digest.html). This tool has many other tricks up its sleeve, but for this post, I just want to cover how it helps me analyze and summarize slow query logs so I can quickly dig into the worst queries that might be bringing down my production application or Drupal or other PHP-based website.

I'm doing this on my Mac, but the process should be similar for most any linux or unix-y environment (including the WSL on Windows 10):

  1. Create a directory to work in: `mkdir db-analysis && cd db-analysis`
  1. Download pt-query-digest: `curl -LO https://percona.com/get/pt-query-digest`
  1. Make it executable: `chmod +x pt-query-digest`
  1. Download your `slow-query.log` file from the database server (or if using something like AWS RDS/Aurora, download it from AWS Console).
  1. Run `pt-query-digest` over the log file: `./pt-query-digest slow-query.log`

At this point, you should see a full report with a summary of the worst queries at the top (along with stats about how many times they were invoked, the average amount of time they took, rows examined and sent, etc.

```
$ ./pt-query-digest slowquery.log

# 4.3s user time, 200ms system time, 39.12M rss, 4.12G vsz
# Current date: Thu Nov 29 10:02:45 2018
# Hostname: JJG.local
# Files: slowquery.log
# Overall: 4.51k total, 36 unique, 1.27 QPS, 15.65x concurrency __________
# Time range: 2018-11-27 21:00:23 to 21:59:38
# Attribute          total     min     max     avg     95%  stddev  median
# ============     ======= ======= ======= ======= ======= ======= =======
# Exec time         55640s      5s    118s     12s     16s      4s     13s
# Lock time        18446744073714s    34us 18446744073710s 4085657602s   260us 271453769812s   194us
# Rows sent          2.95M       0 103.99k  684.27       0   8.14k       0
# Rows examine     293.63M       0  18.67M  66.59k    0.99 583.21k    0.99
# Query size        44.63M      79   1.22M  10.12k   2.16k  97.85k   2.06k

# Profile
# Rank Query ID                      Response time    Calls R/Call  V/M   
# ==== ============================= ================ ===== ======= ===== 
#    1 0x5AE6E128A4790517E5CFFD03... 52666.0213 94.7%  4363 12.0711  0.86 UPDATE some_table
#    2 0x222A6FC43B63B119D2C46918...   618.3909  1.1%    29 21.3238  1.91 UPDATE some_table
#    3 0xD217B90797E8F34704CF55AF...   463.7665  0.8%    29 15.9919  0.07 SELECT some_other_table some_other_other_table
...
```

And then the rest of the report shows the queries in ranked order from worst to least offensive.

At this point, I'll grab the worst offender (usually there's only one that is taking up 90% or more of the slow query time) and run it using `EXPLAIN` on my MySQL server. This gives me more details about whether indexes would be used, whether temporary tables would be created, etc. And from that point, it's a matter of working with the application developers (or in many cases, my own dumb code!) to improve the query, or if that's not possible or the root cause, working on the MySQL configuration to ensure all the tuning parameters are adequate for the queries being run and the database being used.
