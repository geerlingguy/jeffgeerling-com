---
nid: 3056
title: "The Raspberry Pi makes a great USB webcam for $100"
slug: "raspberry-pi-makes-great-usb-webcam-100"
date: 2020-11-23T15:31:26+00:00
drupal:
  nid: 3056
  path: /blog/2020/raspberry-pi-makes-great-usb-webcam-100
  body_format: markdown
  redirects: []
tags:
  - cameras
  - logitech
  - open source
  - otg
  - raspberry pi
  - usb
  - uvc-gadget
  - video
  - webcam
  - youtube
---

There are many Raspberry Pi projects where I spend a few hours (or dozens of hours) building something with a Pi, and realize at the end that not only could I have purchased an off-the-shelf product to do the same thing for half the component cost, but it would work better too.

But this is not one of those projects:

{{< figure src="./pi-webcam-tripod.jpg" alt="Pi Webcam on Tripod - Pi Zero W and HQ Camera" width="600" height="600" class="insert-image" >}}

The Raspberry Pi and its HQ camera make a surprisingly potent webcam, and if you want to cover the basics, and rival the image quality of all but the highest-end dedicated webcams, you can do it for under $100.

{{< figure src="./jeff-dell-xps-framegrab-pi-webcam.jpg" alt="Still frame grab from recording on Dell XPS 13 using Raspberry Pi Webcam" width="640" height="360" class="insert-image" >}}

Above is a single frame from a recording I did with the HQ Camera on my Raspberry Pi Zero W connected as a standard USB webcam using the Camera app on Windows 10 on my Dell laptop.

That particular Dell laptop is the infamous XPS model with a 'nose cam'—a camera placed in the most unfortunate location: under the screen, so it looks straight up your nostrils at a low angle:

{{< figure src="./dell-nosecam.jpg" alt="Dell XPS 13 Nosecam built-in webcam" width="560" height="315" class="insert-image" >}}

Dell fixed the camera position in newer XPS laptops, but most laptops still have a pretty poor excuse for a camera in their thin display bezel—there's just not enough room in there for a good sensor and lens.

## Video for the Pi Webcam

I go beyond the content of this post with demos, an assembly guide, and more, in my video [Raspberry Pi Zero is a PRO HQ webcam for less than $100!](https://www.youtube.com/watch?v=8fcbP7lEdzY). Go check out the video for a ton more detail than I could cover here.

## A _real_ USB webcam

Using the power of the Pi's OTG port, you can build a _true_ USB webcam—not some hacked-together IP camera that requires extra software to work, requires a flaky `ffmpeg` stream over the network, or only works with a specific app. The Pi Zero's USB port allows power to be delivered to the Pi, and data communications at the same time—perfect for powering a simple camera:

{{< figure src="./pi-zero-usb-otg-port-webcam.jpg" alt="Raspberry Pi Zero with USB OTG cable plugged in for webcam use" width="400" height="400" class="insert-image" >}}

There are now many posts and Gists detailing the process of enabling this OTG webcam, most notably David Hunt's blog post: [Raspberry Pi Zero with Pi Camera as USB Webcam](http://www.davidhunt.ie/raspberry-pi-zero-with-pi-camera-as-usb-webcam/).

{{< figure src="./david-hunt-blog-post.png" alt="David Hunt blog post talking about webcam gadget scripts and serial devices" width="420" height="388" class="insert-image" >}}

But most of these resources dive straight into configuring `dtparams`, modifying boot configs, compiling C code using `make`, and enabling serial interfaces... and all I wanted was a quick way to turn my Pi into a reliable little USB webcam!

So I spent a few hours working everything into an open source project that uses Ansible to deploy the software to the Pi with simple, understandable automation. It can be run either on the Pi directly or from another computer: [Raspberry Pi Webcam on GitHub](https://github.com/geerlingguy/pi-webcam).

This project installs a lightly-modified fork of one of the popular `uvc-gadget` repos with the software that makes everything work (you can configure what fork it uses)—but my intention is only to make the installation quick and easy so more people can use the Pi as a webcam, even if they aren't programmers.

During the pandemic this year, it's frequently hard to get a webcam, but I've noticed Pi Zeros and HQ Camera modules have been well-stocked as the year has worn on. If you can't buy it, _build_ it!

I'm hoping that more people in the community can work to make the underlying uvc-gadget application (which has a _ton_ of disparate forks right now) [easier to configure](https://github.com/geerlingguy/pi-webcam/issues/4) and more stable (right now [it only works on the Pi Zero unless you run an older release of Raspberry Pi OS!](https://github.com/geerlingguy/pi-webcam/issues/5).

Anyways, the [Raspberry Pi Webcam README](https://github.com/geerlingguy/pi-webcam#readme) has all the details for setup of the webcam, including every part that I used to assemble my own webcam.

The process takes about 20-30 minutes, including assembly:

  1. Flash Raspberry Pi OS to a microSD card.
  2. Boot that card in the Pi, complete the setup wizard, and run the pi-webcam playbook on it.
  3. Shut down the Pi.
  4. Assemble the camera module to the Pi.
  5. Plug the Pi Zero's USB port (not PWR IN) into your computer's USB port.

After 30 seconds or so, any standard video software should identify and be able to use the webcam.

{{< figure src="./raspberry-pi-zero-webcam-hq-camera-pi-400.jpg" alt="Raspberry Pi HQ Camera on Pi Zero with Pi 400 used as a webcam" width="600" height="338" class="insert-image" >}}

And in case you were wondering: Yes, the Pi Webcam works great with a Pi 400—I used it to record a few video clips and also to chat via Google Meet online:

{{< figure src="./jeff-joel-google-meet-raspberry-pi-zero-webcam-hq-camera.jpg" alt="Jeff chats with Joel on Google Meet on the Pi 400 using the Pi Webcam" width="599" height="276" class="insert-image" >}}

> **Question**: _What about [showmewebcam](https://github.com/showmewebcam/showmewebcam)?_
> 
> I like that project, and am following its progress as well. Though I don't like the idea of downloading a random Pi OS image and dropping it on a general computer like the Pi, especially if said computer has a camera attached to it. I'm not implying anything malicious, I just like having more fine-grained control and understanding over what I'm installing.
> 
> That said, the showmewebcam project does have some nice features like faster boot, and setting the ACT LED to turn on when the camera is in use, and off otherwise.

## Not all is perfect

There are a few tradeoffs, of course, and I'd be remiss to not mention them here:

  1. **No built-in microphone**: You will need to use a separate mic or your computer's built-in microphone.
  2. **No autofocus**: For me, it's not an issue as I use it in fixed positions with subjects (like myself, or a project on a workbench from above) that aren't moving out of the focal plane.
  3. **Dropped frames and latency** (especially on older Pis at higher resolutions): I set the default to 720p which works great for most cases, but if you want to push to 1080p you can run into dropped frames or even latency, which requires adding audio delay so it is in sync with the video (e.g. via Audio Hijack or OBS).

For many, the tradeoffs are worth it. For people who need a more portable solution, it might not be as nice to always have to mount the Pi and set its focus. Plus it _is_ a slight bit larger than your typical cheap webcam.

## Adaptability adds to the appeal

The other nice thing about the Pi and the HQ Camera module is that it is fully programmable and of decent quality, and so in addition to its life as a webcam, I've been using the combo for [timelapses](https://github.com/geerlingguy/pi-timelapse), background footage, and even wildlife video and astrophotography (more on that soon!).

Some people have questioned the utility of the HQ camera module, but I embrace it—having a couple of these cameras, along with adapters for my [Nikon F](https://amzn.to/3m29VUM) and Sony E mount lenses, along with a [Telescope 1.25" C-mount adapter](https://amzn.to/336ETn0) means I have a software-controllable camera that I can easily use with any of my lenses or telescopes to explore some new photography and video ideas.

Many of my Pi projects end up costing more than over off-the-shelf products with a worse end-user experience—but I learn a lot in the process, and the projects inspire more personal creativity, and that's worth a lot more to me.

But in _this_ case, I'm happy to report my Pi Webcam actually _is_ a better value, in some regards, than boring old webcams—especially since you can usually find the Pi in stock!
