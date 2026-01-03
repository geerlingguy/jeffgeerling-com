---
nid: 3337
title: "MNT Reform - a hackable laptop, not for everyone"
slug: "mnt-reform-hackable-laptop-not-everyone"
date: 2024-01-09T16:00:42+00:00
drupal:
  nid: 3337
  path: /blog/2024/mnt-reform-hackable-laptop-not-everyone
  body_format: markdown
  redirects:
    - /blog/2024/mnt-reform-open-source-laptop
aliases:
  - /blog/2024/mnt-reform-open-source-laptop
tags:
  - computer
  - laptops
  - linux
  - mnt
  - open source
  - reform
  - review
  - video
  - youtube
---

{{< figure src="./mnt-reform-hero-bottom.jpg" alt="MNT Reform bottom with purple battery cells" width="700" height="auto" class="insert-image" >}}

The [MNT Reform](https://shop.mntre.com/products/mnt-reform)'s design, the components, _everything_—is open source. If iFixIt did a teardown, they'd probably give it an 11 out of 10.

You can replace _individual battery cells!_ Some people with these laptops hacked in their own speakers, added more internal Ethernet, or even swapped out the CPU itself.

Does that mean I think you should buy it? No, probably not. It's expensive ([starting at €1199](https://shop.mntre.com/products/mnt-reform)), and it's built for a certain type of person. It's not gonna replace a MacBook or a cheap Chromebook.

But why does this exist, and why am I excited about it?

> **Disclaimer**: The reform used in this review was sent to me for testing; it's already been shipped back to MNT Research. They haven't paid me anything, and they have no input into the content of this blog post.

This blog post contains a lightly edited transcript of my video on the MNT Reform, which you can watch below:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/_DA0Jr4WH-4" frameborder='0' allowfullscreen></iframe></div>
</div>

## Specs

The version I tested, with a Banana Pi BPI-CM4 pre-installed, costs around $1500. The base model is closer to $1200.

{{< figure src="./geekbench-5-a311d-vs-pi-rk3588.jpg" alt="Geekbench 5 results - Raspberry Pi BCM2711, Banana Pi BPI-CM4 A11D, Rockchip RK3588" width="700" height="auto" class="insert-image" >}}

But this one has a 6-core A311D SoC, which I've tested before. It's a bit faster than the Compute Module 4, but a bit slower than the RK3588 in top-of-the-line Arm SBCs like the Rock 5 model B.

It also has 4 GB of RAM, a 1 TB NVMe SSD, a _trackball_, and they also sent along a few premium add-ons, like this white Piñatex sleeve and a full printed handbook.

{{< figure src="./mnt-reform-white-pinatex-cover.jpg" alt="MNT Reform White Pinatex Cover" width="700" height="auto" class="insert-image" >}}

But you can change literally _everything_. Not only can you pop out the keyboard and use it separately, you can also swap out the trackball for a trackpad. And you can swap out the Banana Pi for a Raspberry Pi. Or you can stick with a slightly slower but more IO-capable i.MX instead.

But going along with the theme of repairability, _everything_ about this laptop, from the motherboard to the trackball module, is open source hardware. That means there are [schematics, 3D CAD files, pretty much every little detail](https://mntre.com/docs-reform.html) is available for download.

Meaning if you don't like their trackball layout, you could build one of your own! It's like [Framework's laptop](https://frame.work), except it's truly open and hackable hardware. Since MNT isn't playing in Intel's sandbox, they have the freedom to open up a lot more of their stack, including [their firmware](https://source.mnt.re/reform/reform/-/tree/master/reform2-lpc-fw).

That comes with some downsides, though.

{{< figure src="./mnt-reform-thickness-macbook-air.jpg" alt="MNT Reform thickness 40mm compared to MacBook Air" width="700" height="auto" class="insert-image" >}}

Like... look at how thick this thing is. Closed, it's about 40mm tall. That's fighting with 25-year-old laptop designs in terms of overall thickness. It's a nice metal body, though, so it doesn't have much flex.

And the mechanical keyboard hearkens back to a time when laptop keyboards actually felt nice.

A MacBook Air this ain't. It's just not built to compete in that market, or with things like Chromebooks.

## Getting Started

To demonstrate that and more, I'll jump right into my experience using it. The first step in setting this thing up is connecting the batteries.

If you don't want to get your hands dirty and take full ownership of your laptop, the MNT Reform is not for you.

The power supply they ship is a Mean-Well, so it's a quality adapter, and it's rated at 60 Watts, which is probably a bit generous. I don't think this system would ever pull that much.

But better safe than sorry. There's a 4-amp fuse by the power plug, so this thing couldn't pull more than 48W for more than a few seconds anyway.

One thing I found slightly annoying was there's no indication on the top or side that you have it plugged in. It'd be nice if there were a tiny LED showing whether the laptop's plugged in and charging.

As it is, there's just an amber LED under the wireless antenna on the bottom. You could get battery status when it's booted up, but I like having a visible indicator on the exterior.

That's a minor gripe, though, let's get this thing booted!

## First Boot

{{< figure src="./mnt-reform-power-oled.jpg" alt="MNT Reform Power OLED" width="700" height="auto" class="insert-image" >}}

And... booting it up is a little different, too. You press a 'circle key', then navigate to the 'Boot up' option on the little OLED above the keyboard. That display also has other basic utilities like checking individual battery cell voltages.

But I wanted to boot it up, so I chose that option.

The base OS the Reform ships with is already pretty complete. It comes with a ton of software built-in, and two different graphical environments, Sway or Gnome. (They actually just changed things up and moved to Wayfire, but I'll cover Gnome here.)

{{< figure src="./mnt-reform-linux-help-screen.jpg" alt="MNT Reform Linux help CLI screen" width="700" height="auto" class="insert-image" >}}

But if you don't, the first thing you see after logging in is this nice page of help topics.

I like how they do that, and they also have a whole section on Linux basics in the operator's manual. Doing that helps people who might know a little bit about Linux but never actually used it before.

Dumping you into the command line forces the issue too. It's not like you just boot right into a web browser like a Chromebook. You have to learn how to do that in Linux!

## Gnome and Hardware Quirks

But Gnome it is. I spent some time getting used to the Reform, and the little A311D chip is fast enough for at least casual use. I could play back YouTube videos at 1080p, though the tinny built-in speakers won't hold a candle to my MacBook.

If you wanna solve _that_, just plug in some headphones. The built-in amp sounds great on my ATH-M20s.

But there again, there's a little annoyance that's not a _big_ deal, but it is different than most other modern devices. When I plugged in my headphones, I also had to go into the sound settings and switch inputs.

I don't have to do that on my Mac or pretty much any PC in the past decade or two. But there might be a way to hack Linux a bit to get that automatic output switching to work.

But that's kind of the theme with this thing—it gets very close to what I'm used to, but it's just a tiny bit different, enough to be grating the first few hours I'm using it.

## Input Devices

{{< figure src="./mnt-reform-keyboard-trackball.jpeg" alt="MNT Reform keyboard and trackball" width="700" height="auto" class="insert-image" >}}

Like take the keyboard. It has a split-spacebar layout, and if you're like me and your muscle memory has you hitting the center of where the spacebar _should_ be, you have to either adjust your muscle memory to hit one of the other parts, or remap the keys to use spacebar again.

Same goes for Control, which is moved up to where Caps Lock would normally be. I'm a weirdo and I remap that to Escape, but on this keyboard I have to remap Control back down to the bottom left to get comfortable.

It's not hard to do, but this keyboard is pretty fussy like that. I'd rather just have a standard North American QWERTY layout like I'm used to.

The keyboard's mechanical switches feel great. Certainly better than any other modern laptop I've touched. It needs room for it, meaning the laptop's a bit chonky, but it is nice to type on it.

For pointer control, you can go with either a trackball or trackpad. I tried both, and I had a couple gripes with both these options.

While I do love trackballs—the old giant Kensington trackball was pretty awesome back in the day—this one was a bit smaller, and sunken down so far it was hard to really control it well.

Even with the tracking speed set to max, it took far too much work to move around the screen with it.

Having tons of mechanical buttons around it was nice, but ultimately I went for the Trackpad.

{{< figure src="./mnt-reform-trackpad-use.jpg" alt="MNT Reform Trackpad Use" width="700" height="auto" class="insert-image" >}}

It's not without its quirks, though. It doesn't have any physical buttons, so you _have_ to use tap to click. Which I don't like, just because it feels less precise to me.

Also, that means dragging things around or resizing windows requires a little bit of a dance as you tap and hold with one finger while other fingers do the moving.

Apple's trackpad is still my gold standard, but at least with this built-in trackpad, the tracking speed was nicer, and two-finger scrolling worked great.

## Screen, Networking, Battery

The screen was great, and it's not a bad size for the HD resolution. There's an external HDMI port but at least with the Banana Pi CM4 you can't use it yet. It worked fine when I swapped in a Compute Module 4 though.

I like that the software dimming controls worked out of the box, sometimes with these Linux laptops you can't adjust it to low brightness, or the power saving dimming function doesn't work.

Other hardware integration into Gnome was a little wonky though. The battery indicator would work sometimes, and other times it would just show as 0%, whether I was plugged in or running off battery power.

There are some power commands you can run in Linux to get that info but I just wanted the time estimate or a percentage to show.

I did run through one full battery cycle, playing back a fireplace livestream on YouTube full screen, and it ran for about 2 and a half hours. You can probably get a bit more if you use it conservatively.

It did shut itself down when the battery was exhausted, so it's nice to know the power management is working behind the scenes, even if the UI was a little rough.

WiFi was also quirky in Gnome. I kept trying to connect to my network, and it would say "Authentication Required", but it never actually popped a password dialog.

This looks like a Gnome issue, though, since I found other people with the same problem. The fix was to connect to a hidden network, even though mine isn't really hidden.

That got me online, and it's nice to have both wired Ethernet and WiFi built into a laptop again.

## Physical Aspects

The hinges are great and solid, and there's a magnet that holds the lid closed—just enough tension you have to get a finger in to pull up the lid.

But I do wonder if, like my ancient PowerBook 3400c, the heavy screen will start to sag after a few years, with all that weight on the hinge.

The nice thing with the Reform is _everything_ is available on their store. You can [buy a set of hinges](https://shop.mntre.com/products/mnt-reform-hinges?taxon_id=13) if yours wear out.

That, combined with the fact that things in this laptop are actually big enough to be repaired without breaking things, is one of the main draws to this laptop.

What's a little less, though, is the thickness.

{{< figure src="./mnt-reform-powerbook-macbook-size-comparison.jpg" alt="MNT Reform vs PowerBook 3400c vs M2 MacBook Air" width="700" height="auto" class="insert-image" >}}

I measured it at about 40 millimeters. For comparison, my 25 year old PowerBook 3400c is 65, so we're doing good there.

But it's more than three times thicker than my MacBook Air.

Modern bags and backpacks aren't made for thicker laptops. It fits in my old Case Logic shoulder bag, but only barely.

The thing is, if you're spending over a thousand bucks on a laptop with these specs, you probably aren't buying it to be an ultralight.

It's much more reasonable as an open-hardware portable computer than a sleek go-everywhere laptop, even though you could use it that way in a pinch.

Overall, the things I love most about the hardware are the quality of all the finishes, the ease of access to every part, and the fact I can get at everything—and buy replacement parts if something breaks.

And that's what'll sell certain people on this laptop. Not the specs.

## Compute Module 4 Swap

{{< figure src="./mnt-reform-cm4-pi-swap.jpg" alt="MNT Reform Raspberry Pi Compute Module 4 Swap" width="700" height="auto" class="insert-image" >}}

I also swapped in my own Compute Module 4 for the Banana Pi.

It wasn't hard, and the printed guide that came with the upgrade kit had all the details with some nice illustrations.

You flip over the computer, remove the acrylic bottom cover, remove the heat sink, unseat the BPI-CM4, and plug in the Pi.

There are a couple extra things you need to do for the Pi. For one, there's only one WiFi antenna plug on the CM4, so you should really tape off the other one that's inside, so it doesn't short something out on the motherboard.

And you also need to install an HDMI to Displayport adapter so the internal display works. This was probably the most delicate part of the whole operation. The tiny wires are a little fragile, and you have to pull them to full extension to get it to plug in.

But I did get it back together.

When I booted it up, I could only get output through the HDMI port, and it stopped booting with an error saying the SD card didn't initialize correctly.

I tried three different microSD cards, even a full size SD card, all with Raspberry Pi OS, and got the same error.

So I finally switched over to an eMMC Compute Module, bypassing that external SD card slot. That seemed to do the trick.

And to make the internal display and other hardware features work correctly, I had to prep the Pi with the right configuration options and a custom overlay. I wrote up my experience and exactly what I did to get it working in [this GitHub issue](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/397#issuecomment-1870521676), so if you're trying to do the same thing, go check that for more.

But with that all out of the way, I finally got everything to boot on the Pi, and most things worked great!

The internal NVMe slot doesn't work on the Pi, so you have to use a Mini PCIe to NVMe adapter if you want use an SSD with the Compute Module.

## Should you buy one?

The Reform has been around a while now, and users have been hacking away at them for over a year. In fact, some people made completely custom setups, like [Jacqueline's with a fully custom keyboard](https://mntre.com/media/reform_md/2022-07-01-july-update.html), or [autumn rain's SOQuartz build](https://tenforward.social/@artemis/111651313036967158).

{{< figure src="./mnt-reform-next-mastodon.jpg" alt="MNT Next on Mastodon" width="700" height="auto" class="insert-image" >}}

MNT also has a Pocket Reform that's in final preproduction right now, and they announced they're working on [MNT Reform Next](https://mastodon.social/@mntmn/111649131139949948), a slimmed down version of the Reform. The sample unit runs an RK3588, and it should be around 26mm thick, which is a lot more like a modern laptop than a brick.

And if Raspberry Pi manages to make a Compute Module 5 in the same form factor as the CM4, you could upgrade your Reform to be even faster.

It's certainly been fun having this here for a few weeks. And I'm a little sad to see it go. It wouldn't be able to run as my daily driver since it can't quite handle 4K video like I need, and it only has 1 Gigabit networking.

But it is a very cool project, and I hope MNT Research can continue getting the funding to build the hardware they're building.

Their entire philosophy is open at the core, and that's extremely difficult to find in the hardware space, especially for _actually working_ hardware that ships.

I've seen many open hardware startups come and go, and I thought MNT would be too good to be true, but they've been around enough time I have faith they'll launch the Next and it'll be even better.

## Would I recommend it?

In the end, though, do I think you should buy one of these?

Maybe. But for most of you reading this, probably not. It's a little too expensive for the hardware you get. But there's a certain type of person this laptop is _pefect_ for. And for you, yeah, get one.

{{< figure src="./mnt-reform-bottom-manual-screwdriver.jpeg" alt="MNT Reform bottom with manual and screwdriver" width="700" height="auto" class="insert-image" >}}

It's refreshing to see hardware like this in a sea of impossible-to-repair laptops with locked-down firmware.
