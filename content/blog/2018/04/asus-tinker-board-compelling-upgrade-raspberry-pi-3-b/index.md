---
nid: 2834
title: "The ASUS Tinker Board is a compelling upgrade from a Raspberry Pi 3 B+"
slug: "asus-tinker-board-compelling-upgrade-raspberry-pi-3-b"
date: 2018-04-18T20:23:09+00:00
drupal:
  nid: 2834
  path: /blog/2018/asus-tinker-board-compelling-upgrade-raspberry-pi-3-b
  body_format: markdown
  redirects: []
tags:
  - asus
  - computer
  - performance
  - reviews
  - sbc
  - tinker board
---

I've had a long history playing around with Raspberry Pis and other Single Board Computers (SBCs); from building a [cluster of Raspberry Pis to run Drupal](https://www.pidramble.com), to building a [distributed home temperature monitoring system with Raspberry Pis](https://opensource.com/life/16/3/how-i-use-raspberry-pis-help-my-kids-sleep-better), I've spent a good deal of time testing the limits of an SBC, and also finding ways to use their strengths to my advantage.

{{< figure src="./asus-tinker-board-sbc.jpg" alt="ASUS Tinker Board SBC" width="650" height="446" class="insert-image" >}}

ASUS sent me a [Tinker Board](https://www.asus.com/us/Single-Board-Computer/Tinker-Board/) late last year, and unfortunately due to health reasons, I had to delay working on a review of this nice little SBC until now. In the mean time, the Raspberry Pi foundation [released the Pi model 3 B+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/), which ups the ante and also negates a few of the advantages the more expensive Tinker Board had over the older model 3 B (not +). I just posted a [comprehensive review of the Pi model 3 B+](https://www.jeffgeerling.com/blog/2018/raspberry-pi-3-b-review-and-performance-comparison), and am now posting this review of the Tinker Board to compare and contrast it to the latest Pi offering.

{{< figure src="./raspberry-pi-model-3-b-plus-asus-tinker-board-comparison.jpg" alt="Raspberry Pi model 3 B+ and ASUS Tinker Board overview comparison" width="650" height="506" class="insert-image" >}}

Here's a really quick overview of how the two models stack up:

<table>
<thead>
<tr>
<td>&nbsp;</td>
<td><strong>Raspberry Pi model 3 B+</strong></td>
<td><strong>ASUS Tinker Board</strong></td>
</tr>
</thead>
<tbody>
<tr>
<td><strong>CPU</strong></td>
<td>Cortex-A53 Quad Core @ 1.4GHz</td>
<td>Cortex A17 Quad Core @ 1.8GHz</td>
</tr>
<tr>
<td><strong>RAM</strong></td>
<td>1 GB LPDDR2 (900 MHz)</td>
<td>2 GB LPDDR3 (dual channel)</td>
</tr>
<tr>
<td><strong>GPU</strong></td>
<td>Broadcom VideoCore IV @ 400 MHz</td>
<td>Mali-T764 @ 600MHz</td>
</tr>
<tr>
<td><strong>Network (LAN)</strong></td>
<td>10/100/1000 Mbps (~230 Mbps real world)</td>
<td>10/100/1000 Mbps</td>
</tr>
<tr>
<td><strong>Network (WiFi)</strong></td>
<td>2.4GHz or 5GHz 802.11n/ac</td>
<td>2.4GHz 802.11n</td>
</tr>
<tr>
<td><strong>Audio interface</strong></td>
<td>48kHz / 16 bit</td>
<td>192kHz / 16 bit</td>
</tr>
<tr>
<td><strong>GPIO</strong></td>
<td>40 pin header (not color coded)</td>
<td>40 pin header (color coded)</td>
</tr>
<tr>
<td><strong>Price</strong></td>
<td><a href="https://www.amazon.com/CanaKit-Raspberry-Power-Supply-Listed/dp/B07BC6WH7V/ref=as_li_ss_tl?s=electronics&amp;ie=UTF8&amp;qid=1522789079&amp;sr=1-3&amp;keywords=raspberry+pi+3+b+&amp;dpID=51IC7SDI3cL&amp;preST=_SY300_QL70_&amp;dpSrc=srch&amp;linkCode=ll1&amp;tag=mmjjg-20&amp;linkId=c25d1019a84fcb38719a8e8de27daf28">$35</a></td>
<td><a href="https://www.amazon.com/Tinker-board-RK3288-1-8GHz-Mali-T764/dp/B06VSBVQWS/ref=as_li_ss_tl?ie=UTF8&amp;qid=1522789055&amp;sr=8-3&amp;keywords=tinker+board&amp;dpID=51XkGSoKSyL&amp;preST=_SY300_QL70_&amp;dpSrc=srch&amp;linkCode=ll1&amp;tag=mmjjg-20&amp;linkId=ca68713345fa2c10eb2b08367f090e59">$49.99</a></td>
</tr>
</tbody>
</table>

I'm leaving out a lot of other specs that don't affect my day-to-day usage of an SBC, but what really stands out to me—and what may still make the Tinker Board worth the extra $15—is the slightly higher-clocked CPU and GPU, the faster onboard networking (which isn't crippled by being shared with the USB 2.0 bus like on the Pi), and double the RAM. The color-coded GPIO pins are a nice bonus, too, as I spend less time fumbling around counting pins on the Pi's unmarked header when experimenting with GPIO projects.

My initial impressions of the Tinker Board hardware are very good; the hardware is almost a perfect match to the layout of the Pi model 2 B, 3 B, and 3 B+—enough so that the Tinker Board fit in all my Pi cases. Note that the CPU seems to stand off _ever so slightly_ higher than the Pi's, so some cases with active cooling (e.g. a fan) might not fit the Tinker Board perfectly (one of my cases wouldn't clamp down all the way).

But as with many other SBCs, the _software_ support is where the rubber meets the road, so let's dive in and see how things stack up!

## Getting started with the Tinker Board

The process for getting the OS onto a microSD card is exactly the same as the Raspberry Pi's Raspbian or most other SBCs (this is written for a Mac, but it's similar if you use Linux):

  1. Download and expand the [TinkerOS disk image](https://www.asus.com/us/Single-Board-Computer/Tinker-Board/#tinker-board-Download).
  2. Insert a microSD card (I recommend the [Samsung Evo+ 32GB](https://www.amazon.com/Samsung-Class-Micro-Adapter-MB-MC32DA/dp/B00WR4IJBE/ref=as_li_ss_tl?s=pc&ie=UTF8&qid=1467829489&sr=1-3&keywords=evo+&linkCode=ll1&tag=mmjjg-20&linkId=dbb3aff130ee0dede5197fca4c8fdb3f)), and unmount it: `diskutil unmountDisk /dev/disk2` (use `diskutil list` to find which disk it is; could be `/dev/disk3` or something else).
  3. Write the disk image to the card: `pv YYYYMMDD-tinker-board-linaro-stretch-alip-vX.X.img.img | sudo dd of=/dev/rdisk2 bs=1m` (I use `pv` to track progress while the card is written).
  4. Eject the new `NO NAME` disk that appears after the image is written.
  5. Insert the microSD card into the Asus Tinker Board, and boot it up!

I am using the Debian-based OS (based on Debian 9 / Stretch), since that's the closest to Raspbian and has the best support and usability for general SBC usage and testing.

The Debian flavor of TinkerOS is as close to bare bones Debian as you can get, and it boots right into the desktop (no need for a login) when you turn on the Tinker Board. If you plug in networking, it will automatically grab an IP address and join the network via DHCP, just like the Pi, and it has SSH enabled out of the box, so you can ssh into it with `ssh linaro@[tinker-board-ip-here]` right away (I used `sudo fing` with [Fing](https://www.fing.io/download-free-ip-scanner-desktop-linux-windows-osx/) to find out the IP address of the Tinker Board from my Mac, so I could do everything headless).

## Networking

After my experience with the [ODROID-C2 and Orange Pi](//www.jeffgeerling.com/blog/2016/review-odroid-c2-compared-raspberry-pi-3-and-orange-pi-plus)—both of which clobbered the Raspberry Pi's wired networking performance—I was excited to see if the Tinker Board lived up to its promise of true 1 Gbps networking:

{{< figure src="./asus-tinker-board-onboard-lan-file-copy-benchmark.png" alt="ASUS Tinker Board and Raspberry Pi model 3 B+ Benchmarks - Network Onboard LAN speeds" width="650" height="287" class="insert-image" >}}

For file copies, which involve both networking and reading/writing on the microSD card, the Tinker Board does a respectable job. Especially for the writes, where the Tinker Board's much improved microSD controller bandwidth shines, allowing speeds up to 3x faster than the Raspberry Pi.

{{< figure src="./asus-tinker-board-iperf-lan-benchmark.png" alt="ASUS Tinker Board and Raspberry Pi model 3 B+ Benchmarks - Network iperf Onboard LAN speeds" width="650" height="218" class="insert-image" >}}

In terms of raw network performance, as measured by `iperf`, there's no competition. The ASUS Tinker Board's dedicated gigabit LAN bandwidth allows it to saturate a gigabit Ethernet connection, and it's not shared with the USB bus, nor with the microSD bus, meaning all other operations can operate at full speed as well.

For WiFi, it's a little bit of a different story. One of the Pi 3 B+'s headline features is a completely redesigned wireless package, from a new EMI shield, to a new antenna and 802.11ac 5 GHz networking support. The Pi 3 B+, then, has a major edge over the Tinker Board when it comes to _potential performance_ with built-in WiFi. Let's see what that means in real-world usage:

{{< figure src="./asus-tinker-board-onboard-wifi-benchmark-file-copies.png" alt="ASUS Tinker Board and Raspberry Pi model 3 B+ Benchmarks - WiFi file copies" width="650" height="297" class="insert-image" >}}

For things like file copies over WiFi, the performance difference isn't always huge, but the better bandwidth and signal on the Pi 3 B+ does mean you can get more reliable and speedy transfers.

{{< figure src="./asus-tinker-board-onboard-wifi-benchmark-iperf.png" alt="ASUS Tinker Board and Raspberry Pi model 3 B+ Benchmarks - WiFi iperf" width="650" height="217" class="insert-image" >}}

The raw performance measured with iperf (taking out the Internet connection and file system entirely) shows that the higher-specced Pi 3 B+ can outperform the 802.11n 2.4 GHz-only Tinker Board, getting about double the performance when all other variables are the same. But in either case, if you're using WiFi, you won't be able to achieve near the low latency, reliability, and bandwidth that you would using the wired LAN port, and performance will vary quite a bit (especially depending on signal quality).

For more benchmark details, see [Networking Benchmarks](http://www.pidramble.com/wiki/benchmarks/networking) on the Raspberry Pi Dramble website.

## microSD

One performance metric that trips people up the first time they use an SBC is the slow performance of the main drive—the microSD card that runs the OS and impacts the performance of almost everything else on the system. MicroSD cards are not known for great performance in general computing tasks (which involve lots of small file reads and writes); they are usually optimized for reading or writing very large amounts of data as fast as possible, as they're most optimized for media recording devices and multiple-GB files. But the Raspberry Pi cripples the microSD performance even further, as you usually can't even sustain a large file read or write at more than 20 MB/second. Some of the microSD cards I've tested can hit 60 or more MB/second when I'm using them in my Mac with a USB 3.0 UHS-II SD card reader! So how does the ASUS Tinker Board compare?

{{< figure src="./asus-tinker-board-microsd-card-performance-benchmarks-revision-2.png" alt="ASUS Tinker Board and Raspberry Pi model 3 B+ Benchmarks - microSD card performance" width="650" height="325" class="insert-image" >}}

The microSD controller in the Tinker Board is clearly operating at a much higher data rate than the one in the Pi; even with the SD overclock enabled on the Pi, it gets nowhere near the performance of the Tinker Board. The hdparm raw read throughput looks impressive, but isn't really a practical aid in measuring how the two devices would feel in real world scenarios. However, the 4k read and write benchmarks track much more realistic scenarios (e.g. when you're booting the SBC, or opening an app, compiling something, browsing the web, etc.), and even here, the ASUS Tinker Board is up to _35% faster than the Pi 3 B+_!

The microSD card I tested with is the fastest one I have benchmarked for SBC use (and [I have benchmarked them all!](//www.jeffgeerling.com/blog/2018/raspberry-pi-microsd-card-performance-comparison-2018)), [Samsung's Evo+ 32GB microSD card](https://www.amazon.com/Samsung-Class-Micro-Adapter-MB-MC32DA/dp/B00WR4IJBE/ref=as_li_ss_tl?ie=UTF8&qid=1524065343&sr=8-3&keywords=samsung+evo++32gb&dpID=419o58jbNhL&preST=_SX300_QL70_&dpSrc=srch&linkCode=ll1&tag=mmjjg-20&linkId=32d133adddfadea5bbec24d3485f555d). Highly recommended!

For more benchmark details, see [microSD Card Benchmarks](http://www.pidramble.com/wiki/benchmarks/microsd-cards) on the Raspberry Pi Dramble website.

## Power Consumption

One thing most SBCs do very well is conserve power; the mobile System-on-a-Chip (SoC) on which these computers are based is usually optimized for conserving power, especially when not doing intensive operations, because they're designed to operate primarily on battery power. Comparing the power consumption across different activities on the Pi and Tinker Board:

{{< figure src="./asus-tinker-board-power-consumption-benchmarks.png" alt="ASUS Tinker Board and Raspberry Pi model 3 B+ Benchmarks - Power consumption" width="650" height="269" class="insert-image" >}}

The idle power consumption is neck-and-neck, and bodes well for the Tinker Board; as we'll see later, the higher CPU frequency and CPU performance gains more than justify the increased power consumption under load, but it's very good to see the idle power consumption matches (within a margin of error) the Pi 3 B+. This means the Tinker Board does a good job of sipping power normally, but can quickly ramp up to tackle a CPU-intensive task, with slightly better power-efficiency (all things considered) than the Pi.

For more benchmark details, see [Power Consumption Benchmarks](http://www.pidramble.com/wiki/benchmarks/power-consumption) on the Raspberry Pi Dramble website.

### The importance of a good power supply

Just as with Raspberry Pis, the Tinker Board needs a good, high-output power supply to be able to run at full capacity and consistently. Especially when under heavy load, the Tinker Board can pull more than 2A peak power, and your best bet is to get a good, dedicated power supply like the [NorthPada Tinker Board 5V 3A power supply](https://www.amazon.com/NorthPada-Tinker-Supply-Charger-Adapter/dp/B072FTJH73/ref=as_li_ss_tl?ie=UTF8&qid=1522790449&sr=8-3&keywords=tinker+board+power+supply&dpID=31-98pBGC6L&preST=_SX300_QL70_&dpSrc=srch&linkCode=ll1&tag=mmjjg-20&linkId=4df7c309c11bc7caf8da5df8132550e4).

## CPU and Memory Performance

Let's see how the Pi and Tinker Board stack up when it comes to raw CPU and memory read/write performance, as measured by `sysbench`:

{{< figure src="./asus-tinker-board-sysbench-cpu-memory-benchmarks.png" alt="ASUS Tinker Board and Raspberry Pi model 3 B+ Benchmarks - CPU and Memory speed" width="650" height="249" class="insert-image" >}}

Even with the latest Pi 3 B+ CPU frequency increase, and the better thermal control from the new CPU package, the older Tinker Board's CPU soundly beats the Pi's by 25%. However, the memory performance is almost an inverse, as the Pi beats the Tinker Board by about 30% for both read and write operations.

In real-world usage, these numbers are much closer, but as we'll see in a minute, there are use cases where the overall system performance gives a thorough recommendation to the Tinker Board.

## Drupal Performance

The most important benchmarks are real-world use cases. For something like logging temperature data, even the lowliest Pi Zero or Pi model A could handle it with aplomb. But for more advanced use cases, like using an SBC like the Tinker Board as a general purpose Debian workstation, or serving a website, the overall system performance has a huge impact on whether the computer feels fast or not. I do a lot of work with the Drupal open source Content Management System, so one of my best benchmarks is to install and run the latest version of Drupal, and run two tests: anonymous (cached) page loads, which test networking and memory access mostly; and authenticated (uncached) page loads, which tests CPU, database, and disk access:

{{< figure src="./asus-tinker-board-drupal-benchmarks.png" alt="ASUS Tinker Board and Raspberry Pi model 3 B+ Benchmarks - Drupal CMS page load performance" width="650" height="254" class="insert-image" >}}

The anonymous benchmark ran 55% faster on the Tinker Board, and uncached page loads were 50% faster. It's interesting, because _individually_, the microSD, CPU, and memory benchmarks don't show more than a 20-30% performance improvement over the Pi 3 B+. But if you put everything together in this real-world benchmark, there's a _huge_ performance delta, completely in the Tinker Board's favor.

Overall, it feels to me like the A17 SoC on the ASUS Tinker Board is tuned a little better for peak performance than the Pi's A53 SoC, and even though there's a little higher peak energy consumption, the performance boost more than justifies it.

> Because of a few slight differences in the default OS layout with TinkerOS vs Raspbian, I had to modify the way I installed Drupal and the LEMP stack using [Drupal Pi](https://github.com/geerlingguy/drupal-pi) to [make sure all the installation steps worked on the Tinker Board](https://github.com/geerlingguy/drupal-pi/issues/31). After working through a few missing packages, everything seemed to run well.

For more benchmark details, see [Drupal Benchmarks](http://www.pidramble.com/wiki/benchmarks/drupal) on the Raspberry Pi Dramble website.

## Summary

So in the end, I think the question most people would ask themselves is: is the ASUS Tinker Board worth $15 more than a Raspberry Pi model 3 B or model 3 B+? I'd say yes, if you answer the following:

  - You need the best performance out of an SBC
  - You need more than 1 GB of RAM
  - You want the slightly nicer setup experience, support, and fit-and-finish of the Tinker Board vs. other Pi clones (like Orange Pi, ODROID, etc.)
  - You need fast networking

But if you didn't answer yes to one or more of those statements, I'd have a harder time recommending it.

The Pi community is pretty diverse and has you covered for so many projects and use cases, whereas there's fewer developers and bloggers posting about experiences with the Tinker Board. So the community still has room for improvement, but it's a little nicer, in my limited experience, than that of the other SBCs I've used.

The Pi is _fast enough_ for most use cases, and especially with the modest speed bumps in the model 3 B+ that put it almost on par with the Tinker Board in some uses, it makes it hard to justify the increased price of the Tinker Board.

Even if the Tinker Board isn't right for you, it's worth watching ASUS and their next moves in this space. I like the design of the Tinker Board's colorful GPIO 100x more than the Pi, and their guides, forums, downloads, and support are pretty decent—as long as they keep them up to date. I'm really interested to see if ASUS will release a newer model in the next year that might go beyond where even the current Tinker Board is, performance-wise, as that would more than justify purchasing another one or two for me!

### What about the Tinker Board S?

This year, ASUS released a slightly improved version of the Tinker Board, the [Tinker Board S](https://www.asus.com/us/Single-Board-Computer/Tinker-Board-S/). It includes 16 GB of onboard eMMC memory—much faster for general computing than a microSD card—for an extra $20 or so. There are a few other small differences, but the eMMC addition is the biggest improvement. For my use cases, the eMMC doesn't make a big enough difference to justify the cost, so I'm more interested in products in the $50 range and lower. Once an SBC approaches $100 or so, there are other options (like a used Intel core i5 desktop) which offer 10-100x the performance and infinite expansion options.

But that's just me—I am okay with a larger footprint desktop computer for use cases which require more desktop-like disk, CPU, and memory performance. If you need that kind of performance in an SBC form factor, the S might be a good option too. The Tinker Board S should be available for sale in spring or summer 2018.
