---
nid: 2633
title: "Review: Raspberry Pi model 3 B, with Benchmarks vs Pi 2"
slug: "review-raspberry-pi-model-3-b-benchmarks-vs-pi-2"
date: 2016-03-18T12:14:01+00:00
drupal:
  nid: 2633
  path: /blog/2016/review-raspberry-pi-model-3-b-benchmarks-vs-pi-2
  body_format: markdown
  redirects: []
tags:
  - armv7
  - benchmarks
  - cpu
  - dramble
  - raspberry pi
  - reviews
---

<p style="text-align: center;">{{< figure src="./raspberry-pi-3-front.jpg" alt="Raspberry Pi 3 - Front" width="500" height="344" class="insert-image" >}}</p>

<p style="text-align: center;">{{< figure src="./raspberry-pi-3-back.jpg" alt="Raspberry Pi 3 - Back" width="500" height="344" class="insert-image" >}}</p>

On Pi Day (3/14/16), I finally acquired a [Raspberry Pi model 3 B](https://www.raspberrypi.org/blog/raspberry-pi-3-on-sale/) from my local Micro Center (I had ordered one from Pimoroni on launch day, but it must be stuck in customs). After arriving home with it, I decided to start running it through its paces. Below is my review and extensive benchmarking of the Pi 3 (especially in comparison to the Pi 2).

## Hardware changes

There are a few notable hardware changes on the Pi 3:

  1. The LEDs have moved to the opposite side of the 'front' of the board, having been displaced by a tiny wireless antenna where they used to be. This has the unfortunate side effect of making the LED openings on most older Pi cases (including the Raspberry Pi 'official' case) misaligned. I can still see a faint light through the front of my case, and everything fits fine, so it's not a huge deal to me.
  2. The microSD card is not retained by a spring 'push to eject' mechanism anymore; it simply slides in and slides out (just like the Pi Zero). This helps cut down on accidental removal when holding the Pi to insert USB plugs, but it can also make the card slightly harder to remove in some cases.
  3. There's a wireless antenna near the GPIO. If you need to use Bluetooth or WiFi, make sure you place the Pi 3 in a case that's not a [faraday cage](http://falloutshelter.me/how-to-make-a-faraday-cage-to-protect-your-electronics-from-an-emp/), and also consider the orientation of your Pi when trying to pick up radio signals—orienting it away from your router behind a brick wall will lead to a poor connection.

## Networking Benchmarks

Network performance is one of the most straightforward, but most caveat-laden, aspects to benchmark. You can measure raw throughput, network file copy, and file download/upload performance. However, some of the benchmarks (e.g. file copies) are also dependent on other parts of the Pi (e.g. disk I/O, USB bus, memory I/O, etc.), so I focus on raw network throughput. And in that regard, the Pi 3 offers a respectable gain over the Raspberry Pi model 2 B:

<p style="text-align: center;">{{< figure src="./raspberry-pi-3-vs-2-networking-benchmarks.png" alt="Raspberry Pi Model 3 B - Networking iperf throughput benchmark vs pi 2" width="532" height="394" >}}</p>

For the Pi 2, I tested WiFi with an [Edimax USB 2.0 802.11n adapter](https://www.amazon.com/Edimax-EW-7811Un-150Mbps-Raspberry-Supports/dp/B003MTTJOY/ref=as_li_ss_tl?ie=UTF8&ref_=as_li_ss_tl&linkCode=ll1&tag=mmjjg-20&linkId=56e1b8df3f3a29dffe0049e519732cd5), and for the Pi 3, I tested with the built-in WiFi; in both cases the signal strength was excellent, and I connected to an AirPort Extreme (6th gen) WiFi router. WiFi performance was consistent on both Pis, and with both, I disabled WiFi power management to make the connection stable (see caveats at the end of this section).

For the 'GigE' test, I plugged a [TRENDnet USB 3.0 Gigabit ethernet adapter](https://www.amazon.com/TRENDnet-Ethernet-Chromebook-Specific-TU3-ETG/dp/B00FFJ0RKE/ref=as_li_ss_tl?ie=UTF8&linkCode=ll1&tag=mmjjg-20&linkId=3615dd10bc52f0064bcf05875b958a79) into one of the Pi's USB 2.0 ports, configured the adapter as an `eth1` interface, and disconnected/disabled the built in interface(s). See this article for more info: [Gigabit Networking on a Raspberry Pi](/blogs/jeff-geerling/getting-gigabit-networking).

The good news? **The Pi 3 can hit sustained throughput of 321 Mbps using a Gigabit adapter**. This means the Pi can sustain a theoretical 40 MB/s file copy, making the Pi 3 a marginally-useful file server (e.g. NFS) or dedicated proxy/router—much more so than any Pi before.

The bad news? Don't expect those numbers to be sustainable if you shove lots of bits through the Pi; in my testing, even with a passive aluminum heatsink, the Pi 3 started throttling the transfer speeds when pushing it to the max after 3-5 minutes, and needed a 2-4 minute cool-down period before speeds would max out again.

The built-in LAN offered almost identical benchmark results as it did on the Pi 2.

When it comes to WiFi, there are some other caveats:

  - [SSH sometimes has issues via WiFi](https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=138631) - there are some strange issues with certain routers and built-in WiFi.
  - Disable WiFi power management (`sudo iwconfig wlan0 power off`), otherwise you may experience a lot of dropped packets and issues with things like SSH. You can persist this change using [these instructions](http://askubuntu.com/a/129634/88829). For the Edimax, see my notes in my [Edimax 802.11n WiFi adapter review](/blogs/jeff-geerling/edimax-ew-7811un-tenda-w311mi-wifi-raspberry-pi) on preventing sleep mode.

For the _full_ dataset and rationale behind different benchmarks, check out: [Raspberry Pi Networking Benchmarks](http://www.pidramble.com/wiki/benchmarks/networking).

## microSD Card Benchmarks

In late 2015, I published a comprehensive [benchmark of microSD card performance on the Raspberry Pi 2](/blogs/jeff-geerling/raspberry-pi-microsd-card). The Pi 3, with its faster clock and new SoC architecture, has the potential to make microSD card operations even faster, so I re-ran benchmarks on all the Samsung and SanDisk cards I have on the Pi 3, and have added those results to my [Pi Dramble microSD Card Benchmarks](http://www.pidramble.com/wiki/benchmarks/microsd-cards) page. In summary:

<p style="text-align: center;">{{< figure src="./raspberry-pi-3-vs-2-microsd-4k-random-read-benchmark.png" alt="Raspberry Pi Model 3 B vs Model 2 B - microSD card reader 4K random read benchmark" width="530" height="387" >}}</p>

One caveat: With microSD performance timings, the numbers are always about +/- 5% different between runs, so the real-world difference between the Pi 2 and Pi 3 in their default state will be minimal at best—though the Pi 3 _is_ measurably and reliably a little faster, in my testing.

Things get even more interesting if you [overclock the microSD card reader in the Raspberry Pi 2/3](/blog/2016/how-overclock-microsd-card-reader-on-raspberry-pi-3). Overclocking adds another 20% speed boost to most file operations (at least for reads), and can double large file read/write performance! Unless you need the utmost performance and have very reliable power supplies and microSD cards, though, it's safer to leave the Pi at its normal clock.

## Keeping it cool: the (hot) 64-bit Cortex-A53 Broadcom SoC

<p style="text-align: center;">{{< figure src="./raspberry-pi-3-aluminum-heat-sink.jpg" alt="Raspberry Pi 3 - aluminum heat sink" width="425" height="274" >}}<br />
<em>For the Pi 3, a heat sink isn't just for overclockers.</em></p>

The Raspberry Pi 3's new A53-series 64-bit System-on-a-Chip uses a bit more power than the older ARM processors used in previous Pis, and as a result, there is also more thermal dissipation; if the heat from the chip doesn't have anywhere to go, then things can get hot enough to trigger some processor throttling.

Many overclockers would put heat sinks on their Pi 2s and older models, but in my testing, thermal throttling was never an issue—even when running with a moderate overclock and hammering the Pi Dramble with thousands of PHP requests/second continuously (e.g. 100% CPU for many minutes). Reddit user ghalfacree used a thermal imager to take [thermal images of the various Raspberry Pi models](https://www.reddit.com/r/raspberry_pi/comments/48lhot/raspberry_pi_family_thermal_analysis_thermal/?ref=share&ref_source=link), and you can see there's a marked difference when it comes to heat dissipation from the CPU on the Pi 3.

For this reason, I purchased some [passive aluminum heat sinks](https://www.amazon.com/LinuxFreak-brand-Aluminum-Heatsink-Raspberry/dp/B00A88DVTG/ref=as_li_ss_tl?ie=UTF8&psc=1&redirect=true&ref_=as_li_ss_tl&ref_=oh_aui_search_detailpage&linkCode=ll1&tag=mmjjg-20&linkId=f037213229bd6d3ea67880d446324b42) (with pre-applied thermal paste) and applied them to the SoC on my Raspberry Pi 3s. So far the heat sink seems to be working well; it dissipates enough heat to prevent CPU throttling under high load. I haven't done much testing with overclocking, but I typically keep the defaults since I favor reliability over performance.

Running `stress --cpu 4` to hammer the processor continuously, I didn't notice any sustained throttling after installing the heat sink (there was a short (1-2 second) throttle every few minutes), and temperatures seemed to level off around 81.0°C (at least according to the internal CPU temperature reporting). Measuring the surface temp of the heat sink showed about 65°C—quite hot to the touch! But unless you're going to be running the CPU at full throttle, overclocked, all the time, I think a passive heat sink and a case that allows some amount of convective airflow will be enough.

Also, a ProTip for monitoring CPU frequency while doing benchmarks; run `while true; do vcgencmd measure_temp && vcgencmd measure_clock arm; sleep 2; done` in a separate terminal window to see updates continuously. Thanks to [GTR2fan](https://www.raspberrypi.org/forums/viewtopic.php?p=923556#p923556) on the Pi forums for that!

## Powering the Pi 3

The Raspberry Pi 3 is [no Pi Zero](http://www.jeffgeerling.com/blogs/jeff-geerling/raspberry-pi-zero-conserve-energy) when it comes to conserving power and handling almost any kind of flaky power supply.

<p style="text-align: center;">{{< figure src="./raspberry-pi-firmware-undervolt-rainbow-icon.jpg" alt="Raspberry Pi 3 - low voltage onscreen rainbow icon" width="300" height="200" >}}<br />
<em>The undervolt rainbow made frequent appearances when building PHP from source.</em></p>

I have many USB power supplies of varying quality. Pis < 3 would survive with almost any USB power source (as long as you don't need to power a bunch of USB devices off the Pi), but the Pi 3 needs a much better supply. Even using a reliable Apple 2A iPad charger, I noticed the red power LED flicker off every now and then, with a corresponding momentary voltage dip below 5.12V and an undervolt rainbow.

You _need_ a good power adapter for the Pi 3, much more so than in the past, even if you're running it headless. Under heavy load (e.g. PHP processes pegging all 4 CPU cores), the Pi 3 had momentary voltage drops. If you're running the Pi 3 as a desktop replacement, attached to a monitor, using Raspbian's GUI with a keyboard and mouse, this is even more crucial to a painless experience.

Luckily for my [Pi Dramble](http://www.pidramble.com/), the 6 port USB charger I use provides a solid 2A per port, and things seem to run fine there, even under load.

### Power benchmarks

<p style="text-align: center;">{{< figure src="./raspberry-pi-2-vs-3-power-benchmark.png" alt="Raspberry Pi 2 vs Raspberry Pi 3 model B power consumption" width="544" height="394" >}}</p>

The Pi 2 was slightly more power-hungry than all the Pis before, and the Pi 3 continues the tradition; the higher-clocked CPU, extra built-in circuits, and newer quad core architecture add up to about a 40% increase in power draw when under heavy load. Luckily, idle and normal CPU load doesn't incur too much of a penalty vs. the Pi 2—it's only bursty CPU spikes that draw more power (and generate a _lot_ more heat).

I have some tips for limiting power consumption on the Pi 3 (similar to Zero, A+, etc.) in this post: [Conserve power when using Raspberry Pis](/blogs/jeff-geerling/raspberry-pi-zero-conserve-energy).

## PHP benchmarks – Drupal 8

Since I'm a Drupal developer in my day job, and since I like tinkering with my [Raspberry Pi Dramble](http://www.pidramble.com/) cluster to tinker with Ansible, Drupal, GPIO, and more, I like to use Drupal to benchmark the entire system—memory, CPU, disk I/O, and networking. I've been maintaining and re-running a large number of benchmarks to test Drupal on the Raspberry Pi in various configurations. Full details (which are continuously updated) are listed on the Pi Dramble [Drupal Benchmarks](http://www.pidramble.com/wiki/benchmarks/drupal) page, but here are some relevant benchmarks comparing the Pi 3 to the Pi 2:

<p style="text-align: center;">{{< figure src="./drupal-8-performance-benchmark-pi2-pi3-php7.png" alt="Drupal 8.0.5 and PHP 7.0.4 performance on Raspberry Pi 2 vs Raspberry Pi 3" width="512" height="395" >}}</p>

I've beaten the [PHP 5.6 vs PHP 7 vs HHVM](/blogs/jeff-geerling/benchmarking-drupal-8-php-7-vs-hhvm) benchmarks to death, so from this point forward I'm only going to be dealing with PHP 7.x when benchmarking Drupal 8. The [Drupal Pi](https://github.com/geerlingguy/drupal-pi) project allows you to build PHP from source in the project's `config.yml`, and using that I installed PHP 7.0.4 with Drupal 8.0.5.

The Pi 3 offers a decent and highly consistent 30-33% performance improvement for Drupal 8 and the LEMP stack.

## Summary

The Raspberry Pi 3 is, in some ways, just an evolutionary improvement over the Pi 2. In terms of major changes, the Pi 2 was a much larger change over the B+ and all other Pis before due mainly to its multi-core processor. The Pi 3's incremental improvements, and convenient built-in WiFi and Bluetooth, make the Pi 3 the best Pi for almost any general computing need. I the Pi 3 release is like an iPhone 'S' release—no major changes to the look and feel or earth-shattering new features... but everything _feels_ better, and there are small improvements to make usage easier (e.g. no more $10 WiFi dongle to buy separately). It's the first Pi on which Raspbian's desktop UI and browser feels usable outside of testing purposes, and that's pretty exciting!

For the first time, however, I recommend purchasing an official Raspberry Pi power supply (or making sure the one you use is very good quality with consistent 2+ amp output), and also purchasing at least a passive heat sink to adhere (with proper thermal compound) to the Broadcom SoC.

## Further reading

  - [Raspberry Pi Dramble](http://www.pidramble.com/) - A cluster ('bramble') of Raspberry Pis hosting a HA Drupal 8 site in my basement
  - [Raspberry Pi thermal imaging - Pi model temperature comparison under load](https://imgur.com/a/tzgPU)
  - [Raspberry Pi microSD card benchmarks](http://www.pidramble.com/wiki/benchmarks/microsd-cards)
  - [Raspberry Pi networking benchmarks](http://www.pidramble.com/wiki/benchmarks/networking)
  - [Raspberry Pi power consumption](http://www.pidramble.com/wiki/benchmarks/power-consumption)
  - [Raspberry Pi Drupal 8 benchmarks](http://www.pidramble.com/wiki/benchmarks/drupal)
