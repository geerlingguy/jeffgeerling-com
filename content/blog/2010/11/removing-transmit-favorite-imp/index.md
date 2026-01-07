---
nid: 2289
title: "Removing the \"Transmit Favorite Importer\""
slug: "removing-transmit-favorite-imp"
date: 2010-11-11T18:42:50+00:00
drupal:
  nid: 2289
  path: /blogs/jeff-geerling/removing-transmit-favorite-imp
  body_format: full_html
  redirects: []
tags:
  - finder
  - ftp
  - mdworker
  - spotlight
  - transmit
  - trash
aliases:
  - /blogs/jeff-geerling/removing-transmit-favorite-imp
---

<p>I recently upgraded Transmit using the in-application Update functionality, but after that, whenever I tried emptying the trash, I received a warning that I couldn&#39;t delete the &quot;Transmit Favorite Importer,&quot; because it was still in use.</p>
<p>Well, the Transmit Favorite Importer ties into the mdworker process on a Mac, which updates the Spotlight search index. Knowing this, I went into Activity Monitor, found the mdworker process, Quit it, and then emptied Trash. Voila! No more Transmit Favorite Importer!</p>
<p>A simple restart will do the trick as well, but if you are like me and have twenty applications open and don&#39;t have time to get back into the groove after a restart, this is a quicker way of getting your trash emptied.</p>
