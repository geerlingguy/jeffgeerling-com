---
nid: 2449
title: "Remove Tower's .git folder association in Mac OS X's Finder"
slug: "remove-towers-git-folder"
date: 2014-03-12T13:59:20+00:00
drupal:
  nid: 2449
  path: /blogs/jeff-geerling/remove-towers-git-folder
  body_format: full_html
  redirects: []
tags:
  - finder
  - git
  - mac
  - mac os x
  - tower
---

I use <a href="http://www.git-tower.com/">Tower</a> from time to time to do some git operations that require a little more attention or a better visual overview than what I can get via the CLI and built-in tools. However, I noticed that Tower likes to take over any folder with .git, and make Mac OS X's finder turn it into a 'Tower' package, so double-clicking the folder (which now behaves like a mini app or file) opens Tower.

I don't like that behavior, because I have some [example].git folders that I want to browse in the Finder or in other Mac apps without having to 'Show Package Contents'. Apparently <a href="http://gitx.lighthouseapp.com/projects/17830/tickets/15">GitX has the same issue</a>, and I'm not the only one annoyed by this behavior.

The fix, for me, was simple:

<ol>
<li>Get info on the .git folder (right-click and 'Get Info', or select the folder and hit Command-I).</li>
<li>Select 'Terminal' under "Open with:"</li>
<li>The "Open with:" menu should then change to Finder.app (because Terminal realizes this is actually a folder).</li>
</ol>

It seems like, after doing this and clicking 'Change All...', you can't switch back to the old behavior, but that's fine by me. I'll open .git folders in Tower when I want to, thankyouverymuch!
