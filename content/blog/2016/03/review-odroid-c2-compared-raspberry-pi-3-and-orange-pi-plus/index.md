---
nid: 2637
title: "Review: ODROID-C2, compared to Raspberry Pi 3 and Orange Pi Plus"
slug: "review-odroid-c2-compared-raspberry-pi-3-and-orange-pi-plus"
date: 2016-03-24T12:14:05+00:00
drupal:
  nid: 2637
  path: /blog/2016/review-odroid-c2-compared-raspberry-pi-3-and-orange-pi-plus
  body_format: markdown
  redirects: []
tags:
  - benchmarks
  - clones
  - computer
  - odroid
  - odroid c2
  - orange pi
  - raspberry pi
  - reviews
---

> **tl;dr**: The ODROID-C2 is a very solid competitor to the Raspberry Pi model 3 B, and is anywhere from 2-10x faster than the Pi 3, depending on the operation. The software and community support is nowhere near what you get with the Raspberry Pi, but it's the best I've seen of all the Raspberry Pi clones I've tried.

The original Raspberry Pi was the first mass-market 'single board' computer that kicked off a small computing revolution in terms of hardware interaction via GPIO, experimental monitoring, automation, and robotics projects, etc. Through the past few years, it has evolved from being a very slow and limited computing platform to being as fast as some lower-specced smartphones, and can now run a desktop Linux environment bearably well. The Raspberry [Pi 2](https://www.raspberrypi.org/products/raspberry-pi-2-model-b/) and [Pi 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/) (just announced on Feb 29—see [my review of the Pi 3 here](/blog/2016/review-raspberry-pi-model-3-b-benchmarks-vs-pi-2)) were the first models with quad core processors, and they're both decent generic Linux computers, especially for the low $35 price tag!

Once the Pi became a popular product, similar single board computers were introduced with different features and functionality, in a similar price range. I recently reviewed one of the main competitors, the [Orange Pi Plus](/blog/2016/orange-pi-plus-setup-benchmarks-and-initial-impressions), which for $39 offers faster networking, onboard fast eMMC storage, and a bevy of other features—but which also requires a lot more effort to get up and running, and has nowhere near the community and documentation surrounding the Raspberry Pi.

<p style="text-align: center;">{{< figure src="./odroid-c2-front.jpg" alt="ODROID-C2 - Front" width="500" height="354" class="insert-image" >}}</p>

<p style="text-align: center;">{{< figure src="./odroid-c2-back.jpg" alt="ODROID-C2 - Back" width="500" height="350" class="insert-image" >}}</p>

Another primary competitor in the space is the ODROID, from Hardkernel. The original ODROID-C1 was already a decent platform, with a few more features and more RAM than the comparable Pi at the time. The [ODROID-C2](http://www.hardkernel.com/main/products/prdt_info.php?g_code=G145457216438) was just announced in February, and for $39 (only $5 over the Pi 3 price tag) offers a few great features over the Pi 3 like:

  - 2GHz quad core Cortex A53 processor (Pi 3 is clocked at 1.2 GHz)
  - Mali-450 GPU (Pi 3 has a VideoCore IV 3D GPU)
  - 2 GB RAM (Pi 3 has 1 GB)
  - Gigabit Ethernet (Pi 3 has 10/100)
  - 4K video support (Pi 3 supports HD... drivers/support are usually better for Pi though)
  - eMMC slot (Pi 3 doesn't offer this option)
  - UHS-1 clocked microSD card slot (Pi 3 requires overclock to get this speed)
  - Official images for Ubuntu 16.04 MATE and Android (Pi 3 uses Raspbian, a Debian fork)

The Pi 3 added built-in Bluetooth and WiFi, which, depending on your use case, might make the price of the Pi 3 even more appealing solely based on a feature comparison.

But features and specs are really just the tip of the iceberg. As I found when reviewing the Orange Pi, there are many factors you have to consider when evaluating what single board computer makes the most sense for your projects or usage; especially if you're not a hardcore Linux kernel hacker, you might want to consider factors like the user community, forums, and software support you get from the companies/foundations behind the boards.

## Acquiring an ODROID-C2

Unlike the Pi 3 (and pretty much every Pi since the B+), there's no huge run on ODROID-C2s, so I went to the official USA distributor's site (AmeriDroid) and bought an [ODROID-C2](http://ameridroid.com/products/odroid-c2) for $41.95 plus $7 shipping (I also added in an official clear case and the recommended power adapter, for convenience—though you can power the ODROID-C2 through the USB OTG port just like the Pi). Note that there was a recent post in the ODROID forums stating that the [first batch of ODROID-C2s had already been sold out](http://forum.odroid.com/viewtopic.php?f=135&t=19936) as of March 16, but many distributors still have them in stock.

Getting a Pi 3 can be an exercise in frustration; almost a month in, it's only in stock in some stores, and people are still price gouging by selling at higher prices with cheaply-assembled Pi starter kits and on eBay. I was lucky to find them in stock at my local Micro Center for list price; the situation should improve over time... but considering the Pi Zero is still perpetually out of stock everywhere, the Pi Foundation definitely needs to beef up its manufacturing and distribution partnerships to meet demand!

## Hardware

<p style="text-align: center;">{{< figure src="./raspberry-pi-3-odroid-c2-comparison-flat.jpg" alt="ODROID-C2 and Raspberry Pi 3 comparison - face" width="322" height="400" class="insert-image" >}}<br />
<em>A view of the ODROID-C2 and Pi 3 from the top.</em></p>

<p style="text-align: center;">{{< figure src="./raspberry-pi-3-odroid-c2-comparison.jpg" alt="ODROID-C2 and Raspberry Pi 3 comparison - ports" width="500" height="331" class="insert-image" >}}<br />
<em>A view of the ODROID-C2 and Pi 3 from the side.</em></p>

One of the first _major_ differences between the Pi 2/3 and the C2 is the massive heat sink that's included with the ODROID-C2. Based on my observations with CPU temperatures on the Pi 3, the heat sink is a necessity to keep the processor cool at its fairly high 2 GHz clock. The board itself feels solid, and it feels like it was designed, assembled, and soldered slightly better than the larger Orange Pi Plus, on par with the Pi 3.

One extremely thoughtful feature is the ODROID-C2 board layout mimics the Pi B+/2/3 almost exactly; the largest components (e.g. LAN, USB, HDMI, OTG, GPIO, and even the screw holes for mounting!) are identically placed—meaning I can swap in an ODROID-C2 in most situations where I already have the proper mounts/cases for a Pi.

## Setup and first boot

The process for setting up an ODROID-C2 is pretty much the same as the Raspberry Pi; you download the official OS image from the appropriate wiki page (in this case, I downloaded [Ubuntu 16.04 1.1](http://odroid.com/dokuwiki/doku.php?id=en:c2_release_linux_ubuntu)), expand the image file (since it's a large `.xz` file, I used [The Unarchiver](http://wakaba.c3.cx/s/apps/unarchiver.html) for Mac to expand it), then flash it to a microSD card.

On my Mac, I inserted a Samsung EVO 16GB card, ran `diskutil unmountDisk /dev/disk2`, then ran `sudo dd if=image-expanded.img of=/dev/rdisk2 bs=1m` to copy the image to the microSD card. The official Ubuntu image is over 5 GB, so it takes a little time. (For the Pi, there's an official CLI-only 'Raspbian Lite', which clocks in around 1 GB, so it's little faster to copy.)

<p style="text-align: center;">{{< figure src="./odroid-c2-microsd-card-slot-back-gpio.jpg" alt="ODROID-C2 - microSD card slot under the GPIO pins on back" width="440" height="400" class="insert-image" >}}<br />
<em>The microSD card slot is in a peculiar location, just clearing the GPIO pins on the underside.</em></p>

Insert the microSD card into the slot on the underside of the ODROID-C2 (it's in a bit of a strange location, with the card sticking out over the soldered GPIO pin connections), then plug in your keyboard, mouse, and HDMI monitor, and then plug in power to boot it up.

It boots to a pleasing Ubuntu desktop login page (default admin username is `odroid` with the password `odroid`), and after first boot, everything is configured and ready to go. One nice thing about the setup experience is you don't have to manually run `sudo raspi-config` and expand the filesystem manually (or do the same via a GUI config panel)—on first boot, the OS expands the filesystem to cover your whole microSD card automatically.

> The official Ubuntu MATE environment is nice, but for better efficiency, I used the ODROBIAN [Debian Jessie ARM64 image for ODROID-C2](http://oph.mdrjr.net/odrobian/images/s905/) instead. The download is only 89 MB compressed, and the expanded image is ~500 MB, making for an almost-instantaneous `dd` operation. There are some other images available via the community as well, but ODROIBIAN seems to be the most reliable—plus it already has [excellent documentation](http://oph.mdrjr.net/odrobian/doc/#README)!

## Using the C2

Since it defaults to Ubuntu MATE, the desktop environment is pleasant (more so than Raspbian's default GUI), and it even comes with both Chromium and FireFox installed, so you can choose from one of the two most popular and well-supported browsers. However, after I ran `sudo apt-get update && sudo apt-get upgrade` (which took quite a while the first time) to make sure all packages were up to date), neither Chromium nor FireFox would launch; they would launch and then quit after a few seconds. So I re-imaged the card (which took a couple hours) and tried again.

Chromium took about 4 minutes to launch the first time (it seemed like nothing was happening, but one CPU core was spiked at 100% the whole time), and FireFox took about 8 seconds the first time. After that, both took 4-5 seconds to launch, and nothing seemed slow or inconsistent when using them.

Most apps that come preinstalled with MATE worked flawlessly, though every once in a while FireFox or Chromium would crash and need to be restarted (Chromium much more so than FireFox—see [this forum topic](http://forum.odroid.com/viewtopic.php?f=135&t=20085)). Hopefully this is just a growing pain with a relatively new ODROID revision and a new OS distribution, but it's a little disconcerting, especially after hearing grief on some forums about Hardkernel being stuck on the Linux 3.x kernel for a while.

It's hard to match the level of software/OS support the Raspberry Pi foundation and community provides, but of all the single board computers, the ODROID-C2 and the Hardkernel community seem to have the most solid footing; reading through forum posts like [Ubuntu 16.04 LTS for ODROID-C2](http://forum.odroid.com/viewtopic.php?f=136&t=18709) makes me confident that the Hardkernel devs and community are working to smooth out the rough patches, and in just the past month, the progress has been excellent!

## Benchmarking the C2 vs Pi 3 vs Orange Pi Plus

For the [Pi Dramble](http://www.pidramble.com/), I have a few pain points with the current generation of Raspberry Pis; I could always use more raw CPU speed (that's the main bottleneck for authenticated web requests), but one of the even more important considerations is network bandwidth—the Pi 3's limited bus only allows up to ~95 Mbps over wired lan, or up to ~321 Mbps if using a USB 3.0 adapter. The ODROID-C2's faster CPU clock, default UHS-1-clocked microSD reader, and built-in Gigabit Ethernet port paint a great portrait on paper—but the proof is in the pudding. As with all my other reviews, I've run the ODROID-C2 through my benchmarking gauntlet to compare it to the Pi 3 and Orange Pi Plus.

### CPU Benchmarks

Others have already [beaten the CPU benchmarks to death](http://openbenchmarking.org/result/1603051-GA-ODROIDPI362); architecturally, the quad-core Cortex A53 64-bit processor is very close to the Pi 3's processor; however, the .8 Ghz faster clock rate and larger memory allocation does provide a marked increase in performance over the Pi 2/3 for many tests, including some real-world Drupal web application tests later in this post.

### Network

A fast and reliable network link is important if you either need lots of throughput for things like serving lots of web traffic or passing around files on a network (e.g. using the ODROID-C2 as a NAS). I have [comprehensive networking benchmarks](http://www.pidramble.com/wiki/benchmarks/networking) posted on the Pi Dramble site for the Pi 2 and Pi 3, but let's see how the ODROID-C2 compares:

<p style="text-align: center;">{{< figure src="./odroid-c2-networking-benchmarks.png" alt="ODROID-C2 - Networking benchmarks vs Raspberry Pi 3 and Orange Pi Plus" width="512" height="390" class="insert-image" >}}</p>

The raw stats:

  - 100 MB file download (via 100 Mbps Internet, onboard Gigabit Ethernet): **10.7 MB/s** (10.6 MB/s on Pi 3)
  - 100 MB LAN file copy from ODROID-C2 to Mac (onboard Gigabit Ethernet): **32.7 MB/s** (13.98 MB/s on Pi 3)
  - 100 MB LAN file copy from Mac to ODROID-C2 (onboard Gigabit Ethernet): **39.5 MB/s** (9.98 MB/s on Pi 3)
  - `iperf` raw throughput (onboard Gigabit Ethernet): **938 Mbps** (321 Mbps on Pi 3)

`iperf` gave absolutely an absolutely rock solid 938 Mbps, which is awesome—the Orange Pi was a little shaky in its results, varying in test runs from 300-750 Mbps, but never getting near a full 1 Gbps throughput. The Raspberry Pi 3 can get 95 Mbps on the built in 10/100 Ethernet port, or up to 321 Mbps on a [Gigabit USB 3.0 adapter](/blogs/jeff-geerling/getting-gigabit-networking). The ODROID-C2 delivers on the networking throughput in spades; pair it up with a nice SSD in a USB enclosure and a fast eMMC card, and this could be an excellent option for NAS or any kind of streaming!

### Power consumption

For some projects (and in general, in my opinion), the amount of power that's drawn is an important consideration. Typically, the less current draw the better, especially if you don't have as good a quality power supply, or might need to run the board off a battery for certain applications (e.g. mobile robotics, mobile sensors, mesh networks). I have a good overview of [power consumption for the various Raspberry Pis](http://www.pidramble.com/wiki/benchmarks/power-consumption), and here are a few stats for the ODROID-C2:

<p style="text-align: center;">{{< figure src="./odroid-c2-power-benchmarks.png" alt="ODROID-C2 - Power benchmarks vs Raspberry Pi 3" width="507" height="391" class="insert-image" >}}</p>

The raw stats:

  - Idle, no keyboard: **350 mA** (260 mA on Pi 3)
  - ApacheBench webserver stress test: **800 mA** (480 mA on Pi 3)
  - 400% CPU load: **650 mA** (730 mA on Pi 3)

The most surprising thing to me is how the `ab` stress test (basically hitting Drupal hard for a long time, pegging the CPU cores, the memory, and the microSD card at the same time with uncached requests) used a lot more power on the ODROID-C2 vs the Pi 3. The Pi 3 must have a little better power optimization overall, while the ODROID-C2 has a little better power optimization for the CPU itself.

### Storage / microSD card

Unfortunately, I am not able to test the eMMC performance at this time as I don't have the required module, but I did run a set of benchmarks against the built-in microSD card reader (using a Samsung EVO 16 GB card), comparing the results to a Raspberry Pi 3 running Raspbian (with the [microSD card reader overclocked](/blog/2016/how-overclock-microsd-card-reader-on-raspberry-pi-3)):

<p style="text-align: center;">{{< figure src="./odroid-c2-microsd-card-benchmarks.png" alt="ODROID-C2 - microSD card reader benchmarks vs Raspberry Pi 3" width="505" height="391" class="insert-image" >}}</p>

The raw stats:

  - `hdparm` buffered: **35.29 MB/s** (40.88 MB/s on RPi)
  - `dd` write: **30.2 MB/s** (39.1 MB/s on RPi)
  - `iozone` 4K random read: **9.64 MB/s** (11.77 MB/s on RPi)
  - `iozone` 4K random write: **2.04 MB/s** (2.36 MB/s on RPi)

I posted more [comprehensive benchmarks for microSD cards on the Raspberry Pi](http://www.pidramble.com/wiki/benchmarks/microsd-cards), but what I think may be even more interesting is running the OS off the eMMC; it promises to be 5-10x faster than even the fastest microSD cards I've tested, and it's not too expensive an addition to the ODROID-C2 (the [8GB eMMC module](http://ameridroid.com/products/8gb-emmc-black-module-c2-linux) with Ubuntu is currently $21).

Without microSD card overclocking turned on for the Pi, the numbers for the Pi are all basically halved—be wary of any benchmarks that claim the Pi 2/3 are 2x slower than the ODROID-C2 or other boards... the only real difference in that case is the Pi defaults to a more stable slower clock for the microSD reader, but if you have good microSD cards (UHS-1 or better), there's not much risk to overclocking the reader.

### Drupal performance

For _my_ purposes, one of the most comprehensive benchmarks is one that tests the full LEMP stack, pegging all four CPU cores, hitting disk I/O heavily, and consuming most of the onboard RAM. I used the [Drupal Pi](https://github.com/geerlingguy/drupal-pi) project to quickly install the LEMP stack on the ODROID-C2, with Nginx 1.6.x, PHP 7.0.x, and MySQL 5.6.x. It installs a copy of Drupal 8.0.5, which can be a pretty heavyweight application if you bypass all of Drupal's caching. Here are the results:

<p style="text-align: center;">{{< figure src="./odroid-c2-drupal-benchmarks.png" alt="ODROID-C2 - Drupal benchmarks vs Raspberry Pi 3" width="504" height="386" class="insert-image" >}}</p>

The raw stats:

  - Anonymous (cached) requests (Drupal 8.0.5, PHP 7): **183.93 req/s** (128.03 req/s on Pi)
  - Authenticated (uncached) requests (Drupal 8.0.5, PHP 7): **16.18 req/s** (12.02 req/s on Pi)
  - Cached requests (Nginx as reverse proxy): **9,860 req/s** (2,220 req/s on Pi)

The ODROID-C2 is almost 40% faster than the Pi 3 across the board... meaning I'm a little bit tempted to switch a couple of the Pis in my existing Pi Dramble out with ODROID-C2s, just for the nice speed boost! Here are the [full Drupal benchmarks](http://www.pidramble.com/wiki/benchmarks/drupal#single-pi-drupal-8) on a Pi 2 and Pi 3 for comparison.

Note that, when measuring fully cached results—where the network bandwidth is the limiting factor—the ODROID-C2 blows the Pi out of the water, even if the Pi uses a Gigabit USB 3.0 adapter, due to the incredible speed advantage the onboard 1 Gbps Ethernet provides.

## Summary and recommendations

<p style="text-align: center;">{{< figure src="./single-board-computers-raspberry-pi-zero-3-odroid-c2-a-plus-model-b-orange-pi-plus.jpg" alt="Single board computers - Orange Pi Plus, Raspberry Pi A+, 3 model B, Zero, ODROID-C2" width="640" height="566" class="insert-image" >}}</p>

A few years into the small single-board ARM computer revolution, the playing field is starting to level out; the Raspberry Pi is perpetually the leader in terms of breadth of community and mindshare, while various clone manufacturers try to differentiate based on slightly differing feature sets and spec bumps. Some clones' documentation and community are painfully inadequate, leading to a bad initial experience and frustration with any small issues.

The ODROID-C2 is a very solid competitor to the Raspberry Pi model 3 B, and is anywhere from 2-10x faster than the Pi 3, depending on the operation. It's network performance, CPU performance, and 2 GB of RAM are extremely strong selling points if you thirst for better throughput and smoother UIs when using it for desktop computing. The Mali GPU cores are fast enough to do almost anything you can do on the Raspberry Pi, and the (smaller, but dedicated) community surrounding the ODROID-C2 is quick to help if you run into issues.

The ability to easily install Android or Ubuntu MATE (or one of the community distros, like ODROBIAN) is a benefit, and instructions are readily available (more so than other clones).

One of the best advantages of the C2? You can likely grab one within a few days, shipped via one of Hardkernel's distributors. Good luck getting a Pi 3 at list price in the next few weeks!

The fact that I'm considering adding an ODROID-C2 to my [Raspberry Pi Dramble](http://www.pidramble.com/) cluster should indicate how highly I regard it as an alternative to the Raspberry Pi 3 _for use as a headless server_. For single-board beginners, and for general stability and ongoing support, you'll have more success and happiness starting with a Pi 2 or Pi 3. But for those used to the ecosystem and the limitations of ARM-based Linux, the ODROID-C2 is a very nice product!

You can [buy the ODROID-C2 from ameriDroid](http://ameridroid.com/products/odroid-c2) for $41.95.
