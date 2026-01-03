---
nid: 3386
title: "Remote shell to a Raspberry Pi at 39,000 ft"
slug: "remote-shell-raspberry-pi-39000-ft"
date: 2024-06-25T17:24:51+00:00
drupal:
  nid: 3386
  path: /blog/2024/remote-shell-raspberry-pi-39000-ft
  body_format: markdown
  redirects: []
tags:
  - raspberry pi
  - remote access
  - remote connection
  - ssh
---

For a few weeks I've been beta testing remote shell, the latest addition to Raspberry Pi Connect. Just a couple hours ago I was on a flight home from the new Micro Center in Charlotte.

{{< figure src="./remote-shell-laptop-airplane.jpeg" alt="Pi Connect Remote Shell in airplane on laptop" width="700" height="auto" class="insert-image" >}}

One huge problem with VNC or remote desktop is how flaky it is if you have limited bandwidth or an unstable connection, like on an airplane.

It takes forever to start a screen sharing session, and the airplane's flaky WiFi usually causes the session to lock up, meaning you can't do much at all.

Remote _terminal_ access, just relaying text commands, is the best solution for that problem. And sure, I have a VPN I could use with SSH to get to my Pi, but [Raspberry Pi Connect just added support for remote shell access](https://www.raspberrypi.com/news/raspberry-pi-connect-remote-shell-access-and-support-for-older-devices/).

It's similar to SSH works, but with SSH you'd need your Pi exposed to the Internet. Not good. That's why I have a VPN, but a private VPN isn't something most people want to set up and maintain.

So for any situation where you _don't_ need the whole graphical environment, or where you have limited bandwidth, you can use the new remote shell feature.

{{< figure src="./remote-shell-laptop-btop-airplane.jpeg" alt="Pi Connect Remote Shell in airplane on laptop - btop" width="700" height="auto" class="insert-image" >}}

From my Southwest flight, I could connect straight from my laptop to the Pi in my rack at my studio, and terminal commands ran without a hitch.

The initial connection was quick, and I could even watch a _movie_ through it! Well... at least if that movie is [Star Wars ASCIIMATION](https://www.asciimation.co.nz) playing through telnet!

But it was way more stable, and I could get actual work done. My lone attempt at screen sharing froze the first time I tried launching an app.

I have a brief video covering my testing on my 2nd YouTube channel:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/Gkw1ZhShkiw" frameborder='0' allowfullscreen></iframe></div>
</div>

I'm glad Raspberry Pi's adding this functionality to Pi Connect (the community has been asking for this feature since day one!). It's not quite the same thing as Tailscale, Cloudflare Tunnel, or Twingate, but it's useful if you have a Raspberry Pi you want to remote into without any VPN.

I have more about Raspberry Pi Connect, including how to get started in [my earlier blog post](/blog/2024/raspberry-pi-getting-services-game). You can also read more on [Raspberry Pi's announcement blog post](https://www.raspberrypi.com/news/raspberry-pi-connect-remote-shell-access-and-support-for-older-devices/), including how they're supporting _every Pi device_ now, at least for remote shell access.
