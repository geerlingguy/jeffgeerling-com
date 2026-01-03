---
nid: 3256
title: "Pi Cluster vs Ampere Altra Max 128-core ARM CPU"
slug: "pi-cluster-vs-ampere-altra-max-128-core-arm-cpu"
date: 2022-11-23T15:02:55+00:00
drupal:
  nid: 3256
  path: /blog/2022/pi-cluster-vs-ampere-altra-max-128-core-arm-cpu
  body_format: markdown
  redirects: []
tags:
  - altra
  - ampere
  - arm
  - benchmarks
  - cpu
  - deskpi
  - linpack
  - raspberry pi
  - super6c
  - supercomputer
  - top500
---

{{< figure src="./Ampere-Altra-Max-vs-Raspberry-Pi-CM4.jpg" alt="Raspberry Pi Compute Module 4 and Ampere Altra Max M128-30" width="700" height="430" class="insert-image" >}}

Sometimes life has a funny way of lining up opportunities, and one presented itself when Patrick from [ServeTheHome](https://www.servethehome.com/) reached out and said, "Jeff, I have an Ampere Altra Max server. You wanna come see it?"

Of _course_ I did.

But seeing as Patrick is more than 800 miles away, I had to come up with a reason to go see it, so I pulled out my 6-node Raspberry Pi cluster—with it's 24 ARM Cortex A72 CPU cores—and decided to have a little competition.

And of course that competition is documented in a YouTube video:

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class="embed-container"><iframe src="https://www.youtube.com/embed/UT5UbSJOyog" frameborder="0" allowfullscreen=""></iframe></div>

In the video, Patrick and I talk at length about areas where ARM is strong in the enterprise vs. areas Intel and AMD are still dominant. As a high level summary:

  - ARM is great in integer performance and for workloads like running webservers and VMs.
  - x86 is great in floating point performance and compute density, especially with the latest generation of AMD EPYC CPUs ('Genoa'—and Intel's Sapphire Rapids Xeon processors are coming soon!).
  - The ARM ecosystem has matured to the point where it's enterprise-ready, though it's not without its warts, and while [SystemReady](https://www.arm.com/architecture/system-architectures/systemready-certification-program) is a step in the right direction, the x86 ecosystem has benefitted from many years of relative stability.
  - There are now robust and flexible ARM hardware options from a range of hardware manufacturers like Gigabyte, Asa, and Supermicro—including a beast of a GPU-centric machine ServeTheHome will review soon!

But in this blog post, I wanted to focus on the benchmarking we did, and how different ARM systems—including Apple's M1—stack up in terms of historical top500 rankings and performance efficiency.

## Benchmarking ARM CPUs

The go-to cross-platform benchmark these days seems to be [Geekbench 5](https://www.geekbench.com), mostly for these reasons:

  - It's easy to run
  - It runs on (almost) every platform
  - It gives a simple single core + multicore score

And it's not a terrible way to get a quick idea of a CPU's potential. But my main complaint—understanding it's a simple benchmark not tied closely to _real-world_ application benchmarks—is that it really only tests bursty performance.

{{< figure src="./deskpi-super6c-kioxia-xg6-ssd-raspberry-pi-cluster.jpeg" alt="DeskPi Super6c with 6 Raspberry Pi Compute Module 4 and a Kioxia XG6 NVMe SSD" width="700" height="467" class="insert-image" >}}

The other major flaw—at least for my cluster benchmarking—is that it's single-node-only. It's not that useful when you want to test a full cluster's compute performance.

And so I lean on Linpack. [HPL](https://netlib.org/benchmark/hpl/) is not without fault, but one thing it does _very_ well is capture a broader spectrum of CPU performance, especially under extended load, and especially in clustered environments via MPI.

Many systems fall apart if you torture them, pegging all cores to 100% for 30+ minutes.

Plus... it's kinda fun for the [sysadmin inside of me](https://redshirtjeff.com/listing/cosplaying-as-a-sysadmin?product=211) to see how my build [stacks up historically against the top500 supercomputers](https://hpl-calculator.sourceforge.net/hpl-calculations.php).

But I had a problem: HPL is hard to get running across multiple architectures and types of systems. Trying to get it running on niche setups (like Raspberry Pi clusters) leads you down a rabbit hole of outdated blog posts and tricky hacks.

So after working on automating the HPL runs for the past couple years, I finally set up a new project, [top500-benchmark](https://github.com/geerlingguy/top500-benchmark), which currently targets Ubuntu and Debian, and runs on either a single node or a cluster.

I've tested it with my Pi cluster, with my AMD Ryzen 5 5600x desktop, with Patrick's Supermicro Ampere Altra Max system, and even with my M1 Max Mac Mini (via Docker)!

The playbook compiles MPI, attempts to set the system's CPU scaling governor into 'performance' mode (otherwise the results can be a bit unstable), compiles ATLAS, then compiles and runs HPL using a tunable HPL.dat file.

For help running the setup on your own server or cluster, see the [project README](https://github.com/geerlingguy/top500-benchmark#top500-benchmark---hpl-linpack). There may be a few bugs still, as I've only tested across 6 different systems (2 clusters and 4 workstations/servers), but feel free to open an issue if you encounter any problems!

## Results

The Pis are slow, but relatively efficient, beating out my Ryzen 5 5600x system—admittedly in a build not well optimized for efficiency.

{{< figure src="./m1-max-vs-amd-ryzen-vs-ampere-altra-vs-raspberry-pi-gflops-efficiency.jpg" alt="Gigaflops per watt efficiency - Raspberry Pi cluster vs M1 Max Mac Studio vs Ampere Altra Max vs AMD Ryzen 5 5600x" width="700" height="394" class="insert-image" >}}

The Ampere system blows past the Pi cluster and AMD desktop, but isn't even half as efficient as the silent little M1 Max Mac Studio on which I'm writing this post!

But efficiency isn't everything—for every use case, you have to consider things like noise, performance and power requirements, software compatibility, etc.

And we're not comparing everything on an even playing field, either. There's infinitely more expansion in the Supermicro server than my M1 Max Mac Studio, and the Ryzen setup I tested was built for gaming and AI testing, not for silence or power efficiency.

## Conclusion

Like I said at the beginning of this post, sometimes life throws interesting opportunities your way. In my case I was lucky enough to spend a little time with the Ampere Altra Max. Now I have a point of reference for 'the fastest ARM CPU that can be bought today.' That's a helpful point of reference as I spend most of my days twiddling with tiny ARM systems that are less than 1/100th as powerful!

This opportunity was also the final push towards abstracting my cluster [HPL benchmarking tool](https://github.com/geerlingguy/top500-benchmark#top500-benchmark---hpl-linpack) into its own project. Hopefully more people can experience the ear-piercing whine of server fans as their own servers and clusters plod along trying to place atop the Ampere Altra Max.
