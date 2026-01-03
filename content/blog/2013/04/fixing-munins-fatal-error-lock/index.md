---
nid: 2399
title: "Fixing Munin's [FATAL ERROR] Lock already exists: /var/run/munin/munin-update.lock. Dying."
slug: "fixing-munins-fatal-error-lock"
date: 2013-04-12T16:17:19+00:00
drupal:
  nid: 2399
  path: /blogs/jeff-geerling/fixing-munins-fatal-error-lock
  body_format: full_html
  redirects: []
tags:
  - monitoring
  - munin
aliases:
  - /blogs/jeff-geerling/fixing-munins-fatal-error-lock
---

Recently, I upgraded one of my CentOS and Ubuntu servers to a new version of Munin 2.0.x, and started getting an error stating that munin-update.lock already exists:

```
2013/03/25 23:11:02 Setting log level to DEBUG
2013/03/25 23:11:02 [DEBUG] Lock /var/run/munin/munin-update.lock already exists, checking process
2013/03/25 23:11:02 [DEBUG] Lock contained pid '10160'
2013/03/25 23:11:02 [DEBUG] kill -0 10160 worked - it is still alive. Locking failed.
2013/03/25 23:11:02 [FATAL ERROR] Lock already exists: /var/run/munin/munin-update.lock. Dying.
2013/03/25 23:11:02  at /usr/lib/perl5/vendor_perl/5.8.8/Munin/Master/Update.pm line 128
```

Munin hadn't been updating for a couple weeks, so I finally deleted the existing munin-update.lock file, and munin started running again. If this doesn't help solve your problem, have a look inside the various munin log files in <code>/var/log/munin/</code> to see if one of them contains more details as to why munin isn't working for you.

Also, for some reason, munin 2.x isn't working for me on CentOS 5.x, at least on servers where IPv6 is enabled, unless I manually edit one of the main munin config files. I've opened <a href="http://munin-monitoring.org/ticket/1285#ticket">this bug</a> in the munin issue tracker to see if it will be resolved. The errors I get look like the following, inside <code>/var/log/munin/munin-update.log</code>:

```
Failed to connect to node [IP ADDRESS]:4949/tcp : Invalid argument
Munin::Master::UpdateWorker<domain;sub.domain> failed to connect to node
```

There are some other caveats running munin on a server with IPv6 enabled—check out this page in the munin wiki: <a href="http://munin-monitoring.org/wiki/IPv6">Munin IPv6</a>.
