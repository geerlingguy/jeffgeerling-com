---
nid: 3344
title: "Highly-condensed time-lapse footage with Frigate"
slug: "highly-condensed-time-lapse-footage-frigate"
date: 2024-02-02T03:10:42+00:00
drupal:
  nid: 3344
  path: /blog/2024/highly-condensed-time-lapse-footage-frigate
  body_format: markdown
  redirects:
    - /blog/2024/making-highly-condensed-timelapse-footage-frigate-nvr
aliases:
  - /blog/2024/making-highly-condensed-timelapse-footage-frigate-nvr
tags:
  - camera
  - ffmpeg
  - frigate
  - nvr
  - open source
  - poe
  - timelapse
  - tutorial
---

Frigate's [0.13.0 release](https://github.com/blakeblackshear/frigate/releases/tag/v0.13.0) included a feature near and dear to my heart: easy exporting of timelapses, straight from the Frigate UI.

I'm a little bit [nutty about timelapses](https://www.jeffgeerling.com/search?search_api_fulltext=timelapse), and have made them with dashcams, GoPros, full DSLRs, webcams, and [even Raspberry Pi](https://github.com/geerlingguy/pi-timelapse).

But one thing I _haven't_ done (until now) is make easy timelapses from IP cameras like the [Annke 4K PoE cameras](https://amzn.to/3HPGcdT) I use for security around my house.

Eventually I'm planning on automating things further, but for now, here's my process for building up a timelapse that's relatively small in file size, preserving only frames where there's motion from frame to frame.

For something like clouds/sky, or natural environments, it's better to do a straight timelapse export and maybe recompress it if you want, but for indoor or outdoor security footage, it's nice to condense it down.

## Exporting and compressing

Frigate's export functionality isn't fully-featured—it just lets you export a timelapse (or real-time) for a given time frame right now. [The API exposes a _little_ more depth](https://docs.frigate.video/integrations/api/#post-apiexportcamerastartstart-timestampendend-timestamp), but I like the simplicity of the UI:

{{< figure src="./frigate-export-ui.jpg" alt="Frigate Export UI" width="700" height="auto" class="insert-image" >}}

Once I've exported the file, it's available to download from the server where Frigate's running (or a network storage location if you have Frigate configured to record to a network share). I download the file, then run the following `ffmpeg` command to re-compress it and speed it up a bit more (4x faster) than Frigate's own export functionality does:

```
ffmpeg -i exported-timelapse.mp4 -vf "scale=1920:1080,setpts=0.25*PTS" scaled.mp4
```

This also downsamples the footage to 1080p (from the original 4K source).

Then, if the footage needs a pass to remove any frames where no motion occurs, I run it through the `mpdecimate` filter:

```
ffmpeg -i scaled.mp4 -vf mpdecimate=hi=12800:lo=1200:frac=0.3,setpts=N/FRAME_RATE/TB scaled-and-decimated.mp4
```

The `mpdecimate` filter's documentation is a little obtuse, so the best guide I found is from Trembit: [FFmpeg Mpdecimate filter for Dummies](https://trembit.com/blog/ffmpeg-mpdecimate-filter-for-dummies/).

You might need to tweak some of the options (like `hi`/`lo`/`frac`) depending on the type of motion you want to exclude.

My current use case is for some household construction projects. I place the camera on a sturdy mount (like attached to a joist), wired with PoE through a switch attached to a UPS (so it stays up always, even if electric is cut during the project).

Then I take all the exports from the time periods where works is going on, and join them in Final Cut Pro later, and export a highly-condensed timelapse that's only a few minutes long in the end.

It's nice for not only feeling good about the progress, but also for future reference, if you need to see exactly where a pipe was laid, or how a wall was laid out.

Another option is a GoPro—which I've done in the past—but it's storage is finite, and powering it off battery is practically impossible over more than a 4-6 hour period. Using USB-C battery banks helped, but the only reliable way to do multi-day timelapses was with a USB-C wall wart (some work with it, some don't) and a huge (and expensive) 1 TB microSD card.

Using a central NVR with an IP camera (running off PoE) made the whole affair easier.
