---
nid: 2833
title: "Raspberry Pi 3 B+ Review and Performance Comparison"
slug: "raspberry-pi-3-b-review-and-performance-comparison"
date: 2018-04-05T20:45:56+00:00
drupal:
  nid: 2833
  path: /blog/2018/raspberry-pi-3-b-review-and-performance-comparison
  body_format: markdown
  redirects: []
tags:
  - 3 B+
  - benchmarks
  - pi dramble
  - raspberry pi
  - reviews
  - sbc
---

<p style="text-align: center;">{{< figure src="./raspberry-pi-model-2-3-b-b-plus-generations.jpg" alt="Three generations of Raspberry Pi - model 2 B, model 3 B, model 3 B+" width="488" height="507" class="insert-image" >}}<br>
<em>Three generations of multi-core Pi: model 2 B, model 3 B, model 3 B+</em></p>

Whether it's been a [6-node Raspberry Pi cluster running Drupal 8](http://www.pidramble.com), or a [distributed home temperature monitoring application](https://opensource.com/life/16/3/how-i-use-raspberry-pis-help-my-kids-sleep-better), I use Raspberry Pis for a wide variety of fun projects. The [Raspberry Pi model 3 B+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/) is the latest iteration of the 'top of the line' Pi, with all the bells and whistles, and it still comes in at just $35. This year's iteration improves the CPU frequency, wired LAN performance, and WiFi performance, among other smaller changes, and I ordered one and have taken it for a spin.

What follows are my benchmarks and impressions after a couple weeks poking and prodding the new model 3 B+.

## Hardware - first impressions

{{< figure src="./raspberry-pi-model-3-b-plus-wifi-shield-logo.jpg" alt="Raspberry Pi model 3 B+ top detail Raspberry Pi logo embossed metal" width="488" height="377" class="insert-image" >}}

As can be seen in the photo at top, the model 3 B+ is yet another evolution in the Pi model B family; almost the entire board layout is identical, and there are only two major changes that jump out: a metal cover on the SoC (which greatly helps heat dissipation), and a metal shield with an embossed Raspberry Pi logo covering the WiFi and Bluetooth circuitry (to help contain RF emissions).

A few quick thoughts on the hardware changes:

  - The shiny Pi logo engraved on the wireless cover looks so much more premium than the old one etched on the circuit board (though there's still a small Pi logo on the opposite end of the circuit board!), especially teamed up with the nice metal cover on the Broadcom SoC.
  - The microSD card slot is a push/pull (not push-to-eject) style like all models besides the Pi model 2 B. My muscle memory is really suffering now, since I have Pis from three generations all with different style slots!
  - The new CPU design with a metal enclosure dissipates heat a _lot_ better than the old plastic casing; even without an extra heatsink or active cooling, I was not able to get the processor to throttle because of temperature. It was too easy to kill performance on the older model 3 B when the CPU got too hot, and this means I can use the Pi model 3 B+ like I did the original model B and 2—without a heatsink or active cooling!

There's not much else to say about the hardware; the form factor and board layout is very standardized at this point, and I don't see that changing anytime soon. There's still plenty of room to grow I/O in future revisions, even if it's only swapping out the USB 2.0 ports for USB 3.0. The Pi model 3 B+ fits perfectly in every case I have for my older Pis, though the LED lights are on the opposite side of the board from the model 2 (just like the model 3).

## Networking

One of the changes I was most looking forward to in this revision of the Pi was vastly improved onboard LAN. Instead of a 10/100 controller, the Pi foundation includes a 10/100/1000 Gigabit LAN controller. This means the built-in port is no longer limited to 100 Mbps (~93 Mbps real world). Indeed, as my network benchmarking shows, you get a lot more bandwidth out of the model 3 B+, and it negates the need to [use an external Gigabit USB 3.0 adapter to get faster wired LAN access](//www.jeffgeerling.com/blogs/jeff-geerling/getting-gigabit-networking), as you had to do on prior models:

{{< figure src="./pi-onboard-lan-speeds.png" alt="Raspberry Pi model 3 B+ onboard LAN performance benchmarks" width="650" height="334" class="insert-image" >}}

As you can see, the Pi model 3 B+ is considerably faster than both the 2 B and 3 B, especially when there is no other activity on the shared bus it operates over (as with a network read operation, which is cacheable and very fast). However, even the 3 B+ is hampered severely compared to other SBCs (e.g. ODROID-C2, ASUS Tinker Board, etc.) with a dedicated network bus that can pump through true 1 Gbps ethernet independent of the microSD card operations; you can see that when writing to the card, performance more than halves.

In terms of raw throughput, the model 3 B+'s onboard LAN is now equivalent to plugging in an external USB 3.0 Gigabit adapter—it saturates the available bandwidth, as measured with `iperf`:

{{< figure src="./pi-iperf-onboard-lan.png" alt="Raspberry Pi model 3 B+ onboard LAN iperf benchmark" width="650" height="233" class="insert-image" >}}

> **Note**: when shuffling a lot of data for a long period of time, the Pi 3 B+ (like it's older siblings) could run into thermal limits. During a heavy/long network transfer, the Pi's onboard temperature sensor went from 41°C to about 46.5°C (without using a heatsink or fan). If you want to use the Pi for sustained heavy network traffic, you might want to at least install a heatsink, if not active cooling as well.

I was also interested in whether the changes to the physical layout of the WiFi circuit (and the underlying hardware) would have an impact on WiFi performance... and _boy does it_!

{{< figure src="./pi-onboard-wifi-speeds.png" alt="Raspberry Pi model 3 B+ onboard WiFi performance benchmarks" width="650" height="334" class="insert-image" >}}

The WiFi performance of the model 3 B+ _decimates_ the 3 B. In addition, unlike the finicky WiFi setup on the 3 B, where I had to deal with weird errors like `RTNETLINK answers: Operation not possible due to RF-kill`, and a frequently-disappearing or misbehaving `wlan0` interface, the 3 B+ _just worked_ out of the box. I could set up everything I needed inside the `raspi-config` utility from the command line, and didn't even have to hand-edit any networking files or restart any services or interfaces!

And this is backed up by raw `iperf` interface performance benchmarks:

{{< figure src="./pi-iperf-onboard-wifi.png" alt="Raspberry Pi model 3 B+ onboard WiFi iperf benchmark" width="650" height="193" class="insert-image" >}}

These tests were done using the Raspberry Pis in the exact same physical location, about 20' from my [ASUS RT-AC66U 802.11 ac/n/g/b WiFi router](https://www.amazon.com/Dual-Band-AC1750-4-Port-Gigabit-RT-AC66U_B1/dp/B01N08LPPP/ref=as_li_ss_tl?ie=UTF8&qid=1522879449&sr=8-3&keywords=ASUS+RT-AC66U&dpID=41ud-8G5IiL&preST=_SY300_QL70_&dpSrc=srch&linkCode=ll1&tag=mmjjg-20&linkId=58983f5bfa9871931509625c6805accc), both connected to a dedicated 5 GHz-only network.

For more benchmark details, see [Networking Benchmarks](http://www.pidramble.com/wiki/benchmarks/networking) on the Pi Dramble website.

## microSD

{{< figure src="./microsd-cards-jeff-geerling-raspberry-pi-sbc.jpg" alt="Raspberry Pi microSD cards Noobs Samsung Kingston Toshiba Sony SanDisk SD SBC" width="488" height="329" class="insert-image" >}}

In 2015, I wrote an article [comparing the performance of a number of different microSD cards](//www.jeffgeerling.com/blogs/jeff-geerling/raspberry-pi-microsd-card) you could use with a Raspberry Pi. In this article, I stated:

> One of the highest-impact upgrades you can perform to increase Raspberry Pi performance is to buy the fastest possible microSD card—especially for applications where you need to do a lot of random reads and writes.

This still holds true today; the performance difference between some of the best Samsung or SanDisk cards and cheaper (or sometimes not-so-cheap!) brands is vast. You will have horrible performance for many different use cases if you use a microSD card with slow random read and random write performance.

So, as with each of the previous three Pi model B generations, I've tested all the microSD cards I have on hand, and compiled all the data into helpful charts for you, to help you decide which card to buy:

{{< figure src="./pi-model-3-b-plus-microsd-io-performance-comparison-revised-2.png" alt="Raspberry Pi model 3 B+ microSD card performance comparison" width="650" height="624" class="insert-image" >}}

At this time, due to the overall performance, and especially random read/write performance, I strongly recommend buying the [Samsung Evo+ 32GB microSD](https://www.amazon.com/Samsung-mc128d-128gb-Uhs-i-Adapter/dp/B00WR4IJBE/ref=as_li_ss_tl?th=1&linkCode=ll1&tag=mmjjg-20&linkId=b596196ae91b4131d5dcc2edeb8591ca) card. It is by far the best card for price/performance, and it comes in sizes up to 128 GB (at the time of this writing). Another option if you really need the fastest I/O is to boot from an external USB SSD, which can be faster, but is a little harder to set up and makes the hardware footprint much larger.

For more benchmark details, see [microSD Card Benchmarks](http://www.pidramble.com/wiki/benchmarks/microsd-cards) on the Pi Dramble website.

> **Overclocking the microSD card**: It's relatively easy to [overclock the microSD card reader in the Raspberry Pi](//www.jeffgeerling.com/blog/2016/how-overclock-microsd-card-reader-on-raspberry-pi-3), but for most practical purposes, overclocking the card reader doesn't speed things up to the point where you'll notice a difference. If you're performing frequent large file copies, you'll see the biggest gains, but otherwise with all the cards I've tested the gain is marginal:
> 
> {{< figure src="./pi-model-3-b-plus-overclocked-microsd-card.png" alt="Raspberry Pi model 3 B+ microSD card performance - overclock comparison" width="650" height="283" class="insert-image" >}}
> 
> There _is_ a difference, but it's pretty marginal; I even re-ran the Drupal benchmarks later in this review, but overclocking the microSD reader didn't make a significant difference.

## Power Consumption

Every generation of Pi has a higher-clocked processor, and also a few new circuits that require constant power just to run idle, and the 3 B+ is no exception. Running the exact same tests multiple times, I came up with the following power consumption numbers (in mA, as measured by my [PowerJive USB power meter](https://www.amazon.com/PowerJive-Voltage-Multimeter-chargers-capacity/dp/B013FANC9W/ref=as_li_ss_tl?ie=UTF8&qid=1522880075&sr=8-1&keywords=powerjive+usb&dpID=41jyky8FYmL&preST=_SY300_QL70_&dpSrc=srch&linkCode=ll1&tag=mmjjg-20&linkId=980f61fffea9b8bf7eb64a14a2361981)):

{{< figure src="./pi-power-consumption-model-3-b-plus.png" alt="Raspberry Pi model 3 B+ power consumption comparison to model 2 B and model 3 B" width="650" height="363" class="insert-image" >}}

For a little more processing power, and a lot more networking bandwidth, the Pi model 3 B+ consumes almost _double_ the power of the previous generation Pi model 3. In terms of power efficiency, I might still have to give the crown to the Pi model 2. I hope the next Pi can get a lid on the watts-per-CPU-performance metric. Other SBCs like the Tinker Board consume another double of what the 3 B+ uses... but it also more than doubles the performance metrics. The Pi seems to keep doubling power consumption for only marginal performance gains (see later benchmarks for more on _that_!).

For more benchmark details, see [Power Consumption Benchmarks](http://www.pidramble.com/wiki/benchmarks/power-consumption) on the Pi Dramble website.

### The importance of a good power supply

Every generation of Raspberry Pi has upped the ante in terms of power supply requirements. For the first few Pis, you could toss any little USB power adapter at it, and aside from a tiny glitch here or there, you'd never really experience difficulties. You can even see in my [Raspberry Pi Power Consumption benchmarks](http://www.pidramble.com/wiki/benchmarks/power-consumption) how each generation uses more power at idle, presumably due to more and more active circuits running all the time.

In my first set of performance tests, I was using my standard 5 port USB power supply, which puts out a nominal 2.4A at 5V... but in reality usually serves up 1.8A or so. With the Pi model 2 B and Pi model 3 B, this power supply never really caused an issue, and I never experienced CPU throttling even under load. However, **the Pi model 3 B+ had 2x better performance when using a dedicated 2.4A power supply**.

It was an amazing difference; at first, I thought maybe there was some thermal throttling going on—I monitored the temperature with the command `while true; do /opt/vc/bin/vcgencmd measure_temp && sleep 1; done`, and it showed that the model 3 B spiked to 68.8°C under load, while the Pi model 3 B+ hit 54.2°C. So it doesn't look like there's any thermal throttling, and in fact **the metal CPU enclosure on the model 3 B+ does a remarkably better job** at thermal management than the plastic one on the 3 B.

Next I thought maybe there was some CPU frequency throttling going on. Measuring with the command `watch -n 1 cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq `, the frequency went from idle at `600000` Hz (600 Mhz) to `1400000` Hz (1.4 Ghz). So it didn't look like there was any CPU frequency throttling either.

Finally, to get a raw performance statistic, I decided to run a barebones `sysbench` CPU test (specifically, `sysbench --test=cpu --num-threads=4 --cpu-max-prime=2000 run`) to see how things measured up:

  - Pi model 3 B+: 6.9920s
  - Pi model 3 B: 3.6902s

That seemed awfully suspicious; a CPU clocked at 1.4 GHz should surely be faster—not 2x slower—than almost the same CPU at 1.2 GHz!

Once I switched out the power supply, all the numbers made more sense:

  - `sysbench` test went from 6.9920s to 3.1718s (75% faster)
  - Drupal anonymous page views went from 99.18 req/s to 149.00 req/s (40% faster)
  - Drupal authenticated (uncached) page views went from 9.27 to 15.25 req/s (49% faster)
  - CPU temperature went up to 69.8°C under heavy load (maxed out around 54°C before).

So, as with all things Pi: **If you're experiencing strange issues regarding performance or stability, make sure you have a good (and ideally dedicated) micro USB power supply**.

## Drupal Performance

Since I don't generally use the Raspberry Pi for compute-intensive applications (since the CPU in the Pi is absolutely dwarfed by any modern x86 processor like the i3/i5/i7/i9s in any decent laptop or desktop computer, I'm not too worried about raw CPU benchmarks (though those will come in a minute!); I am more interested in real world applications running on the Pi. And since I'm a Drupal developer, I generally use Drupal as a proxy of overall system performance, since a test like uncached page views is especially taxing on CPU, memory, and I/O throughput:

{{< figure src="./pi-model-3-b-plus-drupal-performance-benchmark.png" alt="Raspberry Pi model 3 B+ Drupal performance comparison to model 2 B and model 3 B" width="650" height="286" class="insert-image" >}}

It's interesting to note how little the improvement is over the Pi model 3 B—I think the main constraints at this point are in I/O (microSD card access being slow and on a shared bus). Sadly, the CPU speed increase (which also means main memory access is faster) doesn't have as much of an effect as you'd hope.

I ran some bare `sysbench` tests as well, just to see the exact performance delta between the past few Pi model B revisions, and they show that while the raw performance metrics do see a marked increase, there's a chance the things you do on a Pi won't be _that_ much faster on the Pi model 3 B+ than they were on the 3 B. And especially coupled with the doubled power consumption... you'll have to make a decision if it's worth the performance-per-watt penalty to get the slightly faster model 3 B+—this could be critical to your decision if, for example, you're using the Pi on battery power, or with solar power, where every mA counts!

For more benchmark details, see [Drupal Benchmarks](http://www.pidramble.com/wiki/benchmarks/drupal) on the Pi Dramble website.

## Summary

So, in the end, is the Pi model 3 B+ a worthy upgrade from the 3 B (or for those holding out, the B+ or 2 B)? I'd say it's a _huge_ improvement when it comes to networking—wired or wireless. If you run a NAS, use the Pi as a static webserver or proxy server, use it as a router, or use it for anything that uses networking at all, the 3 B+ is a no-brainer.

If your needs aren't constrained by network speeds, though, it's a harder sell. It uses a lot more power to get a marginal real-world performance increase. However, the thermal throttling issues of the 3 B and its plastic-encased SoC seem to be resolved by the snazzy new metal enclosure on the 3 B+, so that's one major benefit. And the Broadcom SoC is also pretty good about power scaling—so if you're not constantly maxing out the CPU, the idle power consumption is almost on par with the older 3 B.

In the end, I'd say the Raspberry Pi foundation has come through with another winner—especially with the much-needed networking upgrades—but I'm still hoping and praying they fix the I/O situation so we can have at least one or two major bottlenecks resolved:

  - USB 3.0 instead of 2.0
  - True Gigabit Ethernet (instead of limiting it on a shared USB 2.0 bus)
  - Dedicated and faster microSD card bus (or maybe even eMMC or something!)

The Raspberry Pi is still, in my opinion, the most compelling SBC for hacking, prototyping, and experimentation, and it just keeps getting better, every generation. The software support and community is leagues beyond any competitor, though some hardware specs are a bit rusty. At the price of $35, though, I can live with the tradeoff.

You can [buy the Raspberry Pi model 3 B+ on Amazon](https://www.amazon.com/CanaKit-Raspberry-Power-Supply-Listed/dp/B07BC6WH7V/ref=as_li_ss_tl?ie=UTF8&qid=1522957703&sr=8-3&keywords=pi+3+b+&dpID=51IC7SDI3cL&preST=_SY300_QL70_&dpSrc=srch&linkCode=ll1&tag=mmjjg-20&linkId=bdc2f7534a1bebdbbce0feaf572969d1) or from any other reputable Raspberry Pi dealer.
