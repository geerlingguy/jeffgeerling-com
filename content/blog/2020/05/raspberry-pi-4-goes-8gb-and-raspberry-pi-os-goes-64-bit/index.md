---
nid: 3011
title: "Raspberry Pi 4 goes 8GB, and Raspberry Pi OS goes 64-bit!"
slug: "raspberry-pi-4-goes-8gb-and-raspberry-pi-os-goes-64-bit"
date: 2020-05-28T22:00:33+00:00
drupal:
  nid: 3011
  path: /blog/2020/raspberry-pi-4-goes-8gb-and-raspberry-pi-os-goes-64-bit
  body_format: markdown
  redirects: []
tags:
  - 64-bit
  - benchmarks
  - raspberry pi
  - raspbian
  - video
  - youtube
---

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/aidkpsWlB40" frameborder='0' allowfullscreen></iframe></div>

This morning the Raspberry Pi Foundation [announced a new 8 GB version of the Raspberry Pi 4](https://www.raspberrypi.org/blog/8gb-raspberry-pi-4-on-sale-now-at-75/). They've been selling a 1, 2, and 4 GB version for the past year, and I've been using all three models in my projects.

{{< figure src="./rpi-4-8gb-model-b.jpg" alt="8GB Raspberry Pi 4 - photo from Raspberry Pi Foundation website" width="600" height="auto" class="insert-image" >}}

More RAM is always better, because you can fit more applications on the same Pi, especially if you're using them in a Kubernetes cluster, like I am in my [Turing Pi Cluster series](https://www.youtube.com/watch?v=kgVz4-SEhbE)!

But one problem with more RAM on a Raspberry Pi is that the current version of Raspbian, which is a 32-bit operating system, can only use a small amount of the memory for any given process, so one application couldn't use all 8 GB of RAM.

So the Raspberry Pi Foundation also announced that Raspbian OS is now going to be called Raspberry Pi OS, and there's a new 64-bit beta version available today. You can download it from [this post in the Raspberry Pi forums](https://www.raspberrypi.org/forums/viewtopic.php?f=117&t=275370).

What's so great about 64-bits? Well, there are [lots of reasons it's better](https://medium.com/@matteocroce/why-you-should-run-a-64-bit-os-on-your-raspberry-pi4-bd5290d48947), some which are more technical and I won't talk about in this video, but one very practical thing is there's more software, especially for things like Docker images, that's built with ARM 64-bit compatibility.

As an example, many of the container images that I'm going use in my next Pi Cluster video are available for X86-64, which is basically modern Intel or AMD processors, but they won't run on any Raspberry Pi. But more and more 'arm64' images are becoming available, and these work on all 64-bit ARM processors, like the ones used in [AWS ARM instances](https://aws.amazon.com/ec2/instance-types/a1/) or if you run [Ubuntu 64-bit](https://ubuntu.com/download/raspberry-pi) on your Raspberry Pi.

This new 64-bit Pi OS will allow me to use more Docker images and software, and that's a good thing!

In the comments on the blog post announcing these new products, Ebon Upton also dropped some new information.

He said that the [Raspberry Pi Compute Module 4 will be released this year](https://www.raspberrypi.org/blog/8gb-raspberry-pi-4-on-sale-now-at-75/#comment-1530439). This is really good news for the performance of my Turing Pi cluster! Also, Simon Long, a Raspberry Pi employee, [said](https://www.raspberrypi.org/blog/8gb-raspberry-pi-4-on-sale-now-at-75/#comment-1530366) there would be more details about the transition from Raspbian to Raspberry Pi OS in a blog post coming out tomorrow.

## 64-bit Beta of the Raspberry Pi OS - Test Results

I've been testing the beta 64-bit OS today, and here's what I learned:

Some guides and software that have special Pi configurations are currently broken on the 64-bit OS. One interesting thing I noticed is that with Raspbian, if you check the OS release file that's in `/etc/os-release`, the name is set to "Raspbian", but with Raspberry Pi OS, the name is "Debian". If software uses this name as a way to see whether it's running on a Raspberry Pi or not, that can break things.

{{< figure src="./fft-cpu-benchmark-pi.png" alt="Benchmark - Pi OS 32-bit vs 64-bit FFT CPU benchmark" width="500" height="auto" class="insert-image" >}}

I also [ran a bunch of short benchmarks on the 64-bit OS](https://github.com/geerlingguy/drupal-pi/issues/45) (note: I'm still running a few more), then ran the same benchmarks on the current Raspbian 32-bit release, and the results were surprising. A lot of CPU-heavy operations are faster on the 64-bit OS. See more benchmarks in [this Medium.com post by Matteo Croce](https://medium.com/@matteocroce/why-you-should-run-a-64-bit-os-on-your-raspberry-pi4-bd5290d48947).

In the real world, outside of benchmarking, you won't notice a _huge_ difference, but it's definitely faster.

The bottom line is this: don't get too angry if you're using beta software and you run into some issues! While I was doing my testing, the Pi locked up a couple times during network load testing, requiring a reboot, and I couldn't figure out exactly why. If you need something stable, stick with the current Raspberry Pi OS, and wait for the 64-bit version to be out of beta.

## Summary

I don't yet have the 8 GB Pi 4, but I've ordered one hopefully I'll be able to share my thoughts soon! I'm working hard on the next videos for the Pi Cluster series, and I know a lot of people are interested in them, so to make sure you see them, [subscribe to my YouTube channel](https://www.youtube.com/c/JeffGeerling) and support my work on [Patreon](https://www.patreon.com/geerlingguy) or [GitHub Sponsors](https://github.com/sponsors/geerlingguy).
