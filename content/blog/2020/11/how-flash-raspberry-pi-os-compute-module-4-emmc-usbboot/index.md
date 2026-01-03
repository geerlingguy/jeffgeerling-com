---
nid: 3050
title: "How to flash Raspberry Pi OS onto the Compute Module 4 eMMC with usbboot"
slug: "how-flash-raspberry-pi-os-compute-module-4-emmc-usbboot"
date: 2020-11-03T21:10:27+00:00
drupal:
  nid: 3050
  path: /blog/2020/how-flash-raspberry-pi-os-compute-module-4-emmc-usbboot
  body_format: markdown
  redirects:
    - /blog/2020/how-flash-raspberry-pi-os-compute-module-4-emmc
aliases:
  - /blog/2020/how-flash-raspberry-pi-os-compute-module-4-emmc
tags:
  - cm4
  - compute module
  - emmc
  - flash
  - raspberry pi
  - usb
---

The Raspberry Pi Compute Module 4 comes in two main flavors: one with built-in eMMC storage, and one without it. If you opt for a Compute Module 4 with built-in eMMC storage, and you want to write a new OS image to the Compute Module, or manually edit files on the boot volume, you can do that just the same as you would a microSD card—but you need to first make the eMMC storage mountable on another computer.

This blog post shows how to mount the eMMC storage on another computer (in my case a Mac, but the process is very similar on Linux), and then how to flash a new OS image to it.

## Video Instructions

In addition to the tutorial below, I published a video version of this post covering installation and usage of `rpiboot` for flashing the eMMC on Windows, Ubuntu, Raspberry Pi OS, or macOS:

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/jp_mF1RknU4" frameborder='0' allowfullscreen></iframe></div>

## Preparing the IO Board for mounting

Before you can set the eMMC storage into 'USB mass storage' mode, you have to put a jumper over the first set of pins on the 'J2' jumper—the jumper labeled "Fit jumper to disable eMMC boot":

{{< figure src="./j2-emmc-jumper.jpeg" alt="J2 jumper for fit to disable eMMC Boot Raspberry Pi Compute Module 4 IO Board" width="600" height="450" class="insert-image" >}}

> Don't have a jumper? I bought a [huge pack of jumpers](https://www.amazon.com/gp/product/B07VJKCHVN/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=6f77236cdbb9eebfaf77e8c8989fa3f7&language=en_US) years ago, and grabbed one from that bag. You could also pop any kind of conductor between the two pins, like a female-to-female jumper.

Then, plug a USB cable from your computer (in my case, my Mac—but it could be a Windows or Linux computer too) into the 'USB Slave' micro USB port on the IO Board, and plug in power:

{{< figure src="./usb-slave-and-power-io-board.jpeg" alt="Plug in USB Slave and power on Raspberry Pi Compute Module 4 IO Board for eMMC flashing" width="600" height="450" class="insert-image" >}}

The board will power on, and you'll see the red 'D1' LED turn on, but the Compute Module won't boot. The eMMC module should now be ready for the next step.

## Using usbboot to mount the eMMC storage

The next step is to download the Raspberry Pi usbboot repository, install a required USB library on your computer, and build the `rpiboot` executable, which you'll use to mount the storage on your computer. I did all of this in the Terminal application on my Mac.

First, make sure you have the `libusb` library installed:

  - On my Mac, I have [Homebrew](https://brew.sh) installed, so I ran: `brew install pkgconfig libusb`
  - On Linux (e.g. another Raspberry Pi), run: `sudo apt install libusb-1.0-0-dev`

Second, clone the usbboot repository to your computer:

```
$ git clone --depth=1 https://github.com/raspberrypi/usbboot
```

Third, `cd` into the `usbboot` directory and build `rpiboot`:

```
$ cd usbboot
$ make
```

Now there should be an `rpiboot` executable in the directory. To mount the eMMC storage, run:

```
$ sudo ./rpiboot
```

And a few seconds later, after it finishes doing its work, you should see the `boot` volume mounted on your Mac (or on whatever Linux computer you're using). You might also notice the D2 LED lighting up; that means there is disk read/write activity on the eMMC.

## Flashing Raspberry Pi OS onto the eMMC

At this point, the eMMC storage behaves just like a microSD card or USB drive that you plugged into your computer. Use an application like the Raspberry Pi Imager to flash Raspberry Pi OS (or any OS of your choosing) to the eMMC:

{{< figure src="./select-sd-card-raspberry-pi-imager.png" alt="Raspberry Pi Imager choose eMMC storage to flash" width="680" height="442" class="insert-image" >}}

{{< figure src="./raspberry-pi-imager-writing.png" alt="Raspberry Pi Imager writing disk image to Raspberry Pi Compute Module 4 eMMC" width="680" height="442" class="insert-image" >}}

At this point, if you don't need to make any modifications to the contents of the `boot` volume, you could disconnect the IO board (eject the `boot` volume if it's still mounted!) USB slave port connection, disconnect power, then remove the eMMC Boot disable jumper on J2.

Then plug power back in, and the CM4 should now boot off it's (freshly-flashed) eMMC storage!

If you ever need to mount the `boot` volume or re-flash the eMMC storage, just run `sudo ./rpiboot` again.
