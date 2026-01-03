---
nid: 3114
title: "Getting faster 10 Gbps Ethernet on the Raspberry Pi"
slug: "getting-faster-10-gbps-ethernet-on-raspberry-pi"
date: 2021-07-07T14:01:12+00:00
drupal:
  nid: 3114
  path: /blog/2021/getting-faster-10-gbps-ethernet-on-raspberry-pi
  body_format: markdown
  redirects: []
tags:
  - 10 gbps
  - asus
  - benchmarks
  - iperf3
  - network
  - networking
  - pcie
  - raspberry pi
  - reviews
  - video
  - youtube
---

If you read the title of this blog post and are thinking, "_10 Gbps on a Pi? You're nuts!_," well, check out my [video on using the ASUS XG-C100C 10G NIC on the Raspberry Pi CM4](https://www.youtube.com/watch?v=FTP5h9jnVx0). Back? Good.

To be clear: it's impossible to route 10 gigabits of total network throughput through any Raspberry Pi on the market today.

{{< figure src="./asus-10gbe-ethernet-in-raspberry-pi-cm4.jpg" alt="ASUS 10G NIC in Raspberry Pi Compute Module 4 IO Board" width="500" height="356" class="insert-image" >}}

But it _is_ possible to connect to a 10 gigabit network _at 10GBase-T speeds_ using a Raspberry Pi Compute Module 4 and an appropriate PCI Express 10G NIC. And on my Pi PCI Express site, I documented exactly how I got an [ASUS XG-C100C](https://pipci.jeffgeerling.com/cards_network/asus-xg-c100c-10g.html) working on the Raspberry Pi. All it takes is a quick recompile of the kernel, and away it goes!

{{< figure src="./ethtool-10gbaset-output.jpg" alt="ethtool showing 10 gigabit speed for ASUS 10G NIC on Raspberry Pi in terminal" width="700" height="394" class="insert-image" >}}

But this blog post isn't about how I got the card working, or about 10 gigabit networking in general. I want to cover optimizations you can make to take a Raspberry Pi from 3 Gbps to _3.6 Gbps_!

> If you think trying to increase not-10-gigabit to still-not-10-gigabit speeds is dumb and I'm an idiot for trying this stuff on a Raspberry Pi and not [your platform of choice], the back button is just a few centimeters away from here, go click it 😉

## Overclocking

For the ASUS card I tested, overclocking the Pi's CPU (defaulted to 1.5 GHz) didn't actually make much of a difference, since the CPU was not the limiting factor for processing network packets. The NIC does a good job offloading that task.

But for many NICs, they _don't_, and having the CPU run faster means it can handle more packet throughput, allowing you to get more bandwidth. (You can use `atop` to measure if your NIC is CPU-throttled—run it during an `iperf3` test and see if IRQ interrupts turn red at 98-99%).

To overclock a Pi, it's pretty simple; edit `/boot/config.txt` and add the following lines:

```
over_voltage=6
arm_freq=2000
```

Reboot, and the Pi is now a 2.0 GHz Pi. Higher values are possible, but with 99% of Pis out there, a 2.0 GHz clock is as high as I go to keep stability without specialized cooling.

## PCI Express hierarchy optimization

I have to be honest, I am basically a beginner-level practitioner of the PCI Express protocol. But after a [recommendation from NickMihailov on GitHub](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/15#issuecomment-753489260), I added the following kernel parameter before `rootwait` in my `/boot/cmdline.txt` and rebooted:

```
pci=pcie_bus_perf
```

This option set's the Linux device's MPS (Max Payload Size) to the largest possible value based on the Pi's PCI Express bus. The maximum on the Pi is 512 bytes—and checking before setting this option, I could see the card was registering at _128 bytes_.

The lower setting is good for compatibility, or if you have multiple PCI Express devices and need features like hotplug and peer-to-peer DMA, but for the highest speed, [it's better to have a larger payload size](https://blog.linuxplumbersconf.org/2017/ocw/system/presentations/4737/original/mps.pdf) so you can fit more data in fewer packets through the bus.

I tested with and without this option enabled, and went from `3.02 Gbps` with it disabled (128 bytes) to 3.42 Gbps with it enabled (512 bytes). That's a 12% speedup!

## Jumbo Frames

Jumbo frames are basically Ethernet frames with a larger 'payload' size. It's like switching your data packets from little 'Smart Car' sized vehicles to 18-wheeler trailers. You can put 9000 bytes of data into jumbo frame packets, while only 1500 bytes go into a standard frame. (This number is often referred to as 'MTU', or 'Maximum Transmission Unit', so you'd say a Jumbo frame has 9000 MTU.)

The Pi's internal Ethernet interface requires a kernel recompile to change the MTU from the default, but external NICs are typically happy to let you assign whatever MTU you want (within reason).

To set it for the ASUS NIC, I ran the following command:

```
sudo ifconfig eth1 mtu 9000 up
```

The major caveat? Anything else between your NIC and the NIC you want to communicate with also has to have jumbo frames enabled. On a tightly-controlled LAN with good equipment, it's not a big issue. But over larger networks, or if you don't really know what you're doing, it's best to stick to the normal 1500 MTU setting.

With Jumbo Frames _and_ the PCI Express optimization mentioned previously, [I can get **3.59 Gbps**](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/15#issuecomment-870792558) between my Mac and the Pi.

In total, those two optimizations made the maximum network speed almost 20% faster!

## Conclusion

The Raspberry Pi's current built-in NIC gets you a pretty solid 943 Mbps over a 1GBase-T network. For most people, that's fine. Some of these optimizations (most notably 9000 MTU / Jumbo Frames) will push that beyond 960 Mbps, but it's not a huge difference.

It's nice to know that even current-generation Pis can benefit from 2.5G and 5G networking, especially since (at least for 2.5G) newer network gear and inexpensive NICs allows a pretty much free doubling of speed using existing cabling (assuming you're already using Cat5e or better).

And maybe a newer generation Pi 5 could allow us to tap into more PCI Express lanes at a faster rate, and make it so Pis can be first-class citizens on a 10 gigabit network!
