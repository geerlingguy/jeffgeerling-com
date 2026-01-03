---
nid: 3458
title: "Raspberry Pi cluster spotted inside $6k audio processor"
slug: "raspberry-pi-cluster-spotted-inside-6k-audio-processor"
date: 2025-04-10T03:11:15+00:00
drupal:
  nid: 3458
  path: /blog/2025/raspberry-pi-cluster-spotted-inside-6k-audio-processor
  body_format: markdown
  redirects:
    - /blog/2025/raspberry-pi-cluster-spotted-inside-9k-audio-processor
aliases:
  - /blog/2025/raspberry-pi-cluster-spotted-inside-9k-audio-processor
tags:
  - audio
  - broadcast
  - cluster
  - cm4
  - cm5
  - compute module
  - nab
  - optimod
  - orban
  - raspberry pi
---

People often ask me whether Pi clusters are useful besides just tinkering. I've [built my fair share](https://www.jeffgeerling.com/tags/cluster), including my most recent ['Lamp Rack' Kubernetes-in-a-Lamp cluster](https://www.jeffgeerling.com/blog/2025/running-lamp-stack-lamp-rack).

Well... I have a definitive answer: the [Orban Optimod 5000-series](https://www.orban.com/overview-optimod-5750-audio-processor) audio processors:

{{< figure src="./orban-optimod-5750-cm4-pi.jpg" alt="Orban Optimod 5750 Pi CM4 cluster inside" width="700" height="394" class="insert-image" >}}

These rackmount units each include a 3-node Raspberry Pi cluster, and they cost between $6,000-15,000! I found this specimen at the Orban booth at NAB 2025, and they sell a lot of these to broadcasters around the world.

_From what I understand_, one Pi is used for remote control, web UI, firmware updates, and local display. Another is used for multi-stream audio processing (independent of the 'head' Pi, so it can keep going even if there's a problem on the display/remote access side), and a third Pi, which I believe is optional, used for watermarking audio streams for data like [Luminate/SoundScan](https://www.isrc.com/FAQ-Soundscan.php) ratings data.

Can you set up a box like this another way? Certainly.

Can you do that with minimal power consumption, leaning on vendor support for custom hardened and _recent_ Linux images via [rpi-image-gen](https://github.com/raspberrypi/rpi-image-gen) for 10+ years of support? It becomes harder with most other vendors' modules. Relying on the Pi CM4/CM5 certainly saves time implementing an entire SoC / custom SoM design.

This is one of the more public uses of more than one CM inside a media box—there were a _large_ number of expensive devices on the show floor with Pis buried inside. It's one of the easiest ways to take a company's vast experience with audio/video/RF processing and ASICs/FPGAs... and slapping a well-supported Linux and remote control option onto decades-old architectures.
