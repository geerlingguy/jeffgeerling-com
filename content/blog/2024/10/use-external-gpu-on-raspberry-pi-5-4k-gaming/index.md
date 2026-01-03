---
nid: 3409
title: "Use an External GPU on Raspberry Pi 5 for 4K Gaming"
slug: "use-external-gpu-on-raspberry-pi-5-4k-gaming"
date: 2024-10-08T17:17:58+00:00
drupal:
  nid: 3409
  path: /blog/2024/use-external-gpu-on-raspberry-pi-5-4k-gaming
  body_format: markdown
  redirects:
    - /blog/2024/full-external-gpu-acceleration-on-raspberry-pi-5-2024
    - /blog/2024/external-gpu-does-full-4k-gaming-on-raspberry-pi-5
    - /blog/2024/how-use-external-gpu-full-4k-gaming-on-raspberry-pi-5
    - /blog/2024/how-use-external-gpu-4k-gaming-on-raspberry-pi-5
    - /blog/2024/how-use-external-gpu-on-raspberry-pi-5-4k-gaming
aliases:
  - /blog/2024/full-external-gpu-acceleration-on-raspberry-pi-5-2024
  - /blog/2024/external-gpu-does-full-4k-gaming-on-raspberry-pi-5
  - /blog/2024/how-use-external-gpu-full-4k-gaming-on-raspberry-pi-5
  - /blog/2024/how-use-external-gpu-4k-gaming-on-raspberry-pi-5
  - /blog/2024/how-use-external-gpu-on-raspberry-pi-5-4k-gaming
tags:
  - 4k
  - amd
  - gaming
  - gpu
  - kernel
  - linux
  - livestream
  - open source
  - raspberry pi
  - video
---

After I saw Pineboards [4K Pi 5 external GPU gaming demo](https://www.tomshardware.com/raspberry-pi/raspberry-pi-5-and-external-amd-gpu-used-to-play-4k-open-source-kart-racing-game-pineboards-demos-supertuxkart-using-hat-upcity-lite-board) at Maker Faire Hanover, I decided it was time to set up my GPU test rig and see how the [Pi OS `amdgpu` Linux kernel patch](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/564) is going.

{{< figure src="./amdgpu-rx-460-running-glmark2-pi-5.jpeg" alt="GLmark2 running on Pi 5 with AMD RX 460 external GPU" width="700" height="auto" class="insert-image" >}}

I tested it out [on a livestream over the weekend](https://www.youtube.com/watch?v=EAlrCFJZlnI), but I thought I'd document the current state of the patch, how to apply it, and what else is left to do to get _full_ external GPU support on the Raspberry Pi.

I also have a full video up with more demonstrations of the GPU in use, you can watch it below:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/a-ImUnRwjAo" frameborder='0' allowfullscreen></iframe></div>
</div>

## Hardware setup for an external PCI Express GPU

There are a few different routes you can go to physically plug a graphics card into a Pi 5.

My preferred setup is [this JMT External Graphics Card stand](https://amzn.to/3U0obQR) that uses Oculink with an M.2 to Oculink adapter (included). To use it, you also need an [Oculink cable](https://amzn.to/47YtVAi), and those together run $80.

On top of that (or more specifically, on top of the _Pi_), you need a HAT that converts the PCIe FFC connection on the Pi 5 to an M.2 slot, and my choice is the [Pineboards HatDrive! Bottom](https://pineboards.io/products/hatdrive-bottom-2230-2242-2280-for-rpi5), though there are [tons of other options](https://pipci.jeffgeerling.com/hats). That adds on another $20 or so.

The other option is to skip the external GPU stand entirely and mount it right on top of the Pi 5. You can do that with the [uPCIty Lite](https://pineboards.io/products/hat-upcity-lite-for-raspberry-pi-5), which is $30, and has an open-ended x4 PCIe slot.

That takes care of the PCIe signaling—but you also need to provide adequate power.

The Pi's PCIe FFC only supports up to 5W of power output. Regardless of the HAT you choose, you'll need to provide adequate power to the _slot_ (up to 75W), and usually also to the card you insert into it (via PCIe ATX power connectors—requirements vary by card).

For that, I'm using this [LIAN LI 750W SFX PSU](https://amzn.to/4eKapd0), which has adequate power and cabling to supply power to the PCIe riser—or the uPCIty's 4-pin 12V CPU power intput, as well as to the graphics card's supplemental PCIe power jack.

{{< figure src="./amdgpu-rx-460-plugged-into-raspberry-pi-5.jpeg" alt="external AMD RX 460 running on Raspberry Pi 5" width="700" height="auto" class="insert-image" >}}

_If you choose uPCIty Lite_, or some other method that doesn't have a 24-pin ATX power input like the graphics card stand I'm using, you'll also need a way to force your ATX power supply to turn on, like this [ATX 24-pin Power Switch](https://amzn.to/3Y9TafD)—or a jumper placed across the appropriate pins on the connector.

## Choosing a card and Getting PCIe Gen 3

With the PCI Express slot ready to go, you need to choose a card to go _into_ it. After a few years of [testing various cards](https://pipci.jeffgeerling.com/#gpus-graphics-cards), our little group has settled on Polaris generation AMD graphics cards.

Why? Because they're _new enough_ to use the open source `amdgpu` driver in the Linux kernel, and _old enough_ the drivers and card details are pretty well known.

We had some success with older cards using the `radeon` driver, but that driver is older and the hardware is a bit outdated for any practical use with a Pi.

_Nvidia_ hardware is right out, since outside of community `nouveau` drivers, Nvidia provides little in the way of open source code for the parts of their drivers we need to fix any quirks with the card on the Pi's PCI Express bus.

GitHub user Coreforge and myself (and Pineboards now, too) all chose the RX 460 4 GB as the model to test with, because it's new enough to be useful, old enough to be cheap, and uses PCI Express Gen 3, which is perfect for the Pi 5's bus.

Speaking of, to force Gen 3 speed on the Pi 5's PCI Express bus, you need to edit `/boot/firmware/config.txt` and add the following line at the bottom:

```
dtparam=pciex1_gen=3
```

The Pi 5's external PCI Express bus only provides 1 lane (x1), for 8 GT/s (a boost from the 5 GT/s you get with the default PCIe Gen 2 speed).

## Applying the Linux kernel patch

With the hardware connected and the Gen 3 speed configured, you could boot the Pi and identify the card using `lspci`, but Raspberry Pi OS won't be able to _use_ the card, because the `amdgpu` driver isn't included by default in the Pi OS.

Therefore, it's time to [recompile the Linux kernel](https://www.redshirtjeff.com/shop/p/recompile-linux-shirt)!

Follow Raspberry Pi's guide: [Build the Linux kernel](https://www.raspberrypi.com/documentation/computers/linux_kernel.html#building).

After the `git clone` step, you'll need to download and apply [the patchset we've been working on](https://github.com/geerlingguy/linux/pull/8) to enable Polaris-generation cards on Pi 5. Assuming you're in the `linux` checkout directory (`cd linux`), run these commands:

```
wget -O amdgpu-pi5.patch https://github.com/geerlingguy/linux/pull/8.patch
git apply -v amdgpu-pi5.patch 
```

You should see it apply successfully—if not, either the patch is outdated for the latest `6.6.y` Pi OS branch, or you may have checked out a different kernel release. This particular patch was made against the 6.6.y Linux kernel.

Before you start recompiling the Linux kernel (following the rest of the instructions in the Pi kernel guide), you should also patch in Coreforge's optimized `memcpy` library:

```
wget https://gist.githubusercontent.com/Coreforge/91da3d410ec7eb0ef5bc8dee24b91359/raw/b4848d1da9fff0cfcf7b601713efac1909e408e8/memcpy_unaligned.c

gcc -shared -fPIC -o memcpy.so memcpy_unaligned.c
sudo mv memcpy.so /usr/local/lib/memcpy.so
sudo nano /etc/ld.so.preload

# Put the following line inside ld.so.preload:
/usr/local/lib/memcpy.so
```

{{< figure src="./linux-kernel-configuration-6.6.y-pi-5.jpg" alt="Linux kernel compilation on Pi 5 - menuconfig graphics drivers" width="700" height="auto" class="insert-image" >}}

To make sure the `amdgpu` driver is enabled when you recompile the Linux kernel, run `make menuconfig` (you'll also need to `apt install libncurses-dev`), and navigate through the menus to select AMD GPU.

Then, follow the instruction to compile the kernel (`make -j6 Image.gz modules dtbs`), and install it, moving all the parts into place with the `sudo cp` commands.

The last thing you need to do is install the AMD firmware:

```
sudo apt install firmware-amd-graphics
```

Now, reboot, and the Pi 5 _should_ be able to output video through the HDMI port, DisplayPort, or whatever other port on the external graphics card.

If not, debug the connection using a UART connection to the Pi, the Pi's onboard micro HDMI connection, or over SSH — use `dmesg` to see kernel messages (usually there's a pretty obvious error you can start searching).

## 4K Gaming on Pi 5 (for real)

Now comes the fun part. The Pi 5 _supposedly_ supports 4K display output. But if you use it at 60 Hz, even normal UI elements will feel a bit laggy.

With the RX 460, I get smooth 60 Hz output at 4K resolution. And if you install a game like SuperTuxKart (`sudo apt install supertuxkart`), you'll be able to play with all graphics settings maxed out, at 4K.

It gives me 15-20 fps at that resolution, but if I drop the graphics options down a slight bit, I can get 60+ fps all day. The Pi 5's internal VideoCore GPU isn't playable with maxed out graphics settings even at 1080p!

{{< figure src="./doom-3-4k-raspberry-pi-5-rx-460.jpg" alt="Doom 3 running at 4K on a Raspberry Pi 5" width="700" height="auto" class="insert-image" >}}

I also installed Doom 3 with [Pi-Apps](https://pi-apps.io), and got a solid 60 fps at 4K (it seems like the engine locks the game at 60 fps, I could get a lot more than that if I were able to unlock it—but it's been a long time since I hacked around with the old Id games' console...

Again, the Pi's internal GPU struggles to give a playable experience even on lower graphics settings at 1080p.

I couldn't get Steam installed using Box86/Box64 yet, but would like to try that with Doom Eternal and some other games I know play okay on other Arm64 platforms like my Ampere workstations (incidentally, with Nvidia GPUs like the 4070 Ti and 4090... which have better Arm64 drivers for more fully-compliant PCI Express buses).

Outside of games, I ran `glmark2-es2`, and on the Pi's internal V3D graphics, I got a score of about 1800. On the external AMD RX 460, I got 2383.

{{< figure src="./nvtop-rx-460-raspberry-pi-5.jpg" alt="nvtop running on Raspberry Pi 5 RX 460" width="700" height="auto" class="insert-image" >}}

In a bit of a surprise, `nvtop` actually works out of the box (`sudo apt install nvtop`) and provides a much better overview of GPU utilization than `radontop`. It even includes temperature and fan speed info, in addition to the basics like clock speeds and feature utilization.

## Other GPU uses

One downside to the Polaris generation AMD graphics cards is [ROCm support was dropped years ago](https://www.techpowerup.com/288864/amd-rocm-4-5-drops-polaris-architecture-support), so using the RX 460 for compute is a bit tricky.

With only 4 GB of VRAM and a few-generations-outdated GPU efficiency, it's not that compelling for things like LLMs or model training anyways. But one could pursue smaller models or other compute uses, as an academic exercise.

The much more enticing use is for _transcoding_.

Linux has decent support for GPU-accelerated video encode/decode, using the [VA-API](https://en.wikipedia.org/wiki/Video_Acceleration_API) (Video Acceleration API).

And the RX 460 _should_ support up to 10-bit H.264 encode/decode (at least if I'm reading specs correctly), up to 4K... but this is something I haven't gotten working on _my_ setup, just yet. Checking with `vainfo` gives an error:

```
pi@pi5-pcie:~ $ DISPLAY=:0 vainfo
libva info: VA-API version 1.17.0
libva info: Trying to open /usr/lib/aarch64-linux-gnu/dri/radeonsi_drv_video.so
libva info: va_openDriver() returns -1
vaInitialize failed with error code -1 (unknown libva error),exit
```

So far transcoding support hasn't been Coreforge's focus, as much as memory alignment fixes. And on _his_ machine, [`vainfo` is showing support for H.264, HEVC, VC1, and MPEG2 transcoding!](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/564#issuecomment-2400023786). At this point I'm trying to figure out what's different between our systems so I can get it working.

If you could grab a cheap old graphics card, drop it on a Pi 5, and transcode video with it, it makes for an even more compelling low-power, quiet [Arm NAS](https://github.com/geerlingguy/arm-nas) running a completely open source stack like Jellyfin + SMB + OpenZFS.

## What's left?

I've been running this configuration for a couple days, and it's perfectly stable. There are still memory alignment bugs that some applications run into, and the driver is not completely compatible yet.

{{< figure src="./chromium-browser-tab-empty-pi-5-external-gpu.jpg" alt="Chromium UI freeze with external AMD GPU" width="700" height="auto" class="insert-image" >}}

The Chromium browser interface seems to freeze sometimes when running through the external graphics card, and I'm not quite sure what's causing that. The settings menu pops up, and the title bar updates (e.g. if you type in "Jeff Geerling" in the location bar and hit enter), but nothing else in the window updates.

I installed Firefox (`sudo apt install firefox`), and it didn't have any issues—so my best guess is Chromium is trying to use GPU acceleration for it's UI by default, and there's a driver bug it's hitting in that state.

Outside of that, it would be nice to get the `amdgpu` driver in the kernel working with _all_ generations of AMD GPUs, so one _could_ use newer cards, or experiment with modern ROCm on a Pi 5.

The PCI Express Gen 3 x1 bus speed is a limiting factor, but there are plenty of use cases where that's enough bandwidth.

Besides, it's just fun to push hardware to its limits. I've certainly learned a lot about PCIe, arm64, the Linux kernel, and AMD's drivers already!
