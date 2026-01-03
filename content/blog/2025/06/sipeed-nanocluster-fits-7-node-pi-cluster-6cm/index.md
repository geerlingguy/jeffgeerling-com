---
nid: 3468
title: "Sipeed NanoCluster fits 7-node Pi cluster in 6cm"
slug: "sipeed-nanocluster-fits-7-node-pi-cluster-6cm"
date: 2025-06-06T14:00:39+00:00
drupal:
  nid: 3468
  path: /blog/2025/sipeed-nanocluster-fits-7-node-pi-cluster-6cm
  body_format: markdown
  redirects:
    - /blog/2025/sipeed-nanocluster-fits-7-compute-nodes-6-cm
    - /blog/2025/sipeed-nanocluster-fits-7-compute-nodes-6cm
aliases:
  - /blog/2025/sipeed-nanocluster-fits-7-compute-nodes-6-cm
  - /blog/2025/sipeed-nanocluster-fits-7-compute-nodes-6cm
tags:
  - cluster
  - linux
  - raspberry pi
  - sipeed
  - video
  - youtube
---

{{< figure src="./sipeed-nanocluster-mug.jpg" alt="Sipeed NanoCluster with Raspberry Pi CM5 and coffee mug" width="700" height="394" class="insert-image" >}}

Sipeed's [NanoCluster](https://sipeed.com/nanocluster) is a tiny compute module clusterboard with room for up to 7 tiny computers.

Each slot has two inline M.2 (NGFF) slots which accept either a custom-designed SoM (System on Module) or an adapter board to adapt a standard Compute Module form-factor board into the slot (as pictured above).

One end has a large fan for cooling, and the other end has power and IO. You can power the board via either PoE++ (60W) or through USB-C PD (65W). Or _both_, with redundant power fail-over.

Because of the limited power budget and narrow space between boards—especially if you fit NVMe SSDs (the riser cards can hold a 2242 NVMe SSD, and/or microSD)—it’s recommended you only run 4 or a maximum of 5 CM5s. CM4s may fit more within that power budget, but I’ve found 4 is probably the best number if you want to get the best performance.

Slot 1 has power control over the other slots through GPIO, as well as optional UART support to at least some of the other slots. There are also USB and HDMI ports wired to slot 1 for external display and keyboard/accessories.

{{< figure src="./sipeed-nanocluster-poe-power.jpeg" alt="Sipeed NanoCluster running with CM5s using PoE++" width="700" height="467" class="insert-image" >}}

All nodes are interconnected over 1 Gbps links to a RISC-V switch chip on the underside of the board. That is a managed switch which has a web UI for control over port status, VLANs, etc. (most of the basic controls you’d expect are exposed, though currently only in a Chinese language UI).

Externally, there is a single PoE++-capable 1 Gbps Ethernet link to the outside world. So for storage or high-bandwidth applications, this board has the same challenge/bottleneck there as other boards like the Turing Pi 2 and Super6c.

I have a video going over my complete bringup and testing experiencing, highlighting some challenges with power and cooling when cramming in so many nodes in such a small space:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/UEtpaiODNs0" frameborder='0' allowfullscreen></iframe></div>
</div>

Most of the test data I gathered for both the video and this blog post is summarized in the [GitHub issue on the NanoCluster](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/739) in my Pi PCIe project. Sipeed also offers [NanoCluster documentation and specs](https://wiki.sipeed.com/hardware/en/cluster/NanoCluster/index.html) on their wiki.

> Note: Sipeed sent the NanoCluster I tested in this blog post and video. They did not pay for a review nor have any input into my testing or the contents of these posts. See my [sponsorship and review policies](https://github.com/geerlingguy/youtube?tab=readme-ov-file#sponsorships).

## Power and Cooling

Sipeed recommends running only 4 Compute Module 5s, especially if you're adding on M.2 NVMe SSDs on the back of the CM4/CM5 carrier boards (each board includes a 2242-size slot).

{{< figure src="./sipeed-nanocluster-thermal-image.jpg" alt="Thermal image of Sipeed NanoCluster" width="700" height="394" class="insert-image" >}}

And from all my testing, I found that to be a wise recommendation. I first tried running _six_ CM5s, but even without any NVMe SSDs (running them all on their built-in eMMC storage), when I ran stress tests, I would sometimes lose connectivity for a bit, the system power draw would pass 60W (which is the PoE++ max power input rating—65W for USB-C PD), and I would run into thermal throttling since I couldn't even use slim heatsinks on the nodes.

Running 5 CM5s, the cluster was much more stable—though individual nodes would still throttle from time to time. If you cut it down to 4 nodes, there's more power headroom (with 5, I would still use up all 60W of power under load), and you have enough space for thin heatsinks between each node.

The included fan is set to run full blast (resulting in 58 dBa of noise within 6" of the cluster—not quiet enough for a desktop, most places), but you can control the fan speed via GPIO in slot 1.

Even at full blast, blowing straight into the mass of computers, they will overheat without any heatsinks to draw heat away from the main SoC, if you're running them flat out, like with LLMs, distcc, or MPI.

More realistic workloads like running my website on a K3s cluster didn't result in any throttling, however, so YMMV.

Overall power draw in different scenarios can be seen in the graph below:

{{< figure src="./sipeed-nanocluster-power-consumption.jpg" alt="Sipeed NanoCluster power consumption via PoE++ and USB-C PD" width="700" height="394" class="insert-image" >}}

## Performance and Use Cases

I ran four different applications to test cluster performance: a K3s cluster running a Drupal website, distributed-llama for distributed LLM inference testing, distcc to perform a distributed Linux kernel compile, and HPL for raw cluster compute performance (FP64 on CPU).

In all four cases, I had no issues with connectivity or getting things running.

## K3s Kubernetes cluster

Using my [Raspberry Pi Cluster](https://github.com/geerlingguy/pi-cluster) Ansible playbook to install K3s and deploy Drupal, Prometheus, and Grafana, I had no issues running some real-world applications inside Kubernetes.

Like with the Turing Pi 2 and DeskPi Super6c, there are some bottlenecks, most notably a single 1 Gbps connection to the outside world. But for many cluster apps that run in Kubernetes, that's not a big deal.

In the past, I've [run this website on a Pi cluster](/blog/2022/hosting-website-on-farm-or-anywhere), and there's nothing preventing me from doing the same on the NanoCluster.

## Distributed Llama

{{< figure src="./sipeed-nanocluster-distributed-llama.jpg" alt="Distributed Llama running on Pi NanoCluster" width="700" height="394" class="insert-image" >}}

After having a number of people ask me about running [Exo](https://github.com/exo-explore/exo) on a Pi cluster, I found [getting it going on the Pi is a work in progress](https://github.com/exo-explore/exo/issues/290).

So I switched gears and tried out [Distributed Llama](https://github.com/b4rtaz/distributed-llama), which helpfully includes [instructions for Raspberry Pi cluster install](https://github.com/b4rtaz/distributed-llama?tab=readme-ov-file#-setup) right in the README!

Using that, and seeing as I only have smaller 4GB CM5s at my disposal, I ran the `Llama 3.2 1B Instruct Q40` model recommended in the README, and got around 17 tokens/second.

It was plenty fast enough for a chat bot, but with larger models, the speeds will definitely be reduced.

If you're only after high performance LLMs, a single machine and a beefy GPU will get you a lot further than this cluster. If you're after _learning_ about how to distribute workloads like LLMs horizontally, this cluster is a handy tool for that.

## distcc distributed Linux kernel compile

{{< figure src="./sipeed-nanocluster-distcc-linux-kernel-compile.jpg" alt="distcc - distributed Linux kernel compile on Pi NanoCluster" width="700" height="394" class="insert-image" >}}

[distcc](https://www.distcc.org) is a fast, free, distributed Linux C/C++ compiler, and using it, you can speed up compile times for things like the Linux kernel. [Something I do a lot](https://www.redshirtjeff.com/shop/p/recompile-linux-shirt).

Rather than buying an Ampere Arm workstation to speed up arm64 Linux compilation (which can get it done in under 2 minutes), can I improve on the standard Pi 5's pokey 45 minute compile time?

It turns out I can—with _four_ nodes, I was able to cut the compile time down to just over 22 minutes. I noticed the Pis weren't all running full blast, so there's a bottleneck, maybe in the networking layer. I think I could get faster compile times with a little more tweaking.

## HPL (Top500) High Performance Linpack

I ran my [top500-benchmark](https://github.com/geerlingguy/top500-benchmark/issues/63) against the NanoCluster with 4 4GB CM5s, and got a FP64 result of 112.25 Gflops, consuming 62W of power. That's about 3.5x faster than the performance of a [single CM5 (32.152 Gflops)](https://github.com/geerlingguy/top500-benchmark/issues/48), but it's less than half as efficient, accounting for the PoE++ power injector and board overhead with this solution.

(The single CM5 was using a more efficient 27W USB-C GaN adapter and the more lightweight CM5 IO Board.)

The total NanoCluster performance put it just past my [base model M2 MacBook Air](https://github.com/geerlingguy/top500-benchmark?tab=readme-ov-file#results), but efficiency-wise, this little cluster is only a little more efficient than the Intel systems I've tested.

Again, this is not going to put a high-performing HPC powerhouse in the palm of your hand—but it's much more fun testing HPC/distributed applications on a little cluster like this than a pile of hot, used mini PCs burning 150+ watts in aggregate, with a bunch of power supplies hanging out in the back! (At least, I think so.)

## Conclusion

There are a lot of little things I didn't cover in this post that I briefly touch on towards the end of the video—so please watch that for a lot of the smaller things.

But, I think you'll fall into one of two camps:

  1. It's a fun little cluster board, with obvious limitations. You might be willing to overlook those because it's not that expensive.
  2. This is a completely impractical device with no use case, and Raspberry Pis are overpriced garbage.

For the latter, I'm not sure if I'll ever convince you that you can still have fun with things that aren't your version of ideal... but for the former, Sipeed, I think, hit a nice spot between cheap and functional with this thing.

It's not perfect, and you _definitely_ have to tinker with things to get the right setup for power, performance, and noise. But I'm happy to do that. It let me play with software I never would've touched without it, like distributed-llama and `distcc`.

Right now it's on preorder, but it [should be available soon](https://sipeed.com/nanocluster) for between 50 to 150 bucks, depending on where you live and what options you choose.
