---
nid: 3422
title: "Raspberry Pi CM5 is 2-3x faster, drop-in upgrade (mostly)"
slug: "raspberry-pi-cm5-2-3x-faster-drop-upgrade-mostly"
date: 2024-11-27T08:00:12+00:00
drupal:
  nid: 3422
  path: /blog/2024/raspberry-pi-cm5-2-3x-faster-drop-upgrade-mostly
  body_format: markdown
  redirects:
    - /blog/2024/raspberry-pi-cm5-2-3x-faster-drop-cm4-upgrade-mostly
aliases:
  - /blog/2024/raspberry-pi-cm5-2-3x-faster-drop-cm4-upgrade-mostly
tags:
  - cm5
  - compute module
  - raspberry pi
  - video
  - youtube
---

{{< figure src="./cm5-angle.jpeg" alt="Raspberry Pi Compute Module 5" width="700" height="auto" class="insert-image" >}}

The Raspberry Pi [Compute Module 5](http://raspberrypi.com/products/compute-module-5/) is smaller than a credit card, and I already have it gaming in 4K with an eGPU, running a Kubernetes cluster, and I even upgraded my NEC Commercial display from a CM4 to CM5, just swapping the Compute Modules!

The Compute Module 4 was hard to get for _years_. It launched right after the COVID supply chain crisis, leading to insane scalper pricing.

It was so _useful_, though, that Raspberry Pi sold every unit they made, and they're inside _everything_: from [commercial 3D printers](https://youtu.be/cbm03jtWWL0?t=2851), to [TVs](https://www.jeffgeerling.com/blog/2022/tv-thats-not-necs-pi-powered-55-display), to [IP KVM cards](https://pipci.jeffgeerling.com/boards_cm/blikvm-pci-express-card.html).

After [pre-announcing the CM5](https://www.youtube.com/watch?v=Lky4FSfbc1E) earlier this year, the biggest question was, is it a drop-in replacement?

Yes. _For the most part._

I've been testing it in _tons_ of Compute Module boards, and it's been awesome seeing a 2-3x speedup just dropping in the new module.

It boots up in seconds, it has USB 3 instead of USB 2, and it's compatible with PCIe Gen 3 instead of Gen 2. The CPU is 2-3x faster, RAM is _3-4x_ faster, _WiFi_'s faster, storage is faster... It's basically a Pi 5, but without the plugs. Most CM4 cases and accessories still work with it, just there's a LOT more bandwidth.

The big advantage to a Compute Module versus a Pi 5 is modularity. And I published a video today going over a ton of use cases enabled by various Compute Module carrier boards. All the ones I've tested were built for the CM4, but the CM5 is an instant drop-in upgrade:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/X4blR5Ua3S0" frameborder='0' allowfullscreen></iframe></div>
</div>

I won't cover the individual use cases in this blog post. Rather, I'll focus on CM5 benchmarking and my notes from using the hardware a few weeks.

{{< figure src="./CM5-Pricing-Table.png" alt="CM5 Launch Pricing Table" width="700" height="auto" class="insert-image" >}}

The second-most-asked question is how much it will cost. Put simply, the 8GB CM5 is roughly the same price as the 8GB CM4. The 4GB module is $5 more, and the 2GB module is $10 more. So the cheapest CM5 is now $45 instead of $35—they're dropping the 1GB option from the lineup this generation. For any specific pricing information, please consult the [CM5 Product Brief](https://datasheets.raspberrypi.com/cm5/cm5-product-brief.pdf).

## Performance

Good news: you can expect almost all the same numbers as a Pi 5 with the same amount of RAM.

Raspberry Pi made some quality of life improvements for management, too:

  - You can edit the EEPROM (e.g. to change the `BOOT_ORDER`) without needing another computer
  - Raspberry Pi maintains [pi-gen-micro](https://github.com/raspberrypi/pi-gen-micro) to build smaller custom Pi OS installations

{{< figure src="./Benchmarks-CM5.001.boot_.png" alt="CM5 Benchmark - Boot time" width="700" height="auto" class="insert-image" >}}

Right off the bat, the most refreshing difference is it boots up about 4 seconds faster.

{{< figure src="./Benchmarks-CM5.002.hpl_.png" alt="CM5 Benchmark - HPL Linpack FP64" width="700" height="auto" class="insert-image" >}}

{{< figure src="./Benchmarks-CM5.003.hpl-efficiency.png" alt="CM5 Benchmark - HPL Efficiency" width="700" height="auto" class="insert-image" >}}

Once it's running, the CPU is almost 3x faster. And it's also about 1.5x more efficient, according to my High Performance Linpack tests.

{{< figure src="./Benchmarks-CM5.004.linux_.png" alt="CM5 Benchmark - Linux compile" width="700" height="auto" class="insert-image" >}}

And of course, I had to test recompiling the Linux kernel. The CM5 obliterates the CM4, it's more than 3x faster.

{{< figure src="./Benchmarks-CM5.005.x264-4k.png" alt="CM5 Benchmark - x264 4K Transcode" width="700" height="auto" class="insert-image" >}}

{{< figure src="./Benchmarks-CM5.006.x264-1080p.png" alt="CM5 Benchmark - x264 1080p Transcode" width="700" height="auto" class="insert-image" >}}

Video encoding is also about 3x faster. I tested x264 transcoding both at 4K and 1080p resolutions, using Phoronix. All these benchmarks are helped by the faster LPDDR4x RAM on the CM5, which I tested using tinymembench:

{{< figure src="./Benchmarks-CM5.007.ram_.png" alt="CM5 Benchmark - RAM speed" width="700" height="auto" class="insert-image" >}}

But all these speedups consume more power, at least at full blast: the CM5 uses almost _twice_ the power flat out. But at idle, the CM5 uses a tiny bit _less_: I measured 2.3 watts at the wall:

{{< figure src="./Benchmarks-CM5.008.power_.png" alt="CM5 Benchmark - Power consumption" width="700" height="auto" class="insert-image" >}}

And if you're deciding on which CM5 to buy, more RAM is better, at least if you're looking for raw performance.

{{< figure src="./Benchmarks-CM5.009.hpl-cm5.png" alt="CM5 Benchmark - HPL on various RAM capacities" width="700" height="auto" class="insert-image" >}}

You can save some money with less RAM, but don't expect the performance numbers on a 2 gig model to match the 8 gig model.

{{< figure src="./Benchmarks-CM5.010.igpu_.png" alt="CM5 Benchmark - iGPU GLMark2 V3D performance" width="700" height="auto" class="insert-image" >}}

The built-in graphics are much faster, too. Just testing with GLMark I saw the score jump from about 750 to 1916. It's not nearly as fast as even an older graphics card, but any improvement is welcome, especially for things like 4K displays.

You might've noticed, there was a third module in most of these graphs, except that last one. That's _another_ CM5, [this one being made by Radxa](https://radxa.com/products/cm/cm5/). It uses a Rockchip RK3588S2, which is a monster in its own right, beating the Pi on _almost_ every benchmark, including efficiency.

The elephant in the room is all the Compute Module clones. Because of the Pi shortages, every SBC maker on the planet built their own Compute Module. Though... some work better than others. A lot are _faster_ than the Pi, but pricing is fairly similar, when you compare RAM and relative performance.

The big difference between the Pi and all the others, though, is support. I've written how other SBCs _could_ become Pi-killers—I mean the hardware is often there—but they lack _support_.

{{< figure src="./compute-module-5-clones.jpg" alt="Compute Module 5 and Clones" width="700" height="auto" class="insert-image" >}}

One big part of that is the breadth of options for the Pi, which may or may not work on other Compute Modules. And if you want to try, you can expect to debug hardware and OS issues yourself. Like I couldn't get a valid GLMark score for the Radxa, because I couldn't get an OS image to boot and use the built-in Mali GPU in time for this post! It's often a frustrating experience.

I regularly test other Compute Modules, though, and I post _all_ my test data and experiences in my [sbc-reviews GitHub repo](https://github.com/geerlingguy/sbc-reviews).

## Hardware - CM5 IO Board

{{< figure src="./cm5-io-board.jpeg" alt="CM5 IO Board" width="700" height="auto" class="insert-image" >}}

Along with the CM5, Raspberry Pi's selling an updated IO board, for $20, with a few helpful changes. First, a power button, with the same behavior as the Pi 5. This would've saved _so_ much time debugging graphics cards on the CM4.

Then, there's a new tiny fan header, the same one on the Raspberry Pi 5. Companies like EDAtec already have active coolers for the CM5, and I'll test some cooling options on my my 2nd channel, Level2Jeff.

On the port side, they got rid of the 12 volt barrel jack for power, and now they just use USB-C. They dropped down to two multipurpose Camera/Display ports. Each one has 4 lanes of MIPI bandwidth, just like the Pi 5.

There are still two full-size HDMI ports, an Ethernet port, and two USB type-A ports, but these are upgraded to USB 3. There's a microSD card that only works on Lite Compute Modules without eMMC, and finally an M.2 slot, with a little LED that blinks when you're using an SSD.

This is nice, because probably 99% of people buying these things would plug in storage. On the CM4, you had to use an awkward adapter card, but that's not required anymore.

Maybe we could see this on the Pi 5 someday? Or if not, maybe we could hack it using the Compute Module! That's foreshadowing...

## Hardware - CM5

{{< figure src="./cm5-memory-emmc-silkscreen.jpeg" alt="CM5 Silkscreen - RAM and eMMC options" width="700" height="auto" class="insert-image" >}}

The feature that'll make the biggest impact for _me_, since I use a lotta compute modules, is this new silkscreen up in the top corner. It has resistors for the RAM and storage sizes, so the specs are right up top.

The major changes from the CM4 include:

  - BCM2712 D0 stepping SoC, with 4x Cortex A76 CPU cores at 2.4 GHz
  - RP1 chip for IO expansion (GPIO, MIPI Camera/Display, 2x USB 3.0 bus, Ethernet)
  - eMMC storage is moved to the bottom of the Compute Module
  - The Wireless chip has been raised up onto a short PCB mezzanine (I believe it can be had separately now, for system integrators, maybe?)
  - The RAM is now an LPDDR4x RAM module, sporting much higher speeds (and on-chip ECC)
  - The Pi 5 PMIC is included on the CM5 board, for USB-C PD negotation or direct 5V input like on the Pi 5

Other things are familiar, like the switchable PCB antenna / u.fl connector, the 2x 200-pin hirose board to board connections, and the Broadcom BCM54210PE (which [enables hardware PTP timestamping support](/blog/2022/ptp-and-ieee-1588-hardware-timestamping-on-raspberry-pi-cm4)).

I've been testing the CM5 on various carrier boards, even with eGPUs and 10 Gbps NICs on the official IO Board, and all that testing can be seen in [my YouTube video on the CM5](https://www.youtube.com/watch?v=X4blR5Ua3S0).

## Conclusion

{{< figure src="./cm5-compute-blade.jpeg" alt="CM5 in Compute Blade" width="700" height="auto" class="insert-image" >}}

But tying up the CM5, Raspberry Pi kept the price the same for the 8 gig model; those start at $75 for the Lite version. For 4 gig, they're going up five bucks, and for 2 gig, it's up 10 bucks, from $35 to $45.

They're dropping the 1 gig model from the lineup, and in reality, a lotta applications choke with less than 2 gigs of RAM, so I'm not surprised.

When the Compute Module 4 came out, it changed _literally_ everything about the Compute Module. Including the form factor. That meant everything built for the CM1 and CM3 had to be redesigned, and it made many hardware developers angry.

Luckily, this time they kept the form factor, meaning for _most_ things, it's a drop-in upgrade, where you get 2-3x faster performance, and at least for the larger models, the same price.
