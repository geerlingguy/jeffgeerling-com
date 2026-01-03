---
nid: 3320
title: "Everything I've learned building the fastest Arm desktop"
slug: "everything-ive-learned-building-fastest-arm-desktop"
date: 2023-10-27T14:00:31+00:00
drupal:
  nid: 3320
  path: /blog/2023/everything-ive-learned-building-fastest-arm-desktop
  body_format: markdown
  redirects:
    - /blog/2023/everything-ive-learned-about-fastest-arm-desktop
aliases:
  - /blog/2023/everything-ive-learned-about-fastest-arm-desktop
tags:
  - altra
  - ampere
  - arm
  - arm64
  - cpu
  - mac pro
  - memory
  - workstation
---

{{< figure src="./ampere-altra-developer-platform-hero-shot_0.jpeg" alt="Ampere Altra Developer Platform Hero Shot" width="700" height="394" class="insert-image" >}}

This is the fastest Arm desktop in the world, yes, even faster than the [M2 Ultra Mac Pro](https://www.apple.com/mac-pro/). And today, I made it even faster.

I upgraded everything: Faster RAM, 128 core CPU, 40 series GPU, I did it all, and we'll see how much we can obliterate the M2 Mac Pro.

128 cores—that's five times more cores, I'm also going to upgrade this thing from 96 all the way to _384 gigabytes_ of RAM. The Mac Pro? Sorry, it only goes up to 192.

And we're just in time for the [new Cinebench 2024 benchmark](https://www.maxon.net/en/article/maxon-introduces-cinebench-2024), which—yes—this machine dominates.

But it's not all perfection. The M2's individual cores are faster, and I didn't even mention Intel or AMD—they also do really well single-core. And 128 cores can be overkill if your application can't use all of them.

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class="embed-container"><iframe src="https://www.youtube.com/embed/argfZlPZKdY" frameborder="0" allowfullscreen=""></iframe></div>
</div>

_The following is a transcript of the above video. Please watch the [original video](https://www.youtube.com/watch?v=argfZlPZKdY) for more context._

I tested two systems for this video:

  - [Ampere Altra Developer Platform](https://www.ipi.wiki/products/ampere-altra-developer-platform) (a full system build, in my case with the 96-core and 128-core CPU)
  - [Ampere Altra Dev Kit](https://www.ipi.wiki/products/com-hpc-ampere-altra), in my case with the 64-core CPU)

Ampere and ADLINK designed this system to be the ultimate Arm development workstation. And that, it is. But I like doing crazy things. Can this also be a great gaming rig? Can the CPU break a teraflop? Can we install a 4070 Ti in it?

## Current Status

As of today, I have this thing running 128 CPU cores at 2.8 GHz. I upgraded the RAM to 384 GB of DDR4 3200 ECC RAM, specifically six Samsung 64 GB sticks. I installed an Nvidia 4070 Ti.

It's running both Ubuntu 22.04 Server and Windows 11 for Arm now. I even got Steam installed on Ubuntu, after so many commenters kindly pointed out [Box86](https://box86.org) and [Box64](https://github.com/ptitSeb/box64) exist!

But before we get into full benchmarks and gaming, I want walk you through the RAM and CPU upgrades, because I learned a lot about this platform. Like, did you know at a certain point, more CPU cores doesn't necessarily give you more performance, even on pure multicore tasks?

Yeah. And the main reason for that? Memory is just not getting faster at the same rate as our CPUs.

## Upgrading the RAM (The importance of benchmarking)

Have you ever seen one of those fancy server motherboards on Serve The Home? [This is a new server](https://www.servethehome.com/supermicro-as-2015hs-tnr-review-a-server-with-amd-epyc-bergamo/2/) for AMD's Bergamo CPU.

Do you see how many memory slots are in this thing? There are _twenty four_! There're two memory slots for each of the _twelve_ memory channels on the processor.

That's a lot, compared to a normal desktop, where you might get two or four slots for RAM. What gives? Well, modern multicore CPUs are getting faster and faster, but feeding them with data hasn't kept up. So big servers need more and more sticks of RAM feeding data to individual CPU cores just so they don't sit around waiting.

{{< figure src="./ram-samsung-transcend-detail.jpeg" alt="RAM - Samsung and Transcend detail DDR 3200 ECC CL22" width="700" height="394" class="insert-image" >}}

And RAM goes a lot deeper too. Look at these two sticks of RAM. See how the one on the right has twice the number of memory modules? That allows the individual stick of RAM to pump through data more quickly than the one on the left, even though _both_ of them are rated at DDR 3200 and CL22.

If you look _really_ closely on the labels, you can see one is 1Rx4, and the other one is 1Rx8. [Actually Hardcore Overclocking](https://www.youtube.com/watch?v=w2bFzQTQ9aI) has a great video on this, but bottom line, this x4 stick is about 30% faster than the x8!

I tested three setups: 96 GB of Transcend RAM, 96 GB of Samsung RAM, and _384 GB_ of Samsung RAM, and I learned a lot about memory latency and bandwidth.

But the most important thing I learned is this system design only exposes 6 out of the 8 available memory channels on this beefy CPU.

So there's actually an upper limit to how much performance I can get just upgrading the CPU.

This system's memory bandwidth [tops out around 174 Gigabytes per second](https://github.com/AmpereComputing/HPL-on-Ampere-Altra/issues/11#issuecomment-1732099325), but you might get more with more memory channels.

## Upgrading the CPU (96 to 128 cores!)

A lot of Ampere server builds do give all eight, and maybe I'll get one someday. But for now, I still wanted to test all 128 cores.

For the upgrade, it's a little different than a normal desktop CPU. I popped off the water cooling block, which is normal, but underneath, I made sure to follow the 'OPEN' pattern for loosening the CPU bracket.

I pulled out the 96-core CPU, and that is a _lot_ of pins:

{{< figure src="./lga-socket-ampere-altra-max-cpu.jpeg" alt="LGA Socket for Ampere Altra Max CPU" width="700" height="467" class="insert-image" >}}

I mean, on any of these modern Epyc, or Xeon, or Altra systems, there's just an enormous amount of pins, in this case for up to _8_ memory channels and _128_ lanes of PCI express. That's just a ton of bandwidth.

So in goes the 128-core CPU, and in my case, it's the 2.8 Gigahertz version. They actually make a 3 GHz version, but since Ampere sent this thing to me for testing, and the overall efficiency's probably a tiny bit better at 2.8 Gigahertz anyway, I'm not complaining.

I plugged it back in, booted back up, and it posted at 2.8 Gigahertz, so the next step was to boot into Linux and make sure I could see all 128 cores, which it did.

I ran my linpack benchmark again. On the 96-core CPU it got about 1.2 Teraflops—but I could still only get around 1.2 Teraflops.

After a ton of research, and after upgrading the system to 384 gigabytes of RAM, I could eke out about 1.3 teraflops, but it seems like that's the upper limit on this particular motherboard.

Which, I mean... that's not bad at all. But if you put the same CPU in a server with all 8 channels of RAM, this thing should go even faster, probably past 1.5 teraflops.

But if you _really_ care about teraflops, you need a graphics card.

Nowadays more and more workloads can go _way_ faster using a GPU, especially AI and machine learning. Not to mention games and design apps.

And sorry, Apple, but only allowing your own integrated GPU just doesn't cut it.

## Installing the GPU (4070 Ti)

I decided to go with an Nvidia 4070 Ti, and before you start yelling at me about not using AMD for a Linux-first build... AMD's drivers on Arm aren't quite as stable yet.

Nvidia making their own massive Arm processors probably has something to do with that, but in any case, I went with [this understated ProArt GPU from ASUS](https://amzn.to/49chAc0). It's not gaudy like most modern graphics cards, and it fits nicely in the case. I test-fitted my 4090 but that thing's a monster, and would also require this bigger power supply.

Maybe I'll upgrade to it someday, but for now, 4070 it is.

Now, before I could get anything out through the graphics card, I had to get drivers going.

Ampere has [a guide for the process](https://github.com/AmpereComputing/NVIDIA-GPU-Accelerated-Linux-Desktop-on-Ampere), but basically I installed a desktop environment since I was running Ubuntu Server, then I installed the Nvidia drivers.

I shut down the system, plugged my monitor into the card with HDMI instead of the integrated VGA port, and away it went!

One thing to note is you won't get any of the early boot stuff like the BIOS screen through a graphics card. Those things still go through the integrated ASPEED controller. But everything else in the OS goes through the GPU now.

### GPU support in Linux

And Ubuntu had no problems!

I ran Glmark2 and got a score of 10,260, and installed OBS and was excited to see the NVENC hardware encoding worked without any extra setup.

I used OBS to record all the rest of my testing, and it worked without a hitch, allowing the GPU to do all the heavy compression for screen recordings.

Next I booted up SuperTuxKart and got an easy 100 fps with all the settings completely maxed out. I mean, this beat the pants off any other Arm system I've tested so far.

I also installed Blender and messed around with a demo scene. The UI was responsive, and rendering wasn't too painful, but I did notice Blender's CUDA support wasn't working. So the 128-core CPU could keep things moving, but I'm guessing a little more work is required for GPU acceleration.

GPUs are also huge for things like ChatGPT or Llama. And it's easy enough to install Llama locally so I grabbed a massive 13 billion parameter model and installed a web UI. The Ampere chewed through it as I asked a series of questions.

It worked okay, but could be a lot faster if I could get GPU support going. I had a little trouble but again, it's probably not too difficult to get it working, it's just that not many devs working on this software have access to these fast Arm workstations yet.

I mean, even without the GPU, large language models are certainly one way to utilize all 128 cores!

To round things out, I also played back a YouTube video at 4K60 and there was zero issue there. Firefox seems to be using the GPU just fine.

### GPU support in Windows

I rebooted into Windows 11 and things were a lot more bleak there.

{{< figure src="./microsoft-basic-display-adapter.jpg" alt="Microsoft Basic Display Adapter" width="700" height="394" class="insert-image" >}}

The GPU can be seen by Windows, but Nvidia only publishes Arm drivers for Linux, not Windows. So in device manager you just see a Basic Display Adapter, and it can't really do anything.

OBS runs in Windows, but only with software encoding. And Blender won't start at all since it requires OpenGL and a graphics card, neither of which Windows can get going yet on Arm.

## Windows and Cinebench 2024

But Windows _didn't_ have any problems with the CPU or RAM. it picked up on all 128 cores, and all 384 gigs of RAM.

I was excited, because Cinebench just released their latest 2024 version, and one of the headline features is Windows on Arm support!

They mentioned Snapdragon CPUs, like the one that's in the Windows Dev Kit 2023 I tested last year.

I booted up that system and after waiting an hour or so for Windows Update to finish, I ran Cinebench and got 69 single and 435 multicore.

Just for fun, I also ran it on my M1 Max Mac Studio, and got 111 single, and 799 multi.

On the Ampere? 47 single and 2,409 multi!

{{< figure src="./cinebench-2024-scores-arm-cpus.jpg" alt="Cinebench 2024 Arm CPU Scores" width="700" height="394" class="insert-image" >}}

That even beats the [M2 Ultra](https://www.cpu-monkey.com/en/cpu_benchmark-cinebench_2024_multi_core), which gets a maximum of 1,918 on the multicore test.

Now, the M2 Ultra is gimped a little bit: it only has 24 CPU cores.

But I noticed the MP ratio is only 51x on the Ampere. That ratio should be a lot higher, like at least 100 times. What gives?

Well, I opened up Task Manager, and whether I ran the 96-core or 128-core CPU, and even trying the _Enterprise_ edition of Windows on Arm, there was no way to get Cinebench to use more than 64 CPU cores. _Windows_ used all the cores, it was just Cinebench that seemed to have an issue.

If that gets fixed we should be able to go way past 2,400. Maybe around 4,000–but we'll see. I've been in contact with Maxon, and they now have access to some beefier hardware for testing.

So Cinebench is one thing, but something a lot of people mentioned is I could try Minecraft on Windows, since there may be an Arm native version in the Microsoft Store.

### Games: Minecraft on Windows

I installed the Java and Bedrock edition from the Store, and... well... it ran. It wasn't quite playable, and it looks like it's trying to run the game off the tiny ASPEED graphics, which can barely do 10 frames a second.

## Steam on Ampere with Box86 and Box64

But it's an entirely different experience on Linux. I installed Minecraft with Pi-Apps, and it ran beautifully. Zero issues getting 60 fps. I can't get ray tracing on this version, though. It's the one from the Google Play store, and I don't think that edition has RTX support.

Next I also tried installing Steam, and finally have that running! I followed Ampere's guide for installing Steam using Box86 and Box64, though I did have to tweak one install step to get the latest version.

The [main developer of Box86](https://github.com/AmpereComputing/Steam-on-Ampere/issues/11#issuecomment-1732650185) actually has some Ampere hardware to test now, too, and he's already fixed some emulation bugs while I was making this video.

But anyway, with Steam installed, I started downloading all the games, to see what works. I made sure Proton was enabled, then booted up each game.

CS:GO installed and seemed to start launching, but it kept getting stuck in a boot loop where it would just die silently.

Halo Master Chief Collection would launch and eventually get to a black screen, but it died every time with this little Fatal Error message.

Portal 2 did the same thing as Counter Strike, where it would just silently die every time I launched it.

Despite the fact I got Crysis to run at like 1 frame per second on Windows, I couldn't get it to launch at all on Ubuntu.

I tried Quake but got an OpenGL error, and Need for Speed also died. Obduction gave me the same little fatal error Halo did, and Portal 1 also died.

Finally I tried Superhot, and... that actually worked! It was nice and smooth.

Seeing some progress, I downloaded another older game, Horizon Chase Turbo, and got it running decently well, but only like 10 or 20 fps.

My lucky streak was over though as I couldn't get Batman Arkham Knight to launch either, and Doom gave me this weird fatal error about some OpenGL function not being available.

{{< figure src="./ksp-steam.jpg" alt="Kerbal Space Program running on Ampere Altra Max with 4070 Ti" width="700" height="394" class="insert-image" >}}

My luck was back though, once I ran Kerbal Space Program, it seemed to run great and was plenty fast to be enjoyable. Blasting Jeb off in a rocket never gets old.

This stuff is in very active development right now, so things'll change. I highly recommend you follow Box64's development to find out if your favorite games could run on a Dev Workstation yet.

I mean, gaming isn't at all Ampere's main goal here, but it's cool to see how quickly the community's made things work, and I'm glad Ampere and ADLINK have been supportive of getting more stuff running.

## Devkit and what's next

After all that testing on the Workstation, I also set up a bare Dev Kit on my test bench. Ampere sent me a board with a smaller 64-core CPU, and I installed the 96 GB of RAM that I originally bought for the Workstation along with a Kioxia SSD and a Corsair power supply.

And it ran actually a tiny bit more efficient than the full Workstation, putting it squarely at the top of my [top500 efficiency ranking](https://github.com/geerlingguy/top500-benchmark#results), outperforming even the Orange Pi 5!

There are a few quirks to it, though. Like the main fan header isn't actually wired up, so you have to use an adapter to get the CPU fan working. And (like I mentioned earlier) it only exposes 6 of the 8 memory channels, so the highest-end CPUs can't perform to their full potential. Finally, power consumption is about 3W powered off since it runs a built-in BMC for remote access, and booted up it idles around 50W.

But if you use it for anything that needs lots of CPU power and expansion, it's one of the most energy efficient computers on the market.

These things are infinitely more upgradeable than a Mac Pro, while costing less than half as much, and I'm excited to see where ADLINK and Ampere take this platform in the future. This is a good start, and I think they could actually make a dent in areas even outside the workstation space, but we'll see. Right now a lot of focus is on the even _more_ massive [AmpereOne CPUs](https://amperecomputing.com/briefs/ampereone-family-product-brief), with up to _192_ cores, DDR5, and PCIe Gen 5!

This thing can't do media production like my Mac, but for all my dev work, it could definitely be my main computer.
