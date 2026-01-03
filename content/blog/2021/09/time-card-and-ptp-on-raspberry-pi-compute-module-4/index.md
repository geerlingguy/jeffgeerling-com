---
nid: 3125
title: "Time Card and PTP on a Raspberry Pi Compute Module 4"
slug: "time-card-and-ptp-on-raspberry-pi-compute-module-4"
date: 2021-09-01T14:01:17+00:00
drupal:
  nid: 3125
  path: /blog/2021/time-card-and-ptp-on-raspberry-pi-compute-module-4
  body_format: markdown
  redirects: []
tags:
  - facebook
  - networking
  - open compute project
  - open source
  - ptp
  - raspberry pi
  - time card
---

Ahmad Byagowi, the project lead for Open Compute Project's Time Appliance, reached out to me a couple weeks ago and asked if I'd be willing to test the new [Time Card Facebook had announced in mid-August](https://engineering.fb.com/2021/08/11/open-source/time-appliance/) on a Raspberry Pi Compute Module 4. Since I have a sort of obsession with plugging anything and everything into a Pi to see what works and what doesn't, I took him up on the offer.

The official specs had PCI Express Gen 3 on a x4 slot as a requirement, but it seems the Gen 3 designation is a little loose—the card and its driver should work fine on an older Gen 2 bus—like the one the Raspberry Pi Compute Module 4 exposes if you use the official IO Board:

{{< figure src="./raspberry-pi-compute-module-4-pcie-x1-focus-stacked.jpeg" alt="Raspberry Pi Compute Module 4 IO Board PCI Express Slot" width="600" height="391" class="insert-image" >}}

The slot is x1, but you can plug in any width card using an adapter [like this one](https://amzn.to/32oz9ou) or by hacking an open end into it with a razor saw or dremel tool.

## The Time Card

{{< figure src="./time-card-next-to-cm4-io-board.jpeg" alt="Time Card next to Raspberry Pi Compute Module 4 IO Board" width="600" height="445" class="insert-image" >}}

I won't get deep into the details of the Time Card—check out Facebook's post linked in the first paragraph above, or the [open source Time Card spec on GitHub](https://github.com/opencomputeproject/Time-Appliance-Project/tree/master/Time-Card)—but it's basically a PCI Express card that turns any computer into a [Stratum 1](https://endruntechnologies.com/products/ntp-time-servers/stratum1) time server.

That is, it has a built-in GNSS receiver that can acquire time from GPS, GLONASS, or any of the other positioning satellite networks, accurate to the tens of nanoseconds. Then it includes a Rubidium oscillator—the MAC from Microchip, in my card's case—to hold time accurate to a few nanoseconds for up to a couple days. And to tie everything together, there's an FPGA that interfaces with the PCIe bus and incorporates 4 PPS I/O ports.

I go into a _lot_ more detail, along with a full hardware walkthrough, in the video I just published, [The Time Card makes the most accurate Raspberry Pi clock EVER!](https://www.youtube.com/watch?v=tU0xC1ynaT8).

But the big thing the Time Appliance Project brings to the table is the ability to build a 'grandmaster' clock source based on an open design. Basically, a server that distributes extremely precise time to other computers and devices on the same network, using the Precision Time Protocol (PTP). These kinds of devices existed before, but usually they are more expensive, less standardized (in terms of integration into a rack or data center), and run proprietary software that requires vendor support.

The Time Appliance Project (and the Time Card, by extension) aims to make a standard for 'time appliances' that is more inexpensive than existing solutions and runs on an open source software stack.

## PTP and the Pi

PTP allows for a local network to have a time reference more precise than NTP, while not requiring every endpoint on the network to have its own GPS reference.

For the highest level of accuracy, PTP requires hardware timestamping support on the computer's NIC. Many popular NICs have timestamping support—for example, the [Intel I340 that I've already tested](https://pipci.jeffgeerling.com/cards_network/intel-i340-t4-4-port-1g.html) on the Compute Module 4:

{{< figure src="./5x-1-Gbps-NIC-Intel-I340-T4-on-Raspberry-Pi-Compute-Module-4.jpeg" alt="Intel I340 on Raspberry Pi Compute Module 4" width="600" height="272" class="insert-image" >}}

But here's something you might not know: the Compute Module 4's built-in NIC, a [Broadcom BCM54210PE PHY](https://www.broadcom.com/products/ethernet-connectivity/phy-and-poe/copper/gigabit/bcm54210), is actually capable of hardware timestamping—unlike the BCM54213PE used in the Pi 4 model B!

{{< figure src="./cm4-vs-pi-4-model-b-hardware-timestamping-ptp.jpg" alt="CM4 vs Pi 4 model B Broadcom NIC Ethernet chip difference" width="600" height="319" class="insert-image" >}}

However, Ahmad pointed me to this open issue: [CM4 is missing IEEE1588-2008 support through BCM54210PE](https://github.com/raspberrypi/linux/issues/4151). So _for now_, hardware timestamping on the CM4 has to be routed through an external PCI Express NIC that supports it.

## Time Card Driver

As part of my work testing the card for my [Pi PCI Express Card Database](https://pipci.jeffgeerling.com/cards_other/time-card.html), I discovered the driver in the Time Card project on GitHub won't compile on the Pi's default kernel version (5.10), due to some driver-specific functionality that requires 5.11 or newer _just to compile_. It seems that the driver recommends 5.12 or newer, and if you compile the latest 5.14 or 5.15 kernels, you can add support natively, as the `ptp_ocp` driver is now part of the kernel source!

And so that's what I did. Using my [Linux cross-compile environment](https://github.com/geerlingguy/raspberry-pi-pcie-devices/tree/master/extras/cross-compile) I cloned the Raspberry Pi Linux source tree, checked out the 5.14 branch, and compiled a kernel with the following enabled in `menuconfig`:

```
Device Drivers
  > PTP clock support
    > OpenCompute TimeCard as PTP clock
```

After copying over my custom kernel, I rebooted the Pi, and `dmesg` showed the driver initializing correctly:

```
pi@cm4:~ $ dmesg | grep ptp
[    4.425124] ptp_ocp 0000:01:00.0: enabling device (0000 -> 0002)
[    4.425224] ptp_ocp 0000:01:00.0: Time: 3603.563280960, UNSYNCED
[    4.427082] ptp_ocp 0000:01:00.0: Version 1.2.0, clock PPS, device ptp0
[    4.427123] ptp_ocp 0000:01:00.0: TOD Version 2.0.1
[    4.427143] ptp_ocp 0000:01:00.0: control: 10000001
[    4.427156] ptp_ocp 0000:01:00.0: TOD Protocol UBX enabled
[    4.427171] ptp_ocp 0000:01:00.0: GNSS ALL
[    4.427187] ptp_ocp 0000:01:00.0: status: 0
[    4.427202] ptp_ocp 0000:01:00.0: correction: 0
[    4.427216] ptp_ocp 0000:01:00.0: utc_status: 0
[    4.427229] ptp_ocp 0000:01:00.0: utc_offset: 0  valid:0  leap_valid:0
```

But as I mentioned, the CM4 itself doesn't support hardware timestamping yet. I'll be doing more testing with the card (I haven't even put it in a spot where I can get GPS reception yet!), and I'm hopeful the CM4 could be used as a Time Appliance / grandmaster clock so people could have an easier and less expensive option for highly accurate timing on their networks!

It's not only useful in the data center—a good clock source can be used in media production, industrial automation, 5G, heck, maybe even in [coordinating turn signals](https://www.youtube.com/watch?v=2z5A-COlDPk) someday!

Be sure to [check out my YouTube video on the Time Card](https://www.youtube.com/watch?v=tU0xC1ynaT8) for more details and stay tuned—this isn't the last you'll see of the Pi and Time Card on the blog!
