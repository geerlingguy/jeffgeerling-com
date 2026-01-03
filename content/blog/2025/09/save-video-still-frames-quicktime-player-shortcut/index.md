---
nid: 3494
title: "Save video still frames from QuickTime Player with a shortcut"
slug: "save-video-still-frames-quicktime-player-shortcut"
date: 2025-09-18T04:23:20+00:00
drupal:
  nid: 3494
  path: /blog/2025/save-video-still-frames-quicktime-player-shortcut
  body_format: markdown
  redirects:
    - /blog/2025/quicker-way-save-video-still-frame-quicktime-player
aliases:
  - /blog/2025/quicker-way-save-video-still-frame-quicktime-player
tags:
  - keyboard shortcuts
  - macos
  - paste
  - quicktime
  - tips
  - tutorial
---

Almost 15 years ago, I wrote [Grab a Single Frame from a Video in QuickTime X](/blogs/jeff-geerling/grab-single-frame-video). And for many years since, I slightly modified that workflow. Instead of using Preview, I would use [`pngpaste`](https://github.com/jcsalterego/pngpaste), and paste the copied frame from QuickTime player into a file.

For example:

  1. Open a video in QuickTime and scrub to the frame you would like to save as an image.
  2. Press Command-C
  3. Switch to Terminal
  4. Run `pngpaste image-name-here.jpg`
  5. Profit!

However, there are two problems with that workflow:

  1. In recent months, some of my [HEVC/H.265 footage would get garbled when using `pngpaste`](https://github.com/jcsalterego/pngpaste/issues/27).
  2. The workflow required me pressing no less than _six_ keystrokes (three command combos) minimum, when pulling a batch of still frames out of my video clips.

Since I no longer take still photos at some events, and rely on clips from videos for my long-term memories in Photos, I hate how long it takes to do all those commands in sequence, e.g. when pulling out 200 still frames from 50 different video clips.

So... I present, my more-involved-but-more-streamlined 2025 update to that workflow!

## AppleScript to the Rescue!

AppleScript has long been a great tool for automating mixed UI and scripted workflows on macOS—I remember using it back in the 90s on like System 7.5!

To solve the problem of HEVC content getting garbled, _and_ to cut out 66% of the minimal command flow from my previous workflow, I created an Automator Quick Action:

  1. Open Automator
  2. Create a new Quick Action
  3. Search for 'Run AppleScript' in the Actions Library, and drag it into the Automator document
  4. Paste the following AppleScript into the 'Run Applescript' text area:

```
on run {input, parameters}
	-- Set up save file.
	set formattedDate to (do shell script "date +'%Y-%m-%d at %I.%M.%S %p'")
	set filename to "video_frame " & formattedDate & ".jpg"
	set the save_location to ((path to downloads folder) as string) & filename

	tell application "QuickTime Player"
		activate
		tell application "System Events"
			keystroke "c" using command down -- Copy frame
		end tell
	end tell
	tell application "Preview"
		activate
		delay 0.3
		tell application "System Events"
			keystroke "n" using command down -- New document
			delay 0.3
		end tell
		save front document in file save_location -- Save image
		close every window of it
	end tell
	tell application "QuickTime Player"
		activate
	end tell
	return input
end run
```

The comments tell what each part of the AppleScript does. Save the Quick Action with a name like 'Save QuickTime Frame as JPEG'.

{{< figure src="./macos-keyboard-services-shortcut-universal.jpg" alt="macOS Keyboard settings - Services universal keyboard shortcut for QuickTime image paste" width="700" height="612" class="insert-image" >}}

To set a universal keyboard shortcut to trigger the App, I did the following (thanks to [this SE answer for giving me the final assist](https://apple.stackexchange.com/a/460091)):

  1. Open System Settings
  2. Navigate to Keyboard > Keyboard Shortcuts..., and click on "Services"
  3. Click on your Quick Action (should be under 'General') and double click in the space where it says `none`.
  4. Enter a key combo you want to use. (I did Shift + Option + Command + F, or ⇧⌥⌘F)
  5. Click 'Done'

Now, you can open a video in QuickTime, scrub to a frame you want to capture, and press the key combo to save the current frame into your Downloads folder. _Nice!_

You may get prompted for Accessibility and file permissions the first time you run the Quick Action. If you dismiss that dialog, you will have to go into the Privacy & Security settings and manually grant QuickTime and Quick Action permissions.
