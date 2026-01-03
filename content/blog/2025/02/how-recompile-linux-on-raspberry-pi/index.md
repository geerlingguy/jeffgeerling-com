---
nid: 3443
title: "How to Recompile Linux (on a Raspberry Pi)"
slug: "how-recompile-linux-on-raspberry-pi"
date: 2025-02-18T21:46:41+00:00
drupal:
  nid: 3443
  path: /blog/2025/how-recompile-linux-on-raspberry-pi
  body_format: markdown
  redirects: []
tags:
  - drivers
  - intel
  - kernel
  - level2jeff
  - linux
  - raspberry pi
  - tutorial
  - video
  - xe
  - youtube
---

Because I get the same question on every video where I recompile the Linux kernel on a Pi to work on GPU or other hardware driver support, I finally made a video answering it:

_How do you recompile Linux?_

In my case, since I mostly rebuild the kernel for the Pi, I rebuild [Raspberry Pi's Linux kernel fork](https://github.com/raspberrypi/linux) instead of 'mainline' linux (the upstream [Linux kernel source](https://www.kernel.org)).

There are a couple great guides for recompiling Linux on the Pi:

  - [Jeff Geerling's cross-compile environment](https://github.com/geerlingguy/raspberry-pi-pcie-devices/tree/master/extras/cross-compile#readme), with guides for compiling on a Pi, or from any other computer quickly, using a containerized build environment that's easy to set up on Mac, Windows, or Linux.
  - Raspberry Pi's thorough [guide for building and cross-compiling Linux](https://www.raspberrypi.com/documentation/computers/linux_kernel.html#building), including how to compile 32-bit versions for older generations of Pi.

My video today mostly goes through that (with a few little tips on making the experience more convenient):

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/7ZxgZZu_NEA" frameborder='0' allowfullscreen></iframe></div>
</div>

In the video, I also mention one practical reason I'm rebuilding the kernel _currently_ is to work on Raspberry Pi (and more broadly, arm64) support for Intel Arc GPUs (I'm testing a [B580](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/695) and [A750](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/510) currently.)

And _yes_, the Raspberry Pi [should support Resizable BAR](https://github.com/raspberrypi/linux/issues/6621#issuecomment-2605589332), though we're trying to figure out why the Xe drivers aren't working correctly with it right now.
