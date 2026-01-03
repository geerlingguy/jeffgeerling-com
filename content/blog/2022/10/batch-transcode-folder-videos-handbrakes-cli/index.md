---
nid: 3249
title: "Batch transcode a folder of videos with Handbrake's CLI"
slug: "batch-transcode-folder-videos-handbrakes-cli"
date: 2022-10-24T14:07:36+00:00
drupal:
  nid: 3249
  path: /blog/2022/batch-transcode-folder-videos-handbrakes-cli
  body_format: markdown
  redirects: []
tags:
  - cli
  - handbrake
  - mac
  - rip
  - terminal
  - transcoding
  - video
---

I've used [Handbrake](https://handbrake.fr) for years, to transcode practically any video file—including ripped DVDs and Blu-Rays—so I can watch the videos on practically any device. It's especially helpful for .mkv files, which can have a hodgepodge of video formats inside, and are notoriously difficult to play back, especially on older or more locked down playback devices.

But Handbrake's achilles heel, as a GUI-first application, is in a lack of easy batch operation. You can queue videos up one at a time, which is nice, but more recently, as I've ripped more TV seasons onto my NAS, I've wanted to transcode 5, 10, or 20 files at a time.

Enter [HandBrakeCLI](https://handbrake.fr/downloads2.php). Assuming you're on a Mac and installed Handbrake already (e.g. with `brew install --cask handbrake`), download `HandBrakeCLI`, mount the downloaded disk image, and copy the executable into a system path:

```
sudo cp /Volumes/HandBrakeCLI-1.5.1/HandBrakeCLI /usr/local/bin/
```

Then you can use it to loop over an entire directory—even recursively—and transcode all the video files within.

Here's a very tiny bash script I use to do just that, converting any file that ends in `.mkv` to an MP4 using the `General/HQ 1080p30 Surround` preset:

<script src="https://gist.github.com/geerlingguy/b21cc38430d06d39df82b0ab4f6c7d00.js"></script>

Let that run for a while, and you can transcode an entire TV series in one go.
