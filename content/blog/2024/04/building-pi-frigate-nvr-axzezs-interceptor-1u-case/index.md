---
nid: 3368
title: "Building a Pi Frigate NVR with Axzez's Interceptor 1U Case"
slug: "building-pi-frigate-nvr-axzezs-interceptor-1u-case"
date: 2024-04-19T14:12:53+00:00
drupal:
  nid: 3368
  path: /blog/2024/building-pi-frigate-nvr-axzezs-interceptor-1u-case
  body_format: markdown
  redirects:
    - /blog/2024/building-pi-nvr-axzezs-interceptor-1u-case
aliases:
  - /blog/2024/building-pi-nvr-axzezs-interceptor-1u-case
tags:
  - axzez
  - frigate
  - homelab
  - nvr
  - rack
  - raspberry pi
  - video
  - youtube
---

{{< figure src="./axzez-interceptor-1u-raspberry-pi-frigate-nvr.jpeg" alt="Axzez 1U Interceptor Case with Raspberry Pi NVR" width="700" height="auto" class="insert-image" >}}

In today's video, I walked through [setting up Axzez's Interceptor 1U case with a Raspberry Pi as a Frigate NVR](https://www.youtube.com/watch?v=7wkVGcdI2vk), or Network Video Recorder.

Doing so allows me to plug multiple PoE security cameras straight into the back of the device, and record their IP video streams to disk (the case has space for up to 3 hard drives or SSDs). And by adding on a USB Coral TPU, I can also run inference on frames where motion is detected, and identify people, cars, bikes, and more using built-in object recognition models.

{{< figure src="./interceptor-1u-rear-lan-plugged-in.jpeg" alt="Axzez 1U Interceptor Case with network and Coral TPU plugged in" width="700" height="auto" class="insert-image" >}}

The video makes use of my open source [pi-nvr](https://github.com/geerlingguy/pi-nvr) project, which uses Ansible to install NVR software on a Raspberry Pi. A Raspberry Pi isn't a strict requirement—Frigate and other open source NVR apps run great on a wide variety of computers—but it is efficient and well-supported. And, nowadays you can find a Pi 4 or Pi 5 most anywhere.

The Axzez Interceptor makes use of the Compute Module 4, which exposes PCI Express through it's board-to-board connector. This lets the Interceptor use up to 5 SATA connections for the hard drives, meaning using disks in RAID is more reliable than if you were to plug them in using USB.

A Pi 5 or future Compute Module 5 could increase bandwidth and likely support 2-4x more cameras than the Compute Module 4, but I am only planning on deploying four or five HD (1080p) cameras for now.

## Optimizing Frigate on the Raspberry Pi

Unless you've been under a rock, the past few years have changed a lot regarding the [Raspberry Pi's value proposition as a tiny homelab PC](https://www.youtube.com/watch?v=jjzvh-bfV-E). Between shortages and the first-ever price increase for the Pi 5 base model ($35 for 1 GB Pi 4 to $60 for 4GB Pi 5), there are a lot of times when a used mini PC could be a better value, even if it uses 1.5-2x more power at idle.

Especially considering the iGPUs built into more modern Intel mini PCs, they are a great value for a simple router, a small VM server running Proxmox, or even as a Frigate NVR box. You could even skip the Coral TPU if the built-in iGPU is fast enough.

But the Pi is still a decent value—and you don't need a more expensive Pi 5 to run Frigate well.

I have been exploring [ways to optimize Frigate's performance on the Compute Module 4 and other Pi models](https://github.com/geerlingguy/pi-nvr/issues/8), and here are a few quick wins—which also help on faster computers, but may not be _as_ necessary:

  - Don't use the camera's main stream for the `detect` role; you can use a 480p substream (some cameras even output 360p), and it will still have enough resolution for the Pi to process.
  - Only use the full resolution stream (1080p or 4K) for the `record` role. It will be recorded in the background (if you choose), and any detected objects will save off clips using that raw recorded footage.
  - Configure Frigate's storage to use NVMe or disk-based storage, don't have it write to eMMC memory or any kind of microSD card. Ideally, get NVR-ready hard drives, like WD's Purple / Surveillance line. They're designed for constant writes and some reads, and should work a little better for the purpose.

I'm still trying to figure out how to speed up operations like exporting footage either as timelapses or the realtime clips. Some things are limited by the I/O of the Pi itself, and would benefit from running on a Pi 5 vs a Pi 4 or CM4.

Watch the full video with my build process and a bit more on Frigate setup on the Raspberry Pi here:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/7wkVGcdI2vk" frameborder='0' allowfullscreen></iframe></div>
</div>
