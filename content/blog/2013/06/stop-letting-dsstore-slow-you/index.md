---
nid: 2409
title: "Stop letting .DS_Store slow you down"
slug: "stop-letting-dsstore-slow-you"
date: 2013-06-02T17:44:32+00:00
drupal:
  nid: 2409
  path: /blogs/jeff-geerling/stop-letting-dsstore-slow-you
  body_format: full_html
  redirects: []
tags:
  - dotfiles
  - ds_store
  - files
  - git
  - gitignore
  - mac
  - mac os x
  - tips
  - vcs
  - version control
aliases:
  - /blogs/jeff-geerling/stop-letting-dsstore-slow-you
---

I have over 100 git repositories on my Mac, and for almost every one, I sometimes browse the directory structure in the Finder. Once I do that, I inevitably end up with a few pesky <a href="http://en.wikipedia.org/wiki/.DS_Store"><code>.DS_Store</code></a> files that want to be added to my repo:

<p style="text-align: center;">{{< figure src="./ds_store-files.jpg" alt="Pesky .DS_Store Files in Terminal during Git Status" width="500" height="199" >}}</p>

.DS_Store files don't add anything of value to my code (they just tell Mac OS X about folder display and icons), so I always end up adding them to my own projects' <code>.gitignore</code> files. But when I'm working on other repositories (like Drupal, or a fork from GitHub) I don't want to add a <code>.gitignore</code> if none exists, or mess with the project's existing <code>.gitignore</code>. So what's a coder to do?

There are a couple good solutions:

<ol>
<li>Set git's core.excludesfile setting to a file of your choosing, with <code>*.DS_Store</code> inside:

```
$ git config --global core.excludesfile ~/.gitignore
$ echo *.DS_Store >> ~/.gitignore
```

(Adapted from <a href="http://stackoverflow.com/a/6701239">this SO answer</a>.)</li>
<li>You can avoid adding a .gitignore file on a per-repo basis by adding <code>*.DS_Store</code> to one repository's <code>.git/info/exclude</code> file (the .git folder is an invisible folder in the root of your git repo).</li>
</ol>

There! No more <code>.DS_Store</code> killing your commit momentum!

[Update: <a href="https://twitter.com/applemachome">@applemachome</a> told me about a for-pay app, <a href="http://www.zeroonetwenty.com/blueharvest/">BlueHarvest</a>, that should help with this problem in a more general fashion (it can keep pesky .DS_Store files off of external and shared network volumes, too!). But it's probably overkill for most people.]
