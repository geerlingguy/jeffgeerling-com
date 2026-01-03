---
nid: 3317
title: "Can the Raspberry Pi 5 handle 4K?"
slug: "can-raspberry-pi-5-handle-4k"
date: 2024-05-31T13:59:25+00:00
drupal:
  nid: 3317
  path: /blog/2024/can-raspberry-pi-5-handle-4k
  body_format: markdown
  redirects:
    - /blog/2023/libreelec-on-raspberry-pi-5
    - /blog/2023/libreelec-and-4k-playback-on-raspberry-pi-5
    - /blog/2023/can-raspberry-pi-5-handle-4k
aliases:
  - /blog/2023/libreelec-on-raspberry-pi-5
  - /blog/2023/libreelec-and-4k-playback-on-raspberry-pi-5
  - /blog/2023/can-raspberry-pi-5-handle-4k
tags:
  - libreelec
  - media
  - pi 5
  - raspberry pi
  - tv
---

{{< figure src="./apple-tv-raspberry-pi-5-libreelec.jpeg" alt="Apple TV and Raspberry Pi 5 connected to LG OLED TV" width="700" height="auto" class="insert-image" >}}

In the past, I've booted [LibreELEC](https://libreelec.tv) on the Raspberry Pi Compute Module 4 in my "[This is not a TV](/blog/2022/tv-thats-not-necs-pi-powered-55-display)" Sharp NEC display.

According to [LibreELEC's Pi 5 blog post](https://libreelec.tv/2023/09/28/rpi5-support/), the new BCM2712 SoC decodes 4K and 1080p content just fine in H.264, and supports HEVC 4K60 hardware decoding.

And they've tested AV1, VC1, and VP9 at 1080p with no issue, though 4K in non-native formats does encounter frame dropping.

I wanted to put the Pi through some testing of my own, now that the Pi 5's been out for months, and LibreELEC version 12 is stable.

> Note: If you're interested in whether the Pi 5 can handle a 4K desktop monitor for Pi OS or Ubuntu, the answer to that is _definitely yes_. It is a much smoother experience than Pi 4, but if you want to do any media playback or gaming _within_ a desktop environment... it's not buttery smooth.
>
> This blog post covers 4K video playback, not 4K desktop environment rendering.

## Installing LibreELEC

This blog post won't go through the hardware and software setup for LibreELEC on the Pi 5, but the basic process is:

  1. Download the [LibreELEC Raspberry Pi image](https://libreelec.tv/downloads/raspberry/)
  2. Flash the image to a microSD card with [Balena Etcher](https://etcher.balena.io)
  3. Insert the microSD card into the Pi 5 and boot it connected to a TV.

For a full guide (and more visuals to accompany this blog post), watch my latest video on YouTube:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/3hFas54xFtg" frameborder='0' allowfullscreen></iframe></div>
</div>

## Remote Control

Before I get to the 4K results, I wanted to mention one important aspect of using a Pi 5 in a home theater environment, and that's how you control it.

A full keyboard and mouse would be cumbersome in a living room, though that doesn't stop some people from using a Logitech K400 or something similar. But the three primary options are:

  - HDMI-CEC allows you to use your existing TV or universal remote to send remote control commands directly to the Pi through HDMI. This is supported out of the box with LibreELEC and works with most modern TVs
  - A wireless mini remote like the [Rii i4](https://amzn.to/3yDPM2v) is handy since you might want to type in text using the built-in keyboard. It also has a trackpad, and LibreELEC supports mouse-based control.
  - A [Flirc USB IR receiver](https://amzn.to/3KjQJ2u) lets you directly control the Pi with any IR remote (or an IR blaster and any universal remote), and worked out of the box with all the IR remotes I've tested.

{{< figure src="./flirc-usb-raspberry-pi-5.jpeg" alt="Flirc USB Raspberry Pi 5" width="700" height="394" class="insert-image" >}}

Flirc even makes their own universal IR remote, the [Skip 1S](https://amzn.to/3yH0s0c), and it's a decent option in lieu of the Logitech Harmony line I used to recommend. The Pi Hut has a nice article explaining [how to use the Flirc IR Receiver for media control](https://thepihut.com/blogs/raspberry-pi-tutorials/control-your-raspberry-pi-media-centre-with-flirc).

## The 4K Experience

The main reason I set off on this journey with LibreELEC in the first place was to see how the Pi 5 handled 4K content. After all, there's only a hardware decoder for HEVC (H.265), the H.264 decoder was dropped in the latest BCM2712 SoC.

Pi engineers in the forums state the 2.5x faster Arm A76 CPU can handle H.264 decoding with more aplomb than the hardware decoder present on the Pi 4, but _can it really_?

{{< figure src="./pi-5-libreelec-big-buck-bunny-samples.jpg" alt="Big Buck Bunny on TV for Pi 5 LibreELEC resolution testing" width="700" height="auto" class="insert-image" >}}

For my testing, I converted [Big Buck Bunny](https://archive.org/details/big-buck-bunny-4k) from 4K 60 fps to various resolutions, using the 'HQ' defaults in Handbrake to convert to HEVC, H.264, AV1, and VP9. Here are the results:

| Resolution | Format | Notes |
| --- | --- | --- |
| 4K60 | H264 | watchable but with small stutters every now and then |
| 4K60 | HEVC | butter smooth |
| 4K60 | AV1 | jittery, not watchable |
| 4K60 | VP9 | better than AV1, but stutters enough to be noticeable |
| 4K30 | H264 | butter smooth |
| 4K30 | HEVC | butter smooth |
| 4K30 | AV1 | mostly smooth but with stutters, watchable |
| 4K30 | VP9 | mostly smooth with a few stutters but infrequent and easily watchable |
| 1080p60 | AV1 | almost perfect, only a frame skip every now and then |
| 1080p60 | H264 | almost perfect, only a frame skip every now and then |
| 1080p60 | HEVC | butter smooth |
| 1080p60 | VP9 | almost perfect, only a frame skip every now and then |
| 1080p30 | all formats | butter smooth |

I also tested many of my 'real world' video examples, as well as YouTube streaming through Kodi's default YouTube Add-On:

| Video type | Resolution | Format | Notes |
| --- | --- | --- | --- |
| YouTube | 4K30 | VP9 | butter smooth |
| NASA TV | 720p30 | VP9 | butter smooth |
| Dune (HDR10) | 4K24 | H.265 (HEVC) | butter smooth |
| Chernobyl | 1080p24 | H.264 | butter smooth |
| Bluey | 720p24 | H.264 | butter smooth |

My conclusion: real-world content, outside of 60fps 4K footage which is surprisingly rare still outside of consumer home videos, works fine on the Pi 5. Certainly as smooth as my 3rd-gen Apple TV 4K. And HDR10, Dolby Atmos, etc. are supported—though you may have trouble getting content from streaming platforms. But that's a whole _other_ ball of wax.

## Power and Noise

Before we go, I should mention the elephant in the room when it comes to the Pi and media center use: power control.

Unlike most set top boxes, the Pi 5 still doesn't have an easy way to 'wake' or power up after it's been powered off. What's worse, by default it'll burn 1.8W in the poweroff state, all day long. Not very energy-efficient!

For the leech current, you can fix that using [this guide I wrote last year, to set `POWER_OFF_ON_HALT`](/blog/2023/reducing-raspberry-pi-5s-power-consumption-140x) to a better default.

For powering on the Pi after it's been shut down... that's a little more complicated, but here are three options:

  1. You could integrate [fakewake](https://github.com/thagrol/fakewake) to virtually press the Pi 5's power button.
  1. You could add a [5V IR relay](https://amzn.to/3R61b1g) inline with the Pi 5's power supply to supply power or cut it off. (Or put the Pi 5 on a smart outlet with remote control).
  1. It could be possible—though it doesn't seem the Pi engineers are pursuing the feature at this time—to [send a magic Wake-on-LAN packet to boot the Pi 5](https://forums.raspberrypi.com/viewtopic.php?p=2189471), since the RP1 could listen for it while the Pi's powered off.

All those solutions are a little bit of a kludge, but could be made to work. Some other SBCs, like those from Orange Pi, may have the ability to [wake with an IR remote](http://forum.orangepi.org/orangepibbsen/forum.php?mod=viewthread&tid=2048), but how well that works depends on the specific model and software you're running on it.

You could just leave the Pi 5 running 24x7, though, if you're okay with it burning 3.7W at idle. My Pi 5 consumed 7-8W while playing back AV1 4K 60fps video, and 5-6W while playing back 4K 24fps HEVC content.

Fan noise with the official case is slightly noticeable during silent portions of a movie (from about 5' away), but I'd recommend using a fanless case if you want a truly silent setup.

I'll close this post out noting the one (and only) issue I ran into while testing LibreELEC 12: if I used my 5 GHz WiFi network, [it would drop out after a while and refuse to re-connect](https://github.com/LibreELEC/LibreELEC.tv/issues/8762). I did not have any issue on my 2.4 GHz WiFi or wired Ethernet.
