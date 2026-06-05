---
date: '2026-06-05T09:00:00-05:00'
tags: ['ip', 'kvm', 'pikvm', 'jetkvm', 'sipeed', 'glinet', 'homelab', 'youtube', 'video']
title: 'I tested every IP KVM in my Homelab'
slug: 'i-tested-every-ip-kvm'
---
TODO: PHOTO HERE

Since the PiKVM came out in 2017, there's been an _explosion_ of these tiny remote control boxes. And I've tested _almost every one_. What are these things good for?

Well, you can already use like remote desktop, Screen Sharing on the Mac, or VNC to remote control a computer from anywhere on a LAN. And if you don't have a private VPN, you could use RealVNC, Raspberry Pi Connect, or wire up Tailscale or Pangolin for fully remote access. Those solutions are great, and so is just SSH, like for cloud servers.

But there are situations where you don't _want_ to have remote control software running on the computer. In my case, sometimes I'm benchmarking a computer, and I don't want screen sharing using up any resources. Or what if you have a computer you wanna access remotely _no matter what_. Screen sharing, and even SSH, don't do any good if the computer's locked up. Or turned off.

Enter the IP KVM. High end server hardware has these things built-in, and they call it names like Integrated Lights-Out, iDRAC, or IMPI. So usually you wouldn't need one of these if you're running server motherboards, like my Arm NAS. I can just use the built-in OpenBMC interface.

But if you don't have that, or if you wanna get full remote control through a video card or something, instead of the built-in VGA graphics, IP KVMs let you do that.

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/4wYxgPfQAjM' frameborder='0' allowfullscreen></iframe></div>
</div>

IP KVM stands for "IP Keyboard Video and Mouse". Basically, putting control of your computer over an IP network.

_All_ of these have a slightly different purpose. And _most_ of these are pretty affordable now.

The high-end boxes have tons of special features like PoE support, HDMI passthrough, and backup 5G modems. But sometimes you just wanna stick one of these on a computer and get display, keyboard, and mouse control. You can get some models for under $50 if that's all you need.

But today, I'll run through _all_ of these devices. This isn't a full review of each device, for that, I'll happily refer you out to other tech YouTubers, who've been putting these through their paces.

But this is as comprehensive an overview as I can do, after testing over _months_. A few of them for even _years_. The crazy thing is, these are all pretty good, and you just have to find the one that meets your needs the best.

But before we get started, a word of caution:

_One_ of these devices actually got me a visit from the FBI. And _all_ these things can be security holes, just waiting to be exploited. Any form of remote control needs to be treated like an open door into your network—make sure you put a good lock on it.

Keep 'em up to date, don't buy one if you don't trust the vendor, and firewall them off as much as you can. Using an IP KVM is like giving someone root access if they get into your BIOS.

To see just how damaging things can be, check out [this article](https://arstechnica.com/security/2026/03/researchers-disclose-vulnerabilities-in-ip-kvms-from-4-manufacturers/) about some pretty serious vulnerabilities some of the devices I'm about to review have run into.

All that outta the way, let's start off with the classic, the PiKVM.

## PiKVM

{{< figure
  src="./TODO"
  alt="TODO"
  width="700"
  height="auto"
  class="insert-image"
>}}

For me, this thing started it all. The folks at [PiKVM](https://pikvm.org) built the open source software that was used in every first-generation clone, and cemented Raspberry Pi as the computer used in these things. My Dad and I tested all the PiKVM models, and I like everything about 'em except one thing: the price. I 100% recommend them, especially since your directly supporting the folks who wrote the software. But I also know a lotta people stop looking once they see the price tag.

Going from [$275 to $400 bucks](https://pikvm.org/buy/#pikvm-v4-plus), they offer features like HDMI passthrough, two-way audio, power controls, addons for KVM switching, 5G backup, and a [fully open source](https://github.com/pikvm/pikvm/) software stack. They even have instructions for building your own, if you have a Pi and you wanna save some money!

  - Prices:
    - PiKVM v4 Plus (with CM4): $400(ish) on [PiShop.us](https://pikvm.org/buy/#pikvm-v4-plus)
    - PiKVM v4 Mini (sans-CM4): $270(ish) on [CloudFree](https://pikvm.org/buy/#pikvm-v4-mini)
    - PiKVM v3 (with Pi 4): $275(ish) on [PiShop.us](https://pikvm.org/buy/#pikvm-v3-preasm)

  - Chipset: BCM2711
  - Topline features: 1080p at 60fps, HDMI passthrough, two-way audio support, ATX power control, multi-computer option with extra hardware, a PCI Express slot for 4G or 5G cards for redunant Internet, and uses around 3W of power
  - Open source: GPLv3 license, source is [here](https://github.com/pikvm/pikvm/), basis for almost all the Raspberry Pi-powered KVMs

## BliKVM

{{< figure
  src="./TODO"
  alt="TODO"
  width="700"
  height="auto"
  class="insert-image"
>}}

The [BliKVM](https://blikvm.com) is basically the PiKVM, but cheaper, because the company benefitted from the software PiKVM already built. So on just the hardware level, it has the same benefits and tradeoffs. But on the ecosystem side, you're not putting money back into the open source project that started it all. They have modified the software a little now, and they acknowledge where they get the software, but honestly? Starting over [over $200](https://blicube.aliexpress.com/store/1101755276) for a cheaper Allwinner version, they're outclassed by newer KVMs. My favorite thing BliKVM did was their PCI Express version, that you can slot inside your computer. I still use that thing sometimes.

  - $235 to $300 on [AliExpress](https://blicube.aliexpress.com/store/1101755276)
  - Chipset: Allwinner H616 or Raspberry Pi CM4
  - Topline features: Versions with Pi or Allwinner chip, a PCIe card version you can stick inside a PC, and plenty of accessories if you need extra features like HDMI passthrough. A bit of a messy setup, but it has everything out of the box.
  - Open source: GPLv3 license, source is [here](https://github.com/blikvm/blikvm)

## GL-iNet Comet

{{< figure
  src="./TODO"
  alt="TODO"
  width="700"
  height="auto"
  class="insert-image"
>}}

A company that's extending KVMs even _further_ is GL-iNet. They're already popular for like portable routers, but they kicked off their KVM journey with the [Comet](https://www.gl-inet.com/products/gl-rm1/), that costs $99, and like BliKVM, their software is a fork of [PiKVM](https://github.com/gl-inet/glkvm). So between that and using a cheaper RISC-V computer instead of Raspberry Pi, they can cut down the cost a _lot_. They also bump the supported resolution up to 4K, and they have external options for ATX power control or even this cute little FingerBot, if you need to push a button remotely.

  - $99.99 from [GL-iNet](https://store.gl-inet.com/products/comet-gl-rm1-remote-keyboard-video-mouse)
  - Chipset: RV1126
  - Topline features: 4K at 30fps, 8GB eMMC, option for ATX board and Fingerbot for remote power button pushes
  - Open source: Self-hosted cloud feature, KVM UI based on PiKVM, source is [here](https://github.com/gl-inet/glkvm)

## GL-iNet Comet Pro

{{< figure
  src="./TODO"
  alt="TODO"
  width="700"
  height="auto"
  class="insert-image"
>}}

Now the Comet is pretty barebones, which is why they also sent me a [Comet _Pro_](https://store.gl-inet.com/products/comet-pro-gl-rm10-remote-kvm-over-wi-fi-6) to test. And I should say, _most_ of the KVMs I'm testing are review samples, just to be clear. That's why I marked this video as 'sponsored'. Even though none of the companies paid me any money or have a say in the video, I wanna be clear that I only paid for a few of these KVMs.

But that outta the way, the Pro isn't quite double the cost, but it adds on WiFi support, 4x more onboard storage for like bootable ISOs, a touchscreen, HDMI passthrough, and it still supports the FingerBot and ATX power control.

GL-iNet has a couple other unreleased KVMs, too, which I hope to test out someday (one for USB control, the other for 4-computer switching).

  - $179.99 from [GL-iNet](https://store.gl-inet.com/products/comet-pro-gl-rm10-remote-kvm-over-wi-fi-6)
  - Chipset: RV1126B (unconfirmed)
  - Topline features: 4K at 30fps, built-in WiFi, 32GB eMMC, touchscreen, HDMI passthrough, option for ATX board and Fingerbot for remote power button pushes
  - Open source: Self-hosted cloud feature, KVM UI based on PiKVM, source is [here](https://github.com/gl-inet/glkvm)

## Sipeed NanoKVM Cube

{{< figure
  src="./TODO"
  alt="TODO"
  width="700"
  height="auto"
  class="insert-image"
>}}

Switching tracks to something _way_ smaller, this is the little guy that [got me an FBI visit](https://www.youtube.com/watch?v=Lc2hB2AwHso). This [NanoKVM](https://wiki.sipeed.com/hardware/en/kvm/NanoKVM/introduction.html) is _so_ cheap at $70, that apparently hackers were sending these to US workers to access corporate networks, in some espionage scheme. That doesn't mean the NanoKVM is 'bad', just that they're cheap and inconspicuous, and that made them great for [North Korean spies](https://www.runzero.com/blog/oob-p1-ip-kvm/).

Of course, Sipeed who makes these things didn't help the fact by including a tiny microphone. I made a short video about it. The problem is Sipeed built this thing with a RISC-V development board, that just so happens to include a tiny microphone. But in general, if you're nervous about using hardware like this from China, then just pick something else. Sipeed also took a while to open source their firmware, which _also_ didn't help NanoKVM's trust level.

But I still like this little guy, if for no other reason than it showed manufacturers you could get tiny KVMs going under $100.

  - $69 on [AliExpress](https://www.aliexpress.us/item/3256807365797749.html)
  - Chipset: SG2002 (RISC-V)
  - Topline features: 1080p at 60fps, 32GB microSD, Comes with ATX breakout when buying full kit
  - Open source: [KVM UI source](https://github.com/sipeed/NanoKVM)

## Sipeed NanoKVM PCIe

I haven't tested it, but Sipeed also makes the [NanoKVM PCIe](https://wiki.sipeed.com/hardware/en/kvm/NanoKVM_PCIe/introduction.html) form factor, for installation inside a computer.

  - $73 on [AliExpress](https://www.aliexpress.us/item/3256808448646497.html)
  - Chipset: SG2002 (RISC-V)
  - Topline features: 4K at 30fps, 32GB eMMC, HDMI passthrough, options for PoE, WiFi, ATX breakout adding on up to $120 total
  - Open source: [KVM UI source](https://github.com/sipeed/NanoKVM)

## Sipeed NanoKVM Pro / Pro PCIe

{{< figure
  src="./TODO"
  alt="TODO"
  width="700"
  height="auto"
  class="insert-image"
>}}

Sipeed also branched out kinda like GL-iNet and made a [Pro version](https://wiki.sipeed.com/hardware/en/kvm/NanoKVM_Pro/introduction.html) with a touchscreen, a control wheel, WiFi, HDMI passthrough, really the whole nine yards.

_And_ they made two PCI Express card versions too. And all these things are pretty cheap still, under $100. The cheaper NanoKVMs are built around the Sophgo SG2002 RISC-V chip, and the Pro models use Axera's dual-core Arm AX630C chip.

I've tested all their different models, and they all work great. Sipeed's UI is completely custom, too, and quite minimal. Availability at least in the US can be hit or miss, but I'm not sure if that's more from tariffs, production speed, or import restrictions.

  - $99 on [AliExpress](https://www.aliexpress.us/item/3256809862156511.html)
  - Chipset: AX630C
  - Topline features: 4K at 30fps, 32GB eMMC, HDMI passthrough, PoE, built-in display with control wheel, options for WiFi, ATX breakout adding on up to $120 total
  - Open source: [KVM UI source](https://github.com/sipeed/NanoKVM)

## JetKVM

{{< figure
  src="./TODO"
  alt="TODO"
  width="700"
  height="auto"
  class="insert-image"
>}}

One IP KVM that was _definitely_ impacted by import restrictions was the [JetKVM](https://jetkvm.com). I did a whole video on it pre-launch, and I still love these little guys for the fast UI and clean aesthetic. And the two little screws up top mean you can hard-mount these into rackmounts, like I'm using in my clock rack.

I don't know if it's just me, but this whole setup feels like one of the most polished out of all the devices I set up. From the packaging, to the solid metal unit, to the snappy UI, I still use these around the studio more than any other device.

These use a RISC-V chip, which helps them stay around $100, but because of import issues, they never really got to ship in quantity at the same low price I think they intended to.

There are some quirks, like no built-in PoE, and a mini HDMI port on the back that needs an adapter, but overall this is one of my favorite little IP KVMs. I mean look at the cute little watch face front!

WisdPi makes a [PoE splitter](https://wisdpi.com/products/jet-poe-splitter) you can use to power it over Ethernet, and that's also what I'm using in my clock rack.

Anyway, the JetKVM is a lot like the PiKVM in that the team behind it devoted a lot of time and resources to building an entirely new open source software stack...

_Also_ like PiKVM, other companies quickly forked it and built their _own_ tiny, cheap KVMs, kinda sucking away a lotta the potential market.

  - $103 on [wisdPi](https://www.wisdpi.com/products/jetkvm)
  - Chipset: RV1106G3
  - Topline features: 1080p at 60fps, 16GB eMMC, touchscreen, small zinc-alloy body, ATX, Serial, DC Power control attachments sold separately
  - Open source: KVM [Go-based App](https://github.com/jetkvm/kvm) (GPLv2), [Firmware](https://github.com/jetkvm/rv1106-system) (upstream licenses)

## LuckFox PicoKVM

{{< figure
  src="./TODO"
  alt="TODO"
  width="700"
  height="auto"
  class="insert-image"
>}}

One of these companies is LuckFox. They're a newer embedded device manufacturer, and their [PicoKVM](https://www.waveshare.com/luckfox-picokvm.htm?sku=30583) is basically the JetKVM, but square, with the screen on top. The price is a bit lower, though, and if you don't need it rackmounted, I guess it's a viable option.

  - $61.99 on [Waveshare](https://www.waveshare.com/luckfox-picokvm.htm?sku=30583)
  - Chipset: RV1106G3
  - Topline features: 1080p at 60Hz, 8GB eMMC, Touchscreen, GPIO for ATX power, microSD expansion
  - Open source: KVM UI is a [fork of JetKVM](https://github.com/luckfox-eng29/kvm) (GPLv2), and they provide [hardware schematics](https://github.com/LuckfoxTECH/luckfox-pico)

## LeafKVM

{{< figure
  src="./TODO"
  alt="TODO"
  width="700"
  height="auto"
  class="insert-image"
>}}

Another KVM that built off JetKVM's software is the [LeafKVM](https://kvm.rs). But unlike the JetKVM, it built in a larger display, and added one feature I haven't seen anywhere else: a VGA adapter that doesn't need extra power. You have to buy their adapter, and it only works with the LeafKVM, but it worked perfectly on my old Xserves. Those things only have two USB ports on the back, so using one for a VGA power adapter is kinda wasteful.

The big problem I have with LeafKVM, at least for my rackmount use, is that ports go out both sides. It's kinda like the Raspberry Pi: no matter what, you're gonna have cables splayed out all over the place. This also means it's less useful for rackmounting.

But it's just finishing up a crowdfunding campaign on Crowd Supply, where it's $120 right now.

  - $120 on [CrowdSupply](https://www.crowdsupply.com/leafkvm/leafkvm), price increase after campaign ends
  - Chipset: RV1126B
  - Topline features: 4K 30fps (or 1080p 90fps), microSD storage, IPS touchscreen, WiFi built in, HDMI preview on device, optional ATX power control, PoE support (option), special VGA to HDMI adapter that doesn't require extra power (when used with LeafKVM), as well as RustDesk support in software
  - Open Source: hardware planned on CERN-OHL-HW license, software build scripts "will be provided", UI forked from JetKVM

## TinyPilot Voyager 3

{{< figure
  src="./TODO"
  alt="TODO"
  width="700"
  height="auto"
  class="insert-image"
>}}

Now getting back to a PiKVM-style Pi-based device, [TinyPilot](https://tinypilotkvm.com/products/tinypilot-voyager-3) is another box I've covered before, except they're up to the Voyager 3 now. Their 3rd generation hardware is even easier to set up, and it's even laid out in a more thoughtful box, compared to some other solutions.

I think TinyPilot targets more the business side users than a hobbyist looking to save a few bucks, judging by the price and how they have licensing and management set up. It's still good to see this thing kicking around after a few years, and I think features like Role-Based Access Control and better warranties help.

They also partnered up for sales in Canada, Europe _and_ the US, meaning it's easier to get these units wherever you are, especially compared to some of the cheap Chinese options.

And finally, they're building out a central management system that you can self-host; it's still in beta, but I got it working through my Mac running in Docker.

  - $379.00 on [TinyPilot Store](https://tinypilotkvm.com/products/tinypilot-voyager-3) ($499.00 for PoE + 2nd LAN)
  - Chipset: BCM2711 (Pi CM4)
  - Topline features: Web access, 1080p60, built-in status LCD, HDMI passthrough, metal case, rackmount options, RBAC with up to 8 simultaneous users, 1-year warranty (with options for extended warranties, up to 4 year), ships from North Carolina, USA, or Ontario Canada, available through CDW, Insight, SHI, DigiKey, Amazon Business, or in Europe through Welectron — bottom line, built for business use, probably not the best option for individuals running it in a homelab
  - Open source: Community version is free, MIT-licensed. Pro license is perpetual per device.

## Openterface KVM-GO

{{< figure
  src="./TODO"
  alt="TODO"
  width="700"
  height="auto"
  class="insert-image"
>}}

At this point, all these KVMs have been what I'd call 'traditional' IP KVMs, where you plug them into Ethernet and you can access a computer across your LAN.

But we're gonna take a little detour and look at [Openterface's KVM-GO](https://www.crowdsupply.com/techxartisan/openterface-kvm-go). It's meant to just plug one computer into another, like if you're in front of a rack with a tablet, and want to jack in. I've used it a few times for interfacing with my older machines and some servers, because it has a VGA port, but it can be a little awkward to get their control software running.

My favorite feature is these are all powered over the same USB-C connection you use for control, so you don't have to find an extra wall plug or even use PoE.

They have versions for direct connection to VGA, DisplayPort, or HDMI, and the kits cost about $120 each, or a little over $300 for all of 'em.

They also make a more generic [Mini KVM](https://www.crowdsupply.com/techxartisan/openterface-mini-kvm) for $99, but I haven't spent as much time testing that.

  - $119 for each kit, or $319 for full set on [Crowd Supply](https://www.crowdsupply.com/techxartisan/openterface-kvm-go)
  - Chipset: Macro Silicon MS2130S
  - Topline features: 4K at 30fps (default 1080p), Bluetooth for iPad use, aluminum alloy case, USB-C powered, microSD storage
  - Open source: OSHWA Certified after Crowdfunding
  - _Also have a Mini-KVM_ for $99 on [Crowd Supply](https://www.crowdsupply.com/techxartisan/openterface-mini-kvm)

## Sipeed NanoKVM USB / Pro

{{< figure
  src="./TODO"
  alt="TODO"
  width="700"
  height="auto"
  class="insert-image"
>}}

Speaking of USB, Sipeed also makes [USB versions of their NanoKVM](https://www.aliexpress.us/item/3256808188117625.html), also for around $100. I don't have one of these, but I _do_ have a Pi-Cast.

  - $99 on [AliExpress](https://www.aliexpress.us/item/3256808188117625.html)
  - Chipset: SG2002 (I think)
  - Topline features: 4K at 30fps (60fps Pro), Aluminum Alloy case, HDMI passthrough, browser and desktop apps available
  - Open source: KVM UI source is [https://github.com/sipeed/NanoKVM-USB](https://github.com/sipeed/NanoKVM-USB) (GPLv3)

## Pi-Cast

{{< figure
  src="./TODO"
  alt="TODO"
  width="700"
  height="auto"
  class="insert-image"
>}}

I actually had some trouble getting the [Pi-Cast](https://www.crowdsupply.com/hackergadgets/pi-cast-kvm) working on my iPad. But basically, it's a PiKVM, but instead of accessing it over the LAN, you access it over a direct IP connection that's set up through the USB-C port you plug into your computer.

It's similar to the other USB KVMs I've mentioned, except it hosts its own little webserver, so you don't have to run special software on your computer.

But because it runs on a Pi, it's a bit more expensive, coming in at $214.

  - $214 on [CrowdSupply](https://www.crowdsupply.com/hackergadgets/pi-cast-kvm)
  - Chipset: BCM2711 (Pi CM4)
  - Topline features: 1080p at 60Hz, OLED status display, OTG port for direct connection to iPad, WiFi AP built-in, options for ATX control, PoE, LTE/5G, Dual-ATX KVM switch control
  - Open source: Software is PiKVM, Schematic available at https://github.com/hackergadgets/Pi-Cast-KVM

## DezKVM-Go

{{< figure
  src="./TODO"
  alt="TODO"
  width="700"
  height="auto"
  class="insert-image"
>}}

Way on the opposite side of the spectrum is this little guy. This is the [DezKVM-Go](https://www.tindie.com/products/tobychui/dezkvm-go-kvm-over-usb-device/), the cheapest KVM of the bunch, which also works through USB.

It's made by Toby Chui, and I'm sorry if I pronounced that wrong. But it's an open source hardware design, with a little open source web app you can either run off GitHub or self-host.

That means you don't even need an app on your iPhone or whatever, you can just run it in the browser. Well, at least if your browser is Chrome, Edge, or a recent version of FireFox.

This thing is so cheap because it relies on a this little HDMI to USB adapter. It muxes in keyboard and mouse control over USB, and you can control everything through WebSerial.

It worked great under Windows, but I did have some trouble in Ubuntu 26.04. I'm not sure if it's a Linux permissions thing or what, but just something to keep in mind.

If this were $200 I'd complain about that, but not for $25. For that, it's a neat little box that maybe more people could contribute to, to make it the most handy way to jack in from a crash cart.

  - $24.99 on [Tindie](https://www.tindie.com/products/tobychui/dezkvm-go-kvm-over-usb-device/)
  - Chipset: Uses 3rd party HDMI converter (MS2109), and generic USB chips
  - Topline features: Self-hosted or GitHub-hosted web UI, no app required; have to plug into a computer to use. WebSerial requires Chrome, Edge, or Firefox
    - Can be extended with DezKVM software with an SBC or miniPC to manage one or multiple systems over IP

  - Open source: Software is custom Go and JS, licensed as GPLv3. Hardware is Creative Commons non-commercial. [Toby Chui designed it](https://www.youtube.com/watch?v=bRKyux_CxCg).

## ArkKVM

{{< figure
  src="./TODO"
  alt="TODO"
  width="700"
  height="auto"
  class="insert-image"
>}}

The crowdfunded [ArkKVM](https://store.arkkvm.com/products/arkkvm-open-source-ip-kvm) looks like a JetKVM clone that fixes a few minor annoyances by using full-size HDMI and including PoE support out of the box.

  - $99 on [ArkKVM store](https://store.arkkvm.com/products/arkkvm-open-source-ip-kvm)
  - Chipset: RV1106B
  - Topline features: Almost a clone of the JetKVM, fixing a few shortcomings, but without any screws. Screws can be nice for hard mounting like in racks.
  - Open source: ArkKVM told me they'll be releasing the Rust code for the UI and the image sometime in June, but time will tell. I know some companies are better about it than others: [https://github.com/arkkvm](https://github.com/arkkvm)

## Conclusion

Now I tried to just give you the overview of each of these KVMs, but I guess if you have to choose one, the key is to put together a list of the things you _have_ to have.

Like for me, the main thing I want is having all the ports on one side, to make it easier to put in a rack or keep cables managed. That rules out a few of these units, but that might not be as important in your use case. Maybe you need better latency, or 4K support. Those things aren't as important to me.

And I always like a good value; slapping a $400 remote control box on a $300 mini PC is a bit much, but maybe you need a special feature like backup 5G Internet.

I will say, the KVM I use the most around the Studio is the JetKVM. It's tiny, bus-powered, and simple. And most of the time, that's what I need.

A lot of features are still being actively developed, like on the JetKVM it looks like it's finally getting audio support a year after launch. So look at the links I put in the description for the latest specs.

I mean, even while I was making this video, GL-iNet announced _more_ KVMs, the [Comet Q](https://www.kickstarter.com/projects/glinet/comet-q) for USB control, and [Comet X](https://www.gl-inet.com/products/gl-rm4pe/) with a built-in 4-computer switcher. Then there's [ArkKVM](https://store.arkkvm.com/products/arkkvm-open-source-ip-kvm), which looks like a JetKVM clone that fixes a few minor annoyances like using full-size HDMI and including PoE support out of the box.

Bottom line: the market for these things is booming, and there are probably more IP KVMs on the market by the time you're watching this.
