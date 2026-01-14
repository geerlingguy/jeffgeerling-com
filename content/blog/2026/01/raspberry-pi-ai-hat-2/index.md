---
draft: true
date: '2026-01-15T02:00:00-06:00'
tags: ['tag_here']
title: "Raspberry Pi's new AI HAT+ 2 adds 8GB of RAM for local LLMs in 3W"
slug: 'raspberry-pi-ai-hat-2'
---

{{< figure
  src="./raspberry-pi-ai-hat-2.jpg"
  alt="Raspberry Pi AI HAT+ 2"
  width="700"
  height="auto"
  class="insert-image"
>}}

Today Raspberry Pi launched their new [$130 AI HAT+ 2](https://www.raspberrypi.com/products/ai-hat-2/) which includes a Hailo 10H and 8 GB of [LPDDR4X RAM](https://www.micron.com/products/memory/dram-components/lpddr4/part-catalog/part-detail/mt53e2g32d4de-046-wt-c).

With that RAM, the Hailo 10H is capable of running LLMs entirely separate from the Pi's CPU, freeing it up to do other tasks. The chip runs at a maximum of 3W, with 40 TOPS of INT8 NPU inference performance in addition to the equivalent 26 TOPS INT4 machine vision performance on the earlier AI HAT with Hailo 8.

In practice, it's not as amazing as it sounds.

You still can't upgrade the RAM on the Pi, but at least this way if you _do_ have a need for an AI coprocessor, you don't have to eat up the Pi's memory to run things on it.

And it's a lot cheaper and more compact than [running an eGPU on a Pi](/blog/2025/big-gpus-dont-need-big-pcs/). In that sense, it's more useful than the silly NPUs Microsoft forces into their 'AI PCs'.

But it's still a solution in search of a problem, in all but the most niche of use cases.

Besides feeling like I'm living in the world of the [Turbo Encabulator](https://www.youtube.com/watch?v=Ac7G7xOG2Ag) every time I'm testing AI hardware, I find the marketing of these things to be very vague, and the applications not very broad.

For example, the Hailo 10H is advertised as being used for a [Fujitsu demo of automatic shrink detection for a self-checkout](https://www.youtube.com/watch?v=flD-WfJ4pUg).

That's certainly not a worthless use case, but it's not something I've ever really cared to work on. I have a feeling this board is more meant for development purposes, for people who want to deploy the 10H in other devices, rather than as a total solution to a problem many Pi users need to solve.

Especially when it comes to the headline feature: running inference, like with LLMs.

## Video

I also published a video with all the information in this blog post, but if you enjoy text more than video, scroll on past—it doesn't offend me!

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/jRQaur0LdLE' frameborder='0' allowfullscreen></iframe></div>
</div>

## LLM performance on the AI HAT+ 2

I ran everything on an 8 gig Pi 5, so I could get an apples-to-apples comparison, running the same models on the Pi's CPU as I did on the AI HAT's NPU.

They both have the same 8GB LPDDR4X RAM configuration, so _ideally_, they'd have similar performance.

I tested every model Hailo put out so far, and compared them, Pi 5 versus Hailo 10H:

{{< figure
  src="./pi-ai-hat-2-llm-compare-inference.jpg"
  alt="Raspberry Pi AI HAT+ 2 - Inference performance NPU vs CPU"
  width="700"
  height="auto"
  class="insert-image"
>}}

The Pi's built-in CPU trounces the Hailo 10H.

The Hailo is only close, really, on Qwen2.5 Coder 1.5B.

It _is_ slightly more efficient in most cases:

{{< figure
  src="./pi-ai-hat-2-llm-compare-efficiency.jpg"
  alt="Raspberry Pi AI HAT+ 2 - Inference efficiency NPU vs CPU"
  width="700"
  height="auto"
  class="insert-image"
>}}

But looking more closely at power draw, we can see why the Hailo doesn't keep up:

{{< figure
  src="./pi-ai-hat-2-power-draw-compare-llm.jpg"
  alt="Raspberry Pi AI HAT+ 2 - Power draw NPU vs CPU"
  width="700"
  height="auto"
  class="insert-image"
>}}

The Pi's CPU is allowed to max out it's power limits (10W on the SoC), which are a lot higher than the Hailo's (3W).

## Qwen 30B on a Pi

So power holds it back, but the 8 gigs of RAM holds back the LLM use case (vs just running on the Pi's CPU) the most. The Pi 5 can be bought in up to a _16 GB_ configuration. That's as much as you get in decent consumer graphics cards[^vram].

Because of that, many quantized medium-size models target 10-12 GB of RAM usage (leaving space for context, which eats up another 2+ GB of RAM).

A couple weeks ago, [ByteShape got Qwen3 30B A3B Instruct to fit on a 16GB Pi 5](https://byteshape.com/blogs/Qwen3-30B-A3B-Instruct-2507/). Now this post isn't about LLMs, but the short of it is they found a novel way to compress the model to fit in 10 GB of RAM.

A little bit of quality is lost, but like a JPEG, it's still good enough to ace all the contrived tests (like building a TODO list app, or sorting a complex list) that the tiny models I ran on the Hailo 10H didn't complete well (see the video earlier in this post for details).

{{< figure
  src="./llama-cpp-pi-5-qwen3-30b-a3b-instruct.jpg"
  alt="Raspberry Pi 16GB running Qwen3 30B model"
  width="700"
  height="auto"
  class="insert-image"
>}}

To test the 30B model, I [installed llama.cpp following this guide from my blog](https://www.jeffgeerling.com/blog/2024/llms-accelerated-egpu-on-raspberry-pi-5/), and [downloaded the compressed model](https://huggingface.co/byteshape/Qwen3-30B-A3B-Instruct-2507-GGUF/).

I asked it to generate a single page TODO list app, and it's still not a speed demon (this is a Pi CPU with LPDDR4x RAM we're talking about), but after a little while, it gave me this:

{{< figure
  src="./pi-ai-16gb-qwen3-30b-todo-list-app.jpg"
  alt="Raspberry Pi 16GB Qwen3 Generated TODO list app"
  width="700"
  height="auto"
  class="insert-image"
>}}

It met all my requirements:

  - I can type in as many items as I want
  - I can drag them around to rearrange them
  - I can check off items and they go to the bottom of the list...

It's honestly crazy how many small tasks you can do even with free local models... even on a Pi. [Natural Language Programming](https://en.wikipedia.org/wiki/Natural_language_programming) was just a dream back when I started my career.

Besides being angry Google, OpenAI, Anthropic and all these other companies are [consuming all the world's money and resources](https://am.jpmorgan.com/us/en/asset-management/adv/insights/market-insights/market-updates/on-the-minds-of-investors/is-ai-already-driving-us-growth/) doing this stuff—not to mention [destroying the careers of thousands of junior developers](https://www.cio.com/article/4062024/demand-for-junior-developers-softens-as-ai-takes-over.html)—it is kinda neat to see NLP work for very tightly defined examples.

## Benchmarking computer vision

But I don't think this HAT is the best choice to run local, private LLMs (at least not as a primary goal).

What it _is_ good for, is vision processing. But the original AI HAT was good for that too!

In my testing, Hailo's [hailo-rpi5-examples](https://github.com/hailo-ai/hailo-rpi5-examples) were not yet updated for this new HAT, and even if I specified the Hailo 10H manually, model files would not load, or I ran into errors once the board was detected.

But Raspberry Pi's models ran, so I tested them with a Camera Module 3:

{{< figure
  src="./pi-ai-hat-vision-30fps-yolo.jpg"
  alt="Raspberry Pi AI HAT+ 2 running YOLO vision model at 30fps"
  width="700"
  height="auto"
  class="insert-image"
>}}

I pointed it over at my desk, and it was able to pick out things like my keyboard, my monitor (which it thought was a TV), my phone, and even the mouse tucked away in the back.

It all ran quite fast—and 10x faster than on the Pi's CPU—but the problem is I can do the same thing with the _original_ AI HAT ($110)—or the [AI Camera](https://www.raspberrypi.com/products/ai-camera/) ($70).

If you _just_ need vision processing, I would stick with one of those.

The headline feature of the AI HAT+ 2 is the ability to run in a 'mixed' mode, where it can process machine vision (frames from a camera or video feed), while also running inference (like an LLM or text-to-speech).

{{< figure
  src="./pi-ai-hat-mixed-vision-llm-no-work.jpg"
  alt="Raspberry Pi AI HAT+ 2 mixed inference and vision not working"
  width="700"
  height="auto"
  class="insert-image"
>}}

Unfortunately, when I tried running two models simultaneously, I ran into segmentation faults or 'device not ready', and lacking any working examples from Hailo, I had to give up on getting that working in time for this post.

Just like the original AI HAT, there's some growing pains.

It seems like with most hardware with "AI" in the name, it's hardware-first, then software comes later—if it comes at all. At least with Raspberry Pi's track record, the software _does_ come, it's just... often the solutions are only useful in tiny niche use cases.

## Conclusion

8 GB of RAM is useful, but it's not quite enough to give this HAT an advantage over just paying for the bigger 16GB Pi with more RAM, which will be more flexible and run models faster.

The main use case for this HAT might be in power-constrained applications where you need both vision processing _and_ inferencing. But even there... it's hard to say "yes, buy this thing", because for just a few more watts, the Pi could achieve better performance for inference in tandem with the $70 [AI Camera](https://www.raspberrypi.com/products/ai-camera/) or the $110 [AI HAT+](https://www.microcenter.com/product/687346/product?src=raspberrypi) for the vision processing.

Outside of running tiny LLMs in less than 10 watts, maybe the idea is you use the AI HAT+ 2 as a development kit for designing devices using the 10H like self-checkout scanners (which might not even run on a Pi)? I'm not sure.

[^vram]: With the obvious caveat that the VRAM on GPUs runs a lot faster than equivalent LPDDR4 RAM on a Pi!
