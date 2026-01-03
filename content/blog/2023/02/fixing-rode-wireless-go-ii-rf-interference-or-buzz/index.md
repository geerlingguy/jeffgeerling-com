---
nid: 3271
title: "Fixing Rode Wireless Go II RF Interference or buzz"
slug: "fixing-rode-wireless-go-ii-rf-interference-or-buzz"
date: 2023-02-08T05:23:01+00:00
drupal:
  nid: 3271
  path: /blog/2023/fixing-rode-wireless-go-ii-rf-interference-or-buzz
  body_format: markdown
  redirects: []
tags:
  - audio
  - interference
  - microphone
  - recording
  - rf
  - rode
  - wireless
---

Recently I recorded an entire video for my YouTube channel using only a [Rode Wireless GO II](https://amzn.to/3YhYvza) lavaliere mic.

I typically spend the time to set up a second mic source—usually my shotgun mic into a separate recorder—but this time I was feeling lazy. I had never had an issue with the wireless lavs in my basement, and the Rode system includes a built-in recorder _in the bodypack transmitter_ so I have backup audio that has saved my bacon a few times when interference did cause cutouts to the camera input.

But because of that overconfidence, I had to reshoot the entire video (I tried [removing the RFI using iZotope RX 10](/blog/2023/removing-rf-interference-cell-phone-audio-recording), but there were parts where the interference was still too prominent). Lesson learned: always have the backup audio.

During the reshoot, I still relied on the lav for my primary mic, but it _still had the interference_, even though I set my phone and iPad into airplane mode, and made sure all WiFi devices within about 20' were powered off!

Luckily, I had the backup track from the overhead shotgun mic... but this puzzled me. I hadn't ever run into this problem with the Wireless Go II before—even in more noisy environments like [when I recorded this video with my Dad at a 330 kW radio transmitter site](https://www.youtube.com/watch?v=6_u8x8V4YYs)!

## Beware simple 'Soft' UIs

The problem, it turns out, was I had inadvertently enabled a 'Pad' setting on my transmitter.

The Wireless Go II receiver has three buttons, and those three buttons control about 12 different options. Because of that, some things are controlled by pressing one button a few times, then another. Others are controlled by pressing multiple buttons in combination for a period of time.

Well... since I only change settings maybe once a month, I never quite remember how to do something like switch from mono output (two mics into one channel) to stereo (one mic per channel), so I end up hitting random buttons different ways until I get the thing set how I like it.

{{< figure src="./rode-wireless-go-ii-pad-indicator.jpeg" alt="Rode Wireless Go II pad indicator RFI noise" width="700" height="394" class="insert-image" >}}

_See the little blue triangle next to channel 1? That's the 'Pad' indicator._

Unfortunately, one other thing I ended up doing was enabling 'Pad', which is not that well-documented on Rode's website. Pad turns down the level of the channel quite a bit, in case you have a microphone very near a person's mouth (or are using it for something like a musical instrument).

But doing so decreases the signal-to-noise ratio, meaning I have to turn the level up more for standard speech and normal mic placements (like on my lapel), thus exposing the tiny amounts of RFI that would otherwise be indiscernible in the recording.

Thanks to [this video](https://www.youtube.com/watch?v=PL9y3OMURTM), I learned of this new secondary pad feature that must've been added in a recent firmware update.

I turned off the pad, re-tested everything, and now there's no more RFI problem. The noise is still there, but my voice is now about 20dB stronger in the signal, so it's almost impossible to hear, even in silent portions with moderate compression.

## Pros need buttons and switches

There's a reason the [more expensive pro mics](https://amzn.to/3DSD7Z0) have more buttons (and usually more labels)—it's harder to mess something up if the interface is more intuitive.

This is also why I think it's a travesty that so many cars are following Tesla's lead and throwing soft UIs everywhere, where you just have a touchscreen and maybe a few buttons that change behavior depending on context.

Our human brains aren't made to cope with malleable user interfaces. They only work on things like smartphones and tablets because we focus our full attention on the screen.

At least the Wireless Go II still has a physical button 😛
