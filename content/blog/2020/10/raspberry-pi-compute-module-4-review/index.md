---
nid: 3043
title: "The Raspberry Pi Compute Module 4 Review"
slug: "raspberry-pi-compute-module-4-review"
date: 2020-10-19T07:08:20+00:00
drupal:
  nid: 3043
  path: /blog/2020/raspberry-pi-compute-module-4-review
  body_format: markdown
  redirects: []
tags:
  - cm4
  - compute module
  - raspberry pi
  - reviews
  - video
  - youtube
---

{{< figure src="./raspberry-pi-compute-module-4-hero.jpg" alt="Raspberry Pi Compute Module 4" width="600" height="376" class="insert-image" >}}

## Introduction

Six years ago, the Raspberry Pi Foundation introduced the [Compute Module](https://www.raspberrypi.org/blog/raspberry-pi-compute-module-new-product/): a teensy-tiny version of the popular Raspberry Pi model B board.

Between then and now, there have been multiple revisions to the Compute Module, like the 3+ I used in my [Raspberry Pi Cluster YouTube series](https://www.youtube.com/watch?v=kgVz4-SEhbE), but they've all had the same basic form factor and a very limited feature set.

But today, that all changes with the fourth generation of the compute module, the [Compute Module 4](https://www.raspberrypi.org/blog/raspberry-pi-compute-module-4/)! Here's a size comparison with the previous-generation Compute Module 3+, some other common Pi models, and an SD and microSD card (remember when the original Pi used a full-size SD card?):

{{< figure src="./raspberry-pi-model-size-comparison.jpg" alt="Raspberry Pi Compute Module 4 size comparison with Zero W, 4 model B, 3+, and microSD card" width="700" height="458" class="insert-image" >}}

## Video version of this post

I also posted a video review of the Compute Module 4, embedded below (scroll past it for the blog post version of the review):

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/HUamq0ey8_M" frameborder='0' allowfullscreen></iframe></div>

> **Update**: I also did a [Live Q&A and Demo Video](https://www.youtube.com/watch?v=vc_Lh_a1BQI) which has another hour of content going deeper into things I couldn't cover in the review!

## Compute Module 4 Overview

The Compute Module 4 is basically a Raspberry Pi 4 model B, with all the ports cut off. Instead of the ports, you plug the Compute Module into another board with its special board-to-board connectors. But the Compute module has a few other tricks up its sleeve:

  - **Faster eMMC**: It has optional onboard eMMC storage, which is now much faster than any microSD card I've tested
  - **PCI Express**: It drops the USB 3.0 interface for a PCI Express interface, meaning you can do some pretty cool things in lieu of having a couple USB 3.0 ports.
  - **WiFi and U.FL**: It has an external antenna connector for its wireless interface. What's that? Oh yes, there's now a version of the Compute Module with Bluetooth and WiFi!
  - **More Options**: There are now _thirty two_ different Compute Module flavors to choose from, whether you want onboard WiFi or not, whether you want eMMC storage, or whether you want 1, 2, 4, or even _eight_ gigabytes of RAM!

You can find all the details on the Raspberry Pi website, but here are the highlights:

The cheapest CM4 is the Lite version with 1 GB of RAM, no wireless, and no onboard storage, and that'll run just $25.

The most expensive, creme-de-la-creme version, with WiFi, Bluetooth, 8 GB of RAM, and 32 GB of faster eMMC storage, costs $90.

But to use the Compute Module 4, you will either need to build your own board to integrate it, or buy the Pi Foundation's new [Compute Module 4 IO Board](https://www.raspberrypi.org/products/compute-module-4-io-board/), which is an extra $35. This board turns your Compute Module 4 into a Pi 4 on steroids, because it has all the ports on a standard model B Pi and then some. The only thing lacking is built-in USB 3.0 ports, and that's one of the differences that made me do a double-take.

I remember earlier this year, [Eben Upton mentioned in a podcast](https://www.cnx-software.com/2020/07/17/raspberry-pi-compute-module-4-coming-next-year-with-pcie-nvme-support/) that the Raspberry Pi would someday have its PCIe 1x interface exposed directly. And now it is!

{{< figure src="./raspberry-pi-pcie-slot-compute-module-4-io-board.jpeg" alt="Raspberry Pi Compute Module 4 PCIe slot on IO Board" width="600" height="400" class="insert-image" >}}

You get this nice PCIe port on the IO board, and you can plug in any PCIe device, as long as it only uses 'one lane' of capacity. For example, if you just want to have a couple USB 3.0 ports like you would on a model B, you can plug in an adapter like the [Syba USB 3.1 PCI express card](https://www.amazon.com/gp/product/B019LHYSMI/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=6b7c4ddbff1ced6aed3ab6f3bac1fe90&language=en_US) I used:

{{< figure src="./syba-usb-3-pcie-adapter-in-compute-module-4-io-board.jpeg" alt="Syba USB 3.1 PCIe adapter board in Raspberry Pi Compute Module 4 IO board" width="600" height="387" class="insert-image" >}}

Or... if you want to get bleeding-edge performance out of disk storage, pop in an NVMe adapter with an NVMe, and enjoy the fastest disk IO ever—at least on a Raspberry Pi:

{{< figure src="./nvme-raspberry-pi-4-compute-module-samsung-evo-plus-970.jpeg" alt="Samsung EVO Plus 970 SSD NVMe in Raspberry Pi Compute Module PCIe slot" width="600" height="458" class="insert-image" >}}

I'll be posting a video on [my YouTube channel](https://www.youtube.com/c/JeffGeerling) about all the new disk options on the Compute Module 4, so be sure to subscribe to my channel for that, but I'll talk about performance a little later in this post.

## A Complete Redesign

First, I want to talk a little bit about why the Compute Module is a complete redesign from past versions:

A few of the things I noted in my [Turing Pi cluster review](/blog/2020/raspberry-pi-cluster-episode-6-turing-pi-review) included the lack of enough power and board space to fit in all the features the Pi 4 crams into its small package, especially the un-throttled 1.5 GHz clock of the Pi 4's system on a chip.

Also, because of the physical constraints of the DIMM form factor, it would've been impossible (at least, according to my eyes) to include all the features like WiFi, with a built-in antenna, eMMC storage, and an ethernet controller chip.

For all these reasons, and to make it easier to affix the Compute Module to different boards, a more specialized 'board to board' connector was used. There are two of them, and they each have 100 pins, to connect power, IO, and the GPIO pins to the Compute Module:

{{< figure src="./board-to-board-connector-compute-module-4.jpeg" alt="Board-to-Board Connector 100-pin Raspberry Pi Compute Module 4" width="600" height="419" class="insert-image" >}}

One of the biggest changes from the CM3 plus and earlier is the CM4 now includes an onboard gigabit ethernet controller, so you can get the best network performance possible without a manufacturer having to include it on an external IO board or using an external adapter.

## About that PCIe Slot

The headline feature, though, especially for me, is the PCIe slot. But to be clear, this is the smallest PCIe flavor, with just 1 'lane', or '1x' bandwidth available. So, not to burst your bubble, but you won't be able to use an [Nvidia RTX 3080](https://www.amazon.com/NVIDIA-GEFORCE-RTX-2080-Founders/dp/B07HWMDDMK/ref=as_li_ss_tl?dchild=1&keywords=nvidia+rtx+3080&qid=1602622462&s=electronics&sr=1-1&linkCode=ll1&tag=mmjjg-20&linkId=772390fa53acfe9ac335e90b3917c500&language=en_US) on your Raspberry Pi. It still won't run your favorite PC game at 8K resolution and 240 fps.

### USB 3.0

But it _will_ run a lot of things. For starters, if you are in love with USB 3.0 and are sad to see it missing here, you can buy a USB 3 PCIe expansion card, but be sure it uses the VLI VL805 chipset, otherwise it might not be fully compatible with Raspberry Pi OS and you'll get stuck with USB 2.0 speeds.

I actually bought _three_ different PCIe USB 3.0 cards to see how they worked, and two of the three didn't provide USB 3.0 throughput for most of my devices. They kept mounting drives at USB 2.0 speeds, which was very annoying.

{{< figure src="./usb-pcie-adapter-cards.jpeg" alt="USB 3.0 PCIe x1 Adapter Cards" width="600" height="280" class="insert-image" >}}

(From left to right:) The first was a generic "PCI-Experss" card from [A ADWITS](https://www.amazon.com/gp/product/B07RWKV2D2/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=4662b851e06627ffacd2e43a188dc169&language=en_US)—and no, I that's not a typo, that's how it's spelled on the box—has the VL805 chip in it, but it only mounted a couple of my USB 3.0 drives at that rate. The others, like the fastest one I've tested on a Pi 4, mounted as a USB 2.0 device, and was very slow, but worked fine otherwise.

I had higher hopes for the [2 port Inateck card](https://www.amazon.com/gp/product/B00JFR2H64/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=d7cc2e859ef6daa777f1c1b8f8552e84&language=en_US), but was nervous about the Fresco Logic chip on it. As it turns out, it had similar issues, where it would mount some drives at USB 3.0 speeds _sometimes_, but not always.

The best USB 3.0 card I tested was the [Syba SD-PEX20199](https://www.amazon.com/gp/product/B019LHYSMI/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=cdb61cd5a0792c7f80418dd95ac59558&language=en_US), and it even includes a USB Type-C slot! It mounted all my devices at USB 3.0 speeds, and worked perfectly with the Raspberry Pi. Just be careful plugging in power-hungry devices; it can only put through a little power since it shares the 12v power supply with the IO board itself!

### NVMe

The thing I was most excited about was NVMe support. I had to find out if an NVMe drive attached directly to the Raspberry Pi's PCIe bus would be faster than one connected through a USB 3.0 slot.

So I plugged my [XPG SX6000 drive](https://www.amazon.com/XPG-SX6000-Gen3x4-1500MB-ASX6000PNP-1TT-C/dp/B07H53JT77/ref=as_li_ss_tl?dchild=1&keywords=xpg+sx6000&qid=1602622729&sr=8-1&th=1&linkCode=ll1&tag=mmjjg-20&linkId=0457f9707a627e07f40e58eeda172c98&language=en_US) into [this PCIe to NVMe adapter](https://www.amazon.com/gp/product/B07JQD2WBN/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=a536ea3f463733f81d5885747b96e92d&language=en_US) and... nothing.

So I bought [two](https://www.amazon.com/gp/product/B082D6RF6S/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=f5d617f5d70d22dd7e7e6ec91890a4a7&language=en_US) [other](https://www.amazon.com/gp/product/B07HRLBVXB/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=805db83311ee4ce4f086f528a9196cf2&language=en_US) NVMe to PCIe adapters and... nothing!

I should note here that NVMe support is _not_ enabled out of the box on Raspberry Pi OS. You have to run the command `modprobe nvme-core` and then reboot to enable the NVMe kernel module.

Anyways, I could use the command `lspci` and see the NVMe controller from Realtek was at least recognized, but the drive itself wouldn't show up, and I found some weird errors in the system's logs using `dmesg`:

{{< figure src="./lspci-dmesg-pi-compute-module-4-nvme-realtek.png" alt="dmesg error output for Realtek NVMe drive on Compute Module 4" width="600" height="168" class="insert-image" >}}

So I bought another spare NVMe drive for testing, the [Samsung 970 EVO Plus](https://www.amazon.com/gp/product/B07MG119KG/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=9c763dd9f80d8e51d35b45f03c8920b4&language=en_US), which is a bit more expensive than the XPG drive. I popped it in the adapter, and booted the Pi.

Bingo! I was able to see the device using `lsblk`, so I formatted it and mounted it for testing.

And let me tell you, it is _fast_. You're hearing it here, first. The Raspberry Pi Compute Module 4 offers the fastest disk IO of any Raspberry Pi yet.

Here's a graph of the four main storage options for the Compute Module:

{{< figure src="./cm4-disk-performance-emmc-usb-nvme.png" alt="Compute Module 4 - eMMC, microSD, USB, and NVMe performance benchmark" width="600" height="320" class="insert-image" >}}

You can see the performance of USB 3.0 or NVMe drives is far beyond that of onboard eMMC or microSD cards. SSDs are incredibly fast for sequential writes for large files, but what really sets this Pi apart is the ability to get native NVMe performance, which more than doubles the 4K performance over a USB 3.0-attached drive—check out that 4K random write speed!

Sadly, you can't use an NVMe drive as a boot volume, at least not yet. I think it would be awesome if I could use a few Lite CM4s with NVMe drives in a tiny cluster that would absolutely knock the socks off the [Turing Pi cluster](https://github.com/geerlingguy/turing-pi-cluster) I built earlier this year.

Speaking of, I heard from [Turing Machines](https://turingpi.com) that they **do** plan on building a new 'version 2' board with full support for the Compute Module 4, and I can't wait to see how it turns out!

### Video Cards?

All right, so you can get USB or NVMe over the PCIe bus, but what about upgraded video cards?

Well, there _are_ some slower PCI video cards that work with just a 1x bus, but most of them either have no drivers for Linux (so they wouldn't work with Raspberry Pi OS), or if they _do_ have Linux drivers, the drivers are only available for 'x86' processors. The Pi uses an 'arm' processor, which would not work with the x86 drivers.

Anyways, in all my searching, I could only find _one_ PCI video card that seems like it would be hardware-compatible with the Compute Module 4, the [ZOTAC GeForce GT 710](https://amzn.to/36CTTf5). Note that I said _hardware_ compatible. The graphics chip has Linux drivers, but only for X86. There might be a way to get it running, but I'm not sure. What do you think? Leave a comment if you want me to try to buy one of these cards and test it out on the Pi!

### Other PCI accessories

There are a number of other adapters you can get for PCIe, including SATA adapters for hard drives and SSDs, sound cards, printer ports, network adapters, and even old parallel port adapters! The most important thing to look at is whether the card has Linux support. Some things are supported out of the box, but for other things, you need to install a driver, and it has to be compatible with not only _Linux_, but also the ARM processor architecture.

## Networking

The other headline feature compared to the older Compute Modules is the inclusion of onboard WiFi _and_ Gigabit Ethernet. You can choose whether to get Wifi and Bluetooth, but all versions come with gigabit ethernet built in, courtesy of this little Broadcom chip:

{{< figure src="./broadcom-chip-gigabit-ethernet-raspberry-pi-compute-module-4.jpeg" alt="Broadcom Gigabit Ethernet controller for Raspberry Pi Compute Module 4" width="600" height="400" class="insert-image" >}}

The CM4 performs just as well as a Pi 4 model B in my testing.

{{< figure src="./cm4-networking-performance.png" alt="Compute Module 4 - network and WiFi performance benchmark" width="600" height="303" class="insert-image" >}}

The wired network gets 942 Mbps, which is about as fast as I've seen on my home gigabit network, and it's infinitely faster than the older Compute Module boards—which have no onboard networking at all! Even with the Turing Pi cluster board, it only gave you 100 Mbps per Compute Module, so this alone is a HUGE improvement.

And wireless, which is also not available at all on older Compute Module versions, gets up to 80 Mbps on my home 802.11ac network. Now, here's where it gets a little more interesting. The CM4 is the first Pi of any type to offer a [U.FL](https://en.wikipedia.org/wiki/Hirose_U.FL) antenna connector. Because many people who integrate the CM4 into a device may put it inside a metal enclosure, if they want WiFi to work, they need to attach an external antenna.

The Pi Foundation will sell you a certified antenna you can plug into this tiny connector, and that antenna can then be mounted somewhere to allow the Pi to still get a solid WiFi connection.

{{< figure src="./ufl-antenna-raspberry-pi-compute-module-4.jpeg" alt="U.FL connector and antenna plugged into Raspberry Pi Compute Module 4 for WiFi" width="600" height="418" class="insert-image" >}}

But _technically_ (and you didn't hear this from me!), you could grab any standard U.FL antenna like the [Highfine U.FL antenna](https://www.amazon.com/gp/product/B01GMBUS8O/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=597ec050a9ffa7099903c5456ab077a8&language=en_US) I have, and use it.

To enable the antenna connector (and disable the built-in PCB antenna), you need to edit the `/boot/config.txt` file on your Pi, and add the following line, then reboot the Pi:

```
# Switch to external antenna.
dtparam=ant2
```

I did some testing with this antenna just to compare the tiny built in triangle antenna on the PCB, and the results surprised me.

{{< figure src="./raspberry-pi-compute-module-4-wifi-antenna-comparison.png" alt="Raspberry Pi Compute Module 4 WiFi antenna comparison" width="600" height="356" class="insert-image" >}}

With the built-in PCB antenna, the signal level was -43 dBm (measured with `cat /proc/net/wireless`), with a quality rating of 67/70 (measured with `iwlist wlan0 scanning`). And that's pretty respectable, even though my router is only about 20 feet away. With the external antenna, I could get -40 dBm (with a quality rating of 70/70), but that was only after I adjusted its position a bit to get the best possible signal.

If I unplugged the antenna, the signal was terrible, at -74 dBm with a quality of 36/70, and it could only do about 6 Mbps. So the onboard antenna is a great design—as long you're not enclosing the Pi in a metal box or faraday cage!

So for both wireless and wired networking, the CM4 is on par with the regular Pi 4, and far beyond the capability of earlier Compute Modules—it surprised me how much functionality is crammed into such a tiny board.

## CPU

If you've used the Pi 4, you know what you'll be getting with the CM4, performance-wise. But if you used the Compute Module 3+ or an older version, the Compute Module 4 is a huge leap in performance, for a few different reasons.

First, the CPU clock was increased from an underclocked 1.2 GHz to 1.5 GHz. Second, the CPU is upgrade from a Cortex A53 to an A72, and that means there's more bandwidth, more caches, and all-around better performance even at the same clock speeds.

But don't take my word for it. Here are some benchmarks between the Compute Module versions:

{{< figure src="./cm4-cpu-performance.png" alt="Compute Module 4 - Phoronix CPU performance benchmark" width="600" height="498" class="insert-image" >}}

These three benchmarks represent some real-world scenarios that require good CPU performance to run well. In every case, the Compute Module 4 is _twice_ as fast as the previous 3+. It's barely even a contest.

In real-world use, for things like web browsing and playing games, the difference isn't usually as stark, but it does feel a lot faster, and every time I go back to my 3+ I realize how big the performance gap is.

## eMMC Storage

{{< figure src="./raspberry-pi-compute-module-4-emmc.jpeg" alt="Raspberry Pi Compute Module 4 - eMMC" width="600" height="400" class="insert-image" >}}

Some people spend a bit of time working with external storage and try to get the best disk performance possible. But for most people considering the Compute Module (especially for embedded use), the built-in eMMC offers the best performance for the dollar.

The Pi engineers increased the eMMC bus from 4 bits to [8 bits](https://elinux.org/Tests:eMMC-8bit-width), so you can get more bandwidth out of the eMMC storage. And it really shows in the benchmarks I ran:

{{< figure src="./cm4-disk-performance-emmc.png" alt="Compute Module 4 - eMMC disk performance benchmark" width="600" height="314" class="insert-image" >}}

Random IO is _twice_ as fast on the CM4 than it was on the CM3. And sequential performance is a way better too. The Compute Module 3's eMMC had slower sequential performance than the fastest microSD cards I tested, but the CM4 is neck-in-neck, meaning there are no tradeoffs with eMMC storage on the Compute Module anymore.

And since random IO is more important for most computing tasks, that makes built-in eMMC the best option for most people, especially since it keeps the whole compute module package tiny, so it'll fit almost anywhere.

Now, if you need to flash a new OS to the eMMC, it's a little more complicated than doing the same thing with a microSD card, but thanks to Raspberry Pi's [`usbboot` utility](https://github.com/raspberrypi/usbboot), it's not too hard as long as you have another computer or Pi handy. I'll cover how to do that in a later video.

### USB Boot?

Speaking of USB boot, what about booting the Compute Module from a USB drive? After all, I did a [whole post on how to USB boot with the Pi 4](/blog/2020/im-booting-my-raspberry-pi-4-usb-ssd). Can you do it on the Compute Module? Well, yes, but if you want USB 3.0 speeds, you'll need to drop a PCIe USB adapter card in the single PCI express slot and plug in your drive through that. The ports from the Pi itself on the IO board are USB 2.0 only.

But it works just as well as on the Pi 4, assuming you use a USB 3.0 adapter.

I was _really_ hoping to be able to boot the Pi off an NVMe and do some more testing that way, but alas that is not yet supported, and if you try it with a Lite Compute Module, the Pi just sits there looking aimlessly at microSD, then USB, then microSD, forever:

{{< figure src="./raspberry-pi-compute-module-searching-for-boot-drive.gif" alt="Raspberry Pi trying to find boot volume USB MSD or microSD SD card" width="480" height="270" class="insert-image" >}}

_Technically_ you can still boot off an NVMe, but only if you put it in a USB 3.0 adapter, plugged into a USB 3.0 PCI adapter... but that's not the same as booting directly off an NVMe drive and you miss out on a lot of performance!

### NFS Performance

One other thing I wanted to check is how well the Compute Module performs as an NFS (Networked File System) server. I currently have an old 2011 Mac mini that I still use to store many terabytes of old video files and backups of my computers, but it's so old it's not even supported by Apple anymore.

So I wanted to see if the Compute Module could be faster than the ten-year-old Mac mini for file storage, and—spoiler alert—it is!

{{< figure src="./cm4-nfs-performance.png" alt="Compute Module 4 - NFS network copy performance benchmark" width="600" height="284" class="insert-image" >}}

On the Mac mini, the fastest consistent write speed I could get is around 35 MB per second, mostly because the drives are all attached to old USB 2.0 ports. On the Pi, if I wrote to either an external USB 3.0 drive or an NVMe drive, I could write over the network at about 70 MB per second (2x faster than the old Mac mini).

Now, a _brand new_ Mac mini would saturate the network's bandwidth and give me somewhere around 100 MB per second, but that would also cost at least $800, and that's a lot to pay to get that extra 30 MB per second.

## IO Board - New Features

All right, so enough of the Compute Module itself, it is, to put it in the words of Steve Jobs, a 'screamer' compared to all the previous Pis.

What about its official companion development board?

{{< figure src="./raspberry-pi-compute-module-4-io-board.jpeg" alt="Raspberry Pi Compute Module 4 IO Board" width="600" height="417" class="insert-image" >}}

The Compute Module 4 IO board has a few new tricks up its sleeve, too.

Not only does it have all the same breakouts and connections that the old IO board had, it also has PoE (Power over Ethernet) support (provided you add an appropriate PoE or PoE+ HAT), so you can power the board from an Ethernet cable.

We've already covered the PCIe slot, but right above it is a 4-pin PSU connector that can be used to provide power to accessories, as well as a 4-pin fan connector that can power and control a fan.

Down along the bottom, there's a 12v barrel plug power jack. I'm using this jack to power the IO board using a generic [TMEZON 12v 2A power adapter](https://www.amazon.com/gp/product/B00Q2E5IXW/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=cfb0cd370d26ca089cf5825180c2ccdb&language=en_US). Any power adapter should work as long as it supplies 12v at 2A or more, and has a 2.1mm X 5.5mm barrel plug.

Then there's a microSD card slot for use with the Compute Module Lite version (the slot isn't recognized at all for eMMC versions), two USB 2.0 ports (along with a header for two more USB ports), and the RJ45 network jack.

It also has two full-size HDMI ports so you can drive up to two external displays.

{{< figure src="./raspberry-pi-hdmi-mini-micro-full-size.jpeg" alt="HDMI ports on various generations of Raspberry Pi" width="600" height="400" class="insert-image" >}}

It's interesting that they're _full-size_, because now when I'm switching between my Pi projects I have to deal with the following:

  - Full-size HDMI on the original Pi, Pi 2, Pi 3, and Pi 3+
  - Mini HDMI on the Pi Zero
  - Micro HDMI on the Pi 4
  - Full-size HDMI on the IO board

Go figure! People who complain about USB-C dongles have not had to put up with testing multiple generations of Raspberry Pi :)

There's a built in RTC, or Real-Time Clock, with a slot for a standard CR2032 backup battery.

And there's a standard HAT ('Hardware Attached on Top') connector, and it allows you to interface with the Pi's GPIO. It has mounting holes in the same place as a standard Pi B model, so you can mount HATs within the board's footprint. And finally there are some display and camera connectors along the side and top edge, along with a set of jumpers to help when flashing an eMMC module or to disable firmware updates.

There are two things I think I could call out as downsides to the IO board and Compute Module board-to-board designs: first, the IO board is pretty large. I understand why, since it support _every_ feature of the CM4, including mounting full-size Pi HATs, but it would be nice if it took up a little less desk space even if a few features were dropped.

Second, having two 100 pin board-to-board connectors close together makes attaching and removing the Compute Module a slight bit more tricky than it should be. You're _supposed_ to pull straight up to detach the module, but it's pretty much impossible to do that unless you use spudgers. With your fingers, you kind of have to pry up one side first, and then the module pops out. Plugging it in is a little easier, since you can just push down with equal pressure on both sides.

{{< figure src="./board-to-board-underside-raspberry-pi-compute-module-4.jpeg" alt="Underside of the Raspberry Pi Compute Module 4, showing board-to-board connectors" width="600" height="395" class="insert-image" >}}

There are a ton of other little details that I haven't had time to convey in this post, but I think the Pi Foundation did a great job with this board, given the constraints of the form factor and price. I'm sure keeping the new version starting at the same price as the old version was no small feat!

## Summary

I'm really happy with the Compute Module 4. It delivers on the promise of native PCIe support, and uses a form factor that will fit well into embedded systems, with some great new features like onboard WiFi, Bluetooth, and Ethernet, and substantial performance improvements to boot!

{{< figure src="./turing-pi-cluster-board.jpeg" alt="Turing Pi Cluster Board for Raspberry Pi Compute Module" width="600" height="401" class="insert-image" >}}

As I mentioned earlier in the post, I also talked to Turing Machines and they said they're already hard at work on a 'version 2' of their [Turing Pi](https://turingpi.com) cluster board. Once that comes out, I'm going to do all I can to get it immediately, load it up with Compute Modules, and rebuild my [Pi Dramble](http://www.pidramble.com) cluster on it.

> **Edit**: Turing Machines have _officially_ announced the [Turing Pi V2](https://turingpi.com/turing-pi-2/). I'm excited to see it!

The Compute Module 4 offers all the performance of the Pi 4 model B, far surpassing the features and performance of the Compute Module 3+ and all the other versions that came before.

Check out the Compute Module 4 on the Raspberry Pi website and see where you can buy one: [Compute Module 4](https://www.raspberrypi.org/products/compute-module-4/).
