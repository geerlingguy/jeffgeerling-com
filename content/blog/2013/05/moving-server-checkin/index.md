---
nid: 2407
title: "Moving Server Check.in functionality to Node.js increased per-server capacity by 100x"
slug: "moving-server-checkin"
date: 2013-05-21T03:27:39+00:00
drupal:
  nid: 2407
  path: /blogs/jeff-geerling/moving-server-checkin
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal planet
  - node
  - node.js
  - performance
  - queue
  - scalability
  - server check.in
aliases:
  - /blogs/jeff-geerling/moving-server-checkin
---

Just posted a new blog post to the Server Check.in blog: <a href="https://servercheck.in/blog/moving-functionality-nodejs-increased-server">Moving functionality to Node.js increased per-server capacity by 100x</a>. Here's a snippet from the post:

<blockquote>
One feature that we just finished deploying is a small Node.js application that runs in tandem with Drupal to allow for an incredibly large number of servers and websites to be checked in a fraction of the time that we were checking them using only PHP, cron, and Drupal's Queue API.

If you need to do some potentially slow tasks very often, and they're either network or IO-bound, consider moving those tasks away from Drupal/PHP to a Node.js app. Your server and your overloaded queue will thank you!

<a href="https://servercheck.in/blog/moving-functionality-nodejs-increased-server">Read more</a>.
</blockquote>

tl;dr Node.js is awesome for running through a large number of network or IO-bound tasks that would otherwise become burdensome at scale using Drupal's Queue API.
