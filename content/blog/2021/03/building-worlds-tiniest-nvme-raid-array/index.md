---
nid: 3083
title: "Building the World's Tiniest NVMe RAID Array"
slug: "building-worlds-tiniest-nvme-raid-array"
date: 2021-03-23T17:41:21+00:00
drupal:
  nid: 3083
  path: /blog/2021/building-worlds-tiniest-nvme-raid-array
  body_format: markdown
  redirects: []
tags:
  - nvme
  - raid
  - raspberry pi
  - ssd
  - video
  - youtube
---

Just posting to the blog for reference; I posted this video on YouTube recently, in which I built (what I believe to be) the world's tiniest NVMe SSD RAID array, using the Raspberry Pi Compute Module 4 and three diminutive [WD SN520 NVMe drives](https://amzn.to/2MrmvA7) (which are M.2 2230 size, which makes them each about the size of a quarter):

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/AoNxDe1a-X8" frameborder='0' allowfullscreen></iframe></div>
</div>

I ran some benchmarks in RAID 5 and RAID 0, as well as one drive by itself, and found one surprising thing: the Pi's overall IO bandwidth is already saturated by just one drive, so putting NVMe disks in RAID doesn't really help with performance, like it does with slower spinning hard drives.

Also, with RAID 5, the parity calculations and bus throughput on the Pi make it a lot slower than you may expect, if you're coming from a much faster PC with more PCI Express bandwidth and a much faster CPU.

Watch the video above for more, and if you like what you see, make sure you [subscribe to my YouTube channel](https://www.youtube.com/c/JeffGeerling)!
