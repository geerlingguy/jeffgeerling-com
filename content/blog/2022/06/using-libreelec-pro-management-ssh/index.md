---
nid: 3212
title: "Using LibreELEC like a pro\u2014management via SSH"
slug: "using-libreelec-pro-management-ssh"
date: 2022-06-01T20:49:32+00:00
drupal:
  nid: 3212
  path: /blog/2022/using-libreelec-pro-management-ssh
  body_format: markdown
  redirects:
    - /blog/2022/using-libreelec-pro—management-ssh
aliases:
  - /blog/2022/using-libreelec-pro—management-ssh
tags:
  - kodi
  - libreelec
  - linux
  - raspberry pi
  - remote access
  - ssh
  - usb
---

For a recent project, I needed to install LibreELEC/Kodi on a Raspberry Pi Compute Module 4 with built-in eMMC storage.

Because it's inconvenient to be swapping the Pi around from the embedded display I was using it in to my preferred carrier board I use for flashing Pis and interacting with their filesystems, I wanted to manage my LibreELEC install over SSH.

It seems like whatever documentation the [LibreELEC Wiki](https://wiki.libreelec.tv) _used_ to have for remote SSH access is missing, and all I could find were references to enabling SSH during a GUI setup wizard. If you didn't see that during initial setup, the easiest way is to add `ssh` to the end of the line in the system's `cmdline.txt` file, then reboot.

So I pulled the Pi, used `usbboot` to mount the fat32 volume on my Mac, and opened `cmdline.txt` and added `ssh`. Then I popped the Pi back in the embedded display, and started it up.

Sure enough, I could now SSH in:

{{< figure src="./ssh-into-libreelec.png" alt="SSH into LibreELEC" width="700" height="284" class="insert-image" >}}

The default user is `root` and the default password is `libreelec`. No wonder they don't have SSH enabled by default :P

If you have a typical network, you don't need to hunt for the Pi's IP address either, you can just type in `ssh root@LibreELEC.local` and that should find it by mDNS on your local network.

Now, another thing I wanted to do was enable USB so I could plug a keyboard or flash drive into my embedded display. The [CM4 doesn't enable the built-in USB 2.0 ports by default](/blog/2020/usb-20-ports-not-working-on-compute-module-4-check-your-overlays)—or at least it didn't, historically.

But if I tried editing the `/flash/config.txt` file, it said it wasn't editable. Apparently the `/flash` directory is mounted read-only at boot, so I had to [remount it as read-write](https://wiki.libreelec.tv/configuration/config_txt#edit-via-ssh).

Once I did that, I added `dtoverlay=dwc2,dr_mode=host` to enable USB 2.0 at the end of the `/flash/config.txt` file, and rebooted (`reboot`).

It's probably a good idea to change the default SSH password (`passwd` while logged in as `root`) while you're in there.

SSH can be useful for a number of things. Remote management, config backups, uploading/downloading files, and remote rebooting of your LibreELEC box, to name a few.
