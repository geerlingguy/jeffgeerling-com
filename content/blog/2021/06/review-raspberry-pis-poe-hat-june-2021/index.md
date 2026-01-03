---
nid: 3109
title: "Review of Raspberry Pi's PoE+ HAT (June 2021)"
slug: "review-raspberry-pis-poe-hat-june-2021"
date: 2021-06-17T14:01:46+00:00
drupal:
  nid: 3109
  path: /blog/2021/review-raspberry-pis-poe-hat-june-2021
  body_format: markdown
  redirects:
    - /blog/2021/raspberry-pi-poe-hat-june-2021-revision-not-recommended
    - /blog/2021/raspberry-pi-poe-hat-june-2021-not-recommended
aliases:
  - /blog/2021/raspberry-pi-poe-hat-june-2021-revision-not-recommended
  - /blog/2021/raspberry-pi-poe-hat-june-2021-not-recommended
tags:
  - networking
  - poe
  - power
  - power over ethernet
  - psu
  - raspberry pi
---

The PoE+ HAT powers a Raspberry Pi 3 B+ or 4 model B over a single Ethernet cable, allowing you to skip the USB-C power adapter, assuming you have a PoE capable switch or injector.

Unfortunately, I would recommend the original PoE HAT over the newer PoE+ HAT for _most_ users—though Raspberry Pi have redesigned the HAT slightly and it's more on par with the original, though hard to distinguish which model you're getting. (_Updated mid-2023_)

For more background on PoE in general, and a bit more detail about the board itself and my tests, please watch my video on the PoE+ HAT—otherwise scroll past it and read on for all the testing results:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/XZ08QKAbBoU" frameborder='0' allowfullscreen></iframe></div>
</div>

## Pi PoE History  

In 2018, the Pi Foundation [introduced the PoE HAT for the Pi 3 B+](https://www.raspberrypi.org/blog/introducing-power-over-ethernet-poe-hat/). That initial version had a fatal flaw: on many Pi boards, it could only supply about 200 milliwatts of power to USB before the current limiter reset. Martin Rowan first [documented](https://www.martinrowan.co.uk/2018/09/raspberry-pi-official-poe-hat-fail-if-you-want-to-use-the-usb-ports/) how plugging in almost anything besides a keyboard and mouse would trigger the Pi's overcurrent protection.

The Pi Foundation refunded or replaced all the first version PoE HATs with a new revision. The [new HAT has a 'mezzanine board'](https://www.raspberrypi.org/blog/poe-hat-revision/) that patches over the problem, and I've been running these boards for years without a problem.

The power issues were solved for the Pi 3 B+, but after the Pi 4 came out, people started plugging in more power-hungry devices like USB 3 SSDs, and the Pi's internals could draw even more power. This exposed a flaw can hit some users: the PoE HAT just can't put through all the power a fully-loaded Pi 4 needs.

{{< figure src="./poe-power-802.3af-12.95w.png" alt="802.3af PoE standard supplies 12.95W to PD" width="600" height="338" class="insert-image" >}}

And _that's_ because the first PoE HAT used the **802.3af** standard. It only guarantees up to about 13W of power to a "powered device" like the Raspberry Pi.

Devices like SSDs consume around 3W, and two of them together would be 6W. According to the [Pi documentation](https://www.raspberrypi.org/documentation/hardware/raspberrypi/power/README.md) the Pi 4 itself, minus the USB usage, should have 9W available to it for stable operation.

{{< figure src="./poe-power-15w-total.png" alt="15W total power consumption with Raspberry Pi and 2 SSDs" width="600" height="338" class="insert-image" >}}

If you do the math, 3 + 3 + 9 = **15W**, which is _more than PoE can guarantee_, and _doesn't even include the overhead of the PoE HAT's own power draw_!

And looking back at that power supply documentation again, the 'Recommended PSU current capacity' is 3 Amps for the Pi 4 model B. Basic PoE can't supply more than 13W—or _2.6A total_ at 5V—so we're in a bit of a pickle.

{{< figure src="./pi-dramble-with-poe.jpeg" alt="Raspberry Pi Dramble with PoE Switch" width="600" height="416" class="insert-image" >}}

I currently have a number of Pi 4's using the original PoE HAT, and they've been online for years (see my [Raspberry Pi Dramble cluster](https://www.pidramble.com)). But I don't overclock them, and I don't have anything plugged in via USB, so I'm well within the power requirements.

## PoE+ HAT

Taking all that into account, the Pi Foundation [just announced a new PoE+ HAT](https://www.raspberrypi.org/blog/announcing-the-raspberry-pi-poe-hat/).

{{< figure src="./raspberry-pi-poe-plus-hat-and-box.jpeg" alt="Raspberry Pi PoE+ HAT and box" width="550" height="390" class="insert-image" >}}

And that plus isn't just a marketing term—it refers to the fact that the new version of the HAT supports **802.3at**, which is known as PoE+. It's still backwards compatible, so it can work with older PoE switches, but if you have a PoE+ switch, you can get about _25W_ through the new HAT.

That means you could pump nearly _5A_ into the Pi through PoE+!

Now, before you get all excited, you have to make sure you have a PoE+ switch or injector. A lot of cheaper and older PoE devices only support the older _af_ standard, so you'd still only get 13W.

## PoE+ Switch

Lucky for me, I have a nice HP enterprise PoE+ switch provided by a fan of my YouTube channel. And this switch even offers a web UI where I can check power consumption per port.

{{< figure src="./power-draw-old-hats-3-4W.jpg" alt="HP PoE Switch Power Draw of two Pis" width="600" height="372" class="insert-image" >}}

Looking at the two Pi's I'm currently powering with the original HATs, I can see they're using about 3-4W each, which is well under the HAT's maximum.

## New PoE++ HAT Differences

{{< figure src="./old-poe-new-poe-plus-raspberry-pi-hat.jpeg" alt="Old and new PoE and PoE+ HATs from Raspberry Pi" width="600" height="332" class="insert-image" >}}

The [announcement blog post details the major differences](https://www.raspberrypi.org/blog/announcing-the-raspberry-pi-poe-hat/), but there were two things I really wanted to dig into:

  1. The new power circuit, which converts the ~48V DC power from Ethernet to ~5V DC power for the Pi. It's supposedly more efficient, and uses a new planar transformer that, if nothing else, looks a lot cooler than the old wound transformer, though it lacks the stylish Pi logo.
  2. The new fan, which is from a different manufacturer and outputs 0.2 CFM more air at max speed (12,000 rpm). The new fan is almost identical to the fan used in the Pi Case Fan kit, so I'm guessing the switch could be optimization of the supply change, or just related to parts availability.

## Mounting the HAT

The M2.5 mounting hardware is the same as you get with the original HAT. I'm using some of my own 12mm screws to mount the Pi to my rack tray.

{{< figure src="./screw-protruding-poe-plus-raspberry-pi.jpg" alt="PoE+ HAT screw on fan touching camera connector on Raspberry Pi 4 model B" width="550" height="310" class="insert-image" >}}

One thing that's a bit concerning: the pre-installed fan screw pictured above is too long. It's a 12 millimeter screw, and when you put on the HAT, the screw pushes against the camera connector.

I could ignore it and live with a little board flex, or not tighten the screws all the way. Or I could replace the screw with a 10mm screw, but I don't have one on hand. And technically I could reverse the screw and have a little jagged end sticking out, but then it doesn't slide into my rack as nicely.

So I decided to take care of the problem my favorite way, by making lots of sparks with a Dremel:

{{< figure src="./dremel-cutting-poe-plus-screw.jpg" alt="Dremel cutting sparks of screw on Raspberry Pi PoE+ HAT" width="550" height="332" class="insert-image" >}}

I'm not sure how that passed the board's QA, and hopefully newer batches switch to shorter screws!

And this doesn't matter to _me_ so much, but the new HAT doesn't fit in the official Pi 4 Case. It's just a bit too big. I never use the HAT in any enclosed case so for _me_ it's not an issue. But it is a little annoying that the old HAT _did_ fit, while the new one _doesn't_.

{{< figure src="./poe-header-smd.jpeg" alt="PoE+ Header SMD part that is fragile and prone to lifting" width="575" height="384" class="insert-image" >}}

Another thing I disliked about original HAT's design, and it's the same on the new HAT, is the fragile surface mount socket used for the PoE header connection here. I've had to re-solder it on two of my original HATs, because when you pry the HAT off the Pi, it can get yanked off the tiny solder joints.

Most of the time people just stick the HAT on and it never gets removed, so it's a minor annoyance.

## Running the HAT - Performance

With the HAT mounted, I first tested the fan; the old HAT was a little annoying (but not too obtrusive) when it's fan was going full blast. Well, I compared the new ADDA fan (2.4 CFM at 12k RPM) to the old Sunon fan (2.2 CFM at 10k RPM), and here are the results:

| HAT 🎩 | Airflow 🌬 | Loudness 🔊 |
| --- | --- | --- |
| PoE HAT | 2.2 CFM | 45 dB (max) |
| PoE+ HAT | 2.4 CFM | 54 dB (max) |

You'll have to watch the video linked at the beginning of this post to hear exactly what they sound like, but let's just say you notice when they're running if you're in the same room. And even in my rack in the basement, I can hear the whiny little fan on the PoE+ HAT over the din of the rest of the rack when it's going full blast.

Tweaking the fan settings following the directions in my blog post [Taking control of the Pi PoE HAT's overly-aggressive fan](/blog/2021/taking-control-pi-poe-hats-overly-aggressive-fan) helps, though, because at _low_ speeds, the new fan is actually a bit quieter than the old fan—32 dB on the PoE+ HAT, vs. 38 dB on the PoE HAT.

## Problems

The new PoE+ HAT identifies as a power device in Linux, so you can actually grab some stats about current draw via the command line. For example:

```
$ cat /sys/devices/platform/rpi-poe-power-supply@0/power_supply/rpi-poe/current_now
601000
```

This outputs the current in microamps, meaning at the time of the reading, the PoE+ HAT was supplying 0.6A to the Pi (0.6A at 5V is 3W).

That's pretty typical. But what's _not_ typical is how much power the new PoE+ HAT uses by _itself_! Checking on my enterprise-grade PoE switch, I saw the port with the new PoE+ HAT using almost 6W.

So it doubles the idle power consumption of the Pi.

What about the original HAT? Well, I configured the exact same Pi with the exact same microSD card, and the exact same port on the switch (and tried two other ports too, to make sure it's not a fluke), and the original PoE HAT only used about 4.1W at idle, for the Pi plus the HAT!

**The PoE+ HAT consumes around 60-70% more power** at idle than the old PoE HAT.

If your Pi is running full blast with USB devices plugged in, the difference isn't as dramatic. But if you're like me, and you have some Pis running lightweight utilities like a web server or some monitoring utilities, doubling the idle power consumption isn't exactly ideal.

Even with the Pis shut down, the old HAT consumed 2.6W, and the new one consumes 4.8W. That's a pretty significant amount of power going to waste, almost twice as much as the original PoE HAT.

## Death by overclock

{{< figure src="./stress-test-pi-poe-plus-hat-two-ssds.jpeg" alt="Raspberry Pi PoE+ HAT stress test with two USB 3 SSDs" width="600" height="377" class="insert-image" >}}

I was also excited to really stress the new HAT, so I overclocked the Pi's CPU to 2 GHz, plugged in two SSDs, and set up a stress test. I ran stress-ng on all four CPU cores, ran iperf3 network traffic benchmarks, and wrote data to both SSDs simultaneously.

The first time I ran the test, I was able to do it all, and it worked for a few minutes before I stopped it. The maximum current draw on the Pi itself was 11.2W, while the PoE switch was telling me the whole system was pulling over 14W.

But I tried running the test a few more times, and every time, the Pi would reset after a few seconds at full blast.

The same thing happened when I powered the Pi via USB-C, so the moral of _this_ story is to use a powered USB hub if you use high powered USB devices. The Pi 4's USB ports can only supply a maximum of 1.2 Amps, no matter how much power the Pi itself gets.

## Use with USB-C Power Adapters

Some people asked if I could power the Pi via USB-C instead of over Ethernet while the HAT is attached. So I plugged in USB-C power with the HAT attached and... everything seemed to work just as well—at least, without any hard drives plugged in.

I did notice there was still power flowing through the PoE+ HAT after being tipped off about it by Martin Rowan on Twitter, and I measured over 60 volts across these two leads:

{{< figure src="./measure-voltage-backfeed-across-poe-plus-hat.jpeg" alt="61v across PoE+ HAT Headers when testing on Raspberry Pi with USB-C power" width="600" height="431" class="insert-image" >}}

There's an Ethernet cable plugged in here, but that cable's plugged into a regular switch. I also found this video clip from [Martin Rowan's PoE+ HAT review](https://www.martinrowan.co.uk/2021/06/raspberry-pi-poe-hat-review-part-2-problems/):

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/1UrwJo1bnhE" frameborder='0' allowfullscreen></iframe></div>
</div>

I was wondering why his Pi had that horrible sound, but mine didn't. Well, it turns out I just needed to plug in my hard drive. Then my Pi made the same sound.

Hopefully this coil whine or whatever it is doesn't indicate a deeper issue—I haven't had time to dig in much, but it's really unpleasant to hear in person.

So USB-C power _does_ work, but if you're not going to power the Pi through Ethernet, take off the HAT.

## Conclusion

{{< figure src="./poe-hat-old-and-new-poe-plus-raspberry-pi.jpeg" alt="Raspberry Pi PoE HAT and PoE+ HAT and boxes side by side" width="600" height="400" class="insert-image" >}}

After all this testing, I can't recommend the new PoE+ HAT for most users. Some people like overclockers who have multiple USB devices plugged in might benefit from a little extra power. But for most people, the original PoE HAT seems like a better option. You'll save energy and have a product that fits the Pi 4 model B out of the box without any modifications.

Both of them are $20, so price doesn't make a difference. And you can also find [other PoE HAT options](https://amzn.to/2SEBrOw) for the Pi too, but be careful with some of the cheaper options, since they lack protections that could kill your Pi or the switch it's plugged into.

In the end I find it slightly ironic that James Adams said in the [2018 post announcing the original PoE HAT's revision](https://www.raspberrypi.org/blog/poe-hat-revision/), and I quote:

> "It’s embarrassing to have released a product with a bug like this, but it's a lesson well-learned, and we'll be improving our internal processes to prevent a recurrence."

There are definitely similar teething problems with this next-gen PoE+ HAT, and hopefully QA for the next board's launch is better.

I'll dive more into Power over Ethernet in general in a future post and video, so make sure you [follow this blog via RSS](/blog.xml) or are [subscribed to my YouTube channel](https://www.youtube.com/c/JeffGeerling).

> **June 17 Update—just prior to posting**: I just got an email back from the Pi Foundation with some answers to questions I had making this video:
>
> **USB-C backfeed**: This should not do any damage, but according to the Pi folks, this is not a supported mode of operation and the HAT should be removed if using USB-C to power the Pi.
>
> **Higher Power Consumption**: This is to be expected with the new power circuit, especially if the PoE voltage is at the upper end of the allowed range (48V), like I have from my PoE+ switch. If lower power consumption at idle is important, you should stick with the original PoE HAT.
>
> **Louder ADDA Fan**: The new fan is also rated for higher temperatures and a longer lifetime, and the bearings used are a little noisier at high speeds.
>
> I still wish the board would not use so much power, but I half-wonder if this board is targeted at a future possible revision to the Pi 4 (B+?) or the use case of powering PCI Express devices on the CM4 IO Board... because it's kind of overkill (the wasteful kind) for the normal Pi 4 model B!
