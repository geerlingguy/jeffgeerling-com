---
date: '2026-02-18T14:50:00-06:00'
tags: ['hailo', 'ai', 'hat', 'raspberry pi', 'frigate', 'nvr', 'dvr', 'docker', 'pcie']
title: 'Frigate with Hailo for object detection on a Raspberry Pi'
slug: 'frigate-with-hailo-for-object-detection-on-a-raspberry-pi'
---
I run [Frigate](https://frigate.video) to record security cameras and detect people, cars, and animals when in view. My [current Frigate server](/blog/2024/building-pi-frigate-nvr-axzezs-interceptor-1u-case/) runs on a Raspberry Pi CM4 and a [Coral TPU](https://amzn.to/4aWdOpQ) plugged in via USB.

Raspberry Pi offers [multiple AI HAT+'s](https://www.raspberrypi.com/products/ai-hat/) for the Raspberry Pi 5 with built-in Hailo-8 or Hailo-8L AI coprocessors, and they're useful for low-power inference (like for image object detection) on the Pi. Hailo coprocessors can be used with other SBCs and computers too, if you buy an [M.2 version](https://www.waveshare.com/hailo-8.htm).

{{< figure
  src="./exaviz-cruiser-mini-rack-nas-nvr-build.jpg"
  alt="Exaviz Cruiser 10 inch mini rack NVR NAS build"
  width="700"
  height="auto"
  class="insert-image"
>}}

Frigate offers Hailo support, but getting it working on my new build (pictured above—full writeup coming soon) threw me for a loop, so I'm documenting the process for _my_ build here, for my own future reference.

Assuming you have a fresh Pi OS install on a Pi 5 or CM5, and you have the Hailo module connected via PCIe (either a HAT+ module, or via an M.2 slot), do the following:

  1. Follow [Frigate's guide to install the Hailo-8 driver from source](https://docs.frigate.video/frigate/installation/#hailo-8).
  1. Follow [Frigate's guide for setting up Hailo as an object detector](https://docs.frigate.video/configuration/object_detectors/#hailo-8) in your Frigate `config.yml` (note: I use my open source [Pi NVR project](https://github.com/geerlingguy/pi-nvr)).
  1. Start Frigate.

If you see a message like:

```
WARNING : CPU detectors are not recommended and should only be used for testing or for trial purposes.
```

Then your detector configuration is likely wrong. Check back through your `model` and `detectors` config in `frigate.yml` and try again :)

## PCIe `force_desc_page_size` issue

Outside of configuration issues that took a few tries to fix, I ran into this error message when running `docker logs frigate`:

```
[HailoRT] [error] CHECK failed - max_desc_page_size given 16384 is bigger than hw max desc page size 4096
...
RuntimeError: HailoRT inference thread has stopped, restart required.
```

That error led me to [this forum thread](https://community.hailo.ai/t/pcie-max-desc-page-size-issue/136/15), which suggested a fix:

Create a file `/etc/modprobe.d/hailo_pci.conf` (e.g. with `sudo nano`), with the following contents:

```
options hailo_pci force_desc_page_size=4096
```

Then either reboot the Pi, or run the following commands to unload, then reload, the hailo driver:

```
sudo modprobe -r hailo_pci 
sudo modprobe hailo_pci 
```

The Frigate container logs should report the Hailo detector is now in use:

```
[2026-02-18 14:14:35] detector.hailo  INFO: Starting detection process: 621
```

And now, the system dashboard is showing `hailo` as running at around 12ms inference speed, with very low CPU usage overall (this was testing with two cameras):

{{< figure
  src="./hailo-frigate-detector-inference-cpu-usage.png"
  alt="Hailo 8 object detection on Raspberry Pi CM5 with Frigate"
  width="700"
  height="auto"
  class="insert-image"
>}}

The nice thing is, this works on the cheaper Hailo-8L that you can find in the $70 AI HAT+ (the 'base model'), which is often much cheaper than the now-ancient [Google Coral TPU](https://amzn.to/4aWdOpQ)—at least the USB version that's more broadly compatible.

I'm still at a loss as to why Google abandoned Coral after one generation. It seems like they could've dominated the 'edge TPU' market, but they kinda gave it up after hitting 4 TOPS.
