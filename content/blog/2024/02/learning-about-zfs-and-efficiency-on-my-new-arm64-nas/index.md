---
nid: 3352
title: "Learning about ZFS and efficiency on my new Arm64 NAS"
slug: "learning-about-zfs-and-efficiency-on-my-new-arm64-nas"
date: 2024-02-29T16:53:20+00:00
drupal:
  nid: 3352
  path: /blog/2024/learning-about-zfs-and-efficiency-on-my-new-arm64-nas
  body_format: markdown
  redirects:
    - /blog/2024/learning-about-zfs-on-my-new-arm64-nas
aliases:
  - /blog/2024/learning-about-zfs-on-my-new-arm64-nas
tags:
  - 45drives
  - cockpit
  - hl15
  - houston
  - linux
  - nas
  - video
  - youtube
  - zfs
---

{{< figure src="./hl15-ampere-altra-fully-built.jpeg" alt="HL15 with Ampere Altra and ASRock Rack motherboard - NAS fully built" width="700" height="auto" class="insert-image" >}}

I've been building out a new Arm-based NAS using ASRock Rack's new 'Deep Micro ATX' motherboard for Ampere Altra and Altra Max CPUs.

I posted about the hardware earlier, in [Building an efficient server-grade Arm NAS](/blog/2024/building-efficient-server-grade-arm-nas). Go check that out if you want details on the specific hardware in this setup.

But at the end of the build, I installed Rocky Linux, and found the power consumption to be a bit higher than expected—over 150W at idle!

As it turns out, the NAS must've been doing something when I took that initial measurement, because after monitoring it for a few more days, the normal idle power usage was around 123W instead.

I wanted to get ZFS running on the NAS, and ideally use 45Drives' [Houston Command Center](https://www.45drives.com/blog/storage/software/houston-overview-a-linux-server-ui-by-45drives/), especially since they maintain plugins to integrate with their hardware products. The [45Homelab HL15](https://store.45homelab.com/configure/hl15) is a nice, if expensive, homelab/SMB-oriented rackmount or desktop 15-bay storage chassis.

However, I ran into problems:

  - Rocky Linux (indeed, all RHEL-derivative distros) doesn't have pre-built ZFS packages available in the default repos, and OpenZFS [so far doesn't build packages for arm64 on EL](https://github.com/openzfs/zfs/issues/14511) either. I could manually compile ZFS, but don't want to take on that maintenance burden.
  - [45Drives' own repositories](https://repo.45drives.com) are maintained only for x86_64. This means I'd have to try my hand compiling their Cockpit plugins for arm64, something [it doesn't look like anyone's attempted before](https://forum.45homelab.com/t/houston-cockpit-setup-on-arm64/).

As a result, I switched to Ubuntu 22.04, which includes ZFS packages in the default repositories, and is also feels a little more finely-tuned for arm64, especially Ampere CPUs, than Red Hat derivatives. (I should mention I'm happy to see standard UEFI-compatible builds of all the major distros that are arm64-compatible. Rocky Linux worked great in my testing, outside of the ZFS use case!)

{{< figure src="./hl15-arm-nas-ansible-playbook.png" alt="HL15 Arm NAS Ansible Playbook YAML" width="700" height="auto" class="insert-image" >}}

All that decided, it was pretty easy to build up my Ansible playbook to install ZFS and configure some storage pools. That playbook is available under an open source license here, by the way: [hl15-arm-nas](https://github.com/geerlingguy/hl15-arm64-nas).

I made an entire video about my experiences, embedded below—but scroll past it if you just want to see my test data and conclusions:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/iD9awxmOGG4" frameborder='0' allowfullscreen></iframe></div>
</div>

## Power Efficiency

First, I decided to get a feel for the power consumption of various components in the system. My test method was to use a [Thirdreality Zigbee power metering plug](https://amzn.to/49oQONb), connected to Home Assistant, where I set up a dashboard with an [ApexCharts card](https://github.com/RomRider/apexcharts-card), to monitor power consumption over time.

I booted the entire system, waited 5 minutes for idle power to level off, and took a measurement. Then I shut down, removed one component (e.g. the hard drives, or the HBA), and booted back up.

{{< figure src="./hl15-power-testing-full-graph.png" alt="HL15 Power Testing - Full Graph" width="700" height="auto" class="insert-image" >}}

After a few hours, here are the results of that testing:

| Device | Idle power* (W) |
| --- | --- |
| Samsung QVO 8TB SATA SSD (x1) | 1W |
| Seagate Exos 20TB SATA HDD (x1) | 6W |
| Broadcom MegaRAID 9405W-16i HBA | 16W |
| Samsung 16GB ECC DDR 3200 RAM (x1) | 3W |
| CoolerGuys Case Fan (x1) | 2W |
| Noctua CPU Cooler Fan (80mm) | ~ |
| Intel X550 10G Ethernet (x1) | 2W |
| Ampere Altra Q32-17 CPU | 9W |
| ASPEED BMC running OpenBMC (integrated) | 6W |

That left about 20W being used up by the motherboard and power supply losses. Not that bad, actually, and I think I could get a Titanium-rated PSU that has higher efficiency in the 100-watt range, to bring down power draw even further.

The parts of the system consuming the most power were the HBA and hard drives—moving to all-flash, NVMe-based storage may result in some savings. The CPU IO blocks may consume more power in that scenario, but probably not as much in aggregate as the separate HBA. Also, enterprise-grade NVMe storage can eat up a bit more wattage even than HDDs... but offer magnitudes better latency and IOPS. Always a tradeoff.

To get a feel for how much performance _efficiency_ I could get, I leaned on my trusty [top500-benchmark](https://github.com/geerlingguy/top500-benchmark) project, an Ansible playbook that configures and runs HPL (High Performance Linpack), a CPU-intensive benchmark, against various systems.

The efficiency crown is currently owned by the Ampere Altra 64-core CPU, and in my system—which is not quite as power-optimized—I could get good numbers, but not quite as close.

I got 332.07 Gflops at 100W, for an overall efficiency score of 3.32 Gflops/W; that's without the extra storage and HBA attached.

Not bad at all, and even at full-tilt with all the storage installed, I can eke out 3 Gflops/W, which is better than I can do on any of my Intel or AMD systems (yet... I haven't tested some of their most efficient chips).

## ZFS Performance

With all that testing out of the way, I started benchmarking ZFS on the storage I had configured—6 Exos 20 TB hard drives, and 4 Samsung QVO 8TB SSDs, all connected through the HBA.

I wanted to see if the QVO 'consumer' grade SSDs would have any impact on performance when used as a SLOG or L2ARC, and they did—just... in a negative direction :)

I limited my testing to larger file sequential-write testing (using a test size of 128 GB to break through the 64 GB ARC cache ZFS automatically creates in RAM), and small file size testing (4K).

{{< figure src="./hl15-zfs-large-file-operations.png" alt="HL15 ZFS Large File Operations Benchmarks" width="700" height="auto" class="insert-image" >}}

The most interesting results were when I mirrored two of the SSDs as a SLOG (an external ZFS Intent Log (ZIL))—when I did that, the SSDs actually bottlenecked the hard drive array. They caused power draw to fluctuate quite a bit as the hard drives would write, then go idle waiting, then write... They also slowed down many operations to just 250 MB/sec, which was the total throughput I saw monitoring ZFS's io operations with `zpool iostat -v`.

For small files, I didn't want to sit for hours to see what the disks themselves would do, so I limited my test size to 256 MB, and got basically the same results under all scenarios since RAM speed and ARC was mostly being tested:

{{< figure src="./hl15-zfs-small-file-operations.png" alt="HL15 ZFS Small File Operations Benchmarks" width="700" height="auto" class="insert-image" >}}

I wound up sticking with the 6x HDDs in a RAIDZ2 array, which should give me enough for 500 MB/sec reads and writes or so over my 10G network, and the 4x SSDs in a mirrored vdev array, which saturates the 10G connection, at least for smaller multi-GB copies that don't fill up the drives' internal caches.

I would really like to test out some U.2 NVMe SSDs, and I still have a bit of software setup to automate—not to mention adding a second local server that will store an online replica for my second local copy of the data (RAID is not backup, remember...). But all those adventures will be documented in various issues on my [hl15-arm-nas](https://github.com/geerlingguy/hl15-arm64-nas) repo.
