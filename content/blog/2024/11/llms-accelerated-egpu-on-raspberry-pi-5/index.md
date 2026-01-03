---
nid: 3421
title: "LLMs accelerated with eGPU on a Raspberry Pi 5"
slug: "llms-accelerated-egpu-on-raspberry-pi-5"
date: 2024-11-19T21:26:55+00:00
drupal:
  nid: 3421
  path: /blog/2024/llms-accelerated-egpu-on-raspberry-pi-5
  body_format: markdown
  redirects: []
tags:
  - ai
  - amd
  - gpu
  - guide
  - llama.cpp
  - llm
  - open source
  - tutorial
  - video
  - youtube
---

After a long journey [getting AMD graphics cards working on the Raspberry Pi 5](/tags/gpu), we finally have a stable patch for the `amdgpu` Linux kernel driver, and it works on AMD RX 400, 500, 6000, and (current-generation) 7000-series GPUs.

With that, we also have stable Vulkan graphics and compute API support.

When I wrote about [getting a Radeon Pro W7700 running on the Pi](/blog/2024/amd-radeon-pro-w7700-running-on-raspberry-pi), I also mentioned [AMD is not planning on supporting Arm](https://github.com/ROCm/ROCm/issues/3960) with their ROCm GPU acceleration framework. At least not anytime soon.

Luckily, the Vulkan SDK can be used in its place, and in some cases even outperforms ROCm—especially on consumer cards where _ROCm isn't even supported on x86_!

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/AyR7iCS7gNI" frameborder='0' allowfullscreen></iframe></div>
</div>

## Installing `llama.cpp` with Vulkan support on the Pi 5

Assuming you already have an AMD graphics card (I tested with an RX 6700 XT), and you built a custom kernel using our `amdgpu` patch ([instructions here](/blog/2024/amd-radeon-pro-w7700-running-on-raspberry-pi)), you can compile `llama.cpp` on the Pi 5 with Vulkan support:

```
# Install dependencies: Vulkan SDK, glslc, cmake, and curl dev library
sudo apt install -y libvulkan-dev glslc cmake libcurl4-openssl-dev

# Clone llama.cpp
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp

# Build with Vulkan support (for Cuda, someday, `-DGGML_CUDA=1`
cmake -B build -DGGML_VULKAN=1
cmake --build build --config Release -j $(nproc)
```

Now, you can download a model (e.g. off HuggingFace), and test to ensure `llama.cpp` is using the GPU to accelerate inference:

```
# Download llama3.2:3b
cd models && wget https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF/resolve/main/Llama-3.2-3B-Instruct-Q4_K_M.gguf

# Run it.
cd ../
./build/bin/llama-cli -m "models/Llama-3.2-3B-Instruct-Q4_K_M.gguf" -p "Why is the blue sky blue?" -no-cnv -e -ngl 100 -t 4

# You should see in the output, ggml_vulkan detected your GPU. For example:
# ggml_vulkan: Found 1 Vulkan devices:
# ggml_vulkan: 0 = AMD Radeon RX 6700 XT (RADV NAVI22) (radv) | uma: 0 | fp16: 1 | warp size: 64
```

> **Nov 2025 Update**: You can now use Llama.cpp's built-in Web UI as well:
>
> ```
> ./build/bin/llama-server -m "models/Llama-3.2-3B-Instruct-Q4_K_M.gguf" --jinja -c 0 --host 127.0.0.1 --port 8033 -ngl 100
> ```

You can also monitor the GPU statistics with tools like `nvtop` (`sudo apt install -y nvtop`) or `amdgpu_top` ([build instructions](https://github.com/Umio-Yasuno/amdgpu_top?tab=readme-ov-file#build-from-source)).

On my RX 6700 XT, I can confirm the model gets loaded into the VRAM and the GPU is used for inference:

{{< figure src="./nvtop-rx-6700-xt-llm.jpg" alt="nvtop RX 6700 XT showing VRAM usage on Pi 5" width="700" height="auto" class="insert-image" >}}

## Performance

I went to Micro Center and bought a couple more consumer graphics cards for testing, and matched that up with the cards I already own, as well as my M1 Max Mac Studio, which has 64 GB of shared RAM and 24 GPU cores:

{{< figure src="./llama-cpp-pi-5-gpu-benchmarks.jpg" alt="llama.cpp inference speeds on Pi 5 and M1 Max Mac Studio" width="700" height="auto" class="insert-image" >}}

I tested a variety of models—including some not pictured here, like Mistral Small Instruct (a 22 Billion parameter model), and Qwen2.5 (a 14 Billion parameter model). Some models had to split between the Pi's pokey CPU and the GPU, while others could fit entirely on the GPU.

The `amdgpu` driver patch translates memory access inefficiently in many cases, and I think that's what kills performance with larger models.

But for smaller models—ones that are targeted at client devices and consumer GPUs—the Pi and Vulkan doesn't seem to be much of a bottleneck!

And [as pointed out on Reddit](https://www.reddit.com/r/LocalLLaMA/comments/1gucux2/comment/lxtyiiu/), the main virtue of this system as opposed to any old PC with a graphics card is idle power efficiency:

{{< figure src="./llama-cpp-pi-idle-power-consumption.jpg" alt="llama.cpp system Pi 5 idle power draw" width="700" height="auto" class="insert-image" >}}

The Pi only consumes 3W of power at idle, and if you pair it with an efficient graphics card and PSU, the entire setup only uses 10-12W of power when it's not actively running a model!

I see plenty of AMD and Intel systems that burn that much power _just in the CPU_, not accounting for the rest of the system.

## Goals

I am a bit of an 'AI skeptic'. I still prefer we call it machine learning and LLMs, instead of 'AI chatbots' and stuff like that—those are marketing words. I'm also concerned the AI bubble is still inflating, and the higher it goes, the worse the fallout will be.

However, I do see some great use cases—ones made easier when you can build a tiny, compact, power-sipping LLM runner. Future CM5 + GPU dock, anyone?

For me, the three things I can see one of these builds doing are:

  - Faster, local text-to-speech and speech-to-text transcoding (for [Home Assistant Voice Control](https://www.home-assistant.io/voice_control/))
  - Useful AI 'rubber duck' sessions (I can bounce an idea off an AI model—kind of like a tiny local Google search index without the first page of results all being ads)
  - Reducing the inexorably-large footprint of LLMs running everywhere all the time. If you're running a homelab on a Dell R720, not only are you likely going deaf over time, it's eating up a _lot_ of power... a small, quiet setup for LLMs is good, IMO.

{{< figure src="./pi-5-llama-llm-gpu-rx-6700-xt-setup.jpeg" alt="Pi 5 llama.cpp RX 6700 XT setup" width="700" height="auto" class="insert-image" >}}

The Pi 5 setup I have is about $700 new, and could be down to $300-400 if you use a used graphics card or one you already own. Here's my exact setup (some links are affiliate links):

  - [Raspberry Pi 5 8GB](https://www.raspberrypi.com/products/raspberry-pi-5/) ($80)
  - [Raspberry Pi 27W Power Supply](https://www.raspberrypi.com/products/power-supply/) ($14)
  - [1TB USB SSD](https://amzn.to/3OjJysQ) ($64)
  - [Pineboards HatDrive! Bottom](https://amzn.to/3Zbz0T5) ($20)
  - [JMT M.2 Key to PCIe eGPU Dock](https://amzn.to/4eCpi0g) ($55)
  - [OCuLink cable](https://amzn.to/3YTXNJW) ($20)
  - [Lian-Li SFX 750W PSU](https://amzn.to/48T4a4R) ($130)
  - [AMD RX 6700 XT](https://amzn.to/3UXywgI) ($400)

If Raspberry Pi built a Pi 5 with 16 GB of VRAM, some larger models may be more feasible. We also can still optimize the `amdgpu` driver patch further, but follow my [Pi PCIe project](https://pipci.jeffgeerling.com) for more on that.

[All my test data and benchmarks are in this issue on GitHub](https://github.com/geerlingguy/ollama-benchmark/issues/1).

I'd like to thank GitHub user [@0cc4m](https://github.com/0cc4m) especially for help getting this working, along with others who've contributed to the issues over on my [Pi PCIe project](https://pipci.jeffgeerling.com)!
