---
nid: 2925
title: "The Raspberry Pi 4 needs a fan, here's why and how you can add one"
slug: "raspberry-pi-4-needs-fan-heres-why-and-how-you-can-add-one"
date: 2019-07-17T14:21:58+00:00
drupal:
  nid: 2925
  path: /blog/2019/raspberry-pi-4-needs-fan-heres-why-and-how-you-can-add-one
  body_format: markdown
  redirects: []
tags:
  - case
  - cpu
  - fan
  - hacks
  - how-to
  - performance
  - raspberry pi
  - throttling
  - tutorial
---

> **December 2020 Update**: Lo and behold, the Pi Foundation tacitly acknowledges the Pi needs a fan in the official case, because now they sell the [Case Fan](https://www.raspberrypi.org/blog/new-raspberry-pi-4-case-fan/)!

The Raspberry Pi Foundation's [Pi 4 announcement blog post](https://www.raspberrypi.org/blog/raspberry-pi-4-on-sale-now-from-35/) touted the Pi 4 as providing "PC-like level of performance for most users". The Foundation even offers a [Raspberry Pi 4 Desktop Kit](https://www.raspberrypi.org/products/raspberry-pi-4-desktop-kit/).

The desktop kit includes the official Raspberry Pi 4 case, which is an enclosed plastic box with nothing in the way of ventilation.

I have been using Pis for various projects since their introduction in 2012, and for many models, including the tiny Pi Zero and various A+ revisions, you didn't even need a fan or heatsink to avoid CPU throttling. And thermal images or point measurements using an IR thermometer usually showed the SoC putting out the most heat. As long as there was at least a little space for natural convection (that is, with no fan), you could do almost anything with a Pi and not have to worry about heat.

The Pi 4 is a different beast, though. Not only does the CPU get appreciably hot even under normal load, there are a number of other parts of the board that heat up to the point they are uncomfortable to touch.

Here's a thermal image taken with my [Seek thermal imager](https://www.amazon.com/Seek-Thermal-Compact-Imager-iOS-Apple/dp/B00NYWABAA/ref=as_li_ss_tl?keywords=seek+thermal&qid=1563294096&s=hi&sr=1-1-spons&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=6e3fdda32b0f76051f721598b8c232b7&language=en_US) highlighting the parts of the board generating the most heat after 5 minutes at idle:

{{< figure src="./raspberry-pi-4-thermal.jpg" alt="Raspberry Pi 4 Thermal IR image Seek" width="650" height="488" class="insert-image" >}}

The CPU/System-on-a-Chip (SoC) was around 60°C as well, but the metal casing helps spread that heat around the perimeter pretty well, and in the IR image, the heat radiating off the top of the CPU is somewhat masked by the reflective metal surface. You might notice, however, the bright white areas on the lower left. That's all the power circuitry coming off the USB-C power input. That area of the board is almost always putting out a pretty large chunk of heat, and the components in this area don't put off heat as well as the metal-bodied CPU.

Finally, this image was taken at idle, but if you have any activity on the USB ports, the USB controller chip on the right (that small red spot before you get to the far right of the image) lights up bright white and gets to be 60-70°C as well. A firmware update for the Pi 4 _may_ help keep that chip a little cooler, but it will still get hot under load.

So imagine if you're truly using the Pi 4 as a desktop replacement, with at least one external USB 3.0 hard drive attached, WiFi connected and transferring large amounts of data, a USB keyboard and mouse, a few browser windows open (the average website these days might as well be an AAA video game with how resource-intense it is), a text editor, and a music player. This amount of load is enough to cause the CPU to throttle in less than 10 minutes, in my testing.

> Why is throttling bad? Two reasons: First, throttling prevents you from getting the full CPU speed the Pi can offer, meaning things that you're doing will take longer. Second, it indicates that parts inside the Pi (usually just CPU, but likely other parts) are getting hot enough to reach their own internal safety limits. If you run computing hardware at its thermal capacity for long periods of time, this will cause more wear on the parts than if they are run well inside their limits.

If you're just doing extremely light browsing, reading Wikipedia and the like, it might not hit the point where it throttles. But watching videos, scrolling through more complex sites, and switching applications frequently gets the CPU up to 80°C pretty fast, _especially if it's closed up inside a plastic box with no ventilation_.

For my more formal testing, I started running `stress --cpu 4` to make the CPU do lots of work, continuously. After a couple minutes, using `vcgencmd measure_temp` and `vcgencmd get_throttled`, I was able to see the CPU start throttling as it hit 80°C (176°F):

{{< figure src="./raspberry-pi-4-throttled-without-fan-80c.png" alt="Raspberry Pi 4 throttling CPU at 80 degrees celsius measured using vcgencmd" width="325" height="225" class="insert-image" >}}

> To install `stress`, run `sudo apt-get install -y stress`. You can monitor the current temperature in a terminal window by running the command `watch -n 1 vcgencmd measure_temp`. When the CPU throttles, the command `vcgencmd get_throttled` outputs `0x20002` (the first `2` indicates the Pi has throttled at some point between the prior boot and now; the last `2` indicates the Pi is _currently_ throttling the CPU frequency.

## Modding the official Pi case to have a fan

**tl;dr**: Watch the video (skip to 9:15 for the most exciting part, or read through the instructions below):

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/mTHAO9P_hxQ" frameborder='0' allowfullscreen></iframe></div>

Without any ventilation, it's kind of a little plastic oven inside the Pi 4 case. A heat sink might help in some tiny way, but that heat has nowhere to go! So I decided to follow the lead of Redditor [u/CarbyCarberson](https://www.reddit.com/r/raspberry_pi/comments/can2oe/modified_default_case_for_the_4b_with_temperature/) and put a fan in the top cover.

{{< figure src="./pi-fan-pi-4-outside-case.jpg" alt="Pi Fan outside Raspberry Pi 4 case unplugged" width="650" height="487" class="insert-image" >}}

  1. I purchased a [Pi-Fan](https://www.amazon.com/MakerFocus-Raspberry-Brushless-Connector-Separating/dp/B072FW3DDQ/ref=as_li_ss_tl?keywords=pi-fan&qid=1563294616&s=gateway&sr=8-4&linkCode=ll1&tag=mmjjg-20&linkId=cb52387af7bd0d3de6c7ee0e6fadf29e&language=en_US) (came in a 2-pack) from Amazon, since it fits nicely above the board and comes with the proper screws for mounting. It plugs directly into the Pi's GPIO pins and needs no modifications.
  1. The easiest way to make a hole for the fan is to use a [1 1/8" hole saw](https://www.amazon.com/Tools-Bi-Metal-Arbored-Technology-8-Inch/dp/B0052EDJ3O/ref=as_li_ss_tl?keywords=1+1/8%22+hole+saw&qid=1563343627&s=gateway&sr=8-3&linkCode=ll1&tag=mmjjg-20&linkId=4971fd1d12667b4fd697b8945fe25419&language=en_US), drilling slowly.
  1. Put the hole saw on your drill, and either use the lower speed setting, or hold the trigger gently, and apply light pressure drilling while holding the Pi case steady.
    - If you spin the hole saw too fast, you'll either lose control and scratch up your Pi case, or burn the plastic and make it look pretty ugly.
  1. Drill directly over the center of the top of the case (make sure the Pi is _not_ inside!), in the middle of the area opposite the Pi logo (this way the fan won't be hitting the network or USB jacks).
  1. Use a file and/or sandpaper (up to 600 grit for a really nice finish) to smooth out the cut after you drill through.
  1. Place the fan on top of the hole, lining it up as closely as you can, then use a mechanical pencil or some other method to mark where the screw holes are around the fan's perimeter.
  1. Use a 7/64" drill bit to drill out the fan screw holes you just marked.
  1. Use sandpaper to knock down the burrs from those screw holes on the inside.
  1. Place the fan under the top of the case, label sticking up (so you can see it through the top of the Pi case), and use the screws and nuts to secure the fan to the case.

When you're putting the Pi back into the case, put it in as normal, then connect the red wire from the pan to the Pi's pin 4 (5V), and the black wire to the Pi's pin 6 (ground). (Reference: [GPIO pinout diagram](https://learn.sparkfun.com/tutorials/raspberry-gpio/gpio-pinout).) Next time you plug in the Pi, the fan should start spinning right away. If it doesn't, either something is physically blocking the fan blades from turning, you have the fan plugged into the wrong GPIO pins, or your fan's a dud!

{{< figure src="./raspberry-pi-4-official-case-with-fan.jpg" alt="Raspberry Pi 4 official case with fan" width="650" height="516" class="insert-image" >}}

> If you don't have a drill and/or don't want to purchase a 1 1/8" hole saw, you can also use a Dremel tool, though it takes a lot more care to drill through plastic without burning it or wrecking the rest of the top cover! Use a slow speed, and drill out a hole slightly less than the final size using a Dremel drill bit. Then use a round sanding bit to slowly cut back the last 1/8" or so of plastic to reach the fan's outline. Then use the Dremel drill bit again to drill out the screw holes. Not as simple as using a real drill, but it can work.

## Temperatures after installing a fan

After installing the fan, I booted the Pi and ran `stress --cpu 4` and let it go for an hour. The entire time, the CPU's temperature stayed at or under 60°C (140°F), a full 20°C lower than the throttling point:

{{< figure src="./raspberry-pi-4-with-fan-at-60c-stable.png" alt="Raspberry Pi 4 with stable CPU temperature at 60 degrees celsius" width="325" height="203" class="insert-image" >}}

I have also been running a Kubernetes cluster with four Raspberry Pi 4's (see more: [Rasbperry Pi Dramble](https://www.pidramble.com)), and with the built-in fans on the official PoE HAT, those Pi's processors do not throttle either, even when I'm running a suite of tests which stresses the entire system for an hour or more. The area around the Pis gets fairly warm (since the fans are moving that heat out), but that's a good thing—the heat can dissipate into the surrounding air instead of forming a bubble around the board itself!

The Pi-Fan that I am using produces 50 dB of sound at a distance of one foot (30 cm), so it's not silent, but it's actually a bit quieter than the little fans on the PoE HAT, which also have a higher pitched 'whine' to them that I found more distracting. When it's running, the fan also draws 80 mA of power, continuously, so if you're counting milliamps when supplying power to the Pi (e.g. when running off solar or battery), keep that in mind!

## The Pi 4 needs a fan

A heatsink installed inside the Pi 4's official case will do precious little to avoid throttling the CPU (and likely other components, as they all get very hot). A case like the 'Flirc' heatsink-as-a-case might help a little, though it still only offers passive heat dissipation. The Pi 3 B+ was the first model I used a fan with for intensive computing (e.g. running a Kubernetes cluster), but it could be used for light computing fanless. The Pi 4 pretty much demands a fan, and I'm amazed that the Pi 4 case doesn't even include holes for better natural heat convection.

Here's to hoping the official Pi 4 B+ case includes some active ventilation, if we're going to keep increasing the speed and energy consumption of not only the SoC but all other Pi subsystems. Until then, I'll be modding my cases to include fans, or using something like the PoE board, with built-in ventilation, to keep my Pis cool.

There are some other options which may be even easier than modifying the official case, like the [Fan Shim](https://shop.pimoroni.com/products/fan-shim) from Pimoroni or purchasing a 3rd party case with a fan built in. But this option was easy enough and all I needed to complete the project was a $4 fan and a $7 hole saw drill bit (which I can use for other projects in the future).
