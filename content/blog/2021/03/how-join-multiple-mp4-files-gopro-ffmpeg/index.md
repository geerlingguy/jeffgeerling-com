---
nid: 3082
title: "How to join multiple MP4 files from a GoPro with ffmpeg"
slug: "how-join-multiple-mp4-files-gopro-ffmpeg"
date: 2021-03-18T03:32:02+00:00
drupal:
  nid: 3082
  path: /blog/2021/how-join-multiple-mp4-files-gopro-ffmpeg
  body_format: markdown
  redirects: []
tags:
  - cli
  - ffmpeg
  - gopro
  - mp4
  - video
---

I recently shot some footage with a GoPro, and realized after the fact the GoPro 'chapters' the footage around 4 GB, so I ended up with a number of 4 GB files, instead of one larger file. There are various reasons for this, but in the end, I really wanted one long file, so it would be easier to synchronize with footage from another camera and my audio recorder.

> **2023 Update**: The following one-liner works a bit faster, and doesn't require creating all the intermediate files as the original method below did:
>
> `ffmpeg -f concat -safe 0 -i <(for f in *.MP4; do echo "file '$PWD/$f'"; done) -c copy output.mp4`
>
> This command assumes you're running the command within the same directory as all your GoPro `.MP4` files, and there are no other `.MP4` files in that directory.

So I found [this answer on StackOverflow](https://superuser.com/a/1059261/80658), which had exactly the commands I needed:

```
ffmpeg -i 1.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts intermediate1.ts
ffmpeg -i 2.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts intermediate2.ts
ffmpeg -i 3.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts intermediate3.ts
ffmpeg -i 4.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts intermediate4.ts
ffmpeg -i "concat:intermediate1.ts|intermediate2.ts|intermediate3.ts|intermediate4.ts" -c copy -bsf:a aac_adtstoasc output.mp4
```

> **Note**: If you use the 'High Efficiency' (HEVC) encoder for your GoPro videos, change `h264_mp4toannexb` to `hevc_mp4toannexb` in the above commands.

This assumes I renamed my files from the GoPro to `1.mp4` and so on, and I'm in the same directory as those files. In the end, you should get a losslessly-joined MP4 file with the contents of all the video files from the sequence.

This is an annoying interim step for long-running footage from a GoPro—and I've noticed other action cams and dash cams seem to do the same thing.

And unfortunately, you can't just use `concat:` to join the files together in a one-liner, you have to build the intermediate files first (thus you need triple the original footage's size on your disk to do this trick). You can delete the originals and intermediate files once you confirm the `output.mp4` file is correct.
