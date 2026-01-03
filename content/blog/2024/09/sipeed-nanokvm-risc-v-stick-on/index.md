---
nid: 3403
title: "Sipeed NanoKVM: A RISC-V stick-on"
slug: "sipeed-nanokvm-risc-v-stick-on"
date: 2024-09-20T14:00:42+00:00
drupal:
  nid: 3403
  path: /blog/2024/sipeed-nanokvm-risc-v-stick-on
  body_format: markdown
  redirects: []
tags:
  - kvm
  - open source
  - pi-kvm
  - reviews
  - risc-v
  - sipeed
  - video
  - youtube
---

{{< figure src="./sipeed-nanokvm-box-contents.jpeg" alt="Sipeed NanoKVM" width="700" height="auto" class="insert-image" >}}

This is the [Sipeed NanoKVM](https://wiki.sipeed.com/hardware/en/kvm/NanoKVM/introduction.html). You stick it on your computer, plug in HDMI, USB, and the power button, and you get full remote control over the network—even if your computer locks up.

How did Sipeed make it so small, and so cheap? The 'full' kit above is about $50, while the cheapest competitors running PiKVM are closer to [$200](https://www.aliexpress.us/item/3256805673100994.html) and up!

_This blog post is a lightly-edited transcript of the following video on my YouTube channel:_

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/riDd6d0Vmy0" frameborder='0' allowfullscreen></iframe></div>
</div>

## IP-KVM

The Sipeed NanoKVM is the smallest IP KVM I've ever seen. The hardware is based around the tiny postage-stamp-sized [LicheeRV Nano](https://wiki.sipeed.com/hardware/en/lichee/RV_Nano/1_intro.html), with a tiny RISC-V [SG2002](https://milkv.io/chips/sg2002) SoC.

The extra boards added on top turn it into a KVM (Keyboard, Video and Mouse), and running over IP means you have total control over any computer or server you plug it into, over your network.

We'll get to how well it works later. But one question I get a lot is why use an IP KVM like this, at all? There's already software KVMs like Microsoft Remote Desktop, Apple's Screen Sharing, and even Raspberry Pi Connect.

Those are free and they work great.

Well, none of those work _at all_ when your computer's locked up. Or off. Or a thousand miles away and the power just tripped and there's an error message stopping it from booting back up.

{{< figure src="./sipeed-nanokvm-on-pc.jpeg" alt="Sipeed NanoKVM on PC" width="700" height="auto" class="insert-image" >}}

An IP KVM is a separate tiny computer that runs completely independent of the computer it's controlling. High end servers typically have this built in, and it's called something like [IPMI](https://en.wikipedia.org/wiki/Intelligent_Platform_Management_Interface), [iDRAC](https://www.dell.com/en-us/lp/dt/open-manage-idrac), or [lights-out or out-of-band management](https://en.wikipedia.org/wiki/Out-of-band_management). For example, the [Ampere server in my rack](/blog/2024/building-efficient-server-grade-arm-nas) runs OpenBMC, and I can login to it and get remote access. For sysadmins and homelabbers, it's useful to not have to walk around to all their servers to manage em.

But not every server has this built-in. Even if they do, some servers require expensive subscriptions or the vendor stops giving out security updates.

And old, unsupported remote access with full control of your servers? That's a security nightmare! Even with something newer, if you care about security, alarm bells are probably going off in your head.

If this tiny KVM can reboot your computer, go into the BIOS, and even install an OS, it's pretty dangerous to just let one of these live online, right?

Well, yeah. And that's one reason _security_ of IP KVMs, and the NanoKVM in particular, is under a lot of scrutiny.

## Security

So before we test it, let's get to the elephant in the room.

Unlike the other IP KVMs I've used before, like PiKVM, BliKVM, or TinyPilot, the NanoKVM runs its own proprietary OS.

And _right now_, at least, the source code isn't all open source. There's [a long issue about it on GitHub](https://github.com/sipeed/NanoKVM/issues/1), but the tl;dr? Sipeed said they won't open source the code until they either [sell 10,000 units or get 2,000 stars on the repository](https://github.com/sipeed/NanoKVM/issues/1#issuecomment-2278831374).

Why is this important? For other KVMs, even if they ship with a proprietary OS, you can usually get [PiKVM](https://pikvm.org) running. PiKVM is the gold standard of open source IP KVM software.

But PiKVM doesn't run on here—at least not yet.

And that's because the NanoKVM uses RISC-V. The CPU architecture is different, and some features aren't implemented the same as on the Arm CPUs used in the other KVMs.

Sipeed's working to get PiKVM built for RISC-V, but that's not ready yet, so right now, if you buy the NanoKVM, you'll likely run it with Sipeed's proprietary OS.

Why should you care? Well, some people don't, and that's fine. But since this product is made by a company in China, using a RISC-V chip and software built in China, some people get nervous about potential backdoors or security risks.

My iPhone was also made in China and runs a proprietary OS, but that OS was made by Apple, in the US. So it's a matter of trust.

But for anyone involved in open source, we trust software a lot more if we can build it ourselves.

So a wait and see approach might be best. I was concerned when one user [reported security holes in an earlier build](https://lichtlos.weblog.lol/2024/08/how-to-reverse-the-sipeed-nanokvm-firmware), but the community's already been [reverse-engineering the build](https://github.com/sipeed/NanoKVM/issues/1#issuecomment-2276781541), and Sipeed's fixed many of the issues in later versions of the OS. Also, GitHub user `scpcom` pointed out Dell doesn't release _all_ the code behind their iDRAC solution either!

But none of this matters _at all_ if this hardware is a dud. Debate security in the comments, but let me show you how it works.

## Testing with an SBC

{{< figure src="./sipeed-nanokvm-lichee-pi-3a.jpeg" alt="Sipeed NanoKVM plugged into Lichee Pi 3A" width="700" height="auto" class="insert-image" >}}

To test the NanoKVM, I plugged it into a [Lichee Pi 3A](https://github.com/geerlingguy/sbc-reviews/issues/50), a new SBC from Sipeed.

In the NanoKVM box (see photo at the top of this post), you get the NanoKVM itself, a little breakout board that plugs into your computer's front panel header, a USB cable to plug from that into the NanoKVM, and some jumper cables in case you need them. You have to supply your own USB-C power adapter, at least for now.

Someday they might have a PoE option too, and _technically_ you could run it straight off your computer's USB power, but that could lead to some issues, so I'd rather power it from my own adapter.

You plug in Ethernet, HDMI, and USB, and then plug in power to the USB-C aux port on the NanoKVM. It'll boot up, grab an IP address, and display everything on the built-in OLED.

{{< figure src="./sipeed-nanokvm-oled-display.jpeg" alt="Sipeed NanoKVM OLED display" width="700" height="auto" class="insert-image" >}}

Now this is the full $40 version, there's a light version without an OLED if you don't need it. But another nice feature of the full version is this enclosure, with a handy mapping of what all the ports do, and it even has a QR code that links straight to the wiki.

But if I go to IP address in my browser, I get the NanoKVM UI.

{{< figure src="./sipeed-nanokvm-linux-ui-keyboard.jpeg" alt="Sipeed NanoKVM Linux UI" width="700" height="auto" class="insert-image" >}}

Right away, I can remote control the Lichee Pi, just like I was plugged straight into it, and the latency is pretty good (estimated between 80-200ms). You won't be doing remote gaming on here, but it's fine for remote controlling a server or monitoring things.

The UI for NanoKVM is all tucked inside a bar overlaying the top of the screen. There are options for things like the resolution and quality of the stream. There are features like a virtual keyboard if you're on a tablet, and that works fine. Then there are options for different cursors, and options to mount ISOs or run user scripts.

There's also direct terminal access, so you can login as root to the KVM itself and run commands on it. (You can also login via SSH, which will come in handy later.)

There are power controls, an option to send a wake on lan packet to wake up a computer on the network, and there's even a built in serial terminal.

You can connect the NanoKVM to a serial port on any device, not just the computer it's hooked up to, and control it remotely. A handy feature, but I didn't have time to test it out yet.

If you don't need to access any of these settings, you can collapse the tray, but it stays on top of your display, which could be annoying if you need to click underneath it.

There's built-in integration with Tailscale, with [a guide for setting it up on the Wiki](https://wiki.sipeed.com/hardware/en/kvm/NanoKVM/network/tailscale.html). If you use Tailscale, you can access the NanoKVM from anywhere in the world. [Wireguard is also supported now](https://github.com/sipeed/NanoKVM/issues/29#issuecomment-2333184427). Remote access off your private network opens up its own security risks, but it's nice to have it supported up front.

## Fixing bugs

I mentioned earlier, SSH would come in handy. While I was testing, a firmware update came out with improved streaming quality and a few bug fixes, so I went to install it.

I used the 'Check for Update' option, but [I ran into this bug in the auto update feature](https://github.com/sipeed/NanoKVM/issues/42). Sipeed wrote a little Python script to force-update the firmware, and it could be downloaded and run through SSH.

That worked, but that's one issue I ran into testing this thing. I also discovered my Mikrotik switches (more specifically, the SFP adapters I use) only support 1, 2.5, 5, or 10 Gbps (not 10 or 100 Mbps). The NanoKVM only supports 100 Megabits, and some newer switches don't support that.

Then, I ran into some slowdowns running through some Nvidia graphics cards, which made it unusable. And one of my PC's motherboards just wouldn't boot because of a hardware bug I ran into, which Sipeed says will be fixed in the next hardware revision.

If your computer or SBC doesn't have USB port backfeed protection, a device like this can feed in 5 volts of power, leading to strange behavior.

And the version of the NanoKVM I'm testing [_does_ backfeed 5 volts](https://github.com/sipeed/NanoKVM/issues/40), so the Lichee Pi 3A I was testing had some weird boot issues until I unplugged USB.

{{< figure src="./sipeed-nanokvm-open-5v-resistor.jpeg" alt="Sipeed NanoKVM 5V resistor placement" width="700" height="auto" class="insert-image" >}}

There's a newer revision with a diode instead of a 0 ohm resistor, and I'll probably bodge mine with a diode there just to be safe, but that's one theme I see with this thing:

Sipeed is shipping NanoKVMs out already, but they need a little more time in the oven.

## Conclusion

The _idea_ of the NanoKVM is great. I'm used to paying at _least_ $150 for an IP KVM, usually more. At fifty bucks, I know a lotta people will just buy one without thinking. The price is right. But it needs a little more time before it can really deliver on its promise.

I really _want_ to recommend it. But I can't, at least not yet. If you wanna try it out in an isolated environment, go for it. You can even get a Lite version for $20 if you don't need power control!

But for anything mission-critical, I'd still recommend something like the [PiKVM v4](https://pikvm.org/buy/) or the [BliKVM](https://www.blicube.com/blikvm-v4-allwinner/). There are a bunch of options out there now, and it's cool to see the wild ideas people come up with. Like the BliKVM PCIe runs in a PCIe slot inside your computer. Or this Pi-Cast plugs straight into a tablet or laptop, no network required.

But most of those solutions are expensive, _and_ they're way larger. There's plenty of room in the market for the NanoKVM, so I hope it succeeds.
