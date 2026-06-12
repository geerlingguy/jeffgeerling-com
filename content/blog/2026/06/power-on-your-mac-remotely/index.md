---
date: '2026-06-12T09:00:00-05:00'
tags: ['mac', 'macos', 'youtube', 'video', 'remote', 'homelab', 'power']
title: 'You can finally power on a Mac remotely'
slug: 'power-on-your-mac-remotely'
---
Apple FINALLY lets you [turn on your Mac remotely](https://support.apple.com/en-us/125517), without having to press the power button. In the media, articles suggest it's a reaction to [Mac mini power button complaints](https://9to5mac.com/2026/05/11/macos-26-5-adds-new-way-to-control-your-macs-power-state-via-switches/).

{{< figure
  src="./m4-mini-remote-power-button.jpg"
  alt="Turning on an M4 Mac mini remotely using Home Assistant on a Framework 12"
  width="700"
  height="auto"
  class="insert-image"
>}}

While I agree the M4 mini's power button is in a really dumb spot, that's not why I care about this feature. The two _bigger_ use cases for me have been a pain for years:

  - Remote Macs in a lab/CI environment, where I don't need them running 24x7, especially when someone accidentally shuts one down.
  - Macs mounted in road cases or portable racks. It'd be a godsend for them to turn on automatically as I set up for the event (e.g. at a concert or in live broadcast environments).

Macs gained ['Wake on LAN'](https://en.wikipedia.org/wiki/Wake-on-LAN) support in Mac OS X 10.4, released in 2005. Here's the setting as it appears on my [Power Macintosh G4 MDD](https://www.jeffgeerling.com/blog/2024/build-log-power-mac-g4-mdd/):

{{< figure
  src="./mac-os-x-10.4-energy-saver-wake-power-wol-options.jpg"
  alt="Energy Saver options in Mac OS X 10.4 include WoL and Power on after power failure"
  width="700"
  height="auto"
  class="insert-image"
>}}

This setting allows you to wake a Mac from _sleep_ remotely, by sending it a [magic packet](https://superuser.com/questions/1066619/what-is-a-magic-packet-for-waking-a-computer). They also added 'reboot after power failure' in 10.4, which is great if you're okay hard-cutting power to your Mac so it'll boot when you turn power back on. That's fine for emergencies or when your UPS dies, but it's risky since it's not a safe shutdown scenario.

PCs [had the ability](https://web.archive.org/web/20130828233419/http://www.pcguide.com/ref/power/sup/func_SoftPower.htm) to boot from power off (regardless of shutdown state) on most systems complying with Intel's ATX standard, since 1995.

Three decades later, with the release of macOS 26.5, Apple caught up: you can finally set your Mac to 'Always' boot whenever power is restored, regardless of how it was shut down.

I tested this feature on my M4 Mac mini, which is in the limited set of Macs supporting this feature:

  - Mac mini introduced in 2024 or later
  - Mac Studio introduced in 2025 or later
  - iMac introduced in 2024 or later

I made a short video going through everything in this post, if you'd like to watch:

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/9prKU2Vuo-0' frameborder='0' allowfullscreen></iframe></div>
</div>

Like blogs more than videos? Read on!

## Remote Power Control

{{< figure
  src="./m4-mini-zigbee-smart-outlets.jpg"
  alt="Zigbee smart outlets for power monitoring and control in server rack"
  width="700"
  height="auto"
  class="insert-image"
>}}

Rather than rehash the details of how I use [these Zigbee Smart Outlets](https://amzn.to/45oROls) to monitor and control power for most of my servers, I'll link you to the blog post: [How I monitor and control all my powered devices (Zigbee + HA)](https://www.jeffgeerling.com/blog/2025/how-i-monitor-and-control-all-my-powered-devices-zigbee-ha/).

## Configuring macOS to Always power on

To configure macOS to Always boot when power is applied (whether from an outage or a planned shutdown):

  1. Open System Settings, and go to 'Energy'
  1. Select "Always" for the 'Start up when power is connected' option

{{< figure
  src="./macos-energy-setting-startup-when-power-connected-always.jpg"
  alt="macOS Energy setting for Always starting when power is connected"
  width="700"
  height="auto"
  class="insert-image"
>}}

I tested the feature by shutting down my Mac, plugging it into the smart outlet, and toggling power on the smart outlet. The M4 mini booted up within 2 seconds, though it didn't make the normal startup chime that happens when I cold boot with the power button[^startupchime].

## Two Caveats

There are two things you should know if you operate your Mac remotely:

  1. If you're using FileVault (most people are), and want to log in remotely after the Mac boots, you will first need to log in via SSH and enter the password for an admin account. This will unlock the Mac, after which you can log in with a normal session (via SSH or Screen Sharing). This feature was added in macOS 26.0 and I covered it in this post: [Remote login via SSH with FileVault](https://www.jeffgeerling.com/blog/2025/you-can-finally-manage-macs-filevault-remotely-tahoe/)
  1. If you use Screen Sharing to log into a remote Mac, and then you close the Screen Sharing session _without logging out_ on a Mac with a display attached, the remote Mac will 'wake up' to a logged-in desktop, as if you were just using it. If you're in a shared office space or something, that could be quite a problem! I try to remember to log out before closing a Screen Sharing session.

## And a Bug

In the course of making a video on this, I was testing a few different boot scenarios. Everything worked, except for one:

{{< figure
  src="./m4-mini-remote-power-off-bad.jpg"
  alt="macOS Shut Down command in login window"
  width="700"
  height="auto"
  class="insert-image"
>}}

If I booted up the Mac (either with the power button or by switching on the outlet), but did _not_ log in, and chose the 'Shut Down' option in the login window to power off the Mac, it would not power back on when power was connected. I _had_ to physically press the power button.

I tested this four times, and also tested logging in and shutting down normally, and in all cases this bug was confirmed.

I was going to file a bug in Apple's '[Radar](https://radar.apple.com)' system, but I don't have an 'AppleConnect' account. So then I found macOS has a built in 'Feedback Assistant' app, so I used that instead. I created report `FB23071345: Boot after power restore fails if Mac is shut down from login screen` in case anyone at Apple is listening :)

{{< figure
  src="./feedback-for-macos-boot-fails.jpg"
  alt="Submitting my bug report to Apple Feedback"
  width="700"
  height="auto"
  class="insert-image"
>}}

## Conclusion

Special thanks to Redditor [prodigalAvian](https://www.reddit.com/r/homelab/comments/1txnj04/comment/opyd44t/), whose comment was the first place I found out about this feature. I've been using smart outlets to control power for my PCs for years—I'm glad I can finally do the same thing for Macs—at least the newer ones.

[^startupchime]: Maybe one of the engineers working on this feature was getting driven mad by testing on a rack full of Macs, and determined it's better to not hear a cacophony of multiple [Mac bongs](https://www.youtube.com/watch?v=e7LW_NvSuIk) slightly offset from one another.
