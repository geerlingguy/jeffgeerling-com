---
nid: 2997
title: "Raspberry Pi Cluster Episode 1 - Introduction to Clusters"
slug: "raspberry-pi-cluster-episode-1-introduction-clusters"
date: 2020-04-29T20:13:44+00:00
drupal:
  nid: 2997
  path: /blog/2020/raspberry-pi-cluster-episode-1-introduction-clusters
  body_format: markdown
  redirects: []
tags:
  - ansible
  - bramble
  - cluster
  - computer
  - kubernetes
  - pi dramble
  - raspberry pi
  - turing pi
  - video
  - youtube
---

> I will be posting a few videos discussing cluster computing with the Raspberry Pi in the next few weeks, and I'm going to post the video + transcript to my blog so you can follow along even if you don't enjoy sitting through a video :)

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/kgVz4-SEhbE" frameborder='0' allowfullscreen></iframe></div>

This is a [Raspberry Pi Compute Module](https://www.raspberrypi.org/products/compute-module-3-plus/).

{{< figure src="./pi-7-compute-module-stack.jpeg" alt="7 Raspberry Pi Compute Modules in a stack" width="455" height="380" class="insert-image" >}}

And this is a stack of _7_ Raspberry Pi Compute Modules.

It's the same thing as a [Raspberry Pi model B](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/), but it drops all the IO ports to make for a more flexible form factor, which the Rasbperry Pi Foundation says is "suitable for industrial applications". But in my case, I'm interested in using it to build a cluster of Raspberry Pis.

I'm going to explore the concept of cluster computing using Raspberry Pis, and I'm excited to be in posession of a game-changing Raspberry-Pi based cluster board, the [Turing Pi](https://turingpi.com).

{{< figure src="./turing-pi-hero.jpeg" alt="Turing Pi" width="650" height="433" class="insert-image" >}}

I'll get to the Turing Pi soon, but in this first episode, I wanted to cover why I love using Raspberry Pis for clusters.

But first, what _is_ a cluster?

## Cluster Computing

A lot of people try to solve complex problems with computers. Sometimes they do things like serve a web page to a huge amount of visitors. This requires lots of bandwidth, and lots of 'backend' computers to handle each of the millions of requests. Some people, like weather forecasters, need to find the results of billions of small calculations.

There are two ways to speed up these kinds of operations:

  1. By scaling _vertically_, where you have a single server, and you put in a faster CPU, more RAM, and faster connections.
  2. By scaling _horizontally_, where you split up the tasks and use multiple computers.

{{< figure src="./cray-supercomputer.jpg" alt="Cray Supercomputer" width="650" height="434" class="insert-image" >}}

Early on, systems like [Cray supercomputers](https://en.wikipedia.org/wiki/Cray) took _vertical_ scaling to the extreme. One massive computer that cost millions of dollars was the fastest computer for a time. But this approach has some limits, and having everything invested in one machine means downtime when it needs maintenance, and limited (often painfully expensive) upgrades.

In most cases, it's more affordable—and sometimes, the only way possible—to scale horizontally, using many computers to handle large calculations or lots of web traffic.

Clustering has become easier with the advent of [Beowulf-style clusters](https://en.wikipedia.org/wiki/Beowulf_cluster) in the 90s and newer software like [Kubernetes](https://kubernetes.io), which seamlessly distributes applications across many computers, instead of manually placing applications on different computers.

Even with this software, there are two big problems with scaling horizontally—especially if you're on a budget:

  1. Each computer costs a bit of money, and requires individual power and networking. For a few computers this isn't a big problem, but when you start having five or more computers, it's hard to keep things tidy and cool.
  2. Managing the computers, or 'nodes' in cluster parlance, is easy when there are one or two. But scaled up to five or ten, even doing simple things like rebooting servers or kicking off a new job requires software to coordinate everything.

## The Raspberry Pi Dramble

In 2015, I decided to set up my first 'bramble'. A bramble is a cluster of Raspberry Pi servers. "Why is it called a bramble?" you may ask? Well, because a natural cluster of raspberries that you could eat is called a 'bramble'.

{{< figure src="./bramble-raspberries.jpeg" alt="Bramble of Raspberries" width="650" height="366" class="insert-image" >}}

So I started building a bramble using software called [Ansible](https://www.ansible.com) to install a common software stack across the servers to run [Drupal](https://www.drupal.org). I set up Linux, Apache, MySQL, and PHP, which is commonly known as the ['LAMP' stack](https://en.wikipedia.org/wiki/LAMP_(software_bundle)).

Since my bramble ran Drupal, I made up the portmanteau 'dramble', and thus the [Raspberry Pi Dramble](https://www.pidramble.com) was born.

{{< figure src="./dramble-original.jpeg" alt="Raspberry Pi Dramble - original 6-node cluster" width="650" height="431" class="insert-image" >}}

The first version of the cluster had six nodes, and I had a bunch of micro USB cables plugged into a USB power adapter, plus a bunch of Ethernet cables plugged into an 8 port ethernet switch.

When the Raspberry Pi model 3 came out, I trimmed it down to 5 nodes.

Then, when the [Raspberry Pi Zero](https://www.raspberrypi.org/products/raspberry-pi-zero/) was introduced, which is the size of a stick of bubble gum, I bought five of them and made a tiny cluster using [USB WiFi adapters](https://www.amazon.com/Plugable-Wireless-802-11n-Network-RTL8188EUS/dp/B00H28H8DU/ref=as_li_ss_tl?ac_md=1-0-VW5kZXIgJDk=-ac_d_pm&cv_ct_cx=wifi+usb&dchild=1&keywords=wifi+usb&pd_rd_i=B00H28H8DU&pd_rd_r=85325388-a011-440b-93fa-9009f4c6b111&pd_rd_w=vUkbx&pd_rd_wg=Dprjw&pf_rd_p=4ad7736a-c9f7-4bcd-8a16-bd943c26821c&pf_rd_r=8EPRNND3GNCG8HY8WJ7T&psc=1&qid=1588190059&sr=1-1-22d05c05-1231-4126-b7c4-3e7a9c0027d0&linkCode=ll1&tag=mmjjg-20&linkId=16bec3c91bdc8b344dafb73125b1faaf&language=en_US), but realized quickly the old processor on the Zero was extremely underpowered, and I gave up on that cluster.

{{< figure src="./pi-zero-dramble-mini.jpeg" alt="Raspberry Pi Dramble - mini Pi Zero cluster" width="650" height="431" class="insert-image" >}}

In 2017, I decided to start using Kubernetes to manage Drupal and the LAMP stack, though I still used Ansible to configure the individual Pis and get Kubernetes installed on them.

And today's Dramble, which is made up of four Raspberry Pi model 4 boards, uses the official [Power-over-Ethernet (PoE) board](https://www.raspberrypi.org/products/poe-hat/), which allowed me to drop the tangle of USB power cables, but requires a more expensive [PoE switch](https://www.amazon.com/NETGEAR-Gigabit-Ethernet-Unmanaged-Desktop/dp/B01MRO4M73/ref=as_li_ss_tl?dchild=1&keywords=poe+switch&qid=1588190113&sr=8-5&linkCode=ll1&tag=mmjjg-20&linkId=2e43c4da9f4aca7a7834cb0bcce3fb8d&language=en_US).

{{< figure src="./dramble-version-4-poe.jpeg" alt="Raspberry Pi Dramble - 2020 version with PoE and Pi 4" width="650" height="452" class="insert-image" >}}

The Pi Dramble isn't all serious, though. I've had some fun with it, including making a homage to an old movie I enjoyed:

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/yF63TnaZfaY" frameborder='0' allowfullscreen></iframe></div>

Through this whole experience, I've documented every aspect of the build, including all the Ansible playbooks, as an [open source project](https://github.com/geerlingguy/raspberry-pi-dramble) that's linked from [pidramble.com](https://www.pidramble.com), and many others have followed these plans and built the Pi Dramble on their own!

## Why Raspberry Pi?

This is all to say, I've spent a lot of time managing a cluster of Raspberry Pis, and the first question I'm usually asked is "why did you choose Raspberry Pis for your cluster?"

That's very good question.

An individual Raspberry Pi is not as fast as most modern computers. And it has limited RAM (even the latest Pi model 4 has, at most, 4 GB of RAM). And it's not great for speedy or reliable disk access, either.

It's slightly more cost-effective and usually more power-efficient to build or buy a small [NUC ("Next Unit of Computing") machine](https://www.amazon.com/NUC8i7BEH-Quad-Core-i7-8559U-Bluetooth-Thunderbolt/dp/B07JJPF8MV/ref=as_li_ss_tl?dchild=1&keywords=intel+nuc&qid=1588190190&sr=8-3&linkCode=ll1&tag=mmjjg-20&linkId=dad12aada92ebb24d4a6f2ae9636f4d0&language=en_US) that has more raw CPU performance, more RAM, a fast SSD, and more expansion capabilities.

But is building some VMs to simulate a cluster on an NUC fun?

I would say, "No." Well, not as much as building a cluster of Raspberry Pis!

And managing 'bare metal' servers instead of virtual machines also requires more discipline for provisioning, networking, and orchestration. Those three skills are very helpful in many modern IT jobs!

Also, while you may want to optimize for pure performance, there are times, like when building Kubernetes clusters, where you want to optimize for CPU core count. If you wanted to build a single computer with 32 CPU cores, you might consider the [AMD ThreadRipper 3970x](https://www.amazon.com/AMD-Ryzen-Threadripper-3970X-64-Thread/dp/B0815JJQQ8/ref=as_li_ss_tl?dchild=1&keywords=3970x&qid=1588190227&sr=8-1&linkCode=ll1&tag=mmjjg-20&linkId=db25aa9793bf35f29e196f8f26107ae9&language=en_US), which has 32 cores. Problem is, the processor costs nearly $2,000, and that's just the processor—the rest of the computer's components would put you past $3,000 total for this rig.

{{< figure src="./cpu-core-comparison.jpg" alt="CPU core comparison - ThreadRipper and Pi Compute Module 3+" width="650" height="366" class="insert-image" >}}

For the Raspberry Pi, each compute board has a 4-core CPU, and putting together 7 Pis nets you 28 cores. Almost the same number of cores, but costs less than $300 total. Even with the added cost of a Turing Pi and a power supply, that's the same number of CPU cores for 1/4 the cost!

> Yes, I know 1 ThreadRipper core ≠ 1 Pi CM core; but in many K8s applications, a core is a core, and the more the merrier. Not all operations are CPU-bound and would benefit from having 4-8x faster raw throughput, or the many other little niceties the ThreadRipper offers (like more cache).

Finally, one of the most important lessons I learn working with Arduinos and Raspberry Pis is this: working with resource constraints like limited RAM or slow IO highlights inefficiencies in your code, in a way you'd never notice if you always build and work on the latest Core i9 or ThreadRipper CPU with gobs of RAM and 100s of thousands of IOPS!

If you can't get something to run well on a Raspberry Pi, consider this: many smartphones and low-end computers have similar constraints, and people using these devices would have the same kind of experience.

Additionally, even on fast cloud computing instances, you'll run into network and IO bottlenecks from time to time, and if your application fails in those situations, you could be in for a world of pain. Getting them to run on a Raspberry Pi can help you identify these problems quickly.

## Why Turing Pi?

So, getting back to the Turing Pi: what makes this better than a cluster of standard Raspberry Pis, like the Pi Dramble?

{{< figure src="./jeff-turing-pi-surprise.jpeg" alt="Jeff Geerling acts surprised for a YouTube thumbnail pic, while holding a Turing Pi" width="650" height="433" class="insert-image" >}}

Well, [subscribe to my YouTube channel](https://www.youtube.com/c/JeffGeerling)—I'll explore what makes the Turing Pi tick and how to set up a new cluster in my next video! If you liked this content and want to see more, consider supporting me on [GitHub](https://github.com/sponsors/geerlingguy) or [Patreon](https://www.patreon.com/geerlingguy).
