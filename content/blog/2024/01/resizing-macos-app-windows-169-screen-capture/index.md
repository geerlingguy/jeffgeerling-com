---
nid: 3341
title: "Resizing macOS app windows for 16:9 screen capture"
slug: "resizing-macos-app-windows-169-screen-capture"
date: 2024-01-28T19:18:02+00:00
drupal:
  nid: 3341
  path: /blog/2024/resizing-macos-app-windows-169-screen-capture
  body_format: markdown
  redirects: []
tags:
  - applescript
  - mac
  - macos
  - screen capture
---

I frequently need to capture a window of some Mac app for a recording (usually for my YouTube channel), and I've used a little AppleScript I wrote years ago for the purpose.

Somehow, that script (which I saved as a 'one shot' App (`.app` extension) that just runs then quits) got deleted off my Script Editor folder in my iCloud Drive, so I had to re-create it.

Luckily, the syntax for this operation is dead simple:

```
tell application "Safari"
	set bounds of front window to {0, 50, 1280, 770}
end tell
```

You can adjust the `{X, Y, width, height}` parameters accordingly—note that the width and height seem to be additive to the X/Y. So I use 770 instead of 720 for the height (720 + 50).

In `Script Editor`, save the file as a `.app`, with the option to keep it running unchecked. Now, whenever you want a window sized perfectly for capture, just press Command + Spacebar, then type in the name of the Script/App you saved, and hit enter. The top-most window in Safari will scale to exactly 720p resolution.

I have similar scripts set up for Terminal and other apps I frequently capture, so I just hit Command + Spacebar, type the name of the app I need to resize, and press enter.

I also had an [earlier post describing resizing Terminal here](https://www.jeffgeerling.com/blog/2020/making-terminal-window-right-aspect-ratio-streaming-or-recording), but that method required a bit more AppleScript that's really not necessary for my use case.

I also use an open source app, [DeskPad](https://github.com/Stengo/DeskPad), to put my screen in a virtual desktop monitor sometimes. It's useful when I need to record it over a long period of time, and don't want my other activity to interfere (e.g. a long-running task without my mouse flying over the screen a bunch).
