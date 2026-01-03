---
nid: 3071
title: "Argon One M.2 Raspberry Pi SSD Case Review"
slug: "argon-one-m2-raspberry-pi-ssd-case-review"
date: 2021-02-05T16:12:46+00:00
drupal:
  nid: 3071
  path: /blog/2021/argon-one-m2-raspberry-pi-ssd-case-review
  body_format: markdown
  redirects: []
tags:
  - argon one
  - benchmarks
  - case
  - m.2
  - raspberry pi
  - sata
  - ssd
---

I'm a fan of Raspberry Pi cases that keep my Pi cool. And the cases made by Argon Forty have great cooling, which is one reason they're a popular choice. Their latest Argon One M.2 case also adds a built-in high speed SSD drive slot!

{{< figure src="./argon-one-m2-hero.jpeg" alt="Argon One M.2 Case for Raspberry Pi" width="600" height="399" class="insert-image" >}}

A few months ago, someone from Argon Forty reached out and asked if I'd like to review the [Argon ONE M.2](https://amzn.to/2MVERJy), after they watched my video on booting a Pi 4 from an external SSD, and I accepted.

Unlike most Pi cases, this one actually adds features through it's design, like putting all the ports on the back, and adding a mostly-internal SSD, and so I decided to put it through its paces and see what I liked, and what I didn't like.

## Video Review

I also posted a video version of this blog post on YouTube:

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/rLBdi8B5Wgk" frameborder='0' allowfullscreen></iframe></div>

## The Hardware

First, let's look at the hardware design. It's not my favorite, and it gets dangerously close to being an angular gaming monstrosity, but it's muted enough and doesn't have any annoying bright LEDs. I don't like flashy or gaudy designs, and this is mostly sleek and minimal. One thing I _don't_ like, though, is the angled top, which makes it hard to stack anything else on it. I often stack Pis in other cases, like my favorite passively-cooled Pi case, the [Flirc](https://amzn.to/2Lqjjo0).

But for most people that's not a big concern—if you're going to put one of these on your desk as a computer or next to your TV as a gaming or media device, stackability isn't as important.

{{< figure src="./argon-one-open-m2.jpeg" alt="Argon One M.2 Open case" width="600" height="322" class="insert-image" >}}

Assembling all the parts was a little bit of a burden. There were a number of small screws and things that had to be put together to get the whole case together, but as long as you're slow and careful, everything fits together nicely.

It's definitely not a case where you'll get quick access to the Pi itself if you need to pull it out and use it elsewhere sometimes. And even something simple like swapping the microSD card requires the removal of four long screws on the bottom.

But it does have a few really neat tricks up its sleeve.

{{< figure src="./argon-one-gpio.jpeg" alt="Argon One M.2 GPIO Header up top" width="600" height="400" class="insert-image" >}}

First, it's really solid, as the entire top case is metal. Up on top, there's a little magnet cover over a 40-pin GPIO header, with colored labels for all the pins, which is convenient.

On the front, there's an IR receiver, so you could use a remote control with your Pi if you want. Since IR requires a transparent window, you can also see the Pi's status LEDs through it, which is a feature missing from some other metal cases.

{{< figure src="./argon-one-m2-back-case-ports.jpeg" alt="Argon One M.2 Case - Back ports" width="600" height="386" class="insert-image" >}}

The back is where the party is, though, and there are a few things I really like:

Instead of micro HDMI, you get two full size HDMI ports. The USB-C and audio jack are both put out the back as well, through a little 90° daughter card that plugs into the side of the Pi.

There's also a little power button, which can be disabled if you want the Pi to work like it normally would, where it powers up when you plug it in. That's a really nice touch, because they could've just as easily made it so you _have_ to use the power button.

Then there's an extra USB port at the bottom, and that's the feature I'm most excited about on this case. The whole bottom of the case is a custom internal USB 3.0 to M.2 SSD adapter.

## M.2 SSD Adapter

{{< figure src="./argon-one-m2-board-kingston-a400-ssd.jpeg" alt="Argon One M.2 Bottom Case SSD adapter" width="600" height="439" class="insert-image" >}}

It accepts any M.2 SATA SSD, but I should note that it may be confusing figuring out which drives will work with it—on the label it mentions 'B Key & B+M Key', but that's just the _physical_ connectors it's compatible with.

I've found in all my testing with NVMe and M.2 storage that the labels on the drives themselves are often confusing, and some drives that physically fit don't actually work with the interface, depending on the USB storage controller chip that's used!

I had the following drives on hand:

  - [Kingston SA400 120 GB SSD](https://amzn.to/3rpVVpT)
  - [Samsung 970 EVO Plus 250 GB NVMe SSD](https://amzn.to/36HTlDF)
  - [WD_Black 500GB SN750 NVMe SSD](https://amzn.to/3cKBdNt)
  - [XPG SX6000 Lite 120GB SSD](https://amzn.to/3cLu5R8)

If you look at the names of all these drives, they all have keywords like SSD, some of them mention NVMe, but NONE of them mention anything about SATA or the M.2 key in the title.

You have to dig into the drive specs to find any information about the key or whether the drive uses SATA or NVMe.

And it's even more annoying because you can technically fit M-key NVMe drives into the B and B&M key slot on the Argon One (if you push with a little force), even though M-key drives shouldn't fit.

It's not Argon Forty's fault, but it is really annoying to me, as a consumer, that I have a number of different adapters and USB devices, and all of them work with a different set of almost-identical looking drives, all of which say they're M.2 SSDs.

Anyways, sorry about that little side rant.

Can you guess how many of my drives work with the Argon One M.2? Only the Kingston, since it's a SATA drive with a B+M key connector.

Again, this isn't Argon Forty's fault, but you do have to be careful when choosing an SSD. Make sure it has a B or B+M key connector, and make sure it says SATA, and not PCIe or NVMe!

{{< figure src="./argon-one-m2-asm1153e.jpeg" alt="ASM1153e USB 3.0 to SATA3 Controller Chip with UASP support in Argon One M.2" width="600" height="373" class="insert-image" >}}

I went one step further and pulled the M.2 adapter board out of the case, so I could look at the chip on the bottom, and it's an ASmedia ASM1153E, which is a good SATA III controller with UASP support, so it should work great for any modern SATA SSD.

If you don't know what UASP is or why it matters, check out my [video on UASP and the Raspberry Pi](https://www.youtube.com/watch?v=t0kYcM1E5fY).

## Kingston SSD performance

Now that I have a working SSD, I wanted to see how it compared to the microSD card for general performance. And since I learned from my network testing in previous videos that the CPU clock speed on the Pi can have an impact on IO performance, I also ran my benchmarks with a 2 gigahertz overclock.

{{< figure src="./argon-one-benchmark-sequential.png" alt="Argon One M.2 SSD vs microSD performance - sequential" width="980" height="408" class="insert-image" >}}

{{< figure src="./argon-one-benchmark-random.png" alt="Argon One M.2 SSD vs microSD performance - random" width="993" height="404" class="insert-image" >}}

And as I've found with all the other SSDs I've tested, even a cheap low-end SSD like the Kingston SA400 smokes even the fastest microSD cards.

The SSD is 10x faster writing large files, and 7x faster writing small files.

There's no competition, and if you're going to run a Raspberry Pi 4 as your main computer, or as a little server, the M.2 slot on the Argon One is a no-brainer. Everything will feel faster using an SSD, and the storage should be more reliable too.

Also, because the Pi 4 supports USB boot now (I made a [whole video about it](https://www.youtube.com/watch?v=8tTFgrOCsig)), I tested that too, and it worked great. You don't even need a microSD card in the Pi.

The one downside to the way this case works is the way the USB to USB adapter is made; it sticks out a bit on top, and that means the top USB 3.0 port on the Pi has a tiny bit less space available for thicker USB devices, like my [Corsair Voyager](https://amzn.to/36HWJ1l) flash drive.

You can fix that issue by using a separate USB 3 cable, but that takes up a LOT more space and doesn't keep the Argon case as tidy. Most USB devices are fine, though, it's just the thicker plugs you have to worry about.

## Keeping its cool

Besides the built-in SSD storage, one other reason a lot of people like Argon Forty's cases is for better cooling.

I tested the thermals on my Raspberry Pi 4 and found the case to work pretty well with it's included fan—but it also works well enough _without_ the fan that I'm tempted to recommend leaving it disconnected unless you really need that extra cooling, like for overclocking or tons of disk IO.

{{< figure src="./argon-one-temperature-graph.png" alt="Argon One M.2 Pi Temperature Graph with and without Fan" width="1000" height="612" class="insert-image" >}}

Looking closely at the temperature graph, the Pi never hit more than 60°C with no fan, meaning there's a ton more thermal headroom before it would start throttling.

{{< figure src="./argon-one-infrared-top-temp-angle-2.jpeg" alt="Argon One M.2 Infrared Temperature overhead" width="480" height="360" class="insert-image" >}}

And if you look at an infrared picture of the case you can see why; the whole top of the case acts like a giant heat sink, and that's plenty for the Pi to stay cool.

The top of the case does get a little warm, but it's never hot to the touch; it only got up to about 40°C at the hottest point, near the middle.

I should note that during these benchmarks, I had the fan either disconnected, or connected and running at 100% the entire time. When the fan is running full speed, it makes a slightly annoying sound, but it's nowhere near as loud or annoying as the official Raspberry Pi Case Fan ([video review here](https://www.youtube.com/watch?v=ch_OC4kDWVY)) I tested a few weeks ago.

## Fan, IR, and power control

To use all the features of the Argon One case, you can install the Argon One software for the Pi. It gives you control over power button functionality, fan speeds, and the IR receiver. I'm not going to cover all that in this video, but I _was_ interested in playing around with the fan settings.

I installed their software:

```
curl https://download.argon40.com/argon1.sh | bash 
```

Then I ran `argonone-config`.

When you enter the tool, you can choose between running the fan all the time, setting different fan speeds for different temperatures, or even go and manually edit the Argon One Daemon config file.

I tested a few different settings, and in every case, even when the fan was at 30% power, the fan was still about as loud as it was at 100%. Again, it's not too bad, but unless you need the fan running, passive cooling seems to work well.

If you want to do a lot of disk IO with an M.2 SSD, though, you might want to leave the fan on continuously, because there's no direct heat sink between the case and the SSD, and there's also no temperature probe in the drive area, so even if the Pi isn't overheating, the SSD _could_.

## Conclusion

At $45, this case is the most expensive Raspberry Pi case I've used, and is more expensive than the cheapest Pi 4 model B. The built-in M.2 SSD slot saves the cost of an external adapter, and it's the nicest overall package for a Pi 4 plus fast SSD storage I've seen.

The little USB to USB adapter on the back is a little annoying, but that's the price you pay for having the nicest, fastest, most compact Pi 4 model B setup.

I would _really_ love to see what Argon Forty can do with a Compute Module 4, though—with native NVMe support, and more stable overclocking with the better SoC in the CM4, you could get even more speed from that setup, with an even smaller case!

You can [get the Argon One case from Amazon.com](https://amzn.to/2MVERJy).
