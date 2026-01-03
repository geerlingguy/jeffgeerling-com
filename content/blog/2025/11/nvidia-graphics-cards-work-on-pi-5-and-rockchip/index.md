---
nid: 3515
title: "Nvidia Graphics Cards work on Pi 5 and Rockchip"
slug: "nvidia-graphics-cards-work-on-pi-5-and-rockchip"
date: 2025-11-26T23:45:45+00:00
drupal:
  nid: 3515
  path: /blog/2025/nvidia-graphics-cards-work-on-pi-5-and-rockchip
  body_format: markdown
  redirects: []
tags:
  - drivers
  - gpu
  - linux
  - nvidia
  - open source
  - pcie
  - raspberry pi
  - rk3588
---

A few months ago, GitHub user [@yanghaku dropped a 15 line patch to fix GPU support for practically all AMD GPUs](/blog/2025/full-egpu-acceleration-on-pi-500-15-line-patch) on the Raspberry Pi (and demoed a 3080 running on the Pi with a separate, unreleased patch). This week, GitHub user [@mariobalanica dropped this (larger) patch which does the same for Nvidia GPUs](https://github.com/NVIDIA/open-gpu-kernel-modules/pull/972)!

{{< figure src="./raspberry-pi-5-in-mug-with-nvidia-a4000.jpeg" alt="Raspberry Pi 5 in mug with Nvidia A4000 GPU" width="700" height="394" class="insert-image" >}}

I have a Raspberry Pi and an Nvidia graphics card—and I'm easily distracted. So I put down my testing of a GB10 system for a bit, and compiled mariobalanica's branch.

## Building on the Pi

These directions are subject to change, as the code in use is still under active development.

  1. Flash Pi OS 13 'Trixie' to a new boot drive using Raspberry Pi Imager
  1. Boot the Pi and run `sudo apt update && sudo apt upgrade -y` to make sure you're on the latest versions
  1. Switch to the 4K kernel (right now the PR only works on the 4K kernel, not the 16K kernel the Pi runs by default):

         sudo nano /boot/firmware/config.txt
         
         # Add the following line at the bottom of the file:
         kernel=kernel8.img
         
         sudo reboot

  1. Reboot the Pi: `sudo reboot`
  1. Download the latest arm64 Nvidia Linux arm driver `.run` file from [here](https://www.nvidia.com/en-us/drivers/unix/) (I used version `580.95.05`)
  1. Run the `.run` file without building kernel modules: `sudo sh ./NVIDIA-Linux-aarch64-580.95.05.run --no-kernel-modules`
  1. Clone [@mariobalanica](https://github.com/mariobalanica)'s Nvidia kernel module branch: `cd ~/Downloads && git clone --branch non-coherent-arm-fixes https://github.com/mariobalanica/open-gpu-kernel-modules.git`
  1. Build and install the open kernel modules from the branch you just cloned:

         cd open-gpu-kernel-modules
         make modules -j$(nproc)
         sudo make modules_install -j$(nproc)

  1. Update the module dependency database: `sudo depmod -a`
  1. Reboot: `sudo reboot`

## Display Output

For my Nvidia A4000, at least, I was unable to get any of the DisplayPort connections to output an image to my monitor. I didn't see any errors in `dmesg`, nor did I have a blank display with a blinking cursor (that happens on [Intel GPUs on the Pi](/blog/2025/all-intel-gpus-run-on-raspberry-pi-and-risc-v) currently, unless you compile a later version of Mesa—there you can press Alt + F2 to get to a console at least).

{{< figure src="./pi-cm5-nvidia-a4000-blank-screen.jpg" alt="Pi CM5 with Nvidia A4000 with blank screen" width="700" height="394" class="insert-image" >}}

I even tried disabling the iGPU (commenting `dtoverlay=vc4-kms-v3d` out in the boot config file and restarting), and that had no effect.

A headless Pi can still do a lot, though, so I moved on to testing GPU-accelerated tasks next.

## GPU Accelerated Compute

For best performance, you should [configure the PCIe lane on the Pi to use PCIe Gen 3](/blog/2023/forcing-pci-express-gen-30-speeds-on-pi-5).

`nvidia-smi` did return correct GPU info, though:

```
jgeerling@cm5:~ $ nvidia-smi
Wed Nov 26 16:52:14 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.95.05              Driver Version: 580.95.05      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX A4000               Off |   00000001:01:00.0 Off |                  Off |
| 41%   31C    P8              8W /  140W |       1MiB /  16376MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
```

I wanted to test out `llama.cpp` for GPU AI acceleration, so I [compiled that from source](/blog/2024/llms-accelerated-egpu-on-raspberry-pi-5) using the Vulkan option, since I couldn't quickly get CUDA working. CUDA may perform a bit faster for Nvidia GPUs. But, for now, Vulkan it is!

```
jgeerling@cm5:~/Downloads/llama.cpp $ ./build/bin/llama-bench -m models/Llama-3.2-3B-Instruct-Q4_K_M.gguf -n 128 -p 512,4096 -pg 4096,128 -ngl 99 -r 2
ggml_vulkan: Found 2 Vulkan devices:
ggml_vulkan: 0 = NVIDIA RTX A4000 (NVIDIA) | uma: 0 | fp16: 1 | bf16: 0 | warp size: 32 | shared memory: 49152 | int dot: 1 | matrix cores: NV_coopmat2
ggml_vulkan: 1 = V3D 7.1.10.2 (V3DV Mesa) | uma: 1 | fp16: 0 | bf16: 0 | warp size: 16 | shared memory: 16384 | int dot: 0 | matrix cores: none
build: 7cba58bbe (7169)
```

| model                          |       size |     params | backend    | ngl |            test |                  t/s |
| ------------------------------ | ---------: | ---------: | ---------- | --: | --------------: | -------------------: |
| llama 3B Q4_K - Medium         |   1.87 GiB |     3.21 B | Vulkan     |  99 |           pp512 |    3174.16 ± 1248.07 |
| llama 3B Q4_K - Medium         |   1.87 GiB |     3.21 B | Vulkan     |  99 |          pp4096 |       2998.82 ± 1.12 |
| llama 3B Q4_K - Medium         |   1.87 GiB |     3.21 B | Vulkan     |  99 |           tg128 |        121.98 ± 0.29 |
| llama 3B Q4_K - Medium         |   1.87 GiB |     3.21 B | Vulkan     |  99 |    pp4096+tg128 |       1404.36 ± 0.11 |

These numbers are pretty good for this particular GPU, but I haven't validated it with CUDA and Vulkan in other systems to say whether this is as good as can be expected out of an A4000...

Here's a quick video showing the above setup in action:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/SPTYjF8qH0A" frameborder='0' allowfullscreen></iframe></div>
</div>

## CUDA Support

I haven't worked much with CUDA before, generally relying on distro packages when testing on x86. So I had to figure out how to set up CUDA on Debian with this custom patched version of the open GPU driver.

To find the right version, you have to browse through the [CUDA Toolkit Download Archive](https://developer.nvidia.com/cuda-toolkit-archive), and find the right version that corresponds to the driver version you install—in our case, `580.95.05`.

And it just so happens CUDA version 13.0.2 is the correct one. Download it (I chose the `Linux` > `arm64-sbsa` > `Native` > `Ubuntu` > `24.04` > `runfile (local)` option) and run the installer:

```
wget https://developer.download.nvidia.com/compute/cuda/13.0.2/local_installers/cuda_13.0.2_580.95.05_linux_sbsa.run
sudo sh cuda_13.0.2_580.95.05_linux_sbsa.run
```

When installing, de-select the driver install option so it doesn't wipe out your custom driver installed earlier. Then update a couple environment variables:

```
export PATH=${PATH}:/usr/local/cuda-13.0/bin
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/cuda-13.0/lib64
```

Once you've done all that, confirm that CUDA is installed:

```
$ nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2025 NVIDIA Corporation
Built on Wed_Aug_20_01:57:39_PM_PDT_2025
Cuda compilation tools, release 13.0, V13.0.88
Build cuda_13.0.r13.0/compiler.36424714_0
```

If you'd like to further confirm CUDA is working, you can run the `deviceQuery` utility provided in the [cuda-samples](https://github.com/nvidia/cuda-samples) repository. Follow the README in that repository, then run deviceQuery in the build directory:

```
$ ./build/Samples/1_Utilities/deviceQuery/deviceQuery 
./build/Samples/1_Utilities/deviceQuery/deviceQuery Starting...

 CUDA Device Query (Runtime API) version (CUDART static linking)

Detected 2 CUDA Capable device(s)

Device 0: "NVIDIA GeForce RTX 4070 Ti"
...

Device 1: "NVIDIA RTX A4000"
...
  Device PCI Domain ID / Bus ID / location ID:   1 / 4 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >
> Peer access from NVIDIA GeForce RTX 4070 Ti (GPU0) -> NVIDIA RTX A4000 (GPU1) : No
> Peer access from NVIDIA RTX A4000 (GPU1) -> NVIDIA GeForce RTX 4070 Ti (GPU0) : No

deviceQuery, CUDA Driver = CUDART, CUDA Driver Version = 13.0, CUDA Runtime Version = 13.0, NumDevs = 2
Result = PASS
```

## Conclusion

The driver patch is meant to work with not only the Pi, but many other Arm systems where Nvidia cards are not yet officially supported. So... practically anything that's not big enterprise cloud-native.

mariobalanica was building and testing the patch on an RK3588 board, which should actually go a bit faster than the Pi—it's SoC is faster and more efficient, _and_ it has PCIe Gen 3 x4 support (the Pi 5 only does up to Gen 3 x1).

At this point, I'm working on more tests with more cards, and my next priority will be getting display output. Hopefully it's something simple, and I don't have to recompile the kernel again :D
