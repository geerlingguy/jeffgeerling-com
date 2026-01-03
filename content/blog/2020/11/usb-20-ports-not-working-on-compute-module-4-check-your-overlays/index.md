---
nid: 3054
title: "USB 2.0 ports not working on the Compute Module 4? Check your overlays!"
slug: "usb-20-ports-not-working-on-compute-module-4-check-your-overlays"
date: 2020-11-16T16:16:25+00:00
drupal:
  nid: 3054
  path: /blog/2020/usb-20-ports-not-working-on-compute-module-4-check-your-overlays
  body_format: markdown
  redirects: []
tags:
  - boot
  - compute module
  - config
  - raspberry pi
  - usb
---

Out of the box, to conserve power, the new Raspberry Pi Compute Module 4 doesn't enable its built-in USB 2.0 ports.

{{< figure src="./cm4-io-board-usb2-ports-disabled.jpg" alt="Compute Module 4 IO Board USB 2.0 ports are disabled by default" width="600" height="369" class="insert-image" >}}

You might notice that if you plug something into one of the USB 2 ports on the IO Board and don't see it using `lsusb -t`. In fact, you see nothing, by default, if you run `lsusb -t`.

To enable the USB 2.0 ports on the Compute Module 4, you need to edit the boot config file (`/boot/config.txt`) and add:

```
dtoverlay=dwc2,dr_mode=host
```

Then reboot the Pi. Now you should be able to use the built-in USB 2.0 ports!
