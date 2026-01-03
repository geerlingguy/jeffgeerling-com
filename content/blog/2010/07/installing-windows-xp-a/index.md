---
nid: 1915
title: "Installing Windows XP from a Microsoft-downloaded .exe file"
slug: "installing-windows-xp-a"
date: 2010-07-06T19:16:59+00:00
drupal:
  nid: 1915
  path: /blog/2010/installing-windows-xp-a
  body_format: full_html
  redirects: []
tags:
  - burn
  - windows
  - XP
---

<p>I recently received a downloaded copy of Windows XP SP3 from Microsoft (I ordered the downloadable file, rather than a mailed CD, for installing on one of my Macs), and noticed that, unlike usual disk images, this file had the extension .exe rather than .iso or .img...</p>
<p>To get it to work with VMWare, I needed to either turn the file into an image, or burn it to a physical CD or DVD. After searching fruitlessly for hours, I finally found a great little app, <a href="http://www.nliteos.com/">nlite</a>, that helped me burn the files that came out of the .exe archive to a disc (the app is also a great help for slipstreaming an XP install).</p>
<p>To burn the .exe to a disk image or disc:</p>
<ol>
<li>Expand the .exe image by double-clicking on it, and choosing a folder into which to expand the files.</li>
<li>Download <a href="http://www.nliteos.com/">nlite</a>, and run it.</li>
<li>Follow the steps to create a bootable ISO, and select the folder into which you expanded your install files in step 1.</li>
<li>Burn the disc, or copy the ISO where you need it, and enjoy!</li>
</ol>
