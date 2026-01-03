---
nid: 3373
title: "Achieving Pro Zoom meeting quality on my Mac"
slug: "achieving-pro-zoom-meeting-quality-on-my-mac"
date: 2024-05-09T16:51:18+00:00
drupal:
  nid: 3373
  path: /blog/2024/achieving-pro-zoom-meeting-quality-on-my-mac
  body_format: markdown
  redirects: []
tags:
  - cameras
  - desk
  - obs
  - remote work
  - video
  - youtube
  - zoom
---

{{< figure src="./desk-setup-azden-mic.jpg" alt="Azden shotgun mic on desk setup" width="700" height="auto" class="insert-image" >}}

For the past decade, I've worked remote. I slowly moved from full-time software and infrastructure dev to YouTuber, and throughout that time, I kept tweaking my desk video recording/conferencing setup.

I wanted to document my setup today, as I've tweaked it a bit in my new studio space. Hopefully some of my tools and techniques can help you, or maybe you can find a way to make a simpler (hopefully cheaper) but higher quality setup!

I made a video going through everything in detail, but I'll mention the highlights in this post:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/UF-MAuGPhcY" frameborder='0' allowfullscreen></iframe></div>
</div>

> Note: I have linked to most of the products I mention below using Amazon affiliate links, which means if you buy a product using that link, I get a tiny kickback. If you wish to bypass that, no problem—I mention the full product name so you can search it yourself or buy from some other site!

{{< figure src="./desk-setup-2024.jpg" alt="Desk Setup 2024 for video conferencing zoom recording obs" width="700" height="auto" class="insert-image" >}}

For video, I have my [Sony a6600](https://amzn.to/3JWnxhC) with a [Sony 24mm f/1.8 lens](https://amzn.to/4bNRVab) mounted on an [Elgato Prompter](https://amzn.to/3wDVGzI).

The camera is powered by an [AC adapter / 'dummy battery pack'](https://amzn.to/4dvDRnc) so the battery doesn't overheat, or run out, in the middle of a long meeting. I have that adapter plugged into a [ThirdReality Zigbee Smart Outlet](https://amzn.to/3JTrQdD), which I tie into my Home Assistant Yellow. The switch can be remotely controlled on my Stream Deck using the [StreamDeck Home Assistant Plugin](https://github.com/cgiesche/streamdeck-homeassistant), so I can press a button to turn on the camera remotely (and turn it off).

I also have two [Elgato Key Lights](https://amzn.to/4bdBfsK) for key/fill light, then a cheap [Utilitech 4' LED worklight](https://www.lowes.com/pd/Utilitech-4-ft-Light-LED-Linear-Shop-Light/5000858985) to fill in the background and provide a small amount of 'catch' light on my hair (it helps separate my hair from the background).

To mount the Prompter setup on my desk, I have a [HUANUO Monitor Stand Desk Mount](https://amzn.to/3WA1NQj), with a [Manfrotto 2909 Super Clamp](https://amzn.to/4b81EIo) holding a [Manfrotto 244 Variable Friction Magic Arm](https://amzn.to/4bam1oi). That magic arm is very heavy duty, and can hold like 20+ lbs, which is great for a setup involving a mirrorless camera.

For audio, I'm using an [Azden SGM-250CX Compact Shotgun](https://amzn.to/4dJ7yRY), mounted on a [Manfrotto 196B-2 Articulated Arm](https://amzn.to/3UtDpgy), plugged into a [Behringer UMC202-HD USB Audio Interface](https://amzn.to/4acTFs4) (my Behringer's been discontinued but the newer model linked here is about the same, just one channel).

The shotgun is positioned _just_ out of the top of the frame, as close as possible to my mouth, so the sound quality is about as good as a desktop mic, just without some of that podcast/radio-y proximity effect on the low end.

Because the camera's HDMI output goes through an [Elgato Cam Link 4K](https://amzn.to/3wvfRjn), which adds about 200ms of latency to the video signal, I have to add delay to the audio as well.

In OBS, under 'Advanced Audio Properties', I can add a 'Sync Offset' to the Mic input. But for apps like Zoom or Teams, I have to get more creative. Even if I use the OBS Virtual Camera, there's no way I can find to have its processed audio feed get out of OBS and route it into Zoom/Teams/etc.

So I use Rogue Amoeba's [Loopback](https://rogueamoeba.com/loopback/) and [Audio Hijack](https://rogueamoeba.com/audiohijack/) to add a 200ms delay to a secondary mic input audio source for any application on my Mac to use:

{{< figure src="./audio-hijack-pro-sync-offset.jpg" alt="Rogue Amoeba Audio Hijack Pro Sync Offset Audio" width="700" height="auto" class="insert-image" >}}

Then in Zoom I choose the audio input source I set up for passthrough audio in Loopback, and the audio signal syncs up perfectly to the video signal. Nice!

With all this, I'm able to press two buttons on my Stream Deck to turn on the lights and camera, then I open up either OBS or Zoom (or both), and I end up looking like:

{{< figure src="./jeff-geerling-zoom-camera-2024.jpg" alt="Jeff Geerling Looking at Zoom" width="700" height="auto" class="insert-image" >}}

...Except hopefully looking a little more natural!
