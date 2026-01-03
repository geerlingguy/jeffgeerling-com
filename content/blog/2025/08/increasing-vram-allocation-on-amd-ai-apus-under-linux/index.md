---
nid: 3483
title: "Increasing the VRAM allocation on AMD AI APUs under Linux"
slug: "increasing-vram-allocation-on-amd-ai-apus-under-linux"
date: 2025-08-08T01:38:22+00:00
drupal:
  nid: 3483
  path: /blog/2025/increasing-vram-allocation-on-amd-ai-apus-under-linux
  body_format: markdown
  redirects: []
tags:
  - ai
  - amd
  - drivers
  - gpu
  - how-to
  - linux
  - memory
  - tutorial
---

Since I saw some posts calling out the old (now deprecated) way to increase GTT memory allocations for the iGPU on AMD APUs (like the AI Max+ 395 / Strix Halo I am [testing in the Framework Mainboard AI Cluster](/blog/2025/i-clustered-four-framework-mainboards-test-huge-llms)), I thought I'd document how to increase the VRAM allocation on such boards under Linux—in this case, Fedora:

```
# To remove an arg: `--remove-args`
# Calculation: `([size in GB] * 1024 * 1024) / 4.096`
sudo grubby --update-kernel=ALL --args='amdttm.pages_limit=27648000'
sudo grubby --update-kernel=ALL --args='amdttm.page_pool_size=27648000'
sudo reboot
```

The old way, `amdgpu.gttsize`, will throw the following warning in the kernel log:

```
[    4.232151] amdgpu 0000:c1:00.0: amdgpu: [drm] Configuring gttsize via module parameter is deprecated, please use ttm.pages_limit
```

After configuring the kernel parameters and rebooting, verify the AMD GPU driver is seeing the increased memory allocation:

```
$ sudo dmesg | grep "amdgpu.*memory"
[    4.148060] [drm] amdgpu: 512M of VRAM memory ready
[    4.148068] [drm] amdgpu: 108000M of GTT memory ready.
```

The two best sources of documentation for the `amdttm.pages_limit` and `amdttm.page_pool_size` parameters I've found are:

  - [AMD Instinct MI300A system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300a.html)
  - [Preparing AMD APUs for LLM usage](https://blog.linux-ng.de/2025/07/13/getting-information-about-amd-apus/)
  - [lhl's post about AMD GTT/TTM sizes on Framework Community Forum](https://community.frame.work/t/igpu-vram-how-much-can-be-assigned/73081/7?u=geerlingguy)

For the AI Max+ 395, at least, there are some people saying 96 GB of VRAM is the maximum you can allocate to the iGPU, out of 128 GB of system RAM. But that's not true. Usually that's the maximum allocation possible in the _BIOS_ ([see Framework's BIOS settings here](https://github.com/geerlingguy/sbc-reviews/issues/80#issuecomment-3165491010)), and maybe also the maximum you can address in _Windows_—but after some experimentation with giant models on my cluster, I've found a value around 108 GB (108,000 MB) is the maximum before I start getting errors.

I tried 110 GB but ran into some segfaults while loading up models like Llama 3.1 405B across multiple nodes using llama.cpp RPC.

The GPU drivers will allocate VRAM on the fly, though, regardless of GTT settings—which can be very confusing with different tools reporting anything from 512 MB of VRAM max (like `nvtop` and `btop`, currently), to `70 GB` (`vulkaninfo`).

It seems like tools will have to adapt to dynamic VRAM allocation, as none of the monitoring tools I've tested assume VRAM can be increased on the fly.
