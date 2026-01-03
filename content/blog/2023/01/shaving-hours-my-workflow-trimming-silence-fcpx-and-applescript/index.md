---
nid: 3265
title: "Shaving Hours off my Workflow - Trimming silence with FCPX and AppleScript"
slug: "shaving-hours-my-workflow-trimming-silence-fcpx-and-applescript"
date: 2023-01-19T23:13:31+00:00
drupal:
  nid: 3265
  path: /blog/2023/shaving-hours-my-workflow-trimming-silence-fcpx-and-applescript
  body_format: markdown
  redirects:
    - /blog/2023/shaving-hours-my-workflow-trimming-silence-fcpx
aliases:
  - /blog/2023/shaving-hours-my-workflow-trimming-silence-fcpx
tags:
  - applescript
  - editing
  - editor
  - final cut pro
  - github
  - javascript
  - open source
  - video
---

{{< figure src="./final-cut-it-out-gap-clip-silence-automation-final-cut-pro-x.jpg" alt="Final Cut Pro X - Automatically trimmed silence cuts" width="700" height="374" class="insert-image" >}}

For the past few years, my workflow for editing videos for my YouTube channel was the following:

  1. Write and record narration / 'A-roll' using a teleprompter
  2. Import recording into timeline, and chop out silent portions manually using the blade and/or range tools
  3. Work on the rest of the edit (adding 'B-roll' and inserts).

Step 3 is where the vast majority of editing time is spent, especially when I need to add in charts, motion graphics, etc.

But Step 2 is mind-numbingly boring, especially since it means for a typical 10 minute video, I'm going to sit there for 30 minutes or so tweaking all the cuts in the silent portion, to try to make the audio flow from one section of the recorded text to the next.

And it's not just for teleprompter recordings. If you're editing screencasts, streaming VODs, vlogs, or interviews, there's a good chance there are a lot of silent portions that need to be cut out before the full editing process begins.

There are some great apps out there that automate some or all of this for you, like:

  - [Recut](https://getrecut.com) ($99, no subscription required)
  - [Timebolt](https://www.timebolt.io) ($17/month and up, depending on subscription)
  - [Descript](https://www.descript.com) ($12/month and up, depending on subscription)

But I figured, Final Cut Pro X is a professional video editing application used by tons of content creators around the world... surely there's a way I can do this without buying separate software that spits out an edit decision list I have to import into Final Cut, right?

Well... sort-of. After a good deal of research and testing, my new method for cutting out gaps of silence is [this osascript from jashmenn](https://gist.github.com/jashmenn/66f2806ae6da643a0bb16452629deee8). It needed a little tweaking to work for _my_ workflow, but combines ffmpeg's `silencedetect` filter with a little OSA/AppleScript automation to make all the cuts for me.

Step 2 goes like this, now:

  1. Run `ffmpeg -i [video.mp4] -af silencedetect=n=-35dB:d=800ms -f s16le -y /dev/null 2>&1 | tee silence.txt`
  2. Make sure Final Cut Pro is open to a timeline (or compound clip) with the same video portion visible.
  3. Run `./final-cut-it-out.js silence.txt`

The script runs through the video and makes cuts at all the silent portion boundaries, then goes back and deletes all those portions.

It's not perfect, and it would be nice to have a few of the more robust features like a real noise gate (attack, decay, etc. so I don't have tiny bits where there is a pop or I set something down), but this makes it so I can just run through and delete the bad takes, adjust the timings for some of the gap cuts, and be on my way!

I should note I changed the `moveToTimecode` portion of the code using [rlau1115's changes for 23.98p footage](https://gist.github.com/jashmenn/66f2806ae6da643a0bb16452629deee8?permalink_comment_id=3492585#gistcomment-3492585).

I also set a noise threshold of `-35dB` and a delay of `800ms` since that seems to offer the best results for my type of speech.

Finally, I also adjusted the margins to give the right amount of padding for the flow of my speech:

```
  const startMargin = 0.175;
  const endMargin = 0.200;
```

Your mileage may vary. I've actually forked the Gist into a separate GitHub repository, [final-cut-it-out](https://github.com/geerlingguy/final-cut-it-out), since I would like to work on improving it and making it more flexible for different framerates and margins.
