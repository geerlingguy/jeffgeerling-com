---
nid: 3157
title: "Fix for Nvidia Jetson Nano 2GB Developer Kit stuck in boot loop"
slug: "fix-nvidia-jetson-nano-2gb-developer-kit-stuck-boot-loop"
date: 2021-12-13T20:45:50+00:00
drupal:
  nid: 3157
  path: /blog/2021/fix-nvidia-jetson-nano-2gb-developer-kit-stuck-boot-loop
  body_format: markdown
  redirects: []
tags:
  - boot
  - etcher
  - jetson
  - nano
  - nvidia
  - sbc
---

I recently got an [Nvidia Jetson Nano 2GB Developer Kit](TODO), and I read through and followed the [Developer Kit Getting Started Guide](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#intro) straight from Nvidia's website.

I downloaded the 7 GB(!) microSD card from their website, and flashed it to a 128 GB microSD card using Balena Etcher.

Then I popped the microSD card into my dev kit board, plugged in HDMI and a USB-C 3A power supply, and waited... I kept seeing a giant NVIDIA logo on my display, and after about 20 seconds, it would seemingly reboot to black screen, then the logo... and repeat forever.

Searching around the Nvidia forums, I eventually found this issue: [Nano 2GB boot looping](https://forums.developer.nvidia.com/t/nano-2gb-boot-looping/157972/5), and finally found the problem: apparently the default image download is _only for the 4GB Nano model_.

I had used Google/DDG to find the getting started guide, and it linked to the 4GB kit guide—there's an [entirely different URL for the 2GB kit](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-2gb-devkit)!

So I went through that guide, downloaded _its_ image, and flashed _it_ to the microSD card. Now the Nano is booting like a champ.

Why do they have specific images for each RAM size? No clue.
