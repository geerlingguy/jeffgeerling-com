---
nid: 3066
title: "WiFi 6 is not faster than Ethernet on the Raspberry Pi"
slug: "wifi-6-not-faster-ethernet-on-raspberry-pi"
date: 2021-01-08T16:30:36+00:00
drupal:
  nid: 3066
  path: /blog/2021/wifi-6-not-faster-ethernet-on-raspberry-pi
  body_format: markdown
  redirects: []
tags:
  - benchmarking
  - cm4
  - compute module
  - edup
  - iperf3
  - linux
  - performance
  - raspberry pi
  - video
  - wifi 6
  - youtube
---

I didn't know it at the time, but my results testing the [EDUP WiFi 6 card](https://pipci.jeffgeerling.com/cards_network/edup-intel-ax200-wifi-6.html) (which uses the Intel AX200 chipset) on the Raspberry Pi in December weren't accurate.

It _doesn't_ get 1.34 gigabits of bandwidth with the Raspberry Pi Compute Module 4 like I stated in my December video, [WiFi 6 on the Raspberry Pi CM4 makes it Fly!](https://www.youtube.com/watch?v=csI19aOJEik).

I'm very thorough in my benchmarking, and if there's ever a weird anomaly, I try everything I can to prove or disprove the result before sharing it with anyone.

In this case, since I was chomping at the bit to move on to testing a [Rosewill 2.5 gigabit Ethernet card](https://pipci.jeffgeerling.com/cards_network/rosewill-rc20001-25gbe.html), I didn't spend as much time as I should have re-verifying my results.

{{< figure src="./mzhou-wifi-6-pi-adapter.jpeg" alt="MZHOU WiFi Bluetooth M.2 NGFF Adapter Card for PCIe Raspberry Pi Compute Module 4 AX200 Intel 6" width="600" height="401" class="insert-image" >}}

In this post I'll describe how testing [this $20 M.2 WiFi adapter card](https://pipci.jeffgeerling.com/cards_m2/mzhou-wifi-bt-ngff-to-pcie.html) suggested by Javier Choclin led to me learning a _lot_ about Linux's wireless networking stack.

## Video for this post

There is a video that goes along with this blog post, for the visually-inclined:

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/1kWAdtoq8TQ" frameborder='0' allowfullscreen></iframe></div>

## It's just not possible!

Full transparency, what really got me started thinking about my performance results was [this comment](https://www.youtube.com/watch?v=csI19aOJEik&lc=UgxbRWag1HyiQocv6id4AaABAg) on YouTube, which reads:

> Intel ax200 is a 2x2 chip. Max 11ax Phy datarate it can support is MCS11 (1024-QAM) which is 1201Mbps. It is impossible to get 1340 Mbps iperf throughput using a 2x2 chipset. Can you share the iperf log showing 1340Mbps like you showed for ethernet :)

That 1.2 gigabit limit is _definitely_ lower than the 1.34 gigabit result I got in my testing.

So what gives?

Well, let's start with the facts:

  - A couple months ago, when I tested five Ethernet interfaces at the same time on the [Intel I340-T4 card](https://pipci.jeffgeerling.com/cards_network/intel-i340-t4-4-port-1g.html), I put each interface on its own network, connecting just that interface to an individual Raspberry Pi on the same network. I got **4.15 Gbps** with the four interfaces on that card and the internal network interface using Jumbo Frames.
  - When I tested the EDUP WiFi 6 card, I got 930 Mbps of one-way throughput.
  - When I tested an [ASUS 10 Gbps card](https://pipci.jeffgeerling.com/cards_network/asus-xg-c100c-10g.html) (more on it coming soon!), I got **3.26 Gbps** of one-way throughput.
  - When I tested an Intel AX200 Desktop Kit in the MZHOU adapter, I got **930 Mbps** of one-way throughput.
  - Then I tested it _again_, though I had the Pi disconnected from it's wired network connection, and I only got **600-800 Mbps** of one-way throughput.

{{< figure src="./cm4-network-adapters-full-graph.jpeg" alt="Compute Module 4 Network Adapter Speed Benchmark Results" width="700" height="394" class="insert-image" >}}

In hindsight, the problem is more obvious—getting 930 Mbps for all the wireless tests when Ethernet was connected should've clued me in earlier. But getting to the point where I could prove what I _thought_ might've happened _actually_ happened took some time.

## Testing the MZHOU WiFi/Bluetooth M.2 NGFF adapter

To quickly review the card that I tested for this post—if you want to adapt an M.2 WiFi and bluetooth module you have laying around, maybe from an old broken down laptop or desktop computer, [this little MZHOU adapter I tested](https://amzn.to/34A3sth) works a treat!

With that out of the way... let's get back to the substance of this post.

## Strange behaviors in the Linux networking stack

Anyways, getting back to the problem I uncovered, I found it odd that both of my WiFi tests got about 930 Mbps when I tested them the first time.

I was using `iperf3`'s `--bind` option, which according to the documentation:

> binds to the interface associated with the address <host>

So if I have two interfaces, let's say `eth0` on 192.168.0.5, and `wlan0` on 192.168.0.6, and I wanted to test the `wlan0` interface, I could just use `--bind 192.168.0.6`, right?

Well, no, actually.

Linux's kernel networking stack is optimized for getting packets routed in the most efficient manner. Usually, that's a great thing!

But the problem was that the Linux kernel saw that both my wired network and wifi connections were operating on the same network, so it optimized the packet flow for me by routing data through the wired ethernet connection, _even though I told iperf3 to bind to the wifi interface_.

Long story short, I am not the first person to run into this issue, and I found out about a couple things that I could try to combat the problem, like adjusting the [`arp_filter` setting](https://sysctl-explorer.net/net/ipv4/arp_filter/) to disable the kernel's intelligent routing, or segregating all my network interfaces on their own subnets.

But the easiest thing, in the end, was to disable the network interface I _wasn't_ testing. So before I re-ran my benchmarks, I ran `sudo ip link set eth0 down` to disable the onboard gigabit ethernet.

And after doing that, and running more benchmarks, I have to agree with marvell marvell: it is, in fact, impossible to get more than 1.2 gigabits of throughput with the Intel AX200.

{{< figure src="./ax200-wifi-performance-raspberry-pi.jpeg" alt="Intel AX200 WiFi Performance Benchmarks Raspberry Pi Compute Module 4" width="700" height="394" class="insert-image" >}}

My benchmarking showed that throughput reached around 800 Mbps from the Pi to the router, and 1.1 Gbps from the router to the Pi.

Those results are still excellent, and beat any older WiFi device I have in my house right now—including my $3000 MacBook Pro—but my conclusion from the last video that "WiFi is faster than Ethernet" on this Pi isn't entirely true.

Before I move on from that topic, I should mention the maintainers of `iperf3` have been trying to make benchmarking work better with multiple devices on the same network, and there's a [bleeding edge option I tested called `--bind-dev`](https://github.com/esnet/iperf/commit/21581a72160c90da1cb3040a1207559e505de981), but unfortunately [it didn't make a difference on the Raspberry Pi](https://github.com/esnet/iperf/issues/1099).

## Learning about `wpa_supplicant`

In the middle of all this benchmarking, I decided to also dig in and learn more about `wpa_supplicant` that we use to control WiFi on our Raspberry Pis, or in Debian in general.

I noticed in my testing that if I had both the internal WiFi interface (`wlan0`) and the PCIe interface (`wlan1`) enabled, `wpa_supplicant` would always choose the external interface. And usually that was what I wanted, so I didn't question it. But _why_ did it always choose the external interface?

I realize the number of people with multiple WiFi interfaces on their computers is probably very tiny, but still, the `wpa_supplicant` documentation shows nothing about how to specify an interface for a configuration during startup—only how to specify an interface when invoking `wpa_supplicant` directly.

Well, after wondering this a long time, inspiration finally struck me after I saw [this answer](https://superuser.com/a/1553310/80658) from Hannes on Stack Exchange. His post reminded me of the obvious fact: I'm using Linux. I can figure this out myself!

First I tried finding the wpa_supplicant codebase and documentation, and found the docs through [this website](https://hostap.epitest.fi/wpa_supplicant/)... but a lot of the links were either broken or somewhat unhelpful. I couldn't even find a clone of the source on GitHub (though I didn't look _too_ hard). So I switched gears and had more luck searching for the code behind `dhcpcd`, which took me to Roy Marple's website (https://roy.marples.name). His site has links to the [official code repository](https://roy.marples.name/cgit/dhcpcd.git/), as well as a [GitHub mirror](https://github.com/rsmarples/dhcpcd) that's easier to browse.

Looking around in the code, I noticed the files that load wpa_supplicant on the Raspberry Pi are in the `hooks` folder. Specifically, the source for the `wpa_supplicant` hook is [in this file](https://github.com/rsmarples/dhcpcd/blob/master/hooks/10-wpa_supplicant).

Right at the top, it looks like there's my answer: there's a bash `for` loop that looks for a given set of `wpa_supplicant` files, starting with a file named after the interface:

```
	for x in \
		/etc/wpa_supplicant/wpa_supplicant-"$interface".conf \
		/etc/wpa_supplicant/wpa_supplicant.conf \
		/etc/wpa_supplicant-"$interface".conf \
		/etc/wpa_supplicant.conf \
	; do
```

If it doesn't find a file with the interface name in it, it goes to the plain config file. If it doesn't find either, it goes up a directory, into et-see, and searches for the same files.

There's still more digging I could do—but my curiosity was satisfied for the time being, and I was itching to get back to some testing with 10 Gbps networking gear.

## More testing with the MZHOU and Coral.ai

Getting back to the _original_ topic of my post, the [MZHOU adapter card](https://pipci.jeffgeerling.com/cards_m2/mzhou-wifi-bt-ngff-to-pcie.html): I'm planning on testing a [Google Coral.ai TPU](https://www.coral.ai/products/m2-accelerator-ae) with this card, and that's the main reason I bought it in the first place.

But it's just a happy accident that I learned a ton about WiFi and Linux networking in the process of testing this boring little adapter!
