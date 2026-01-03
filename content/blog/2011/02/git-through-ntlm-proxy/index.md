---
nid: 2307
title: "Git through an NTLM Proxy (Corporate Firewall) for drupal.org"
slug: "git-through-ntlm-proxy"
date: 2011-02-25T15:43:13+00:00
drupal:
  nid: 2307
  path: /blogs/jeff-geerling/git-through-ntlm-proxy
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal planet
  - git
  - github
  - ntlm
  - proxy
aliases:
  - /blogs/jeff-geerling/git-through-ntlm-proxy
---

<p>Borrowing from answers in <a href="http://stackoverflow.com/questions/1783659">this</a> Stack Overflow question, here's how you can get through a corporate (Microsoft) NTLM Proxy to clone git repositories from drupal.org:</p>

<p><code>cd</code> into your drupal contrib directory (or wherever you want to put the repository).</p>

<p><code>$ export http_proxy="http://username:password@proxy:port/"</code></p>

<p><code>$ git clone http://git.drupal.org/project/[projectname]</code></p>

<p>Basically, you're first setting an environment variable to tell your shell to use an HTTP proxy, with your username/password combo. This variable will be used when making connections to git.drupal.org (and other services, like github). You can also set this in your <code>~/.profile</code>, <code>.bash_rc</code>, or <code>.bash_profile</code> so it will be saved for future Terminal sessions.</p>

<p>If the above method doesn't work, you could do a couple other things - try setting up a local proxy on your own computer. You could use <a href="http://www.hrsoftworks.net/Products.php">NTLMaps</a> for linux/bsd/osx (I use this to <a href="http://www.jeffgeerling.com/articles/computing/2010/share-a-proxied-network">share my proxied connection over WiFi to iOS devices</a>), or use <a href="http://www.hrsoftworks.net/Products.php">Authoxy</a> for the Mac, and then authenticate against your own localhost proxy on a port of your choosing. This works better for more restrictive firewalls.</p>

<p>For example, if you use NTLMaps or Authoxy, you may be able to get away with just setting a git config variable:</p>

<p><code>$ git config --global http.proxy http://localhost:[port]</code></p>
