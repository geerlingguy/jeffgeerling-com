---
nid: 3123
title: "Why build a Raspberry Pi Cluster?"
slug: "why-build-raspberry-pi-cluster"
date: 2021-08-11T14:04:25+00:00
drupal:
  nid: 3123
  path: /blog/2021/why-build-raspberry-pi-cluster
  body_format: markdown
  redirects: []
tags:
  - cluster
  - computing
  - kubernetes
  - raspberry pi
  - video
  - youtube
---

{{< figure src="./pi-cluster-banana.jpeg" alt="Raspberry Pi Cluster next to a banana for scale" width="660" height="438" class="insert-image" >}}

After I posted my Raspberry Pi Blade server video last week, lots of commenters asked what you'd do with a Pi cluster. Many asked out of curiosity, while others seemed to shudder at the _very idea of a Pi cluster_, because _obviously_ a cheap PC would perform better... right?

Before we go any further, I'd say probably 90 percent of my readers _shouldn't_ build a Pi cluster.

But some of you should. _Why?_

Well, the first thing I have to clear up is what a Pi cluster _isn't_.

> Note: This blog post corresponds to my YouTube video of the same name: [Why would you build a Raspberry Pi Cluster?](https://www.youtube.com/watch?v=8zXG4ySy1m8). Go watch the video on YouTube if you'd rather watch the video instead of reading this post!

## What a Pi cluster CAN'T do

Some people think when you put together two computers in a cluster, let's say both of them having 4 CPU cores and 8 gigs of RAM, you end up with the ability to use 8 CPU cores and 16 gigs of RAM.

{{< figure src="./cluster-not-8-cores-16-gb-ram.jpg" alt="Cluster is not just lumping together all cores and RAM from all computers" width="661" height="355" class="insert-image" >}}

Well, that's not really the case. You still have two separate 4-core CPUs, and two separately-addressable 8 gig portions of RAM.

Storage can sometimes be aggregated in a cluster, to a degree, but even there, you suffer a performance penalty and the complexity is _much_ higher over just having one server with a lot more hard drives.

So that's not what a cluster is.

Instead, a cluster is a group of similar computers—or even in some cases, wildly different computers—that can be coordinated through some sort of cluster management to perform certain tasks.

The key here is that tasks must be split up to work on members of the cluster. Some software will work well in parallel. But there's other software, like games, that can only address one GPU and one CPU at a time. Throwing Flight Simulator at a giant cluster of computers isn't gonna make it any faster. Software like that simply won't run on _any_ Pi cluster, no matter how big.

## What a Pi cluster CAN do

Luckily, there's a LOT of software that _does_ run well in smaller chunks, in parallel.

{{< figure src="./pi-homelab-rack.jpeg" alt="Raspberry Pi Homelab Rack" width="600" height="400" class="insert-image" >}}

For example, right now in my little home cluster—which I'm still building out—I'm running Prometheus and Grafana on one Pi, monitoring my Internet connection, indoor air quality, and household power consumption. That Pi's also running [Pi-hole](https://pi-hole.net) for custom DNS and to prevent ad tracking on my home network.

This next Pi runs Docker and serves the website [PiDramble.com](http://www.pidramble.com).

And the next one manages backups for my entire digital life, backing up everything offsite on Amazon Glacier. (I'll be exploring my backup strategy in-depth and sharing my open source backup configuration later this year.)

I also have another set of Pis that typically runs Kubernetes (and hosts PiDramble.com, among other sites), but I'm rebuilding that cluster right now, so the other sites are running on a DigitalOcean VPS.

But there's tons of other software that runs great on Pis. Pretty much any application that can be compiled for ARM processors will run on the Pi. And that includes most things you'd run on servers these days, thanks to Apple adopting ARM with the new M1 Macs, and Amazon using Graviton instances in their cloud.

I'm considering hosting NextCloud and Bitwarden soon, to help reduce my dependence on cloud services and for better password management. And many people run things like Home Assistant on Pis to manage home automation, and there are thousands of different Pi-based automation solutions for home and industry.

## But why a cluster?

But before we get to specifically why some people build _Pi_ clusters, let's first talk about clusters in general.

Why would anyone want build a cluster of _any_ type of computer? I already mentioned you don't just get to lump together all the resources. A cluster with ten AMD CPUs and ten RTX 3080s can't magically [play Crysis at 8K](https://www.youtube.com/watch?v=JE_3VJD8jk0) at 500 fps.

Well, there are actually a number of reasons, but the two I'm usually concerned with are **uptime** and **scalability**.

For software _other_ than games, you can usually design it so it scales up and down by splitting up tasks into one or more application instances. Take a web server for instance. If you have one web server, you can scale it up until you can't fit more RAM in the computer or a faster CPU.

But if you can run multiple instances, you could have one, ten, or a hundred 'workers' running that handle requests, and each worker could take as much or as little resources as it needs. So you could, in fact, get the performance of ten AMD CPUs split up across ten computers, but in aggregate.

Not everything scales that easily, but even so, another common reason for clustering is uptime, or reliability. Computers die. There are two types of people in the world: people who have had a computer die on them, and people who will have a computer die on them.

And not just complete failure, computers sometimes do weird things, like the disk access gets slow. Or it starts erroring out a couple times a day. Or the network goes from a gigabit to 100 megabits for seemingly no reason.

If you have just one computer, you're putting all your eggs in one basket. In the clustering world, we call these servers "snowflakes". They're precious to you, unique and irreplacable. You might even name them! But the problem is, all computers need to be replaced someday.

And life is a lot less stressful if you can lose one, two, or even ten servers, while your applications still run happy as can be—because you're running them on a cluster.

Having multiple Pis running my apps—and having good backups and automation to manage them—means when a microSD card fails, or a Pi blows up, I toss it out can have a spare running in minutes.

## But why a Pi Cluster?

But that doesn't answer the question why someone would run _Raspberry Pis_ in their cluster.

A lot of people questioned whether a 64-core ARM cluster built with Raspberry Pis could compete with a single 64-core AMD CPU. And, well, that's not a simple question.

First I have to ask: _what are you comparing?_

{{< figure src="./threadripper-5500-dollars.jpg" alt="Threadripper 64-core CPU for five thousand dollars" width="600" height="258" class="insert-image" >}}

If we're talking about price, are we talking about [64-core AMD CPUs](https://amzn.to/3AymNst) that _alone_ cost $6,000 dollars? Because that's _certainly_ more expensive than buying 16 Raspberry Pis _with all the associated hardware_ for around $3,000, all-in.

If we're talking about power efficiency, that's even _more_ tricky.

Are we talking about idle power consumption? Assuming the worst case, with PoE+ power to each Pi, 16 Pis would total about 100W of power consumption, all-in.

According to [Serve The Home's testing](https://www.servethehome.com/amd-epyc-7742-benchmarks-and-review-simply-peerless/), the AMD EPYC 7742 uses a minimum of 120 Watts—and that's _just the CPU_.

Now, if you're talking about running something like crypto mining, 3D rendering, or some other task that's going to try to use as much CPU and GPU power as possible, constantly, that's an entirely different equation.

The Pi's performance per watt is okay, but it's no match for a 64-core AMD EPYC running full blast.

Total energy consumption would be higher—400+ W compared to 200W for the entire Pi cluster full-tilt—but you'll get a lot more work out of that EPYC chip on a per-Watt basis, meaning you could compute more things, faster.

But there are a LOT of applications in the world that don't need full-throttle 24x7. And for those applications, unless you need frequent bursty performance, it _could_ be more cost-effective to run on lower power CPUs like the ones in the Pi.

## Performance isn't everything

But a lot of people get hung up on performance. It's not the be-all and end-all of computing.

I've built at least five versions of my Pi cluster. I've learned a LOT. I've learned about Linux networking. I've learned about Power over Ethernet. I've learned about the physical layer of the network. I've learned how to compile software. I've learned how to use Ansible for bare metal configuration and network management.

These are things that I may have learned to some degree from other activities, or by building virtual machines one one bigger computer. But I wouldn't know them _intimately_. And I wouldn't have had as much _fun_, since building physical clusters is so hands-on.

So for many people, myself included, I do it mostly for the educational value.

Even still, some people say it's more economical to build a cluster of old laptops or PCs you may have laying around. Well, I don't have any laying around, and even if I did, unless you have pretty new PCs, the performance per watt from a Pi 4 is actually pretty competitive with a 5 to 10 year old PC, and they take up a LOT less space too.

And besides, the Pis typically run silent, or nearly so, and don't act like a space heater all day, like a pile of older Intel laptops.

## Enterprise use cases

But there's one other class of users that might surprise you: enterprise!

Some people need ARM servers to integrate into their Continuous Integration or testing systems, so they can build and test software on ARM processors. And it's a lot cheaper to do it on a Pi than on a Mac mini or an expensive Ampere computer, if you don't need the raw performance.

And some enterprises need an on-premise ARM cluster to run things like they would on AWS Graviton, or to test things out for industrial automation, where there are tons of Pis and other ARM processors in use.

Finally, some companies integrate Pis into larger clusters, as small low-power ARM nodes to run software that doesn't need bleeding-edge performance.

## But there's no ECC RAM!

Another sentiment I see a lot is that it's "too bad the Pi doesn't have ECC RAM."

Well, the Pi _technically does_ have ECC RAM! Check the [product brief](https://datasheets.raspberrypi.org/rpi4/raspberry-pi-4-product-brief.pdf)! The Micron LPDDR4 RAM the Pi uses technically has on-die ECC.

I'd say half the people who complain about a lack of ECC couldn't explain specifically how it would help their application run better.

But it _is_ good to have for many types of software. And the Pi has it... or does it? Well, no—at least not in the same way high-end servers do. On-die ECC can prevent memory access errors in the RAM itself, but it doesn't seem to be integrated with the Pi's System on a Chip, so the error correction is minimal compared to what you'd get if you spent tons of money on a beefy server with ECC integated through the whole system.

## Conclusion

So anyways, those are my thoughts on what you could do with a cluster of Raspberry Pis. I'm sure people will find a lot to nitpick, and that's perfectly fine.

Some people don't see the value or the fun in building clusters, just like some people couldn't fathom why someone would want to build their own chair out of wood using hand tools, when you can just buy a functional chair from Ikea or any furniture store.

But I will continue building and rebuilding Pi clusters (and clusters in AWS, and clusters on my Mac using VMs, and other types of clusters too!), and will continue enjoying the experience and learning process. What are some other things you've seen people do with Pi clusters? And have you built your own cluster of computers before, Raspberry Pi or anything else? I'd love to see your examples in the comments.
