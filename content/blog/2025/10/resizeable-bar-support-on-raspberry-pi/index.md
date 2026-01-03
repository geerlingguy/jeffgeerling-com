---
nid: 3503
title: "Resizeable BAR support on the Raspberry Pi"
slug: "resizeable-bar-support-on-raspberry-pi"
date: 2025-10-09T14:12:44+00:00
drupal:
  nid: 3503
  path: /blog/2025/resizeable-bar-support-on-raspberry-pi
  body_format: markdown
  redirects: []
tags:
  - egpu
  - gpu
  - intel
  - kernel
  - linux
  - pi os
  - raspberry pi
  - xe
---

While not an _absolute_ requirement for modern graphics card support on Linux, [Resizeable BAR](https://www.intel.com/content/www/us/en/support/articles/000090831/graphics.html) support makes GPUs go faster, by allowing GPUs to throw data back and forth on the PCIe bus in chunks larger than 256 MB.

In January, I opened an issue in the Raspberry Pi Linux repo, [Resizable BAR support on Pi 5](https://github.com/raspberrypi/linux/issues/6621).

{{< figure src="./sparkle-intel-arc-b580-on-raspberry-pi-500-plus.jpg" alt="Intel Arc B580 on Raspberry Pi 500+" width="700" height="394" class="insert-image" >}}

Unlike most PCs with a BIOS or UEFI support, the Raspberry Pi _should_ just support BAR resize by default. However, when testing Intel Xe GPU drivers (for Alchemist/Battlemage GPUs) on Raspberry Pi OS, I would get errors like:

```
# On the Arc A750
[   10.099135] xe 0000:03:00.0: [drm] Failed to resize BAR2 to 8192M (-ENOSPC). Consider enabling 'Resizable BAR' support in your BIOS

# On the Arc B580
[    4.795416] xe 0001:03:00.0: [drm] Failed to resize BAR2 to 16384M (-ENOSPC). Consider enabling 'Resizable BAR' support in your BIOS
```

After some firmware updates, Pi OS was able to structure the PCIe bus correctly, but the Intel drivers still wouldn't cleanly resize the BAR.

Through a lot of debugging between Pi OS devs (thanks _especially_ to P33M and 6by9) and the wider Pi community, we discovered a way to get resizable BAR working with the Xe drivers:

## How to enable Resizable BAR

Well, I should say 'sorta' — because for now, you have to pick a BAR size to resize to, and configure that for the Xe driver as well.

First, for reference, here's a [mapping of bit values to BAR sizes](https://angrysysadmins.tech/index.php/2023/08/grassyloki/vfio-how-to-enable-resizeable-bar-rebar-in-your-vfio-virtual-machine/) for the [`resource2_resize` option](https://github.com/torvalds/linux/commit/8bb705e3e79d84e77edd4499e74483dd96a4626c) we'll use later:

| Bit / Size | Bit / Size | Bit / Size |
| :-- | :-- | :-- |
| 1 = 2MB<br>2 = 4MB<br>3 = 8MB<br>4 = 16MB<br>5 = 32MB | 6 = 64MB<br>7 = 128MB<br>8 = 256MB<br>9 = 512MB<br>10 = 1GB | 11 = 2GB<br>12 = 4GB<br>13 = 8GB<br>14 = 16GB<br>15 = 32GB |

I chose an 8GB BAR[^bar-size], as that's what the A750 asked for in the error message (`Failed to resize BAR2 to 8192M`).

To get the resize to work (assuming you have the Xe driver already installed, which _currently_ requires a [custom kernel build on the Pi](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/695)):

  1. Blacklist the Xe driver so it won't load until the BAR has been resized: edit `/etc/modprobe.d/raspi-blacklist.conf` and add `blacklist xe`
  2. Edit `/boot/firmware/cmdline.txt`, and add `xe.vram_bar_size=8192` to the arguments
  3. Reboot the Pi
  4. Perform a manual BAR resize:

        # echo 0001:02:02.0 > /sys/bus/pci/drivers/pcieport/unbind
        # echo 0001:02:01.0 > /sys/bus/pci/drivers/pcieport/unbind
        # echo 0001:01:00.0 > /sys/bus/pci/drivers/pcieport/unbind
        # echo 13 > /sys/bus/pci/devices/0001\:00\:00.0/0001\:01\:00.0/0001\:02\:01.0/0001\:03\:00.0/resource2_resize

  5. Probe Xe: `sudo modprobe xe` (while monitoring dmesg with `dmesg --follow` in another window)

Note the function number in the first command above would be `02:04:0` for an A750, but `02:02.0` for the B580. You can see what PCI bridge devices are listed for the "Intel Corporation Device" with `lspci`.

For this to work, you also need the upstream Linux patch [Release unused bridge resources during resize](https://patchwork.kernel.org/project/linux-pci/patch/20240507213125.804474-1-alex.williamson@redhat.com/), which is accounted for in 6by9's [Testing PCIe graphics cards on Pi 5](https://github.com/raspberrypi/linux/pull/7072) pull request, which I'm now testing on my own Pi.

After doing all that, and probing `xe`, it seems to be happy with the memory layout, no longer complaining about a 'small BAR device' (the Pi's default BAR size is 256MB):

```
[  375.318614] xe 0001:03:00.0: enabling device (0000 -> 0002)
[  375.318793] xe 0001:03:00.0: [drm] unbounded parent pci bridge, device won't support any PM support.
[  375.318935] xe 0001:03:00.0: [drm] Found dg2/g10 (device ID 56a1) discrete display version 13.00 stepping C0
[  375.320059] xe 0001:03:00.0: [drm] VISIBLE VRAM: 0x0000001800000000, 0x0000000200000000
[  375.320237] xe 0001:03:00.0: [drm] VRAM[0, 0]: Actual physical size 0x0000000200000000, usable size exclude stolen 0x00000001fc000000, CPU accessible size 0x00000001fc000000
[  375.320241] xe 0001:03:00.0: [drm] VRAM[0, 0]: DPA range: [0x0000000000000000-200000000], io range: [0x0000001800000000-19fc000000]
[  375.320245] xe 0001:03:00.0: [drm] Total VRAM: 0x0000001800000000, 0x0000000200000000
[  375.320248] xe 0001:03:00.0: [drm] Available VRAM: 0x0000001800000000, 0x00000001fc000000
[  375.334678] xe 0001:03:00.0: vgaarb: VGA decodes changed: olddecodes=io+mem,decodes=none:owns=none
[  375.338149] xe 0001:03:00.0: [drm] Finished loading DMC firmware i915/dg2_dmc_ver2_08.bin (v2.8)
[  375.343724] xe 0001:03:00.0: [drm] GT0: Using GuC firmware from i915/dg2_guc_70.bin version 70.49.4
...
```

See [this comment](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/695#issuecomment-3382389401) for more details and logs.

## Automating the resize

It's quite annoying to have to enter all those commands on every boot. So instead, user [RSC-Games posted a systemd unit](https://github.com/raspberrypi/linux/issues/6621#issuecomment-3382654892) to do it automatically.

Create a script in `/usr/bin/bar_resize.sh`:

```
#!/usr/bin/env bash
# Note: This script could be a bit more automatic, detecting the proper card or just bailing out
# if no card is identified. I leave that as an exercise for the person copying and pasting it ;)
echo 0001:02:02.0 > /sys/bus/pci/drivers/pcieport/unbind
echo 0001:02:01.0 > /sys/bus/pci/drivers/pcieport/unbind
echo 0001:01:00.0 > /sys/bus/pci/drivers/pcieport/unbind
echo 13 > /sys/bus/pci/devices/0001\:00\:00.0/0001\:01\:00.0/0001\:02\:01.0/0001\:03\:00.0/resource2_resize
modprobe xe
```

(Note: Set `02:04.0` for the A750, or `02:02.0` for B580, and change `13` according to your target BAR resize.)

Make sure that script is executable (`sudo chmod +x /usr/bin/bar_resize.sh`), then create a systemd unit file in `/etc/systemd/system/resize-bar.service`:

```
[Unit]
Description=Resize the BAR allocation and manually load the Xe driver.

[Service]
Type=oneshot
ExecStart=/usr/bin/bar_resize.sh

[Install]
WantedBy=basic.target
```

Then enable the unit:

```
sudo systemctl enable resize-bar.service
```

You still have to add the `/boot/firmware/cmdline.txt` change manually (`xe.vram_bar_size=8192`), and make sure `blacklist xe` is in the `/etc/modprobe.d/raspi-blacklist.conf` file.

**NOTE**: If you're going to swap out AMD cards or not use the Intel card for a while, be sure to back out the changes, and disable the service (`sudo systemctl disable resize-bar.service`).

## Conclusion

{{< figure src="./intel-b580-on-pi-500-plus-llm-running.jpg" alt="Intel B580 on Pi 500+ running an LLM with llama.cpp" width="700" height="394" class="insert-image" >}}

We're getting close to full Intel eGPU support on the Pi—[AMD eGPUs have been stable since late last year](/blog/2024/use-external-gpu-on-raspberry-pi-5-4k-gaming), and are even _more so_ after yanghaku [submitted a much simpler patch](https://github.com/geerlingguy/raspberry-pi-pcie-devices/discussions/756) which has a good shot at being [merged into Pi OS's linux kernel](https://github.com/raspberrypi/linux/pull/7072)! See [my latest eGPU test results here](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/764).

[^bar-size]: I also tested a 16GB BAR on my 16 GB model Pi 500+ with the B580, but got an error `echo: write error: No space left on device` when I tried that. I assumed BAR sizes can be larger than the on-device RAM, but maybe that assumption is wrong? That also led me to research why a card with only 12GB of VRAM is requesting a 16GB BAR, and as far as I can tell, it has something to do with potential uses like [SR-IOV](https://en.wikipedia.org/wiki/Single-root_input/output_virtualization) where multiple VMs could access a single device, thus requiring more BAR space for the physical device being shared... BAR is still a little bit of a mystery to me.
