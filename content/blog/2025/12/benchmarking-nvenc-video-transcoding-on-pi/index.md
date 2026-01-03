---
nid: 3520
title: "Benchmarking NVENC video transcoding on the Pi"
slug: "benchmarking-nvenc-video-transcoding-on-pi"
date: 2025-12-11T22:06:11+00:00
drupal:
  nid: 3520
  path: /blog/2025/benchmarking-nvenc-video-transcoding-on-pi
  body_format: markdown
  redirects: []
tags:
  - amd
  - cm5
  - drivers
  - gpu
  - jellyfin
  - linux
  - nvidia
  - pcie
  - raspberry pi
  - transcoding
---

{{< figure src="./asus-proart-egpu-dock-4070-ti-raspberry-pi.jpg" alt="ASUS ProArt 4070 Ti in eGPU dock on Raspberry Pi CM5" width="700" height="394" class="insert-image" >}}

Now that [Nvidia GPUs run on the Raspberry Pi](/blog/2025/nvidia-graphics-cards-work-on-pi-5-and-rockchip), I've been putting all the ones I own through their paces.

Many people have an older Nvidia card (like a 3060) laying around from an upgrade. So could a Pi be suitable for GPU-accelerated video transcoding, either standalone for conversion, or running something like Jellyfin for video library management and streaming?

That's what I set out to do, and the first step, besides getting the drivers and CUDA going (see blog post linked above), was to find a way to get a repeatable benchmark going.

Luckily, I found Proryanator's [encoder-benchmark](https://github.com/Proryanator/encoder-benchmark/), which is built with Rust and uses `ffmpeg` to benchmark _any_ popular GPU-accelerated video endcoder/decoder (including Nvidia, AMD, Intel, and Apple).

## Raw performance: `encoder-benchmark`

I set it up on my Pi like so:

```
# Install rust/cargo
curl https://sh.rustup.rs -sSf | sh
# (then log out / log back in to let the environment changes take effect)

# Build the benchmark
git clone https://github.com/Proryanator/encoder-benchmark.git
cd encoder-benchmark
cargo build --release

# Manually download source files (I chose `4k-60.y4m`, `1080-60.y4m`, and `720-60.y4m`):
https://utsacloud-my.sharepoint.com/personal/hlz000_utsa_edu/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fhlz000%5Futsa%5Fedu%2FDocuments%2FEncoding%20Files&ga=1

# Run the benchmark
./target/release/benchmark
```

On my Raspberry Pi Compute Module 5, with an Nvidia 4070 Ti, I got the following results:

| Video file | File size | Time (sec) | Average fps |
| --- | --- | --- | --- |
| 720-60.y4m | 2.4G | 4 | 438 |
| 1080-60.y4m | 5.3G | 15 | 122 |
| 4k-60.y4m | 11G | 62.206 | 30 |

The 1% lows were a little troubling—usually they were around half the average FPS, meaning the GPU is probably not getting fed data fast enough to feed the NVENC cores...

Part of that is probably due to my boot volume being an external USB 3.0 SSD (maximum read speeds around 300-350 MB/sec), and the other part the Pi's paltry PCIe specs: one lane of Gen 3, for 8 GT/sec.

So I put the card in my Intel Core Ultra 285K PC instead, where it has a full PCIe Gen 5 x16 slot. The 4070 Ti is only rated for Gen 4, but still... that's a lot more bandwidth!

On the PC, I got:

| Video file | File size | Time (sec) | Average fps |
| --- | --- | --- | --- |
| 720-60.y4m | 2.4G | 1 | 1206 |
| 1080-60.y4m | 5.3G | 2 | 630 |
| 4k-60.y4m | 11G | 11 | 169 |

This is... a LOT faster. And looking at `nvtop`'s output, I could see why: on the Pi, the PCIe bus bandwidth limited the NVENC engine to about 800 MB/sec of data throughput, which slows down transfer of larger video files especially (e.g. 4K ProRes, or high quality BD rips). Not only that, the bus has to wait for the slower disk to catch up.

On the Intel PC, I saw the PCIe bandwidth max out around 2 GB/sec, continuously, as it was fed from a fast NVMe drive also running at Gen 4 speeds...

## Jellyfin, though?

But for my movie library, streaming to two or three devices in my home, I don't care too much about maximum throughput, unconstrained.

I just need to make sure I can feed video through to devices like TVs or laptops, or remote locations through my in-home VPN, at various bitrates.

And on that account, the Pi seems to do just fine.

I [installed Jellyfin](https://jellyfin.org/docs/general/installation/) using their official install script, logged in, and set the Playback > Transcoding option to "Nvidia NVENC". Then after putting a few of my 4K and 1080p videos (all encoded in H.265) on my Pi, I played two at once:

{{< figure src="./pi-cm5-transcoding-jellyfin-nvidia-4070-ti-2stream-nvtop.jpg" alt="Raspberry Pi CM5 transcoding two videos with Nvidia GPU" width="700" height="394" class="insert-image" >}}

It worked just fine.

The total system power draw at idle with this setup is around 29W (including Pi and eGPU dock PSU losses), and it ramps up to around 100W while transcoding one stream (4K), and 130W transcoding two streams (4K and 1080p).

So, if you have a GPU, a Pi, and a spare PSU laying around, consider buying an eGPU dock and plonking them together. You can do worse, and because you're bound to hit a snag or two with this still-strange setup, maybe you'll learn something new!

I've been running a lot of other tests on my Nvidia and AMD graphics cards lately, I'll cover more later :)
