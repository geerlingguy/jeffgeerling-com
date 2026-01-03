---
nid: 3283
title: "First look: ASUSTOR's new 12-bay all-M.2 NVMe SSD NAS"
slug: "first-look-asustors-new-12-bay-all-m2-nvme-ssd-nas"
date: 2023-05-01T00:10:52+00:00
drupal:
  nid: 3283
  path: /blog/2023/first-look-asustors-new-12-bay-all-m2-nvme-ssd-nas
  body_format: markdown
  redirects: []
tags:
  - asustor
  - flash
  - homelab
  - nas
  - network
  - nvme
  - server
  - ssd
  - storage
---

Last year, after I started a search for a good out-of-the-box all-flash-storage setup for a video editing NAS, I floated the idea of an all-M.2 NVMe NAS to ASUSTOR. I am not the first person with the idea, nor is ASUSTOR the first prebuilt NAS company to build one (that honor goes QNAP, with their [TBS-453DX](https://www.qnap.com/en/product/tbs-453dx)).

But I do think the concept can be executed to suit different needs—like in my case, video editing over a 10 Gbps network with minimal latency for at least one concurrent user with multiple 4K streams and sometimes complex edits, without lower-bitrate transcoded media (e.g. ProRes RAW).

{{< figure src="./flashstor01-front.jpeg" alt="ASUSTOR Flashstor 12 Pro - front and top" width="700" height="394" class="insert-image" >}}

And so, we now have two new entrants from ASUSTOR, the 6-M.2-slot [Flashstor 6 (FS6706T)](https://amzn.to/40RXAFW) with dual 2.5 Gbps networking for $449, and the 12-M.2-slot [Flashstor 12 Pro (FS6712X)](https://amzn.to/3HsOmJE) with 10 Gbps networking for $799.

Both have identical exteriors save for the RJ45 Ethernet ports: the 6-bay unit has two 2.5G ports (pictured first), while the 12-bay unit has a single 10G port (pictured second):

{{< figure src="./flashstor03-back-6-bay.jpeg" alt="Flashstor 6 - back rear" width="700" height="467" class="insert-image" >}}

{{< figure src="./flashstor02-back-12-bay.jpeg" alt="Flashstor 12 Pro - back rear" width="700" height="394" class="insert-image" >}}

The units both run on an Intel [Celeron N5105](https://ark.intel.com/content/www/us/en/ark/products/212328/intel-celeron-processor-n5105-4m-cache-up-to-2-90-ghz.html) processor, and have HDMI, optical TOSlink S/PDIF, and USB ports, along with a Kensington lock slot.

ASUSTOR sent me both units for testing (though I will soon pass them along to [Raid Owl](https://www.youtube.com/c/RaidOwl/videos) so he can continue the testing!), and I've only had a chance for a quick teardown so far—I wasn't yet able to initialize the unit (more on that later).

If you flip one over, you can see the lone fan that's directly under the M.2 NVMe slots (and pushes air through slots in the PCB across a massive heatsink covering the CPU):

{{< figure src="./flashstor04-bottom-fan.jpeg" alt="Flashstor 12 Pro bottom with fan and labels" width="700" height="394" class="insert-image" >}}

Gaining access to the M.2 slots requires the removal of four small screws. You slide the fan cover out, and that also disconnects a little USB-A port that powers the fan itself:

{{< figure src="./flashstor05-fan-unit.jpeg" alt="Flashstor 12 Pro fan unit popped off" width="700" height="394" class="insert-image" >}}

And underneath, you can find M.2 slots labeled 1-6, and peeking closely above those slots, there are a number of ASMedia ASM1480 PCIe multiplexers:

{{< figure src="./flashstor06-topside-nvme-slots.jpeg" alt="Flashstor 12 NVMe slot" width="700" height="394" class="insert-image" >}}

Those multiplexers seem to be the primary means of splitting up PCIe traffic on the 6-bay unit—the N5105 only has 8 PCIe Gen 3 lanes—and supporting two NICs (in the 6-bay unit) or one 10G NIC (in the 12-bay unit) plus all those M.2 slots... you have to mux the traffic.

If you flip over the 6-bay unit and pop off the top cover, you reveal a bunch of unpopulated pads for the additional M.2 slots, along with some pads for extra ICs:

{{< figure src="./flashstor-6-unpopulated-slots.jpeg" alt="Flashstor 6 unpopulated slots on topside" width="700" height="467" class="insert-image" >}}

On the 12-bay unit, those ICs are populated, and they are 3 of ASMedia's ASM2806 PCI express switch chips:

{{< figure src="./flashstor07-bottomside-nvme-slots.jpeg" alt="Flashstor 12 Pro topside populated NVMe slots" width="700" height="394" class="insert-image" >}}

{{< figure src="./flashstor-12-pro-pcie-switch-chips.jpeg" alt="Flashstor 12 Pro populated M.2 slots and PCIe switch chips" width="700" height="467" class="insert-image" >}}

The 12-bay unit has an extra heatsink over the 10 Gbps NIC chip, while the 6-bay unit uses two 2.5 Gbps Realtek RTL8125GB NICs.

{{< figure src="./flashstor08-ram-slots.jpeg" alt="Flashstor 12 Pro - RAM slot for DDR4 SODIMM 3200" width="700" height="394" class="insert-image" >}}

Also on the topside are two DDR4 SODIMM slots. The units both come with 4GB of Apacer DDR4 3200 CL22 RAM in one of the slots. The N5105 supports up to 16GB of RAM total, and though Patrick from Serve The Home was able to get 64 GB of RAM _recognized_, he encountered errors as more than 40GB of data was cached in RAM. I would stick to the 16GB rated maximum if you want the best stability.

{{< figure src="./flashstor09-nvme-retention-clips.jpeg" alt="Flashstor 12 Pro M.2 retention clips" width="700" height="394" class="insert-image" >}}

The M.2 slots each have a little plastic retention tab, making installation and removal of drives extremely simple (easier even than the little plastic twisty mechanism employed by nicer motherboards these days). After the drive clicks in, I don't have any worry it would move even with a modest drop of the NAS.

{{< figure src="./flashstor10-power-led.jpeg" alt="Flashstor 12 Pro power LED red motif" width="700" height="394" class="insert-image" >}}

After powering it up, I noticed a strong red motif emblazoned around the power button on the side, along with the four status LEDs on the top lighting up.

{{< figure src="./flashstor11-network-id.jpeg" alt="iNet Network Scanner - Asustor device" width="700" height="467" class="insert-image" >}}

With the unit powered up, I fired up iNet Network Scanner and found the device on the network, with the device name "FS6712X 24E6". I could connect via SSH or HTTP on port 8000, so I did both! While I was putzing around trying to initialize the NAS with two Kioxia XG6 SSDs, I also logged in with username and password `admin`, and started exploring:

{{< figure src="./flashstor13-10g-link.jpeg" alt="Flashstor 12 Pro 10 Gigabit link" width="700" height="467" class="insert-image" >}}

`ethtool eth0` reported a full duplex 10 Gbps link, and so I tried `lspci -vvvv`, but whatever flavor of mini Linux this box uses (it runs a Linux fork from ASUSTOR called ADM, or ASUSTOR Data Manager), it only reports IDs, and I couldn't pull more info than that:

{{< figure src="./flashstor14-lspci-ids.jpeg" alt="Flashstor 12 Pro lspci SSH terminal output" width="700" height="467" class="insert-image" >}}

I also tried plugging in the HDMI output, but at least for now, all I see is a blinking cursor:

{{< figure src="./flashstor15-hdmi-output-blinking-cursor.jpeg" alt="ASUSTOR Flashstor 6 HDMI output blinking cursor" width="700" height="467" class="insert-image" >}}

Maybe there will be some sort of UI after initialization. Speaking of initialization, I eventually got the following error message during that process:

{{< figure src="./flashstor16-error-initializing.jpeg" alt="ASUSTOR ADM Flashstor Initialization error screen" width="700" height="467" class="insert-image" >}}

As I'm wheels up for the UK right now (I'm literally typing this on the plane before takeoff), I didn't have time to explore further—that'll come soon (along with more detail of the 6 vs 12 Pro units!). But I did take a quick power usage reading with no NVMe drives installed and 4GB of RAM:

{{< figure src="./flashstor17-17w-power-usage.jpeg" alt="17W power usage Flashstor 12 Pro" width="700" height="467" class="insert-image" >}}

That was while connected to my 10 Gbps network, so power usage on the Flashstor 6 may be a little reduced. I will be putting these through there paces soon—and I see [Serve The Home has already gotten some preliminary test results](https://www.servethehome.com/a-quick-look-at-the-asustor-flashstor-6-fs6706t-nas/). What else would you like to see?
