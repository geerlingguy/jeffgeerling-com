---
nid: 3406
title: "Qualcomm Snapdragon Dev Kit for Windows Teardown (2024)"
slug: "qualcomm-snapdragon-dev-kit-windows-teardown-2024"
date: 2024-09-26T03:27:19+00:00
drupal:
  nid: 3406
  path: /blog/2024/qualcomm-snapdragon-dev-kit-windows-teardown-2024
  body_format: markdown
  redirects:
    - /blog/2024/teardown-qualcomms-snapdragon-x-elite-dev-kit-windows
    - /blog/2024/teardown-qualcomms-snapdragon-dev-kit-windows-2024
aliases:
  - /blog/2024/teardown-qualcomms-snapdragon-x-elite-dev-kit-windows
  - /blog/2024/teardown-qualcomms-snapdragon-dev-kit-windows-2024
tags:
  - copilot
  - pc
  - qualcomm
  - snapdragon
  - teardown
  - windows
---

> **Update - October 17**: Today [Qualcomm cancelled all remaining orders, and will no longer support the Dev Kit](/blog/2024/qualcomm-cancels-snapdragon-dev-kit-refunds-all-orders).

In late July, a week after ordering the [Snapdragon Dev Kit](https://www.arrow.com/en/products/c8380-12c-mp-32g/thundercomm), I wondered [where it was](https://www.jeffgeerling.com/blog/2024/where-qualcomms-snapdragon-x-elite-dev-kit). Arrow's website [said 'Ships tomorrow' when I ordered](https://twitter.com/geerlingguy/status/1819386097153065238), after all.

Many developers eager to test their code on Windows on Arm, on the premiere new 'CoPilot+' PCs that would revolutionize computing as we know it, were also wondering.

{{< figure src="./snapdragon-21-disassembled.jpeg" alt="Snapdragon Dev Kit - teardown complete" width="700" height="auto" class="insert-image" >}}

Well, wonder no more — 2.5 months later, with my wallet $900 lighter, the Dev Kit finally arrived. Ignoring the little 🚫 stickers covering two of the phillips-head case screws, I tore mine down to see what kind of hardware necessitated such a delay in shipping the developer kit meant to get developers excited to build software for the revolutionary AI PCs that would be shipping to customers in ... wait—they already shipped [in _June_](https://blogs.windows.com/devices/2024/06/18/top-things-to-know-about-copilot-pcs-from-microsoft-surface-available-today-at-microsoft-com/)?

What's the point of a $900 platform dev kit that can't be resold (we'll get to that) that ships months after consumers already have the final hardware? _That's a rhetorical question._

## The Snapdragon X Dev Kit

The box is nice enough.

{{< figure src="./snapdragon-01-box.jpeg" alt="Snapdragon Dev Kit - box" width="700" height="auto" class="insert-image" >}}

The first thing to greet us are two information cards inside a thin envelope; one gives links to the developer discord and some other resources, and the other shows warranty information.

{{< figure src="./snapdragon-02-warranty.jpeg" alt="Snapdragon Dev Kit - Warranty card" width="700" height="auto" class="insert-image" >}}

Apparently if you replace any component, the warranty is void.

Moving on, the box contains the Computer inside a plastic bag (removed in this picture), and the power supply and a USB-C to HDMI dongle inside a black box (also removed in this picture).

{{< figure src="./snapdragon-03-contents.jpeg" alt="Snapdragon Dev Kit - box contents" width="700" height="auto" class="insert-image" >}}

Across the front of the computer, there's a snazzy gold Snapdragon X Elite sticker, a USB-C USB 4 port (labelled '2'), a power button, a little trapdoor for the microSD card slot (it hides another little feature we'll find later), and a power LED.

{{< figure src="./snapdragon-04-front.jpeg" alt="Snapdragon Dev Kit - front" width="700" height="auto" class="insert-image" >}}

Here's a closeup of the trapdoor open (below). There are a couple things hiding behind there we'll get to in the teardown.

{{< figure src="./snapdragon-05-microsd.jpeg" alt="Snapdragon Dev Kit - microSD door" width="700" height="auto" class="insert-image" >}}

Moving on to the left side, there's a large vent that almost takes up the entire side of the thing—it's an exhaust vent, but we don't know that yet, we'll have to see how that works in the teardown.

{{< figure src="./snapdragon-06-side-vent.jpeg" alt="Snapdragon Dev Kit - side vent" width="700" height="auto" class="insert-image" >}}

The back has a 19V power jack, 2.5 Gbps Ethernet, 2x USB-A ports, 2x USB-C ports (labeled '0' and '1', and a headphone jack.

{{< figure src="./snapdragon-07-rear-ports.jpeg" alt="Snapdragon Dev Kit - rear ports" width="700" height="auto" class="insert-image" >}}

As the other side is blank, I decided to stack a few other mini Windows PCs on top to get a feel for the size of this thing.

It's certainly much larger than the smaller-than-NUC-sized mini PCs from the likes of GMKtec:

{{< figure src="./snapdragon-08-compare-gmktek.jpeg" alt="Snapdragon Dev Kit - size compare GMKtek mini PC" width="700" height="auto" class="insert-image" >}}

And it's about the same size as a typical square-box-style 1 liter mini PC, like the one I have from Lenovo (these thin clients are found all over the place, including for cheap on eBay).

{{< figure src="./snapdragon-09-compare-1lpc.jpeg" alt="Snapdragon Dev Kit - size compare Lenovo 1L PC" width="700" height="auto" class="insert-image" >}}

Comparing it to the Windows Dev Kit 2023, it's nearly the same width (though a hair wider), and a bit deeper.

{{< figure src="./snapdragon-10-compare-windevkit.jpeg" alt="Snapdragon Dev Kit - size compare Win Dev Kit 2023" width="700" height="auto" class="insert-image" >}}

Finally, flipping it over on its top, we encounter a notice that this unit is NOT for resale.

{{< figure src="./snapdragon-11-fcc-resale.jpeg" alt="Snapdragon Dev Kit - not for resale fcc warning" width="700" height="auto" class="insert-image" >}}

Instead, it's for "Evaluation only ; not FCC approved for resale."

Supposedly, that means they have produced a limited quantity of these developer kits, and are not intending this design for the consumer market (at least not at this time).

There _were_ little 🚫 stickers covering two of the four phillips head screws on the bottom, but they were easy to deal with—just give the screwdriver a little extra pressure as you unscrew those two screws.

{{< figure src="./snapdragon-devkit-no-unscrew.jpeg" alt="Snapdragon Dev Kit - no unscrew stickers" width="700" height="auto" class="insert-image" >}}

## Teardown

Taking off the back cover, there's a pretty good amount of empty space surrounding the large cooling fan. But you quickly see the general layout: PCIe devices surround the SoC (presumably under the fan and copper heatsink), and then IO borders everything on the edges of the board.

{{< figure src="./snapdragon-12-open.jpeg" alt="Snapdragon Dev Kit - open" width="700" height="auto" class="insert-image" >}}

The lid has metal shielding, and everything is grounded with EMI/RFI tape to other parts of the case (including the heatsink, the rear case, and ports), so I presume at least _some_ work was put into FCC compliance. They probably didn't want to go through the process of a full compliance test (which IMO is a shame).

The NVMe is mounted with a full-length heatsink (with thermal pads on top and bottom). Whoever designed the thermals for this box at least oriented the heatsink fins the right way (on both the NVMe, and as we'll see soon, also the WiFi card). The air is meant to flow through vents on the bottom case towards the giant fan and cooler.

{{< figure src="./snapdragon-13-nvme-heatsink.jpeg" alt="Snapdragon Dev Kit - NVMe Heatsink" width="700" height="auto" class="insert-image" >}}

The NVMe is a 2280 size SSD, a 512 GB [Foresee XP2200F512G](https://www.longsys.com/products/solid-state-drive/commercial-pcle-ssd/xp2200-pcie-ssd.html), made by Longsys.

{{< figure src="./snapdragon-15-foresee-nvme-ssd.jpeg" alt="Snapdragon Dev Kit - Foresee NVMe SSD" width="700" height="auto" class="insert-image" >}}

The external Ethernet port is actually on a separate daughtercard marked "Running HDMI Board" with an unpopulated HDMI port, and a display cable connector that is not connected to anything (far right in picture below).

The Ethernet jack is connected back to a mini PCIe card with magnetics and an RTL8125BG—a 2.5 Gbps Realtek NIC.

{{< figure src="./snapdragon-14-pcie-slot-ethernet-wifi.jpeg" alt="Snapdragon Dev Kit - PCIe slot Ethernet and WiFi expansion cards" width="700" height="auto" class="insert-image" >}}

Pictured above is also the location of the WiFi card slot (M.2 E-key), and you can even spot an unpopulated full-length PCIe slot there too. Not sure if it's wired up to the SoC at all, but I intend to find out—eventually ;)

WiFi is provided via module labeled `T99H432.10`, a [Qualcomm 'FastConnect 7800'](https://www.qualcomm.com/products/technology/wi-fi/fastconnect/fastconnect-7800) card that supports WiFi 7 and Bluetooth 5.4. I found one laptop, the [MSI Alpha 17 C7V](https://www.msi.com/Laptop/Alpha-17-C7VX/Specification), with the same model number (but .03 instead of .10). Like the NVMe SSD, it is installed with thermal pads and heatsinking on the top and bottom (the bottom heatsink is a metal tray that wraps around the M.2 device and holds on the top heatsink with four clips.

{{< figure src="./snapdragon-16-wifi-e-key.jpeg" alt="Snapdragon Dev Kit - WiFi E key card" width="700" height="auto" class="insert-image" >}}

After removing the daughtercard the Ethernet port is mounted to, I also revealed pads for the ghost of an HDMI port:

{{< figure src="./snapdragon-devkit-running-hdmi-board.jpeg" alt="Snapdragon Dev Kit - ghost HDMI port" width="700" height="auto" class="insert-image" >}}

Now I'd _love_ to know the full story behind this mysterious HDMI port. The daughtercard has a Display Connector Cable (eDP) on the flip-side, and a [Parade PS195](https://www.paradetech.com/parade-launches-displayport-2-0-to-hdmi-2-1-protocol-converter-solutions/) DisplayPort 2.0 to HDMI 2.1 protocol converter chip. It obviously costs money to include these things, and it's a huge waste if there's no HDMI actually _using them_. I guess they saved on the eDP cable from the motherboard to the daughtercard, but still...

> Update: Richard Campbell [speculates](https://www.youtube.com/watch?v=NlEV38cO8Gs) this could be a significant reason behind the shipping delay for the Dev Kit.

The original announcement included a convenient HDMI port. We should all use DisplayPort, sure, but HDMI is ubiquitous, so it's removal isn't an accident. Maybe that was the reason this thing took an extra 3+ months to bake post-consumer-launch?

Speaking of daughtercards...

There's a tiny daughtercard on the opposite (front) side called "Running ECB" - does it have something to do with cryptography? Platform security? Not sure. The plug it is plugged into is labeled `EC_I/F`, and it has a [GigaDevice GD32F330G8 Arm MCU](https://www.gd32mcu.com/data/documents/datasheet/GD32F330xx_Datasheet_Rev_3.0.pdf), plus a larger ITE chip I couldn't make out. Let me know if you know what this thing is for in the comments:

{{< figure src="./snapdragon-18-mystery-boar.jpeg" alt="Snapdragon Dev Kit - mystery board Running ECB" width="700" height="auto" class="insert-image" >}}

But removing that daughtercard exposes the microSD card slot... and a NanoSIM slot! Interesting. Maybe meant for a model with 5G integration as well?

{{< figure src="./snapdragon-17-sim-microsd-slot.jpeg" alt="Snapdragon Dev Kit - SIM card tray hidden near microSD" width="700" height="auto" class="insert-image" >}}

The fan is APEXE model B82DBHA2467, with a 4-pin standard fan header on the motherboard (easy to remove, separate from the copper heatsink). It is connected to the heatsink with screws, and there is a taped on duct to port the exhaust out the side of the Dev Kit.

{{< figure src="./snapdragon-19-fan.jpeg" alt="Snapdragon Dev Kit - cooling fan" width="700" height="auto" class="insert-image" >}}

The cooler is a massive copper heatsink with heat pipes and a massive cooling stack for the SoC itself (at least in comparison to the SBCs I normally deal with, lol).

{{< figure src="./snapdragon-20-copper-heatsink.jpeg" alt="Snapdragon Dev Kit - copper heatsink and heatpipes" width="700" height="auto" class="insert-image" >}}

There are thermal pads on all the little power ICs (look at the large field of PMICs surrounding the SoC and RAM!), and a large—nay, _excessive_—amount of thermal compound on all four RAM chips and the SoC itself.

There are a couple CSI ports, many unpopulated headers, an unpopulated eMMC spot near the RAM, and there's a micro USB debug port labeled `DBG_UART` as well.

{{< figure src="./snapdragon-21-disassembled.jpeg" alt="Snapdragon Dev Kit - teardown complete" width="700" height="auto" class="insert-image" >}}

But with the thermal compound removed, we can finally see the shiny surface of the Snapdragon X Elite SoC, and the four LPDDR5x RAM modules lined up alongside:

{{< figure src="./snapdragon-22-soc-ram.jpeg" alt="Snapdragon Dev Kit - Snapdragon X Elite SoC and RAM with eMMC pads" width="700" height="auto" class="insert-image" >}}

The thermal compound was not as easy to remove as I'd hoped, I stopped trying to clean it off all the little caps surrounding the chips for fear I'd dislodge one with my cotton swabs!

One final bit, the chips powering the two rear USB-C ports are [Parade PS8830A4 USB4 Retimers](https://www.paradetech.com/products/ps8830/), supporting DisplayPort 2.0 and Thunderbolt 3.0 (apparently):

{{< figure src="./snapdragon-23-usb-c.jpeg" alt="Snapdragon Dev Kit - USB-C port chips" width="700" height="auto" class="insert-image" >}}

I don't think Thunderbolt is supported on Snapdragon, but it is supposed to at least support USB 4.

Soon: I'll actually plug this thing, turn it on, and see why they chose to ship a developer unit with Windows 11 _Home_, and without any downloadable restore media (so far... asking about that now).

I will be posting some of my notes and test data in real time in [this GitHub issue](https://github.com/geerlingguy/sbc-reviews/issues/51).
