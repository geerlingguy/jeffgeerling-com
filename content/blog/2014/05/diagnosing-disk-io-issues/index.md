---
nid: 2453
title: "Diagnosing Disk I/O issues: swapping, high IO wait, congestion"
slug: "diagnosing-disk-io-issues"
date: 2014-05-12T18:12:12+00:00
drupal:
  nid: 2453
  path: /blogs/jeff-geerling/diagnosing-disk-io-issues
  body_format: full_html
  redirects: []
tags:
  - iotop
  - linux
  - memory
  - mysql
  - performance
  - swap
  - top
---

One one small LEMP VPS I manage, I noticed munin graphs that showed anywhere between 5-50 MB/second of disk IO. Since the VM has an SSD instead of traditional spinning hard drive, performance wasn't too bad, but all that disk I/O definitely slowed things down.

I wanted to figure out what was the source of all the disk I/O, so I used the following techniques to narrow down the culprit (spoilers: it was MySQL, which was using some swap space because it was tuned to use a little too much memory).

<h2>iotop</h2>

First up was <code>iotop</code>, a handy top-like utility for monitoring disk IO in real-time. Install it via yum or apt, then run it with the command <code>sudo iotop -ao</code> to see an aggregated summary of disk IO over the course of the utility's run. I let it sit for a few minutes, then checked back in to find:

```
Total DISK READ: 3.94 K/s | Total DISK WRITE: 23.66 K/s
  TID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO>    COMMAND                                                                                                                                                                        
  755 be/4 mysql         0.00 B      0.00 B  0.00 %  4.10 % mysqld --basedir=/usr --datadir=/var/lib/mysql --plugin-dir=/usr/lib64/mysql/plugin --us~r/log/mysqld.log --pid-file=/var/run/mysqld/mysqld.pid --socket=/var/lib/mysql/mysql.sock
  756 be/4 mysql         0.00 B      0.00 B  0.00 %  4.08 % mysqld --basedir=/usr --datadir=/var/lib/mysql --plugin-dir=/usr/lib64/mysql/plugin --us~r/log/mysqld.log --pid-file=/var/run/mysqld/mysqld.pid --socket=/var/lib/mysql/mysql.sock
  757 be/4 mysql         0.00 B      0.00 B  0.00 %  3.81 % mysqld --basedir=/usr --datadir=/var/lib/mysql --plugin-dir=/usr/lib64/mysql/plugin --us~r/log/mysqld.log --pid-file=/var/run/mysqld/mysqld.pid --socket=/var/lib/mysql/mysql.sock
  758 be/4 mysql         0.00 B      0.00 B  0.00 %  2.81 % mysqld --basedir=/usr --datadir=/var/lib/mysql --plugin-dir=/usr/lib64/mysql/plugin --us~r/log/mysqld.log --pid-file=/var/run/mysqld/mysqld.pid --socket=/var/lib/mysql/mysql.sock
   29 be/4 root          0.00 B      0.00 B  0.00 %  0.33 % [kswapd0]
  763 be/4 mysql       448.00 K     21.50 M  0.00 %  0.12 % mysqld --basedir=/usr --datadir=/var/lib/mysql --plugin-dir=/usr/lib64/mysql/plugin --us~r/log/mysqld.log --pid-file=/var/run/mysqld/mysqld.pid --socket=/var/lib/mysql/mysql.sock
  250 be/3 root          0.00 B    248.00 K  0.00 %  0.08 % [jbd2/vda-8]
  601 be/4 root         16.00 K     66.03 M  0.00 %  0.04 % [flush-252:0]
19924 be/4 root          2.42 M      0.00 B  0.00 %  0.01 % python /usr/sbin/iotop -ao
19369 be/4 nginx       740.00 K      0.00 B  0.00 %  0.01 % php-fpm: pool www
...
```

<h2>top swap</h2>

Next I just wanted to see how much swap space was being consumed by which processes, so I launched top (with <code>top</code>), then pressed <code>O</code> (capital O), then <code>p</code> to show all the processes ranked by swap usage:

```
top - 13:10:15 up 10 days,  2:43,  1 user,  load average: 0.18, 0.17, 0.17
Tasks:  80 total,   1 running,  79 sleeping,   0 stopped,   0 zombie
Cpu(s): 62.0%us,  5.3%sy,  0.0%ni, 31.0%id,  0.3%wa,  0.0%hi,  0.3%si,  1.0%st
Mem:    502260k total,   398908k used,   103352k free,     2492k buffers
Swap:   524280k total,   130928k used,   393352k free,    49184k cached

  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  SWAP COMMAND                                                                                                                                                                    
  747 mysql     20   0  962m 153m 3148 S 53.8 31.3 992:52.91  90m mysqld                                                                                                                                                                      
28448 root      20   0  139m 1868  764 S  0.0  0.4   0:12.22 5444 munin-node                                                                                                                                                                  
25287 nginx     20   0 49516 1456  696 S  0.0  0.3   0:50.94 4532 nginx
```

It was easy to quickly figure out the source of all the IO using <code>iotop</code> and <code>top</code>, and after tweaking the MySQL configuration to use half the memory, all the processes now sit happily in RAM, avoiding all the swapping overhead! The difference wasn't too great, but it did result in 10-15% faster page loads (on average) for authenticated users on a Drupal site running on the VPS.
