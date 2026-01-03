---
nid: 2376
title: "Glitchy Video and Freezes on MacBook Pros"
slug: "glitchy-video-and-freezes"
date: 2012-09-04T03:46:53+00:00
drupal:
  nid: 2376
  path: /blogs/jeff-geerling/glitchy-video-and-freezes
  body_format: full_html
  redirects: []
tags:
  - crash
  - mac
  - macbook pro
  - nvidia
---

I've had a few friends report strange issues with their MacBook Pro laptops. Often they would report that the video signal on either an internal or external display becomes 'glitchy' or 'jumpy'. I initially thought it could be a connection issue, as I've seen many a VGA cable that becomes loose cause weird sync issues. However, they also reported that the cursor continued to work normally, moving around when they were moving the mouse/trackpad.

<p style="text-align: center;">{{< figure src="./macbook-pro-graphics-glitch.jpg" alt="MacBook Pro Graphics Glitch" width="450" height="252" >}}<br />
Doesn't look too nice...</p>

I typically recommend people take these sorts of issues to the Genius Bar at an Apple Store, especially since the problem isn't easy to replicate when I take a minute or two to look at the laptop—often the problem only happens after constantly using the computer for more than half an hour.

However, I finally got to experience the problem first-hand, when my sister brought me her laptop and I used it for an evening of blogging and browsing. After half an hour or so, the screen started getting quite jittery:

<p style="text-align: center;"><iframe width="640" height="360" src="http://www.youtube.com/embed/4kjWH950opM" frameborder="0" allowfullscreen></iframe></p>

I forcefully shut down the laptop by holding down the power button for 10 seconds (Control + Command + Power didn't work to reset it). Once restarted, I only had to open Chrome and load up a page or two, and the flickering came back.

After another reboot, I opened up the Console app and looked through the log files, and found a lot of recurrences of the following:

```
9/1/12 9:53:38.000 PM kernel[0]: IOVendorGLContext::ReportGPURestart 
9/1/12 9:53:42.221 PM WindowServer[88]: CGXSetWindowListAlpha: Invalid window 0
9/1/12 9:54:12.000 PM kernel[0]: NVDA(OpenGL): Channel exception! exception type = 0x3 = Fifo: Unknown Method Error
9/1/12 9:54:17.000 PM kernel[0]: NVDA(OpenGL): Channel exception! exception type = 0xd = GR: SW Notify Error
9/1/12 9:54:17.000 PM kernel[0]: NVDA(OpenGL): Channel exception! exception type = 0x6 = Fifo: Parse Error
```

It looks like something was going wrong with the NVidia ('NVDA') graphics processor, and it got stuck in a loop that was causing the wonkiness. Looking up those errors on Google found a ton of other people having similar problems, for instance:

<ul>
<li><a href="https://discussions.apple.com/thread/1916253">NVDA(OpenGL): Channel exception!</a> (Apple Support Communities)</li>
<li><a href="https://discussions.apple.com/thread/2010331">System crash caused by Nvidia Driver</a> (Apple Support Communities)</li>
<li><a href="http://onsoftware.en.softonic.com/fix-for-nvdaopengl-channel-exception-imac-error">Fix for NVDA(OpenGL): Channel exception! iMac error</a> (Softonic)</li>
<li><a href="http://www.betalogue.com/2009/06/09/mac-os-x-nvidia/">Bug with NVIDIA graphics driver?</a> (Betalogue)</li>
<li><a href="http://highmac.com/how-to/fix-kernel-nvdaopengl-channel-exception/">How to Fix "kernel NVDA(OpenGL) Channel exception!"</a> (High End Mac)</li>
</ul>

It seems to me that this problem is either hardware or driver-related, so it's usually not possible to fix it without replacing the entire logic board on most Macs... but many people have reported fewer crashes by doing the following:

<ul>
<li>Installing something like <a href="http://clicktoflash.com/">ClickToFlash</a> to make Flash not load on websites unless they explicitly allow it.</li>
<li>Installing <a href="http://codykrieger.com/gfxCardStatus">gfxCardStatus</a> and manually setting the GPU to either Intel Graphics or the dedicated graphics to prevent switchover-related crashes.</li>
<li>Reinstalling Mac OS X, or updating to the latest version (but this seems to rarely help).</li>
<li>Not running as many GPU-intense applications (like games, apps like Twitter, etc.).</lI>
</ul>

The last option is probably a bit extreme, but it could help. The first two options should always be attempted before giving up and bringing your laptop into Apple for service, though... and they're often a good idea to conserve power regardless!

The recurring theme, though, is that people had to bring their laptops in to Apple for a logic board replacement (so a new GPU would be installed). Many people reported that only a full logic board replacement would solve the problem once and for all. I'm recommending my sister take in her MacBook Pro for service, and I'll report back the results of her visit.
