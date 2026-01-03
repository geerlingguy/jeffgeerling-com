---
nid: 2347
title: "Simple MAMP/MAMP Pro VirtualHosts in Parallels / Windows XP"
slug: "simple-mampmamp-pro"
date: 2011-11-29T17:08:43+00:00
drupal:
  nid: 2347
  path: /blogs/jeff-geerling/simple-mampmamp-pro
  body_format: full_html
  redirects: []
tags:
  - dns
  - hosts
  - ip
  - mamp
  - parallels
  - virtualhosts
  - windows
aliases:
  - /blogs/jeff-geerling/simple-mampmamp-pro
---

(This tip should also work similarly with Vista, Windows 7, etc.).

After browsing around a bunch of different forums, the MAMP site, and Parallels documentation, I was still flummoxed by Parallels' weird Shared Host networking behavior, which seemingly didn't allow me to access virtualhosts I set up with MAMP for developing sites locally.

After much experimentation, I found that the simplest way to be able to type in 'local.example.com' (or 'dev.example.com', if that's your style) in Internet Explorer on Windows, and get a virtual host running via MAMP on my Mac, is to do the following:

<ol>
	<li>In Parallels' options for your virtual machine, go to Hardware, then Network 1, and choose 'Default Adapter' for 'Type'.</li>
	<li>Restart Windows in Parallels.</li>
	<li>Get your Mac's IP address (for your WiFi adapter or Ethernet; whatever's the primary interface).</li>
	<li>Open your Windows Hosts file and add your virtual hosts:

<ol>
	<li>Start &gt; Run... and enter "c:\windows\system32\drivers\etc\hosts" (use Notepad to open).</li>
	<li>Add a line like the following to the file and save: "[MAC_IP_ADDRESS] &nbsp; local.example.com"</li>
</ol></li>
</ol>

You should now be able to access whatever site you have defined at local.example.com in MAMP via Windows Internet Explorer.

<strong>Update: It looks like this will work if you choose the 'Shared Network' type as well; go figure. Parallels' networking support is a bit more dodgy than VMWare Fusion (which I'd been using on my old MacBook Pro for quite a while without a problem... when I bought a MacBook Air, I thought I'd try out Parallels again).
