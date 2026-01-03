---
nid: 3390
title: "NUMA Emulation speeds up Pi 5 (and other improvements)"
slug: "numa-emulation-speeds-pi-5-and-other-improvements"
date: 2024-07-12T14:01:15+00:00
drupal:
  nid: 3390
  path: /blog/2024/numa-emulation-speeds-pi-5-and-other-improvements
  body_format: markdown
  redirects:
    - /blog/2024/numa-emulation-could-speed-pi-5-and-other-improvements
aliases:
  - /blog/2024/numa-emulation-could-speed-pi-5-and-other-improvements
tags:
  - arm64
  - kernel
  - linux
  - numa
  - patches
  - raspberry pi
  - video
  - youtube
---

Recently an Igalia engineer posted a [NUMA Emulation patch](https://lore.kernel.org/lkml/20240625125803.38038-1-tursulin@igalia.com/) for the Pi 5 to the Linux Kernel mailing list. He said it could improve performance of Geekbench 6 scores up to 6% for single-core, and 18% for multicore.

My testing didn't quite match those numbers, but I did see a significant and consistent performance increase across both Geekbench 6:

{{< figure src="./pi-5-geekbench-numa-emulation-patch-faster.jpg" alt="Raspberry Pi 5 Geekbench 6 Score comparison with NUMA Emulation enabled" width="700" height="auto" class="insert-image" >}}

And High Performance Linpack:

{{< figure src="./pi-5-hpl-numa-emulation-patch-faster.jpg" alt="Raspberry Pi 5 HPL Gigaflops and efficiency comparison with NUMA Emulation enabled" width="700" height="auto" class="insert-image" >}}

If you want to see all the gory details of my test process and setup (and how to replicate the results), check out the issue I posted to my top500 repository: [Benchmark Raspberry Pi 5 Linux kernel NUMA patch](https://github.com/geerlingguy/top500-benchmark/issues/36).

**Update August 2024**: Until this is in Pi OS proper, you can install the patch by running `sudo rpi-update pulls/6273`, see [this issue](https://github.com/raspberrypi/firmware/issues/1854#issuecomment-2265721079). You can still follow the steps below if you like, but using `rpi-update` means you don't have to recompile the kernel :)

<s>Evaluating the patch is a little involved (especially if you're not familiar with compiling the Linux kernel)</s>:

  1. [Download the .mbox file](https://lore.kernel.org/lkml/20240625125803.38038-1-tursulin@igalia.com/t.mbox.gz) for the kernel patch thread.
  1. Apply it to your [raspberrypi/linux](https://github.com/raspberrypi/linux) checkout with `git am [filename.mbox]`
  1. [Rebuild the Linux kernel](https://www.raspberrypi.com/documentation/computers/linux_kernel.html#building), ensuring NUMA Emulation is enabled in the kernel config.
  1. Add `numa=fake=4` to `/boot/firmware/cmdline.txt` before the `rootwait` option, and reboot.
  1. Prefix any commands you want to test with `numactl`, e.g.: `numactl --interleave=all ./geekbench6`. (Install `numactl` with `sudo apt install -y numactl`.)

It remains to be seen whether the patch will make it in—[similar NUMA emulation exists for x86 already](https://www.kernel.org/doc/html/v5.8/x86/x86_64/fake-numa-for-cpusets.html), so there is precedent. Otherwise Raspberry Pi could maintain the code in their own Linux fork or pull some of the memory layout changes into firmware, maybe.

## Pi 1, 3+ Efficiency gains via s2idle

Separately, Stefan Wahren posted a patch for the Raspberry Pi 1 B, 3 A+, and 3 B+, [implementing support for S2Idle on those models](https://docs.kernel.org/admin-guide/pm/sleep-states.html?highlight=s2idle#suspend-to-idle).

[Suspend-to-idle](https://docs.kernel.org/admin-guide/pm/sleep-states.html?highlight=s2idle#suspend-to-idle) is a lightweight sleep state a computer can employ to save a little juice while it's not doing much.

In the Pi's case, at least on the Pi 1 B, this results in a 23% power savings while idle:

  - running but CPU idle = 1.67 W
  - suspend to idle = 1.33 W

The patch doesn't work with reducing the USB bus power draw (due to [this issue](https://github.com/raspberrypi/firmware/issues/1894)), but if that could be solved, there may be even more upside in the future.

No word on whether this patch will make it in, but it's being actively reviewed at the time of this writing.

## A2 microSD card Command Queueing support (for 2-3x faster random access)

One thing that's actually implemented on the Pi 5 now—no need for a kernel patch review—is [A2 microSD card Command Queueing](https://forums.raspberrypi.com/viewtopic.php?t=367459).

To enable it on your Pi 5, make sure you're on the latest update, and add `dtparam=sd_cqe` to `/boot/firmware/config.txt` and reboot.

If it's working, and you have an A2 card (most older cards are either A1 or not rated at all), then you should see something like the following in `dmesg` logs:

```
mmc0: Command Queue Engine enabled, 31 tags
```

Check my [full test results here](https://github.com/geerlingguy/sbc-reviews/issues/21#issuecomment-2212599505), but here's a summary of my testing with both the Raspberry Pi Diagnostics tool:

{{< figure src="./pi-5-microsd-a2-command-queueing-iops.jpg" alt="Raspberry Pi 5 A2 Command Queueing performance comparison - IOPS" width="700" height="auto" class="insert-image" >}}

...and my own [disk-benchmark.sh](https://github.com/geerlingguy/pi-cluster/blob/master/benchmarks/disk-benchmark.sh) tool using `iozone`:

{{< figure src="./pi-5-microsd-a2-command-queueing-benchs.jpg" alt="Raspberry Pi 5 A2 Command Queueing performance comparison - Data" width="700" height="auto" class="insert-image" >}}

I have a full video on my YouTube channel going over everything in more detail, with a little more explanation, including why I haven't been able to test the NUMA emulation (which aims to be generic for all Arm devices) on Rockchip RK3588 boards:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/2ZrVyFCkOew" frameborder='0' allowfullscreen></iframe></div>
</div>
