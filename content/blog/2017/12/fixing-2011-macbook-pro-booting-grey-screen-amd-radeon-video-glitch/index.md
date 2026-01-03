---
nid: 2825
title: "Fixing a 2011 MacBook Pro booting to a Grey Screen - AMD Radeon Video Glitch"
slug: "fixing-2011-macbook-pro-booting-grey-screen-amd-radeon-video-glitch"
date: 2017-12-23T16:59:13+00:00
drupal:
  nid: 2825
  path: /blog/2017/fixing-2011-macbook-pro-booting-grey-screen-amd-radeon-video-glitch
  body_format: markdown
  redirects: []
tags:
  - amd
  - electronics
  - gpu
  - mac
  - macbook pro
  - repair
  - resistor
  - soldering
---

I've been a Mac user for years, and I've repaired hundreds of different Macs, from the early II series to the latest 2015 and 2016 model MacBook Pros, iMacs (and other Apple hardware to boot!), and there is almost never a hardware situation where I've thrown in the towel and told someone to ditch their Mac.

The 2011 MacBook Pro has, for almost a decade, been the exception to that rule. There was a major flaw in the AMD Radeon GPUs included with that model year's logic board which seemed to cause GPU failure either due to overheating, internal chip problems, BGA solder joints getting broken, or a combination of the above. The problem was so rampant, Apple was forced to set up a [free repair program for affected MacBook Pros](https://www.apple.com/support/macbookpro-videoissues/)—though the 2011 model has since been dropped from that program. I've handled three 2011 MacBook Pros (none of them my own—I had an Air back then), and all three of them were scrapped because of the GPU issue.

My sister just turned over her 2011 15" MacBook Pro, which she said was running slow, and I dug in. First off, it was using a slow 5200 RPM hard disk; after replacing that with a nice, fast SSD, and ensuring she had 8 GB of RAM in the laptop, I was pretty pleased with my work, and was about to shut down the laptop and send it on its way. But then, I noticed the display would 'glitch'. Horizontal banding, some weird color issues... things I had seen before.

<p style="text-align: center;">{{< figure src="./samsung-850-ssd-in-macbook-pro-2011-sata.jpg" alt="Replaced 5200 rpm hard drive HDD with Samsung 850 SSD in 2011 MacBook Pro" width="650" height="439" class="insert-image" >}}<br>
<em>Replacing the slow hard drive with an SSD makes this thing feel brand new!</em></p>

## Beginning of the Debugging Journey

Fearing the worst, I rebooted into the [Apple Hardware Test mode](https://support.apple.com/en-us/HT201257) (right after startup sound, hold 'D' key). I ran the quick test, which found no errors. So I ran the full (super long) test... no errors again. Huh—usually the GPU issue would present itself during the AHT, but not this time.

{{< figure src="./apple-hardware-test-no-problems-found.jpg" alt="Apple Hardware Test - No problems found. AHT" width="650" height="488" class="insert-image" >}}

So I rebooted. Apple logo, then progress bar, then grey screen. Ten minutes later, still a grey screen—and the fans are spinning madly. Not good.

So then I tried:

  - [Safe mode](https://support.apple.com/en-us/HT201262) (hold down Shift from startup sound through to login or desktop)—same thing, stuck on grey screen after Apple logo + progress bar.
  - [Recovery mode](https://support.apple.com/en-us/HT201314) (hold down Command + R from startup sound to Apple logo)—same thing, again.
  - [Internet Recovery mode](https://support.apple.com/en-us/HT201314#internet) (hold down Option + Command + R from startup sound to Apple logo)—same thing, again.

Getting nervous, I then tried [single-user mode](https://support.apple.com/en-us/HT201573) (hold down Command + S from startup sound until you see <s>the matrix</s> text going past as the Mac boots into its FreeBSD underpinnings)—and was happy to find at least _this_ worked fine. I did an `fsck -y` to check the hard disk. A few records were off, but they were repaired successfully. I didn't see anything obviously wrong, but knowing from past experience that problems usually surface only when the GPU/Radeon .kext files (Kernel Extensions) are loaded... I was assuming the worst.

I was going to pop out the SSD and RAM, and suggest my sister sell the laptop for scrap... but then I thought twice—I would look if there was _any_ possible way to resurrect this thing.

Obviously everything else was working fine—Internet Recovery proved wifi/networking was okay. Single user mode proved disk, RAM, CPU, and even integrated graphics were okay. The _only_ thing that seemed wrong was the Radeon GPU. _Surely_ there's a way to bypass it!

Lucky for me, I found this answer on Stack Exchange: [GPU problem - Boot Hangs on Grey Screen](https://apple.stackexchange.com/a/295805/17366).

## Attempting to drop the Radeon .kexts

That answer had a fairly comprehensive guide to—using software changes only—disable the Radeon GPU and get the Mac happy again.

After running through the guide twice, I eventually got the Mac to boot... to a grey screen again. But this time it would reboot itself within a minute or so, so that was different! Alas, after hacking around a bit more with System Integrity Protection disabled, the reboot cycle eventually became quite short indeed:

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/PuDxASIVsqE" frameborder='0' allowfullscreen></iframe></div>

(This got old, _fast_.)

Hitting dead ends when attempting the software fix, I was about ready to throw in the towel... but then I scrolled further in that Stack Exchange answer, and noticed a link to this interesting article: [MacBook 2011 Radeon GPU Disable - Real Radeongate Solution](https://realmacmods.com/macbook-2011-radeon-gpu-disable/).

Being somewhat handy with a soldering iron (but having never done SMD work—basically, soldering little bits and bobs that are the size of a speck of dust!), I thought I'd give it a go. Better than telling my sister to junk the laptop!

## Hardware hack to cut off the GPU entirely

I'm not going to rehash the entire article from RealMacMods (after all, they found the process, and they also offer it as a service for $85 for anyone not willing or able to do it himself!), but I did want to highlight a few parts where I think it's important to further illustrate what needs to happen.

The first part of the process involves prepping the software side of the Mac by doing the following:

  1. Build a USB boot drive with Arch Linux.
  2. Boot the MacBook Pro from said USB drive (hold option key at startup to choose it).
  3. Follow the directions to get in the right Arch Linux boot mode so you get to the console.
  4. Hack your EFI by adding a file telling your Mac to disable the Radeon GPU.
  5. Reboot into Safe Boot mode (Shift key all the way through startup).
  6. Shut down using the Apple Menu > Shut Down option.

Again, see the [source article from RealMacMods](https://realmacmods.com/macbook-2011-radeon-gpu-disable/) for the gory details (they even offer a $10 download to package up the fix for you—well worth it if you're not used to a command line!).

Once that's done, it's time to get your hands dirty, by permanently modifying the MacBook Pro's logic board!

First, to prepare the patient for surgery:

  1. Unplug the Mac, put it on a nice, non-scratching, non-static surface, and flip it over. (I use a [cutting mat](https://www.amazon.com/Alvin-Professional-Self-Healing-Cutting-GBM1218/dp/B0015AOIYI/ref=as_li_ss_tl?ie=UTF8&qid=1514006181&sr=8-3&keywords=cutting+mat&linkCode=ll1&tag=mmjjg-20&linkId=94f6afcd5122a87dccba47b6bd8011ad) on my workbench... which is an old desk).
  2. Unscrew the 10 tiny phillips screws on the bottom.
  3. Pull off the back cover (should come off quite easily unless it's dented somewhere), and place it aside.

At this point, you're going to want to make sure you have the tools to make this operation not-impossible—you need to desolder / remove a tiny resistor ('R8911') from the logic board, and you need a few tools to do that:

<p>{{< figure src="./macbook-pro-on-workbench-soldering-station.jpg" alt="Weller soldering station and magnifying glass at workbench with 2011 MacBook Pro" width="650" height="382" class="insert-image" >}}<br>
<em>Pictured: <a href="https://www.amazon.com/Weller-WES51-Analog-Soldering-Station/dp/B000BRC2XU/ref=as_li_ss_tl?s=aps&ie=UTF8&qid=1514006662&sr=1-2-catcorr&keywords=weller+soldering+station&linkCode=ll1&tag=mmjjg-20&linkId=35e55fc7b00ab7f48968d9ca55199476">Weller soldering station</a>, <a href="https://www.amazon.com/SE-MZ101B-Helping-Magnifying-Glass/dp/B000RB38X8/ref=as_li_ss_tl?_encoding=UTF8&pd_rd_i=B000RB38X8&pd_rd_r=3M6QYDYYC7MSJH97TAG7&pd_rd_w=UpjsG&pd_rd_wg=LU83Q&psc=1&refRID=3M6QYDYYC7MSJH97TAG7&linkCode=ll1&tag=mmjjg-20&linkId=064c9aa0341a4daa9912ea60c35edea2">helping hand with magnifying glass</a>, and a <a href="https://www.amazon.com/Weller-PTF7-PTS7-TC201T-Degree/dp/B06XX6CZ18/ref=as_li_ss_tl?s=hi&ie=UTF8&qid=1514006759&sr=1-4&keywords=weller+soldering+tip+wes51&linkCode=ll1&tag=mmjjg-20&linkId=32a07bc876a324d59e9c5c8ce341d6dc">precision tip</a> for the soldering iron.</em></p>

You can use a handheld magnifying glass... but if you're like me, you're going to need both hands to steady the soldering iron when desoldering the tiny, tiny resistor from the logic board. How tiny? Take a look through the magnifying glass:

{{< figure src="./macbook-pro-2011-radeon-gpu-disable-resistor.jpg" alt="MacBook Pro 2011 Radeon GPU disable resistor through magnifying glass" width="650" height="445" class="insert-image" >}}

Still don't see it? Let's zoom and enhance:

{{< figure src="./resistor-zoomed-in-mbp-2011-radeon.jpg" alt="MacBook Pro 2011 Radeon GPU resistor to disable highlighted through magnifying glass" width="474" height="360" class="insert-image" >}}

And a wider shot, for perspective:

{{< figure src="./resistor-gpu-radeon-macbook-pro-highlight.jpg" alt="MacBook Pro 2011 Radeon GPU resistor highlighted" width="650" height="425" class="insert-image" >}}

So, with the resistor identified, it's time to turn on the iron (I set mine to 500°F and tinned the tip with a tiny bit of lead-free solder) and get to work! I hold the iron in my left hand, and provide a little resistive force to steady it with my right hand. Touch the tip of the iron to each metal side of the resistor (where the joints are), alternating one side to the other for about 1-2 seconds each, until you notice the resistor starts to become free from the logic board. Once that happens (after about 15 seconds in my case), put the tip against the side of the resistor facing the open space on the logic board, and push, with a very slight upward (away from the logic board) force.

You might need to keep heating the resistor a bit before it pops free. And if you're like me, you might shoot the little resistor a few inches across the logic board! Just be sure to do the following after it comes off:

  1. Make sure there's not a solder joint between the two pads where the resistor used to be. If there are, heat the pads with the iron tip until you can 'wick away' the solder a little. Just enough to not join the two pads together.
  2. Set down the iron / put it in it's holder, and get the resistor off the logic board. Hopefully you can just lift the bottom-cover-less laptop, turn it over, and you see a tiny black speck fall to you work surface.

After you get the resistor off. Take a second and marvel at it's minute size. And realize there are _thousands_ of these things soldered to the logic board!

{{< figure src="./resistor-smd-and-through-hole.jpg" alt="Resistors - through hole and tiny SMD surface mount" width="650" height="397" class="insert-image" >}}

Those are specks of dust in the image—except for the very-slightly-larger black spec next to the standard through-hole resistor. The resistor is small enough I can't pick it up with my fingers—or even a standard needle-nose pliers!

With the resistor gone, one step remains: replace the bottom cover, plug it in, and turn it on!

I did so, and less than 40 seconds later (the SSD makes the boot process _fast_!), the Mac was as good as it's ever been, sans AMD Radeon GPU:

{{< figure src="./intel-hd-graphics-3000-no-amd-radeon.jpg" alt="Intel HD Graphics 3000 integrated graphics GPU and no AMD Radeon GPU on 2011 MacBook Pro" width="650" height="478" class="insert-image" >}}

One last thread that was worth a read-through for more background and debugging information was from the RealMacMods forum, [After GPU repair issues (R8911 removal)](https://realmacmods.com/forums/topic/after-gpu-repair-issues-r8911-removal/). After removing the resistor, be very careful when upgrading the OS or making other major changes (be sure to keep current backups!). And, as suggested by RMM, try to avoid resetting the NVRAM, just in case that makes things go a bit south.
