---
nid: 2900
title: "AirPods get stuck in low-quality 16 kHz audio mode when starting a VM"
slug: "airpods-get-stuck-low-quality-16-khz-audio-mode-when-starting-vm"
date: 2018-12-27T23:00:25+00:00
drupal:
  nid: 2900
  path: /blog/2018/airpods-get-stuck-low-quality-16-khz-audio-mode-when-starting-vm
  body_format: markdown
  redirects: []
tags:
  - airpods
  - apple
  - audio
  - bluetooth
  - mac
  - midi
  - phone
  - tutorial
  - utilities
---

I always love when I find a really dumb solution that works reliably to fix a problem that should never really be a problem in the first place. But having worked with audio devices before—though nothing nearly as complex as the AirPods—I am willing to cut Apple some slack in building a seamless aural experience with using AirPods across phone calls, VOIP, iOS devices, Macs, music, and Apple TVs... it's hard to execute perfectly, and as I said in my [review of the AirPods](/blog/2016/tale-two-apples) two years ago, these little earbuds are as close to perfection when it comes to a wireless sound solution for someone like me.

Anyways, here's the problem:

Sometimes (maybe 10% of the time) when I run `vagrant up` to build a local development environment for one of my software projects, and I'm listening to music, my AirPods suddenly switch into super-low-quality audio mode. It sounds like you're listening to a song played through a long subway tunnel or something.

What's happening behind the scenes is something in Vagrant or VirtualBox's boot sequence is making a change on the computer to assume some control over USB and/or audio IO, and that seems to—sometimes—affect the audio mode used by the AirPods.

This happens sometimes in other situations too; sometimes the AirPods switch to 'old POTS voice call quality mode' (as I call it) and stay there even after you hang up on a phone call. It often happens when you're using the AirPods' microphone with VOIP apps too.

Apple has some pretty awesome little utilities, though, which can help in these situations. As with last year's post, [How I discovered my left AirPod was bad](/blog/2017/how-i-discovered-my-left-airpod-was-bad), in which I discovered a handy Bluetooth device diagnostics tool called Bluetooth Explorer, I have long known about an essential built-in audio app on the Mac which has been around for years: [Audio MIDI Setup](https://support.apple.com/guide/audio-midi-setup/welcome/mac).

{{< figure src="./audio-midi-setup-app-icon.png" alt="Apple Audio Midi setup app icon" width="200" height="200" class="insert-image" >}}

By the name of the app (not to mention the icon—a music keyboard!), you wouldn't know that it's kind of a jack-of-all-trades when it comes to diagnosing and configuring almost any audio I/O aspect of your Mac, including surround sound inputs and outputs, microphone levels, output levels, and other specialized configuration. MIDI is really only a tiny part of what this app does!

This app can quickly highlight the problem that occurs when the AirPods get stuck in low-quality-output mode:

{{< figure src="./audio-midi-setup-airpod-16khz.png" alt="Audio MIDI Setup AirPod stuck at 16 kHz" width="650" height="476" class="insert-image" >}}

Basically, the AirPods get stuck playing the Bluetooth audio stream at 16 kHz, which is okay(ish) for voice calls, but sounds _terrible_ if you're listening to movies or music. Or anything, really, besides terrible quality audio streams or AM radio.

So after having this happen three times, I've found one solution which _doesn't_ require a reboot, which works _every_ time, restoring a pure, 48.0 kHz audio stream to the AirPods:

  1. Have some audio playing (e.g. play a song in iTunes)
  2. Open Audio MIDI Setup
  3. Select your Airpods in the list of devices (the one with 1 out or 2 outs)
  4. Toggle the 'Format' menu from "1 ch 16-bit..." to "2 ch 32-bit..."
      (Note that this will blip the audio for a few ms, but it will switch back)
  5. Keep Audio MIDI Setup open
  6. Disconnect your AirPods to your Mac using the Bluetooth menu
  7. Re-connect your AirPods to your Mac using the Bluetooth menu
  8. Wait for some playing audio to return to your AirPods—it will still be tinny and yucky sounding.
  9. Quit Audio MIDI Setup.

After Audio MIDI Setup quits, the audio should switch over to 32-bit/48 kHz mode again. No idea why, but hey, it works, and I don't have to reboot my entire Mac just to listen to audio again!

I originally posted the above fix as an [answer](https://apple.stackexchange.com/a/343974/17366) to the Stack Overflow question [AirPods: Extremely poor mic quality on Mac](https://apple.stackexchange.com/q/282705/17366), but I thought I'd post it here so I can more easily keep the post updated over time... and because I usually search my blog for quick fixes like this and this fix wasn't on my blog yet!
