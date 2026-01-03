---
nid: 3420
title: "AMD Radeon PRO W7700 running on Raspberry Pi"
slug: "amd-radeon-pro-w7700-running-on-raspberry-pi"
date: 2024-11-15T15:00:36+00:00
drupal:
  nid: 3420
  path: /blog/2024/amd-radeon-pro-w7700-running-on-raspberry-pi
  body_format: markdown
  redirects:
    - /blog/2024/amd-radeon-pro-w7700-gpu-running-on-raspberry-pi
aliases:
  - /blog/2024/amd-radeon-pro-w7700-gpu-running-on-raspberry-pi
tags:
  - amd
  - gpu
  - graphics
  - raspberry pi
  - video
  - youtube
---

{{< figure src="./pi-5-amd-radeon-pro-w7700-workstation-graphics-card.jpg" alt="Raspberry Pi 5 with AMD Radeon PRO W7700 graphics card" width="700" height="auto" class="insert-image" >}}

After _years_ of work among a bunch of people in the Pi community (special callout to Coreforge!), we finally have multiple generations of AMD graphics cards working on the Raspberry Pi 5.

We [recently got Polaris-era GPUs working](/blog/2024/use-external-gpu-on-raspberry-pi-5-4k-gaming) (like the RX460), but in the past month we've gotten 6000 and 7000-series GPUs up and running. And many parts of the driver work at full performance—well, as much as can be had on the Raspberry Pi's single PCIe Gen 3 lane (8 GT/sec)!

I've been testing tons of modern AAA games, like Doom Eternal and Crysis Remastered, and can get 10-15 fps at 4K with Ray Tracing on, or 15-20 fps at 4K. Dropping down to 1080p is not enough to overcome the Pi's CPU bottleneck—only at resolutions under 720p does the Pi's CPU and the single PCIe lane not seem to get in the way _quite_ as much.

{{< figure src="./doom-eternal-rtx-raspberry-pi-5.jpg" alt="Doom Eternal with RTX on Raspberry Pi 5" width="700" height="auto" class="insert-image" >}}

The screenshot above is showing some gameplay at 4K High settings, with ray tracing enabled. Not too shabby for a Raspberry Pi! Though the CPU and 8 GB of RAM holds back the GPU for modern AAA games.

Slightly older games like Portal 2 run at 4K 60fps with zero issues. Full acceleration, smooth gameplay, with only an occasional hiccup as an asset loads in.

<div style="text-align: center;">
<video style="max-width: 95%; width: 640px; height: auto;" controls>
  <source src="./portal-2-raspberry-pi-5-gameplay.mp4" type="video/mp4" />
  Your browser does not support the video tag.
</video>
</div>

I'll have more examples later, but first: I _hate_ when someone shows you something cool, but doesn't show you how to do it yourself. So here's exactly how you can set up your own Pi 5 + AMD 7000-series graphics card:

## How to use a Radeon 7000-series card with the Pi 5

  1. Clone the [Raspberry Pi Linux kernel](https://github.com/raspberrypi/linux/tree/rpi-6.6.y) patching the default Raspberry Pi `6.6.y` kernel tree with [Coreforge's GPU-enablement patch](https://github.com/raspberrypi/linux/compare/rpi-6.6.y...Coreforge:linux:rpi-6.6.y-gpu) (or just check out Coreforge's branch directly).
  2. Before compiling the kernel, run `make menuconfig` and select the options:
    1. Kernel Features > Page Size > 4 KB (for Box86 compatibility)
    2. Kernel Features > Kernel support for 32-bit EL0 > Fix up misaligned multi-word loads and stores in user space
    3. Kernel Features > Fix up misaligned loads and stores from userspace for 64bit code
    4. Device Drivers > Graphics support > AMD GPU (optionally SI/CIK support too)
    5. Device Drivers > Graphics support > Direct Rendering Manager (XFree86 4.1.0 and higher DRI support) > Force Architecture can write-combine memory
  3. Recompile the kernel following [Raspberry Pi's instructions](https://www.raspberrypi.com/documentation/computers/linux_kernel.html#building)
  4. Install the AMD firmware (see note below)
  6. Reboot the Pi with the card attached using an appropriate PCIe riser and external ATX power supply.

### AMD GPU Firmware for Pi OS 12 (Bookworm)

Because Pi OS 12 is based on Debian 12 Bookworm, and its [`firmware-amd-graphics`](https://packages.debian.org/bookworm/all/firmware-amd-graphics/filelist) package doesn't include the firmware for the latest-generation AMD cards, you  have to install that package _and_ download supplemental firmware files from the [`linux-firmware` repo](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/tree/amdgpu):

```
# Install the base AMD GPU firmware
sudo apt install -y firmware-amd-graphics

# Download supplemental firmware files for 7000-series cards
cd /usr/lib/firmware/amdgpu
sudo wget https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/amdgpu/psp_13_0_10_sos.bin & \
sudo wget https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/amdgpu/smu_13_0_10.bin & \
sudo wget https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/amdgpu/gc_11_0_3_pfp.bin & \
sudo wget https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/amdgpu/gc_11_0_3_mes_2.bin & \
sudo wget https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/amdgpu/gc_11_0_3_mes1.bin & \
sudo wget https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/amdgpu/psp_13_0_10_ta.bin & \
sudo wget https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/amdgpu/gc_11_0_3_me.bin & \
sudo wget https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/amdgpu/gc_11_0_3_rlc.bin & \
sudo wget https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/amdgpu/gc_11_0_3_mec.bin & \
sudo wget https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/amdgpu/gc_11_0_3_imu.bin & \
sudo wget https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/amdgpu/sdma_6_0_3.bin
```

Confirm everything is working by plugging a monitor into the graphics card; then confirm the card's GPU is in use by running `glxinfo -B` (part of the `mesa-utils` package), for example:

```
$ DISPLAY=:0 glxinfo -B
name of display: :0
display: :0  screen: 0
direct rendering: Yes
Extended renderer info (GLX_MESA_query_renderer):
    Vendor: AMD (0x1002)
    Device: AMD Radeon Pro W7700 (gfx1101, LLVM 15.0.6, DRM 3.54, 6.6.60-v8-AMDGPU+) (0x7470)
    Version: 23.2.1
    Accelerated: yes
    Video memory: 15360MB
...
```

(Prepend `DISPLAY=:0` if you're running these commands over SSH.)

### Hardware video transcoding support

If you want to enable hardware transcoding, you need to install the Mesa VAAPI drivers:

```
sudo apt install mesa-va-drivers vainfo
```

Then you should be able to see the VAAPI info, and apps like OBS (`sudo apt install obs-studio`) should be able to use the hardware transcoding instead of `x264` running on the Pi's CPU. Confirm it's working with `vainfo`:

```
pi@pi5-pcie:~ $ vainfo
libva info: VA-API version 1.17.0
libva info: Trying to open /usr/lib/aarch64-linux-gnu/dri/radeonsi_drv_video.so
libva info: Found init function __vaDriverInit_1_17
libva info: va_openDriver() returns 0
vainfo: VA-API version: 1.17 (libva 2.12.0)
vainfo: Driver version: Mesa Gallium driver 23.2.1-1~bpo12+rpt3 for AMD Radeon Pro W7700 (gfx1101, LLVM 15.0.6, DRM 3.54, 6.6.60-v8-AMDGPU+)
vainfo: Supported profile and entrypoints
      VAProfileH264ConstrainedBaseline:	VAEntrypointVLD
      VAProfileH264ConstrainedBaseline:	VAEntrypointEncSlice
      VAProfileH264Main               :	VAEntrypointVLD
      VAProfileH264Main               :	VAEntrypointEncSlice
      VAProfileH264High               :	VAEntrypointVLD
      VAProfileH264High               :	VAEntrypointEncSlice
      VAProfileHEVCMain               :	VAEntrypointVLD
      VAProfileHEVCMain               :	VAEntrypointEncSlice
      VAProfileHEVCMain10             :	VAEntrypointVLD
      VAProfileHEVCMain10             :	VAEntrypointEncSlice
      VAProfileJPEGBaseline           :	VAEntrypointVLD
      VAProfileVP9Profile0            :	VAEntrypointVLD
      VAProfileVP9Profile2            :	VAEntrypointVLD
      VAProfileAV1Profile0            :	VAEntrypointVLD
      VAProfileAV1Profile0            :	VAEntrypointEncSlice
      VAProfileNone                   :	VAEntrypointVideoProc
```

## Hardware

The exact hardware I used is listed below. Some of the links are Amazon affiliate links, but you can just search the text if you want to avoid the links ;)

Here's a list of all the hardware I used for my setup (some links are affiliate links):

  - [AMD RX 6700 XT](https://amzn.to/3UOyQOX)
  - [AMD Radeon PRO W7700](https://amzn.to/40MXNxO)
  - [OCuLink M.2 to GPU dock](https://amzn.to/4hQxCg0)
  - [OCuLink cable](https://amzn.to/3YMXIHT)
  - [Pineboards M.2 HAT](https://pineboards.io/products/hatdrive-bottom-2230-2242-2280-for-rpi5)
  - [Raspberry Pi 5 8GB](https://www.raspberrypi.com/products/raspberry-pi-5/)
  - [Acer Nitro 27" 4K monitor](https://amzn.to/4hLBDlN)
  - [Lian-Li 750W SFX PSU](https://amzn.to/3AKIefE)

## What works

{{< figure src="./portal-2-4k-max-raspberry-pi-5.jpg" alt="Portal 2 at 4K Max settings on Raspberry Pi 5" width="700" height="auto" class="insert-image" >}}

The patches are still not complete, but are very stable (I've had my setup running continuously for a few days at a time, with no lockups). Not everything works, but many things do:

  - **Steam games** (emulated via Box86/Proton): Doom Eternal, Crysis Remastered, Doom 3, Halo MCC (Halo 3), Minecraft Bedrock Edition, Obduction, Portal 2, SuperTuxKart, and [the list goes on](https://box86.org/app/)...
  - **Multiple Monitors**: I tested up to 6 displays, and could even have my two 4K displays at 4K while the others were at 1080p... however Pi OS's resolution scaling works best if all your monitors are at similar scales, so it can be frustrating optimizing for either 4K or 1080p!
  - **Hardware Transcoding**: At least when you're not bandwidth-constrained on the Pi's PCIe bus! Trying to capture the screen is tricky because of the dance the Pi needs to do between the compositor, system RAM/CPU, and the GPU. Apps like VLC and `ffmpeg` may need to be compiled to work correctly with VAAPI on the Pi 5—at least for now. Transcoding isn't perfect though...
  - **OBS/Live Streaming**: I was able to game at 4K and capture the display smoothly at 720p. But higher resolutions like 1080p or 4K would cause a lot of frame dropping. The _display_ output was smooth, but the OBS stream got choppy. Probably a bandwidth issue (see previous bullet point).

### Things that don't work

  - **Hardware Transcoding**: It works but can have issues (and on some cards, artifacts in the encoded stream). I also haven't had a chance to test with Jellyfin or Plex yet, but I'm hopeful it will 'just work.'
  - **GPU-accelerated LLMs that require ROCm (or CUDA)**: There are some efforts to accelerate frameworks like [Ollama](https://ollama.com) and [LM Studio](https://lmstudio.ai) with Vulkan (which is running great on the Pi 5... but those efforts usually target x86 and not Arm! I'm hopeful we can make headway here.
  - **Steam games**: Any games requiring anti-cheat, and some games that have weird code/launchers, like Red Dead Redemption 2. I also couldn't get Forza Horizon 4 to launch due to a lack of RAM, and Tomb Raider (2013) and Halo: Reach wouldn't launch for unknown reasons.
  - **Cryptocurrency mining**: Even if it _did_ work, I wouldn't test it. I don't touch crypto with a 10 ft. pole, for a variety of reasons. (So please stop asking in DMs!)
  - **Blender**: So far I haven't been able to get Blender to run on arm64; the only time I've been successful is when running the x86 version on Windows on Arm on the Ampere Workstation—but that's far from optimal, and relied on brute-force emulation with the 128 core Altra Max CPU!

## Patch Notes / Current Status

We're still working on the patches; it's kind of a side hobby for everyone involved, and people dip in and dip out to test various aspects of the patches over time.

If you want to get involved, take a look at the [existing graphics cards in the database](https://pipci.jeffgeerling.com/#gpus-graphics-cards) over on the Raspberry Pi PCIe website!

## Demo

For some example gameplay footage at 4K, along with demos of multi-display work and OBS hardware encoding, check out my video on YouTube:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/7Qx_bdFSSuc" frameborder='0' allowfullscreen></iframe></div>
</div>
