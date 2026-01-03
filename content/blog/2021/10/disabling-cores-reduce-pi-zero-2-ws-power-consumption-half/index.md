---
nid: 3137
title: "Disabling cores to reduce the Pi Zero 2 W's power consumption by half"
slug: "disabling-cores-reduce-pi-zero-2-ws-power-consumption-half"
date: 2021-10-28T16:40:09+00:00
drupal:
  nid: 3137
  path: /blog/2021/disabling-cores-reduce-pi-zero-2-ws-power-consumption-half
  body_format: markdown
  redirects:
    - /blog/2021/reducing-pi-zero-2-ws-power-consumption-x
aliases:
  - /blog/2021/reducing-pi-zero-2-ws-power-consumption-x
tags: []
---

By default, the new Pi Zero 2 W (see my [Zero 2 W review here](https://www.youtube.com/watch?v=lKS2ElWQizA)) runs a 4-core ARM Cortex A53 CPU at 1 GHz.

{{< figure src="./pi-zero-2-chip-bga-ballout-pi-logo.jpg" alt="Raspberry Pi Zero 2 W BGA Xray pattern with mini Raspberry Pi Logo" width="600" height="600" class="insert-image" >}}

If you haven't seen my full blog post exploring the Zero 2 W from the inside, complete with X-ray imagery—[go check it out now](/blog/2021/look-inside-raspberry-pi-zero-2-w-and-rp3a0-au)!

From my review, I found that the Zero 2 uses 100 mA at idle (compared to 80 mA for the single-core Pi Zero W that preceded it), but will use up to 500 mA full-tilt, when all four CPU cores are maxed out.

For many users of the Zero 2, this is no problem, as the extra multicore performance is worth it. But a few people asked whether disabling cores could save energy in situations where the software running on the Zero 2 wasn't multithreaded or didn't need multiple CPU cores to run effectively.

So I tried it! Booting up a fresh instance of 32-bit Pi OS, I checked on the cores:

```
pi@zero:~ $ lscpu
Architecture:        armv7l
Byte Order:          Little Endian
CPU(s):              4
On-line CPU(s) list: 0-3
Thread(s) per core:  1
Core(s) per socket:  4
Socket(s):           1
Vendor ID:           ARM
Model:               4
Model name:          Cortex-A53
Stepping:            r0p4
CPU max MHz:         1000.0000
CPU min MHz:         600.0000
BogoMIPS:            38.40
Flags:               half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm crc32
```

Running `stress-ng -c 4` yielded anywhere between 370-460 mA of power consumption, measured by my [PowerJive USB power meter](https://amzn.to/3jGybMX)—translating to about 2.3W of power usage.

I tried disabling core 3, by running `echo 0 > /sys/devices/system/cpu/cpu3/online` as root, but got:

```
root@zero:/home/pi# echo 0 > /sys/devices/system/cpu/cpu3/online
bash: /sys/devices/system/cpu/cpu3/online: Permission denied
```

So next, I tried using [the `maxcpus` option](https://www.kernel.org/doc/html/latest/admin-guide/kernel-parameters.html) in the kernel command line. I edited the `/boot/cmdline.txt` file and added `maxcpus=1` after `console=tty1`, then saved the file and rebooted.

Upon rebooting, I noticed there was only one Raspberry Pi instead of the customary 4 on the HDMI output—a good sign if any!

{{< figure src="./raspberry-pi-single-pi-logo.jpeg" alt="Raspberry Pi boot logo showing one processor core" width="640" height="427" class="insert-image" >}}

I logged in and checked:

```
pi@zero:~ $ lscpu
Architecture:         armv7l
Byte Order:           Little Endian
CPU(s):               4
On-line CPU(s) list:  0
Off-line CPU(s) list: 1-3
Thread(s) per core:   1
Core(s) per socket:   1
Socket(s):            1
Vendor ID:            ARM
Model:                4
Model name:           Cortex-A53
Stepping:             r0p4
CPU max MHz:          1000.0000
CPU min MHz:          600.0000
BogoMIPS:             64.00
Flags:                half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm crc32
```

So it looks like that worked! Now, I tried running `stress-ng` again, and sure enough, the power consumption averaged 200 mA (less than half of the 4-core reading), spiking only as high as 260 mA, so less than 1.3W.

{{< figure src="./200ma-raspberry-pi-zero-2-disabled-cpu-cores.jpeg" alt="200ma Raspberry Pi Zero 2 with disabled CPU cores power savings" width="640" height="427" class="insert-image" >}}

I still couldn't manually bring a core online or offline as root, so it looks like you can only manage them via the kernel `cmdline.txt` options at boot.

I ran the `pts/encode-mp3` test that's part of the Phoronix suite, to see if the performance would match my previous run, and since it's basically a single-threaded test, it did:

{{< figure src="./mp3-encode-zero-2-single-core.jpg" alt="MP3 encode benchmark with single-threaded Phoronix text on Pi Zero 2 W with cores disabled" width="700" height="368" class="insert-image" >}}

So there you have it—with the Pi Zero 2 W, you can reduce power consumption if you don't _need_ to use multiple cores for your project, by disabling them.
