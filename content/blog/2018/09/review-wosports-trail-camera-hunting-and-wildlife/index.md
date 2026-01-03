---
nid: 2870
title: "Review: Wosports Trail Camera for Hunting and Wildlife"
slug: "review-wosports-trail-camera-hunting-and-wildlife"
date: 2018-09-24T00:20:51+00:00
drupal:
  nid: 2870
  path: /blog/2018/review-wosports-trail-camera-hunting-and-wildlife
  body_format: markdown
  redirects: []
tags:
  - cameras
  - hunting
  - photography
  - reviews
  - trail
  - wosports
---

For the past few years, I've been tweaking a few different camera rigs for wildlife and outdoor photography. I have set up a few different time-lapse rigs using my Raspberry Pis with Pi Cameras, and I've set up my Nikon D750 in a few different ways with its built-in intervalometer, or with a wireless remote.

This is great, but I've always wanted to set up the Pi with an infrared Pi Camera, as well as a motion sensor, so I could capture wildlife at _night_. I know there are some animals that peruse the seeds in our yard around the bird feeders, but it's well nigh impossible to capture them with my other non-infrared cameras... and they tend to come out when I'm asleep.

[Wosports](https://wosports.com) contacted me and asked if I'd like a discount on their 'Trail Camera' to give it a test, and I thought it was a great opportunity to check out the basic/low-end of trail cameras, so I took them up on the offer.

{{< figure src="./woosports-hd-hunting-camera-hero.jpg" alt="Wosports Trail Camera" width="390" height="584" class="insert-image" >}}

After a few weeks playing around with the camera in many different environments, I have a pretty good idea of its strengths and weaknesses. And overall, what's my recommendation?

> **tl;dr**: The [Wosports Trail Camera](https://www.amazon.com/Wosports-Trail-Camera-Hunting-Wildlife/dp/B076LJ3NQ4/ref=as_li_ss_tl?ie=UTF8&qid=1537748338&sr=8-5&keywords=trail+camera+wosports&linkCode=ll1&tag=mmjjg-20&linkId=f67474daeae1d95fa5fa3f387a97c086&language=en_US) is a decent low-end introduction to trail cameras. The user interface is extremely basic and sometimes a bit confusing, and there are some weird glitches that can require pulling the battery to reset things sometimes. The video and photo quality is passable, but it won't give pictures you could hang on your wall. If you want to see the animals passing by, this is a great option. If you need high quality video, or a lot of customizability, you will probably need to spend at least double to get a camera with those features.

## Build quality and weatherproofing

One of the things that worries me most with my Raspberry Pi-based setups is weather resistance. I'm always worried about humidity, heat, etc., and would never leave the Pi rig I normally use out on a stormy day. This hunting camera comes with some basic weather sealing, though it seems the manual doesn't recommend leaving it in the elements for longer periods of time.

I left it outside for a few days, strapped to a tree by the bird feeders, and it survived a couple 95°F+ St. Louis summer days, and two long dousings from the irrigation system (I honestly forgot the lens was _directly_ in the path of one of the sprinkler heads!). Then I moved it to a different part of the yard, and it kept on trucking in the shade and in drier conditions.

The whole unit has few seams—mostly on the front for the camera lens (plastic), the IR filter lens (also plastic), and the IR LED lens (also plastic). The side has a long door with a nice latch and a rubber weather strip, and it holds in all the tiny buttons, the full-size SD card slot, and the 8-AA battery holder.

{{< figure src="./woosports-hd-hunting-camera-side-sd-controls.jpg" alt="Wosports Trail Camera - controls, SD card slot, and battery pack on side" width="650" height="434" class="insert-image" >}}

There's also a ribbed extension on the back that allows it to grip on a tree trunk with an included nylon strap, and a standard tripod mount on the bottom so you can mount the whole camera on any kind of tripod or outdoor tripod screw mount.

{{< figure src="./woosports-hd-hunting-camera-bottom-back-tripod-tree.jpg" alt="Wosports Trail Camera - bottom tripod mount and rear" width="650" height="434" class="insert-image" >}}

## Battery Life

I'm used to running a Raspberry Pi and camera off a 10,000 mAh external USB battery, and it typically runs for a couple days before needing a recharge. It would be nice to get even more battery life, and a dedicated camera like this one promises even better battery life since it can effectively go to sleep between camera shots (it's a lot trickier to do that on a Pi computer).

The first thing you'll notice is that this camera takes _eight_ AA batteries. The weight pretty much doubles with a full complement of batteries, but it still feels very solid. Here's a picture of the battery tray that slides into the side:

{{< figure src="./woosports-hd-hunting-camera-battery-pack-aa-8.jpg" alt="Wosports Trail Camera - 8 AA battery pack" width="650" height="376" class="insert-image" >}}

The battery tray and the cavity into which it goes are both pretty solid, and not made of cheap plastic. The only concern I have is the tab you use to release the tray—it requires a little force to unlatch the battery pack, so if there's any part that would fail it would probably be the tab. Note that even without the tab to hold in the pack, the weather-resistant door that covers the entire side would hold the pack in place.

## Image and Video Quality

The pictures and videos you get from the trail camera won't win any awards, but they are serviceable. Rather than bore you with words, here are a few examples put together in a single video:

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/hJIdWKth_7Y" frameborder='0' allowfullscreen></iframe></div>

And here's a quick picture I snapped inside my living room in the evening:

<a href="./interior-evening.jpg">{{< figure src="./interior-evening-low.jpg" alt="Interior picture during the evening" width="650" height="487" class="insert-image" >}}</a>

(Click on the above picture to download the full-resolution file straight from the camera.)

There was enough light to get a full-color image without the infrared LEDs activating, but it's still fairly grainy and you can see a good amount of image noise. In full daylight, the grainy aspect goes away, but there's still a bit of noise in light-to-dark transition areas, and I wouldn't really classify the lens and sensor together as being capable of giving 8 megapixels of sharp, noise-free resolution, more like 2-4 megapixels if you scale down the image a bit.

## User Interface and Features

{{< figure src="./woosports-hd-hunting-camera-front-monitor.jpg" alt="Wosports Trail Camera front LCD interface" width="520" height="426" class="insert-image" >}}

The UI on the device is very spartan. It's not meant to be a camera, but a trail camera, so it doesn't have a lot of options for fine tuning anything. It lets you choose the minimum interval for when it will take a picture or video, and there are a few other options to control the quality and time, but that's about it.

One thing that seemed to happen maybe 10% of the time I turned it off was that the unit would remain on, even if I switched it back to photo or video mode and off again. The only way to power it down was to pop out the battery pack and wait a few seconds. I tend to be forgiving of these kinds of issues because the software to detect a three way soft switch like the one used to control the mode (or 'off') can sometimes be strangely tricky depending on the processor the device uses!

But it would be nice to have a little more polish—maybe one switch for on-off, one for photo or video mode, and one more button so getting through the menus (and exiting once done) would be a little easier. The UX and button design leaves a little to be desired, but in the end the interface works.

## Summary

As I stated in the introduction, this camera won't give you award-winning shots of wildlife. It won't even give you something you'd be proud to post on Instagram. But it provides clear enough video, and audible audio, and will show you anything that walks in front of it, from larger animals and humans down to medium-sized birds like sparrows or mourning doves! Buy it if you need a reliable and fairly durable trail camera for a good price, but don't buy it if you want stunning wildlife photos (you need much more expensive gear for that!).

[Buy the Wosports Trail Camera](https://www.amazon.com/dp/B076LJ3NQ4/ref=as_li_ss_tl?_encoding=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=2e1636cc752d02efd303caec89e804ac&language=en_US) on Amazon.com, or visit the [Wosports](https://wosports.com) website for more information.
