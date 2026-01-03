---
nid: 3282
title: "Testing a 96-core Ampere Altra Developer Platform"
slug: "testing-96-core-ampere-altra-developer-platform"
date: 2023-04-21T14:00:22+00:00
drupal:
  nid: 3282
  path: /blog/2023/testing-96-core-ampere-altra-developer-platform
  body_format: markdown
  redirects:
    - /blog/2023/testing-ampere-altra-developer-platform
aliases:
  - /blog/2023/testing-ampere-altra-developer-platform
tags:
  - altra
  - ampere
  - arm
  - pc
  - reviews
  - video
  - workstation
  - youtube
---

If you're tired of waiting for Apple to migrate its Mac Pro workstation-class desktop to Apple Silicon, the [Ampere Altra Developer Platform](https://www.ipi.wiki/products/ampere-altra-developer-platform) might be the next best thing:

{{< figure src="./ampere-altra-developer-platform-hero-shot.jpeg" alt="Ampere Altra Developer Platform in Jeff Geerling's workshop" width="700" height="394" class="insert-image" >}}

I somehow convinced Ampere/ADLINK to send me a workstation after my now [_years-long_ frustrated attempts at getting graphics cards working on the Raspberry Pi](/blog/2023/i-built-special-pcie-card-test-gpus-on-pi). And they sent me a beast of a machine:

  - Ampere Altra Max M96-28 on a COM-HPC daughter card (96 cores @ 2.8 GHz)
  - 64 GB of ECC DDR4-3200 RAM
  - 128 GB NVMe M.2 storage

The individual cores are quite a bit slower than Apple's latest M2 cores (less than _half_ as fast!), but the Neoverse N1 cores are on par with the latest Qualcomm offerings and give similar performance to any Arm cloud servers on the market today.

And... there are _ninety-six_ of them!

In many ways, this workstation is _better_ than any Arm machine Apple has on offer right now (and I say that as a Mac Studio owner...):

  - It has upgradeable RAM
  - It has an upgradeable CPU
  - It has upgradeable NVMe SSD storage
  - It has _five_ PCI Express slots (3 PCIe Gen 4 x16, 2 PCIe Gen4 x4)
  - It uses a standard PC form factor (allowing for different cases, power supplies, and cooling options
  - It even includes a BMC (from ASPEED) for remote IPMI management! (Though this consumes 3-5W at all times, even when the workstation is powered off)

There's something to be said for having nearly the same power (with a competent integrated GPU) silently running in a couple liter case, in the form of the Mac Studio.

But if you want the fastest and most expandable Arm desktop on the planet right now—and one that runs Linux _natively_, no hacky setup required—this is it.

This unit has ['SystemReady' certification](https://www.arm.com/architecture/system-architectures/systemready-certification-program), meaning I should be able to download any standard Linux distro and install it, no custom DTBs or images required. I flashed [Ubuntu 22.04 Server for Arm](https://ubuntu.com/download/server/arm), to a USB drive, inserted it, and installed over the default Ubuntu 20.04 install on the internal NVMe drive. No problems at all! I also downloaded [Ubuntu 22.04 desktop](https://cdimage.ubuntu.com/jammy/daily-live/current/), and that worked fine too.

## Performance

{{< figure src="./ampere-altra-com-hpc-daughtercard-running-developer-platform-adlink.jpeg" alt="Ampere Altra Max 96-core CPU on COM-HPC daughtercard in ADLINK Developer Platform" width="700" height="467" class="insert-image" >}}

The 96-core version I have only had four of the six RAM slots populated, so it's [leaving a little performance on the table due to cross-core NUMA latency](https://connect-admin.amperecomputing.com/api/secure-file-download/download-regular?file=new-private-files/94/tech/Altra_Family_NUMA_Optimization_Guide_v0.50_20211020.pdf&amp;type=technical-document&amp;doc_id=678) in the current configuration. But I ran various benchmarks on the system as configured. (Use [this link](https://github.com/geerlingguy/sbc-reviews/issues/19) to read through my raw benchmarking results.)

Geekbench is far from perfect, but it's fun to run since it's been run on anything from multi-processor servers down to single board computers.

[This system](https://browser.geekbench.com/v5/cpu/21070727) got an 807 for single-core, which isn't all that fast, about on par with 6th or 7th-gen Intel CPUs. But you don't go Ampere for single core performance. The multicore score of 30,121 is faster than any other CPU I've _personally_ tested, and there's room for improvement. There may be some buggy tests in Geekbench 5 that don't take advantage of all 96 cores, and I haven't successfully run [the preview release of Geekbench 6 for Arm yet](https://www.geekbench.com/preview/)—see [this bug report](http://support.primatelabs.com/discussions/geekbench/81903-geekbench-6-for-linux-arm64-raspberry-pi-asahi-on-mac-etc).

A more practical benchmark is the Top500's favored benchmark, High-Performance Linpack (or HPL). I ran it using my open source [top500-benchmark](https://github.com/geerlingguy/top500-benchmark) automation.

The first time I ran it, I set it to distribute linear math equations to all 96 cores as fast as it could.

That gave me 377 Gflops at 220W, giving me an efficiency of 1.71 Gflops/W. That's fast, but we can do better. Remembering the core layout discussion from [this Anandtech article](https://www.anandtech.com/show/16979/the-ampere-altra-max-review-pushing-it-to-128-cores-per-socket/3), I decided to adjust `Ps` to 4 and `Qs` to 24, to try to separate out the problems among the four quadrants of the massive chip.

The score was much better, hitting 401 Gflops at 200 Watts, with an efficiency of 2.01 Gflops/W.

{{< figure src="./performance-efficiency-ampere-altra-96-core-graph.png" alt="Performance and efficiency graph for HPL benchmark for Ampere Altra 96-core CPU" width="700" height="394" class="insert-image" >}}

That's 6% more performance, and _16%_ more efficiency, just by optimizing the way the software runs.

We could probably get even more performance, too. I love doing tests like this, because it illustrates two things:

  1. Single benchmark numbers are meaningless. Keep that in mind whenever you're looking at reviews.
  2. On modern chip architectures, _software support_ is just as important as the hardware itself to unlock all the performance.

Across a range of Phoronix benchmarks ([example](https://openbenchmarking.org/result/2304174-NE-AMPEREALT36&amp;grs), [example 2](https://openbenchmarking.org/result/2304174-NE-AMPEREALT14)), this CPU is usually in the upper end of performance (compared to most _desktop_ CPUs at least)—but it's not the top dog.

Most of the time, that honor goes to AMD's latest EPYC chips. Those things are _monsters_ when it comes to performance.

But this chip does shine in some areas, like for multi-tenant web application servers, and _especially_ for efficiency, at least under load. My Mac Studio still owns the efficiency crown (I get 4 Gflops/W on it!)—which is why I'd love to see Apple make a true "Pro" workstation. But the Ampere is a lot more efficient than X86 for most workloads, which is why so many cloud providers have been pushing Arm lately (as fast-but-efficient rather than bleeding-edge performance is an ever-growing concern in modern datacenters).

I should note that this system burns through 60-70W at idle, a symptom of the system's overall "stripped down server" heritage (versus Apple Silicon's "built up from a mobile phone"). I can imagine a future Ampere system being lighter on power usage at idle—it's just not something this current generation had as a design goal.

## Windows

After seeing [this video from I-Pi demonstrating Windows on Ampere](https://www.youtube.com/watch?v=Rxe-UyDq5XY), I decided to try installing Windows on a second NVMe SSD.

The first thing I tried was finding a Windows on Arm ISO. Microsoft, unfortunately, only offers an x86 Windows 11 ISO on their [download page](https://www.microsoft.com/en-us/software-download/windows11/).

Searching around, I found the [Windows 11 on Arm Insider Preview](https://www.microsoft.com/en-us/software-download/windowsinsiderpreviewarm64), which requires an Insider account. Well that's okay, I already have one...

Except... apparently my account was blocked for some reason. I got [this error](https://twitter.com/geerlingguy/status/1644808038321119233) every time I tried downloading it. And I tried Safari, FireFox, and Chrome. I even tried Edge on my Windows 11 PC! Nothing worked.

So I tried building a custom ISO using [UUPDump](https://uupdump.net/), but the image it generated just resulted a Synchronous Exception, and the installer wouldn't boot.

Over [on Twitter](https://twitter.com/geerlingguy/status/1648017930766917634), people offered suggestions, ranging from installing Parallels or VMWare Fusion on my Mac, to using other UUP tools, to even downloading a recovery image for my Windows Dev Kit (see my [Dev Kit review](/blog/2022/testing-microsofts-windows-dev-kit-2023)).

That seemed like the easiest path forward, so I fished out the hardware to grab the serial number. I input that, downloaded the zip file, expanded it, used the Recovery Tool to create a USB install drive, and finally copied over all the Windows Dev Kit recovery files.

Did _that_ work? Nope :(

[Paul on Mastodon](https://mas.to/@pauld/110215582878031319) suggested I install Parallels on my Mac and use the ISO it generates. So, I did that!

{{< figure src="./windows-boot-logo.jpg" alt="Windows boot logo on Ampere Altra Developer Platform" width="700" height="394" class="insert-image" >}}

That got _further_, to the point it looked like Windows started booting—but I got the blue screen of death.

I was about to give up when I found [this article from Cloudbase](https://cloudbase.it/ampere-altra-industry-leading-arm64-server/). It seems they got it working on a server-grade Ampere Altra system. And they even documented the process—which required that unobtainable Windows for Arm Preview download!

So I got help from David Burgess over on [DB Tech](https://www.youtube.com/channel/UCVy16RS5eEDh8anP8j94G2A) (thanks, David!). He was able to download the VMDK file and sent it to me.

I converted it from a VMDK file to a raw disk image using `qemu-img`, then I copied that onto the NVMe drive on the machine. And, after a reboot, it... did the exact same thing as the Parallels image:

{{< figure src="./windows-bsod-acpi-bios-error.jpg" alt="Windows 11 Blue Screen of Death ACPI_BIOS_ERROR message on Ampere Altra Developer Platform" width="700" height="394" class="insert-image" >}}

It looks like I'm still getting a BIOS error.

## Expansion - Graphics

Moving on from Windows, I decided to test at least one of my Nvidia graphics cards.

The I-Pi Wiki includes a [list of approved graphics cards](https://www.ipi.wiki/pages/comhpc-docs?page=NVIDIA_cards.html), and _supposedly_ some other ones should work too. (I mean, Gigabyte seems to have Ampere servers with [A100s practically oozing out of them](https://www.servethehome.com/gigabyte-g492-pd0-is-the-ampere-altra-max-arm-nvidia-a100-server/)!)

{{< figure src="./nvidia-rtx-8000-in-ampere-developer-platform.jpeg" alt="Nvidia RTX 8000 installed in Ampere Altra Developer Platform" width="700" height="467" class="insert-image" >}}

I spent a few hours trying to get this RTX 8000 working. Just like on the Raspberry Pi and Rock 5 B, it was recognized, and I could install Nvidia's Arm drivers.

{{< figure src="./rm_init_adapter-failed-nvidia-driver-error-ampere-altra-arm-rtx-8000.jpg" alt="rm_init_adapter failed Nvidia driver exception on Ampere Altra Developer Platform" width="700" height="394" class="insert-image" >}}

But I still ended up getting this 'RM Init Adapter' failed error, and I couldn't get the card working.

I'll keep plugging away, though. Make sure you [subscribe to this blog](https://www.jeffgeerling.com/blog.xml) or [my YouTube channel](https://www.youtube.com/c/JeffGeerling) to follow along!
