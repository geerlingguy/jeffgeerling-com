---
nid: 2295
title: "Drupal.org approaching 1,000,000 nids!"
slug: "drupalorg-approaching-1000000-nids"
date: 2010-12-14T21:35:51+00:00
drupal:
  nid: 2295
  path: /blog/2016/drupalorg-approaching-1000000-nids
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal planet
---

<p>I noticed a few months ago that we hit the mid-950,000 range for posts... since then, I've forgotten to mark down the numbers through time (I wanted to try plotting the exact day when we'd cross over to 1,000,000 posts).</p>
<p>Today (December 14), we were at node #998,346 (obviously, some nodes have been deleted, and database causes notwithstanding... but the count still advances!).  Predictions as to when we'll hit this milestone? It'd be awesome if we could hit it exactly on the Drupal 7.0 release announcement, but I'm not holding my breath for <em>that</em>!</p>
<p>The better question is, "How many nodes can a drupal site have before the node table runs out of room (i.e. the nid column runs out of space?). The answer is <del>9,999,999,999</del> <strong>4,294,967,295</strong> (as of Drupal version 7), and that, my friends, is a very large number. Of course, you could increase the length of that field (and related fields) on one of your sites to add more room, but I calculated it out, and it would take adding 10,000 new nodes every day for the next <del>2,740</del> ~1,200 years before you'd have to worry about hitting the nid limit!</p>
<p>That means drupal.org shouldn't have to worry about increasing the size (int(10)) nid column until the year <del>102009</del> ~50000 (with a linear increase)! I would bet we won't be using MySQL by that time... and I'm guessing we'll have reached at least Drupal version 1,000 or so.</p>
<p><em>Updated based on comments below.</em></p>
