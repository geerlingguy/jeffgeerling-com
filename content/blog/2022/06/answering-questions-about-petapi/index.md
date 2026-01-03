---
nid: 3219
title: "Answering Questions about the PetaPi"
slug: "answering-questions-about-petapi"
date: 2022-06-22T13:59:20+00:00
drupal:
  nid: 3219
  path: /blog/2022/answering-questions-about-petapi
  body_format: markdown
  redirects:
    - /blog/2022/answering-questions-about-petapi-12-petabyte-raspberry-pi
aliases:
  - /blog/2022/answering-questions-about-petapi-12-petabyte-raspberry-pi
tags:
  - hba
  - nas
  - petabyte
  - petapi
  - raspberry pi
  - storage
  - video
  - youtube
---

A few weeks ago, I posted a video about the [Petabyte Pi Project](https://www.youtube.com/watch?v=BBnomwpF_uY)—an experiment to see if a single Raspberry Pi Compute Module 4 could directly address _sixty_ 20TB hard drives, totaling 1.2 Petabytes.

{{< figure src="./petabyte-of-seagate-exos-hard-drives.jpeg" alt="Petabyte of Seagate Exos Hard Drives" width="700" height="423" class="insert-image" >}}

And in that video, it _did_, but with a caveat: RAID was unstable. For some reason, after writing 2 or 3 GB of data at a time, one of the HBAs I was using would flake out and reset itself, due to PCI Express bus errors.

{{< figure src="./raspberry-pi-petapi-hbas-storinator.jpeg" alt="Raspberry Pi inside Storinator XL60 with 4 HBAs 60 drive PetaPi" width="700" height="467" class="insert-image" >}}

Since publishing that video, I've done a lot more testing, based on suggestions from viewers and the Broadcom engineers I've worked with to get [some of their LSI HBAs and RAID cards working on the Pi](https://pipci.jeffgeerling.com/#sata-cards-and-storage).

> I also made a video for this blog post answering even more questions than I do in this blog post, like 'what does it sound like when 60 enterprise hard drives power down?'—check it out here: [It works! 1.2 Petabytes on the Raspberry Pi](https://www.youtube.com/watch?v=R2S2RMNv7OU).

## HBA Firmware

The first thing I tried was upgrading the firmware on the HBAs—four Broadcom 9405W-16i cards. I noticed they were on version 5, which was from _November 2017_. A _lot_ has changed in the past five years, and HBAs and RAID cards see a lot of active development to fix bugs, optimize throughput, etc., since they basically run their own on-chip OS.

But upgrading firmware wasn't a walk in the park. I tried on the Pi, but got an 'image signature validation' error.

{{< figure src="./flash-broadcom-hba-pc.jpg" alt="Flash Broadcom HBA in Windows PC" width="700" height="394" class="insert-image" >}}

So I popped one of the cards into my little HP desktop running Windows 10, and tried upgrading, but got a similar error: "The firmware flash image is invalid"

You can [read through the whole journey in this GitHub issue](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/196#issuecomment-1140383611), but I'll just get to the point: I had to use a very old version of StorCLI (Broadcom's storage CLI utility) to flash any firmware version newer than 14 to these 94xx-series cards.

And it's not just me—another user in that GitHub thread had the same problem, and wound up confirming the same fix worked for him. Maybe this blog post will motivate one of the Broadcom engineers to fix up whatever bug was introduced in storcli that breaks firmware upgrades for their older 94xx lineup of HBAs... or at least the 9405W-16i!

Once I upgraded the firmware on all four cards to the latest version (23 as of this writing), I re-tested all 60 drives in a Btrfs RAID 0 array, and this time, it was more stable, and _very_ slightly (but measurably) faster.

{{< figure src="./card-reset-fault-state-hba-mpt3sas.jpg" alt="Card reset diagnostics from mpt3sas driver in Linux" width="700" height="394" class="insert-image" >}}

I still experienced random card resets under load (see dmesg output above), but now instead of having one or two hard drives drop off after the card came back up, all drives would come back, and long file copies (e.g. 50+ GB) would complete!

But that's still not a great experience—a card reset takes 1-3 minutes, and during that time, no disk activity goes through, so users are stranded until the drives come back online.

## Forcing PCI Express Gen 1 speeds

Some users suggested I force PCI Express Gen 1 speeds (2500 MT/sec versus 5000 MT/sec on Gen 2). This would result in diminished performance, but the hope is that with a slower speed, the USB 3-cable-based link between the Pi's x1 slot and the PCI Express switch board I was using would be more stable—if that was the issue.

So I found [Alex Forencich's `pcie-set-speed.sh` script](https://www.alexforencich.com/wiki/en/pcie/set-speed) and ran it:

```
pi@sas:~ $ sudo ./pcie-set-speed.sh 03:00.0 1
Link capabilities: 0173dc12
Max link speed: 2
Link status: 7012
Current link speed: 2
Configuring 0000:02:01.0...
Original link control 2: 00000002
Original link target speed: 2
New target link speed: 1
New link control 2: 00000001
Triggering link retraining...
Original link control: 70110040
New link control: 70110060
Link status: 7011
Current link speed: 1
```

I confirmed the link speed as reported by `lspci` was downgraded:

```
		LnkSta:	Speed 2.5GT/s (downgraded), Width x1 (downgraded)
			TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
```

And I did the same for all four HBAs. I re-created my Btrfs RAID 0 array, and as expected, the raw performance under Gen 1 speeds was slower than under Gen 2 (at least for short periods):

{{< figure src="./pcie-speed-comparison-gen1-gen2-hbas.png" alt="PCIe Gen 1 vs Gen 2 link speed file benchmark performance" width="700" height="394" class="insert-image" >}}

But as long as the performance is able to stay above 110 MB/sec, that's still plenty to saturate the Pi's 1 Gbps Ethernet connection.

So I tried a few file copies to the Pi running at Gen 1 speeds, and this time, it was very stable, allowing me to copy 70 GB at a time without breaking a sweat. Write speeds varied between 50 and 100 MB/sec, averaging around 70, and Read speeds averaged 100 MB/sec.

## Overclocking

Because a lot of the slowdown for a network copy comes from the Pi's SoC itself, I also tested an [overclock](/blog/2020/overclocking-raspberry-pi-compute-module-4) from the base clock of 1.5 GHz to 2.2 GHz, and that resulted in a noticeable speedup, especially in terms of the consistency of read and write speeds over long periods:

{{< figure src="./network-copy-performance-overclock.png" alt="Network Copy Performance - SMB with Pi Overclock" width="700" height="394" class="insert-image" >}}

## Other questions

Viewers asked a number of other questions I thought I'd answer here:

  - **How much power does it use?**  
    502W with all drives spinning at idle, 516W during a RAID 0 benchmark, and 640W peak (as measured) during the final batch of drive spinups at boot. If I only run 15 drives, it runs around 200W. So with 60 drives and a Raspberry Pi as the CPU, this XL60 chassis will eat up around 360 kWh per month.
  - **How much does it weigh?**  
    All-in, around 300 lbs. (136 kg). When I need to move it, I have to pull all the hard drives, both so it's light enough for two people to safely carry, and to protect the hard drives themselves.
  - **How much does it cost?**  
    You can check 45Drives' [online configurator](https://www.45drives.com/products/storinator-xl60-configurations.php), but the configuration I have runs about $50,000 (drives included). Of course, I put all the included server hardware aside, so maybe more like $40,000 plus the cost of the Pi, the PCIe switch, and 4x Broadcom 9405W-16i HBAs.
  - **How loud is it?**  
    At a distance of 2' from the rear, I measured 75dB. The large fans make a pleasant enough sound, but the tiny 40mm PSU fans make quite a whine at full blast.

## Future Plans

{{< figure src="./storinator-in-homelab-rack.jpeg" alt="Storinator in homelab rack" width="375" height="500" class="insert-image" >}}

I do plan on deploying the Storinator XL60 in my basement homelab, but I will likely not run all 60 hard drives inside for the short term... because try as I might, I have nowhere _near_ 1 PiB of files to store. _Yet._

Plus, I'd have to figure out a way to back up a whole petabyte! Right now I only have the capacity / need for two local copies (plus one offsite) for a few dozen TB.

If you have any other questions about the Storinator or the PetaPi, leave 'em below!
