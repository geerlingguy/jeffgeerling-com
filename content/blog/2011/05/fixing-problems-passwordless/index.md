---
nid: 2319
title: "Fixing Problems with Passwordless SSH Authentication"
slug: "fixing-problems-passwordless"
date: 2011-05-02T15:35:14+00:00
drupal:
  nid: 2319
  path: /blogs/jeff-geerling/fixing-problems-passwordless
  body_format: full_html
  redirects: []
tags:
  - security
  - server
  - ssh
---

I use CentOS, but these guidelines should apply no matter what flavor of linux you use. We all know it's a good security practice to lock down your server and require SSH logins to <a href="http://www.linuxproblem.org/art_9.html">use an RSA key/pair</a>, rather than a password, right? Plus, it makes it easier for you to login to your server from your primary computers/devices...

I was setting up a new server recently, and spent probably half an hour figuring out why the standard way of creating a shared key, sending it to the server, putting it in /home/[username]/.ssh/authorized_keys, and trying to log in without a password wasn't working for me.

It turns out, there were permissions issues I hadn't thought of (I usually would create accounts through cPanel, since I only live in the Terminal out of necessity, from time to time). When you create the authorized_keys file, which contains public SSH keys for your computers, you need to make sure the permissions are set so that:

<ul>
	<li>The ~/.ssh directory is owned by wheel (or a group that has SSH access), and that it is readable/writable by your user.</li>
	<li>The ~/.ssh/authorized_keys file is owned by wheel (or a gruop that has SSH access), and that it is readable/writeable only by your user. (<code>$ chmod 644 [username]</code>).</li>
</ul>
