---
nid: 3424
title: "Raspberry Pi boosts Pi 5 performance with SDRAM tuning"
slug: "raspberry-pi-boosts-pi-5-performance-sdram-tuning"
date: 2024-12-02T17:19:21+00:00
drupal:
  nid: 3424
  path: /blog/2024/raspberry-pi-boosts-pi-5-performance-sdram-tuning
  body_format: markdown
  redirects:
    - /blog/2024/raspberry-pi-5-adds-more-performance-better-sdram-tuning
aliases:
  - /blog/2024/raspberry-pi-5-adds-more-performance-better-sdram-tuning
tags:
  - benchmarking
  - hacks
  - memory
  - overclock
  - performance
  - pi 5
  - raspberry pi
---

**tl;dr** Raspberry Pi engineers tweaked SDRAM timings and other memory settings on the Pi, resulting in a 10-20% speed boost at the default 2.4 GHz clock. I of course had to test overclocking, which got me a _32%_ speedup at 3.2 GHz! Changes may roll out in a firmware update for all Pi 5 and Pi 4 users soon.

{{< figure src="./pi-5-overclock-desk-mess.jpeg" alt="Raspberry Pi 5 with SDRAM tweaks applied on desk" width="700" height="auto" class="insert-image" >}}

My quest for the [world record Geekbench 6 score on a Pi 5](https://browser.geekbench.com/v6/cpu/search?dir=desc&q=Raspberry+Pi+5+Model+B&sort=score) continues, as a couple months ago [Martin Rowan](https://www.martinrowan.co.uk/2024/09/raspberry-pi-5-overclocking-to-beat-geekbench-record/) used cooling and [NUMA emulation tricks](/blog/2024/numa-emulation-speeds-pi-5-and-other-improvements) to beat my then-record score.

But Raspberry Pi's engineers are [tweaking memory timings even further](https://forums.raspberrypi.com/viewtopic.php?t=378276). They've talked to Micron and implemented a number of small tweaks that—along with NUMA emulation—really add up to a performance improvement for multi-core workloads. And even a little improvement for single-core!

> The sdram refresh interval is currently using the default data sheet settings. You can actually monitor the temperature of the sdram and it reports if refresh at half or quarter the rate can be done. That allows the overhead due to refresh to be reduced by a half or a quarter which does improve benchmark results.
>
> We got in contact with Micron, and there is good news. They have said they actually test their 8GB sdram with the 4GB refresh rate timing (rather than the slower jedec timings), and so it was be safe to run the 8GB parts with 4GB timing.

The tweaks can also give the Pi 4 a boost, but the Pi 5 improves more dramatically:

> Pi 5 also has faster sdram, better access to sdram (i.e. wider/faster internal buses), so generally the improvements with NUMA are greater.

## SDRAM Tweaks

To get the latest RAM speedups _for now_ (this may be default soon):

  1. Update the Pi's firmware to the latest version: `sudo rpi-update` (confirm with `Y`)
  2. Edit the bootloader config: `sudo rpi-eeprom-config -e`
  3. Add the configuration `SDRAM_BANKLOW=1` (for Pi 5... for Pi 4, use `3`)
  4. Reboot

## NUMA Emulation

Since my [first post on NUMA emulation on the Pi 5](/blog/2024/numa-emulation-speeds-pi-5-and-other-improvements), the patches required have been added to Raspberry Pi's OS kernel.

So to use NUMA, all you have to do is make sure you're on the latest Pi OS (e.g. `sudo apt full-upgrade`).

To check if NUMA emulation is working, run `dmesg | grep NUMA` and make sure it says something like `mempolicy: NUMA default policy overridden to 'interleave:0-7'`. You can tweak the settings if you want by adding `numa=fake=[n]` inside `/boot/firmware/cmdline.txt`, though the defaults _should_ be appropriate for most use cases.

If you see a message like `Unknown kernel command line parameters numa_policy=interleave numa=fake=8` in your `dmesg` output, you may be running an older kernel, or if you're running a custom Linux kernel, make sure you have NUMA emulation configured in the kernel config options.

## Overclocking

Following my own guide for [overclocking the Pi 5](/blog/2023/overclocking-and-underclocking-raspberry-pi-5), I set the following inside `/boot/firmware/config.txt`:

```
over_voltage_delta=72000
arm_freq=3200
gpu_freq=1000
```

After rebooting, I set the fan to 100%, [hacked the kernel with my pi-overvolt project](https://github.com/geerlingguy/pi-overvolt) to boost the core voltage, and set the scaling governor to `performance`:

```
$ pinctrl FAN_PWM op dl
$ cd pi-overvolt && sudo ./removelimit && vcgencmd cache_flush
$ echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
```

## Geekbench World Record, Part 2

With just the default firmware changes, my Geekbench scores already increase quite a bit (+8% single, +18% multi). Adding a 3.2 GHz overclock on top (using my [pi-overvolt](https://github.com/geerlingguy/pi-overvolt) hack to boost voltages), those increases go to +32% single, +31% multi, resulting in yet [another world-record Geekbench 6 score](https://browser.geekbench.com/v6/cpu/search?dir=desc&q=Raspberry+Pi+5+Model+B&sort=score)!

| Geekbench Result | [Pi 5 - defaults](https://browser.geekbench.com/v6/cpu/9130658) | [SDRAM + NUMA](https://browser.geekbench.com/v6/cpu/9202663) | [3.2 GHz OC](https://browser.geekbench.com/v6/cpu/9204206) |
| --- | --- | --- | --- |
| Single | 833 | 899 (+8%) | 1153 (+32%) |
| Multi | 1805 | 2169 (+32%) | 2468 (+31%) |

I also ran these tests with just an [Argon THRML 30-AC Active Cooler](https://amzn.to/3OAkUo7). To try to keep temps under control, I boosted the fan speed to 100%: `pinctrl FAN_PWM op dl`.

> **A word on overclocking**: I've now overclocked around 20 Pi 5s, and found most to be capable of 2.6 or 2.8 GHz, and many (about half) to be capable of 3.0 GHz. But beyond that, very few can hit 3.1 GHz or beyond. More exotic overclocking (to 3.4 or 3.5 GHz) is much more difficult, and I've only had _one_ Pi 5 that even boots reliably at those speeds, with more extensive cooling. RAM timings were already not happy at those speeds, and with the extra SDRAM tweaks, I imagine extreme overclocking will be even _more_ unstable.

## Conclusion

These optimizations could become default soon. I started looking into this after someone on Twitter mentioned seeing [Pi 500 Geekbench results](https://browser.geekbench.com/search?page=2&q=raspberry+500) starting in September—all seemingly with these tweaks in place already!

Memory speed has been a thorn in the Pi 5's side in comparison to many RK3588 boards. It's nice to see the SDRAM tweaks giving it a significant speed boost, over a year post-launch.

And eagle-eyed readers may note I only overclocked to 3.2 GHz instead of 3.4 GHz this time. I'll leave the door open for someone else to combine all the above tricks to hit another new WR score ;)
