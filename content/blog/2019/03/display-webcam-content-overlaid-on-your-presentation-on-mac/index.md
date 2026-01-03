---
nid: 2914
title: "Display webcam content overlaid on your presentation on a Mac"
slug: "display-webcam-content-overlaid-on-your-presentation-on-mac"
date: 2019-03-22T02:40:33+00:00
drupal:
  nid: 2914
  path: /blog/2019/display-webcam-content-overlaid-on-your-presentation-on-mac
  body_format: markdown
  redirects: []
tags:
  - mac
  - presentations
  - quicktime
  - raspberry pi
  - tutorial
  - video
  - vlc
  - webcam
---

For my Raspberry Pi Dramble presentation, [Everything I know about Kubernetes I learned from a cluster of Raspberry Pis](https://www.midcamp.org/2019/topic-proposal/everything-i-know-about-kubernetes-i-learned-cluster-raspberry-pis), I wanted to be able to show all of the audience—who could be dozens or hundreds of feet away—a tiny Raspberry Pi cluster of computers, which is in total about the size of a cantaloupe.

{{< figure src="./logitech-webcam-shooting-pis-for-presentation.jpg" alt="Logitech webcam and Raspberry Pi Dramble Cluster for presentation" width="650" height="433" class="insert-image" >}}

I wanted to find a way to display an external USB webcam (in my case [this Logitech 1080p webcam](https://www.amazon.com/Logitech-C922x-Pro-Stream-Webcam/dp/B01LXCDPPK/ref=as_li_ss_tl?ascsub&crid=14OGNW5QULF33&cv_ct_id=amzn1.osp.fbf3c4ea-9062-42af-98ad-b23785c16816&cv_ct_pg=search&cv_ct_wn=osp-search&keywords=logitech+1080p+webcam&pd_rd_i=B01LXCDPPK&pd_rd_r=ab94a3f2-baf6-4310-84c8-f32fa5f3b03a&pd_rd_w=l6wsI&pd_rd_wg=D8O5p&pf_rd_p=37dcfc87-cdc2-4138-941e-56f6d8e6b463&pf_rd_r=4YB61R738FZEJKDYQ053&qid=1553185883&s=gateway&sprefix=logitech+1080p+,aps,253&linkCode=ll1&tag=mmjjg-20&linkId=604c5e78d947726ce14c09dcb2a614e0&language=en_US)) live picture, overlaid on my presentation. I found that there are actually _two_ ways to do it on the Mac:

  - Using QuickTime Player with 'Float on top'
  - Using VLC with 'Float on Top'

## Preparing the webcam

If you use a Logitech camera like I do, you can ensure it's focus is tack-sharp and color balance is the way you want it to be:

  1. Download the 'Camera Settings' app, and open it up after you plug in your webcam, but before you get started with your presentation.
  1. Go to the 'Advanced Settings'
  1. Turn off autofocus, then manually adjust the focus slider until it's tack sharp.
  1. Also consider turning off auto white-balance and setting that manually too so the color balance doesn't change during the presentation.

## Using QuickTime

  1. Open QuickTime.
  1. Choose File menu > New Movie Recording
  1. Choose 'High' or 'Maximum' resolution from the little dropdown menu next to the record button.
  1. When you need it to 'float' on top of all other windows, choose View menu > Float on top.

Now it should look something like this:

{{< figure src="./quicktime-player-float-on-top-resized.png" alt="QuickTime Player float on top of other windows" width="650" height="406" class="insert-image" >}}

There are two downsides to using QuickTime, though:

  1. You can't get the player controls to stay hidden on hover like you can with VLC, so you have to be careful moving your mouse over the video window.
  1. For certain apps, like Keynote, it actually _doesn't_ 'float on top', which may defeat the point depending on what/how you're presenting!

Luckily, VLC overcomes both of these issues—though I sometimes had stability issues with the webcam connection in VLC. The image froze sometimes and I would have to re-plug the webcam to get it back in VLC (while QuickTime never exhibited the same problem, even while VLC was doing a freeze frame!).

## Using VLC

If you want to float a VLC-driven live view of the webcam, do the following:

  1. Download and install VLC.
  1. Open VLC, and go to VLC menu > Preferences...
  1. Go to the Video section, and uncheck the 'Window decorations' setting.
  1. Choose File menu > Open Capture Device...
  1. In the Capture tab, check the 'Video' checkbox, then select your USB webcam. If it asks for a resolution, choose the maximum you need (e.g. 1280 x 720 or 1920 x 1080).
  1. Click Open and a window should pop up with the live feed from your webcam. Yay!
  1. When you need it to 'float' on top of all other windows, choose Video menu > Float on Top.

Now it should look something like this:

{{< figure src="./vlc-player-float-on-top-resized.png" alt="VLC player float on top of other windows" width="650" height="406" class="insert-image" >}}

## How did it work?

You tell me: skip to 13:10 in the video below!

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/z2g7r7Wyh9g" frameborder='0' allowfullscreen></iframe></div>

## Conclusion

Any other cool hacks you can think of to show off something via the external webcam? I know one thing I'd like to figure out is how I can use one of my mirrorless or DSLR cameras with it's fancy lenses as my external webcam, for some even better image quality!
