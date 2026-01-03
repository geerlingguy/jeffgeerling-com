---
nid: 2458
title: "Route local emails to another email address using Postfix on Linux"
slug: "route-local-emails-another"
date: 2014-06-02T13:18:17+00:00
drupal:
  nid: 2458
  path: /blogs/jeff-geerling/route-local-emails-another
  body_format: full_html
  redirects: []
tags:
  - aliases
  - linux
  - mail
  - postfix
  - root
  - sendmail
---

When I set up new servers, I like to make sure any system messages like cron failures, server issues, or emails that are routed to <code>johndoe@example.com</code> (where 'example.com' is the hostname of the server—meaning emails to that domain will get routed through the server itself and not hit an external MX server unless postfix/sendmail is configured correctly) are sent to my own email address.

It's relatively straightforward to route emails to internal users (like <code>webmaster</code>, <code>root</code>, etc.) to an external email address; you simply need to edit the <code>/etc/aliases</code> file, adding a rule like the one below, then run the command <code>sudo newaliases</code>:

```
webmaster:	root

# Person who should get root's mail
root:		youremail@example.com
```

By default, most internal users are routed to root as well (including webmaster), so setting an external email address (or a list of addresses, separated by comma) for the root account will allow you to more easily see what's happening on your server. Don't forget to run <code>sudo newaliases</code> to pick up the changes!
