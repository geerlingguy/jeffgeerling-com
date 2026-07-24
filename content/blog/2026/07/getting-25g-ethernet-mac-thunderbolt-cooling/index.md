---
draft: true
date: '2026-07-30T09:00:00-05:00'
tags: ['thunderbolt', '25g', 'ethernet', 'mac', 'macos', 'noctua', 'youtube', 'video', 'tutorial', '3d printing']
title: 'Getting 25 Gbps Thunderbolt Ethernet on my Mac Studio'
slug: 'getting-25g-ethernet-mac-thunderbolt'
---
Mentioned in this blog post:

  - Generic OCP 25G Thunderbolt Adapter: https://amzn.to/4vGLjDG
  - Dual 25GbE TB Dock: https://store.raidendigit.com/products/lightone-25gbe-thunderbolt-docking-station
  - Sonnet Twin25G: https://amzn.to/4tVqlAM
  - Atto ThunderLink: https://amzn.to/48Tj0cG
  - Blog post where I found out about the 25G adapter: https://kohlschuetter.github.io/blog/posts/2026/01/27/tb25/
  - Aluminum Heatsinks: https://amzn.to/48DSiVn
  - Noctua NF-A8 80mm 5V fan: https://amzn.to/4gUpZqK
  - Noctua NA-FC1 Speed Controller: https://amzn.to/4vQq8iB
  - Generic USB 5V fan (louder but cheaper): https://amzn.to/4cCM6OS
  - 3D print - 80mm fan duct: https://www.printables.com/model/1789472-80mm-fan-mod-for-25g-thunderbolt-nic
  - 3D print - Noctua 80mm fan grill: https://www.printables.com/model/1098017-high-efficiency-noctua-80mm-fan-grill

TODO: PHoto of mac back port

I've been using the 10 gig Ethernet port on my Mac Studio. I can edit 4K video straight off my NAS over the network. I can also run backups at like a gigabyte per second.

But... I want _more_. I upgraded my rack and my NAS to 25 gigs a couple years ago, but nothing else in the Studio takes advantage of it yet.

I looked up 25 gig networking options for the Mac, and they're all _crazy_ expensive. Like [this Sonnet adapter](https://www.sonnetstore.com/products/twin25gt5-thunderbolt5-adapter) is a _thousand_ dollars. That's... way more than I'm willing to pay. But if you need it on a Mac, you _have_ to pay, because you can't just use PCI Express. You have to use Thunderbolt.

So I shelved the idea, until I saw [_this_ blog post](https://kohlschuetter.github.io/blog/posts/2026/01/27/tb25/). Someone found a cheap 25 gig Thunderbolt adapter that looks like it's using server-pull hardware with a little adapter board. And you can get it going on a Mac.

Back in January, it was only $160, which for me—that's an insta-buy. Since that time, it jumped up to $299, which still might be good compared to the Sonnet... but I don't blame you if 10 gigs is enough at that price point.

_This blog post is a companion to the following YouTube video:_

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/_--JjauL19A' frameborder='0' allowfullscreen></iframe></div>
</div>

## First Test - Two Problems to Solve

But before I could test 25 gigs, I actually had to run some new fiber to my desk. When I built out the studio, I ran fiber up to the front room, where I _thought_ I'd set up my desk.

But then once I moved in, I realized the studio space was a way better environment for sound. So I set up shop in here... where I only dropped Cat6A, which is only good for 10 gigs.

After I pulled some fiber, I wound up plugging in this short patch cable, which has been there for a couple months now. I'm sure if you subscribe to Level 2 Jeff, you've seen it a few times. Well, while recording this video, I finally fixed that by buying a 5 meter cable and putting it in the cable channel. Much better.

But with that direct 25 gig fiber connection, I tested the bandwidth. That's when I ran into two problems:

First, the version of iperf3 I was running on the NAS was too old. Multi-threading wasn't working, so no matter what, I was TCPmaxxing around 15 gigabits.

And second, the enclosure was getting _hot_. Like... I completely forgot to get footage before I stuck on these heatsinks, but it was painful to touch it.

I could solve the first problem pretty easily, though; I just compiled the latest version of iperf3. That got me to 20 gigabits, since more than one CPU core could hand the transfers on my NAS. But the second problem... that was a little more tricky.

You see, the enclosure got hot, but it wasn't even thermally bonded to the OCP 2 network card that was running inside! That means the actual chips that handle the network traffic? Those things were _cooking_.

And they had little heatsinks on them, but these things are meant to be inside servers with high pressure fans like this one, not in a little passively-cooled enclosure.

It was basically acting like a little oven.

## Fixing the Heating issue

Now in that original blog post, Christian mentioned he slapped a couple giant heatsinks on the enclosure. That brought the chip down to a temperature it wasn't cooking itself, but it was still getting pretty hot.

I wanted to make sure things were stable, because this is my main workstation, and there are times I'll be pushing through 25 gigs for minutes, maybe even _hours_ at a time. And that meant active cooling.

[hold: USB fan]

My first idea was to just set this fan in front of the thing, with a couple small heatsinks.

That _kinda_ worked, but it would still get a little hot. Plus, the fan was just loud enough to be distracting, even on its lowest setting.

And it was right around this time that Prusa actually sent me an email, asking if I wanted to try out some of their new filament they worked on with Noctua, to match the color of their fans.

I had just finished upgrading my MK4 to an MK4S with my son, and they also offered to send a Core One if I wanted to test their latest and greatest. And that was an offer I couldn't refuse, so here's what I did.

I printed this prototype fan cowling in orange since I was still waiting on the Noctua spools after the Core One showed up.

I made it so you take off one side of the enclosure, screw this shroud on, and screw in an 80mm fan. It fits together nicely, but there were a couple small issues. One was this little gap between the fan and the shroud. I know from past experience, air has a funny way of not pushing through higher pressure zones if you give it room to escape. So that has to go.

The other was this USB cable for fan power, which just looks bad. So I tweaked the final design a bit to make the fan flush, and here's that version. I printed it in Noctua's beige-colored PLA, along with a Noctua-brown fan grill. It printed perfectly, though I did have a few gripes with the Core One I'll get to in a separate video.

For power, though, I figured there has to be a way to tap into the NIC's power supply, right?

I probed around and found out I could get _almost_ 5 volts on these through holes over here. And _almost_ 5 volts should be good enough for a fan. Assuming it's a 5 volt fan and not a more standard 12 volt.

So I took a fan connector that came with my Noctua 80mm 5 volt fan, soldered its wires to the ground and 5 volt pin I found on the NIC, and tested it out just using a normal USB-C power supply.

It looks like the fan only used around half a watt as measured by my Sabrent power meter. So the next step was to put everything together.

I stuck on a braided fan connector I had cut down to size with some kapton tape, then I screwed everything back together.

[Noctua Fan Mod 19 Fan final assembly.MP4]

And it wouldn't be a networking project if I didn't end up slicing a finger? Right on the tip.

But I plugged it in, started running some iperf tests, and checked the temperature. It was sitting at less than 36°C after 10 minutes, with the fan on low. And this being a Noctua fan, I couldn't hear it at all under the desk.

But how does it actually _perform_, now that I went through all this work to keep it cool?

## How does 25 Gbps perform on the Mac?

Well, just like earlier, it maxes out around 20 to 25 Gigabits total, because of Thunderbolt limitations. Even if you have Thunderbolt 5, like I do, you're not gonna get any more bandwidth.

But testing samba file copies between my NAS and my Mac, I got around 1.4 gigabytes per second of read, and 1 gigabyte per second for write. Now the crazy thing is, that's only marginally better than the built-in 10 gig Ethernet. It's an improvement, sure... but was all the work pulling cable, designing a fan cowling, paying $200 for all the parts, and assembling everything worth it?

Maybe. At least I got this blog post out of it. And if you're watching this part, you're one of the like 30% of viewers who actually watch past the first 30 seconds, so thanks for that.
