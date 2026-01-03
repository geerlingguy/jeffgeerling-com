---
nid: 3438
title: "How is Deepseek R1 on a Raspberry Pi?"
slug: "how-deepseek-r1-on-raspberry-pi"
date: 2025-01-28T22:35:16+00:00
drupal:
  nid: 3438
  path: /blog/2025/how-deepseek-r1-on-raspberry-pi
  body_format: markdown
  redirects: []
tags:
  - ai
  - deepseek
  - gpu
  - llama.cpp
  - llm
  - ollama
  - openai
  - pi 5
  - raspberry pi
  - video
---

{{< figure src="./Thumbnail-1.jpg" alt="Deepseek on Pi 5" width="700" height="394" class="insert-image" >}}

OpenAI, which is only really open about [consuming all the world's energy](https://fortune.com/2023/07/11/sam-altman-oklo-ipo-spac-openai-nuclear-microreactors-green-energy/) and [half a trillion of our taxpayer dollars](https://www.cnn.com/2025/01/21/tech/openai-oracle-softbank-trump-ai-investment/index.html), just got rattled to its core.

Deepseek, a new AI startup run by a Chinese hedge fund, _allegedly_ created a new open weights model called R1 that beats OpenAI's best model in every metric.

And they did it for [$6 million](https://www.reuters.com/technology/artificial-intelligence/what-is-deepseek-why-is-it-disrupting-ai-sector-2025-01-27/), with GPUs that run at half the memory bandwidth of OpenAI's.

Besides the embarassment of a Chinese startup beating OpenAI using _one percent_ of the resources (according to Deepseek), their model can 'distill' other models to make them run better on slower hardware.

Meaning a Raspberry Pi can run one of the best local Qwen AI models even better now.

OpenAI's entire moat is predicated on people not having access to the insane energy and GPU resources to train and run massive AI models.

But that moat disappears if everyone can buy a GPU and run a model that's _good enough_, for free, any time they want.

_This blog post is an edited transcript of my video on the same topic, embedded below:_

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/o1sN1lB76EA" frameborder='0' allowfullscreen></iframe></div>
</div>

## Raspberry Pi AI

But sensationalist headlines aren't telling you the full story.

The Raspberry Pi can technically run Deepseek R1... but it's not the same thing as Deepseek R1 _671b_, which is a _four hundred gigabyte_ model.

_That_ model (the one that actually beats ChatGPT), still requires a massive amount of GPU compute.

But the big difference is, [assuming you have a few 3090s](https://www.reddit.com/r/LocalLLaMA/comments/1c55asg/4_x_3090_build_info_some_lessons_learned/), you could run it at home. You don't have to pay OpenAI for the privilege of running their fancy models.

You can just install Ollama, download Deepseek, and play with it to your heart's content.

And _even if you don't_ have a bunch of GPUs, you could _technically_ still run Deepseek on any computer with enough RAM.

{{< figure src="./deepseek-671b-ampereone_0.jpg" alt="DeepSeek 671b AmpereOne" width="700" height="394" class="insert-image" >}}

I tested Deepseek R1 671B using Ollama on the AmpereOne 192-core server with 512 GB of RAM, and it ran at just over 4 tokens per second. Which isn't _crazy_ fast, but the AmpereOne won't set you back like $100,000, either!

Even though it's only using a few hundred watts—which is honestly pretty amazing—a noisy rackmount server isn't going to fit in everyone's living room.

A Pi _could_, though. So let's look at how the smaller 14b model runs on it:

{{< figure src="./deepseek-14b-pi-5-16gb-cpu.jpg" alt="DeepSeek 14b Raspberry Pi 5 16GB" width="700" height="394" class="insert-image" >}}

It's... definitely not gonna win any speed records. I got around 1.2 tokens per second.

It _runs_, but if you want a chatbot for rubber duck debugging, or to give you a few ideas for your next blog post title, this isn't fun.

## Raspberry Pi GPU AI

But we can speed things up. A lot. All we need is an external graphics card, because GPUs and the VRAM on them are faster than CPUs and system memory.

{{< figure src="./deepseek-amd-w7700-pi-5.jpg" alt="DeepSeek running on eGPU W7700 AMD Pi 5" width="700" height="394" class="insert-image" >}}

I have this setup I've been testing with an AMD W7700 graphics card. It has 16 gigs of speedy VRAM, and as long as it can fit the whole AI model, it should be much faster:

| model                          |       size |     params | backend    | ngl |          test |                  t/s |
| ------------------------------ | ---------: | ---------: | ---------- | --: | ------------: | -------------------: |
| qwen2 14B Q4_K - Medium        |   8.37 GiB |    14.77 B | Vulkan     |  99 |         pp512 |        193.31 ± 0.35 |
| qwen2 14B Q4_K - Medium        |   8.37 GiB |    14.77 B | Vulkan     |  99 |        pp4096 |        168.01 ± 0.25 |
| qwen2 14B Q4_K - Medium        |   8.37 GiB |    14.77 B | Vulkan     |  99 |         tg128 |         24.41 ± 0.24 |
| qwen2 14B Q4_K - Medium        |   8.37 GiB |    14.77 B | Vulkan     |  99 |  pp4096+tg128 |         54.26 ± 0.92 |

`llama-bench` reports 24 to _54_ tokens per second, and this GPU isn't even targeted at LLMs—you can go a _lot_ faster. For full test results, check out my ollama-benchmark repo: [Test Deepseek R1 Qwen 14B on Pi 5 with AMD W7700](https://github.com/geerlingguy/ollama-benchmark/issues/9).

## Conclusion

AI is still in a massive bubble. [Nvidia just lost _more than half a trillion dollars in value_](https://www.cnbc.com/2025/01/27/nvidia-sheds-almost-600-billion-in-market-cap-biggest-drop-ever.html) in one day after Deepseek was launched.

But their stock price is [still 8x higher than it was in 2023](https://finance.yahoo.com/quote/NVDA/?.tsrc=applewf), and it's not like anyone's hyping up AI any _less_ now.

The one good takeaway, I think, is people might realize we don't need to devote more than half the world's energy resources or set up a Dyson sphere around the sun, just to help computers solve trillions of multiplication problems to spit out another thousand mediocre web apps.

The other takeaway is that there's new confusion in AI models over who, precisely, is [Winnie the Pooh](https://nationalpost.com/news/who-is-winnie-the-pooh-chatgpt-and-deepseeks-new-ai-chatbot-beg-to-differ).
