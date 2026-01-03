---
nid: 3321
title: "Getting RISC-V (again): Milk-V's Mars CM"
slug: "getting-risc-v-again-milk-vs-mars-cm"
date: 2023-11-01T15:02:16+00:00
drupal:
  nid: 3321
  path: /blog/2023/getting-risc-v-again-milk-vs-mars-cm
  body_format: markdown
  redirects: []
tags:
  - architecture
  - arm
  - isa
  - jh7110
  - linux
  - milk-v
  - risc-v
  - sbc
---

{{< figure src="./milk-v-mars-cm-with-box.jpg" alt="Milk-V Mars CM with Box" width="700" height="422" class="insert-image" >}}

tl;dr: No, it's not a replacement for a Raspberry Pi Compute Module 4. But yes, it's an exciting tiny RISC-V board that could be just the ticket for more RISC-V projects, tapping into the diverse ecosystem of [existing Compute Module 4 boards](https://pipci.jeffgeerling.com/boards_cm).

This tiny computer is the [Mars CM](https://milkv.io/mars-cm). It's the exact same size and shape as the Raspberry Pi Compute Module 4. It _should_ be a drop-in replacement. And on its box it says it supports 4K, Bluetooth and WiFi, and has gigabit Ethernet. It's also supposed to have PCI Express!

Why is this thing important? Well, right now at least, [it's still hard to buy Compute Modules](https://rpilocator.com/?country=US&cat=CM4). There are tons of [really cool projects](https://pipci.jeffgeerling.com/boards_cm) that use them.

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/RhPKZ5JpbHw" frameborder='0' allowfullscreen></iframe></div>
</div>

_This blog post is a lightly-edited transcript of video embedded above. [Watch the video](https://www.youtube.com/watch?v=RhPKZ5JpbHw) for the full context._

But like I said, it's hard to find one. Could you just drop a Mars CM in its place?

That's the hope. I mean, [feldspaten got his working on a Turing Pi 2 cluster board](https://feldspaten.org/2023/10/27/RISC-V-in-a-Turing-Pi-2/). So if you have a CM4 board, and can't find a CM4 for it... maybe this is an option?

I actually tested the same processor the Mars CM uses—the JH7110—on the StarFive VisionFive 2. And it's not a bad little processor, it just has some growing pains! Make sure to [read my post on the VisionFive 2](/blog/2023/risc-v-business-testing-starfives-visionfive-2-sbc) for more background on RISC-V and the JH7110 specifically.

{{< figure src="./milk-v-mars-cm.jpeg" alt="Milk-V Mars CM" width="700" height="394" class="insert-image" >}}

I bought the Mars CM for $54 plus $12 shipping on [ARACE](https://arace.tech/products/milk-v-mars-cm)—I bought the model with 4 gigs of RAM and 16 gigs of built-in eMMC storage, here on the back.

## Bringup

I plugged the Mars CM into my Compute Module 4 IO Board, and after a little while, the little green LED on the Mars CM started flashing, two blinks every other second. But no HDMI output.

Maybe I needed to download an OS?

So I went to the URL on the side of the box ([http://milkv.io/docs/mars-cm](http://milkv.io/docs/mars-cm)), and... well, I guess I'm one of the first people to get one of these things, because the page for it isn't even up yet! (Still isn't, at the time of this writing.)

So I browsed around, and they already have a plain old [Mars](https://milkv.io/mars), so I went to _that_ board's [Getting Started guide](https://milkv.io/docs/mars/getting-started) and I downloaded [their release of Debian](https://milkv.io/docs/mars/resources/image). It looks like it's based on the VisionFive image, so hopefully it works out of the box.

I flashed it to a microSD card with Etcher, stuck the card into the Compute Module 4 IO Board, and rebooted, and...

Well, same thing happened. On the Pi Compute Module, if you have an eMMC module, the microSD card is ignored completely, so that might be the case here, too.

But seeing as the only page that was visible in the Mars CM docs was an [Intro page](https://milkv.io/docs/mars/compute-module/introduction), I decided to head over to the MilkV community forums and see if anyone else had the same problem.

And... it turns out the [Compute Module subforum](https://community.milkv.io/c/mars/mars-cm/10) was completely empty!

So I did what any good noob would do and [started a new topic](https://community.milkv.io/t/mars-cm-getting-started-guide-missing/845/10), asking how to get this thing going.

I also started a [new issue in my sbc-reviews repo](https://github.com/geerlingguy/sbc-reviews/issues/22) to track my work.

And luckily, I wound up trying out serial console access. I have [this little USB to UART adapter](https://amzn.to/45V1Jf1), and following the [Mars documentation](https://milkv.io/docs/mars/getting-satrted/setup), I crossed my fingers and hoped the GPIO pinout was the same.

And luckily it was!

{{< figure src="./opensbi-boot-uart-serial-console-mars-cm-coolterm-mac.jpg" alt="OpenSBI Boot UART Serial Console Mars CM" width="700" height="394" class="insert-image" >}}

I launched CoolTerm and watched the serial output. It looks like it uses the default password `milkv` for the `root` user, and now that I'm logged in, I grabbed the IP and tried to SSH in.

Unfortunately, the default SSH config is a bit too secure for that.

So I had to run the one-line commands below over serial to make it so I could log in over SSH:

```
sed -i '/PasswordAuthentication yes/s/^#//g' /etc/ssh/sshd_config
sed -i '/PermitRootLogin prohibit-password/s/^#//g' /etc/ssh/sshd_config
sed -i '/PermitRootLogin prohibit-password/s/PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config

systemctl restart sshd
```

I was finally in!

## Exploring the board

Apt gave me a few issues installing things initially, but here's the `neofetch` output:

```
       _,met$$$$$gg.          root@starfive 
    ,g$$$$$$$$$$$$$$$P.       ------------- 
  ,g$$P"     """Y$$.".        OS: Debian GNU/Linux bookworm/sid riscv64 
 ,$$P'              `$$$.     Host: Milk-V Mars CM eMMC 
',$$P       ,ggs.     `$$b:   Kernel: 5.15.0 
`d$$'     ,$P"'   .    $$$    Uptime: 30 mins 
 $$P      d$'     ,    $$P    Packages: 1324 (dpkg) 
 $$:      $$.   -    ,d$$'    Shell: bash 5.2.2 
 $$;      Y$b._   _,d$P'      Terminal: /dev/pts/0 
 Y$$.    `.`"Y$$$$P"'         CPU: (4) @ 1.500GHz 
 `$$b      "-.__              Memory: 426MiB / 3874MiB 
root@starfive:~# 
   `Y$$.
     `$$b.
       `Y$$b.
          `"Y$b._
              `"""
```

These are the basic specs in Linux. I started compiling all this data into [my sbc-reviews repo](https://github.com/geerlingguy/sbc-reviews/issues/22), so go check that out if you want _all_ the gory details.

Before I benchmarked the CPU, I wanted to see if the PCI Express interface worked at all... and it does! I was able to get a Kioxia SSD running without any tweaking. It reports as PCIe Gen 2, so it could, in theory, get 400 megabytes per second.

But in this case, all I could get was 150 to 250 megabytes per second. Same as the VisionFive 2.

So it's nice to have working PCIe, but it's limited a bit by the processor.

## Performance

But to test the processor's general performance, I ran Geekbench. It runs on Arm, X86, and even RISC-V in preview, so I downloaded it, but then I couldn't expand it!

The default OS image only gives you 4 gigs of disk space. So I had to follow [this process](https://doc-en.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/extend_partition.html) to recreate the disk partition and expand it with a utility called `resize2fs`.

It's a little nerve-wracking, even if you've done a lot of command line disk partitioning stuff before. Hopefully they can get automatic disk resizing working like Raspberry Pi and other SBC vendors.

I also was glancing around on the VisionFive 2 site, and it looks like it [might not be a good idea to upgrade the system](https://doc-en.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/avoid_running.html), at least for the VisionFive. That same advice applies to the Mars CM too for now.

I mean, I get it, it's early days for RISC-V, but when I read documentation and it says "don't update," that raises a few alarm bells.

But getting back to Geekbench, I could finally run it. It took a _very_ very long time, but [here's the result](https://browser.geekbench.com/v6/cpu/3281902):

  - 74 single core
  - 219 multi core

That's... not amazing. And it illustrates two things: one, that some of the tests Geekbench uses are not quite optimized for RISC-V. And two, even with those optimizations, this CPU is just a lot slower than even older high-performance Arm cores.

{{< figure src="./geekbench-comparison-pi-mars-cm.jpg" alt="Geekbench 6 performance Mars CM vs Raspberry Pi" width="700" height="394" class="insert-image" >}}

The Raspberry Pi 4 is 3 times faster, and the brand new Pi 5 is nearly _7_ times faster!

And it's not just Geekbench. I ran my [top500 Linpack benchmark](https://github.com/geerlingguy/top500-benchmark), and the Mars CM gets just _two_ gigaflops. The Pi 4 gets 12, and the Pi 5, 30!

I ran a bunch of other benchmarks, and also measured power consumption. And this isn't a _terrible_ little SBC. But it's far from efficient, compared to any modern Arm processor:

{{< figure src="./hpl-efficiency-mars-cm-pi-orange-pi-rockchip.jpg" alt="HPL Efficiency Mars CM vs Pi vs Orange Pi Rockchip RK3588" width="700" height="394" class="insert-image" >}}

For Linpack, the half-gigaflop per watt rating is at the bottom of my list, compared to more modern Rockchip boards getting over _four_ gigaflops per watt.

At idle, the Mars CM only pulls down like 1 watt, so _that's_ too bad.

And built-in networking puts out about a gigabit, so that's good too. But the eMMC interface is a little slow, maxing out around 45 MB/sec.

That puts it in the ballpark of the Pi 4, at least, but the Ethernet connection doesn't support PTP timestamping like the CM4, so it's not quite as flexible.

Plus, I couldn't get WiFi to work at all, despite attempts to get a connection to any of my four test WiFi networks.

It's probably a matter of the OS image just not being complete yet. So depending on when you read this post, WiFi might be working.

## Conclusion

RISC-V is very cool. I love seeing this new hardware. And the fact the base architecture is open is great.

But there are a _lot_ of people who are a bit optimistic about where we are today. I've gotten comments saying "Arm is dead in the water," or "RISC-V will take over in 5 years because it's open."

_That's just not true._

Discounting the fact there are only a few decently-fast RISC-V designs on the market, and the price to performance is just not there, individual chip designs still require licensing.

So it's not like if someone made a Zen 4 RISC-V core, every chip maker could just pump it out. So while RISC-V is _more_ open, it is not just a totally open hardware ecosystem. So it won't win by default.

It has to win, like all technology does, by _solving problems_. And right now, for tiny microcontrollers, or disk controllers, or things like that, it can, and it is.

But in terms of this thing being a Compute Module 4 killer? Well, the fact it's still hard to find CM4s even while Raspberry Pi is cranking out thousands every week speaks volumes.

{{< figure src="./milk-v-mars-cm-with-compute-module-4-clones-arm.jpg" alt="Milk-V Mars CM with other CM4 clone boards Arm" width="700" height="444" class="insert-image" >}}

And there are plenty of Arm competitors to fill the niche of 'not Raspberry Pi' compute modules, like the [Pine64 SoQuartz](https://github.com/geerlingguy/sbc-reviews/issues/7), the [Radxa CM3](https://github.com/geerlingguy/sbc-reviews/issues/15), or the [Banana Pi CM4](https://github.com/geerlingguy/sbc-reviews/issues/11), all which I've tested before.

This is a very cool little board. I love that it already works so well. And that it includes PCI Express built-in. But is it a replacement for the Raspberry Pi? No. It doesn't do hardware PTP timestamping. It isn't compatible with as much software. It doesn't have all the same IO interfaces, and it's pretty slow. But that doesn't mean I don't like it!

If you're interested in getting into a new architecture, or if you just need a computer to throw onto a Compute Module board, it's certainly worth checking out.

But just like I mentioned in my VisionFive 2 review, this isn't meant for a typical user. That'll come in a generation or two, but right now, RISC-V isn't quite mainstream enough for the average SBC hobbyist or maker.

Now the [Milk-V Pioneer](https://milkv.io/pioneer)... that's a 64-core RISC-V monster... I don't have one, but what do you think? Is it worth checking out?
