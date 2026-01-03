---
nid: 3423
title: "Home Assistant Yellow - instant 2x IoT speedup with CM5"
slug: "home-assistant-yellow-instant-2x-iot-speedup-cm5"
date: 2024-11-27T18:32:08+00:00
drupal:
  nid: 3423
  path: /blog/2024/home-assistant-yellow-instant-2x-iot-speedup-cm5
  body_format: markdown
  redirects:
    - /blog/2024/home-assistant-yellow-instant-2x-speedup-cm5
aliases:
  - /blog/2024/home-assistant-yellow-instant-2x-speedup-cm5
tags:
  - cm5
  - compute module
  - home assistant
  - iot
  - open source
  - raspberry pi
  - smart home
  - yellow
---

In a win for modular, private, local IoT, I just upgraded my Home Assistant Yellow from a Raspberry Pi Compute Module 4 to a Compute Module 5 this morning, and got an instant 2x speed boost.

{{< figure src="./pi-cm5-ha-upgrade.jpg" alt="Home Assistant Yellow upgraded to Pi CM5" width="700" height="auto" class="insert-image" >}}

I first posted about the Yellow [in 2022](/blog/2022/home-assistant-yellow-pi-powered-local-automation), and walked through my smart-but-private HA Yellow setup in my Studio [in a video last year](https://www.youtube.com/watch?v=vTwyInX4KyM).

Because I was running an eMMC CM4 in the Yellow before, I ran a full backup (and downloaded it), yanked the CM4, flashed HAOS to a new NVMe SSD, and plugged that and the CM5 into my Yellow. After running a Restore (it's a handy option right on the first page that appears when you access `homeassistant.local`), I was up and running like there was no difference at all—just everything was a little more snappy.

{{< figure src="./home-assistant-yellow-screw-close-cm5.jpg" alt="Home Assistant Yellow screw on CM5" width="700" height="auto" class="insert-image" >}}

The only caveat is the wide screw heads on the CM5 hold-down screws included with the Yellow are a bit close to the PMIC power circuits (especially a tiny capacitor), so I decided to switch screw heads to one that is a hair (like 0.02mm) smaller in diameter, just so it wasn't touching the edge of the cap. The screws aren't even necessary in any normal environment, as the heatsink uses pressure to hold down the CM5 as well.

As noted in [Home Assistant's blog post announcing CM5 compatibility](https://www.home-assistant.io/blog/2024/11/27/home-assistant-yellow-gets-cm5-support/), the CM5 is probably overkill for _most_ installations.

But for me, I often try out weird automations, or tinker with new features like [locally/private voice automations and text-to-speech](https://www.home-assistant.io/voice_control/), and those benefit _dramatically_ from the speedups. Like in a quick test, inference times on the device with a tiny Pi-optimized model went from 2.8 to 1.3 seconds.

When you're trying to converse with a voice assistant, that kind of latency reduction is huge!

I mentioned in my post early this morning, [Raspberry Pi CM5 is 2-3x faster, drop-in upgrade (mostly)](/blog/2024/raspberry-pi-cm5-2-3x-faster-drop-upgrade-mostly), and that seems to hold true here.

I will continue testing other devices, and maybe I'll figure out a way to indicate CM4/CM5 compatibility on my [Pi PCIe site](https://pipci.jeffgeerling.com/boards_cm).
