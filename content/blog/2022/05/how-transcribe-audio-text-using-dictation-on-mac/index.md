---
nid: 3209
title: "How to transcribe audio to text using Dictation on a Mac"
slug: "how-transcribe-audio-text-using-dictation-on-mac"
date: 2022-05-20T02:41:40+00:00
drupal:
  nid: 3209
  path: /blog/2022/how-transcribe-audio-text-using-dictation-on-mac
  body_format: markdown
  redirects: []
tags:
  - audio
  - captions
  - dictation
  - loopback
  - mac
  - macos
  - sound
  - subtitles
  - transcription
  - video
---

You can use the Dictation feature built into your Mac to transcribe audio files, and in my experience, it's been about 98-99% accurate, so it saves a lot of time if you want to index your audio files, or you need a transcript for some other purpose.

These instructions were last updated for macOS Monterey 12.4.

First, open up System Preferences, go to Keyboard, then the 'Dictation' tab:

{{< figure src="./dictation-system-preferences.jpg" alt="Apple Dictation System Preferences" width="448" height="400" class="insert-image" >}}

Turn on Dictation, and when prompted, accept the terms for Apple's Dictation service. Also take note of the 'Shortcut' (e.g. 'press dictation key' or 'press control twice'. You'll use that to activate dictation later.

Make sure you have your Mac's microphone selected, then open up TextEdit and create a new document:

{{< figure src="./untitled-textedit-document-mac.png" alt="Untitled TextEdit document" width="500" height="307" class="insert-image" >}}

Activate the dictation shortcut (e.g. press the dictation key), then start playing back your audio file through your Mac's speakers. The mic should pick up the audio and start transcribing live into the open document.

## Bonus: Routing audio internally on the Mac with Loopback

If you have Rogue Amoeba's [Loopback](https://rogueamoeba.com/loopback/), you can also [use it to route the audio signal internally](https://rogueamoeba.com/support/knowledgebase/?showArticle=LB-Transcription), so you don't have to have audio playing out through the speakers.

After you have Loopback installed and running, create a new device called 'Transcription Device'. Delete the default Pass-thru source, and add in Quicktime Player as a new source:

{{< figure src="./loopback-transcription-device.png" alt="Loopback for Mac Transcription Device" width="700" height="316" class="insert-image" >}}

Quit Loopback (the device will still be present on the system after quitting), then go back to the Dictation settings in System Preferences. In there, choose the new 'Transcription Device' sound input:

{{< figure src="./dictation-transcription-device-macos-system-preferences.png" alt="Transcription Device in System Preferences Dictation" width="700" height="525" class="insert-image" >}}

Then go back to TextEdit, and in a new document, activate Dictation using your configured shortcut (e.g. the dictation key). Pop over to QuickTime Player, and play your audio or video file, and watch as the words are transcribed as if by magic!

{{< figure src="./live-transcription.jpg" alt="Live transcription using Loopback from QuickTime to TextEdit on the Mac" width="700" height="231" class="insert-image" >}}

## Alternative: Welder (or other online services)

As an alternative, you could use an online upload-to-transcribe service like [Welder](https://www.getwelder.com/transcribe). I tested the same files on Welder that I used with Dictation, and Welder was better about adding punctuation and separating multi-person interviews.

Their transcription feature can be used for free; upload a video or audio file, and within a few minutes, you can read or download the transcribed text.
