---
nid: 3331
title: "Pi clusters aren't dumb"
slug: "pi-clusters-arent-dumb"
date: 2023-12-01T15:58:55+00:00
drupal:
  nid: 3331
  path: /blog/2023/pi-clusters-arent-dumb
  body_format: markdown
  redirects: []
tags: []
---

...and the [video I just posted on the Mars 400](https://www.youtube.com/watch?v=v56JNYCk11E) explores the topic a bit more.

{{< figure src="./mars-400-deskpi-super6c-turing-pi-4.jpg" alt="Mars 400 DeskPi Super6c and Turing Pi 2 CM4 Raspberry Pi clusters" width="700" height="auto" class="insert-image" >}}

But every time I've posted a video, blog post, tweet (_xeet?_), or anything else on the topic of Pi clusters, a common sentiment is "you can do that faster and cheaper with a set of VMs."

Or, during the Pi shortage (which is [basically over](https://rpilocator.com)), when you could only buy Pis from scalpers for insane markups, the sentiment was "you can do that faster and for the same price with a bunch of used mini PCs."

Luckily, with Compute Modules coming back into general availability at MSRP, and Pi 4s being available at most local retailers as well (at least here in the US?), building hobby clusters of 3, 4, or 6 Raspberry Pis is achievable again, for a few hundred bucks, all-in.

As I've [said before](/blog/2021/why-build-raspberry-pi-cluster), Pi clusters aren't going to rip through HPC tasks. A beefy Pi cluster can't even come close to the raw performance of a single socket Threadripper or Ampere Altra system (much less any modern desktop). And that's true even if you use more expensive Pi 5s.

But I still love building them for four reasons:

  1. Lack of noise
  2. Compact size
  3. Power efficiency
  4. Fun

On that third point, there _are_ other Arm boards with even better power efficiency, like the Rock 5 B, or Orange Pi 5. But for an equivalent model, you wind up spending 2-3x more than the Pi (at MSRP, that is... this was a different argument earlier this year).

But as someone who has run thousands of servers in production (Kubernetes, cloud-hosted clusters, bare metal...), the ability to have a lab cluster, with _real_ hardware, and _real_ network connections, sitting next to me _on my desk_, has been helpful.

There are issues in networking, power, and performance you don't encounter if you're always sitting in front of a cloud dashboard, or running a set of VMs on your beefy workstation (where networking is basically 'free', and fast NVMe SSDs will burn through any poorly-written code that hits disk).

For my career, having the knowledge and skills to automate and built out software-defined networking, find performance bottlenecks, and even diagnose physical cabling and power issues, has been invaluable.

> Note: Well... now I do writing and YouTube, and don't manage thousands of servers... my own inventory is down to about 15 prod servers. So take that as you will.

It's also _fun_.

And sometimes, when you're working in production in stressful situations, having a way to explore things in a low-stress environment. If you accidentally blow up a Pi 4 doing strange things with it... it's a lot less depressing when replacing it is only $35.

{{< figure src="./raspberry-pi-4-broken.jpeg" alt="Raspberry Pi 4 broken" width="700" height="auto" class="insert-image" >}}

Plus it encourages more risk-taking, and doing wild things. You quickly learn where bottlenecks lie, and whether that's CPU, memory, disk, or network—all of which can be massive issues in cloud environments!—you'll also learn hacks to overcome these issues, or in some cases, you can uncover and fix bugs in your own software that cause them!

One time, I spent a little time fixing a bug that could cause my local Pi cluster to bog down to a few requests per second—it was a filesystem lookup that was hitting on every page request (even cached). Fixing that on my Pi cluster, where it was excruciatingly obvious, meant that after deploying it to my cloud environment, I wound up with about 10% faster page requests.

And that might not seem like much, but under heavy load, it could be the difference between some visitors hitting error pages, or the site being able to cope.
