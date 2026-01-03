---
nid: 3002
title: "Making a Terminal window the right aspect ratio for streaming or recording"
slug: "making-terminal-window-right-aspect-ratio-streaming-or-recording"
date: 2020-05-08T02:26:15+00:00
drupal:
  nid: 3002
  path: /blog/2020/making-terminal-window-right-aspect-ratio-streaming-or-recording
  body_format: markdown
  redirects: []
tags:
  - applescript
  - recording
  - screen capture
  - script
  - video
---

Recently I've been spending a bit of time producing video content of both browser windows and Terminal windows for screen recordings and livestreams on [my YouTube channel](https://www.youtube.com/c/JeffGeerling).

One common issue I have to deal with is trying to optimize the aspect ratio of the window for the video dimensions. In 99% of all cases, I need the window to be 16:9. And ideally, I want the window to be recorded at 1280x720 at 2x 'retina' resolution, so when I capture the window, it will be nice and sharp at 1080p, which is my typical output resolution.

In the past, I'd open up a 1280x720 image at 2x resolution, then drag the Terminal window over it. However, getting that to be pixel perfect is sometimes frustrating, and it's always annoying since it takes me an extra 10-20 seconds per recording.

In my searching, I found this handy article from way back in 2013: [How to Resize Windows on your Mac to Specific Sizes](https://www.labnol.org/software/resize-mac-windows-to-specific-size/28345/).

As it turns out, the AppleScript example in the blog post works perfectly still (yay for compatibility in AppleScript!), and I can open `Script Editor.app`, paste in the contents (with a couple modifications seen below), and then run it while Terminal is open. The frontmost Terminal window will scale to exactly 1280 pixels wide by 720 pixels high, then I can capture that Application Window in iShowU Instant, and boom! Perfect aspect ratio and resolution for my 1080p screen recordings!

Here's the AppleScript I'm using:

```
set theApp to "Terminal"
set appHeight to 720
set appWidth to 1280

tell application "Finder"
	set screenResolution to bounds of window of desktop
end tell

set screenWidth to item 3 of screenResolution
set screenHeight to item 4 of screenResolution

tell application theApp
	activate
	reopen
	set yAxis to (screenHeight - appHeight) / 2 as integer
	set xAxis to (screenWidth - appWidth) / 2 as integer
	set the bounds of the first window to {xAxis, yAxis, appWidth + xAxis, appHeight + yAxis}
end tell
```
