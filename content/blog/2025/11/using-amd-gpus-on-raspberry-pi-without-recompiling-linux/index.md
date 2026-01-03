---
nid: 3512
title: "Using AMD GPUs on Raspberry Pi without recompiling Linux"
slug: "using-amd-gpus-on-raspberry-pi-without-recompiling-linux"
date: 2025-11-14T14:58:14+00:00
drupal:
  nid: 3512
  path: /blog/2025/using-amd-gpus-on-raspberry-pi-without-recompiling-linux
  body_format: markdown
  redirects: []
tags:
  - amd
  - drivers
  - gpu
  - linux
  - open source
  - raspberry pi
---

I'm working on a more in-depth test of some newer AMD GPUs on the Raspberry Pi, now that the [15 line kernel patch](/blog/2025/full-egpu-acceleration-on-pi-500-15-line-patch) is (IMO) nearly ready for upstreaming.

{{< figure src="./raspberry-pi-cm5-amd-radeon-ai-pro-9700.jpg" alt="Raspberry Pi CM5 with AMD Radeon AI Pro 9700 GPU" width="700" height="394" class="insert-image" >}}

But this blog post shows how to quickly get almost _any_ modern AMD GPU running on a Raspberry Pi 5, CM5, or Pi 500+, thanks to [this patch on the Pi Linux fork](https://github.com/raspberrypi/linux/pull/7113).

> Note: This patch actually enables AMD _and_ Intel. I wrote about [how to get Intel Arc GPUs running on the Pi](https://www.jeffgeerling.com/blog/2025/all-intel-gpus-run-on-raspberry-pi-and-risc-v) yesterday.

Using Raspberry Pi's [rpi-update](https://github.com/raspberrypi/rpi-update) tool, you can quickly upgrade your Linux kernel to the one built by the patch PR above (assuming you're running the latest Pi OS, 'Trixie').

First, make sure your system is up to date and has the AMD firmware package installed:

```
sudo apt update
sudo apt upgrade -y
sudo apt install -y firmware-amd-graphics
sudo reboot
```

Then, log back in and install the updated kernel version which includes the AMD kernel module:

```
sudo rpi-update pulls/7113
```

This will update the Linux kernel to the one built off the PR branch. It enables AMD GPU support on both the BCM2711 used in the Pi 4 generation, and BCM2712 for the Pi 5.

Before rebooting, edit your `/boot/firmware/config.txt` file, and add the following at the bottom:

```
dtparam=pciex1_gen=3  # for faster PCIe Gen 3 speeds on Pi 5
auto_initramfs=0  # to avoid 'weird boot mechanisms or file systems'
```

If you reboot with a GPU attached to the PCIe connection (e.g. on my CM5, I have one plugged into the M.2 slot using [this M.2 to Oculink adapter](https://amzn.to/3K18FlS) and [this eGPU dock](https://amzn.to/4qYWvut)), it might work right away, assuming you have a card with firmware in the package you installed earlier.

If it's a newer card, or if you don't see the card working (e.g. you don't get display output), Run the command `dmesg` and check for `amdgpu` messages, like:

```
[    3.693561] amdgpu 0001:03:00.0: amdgpu: Fetched VBIOS from ROM BAR
[    3.693579] amdgpu: ATOM BIOS: 113-48WD6SHD1-P02
[    3.693616] amdgpu 0001:03:00.0: Direct firmware load for amdgpu/psp_14_0_3_sos.bin failed with error -2
[    3.693626] amdgpu 0001:03:00.0: amdgpu: early_init of IP block <psp> failed -19
```

If you see any firmware load failures, you may need to download the firmware `.bin` files directly from the [linux-firmware.git](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/amdgpu/) repository[^firmware]. Also check for your graphics card in the [Pi PCIe Database](https://pipci.jeffgeerling.com) in case someone else has run into the same errors.

When using `apt` with this PR-based kernel, you can ignore any errors regarding `initramfs`, like `dpkg: error processing package initramfs-tools`[^initramfs], but if you'd like to [get rid of those errors](https://serverfault.com/questions/905921/mkinitramfs-failed-to-determine-device-for), create a `driver-policy` file and add the following:

```
sudo nano /etc/initramfs-tools/conf.d/driver-policy
# Inside the file, put the line:
MODULES=most
```

Reboot the Pi, then check on `dmesg` output again. If you see any more firmware load failures, you may need to download the firmware `.bin` files directly from the [linux-firmware.git](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/amdgpu/) repository[^firmware].

But if you don't see any errors, plug a monitor into the graphics card—you should see output, and have full video acceleration working on the GPU!

[^initramfs]: Since I am only using these setups for short-lived testing, I am not worried about messing up my overall Debian install (I can rebuild it quickly). I would suggest testing GPUs on a separate install of Pi OS if you have a main install that you'd like to use in production scenarios or as your main computer!

[^firmware]: In the past, I had to download a lot of extra firmware, but it seems like the firmware package in Trixie is updated to include almost all AMD GPUs now, so even a very new card like the AI Pro 9700 worked out of the box, no extra downloads needed!
