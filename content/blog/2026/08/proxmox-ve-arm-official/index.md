---
date: '2026-08-05T11:50:00-05:00'
tags: ['proxmox', 'homelab', 'arm', 'raspberry pi', 'ampere', 'nvidia', 'server', 'vm']
title: 'Proxmox officially supports Arm, with some caveats'
slug: 'proxmox-ve-arm-official'
---
Proxmox today announced their [Proxmox Virtual Environment is now available for 64-bit ARM](https://forum.proxmox.com/threads/proxmox-virtual-environment-now-available-for-64-bit-arm-arm64.185527/).

I tested it on my [Ampere Altra Dev Platform](/blog/2023/testing-96-core-ampere-altra-developer-platform/)—the same machine on which I've [booted Windows on Arm](/blog/2023/ampere-altra-max-windows-gpus-and-gaming/) the first time, messed with multiple GPUs, and most recently [tested Houdini's native arm64 support](https://www.youtube.com/watch?v=QdU7WszFTAA).

{{< figure
  src="./proxmox-ve-on-arm-vm.jpg"
  alt="Proxmox VE running on Ampere Altra Max workstation"
  width="700"
  height="auto"
  class="insert-image"
>}}

Install was easy, as the Ampere Altra uses UEFI / ACPI for its hardware, meaning Proxmox didn't have to tailor its ISO to specific platforms, like you have to do with Raspberry Pis and most SBCs using a Device Tree setup.

I just went into the BIOS, selected my USB stick with the [official Proxmox VE 9.2 for ARM64 ISO](https://www.proxmox.com/en/downloads) flashed to it, and ran the graphical installer.

I had a little trouble installing Ubuntu 24.04.1 from an arm64 minimal server live CD inside the VM, so I've opened up this issue on the Proxmox forums: [Testing Proxmox VE on Ampere Altra Max (Armv8)](https://forum.proxmox.com/threads/testing-proxmox-ve-on-ampere-altra-max-armv8.185541/).

## Platform Support

Officially, they only support NVIDIA Grace Hopper and Vera server platforms (I'm guessing NVIDIA was interested in bringing up Proxmox support, and helped in some way?).

For other platforms:

> - Best-effort support on other UEFI-based ARMv9-A or newer hardware (ARMv8-A generally works as well, likewise best-effort)
> - The host must boot through UEFI and describe its hardware through ACPI
> - Device-tree-only single-board computers, such as the Raspberry Pi, are not supported

I don't think that precludes this flavor of Proxmox from running on the Raspberry Pi. The forked [Raspberry Pi 5 UEFI](https://github.com/NumberOneGit/rpi5-uefi) project enables UEFI support (with some limiations) on the Pi 5, and similar projects exist for other popular SBCs, like the [Rockchip RK3588](https://github.com/edk2-porting/edk2-rk3588).

> **Update**: Mastodon user [@luna@catgirl.center got it running on Pi 4](https://mastodon.social/@luna@catgirl.center/117043938463789909) already, using [this UEFI firmware from pftf](https://github.com/pftf/RPi4).

The other main Armv9 platforms I've used are Apple's M-series computers (some older M-series systems may work via Asahi Linux, maybe?), and systems built around the Cix P1 SoC in the [Radxa Orion O6](/blog/2025/radxa-orion-o6-brings-arm-midrange-pc/), [Minisforum MS-R1](/blog/2025/minisforum-stuffs-entire-arm-homelab-ms-r1/), and [Framework AI PC Mainboard](/blog/2026/arm-mainboard-for-framework-laptop/).

Here's a video of the entire install and first look on my Ampere Altra Developer Platform:

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/Lg263L1W97w' frameborder='0' allowfullscreen></iframe></div>
</div>

Due to time limitations, I've only been able to test on my Ampere Altra Max system. I'd love to hear any of your experiences on other arm64 systems in the comments below!
