---
nid: 3060
title: "The Raspberry Pi 4 has a fan now - the Case Fan"
slug: "raspberry-pi-4-has-fan-now-case-fan"
date: 2020-12-06T17:43:55+00:00
drupal:
  nid: 3060
  path: /blog/2020/raspberry-pi-4-has-fan-now-case-fan
  body_format: markdown
  redirects: []
tags:
  - case
  - cooling
  - fan
  - raspberry pi
  - reviews
  - youtube
---

Last year, I wrote a blog post titled [The Raspberry Pi 4 needs a fan](/blog/2019/raspberry-pi-4-needs-fan-heres-why-and-how-you-can-add-one).

And in a video to go along with that post, I detailed the [process of drilling out a hole in the top of the official Pi 4 case](https://www.youtube.com/watch?v=mTHAO9P_hxQ) and installing a 5v fan inside.

{{< figure src="./pi-fan-in-case-hole-drilled.jpeg" alt="Raspberry Pi 4 Case with Fan drilled into top of case" width="600" height="477" class="insert-image" >}}

But that solution wasn't great. The fan was a little loud and annoying, and would stay on constantly. And who wants to damage the nice-looking Pi Case by putting a hole right in the top?

Well, the folks over at Raspberry Pi Trading—in this particular case, engineer Gordon Hollingworth, as detailed in his post about [Designing the Case Fan](https://www.raspberrypi.org/blog/designing-the-raspberry-pi-case-fan/)—must agree with me that the Pi 4 case needs a fan, because they just started selling the [five dollar Pi Case Fan](https://www.raspberrypi.org/blog/new-raspberry-pi-4-case-fan/).

{{< figure src="./raspberry-pi-case-fan.jpeg" alt="Raspberry Pi Case Fan" width="600" height="371" class="insert-image" >}}

The fact that the [Pi 400 I tore down](/blog/2020/raspberry-pi-400-teardown-and-review) last month has a massive heat sink built in means the Pi engineers know how important it is to dissipate heat from the Pi's main processor.

> **Video**: Check out the video that goes along with this blog post:
>
> [Raspberry Pi Case Fan - How Loud is it?!](https://www.youtube.com/watch?v=ch_OC4kDWVY)

## Fan Specs

Some people are interested in knowing exactly what fan is used, and how big it is, so here's an up-close picture:

{{< figure src="./pi-case-fan-size-up-close.jpeg" alt="Raspberry Pi Case Fan size and specs up close" width="500" height="375" class="insert-image" >}}

It looks like this is the [AD0205MX-K50 2.5cm 2506 25x25x6mm DC5V 0.13A fan](https://www.aliexpress.com/i/4000021798010.html), and from AliExpress, at least, it costs ~$4. It is the 7000 rpm, which according to the spec sheet is the quietest version of that fan model.

## Installing the fan

I love how the box has the installation instructions right on the outside. Regardless of how well the fan works, the box designer deserves a shout-out:

{{< figure src="./case-fan-box-detail-instructions.jpg" alt="Install instructions on side of Pi Case Fan box" width="503" height="283" class="insert-image" >}}

To install the fan, pop off the top of the Pi case, line up the Case fan inside the top of the case, and push it in until the tabs click into place. Plug the red, black, and blue wires into the Pi's GPIO header like it shows on the side of the box.

The Case Fan also includes a little heatsink you can stick on top of the system on a chip. If you don't, the Case Fan alone still keeps the Pi from throttling, but spreading the heat using this heat sink makes the fan's job a little easier, so I stuck mine on.

Pop the top cover on the case, and the Pi is good to go!

The fan intake and exhaust are the gaps around the USB and network jacks, and the gap around the microSD card slot and the other ports on the side of the Pi 4, respectively. Read [Gordon Hollingworth's explanation](https://www.raspberrypi.org/blog/designing-the-raspberry-pi-case-fan/) about why this was ultimately chosen. It would definitely be better to have actual vents, but the airflow is adequate using this technique to keep the Pi cool using the fan.

Here's a preview of what it looks like on a thermal camera. You can see it still gets slightly warm on top, even with the fan going:

{{< figure src="./seek-ir-thermal-pi-case-fan.jpeg" alt="Seek Thermal Image of Pi in Case with Case Fan" width="480" height="360" class="insert-image" >}}

## Fan software controls

To support the hardware, a [new Pi OS update released on December 2](https://www.raspberrypi.org/blog/new-raspberry-pi-os-release-december-2020/) that made it easy to configure options for the Fan, like which GPIO port the blue wire is plugged into, or what temperature the Pi should reach before the fan is powered up.

I enabled the fan in the Pi Configuration utility, and left the defaults, which are pin 14 and 80 degrees celsius:

{{< figure src="./pi-case-fan-configuration.jpg" alt="Pi Case Fan configuration in Raspberry Pi OS setup utility" width="450" height="253" class="insert-image" >}}

If you want to configure the fan settings in the boot config.txt file, the settings are:

```
dtoverlay=gpio-fan,gpiopin=14,temp=80000
```

## Testing the fan

Here's a graph of the Pi running with the fan set to run at 80 degrees during a 20 minute stress test using the [Pi CPU stress script](https://gist.github.com/geerlingguy/91d4736afe9321cbfc1062165188dda4) I maintain on GitHub.

{{< figure src="./pi-temperature-graph-case-fan.png" alt="Raspberry Pi temperature graph - Case Fan" width="1000" height="618" class="insert-image" >}}

And wouldn't you know, the fan works!

You can see the point where the fan kicked in and kept the Pi from throttling before it reached 80°C. At no point when I had the fan installed did the Pi throttle its CPU.

I ran the same test _without_ the case fan installed, and the Pi started throttling around 9 minutes into the CPU stress test:

{{< figure src="./pi-temperature-graph-no-fan.png" alt="Raspberry Pi temperature graph - No Fan in Case" width="1000" height="618" class="insert-image" >}}

In both cases, the Pi will behave similarly until the set temperature is reached when the Case Fan turns on.

I _could_ compare the Case Fan to [other Pi cooling solutions I tested before](/blog/2019/best-way-keep-your-cool-running-raspberry-pi-4), but I don't think that's too important here. The Case Fan is built to do one thing: keep the Pi 4 from throttling when it's inside the official Pi 4 case. And it does that.

So it's a good improvement, but the most important thing for _me_, especially since I'm used to the blissful silence of my fanless [Flirc cases](https://amzn.to/3qyVieg), is how loud the fan is when it runs, and how often it runs.

## How loud is the fan?

To test how loud it is, I used the dB Meter app on my iPhone, and put the iPhone a few inches to the left of the Pi in the case:

<blockquote class="twitter-tweet" data-dnt="true" data-theme="dark"><p lang="en" dir="ltr">For those wondering... this is what the Pi 4 Case Fan sounds like. <a href="https://twitter.com/hashtag/RaspberryPi?src=hash&amp;ref_src=twsrc%5Etfw">#RaspberryPi</a> <a href="https://twitter.com/hashtag/CaseFan?src=hash&amp;ref_src=twsrc%5Etfw">#CaseFan</a> <a href="https://t.co/0seeAhkL9q">pic.twitter.com/0seeAhkL9q</a></p>&mdash; Jeff Geerling (@geerlingguy) <a href="https://twitter.com/geerlingguy/status/1335104796366413825?ref_src=twsrc%5Etfw">December 5, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

A little unpleasant, and it has a high pitched whine that reminds of of the sound you get in an unbalanced audio system with a bit of electrical interference.

In the video [Raspberry Pi Case Fan - How Loud is it?!](https://www.youtube.com/watch?v=ch_OC4kDWVY), I also compare that sound to the sound of my 5v 'PiFan' and the blissful silence of a passively-cooled Flirc case.

When you're dealing with fans that cost less than five dollars, you're not going to get some silent noctua-quality fan—you're more worried about controlling the temperature than the noise. But it is something to consider. The smaller the fan, the more likely it has some annoying pitch.

But there is good news. If you set the fan to only come on at 80°C, then it seems to only have to run for 30 to 60 seconds every three to five minutes if the Pi is under constant one hundred percent load.

It cools it down to around 70 degrees, then shuts off until the Pi hits 80 degrees again.

It's a reliable enough compromise that I'd recommend it to anyone using the official case. But if the Pi Foundation plans on making a similar case for the next Raspberry Pi, I hope they consider the thermals in the case design itself, and either build a passive heat sink into the case like the Flirc, or build a fan into the design of the case itself, instead of as an addon.

## Conclusion

If you already use the official Pi 4 case, then for five bucks, the Case Fan isn't a bad deal. It keeps the Pi from throttling, and only kicks in under the heaviest loads.

But it does sound a little annoying and makes its presence known.

I'd still recommend using a different case, like my favorite, the [Flirc case](https://amzn.to/3qyVieg), or finding other creative ways to mount your Pi 4 so it keeps its cool without a noisy little fan.
