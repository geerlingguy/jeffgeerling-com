---
nid: 3153
title: "Turing Pi 2: 4 Raspberry Pi nodes on a mini ITX board"
slug: "turing-pi-2-4-raspberry-pi-nodes-on-mini-itx-board"
date: 2021-12-01T16:35:50+00:00
drupal:
  nid: 3153
  path: /blog/2021/turing-pi-2-4-raspberry-pi-nodes-on-mini-itx-board
  body_format: markdown
  redirects: []
tags:
  - cluster
  - jetson
  - kubernetes
  - raspberry pi
  - turing pi
  - video
  - youtube
---

Last year I spent a bit of time [building a Kubernetes cluster with the original Turing Pi](https://github.com/geerlingguy/turing-pi-cluster). It was fun, and interesting, but ultimately the performance of the Compute Module 3+ it was designed around led me to running my homelab off some newer Pi 4 model B computers, which are at least twice as fast for almost everything I run on them.

{{< figure src="./turing-pi-2-board.jpeg" alt="Turing Pi 2" width="700" height="496" class="insert-image" >}}

So this year, I was excited when the folks at Turing Pi sent me a [Turing Pi 2](https://turingpi.com) to test drive. _And_ the board arrived just in time for Patrick Kennedy from ServeTheHome to challenge me to a cluster build-off at Supercomputing '21! Check out [his ARM cluster build here](https://www.servethehome.com/building-the-ultimate-x86-and-arm-cluster-in-a-box/).

The Turing Pi 2 is a mini ITX motherboard capable of holding up to four Raspberry Pi Compute Module 4s _or_ NVIDIA Jetson Nanos, and it integrates a board management backplane, power management, and gigabit Ethernet switch, alongside various PCI Express breakouts, so you can build a 4-node SBC cluster.

And it performs—as I hoped—much better than the older version. Not only do the CM4, Jetson Nano, and even pin-compatible replacements like Radxa's CM3 and Pine64's SOQuartz all have full gigabit Ethernet, their CPUs are noticeably faster than the CM3+ they replace.

The board I have is a prototype, and as such is still running a very early version of the firmware—RTC PWM fan control aren't even implemented yet! But the folks at Turing Pi seem set on having all the features ironed out for a January 2022 launch. The board will cost about $200, with CM4 adapter cards (which connect a CM4 to the vertical SO-DIMM slot) adding on $10 each.

## PCIe Expansion support

Since each CM4 has one PCI Express Gen 2 lane available, the board exposes each one in a different way.

{{< figure src="./turing-pi-2-overhead.jpeg" alt="Turing Pi 2 overhead top down shot" width="650" height="434" class="insert-image" >}}

For node 1 (at the top of the board), there's a mini PCIe slot with a SIM tray underneath—useful for things like 4G or 5G modems. For node 2, there's another mini PCIe slot (with no SIM tray).

Node 3 is connected to an ASMedia 2-port SATA controller, so you can plug in up to two SATA III drives directly into the Turing Pi 2, and they'll be controlled by the computer in slot 3.

Node 4 is connected to a VL805 USB 3.0 controller, and that exposes a USB 3 front panel header and two USB 3.0 ports on the rear to the computer in slot 4.

The idea is you can use node 3 as a storage controller (e.g. run two drives in RAID 1 and have an NFS share for your cluster running on that node), use node 4 for USB devices (and share them, if needed, through that node), and use nodes 1 and 2 for whatever specific connectivity you want (e.g. a wireless 4G gateway for redundant Internet access).

The back of the board has two bridged 1 Gbps Ethernet adapters—though the Realtek RTL8370MB Ethernet switch is managed, so assuming updated firmware, the board's network configuration should be malleable as well.

## Power

{{< figure src="./atx-power-header-turing-pi-2.jpeg" alt="ATX Power header on Turing Pi 2" width="650" height="434" class="insert-image" >}}

In a first for a Raspberry Pi board, the Turing Pi 2 gets its power via a standard ATX 24-pin power header. You can use any standard PC PSU, or even a [Pico PSU](https://amzn.to/3d2MCXS) and 12V adapter to power the Turing Pi 2.

With four CM4 8GB Lite nodes with WiFi and Bluetooth, plus a connected 2TB Crucial SSD, power consumption was around 15W at idle, and 25W when running under full load on all four nodes (as measured at the wall by a Kill-a-Watt). I'll talk a little more about efficiency in the performance section.

{{< figure src="./reset-power-button-turing-pi-2.jpeg" alt="Reset and Power button detail on Turing Pi 2" width="650" height="434" class="insert-image" >}}

The board also has a reset and power button built in, as well as headers for front panel power and reset functionality. And these buttons work well, providing a sometimes-necessary full halt/reboot to the cluster.

If you press 'reset', the entire cluster will be powered down immediately, then booted back up, one slot at a time. If you press 'power' the cluster will power down gracefully one slot at a time, and remain off. Pressing 'power' again boots the cluster back up, one slot at a time.

## Other IO

Around the edge of the board, there are various other IO options as well. There are UART headers for each Pi, along with a full 40-pin GPIO header for slot 1. There's also a full-size HDMI 2.0 port attached to slot 1.

There are micro USB ports for flashing both the MCU and eMMC modules on the CM4s themselves (you can see them in the picture in the power section above), and unlike the Turing Pi v1, all nodes can be hot-plugged and eMMC can be flashed using software control, courtesy of a new board management backplane, managed by an STM32 chip.

The user interface and CLI for that chip is still a bit rough, so I haven't had a chance to really dig in—hopefully I'll have more time for that soon, since I'm planning on racking up this unit!

{{< figure src="./front-panel-header-usb-3-dsi-turing-pi-2.jpeg" alt="DSI front panel header and USB 3 connector on Turing Pi 2" width="650" height="434" class="insert-image" >}}

There's also a front panel header for LEDs and a power switch, as well as a DSI display connector attached to slot 1.

There are a few other connections, jumpers, and dip switches too, but I'll defer to the official site and documentation for more detail.

## Blinkenlights

{{< figure src="./turing-pi-blinkenlights.gif" alt="Turing Pi 2 Blinkenlights" width="380" height="240" class="insert-image" >}}

Besides performance, one thing I didn't like about the original board was how few status LEDs it had. This new board is much better in that regard, with status LEDs for almost every important feature.

Both of the Ethernet ports on the back have functional link and activity lights. Each slot _also_ has appropriately-colored link and activity lights. Each slot also has a power indicator LED, plus there's an overall board power LED, and an LED to indicate the MCU is 'on' (helpful when deciding to safely shut down the cluster).

And finally, each of the CM4 adapter cards has a green power and activity LED on the back, so you can visually confirm they're powered on and doing something.

All in all, a good show of [blinkenlights](https://en.wikipedia.org/wiki/Blinkenlights) if I've ever seen one.

## Performance

No Raspberry Pi-based cluster will seriously compete in the [Top500](https://www.top500.org) list, but since the list was just updated at Supercomputing '21—which was held a few weeks ago in St. Louis, my hometown—I thought it'd be a fun experiment to see how it fares running HPL (High Performance Linpack), the standard benchmark for the Top500 clusters.

Initially, I had some trouble getting HPL to run. I built an automated playbook to build MPI, ATLAS, and HPL on the cluster (it's in my [turing-pi-2-cluster](https://github.com/geerlingguy/turing-pi-2-cluster) repo), and everything would work, but when I ran the test on more than two nodes, it would just hang.

As it turns out, the problem was DNS (of course [it was DNS](https://redshirtjeff.com/listing/it-was-dns-shirt?product=211)), and once I added all the IP addresses to the cluster hosts files, I was able to get it to run. I benchmarked the cluster at the default clock (1.5 GHz) and overclocked (to 2.0 GHz), and here are the results:

<table>
<thead>
<tr>
<th>Benchmark</th>
<th>Result</th>
<th>Wattage</th>
<th>Gflops/W</th>
</tr>
</thead>
<tbody>
<tr>
<td>HPL (1.5 GHz base clock)</td>
<td>44.942 Gflops</td>
<td>24.5W</td>
<td>1.83 Gflops/W</td>
</tr>
<tr>
<td>HPL (2.0 GHz overclock)</td>
<td>51.327 Gflops</td>
<td>33W</td>
<td>1.54 Gflops/W</td>
</tr>
</tbody>
</table>

The cluster would rank somewhere in the middle of the Top500—at least [in November 1999](https://www.top500.org/lists/top500/list/1999/11/?page=3)! And by my calculation, to make the cutoff for _this_ year's list, I'd only need around 146,772 more Compute Module 4's :)

But what's more pertinent to a little cluster-on-a-board like the Turing Pi 2 is _energy efficiency_. And looking at the Gflops/Watt measurement, it actually ranks favorably in _this_ year's [Green500](https://www.top500.org/lists/green500/list/2021/11/?page=2)—with 1.83 Gflops/W, it would rank in the 150s. Of course, the other servers in that range are throwing out _thousands of teraflops_... so not exactly an equal comparison.

But the cluster does run at 15W idle, and about 24W full tilt, with all four Pis running Linpack. Not too shabby if you compare this little ~$500 cluster to a four node setup of old X86 laptops or mini desktops.

If you want to dig deeper into the test methodology and results, check out my [HPL benchmarking issue on GitHub](https://github.com/geerlingguy/turing-pi-2-cluster/issues/1).

## Video

In addition to this blog post, I have a video that goes more in-depth on the cluster build and board features—[check it out on YouTube](https://www.youtube.com/watch?v=IUPYpZBfsMU):

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/IUPYpZBfsMU" frameborder='0' allowfullscreen></iframe></div>
</div>

## Conclusion

The Turing Pi 2 should cost about $200, and the Compute Module 4 adapter cards $10 each. It should be available in January 2022, and hopefully in greater quantities than the Turing Pi 1, which was almost always out of stock!

I think this board is a great platform for learning and low-end ARM cluster builds, and could also be useful for edge environments or other places where power and budget are primary constraints, but you still need multiple nodes (for whatever reason).

It has improved on the first Turing Pi board in every way except quantity of Pis, but that's to be expected since there's only so much space in the mini ITX footprint, and it also means the board can support many new features, like Nvidia Jetson Nano boards and multiple PCI express expansion cards!

Check it out at [TuringPi.com](https://turingpi.com).
