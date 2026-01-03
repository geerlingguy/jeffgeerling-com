---
nid: 3030
title: "Raspberry Pi Cluster Episode 6 - Turing Pi Review"
slug: "raspberry-pi-cluster-episode-6-turing-pi-review"
date: 2020-07-30T15:27:41+00:00
drupal:
  nid: 3030
  path: /blog/2020/raspberry-pi-cluster-episode-6-turing-pi-review
  body_format: markdown
  redirects: []
tags:
  - cluster
  - k3s
  - kubernetes
  - raspberry pi
  - turing pi
  - video
  - youtube
---

A few months ago, in the 'before times', I noticed [this post](https://news.ycombinator.com/item?id=22677965) on Hacker News mentioning the [Turing Pi](https://turingpi.com/), a 'Plug & Play Raspberry Pi Cluster' that sits on your desk.

It caught my attention because I've been running my own old-fashioned ['Raspberry Pi Dramble'](https://www.pidramble.com) cluster since 2015.

{{< figure src="./pi-dramble-cluster-2019-edition.jpeg" alt="Raspberry Pi Dramble Cluster with Sticker - 2019 PoE Edition" width="600" height="416" class="insert-image" >}}

So today, I'm wrapping up my [Raspberry Pi Cluster series](https://www.youtube.com/playlist?list=PL2_OBreMn7Frk57NLmLheAaSSpJLLL90G) with my thoughts about the Turing Pi that I used to build a 7-node Kubernetes cluster.

## Video version of this post

This blog post has a companion video embedded below:

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/aApByQWqnV0" frameborder='0' allowfullscreen></iframe></div>

## Getting a Turing Pi

Since 2015, my Pi cluster has gotten better every year. But managing the cabling and physical mounting for the cluster is annoying, even though I'm using the PoE HAT now to reduce the cabling down to one network cable per Pi.

So when I saw the Turing Pi, and it's promise of easy integration with [Compute Modules](https://www.raspberrypi.org/products/compute-module-3-plus/), I considered placing a pre-order.

A couple weeks later I got an email from one of Turing Machines' co-founders, asking if I'd seen the board before. I said, "yes I have, it looks really neat! Do you think you could send me one to try out?"

{{< figure src="./turing-pi-with-compute-modules.jpeg" alt="Turing Pi with 7 Raspberry Pi Compute Modules" width="600" height="400" class="insert-image" >}}

Well, he responded with an offer I couldn't refuse—he sent me a prototype board, the Turing Pi 1.1, along with 7 Compute modules, and told me to have some fun with it. And so I did, and in the course of testing it out, I posted a series of videos, showing everyone how I installed [K3s](https://k3s.io) on the cluster, then I installed Minecraft server and proceeded to [dig straight down](https://knowyourmeme.com/memes/never-dig-straight-down).

Recently Turing Machines started producing a ['big batch' of boards](https://twitter.com/turingpi/status/1286666676382171136), and they'll be shipping all the pre-orders over the next few weeks. I thought it would be a good time to post my full review of the Turing Pi, after using it for a couple months.

## Why Pi?

So let's get this question out of the way first, since it's a pretty polarizing topic:

Why cluster a bunch of Raspberry Pis together?

{{< figure src="./why-u-cluster-raspberry-pis-meme.jpeg" alt="Why U Cluster Raspberry Pis Meme" width="500" height="500" class="insert-image" >}}

Isn't it more cost-effective and even more power efficient to build or buy a small [NUC](https://www.intel.com/content/www/us/en/products/boards-kits/nuc.html) or a cheap old laptop? Wouldn't that perform better, especially since you can use a proper SSD, and have more expansion options?

Well... yes, it would.

But is building some VMs on an NUC fun?

{{< figure src="./banana-pi-zeros-face.jpeg" alt="Raspberry Pi Zero Banana Smile Face" width="600" height="419" class="insert-image" >}}

No—not as much as a little cluster of Raspberry Pis, at least.

And while the Pi is no speed demon, it's not a slouch either. In [episode 5](/blog/2020/raspberry-pi-cluster-episode-5-benchmarking-turing-pi), I compared the performance of the Pi 3+ and Pi 4. Neither Pi CPU could be crowned king over all other processors, but they can do most tasks without much pain.

{{< figure src="./turing-pi-less-than-light-energy-consumption.jpg" alt="Turing Pi uses less than half the energy of a 60w light bulb" width="600" height="338" class="insert-image" >}}

And there are some use cases, like energy-efficient clustering (assuming you don't run at 100% CPU utilization all the time), where the Pi does actually have a leg up. You can run a cluster of Pis with 28 CPU cores and no fan with _less than half_ the energy required to run a 60-watt light bulb. Try doing _that_ with any modern Intel CPU!

## What's Wrong with a Model B cluster?

And if you look at the [benchmarks from the previous episode](/blog/2020/raspberry-pi-cluster-episode-5-benchmarking-turing-pi), you might notice the Pi 4 is more than twice as fast as the Compute Module 3 B+ in many ways, so why shouldn't you build a Pi 4 cluster instead of a Turing Pi cluster?

Well, for many people, it's a great option. If you want to build a more traditional cluster built on the Pi 4 model B, I have a [parts list](http://www.pidramble.com/wiki/hardware/pis) and an exhaustive guide on my [Raspberry Pi Dramble Wiki](http://www.pidramble.com/wiki).

But the Turing Pi is built in a way that makes building a Pi cluster a lot easier. I took the Pi over to my workbench so I could take a deeper look at the Turing Pi's hardware.

## Turing Pi Hardware

{{< figure src="./turing-pi-in-case-mini-itx.jpeg" alt="Turing Pi in Mini ITX case" width="600" height="458" class="insert-image" >}}

The Turing Pi fits in any Mini ITX case (I'm using [this case](https://www.amazon.com/gp/product/B07T2HKWZN/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=9f6003fac5310ecbd2763cf6ab8f4ef2&language=en_US) in the picture above), and there are two ways to power the board, either through a standard 12 volt barrel plug power supply, or a 4-pin ATX power connector.

It also has a built-in gigabit network backplane, so you don't have to use a separate network switch.

The 'master' node is the top slot, and you can use it as a management node, since it has an attached full-size HDMI port and two USB 2.0 ports. You control the entire cluster from it, no other computer required.

And each compute module gets its own 40-pin GPIO header—though the prototype board I used only had four GPIO pins. But the final board has full 40-pin headers for each Pi, so you can integrate Pi HATs for many different projects inside one small package.

{{< figure src="./turing-pi-vs-pi-dramble-raspberry-pi-cluster.jpg" alt="Turing Pi vs Raspberry Pi Dramble Cluster" width="600" height="338" class="insert-image" >}}

The Turing Pi also allows hot-swapping the Pis. So if you want to replace one, or add a new Pi, you don't have to power down the cluster to do it. With my Pi Dramble, hot swapping is a long and delicate process, because I'd have to unmount all the Pis on top of the one I want to swap out.

And since the Turing Pi uses DDR2 SODIMM slots for the Compute Module, it's compatible with all the versions of the Compute Module, from the original model to the newer Compute Module 3 or 3+.

The Turing Pi also includes a ['cluster management bus'](https://docs.turingpi.com/turing_pi/children/i2c_cluster_bus/). If you enable the master node's I2C interface, you can manage a number of hardware-level options for each Compute Module:

  - You can manage the onboard network backplane
  - You can power on and off individual Compute Modules
  - You can configure the onboard real time clock (which has battery backup)

The Turing Pi also has flexibility for boot options: each of the seven slots gets a microSD slot attached, and four of them have dedicated USB 2.0 ports; the 1st, 2nd, 4th, and 6th slots. Since the Compute Module gives eMMC storage as an option, you can choose from three different ways to boot the Pi, depending on how much you want to spend or what your performance goals are.

And the Pi Compute module can also be booted over the network, so you could either have one Pi run a NAS and boot all the others, or you could have another NAS on your network store the boot data for all the Pis.

## Things to Improve

{{< figure src="./no-labels-on-turing-pi-usb-port-jumpers.jpeg" alt="No labels on Turing Pi USB slave port or jumpers" width="600" height="400" class="insert-image" >}}

One thing I don't like about the Turing Pi is that the board doesn't have a lot of user-friendly labels and markings. Like you can use the micro USB port to flash the Compute Module in slot 1, but it's not labeled. The jumper that controls how this port works isn't labeled either.

{{< figure src="./raspberry-pi-zero-closeup.jpg" alt="Raspberry Pi Zero with labels closeup" width="500" height="282" class="insert-image" >}}

Compare that to this Pi Zero. The Pi Zero is tiny, yet it still has labels printed on the board for all the major parts.

It would be nice if there were at least labels near every port and all the jumpers so you don't have to look up the documentation to see what everything goes to.

Another thing that'd be nice to have is a fan connector in case you wanted to install the Turing Pi in an enclosure that needed active cooling. And a plug for a power indicator and power button would also be nice, so you could integrate the Turing Pi with a mini ITX case's buttons and status lights.

{{< figure src="./rear-no-io-shield.jpeg" alt="Turing Pi in Mini ITX case with no IO shield" width="600" height="416" class="insert-image" >}}

And finally, I heard that there might be a possibility of an IO shield for the Turing Pi. That would make the back of my case look a bit nicer in the back when the Turing Pi is installed.

All in all, the board is put together well, and I didn't have any hardware-related issues to speak of. I'd assume the final production board that's being shipped now is even better quality, since you can see in the picture below, this board's had some history—someone hand-soldered a jumper to fix the operation of this voltage regulator chip:

{{< figure src="./turing-pi-hand-soldered-jumper.jpg" alt="Hand soldered jumper on Turing Pi" width="553" height="311" class="insert-image" >}}

## The Performance of the Turing Pi

For all this flexibility, what good is it if it doesn't perform well?

Well, the Turing Pi allows any of the current Compute Module revisions to perform to their fullest capability. The CPU is only constrained by the fact that the Compute Module is clocked at a maximum of 1.2 GHz. And that's not a limitation of the Turing Pi, it's because the DIMM connection can't provide enough power using the Compute Module's current design to support faster clock speeds.

And the USB and network connections are constrained by the fact that the Compute Module's system-on-a-chip shares a bus for those connections. The built-in gigabit network switch on the Turing Pi means each Compute Module can use it's full 100 Mbps of network bandwidth simultaneously—but you are limited to 100 Mbps per slot.

If you're looking strictly for the best performance possible with a Pi, the Pi 4 is currently a lot faster for most tasks.

The Turing Pi suffers in performance mainly due to the constraints of the older system-on-a-chip the Compute Module uses.

The board itself performs well, and even without a fan, I never had any issues with thermal throttling, even when running benchmarks for a few hours. The thermal image below shows the hottest temperature I could get one of the boards to reach, after running a Drupal benchmark for over an hour:

{{< figure src="./thermal-image-turing-pi-compute-module.jpeg" alt="Thermal image of Compute Module inside Turing Pi cluster" width="480" height="360" class="insert-image" >}}

I think the main reason the temperature control is so good is because the processor is under-clocked, so it doesn't get quite as hot as the chip in the regular Pi 3 B+ did.

{{< figure src="./kill-a-watt-turing-pi-power.jpg" alt="Kill A Watt Power Consumption showing 15.8W at 120V for Turing Pi" width="377" height="450" class="insert-image" >}}

The Turing Pi also does well when it comes to energy consumption. While booting, I measured about 15W of power consumption (or 0.2A) at 120V using a Kill-A-Watt. Unfortunately, due to the pandemic, I couldn't get access to any better power measurement device, so the numbers may be a little off, but in general, this board uses even less power than a separate network switch and Raspberry Pi 4s like I use in my Dramble cluster—that combination measures 19-20W during cluster startup.

Compared to even a single Intel-based computer or old laptop that performs the same or even better than the Turing Pi, the Turing Pi is usually going to get the crown when it comes to energy efficiency, if that's your main concern (again, assuming you're not pegging all the CPU cores at 100% all day).

## The Price of the Turing Pi

But I think there are two main reasons you might hesitate buying a Turing Pi: the price and shipping delays. The board costs $189, and has been delayed in shipping, mainly due to the pandemic.

The Turing Pi isn't the only hardware device I'm interested in that's been having delays; last month, Ars Technica mentioned the [Pinebook Pro was delayed](https://arstechnica.com/gadgets/2020/06/pinebook-pro-review-a-200-foss-to-the-hilt-magnesium-chassis-laptop/), partly because their manufacturing QA process was stalled by the pandemic. From my conversations with the Turing Machines staff, that's the main reason they've had to delay shipments, too. They wanted to iron out all the little issues so the final production board worked perfectly before they shipped them out.

If they don't do that, then you might end up with some boards having strange hardware issues, and nobody likes buying flaky hardware! That's something that plagued early Pinebook Pros, so I'm glad Turing Machines is taking the time to get the Turing Pi right, and it sounds like that process is almost over.

Even still, if you want to get a Pi cluster up and running quickly today, it's probably going to be faster to [buy and put together all the parts](http://www.pidramble.com/wiki/hardware/pis) for a Pi 4 cluster, like my Pi Dramble.

But say you like all the things the Turing Pi has to offer, why does it cost almost $200, and is that even a good price?

Well, it's complicated.

I spoke with someone from Turing Machines about why the board is almost $189, and the main reason is there are a few expensive parts on the board like the DIMM connectors and the individual ethernet controller chips.

Like the Raspberry Pi, the Turing Pi is built to try to make educational computing hardware—except instead of having one set of components for one computer, the Turing Pi has to have all the parts to run _seven_ computers!

{{< figure src="./LAN9514-network-chips-turing-pi-rear.jpeg" alt="LAN9514 chips on rear of Turing Pi" width="379" height="361" class="insert-image" >}}

So if you find a good chip that costs $5, like the [LAN9514 chip](https://www.microchip.com/wwwproducts/en/LAN9514) on the underside of the board that is used for the network interfaces on the Turing Pi, you're looking at a $35 cost in those chips _alone_.

Pair that with the expensive and hard-to-source [200 pin vertical SO-DIMM connector](http://www.altexcorp.co.jp/lotes/pdf/catalog_page01-49_1206.pdf) used to hold the Compute Module—which is $10 each—and you're already over $100 in parts per per board.

And that's not including the 300-plus other components on the board, much less the R&D and production costs!

## Conclusion

So in the end, is $189 a good price for the Turing Pi? Yes and no. Due to limitations of the Compute Module, it's kind of a minimum floor for the price of a board like this. And I'm guessing Turing Machines isn't making a massive profit, either. Their margins are probably pretty thin on this board.

So it's a good price for the hardware and form factor you're getting, but if you're *only* interested in getting the best-performing Pi cluster for the money, you'd probably be better off with the Pi 4.

I hope you liked the Raspberry Pi Cluster series featuring the Turing Pi—if you enjoyed it and want me to do more things like it, please consider sponsoring my work:

  - [Sponsor me on GitHub](https://github.com/sponsors/geerlingguy)
  - [Sponsor me on Patreon](https://www.patreon.com/geerlingguy)

Also consider [subscribing to my YouTube channel](https://www.youtube.com/c/JeffGeerling), as I'm working on more videos about Raspberry Pis, Kubernetes, Ansible, and more!
