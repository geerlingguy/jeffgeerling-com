---
nid: 3425
title: "AmpereOne: Cores are the new MHz"
slug: "ampereone-cores-are-new-mhz"
date: 2024-12-05T15:12:27+00:00
drupal:
  nid: 3425
  path: /blog/2024/ampereone-cores-are-new-mhz
  body_format: markdown
  redirects: []
tags:
  - ampere
  - arm
  - homelab
  - servers
  - video
  - youtube
---

_Cores_ are the new megahertz, at least for enterprise servers. We've gone quickly from 32, to 64, to 80, to 128, and now to 192-cores on a single CPU socket!

{{< figure src="./ampereone-hero-open.jpeg" alt="AmpereOne A192-32X open" width="700" height="auto" class="insert-image" >}}

Amazon built [Graviton 4](https://www.aboutamazon.com/news/aws/graviton4-aws-cloud-computing-chip), Google built [Axiom](https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu), but if you want _your own_ massive Arm server, Ampere's the only game in town. And fastest Arm CPU in the _world_ is inside the box pictured above.

It has 192 custom Arm cores running at 3.2 Gigahertz, and in _some_ benchmarks, it stays in the ring with AMD's fastest EPYC chip, the 9965 "Turin Dense", which _also_ has 192 cores.

High-core-count servers are the cutting edge in datacenters, and they're so insane, most software _doesn't even know how to handle it_. `btop` has to go full screen on the CPU graph just to fit all the cores:

{{< figure src="./ampereone-btop-192-cores.jpeg" alt="AmpereOne btop 192 cores" width="700" height="auto" class="insert-image" >}}

To support all those cores, this system has 8 channels of DDR5 ECC RAM, and 128 lanes of PCIe Gen 5.

This particular system is a [Supermicro ARS-211ME-FNR](https://www.supermicro.com/en/products/system/megadc/2u/ars-211me-fnr). It's targeted at Telco Edge deployments, and this particular unit was sent by Supermicro and Ampere for testing—I've been doing that for a month now.

This blog post is a lightly-edited transcript of this video (though you can continue past it to read the rest, if you like reading more!):

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/t05OZAruyYY" frameborder='0' allowfullscreen></iframe></div>
</div>

## A Strange New Era

This _isn't_ the world's fastest single-socket server. It's not even the most _efficient_! AMD's latest EPYC 'Turin Dense' CPU takes both of those titles. But this _is_ the best value, in terms of _performance per dollar_.

This is a strange era:

  - AMD reigns for performance _and_ efficiency.
  - Arm reigns for price and specific workloads.
  - Intel, well... [they're really having a year, aren't they?](https://www.investopedia.com/intel-stock-one-disaster-after-another-chip-stocks-wall-street-8710894)

But Ampere [already announced a 256 and _512_-core variant](https://amperecomputing.com/blogs/introducing-ampereone-aurora), which will also bump the memory channels from 8 to 12. That could be a _monster_, but... it's not here yet.

This server _isn't_ targeted at HPC, or High Performance Computing.

Cores are great, but it's all about how you slice them. Don't think of this as a single 192-core server. Think of it more like _48_ dedicated 4-core servers in one box. And each of those servers has 10 gigs of high-speed RAM and consistent performance.

Before we test that, let's dive into the hardware.

## Hardware - Exterior

{{< figure src="./ampereone-remove-pcie-bracket.jpeg" alt="AmpereOne server removing PCIe bracket" width="700" height="auto" class="insert-image" >}}

And right away, you might be confused. Usually servers have their ports on the _back_, not the front. But this server is meant for Telco use for 5G, so it's short-depth, and all the ports are on the front.

Across the front, there are 6 U.2 NVMe drive bays, populated in my system with 2 TB Samsung NVMe drives. Then there's a micro USB serial port for console access, two USB 3 ports, and VGA for monitoring. Then there's a 1 Gbps IPMI port connected to the ASPEED BMC chip, which is running OpenBMC for remote administration. Finishing out the built-in IO, there are two 25 Gbps SFP28 ports, for high-speed networking.

Then there are cutouts where you can install more PCI Express cards. There's an OCP 3 slot (usually populated by more networking, like dual 100 Gbps Mellanox cards), and up to four single-height, or two dual-height PCIe cards. Two slots are PCIe Gen 5 x16, and two are PCIe Gen 5 x8, and in total this system has 4 _Teratransfers_ per second of PCI Express bandwidth, but who's counting?

The sides have mounting points for rails, and the back... doesn't have any ports at all! Well, except for power plugs for dual redundant 1600W Titanium PSUs.

The rest of the back is covered by four giant hot-swap fans with louvres on the back side. This was the first time I'd see louvres on server fans, and I couldn't find any good info about this design online, so I got an answer from Roger Chen, Supermicro's Senior Director of System Design Engineering.

{{< figure src="./ampereone-fan-spinning.jpeg" alt="AmpereOne hot swap fan spinning" width="700" height="auto" class="insert-image" >}}

He said it's so air only comes in through the front. _Makes sense!_ If a fan fails, its doors will close and no air can come in from the hotter back side of the server. And as illustrated in the picture above, the fans have a lot of momentum, so don't stick your finger in the blades if you just yanked it out!

The system's designed with N+1 fan redundancy, a term more familiar to [those in the HVAC industry](https://mainstream-corp.com/n-plus-1-vs-n-minus-1-redundancy/). Basically, fans _will_ fail, so like every other part of this server, it's designed to keep the CPU running full blast even with a dead fan.

Anyway, enough geeking out over a fan. Let's get inside.

## Hardware - Interior

{{< figure src="./ampereone-cpu-ram.jpeg" alt="AmpereOne CPU and RAM" width="700" height="auto" class="insert-image" >}}

Besides two screws retaining the lid, most parts on this system are toolless, which makes maintenance a breeze. Two PCIe risers are lifted out of the way to expose the motherboard, the OCP 3 card slot, and a plastic shroud guiding airflow around the CPU and RAM.

Pop that up, and you reveal a 22110 M.2 NVMe slot, two _additional_ unused PCIe Gen 5 x8 connectors, and the CPU and 16 RAM slots. Since this system was configured for _speed_ over raw capacity, my system only had one DIMM per channel, allowing the RAM to clock in at DDR5 5200 MT/sec.

The CPU itself uses direct-die cooling—at least for the massive CPU core tile in the middle—so I didn't want to risk removing the heatsink and damaging anything. Luckily, Patrick over on ServeTheHome did just that, and you can go look at his [pictures of the A192-32X on STH](https://www.servethehome.com/this-is-ampere-ampereone-a192-32x-a-192-core-arm-server-cpu-arm/).

The IO and memory dies surround the central CPU cores, but they are covered by a rectangular heat spreader. The heatsink provides the necessary pressure to contact the _nearly 6,000 pins_ in the LGA5964 socket.

Elsewhere, there are extra power sockets for internal PCIe cards (e.g. workstation or enterprise GPUs), tidy cabling for NVMe slots, redundant BMC firmware, and... it's fairly well crammed in, being a short-depth server!

## Telco Edge Word Soup

This isn't an HPC (High Performance Computing) server; it probably wouldn't be used to build a Top500 supercomputer—though you could if you tried.

This unit is built for Telco Edge, or more specifically, 5G Open RAN.

Edge is just a fancy way of saying "we put all our servers in the cloud, but then people started noticing latency was worse, so now we're putting some servers back closer to where people use them."

There are _thousands_ of remote cell sites and regional mini-datacenters. If you can [cache the most popular stuff you run on your cell network](https://stlpartners.com/articles/edge-computing/what-is-edge-computing/) on a server running at the 'edge', like in a regional facility or at individual cell sites, that saves a lot over cloud solutions like AWS.

{{< figure src="./ampereone-nvme-bays.jpeg" alt="AmpereOne 6 U.2 NVMe SSD bays" width="700" height="auto" class="insert-image" >}}

Telco companies run a _lot_ of services. So having a machine like this running 48 4-core VMs with great performance for each service makes sense. Using the 6 U.2 slots, you could cache a hundred _terabytes_ of data at the edge, all at ridiculously high speeds.

This Supermicro system is certified at [NEBS level 3](https://en.wikipedia.org/wiki/Network_Equipment-Building_System), which just means all the parts have been tested for deployment in Telco exchanges. There are standards for fire suppression, vibration resistance, airflow, redundancy, and efficiency limits.

ORAN, or Open RAN, stands for [Open Radio Access Networks](https://www.keysight.com/us/en/assets/7121-1103/ebooks/The-Essential-Guide-for-Understanding-O-RAN.pdf). Vendors like Ampere and Supermicro are standards-based, meaning they don't throw in proprietary connections or software. You drop in one of these servers use it for 5G right away.

## Other uses

You can configure these servers for other things too, like for GPU workloads. That could accelerate machine learning or LLMs even better.

You can also build them as CI servers, if you develop software for cars, Macs, or other Arm platforms.

Finally, _webservers_ and web apps are a sweet spot for the custom Arm cores. You get a similar efficiency advantage as [AWS Graviton](https://aws.amazon.com/ec2/graviton/) or [Google Axion](https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu), except... you can actually _buy one of these_ and run it in your own datacenter.

## Getting it running

The short depth made it easy to install in my rack. I put in the rails, and could haul it over to the rack without assistance.

Right after I installed it, though, I found one of the RAM sticks was spitting out 'correctable ECC' errors during benchmarks. Ampere quickly shipped a replacement, and it was easy pulling the server and replacing the stick of RAM right in the rack.

My initial testing uncovered a few quirks. Ampere shipped this with a 64 kilobyte page size for the Linux kernel. This is actually [way more efficient than the 4K default](https://www.phoronix.com/review/aarch64-64k-kernel-perf/3) most people use. And that's why Apple and even Raspberry Pi switched to 16K now.

But if some software bails out on 16K, even _more_ programs don't know what to do when you try running 'em on 64K! And [Geekbench 6 is one of those programs](http://support.primatelabs.com/discussions/geekbench/86728-cant-run-geekbench-6-arm-preview-on-ampereone-192-core-system).

But then after discussing this with Patrick from STH, I realized something he concluded much earlier: [Geekbench 6 is a _really_ bad benchmark for servers with big CPUs](https://www.servethehome.com/a-reminder-that-geekbench-6-is-not-for-big-cpus/)!

I switched to a 4K kernel and ran Geekbench 5 instead, and I got a score [over _80,000_ multi-core](https://browser.geekbench.com/v5/cpu/23018587). That's [not the world record](https://browser.geekbench.com/v5/cpu/multicore?page=10), but it's up there with much more expensive AMD EPYC chips, at least.

## Performance

All my benchmark results and testing notes are documented in my sbc-reviews repo: [AmpereOne A192-32X (Supermicro)](https://github.com/geerlingguy/sbc-reviews/issues/52). Yes, this is a bit more than an SBC, but that's where I put my results, so deal with it :)

Unsurprisingly, on my 25 Gbps network, I got 20 gigabits per second between my [ZFS Arm NAS](https://github.com/geerlingguy/arm-nas) and this server.

With Samba, I could copy files over the network between between 8 to 15 Gigabits, which makes sense with all the overhead of Samba and Ethernet.

Even though it's a little silly, I kicked things off with an HPC benchmark: HPL, or High Performance Linpack.

Letting the thing rip, the 192 core CPU gets [_three teraflops_ of FP64 compute](https://github.com/geerlingguy/top500-benchmark/issues/43). That's almost [3x as fast as an Nvidia 4090](https://www.pugetsystems.com/labs/hpc/NVIDIA-RTX4090-ML-AI-and-Scientific-Computing-Performance-Preliminary-2382/#HPL_Linpack). Granted, that card isn't targeted at the same kind of workloads.

{{< figure src="./ampere-apple-m4-top500-efficiency.jpg" alt="AmpereOne vs Apple M4 Efficiency" width="700" height="auto" class="insert-image" >}}

During that run, the system used almost 700W, making it _nearly_ the most efficient Arm computer I've ever tested. That is, until Apple released the M4! But over 4 Gflops/W is still pretty awesome!

If I bump the clock speed down to 2.6 Gigahertz, and unplug the power-hungry NVMe drives, I can knock out 4.82 Gflops/W, which is frankly amazing.

I don't have an AMD Turin system to test, but I'm in awe that we can build 2U servers with this much power and efficiency in a single socket.

The Turin CPU may be more efficient overall, but one thing the AmpereOne excels at is native arm64 software. To that end, Ampere actually built a specialty benchmark: [`qemu-coremark`](https://github.com/AmpereComputing/qemu-coremark).

It sets up as many 4-core Arm VMs as possible, and runs coremark inside each. _Obviously_ this is slanted in Ampere's favor, but if you _do_ have Arm native software, like if you're running web services or developing for cars which mostly run on Arm, you might be interested in the results.

{{< figure src="./qemu-coremark-benchmark-result-ampereone.jpg" alt="QEMU Coremark arm64 VM benchmark results" width="700" height="auto" class="insert-image" >}}

On this server, I get an aggregate score of about 4.7 million. On a _256-core_ Intel Granite Rapids system with two sockets—one that Wendell from Level1Techs tested—it only gets 1.25 million. That's with 64 more physical CPU cores on a hyperthreaded machine—but of course it's emulating Arm.

Now I have to be completely transparent: Ampere is probably using coremark here because it's one of the few benchmarks where [Phoronix found the AmpereOne system still beats AMD](https://www.phoronix.com/review/amd-epyc-9965-ampereone/3). So not only will it perform worse core-for-core, x86 gets slaughtered if it has to run it emulating the arm64 instruction set!

But if you run Arm-native software, this is a very real picture of the speedup you get running it on Arm-native servers.

I ran through a gauntlet of other tests, too. Linux compiles in under a minute. 64 megabyte memory reads have < 50ns latency. And the PCIe Gen 4 NVMe drives it shipped with hit 8 GB/sec in RAID 0.

Also, with 512 gigs of RAM and a massive CPU, it can run a 405 _billion_ parameter Large Language Model. It's not _fast_, but it did run, giving me just under a token per second.

Ampere has an [optimized version of llama.cpp](https://github.com/AmpereComputingAI/llama.cpp) that can run models even faster.

I'm much more comfortable benchmarking SBCs than servers, though. For raw numbers and more thorough analysis, I'd suggest you read through other articles:

  - Phoronix: [192 Core ARM Server Performance & Power Efficiency](https://www.phoronix.com/review/ampereone-a192-32x)
  - Serve The Home: [AmpereOne A192-32X Review: A 192 Arm Core Server CPU](https://www.servethehome.com/ampere-ampereone-a192-32x-review-a-192-arm-core-supermicro-nvidia-broadcom-kioxia-server-cpu/)
  - Chips and Cheese: [AmpereOne at Hot Chips 2024: Maximizing Density](https://chipsandcheese.com/p/ampereone-at-hot-chips-2024-maximizing-density)

## Quirks and Growth

One thing I don't like about AmpereOne, at least in its current state: idle power consumption.

Doing nothing at all, this machine is burning 200W of power. Removing most of the RAM and the NVMe drives lowers that a little, but it's still a _lot_ of power if you don't run heavy workloads all day.

Having 128 lanes of PCIe is a factor, but even Intel and AMD have better idle states, to the point some EPYC systems idle well under 100W.

AmpereOne is also late. There was a ton of buzz back when it was announced, [back in May—of _2023_](https://amperecomputing.com/press/ampere-unveils-processor-ampereone-192-cores).

If they had shipped by the end of 2023, Ampere could've reigned supreme at the top of the server CPU market for performance _and_ efficiency, if only for a little while.

But for whatever reason, the actual shipping CPUs didn't start rolling out until late this year, after AMD stole their thunder with 'Turin Dense'.

The other problem with the year-plus delay is how it sets expectations moving forward.

Ampere announced the [Aurora](https://amperecomputing.com/blogs/introducing-ampereone-aurora), a 512-core monster CPU with 12 memory channels, back in June. Will it ship in 2025? It's anyone's guess. But I do hope so.

The other theme this year is _Arm is not niche_ anymore.

Arm's grown up. I've been running a ZFS NAS with hundreds of gigs of ECC RAM, 25 gig networking, U.2 NVMe storage, and a hundred terabytes of hard drives, for almost a year now. Every single video I've uploaded in the last 6 months was edited on its disks.

The idea that Arm is experimental, or that you can't run something on Arm, is outdated. Even high-end Arm SBCs running the RK3588 are fast enough to handle edge server use cases.

Some server software, like TrueNAS, [still doesn't support Arm](https://forums.truenas.com/t/truenas-scale-on-arm-2024-thread/2706), but the amount of software that _doesn't_ run on Arm is shrinking by the day.

Only Windows and certain niche server apps seem to be lagging. I already showed off how Windows on Arm runs [better on the Ampere Altra than on Microsoft's own Arm PCs](https://www.youtube.com/watch?v=thz5S_uciHk).

Of course, Linux is still better if you want: GPU support, better performance, and drivers for practically anything. But it's nice to see Microsoft slowly joining the Arm party.

Microsoft's been running Ampere in their own cloud service [since 2022](https://azure.microsoft.com/en-us/blog/azure-virtual-machines-with-ampere-altra-arm-based-processors-generally-available/)! The obvious question is why doesn't Microsoft support Windows on Arm on the only CPUs that can run it to its full potential?

## Conclusion

But let's not get sidetracked. My main takeaway today is we're seeing the death of certain computing myths.

  - **"x86 has faster single core performance"**: Apple's ruled that out with their M4
  - **"Arm is more efficient"**: that's not always true—AMD just built the most efficient 192 core server this year, beating Ampere!

The big difference is the AmpereOne A192-32X [is $5,555](https://www.phoronix.com/review/ampereone-a192-32x), while the EPYC 9965 is [almost _$15,000_](https://www.amd.com/en/newsroom/press-releases/2024-10-10-amd-launches-5th-gen-amd-epyc-cpus-maintaining-le.html)!

{{< figure src="./ampereone-s-tui-stable.jpeg" alt="AmpereOne s-tui running stable at full speed" width="700" height="auto" class="insert-image" >}}

If you want the fastest, most efficient server CPU, that's the EPYC. But if you want the best _value_, the best performance per dollar, it's the AmpereOne—at least assuming the list prices are anywhere near reality. And I think that's why Amazon, Google, Microsoft—all the cloud providers, really—can charge less for more, when they run on Arm.

We're in a strange place. Arm and x86 are both valid options now, depending on what you want, whether that's the best performance, or the best value.

The 192-core AmpereOne arrived a year too late to be the smash hit I originally expected, but it still could win out for value this generation.

I'm also happy to see systems like this that run without exotic water cooling and 240V power. Some high-end enterprise servers will be impossible to repurpose for a homelab in a few years, but this one isn't.

---

_Thanks to Supermicro and Ampere for providing the server. Thanks to Wendell from Level1Techs, Patrick from ServeTheHome, and Jeff from Craft Computing for their assistance in running some benchmarks._
