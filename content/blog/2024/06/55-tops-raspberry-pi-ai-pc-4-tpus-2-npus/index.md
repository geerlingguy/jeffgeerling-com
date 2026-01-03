---
nid: 3383
title: "55 TOPS Raspberry Pi AI PC - 4 TPUs, 2 NPUs"
slug: "55-tops-raspberry-pi-ai-pc-4-tpus-2-npus"
date: 2024-06-05T21:55:56+00:00
drupal:
  nid: 3383
  path: /blog/2024/55-tops-raspberry-pi-ai-pc-4-tpus-2-npus
  body_format: markdown
  redirects: []
tags:
  - ai
  - coral
  - hailo
  - level2jeff
  - machine learning
  - npu
  - raspberry pi
  - tpu
  - video
  - youtube
---

I'm in full-on procrastination mode with [Open Sauce](https://opensauce.com) coming up in 10 days and a project I haven't started on for it, so I decided to try building the stable AI PC with all the AI accelerator chips I own:

  - Hailo-8 (26 TOPS)
  - Hailo-8L (13 TOPS)
  - 2x Coral Dual Edge TPU (8+8 = 16 TOPS)
  - 2x Coral Edge TPU (4+4 = 8 TOPS)

After my first faltering attempt in my [testing of Raspberry Pi's new AI Kit](/blog/2024/testing-raspberry-pis-ai-kit-13-tops-70), I decided to try building it again, but with a more 'proper' PCIe setup, with external 12V power to the PCIe devices, courtesy of an [uPCIty Lite PCIe HAT](https://pineboards.io/products/hat-upcity-lite-for-raspberry-pi-5) for the Pi 5.

{{< figure src="./raspberry-pi-55-tops-ai-board.jpg" alt="Raspberry Pi 55 TOPS AI Board" width="700" height="auto" class="insert-image" >}}

I'm... not sure it's that much less janky, but at least I had one board with a bunch of M.2 cards instead of many precariously stacked on top of each other!

Hardware-wise, I have 63 _potential_ TOPS of neural compute available. But only 55 are available, since the [Alftel 12x PCIe M.2 adapter card](https://pipci.jeffgeerling.com/cards_m2/alftel-12x-pcie-m2-carrier-board.html) I'm using only supports one lane per slot (the Dual Edge TPU's need two lanes wired up for A+E key—a slightly non-standard M.2 configuration).

None of that's helpful _at all_ if I can't load drivers and access all these NPUs and TPUs. Luckily, I can! Following [this guide from MidnightLink](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/648#issuecomment-2145836307) I was able to compile the Coral's apex driver on Pi OS 12, and use it with [CodeProject.AI](https://www.codeproject.com).

Upon making the necessary changes for the Coral TPUs, the Hailo accelerators also worked behind the PCIe switch—something [that doesn't work out of the box right now](https://github.com/raspberrypi/linux/issues/6206) due to some PCIe quirks on the Pi 5. Luckily fixing that only requires the addition of an overlay inside `/boot/firmware/config.txt`:

```
# Required for the Coral TPUs.
kernel=kernel8.img
dtoverlay=pineboards-hat-ai

# Required for the Hailo, unless using the above overlays for Coral compatibility.
dtoverlay=pciex1-compat-pi5,no-mip
```

If you're _not_ using a PCIe switch like I am, you don't need to add any of that, except maybe the `kernel` change for Coral TPUs. And if you're not using a switch (or you have one PCIe Gen 3-rated), you should also try `dtparam=pciex1_gen=3` to almost double your bandwidth.

Anyway, once I did all that, I could also use the Hailo for inference, though examples of how to use _multiple_ Hailo's are not easy to find yet. I know the topology of the [Hailo-8 Century](https://hailo.ai/products/ai-accelerators/hailo-8-century-high-performance-pcie-card/) is very similar to what I've built... just a little less janky. It would be interesting to see full support for multi-NPU setups like this from more software.

[EBV Elektronik](https://www.linkedin.com/feed/update/urn:li:activity:7204200259789533184/) even demoed running 4x Raspberry Pi cameras through 4 separate Hailo-8 NPUs on a [Seaberry](https://pipci.jeffgeerling.com/boards_cm/seaberry.html) board a couple years ago.

With the Hailo-8L available at a more attractive price ($70 in the AI Kit, at least), it's not unreasonable to expect people to hack together systems with multiple NPUs like this. Maybe not 12, though.

I have a [video where I go into more detail](https://www.youtube.com/watch?v=oFNKfMCGiqE) on my 2nd channel, Level2Jeff:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/oFNKfMCGiqE" frameborder='0' allowfullscreen></iframe></div>
</div>

There are still many caveats, which mean I can't just say "this setup is faster than a Copilot+ PC that has 40 TOPS":

  - Software support for uniting multiple NPUs is a bit lacking. Some things can support it, but it's not as easy as one big accelerator.
  - Hailo hasn't stated exactly how much RAM they have on-chip—but it's probably not that much, limiting the use to smaller models.
  - The Pi's PCIe Gen 2 bus can be uprated to Gen 3 (and in my experience works great at this speed)... but most PCIe switches that aren't extremely expensive are still Gen 2, so you are a bit bandwidth-constrained with this setup.
