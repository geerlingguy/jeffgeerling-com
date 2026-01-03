---
nid: 2256
title: "SSH in a Locked-Down Network"
slug: "ssh-locked-down-network"
date: 2009-10-18T15:36:28+00:00
drupal:
  nid: 2256
  path: /blogs/geerlingguy/ssh-locked-down-network
  body_format: full_html
  redirects: []
tags:
  - networking
  - remote connection
  - ssh
  - terminal
aliases:
  - /blogs/geerlingguy/ssh-locked-down-network
---

<p>Recently, during one job for a client, I needed to work for a length of time in a location that had quite severe network restrictions&mdash;in addition to a proxy server, the location blocked every port besides 80, 25, 443, and 8080. In order to use secure shell (SSH) to login to my work web server, I needed to use one of those ports (I used nmap to find open ports on my end).</p>
<p>Luckily, I gained access to another network for a short time, and used that connection to update my work web server to allow SSH over port 8080 (in addition to the standard, port 22). I edited the <code>/etc/ssh/sshd_config</code> file so it reads:</p>
<pre>
Port 22
Port 8080</pre>
<p>(the <code>Port 22</code> line was commented out, originally).</p>
<p>Then I simply used the -p (port) directive when logging in via SSH:</p>
<pre>
$ ssh -p8080 username@example.com</pre>
