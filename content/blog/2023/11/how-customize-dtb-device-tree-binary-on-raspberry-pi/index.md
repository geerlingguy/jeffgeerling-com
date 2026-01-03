---
nid: 3326
title: "How to customize the dtb (device tree binary) on the Raspberry Pi"
slug: "how-customize-dtb-device-tree-binary-on-raspberry-pi"
date: 2023-11-17T17:24:46+00:00
drupal:
  nid: 3326
  path: /blog/2023/how-customize-dtb-device-tree-binary-on-raspberry-pi
  body_format: markdown
  redirects:
    - /blog/2023/how-customize-dtb-device-tree-overlay-on-raspberry-pi
aliases:
  - /blog/2023/how-customize-dtb-device-tree-overlay-on-raspberry-pi
tags:
  - device tree
  - dtb
  - hardware
  - kernel
  - linux
  - open source
  - pcie
  - raspberry pi
---

Every so often, when you're debugging weird hardware issues on SBCs like the Raspberry Pi, it's useful to get way down into the guts of how the Pi represents its hardware to Linux.

And the Linux kernel uses a method called [Device Tree](https://www.kernel.org/doc/html/latest/devicetree/usage-model.html) overlays to do it. On the Pi 5 (and other Pis), these overlays are stored as `.dtb` files inside the `/boot/firmware` directory, and there's an overlay for every major Raspberry Pi hardware model.

I've had to modify the `dtb` files in the past to [increase the PCIe BAR space](https://gist.github.com/geerlingguy/9d78ea34cab8e18d71ee5954417429df) for early GPU testing on the Compute Module 4. And recently I've had to [mess with how the PCIe address space is set up](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/44#issuecomment-1816810789) for testing certain devices on the Raspberry Pi 5.

The problem is, you can't just hand-edit a .dtb file—they're in a format readable only by the Linux kernel. You have to decompile the .dtb file to a .dts (source) file, edit it, then recompile it to a .dtb.

As an example, I needed to change the `msi-parent` for the Pi 5's external PCIe connector to allow for full MSI-X support for a Google Coral TPU (work on getting it to work is [ongoing](https://pipci.jeffgeerling.com/cards_m2/coral-accelerator-ae-key.html)):

```
# Back up the current dtb
sudo cp /boot/firmware/bcm2712-rpi-5-b.dtb /boot/firmware/bcm2712-rpi-5-b.dtb.bak

# Decompile the current dtb (ignore warnings)
dtc -I dtb -O dts /boot/firmware/bcm2712-rpi-5-b.dtb -o ~/test.dts

# Edit the file
nano ~/test.dts

# Change the line: msi-parent = <0x2f>; (under `pcie@110000`)
# To: msi-parent = <0x66>;
# Then save the file.

# Recompile the dtb and move it back to the firmware directory
dtc -I dts -O dtb ~/test.dts -o ~/test.dtb
sudo mv ~/test.dtb /boot/firmware/bcm2712-rpi-5-b.dtb
```

Check out elinux's [Device Tree Reference](https://elinux.org/Device_Tree_Reference) for more useful background info.

I consider myself an absolute noob at Device Trees in Linux... but I've now done this enough times that I'd like a simple reference and most of the ones out there assume you are an expert-level wizard in all things Linux/hardware!
