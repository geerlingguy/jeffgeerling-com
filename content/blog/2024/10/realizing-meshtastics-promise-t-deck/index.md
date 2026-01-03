---
nid: 3411
title: "Realizing Meshtastic's Promise with the T-Deck"
slug: "realizing-meshtastics-promise-t-deck"
date: 2024-10-11T14:35:11+00:00
drupal:
  nid: 3411
  path: /blog/2024/realizing-meshtastics-promise-t-deck
  body_format: markdown
  redirects: []
tags:
  - communications
  - esp32
  - meshtastic
  - node
  - radio
  - tutorial
---

[Meshtastic](https://meshtastic.org)—a simple off-grid mesh network used to transfer short messages—is a neat bit of tech, but until recently, most development has focused on little nodes with or without tiny OLED displays, and a separate phone app or web UI to actually _interact_ with the mesh.

The major use case I have for Meshtastic is backup comms—when cell networks and physical infrastructure may be unavailable. In those conditions, I don't want to run my full computer, or even a full smartphone, just to communicate long range via text.

Enter the T-Deck:

{{< figure src="./lilygo-t-deck-on-workbench-new-firmware.jpeg" alt="Lilygo T-Deck running experimental UI Meshtastic firmware" width="700" height="auto" class="insert-image" >}}

If the Meshtastic community could focus on a few 'halo' devices like this, I think general Meshtastic adoption will increase a lot further. The current state of Meshtastic, where you typically buy a tiny node and then use it with your phone or computer, relegates the tech to an existing base of radio enthusiasts, mostly.[^caveat]

Often when I post about Meshtastic, I get the response: "I thought it was supposed to be off-grid. Doesn't requiring an app that has to be downloaded from an online App Store make that kinda impossible?"

_Yes, yes it does._

And forget about trying to explain how local Bluetooth or WiFi connections don't require a working Internet connection, you've already lost most people's interest by that point.

Which is why I love the T-Deck—it has it's warts, but it's the first truly-standalone Meshtastic node that would be useful to me in an emergency, especially with a 5000 mAh battery that lasts a few days!

Not only that, it still retains the ability to interface with the phone app and self-hosts a Web UI over WiFi for advanced configuration and chat.

But the UI is currently _trash_. At least if you want adoption from anyone outside the world of arcane RF and ham enthusiasts used to QRPing and DXing.

> **Video version**: I have a video version of this blog post as well: [This device makes Meshtastic the BEST off-grid tech](https://www.youtube.com/watch?v=2Ry-ck0fhfw)

## Installing the official Meshtastic UI

The official [Meshtastic UI](https://meshtastic.org/docs/software/meshtastic-ui/) is now available for the T-Deck, available directly through the [Meshtastic Web Flasher](https://flasher.meshtastic.org), as long as you flash a 2.6.x firmware, and select the 'Meshtastic UI' option.

To flash your T-Deck:

1. Open the [Meshtastic Web Flasher](https://flasher.meshtastic.org)
1. Select the T-Deck for the device, the latest firmware version (e.g. 2.6.x beta), and click Flash
1. Click 'Continue' after reading through the firmware notes
1. Select the options "Full Erase and Install" and "Meshtastic UI" (_you can skip the full erase if you're just updating to a slightly newer firmware with the UI built in already_)
1. Turn off your T-Deck. Hold down the little ball button and turn it back on, holding down the ball. Keep holding it at least 3-5 seconds.
1. Plug the T-Deck into your computer, and click the "Erase Flash and Install" button
1. Select the 'J-tag' device when prompted.

These instructions are subject to change, of course. Check the Meshtastic docs for full instructions!

## Installing the Experimental T-Deck UI

> **NOTE**: This section of the blog post is mostly obsolete if you just use the official Meshtastic UI as I outline above. But I'm still including it for completeness!

I've seen murmurs around an experimental T-Deck UI; some people posted about it on Reddit, some in random YouTube video comments. And a quick DDG search brings up [this YouTube Short](https://www.youtube.com/watch?v=N_RQlKSPHbM)... which said 'here's the tutorial', but I couldn't figure out where it was, until I dug into the comments and figured out the Short was using a 'long form video link' which doesn't show on YouTube's desktop layout!

So I eventually found the [full tutorial video](https://www.youtube.com/watch?v=I2g5vr_GtbA), but the actual instructions were buried in the description with little formatting.

So I've re-written the guide for flashing the experimental [device-ui](https://github.com/meshtastic/device-ui) onto the T-Deck:

Download the latest 'fancy T-Deck' build from [here](https://github.com/meshtastic/firmware/actions/runs/11085070443), specifically, the `firmware-2.5.3.bfe99b2.zip` artifact.

> **Note**: This CI-generated build linked above will vanish after 90 days—according to Meshtastic devs, [people kept filing support requests against these experimental builds](https://github.com/meshtastic/firmware/pull/3259#issuecomment-2399143334), so **first and most important**: _don't do that!_
> 
> And second, it looks like at some point you'll need to start building your own images. I'll maybe update this guide to show you how to do that too :)

1. Set the T-Deck into flashing mode: hold down the center trackball while turning on the power switch.
1. Visit [https://flasher.meshtastic.org/](https://flasher.meshtastic.org/) and install `firmware-2.5.3.bfe99b2.zip` (select "Full erase and install").
1. Close out of the Meshtastic flasher and visit [https://esp.huhn.me/](https://esp.huhn.me/) and connect to your T-Deck.
1. Expand `firmware-2.5.3.bfe99b2.zip` and next to the 0x10000 slot, select the `firmware-t-deck-2.5.3.bfe99b2-update.bin` file and click 'Program'.

Once it's done, follow it's instruction: `To run the new firmware please reset your device.`

> **Again, because I know some people will ignore the warning above**: Don't file support requests or waste Meshtastic contributors' time asking for support with the experimental UI firmware. This is just for testing at this point.

## Using the Experimental UI

{{< figure src="./lilygo-t-deck-meshtastic-chats.jpeg" alt="Lilygo T-Deck running experimental UI Meshtastic firmware - messages" width="700" height="auto" class="insert-image" >}}

There's a reason why this is considered experimental. It looks pretty, and the features that _are_ implemented, like the simple connected nodes listing, are already eons better (IMHO) than what you get even in the iOS app.

But there are many, _many_ features that are either not implemented or completely broken. Like a few, off the top of my head:

  - <s>Sending messages</s> (Apparently I forgot to set the region to `US`, oops!)
  - <s>Configuring channels</s> (See Manuel's comment below!)
  - Bluetooth access so my phone app can use the device

There is a lot that _does_ work, though—even some of the simple things that leave a great first impression, like a boot screen, smooth scrolling (mostly), changing the alert tone, and other essential settings. It may seem silly to some people, but those surface-level bits of polish can really rope in first-time users.

Would I recommend you go out and buy a T-Deck and flash this firmware to it? Not yet. The default firmware has more functionality just by virtue of being able to be used over Bluetooth/WiFi—on device functionality is extremely limited because it's mostly [hidden behind arcane key combos](https://meshtastic.org/docs/hardware/devices/lilygo/tdeck/#keyboard-shortcuts).

I think Lilygo's acknowledged the popularity of the T-Deck for Meshtastic, so much so they've built out the [T-Deck Plus](https://www.lilygo.cc/products/t-deck-plus), which includes everything you need pre-built (and pre-flashed, albeit with the default firmware) so you can get up and running without needing a 3D printer or even a separate computer!

[^caveat]: Yes, I know there is a place for many different types of nodes... but Meshtastic's ultimate success is based on getting more people to join the mesh—without geographically-distributed nodes and some people putting nodes higher up, you won't get widespread coverage and the utility is greatly reduced. Just relying on ham/RF enthusiasts (which is kinda where I see Meshtastic today) won't get any kind of critical mass, you have to target other people too. Get them interested on a base level, then start getting them interested in setting up router nodes, being part of the community, etc. :)
