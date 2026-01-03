---
nid: 3076
title: "Hardware RAID on the Raspberry Pi CM4"
slug: "hardware-raid-on-raspberry-pi-cm4"
date: 2021-02-26T16:00:56+00:00
drupal:
  nid: 3076
  path: /blog/2021/hardware-raid-on-raspberry-pi-cm4
  body_format: markdown
  redirects: []
tags:
  - broadcom
  - hdd
  - nvme
  - raid
  - raspberry pi
  - sas
  - sata
  - ssd
  - storage
  - youtube
---

A few months ago, I posted a video titled [Enterprise SAS RAID on the Raspberry Pi](https://www.youtube.com/watch?v=1gAUApGaWKk)... but I never actually showed a SAS drive in it. And soon after, I posted another video, [The Fastest SATA RAID on a Raspberry Pi](https://www.youtube.com/watch?v=oWev1THtA04).

{{< figure src="./broadcom-hba-backplane-sas-drives.jpeg" alt="Broadcom MegaRAID SAS storage controller HBA with HP 10K drives and Raspberry Pi Compute Module 4" width="600" height="389" class="insert-image" >}}

Well now I have _actual enterprise SAS drives_ running on a hardware RAID controller on a Raspberry Pi, _and_ it's faster than the 'fastest' SATA RAID array I set up in that other video.

A Broadcom engineer named Josh watched my earlier videos and realized the [ancient LSI card](https://pipci.jeffgeerling.com/cards_storage/ibm-servraid-br10i-lsi-sas3082e-r-sas-raid.html) I was testing would not likely work with the ARM processor in the Pi, so he was able to send two pieces of kit my way:

  - A [Broadcom MegaRAID 9460-16i](https://amzn.to/2PecbN1) Tri-Mode storage controller
  - A Broadcom-designed reference 'Universal Backplane' following the [SFF-TA-1005](https://www.snia.org/technology-communities/sff/specifications?field_doc_status_value=All&combine=SFF-TA-1005&items_per_page=20) standard

After a long and arduous journey involving multiple driver revisions and UART debugging on the card, I was able to bring up multiple hardware RAID arrays on the Pi.

This blog post is also available in video form on my YouTube channel:

<div class="yt-embed"><style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/Zpfq8ZC2hyI" frameborder='0' allowfullscreen></iframe></div></div>

## SAS RAID

But what is SAS RAID, and what makes hardware RAID any better than the software RAID I used in my SATA video?

The drives you might use in a NAS or a server today usually fall into three categories:

  - SATA
  - SAS
  - PCI Express NVMe

All three types can use solid state storage (SSD) for high IOPS and fast transfer speeds.

SATA and SAS drives might also use rotational storage, which offers higher capacity at lower prices, though there's a severe latency tradeoff with that kind of drive.

RAID, which stands for Redundant Array of Independent Disks, is a method of taking two or more drives and putting them together into a volume that your operating system can see as if it were just one drive.

RAID can help with:

  - Redundancy: A hard drive (or multiple drives, depending on RAID type) can fail and you won't lose access to your data immediately.
  - Performance: multiple drives can be 'striped' to increase read or write throughput (again, depending on RAID type).

Extra caching configuration (to separate RAM or even to dedicated faster 'cache' drives) can speed up things even more than is possible on the main drives themselves, and hardware RAID can provide even better data protection with separate flash storage that caches write data if power is gone.

> **Caveat**: If you can fit all your data on one hard drive, already have a good backup system in place, and don't need maximum availability, you probably don't need RAID, though.

I go into a lot more detail on RAID itself in my [Raspberry Pi SATA RAID NAS video](https://youtu.be/oWev1THtA04?t=169), so check that out to learn more.

Now, back to SATA, SAS, and NVMe.

All three of these describe interfaces used for storage devices. And the best thing about a modern storage controller like the 9460-16i is that you can connect to all three through one single HBA (Host-Bus Adapter).

If you can spend a couple thousand bucks on a fast PC with lots of RAM, software RAID solutions like ZFS or BTRFS offer a lot of great features, and are pretty reliable.

But on a system like my Raspberry Pi, software-based RAID takes up much of the Pi's CPU and RAM, and doesn't perform as well. (See [this excellent post about /u/rigg77's ZFS experiment](https://www.reddit.com/r/raspberry_pi/comments/ljwkl9/zfs_nas_experiment/)).

The fastest disk speed I could get with software mdadm-based RAID was about 325 MB/sec, and that was with RAID 10. Parity calculations may make that maximum speed even lower!

{{< figure src="./read-performance-sw-hw-raid-pi.png" alt="Sequential read performance on Raspberry Pi - Software vs Hardware RAID" width="796" height="272" class="insert-image" >}}

Using hardware RAID allowed me to get **over 400 MB/sec**. That's a 20% performance increase, AND it leaves the Pi's CPU free to do other things.

We'll get more into performance later, but first, I have to address the elephant in the room.

## Why enterprise RAID on a Pi?

People are always asking why I test [all these cards](https://pipci.jeffgeerling.com)—in this case, a storage card that costs $600 _used_—on low-powered Raspberry Pis. I even have a 10th-gen Intel desktop in my office, so, why not use that?

Well, first of all, it's fun, I enjoy the challenge, and I get to learn a lot since failure teaches me a lot more than easy success.

But with _this_ card, there are two other good reasons:

First: it's great for a little storage lab.

{{< figure src="./desk-storage-lab-pi-hba-hardware-raid.jpg" alt="Storage setup with Broadcom RAID HBA and Raspberry Pi Compute Module 4" width="649" height="365" class="insert-image" >}}

In a tiny corner of my desk, I can put 8 drives, an enterprise RAID controller, my Pi, and some other gear for testing. When I do the same thing with my desktop, I quickly run out of space. The burden of having to go over to my other "desktop computer" desk to test means I am less likely to set things up on a whim to try out some new idea.

Second: using hardware RAID takes the IO burden of the Pi's already slow processor.

Having a fast dedicated RAID chip and an extra 4 GB of DDR4 cache for storage gives the Pi reliable, fast disk IO.

If you don't need to pump through gigabytes per second, the Pi and MegaRAID together are _more energy efficient_ than running software RAID on a faster CPU. That setup used 10-20W of power.

My Intel i3 desktop running by itself with no RAID card or storage attached idles at 25W but usually hovers around 40W—twice the power consumption, without a storage card installed.

A Pi-based RAID solution isn't going to take over Amazon's data centers, though. The Pi just isn't built for that. But it is a compelling storage setup that was never possible until the Compute Module 4 came along.

## Broadcom MegaRAID 9460-16i

The MegaRAID card Josh sent is PCIe Gen 3.1 and supports x8 lanes of PCIe bandwidth.

{{< figure src="./pi-bottleneck-1x-pcie-bus-hba.jpg" alt="The Raspberry Pi's x1 PCIe Gen 2 lane is a bottleneck when using the Gen 3.1 x8 lane HBA" width="700" height="394" class="insert-image" >}}

Unfortunately, the Pi can only handle x1 lane at Gen 2 speeds, meaning you can't get the maximum 6+ GB/sec of storage throughput—only 1/12 that. But the Pi can use four fancy tricks this card has that the SATA cards I tested earlier don't:

  1. **SAS RAID-on-Chip**, a computer in its own regard, taking care of all the RAID storage operations. The Pi's slow CPU is saved from having to manage RAID operations.
  2. **4 GB DDR4 SDRAM cache**, speeding up IO on slower drives, and saving the Pi's precious 1/2/4/8 GB of RAM.
  3. Optional [**CacheVault flash backup**](https://docs.broadcom.com/doc/BC-0497EN): plug in a super capacitor, and if there's a power outage, it dumps all the memory in the card's write cache to a built-in flash storage chip.
  4. **Tri-mode ports** allow you to plug any kind of drive into the card (SATA, SAS, or NVMe), and it will work with it.

It also does everything internal to the RAID-on-Chip, so even if you plug in multiple NVMe drives, you won't bottleneck the Pi's poor little CPU (with it's severely limited IO bandwidth). Even faster processors can run into bandwidth issues when using multiple NVMe drives.

Oh, and did I mention it can connect up to 24 NVMe drives or a whopping _240_ SAS or SATA drives to the Pi?

I, for one, would love to see a 240 drive petabyte Pi NAS...

## Getting the card to work

Josh sent over a driver, some helpful compilation suggestions, and some utilities with the card.

I had some trouble compiling the driver at first, and ran into a couple problems immediately:

  - The `raspberrypi-kernel-headers` package didn't exist for the 64-bit Pi OS beta (it has since been created), so I had to compile my own headers for the 64-bit kernel.
  - Raspberry Pi OS didn't support MSI-X, but luckily Phil Elwell [committed a kernel tweak](https://www.raspberrypi.org/forums/viewtopic.php?t=293248#p1772216) to Pi OS that enabled it (at least at a basic level) in response to a forum topic on getting the Google Coral TPU working over PCIe.

With those two issues resolved, I [cross-compiled the Pi OS kernel](https://github.com/geerlingguy/raspberry-pi-pcie-devices/tree/master/extras/cross-compile) again, and fan into another issue: the driver assumed it would have `CONFIG_IRQ_POLL=y` for IRQ polling functionality, but that wasn't set by default for the Pi kernel, therefore I had to recompile _again_ to get that option working.

<p style="text-align: center;"><a href="https://redshirtjeff.com/listing/linux-recompile-shirt?product=211">{{< figure src="./red-shirt-jeff-recompile-kernel-shirt.jpg" alt="Red Shirt Jeff 0 days since I last recompiled the Linux kernel T-shirt" width="400" height="400" class="insert-image" >}}</a></p>

Finally, thinking I was in the clear, I found that the kernel headers and source from my cross-compiled kernel weren't built for ARM64 like the kernel itself, and rather than continue debugging my cross-compile environment, I bit the bullet and did the full 1-hour compile on the Raspberry Pi itself.

An hour later, the driver compiled without errors for the first time.

I excitedly ran `sudo insmod megaraid_sas.ko`, and then... it hung, and after five minutes, printed the following in `dmesg`:

```
[  372.867846] megaraid_sas 0000:01:00.0: Init cmd return status FAILED for SCSI host 0
[  373.054122] megaraid_sas 0000:01:00.0: Failed from megasas_init_fw 6747
```

Things were getting serious, because two other Broadcom engineers joined a conference call with Josh and I, and they had me pull off the serial UART output from the card to debug PCIe memory addressing issues!

We found the driver would work on _32-bit_ Pi OS, but not the 64-bit beta. Which was strange, since in my experience drivers have often worked better under the 64-bit OS.

A few days later, a Broadcom driver engineer sent over patch which fixed the problem, which was related to the use of the `writeq` function, which is apparently not well supported on the Pi. Josh filed a bug report to the Pi kernel issue queue about it: [writeq() on 64 bit doesn't issue PCIe cycle, switching to two writel() works](https://github.com/raspberrypi/linux/issues/4158).

Anyways, the driver finally worked, and I could see the attached storage enclosure being identified in the `dmesg` output!

## Setting up RAID with StorCLI

StorCLI is a utility for managing RAID volumes on the MegaRAID card, and Broadcom has a [comprehensive StorCLI reference](https://docs.broadcom.com/doc/12352476) on their website.

The command I used to set up a 4-drive SAS RAID 5 array went like this:

```
sudo ./storcli64 /c0 add vd r5 name=SASR5 drives=97:4-7 pdcache=default AWB ra direct Strip=256
```

  1. I named the `r5` array `SASR5`
  2. The array uses drives 4-7 in storage enclosure ID 97
  3. There are a few caching options.
  4. I set the strip size to 256 KB (which is typical for HDDs—64 KB would be more common for SSDs).

I created two RAID 5 volumes: one with four [Kingston SA400 SATA SSDs](https://amzn.to/3ks4vCf), and another with four [HP ProLiant 10K SAS drives](https://amzn.to/3ks4xtR).

I used `lsblk -S` to make sure the new devices, `sda` and `sdb`, were visible on my system. Then I partitioned and formatted them with:

  1. `sudo fdisk /dev/sdX`
  2. `sudo mkfs.ext4 /dev/sdX`

At this point, I had a 333 GB SSD array, and an 836 GB SAS array. I mounted them and made sure I could read and write to them.

## Storage on boot

I also wanted to make sure the storage arrays were available at system boot, so I could share them automatically via NFS, so I installed the compiled driver module into my kernel:

  1. I copied the module into the kernel drivers directory for my compiled kernel: `sudo cp megaraid_sas.ko /lib/modules/$(uname -r)/kernel/drivers/`
  2. I added the module name, 'megaraid_sas', to the end of the /etc/modules file: `echo 'megaraid_sas' | sudo tee -a /etc/modules`
  3. I ran `sudo depmod` and rebooted, and after boot, everything came up perfectly.

One thing to note is that a RAID card like this can take a minute or two to initialize, since it has its own initialization process. So boot times for the Pi will be a little longer if you want to wait for the storage card to come online first.

> **A note on power supplies**: I used a couple different power supplies when testing the HBA. I found that if I used a lower-powered 12V 2A power supply, the card seemed to not get enough power, and would endlessly reboot itself. I switched to [this 12V 5A power supply](https://amzn.to/3aTs9og), and the card ran great. (I did not attempt using an external powered 'GPU riser', since I have had mixed experiences with them.)

## Performance

With this thing fully online, I tested performance with `fio`.

{{< figure src="./fio-performance-benchmark.jpg" alt="fio 1 MB random read and write performance benchmark results on SATA SSD and SAS HDD arrays" width="700" height="394" class="insert-image" >}}

For 1 MB random reads, I got:

  - 399 MiB/sec on the SSD array
  - 114 MiB/sec on the SAS array

For 1 MB random writes, I got:

  - 300 MiB/sec on the SSD array
  - 98 MiB/sec on the SAS drives

> Note: 1.000 MiB = 1.024 MB

These results show two things:

First, even cheap SSDs are still faster than spinning SAS drives. No real surprise there.

Second, the limit to the SSD speed is the Pi's PCIe bus. I'm able to get 3.35 Gbps of bandwidth, and that's actually better than the bandwidth I could pump through an [ASUS 10G network adapter](https://pipci.jeffgeerling.com/cards_network/asus-xg-c100c-10g.html), which could only get up to 3.27 gigabits.

There are tons of other tests I could do, but I wanted to see how the drives performed for network storage, so I installed Samba and NFS and ran more benchmarks.

{{< figure src="./nfs-samba-smb-nas-network-copy-performance-pi-hardware-raid.jpg" alt="NFS and Samba performance for NAS with Pi Hardware RAID" width="700" height="394" class="insert-image" >}}

I was amazed both Samba and NFS got almost wire speed for reads, meaning the Pi was able to feed data to my Mac as fast as the gigabit interface could pump it through.

If you remember from my [SATA RAID video](https://www.youtube.com/watch?v=oWev1THtA04), the fastest I could get with NFS was 106 MB/sec, and that speed fluctuated when packets were queued up while the Pi was busy sorting out software RAID.

With the storage controller handling the RAID, the Pi was staying a solid 117 MB/sec _continuously_, during 10+ GB file copies.

## PCIe Switches and 2.5 Gbps Networking

What about 2.5 GbE networking? I actually have two PCIe switches, and a few different 2.5 Gbps NICs I've already successfully used with the Pi. So I tried using both switches and a few NICs, and unfortunately I couldn't get enough power through the switch for both the NIC and the power-hungry storage controller.

I even pulled out my 600W PC PSU, but accidentally fried it when I tried shorting the PS_ON pin to power it up. Oops.

> Watch me zap the PSU (and luckily, not myself) [here](https://youtu.be/Zpfq8ZC2hyI?t=987).

So 2.5 Gbps performance will, unfortunately, have to wait until I get a new power supply.

## Conclusion

Finally, I have true _hardware_ SAS RAID running on the Raspberry Pi. Josh was actually first to do it, though, on 32-bit Pi OS.

The driver we were testing is still pre-release, though. If you run out and buy a MegaRAID controller today, you'll have some trouble getting it working on the Pi until the changes make it into the public driver.

Am I going to recommend you buy this $1000 HBA for a homemade Pi-based NAS? Maybe not. But there _is_ a lower-end version you can get, the [9440-8i](https://www.broadcom.com/products/storage/raid-controllers/megaraid-9440-8i). Still has all the high-end features, and it's less than $200 used on eBay (Dell server pulls, mostly).

Even that might be overkill, though, if you just want to build a cheap NAS and only use SATA drives. I'll be covering more inexpensive NAS options soon, so subscribe to [this blog's RSS feed](/blog.xml), or [subscribe to my YouTube channel](https://www.youtube.com/c/JeffGeerling) to follow along!
