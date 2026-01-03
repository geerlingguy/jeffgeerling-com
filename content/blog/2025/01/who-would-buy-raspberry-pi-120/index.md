---
nid: 3432
title: "Who would buy a Raspberry Pi for $120?"
slug: "who-would-buy-raspberry-pi-120"
date: 2025-01-09T08:00:24+00:00
drupal:
  nid: 3432
  path: /blog/2025/who-would-buy-raspberry-pi-120
  body_format: markdown
  redirects: []
tags:
  - linux
  - pi 5
  - raspberry pi
  - reviews
  - sbc
  - testing
  - video
---

That is indeed a puzzling question, brought about by Raspberry Pi's introduction of the newest Raspberry Pi 5 model, with 16 GB of RAM.

{{< figure src="./pi-5-16gb-ram.jpg" alt="Raspberry Pi 5 16GB RAM" width="700" height="auto" class="insert-image" >}}

I spent a couple weeks testing the new Pi model, and found it _does have its virtues_. But being only $20 away from a complete [GMKTec N100 Mini PC with 8GB of RAM](https://amzn.to/4jb4dO0), it's probably a step too far _for most people_.

{{< figure src="./pi-5-model-pricing.png" alt="Pi 5 model B pricing from 2 to 16 GB" width="700" height="auto" class="insert-image" >}}

For most, the 2 GB ($50) or 4 GB ($60) Pi 5 is a much better option. Or if you're _truly_ budget conscious and want a well-supported SBC, the Pi 4 still exists, and starts at $35. Or a Pi Zero 2 W for $15.

And for stats nerds, the pricing model for Pi 5 follows this polynomial curve almost perfectly:

{{< figure src="./pi-5-model-b-pricing-curve.png" alt="Pi 5 model B pricing curve polynomial fit" width="700" height="auto" class="insert-image" >}}

...very much unlike Apple's memory and storage pricing for the M4 Mac mini, which follows an equation that ranges from "excellent deal" to "exorbitant overcharge".

## Performance

Before I get to the reasons why some people might consider spending $120 on a Pi 5, I ran a bunch of benchmarks, and one of the more pertinent results is HPL:

{{< figure src="./pi-5-8gb-vs-16gb-hpl-efficiency.png" alt="High Performance Linpack - Pi 5 model B 8 GB vs 16 GB" width="700" height="394" class="insert-image" >}}

This compares the performance of the 8 GB Pi 5 against the new 16 GB model. For many benchmarks, the biggest difference may be caused by the 16 GB model having the newer, trimmer [D0 stepping of the BCM2712](/blog/2024/new-2gb-pi-5-has-33-smaller-die-30-idle-power-savings). But for some, having more RAM helps, too.

Applications like ZFS can cache more files with more RAM, leading to lower latency and higher bandwidth file copies—in certain conditions.

For _all_ my 16 GB Pi 5 benchmarks, see [this follow-up comment on my Pi 5 sbc-reviews thread](https://github.com/geerlingguy/sbc-reviews/issues/21#issuecomment-2579400396).

## 5 Reasons a 16 GB Pi 5 should exist

{{< figure src="./raspberry-pi-5-forza-horizon-4-20fps.jpg" alt="Raspberry Pi 5 eGPU setup playing Forza Horizon 4 Benchmark" width="700" height="439" class="insert-image" >}}

But I distilled my thoughts into a list of 5 reasons the 16 GB Pi 5 ought to exist:

  1. **Keeping up with the Joneses**: Everyone seems to be settling on 16 GB of RAM as the new laptop/desktop baseline—even _Apple_, a company notoriously stingy on RAM in its products! So having a high-end SBC with the same amount of RAM as a low-end desktop makes sense, if for no other reason than _just to have it available_.
  2. **LLMs and 'AI'**: Love it or hate it, Large Language Models love RAM. The more, the merrier. The 8 GB Pi 5 can only handle up to an 8 billion parameter model, like `llama3.1:8b`. The 16 GB model can run much larger models, like `llama2:13b`. Whether getting 1-2 tokens/s on such a large model on a Pi 5 is _useful_ is up to you to decide. I posted my Ollama benchmarks results [in this issue](https://github.com/geerlingguy/ollama-benchmark/issues/7)
  3. **Performance**: I already discussed this above, but along with the latest SDRAM tuning the Pi engineers worked on, this Pi is now the fastest _and_ most efficient, especially owing to the newer D0 chip revision.
  4. **Capacity and Consolidation**: With more RAM, you can run more apps, or more threads. For example, a Pi 5 with 4 GB of RAM could run one Drupal or Wordpress website comfortably. With 16 GB, you could conceivably run _three or four_ websites with decent traffic, assuming you're not CPU-bound. You could also run more instances on the same Pi of Docker containers or [pimox](https://github.com/pimox/pimox7) VMs.
  5. **AAA Gaming**: This is, of course, a stretch... but there are some modern AAA games that I had trouble with on my [eGPU Pi 5 setup](/blog/2024/amd-radeon-pro-w7700-running-on-raspberry-pi) which ran out of system memory on the 8 GB Pi 5, causing thrashing and lockups. For example: Forza Horizon 4, which seemed to enjoy using about 8 GB of system RAM total (alongside the 1 GB or so required by the OS and Steam).

I have a full video covering the Pi 5 16GB, along with illustrations of some of the above points. You can watch it below:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/apWi16EROKc" frameborder='0' allowfullscreen></iframe></div>
</div>
