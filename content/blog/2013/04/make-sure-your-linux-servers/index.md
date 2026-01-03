---
nid: 2402
title: "Make sure your Linux servers' date and time are correct and synchronized"
slug: "make-sure-your-linux-servers"
date: 2013-04-24T17:29:16+00:00
drupal:
  nid: 2402
  path: /blogs/jeff-geerling/make-sure-your-linux-servers
  body_format: full_html
  redirects: []
tags:
  - centos
  - date
  - linux
  - ntp
  - timezone
---

Nowadays, most people assume that all modern computers and operating systems have network time synchronization set up properly and switched on by default. However, this is not the case with many Linux servers—especially if you didn't install Linux and configure it yourself (as would be the case with most cloud-based OS images like those used to generate new servers on Linode).

After setting up a new server on Linode or some other Linux VPS or dedicated server provider, you should always do the following to make sure the server's timezone and date and time synchronization are configured and working correctly:

<ol>
<li><a href="http://www.cyberciti.biz/faq/howto-linux-unix-change-setup-timezone-tz-variable/">Set the server's timezone</a> correctly. Basically, create a symbolic link from <code>/etc/localtime</code> to the proper timezone file inside <code>/usr/share/zoneinfo/</code>.
<li>Make sure ntp is installed using your system's package manager (for example, on CentOS/RHEL: <code>$ sudo yum install ntp</code> to install it if it's not installed already).</li>
<li>Make sure ntpd is set to run on startup: <code>$ sudo /sbin/chkconfig ntpd on</code></li>
<li>(Optional: Choose <a href="http://www.pool.ntp.org/en/">different/region-specific NTP servers</a> and place them inside <code>/etc/ntp.conf</code>, replacing the default servers that are in there).</li>
<li>Make sure your iptables firewall is set to accept UDP traffic on port 123:
<code>
$ sudo iptables -I INPUT -p udp --dport 123 -j ACCEPT
$ sudo iptables -I OUTPUT -p udp --sport 123 -j ACCEPT
</code></li>
<li>Test ntp with ntpdate: <code>$ sudo ntpdate pool.ntp.org</code>. This should show that there was an offset from the current system clock and the value retrieved over the Internet.</li>
<li>Start ntpd, and your server should be happily in-sync, hopefully within a second or less at all times, with clocks around the world! <code>$ sudo service ntpd start</code></li>
</ol>

These instructions were tested on CentOS 5.x and 6.x. Other distributions should be similar.
