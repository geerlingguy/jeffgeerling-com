---
nid: 3360
title: "Build log: Macintosh PowerBook 3400c"
slug: "build-log-macintosh-powerbook-3400c"
date: 2024-03-22T14:00:06+00:00
drupal:
  nid: 3360
  path: /blog/2024/build-log-macintosh-powerbook-3400c
  body_format: markdown
  redirects: []
tags:
  - 3400c
  - apple
  - marchintosh
  - powerbook
  - retro
  - video
  - youtube
---

{{< figure src="./powerbook-3400c-after-dark-flying-toasters.jpg" alt="PowerBook 3400c - Flying Toasters" width="700" height="auto" class="insert-image" >}}

This blog post will serve as my long-term build log for the Macintosh PowerBook 3400c I started restoring in the video [Retro Computing Enthusiasts are Masochists](https://www.youtube.com/watch?v=M4604SvoyBc) in early 2024. See also: [Build log: Power Mac G4 MDD](/blog/2024/build-log-power-mac-g4-mdd).

## The fastest laptop _period_

It's 1997. Apple _just_ re-acquired Steve Jobs, but he hasn't been around long enough to materially impact the next few months of product launches.

Gil Amelio, seeing a gap in Apple's laptop offerings, decides to throw the kitchen sink at the market, in the form of the PowerBook 3400c. _It works._

This laptop was the platform for the first G3 laptop, the short-lived 'Kanga', which used almost an identical design as a stopgap for Apple to later introduce the iconic [Wallstreet](https://en.wikipedia.org/wiki/PowerBook_G3#/media/File:WallstreetII.jpg) G3.

For a great overview of the 3400c, check out This Does Not Compute's video [When the World's Fastest Laptop Was a Mac!](https://www.youtube.com/watch?v=0tNgZVZ3XrY).

## _My_ 3400c

{{< figure src="./powerbook-3400c-jeff-geerling-inventorying.jpeg" alt="PowerBook 3400c booting into Mac OS 7.6" width="700" height="auto" class="insert-image" >}}

After college, I worked as a web developer for a few years, and one of the largest projects I built was a massive rewrite of a print publication's website. The new website automatically pulled stories in through their news system as they published stories to the layout specialists.

Around that time, they were upgrading the older laptop stock their designers used, and they had a fairly nice PowerBook 3400c sitting on a shelf for a couple years. I eventually asked what the plan was for it (it was sitting near my desk that whole time!), and the director said it's mine if I wanted—of course I did!

I booted it up once in 2008, but it promptly went in a box with my old SCSI devices, not to be touched again until early 2024.

I booted it up—and it did boot, right into the System 7.6 install I had restored in 2008—then asked a couple other folks tips for keeping it running long-term.

The first thing both Sean (Action Retro) and Steve (Mac84) told me? _Don't boot it up yet._

Oh.

Well, I got lucky, but there were still a few issues.

## First impressions / inventorying the issues

{{< figure src="./powerbook-3400c-disassembled.jpeg" alt="PowerBook 3400c disassembled on desk" width="700" height="auto" class="insert-image" >}}

Both Sean and Steve (and later, Colin from This Does Not Compute) said I should immediately rip out the original PRAM battery, which is hovering just above the display connector and some of the critical parts of the motherboard.

I did this, and revealed a fairly crusty battery pack—along with a connector with the signature green 'schmoo' that plagues these old Macs after they sit for decades.

{{< figure src="./powerbook-3400c-cmos-battery-green-corrosion-schmoo.jpg" alt="PowerBook 3400c PRAM battery green connector corrosion schmoo" width="700" height="auto" class="insert-image" >}}

Removing the Lithium Ion battery pack revealed a little more 'schmoo', but only on the copper lining of the battery bay, not on the battery itself (maybe the battery was a replacement?).

After I pulled both batteries, and rebooted the system, I found it would lock up sometimes. The floppy drive ejected a floppy about 10% of the time (other times I had to coax it with a paperclip). The 12x CD-ROM read discs fine... until it didn't. Sometimes it would sit and do a cycle for a while until it caught back up and could read the rest of a file.

Since the mechanical hard drive isn't long for this world, I also swapped in an SD-card replacement, but that's when I found some other problems...

## IDE HDD to Flash-based storage conversion

Almost any flash storage is faster than the ancient IDE hard drive in this system. And luckily, there are a number of IDE replacements for $15-30 on Amazon.

I first tried swapping in a $16 [GODSHARK SD to IDE Laptop Adapter](https://amzn.to/3wL2JX2), and tested an $11 [SanDisk Extreme PRO 32GB SDHC Card](https://amzn.to/3P4ZIHn) in it. I wrapped the whole thing in a layer of kapton polyimide tape to prevent it from shorting, since there wasn't any way of securing it in the bay. (Later I [3D printed this adapter](https://www.printables.com/model/600620-sd-to-25-ide-caddy/comments#makes) to hold it in more securely.)

I booted the PowerBook off the 3400c Restore CD, but I couldn't initialize the SD card with the Drive Setup utility included with that CD. It just sat for hours (I let it go for 24 hours to no avail).

I rebooted from the 'Disk Tools' floppy that also came with the 3400c (and booted into a black-and-white version of Mac OS), and that actually worked! I had an HFS-formatted SD card in the drive bay now.

I used the 3400c Restore CD to restore Mac OS 7.6 on the SD card, and that seemed to boot okay. After discovering Mac OS 9.2.2 wouldn't install on this system (9.1.x was the latest officially-supported Mac OS), I tried burning a Mac OS 8.6 Install CD to one of the old 700 MB CD-Rs I had laying around.

Unfortunately, that didn't work—nor did inserting that burned CD into my Apple SCSI 2x CD-ROM externally. It seems like the PowerBook 3400c only likes older 650 MB CD-R media. (The 700 MB disc showed up just fine when inserting it in my newer Power Mac G4 MDD's SuperDrive).

{{< figure src="./powerbook-3400c-cf-card-to-ide-adapter.jpg" alt="PowerBook 3400c IDE to CF card Syba adapter" width="700" height="auto" class="insert-image" >}}

I eventually got 8.6 to install from a CF card; I used [this PCMCIA to CF memory card adapter](https://amzn.to/4aq4tDE) with a [SanDisk Ultra 4GB CompactFlash card](https://amzn.to/4cqykO6). To write 8.6 onto the CF card, I used `dd` on my Mac Studio, and an ancient Kingston USB CF card reader.

> For any software I hadn't imaged myself years ago (I save _everything_), like the 8.6 Install CD, I used the invaluable [Macintosh Garden](http://macintoshgarden.org), a huge repository of obsolete Mac software that has just about everything I've ever run on a Mac.

But 8.6 was not quite stable. Unlike 7.6, I would hit random lockups (and at different points) like 'Folder Actions' or 'bus error'. It seemed like that could be down to bad RAM, or bad IDE drive access.

To rule out the drive, I tried a number of other options:

  - $17 [Syba Dual CF to IDE Adapter](https://amzn.to/3TlVb51): This required snipping off one of the pins with my micro flush cutters. I triple-checked it was the correct pin before pulling the trigger, though! It was also a little tough installing it, but it worked out the best of all the drives I tested.
  - $14 [Chenyang mSATA Mini PCI-E SATA SSD to IDE 44-pin Adapter](https://amzn.to/3IriZis) + $20 [ROGOB 128GB mSATA SSD](https://amzn.to/3V7ZymJ): This combo seemed to be stable during a format and 7.6 install... but no matter what I tried, I couldn't get it to be recognized as a boot volume—the PowerBook would always show the flashing disk icon when I powered it on with this drive.
  - Combinations of the above adapters with various SD and CF cards... nothing was stable—though the Syba adapter was the most stable of all.

This led me to wonder if the hard drive cable itself—or some other component—was at fault. I would investigate that later, but tearing down the PowerBook, I also discovered the little riser board with the PC Card slot eject buttons had detached from the motherboard.

## PC Card Eject Button Riser Repair

{{< figure src="./powerbook-3400c-pcmcia-eject-riser-board.jpg" alt="PowerBook 3400c PC Card PCMCIA riser eject buttons" width="700" height="auto" class="insert-image" >}}

I pulled out the left bezel, pulled out the little riser board, and reflowed the solder on the little through-holes holding the pin connectors on it. It's not held in very well—just those four tiny solder joints on the bottom into a four pin header. The top is held in place by plastic holding it from the bezel and the speaker assembly.

People tend to push the eject buttons hard, which in turn puts more stress on the tiny solder joints! Not a great design for a part meant to be mashed on by a human...

## Debugging the Crashes

The easiest way to debug the crashes—since the motherboard, RAM, and hard drive cable are all proprietary and didn't have any obvious flaws—was the 'magic of buying another'.

{{< figure src="./powerbook-3400c-magic-buying-another.jpg" alt="PowerBook 3400c - through the magic of buying another" width="700" height="auto" class="insert-image" >}}

I bought [this 3400c off eBay for $80](https://www.ebay.com/itm/166601269516), and it had no specs listed, just a photo showing a melted bezel, and an otherwise okay-looking 'for parts' 3400c.

When it arrived, I tore it down. It was apparently the _top spec_ 3400c, with a 240 MHz PowerPC 603ev CPU, 144 MB of RAM (using a 128 MB RAM module), and a floppy drive included.

The machine even booted up, and the screen worked, once I installed a hard drive! Not sure what melted the bezel, but hardware-wise, this machine was a _very_ lucky find.

I promptly swapped out almost everything between the two machines to build one fully-functional PowerBook 3400c, and all the random crashes stopped happening. So it was either the motherboard or the RAM, but in any case, it was finally time to get back to upgrades!

## Copying Files and USB 2.0 support

I was mostly using CF cards to transport files to and from my Mac Studio running modern macOS—but for an HFS-formatted drive, I had to [use `hfsutils`](https://www.jeffgeerling.com/blog/2024/getting-files-and-powerbook-3400c-hfsutils) to mount the CF card and copy files to and from it.

Luckily, once I had 8.6 running stable, I could reformat the CF card as HFS Extended (HFS+), which is still readable on modern macOS versions (for how long? who knows...). Much faster.

I wanted to see if I could get a USB 2.0 PC Card running on the 3400c. I know the G3 was compatible out of the box with Mac OS 9, but Mac OS 8.6 required special [USB Card Support](http://macintoshgarden.org/apps/macos-usb-and-firewire-support).

Unfortunately, even though the [Adaptec AUA-1420 USB 2.0 CardBus Adapter](https://www.ebay.com/itm/302251675512) showed up in System Profiler, the USB Card Support installer would not run:

{{< figure src="./usb-adapter-card-not-supported.jpg" alt="PowerBook 3400c Adaptec USB 2.0 Adapter not supported" width="700" height="auto" class="insert-image" >}}

I found an article [The Powerbook 3400c is Cardbus Compliant!](http://macintoshgarden.org/apps/macos-usb-and-firewire-support), with a mention that it worked on _that_ 3400c. So maybe it is possible? Rob said he could only get it to work if plugging the card in _after_ boot. Maybe I should test out USB Storage 1.3.5 instead of 1.4.1?

## AppleShare and Netatalk

I decided to install [netatalk](https://netatalk.io) on a Raspberry Pi 5, so I could share some files over Samba (for newer Macs) and AppleTalk (over TCP), making file sharing way simpler (no need for physical media).

I created this [open source Apple Pi Ansible playbook](https://github.com/geerlingguy/apple-pi), which sets up Netatalk v3 and Samba shares on a Raspberry Pi 5. I messed around with different Netatalk UAMs, trying to find a combination that was compatible with Mac OS 8.6, but Chooser wasn't happy with anything besides Guest access.

So I started a thread on 68kMLA: [PowerBook 3400c on 8.6 + netatalk - Chooser "error of type 12"](https://68kmla.org/bb/index.php?threads/powerbook-3400c-on-8-6-netatalk-chooser-error-of-type-12.46989/#post-526430). In the course of debugging, I was introduced to MacsBug—a little debugger you throw into the System Folder that allows a full debugger to run in the background—it'll pop up whenever an exception is thrown:

{{< figure src="./macsbug-debugging-chooser-exception.jpeg" alt="MacsBug Mac OS 68000 Debugger running on PowerBook 3400c" width="700" height="auto" class="insert-image" >}}

A few quick notes on MacsBug:

  - MacsBug _doesn't_ stand for 'Macs Debugger', but instead "Motorola Advanced Computer Systems deBugger"
  - To enter (if a crash hasn't dumped you in the debugger), press Command + Power
  - To exit, press Command + G (for 'Go')
  - Check out the [full MacsBug reference](https://wiki.preterhuman.net/images/5/59/Macsbug_Ref_%26_Debugging_Guide.pdf)

We'll see where this goes—I'd still like to get this working, but for now, the CF-card-based transfers aren't _too_ much of a pain.

## Future tasks (TODOs)

The system is stable, and almost every bit of hardware is functional, with a full working spare in the donor laptop I bought off eBay. But there are a few things I want to do to make it easier to maintain—and to make it last another 20 years!

### PiSCSI / BlueSCSI

Thanks to [FreeGeek Twin Cities](https://www.freegeektwincities.org), I have an [HDI-30 Male to Centronic 50-pin SCSI adapter](https://amzn.to/3UVFMdY). This is required to adapt most SCSI devices to the weird 30-pin port on the back of the PowerBook. All the PowerBook line's SCSI ports used HDI-30, and there are few adapters available for that port these days. Luckily I have a few long cables, but the ends are massive due to the complexity of so many individual pins/wires in the bundle!

I also purchased a $70 [external PiSCSI without Pi Zero](https://samplerzone.com/products/chicken-rascsi-sd-scsi-drive?variant=39761556308043), and a $15 [Raspberry Pi Zero 2 W](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/) from Micro Center. I intend to get this set up so I can wirelessly transfer files and CD images to and from the PowerBook 3400c via the Pi's WiFi.

There's also the [BlueSCSI v2](https://bluescsi.com), which is powered by a $4 Raspberry Pi Pico. I haven't yet purchased or assembled one of them, but I'm excited to see how I can hack the SCSI bus to do some fun things—especially transport files without any AppleTalk networking complication.

### Recap Electrolytic Capacitors

Vintage electronics—especially those built around the turn of the millenia—are known for failure due to [leaky or shorted electrolytic capacitors](https://resources.pcb.cadence.com/blog/2022-the-causes-of-electrolytic-capacitor-degradation).

Most people 'replace the caps' on a board after 10-20 years for the best reliability. Yellow and black rectangular capacitors are generally less leaky—but can in some conditions explode and wreak their own form of havoc.

But I would like to at least recap the 3400c at some point. Like most older Macs, there's a great [reference of all caps for the 3400c on macdat.net](https://macdat.net/cap_reference/apple/powerbook/3400c.html).

I don't have a stockpile of capacitors, so I've emailed [Console5](https://console5.com/store/). <s>They don't yet have a preassembled kit for the 3400c, and it sounds like they're working on one now!</s>

Console5 now has an [SMD Polymer + Tantalum cap kit for the PowerBook 3400c](https://console5.com/store/apple-macintosh-powerbook-3400c-smd-polymer-tantalum-cap-kit.html)—I have one on hand and will work on a full recap soon!

### WiFi (802.11b)

I ordered a [Lucent WaveLan Turbo Silver WiFi Card](https://www.ebay.com/itm/220617473457) for $20, and since this is similar to the card Apple used in it's earliest WiFi Gear (like my original AirPort base station), I'm hopeful it will work for 802.11b wireless networking on the 3400c.

[This article states you can even run AirPort 1.2](https://fweb.wallawalla.edu/~frohro/Airport/Airport12OS86.html) on Mac OS 8.6 on the 3400c. I'll have to see if that works!

Not that the built-in 10baseT Ethernet is a bad option... it'd just be cool to see if I can get a fully wireless setup.

### Battery Refurbishment (Lithium Ion)

Both machines came with Li-Ion batteries that hold a charge. I've tested my original battery, and it'll go for about 20-30 minutes on a full charge, though the system 'stutters' after a minute or so of sitting idle (at least, the Flying Toasters in After Dark get a bit choppy!).

I would love to find a way to refurbish these batteries, but [from what I've read](https://68kmla.org/bb/index.php?threads/powerbook-3400c-battery-rebuild.42943/), the 3400c's battery is a bit of a pain, and it will brick itself if you tamper with the cells. Not only that, the shell is welded plastic, so it will likely get a bit mangled if I try opening it up.

We'll see... since I have two, I feel okay with sacrificing one in the name of exploration!

### USB 2.0 CardBus, Attempt #2

See above—I might still be able to get my CardBus USB 2.0 card working with an earlier version of USB Card Support. We'll see.
