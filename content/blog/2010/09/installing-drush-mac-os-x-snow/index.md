---
nid: 2335
title: "Installing Drush on Mac OS X \"Snow Leopard\""
slug: "installing-drush-mac-os-x-snow"
date: 2010-09-24T15:36:16+00:00
drupal:
  nid: 2335
  path: /blogs/jeff-geerling/installing-drush-mac-os-x-snow
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal planet
  - drush
aliases:
  - /blogs/jeff-geerling/installing-drush-mac-os-x-snow
---

<p>To those wishing to install Drush on their Mac, but having difficulty, here&#39;s a surefire way to get it running great:</p>
<p>[<strong>Edit</strong>: Umm... instead of doing all the steps below, you can use <a href="http://mxcl.github.com/homebrew/">Homebrew</a> (the &#39;missing package manager for Mac OS X&#39;) and enter <code>$ brew install drush</code>. Much simpler!]</p>
<ol>
<li>Fire up the Terminal (this is why you&#39;re using Drush, so you&#39;d better get comfy in here!).</li>
<li>cd to your Desktop, download drush, and extract it.<br />
<code> $ cd Desktop $ wget http://ftp.drupal.org/files/projects/drush-6.x-3.3.tar.gz $ tar -xvzf drush-6.x-3.3.tar.gz </code></li>
<li>Move the drush directory to /usr/local/lib<br />
<code> $ sudo mv drush /usr/local/lib </code></li>
<li>Make drush executable.<br />
<code> $ sudo chmod u+x /usr/local/lib/drush/drush </code></li>
<li>Make a symbolic link to drush in /usr/bin<br />
<code> $ sudo ln -s /usr/local/lib/drush/drush /usr/bin/drush </code></li>
<li>Set up an alias in your bash environment so you can type &#39;drush <em>command</em>&#39; rather than &#39;/usr/bin/drush <em>command</em>&#39;<br />
<code>
$ cd ~
$ nano .profile
# Inside the .profile file:
alias drush='/usr/bin/drush'
# Then press control-O + return to write the file, and control-X to exit nano
$ source .profile </code></li>
</ol>
<p>Now, you can simply enter &#39;drush <em>command</em>&#39; to use drush.</p>
