---
nid: 3311
title: "NVMe SSD boot with the Raspberry Pi 5"
slug: "nvme-ssd-boot-raspberry-pi-5"
date: 2023-10-22T02:46:29+00:00
drupal:
  nid: 3311
  path: /blog/2023/nvme-ssd-boot-raspberry-pi-5
  body_format: markdown
  redirects:
    - /blog/2023/booting-nvme-ssd-raspberry-pi-5
aliases:
  - /blog/2023/booting-nvme-ssd-raspberry-pi-5
tags:
  - boot
  - eeprom
  - nvme
  - performance
  - pi 5
  - raspberry pi
  - sbc
---

{{< figure src="./pi-5-pcie-nvme.jpg" alt="Pi 5 PCIe NVMe Kioxia XG8 SSD" width="700" height="408" class="insert-image" >}}

In my [video about the Raspberry Pi 5](https://www.youtube.com/watch?v=nBtOEmUqASQ), I mentioned the new external PCIe port makes it possible to boot the standard Pi 5 model B directly off NVMe storage—an option which is _much_ faster and more reliable than standard microSD storage (even with industrial-rated cards!).

Enabling NVMe boot is pretty easy, you add a line to `/boot/firmware/config.txt`, [modify the `BOOT_ORDER`](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#BOOT_ORDER) in the bootloader configuration, and reboot!

Of course, you'll also need to get Pi OS onto the NVMe, and there are a few ways to do that—I'll walk you through my favorite method below.

> Note: Raspberry Pi announced they are developing an official [Raspberry Pi M.2 HAT](https://pipci.jeffgeerling.com/hats/pi-nvme-hat.html), but there is no word on a launch date for it yet. I am also tracking other [PCIe HATs for Raspberry Pi 5 here](https://pipci.jeffgeerling.com/hats).

## Enable the external PCI Express port

> **Note**: If using a HAT+-compliant NVMe adapter (like Raspberry Pi's own NVMe HAT), you do not need to enable the external PCIe port—it will be enabled automatically. But you can still force PCIe Gen 3 speeds using the option below.

First, enable the external PCIe port on the Raspberry Pi 5. Edit `/boot/firmware/config.txt` and add the following at the bottom:

```
# Add to bottom of /boot/firmware/config.txt
dtparam=pciex1

# Note: You could also just add the following (it is an alias to the above line)
# dtparam=nvme

# Optionally, you can control the PCIe lane speed using this parameter
# dtparam=pciex1_gen=3
```

I have the `pciex1_gen=3` part commented out above because Raspberry Pi _allows_ you to tweak the bus speed (you can choose Gen 1 for 2.5 GS/s, Gen 2 for 5 GS/s, and Gen 3 for 8 GS/s), but the port is only rated for up to PCIe Gen 2 speeds.

In practice, I have been able to run multiple NVMe SSDs at Gen 3.0 speed (getting up to 900 MB/sec) on my alpha Pi 5, but YMMV—PCIe can be very fickle, depending on the quality of the FFC cable and connections on your own setup.

## Set NVMe early in the boot order

The PCIe connection should work after a reboot, but your Pi might take a while to start booting. You can reduce that time by telling the Pi to try booting off the NVMe drive first, then looking for other devices. The traditional way to do this is to change the `BOOT_ORDER` in the Raspberry Pi's bootloader configuration:

```
# Edit the EEPROM on the Raspberry Pi 5.
sudo rpi-eeprom-config --edit

# Change the BOOT_ORDER line to the following:
BOOT_ORDER=0xf416

# Add the following line if using a non-HAT+ adapter:
PCIE_PROBE=1

# Press Ctrl-O, then enter, to write the change to the file.
# Press Ctrl-X to exit nano (the editor).
```

Read [Raspberry Pi's documentation on BOOT_ORDER](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#BOOT_ORDER) for all the details. For now, the pertinent bit is the `6` at the end: that is what tells the Pi to attempt NVMe boot first!

The newer, easier way to do this is using `raspi-config`:

```
# Open the Raspberry Pi configuration editor
sudo raspi-config

# Navigate to Advanced Options > Boot > Boot Order
# Highlight 'NVMe/USB Boot' and press enter
# Follow the prompts
```

Reboot your Raspberry Pi 5 to make the change take effect.

NVMe boot won't work unless you have the external PCI Express port enabled, _and_ there's a working NVMe drive with a valid boot partition! If you don't have that (e.g. you used Raspberry Pi Imager with an external USB NVMe adapter to flash Pi OS to an NVMe drive from another computer), then follow the steps in the next section to clone your existing Pi OS install to an NVMe SSD.

## Flash the SSD with Raspberry Pi Imager

To get the NVMe SSD to boot your Pi, it needs to have an OS. One option would be to clone an existing installation to it using `rpi-clone` or some other tool (see below), but my preferred option is to flash a fresh Pi OS install using [Raspberry Pi Imager](https://www.raspberrypi.com/software/).

  1. Install Pi Imager and open it
  2. Plug your NVMe SSD into your computer using a [USB to NVMe adapter](https://amzn.to/3szvWCP)
  3. Choose an OS to install
  4. Choose the drive (connected through your adapter) to flash
  5. Click write (and set any options you'd like)

Once flashing is complete, pull the NVMe drive, attach it to your Pi 5, and it should boot off it (with or without a microSD card inserted)—assuming you have the bootloader up to date and set the `BOOT_ORDER` appropriately!

## Clone your microSD boot volume to an NVMe SSD

Assuming you already have Raspberry Pi OS on a microSD card that is booting your Raspberry Pi 5 internally, and the NVMe SSD is connected and visible (check if you see a device `/dev/nvme0n1` after running `lsblk`), you can use [`rpi-clone`](https://github.com/geerlingguy/rpi-clone) to clone the internal microSD boot volumes to your NVMe SSD:

```
# Install rpi-clone.
git clone https://github.com/geerlingguy/rpi-clone.git
cd rpi-clone
sudo cp rpi-clone rpi-clone-setup /usr/local/sbin

# Clone to the NVMe drive (usually nvme0n1, but check with `lsblk`).
sudo rpi-clone nvme0n1
```

> Note: I'm using my fork of `rpi-clone`, because the official version has gone unmaintained—see [NVMe support](https://github.com/billw2/rpi-clone/pull/147). Huge thanks to `@billw2` for building `rpi-clone`!

> Note 2: You may want to wipe all disk partitions before cloning:
>
> ```
> sudo umount /dev/nvme0n1p?
> sudo wipefs --all --force /dev/nvme0n1p?
> sudo wipefs --all --force /dev/nvme0n1
> sudo dd if=/dev/zero of=/dev/nvme0n1 bs=1024 count=1
> ```

## NVMe behind a PCIe bridge / switch

Currently the Raspberry Pi 5 only exposes one PCIe lane externally—though there are four more lanes taken up by the RP1 chip. Typical PC motherboards have a number of lanes to play with, so you often find two, three, or even _four_ M.2 NVMe slots on high-end motherboards.

Even there, some motherboards have PCI Express switches (or 'bridges') which allow multiple PCIe devices to share the same lane or lanes, in a similar way an Ethernet switch can allow multiple computers to share a single network connection.

{{< figure src="./nvme-boot-behind-pcie-switch-raspberry-pi-.jpeg" alt="NVMe boot behind PCIe switch on Raspberry Pi" width="700" height="394" class="insert-image" >}}

On the Compute Module 4, [bootloader space constraints prevented NVMe boot if you used a switch](https://github.com/raspberrypi/firmware/issues/1684), but I wonder if that restriction is lifted on the Raspberry Pi 5—and if so, is it already implemented?

As of now, no. I can _see_ and _use_ an NVMe SSD through a PCIe switch, but I am not able to _boot_ the Raspberry Pi 5 from it, unless it is directly connected (as the lone PCIe device on the bus).

I've opened an issue to ask about this feature in the Raspberry Pi firmware repo: [Can't boot Pi 5 via NVMe behind PCIe switch / bridge](https://github.com/raspberrypi/firmware/issues/1833).
