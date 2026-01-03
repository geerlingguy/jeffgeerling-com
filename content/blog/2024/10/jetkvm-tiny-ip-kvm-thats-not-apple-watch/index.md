---
nid: 3413
title: "JetKVM: tiny IP KVM that's not an Apple Watch"
slug: "jetkvm-tiny-ip-kvm-thats-not-apple-watch"
date: 2024-10-26T14:09:53+00:00
drupal:
  nid: 3413
  path: /blog/2024/jetkvm-tiny-ip-kvm-thats-not-apple-watch
  body_format: markdown
  redirects:
    - /blog/2024/jetkvm-ip-kvm-thats-not-apple-watch
aliases:
  - /blog/2024/jetkvm-ip-kvm-thats-not-apple-watch
tags:
  - homelab
  - jetkvm
  - kickstarter
  - kvm
  - pi-kvm
  - video
  - youtube
---

{{< figure src="./jetkvm-running.jpeg" alt="JetKVM running" width="700" height="auto" class="insert-image" >}}

Despite what it looks like, this _isn't_ a hot-rod Apple Watch. This is an IP KVM. What does that mean? It's basically a remote control rocket pack for any computer, from a giant tower PC, to a little mini PC you might run in your homelab.

It's called [JetKVM](https://jetkvm.com), and the team behind it sent me two to test out.

> **BIG SCARY DISCLAIMER**: The JetKVM is [currently on Kickstarter](https://www.kickstarter.com/projects/jetkvm/jetkvm). If you decide to back it, and they don't deliver, that's... actually pretty common. I _did_ back their Kickstarter, and I _think_ they'll deliver, but there are no guarantees.
> 
> BuildJet did _not_ pay for this post, and I am _not_ sharing in any profit, or even using an affiliate link. I just saw this tiny KVM come across my feed, thought it looked amazing, and asked if I could test it out.

## How does it work?

{{< figure src="./jetkvm-plug-in-ethernet-mini-pc.jpg" alt="JetKVM plug in Ethernet for mini PC" width="700" height="auto" class="insert-image" >}}

First, you plug in your computer's HDMI to the mini HDMI input, and they include a thin adapter cable since most people don't have mini HDMI. Then you plug in USB to one of your computer's USB-A ports (using the supplied USB-C to USB-A cable).

This should power it up, at least if your computer always provides power to USB—some computers don't, and I'll talk about that scenario later. But the last step is to plug the Ethernet port into your network.

After a few seconds, you should see an IP address on the screen. Visit that IP address, and you'll see the JetKVM interface.

It walks you through setting an optional admin password, and then dumps you right into the remote admin UI.

<blockquote><p><strong>Note</strong>: This blog post goes along with a video on my YouTube channel. Watch the video for more on the actual performance and usage; it's hard to convey that information with the text of a blog post.</p>

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/6pYfHedjjgw" frameborder='0' allowfullscreen></iframe></div>
</div>
</blockquote>

## Why IP KVM

Now, every time I post a video about an IP KVM, someone asks me why they'd need one, instead of just using Remote Desktop Connection or VNC. Raspberry Pi even launched [Pi Connect](https://www.raspberrypi.com/software/connect/) this year!

Well, this goes a level deeper. Instead of requiring software running on your computer, it's completely independent. That means it can work even when your computer's shut down or locked up. It can also send out magic 'Wake on LAN' packets to wake up other computers, even if your main computer's off.

And it can do things like mount virtual disk images and help you reinstall an OS on a computer that you can't get to easily.

Those features are usually built into enterprise servers, under the name IPMI, iDRAC, iLO, or the like.

But the JetKVM puts out of band management into the hands of homelabbers. All this is worthless, though, without fast, secure software.

## Software

{{< figure src="./jetkvm-ui-check-for-updates.jpg" alt="JetKVM UI - Check for updates" width="700" height="auto" class="insert-image" >}}

I love how simple the web UI is. It's like the first time I used [Pi-KVM](https://pikvm.org); the UI is pretty easy to pick up, it has all the tools I need, and it works well on my laptop or on a larger desktop.

It also tucks away a few handy tools, like live connection metrics for latency, jitter, and fps.

You can choose from different EDID monitor emulation options, you have controls for how the mouse works, and it has all the standard KVM features like a virtual keyboard or full-screen.

One feature I _haven't_ tested is ATX power control. I'm guessing there'll be a little menu for pressing the power button or reset, but I haven't seen it yet.

It also has the ability to mount virtual disk images, but it takes that feature a little further. In addition to install discs like you would on other IP KVMs, there's built-in [Netboot.XYZ](https://netboot.xyz) support, so you can boot a remote computer through the network.

I haven't tested that out, but I did test mounting ISOs.

I decided to try out upgrading my [GMKtec N100 mini PC](https://amzn.to/3YD43H2) from Windows 11 to Linux.

Normally I'd use [Ventoy](https://www.ventoy.net) to install an OS, but with JetKVM, I mounted a Debian 12 image and installed a fresh copy of Linux. And I could do this anywhere. I don't have to touch the computer at all.

But while I was rebooting into the BIOS, I realized the mini PC behaves like a Raspberry Pi: when you shut it down, it cuts power to the USB ports. My streaming PC doesn't do that, but this one does, so I had to use a [USB-C power splitter](https://wiki.blicube.com/blikvm/en/usb-splitter-guide/). It supplies constant power to JetKVM even when the mini PC's off.

In terms of keeping itself up to date, JetKVM comes with over-the-air automatic updates enabled. That's easy enough to turn off, though, and you can either manually check for updates, or just ignore them completely, if you want flash your own OS to it.

I did test out an OTA update by switching to the dev channel, and again, I was impressed by the level of polish. There's actual _progress bars_ and meaningful status information, not a blank popup that stares at you for five minutes until the update's complete.

[JetKVM promised](https://jetkvm.com/docs/getting-started/open-source) to release all the code under a GPL open source license in December, when they start shipping. That means you could modify their code and build your own images if you want.

And for those interested, here's how the device enumerates (as of today, with beta software) on your computer's USB bus:

```
# lsusb output:
Bus 001 Device 002: ID 1d6b:0044 Linux Foundation JetKVM USB Emulation Device

# dmesg output during boot:
[   16.932585] usb 1-1: New USB device found, idVendor=1d6b, idProduct=0044, bcdDevice= 0.40
[   17.792471] input: JetKVM JetKVM USB Emulation Device as /devices/pci0003:00/0003:00:01.0/0003:01:00.0/usb1/1-1/1-1:1.0/0003:1D6B:0044.0001/input/input1
[   17.858183] hid-generic 0003:1D6B:0044.0001: input,hidraw0: USB HID v1.01 Keyboard [JetKVM JetKVM USB Emulation Device] on usb-0003:01:00.0-1/input0
[   17.871554] input: JetKVM JetKVM USB Emulation Device as /devices/pci0003:00/0003:00:01.0/0003:01:00.0/usb1/1-1/1-1:1.1/0003:1D6B:0044.0002/input/input2
[   17.893520] hid-generic 0003:1D6B:0044.0002: input,hidraw1: USB HID v1.01 Mouse [JetKVM JetKVM USB Emulation Device] on usb-0003:01:00.0-1/input1
```

So the software for this thing is nearly as full-featured as Pi-KVM, the gold standard for open source KVMs. And it's polished, too. Outside a few small layout bugs, I had no problems controlling a variety of computers.

## Hardware

{{< figure src="./jetkvm-side-profile.jpg" alt="JetKVM - Side profile" width="700" height="auto" class="insert-image" >}}

Taking a look at the outside, two things struck me right away. First, the front display looks like an Apple Watch. And second, when I hold the thing, it's heavy—in a good way.

I asked Adam, one of the co-founders, if he could share more about how they made these things, because the level of polish is a lot better than most homelab stuff I use.

He said the main body and back cover are a die-cast zinc alloy, specifically ZAMAK 7, with 5% aluminum and 95% zinc. They [take those castings](https://www.youtube.com/shorts/sVds6tW8PIA) and use CNC machines to get a nicer finish.

They add a copper plating, and give it a polished gunmetal grey finish.

Apparently to do all that, they had to order a batch of 5,000 cases, which I hope means they also have a ton of these ready to go.

{{< figure src="./jetkvm-watch-prototype-design.jpg" alt="JetKVM smart watch prototype UI" width="600" height="auto" class="insert-image" >}}

The screen is an off-the-shelf component used in some smart watches. That means it (a), does look kinda like an Apple Watch, but more importantly (b), doesn't have an Apple Watch price tag.

Apparently their first UI prototyping was done on this smartwatch, which is probably what led them to using the display.

All that to say, this is one of the nicest homelab devices I've seen, it's a huge improvement over the [NanoKVM](/blog/2024/sipeed-nanokvm-risc-v-stick-on). That thing has a lightweight plastic body and doesn't stay put when it's plugged in. But, it is cheaper.

JetKVM also includes thin, flexible HDMI and USB cables. Pair that with [slimline Ethernet](https://amzn.to/4eO6oVj) and you won't have to worry about it flying off your desk.

{{< figure src="./jetkvm-pcb.jpeg" alt="JetKVM PCB" width="700" height="auto" class="insert-image" >}}

The nice design extends to the inside. JetKVM actually sent the PCB pictured above straight from the assembly line, so I can show you how it looks before installation.

It's powered by a [Rockchip RV1106G3](https://www.lcsc.com/datasheet/lcsc_datasheet_2405141706_Rockchip-RV1106G3_C5328706.pdf), the same chip used in some Luckfox boards.

This chip is meant for camera applications, and it has a single Arm Cortex-A7 core. It's not fast, but it's plenty fast to run a simple web UI. The more important feature is it has almost everything this board needs built in.

It has hardware-accelerated HEVC and H.264 video encoding, embedded 10/100 Ethernet, and integrated RAM—256 megs of DDR3L, to be precise.

There's an [8 gig eMMC chip](https://semiconductor.samsung.com/estorage/emmc/emmc-5-1/klm8g1getf-b041/) for storage. In the middle, there's a Toshiba chip that converts HDMI to CSI. This translates the video signal from your computer into something the Rockchip can understand.

On the bottom there's a little PMIC (Power Management IC) chip, with two inputs. And it looks like right now one input is wired into 5V USB power from your computer, and the other one goes to the RJ11 extension jack. I'm guessing a dongle could supply aux power if your computer doesn't always provide power over USB, like my GMKtec.

The two main hardware gotchas are mini HDMI and the 10/100 Ethernet port.

Both are _fine_, but they do come with a tradeoff. For mini HDMI, most people don't have mini HDMI cables, but luckily JetKVM includes a thin HDMI adapter cable.

And the Ethernet port has the same problem I mentioned on my NanoKVM review: it should work with _most_ switches, but there are some scenarios with newer network switches where they might not play nice at 100 Megabits.

## Latency Test

The big question is how well this thing can perform, with such a tiny, low-power processor.

{{< figure src="./jetkvm-latency-test-80ms.jpg" alt="JetKVM latency test - 80ms" width="700" height="auto" class="insert-image" >}}

For this test, I have an [HDMI splitter](https://amzn.to/4eUJUSt) plugged into my streaming PC. The splitter has port 1 plugged into the JetKVM, which sets the display mode to 1080p, and port 2 is plugged into my gaming monitor on my desk.

I have JetKVM up on my Mac (in the left of the above photo), and the monitor on the right is wired straight into the splitter.

I can run a latency test by setting up a large millisecond timer on the display. Recording in 120 frames per second, I can count frames between when the picture updates on the monitor versus through JetKVM[^wendell].

Doing that, it looks like there's consistently around 80-100 milliseconds of lag, at least on my local network.

I didn't do the same test over a separate network, like through my VPN, but day to day, for the things this is intended for, the latency is perfectly fine.

I could even watch a video on YouTube through it, except, there's a bigger problem with that: no sound!

If you intend to play video games off a console, or to replace Parsec or Moonlight, that's not going to work.

Plus, gaming through this has it's own problems. Like in Halo Infinite, absolute mouse positioning means you can't use the mouse to look around. Eventually, JetKVM will support relative positioning, and that _should_ fix _that_ issue. But don't buy this for remote FPS gaming. It's not made for that at all!

## What it lacks?

{{< figure src="./jetkvm-rear-ports_0.jpeg" alt="JetKVM rear ports" width="700" height="auto" class="insert-image" >}}

This little box certainly isn't perfect; there's tradeoffs with every KVM. In this case, it doesn't have WiFi, so you have to have wired Ethernet. And there's no built-in PoE support, though you could add on a PoE splitter if you want.

And I haven't been able to test any of their RJ11 extensions yet. They said they'll have a few ready for launch.

An ATX power control extension would allow you to emulate a power button press on a PC or server. A DC power control extension would allow you to cut power to a mini PC like this one, since it doesn't have power switch headers.

And eventually they'll have a serial console extension too.

The other thing that's currently lacking is a rackmount adapter, or even a silicon sleeve to hold it in place better. But they do have a [3D model available](https://jetkvm.com/docs/advanced-usage/3d-model), so designing an enclosure might not be too hard.

The last thing missing is dark mode support in the UI. They said Dark Mode might happen in the future; right now they're focused on nailing the rest of the UI.

## Security and Remote / Cloud Access

The last thing I'll talk about is remote access. For myself, I have site VPNs set up at my studio and at home. So if I need remote access, I connect to my VPN, and act like I'm sitting in the building.

But if you _don't_ have that, JetKVM has a free [JetKVM Cloud](https://app.jetkvm.com/) option. You can read more about how it works [in their docs](https://jetkvm.com/docs/networking/remote-access), but the bottom line is it's there if you want it, but it's not required. And it's not even enabled by default.

{{< figure src="./jetkvm-cloud-1000px.jpg" alt="JetKVM Cloud dashboard" width="500" height="auto" class="insert-image" >}}

I did test it out, and after logging in with my Google account (other identity providers may be added after launch), I could add my JetKVM and access it anywhere. Their software handles punching through firewalls, but honestly, if you have any questions about their security or their zero-trust setup, they'll have their GitHub issues open, and they've been pretty responsive on Discord too.

You can also enable Developer Mode to get [SSH access](https://jetkvm.com/docs/networking/local-access#option-1-developer-mode). Using that, you could get in and probably set up something like Tailscale.

And like I said, they promised to [release all the software under a GPL license in December](https://www.kickstarter.com/projects/jetkvm/jetkvm/posts/4218934) when they start shipping.

BUT, and this is a huge caveat: **this is a Kickstarter**. If I had a nickel for every time I backed something on Kickstarter and never got anything out of it... well, I'd at least have 10 cents.

But that's a risk with Kickstarter. If you don't like the idea of throwing your money into the void, just wait. Patience is rewarded. If they're successful, I'm sure they'll be selling these things like hotcakes after they ship to all the backers.

And if you're concerned about the security implications of a tiny device like this giving full remote access to your computer?

Well yeah... that's why safeguarding your physical infrastructure is so important. If a bad actor has physical access to any of your machines, it's game over. That's why a lot of companies disable USB ports entirely.

## Conclusion

In the end, it's a Kickstarter. All the usual Kickstarter caveats apply. It's no skin off my back if you support it or don't support it—I get absolutely nothing either way, and the Kickstarter's already been funded.

I just love seeing creative new takes on an old idea, and this is nothing if not that. The [PiKVM](https://pikvm.org/buy/) still exists, and has its own tricks, like you can pop in a Cellular modem for backup Internet.

And the [NanoKVM](https://github.com/sipeed/NanoKVM) also still exists, with it's own upsides and downsides. I covered the NanoKVM just [a few weeks ago](https://www.jeffgeerling.com/blog/2024/sipeed-nanokvm-risc-v-stick-on).

But JetKVM has a bright future. Hopefully they can develop a v2 with PoE support built-in!

[^wendell]: Thanks to Wendell from Level1Techs for _that_ trick!
