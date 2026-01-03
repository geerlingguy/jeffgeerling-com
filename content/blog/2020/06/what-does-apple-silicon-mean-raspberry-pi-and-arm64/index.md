---
nid: 3023
title: "What does Apple Silicon mean for the Raspberry Pi and ARM64?"
slug: "what-does-apple-silicon-mean-raspberry-pi-and-arm64"
date: 2020-06-25T21:12:32+00:00
drupal:
  nid: 3023
  path: /blog/2020/what-does-apple-silicon-mean-raspberry-pi-and-arm64
  body_format: markdown
  redirects: []
tags:
  - apple
  - arm64
  - cpu
  - intel
  - mac
  - raspberry pi
  - silicon
  - x86
---

> Note: There's a video version of this blog post available here: [What does Apple Silicon mean for the Raspberry Pi and ARM64?](https://www.youtube.com/watch?v=DMUofMagmfc)

<p style="text-align: center;"><a href="https://www.youtube.com/watch?v=DMUofMagmfc">{{< figure src="./Apple-Silicon-Raspberry-Pi-Thumbnail.jpg" alt="Apple Silicon and the Raspberry Pi" width="600" height="338" class="insert-image" >}}</a></p>

A couple weeks ago I tried using the latest Raspberry Pi 4 8 gig model as my main computer for a day, and I [posted a video about my experience](https://www.youtube.com/watch?v=OU6jHvVqJxY).

Besides many diehard Linux fans complaining in the comments about my apparent idiocy caused by being a Mac user, the experience taught me one thing: A lot of software still isn't built for 64-bit ARM processors, or even for Linux in general.

But there's one trend that I'm seeing: most of the open source software I use already works great on a Pi 4 running on its 64-bit ARM processor.

In my testing, I used the latest [64-bit Pi OS beta](https://www.raspberrypi.org/forums/viewtopic.php?t=275370), and I think the Pi Foundation had excellent timing releasing it this year, since many more applications can run on a 64-bit architecture nowadays, and because the newest Pi 4 models have much more RAM to take advantage of the architecture.

I could run the LAMP stack, Docker, Kubernetes, GitLab, Drupal, Wordpress, Minecraft, and almost all the Docker images I normally run on my Mac and in production.

For some things, I had to recompile or build my own Docker image, but most things are actually already built for ARM64, and I noticed I didn't have to spend as much time compiling things myself.

Earlier this week, [Apple announced 'Apple Silicon'](https://www.apple.com/newsroom/2020/06/apple-announces-mac-transition-to-apple-silicon/), which is marketing speak for 'Apple's ditching Intel x86 CPUs and will use 64-bit ARM processors in Macs'.

And they dedicated a whopping _17 seconds_ (sarcasm: noted) of the [WWDC 2020 keynote](https://www.youtube.com/watch?v=GEZhD3J89ZE) highlighting "new virtualization technologies" on the Mac.

<p style="text-align: center;"><a href="https://www.youtube.com/watch?v=GEZhD3J89ZE">{{< figure src="./virtualization-macos-big-sur-silicon-arm64.jpg" alt="Virtualized Docker and Debian VM environments on macOS Big Sur" width="600" height="338" class="insert-image" >}}</a></p>

What does this mean for the Pi and other inexpensive single-board computers? I think this is great news. And listening to [Daring Fireball's podcast interview with Craig Federighi](https://www.youtube.com/watch?v=Hg9F1Qjv3iU), there was even more interesting news:

<p style="text-align: center;"><a href="https://www.youtube.com/watch?v=Hg9F1Qjv3iU">{{< figure src="./craig-federighi-podcast-virtualization-apple-silicon.jpg" alt="Craig Federighi on Daring Fireball podcast talks ARM64 virtualization with Apple Silicon" width="600" height="338" class="insert-image" >}}</a></p>

Craig mentioned that the virtualization on the new Macs won't support X86 at all. He even explicitly called out Docker containers being built for ARM, and being able to run them on ARM instances in AWS.

I'm not going to discuss the [lack of Windows support or Boot Camp](https://www.theverge.com/2020/6/24/21302213/apple-silicon-mac-arm-windows-support-boot-camp) on the new Macs since that's only tangentially related, but I do think there's one very positive implication: as Apple moves off of the X86 platform to 64-bit ARM, more and more organizations and developers will see the importance of building [multi-arch Docker images](https://www.docker.com/blog/multi-arch-build-and-images-the-simple-way/), and also making sure their software compiles on ARM processors like the ones in the Pi.

Like I said earlier, there is already some good momentum in that area. What I think is going to happen is that momentum will start turning into a full-on freight train, and we're going to see the default for most software being "it runs on ARM and X86" instead of the current status quo, which is "it runs on X86, and might run on ARM but it's not really supported that way."

Even if many developers like me decide to jump ship off Apple's platform after macOS 11 is released, there's enough momentum in the Apple ecosystem, and in the computing world in general, to really push the ARM transition forward.

I feel like Apple's announcement at WWDC echoes earlier major changes, like dropping floppy drive support in the first iMac, adopting USB when most of the industry still used serial ports, or abandoning Adobe Flash before it was the 'cool' thing to do.

Microsoft has been trying to diversify into the ARM ecosystem for a while now (e.g. the [Surface Pro X](https://www.microsoft.com/en-us/p/surface-pro-x/8vdnrp2m6hhc?activetab=processor)), but their Windows app support for ARM has been lackluster since they have never really forced developers to support it or even come up with a solid transition plan.

Maybe with Apple's announcement this week, the small amount of momentum ARM has had during the 2010s will turn into a landslide, and we'll see the architecture duke it out with X86 for the next decade, especially because of how important mobile, power-efficient, and edge computing are today!

If you liked this post, you might also be interested in my [Raspberry Pi Cluster series featuring the Turing Pi](https://www.youtube.com/watch?v=kgVz4-SEhbE).
