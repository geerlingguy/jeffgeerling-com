---
nid: 3488
title: "Reverse Engineering ALL the Raspberry Pis"
slug: "reverse-engineering-all-raspberry-pis"
date: 2025-08-25T19:16:05+00:00
drupal:
  nid: 3488
  path: /blog/2025/reverse-engineering-all-raspberry-pis
  body_format: markdown
  redirects: []
tags:
  - level2jeff
  - lumafield
  - pcb
  - raspberry pi
  - reverse engineering
  - sbc
  - video
---

Earlier this month I covered [Jonathan Clark's effort to reverse-engineer the Pi Zero 2 W](/blog/2025/reverse-engineering-raspberry-pi-zero-2w), and just yesterday, I discovered [TubeTime reverse-engineered the Compute Module 5](https://bsky.app/profile/tubetime.bsky.social/post/3lx6erpo5lc2u).

<div class="yt-embed">
<blockquote class="bluesky-embed" data-bluesky-uri="at://did:plc:lrfapunwg5trd7e2r3ccfqwc/app.bsky.feed.post/3lx6erpo5lc2u" data-bluesky-cid="bafyreidfra36luasy6gkijtp6t2tjxiqmb53t36vyiwidjozmnaj6b7xya" data-bluesky-embed-color-mode="system"><p lang="en">i reverse-engineered the Raspberry Pi Compute Module 5! check it out at github.com/schlae/cm5-r...<br><br><a href="https://bsky.app/profile/did:plc:lrfapunwg5trd7e2r3ccfqwc/post/3lx6erpo5lc2u?ref_src=embed">[image or embed]</a></p>&mdash; Tube Time (<a href="https://bsky.app/profile/did:plc:lrfapunwg5trd7e2r3ccfqwc?ref_src=embed">@tubetime.bsky.social</a>) <a href="https://bsky.app/profile/did:plc:lrfapunwg5trd7e2r3ccfqwc/post/3lx6erpo5lc2u?ref_src=embed">August 24, 2025 at 3:57 PM</a></blockquote><script async src="https://embed.bsky.app/static/embed.js" charset="utf-8"></script>
</div>

Both are graciously sharing their schematics and process on GitHub:

  - [jonny12375/rp3a0](https://github.com/jonny12375/rp3a0) for the Zero 2 W / RP3A0
  - [schlae/cm5-reveng](https://github.com/schlae/cm5-reveng) for the CM5 / RP2712

Raspberry Pi shares limited board schematics, but sometimes—especially when digging into some esoteric edge case for a carrier board, or in Jonathan's case, desoldering all the chips and building a Pi Zero 2W into a Pico form factor PCB—you need more.

<div style="text-align: center;">
<video style="max-width: 95%; width: 640px; height: auto;" autoplay loop muted>
  <source src="./lumafield-orbit-cm5-optimized.mp4" type="video/mp4" />
  Your browser does not support the video tag.
</video>
</div>

Well, in both cases, I realized _after_ the fact I was sitting on some highly detailed Lumafield scans, which I had planned on making a video going through at some point for a project I'm working on this year. But that data would've helped in both projects (at least mildly). It's not as good as hand-sanding a PCB and getting high resolution scans, but it is especially helpful in getting a 'look inside' 3D representation of the complete board.

So, along with a video on my 2nd YouTube channel today, I'm releasing _all_ the Lumafield scans of the modern Raspberry Pi lineup (excluding the larger keyboard form factor Pis, like the Pi 400 and Pi 500... maybe I can get to those too, someday).

Here's the video:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/2nlynRkpt0E" frameborder='0' allowfullscreen></iframe></div>
</div>

And here are links to all the Lumafield scans in their Voyager tool, so you can play with them and dig into the Pi internals _yourself_:

  - [Raspberry Pi 4 model B](https://voyager.lumafield.com/project/c50be82c-188c-4405-ac55-676a388d2122)
  - [Raspberry Pi CM4](https://voyager.lumafield.com/project/ad315d0b-7143-4b3d-963d-2018a5314f1b)
  - [Raspberry Pi Zero 2 W](https://voyager.lumafield.com/project/fcbc8145-2873-4432-bfcc-29896cd440c9)
  - [Raspberry Pi 5](https://voyager.lumafield.com/project/5f0cf35f-c5f1-4db0-a0f5-d06ecb9bc359)
  - [Raspberry Pi CM5](https://voyager.lumafield.com/project/9a14818b-f9a7-49d1-b9c9-09e0560e1498)

HUGE thanks to Lumafield for helping me produce these scans.
