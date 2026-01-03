---
nid: 3448
title: "Progress on Intel and Nvidia GPUs on Raspberry Pi"
slug: "progress-on-intel-and-nvidia-gpus-on-raspberry-pi"
date: 2025-02-27T20:00:53+00:00
drupal:
  nid: 3448
  path: /blog/2025/progress-on-intel-and-nvidia-gpus-on-raspberry-pi
  body_format: markdown
  redirects: []
tags:
  - a750
  - amd
  - arc
  - b580
  - drivers
  - gpu
  - graphics
  - intel
  - linux
  - nvidia
  - pcie
  - pi 5
  - raspberry pi
---

{{< figure src="./gpus-pi-5.jpg" alt="GPUs Intel Arc B580 next to Raspberry Pi 5" width="700" height="394" class="insert-image" >}}

Nvidia GPUs have been running fine on Arm for a while now—I just upgraded the [System76 Thelio Astra](/blog/2025/system76-built-fastest-windows-arm-pc) to an RTX 4080 Super and am testing it now.

But Nvidia seems to have a partnership with Ampere, which probably leads to their drivers getting priority support, and likely a few special edge cases in code to work around a couple PCIe quirks on the Altra CPUs. Nvidia _also_ builds their own Arm CPUs—a _lot_ of them—so Arm support is definitely a priority for them.

Unfortunately, that support doesn't extend to the Raspberry Pi. And a company that's in many ways the _polar opposite_, Intel, also has GPU drivers that don't work on the Pi. At least, not until very recently.

## Intel i915 and Xe driver updates for Pi 5

The Intel A-series cards use Linux's i915 driver, and B-series uses the newer Xe driver. Both drivers have a couple quirks that prevent them from loading on the Pi, but we've worked around those in [this patch against the 6.12 LTS kernel](https://github.com/geerlingguy/linux/compare/rpi-6.12.y...geerlingguy:linux:rpi-6.12.y-xe).

For the A750, using that patch and a newer compiled version of Mesa than what ships with the Pi, you can get a full desktop environment and... _some_ 3D acceleration. But it's quite glitchy, probably due to some memory corruption:

<div style="text-align: center;">
<video style="max-width: 95%; width: 640px; height: auto;" autoplay loop muted>
  <source src="./intel-a750-pi-5-youtube-jank.mp4" type="video/mp4" />
  Your browser does not support the video tag.
</video>
</div>

For the B580, I haven't gotten to a desktop environment yet, but I at least got a blinking cursor! That's something, right?

{{< figure src="./b580-pi-5-cursor.jpg" alt="Blinking cursor on B580 on Pi 5" width="700" height="394" class="insert-image" >}}

All the progress and testing is being documented in the following GitHub issues:

  - [Intel Arc A750](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/510)
  - [Intel Arc B580](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/695)

And since I know someone will ask: Resizable BAR support _should_ work on the Pi 5, but right now the Intel drivers don't seem to work with it. We're actively debugging that problem in this issue: [Resizable BAR support on Pi 5](https://github.com/raspberrypi/linux/issues/6621).

## Nvidia driver updates for Pi 5

For Nvidia, every card I test still runs into the same set of errors:

```
[    6.079514] NVRM: nvAssertOkFailedNoLog: Assertion failed: Failure: Generic Error [NV_ERR_GENERIC] (0x0000FFFF) returned from status @ kernel_gsp_tu102.c:482
[    6.079619] NVRM: RmInitAdapter: Cannot initialize GSP firmware RM
[    6.080914] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x62:0xffff:1863)
[    6.081257] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
```

I started a discussion in the Nvidia Open GPU Kernel Modules repo: [Raspberry Pi support (arm64)?](https://github.com/NVIDIA/open-gpu-kernel-modules/discussions/725#discussioncomment-11832953).

To my surprise, Andy Ritger responded [Nvidia now has an internal bug report (#5053788)](https://github.com/NVIDIA/open-gpu-kernel-modules/discussions/725#discussioncomment-11826836).

So... we'll see. I'm hopeful this is a simple bug that just needs a few tweaks to work on the Pi.

## Conclusion

I posted a short video with some demos of the Intel cards on my 2nd YouTube channel, and you can watch it below:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/rrfjNy-SB0A" frameborder='0' allowfullscreen></iframe></div>
</div>

Make sure to follow the various issues on the [Raspberry Pi PCI Express database](https://pipci.jeffgeerling.com) to see progress on different graphics cards.
