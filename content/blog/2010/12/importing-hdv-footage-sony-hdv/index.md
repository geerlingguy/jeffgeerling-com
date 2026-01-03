---
nid: 2293
title: "Importing HDV footage from Sony HDV Cameras into iMovie '11 (or '08/'09)"
slug: "importing-hdv-footage-sony-hdv"
date: 2010-12-01T14:56:44+00:00
drupal:
  nid: 2293
  path: /blogs/jeff-geerling/importing-hdv-footage-sony-hdv
  body_format: full_html
  redirects: []
tags:
  - hd
  - hdv
  - imovie
  - import
  - sony
  - video
---

<p>I have had a ton of trouble today getting a rented&nbsp;Sony HVR-Z1U HDV Camera to work with iMovie '11 - I was having trouble both importing pre-recorded footage (in VCR mode) and importing live footage (in Camera mode). QuickTime Player would allow me to import video from the camera at DV quality, but I couldn't get HD.</p>
<p>I found that the camera was downconverting the video to regular DV (squeezing the pixels so it would still be a 16:9 widescreen picture) when using the i.Link (FireWire/IEEE 1394) port. After trying out a variety of settings, I was finally able to set up the camera so it would import (both in VCR and in Camera mode) HD video, directly into iMovie '11.</p>
<p>You simply need to set the following settings in the camera's menu:</p>
<!--break-->
<p>In Camera mode&nbsp;(under MENU -&gt; IN/OUT REC):</p>
<ul>
<li>i.LINK CONV - OFF</li>
<li>REC FORMAT - HDV</li>
</ul>
<p>In VCR mode&nbsp;(under MENU -&gt; IN/OUT REC):</p>
<ul>
<li>VCR HDV/DV - HDV</li>
<li>i.LINK CONV - OFF</li>
<li>A/V-&gt;DV OUT - ON</li>
</ul>
<p>Now I'm getting full 1080i HD video in iMovie (directly from the camera), which looks a hundred times better than video imported through QuickTime Player, then imported into iMovie.</p>
