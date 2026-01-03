---
nid: 3486
title: "Build log: Macintosh Classic"
slug: "build-log-macintosh-classic"
date: 2025-08-22T14:01:16+00:00
drupal:
  nid: 3486
  path: /blog/2025/build-log-macintosh-classic
  body_format: markdown
  redirects: []
tags:
  - classic
  - computer
  - macintosh
  - marchintosh
  - restore
  - retro
  - video
  - youtube
---

Continuing the [retro computer series](/tags/retro), I've recently completed the _first_ part of a restoration of my Aunt's old Macintosh Classic.

{{< figure src="./macintosh-classic-on-desk.jpeg" alt="Macintosh Classic on desk" width="700" height="467" class="insert-image" >}}

This Classic was handed to me alongside my Uncle Mark's Apple II, which I'll probably cover later (we've played a game of whack-a-mole with issues on that machine! Well worth it but I haven't hit a point where enough things are working to cover it well, heh).

The Classic is a strange Mac—it was [introduced in 1990](https://everymac.com/systems/apple/mac_classic/specs/mac_classic.html) as a budget version of the 1986 Macintosh Plus, with a 68000 CPU in an era when the 68030 was the new hotness.

It started under $1,000, but was a slightly more modern take on the Plus, including a cooling fan, a new motherboard design, and options for up to 4MB of RAM and an internal SCSI hard drive connection.

My aunt's Classic was the $1,499 model which comes with a Memory Expansion Card (which boosted the RAM to 2 MB, with slots for up to 4MB), and an internal 40 MB SCSI drive.

## Evaluating the Condition, Restoring a Classic

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/779nru5udpQ" frameborder='0' allowfullscreen></iframe></div>
</div>

I've recorded the entire process of restoring the Classic, which is embedded above. But I'll summarize the process here, starting with the most important part: "don't turn it on, take it apart!"

That line is familiar to EEVBlog viewers, of course—and in that context it's more about tearing into a new product to see how it's constructed prior to testing it out. But in the case of retro computers, with 40 year old power supplies, RIFA capacitors, and leaky batteries and electrolytic caps... you could just save yourself a lot of trouble by tearing into it _before_ plugging it it in.

And in the case of a Macintosh Classic, there are two _primary_ killers: leaky batteries and leaky capacitors. This blog post isn't an exhaustive look at all that could go wrong. For that, I'll direct your attention to videos from the likes of [Adrian's Digital Basement](https://www.youtube.com/@adriansdigitalbasement), [Mac84](https://www.youtube.com/Mac84), [Branchus Creations](https://www.youtube.com/@BranchusCreations), [Action Retro](https://www.youtube.com/ActionRetro), [This Does Not Compute](https://www.youtube.com/@ThisDoesNotCompute), et all.

But in my case, I quickly checked for the common culprits:

  - **Leaky battery**: Different old Mac models used different PRAM batteries, but _most_ are prone to leaking onto the motherboard. On a few Macs, the battery was accessible externally... but on most, the battery is either soldered to or socketed in the motherboard, and when they leak, they make a mess of everything around them or below them (due to gravity). Luckily this Classic had a Sonnenschein battery, which is one of the very few [not known to leak after decades](https://www.macdat.net/repair/kb/batteries_macintosh.html). I removed the battery and would later replace it with a coin cell in a [MacBatt battery adapter](https://www.tindie.com/products/jurassicomp/macbatt-internal-cr2032-pram-macintosh-battery/).
  - **Leaky capacitors**: A quick visual inspection revealed nothing but a layer of dust, a couple little critters, and _maybe_ a little fluid under one or two capacitors. But it's always hard to tell without giving the area around them a cleaning, and getting the larger ones desoldered—especially on the analog board.
  - **Cracked solder joints**: Especially in compact Macs with no fan, some of the solder connections on the analog board would get 'dried out' or crack, especially for the higher power components. Visually inspecting all the solder joints on the bottom of the board, I didn't see anything alarming, though I did reflow a couple joints with fresh solder, and gave a few areas a good cleaning with isopropyl alcohol.

{{< figure src="./vlcsnap-2025-07-27-21h25m40s201.jpeg" alt="Recapping Macintosh Classic analog board soldering underside with pinecil" width="700" height="394" class="insert-image" >}}

After a preliminary checkup, I ordered a couple sets of capacitors from Console5.com, and [recapped both the analog board and the motherboard](https://github.com/geerlingguy/retro-computers/issues/6).

The analog board varies from Mac to Mac, even in the same model, so you need to match up your board's part number to the part number on a site like Console5.com, to make sure you have the right capacitors.

One thing I hope I can help you avoid in your own compact Mac repair job is breaking the anode cap, the rubber suction cup-like thing covering the little metal spring that contacts part of the CRT glass:

{{< figure src="./macintosh-classic-jeff-repair-analog-anode.jpeg" alt="Jeff breaks anode cap on Mac Classic" width="700" height="394" class="insert-image" >}}

I tried just yanking it, and ripped a little bit of the wire off inside the anode cap, but was able to salvage enough and screw the little metal clip back on. Lesson learned: the clip needs to be pinched/squeezed together to pull out of the CRT, don't just pull straight up!

Also, if you have any concerns over how I'm wearing safety glasses _and_ gloves for this procedure, know that I am very much a belt-and-suspenders kind of person when it comes to potentially harmful voltages. One of my first experiences getting inside a computer was a 120V shock in my first PC, a little scrap-built 386 running DOS 6.22. Luckily both the computer and I survived.

**WARNING**: Note that you should use a good, conductive screwdriver, well-grounded to the chassis (or the ground screw lug on the CRT), to discharge the CRT through the anode _before_ doing any work in there. Check my video for a bit of reference for that process. CRTs, especially color CRTs, use deadly voltages, and can hold a charge for days, weeks, or longer after being unplugged.

{{< figure src="./resoldering-smd-components-tantalum-caps-mac-classic-motherboard.jpeg" alt="Resoldering tantalum caps on Mac Classic motherboard" width="700" height="394" class="insert-image" >}}

Overall the process is tedious but not too difficult if you have moderate experience soldering. The surface mount components on the motherboard can be a little more tricky, but luckily there are only 7 capacitors that need replacing there. You can try direct desoldering, hot air, or a 'snip the can, yank the plastic, and desolder the legs' approach for removing the old caps. I chose the latter method after seeing it used in an iiiDIY video, and it seems to work well enough, not stressing the pads under the old caps too much.

## Upgrades

After recapping the motherboard, I decided to perform two upgrades:

  - **Upgrading the RAM to 4 MB**: Moving the jumper on the Memory Expansion Card to 'SIMM Installed', I installed a [2 x 1MB RAM upgrade kit](https://www.ebay.com/itm/144565895077) from Mac Memories on eBay. It worked without a hitch, and Mac OS 6 saw the 4 MB with no problem.
  - **Installing a PRAM coin cell battery replacement**: The [MacBatt](https://www.tindie.com/products/jurassicomp/macbatt-internal-cr2032-pram-macintosh-battery/) allows me to install a standard CR2302 coin cell battery where the strange 3.6V '1/2 AA' battery goes. It seems to work fine, though the Poor old Mac [doesn't know about dates beyond 2020 without an app like SetDate](https://lowendmac.com/1999/112k-just-another-day-for-macs-but-not-for-all-apps/).

I gave some parts a good cleaning with isopropyl alcohol, dusted everything off inside, and put it all back together... and, it worked!

{{< figure src="./oscar-the-grouch-mac-classic-trash-icon-i-love-trash.jpg" alt="Oscar the Grouch Mac Classic Trash Can" width="700" height="408" class="insert-image" >}}

And it was a fun surprise seeing my Aunt had installed [The Grouch](https://www.cryan.com/blog/20161125.jsp) on this machine all those years ago. Though I'm sure many a parent were not amused when their kids would delete random files just to see Oscar the Grouch pop out of the Mac's Trash can!

## Conclusion and Next Steps

The hard drive initially worked through about 8 boot cycles, and I even had it running for an hour or two at a time twice, to make sure the CRT, analog board, etc. were all fine after the recapping.

But around the 9th or 10th boot, I would just get the flashing question mark on a floppy disk, meaning the Mac didn't see any valid boot volume. The SCSI hard drive still spins up, but after all these years, the read/write heads may be gummed into place, or something worse. I have an [open issue to fix and back up the SCSI drive](https://github.com/geerlingguy/retro-computers/issues/18), and am booting the Classic off an external [BlueSCSI v2](https://bluescsi.com/v2) for now.

I may also [retro-brite the Classic](https://github.com/geerlingguy/retro-computers/issues/8), but I'm not sure. The old plastic color wears pretty well, but it might be nice to get it closer to the original beige color, and even out a few imperfections where something was stuck on the case.

I'm happy the first compact Mac restoration I attempted went so well, and I'm looking forward to cracking the case of _another_ Aunt's slightly older Mac Plus. And looking at some of the other retro projects people will bring to [VCF Midwest](https://www.vcfmw.org) in less than a month ;)
