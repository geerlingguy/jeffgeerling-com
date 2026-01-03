---
nid: 2684
title: "Converting a batch of Dashcam videos into a timelapse"
slug: "converting-batch-dashcam-videos-timelapse"
date: 2016-08-14T04:26:48+00:00
drupal:
  nid: 2684
  path: /blog/2016/converting-batch-dashcam-videos-timelapse
  body_format: markdown
  redirects:
    - /blog/2016/converting-batch-dashcam-videos-one-much-smaller-timelapse
aliases:
  - /blog/2016/converting-batch-dashcam-videos-one-much-smaller-timelapse
tags:
  - batch processing
  - dashcam
  - ffmpeg
  - homebrew
  - mac
  - photography
  - time lapse
  - video
---

I recently took a family vacation from St. Louis, MO to Branson, MO, and as it was the first time driving with [my new Mobius Action Cam Mini](https://www.amazon.com/Black-Box-Mobius-Action-Camera/dp/B00N6AWQ5I/ref=as_li_ss_tl?ie=UTF8&qid=1471115836&sr=8-1&keywords=mobius+action+cam+mini&linkCode=ll1&tag=mmjjg-20&linkId=bdf2e9761f73610209a29fa30b2bb866) dashcam installed on our Toyota Sienna ([see a full writeup and review here](/blog/2016/setting-dashcam-mobius-mini-action-cam-pro)), I wanted to see if I could quickly whip up a time lapse video of the entire drive.

<p style="text-align: center;">{{< figure src="./stl-driving-dashcam-loop.gif" alt="Driving in St. Louis - dashcam loop gif" width="480" height="270" class="insert-image" >}}<br />
<em>A tiny snippet of the final time-lapse video of my STL to Branson drive.</em></p>

While the Mobius has the ability to do time lapses built-in, doing so would require me to choose between either having a time lapse _or_ recording continuous 30fps video. And for insurance purposes, a timelapse with only a frame every second or two would not be that helpful!

So, knowing that my Mac can do many powerful things, I thought it might be able to do the following:

  1. Take a folder of 3-minute 1080p video clips at 30 frames per second straight from the Mobius Action Cam
  2. **Speed up the clips** to turn them into a proper time lapse (~5x or ~10x speedup).
  3. **Merge all the clips** into one, much more compact, time lapse video of the entire trip.

As an experiment, I wanted to just grab two files, speed both up, and merge them—after success there, I'll go on to automate the batch process for an entire directory of videos!

## Speeding up two videos

I grabbed the first two videos in a series of videos from our trip, and put them on my desktop. Then I did the following to get ready to speed up the videos:

  1. Open Terminal (in Applications > Utilities)
  2. Install ffmpeg (using [Homebrew](http://brew.sh/)): `brew install ffmpeg`
  3. Change directories to the Desktop: `cd ~/Desktop` (where I have two videos, `REC_0007.MOV` and `REC_0008.MOV`)

For each video (MOV format, straight from the Mobius Action Cam, 1080p, mono audio), I ran the command:

```
ffmpeg -i REC_0007.MOV -vf "setpts=0.05*PTS" -an SPEEDY7.MOV
```

I switched `7` for `8` to speed up the second video.

What this command does is grabs the input file (`-i`), sets the [Presentation TimeStamp](https://en.wikipedia.org/wiki/Presentation_timestamp) to `[value]*[current PTS]`, which is a fancy way of saying "make the video much faster—in this case 50x faster, with a value of `0.05`, and then store the re-encoded file in the same directory, with a different name.

## Merging two videos

With both videos considerably faster (50x) and smaller (~30 MB instead of ~400 MB), I wanted to merge the two to make one continuous video (since the Dash cam was configured to split clips in 3 minute increments, this is a necessary step if you want any kind of continuous viewing experience).

So, to merge the two clips, since they weren't in a format that allows direct 'concatenation' (e.g. `ffmpeg -i "concat:SPEEDY7.MOV|SPEEDY8.MOV" -codec copy compilation.mov`), I had to first create a text file that included one line for each clip, with the filesystem path to the clip (I called the file `concat.txt`):

```
file 'SPEEDY7.MOV'
file 'SPEEDY8.MOV'
```

> Note: If you don't use individual filenames (e.g. if you want to use a path like `~/Desktop/SPEEDY7.MOV` or `/path/to/file.mov`), then you will need to add the `-safe 0` option before the `-i` in the following command, otherwise you'll see an error like `Unsafe file name '~/Desktop/SPEEDY7.MOV' ... concat.txt: Operation not permitted`.

Then I ran `ffmpeg`'s command to concatenate videos based on a text file:

```
ffmpeg -f concat -i concat.txt -c copy compilation.mov
```

After running this command, I ended up with one video, but there were a few frames of a gap between the two which didn't look that great. I realized that the Mobius Action Cam sticks about an extra second from the previous clip at the start of the next clip... so I need to remove the duplicate frames _after_ the initial clip speedup process but _before_ concatenation using the `-ss` option ('seek' to position—thanks to [this Super User answer for the tip!](http://superuser.com/a/459488)):

```
ffmpeg -i SPEEDY8.MOV -ss 00.12 -an SPEEDY8-fixed.MOV
```

I used a value of `00.12` because I wanted to remove the _first three frames_ of the video after it had been sped up, and ffmpeg only accepts values in HH:MM:SS.SS (in this case, we have 30 fps, and want to remove two frames, so we need to _seek_ to `00.12` seconds (.03 seconds per frame) after the sped up video is written to disk. I also tried using `-ss 01.03` to remove the first 31 frames of the video _prior_ to speeding it up in the first command (e.g. `ffmpeg -ss 01.03 -i REC_0007.MOV -vf "setpts=0.05*PTS" -an SPEEDY7.MOV`), but this resulted in a couple 'junk' frames at the beginning that made the concatenated video have a stutter where the two clips were joined.

Compare by viewing the following video files:

<table style="width: 100%; border: none;" class="mobile-stack">
<tr>
<td style="width: 50%; vertical-align: top; padding: 15px 5px 10px;">
  <p style="text-align: center;"><video id="concat-extra-frames" src="./compilation-extra-frames-brief_0.mp4" width="1280" height="720" controls="true" preload="false" style="max-width: 95%; height: auto;"></video><br />
  <em><a href="./compilation-extra-frames-brief_0.mp4">1080p sped up video concatenation - uncorrected</a></em></p>
</td>
<td style="width: 50%; vertical-align: top; padding: 15px 5px 10px;">
  <p style="text-align: center;"><video id="concat-fixed" src="./compilation-fixed-brief_0.mp4" width="1280" height="720" controls="true" preload="false" style="max-width: 95%; height: auto;"></video><br />
  <em><a href="./compilation-fixed-brief_0.mp4">1080p sped up video concatenation - fixed!</a></em></p>
</td>
</tr>
</table>

I ran that command over both files, then concatenated them again, and now I have a much nicer clip! Now that I've proven I can do this programmatically, the next step is to _automate_ the process so I can process and combine hundreds of videos for a long trip (a 4 hour drive generated almost 100 3-minute clips!).

## Batching the process

I'm an advocate for automating _all the things_, and mundane tasks like re-encoding and concatenating dozens or hundreds of clips is the perfect candidate for automation! I spent some time wrapping all of the above commands into a flexible `dashcam-time-lapse.sh` shell script, which I've posted as a Gist on GitHub:

<script src="https://gist.github.com/geerlingguy/d515b8e85242b1787a4bbdc21c037495.js"></script>

That gist will be updated over time as needed, and I may be able to spend a little more time working on the CLI UX—for now, pop in your dashcam's memory card, adjust the variables at the top of the file, then run the script, and some time later, you'll end up with a file of sped-up footage from a recent drive!

## More Resources

  - [ffmpeg](https://ffmpeg.org/)
  - [ffmpeg options](https://ffmpeg.org/ffmpeg.html#Options)
  - [How do I join (concatenate) video files with ffmpeg?](https://www.ffmpeg.org/faq.html#How-can-I-join-video-files_003f)
