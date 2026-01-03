---
nid: 3327
title: "A PCIe Coral TPU FINALLY works on Raspberry Pi 5"
slug: "pcie-coral-tpu-finally-works-on-raspberry-pi-5"
date: 2023-11-17T19:03:27+00:00
drupal:
  nid: 3327
  path: /blog/2023/pcie-coral-tpu-finally-works-on-raspberry-pi-5
  body_format: markdown
  redirects: []
tags:
  - ai
  - coral
  - machine learning
  - pcie
  - raspberry pi
  - tpu
---

[Coral.ai TPUs](https://coral.ai/products/) are AI accelerators used for tasks like machine vision and audio processing. Raspberry Pis are often integrated into small robotics and IoT products—or used to analyze live video feeds with [Frigate](https://frigate.video).

Until today, nobody I know of has been able to get a PCI Express Coral TPU working on the Raspberry Pi. The Compute Module 4, unfortunately, had some quirks in its PCIe implementation, preventing the use of the Coral over PCIe.

{{< figure src="./google-coral-tpu-pcie-raspberry-pi-5.jpg" alt="Google Coral TPU running over PCIe on Raspberry Pi 5" width="700" height="auto" class="insert-image" >}}

The Raspberry Pi 5 has a much improved PCIe bus—capable of reaching Gen 3 speeds even!—and I've already tested the [first PCIe NVMe HATs for Pi 5](https://www.youtube.com/watch?v=EXWu4SUsaY8).

So can the Pi 5 handle the Coral TPU natively over PCIe?

_Yes_. Though currently, you need to tweak a few things to get it working.

## PCIe bringup for Coral TPU on Pi 5

Buckle up, to get the TPU working, we are going to need to overcome some hurdles:

  - Coral's drivers only work on 4K page size, so we need to switch from the default Pi kernel
  - The Coral is a bit picky with PCIe timings, so (for now at least) we need to disable [PCIe ASPM](https://wiki.archlinux.org/title/Power_management#Active_State_Power_Management)
  - The Pi's default device tree sets up the PCIe bus to not have enough MSI-X interrupts, so we need to change it
  - Pi OS 12 'Bookworm' ships with Python 3.11, but Coral's PyCoral library only runs on 3.9, so we need to run inside Docker (or install an alternate system-wide Python version)
  - There's no A+E key adapter/HAT for the Raspberry Pi (yet), so we need a hardware interface to plug the Coral TPU into the Pi 5's PCIe header

### Pi Config Changes

Some of the changes required to get the Coral working are pretty easy—changing some configuration and rebooting.

First, to switch from the default 16k page size to 4k pages (confirm which kernel you're running with `uname -a`), you can add the line `kernel=kernel8.img` to the bottom of your `/boot/firmware/config.txt` file.

Then, to enable the external PCI Express connector, add the following two lines to the same file (again, at the bottom):

```
dtparam=pciex1
dtparam=pciex1_gen=2
```

Note that I tested with Gen 1, 2, and 3—the TPU was functional at all three speeds, but I had a few link errors (that did not cause any noticeable problems) at Gen 3 with my own setup.

The final configuration change is disabling ASPM for PCI Express devices—this might not be _absolutely_ necessary, but it does clear up some noisy link error correction messages in the system logs.

Edit `/boot/firmware/cmdline.txt` and in the configuration line, add in `pcie_aspm=off` somewhere (I added it prior to `rootwait`.

Save that file and the config.txt changes and reboot, and you can confirm the kernel was switched by running `uname -a`:

```
pi@pi5:~ $ uname -a
Linux pi5 6.1.0-rpi4-rpi-v8 #1 SMP PREEMPT Debian 1:6.1.54-1+rpt2 (2023-10-05) aarch64 GNU/Linux
```

Yours will look a little different, but the key there is to see the `-v8` at the end of the kernel version string.

### Device Tree Change

This next bit is slightly more complicated, as most Raspberry Pi owners don't mess around with Device Trees (the little files that describe the hardware to Linux), but it's not so bad.

In fact, I have a guide for the process on this very blog: [How to customize the dtb (device tree overlay) on the Raspberry Pi](https://www.jeffgeerling.com/blog/2023/how-customize-dtb-device-tree-overlay-on-raspberry-pi).

In fact, the exact steps for modifying the PCIe bus to use the correct `msi-parent` value is shown in that blog post—so follow it to make the correct change.

Why switch the value? See [this post from jdb on the Pi forums](https://forums.raspberrypi.com/viewtopic.php?p=2157674#p2157674).

### Python 3.9 inside Docker

The last step—assuming you have the hardware to connect up a PCIe Coral TPU to the Pi 5's PCIe connector (more on that later)—is to install Docker and run the PyCoral library inside a Debian 10 Docker container, which is much quicker and easier than trying to get PyCoral installed on the system Python on Debian 12.

And wouldn't you know? I have a guide for how to do _exactly that_ elsewhere on this blog: [Testing the Coral TPU Accelerator (M.2 or PCIe) in Docker](/blog/2023/testing-coral-tpu-accelerator-m2-or-pcie-docker)

Follow the [Python 3.10 and 3.11 support](https://github.com/google-coral/pycoral/issues/85) issue on the PyCoral GitHub for any updates about getting it installed on the version of Python that ships with the latest Pi OS.

### Physically Plugging in a Coral TPU to the Raspberry Pi 5

Right now, unfortunately, there are no commercially-available Pi 5 HATs or adapter boards that go from the proprietary PCIe FFC connector on the Raspberry Pi 5 to either a standard PCIe slot, or to an A+E key M.2 connector.

I am certain both of those will exist at some point (hopefully soon!), but for now, your best bet is to order a [HatDrive! Top or Bottom](https://pineberrypi.com/products/hat-top-2230-2240-for-rpi5) from Pineberry Pi and then order a PCIe M.2 M-key to A+E key adapter. Or use the Coral B+M key module with the 'Bottom' version (since it's 2280-size, and won't fit in the 'Top' HAT).

For my own testing, I've been using a prototype board that Mirkotronics / Pineberry Pi sent called 'uPCity'. I am hoping they can sell a version of that board at some point, because it is extremely fun to mess around with [so many different PCI Express devices](https://pipci.jeffgeerling.com) on the Raspberry Pi 5!

## Conclusion

Once everything is wired up, and you [install the `apex` PCIe driver](https://coral.ai/docs/m2/get-started)—and can see `/dev/apex_0`—you could run an image classification example inside the edgetpu examples repo. Give it an image of this bird:

{{< figure src="./edgetpu-bird.jpg" alt="Coral Edge TPU Example Bird image" width="512" height="auto" class="insert-image" >}}

And then it should spit out:

```
root@7bb44c28f378:~# python3 /usr/share/edgetpu/examples/classify_image.py --model /usr/share/edgetpu/examples/models/mobilenet_v2_1.0_224_inat_bird_quant_edgetpu.tflite --label /usr/share/edgetpu/examples/models/inat_bird_labels.txt --image /usr/share/edgetpu/examples/images/bird.bmp
---------------------------
Poecile atricapillus (Black-capped Chickadee)
Score :  0.44140625
---------------------------
Poecile carolinensis (Carolina Chickadee)
Score :  0.29296875
```
