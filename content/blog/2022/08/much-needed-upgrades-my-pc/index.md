---
nid: 3228
title: "Much-needed upgrades to my PC"
slug: "much-needed-upgrades-my-pc"
date: 2022-08-12T23:09:57+00:00
drupal:
  nid: 3228
  path: /blog/2022/much-needed-upgrades-my-pc
  body_format: markdown
  redirects: []
tags: []
---

Earlier this year, when [I built my all-AMD gaming PC](/blog/2022/livestream-i-attempt-build-modern-linux-gaming-pc), I decided to stick with AMD's stock CPU cooler. After all, if they include a particular cooler with the Ryzen 5 5600x, I should assume that cooler is adequate, _right_?

{{< figure src="./amd-wraith-cooler-5600x-cpu.jpg" alt="AMD Wraith cooler on Ryzen 5 5600x CPU" width="700" height="454" class="insert-image" >}}

Wrong! I noticed when comparing benchmarks from Phoronix that my CPU was running a little slower than the average 5600x, and it turns out the 'wraith' cooler just can't keep up under load.

I [tweeted](https://twitter.com/geerlingguy/status/1499794884949065734) as much (expressing my dissatisfaction with the noise it put out), and [Noctua responded](https://twitter.com/Noctua_at/status/1499818637041016839) pretty quickly, offering to send me an NH-U12A to replace it.

{{< figure src="./noctua-chromax-mounting-adapter-plate-b550-amd.jpeg" alt="Noctua B550 AMD CPU mounting adapter plate on motherboard with Ryzen 5 5600x" width="700" height="467" class="insert-image" >}}

The installation was very easy (their kit includes all the necessary adapters and screws for either Intel or AMD boards), and besides being a pretty beefy cooler, this thing looks and runs great.

My Cinebench test runs no longer maxed out the thermals. With the AMD cooler I was hitting 88°C and thermal throttling down to about 4.3 Ghz. With the Noctua, I was able to run at 4.6 GHz turbo clocks all day, and at temperatures around 65°C or less. I could probably lower the fan speed from stock and get an even quieter setup (not that it's loud) if I wanted.

{{< figure src="./noctua-chromax-black-nh-u12a-cpu-cooler-amd-ryzen-radeon.jpeg" alt="Noctua NH-U12A chromax.black CPU cooler installed insice AMD Ryzen Radeon PC build running" width="700" height="477" class="insert-image" >}}

I was pretty amazed by how much difference the cooler made. And I wasn't really surprised how quiet Noctua's solution is, since I've long been replacing fans with their ugly-as-sin brown models for years. This was the first 'chromax' upgrade I did, and I do like the black fans in this build. The brown wouldn't reflect my RGB lighting as nicely, I don't think.

## 4K HDMI capture card

The other upgrade I made was adding a [AVerMedia GC573 4K Capture Card](https://amzn.to/3QnVmtx). This is a PCI Express card with an HDMI input and output that is generally used by streamers to pass through an input to OBS for game consoles or other gaming devices.

{{< figure src="./avermedia-game-capture-4k-card.jpg" alt="AVerMedia GC573 Live Gamer 4k Capture Card installed under Radeon RX 6700 XT" width="700" height="394" class="insert-image" >}}

In my case, I wanted something easy to plug in Raspberry Pis, SBCs, and servers, so I could both record and observe their external displays when I need to do work through their UIs, directly connected.

I often use my [Atomos Ninja V](https://amzn.to/3PgL90F) recorder for that purpose, but one annoying aspect of that recorder is how it splits recording files any time a resolution changes, or whenever the signal drops and picks back up (like during boot).

Using the capture card and OBS, I can get a continuous recording no matter what the output is doing, which makes splicing it into a video edit that much easier. Driver install was all that was needed for Windows to recognize the card as a valid input device, and so far it seems to work well in OBS and any other application that accepts video inputs.

Recording works great, and who knows—maybe I'll use it for some streaming too. We'll see!

You can view the install process in more depth, and see how easy it was to get working, in today's video:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/a3fJ5WlZ1TQ" frameborder='0' allowfullscreen></iframe></div>
</div>

## Thanks for the support

I didn't post anything on the blog yet, because I was in the middle of everything, and just getting [this video posted](https://www.youtube.com/watch?v=MXxPsWjMW1A) was enough work... but I have been dealing with some complications from my Crohn's disease this past week, and will likely be slowing down my work schedule a bit so I can make a full recovery, while also spending a good amount of time with my family.

I thank my Wife and my Mom especially for their love and support—raising a family with young children makes this whole ordeal a bit harder, but their help has gotten me through all this and more over the 20+ years dealing with Crohn's disease.

But I also want to thank everyone who sponsors me on [Patreon](https://www.patreon.com/geerlingguy) and [GitHub Sponsors](https://github.com/sponsors/geerlingguy) especially—this monetary support has made it possible for me to carry on with my open source work and educational videos on YouTube even in the midst of health problems. I am extremely lucky to be in the position I'm in today, and it wouldn't be possible without all this support!
