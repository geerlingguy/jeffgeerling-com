---
nid: 3103
title: "The Apple M1 compiles Linux 30% faster than my Intel i9"
slug: "apple-m1-compiles-linux-30-faster-my-intel-i9"
date: 2021-06-01T19:11:05+00:00
drupal:
  nid: 3103
  path: /blog/2021/apple-m1-compiles-linux-30-faster-my-intel-i9
  body_format: markdown
  redirects: []
tags:
  - arm64
  - benchmarks
  - intel
  - linux
  - m1
  - mac
  - macbook air
  - macbook pro
---

(With a caveat: I'm compiling the ARMv8 64-bit Pi OS kernel.)

It seems every week or so on Hacker News, a story hits the front page showing some new benchmark and how one of the new M1-based Macs matches or beats the higher-priced competition in some specific benchmark—be it [GeekBench](https://news.ycombinator.com/item?id=25065026), [X86-specific code](https://news.ycombinator.com/item?id=25105597), or [building Emacs](https://news.ycombinator.com/item?id=25769469).

Well, here's my quick story.

I've been doing a _lot_ of work with Raspberry Pis lately—more specifically, work which often requires recompiling the Pi OS Linux kernel for the `aarch64` architecture. I recompile the kernel enough I [made my own shirt for it](https://redshirtjeff.com/listing/linux-recompile-shirt?product=211)!

<p style="text-align: center;"><a href="https://redshirtjeff.com/listing/linux-recompile-shirt?product=211">{{< figure src="./it-has-been-zero-days-since-i-recompiled-the-linux-kernel.jpg" alt="Linux shirt from Red Shirt Jeff.com - It has been 0 days since I recompiled the Linux kernel" width="400" height="400" class="insert-image" >}}</a></p>

With [this Docker-based environment](https://github.com/geerlingguy/raspberry-pi-pcie-devices/tree/master/extras/cross-compile) on my 2019 Intel i9 16" MacBook Pro, I can compile the kernel from scratch in about 12 minutes.

The Intel laptop cost over $3000 when I bought it, and the thing is basically a frying pan on my legs and has two obnoxiously-loud fans running full blast whenever you even look at it sideways.

I bought both an M1 10 Gbps Mac mini _and_ a M1 MacBook Air to replace the 16" Pro—for the same total price—and I ran the same compile on it, using the [exact same configuration](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/150).

Total time for the test was 9 minutes on the mini (which has a fan to keep the CPU cool under load) and 10 minutes on the Air (which doesn't have a fan, so it starts to throttle after a while).

{{< figure src="./m1-vs-i9-linux-kernel-recompile.png" alt="M1 vs i9 Linux Kernel Recompile for Raspberry Pi OS" width="636" height="283" class="insert-image" >}}

And even if the mini's fan came on during the build (it probably did), I couldn't even hear it over the ambient 32dB environment in my office. The Air was blissfully silent.

## That's not fair!

Yeah, well, it's one of the things that takes the most time and makes an impact on my own workflow. I know that _cross-compiling_ Linux on an Intel X86 CPU _might_ not be as fast as compiling on an ARM64-native M1... but that's not the point.

This is a very real benchmark that impacts my ability to get work done. And it's faster on even the cheapest low-end M1 Mac. And the fans are silent (or nonexistent), and the heat output and energy consumption is minimal.

I mean heck, the power supply for the i9 MacBook Pro is comically large compared to the Air's supply:

{{< figure src="./macbook-air-vs-pro-i9-power-supply-30w-vs-96w.jpeg" alt="M1 MacBook Air vs Intel 2019 i9 16 inch MacBook Pro USB-C Power Adapter" width="600" height="400" class="insert-image" >}}

And even the 96W adapter is smaller than most PC laptop PSUs I've used, especially for the type of 'luggable desktop' machine commenters will, I'm sure, point out, which could destroy my M1s with more cores (and more power consumption and heat)!

## What matters?

In the end, I'm happy with my decision—overall. The M1 platform definitely has some growing pains.

For example, my mini has weird issues on both HDMI _and_ DisplayPort connections so far:

  - If using HDMI to my LG 4K display at 60 Hz, the display just blanks out entirely for 2-4 seconds every 5 minutes or so. No clue why.
  - If using DisplayPort through a [CalDigit TS3 Plus](https://amzn.to/34E9zfY) dock, the display works great, but when I put the mini to sleep, or the display shuts off, the LG display keeps restarting itself every 10 seconds or so, which is highly annoying.

What matters most to _me_, though, is the fact that I can do my work faster, with less energy use, _way_ longer battery life, and all without burning my legs every time I use my laptop on my lap.

I was questioning whether I'd still use an Apple laptop after my [bad experiences with both the Touch Bar and non-Touch Bar 2016 MacBook Pro](/blog/2017/i-returned-my-2016-macbook-pro-touch-bar), and the 2019 MacBook Pro had just enough charm to keep me running macOS daily. But if these first-generation M1 Macs are anything to go by, I think I'm going to be a happy macOS user for a while longer.

Now, if only Apple and Raspberry Pi could partner up and build an SBC with the M1...
