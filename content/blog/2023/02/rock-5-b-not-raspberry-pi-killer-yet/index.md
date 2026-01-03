---
nid: 3269
title: "The Rock 5 B is not a Raspberry Pi killer\u2014yet"
slug: "rock-5-b-not-raspberry-pi-killer-yet"
date: 2023-02-01T15:00:19+00:00
drupal:
  nid: 3269
  path: /blog/2023/rock-5-b-not-raspberry-pi-killer-yet
  body_format: markdown
  redirects:
    - /blog/2023/rock-5-b-not-raspberry-pi-killer—yet
aliases:
  - /blog/2023/rock-5-b-not-raspberry-pi-killer—yet
tags:
  - radxa
  - raspberry pi
  - reviews
  - rk3588
  - rock 5
  - rockchip
  - sbc
  - video
  - youtube
---

{{< figure src="./rock-5-model-b-knolling.jpg" alt="Rock 5 model B on desk with Raspberry Pi in background" width="700" height="394" class="insert-image" >}}

Radxa's Rock 5 model B is an ARM single board computer that's _3x faster_ than a Raspberry Pi. And that's just the 8-core CPU—with PCI Express Gen 3 x4 (the Pi has Gen 2 x1), storage is _7x faster_! I got over 3 GB/sec with a KIOXIA XG6 NVMe SSD.

It's still half as slow as modern ARM desktops like Apple's M1 mini, or Microsoft's Dev Kit 2023 ([see my review here](/blog/2022/testing-microsofts-windows-dev-kit-2023)). But it's way faster than a Pi, it comes with 2.5 Gig Ethernet, it has two M.2 slots on board... and, well—it also starts at $150!

So you get what you pay for, in terms of performance. But I wanted to know: for a premium SBC price, do you get a better experience?

The thing that turns me off with so many Pi alternatives is how hard it is to go from unboxing the board to actually _using_ it. Being able to just plug it in, install an OS, and... do stuff.

But for Linux, and for running open source software, how does this board stack up? Is it worth paying $150-220 for a more premium SBC?

{{< figure src="./15-lenovo-m710q-tiny-pc.jpg" alt="Lenovo Tiny PC m710q" width="700" height="394" class="insert-image" >}}

Or for that price should you just go ahead and buy a used TinyMiniMicro PC, like the Lenovo M710q (pictured above) with a full Intel Core i7 processor, an enclosure, a hard drive, WiFi, and a power supply! And this thing has upgradeable RAM, too!

So how does the Rock 5 model B stack up?

_If you'd rather watch the video instead of read this blog post—watch my full review of the Rock 5 model B on YouTube:_

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class="embed-container"><iframe src="https://www.youtube.com/embed/CxD_0q8tAdc" frameborder="0" allowfullscreen=""></iframe></div>
</div>

## Specs, price, shipping

This board uses the latest RockChip RK3588 SoC, with an 8 core CPU, a Mali GPU, a 6 TOPS NPU, and 8k encoding and decoding—though, besides the CPU, it's not always easy taking advantage of those other features.

You can get up to 16 GB of RAM, and it can run up to three displays. It says it can do 8K, though it won't perform amazing running anything _on_ an 8K display, just like the Pi performs pretty poorly when you're running a 4K display.

But unlike the Pi, the USB-C port can also do DisplayPort output.

It has an HDMI input, too, but it looks like support for it isn't great yet, if [this Explaining Computers video](https://youtu.be/w85QTDPp-4Q?t=1095) is any indication.

It has built-in 2.5 Gbps Ethernet, two USB 2.0 ports, two USB 3.1 ports, and a mini audio jack.

Up top there's an E-key M.2 for WiFi or other PCI Express devices, and on the bottom, there's _another_ M.2 slot, and this one is a lot more fun. It's M-key for NVMe SSDs, but if you get an [M.2 to x16 PCIe adapter](https://amzn.to/3WXo5b8), you can break out the slot for more interesting things, like graphics cards—see my notes on that later in this post.

{{< figure src="./3-bottom-rock-5-model-b.jpg" alt="Bottom of Rock 5 model B" width="700" height="467" class="insert-image" >}}

The bottom slot only supports 2280 size SSDs, so if you want to use a shorter SSD you need an M.2 [extension adapter](https://amzn.to/3RkuVqa). The killer feature is this slot is PCI Express _Gen 3_ x4. That means you can get up to _4 Gigabytes per second_ through it!

There's also an eMMC socket and a microSD slot, both of which can be used at the same time, and camera and display connectors.

The one I bought is the 4 GB version, and it costs about $150 shipped.

## Initial Setup

To get running, you need a separate power adapter and at _least_ a heatsink. I didn't order the Radxa ones initially, so I stuck on a little heat sink and plugged in a 5v Pi fan.

I wanted to boot the Rock 5 off an NVMe SSD, and apparently you _can_, but it's a bit tricky and you have to reflash a chip on the board using SPI. So I elected to boot off microSD instead.

The [Getting Started Guide on Radxa's Wiki](https://wiki.radxa.com/Rock5/5b/getting_started) was helpful, but I was a little worried when it kept mentioning a USB to TTL serial cable. This was my first time using this thing, and it seemed pretty daunting having the docs suggest I might want to use a serial console on the first boot!

Luckily a monitor, keyboard and mouse worked just fine—maybe the Getting Started Guide could be a little more focused on just, well... _Getting Started_. Leave the complicated stuff for later.

I went to the [download page](https://wiki.radxa.com/Rock5/downloads) and found Android, Debian 11, and Ubuntu images.

{{< figure src="./4-microsd-card-upside-down.jpg" alt="microSD card being inserted upside-down in Rock 5 model B slot" width="700" height="394" class="insert-image" >}}

Once the OS was flashed, I plugged the microSD card in, and noticed the tiny microSD card slot allows plugging the card in upside-down (see picture above)! If you do that, good luck figuring out why it won't boot! I'd rather see a full-size microSD card slot like most other boards have.

## Power Issues

I didn't initially have Radxa's official 30 watt power supply, so I tried the next best thing, my Apple 30W power supply. I mean, 30W is 30W, right?

Wrong.

[Just like the initial version of the Pi 4](https://www.theverge.com/2019/7/10/20688655/raspberry-pi-4-usb-c-port-bug-e-marked-cables-audio-accessory-charging), USB-C power... can be weird. It's not entirely Radxa's fault, though. USB-C power delivery is anything but easy to implement, so I'm not surprised I had issues.

The LED on the board flashed blue and green, but the board kept resetting itself.

My 61W Apple adapter _did_ actually boot. And I also found [this thread on Radxa's forum](https://forum.radxa.com/t/rock5-does-not-work-on-most-pd-power-supplies/12042/6) that gets deeper into power supplies and the Rock 5.

The board's FAQ does have a [section on power supplies](https://wiki.radxa.com/Rock5/FAQs#Power_Supply), and I'd stick with Radxa's recommendation: buy their official power supply. I did, and have had no problems since using it.

## First boot

I booted Debian and saw Linux kernel 5.10—it seems this isn't a full Linux 5.10 build. The Linux images are built with a set of Rockchip patches that are based on older Linux releases.

On top of that, the first time I tried running updates, I got an error about Radxa's apt repository not being signed—but I could at least install `iperf3` so I ignored that error.

I tested the Ethernet adapter, and I got a consistent 2.35 Gbps down, but less than 1 Gbps up (with `--reverse`. That's not symmetrical, but it's still plenty fast.

Power usage was around 4-6W on average, and with my little heatsink and Pi fan, the CPU stayed around 30°C.

{{< figure src="./5-terminal-artifacts-debian-rock-5-b.jpg" alt="Terminal glitchy artifacts in Debian on Rock 5 model B" width="700" height="394" class="insert-image" >}}

Debian's UI was snappy—certainly faster than a Pi—but I did get strange artifacting on the screen sometimes, like when I opened the Terminal and would see these blotchy parts (see image above).

## Performance - CPU

I tried running my [Top500 HPL benchmark](https://github.com/geerlingguy/top500-benchmark), but kept running into `apt` errors. I found [this old forum post from November _2020_](https://forum.radxa.com/t/apt-error-with-latest-buster-image/5074) that had the exact same issue!

The fix was to manually install Radxa's signing key, but it was a bit annoying to have that issue right out of the gate with the latest official Debian image.

With that sorted, I ran Linpack a few different ways—the most efficient is to just use the four A76 performance cores, leaving the four efficiency cores idle. That gave me 46 gflops, using 15W of power. So 3.11 gflops/W.

{{< figure src="./6-gflops-efficiency-hpl-rock-5-b-cm4-raspberry-pi-m1-max-mac-studio.jpg" alt="Efficiency graph - gflops per watt - Rock 5 model B vs Raspberry Pi 4 vs Mac Studio M1 Max" width="700" height="394" class="insert-image" >}}

That's a _lot_ better than the Pi 4, and it's almost as efficient on a per-watt bases as my Mac Studio! It's just... a lot slower than the Mac.

Performance was _slightly_ better running on all 8 cores (47 gflops), but efficiency went down a bit (16W, so 2.94 gflops/W). The slower e-cores are better off just running background tasks.

I also tested different cooling configurations:

  - Fan and heat sink: 65°C under load
  - Fan only: 82°C under load
  - Bare SoC (no fan): 85°C and throttling (but still enough to eke out 45 gflops!)

The whole board gets pretty hot, though, so I would recommend at least a heatsink.

I also ran Geekbench to see how this board stacks up, and the [Rock 5 scored](https://browser.geekbench.com/v5/cpu/18993913) a respectable 565 single-core and 2384 multi-core.

{{< figure src="./7-geekbench-pi-4-rock-5-b-windows-dev-kit-2023.jpg" alt="Geekbench benchmark - Rock 5 model B vs Raspberry Pi 4 vs Windows Dev Kit 2023" width="700" height="394" class="insert-image" >}}

This puts it somewhere between a Raspberry Pi 4 on the lower end, and the Windows Dev Kit 2023 I tested a few months ago.

It's noticeably faster than a Pi, but it's still not a real _desktop_-class processor. It's not even _close_ to M1 performance, let alone newer M2 CPUs. But... it's a single board computer; it's not really meant to be a desktop.

## Performance - Storage

I was most interested in IO performance. There are _four_ lanes of PCI Express Gen 3 in the M.2 slot underneath. The main thing holding the Pi back is IO. I've taken the single PCI Express lane exposed on the Compute Module 4 to the _limit_ over and over again, and it maxes out at 420 MB/sec.

Besides Radxa not including an M.2 screw, I have nothing but good things to say here.

I installed a KIOXIA XG6 drive, and it shows up running at full speed with `lspci`. Testing it out with my disk benchmarking script, I got up to _3 GB/sec_ in sequential reads.

{{< figure src="./8-nvme-ssd-rock-5-model-b-3-gb-sec-fio.jpg" alt="fio benchmark result PCIe Gen 3 NVMe SSD Kioxia XG6" width="700" height="394" class="insert-image" >}}

Even random access was three times faster than the Pi, clocking in at 1.3 GB/sec.

_Booting_ from an SSD requires flashing a chip on the board over SPI, and that's not something for the feint of heart, but it's not that much different than upgrading the Compute Module's EEPROM. I just haven't tried it out yet.

## Advanced Features

{{< figure src="./9-ae-key-m2-wifi-intel-ax210ngw-rock-5.jpg" alt="Intel AX210 WiFi 6E M.2 card in Rock 5 model B top slot A+E key" width="700" height="394" class="insert-image" >}}

I also wanted to test the top A+E key M.2 slot. It's perfect for WiFi and I had an Intel AX210 I recently [tested to 1.5 Gbps on the Raspberry Pi](/blog/2023/getting-15-gbps-wifi-6e-on-raspberry-pi-cm4).

I tried getting it working on the Rock 5, but ran into issues. Bluetooth didn't work at all (which is a known issue), but I also couldn't install Intel's firmware since there was already some Intel firmware built with Rockchip sources.

The card would show up using `nmcli`, but I wasn't able to scan for networks or get connected, and the 6 GHz band is definitely not supported yet, even though I could get that working on the Pi.

Other people in the forums mentioned getting the AX210 working, though, so it was probably a bug I ran into. Radxa sells their own M.2 WiFi adapter, and for best out-of-the-box support, that's probably the way to go.

I wanted to test more PCIe devices in the bottom slot, though. In _theory_, any PCIe device can be plugged in using an [M.2 to PCIe x16 adapter](https://amzn.to/3XV0rxg).

I've been plugging any and every PCIe device I could get my hands on into the Raspberry Pi and compiling the results of my testing into my [Pi PCIe device database](https://pipci.jeffgeerling.com)—many drivers tend to have issues with either ARM64 in general, or quirks in the PCIe implementation on the CM4 in particular.

But what about the newer RK3588 SoC? With PCIe Gen 3, a modest graphics card could give a huge boost for video transcoding, streaming, or even light gaming on Linux!

## GPU on Rock 5?

I was even more intrigued when I saw [this tweet](https://twitter.com/theradxa/status/1592374915231289344).

{{< figure src="./10-neofetch-showing-ati-radeon-hd-7470.jpg" alt="Neofetch lies about the active GPU on the Rock 5 model B" width="700" height="394" class="insert-image" >}}

So I plugged in my Radeon HD 7470, installed AMD's firmware, ran `neofetch`, and, well... it's actually lying in the image above. The GPU driver isn't actually loaded, but since it's connected, `neofetch` _thinks_ it's the active GPU.

But it's not. So _of course_ I [recompiled the kernel](https://forum.radxa.com/t/idea-about-plug-amd-gpu-via-nvme/13132/19?u=geerlingguy). But the Rock 5 wouldn't boot with my custom kernel—the blue LED started blinking and it wouldn't give me any output at all. So _for now_ at least, I put a pin in that.

## 10 Gbps M.2 NIC

{{< figure src="./11-innodisk-10gbe-m2-nic.jpg" alt="Innodisk M.2 10 Gbps NIC" width="700" height="394" class="insert-image" >}}

I also wanted to see if [Innodisk's 10 Gbps NIC](https://www.innodisk.com/en/products/embedded-peripheral/communication/egpl-t101) would work—it's the strangest network card I've ever used.

It showed up with `lspci`, so it was just a matter of getting a driver working.

Since there isn't a driver I can download for ARM Linux, I had to compile the driver in the Linux kernel—which I still couldn't get working yet.

So I put that on pause, too. But I will get back to it soon, because four PCI Express Gen 3 lanes affords 8 GT/sec, or about 4 GB/second of bandwidth.

[According to Thomas Kaiser's research](https://github.com/ThomasKaiser/Knowledge/blob/master/articles/Quick_Preview_of_ROCK_5B.md#pcie), I should be able to _bifurcate_ the PCI Express lanes, so I could connect both a 10 gigabit network card _and_ something like a storage controller, to build a pretty powerful NAS.

## Accessories

To round things out, I tested some of Radxa's Rock 5 accessories:

  - The RTC battery plugs into a header on the board and dangles off the edge.
  - The Fan/heatsink combo worked okay, but only after I installed a different [fan control package](https://forum.radxa.com/t/new-fan-rock5b-not-working/13950/6?u=geerlingguy) than the one included with the board. The included thermal paste—if you could call it that—came out more like a gooey snot than a paste, so I used a little [Noctua NT-H2](https://amzn.to/3Dxactr) instead. The fan is not too loud, though at lower speeds the one I had wobbled a bit and that made a more annoying sound.
  - The standalone heatsink is adequate for most any workload, and as long as you're not fully enclosing the board, it should be enough to keep it cool.
  - The 32 gigabyte eMMC module runs a bit faster than the microSD card interface, and unlike the Raspberry Pi CM4, you can use both eMMC _and_ microSD storage at the same time.

## Comparisons

It's time to compare the Rock 5 model B to some of its closest rivals, starting with the Raspberry Pi.

### Raspberry Pi 4

{{< figure src="./12-pi-4-model-b-and-cm4.jpg" alt="Raspberry Pi 4 model B and CM4 on carrier board" width="700" height="384" class="insert-image" >}}

The Rock 5 trounces the Pi in both CPU performance _and_ efficiency.

It's three times faster in Geekbench, it has faster built-in Ethernet, blazing fast M.2 NVMe support, another slot for fast WiFi. It's a different league entirely when it comes to the hardware.

But the software side still requires a bit more knowledge to be productive—and there's still the matter of sketchy Linux support. There are efforts to 'mainline' support for the Rockchip SoC, meaning you could just run plain Linux distros... but those efforts seem to be taking a while.

So right now, I wouldn't recommend this board to just _anyone_, at least when it comes to software and support, due to its high price. 

Then again, I wouldn't recommend anyone [pay over a hundred bucks for a Pi 4, either](https://www.ebay.com/sch/i.html?_from=R40&amp;_nkw=raspberry+pi+4+model+b&amp;_in_kw=1&amp;_ex_kw=&amp;_sacat=0&amp;LH_Sold=1&amp;_udlo=&amp;_udhi=&amp;_samilow=&amp;_samihi=&amp;_sadis=15&amp;_stpos=63119&amp;_sargn=-1%26saslc%3D1&amp;_salic=1&amp;_sop=12&amp;_dmd=1&amp;_ipg=60&amp;LH_Complete=1), but here we are...

### Orange Pi 5

{{< figure src="./13-orange-pi-5-sbc.jpg" alt="Orange Pi 5 SBC with RK3588S" width="700" height="394" class="insert-image" >}}

This Orange Pi 5 uses the same Rockchip RK3588—well, _almost_ the same. The Orange Pi has the RK3588S, which has a [little less bandwidth](https://wiki.radxa.com/Rock5/RK3588_vs_RK3588S) than the chip in the Rock 5.

It has a lone M.2 slot on the bottom running at PCIe Gen 2 speeds, which means this SSD only gets about 400 MB/sec—just as slow as on a Pi. The Orange Pi 5 also only has 1 Gbps Ethernet, and not even a full 40-pin GPIO header, but it _does_ have a full size microSD card slot, so that's an upgrade!

But the Orange Pi 5 _is_ a lot less expensive. You can get [the same CPU and GPU performance](https://browser.geekbench.com/v5/cpu/compare/18993913?baseline=19710032), at least—and in my case it actually benchmarked a tiny bit _faster_—for _half_ the price!

### Khadas Edge 2

{{< figure src="./14-khadas-edge-2-sbc.jpg" alt="Khadas Edge 2 SBC with black background" width="700" height="370" class="insert-image" >}}

The Khadas Edge 2 also uses the slower RK3588 _S_, yet somehow costs _more_ than the Rock 5 model B!

Besides the nicer marketing around Khadas' boards, I'm not quite sure why they cost so much. It doesn't have the same kind of community and support as the Pi, it doesn't have the higher specs of the Rock 5, and this board doesn't even include Ethernet... or an M.2 slot for that matter!

I just don't see the value, especially when Orange Pi has better features for a third of the price. You can buy a [brand-new Ryzen Mini PC](https://amzn.to/3kX65R8) for the price of one of these Edge 2 boards!

### Tiny PC

{{< figure src="./15-lenovo-m710q-tiny-pc.jpg" alt="Lenovo Tiny PC m710q" width="700" height="394" class="insert-image" >}}

Speaking of Mini PCs, there are _tons_ of these little 'thin client' PCs on eBay. I bought this [Lenovo M710q](https://www.ebay.com/itm/295020790427) with everything I needed—even a Windows license—for $120!

It includes a 4-core Intel i5 CPU, a hard drive, WiFi 6, an M.2 slot, and upgradeable memory.

It's a [little faster in Geekbench](https://browser.geekbench.com/v5/cpu/compare/19439821?baseline=18993913), and a [_lot_ faster in Linpack](https://github.com/geerlingguy/top500-benchmark#results), though efficiency is a little lower.

Running Ubuntu, it only uses 8W at idle, which is double the Rock 5, but still pretty efficient—especially considering this thing is spinning a hard drive inside!

But my point is, once you pass the $100 price point, you're competing with mini PCs like this. And once you go into the $200-300 price point, you could even get a brand new Ryzen PC!

## Conclusion

But here I'm more interested in comparing ARM boards. And the Rock 5 is a _huge_ upgrade over the Raspberry Pi 4, in terms of hardware and capability. Everything is faster, and by a _lot_. There's tons more IO, at the expense of a little extra board space.

But at what cost? Assuming Pis ever become available at MSRP again—and right now that still feels a long way off—the Pi still has two major advantages:

  1. A cheaper point of entry ($35)
  2. Better software and support

But focusing just on the _hardware_, the Rock 5, at $150 and up, is in a _completely_ different price class. A tiny PC, complete with Power supply, a case, a hard drive, and _even a Windows license_, costs less than the base model Rock 5. And that's before you even add in necessities for the Rock 5 like a case and power adapter!

Radxa's done a decent job building up the Rock 5 ecosystem around the RK3588. Besides the Raspberry Pi, this is the best experience I've had with an ARM SBC. But it still has a long way to go before I would call it a 'Pi killer'. Docs need to be more beginner-friendly, the community needs to be less insulated in Discord, and the chip needs more mainline support.

I continue to follow Radxa closely, and I'll continue exploring GPU support with the RK3588—so if you're old school like me and still use RSS, make sure you're [subscribe to this blog](https://www.jeffgeerling.com/blog.xml).
