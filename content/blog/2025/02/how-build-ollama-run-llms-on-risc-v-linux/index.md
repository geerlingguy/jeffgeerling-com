---
nid: 3441
title: "How to build Ollama to run LLMs on RISC-V Linux"
slug: "how-build-ollama-run-llms-on-risc-v-linux"
date: 2025-02-06T03:13:13+00:00
drupal:
  nid: 3441
  path: /blog/2025/how-build-ollama-run-llms-on-risc-v-linux
  body_format: markdown
  redirects: []
tags:
  - chatbot
  - compile
  - linux
  - llama.cpp
  - llm
  - ollama
  - open source
  - performance
  - risc-v
  - tutorial
---

RISC-V is the new entrant into the SBC/low-end desktop space, and as I'm in possession of a HiFive Premier P550 motherboard, I am running it through my usual gauntlet of benchmarks—partly to see how fast it is, and partly to gauge how far along RISC-V support is in general across a wide swath of Linux software.

From my first tests on the [VisionFive 2 back in 2023](/blog/2023/risc-v-business-testing-starfives-visionfive-2-sbc) to today, RISC-V has seen quite a bit of growth, fueled by economics, geopolitical wrangling, and developer interest.

The P550 uses the ESWIN EIC7700X SoC, and while it doesn't have a _fast_ CPU, by modern standards, it is fast enough—and the system has enough RAM and IO—to run most modern Linux-y things. Including llama.cpp and Ollama!

## Compiling Ollama for RISC-V Linux

I'm running Ubuntu 24.04.1 on my P550 board, and when I try running Ollama's simple install script, I get:

```
Unsupported architecture: riscv64
```

I filed a feature request for `riscv64` support: [Support riscv64 architecture](https://github.com/ollama/ollama/issues/8857), but in the mean time, I've adapted the instructions from [this post](https://www.bit-brick.com/2024/10/02/在pi-one-上安装ollama/) in a more complete form. (Since that blog post's publication, it seems most of the little annoyances with the build process are fixed! You just need to manually compile ollama to get it to work.)

Here are the commands I ran to get Ollama built:

```
# Install cmake
sudo apt install -y cmake

# Install Go (download link is under 'Unstable versions')
wget https://go.dev/dl/go1.24rc3.linux-riscv64.tar.gz
sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.24rc3.linux-riscv64.tar.gz
export PATH=$PATH:/usr/local/go/bin

$ go version
go version go1.24rc3 linux/riscv64

# Build ollama
git clone --recurse-submodules https://github.com/mengzhuo/ollama.git
cd ollama
go build .
sudo ln -s `pwd`/ollama /usr/local/bin/ollama
```

And now you can run Ollama (`ollama serve`) in the background, and run a tiny model to see how it works:

```
# Run ollama and test a tiny model (approx. 400 MB)
ollama serve > /dev/null 2>&1 &
ollama run qwen:0.5b
```

Don't get too excited, though; on my P550, it takes _minutes_ to respond to queries with even small models like `llama3.2:3b`. I'll be posting all my benchmark results to my [ollama-benchmark repository](https://github.com/geerlingguy/ollama-benchmark/issues/17) in due time.
