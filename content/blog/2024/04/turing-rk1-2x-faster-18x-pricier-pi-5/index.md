---
nid: 3370
title: "Turing RK1 is 2x faster, 1.8x pricier than Pi 5"
slug: "turing-rk1-2x-faster-18x-pricier-pi-5"
date: 2024-04-26T16:02:16+00:00
drupal:
  nid: 3370
  path: /blog/2024/turing-rk1-2x-faster-18x-pricier-pi-5
  body_format: markdown
  redirects: []
tags:
  - cluster
  - kubernetes
  - raspberry pi
  - rk1
  - turing pi
  - video
  - youtube
---

I've long been a fan of Pi clusters. It may be an irrational hobby, building tiny underpowered SBC clusters I can fit in my backpack, but it is a fun hobby.

{{< figure src="./turing-pi-2-cm4.jpg" alt="Turing Pi 2 with four CM4" width="700" height="auto" class="insert-image" >}}

And a couple years ago, the 'cluster on a board' concept reached its pinnacle with the Turing Pi 2, [which I tested using four Raspberry Pi Compute Module 4's](https://www.jeffgeerling.com/blog/2021/turing-pi-2-4-raspberry-pi-nodes-on-mini-itx-board).

Because Pi availability was nonexistent for a few years, many hardware companies started building their _own_ substitutes—and Turing Pi was no exception. They started designing a new SoM (System on Module) compatible with their Turing Pi 2 board (which uses an Nvidia Jetson-compatible pinout), and the result is the RK1:

{{< figure src="./turing-rk1.jpeg" alt="Turing RK1 SoM" width="700" height="auto" class="insert-image" >}}

The SoM includes a Rockchip RK3588 SoC, which has 8 CPU cores (A76 + A55), 8/16/32 GB of RAM, 32GB of eMMC storage, and built-in 1 Gbps networking.

{{< figure src="./turing-pi-2-with-rk1.jpeg" alt="Turing Pi 2 with RK1" width="700" height="auto" class="insert-image" >}}

I purchased a Turing Pi 2 as part of their initial Kickstarter (I have their revision 2.4 board), and four 8GB RAM modules + heatsinks. But for testing, Turing Pi also sent me four of their 32GB RAM modules. All my test data is available in the [SBC Reviews GitHub issue for the RK1](https://github.com/geerlingguy/sbc-reviews/issues/38).

For standard CPU benchmarks (Geekbench 6, High Performance Linpack, and Linux kernel recompiles), the RK1 consistently beat the Pi 5 (2x faster) and CM4 (5x faster), and the performance scaled with extra nodes (the RK1 cluster with 4 nodes was still 5x faster than the CM4 cluster with 4 nodes, running HPL).

I also ran a real-world cluster benchmark, installing Drupal 10 on the cluster using Kubernetes (k3s, specifically, using my [`pi-cluster`](https://github.com/geerlingguy/pi-cluster) project:

{{< figure src="./drupal-10-cluster-performance_0.jpg" alt="Drupal 10 cluster benchmark - Kubernetes on RK1 and CM4" width="700" height="auto" class="insert-image" >}}

The test setup only had one Drupal pod running, with a separate MariaDB pod running on a separate worker node, but I like this test because it offers more of a real-world perspective. Just because raw CPU compute is 5x faster, a real-world application running on top of a cluster has to take into account physical networking, ingress, networked IO, etc. — all of which are more even across these two vastly different SoMs!

## 10" Mini Rack

Today's video covers not only the RK1 and it's massive performance advantage over the Pi, but also racking it up in a new 10" mini rack from DeskPi.

DeskPi sent me their [RackMate T1](https://deskpi.com/collections/new-arrival/products/deskpi-rackmate-t1-2), an 8U 10" desktop rack, and I installed the Turing Pi 2 board (with four RK1s) inside a [MyElectronics Mini ITX 10" rackmount case](https://www.myelectronics.nl/us/10-inch-2u-mini-itx-case.html). Full disclosure—the RackMate and Mini ITX case were both sent to me by the respective vendors. And in MyElectronics' case, they actually sent this [2U _Dual_ Mini ITX case](https://amzn.to/3UxidYa) (affiliate link), which costs more but also allows you to mount two ITX boards side by side in a standard rack.

{{< figure src="./turing-pi-14.jpeg" alt="Jeff Geerling with DeskPi Rackmate T1 and MyElectronics 10 inch Mini ITX rackmount case" width="700" height="auto" class="insert-image" >}}

These products are all expensive, and for my _own_ needs (remember, I'm a bit of a weirdo building all my SBC clusters), the cost is justified. But they are expensive, so if you want to build the highest value / lowest cost homelab setup, this probably isn't the build for you.

What I like most is the compactness of this build. Assuming I can pick a good half-width switch, and ideally some sort of PDU that can mount in the 10" rack, I would have my ultimate portable lab rack! 10" is the perfect width for mini PCs, SBCs, even Mac minis.

Maybe someone could even make a cute travel case for it like we [used to have for old Macintoshes](https://www.retrotechnology.com/herbs_stuff/m_coll.html#bags)!

{{< figure src="./deskpi-rackmate-t1-mini-itx-10-inch-rackmount.jpeg" alt="DeskPi Rackmate T1 Mini ITX 10 inch rackmount" width="700" height="auto" class="insert-image" >}}

I've asked DeskPi about future 10" rackmount accessories, and it sounds like they're working on a few, so hopefully as I get more time to build out my mini rack, I can share some of those with you. One I'm excited about is a 1U Mini ITX 'tray' that would allow me to mount up to 8 of their DeskPi Super6C boards—that'd be 48 Raspberry Pi CM4s, totaling 192 CPU cores and 384 GB of RAM... for a whopping $5,000 or so, lol. I can dream, can't I?

Watch the video for all the details on this build:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/h6zt8KeXFdA" frameborder='0' allowfullscreen></iframe></div>
</div>

You can find _all_ my test data for the RK1 in [this GitHub issue](https://github.com/geerlingguy/sbc-reviews/issues/38).
