---
nid: 3234
title: "How to download an MP4 from YouTube, every time"
slug: "how-download-mp4-youtube-every-time"
date: 2022-09-06T14:17:18+00:00
drupal:
  nid: 3234
  path: /blog/2022/how-download-mp4-youtube-every-time
  body_format: markdown
  redirects: []
tags:
  - mp4
  - open source
  - transcoding
  - tutorial
  - video
  - youtube
---

I use [yt-dlp](https://github.com/yt-dlp/yt-dlp) to download videos off YouTube quite frequently. I'll use the videos as reference, and I often use it to grab the VOD for one of my livestreams, since there's no simpler way (I'm not going to dig through the bowel's of YouTube's UI to try to download one of my own videos...).

But I also can't handle the default `.webm` videos in all my video editing tools natively, and transcoding is annoying. So I've settled on the following `yt-dlp` command to first try to pull a native MP4 version off YouTube, and failing that, transcode to MP4 immediately after downloading:

```
yt-dlp -S res,ext:mp4:m4a --recode mp4 https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

And if you weren't aware, `yt-dlp` does an excellent job pulling video files from other sites as well, should the need arise.
