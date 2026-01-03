---
nid: 3382
title: "Testing Raspberry Pi's AI Kit - 13 TOPS for $70"
slug: "testing-raspberry-pis-ai-kit-13-tops-70"
date: 2024-06-04T07:06:56+00:00
drupal:
  nid: 3382
  path: /blog/2024/testing-raspberry-pis-ai-kit-13-tops-70
  body_format: markdown
  redirects: []
tags:
  - ai
  - copilot
  - coral
  - hat
  - machine learning
  - npu
  - raspberry pi
  - video
  - youtube
---

Raspberry Pi today launched the [AI Kit](https://www.raspberrypi.com/news/raspberry-pi-ai-kit-available-now-at-70/), a $70 addon which straps a Hailo-8L on top of a Raspberry Pi 5, using the recently-launched M.2 HAT (the Hailo-8L is of the M.2 M-key variety, and comes preinstalled).

{{< figure src="./pi-ai-kit.jpeg" alt="Raspberry Pi AI Kit" width="700" height="auto" class="insert-image" >}}

The Hailo-8L's claim to fame is 3-4 TOPS/W efficiency, which, along with the Pi's 3-4W idle power consumption, puts it alongside Nvidia's edge devices like the Jetson Orin in terms of TOPS/$ and TOPS/W for price and efficiency.

Google's [Coral TPU](https://coral.ai) has been a popular choice for a machine learning/AI accelerator for the Pi for years now, but Google seems to have left the project on life support, after the Coral hardware was scalped for a couple years about as badly as the Raspberry Pi itself!

Pineboards offers a $50 [Coral Edge TPU bundle](https://pineboards.io/products/hat-mpcie-coral-edge-tpu-bundle-for-raspberry-pi-5) as well as a $100 [Dual Edge TPU bundle](https://pineboards.io/products/hat-ai-dual-edge-coral-tpu-bundle-for-raspberry-pi-5) offering 4 and 8 TOPS, respectively. But the Pi AI Kit undercuts those offerings both on price and power efficiency.

The Coral can be had (sometimes) for as little as $25 as a standalone PCIe device, but at 2 TOPS/W, the speed and efficiency of its 6-year-old chip design is a little behind the times. It's still [quite useful for projects like a Frigate NVR](/blog/2024/building-pi-frigate-nvr-axzezs-interceptor-1u-case), but it's far behind even the built-in NPUs on modern chips like the Rockchip RK3588.

I tested the Pi AI Kit in the video embedded below:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/HgIMJbN0DS0" frameborder='0' allowfullscreen></iframe></div>
</div>

The video has a more detailed look at the performance of the AI Kit, but I'll run through some top-level things here.

Raspberry Pi seems to be marketing the AI Kit as a companion to their extensive line of Pi Cameras (they have a _ton_ now, targeted at a variety of use cases). Their `picamera2` library (still in beta) already has some [TensorFlow examples for the AI Kit](https://github.com/raspberrypi/picamera2/tree/main/examples/tensorflow), and `rpicam-apps` has a number of [built-in Hailo AI post-processing stages](https://github.com/raspberrypi/rpicam-apps/tree/main/post_processing_stages/hailo).

I tested a number of them, like YOLOv5 object detection:

{{< figure src="./pi-ai-kit-object-detection_0.jpeg" alt="Raspberry Pi AI Kit Object Detection" width="700" height="auto" class="insert-image" >}}

And YOLOv8 pose estimation:

{{< figure src="./pi-ai-kit-pose-estimation.jpeg" alt="Raspberry Pi AI Kit Pose Estimation" width="700" height="auto" class="insert-image" >}}

There were no hiccups, and I ran through a few other examples in the video, if you want to see how they worked using Hailo's default models (see their [model zoo](https://github.com/hailo-ai/hailo_model_zoo)).

I also ran through a bunch of my own pre-recorded footage at 480p and 720p and it had no issues whatsoever. I did try feeding it a 4K H.264 video file and it kinda didn't like that. It worked, but was a bit sluggish :)

## Going for 51 TOPS

Microsoft recently announced the Copilot+ PC standard of at least 40 TOPS of neural compute power. Qualcomm's Snapdragon X has 45 TOPS, Apple's M4 has 38, Intel's Lunar Lake has 48, and AMD's AI 300 series has 50.

So naturally, I wanted to go further—on a Raspberry Pi.

{{< figure src="./pi-ai-multiple-coral-hailo-tpu-npu-abomination.jpeg" alt="Raspberry Pi 5 multiple TPU NPU in a pile - an unholy mess" width="700" height="auto" class="insert-image" >}}

This configuration is _completely unsupported_ by any of the vendors involved—I used a Raspberry Pi 5, two Hailo NPUs (the Hailo-8L with 13 TOPS and Hailo-8 with 26 TOPS), a Coral Dual Edge TPU (8 TOPS), and a Coral Edge TPU (4 TOPS), totaling 51 TOPS.

And the Pi could _see_ everything in this unholy mess on my desk... I just couldn't get the chips to completely initialize. Likely a power issue, as `dmesg` showed the drivers dying off after PCIe device enumeration, while the driver was loading.

I didn't have time (due to the tight deadline publishing this post) to go much further, but I suspect I'd have more luck using a single PCIe switch instead of chaining together two of Pineboards' [HatBrick! Commander](https://pineboards.io/products/hatbrick-commander-2-ports-gen2-for-raspberry-pi-5) boards.

That, and I could supply external power so I don't tempt fate drawing more than 5W through the Pi 5's PCIe FPC header!

I may make another attempt at _utilizing_ 51 TOPS on a Pi 5 with this board:

{{< figure src="./pi-ai-alftel-12-m2-carrier-pcie.jpeg" alt="Alftel 12x PCIe expansion card with multiple TPUs and NPUs" width="700" height="auto" class="insert-image" >}}

It's a [12x PCIe expansion board from Alftel](https://pipci.jeffgeerling.com/cards_m2/alftel-12x-pcie-m2-carrier-board.html), and I've used it in the past to string together a bunch of NVMe SSDs on the Pi CM4—enough to drive _that_ Pi to its breaking point, in terms of simultaneous active PCIe devices :)
