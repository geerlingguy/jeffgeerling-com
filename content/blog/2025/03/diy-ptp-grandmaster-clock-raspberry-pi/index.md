---
nid: 3455
title: "DIY PTP Grandmaster Clock with a Raspberry Pi"
slug: "diy-ptp-grandmaster-clock-raspberry-pi"
date: 2025-03-28T14:01:30+00:00
drupal:
  nid: 3455
  path: /blog/2025/diy-ptp-grandmaster-clock-raspberry-pi
  body_format: markdown
  redirects:
    - /blog/2025/diy-ptp-grandmaster-clock-server-raspberry-pi
aliases:
  - /blog/2025/diy-ptp-grandmaster-clock-server-raspberry-pi
tags:
  - clock
  - hat
  - ptp
  - raspberry pi
  - time
  - video
  - youtube
---

> **tl;dr**: I set up an open source [Time Pi project](https://github.com/geerlingguy/time-pi) to build a stratum 1 PTP and NTP timeserver using a Raspberry Pi.

Time is important to modern society, and most of us have a clock on our wrist that's more accurate than at any time in human history. But _highly precise_ time is important in many industries, especially robotics, finance, and media production. And with tech like VR working its way into homes, precise time may become more important _there_, too.

The timing industry has many solutions for 'grandmaster' clocks, which take in highly accurate time from GPS, GNSS, or other atomic-clock-backed time sources, and distribute it to local networks with _extreme_ precision—down to the nanosecond range—using PTP.

{{< figure src="./time-pi-raspberry-pi-clock-masterclock-mini-rack.jpeg" alt="Time Pi - Raspberry Pi Time Grandmaster Clock in mini rack with Masterclock NTP clock" width="700" height="394" class="insert-image" >}}

Historically, setting up a DIY PTP grandmaster clock server was a painful and expensive endeavor, pricing out most hobbyists. So I'm introducing a project that's been in the works for some time: [Time Pi](https://github.com/geerlingguy/time-pi), a stratum 1 PTP and NTP timeserver based on a Raspberry Pi 5.

In the picture above, it is installed inside a [LabStack module](https://github.com/JaredC01/LabStack) inside a 3U RackMate TT (an as-yet-unreleased version of DeskPi's mini racks—I'm working with them on ironing out the design). I have powered it using a PoE to USB-C power splitter, from my [GigaPlus 2.5 Gbps PoE+ switch](https://amzn.to/4jbsD9B).

## Video

I'm lucky to live in the same city as [Masterclock](https://www.masterclock.com), a timing solutions company that's been manufacturing time servers and clocks for most of my life.

I've been discussing my project with them for over a year, and they provided me two PoE-powered NTP clocks for the studio, and for my testing with the Time Pi (the analog/digital hybrid clock is pictured above, and a 1U rackmount clock is pictured below):

{{< figure src="./time-pi-1u-masterclock-rackmount-clock.jpeg" alt="Time Pi - 1U Masterclock rackmount clock" width="700" height="394" class="insert-image" >}}

Dr. Demetrios Matsakis, formerly the Chief Scientist for the US Naval Observatory (which helps coordinate the time in UTC!), is now Masterclock's Chief Scientist. He and John Clark (the CTO) were gracious enough to visit my studio and chat with me about _their_ new time server, the GMR6000, and about time and DIY solutions.

{{< figure src="./jeff-geerling-masterclock-demetrios-matsakis-studio.jpeg" alt="Dr. Demetrios Matsakis with Jeff Geerling in studio" width="700" height="500" class="insert-image" >}}

(Special thanks to [Dave Bour](https://www.superdogco.com) for providing the photo above.)

A video I published on my YouTube channel includes my conversations with them (and a lot more detail about the Time Pi). You can watch it below:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/zT71UvUxhjU" frameborder='0' allowfullscreen></iframe></div>
</div>

## Time Pi

Assuming you don't want to watch the full video, I'll also describe the hardware itself here—as it is built around the [TimeHAT from TimeAppliances](https://www.tindie.com/products/timeappliances/timehat-i226-nic-with-pps-inout-for-rpi5/).

The TimeHAT is a $200 HAT for the Pi 5 which includes an Intel i226 2.5 Gbps NIC with PTP hardware timestamping support. There are two SMA connectors for PPS in/out (configurable), an extra U.fl connector to another PPS port on the NIC, and an M.2 slot routed for a custom GPS module.

{{< figure src="./time-pi-alone.jpeg" alt="Time Pi TimeHAT with GPS Module in Mini Rack LabStack module" width="700" height="394" class="insert-image" >}}

The slot is a little interesting, it's described as an "OCP M.2 GNSS 2242 Slot", and it follows the [M2 Sync Module Form Factor](https://www.opencompute.org/documents/m-2-sync-module-ocp-base-specification-1-1-pdf) from the Open Compute Project. Right now I can only find one commercially-available option: [OCP M.2 Neo-M9N GNSS](https://www.tindie.com/products/timeappliances/ocp-m2-neo-m9n-gnss/), a $195 add-on with a timing-focused u-blox GPS module.

The HAT interfaces with the Pi 5 through both PCIe (for the Intel i226 NIC), and GPIO (for GPS communications and configuration).

I _have_ had some hardware issues with the i226 NIC, but it doesn't seem like those issues are related to either the TimeHAT _or_ the Pi, but rather, Intel's Linux drivers. It seems like both the i225 and i226 have various strange issues, and the main one I ran into is [it _won't work at 2.5 Gbps, but does at 1 Gbps_](https://github.com/geerlingguy/time-pi/issues/3).

On the software side, I configure everything (Chrony, NTP, and PTP) with Ansible. Raspberry Pi OS / Debian is the base OS, which makes configuring all the appropriate software easy. Linux has a pretty robust set of timing-related libraries and packages, especially for PTP.

I won't go through the whole setup process in this post—for that, visit the [time-pi repository](https://github.com/geerlingguy/time-pi).

## Conclusion

My first post and video is about the Time Pi hardware and comparing it to some commercial offerings. It's been running stably as an NTP time server in my studio for months now, and I've even gotten GPS to work for timing when used with a battery near one of the exterior walls.

But I will be following up with more timing-related adventures (to be documented here and on YouTube):

  - Permanently installing an outdoor GPS antenna with my Dad, and exploring ways to combat GPS jamming
  - Configuring PTP and testing sync across a variety of target devices (including a consumer Intel motherboard!)
  - Testing various clock options, including diving deeper into Masterclock's own (pictured above)
  - Making another attempt at getting the Pi to interface with the open source Time Card, with it's chip-scale atomic clock (CSAC) for _seriously overkill_ holdover performance
  - (Hopefully) building an ensemble clock with Masterclock to see if we can improve overall timing accuracy combining both our clocks together.
