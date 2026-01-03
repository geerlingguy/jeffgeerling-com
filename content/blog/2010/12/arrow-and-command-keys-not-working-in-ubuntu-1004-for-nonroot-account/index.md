---
nid: 2296
title: "Arrow and Command Keys Not working in Ubuntu 10.04 for non-root Account"
slug: "arrow-and-command-keys-not-working-in-ubuntu-1004-for-nonroot-account"
date: 2010-12-25T03:59:53+00:00
drupal:
  nid: 2296
  path: 
  body_format: filtered_html
  redirects: []
tags:
  - linux
  - passwd
  - shell
  - ssh
  - ubuntu
  - unix
---

For some time, I was having trouble getting the arrow keys to function correctly in my terminal sessions when logging into one of my remote Linode servers running Ubuntu 10.04. Whenever I pressed an arrow key, instead of moving the cursor or going up and down the command history, I would get a string of gibberish like <code>[[A^[[B^[[D^[[C</code>. Not very helpful!

So, after some searching, I found that the cause for this is an incorrect shell environment being set in the passwd file. To fix this problem, simply edit the /etc/passwd file and change the final string (after the last <code>:</code>) to /bin/bash (it is set to /bin/sh if you create a user via the command line/useradd):


```
$ sudo nano /etc/passwd
```

Change this:


```
<username>:x:1000:1000::/home/<username>/:/bin/sh
```

to this:


```
<username>:x:1000:1000::/home/<username>/:/bin/bash
```

...and then save the file, log out, and log back in. Problem solved!
