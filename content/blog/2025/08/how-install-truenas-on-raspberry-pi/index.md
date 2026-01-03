---
nid: 3489
title: "How to install TrueNAS on a Raspberry Pi"
slug: "how-install-truenas-on-raspberry-pi"
date: 2025-08-28T14:06:28+00:00
drupal:
  nid: 3489
  path: /blog/2025/how-install-truenas-on-raspberry-pi
  body_format: markdown
  redirects: []
tags:
  - arm
  - nas
  - raspberry pi
  - truenas
  - tutorial
  - video
  - youtube
  - zfs
---

Now that Joel0 in the TrueNAS community has created a [fork of TrueNAS that runs on Arm](https://forums.truenas.com/t/truenas-on-arm-now-available/49160/16?u=geerlingguy), I thought I'd give it a spin—on a Raspberry Pi.

{{< figure src="./pi-5-with-hard-drives.jpg" alt="Raspberry Pi 5 with Hard Drives" width="700" height="394" class="insert-image" >}}

I currently run an [Ampere Arm server in my rack with Linux and ZFS](/blog/2024/building-efficient-server-grade-arm-nas) as my primary storage server, and a [Raspberry Pi with four SATA SSDs and ZFS](/blog/2024/radxas-sata-hat-makes-compact-pi-5-nas) as backup replica in my studio. My [configuration for these Arm NASes is up on GitHub](https://github.com/geerlingguy/arm-nas).

I've been looking forward to TrueNAS support on Arm for years, though it seems the sentiment in that community was 'Arm servers aren't powerful enough to run serious storage servers'—despite myself and many others doing so for many years... but that's besides the point.

## On a Raspberry Pi?

Yes, in fact.

I've found _numerous_ times, running modern applications on slower hardware is an _excellent_ way to expose little configuration flaws and misconceptions that lead to learning how to run the applications _much_ better on more capable machines.

{{< figure src="./pi-nas-ssd.jpeg" alt="Raspberry Pi 5 NAS with SSDs" width="700" height="467" class="insert-image" >}}

From my [Pi Dramble](https://pidramble.com) to my [Petabyte Pi Project](/blog/2022/petabyte-pi-project), running apps intended for much more powerful hardware taught me a lot. So maybe running TrueNAS, which demands [8 GB of RAM and 16 GB of primary storage](https://www.truenas.com/docs/core/13.0/gettingstarted/corehardwareguide/), would be a fun learning exercise.

I've done it on x86 servers, but that's boring. It's _easy_. I don't learn much when a project goes off without a hitch, and I'm not forced to look closer at some of the configuration quirks.

You can watch the video for a full demo, or read on below:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/XvaXemGDSpk" frameborder='0' allowfullscreen></iframe></div>
</div>

## On a Raspberry Pi, there's no UEFI

One glaring problem with the Raspberry Pi is no official support for UEFI, a standard way to boot computers and interface operating systems to device firmware. Raspberry Pi only _officially_ supports device-tree-based Linux booting, which is much less standard. That means you can't just throw any old Linux distribution on the Pi, you have to have ones tailored to the Pi. There _are_ good OSes for the Pi, like Raspberry Pi OS, based on Debian. But it's not the same as [grabbing Windows on Arm and installing it on my Ampere workstation](/blog/2025/system76-built-fastest-windows-arm-pc).

To get past this restriction, we have to rely on a community project, forked from [Windows on Raspberry Pi](https://worproject.com). Specifically, I'm using [NumberOneGit's rpi5-uefi fork](https://github.com/NumberOneGit/rpi5-uefi).

To get your Pi 5 to support UEFI (CM5 process may be slightly different):

  1. Update the EEPROM to the 2025-06-09 release (or later - check what version you're running in Pi OS with the command `rpi-eeprom-update`):
     a. Typically, you can upgrade using [Raspberry Pi Imager](https://www.raspberrypi.com/software/), `sudo apt full-upgrade -y`, or `sudo rpi-eeprom-update -a`. However, at the time of this writing, those methods will get you to the latest stable release (2025-05-08), so until then, use one of these methods:
     b. Manually update the bootloader with [`usbboot`](https://github.com/raspberrypi/usbboot) from source.
     c. Switch to the beta bootloader release channel: `sudo nano /etc/default/rpi-eeprom-update`, then change `latest` to `beta`, and run `sudo rpi-eeprom-update -a`.
     d. Verify the bootloader version you're running with `rpi-eeprom-update` after a reboot.
  2. Download the latest .zip file release from [rpi5-uefi Releases](https://github.com/NumberOneGit/rpi5-uefi/releases).
  3. Take a microSD card that's already formatted for the Pi (I just pulled the Pi OS card out of my Pi 5 that I just used for the EEPROM update), and clear out the contents of the FAT32 'bootfs' volume. Copy all the contents of the .zip file you downloaded into that folder (including `RPI_EFI.fd`).
  4. Eject the microSD card, insert it into the Pi, and power it on with an HDMI display connected.
  5. You should see a Raspberry Pi logo and the EDK2 bootloader screen appear. Unless you have NVMe or USB boot media installed, it will say "Press any key to enter the Boot Manager Menu."
  6. Since I couldn't find the 'any' key, I pressed 'Enter', then I could navigate through a standard boot manager menu. In there you can configure SD card speeds, set the PCIe bus speed, etc.
  7. After you've changed the settings to your liking (see some [suggestions for Linux](https://github.com/NumberOneGit/rpi5-uefi?tab=readme-ov-file#linux)), save and reset.

{{< figure src="./pi5-uefi-boot-menu.jpg" alt="Raspberry Pi 5 UEFI Boot Menu" width="700" height="394" class="insert-image" >}}

## TrueNAS on a Pi 5

Now that the Pi is booting into UEFI mode, you can install TrueNAS. To do that:

  1. Download a TrueNAS on Arm ISO from [https://truenas-releases.jmay.us](https://truenas-releases.jmay.us) (I chose [25.04.2](https://truenas-releases.jmay.us/TrueNAS-SCALE-Fangtooth/TrueNAS-SCALE-25.04.2-aarch64.iso)).
  2. Use a tool like [Etcher](https://etcher.balena.io) to write the ISO to a USB drive.
  3. After Etcher finishes, eject the USB drive and insert it into the Pi (I used a USB 3 thumb drive, so I inserted it into one of the blue USB 3 ports on the Pi for maximum speed).
  4. If it doesn't automatically boot to the TrueNAS installer, select the external USB drive in the UEFI boot manager and boot into the TrueNAS installer.
  5. Follow the TrueNAS installer's prompts to install TrueNAS on any device other than the installer drive or the microSD card (I used a second USB flash drive plugged into the other USB 3 port). Wait for installation to complete.
  6. When prompted, reboot and remove the USB drive.

TrueNAS SCALE should boot up, and the first boot can take a while as many services need to generate files, configure services, and start them the first time.

{{< figure src="./truenas-raspberry-pi-5-setup-ix-etc-fail.jpg" alt="TrueNAS installer ix-etc failure to start" width="700" height="394" class="insert-image" >}}

In my case, on first boot, the `ix-etc` service failed to start (it timed out), and its purpose is to `Generate TrueNAS /etc files`. After booting, I chose to enter the Linux console, then ran `systemctl start ix-etc`, and rebooted.

After a reboot, TrueNAS seemed to launch all its services without issue, including the web UI. I visited the IP address printed on the console, logged in as the admin user I set up during install, and was greeted with the TrueNAS dashboard:

{{< figure src="./truenas-raspberry-pi-5.jpg" alt="TrueNAS running on Raspberry Pi 5" width="700" height="394" class="insert-image" >}}

## Current Limitations

Right now, most of the limitations are around [missing features in UEFI mode](https://github.com/NumberOneGit/rpi5-uefi?tab=readme-ov-file#supported-peripherals-in-uefi); since Raspberry Pi hasn't pushed RP1 support into the Linux kernel, and nobody's yet reverse-engineered RP1 interfaces, you can't use:

  - Fan header PWM support (no fan control)
  - CSI/DSI connections for displays/cameras
  - GPIO
  - Built-in Ethernet

The Ethernet limitation is especially annoying, as you are _forced_ to use an external USB Ethernet dongle, just like on most non-Qualcomm systems running Windows on Arm.

Andrea della Porta from SUSE is [working on upstreaming RP1 support into Linux](https://www.phoronix.com/news/Raspberry-Pi-5-RP1-Linux-RFC) with some [help from Raspberry Pi](https://forums.raspberrypi.com/viewtopic.php?t=360653), but progress has been a bit slow.

What I've been wondering lately, more and more: _why doesn't Raspberry Pi consider official UEFI support in the first place?_ With or _without_ Microsoft's official blessing, being able to boot vanilla Windows 11 for Arm on the Pi would be neat. Not to mention, any regular Linux Arm distro (including TrueNAS SCALE) would boot too...

## Next Steps

I recently received a new hardware project, the [Homelabs Pi Storage server](https://github.com/kelroy1990/Homelabs-Pi-Storage), which uses a custom CM5 SATA backplane and a 3D printable enclosure for a 6-bay NAS:

{{< figure src="./homelabs-pi-storage-server-cm5.jpeg" alt="Homelabs Pi Storage server" width="700" height="467" class="insert-image" >}}

I got TrueNAS installed on a CM5 Lite (using the same process as above), but when I installed four SATA hard drives, they spun up, but were not recognized. Right now the [Pi 5 UEFI support doesn't allow for more than one PCIe device](https://github.com/NumberOneGit/rpi5-uefi/issues/21), and the Homelabs Pi Storage server has a PCIe switch that branches off to 2.5 Gbps Ethernet and a 6-port SATA controller.

These devices all work perfectly out of the box on Raspberry Pi OS (and I was able to set up a ZFS array, getting 250 MB/s over the built-in 2.5G Ethernet—see below), but they aren't recognized currently when running under UEFI :(

{{< figure src="./windows-zfs-file-copy-homelabs-pi.jpg" alt="Homelabs Pi ZFS array Samba Windows 250 MB per second" width="700" height="394" class="insert-image" >}}

I'm already running vanilla ZFS under Raspberry Pi OS on my other [Raspberry Pi storage server](/blog/2024/radxas-sata-hat-makes-compact-pi-5-nas), and that's running on four SSDs and no hard drives. It can sustain 200 MB/sec writes, and I presume TrueNAS would be able to do the same.

There are also NVMe-only boards, like the [$50 GeeekPi N16 Quad-NVMe HAT](https://amzn.to/41Us51s), which provide a pretty small footprint all-flash server option. But again, since those boards use switch chips (because the Pi is limited to 1 PCIe lane), none of those drives would be accessible to TrueNAS as it stands today. Your best bet if you want to use _TrueNAS_ instead of just managing ZFS on you own on a Pi would be to use a single-purpose HAT or SATA controller or HBA in IT mode, to connect disks directly to the Pi.

Because of the current UEFI limitations, I would still recommend running TrueNAS on higher-end Arm hardware (like Ampere servers). If you want to stick to an SBC, there's [UEFI firmware for RK3588 platforms](https://github.com/edk2-porting/edk2-rk3588) under active development. It may offer even more functionality for some boards, so check the [compatibility list](https://github.com/edk2-porting/edk2-rk3588?tab=readme-ov-file#platinum).

Or you could be boring and just install TrueNAS on x86, where it's fully supported ;)
