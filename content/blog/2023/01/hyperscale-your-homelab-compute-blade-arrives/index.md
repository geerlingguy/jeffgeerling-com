---
nid: 3266
title: "Hyperscale in your Homelab: The Compute Blade arrives"
slug: "hyperscale-your-homelab-compute-blade-arrives"
date: 2023-01-23T15:00:17+00:00
drupal:
  nid: 3266
  path: /blog/2023/hyperscale-your-homelab-compute-blade-arrives
  body_format: markdown
  redirects: []
tags:
  - arm
  - blade
  - homelab
  - raspberry pi
  - server
  - video
  - youtube
---

{{< figure src="./compute-blade-2023.jpeg" alt="Compute Blade Hero Shot" width="700" height="195" class="insert-image" >}}

This is the Compute Blade, and I'm test driving it in a four-node cluster:

{{< figure src="./compute-blade-cluster.jpeg" alt="Compute Blade 4 Node Cluster with PoE Switch" width="700" height="467" class="insert-image" >}}

I'm testing the Dev version, and [@Merocle](https://twitter.com/Merocle) from [Uptime Lab](https://uplab.pro) sent four Blades, a 3D-printed 4-bay case (a metal 1U rackmount enclosure is in the works), and two fan modules.

He's been testing _40_ of these in a rack at Jetbrains for months, and they're about to go live on Kickstarter.

But why build a cluster with these Blades? And what good are they if you can't even buy a Compute Module 4 from Raspberry Pi? Do any alternative compute modules work? I'll get to ALL those questions in this blog post.

Or, if you're more into visual learning, check out my video on the Compute Blade:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class="embed-container"><iframe src="https://www.youtube.com/embed/rKDGlpnP-vE" frameborder="0" allowfullscreen=""></iframe></div>
</div>

## Compute Blade Overview

{{< figure src="./compute-blade-bokeh.jpeg" alt="Compute Blade with bokeh pre-assembly" width="700" height="467" class="insert-image" >}}

Last year I [posted a video](https://www.youtube.com/watch?v=zH9GwYZu_aE) on an early alpha version of the board. Ivan redesigned almost everything since then. And it looks gorgeous! The blade has an M.2 slot and is powered via a 1 Gbps PoE port on the front. The Dev model has extras like a TPM module, USB and HDMI ports, and physical switches for WiFi and bluetooth.

Above the Ethernet port on front there are a bunch of LEDs, a button, and a couple neopixels. I'll cover those later.

On the opposite end there's a fan header. There's a basic fan board that just holds a 40mm fan in place, or... if you're lucky like me, you have a one-of-a-kind 'overengineered edition' fan controller (pictured below). It has _another_ Raspberry Pi on it—in this case the tiny RP2040 microcontroller—and it measures airflow temperatures and adjusts the fan speeds accordingly. It also has more neopixels on _it_.

{{< figure src="./compute-blade-fan-module-overkill-edition.jpeg" alt="Compute Blade fan controller overengineered edition with RP2040 and Neopixels" width="700" height="467" class="insert-image" >}}

As far as just getting air to flow over the Pi goes, yeah... it's definitely overkill.

Both these fan modules slide into the back of the custom 1U blade chassis, and the Compute Blades slide in the front.

{{< figure src="./compute-blade-heatsink.jpeg" alt="Compute Blade Heatsink Machining underside detail" width="700" height="467" class="insert-image" >}}

You might've also observed the sleek red heatsinks. They work amazing, but take a look underneath—they're probably a nightmare to machine. I'm not sure if the heatsinks will make it to mass production but they work and look great. The Pis stayed under 42°C after ten minutes of `stress-ng` on all 16 CPU cores.

Even _without_ heatsinks, these blades supply plenty of power and cooling for stable overclocking. Ivan's been running and testing forty of them for months in the lab where he works, with no downtime (though [one Pi was drowned and did not come back to life](https://twitter.com/Merocle/status/1616521880764022786)).

{{< figure src="./compute-blade-infineon-tpm-2.jpeg" alt="Infineon TPM 2.0 chip on Compute Blade" width="700" height="467" class="insert-image" >}}

The TPM and Dev versions both come with an integrated [Infineon TPM 2.0 module](https://www.infineon.com/cms/en/product/security-smart-card-solutions/optiga-embedded-security-solutions/optiga-tpm/slb-9670vq2.0/). TPM stands for [Trusted Platform Module](https://trustedcomputinggroup.org/resource/trusted-platform-module-tpm-summary/), and it can be used for secure embedded computing—especially paired with a Zymbit which I'll talk about later. This chip stores encryption keys and secure passwords so someone couldn't steal a blade and get your data.

Ivan went a step further and placed the chip _under the Compute Module_ for better security. Even if someone got physical access to the blade, they couldn't break into the TPM without unplugging the Compute Module. That'd turn off power to the chip and (ideally) lock all your data.

Secure Computing is more complicated than this, and the Raspberry Pi isn't perfect, but the Compute Module does offer some improvements for trusted boot and TPM that I'll touch on more in a future video / blog post.

Continuing the theme of turning the Raspberry Pi enterprise-grade, these blades also have two features that fit right in with other racked equipment:

{{< figure src="./compute-blade-front-leds-button-switches.jpg" alt="Compute Blade front - LEDs, button, Ethernet, and switches" width="700" height="394" class="insert-image" >}}

The pull tab at the front is hinged so it can press the front button. And the LEDs indicate SSD activity, power, and Pi activity, plus there are front and top-mounted neopixels you can program to do whatever you want. You can also turn off all the LEDs in software if you want.

[This demo Python script](https://github.com/mookie-/blade-id/blob/main/blade-id) displays CPU temperature using different colors, and allows the LED to be used for locating the blade. If you have a bunch of these in a rack somewhere, finding a particular Blade might be tricky. So you can trigger the neopixel, then when you find the right Blade, press the button to dismiss it.

## Why Compute Blade?

So there's more to this board than meets the eye, but... why? What would you use these things for?

Ivan's original motivation was to get a bunch of ARM computers running for Continuous Integration testing at Jetbrains. They build _tons_ of software for developers, and they need to test them on Macs, PCs, and yes, even Raspberry Pis!

{{< figure src="./compute-blades-in-rack-40x-2u.jpeg" alt="40 Compute Blades in 2U Rack" width="350" height="465" class="insert-image" >}}

He's running _forty_ Blades in 2U. That's:

  - 160 ARM cores
  - 320 GB of RAM
  - (up to) 320 terabytes of flash storage

...in 2U of rackspace.

That's actually useful for some people. Like if you want a relatively low-power ARM cluster for testing or research. Considering they're only burning a few watts each, you could have 160 ARM cores under 200 watts in 2U, with 40 NVMe drives!

Another advantage of running multiple smaller machines instead of a few large ones is resource isolation. If you host lots of small apps, it's more secure to isolate them on their own hardware. Many modern security problems are due to people running more and more services on one system, sharing the same memory and CPU.

For me, these blades make learning easier. I test open source projects like Kubernetes and Drupal. K3s, in particular, runs great on Pi clusters, and I have a whole open source [pi-cluster setup](https://github.com/geerlingguy/pi-cluster) that I've been working on for years. It has built-in monitoring so you can see your cluster health in real-time, and there example Drupal and database deployments built-in.

I've also tested clustering software like Ceph, which I also have in that pi-cluster project, so go check that out on GitHub even if you just have regular old Pis.

It's just more fun to do this stuff with physical computers, running right next to me on my desk.

And sure, I could run some VMs on a PC, but that doesn't give me bare metal control and physical networking. And performance per watt isn't bad at all if you're running certain workloads like web services. My cluster uses less than 30 watts running four NVMe drives under 100% load, and it's quietly sitting here on my desk.

But just running a bunch of Pis in a cluster is old news. [Tons of people are running Pi clusters](https://www.google.com/search?q=raspberry+pi+cluster). The Blade, though? It takes Pi clustering up a notch. Ivan sent over some other accessories he's been testing.

{{< figure src="./compute-blade-zymbit-and-custom-hsm4-board.jpg" alt="Compute Blade with ZYMKEY 4i and HSM4" width="700" height="394" class="insert-image" >}}

This is a [ZYMKEY 4](https://www.zymbit.com/zymkey/), which is an _additional_ hardware security module that plugs into the partial GPIO header on the blade.

The ZYMKEY has encrypted storage, tamper sensors, and a real-time clock built in, and it turns the Blade into a fully secure compute node.

Ivan also made a custom board using Zymbit's HSM4 security module. Using that, he made [this demo](https://twitter.com/Merocle/status/1449342971955093508) where if you pull out the Blade, it can react to that by doing things like automatically destroying sensitive data.

## Other Blades

The rest of the world isn't standing still, though. Pine64 launched [their own blade](https://pine64.com/product/soquartz-blade/), too. I haven't had time to fully test it out yet, but I did throw both the SOQuartz and a Compute Module 4 on it to see how it performs.

{{< figure src="./soquartz-blade-with-nvme-poe-switch.jpg" alt="Pine64 SOQuartz Blade plugged into PoE switch" width="700" height="394" class="insert-image" >}}

The integrated PoE circuit had a bit of coil whine sometimes, and none of the images I downloaded for the SOQuartz would give me working HDMI or NVMe yet, so I swapped over to a Compute Module 4. My eMMC version worked fine, with HDMI, networking, and NVMe all present. But a Lite CM4 didn't work, it would just go to the rainbow screen when it started booting up.

So Pine64's Blade seems functional, but it's definitely more barebones and doesn't seem to be fully supported yet. If the Compute Blade gives you a slice of Pi, the SOQuartz blade feels like it came out a little... half-baked.

## Other CM4-compatible Modules

And I know how hard it is to find a Raspberry Pi right now. I get it. Just looking at [rpilocator.com](https://rpilocator.com), it's pretty bleak.

But there are _four_ other Compute Module clones you can buy now. All of them _say_ they're pin-compatible with the Compute Module 4.

And I have _three_ of them to test. I actually ordered a [BPI CM4](https://wiki.banana-pi.org/BPI-CM4_Computer_module_and_development_Kit), too, but it's still stuck somewhere between China and my house.

{{< figure src="./compute-blade-with-cm4-clones-pine64-soquartz-radxa-cm3-bigq-cb1.jpg" alt="Compute Blade with Raspberry Pi CM4 clones Pine64 SOQuartz Radxa CM3 Bigq CB1" width="700" height="394" class="insert-image" >}}

But I do have these other clones: [BigTreeTech's CB1](https://biqu.equipment/products/pi4b-adapter-v1-0?variant=39847230242914), [Pine64's SOQuartz](https://wiki.pine64.org/wiki/SOQuartz), and [Radxa's CM3](https://wiki.radxa.com/Rock3/CM). They're all meant to be drop-in replacements, though the CB1 doesn't support PCI Express, so I didn't test it on this board. Check out my Live stream from October, where I [tested out the CB1](https://www.youtube.com/watch?v=Krpac-MaD5s) and talked more about the Pi shortage.

But the SOQuartz _does_ have PCI Express, so I tested it. I actually did a [whole video on it and the CM3](https://www.youtube.com/watch?v=aXlcNVKK-7Q) over a year ago! Back then, it was hard to even get the boards to boot! Have things improved since then?

Well... a little. A lotta Raspberry Pi clones take the approach of 'throw hardware at the wall, and see what sticks.'

But if spec sheets were everything, Raspberry Pi would've been just a tiny footnote in computing history. The big difference is in support, and Raspberry Pi has that in spades, especially with their Raspberry Pi OS. Even Orange Pi started getting in that game with [their own custom OS](http://www.orangepi.org/html/softWare/orangePiOS/index.html) last year.

If I head over to Pine64's [download page for the SOQuartz](https://wiki.pine64.org/wiki/SOQuartz_Software_Releases), it's a mess. There are _six_ different OSes listed, and the page doesn't recommend _any_. In fact, it says right on the page the first three images _don't even work_!

I get that Pine64 is community-based, but anyone besides a developer who comes into the Pine64 ecosystem and expects to be productive is in for a rough ride.

That said, after reading [this blog post](https://jamesachambers.com/pine64-soquartz-cm4-alternative-review/), it looked like I might have the best experience with Armbian. So I looked on Armbian's website, and to my surprise, the SOQuartz wasn't even listed. So I kept searching and found that for some reason the recommended Armbian download was hosted on a forum (`www.t95plus.com`) that wasn't even related to either Pine64 _or_ Armbian.

It's not even apparent [how that image was built](https://github.com/adamfowleruk/deskpi-super6c/issues/2)! It felt sketchy but I downloaded the image anyway. And... it wouldn't download. It got to 250 MB, and got stuck. I tried it a few times but couldn't get that to work.

So I switched gears and tested [Plebian Linux](https://github.com/Plebian-Linux/quartz64-images) instead.

Plebian's goal is to get vanilla Linux running without any hacky RockChip patches. This time the download worked, and it actually booted right up, which was a nice surprise at this point. But it doesn't support HDMI or WiFi yet. And even though I could see my NVMe drive with `lspci`, it seems like the OS can't use it.

So it's a bit of a mess, but at least I can say the SOQuartz does run on the Compute Blade, it's just a matter of software support.

The Radxa CM3 is still giving me trouble flashing an OS, so I couldn't test it out yet. Maybe I'm just unlucky, but it's _definitely_ not all rainbows and butterflies with CM4 clones.

If you _do_ still wanna use one, splurge on the Dev version of the Compute Blade. microSD and HDMI access are invaluable for debugging.

So for _production_ use, I don't recommend clones yet. They're slower, and they don't work out of the box like a Pi does. Even though it pains me to say this, hold out for Compute Module 4s. [Raspberry Pi said](https://www.raspberrypi.com/news/supply-chain-update-its-good-news/) stock should improve through 2023—let's hope that's true.

And I asked Ivan if there was any way he could get a batch of CM4s to sell on Kickstarter for early backers, but he said it would be months, even with a bulk order.

## How to buy a Compute Blade (or 20)

{{< figure src="./compute-blade-assembly.jpeg" alt="Compute Blades pre-assembly on Jeff Geerling's Desk" width="700" height="467" class="insert-image" >}}

Regardless, the Compute Blade is a great way to run Pis in clusters—in fact it's my favorite so far. It's satisfying sliding these things in and watching them run in a rack. Ivan's working on a metal 1U rackmount enclosure too, but I don't have a clue how much it would cost.

If you're just tinkering with some Raspberry Pis, the price is a bit steep. But if you have specific needs for dense ARM compute nodes, or you just want the coolest Pi board on the market, the Compute Blade is worth a look.

It's been fun watching the design of these blades from [this first proof of concept version](https://twitter.com/Merocle/status/1445313995305586688) all the way to production, watching Ivan tweak every single part of this board until it became what it is today.

It'll launch on Kickstarter this week, with three models:

  - A basic version for $60
  - A TPM version for $69
  - and the Dev version for $90

...though those prices aren't a hundred percent final yet. Refer to [the Compute Blade Kickstarter](https://www.kickstarter.com/projects/uptimelab/compute-blade?ref=bfyfme) for all the details, or browse the [Compute Blade website](https://computeblade.com) for even more, including a build log!
