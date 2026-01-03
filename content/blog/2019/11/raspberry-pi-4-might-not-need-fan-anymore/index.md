---
nid: 2948
title: "The Raspberry Pi 4 might not need a fan anymore"
slug: "raspberry-pi-4-might-not-need-fan-anymore"
date: 2019-11-14T14:54:42+00:00
drupal:
  nid: 2948
  path: /blog/2019/raspberry-pi-4-might-not-need-fan-anymore
  body_format: markdown
  redirects: []
tags:
  - cooling
  - fan
  - monitoring
  - raspberry pi
  - review
  - reviews
  - seeed
  - temperature
---

> **tl;dr**: After the fall 2019 firmware/bootloader update, the Raspberry Pi 4 can run without throttling inside a case—but only just barely. On the other extreme, the ICE Tower by 52Pi lives up to its name.

<p style="text-align: center;">{{< figure src="./raspberry-pi-4-cooling-options-cases-fans-ice-tower.jpeg" alt="Raspberry Pi 4 cooling options including ICE tower cooling fan and a case mod fan" width="650" height="421" class="insert-image" >}}<br>
<em>Three options for keeping the Pi 4 cozy: unmodified Pi 4 case, modded case with fan, and the ICE Tower.</em></p>

A few months ago, I was excited to work on upgrading some of my Raspberry Pi projects to the Raspberry Pi 4; but I found that for the first time, it was [necessary to use a fan to actively cool the Pi if used in a case](/blog/2019/raspberry-pi-4-needs-fan-heres-why-and-how-you-can-add-one).

Two recent developments prompted me to re-test the Raspberry Pi 4's thermal properties:

  1. Seeed Studio/52Pi sent me one of their [ICE Tower CPU Cooling Fans](https://www.seeedstudio.com/ICE-Tower-CPU-Cooling-Fan-for-Raspberry-pi-Support-Pi-4-p-4097.html), and asked me to review it.
  2. The Raspberry Pi foundation [released a bootloader and firmware update](https://www.geeks3d.com/20191101/raspberry-pi-4-new-firmware-reduces-power-consumption-and-boards-temperatures/) which reduces the temperature of the Pi by enabling power-saving functionality of the Pi's USB 3.0 chipset.

In the blog post I linked to earlier, I came to the conclusion that you _must_ use active cooling for the Raspberry Pi if you run it inside the official Pi case. I wanted to see if, after the firmware update, this was still true.

I also wanted to see what kind of affect the ICE Tower's massive heat sink would have on the Pi's thermal capabilities under load—with and without the active cooling provided by the sleek icy-blue fan it comes with!

## How I tested

I _hate_ when you read an article about benchmark results, and you never see the methodology. That's not science! I wanted to make a completely repeatable and automated process to test and graph the temperature results, using `stress-ng` to put load on the Pi, and the onboard frequency, throttling, and temperature monitoring, to put the Pi through its paces.

Therefore, I wrote [this Raspberry Pi CPU temperature and throttling test script](https://gist.github.com/geerlingguy/91d4736afe9321cbfc1062165188dda4), which does the following:

  1. Begins logging temperature, throttling, and CPU frequency data every 5 seconds.
  2. Waits 2 minutes to establish a baseline reading.
  3. Runs `stress-ng` on all 4 Pi CPUs for 5 minutes.
  4. Waits another 2 minutes to see how the CPU temperature backs off after the stress test.

It's also important to list the details of my test environment, and the actual hardware used:

  - The test environment was steady 72°F (22°C), with gentle airflow provided by a fan running on low in the opposite corner of the room.
  - I used the exact same Raspberry Pi 4 model B with 4 GB of RAM for every test, with the same microSD card.
  - The Pi was plugged into an official Raspberry Pi foundation USB-C AC adaptor.
  - The Pi was run headless, only connected to a wired network for control via SSH (WiFi was inactive).

### Upgrading the Raspberry Pi's Bootloader and Firmware

I first ran all the tests without the updated firmware, using the latest version of Raspbian Lite from the Raspberry Pi foundation's website, then I updated the firmware following the guide in [this article from geeks3d.com](https://www.geeks3d.com/20191101/raspberry-pi-4-new-firmware-reduces-power-consumption-and-boards-temperatures/).

## Results

| Cooling Option | Min Temp (°C) | Max temp (°C) | CPU throttled? |
| ---- | ---- | ---- | ---- |
| Bare Pi | 50 | 77 | NO |
| Pi in official case (no fan) | 51 | 82 | YES |
| Pi in official case (with fan) | 39 | 61 | NO |
| Bare Pi with ICE tower, fan off) | 31 | 51 | NO |
| Bare Pi with ICE tower, fan on) | 29 | 39 | NO |
| Bare Pi — after fw update | 38 | 69 | NO |
| Pi in official case — after fw update | 43 | 76 | NO |

There are two result sets that stand out the most to me.

### Firmware upgrade makes the Pi case usable

If you run the Pi 4 in the official Raspberry Pi Foundation's case, unmodified, the CPU would start throttling within a few minutes of any serious activity. This was what prompted my original blog post on the subject. But after the firmware update, the Pi 4 in an unmodified case might not be so bad. I still don't like running CPUs right up to their thermal limits all the time... but I'd be much more comfortable doing so now that the USB controller is not generating as much heat!

Here's the graph comparing the Pi in the case before (blue line) and after (green line) the firmware upgrade:

{{< figure src="./pi-in-case-before-after.png" alt="Raspberry Pi 4 in case - comparison of temperature under load before and after firmware update" width="650" height="349" class="insert-image" >}}

The delta is between 6-8°C, which is quite significant when you're talking about the tiny Raspberry Pi!

### Active cooling and massive heatsinks make the Pi very happy

The second standout result is a graph comparing all the different cooling options I tested _pre-firmware-update_:

{{< figure src="./pi-cpu-temps-all-graphs-pre-fw-update.png" alt="Raspberry Pi 4 comparison of different cooling methods" width="650" height="349" class="insert-image" >}}

Three major things to note here:

  1. Without any cooling assistance, the Pi can get uncomfortably close to the CPU's temperature throttling limit (~80°C), either bare or in a case.
  2. Active cooling (just a fan blowing on the Pi, no heatsink) is an order of magnitude better than nothing.
  3. The ICE Tower is aptly named.

I mean, look at the bottom graph; if you need to run the Pi wild, there is no better active cooling setup I can think of, short of [liquid immersion cooling](https://en.wikipedia.org/wiki/Server_immersion_cooling)! The temperature _under load_ is lower than the idle temperature of a bare Pi, or even a bare Pi with a fan blowing over it!

## A brief review of the ICE Tower Cooling Fan

Now, you might look at the above graph and immediately jump over to the Seeed Studio shop to [buy one](https://www.seeedstudio.com/ICE-Tower-CPU-Cooling-Fan-for-Raspberry-pi-Support-Pi-4-p-4097.html)... but you need to take into account the massive size of this cooler. It's a specialty tool, one that few really _need_. But it does a darn good job cooling the Pi.

The biggest issue is figuring out how to encase a Pi with this massive heat sink. Here's my hacked-together solution, using a bunch of standoffs to make some open-air frankencase:

{{< figure src="./raspberry-pi-4-with-ice-tower-in-hacky-case.jpeg" alt="Raspberry Pi 4 inside hacky frankencase with the ICE Tower cooling fan" width="650" height="578" class="insert-image" >}}

The fan came in a little box with all the screws needed to mount it to a bare Pi 4, as well as a little thermal pad to place between the copper pipe and the Pi's CPU case. It all fit together perfectly, but after you put it on, you have to figure out the best way to get the whole rig into some sort of case.

## Summary

In the end, I learned two things:

  1. The firmware update makes it so you don't need a fan to use a Raspberry Pi 4 in a typical case anymore. This is great!
  2. The ICE Tower Cooling Fan lives up to its name; it cools the Pi 4 extremely well, but it is massive and requires some thought as to how to encase the Pi if you're considering using it in the real world.
