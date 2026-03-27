---
date: '2026-03-27T09:00:00-05:00'
tags: ['minidv', 'firewire', 'raspberry pi', 'youtube', 'video', 'canon', 'gl1', 'firehat']
title: 'Bring back MiniDV with this Raspberry Pi FireWire HAT'
slug: 'minidv-with-raspberry-pi-firewire-hat'
---
In my last post, I showed you to use [FireWire on a Raspberry Pi](/blog/2026/firewire-on-a-raspberry-pi/) with a PCI Express IEEE 1394 adapter. Now I'll show you how I'm using a new [FireWire HAT](https://equip-1.c-e.group) and a [PiSugar3 Plus](https://amzn.to/4dKtuyg) battery to make a portable MRU, or 'Memory Recording Unit', to replace tape in older FireWire/i.Link/DV cameras.

{{< figure
  src="./firehat-raspberry-pi-recording-from-firewire.jpeg"
  alt="Firehat on Raspberry Pi recording video from Canon GL1 over FireWire"
  width="700"
  height="auto"
  class="insert-image"
>}}

The alternative is an old used MRU like [Sony's HVR-MRC1](https://pro.sony/s3/cms-static-content/operation-manual/3290149121.pdf), which runs around $300 on eBay[^piprice].

In addition to a direct camera connection, this setup can be used to archive MiniDV tapes to the Pi with `dvgrab`, or even with other FireWire devices like audio interfaces and hard drives. After Apple [dropped FireWire support in macOS Tahoe](https://9to5mac.com/2025/07/07/macos-tahoe-reports-of-firewires-death-are-not-greatly-exaggerated/), some users were left in a lurch.

## Video

This blog post is a companion to today's video, where I test recording to tape and to the Pi using two different setups, and even test how the 'old' NLE editing workflow used to work when I started my YouTube channel in 2006:

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/BuKeW45OL-g' frameborder='0' allowfullscreen></iframe></div>
</div>

Don't like watching videos? I don't blame you—read on!

## Hardware

{{< figure
  src="./firehat-pi-5-with-canon-gl1.jpeg"
  alt="Firehat on Raspberry Pi recording video from Canon GL1 over FireWire"
  width="700"
  height="auto"
  class="insert-image"
>}}

The hardware I used in my final setup (pictured above) includes:

  - Raspberry Pi 5 (I used a 4GB model, but any amount of RAM should suffice)
  - [Computer Equipment Group's Firehat](https://equip-1.c-e.group)
  - [PiSugar 3 Plus 5000mAh Pi Battery](https://amzn.to/4dKtuyg)
  - Apple FireWire cable (4 pin to 6 pin)
  - Canon GL1 miniDV Camcorder

The Firehat model I'm using is a prototype (thanks to Twin CD for sending it!). As such, it has a requisite number of bodge wires :)

{{< figure
  src="./firehat-raspberry-pi-via-VT6315N-bodge-pcb.jpeg"
  alt="Firehat bodged PCB traces from VIA VT6315N FireWire controller chip"
  width="700"
  height="auto"
  class="insert-image"
>}}

It will be sold either as a standalone Pi HAT (the 'Firehat'), or integrated into a small standalone device paired with a Radxa Rock 2F ('equip-1'), at least if their [equip-1 / Firehat Crowd Supply campaign](https://www.crowdsupply.com/computer-equipment-group/equip-1) is successful,

{{< figure
  src="./firehat-raspberry-pi-mru-pisugar-battery-5000mah.jpeg"
  alt="Firehat with PiSugar 3 Plus Battery"
  width="700"
  height="auto"
  class="insert-image"
>}}

To make my setup portable, I added on a PiSugar 3 Plus (pictured above), which uses pogo pins to mate to the bottom of the Pi 5, providing power and I2C communication for battery status and configuration.

In my testing, the included 5000 mAh battery gets between 2-4 hours of runtime, depending on whether you're recording the whole time, and what kind of storage media you're using (this setup has built-in WiFi, so you could record direct to a NAS!). I got over 3 hours recording straight to a 64GB Raspberry Pi microSD card.

## Software

The Firehat uses the Pi's GPIO to accept input through three buttons, and the I2C bus and more GPIO pins to sound a buzzer for button feedback, and LED for recording and other status indication, and a small OLED display to show recording time, the device's IP address, storage information, and battery life (if using a PiSugar).

Because Pi OS doesn't come with Linux's FireWire support enabled, you'll have to recompile the Linux kernel first, then install and run the Firehat software to get it fully operational:

  1. [Enable FireWire support on the Pi](/blog/2026/firewire-on-a-raspberry-pi/) following my guide
  2. [Install the Firehat software](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/805) (under 'Equip-1 Setup')
  3. (Optionally) [Enable the Firehat software at boot](https://github.com/computerequipmentgroup/equip-1/issues/5)

Assuming you've set everything up correctly, when you reboot your Pi, you should see the default interface (with 'NO CAM' displayed if you don't have a camera plugged in and powered on):

{{< figure
  src="./firehat-pi-5-no-cam-running.jpeg"
  alt="Firehat running on Raspberry Pi 5 with NO CAM on screen"
  width="700"
  height="auto"
  class="insert-image"
>}}

If you create new recordings, they're saved under your default user account's home folder in a `captures` directory. From there, you can copy the files over to a USB drive, or copy them over WiFi to another computer.

On my Mac I used [Transmit's](https://panic.com/transmit/) SFTP capabilities to log into the Pi and copy down files. You could also use `scp` or `rsync` if you like.

## Alternatives

As mentioned in my [earlier post](/blog/2026/firewire-on-a-raspberry-pi/), you could buy a standard [Mini PCIe HAT](https://amzn.to/47U0vFj) for the Pi, and install this [StarTech Mini PCIe FireWire adapter in it](https://amzn.to/4lRrQeU). That setup was first demonstrated by Redditor toqer and labelled the [Open MRU](https://www.reddit.com/r/tapeless/comments/1n3aqsk/open_mru_raspberry_pi_5_based_mrucapture_device/) in the r/tapeless subreddit.

For all the details, I [documented my own Open MRU setup on GitHub](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/752#issuecomment-3993043500). Without any GPIO-enabled buttons, controlling `dvgrab` is a little more involved—I had to start and stop recordings via `dvgrab` on the command line.

The Open MRU build uses the TI XIO2213A controller, versus the VIA VT6315N in the Firehat. People have tested other FireWire controllers on the Pi in the past, but these are the only two I've _confirmed_ work with the Pi 5 so far.

## Other FireWire devices and the 2029 deadline

I haven't had a chance to test other FireWire devices yet, or FireWire networking (though a 400 Mbps network connection is less than half the speed of the Pi's built-in Ethernet!).

But I've heard from a few people still running FireWire audio interfaces, or wanting to interface with old Macs via their built-in FireWire ports, so if _you've_ tested any non-camera IEEE 1394 devices, please share your experience in the comments.

This setup should continue working with the latest versions of Linux and Pi OS [until at least 2029](https://ieee1394.docs.kernel.org/en/latest/#maintenance-schedule), but the future for FireWire in the Linux kernel after that is less clear.

The equip-1 and Firehat should be available through [this Crowd Supply page](https://www.crowdsupply.com/computer-equipment-group/equip-1). Fingers crossed they can get to production and ship soon!

[^piprice]: The Pi setup above costs between $150-200 brand new.
