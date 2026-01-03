---
nid: 2442
title: "Quick logrotate example for Apache logs and some gotchas"
slug: "quick-logrotate-example-apache"
date: 2013-12-23T20:36:33+00:00
drupal:
  nid: 2442
  path: /blogs/jeff-geerling/quick-logrotate-example-apache
  body_format: full_html
  redirects: []
tags:
  - apache
  - disk
  - linux
  - logrotate
---

On one server, where I have a custom directory where all the Apache (httpd) error and access logs are written, one set per virtualhost, I noticed the folder had grown to multiple gigabytes in size (found using <code>du -h --max-depth=1</code>)—in this situation, there's a handy utility on pretty much every Linux/UNIX system called logrotate that is made to help ensure log files don't grow too large. It periodically copies and optionally compresses the log files and deletes old logs, daily, monthly, or on other schedules.

For this server, to quickly fix the problem of growing-too-large log files, I added a file 'httpd-custom' at <code>/etc/logrotate.d/httpd-custom</code>, with the following contents:


```
 /home/user/log/httpd/*log
/home/user/log/httpd/*err
{
rotate 5
size 25M
missingok
notifempty
sharedscripts
compress
postrotate
/sbin/service httpd reload &gt; /dev/null 2&gt;/dev/null || true
endscript
}
```

Some notes:

<ul>
	<li><strong>rotate 5</strong>: tells logrotate to only keep the past five rotated log files (it will delete the oldest one after it has run more than 5 times).</li>
	<li><strong>size 25M</strong>: tells logrotate to rotate the log after it's grown to 25+ MB.</li>
	<li><strong>compress</strong>: tells logrotate to use gzip (with the -9/most compression option) to compress the log file—this saves a TON of disk space for large log files.</li>
	<li>If logrotate is deleting all rotated logs, and not just compressing/moving them, you probably need to add the 'rotate X' command, where X is the number of rotated logfiles to keep.</li>
</ul>

Read much, much more here: <a href="http://linux.die.net/man/8/logrotate">logrotate man page</a>.
