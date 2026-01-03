---
nid: 71
title: "Bad / Annoying IP Addresses"
slug: "bad-annoying-ip-addresses"
date: 2010-09-22T20:21:47+00:00
drupal:
  nid: 71
  path: /web-design/2010/bad-annoying-ip-addresses
  body_format: full_html
  redirects: []
tags:
  - dns
  - internet
  - ip
aliases:
  - /web-design/2010/bad-annoying-ip-addresses
---

From time to time, there is a very disobedient/annoying computer or set of computers that annoy the heck out of me online—usually by attempting to bring down one of my websites, or by trying to access hundreds of vulnerable locations (which makes my server return a bunch of 404s) on my server.

For information on different IPs, I use the online IP information lookup tool at <a href="http://www.robtex.com/">robtex</a>.

Anywho, to cut a long story short, I will list the IP addresses and reverse DNS information for them on this page. Anybody that feels inclined to block these IP addresses should do so without a pang of conscience.

<h2>204.238.82.18</h2>

This little address belongs to a company called "Security Metrics." One of their computers, located at the DNS entry scan2.securitymetrics.com, decided to fill up one of my site's logs with over 10,000 404/file-not-found errors in the course of 10 minutes. Quite annoying, I say. I don't know much about Security Metrics, but I won't be using their services at any time in the future. Perhaps some random person decided to do a crazy port and vulnerability scan on my server... well, luckily they didn't get far. BLOCKED!

<h2>38.113.234.180</h2>

This address (part of the /38 block of IP addresses, which is <a href="http://web-robot-abuse.blogspot.com/2006/11/38113234180-crawl1cosmixcorpcom.html">reported to be sour</a>) has caused over 1,000 404/file-not-found errors over the past day or so on one of my servers. (Also in this block: 38.113.234.181). BLOCKED!

<h2>66.71.191.90</h2>

This address killed one of my servers not once, but three times in a day. Talk about persistence! Takedowns no longer, sir... you are banned. (Many malformed 'pure-ftpd' requests were coming from that IP address). Looks like <a href="http://www.bizimbal.com/odb/details.html?id=911111">I'm not the only one</a> to have this IP address on my blacklist. BLOCKED!

<h2>146.0.79.23</h2>

This address tried brute-forcing its way into one of my client's sites as the administrator account. It was pesky and persistent, and sneaky too—it would wait about 20 minutes between login attempts. Of course, the admin password is more than 30 characters, random, uppercase and lower, with numbers and symbols... so there's little chance brute-forcing would actually work. Plus, Drupal 7 provides simple brute-force ('flood') prevention. But since I don't like this IP address anyways, BLOCKED!

More to come...
