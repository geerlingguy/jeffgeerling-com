---
nid: 3401
title: "New 2GB Pi 5 has 33% smaller die, 30% idle power savings"
slug: "new-2gb-pi-5-has-33-smaller-die-30-idle-power-savings"
date: 2024-08-29T14:17:34+00:00
drupal:
  nid: 3401
  path: /blog/2024/new-2gb-pi-5-has-33-smaller-die-30-idle-power-savings
  body_format: markdown
  redirects: []
tags:
  - bcm2712
  - broadcom
  - raspberry pi
  - silicon
  - video
  - youtube
---

Raspberry Pi [launched the 2 gig Pi 5 for $50](https://www.raspberrypi.com/news/2gb-raspberry-pi-5-on-sale-now-at-50/), and besides half the RAM and a lower price, it has a new stepping of the main BCM2712 chip.

{{< figure src="./pi-5-C1-vs-D0-Stepping.jpg" alt="BCM2712 C1 vs D0 Stepping chips" width="700" height="auto" class="insert-image" >}}

This is the BCM2712 _D0_ stepping. Older Pi 5's shipped with a _C1_. In [their blog post](https://www.raspberrypi.com/news/2gb-raspberry-pi-5-on-sale-now-at-50/), they said:

> The new D0 stepping strips away all that unneeded functionality, leaving only the bits we need.

Steppings are basically chip revisions where they don't change functionality, and usually just fix bugs, or tweak the layout. But even tiny design changes could have unintended consequences. I wanted to see exactly what happens when I push one of these new chips to the limits.

First, I wanted a performance baseline, so I ran Geekbench with the latest Pi OS and all the defaults.

Except... apparently Geekbench likes more than 2 gigs of RAM. I couldn't get past the multicore Photo Filter test, since the OS kept running outta memory. A lotta software nowadays is built for an _absolute minimum_ of 4 or 8 gigs. So keep that in mind when you're buying a Pi.

{{< figure src="./pi5-geekbench6-oom.jpeg" alt="Geekbench 6 kernel Linux OOM killer" width="700" height="auto" class="insert-image" >}}

Without adding swap, Geekbench was out, but I still wanted to get some raw numbers, so I ran `sysbench`. It's lighter weight, it runs with limited memory, and it still gives me CPU numbers to compare.

Using a combination of [this 10W peltier cooler](https://amzn.to/4e2SRIv) and the bottom heatsink from an [EDAtec fanless case](https://www.digikey.com/en/products/detail/edatec/ED-PI5CASE-OB/21769666), I ran through a number of overclock scenarios:

| Clock Speed (MHz) | sysbench result |
| --- | --- |
| 2400 | 4155 |
| 3000 | 5175 |
| 3100 | 5315 |
| 3200 | 5505 |
| 3300 | 5715 |
| 3400 | 5804 |
| 3500 | 6068 |

> I ran the command `sysbench --test=cpu --cpu-max-prime=20000 --num-threads=4 run`.

At 3.6 GHz the Pi wouldn't boot—there were always memory errors and it would completely freeze. At 3.5 GHz, there were still some stability issues, and I couldn't get the Pi to reboot cleanly.

{{< figure src="./pi-5-heatsink-peltier.jpeg" alt="Pi 5 heatsink - Peltier cooling" width="700" height="auto" class="insert-image" >}}

For any speeds above 3.1 GHz, I also used my [pi-overvolt](https://github.com/geerlingguy/pi-overvolt) hack, which I cover more in depth in my blog post [Hacking Pi firmware to get the fastest overclock](/blog/2024/hacking-pi-firmware-get-fastest-overclock).

There's still a hard limit of 1.1V from the PMIC, so besides splicing in higher voltages direct into the SoC, the only other hardware-level modification I hadn't tried was delidding the Pi's processor.

_Theoretically_, this would allow the Peltier cooler to pull heat off the silicon even faster.

## Delidding

But there was another reason I wanted to delid a 2 gig Pi 5. Raspberry Pi mentioned in their blog post the D0 stepping was simpler and cheaper to make, since they removed 'dark silicon'. That just means there were portions of the BCM2712 that Broadcom put in but Raspberry Pi never used, [like the built-in Ethernet controller](https://forums.raspberrypi.com/viewtopic.php?p=2247912#p2247832). Raspberry Pi built their own Ethernet into the RP1, so they didn't use the controller in the main SoC.

What this means for the D0 is the actual CPU die is smaller. A smaller die fits more chips on a single wafer, meaning individual chips cost less, assuming chip production yields are the same.

I already have a delidded C1 chip from back [when I worked with John McMaster and Kleindiek on my Pi 5 silicon deep-dive](/blog/2024/die-shots-and-transistor-level-debugging-on-raspberry-pi-5), so I just need to delid the D0 chip.

I placed the 2 GB Pi 5 on my workbench, and worked at the corners with a razor blade:

{{< figure src="./pi-5-heatspreader-delidding-razor-blade.jpeg" alt="Pi 5 delid heat spreader with razor knife blade" width="700" height="auto" class="insert-image" >}}

The heat spreader popped off, and I took some measurements, comparing the C1 to the D0 stepping:

| Stepping | Width | Height | Die area |
| --- | --- | --- | --- |
| BCM2712 D0 | 6.30mm | 5.98mm | 37.674mm<sup>2</sup> |
| BCM2712 C1 | 6.47mm | 8.63mm | 55.836mm<sup>2</sup> |

The D0 is 32.5% smaller than the older version, which would definitely bring down the price per chip, assuming the same yield on a given silicon wafer. It seems they're still using the 16nm process node, so that's a good chunk of 'dark silicon' removed!

## Direct Die Cooling

I powered up the Pi, with the new direct-die cooling arrangement, but still had stability issues at 3.6 GHz. Maybe even a little more at 3.5, it was hard to tell.

{{< figure src="./bcm2712-bare-die-cooling.jpeg" alt="BCM2712 bare die running with no cooling" width="700" height="auto" class="insert-image" >}}

Just for fun, I pulled off the cooler entirely, and let the Pi run with just the die exposed to the air. It was happy running like this, even running sysbench at 2.8 GHz for 10 seconds without throttling.

So could you run a Pi completely naked? Sure, but the heat spreader does a good job getting more heat off the whole package, so I'd just leave it on.

My takeaway is the Pi's 16 nanometer chip seems to max out around 3.5 Gigahertz.

## Thermals and Efficiency - The Goldilocks Pi

The other big question though, is whether the smaller design is any better for efficiency or thermals.

CNX Software did some testing and [published a chart](https://www.cnx-software.com/2024/08/27/comparison-of-raspberry-pi-5-with-2gb-and-8gb-ram-hardware-benchmarks-and-power-consumption/), showing a significant difference, 2.7W to 3.5W, for idle power consumption.

I haven't done _exhaustive_ testing, but I did run through my [stress benchmarks](https://gist.github.com/geerlingguy/91d4736afe9321cbfc1062165188dda4), monitoring power and heat. I ran it on all the Pi 5 models, with identical test parameters. I have more [in this GitHub issue](https://github.com/geerlingguy/pi-overvolt/issues/4), but this chart sums it up:

| | Pi 5 2GB D0 | Pi 5 4GB C1 | 4GB Delta | Pi 5 8GB C1 | 8GB Delta |
| --- | --- | --- | --- | --- | --- |
| Idle power | 2.4W | 3.3W | **0.9W (+32%)** | 3.2W | **0.8W (+29%)** |
| Idle temp | 30°C | 32°C | **2°C (+6%)** | 32°C | **2°C (+6%)** |
| stress-ng power | 8.9W | 9.8W | **0.9W (+10%)** | 9.8W | **0.9W (+10%)** |
| stress-ng temp | 59°C | 63°C | **4°C (+7%)** | 64°C | **5°C (+8%)** |

For idle power draw, the improvement almost mirrors the chip size reduction. The chip is 33% smaller, and the idle power draw is almost that much better.

And here are the thermals for my test runs, for completeness:

{{< figure src="./pi-5-c1-vs-d0-thermals.jpg" alt="Pi 5 C1 vs D0 stepping - thermals" width="700" height="auto" class="insert-image" >}}

Some of the power savings could be chalked up to less RAM, because more RAM requires more power. But that doesn't explain all the results. Thomas Kaiser [also found the OPP tables are different with the new chip](https://www.cnx-software.com/2024/08/27/comparison-of-raspberry-pi-5-with-2gb-and-8gb-ram-hardware-benchmarks-and-power-consumption/#comment-620747). The 2 gig model doesn't need as much voltage to hit certain clocks, like it uses 805 mV at 2.1 GHz versus 850 mV for the 8 gig model.

As a final efficiency test, I ran my [top500 HPL benchmark on the 2 gig Pi 5](https://github.com/geerlingguy/top500-benchmark/issues/40). HPL is a memory-intense benchmark, and because the 2 GB model only has 2 GB of RAM, the overall efficiency for this test was worse, coming in at **2.07 Gflops/W**. The 8 GB Pi 5 gets **2.75 Gflops/W**.

For now, the biggest difference between the 2, 4, and 8 GB PI 5s for _most_ people would still be having more RAM. If you know you can run your apps in 2 GB, this is a great little Pi for that. If you can't, then I think Raspberry Pi set up the 4 GB Pi 5 as the 'goldilocks': Not too expensive, with just enough RAM for most uses.

## Conclusion

So is it worth stepping down to a 2 GB Pi 5 just to get the simpler D0 chip? No. But is it cool to have a cheaper 2 gig option exist? Yes. Just make sure you have a use case for it that doesn't need a ton of RAM.
