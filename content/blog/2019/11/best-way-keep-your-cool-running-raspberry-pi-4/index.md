---
nid: 2951
title: "The best way to keep your cool running a Raspberry Pi 4"
slug: "best-way-keep-your-cool-running-raspberry-pi-4"
date: 2019-11-22T13:53:12+00:00
drupal:
  nid: 2951
  path: /blog/2019/best-way-keep-your-cool-running-raspberry-pi-4
  body_format: markdown
  redirects: []
tags:
  - cooling
  - cpu
  - monitor
  - raspberry pi
  - raspbian
  - temperature
  - throttling
---

From home [temperature monitoring](https://github.com/geerlingguy/temperature-monitor) to a [Kubernetes cluster hosting a live Drupal website](https://www.pidramble.com), I have a lot of experience running Raspberry Pis. I've used every model through the years, and am currently using a mix of A+, 2 model B, and 4 model B Pis.

{{< figure src="./raspberry-pi-stack-2-3-4-b-plus.jpeg" alt="Stack of Raspberry Pi model B and B+ 2 3 4" width="500" height="472" class="insert-image" >}}

The 3 model B+ was the first generation that had me concerned more about cooling (the CPU gets _hot_!), and the Pi 4's slightly increased performance made that problem even more apparent, as most of my heavier projects resulted in CPU throttling. I've written about how [the Raspberry Pi 4 needs a fan](/blog/2019/raspberry-pi-4-needs-fan-heres-why-and-how-you-can-add-one), and more recently how [it might not](/blog/2019/raspberry-pi-4-might-not-need-fan-anymore).

But I realized, I've done a _lot_ of testing for my own needs, but never compiled them into one concise post. So today I'm going to remedy that by writing the most complete guide I know of for options for cooling your Raspberry Pi. Each approach has its benefits and drawbacks, which I'll highlight along with the raw temperature data from stress tests.

## tl;dr - Just give me the results!

Well, here goes—in table form, here are the maximum and minimum temperatures for each cooling method:

| Cooling Option | Min Temp (°C) | Max temp (°C) | CPU throttled? |
| ---- | ---- | ---- | ---- |
| [Bare Pi](#bare-pi) | 47 | 80 | YES |
| [Bare Pi (with heatsink)](#bare-pi-heatsink) | 47 | 73 | NO |
| [Pi in official case](#pi-case) | 50 | 84 | YES |
| [Pi in official case (fan mod)](#pi-case-fan-mod) | 36 | 57 | NO |
| [ICE Tower (with fan)](#ice-tower) | 32 | 49 | NO |
| [Flirc case](#flirc) | 34 | 55 | NO |
| [PoE HAT (with fan)](#poe-hat) | 42 | 54 | NO |

(Click on the name of any option to go to the detailed results for that cooling method.)

And here's a graph of the actual temperatures for each cooling method through a 20 minute run of the stress test (5 minutes idle, 10 minutes under stress, then 5 minutes idle):

{{< figure src="./all-results-raspberry-pi-cooling.png" alt="Raspberry Pi 4 temperature cooling results - All" width="650" height="349" class="insert-image" >}}

I'll go through each of the Pi cooling setups in detail through the rest of this post.

### Testing Methodology

  - I used this [CPU stress temperature monitoring script](https://gist.github.com/geerlingguy/91d4736afe9321cbfc1062165188dda4).
  - Every test was performed on the same 4 GB Pi 4 model B, using the same [32GB Samsung Evo+ microSD card](https://www.amazon.com/Samsung-Class-Adapter-MB-MC32GA-AM/dp/B0749KG1JK/ref=as_li_ss_tl?crid=12KMT2CCSNEO6&keywords=samsung+evo+micro+sd&qid=1574374280&sprefix=samsung+evo+micro,aps,157&sr=8-7&linkCode=ll1&tag=mmjjg-20&linkId=e45a40d902b8aca401b52ea169d5aae5&language=en_US) updated to the latest Raspbian OS revision.
  - The Pi is [running the latest firmware/bootloader](www.jeffgeerling.com/blog/2019/upgrade-raspberry-pi-4s-firmware-bootloader-better-thermals) which fixes the USB controller's energy usage.
  - The Pi was plugged into an official Pi Foundation USB-C AC adapter (except in the case of the PoE test).
  - The room was kept a constant 23-24°C.

## 1 - Bare Raspberry Pi<a name="bare-pi"></a>

{{< figure src="./raspberry-pi-bare.jpeg" alt="Raspberry Pi 4 model B - Bare" width="500" height="367" class="insert-image" >}}

{{< figure src="./bare-pi.png" alt="Raspberry Pi 4 temperature cooling results - Bare Pi 4" width="650" height="349" class="insert-image" >}}

**Best for**: Tinkering or testing new things.

The barren Raspberry Pi is useful when you're building a new project, playing with GPIO pins, or testing a new Raspberry Pi setup. It's silent when you don't have a fan attached, and best of all, this is how it comes out of the box.

Since there's no case constraining air flow, natural convection carries away enough waste heat from the CPU and other hot parts of the board to keep it from throttling—at least most of the time. Towards the end of a stress test, it throttled for a few times, but only for a brief moment each time.

The board still gets noticeably hot—enough so that a finger touching the wrong part  could burn you (though you shouldn't pick up a running Pi with your greasy oily hands!). And the heat can make its way over to the microSD card, possibly reducing its stability or longevity.

## 2 - Bare Raspberry Pi with CPU Heatsink<a name="bare-pi-heatsink"></a>

{{< figure src="./raspberry-pi-cpu-heatsink.jpeg" alt="Rasbperry Pi with CPU Heatsink" width="500" height="358" class="insert-image" >}}

{{< figure src="./bare-pi-heatsink.png" alt="Raspberry Pi 4 temperature cooling results - Bare Pi 4 with Heatsink" width="650" height="349" class="insert-image" >}}

**Best for**: Keeping the CPU from throttling under load—but just barely and not in a case.

There are zillions of Pi CPU heatsinks available from Amazon ([here's the heatsink kit I used](https://www.amazon.com/gp/product/B01G9N2GTY/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=8fa9cb423bb472dad3c0489dcc6cd15a&language=en_US)). Almost every one of them will do an adequate job dissipating heat. The key is to increase the surface area beyond the flat plane of the top of the Pi's own CPU enclosure. The more surface area (and the better the thermal pad between the CPU and heat sink), the better the dissipation.

Heatsinks will generally shave 5-10°C off the highest temperatures you encounter, which is significant, but you still need to have air moving across the heatsink for it to do anything. This means either a fully open Pi (great for testing or tinkering, not so great for a semi-permanent installation), a well-ventilated case (with slots or holes in the bottom and top to allow natural convection), or a fan. So not a bad choice, and they're so cheap you should probably stick them on any Pi you can... but heatsinks alone won't solve Pi cooling problems.

## 3 - Official Pi case<a name="pi-case"></a>

{{< figure src="./raspberry-pi-official-case.jpeg" alt="Rasbperry Pi in Official Case" width="500" height="372" class="insert-image" >}}

{{< figure src="./case.png" alt="Raspberry Pi 4 temperature cooling results - Pi in official case" width="650" height="349" class="insert-image" >}}

**Best for**: Cooking things in a plastic Raspberry Pi-sized oven. Otherwise, nothing.

Even though the [official Pi 4 case](https://www.raspberrypi.org/products/raspberry-pi-4-case/) looks nice, it's a bad idea to use it if you don't modify it in any way. It completely encases the Pi, with zero ventilation, meaning all the heat generated by the CPU, ethernet controller, etc. just gets trapped inside. It's great if you want to cook the board, and technically you could keep it running this way indefinitely.

If you use the official Pi 4 case, you'll deal with a CPU that frequently throttles (meaning a slower Pi), and all the other components will be very hot all the time. While some components (like the SoC/CPU) can handle the heat around 85°C, others might not fare so well. I'm looking at _you_, little cheap microSD card!

And no, a heatsink on the CPU inside the Pi 4 case won't help—the heat it dumps still gets stuck in the mini-oven!

## 4 - Official Pi case with fan mod<a name="pi-case-fan-mod"></a>

{{< figure src="./raspberry-pi-official-case-fan.jpeg" alt="Rasbperry Pi in Official Case with Fan mod" width="500" height="362" class="insert-image" >}}

{{< figure src="./case-fan.png" alt="Raspberry Pi 4 temperature cooling results - Pi in official case with fan mod" width="650" height="349" class="insert-image" >}}

**Best for**: Using the official Raspberry Pi case without throttling.

The official Pi case looks nice. And it fits the Pi just so. If you're married to this case, the best option is to mod it to at least provide better ventilation (e.g. by drilling some holes or slots for natural convection). Even better, mod it with a tiny fan like the [Pi-Fan](https://www.amazon.com/gp/product/B072FW3DDQ/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=455791787881e4046e75da69cdbdea18&language=en_US), as I detail in [this post and video](/blog/2019/raspberry-pi-4-needs-fan-heres-why-and-how-you-can-add-one).

## 5 - Flirc case (case-as-a-heatsink)<a name="flirc"></a>

{{< figure src="./raspberry-pi-flirc-case.jpeg" alt="Rasbperry Pi in Flirc Case" width="500" height="348" class="insert-image" >}}

{{< figure src="./flirc.png" alt="Raspberry Pi 4 temperature cooling results - Flirc case" width="650" height="349" class="insert-image" >}}

**Best for**: Almost any use case.

The [Flirc case](https://www.amazon.com/gp/product/B07WG4DW52/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=1892cbe2d6a52a4f05942eb930c58747&language=en_US) is a little pricier than other cases, but is worth it. It is completely silent (no fan), it looks great (aluminum on the sides and a flat rubberized surface on top), and it dissipates heat very well—almost as well as the ICE Tower and its fan!

I will be buying more of these for my more-permanent Pi 4 installations.

## 6 - S2Pi ICE Tower Cooling Fan<a name="ice-tower"></a>

{{< figure src="./raspberry-pi-ice-tower-fan.jpeg" alt="Rasbperry Pi with S2Pi ICE Tower Cooling Fan" width="500" height="348" class="insert-image" >}}

{{< figure src="./ice-tower.png" alt="Raspberry Pi 4 temperature cooling results - Pi with ICE Tower cooling Fan" width="650" height="349" class="insert-image" >}}

**Best for**: Overclockers. Crypto miners. Kubernetes users.

The [ICE Tower](https://www.amazon.com/seeed-studio-Cooling-Raspberry-Support/dp/B07XFLMYSC/ref=as_li_ss_tl?crid=1OPF3ELOCEBCI&keywords=ice+tower+raspberry+pi&qid=1574373758&s=electronics&sprefix=ice+tower+rasp,electronics,152&sr=1-2&linkCode=ll1&tag=mmjjg-20&linkId=f977510442ff91ad5668e6d77084b10e&language=en_US) is, by far, the best-performing cooling solution for the Raspberry Pi. At idle, it keeps the Pi CPU close to ambient temperature, and at full-tilt, the CPU never reached 50°C. This is probably the best-performing cooling solution for the Raspberry Pi short of immersive liquid cooling.

That is to say, for most users, it's overkill. But the best kind. I mean, look at the thing! It gives me vibes of the days when I was overclocking my Pentium II CPU and catching motherboards on fire!

## 7 - Official Pi PoE HAT (with temperature-controlled fan)<a name="poe-hat"></a>

{{< figure src="./raspberry-pi-poe-hat-fan.jpeg" alt="Rasbperry Pi with official PoE HAT and Fan" width="500" height="363" class="insert-image" >}}

{{< figure src="./poe-hat.png" alt="Raspberry Pi 4 temperature cooling results - Pi official PoE HAT" width="650" height="349" class="insert-image" >}}

**Best for**: Keeping a PoE-powered Pi cool, people who don't have the Pi within earshot.

The official PoE HAT includes a small-but-mighty fan which is positioned directly over the Pi 4's CPU. This little fan wins the award for _consistency_; it lets the CPU idle a little hotter than the Flirc and ICE Tower, but it also throttles up as needed to try to keep the CPU in a narrow temperature range (~45-55°C), whereas the Flirc and other solutions allow the Pi to get a little hotter.

The PoE HAT is a bit of a niche product, useful only for those who want to power their Pis from a network connection. The little fan does a good job cooling, but it's also fairly loud when it is doing so, due to its diminutive size. I wouldn't want one of these running within earshot (says the guy with a [Pi Kubernetes cluster](https://www.pidramble.com) running 24x7 in his office...), since the fan powers up and down quite frequently.

## Summary

The Raspberry Pi 3 model B+ and 4 model B have made the Pi a rather competent little computer. But as it starts to match low-end server specs, it also matches their thermal output. If you do anything besides the most lightweight computing tasks, you should consider using one of the better cooling solutions in the post above.

My recommendation for most people is the [Flirc case](https://www.amazon.com/gp/product/B07WG4DW52/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=1fc0a3ed1653529bb4ada89eb18fce3d&language=en_US). If you need to hammer the Pi a lot (and can hack together your own case for it), you might want to consider the [ICE Tower](https://www.amazon.com/seeed-studio-Cooling-Raspberry-Support/dp/B07XFLMYSC/ref=as_li_ss_tl?keywords=ice+tower&qid=1574377098&sr=8-2&linkCode=ll1&tag=mmjjg-20&linkId=34977420ac2812e4beafc0b40d49594b&language=en_US). Otherwise, if you just tinker with the Pi and aren't using it more than a little here and there, you might be happy slapping a [tiny heatsink](https://www.amazon.com/gp/product/B01G9N2GTY/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=fd41e384abf6292572619c624b143c4d&language=en_US) on the CPU.
