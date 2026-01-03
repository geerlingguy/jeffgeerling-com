---
nid: 2317
title: "Grab a Single Frame from a Video in QuickTime X"
slug: "grab-single-frame-video"
date: 2011-04-23T22:31:00+00:00
drupal:
  nid: 2317
  path: /blogs/jeff-geerling/grab-single-frame-video
  body_format: full_html
  redirects: []
tags:
  - mac
  - quicktime
  - quicktime pro
  - screen
  - screen capture
  - video
aliases:
  - /blogs/jeff-geerling/grab-single-frame-video
   - /blogs/jeff-geerling/grab-single-frame-video
---

<blockquote>
<strong>Update</strong>: More recent versions of QuickTime Player have the ability to copy frames of the video by using 'Command + C'. In recent versions, to grab a frame, do the following:

<ol>
<li>In QuickTime Player: Pause on the frame you want to capture (use arrow keys to go forward/backward by 1 frame).</li>
<li>Press 'Command-C' (or select Edit > 'Copy').</li>
<li>In Preview: Press 'Command-N' (or select File > 'New from Clipboard')</li>
<li>Save the new file where you'd like.</li>
</ol>

Also, in 2025 I posted <a href="/blog/2025/save-video-still-frames-quicktime-player-shortcut">Save video still frames from QuickTime Player with a shortcut</a>; you can use a single keyboard shortcut to copy and save the photo using AppleScript!
</blockquote>

There are many things to like about QuickTime X, and many improvements were included over QuickTime Pro 7... but there were also a ton of features removed (like being able to set advanced export options, save a movie as images, and do some other more advanced edits/exports.

However, I'm glad I finally figured out how I can grab one frame from a movie in QuickTime Player X. The problem I was having is this: If you pause the video and use the left/right arrow keys to move the playhead exactly to the frame you want, the player controls are still showing over the video (in addition to the video title bar/window chrome.

If you take a screen grab of the player, those elements will be on top of your video still frame.

To get rid of those elements, and capture one frame of your video as an image, do the following:

<ol>
	<li>Hold down the Command key, and click on the video (while it's paused on the frame you want).</li>
	<li>Press Command + Shift + 4 (in combination), then the Spacebar (the cursor should change to a camera). (**Note**: On macOS High Sierra and later, you can press Command + Shift + 5 instead, and select the 'Capture Window' option.)</li>
	<li>Click on the video window to take a screenshot of just that window. It will be saved to your Desktop.</li>
</ol>

In picture form (for the visually inclined):
<p style="text-align: center;">{{< figure src="./command-click-quicktime-x-still-frame-capture.jpg" alt="Command-Click on a QuickTime Window to remove the chrome for a clean frame grab." width="396" height="511" >}}</p>
There still aren't many great options for exporting in QTX, but you can still download and install QuickTime Pro 7 (it's even included on the OS X Snow Leopard Install DVD!) if you need those advanced features.
