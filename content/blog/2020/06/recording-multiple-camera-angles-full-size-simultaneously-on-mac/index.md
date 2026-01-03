---
nid: 3014
title: "Recording multiple camera angles, full-size, simultaneously, on a Mac"
slug: "recording-multiple-camera-angles-full-size-simultaneously-on-mac"
date: 2020-06-08T19:31:28+00:00
drupal:
  nid: 3014
  path: /blog/2020/recording-multiple-camera-angles-full-size-simultaneously-on-mac
  body_format: markdown
  redirects: []
tags:
  - final cut pro
  - live
  - mac
  - macbook pro
  - macos
  - obs
  - quicktime
  - recording
  - video
  - youtube
---

I've been doing a lot of video production work for the past few months, both for [my YouTube channel](https://www.youtube.com/c/JeffGeerling), and in [helping people with their live streams](/blog/2020/how-i-livestream-obs-sony-a6000-and-cam-link), and one thing that I miss by not having dedicated (and expensive!) video production system like a [NewTek TriCaster](https://www.newtek.com/tricaster/) is being able to record _multiple_ camera angles at their full resolution _simultaneously_ on my Mac.

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/8NRz_ffr_KQ" frameborder='0' allowfullscreen></iframe></div>

There are a lot of little conveniences you get used to if you do professional live video production with high-end equipment that you often can't replicate in a budget studio... like my desk here at my house.

{{< figure src="./desk-multi-cam-setup.jpg" alt="Multi camera setup on Desk at home" width="600" height="338" class="insert-image" >}}

If all your cameras have their own storage, you can record on each of them, then bring the footage into your editor and sync the clips by audio afterwards. But this doesn't work with cameras that don't have onboard storage like webcams or PTZ cameras. Also, many cameras have recording time limitations. For example, my [Sony a6000](https://www.amazon.com/Sony-Mirrorless-Digitial-3-0-Inch-16-50mm/dp/B00I8BICB2/ref=as_li_ss_tl?dchild=1&keywords=sony+a6000&qid=1591624478&sr=8-3&linkCode=ll1&tag=mmjjg-20&linkId=fb82bf8aee3e263fbbcbc11f440592c5&language=en_US), which can only record 30 minute clips.

Wouldn't it be nice if you could record all the cameras _immediately_ on your computer? I mean, you can put multiple camera angles into software like [OBS](https://obsproject.com), and have them on-screen at the same time or switch between them live, so why not be able to also save different camera angles at their full resolution (e.g. 1080p) as separate files, so you can re-mix or re-cut the video angles as you see fit?

Well, unfortunately [OBS doesn't allow recording multiple cameras to separate files](https://obsproject.com/forum/threads/can-obs-record-multiple-video-tracks.52690/). So, during a livestream, unless you're willing to pay for somewhat expensive software like [mimoLive](https://boinx.com/mimolive/), or dedicated video production hardware like the TriCaster, you're stuck recording one video feed (which can have multiple cameras, but not at full resolution in separate files).

{{< figure src="./obs-wide-two-camera-hack.jpg" alt="OBS wide two camera angle recording hack" width="600" height="338" class="insert-image" >}}

One quick hack is to record one super-wide canvas in OBS, and place one camera on one side, and one on the other, and then crop the video out in editing later, but that's not fun to set up, it eats up even more computer resources (many computers would drop frames while recording, especially at higher resolutions and frame rates), and for longer recordings the post-processing required would take _forever_.

There was a utility for the Mac that _used_ to be supported and allowed easy multi-camera recording, called [CaptureSync](http://www.bensoftware.com/capturesync/), but it was unmaintained as of 2019, and likely won't work with newer Macs. It also cost a pretty penny, but as with most things in video production, it was well worth it if you needed this functionality frequently!

> **Update**: You can also use [ISO recording](https://www.vmix.com/knowledgebase/article.aspx/149/what-is-iso-recording-does-vmix-support-it) (_ISO_ for 'iso'lated recording of camera inputs) in [Wirecast](https://www.telestream.net/wirecast/) on Mac or Windows, or [vMix](https://www.vmix.com) on windows. Those apps are even more pricey, but if you rely on this functionality, they are solid options.

Now, on to the meat of this post: you may not know this, but QuickTime Player—an app that comes free with every Mac since forever—has had the capability to record clips from any attached camera for years. I often use it to capture video when I just need a quick clip. All you do is open QuickTime Player, then choose File > New Movie Recording, select a camera and sound source, and click the big red 'Record' button.

But something else you might not realize is _you can run more than one instance of QuickTime Player at the same time_! Here's how:

  1. Go into your Applications folder and find QuickTime Player.
  2. Right-click or control-click on it and choose 'Duplicate'.
  3. Open the original QuickTime Player:
    1. Choose File > New Movie Recording.
    2. Choose a camera and audio source. Make the window smaller so you can preview it alongside the next camera source you're about to open.
  4. Back in your Applications folder, open the new 'QuickTime Player' copy:
    1. Choose File > New Movie Recording.
    2. Choose a camera and audio source. Make the window smaller and move it alongside the other QuickTime video preview window.
  5. Click record in both instances of QuickTime.
  6. After you're done, click stop in both instances, and save the files.
  7. In software like Final Cut Pro, you can now sync the files using a [multicam clip](https://support.apple.com/guide/final-cut-pro/multicam-editing-workflow-ver10e087fd/mac).

{{< figure src="./two-cameras-record-quicktime.jpg" alt="Recording two camera angles in QuickTime" width="600" height="338" class="insert-image" >}}

Nice! One major drawback is you need to have a Mac that can handle the demand recording and saving two simultaneous streams requires. My brand new beefy MacBook Pro can handle two 1080p webcams ([Logitech C920](https://www.amazon.com/Webcam-Widescreen-Calling-Recording-Desktop/dp/B0876TG13V/ref=as_li_ss_tl?dchild=1&keywords=logitech+c920&qid=1591405204&s=electronics&sr=1-4&linkCode=ll1&tag=mmjjg-20&linkId=f887db175d74ed60d03685daba8d20c1&language=en_US)) without an issue. But toss 4K in the mix, and things get a little more dicey. Also, the longer the recording, the more chance you can get some dropped frames or delays, so this is not a great solution for multi-hour lectures or time-lapses.

But can you do three cameras with the same setup? Yep! Just make another copy of QuickTime Player, launch it, and you're off to the races!

{{< figure src="./three-cameras-record-quicktime.jpg" alt="Recording three camera angles in QuickTime" width="600" height="338" class="insert-image" >}}

When I was testing with my [Sony a6000](https://www.amazon.com/Sony-Mirrorless-Digitial-3-0-Inch-16-50mm/dp/B00I8BICB2/ref=as_li_ss_tl?dchild=1&keywords=sony+a6000&qid=1591405149&sr=8-3&linkCode=ll1&tag=mmjjg-20&linkId=70a48a8563e452a0d91232d08fd8a9f2&language=en_US) at 60 frames per second through a [Cam Link 4K](https://www.amazon.com/Elgato-Cam-Link-Broadcast-Camcorder/dp/B07K3FN5MR/ref=as_li_ss_tl?cv_ct_cx=cam+link+4k&dchild=1&keywords=cam+link+4k&pd_rd_i=B07K3FN5MR&pd_rd_r=f30eaa09-4acf-42d4-8a19-1a9cf51ae8cf&pd_rd_w=kLyNv&pd_rd_wg=iyfGc&pf_rd_p=1da5beeb-8f71-435c-b5c5-3279a6171294&pf_rd_r=2B3HX3553RXX079A5RB2&psc=1&qid=1591405171&sr=1-1-70f7c15d-07d8-466a-b325-4be35d7258cc&linkCode=ll1&tag=mmjjg-20&linkId=3ac58161a0c5a2c80987e6276b62b7f9&language=en_US), along with the two aforementioned Logitech C920 webcams, my CPU got a bit toasty, at almost 100°C, and the fans were on at full blast—but the recording still worked!

The limit here is really how many instances of QuickTime Player your Mac can run while recording the video and not melt down.

_Technically_, you could do the same thing with multiple instances of OBS, but OBS is a _lot_ more heavyweight and prone to exploding, and I fear I'd end up with a melted blob of aluminum on my desk.
