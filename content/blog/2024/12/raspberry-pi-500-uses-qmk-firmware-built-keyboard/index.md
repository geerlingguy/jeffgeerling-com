---
nid: 3427
title: "Raspberry Pi 500 uses QMK Firmware for built-in keyboard"
slug: "raspberry-pi-500-uses-qmk-firmware-built-keyboard"
date: 2024-12-10T15:52:00+00:00
drupal:
  nid: 3427
  path: /blog/2024/raspberry-pi-500-uses-qmk-firmware-built-keyboard
  body_format: markdown
  redirects: []
tags:
  - keyboard
  - open source
  - pi 500
  - qmk
  - raspberry pi
  - rp2040
---

I mentioned in my [Pi 500 review](/blog/2024/pi-500-much-faster-lacks-m2) Raspberry Pi is dogfooding their own microcontroller in the new Pi 500. An RP2040 sits next to the keyboard ribbon cable connector, and interfaces it through a USB port directly into the RP1 chip:

{{< figure src="./pi-500-rp2040-keyboard-qmk.jpg" alt="Raspberry Pi 500 PCB with RP2040 for keyboard input" width="700" height="auto" class="insert-image" >}}

In good news for keyboarding enthusiasts, the RP2040 seems to be flashed with the open-source [QMK ('Quantum Mechanical Keyboard') Firmware](https://github.com/raspberrypi/QMK). Thanks to a reader, 'M', who figured that out!

{{< figure src="./system76-launch-keyboard.jpg" alt="System76 Launch keyboard with RP2040 inside" width="700" height="auto" class="insert-image" >}}

A fork of QMK is also used by System76 to power their ['Launch' keyboard](https://support.system76.com/articles/launch-keyboard/) (pictured above), and it allows you to do things like remap your keyboard however you like—for me, turning the useless Caps Lock key into Escape :)

<s>Right now I'm not 100% sure the firmware can be flashed to the RP2040 directly through Pi OS, but I imagine there's a way to do it, judging by [this commit](https://github.com/raspberrypi/QMK/pull/3/files).</s>

<s>I've filed an issue [requesting instructions for re-flashing the RP2040](https://github.com/raspberrypi/QMK/issues/4), since they don't seem to exist in Raspberry Pi's repo, or in the official [Pi 500 Documentation](https://www.raspberrypi.com/documentation/computers/).</s>

There's a [readme with instructions for flashing the Pi 500 membrane keyboard](https://github.com/raspberrypi/QMK/blob/pi500/keyboards/rpi/pi500/README.md#programming-the-keyboard) within the repo!

The next question, since it seems obvious the Pi 500's PCB is intended for something more—could we see an enthusiast-grade mechanical keyboard version of the Pi 500, with all the bells and whistles? I've already been asking System76 if they might consider designing bottom plate for the Launch keyboard that adapts the Pi 500...
