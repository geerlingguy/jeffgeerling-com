---
nid: 3221
title: "PTP and IEEE-1588 hardware timestamping on the Raspberry Pi CM4"
slug: "ptp-and-ieee-1588-hardware-timestamping-on-raspberry-pi-cm4"
date: 2022-07-06T17:25:30+00:00
drupal:
  nid: 3221
  path: /blog/2022/ptp-and-ieee-1588-hardware-timestamping-on-raspberry-pi-cm4
  body_format: markdown
  redirects:
    - /blog/2022/ptp-and-hardware-timestamps-on-raspberry-pi-cm4
aliases:
  - /blog/2022/ptp-and-hardware-timestamps-on-raspberry-pi-cm4
tags:
  - cm4
  - compute module
  - ethernet
  - ntp
  - ptp
  - raspberry pi
  - time
  - time card
---

> **2024 Update**: This works out of the box on the Compute Module 5. [See comment](https://www.jeffgeerling.com/comment/34489#comment-34489).

I've been following the issue [CM4 is missing IEEE1588-2008 support through BCM54210PE](https://github.com/raspberrypi/linux/issues/4151) since I heard about IEEE1588-2008 support on the Compute Module 4 last year.

{{< figure src="./broadcom-nic-cm4.jpeg" alt="Broadcom NIC on Raspberry Pi Compute Module 4" width="700" height="436" class="insert-image" >}}

Apparently the little NIC included on every Compute Module 4—the `BCM54210PE`, which is _different_ than the NIC on the Pi 4 model B (a `BCM54213PE`)—includes support for a feature called PTP, or [Precision Time Protocol](https://en.wikipedia.org/wiki/Precision_Time_Protocol).

> **Update**: I also posted a video about PTP on the CM4 on my YouTube channel: [It's About Time (PTP on the Raspberry Pi CM4)](https://www.youtube.com/watch?v=RvnG-ywF6_s).

If you thought NTP was great, with its millisecond-level accuracy when synchronizing clocks over a network, you'll love PTP—it can sync down to nanoseconds, or in some cases even _picoseconds_!

PTP is more prevalent in HFT (High Frequency Trading) in finance, scientific research, and distributed databases that need highly accurate timings.

But with a tiny Compute Module 4 able to control hardware timestamps—plus the plethora of available high-quality GPS HATs for the Pi—maybe highly-accurate time could be more democratized!

## Getting PTP and PPS

{{< figure src="./pin-9-raspberry-pi-cm4-io-board.jpeg" alt="Pin 9 Raspberry Pi Compute Module 4 IO Board J2" width="700" height="422" class="insert-image" >}}

The Compute Module 4 IO Board comes with two pins (8 and 9 on J2) labeled SYNC_IN and SYNC_OUT. Those pins are _supposedly_ wired to the PHY with 1.8v signalling (see the [CM4 datasheet](https://datasheets.raspberrypi.com/cm4/cm4-datasheet.pdf))—but through a bunch of experimentation, it seems only pin 9 is wired correctly.

So on the Compute Module 4, you can get a PPS input or output through pin 9, but not both at the same time—at least when using the official CM4 IO Board.

The PPS is helpful for debug purposes, and if you need to distribute a PPS to any equipment that uses a PPS input for time sync. Otherwise, PTP is useful for synchronizing time over the Pi's Ethernet connection to any 'slave' devices on the same network.

I'll have more on this in an upcoming video, but I wanted to post instructions for how to set up a CM4 as a PTP master / time server.

Patches were only recently added to the Pi OS kernel fork, for example:

  - [Add PTP support for the CM4](https://github.com/raspberrypi/linux/commit/129b03a77347a09d07c143229fc2ddd27b0d7a36)
  - [Add PPS out for the CM4](https://github.com/raspberrypi/linux/commit/a004834f716de41a111723b95208c40af61999b2)

And the same patchset is already upstream in later versions of the Linux kernel (yay!). But to get these running on a Pi _today_, you need to run `sudo rpi-update` to get the latest kernel version (which is not yet installed when running `sudo apt upgrade`).

Once you do that and reboot, you should see a new `ptp` device:

```
$ ls /dev/ptp*
/dev/ptp0

$ cat /sys/class/ptp/ptp0/clock_name 
bcm_phy_ptp
```

And then you should see its hardware timestamping capabilities listed using `ethtool`:

```
$ ethtool -T eth0
Time stamping parameters for eth0:
Capabilities:
	hardware-transmit
	hardware-receive
	hardware-raw-clock
PTP Hardware Clock: 0
Hardware Transmit Timestamp Modes:
	off
	on
	onestep-sync
	onestep-p2p
Hardware Receive Filter Modes:
	none
	ptpv2-event
```

And for a final test, assuming you have an oscilloscope hooked to pin 9 and a ground pin, you can enable PPS output and monitor it on a scope:

```
$ sudo ./testptp -d /dev/ptp0 -L0,2
set pin function okay
$ sudo ./testptp -d /dev/ptp0 -p 1000000000
periodic output request okay
```

{{< figure src="./pps-output-oscilloscope-pi-cm4.jpg" alt="PPS output on Tektronix oscilloscope from Raspberry Pi Compute Module 4" width="700" height="394" class="insert-image" >}}

## What's next?

Well, remember the open source [Time Card](/blog/2021/time-card-and-ptp-on-raspberry-pi-compute-module-4) I mentioned last year? Well, using it—or something similar, with GPS and a better oscillator, like temperature-controlled oscillator (TCXO) or a chip-scale atomic clock, you could build a very competent (and relatively inexpensive) master clock / stratum-1 time server for both PTP and NTP.

This can be useful for the aforementioned database, HFT, and scientific projects... but it could also bring better timings to other applications as well. Programming changes a bit when you can guarantee you're within _nanoseconds_ of UTC—assuming you have a good GPS chip and decent time holdover for GPS dropouts.

{{< figure src="./overview-pi-cm4-ptp-sync-pps-oscilloscope.jpeg" alt="Raspberry Pi Compute Module 4 PTP Sync PPS on Oscilloscope" width="700" height="467" class="insert-image" >}}

On two Compute Module 4s, using `ptp4l`, I'm able to sync two Compute Module 4's on a LAN to within about 10-15 nanoseconds of each other (that's a 10ns/division time scale in the above picture).

The commands I ran to set up and test PTP were:

```
# Run this on the 'master' Pi:
sudo ptp4l -i eth0 --masterOnly 1 -m --tx_timestamp_timeout 200

# Run this on any 'slave' Pis:
sudo ptp4l -i eth0 --slaveOnly 1 -m --tx_timestamp_timeout 200
```

Thanks especially to Ahmad Byagowi and his team over at Meta spearheading the [Time Appliances Project](https://www.opencompute.org/wiki/Time_Appliances_Project), and to Lasse Johnsen at [Timebeat](https://timebeat.app) for their help in getting this moving. It seemed like things were stuck for a while, but they were able to work with engineers at Raspberry Pi and Broadcom to get the necessary patches written and tested!

I'll cover more on PTP/IEEE1588 and PPS on the CM4 in my upcoming video [on my YouTube channel](https://www.youtube.com/c/JeffGeerling), so subscribe if you want to see that. I will also continue to publish my findings with the Time Card in [this GitHub issue](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/199).
