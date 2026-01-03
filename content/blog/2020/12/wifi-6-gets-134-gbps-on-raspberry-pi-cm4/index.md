---
nid: 3059
title: "WiFi 6 gets 1.34 Gbps on the Raspberry Pi CM4"
slug: "wifi-6-gets-134-gbps-on-raspberry-pi-cm4"
date: 2020-12-22T06:07:47+00:00
drupal:
  nid: 3059
  path: /blog/2020/wifi-6-gets-134-gbps-on-raspberry-pi-cm4
  body_format: markdown
  redirects: []
tags:
  - 802.11ax
  - compute module
  - intel
  - pcie
  - performance
  - raspberry pi
  - wifi
  - wifi 6
---

> **January 1, 2021 Update**: My 1.34 Gbps benchmark was flawed. See [this GitHub issue](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/38) and this updated blog post to learn more: [WiFi 6 is not faster than Ethernet on the Raspberry Pi](/blog/2021/wifi-6-not-faster-ethernet-on-raspberry-pi).

{{< figure src="./edup-in-raspberry-pi-wifi-6-compute-module-4-pcie-io-board.jpeg" alt="EDUP Intel AX200 WiFi 6 802.11ax PCIe card in Raspberry Pi Compute Module 4 IO Board" width="600" height="401" class="insert-image" >}}

After buying three wireless cards, a new WiFi router, optimizing my process for cross-compiling the Linux kernel for the Raspberry Pi, installing Intel's WiFi firmware, and patching Intel's wireless driver to make it work on the Raspberry Pi, I benchmarked the [EDUP Intel AX200 WiFi 6 PCIe card](https://amzn.to/3prkSk3) and got **1.34 Gbps of bandwidth** between the Raspberry Pi and a new [ASUS WiFi 6 router](https://amzn.to/3re0KDy).

This is my story.

## The never-ending budget-busting project

Have you ever started a project that should take a couple hours with a fifty dollar budget, and realized at the end you spent a whole month on it and spent close to a thousand bucks?

Yeah, well, this is one of those projects.

{{< figure src="./raspberry-pi-cm4-built-in-wifi-ac.jpeg" alt="Raspberry Pi Built-in WiFi module 802.11ac Compute Module 4" width="600" height="401" class="insert-image" >}}

When I tested the Compute Module 4's onboard WiFi 802.11ac chip, I got up to around 80 Mbps, even when using an external antenna.

{{< figure src="./asus-ac51-wifi-pcie-ac-card.jpeg" alt="ASUS AC51 Wireless WiFi 802.11ac PCIe card" width="600" height="415" class="insert-image" >}}

I wondered if I could get better performance with a PCI express card. So I bought an [ASUS AC51 PCIe card](https://amzn.to/3ldzLVn) that has a Realtek chip inside, and I spent a few days debugging Realtek's Linux drivers. Eventually, though, I gave up, because most people on Linux seem use a USB version, not PCI express. If you want to read more about that failure, [check out this GitHub issue on the ASUS AC51](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/20).

So after a little more research on well-supported WiFi chipsets on Linux, I settled on the [EDUP Intel AX200 PCIe card](https://amzn.to/3ar3Pu3) pictured at the top of this post. From what I read online, the `iwlwifi` drivers it requires are used a lot more widely, in a variety of desktops and laptops running Linux.

## Video with extra details

The blog post continues below, but if you're more visually-inclined, I also posted this video about WiFi 6 on the Pi:

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/csI19aOJEik" frameborder='0' allowfullscreen></iframe></div>

Apologies for the thumbnail—it performs a thousand times better than not-open-mouthed-Jeff in my A/B testing.

## What's AX? What happened to AC?

But before we get to the card, what's 802.11ax and what's WiFi 6?

{{< figure src="./airport-graphite-original-wifi-router.jpeg" alt="Apple AirPort WiFi Router" width="600" height="404" class="insert-image" >}}

In WiFi's early days, when Apple's [AirPort](https://en.wikipedia.org/wiki/AirPort#AirPort_Base_Station) was all the rage, and we had 802.11b WiFi, with a theoretical maximum speed of 11 Mbps.

In the past couple decades, we had 802.11a and g with 54 Mbps, 802.11n (AKA WiFi 4) with 300-600 Mbps and using either the 2.4 or 5 gigahertz spectrum, and more recently, 802.11ac (AKA WiFi 5) with up to 1.3 Gbps on the 5 gigahertz band.

{{< figure src="./wifi-bandwidth-standards.png" alt="WiFi bandwidth history 2000-2020" width="700" height="357" class="insert-image" >}}

There are some other standards I'm skipping over, but last year the 802.11ax standard was christened as 'WiFi 6', and it's now the gold standard, allowing a theoretical maximum of 10 Gbps over the 5 gigahertz band.

## Getting the card to work

Now, back to the PCI express card. It fits nicely in the 1x slot on the Compute Module 4 IO board without the need for any adapters.

The first thing I do with all the boards I test is boot the Pi and see what I can see using `lspci`:

```
$ sudo lspci -vvv
...
01:00.0 Network controller: Intel Corporation Device 2723 (rev 1a)
```

Since the board showed up, I also ran `dmesg` and looked for the PCI express initialization section, to make sure there weren't any BAR space issues:

```
[    0.940759] pci 0000:00:00.0: BAR 8: assigned [mem 0x600000000-0x6000fffff]
[    0.940790] pci 0000:01:00.0: BAR 0: assigned [mem 0x600000000-0x600003fff 64bit]
```

GPUs and some other cards I've tested run into BAR allocation issues, but this card seemed to be fine.

I also ran `ip a` to see if by some dumb luck, the card was already supported in Pi OS, but I had no such luck. Only the built-in `wlan0` interface was listed alongside `local` and `eth0`.

It looks like it's time to recompile the kernel!

And after going through the struggle of recompiling the Linux kernel almost a dozen times for my [first Pi GPU testing video](https://www.youtube.com/watch?v=ikpgZu6kLKE), I decided to set up a reliable cross-compile environment on my Mac, which has a much faster processor.

## Cross-compiling the kernel

The environment is built inside a virtual machine on my Mac, and the main reason for that is it's hard to mount the Raspberry Pi ext4 filesystem on my Mac (even with Docker for Mac), but it's easy to do inside a Linux VM under VirtualBox. I have to do that to be able to copy the compiled kernel into place for the Pi when using microSD cards.

> There are other ways to do this, e.g. copying driver-specific files over the network instead of the entire kernel, or using netboot—but for now this is how I'm doing it since it's reliable and repeatable in a variety of situations.

The full instructions for cross-compiling are available in my [Raspberry Pi PCIe project](https://pipci.jeffgeerling.com) repo on GitHub: [Raspberry Pi Linux Cross-compilation Environment](https://github.com/geerlingguy/raspberry-pi-pcie-devices/tree/master/extras/cross-compile).

{{< figure src="./intel-iwlwifi-support-kernel-menuconfig.jpg" alt="iwlwifi enable MVM kernel support for Intel AX200 driver menuconfig compile Linux" width="700" height="394" class="insert-image" >}}

The most important thing is to configure the kernel using `menuconfig` (or by hand if you so wish), and to enable the following options:

  - Device Drivers > Network device support > Wireless LAN > Intel > "Intel Wireless WiFi Next Gen AGN (iwlwifi)"
  - "Intel Wireless WiFi MVM Firmware support" (under the iwlwifi option, once selected)

Once that configuration is saved, compile the kernel. On my Mac, in the VM, it takes around 10 minutes. On the Pi 4, it takes around an hour!

> Need more help and details? Check out the video I made on the entire process here: [WiFi 6 on the Raspberry Pi CM4 makes it Fly!](https://www.youtube.com/watch?v=csI19aOJEik).

Once the compile is done, follow the rest of the instructions to copy the built kernel, dtbs, etc. over to the microSD card (assuming you're using a CM4 Lite—otherwise mount the eMMC version of the CM4 separately).

After all the copying was finished, I unmounted both partitions, and shut down the VM. I pulled the microSD card from my Mac, put it back in the Pi, booted it up, and crossed my fingers!

## Installing the Intel WiFi Firmware

I logged into the Pi and ran `dmesg` to check the logs... and I realized there must be something missing, because I saw the message `no suitable firmware found`!

I also had to install the appropriate device firmware from the [Linux Wireless](https://wireless.wiki.kernel.org) website. I found the driver download for the AX200 on the [Intel wireless driver page](https://wireless.wiki.kernel.org/en/users/drivers/iwlwifi), and installed it on the Pi like so:

```
$ wget https://wireless.wiki.kernel.org/_media/en/users/drivers/iwlwifi/iwlwifi-cc-46.3cfab8da.0.tgz
$ tar -xvzf iwlwifi-cc-46.3cfab8da.0.tgz
$ cd iwlwifi-cc-46.3cfab8da.0/
$ sudo cp iwlwifi-*.ucode /lib/firmware
```

I rebooted the Pi and crossed my fingers _again_!

## Running into errors

This time, I ran `dmesg` and saw a lot more output, but also a lot of errors. Using `dmesg --follow`, I found there were similar errors being printed out every couple seconds.

And checking with `ip a` and `iw list`, I found that there was a new wireless device, but it seemed to be stuck in a loop, incrementing its ID each time it tried initializing.

The two main errors I found were:

```
[   50.097951] thermal thermal_zone1: failed to read out thermal zone (-61)
```

And:

```
[   50.898495] iwlwifi 0000:01:00.0: Failed to configure RX queues: -5
```

The thermal zone issue was just misdirection; it's not fatal, and in fact, if I manually read out the thermal zone data, it seems to work, so it's probably a bug in the driver.

For the second error, I eventually found a [helpful patch on the Linux kernel mailing list](https://lore.kernel.org/linux-wireless/3cab5072-17a2-4d9a-2077-93788971c6c4@invisiblethingslab.com/T/#u).

The solution Paweł Marczewski came up with was to delete the error message and the check that triggered it. I figured it was worth a try, so I patched Intel's WiFi driver using the diff in that email.

## Patching Intel's WiFi Driver

I copied out the diff straight from the mailing list page, booted my cross-compile environment again, logged in, and went back into the Linux source directory.

I created a new file called `iwlwifi.patch` with the contents of the diff from the mailing list, and applied it with `git apply -v iwlwifi.patch`. The patch applied cleanly with an offset, and so I recompiled (much faster the 2nd time), copied everything over to the Pi's microSD card, and booted the Pi with the patched driver.

## It works!

I logged into the Pi, and checked `dmesg`, and it worked!

I ran `ip a` to check for the interface, and it showed up as `wlan1`, and I ran `iw list`, and it showed up correctly there too!

So the last thing to test was connecting to my network. I edited the WPA supplicant file in `/etc/wpa_supplicant/wpa_supplicant.conf`, setting my country code and network details

```
ctrl_interface=/var/run/wpa_supplicant
update_config=1
country=us

network={
 scan_ssid=1
 ssid="geerling-acn"
 psk="my-network-passphrase"
}
```

I saved the file and rebooted the Pi.

Everything connected, and the WiFi card picked up an IP address. We were in business!

## Testing speeds ... and realizing my network is 802.11ac

The first time I did this, I ran a few tests using `iperf` but realized at this point that I had an 802.11ax wireless card connecting to a pokey old 802.11ac wireless router. So I had to figure out a way to connect over WiFi 6.

## Testing speeds ... and realizing I don't have another computer with 802.11ax

Instead of upgrading my entire home network, [PixlRainbow on GitHub suggested](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/22#issuecomment-727595765) I try upgrading one of my other computers to WiFi 6, then test connecting _it_ directly to the Pi.

So I was excited when I found a [$20 'Wise Tiger' Intel AX200 card](https://amzn.to/3nGeRiB) for my Dell XPS 13 laptop. I bought it and installed it in the Dell, and made the video [How to Upgrade a Dell XPS 13 to WiFi 6 (802.11ax)](https://www.youtube.com/watch?v=C760v9XpkzE) of the process.

But when I tested the speeds, I was disappointed to find the upgraded card could only pump through 300-400 Mbps on the XPS 13, due to the two-by-two antenna performance and configuration on the Dell. My MacBook Pro, which _doesn't_ have WiFi 6, can get speeds up to 900 Mbps over 802.11ac, so the design of the entire system is extremely important.

I was happy to have WiFi 6 in my Dell laptop, but it wasn't good enough to test how much speed I could get out of my Pi.

## Testing speeds again ... and realizing my wired network is 1 Gbps

So my next step was upgrading my Wireless router. And there are a lot of AX routers available, but most of the ones with faster-than-gigabit speeds cost a lot more than the basic models. And if I wanted to break the gigabit barrier, I'd need one with a faster uplink.

I found my local Micro Center had the [ASUS RT-AX86U WiFi 6 router](https://amzn.to/3re0KDy) with a 2.5 Gbps switchable LAN/WAN port. My home Internet connection can't do anything near that much (thanks, Spectrum!), but I do want to upgrade my internal network to 10 Gbps soon, so it'd be nice to have the fast WiFi connection too.

I bought that router, and replaced my old router with it.

And it was at this point that I realized two more things:

  1. I STILL didn't have any other computers with more than one gigabit of connectivity.
  2. I had blown through my budget for this project weeks ago.

So... I decided to do two things:

First, I bought ten gigabit networking gear, including a [MikroTik 4 SFP+ port 10G switch](https://amzn.to/2KQ4rhO)... and I realized after-the-fact the particular transceivers I bought wouldn't work with the router's 2.5 Gbps port—they only did 1 or 10 Gbps.

And second, I decided to follow the [advice of St0nedB on GitHub](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/22#issuecomment-743984939) and set up the [ASUSWRT-Merlin firmware](https://www.asuswrt-merlin.net) on my router so I could run `iperf` directly between my router and the Raspberry Pi.

The instructions for [benchmarking with `iperf` directly with the ASUS router](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/22#issuecomment-748534025) are linked on GitHub, if you want to try the same thing.

Anyways, here's the bottom line:

{{< figure src="./cm4-networking-benchmarks.png" alt="Raspberry Pi Compute Module 4 Benchmarks - Built-in WiFi AC, Wired 1 Gbps, WiFi 6 AX" width="700" height="353" class="insert-image" >}}

Over my Gigabit network, the Pi matched it's built-in gigabit wired network performance, maxing it out at 930 megabits.

And connected directly to the AX router, it could pump through 1.34 gigabits (or a total of 1.5 gigabits bidirectional, with a full-duplex transfer). This WiFi 6 AX200 card runs _30% faster_ than the built-in gigabit wired networking, and a whopping _16x faster_ than the built-in WiFi!

It can probably get even faster, but I was happy enough with this result.

## Conclusion

So what did I learn?

Getting faster WiFi on the Raspberry Pi isn't too hard, but it does require some extra tweaking and a kernel patch, making it hard for most people to get it working. Hopefully the issues I ran into will be easier to work around in the future.

I want to explore more of the possibilities this fast wireless setup enables, like using WiFi 6 along with fast SATA or NVMe storage for a super fast wireless NAS, or using WiFi 6 along with gigabit ethernet to build a custom router or access point.

If you want to follow along with these adventures, [subscribe to my YouTube channel](https://www.youtube.com/c/JeffGeerling) and browse the issues on my [Raspberry Pi PCIe Device Database](https://pipci.jeffgeerling.com).

And please consider sponsoring my open source work on [GitHub Sponsors](https://github.com/sponsors/geerlingguy) or [Patreon](https://www.patreon.com/geerlingguy)!
