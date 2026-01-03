---
nid: 3290
title: "How I installed TrueNAS on my new ASUSTOR NAS"
slug: "how-i-installed-truenas-on-my-new-asustor-nas"
date: 2023-06-21T14:57:30+00:00
drupal:
  nid: 3290
  path: /blog/2023/how-i-installed-truenas-on-my-new-asustor-nas
  body_format: markdown
  redirects: []
tags:
  - asustor
  - flashstor
  - linux
  - nas
  - truenas
  - tutorial
---

A common question I get asked whenever my ASUSTOR NAS makes an appearance is: "but can it do ZFS?"

I'm still trying to convince them to add it to ADM alongside EXT4 and Btrfs support, but until that time, the 2nd best option is to just run another OS on the NAS! This is now **permitted**, but you won't get technical support from ASUSTOR for other OSes.

Some people (myself included) like buying hardware and... doing what we want with it! And for computer hardware, that often involves installing whatever OS and software we want to do the things we want to do. Pretty crazy, coming from a guy who uses a Mac, right?

{{< figure src="./asustor-flashstor-12-front.jpeg" alt="ASUSTOR Flashstor 12 - front" width="700" height="394" class="insert-image" >}}

The [Flashstor 12](/blog/2023/first-look-asustors-new-12-bay-all-m2-nvme-ssd-nas) just came out, and ASUSTOR sent me one for testing. It has an Intel N5105 CPU in it, and the system is configured as a typical mini PC—just with _twelve NVMe slots_ and 10 Gbps Ethernet. It even has HDMI, USB, and SPDIF optical audio, so it's almost purpose-built to be a quiet media desktop with massive amounts of silent, fast storage.

{{< figure src="./asustor-flashstor-12-hdmi-usb.jpeg" alt="ASUSTOR Flashstor 12 - rear IO USB network HDMI" width="700" height="394" class="insert-image" >}}

It's a little expensive for that purpose, but it could do it. There's nothing preventing you from running Windows on this machine. Or replacing ADM—ASUSTOR's own Busybox Linux-derivative OS—with something a bit more storage-focused, like TrueNAS!

So that's what I'm going to do today. ASUSTOR actually [published a guide for installing TrueNAS](https://www.youtube.com/watch?v=YytWFtgqVy0), but I've added a few more details and I'll also show you how to back up ADM in case you accidentally mess up the factory install in the future!

## Optional, but recommended - Back up ADM

The first thing I did, to make sure I would be able to restore my system to running ADM no matter what, is back up ADM from the Flashstor's built-in eMMC to another USB flash drive.

This is not required, especially if you disable the eMMC in BIOS (see the next section), but I like having the peace of mind, since (AFAICT) there's no way to download a copy ADM from ASUSTOR's website, at least not publicly.

  1. Plug in an empty USB flash drive
  2. Write a bootable Linux ISO to a _different_ USB flash drive (I'm wrote Ubuntu 22.04 Desktop to a flash drive using Balena Etcher), and plug that in, too
  3. Boot the box with a monitor, keyboard, and mouse plugged in, and press F2 once the TianoCore splash screen appears
  4. In the BIOS, move to the left until you reach the Boot menu
  5. Scroll down to 'eMMC' entry, and press `-` repeatedly to move it to the bottom of the boot order (alternatively, go to the USB flash drive entry and press `+` repeatedly to move it to the top)
  6. Press F10 to save changes. Confirm, and reboot.

Once it reboots, it _should_ boot into Ubuntu (or whatever Linux distro you had installed) instead of the built-in ADM OS.

Assuming you're booting from an Ubuntu ISO, when it asks, choose 'Try Ubuntu', and this will boot you into the desktop environment. Open a terminal, and run `lsblk` to verify you can see an `mmcblk0` device (should be 8 GB), and your blank USB flash drive (something like `sdb`).

Make sure your blank USB flash drive (in my case `sdb`) is formatted and mounted. In my case, when I plugged in my exFAT or NTFS-formatted USB drive, Ubuntu identified it and automatically mounted it to `/media/ubuntu/[volume label]`.

{{< figure src="./ubuntu-backup-flashie-emmc-asustor.jpg" alt="Ubuntu back up ADM" width="700" height="394" class="insert-image" >}}

Now, the important part: use `dd` to clone the contents of the eMMC drive to the flash drive:

```
sudo dd if=/dev/mmcblk0 of=/path/to/usb/adm-image.img bs=16M
```

This will take a few minutes, but once it's complete, consider storing that ADM `.img` file somewhere safe so you can re-image the eMMC if you ever need to.

## Optional, but recommended - Disable eMMC

Once you've made a backup of ADM from the eMMC, you _could_ erase the eMMC drive and install Linux on top of it. But **that's a bad idea**, because (a) that eMMC drive is only 8 GB, which means you could run out of space on it pretty easily, and (b) it's easier to leave that volume in place and just boot from an external USB drive.

{{< figure src="./asustor-flashstor-12-bios-emmc.jpg" alt="ASUSTOR BIOS - Disable eMMC support" width="700" height="447" class="insert-image" >}}

So to disable the eMMC drive entirely, for safekeeping:

  1. Boot into BIOS (hold down F2 during boot)
  2. Go to Advanced &gt; Intel Advanced Menu &gt; PCH-IO Configuration &gt; SCS Configuration
  3. Set eMMC 5.1 to 'Disabled'
  4. Press F10 to save changes. Confirm, and reboot.

If you reboot, it will likely just enter the UEFI Shell since it is set to boot only off eMMC from the factory. You have to go back into BIOS following the steps in the next section.

## Install another OS

Assuming you've disabled the eMMC drive, you will now need to set up some other boot drive. I installed a cheap [Kingston 120 GB SSD](TODO) into a similarly cheap Inateck USB to SATA case, then plugged _that_ into the blue (SuperSpeed) USB 3 plug on the back of the NAS.

I plugged my TrueNAS install USB flash drive into the front of the NAS, and then booted into BIOS by pressing the F2 key repeatedly once the TianoCore splash screen appeared.

I made sure the USB flash drive was set at the top of the boot order, pressed F10 to save changes, confirmed and rebooted, and was presented with the TrueNAS installer.

I followed the install wizard, making sure to choose the USB drive (and not one of the internal NVMe—though that is an option!).

{{< figure src="./asustor-flashstor-truenas-install-sdb-succeeded.jpg" alt="ASUSTOR Flashstor 12 TrueNAS install success message" width="700" height="394" class="insert-image" >}}

Once I rebooted (removing the install USB), TrueNAS completed its setup process and booted right up!

Accessing the web UI, I could complete the rest of the initialization process:

{{< figure src="./truenas-installed-storage-dashboard-asustor-flashstor-12.jpg" alt="TrueNAS Storage display running on ASUSTOR Flashstor 12" width="700" height="394" class="insert-image" >}}

## Reverting to ADM

To go back to ADM, first re-enable the eMMC drive if you had previously disabled it, then go to the BIOS Boot Order menu and find the eMMC drive in the list, then press `+` to push it up to the top again. Press F10 to save the setting, reboot, and you'll be back to the ADM you know and love.

## Is this supported?

It's _permitted_ under ASUSTOR's warranty terms, but it looks like they don't provide technical support if you change OSes, since their NASes are sold as a kit with hardware + software combined. You can always switch back to ADM, though.

For full details, here's a still frame from their [video about it](https://www.youtube.com/watch?v=YytWFtgqVy0):

{{< figure src="./adm-notes.jpg" alt="ADM Notes for switching to another OS on an ASUSTOR NAS" width="700" height="411" class="insert-image" >}}

## Conclusion

How does TrueNAS _perform_ on the Flashstor 12 Pro? Well, that's a topic I'll explore in an upcoming video. [Subscribe to my YouTube channel](https://www.youtube.com/c/JeffGeerling) so you don't miss it!
