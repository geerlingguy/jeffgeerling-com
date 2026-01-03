---
nid: 3222
title: "Making Noctua fans work (quietly) with a Supermicro motherboard"
slug: "making-noctua-fans-work-quietly-supermicro-motherboard"
date: 2022-07-14T15:51:13+00:00
drupal:
  nid: 3222
  path: /blog/2022/making-noctua-fans-work-quietly-supermicro-motherboard
  body_format: markdown
  redirects: []
tags:
  - fan
  - motherboard
  - noctua
  - quiet
  - server
  - supermicro
---

I've been building a Mini ITX 'quiet-ish' server using a Supermicro motherboard and some Noctua fans.

I noticed sometimes the system would start 'revving' the fans up to max power. Then after a few seconds they would get quiet again. The CPU temps and other temps on the system were stable and not worrying, but popping off the server's cover, I noticed LED8 on the motherboard would blink red every time the fans would ramp up:

{{< figure src="./led-motherboard-fan.jpg" alt="Supermicro LED8 Fan failure blinking LED" width="700" height="394" class="insert-image" >}}

That LED indicates a 'fan failure' when blinking.

{{< figure src="./supermicro-fan-low-non-recoverable.png" alt="Supermicro Fan low-non-recoverable error" width="700" height="206" class="insert-image" >}}

So looking in the IPMI interface, I noticed the Low 'Non-Recoverable' and 'Critical' levels for fan RPM were set kinda high—at least as far as Noctua fans are concerned (ignore the fact that FAN1 is reading as off—I had switched fan plugs earlier when I was moving around a system fan...). Since I bought slightly oversized fans so they could run at lower rpms (and thus quieter), the server-oriented motherboard didn't know what to make of them.

Typically one installs whiny siren-like server fans that spin at 5000+ rpm, and don't worry much about noise. But I do.

So to get the system to accept that it's normal for a fan to go below 500 rpm, I installed `ipmitool` (`sudo apt install -y ipmitool` on Debian), and ran:

```
ipmitool -I lan -U ADMIN -H [IP] sensor thresh FAN1 lower 150 250 300
```

Replace `ADMIN` with your IPMI username, and `[IP]` with your IPMI IP address.

This sets the `NR` rpm level to `150`, `LC` to `250`, and lower 'non-critical' to `300`. Much more suitable for Noctua fans that commonly run under 1k rpm. And IPMI was happy again:

{{< figure src="./supermicro-fan-normal.png" alt="Supermicro fan is normal again" width="700" height="115" class="insert-image" >}}
