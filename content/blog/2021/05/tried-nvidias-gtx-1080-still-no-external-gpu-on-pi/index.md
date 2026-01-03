---
nid: 3095
title: "Tried Nvidia's GTX 1080 - still no external GPU on a Pi"
slug: "tried-nvidias-gtx-1080-still-no-external-gpu-on-pi"
date: 2021-05-14T01:33:25+00:00
drupal:
  nid: 3095
  path: /blog/2021/tried-nvidias-gtx-1080-still-no-external-gpu-on-pi
  body_format: markdown
  redirects:
    - /blog/2021/tried-nvidia-geforce-gtx-1080-still-no-graphics-card-working-on-pi
aliases:
  - /blog/2021/tried-nvidia-geforce-gtx-1080-still-no-graphics-card-working-on-pi
tags:
  - compute module
  - gpu
  - graphics
  - livestream
  - nvidia
  - raspberry pi
  - video
  - youtube
---

Earlier today I did a livestream on my YouTube channel to [attempt using an Nvidia GeForce GTX 1080 on a Raspberry Pi Compute Module 4](https://www.youtube.com/watch?v=1hFPnpVqzkw).

{{< figure src="./nvidia-geforce-gtx-1080.jpeg" alt="MSI Nvidia GeForce GTX 1080 Graphics Card GPU" width="650" height="434" class="insert-image" >}}

As with all my testing, I'm documenting everything I learn in [this GitHub issue](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/123), which is part of the [Raspberry Pi PCI Express Card Database](https://pipci.jeffgeerling.com) website.

It's only been a few hours, but I've already gotten good suggestions for better debugging than I was able to do on the stream. And someone pointed out it might be the case, due to 32-bit memory limitations on the BCM2711's PCIe bus, that no GPU with more than 4 GB of onboard RAM could work. Though it's hard to confirm there'd be no software workaround—even 1 and 2 GB graphics cards (AMD and Nvidia) are crashing the kernel in similar ways.

The full livestream is available on replay and is embedded below:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/1hFPnpVqzkw" frameborder='0' allowfullscreen></iframe></div>
</div>

And in that livestream, I compared the 'chonky' size of the 1080 card to the diminutive ASRock Rack M2_VGA card [I tested a few weeks ago](https://www.youtube.com/watch?v=MxcafwjWw24), tried installing Nvidia's proprietary driver on 64-bit Pi OS (which locked up), tried recompiling the kernel with Nouveau (which locked up), and then documented all the failures in the GitHub issue linked earlier in this post.

I was expecting failure, and said as much at the beginning of the stream—5% chance of success, 10% chance of [releasing the magic smoke](https://redshirtjeff.com/listing/release-the-magic-smoke?product=46)—but it would be nice to get any graphics card to work well on a Pi, for a variety of uses. But probably not AAA gaming, since gaming on Linux is a tough proposition even in the best of circumstances.

Some people also suggested testing on an Nvidia Jetson board, or a Honeycomb, but the former is a bit pricey, and the latter seems to be unobtanium right now (as with so many components these days). I mean heck, I would also love to find a way to loan an Ampere server for a short time so I could basically use the best ARM hardware on offer... but alas those prices are astronomically beyond my budget right now :)

I'll keep plugging away, and hopefully if not me, then someone will get an AMD or Nvidia GPU working on the Pi. [Coreforge is certainly close with an old Radeon 6450](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/4).
