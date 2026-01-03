---
nid: 2875
title: "Convert Protected M4V videos from iTunes to MP4s with TunesKit"
slug: "convert-protected-m4v-videos-itunes-mp4s-tuneskit"
date: 2018-09-20T21:39:50+00:00
drupal:
  nid: 2875
  path: /blog/2018/convert-protected-m4v-videos-itunes-mp4s-tuneskit
  body_format: markdown
  redirects: []
tags:
  - conversion
  - drm
  - itunes
  - m4v
  - media
  - tuneskit
  - video
---

So, I have amassed a pretty massive media library over the years—my goal has always been to maintain every single bit of digital media I own locally via iTunes (and/or other libraries which can be shared with devices in my home), and be able to play any of my DVDs, Blu-rays, digital purchases, etc. on any of my devices (mostly in the Apple kingdom, but there are a few Raspberry Pis and other devices floating about).

I also like the convenience of purchasing media on the iTunes Store, so I have also amassed a decent collection of movies and TV shows there. One problem: none of those files can be played outside the Apple ecosystem! In the past, I outlined [how I put Blu-ray, HD-DVD, and DVD media onto my Mac](/articles/audio-and-video/2010/ripping-movies-blu-ray-and-dvd). In this post, I'll run through my process for stripping the DRM from protected M4V videos I purchased and downloaded from the iTunes Store.

> Aside: It's ironic that the [International Day against DRM](https://www.defectivebydesign.org/dayagainstdrm) was a couple days ago—it has no bearing on my writing this post, it's just coincidental.
> 
> Note that I do not pirate nor share content I purchased with others... it's crazy the lengths I'll go through to get legally-acquired media onto my devices so I can watch it whenever and wherever I like. Most people aren't willing to put up with the insane barriers to user-friendliness that DRM demands—and that's a major reason the movie industry has a major piracy problem to begin with!

## TunesKit for M4V DRM removal

{{< figure src="./tuneskit-ui.png" alt="TunesKit M4V Converter UI in Windows 10" width="650" height="464" class="insert-image" >}}

A long time ago, something like [Requiem](https://digiex.net/threads/requiem-4-1-remove-itunes-drm-fairplay-from-music-video-and-books.11796/) was a decent-ish option (though kind of kludgy) for DRM removal. But as time has progressed, and the tricks it used no longer work in modern versions of iTunes, it has become necessary to use one of the paid options for DRM removal. Currently, there are two: [TunesKit](https://www.tuneskit.com/tuneskit-for-win.html) and [M4VGear](https://www.m4vgear.com/m4vgear-for-windows.html).

Both of these products have Mac and Windows versions (ostensibly), but after trying _both_ on _both_ platforms, I have found the Windows versions to be a lot more reliable. And TunesKit felt a little more polished (and often worked better in my testing) than M4VGear.

On the Mac, neither of them worked with High Sierra or Mojave (macOS 10.13 or 10.14) nor the latest version of iTunes that those OSes ship with. So you either have to keep a Mac held back to an older OS and iTunes version, or build a [macOS VirtualBox VM](https://github.com/geerlingguy/macos-virtualbox-vm), running older software, and try to get everything working inside there. Both options were unappealing—though not for lack of trying—so I decided to stick to running the Windows version on my Dell XPS 13 running Windows 10 and the latest version of iTunes from the Windows Store.

## The Process

Since I don't have the space to keep my entire media library on my Dell laptop (I have a Mac mini set up for that!), I decided to sign into iTunes, download a set of 10 or so movies at a time, then process them. The process went something like this:

  1. Open iTunes (signed in to my iTunes Store account).
  2. Download a set of 10 movies from iCloud to my local library.
  3. Once the download finishes, quit iTunes.
  4. Open TunesKit M4V Converter
  5. Click 'Library' to open up the iTunes Library from within TunesKit M4V Converter.
  6. Select the movies I just downloaded.
  7. For each movie, deselect all audio tracks and subtitle tracks besides English/US (or whatever languages you prefer).
  8. Click Convert, and wait for all the movies to be converted.
  9. Once those movies are converted, quit TunesKit, open iTunes, and choose 'Remove Download' for the batch of movies you just converted.
  10. Repeat steps 2-9 for all your movies and TV shows until complete.

## Notes

  - If you want the 1080p version of HD movies (sorry, no 4K on the desktop/laptop version of iTunes yet!), make sure you have enabled high quality downloads in the iTunes preferences.
  - If things seem to be stuck (e.g. TunesKit says converting, but the conversion is stuck at 0% for a loooong time), restart the computer and try again. For some reason, things just stop working every once in a while, and I never noticed why. But a restart always fixed it.
  - The fastest way to copy a bunch of HD movies around is with an external USB 3.0 drive (or something faster). You can usually get copy speeds of over 200 MB/sec with a fast drive. Over the network, I could eke out about 111 MB/sec on my home's gigabit network. Note that I have all SSDs everywhere—spinning disc drives will be a bit slower.
