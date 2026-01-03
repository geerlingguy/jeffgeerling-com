---
nid: 26
title: "A good use for a Raspberry Pi - Missile Control"
slug: "good-use-raspberry-pi-missile-control"
date: 2016-01-02T05:26:26+00:00
drupal:
  nid: 26
  path: /blog/2016/good-use-raspberry-pi-missile-control
  body_format: full_html
  redirects: []
tags:
  - hacks
  - missile launcher
  - opencv
  - raspberry pi
  - usb
---

My brother gave me what will likely be one of the best useless-but-oh-so-fun gifts ever—a <a href="http://dreamcheeky.com/thunder-missile-launcher">Dream Cheeky Thunder</a> USB foam missile launcher.

<p style="text-align: center;">{{< figure src="./thunder-missile-launcher.jpg" alt="Dream Cheeky Thunder Missile Launcher - USB" width="300" height="300" >}}</p>

The launcher can be used with an extremely boorish app for Mac or Windows... or you can control it with some basic USB communication! I've found a few projects which allow the launcher to be controlled via any OS with Python fairly easily:

<ul>
<li><a href="https://github.com/nmilford/stormLauncher">stormLauncher</a> - A basic Python script that allows command-line usage.</li>
<li><a href="https://github.com/codedance/Retaliation">Retaliation</a> - A Python script that integrates with Jenkins build servers and fires at preselected targets upon build failure.</li>
<li><a href="http://www.amctrl.com/rocketlauncher.html">USB Rocket Launcher implementation</a> - A quick overview of the USB commands to use the launcher.</li>
</ul>

My idea is to figure out a way to use one of my spare Raspberry Pis to give some brains to this launcher; I will hopefully be able to set it in 'patrol' mode, and by mounting a Pi camera on the top, I can use <a href="http://opencv.org/">OpenCV</a> to do facial detection, aim the missiles just under a detected face, and fire.

Responsiveness isn't amazing, but it would be a fun project to hack on when I get some time. For now, I'm happy enough using my keys to point it at someone (to usually myself since others aren't willing targets) and fire :)
