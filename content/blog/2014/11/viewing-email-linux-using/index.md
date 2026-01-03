---
nid: 2482
title: "Viewing email in Linux using postfix's mailq and postcat"
slug: "viewing-email-linux-using"
date: 2014-11-17T16:35:44+00:00
drupal:
  nid: 2482
  path: /blogs/jeff-geerling/viewing-email-linux-using
  body_format: full_html
  redirects: []
tags:
  - debugging
  - email
  - linux
  - mail
  - mailq
  - postfix
  - sendmail
aliases:
  - /blogs/jeff-geerling/viewing-email-linux-using
---

When I'm developing using the <a href="https://github.com/geerlingguy/drupal-dev-vm">Drupal Development VM</a>, or checking into email processing on any of my servers, I usually use postfix to handle mail sending. Postfix is simple, preinstalled on most Linux distributions (and easy to set up if not), and is easy enough to use.

Here are the most common commands I use when either developing or troubleshooting email in production:

<ul>
<li><code>mailq</code> - print a list of all queued mail</li>
<li><code>postcat -vq [message-id]</code> - print a particular message, by ID (you can see the ID along in <code>mailq</code>'s output)</li>
<li><code>postqueue -f</code> - process the queued mail immediately</li>
<li><code>postsuper -d ALL</code> - delete ALL queued mail (use with caution—but handy if you have a mail send going awry!)</li>
</ul>

There are many other helpful commands and scripts to help deal with mail (e.g. deleting all messages to a certain domain, or deleting specific message IDs easily), but these are the main ones I use during day-to-day development and troubleshooting.
