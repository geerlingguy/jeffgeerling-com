---
nid: 3313
title: "Testing PCIe on the Raspberry Pi 5"
slug: "testing-pcie-on-raspberry-pi-5"
date: 2023-09-28T06:00:43+00:00
drupal:
  nid: 3313
  path: /blog/2023/testing-pcie-on-raspberry-pi-5
  body_format: markdown
  redirects:
    - /blog/2023/testing-all-my-pcie-devices-on-raspberry-pi-5
    - /blog/2023/testing-all-pcie-on-raspberry-pi-5
aliases:
  - /blog/2023/testing-all-my-pcie-devices-on-raspberry-pi-5
  - /blog/2023/testing-all-pcie-on-raspberry-pi-5
tags:
  - linux
  - open source
  - pcie
  - pi 5
  - raspberry pi
  - sbc
---

If you haven't heard, the [Raspberry Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/) was announced today (it'll be available in October).

{{< figure src="./raspberry-pi-5-model-b-credit-card.jpg" alt="Raspberry Pi 5 model B with credit card behind it" width="700" height="467" class="insert-image" >}}

I have a [full video](https://www.youtube.com/watch?v=nBtOEmUqASQ) going over the hardware—what's changed, what's new, and what's gone—and I've embedded it below. Scroll beyond to read more about specs, quirks, and some of the things I learned testing a dozen or so PCIe devices with it.

## The Video

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/nBtOEmUqASQ" frameborder='0' allowfullscreen></iframe></div>
</div>

## Specifications / Comparison to Pi 4

| | Raspberry Pi 4 | Raspberry Pi 5 |
| --- | --- | --- |
| CPU | 4x Arm A72 @ 1.8 GHz (28nm) | 4x Arm A76 @ 2.4 GHz (16nm) |
| GPU | VideoCore VI @ 500 MHz | VideoCore VII @ 800 MHz |
| RAM | 1/2/4/8 GB LPDDR4 @ 2133 MHz | 4/8 GB LPDDR4x @ 4167 MHz |
| USB | USB 2.0 (shared), USB 3.0 (shared) | 2x USB 2.0, 2x USB 3.0 |
| PCIe | (Internal use) | PCIe Gen 2.0 x1 |
| Southbridge | N/A | RP1 via 4 PCIe Gen 2.0 lanes |
| Ethernet | 1 Gbps | 1 Gbps (w/ PTP support) |
| Wifi/BT | 802.11ac/BLE 5.0 | 802.11ac/BLE 5.0 |
| GPIO | 40-pin header via BCM2711 | 40-pin header via RP1 Southbridge |
| Fan | 5v via GPIO pins, no PWM | 4-pin fan header, with PWM |
| UART | via GPIO, requires config | via UART header, direct to SoC |
| Price | $35 (1GB) / $45 (2GB) / $55 (4GB) / $75 (8GB) | $60 (4GB) /$80 (8GB) |

## Pi 5 Overview

{{< figure src="./Raspberry-Pi-5-Top.png" alt="Raspberry Pi 5 top - image courtesy of Raspberry Pi Trading" width="700" height="466" class="insert-image" >}}

The Raspberry Pi 5 model B preserves the credit-card-sized footprint of the previous generations, but crams a bit more functionality into the tiny space, including an RTC, a power button, a separate UART header, a 4-pin fan connector, a PCI Express FPC connector, two dual-purpose CSI/DSI FPC connectors, and four independent USB buses (one to each of the 2x USB 3.0 ports and 2x USB 2.0 ports).

Some things have moved or been modified:

  - The Ethernet jack flipped back over to the same orientation as the Pi 3 B+ and earlier
  - The two ACT/STATUS LEDs have become one, in a combined STAT LED that changes color
  - The VL805 USB 3.0 controller chip has been replaced by an RP1 'southbridge', which soaks up 4 PCIe lanes from the new BCM2712 SoC and distributes them to all the interfaces
  - The A/V jack is gone, in its place is an unpopulated analog video header
  - The CSI and DSI ports are gone, replaced by two dual-purpose CAM/DISP ports capable of more bandwidth and flexible use (you can have stereo cameras on the Pi 5 directly now)
  - The PMIC chip is upgraded and can handle 25W of USB-C power input at 5V/5A (Raspberry Pi sells a new PSU for this, though the old 3A PSU can be used still)

{{< figure src="./pi4-pi5-general-overview.png" alt="Pi 5 vs Pi 4 general overview" width="700" height="377" class="insert-image" >}}

{{< figure src="./pi4-pi5-memory-latency-corrected.jpg" alt="Pi 4 vs Pi 5 memory latency" width="700" height="399" class="insert-image" >}}

The Pi 5 is 2-3x faster than the Pi 4 in every meaningful way:

  - The SoC performs between 1.8-2.4x faster on every CPU and system benchmark I've run
  - LPDDR4X memory runs double the speed (at a lower voltage) than the LPDDR4 of the Pi 4, leading to 2-4x faster memory access, with a substantial improvement in latency
  - Overall USB bandwidth is double, owing to the four independent USB buses
  - HDMI output performance is doubled, and you can run 4K @ 60 Hz without stuttering while performing other activities (the Pi 4 would have issues even at 30 Hz sometimes).
  - The microSD card slot is UHS-I (SDR104), doubling the performance from the Pi 4 to 104 MB/sec maximum
  - The WiFi performance is also doubled—I got 200 Mbps via 5 GHz 802.11c versus the 104 Mbps I got on the Pi 4.

{{< figure src="./pi4-pi5-io-wifi.png" alt="Pi 5 vs Pi 4 WiFi and microSD" width="700" height="370" class="insert-image" >}}

Cryptography-related functions are _45x faster_, owing to the Arm crypto extensions finally making their way into the Pi 5's SoC:

{{< figure src="./pi4-pi5-cryptography.png" alt="Pi 5 vs Pi 4 Cryptography functions" width="700" height="197" class="insert-image" >}}

## Pi 5 and Raspberry Pi OS 12 "Bookworm"

The Pi 5 has been built to work best with Pi OS 12 "Bookworm" (based on the Debian release of the same name), and during the alpha testing phase, we did encounter some growing pains—a few of which may make it to production, as they are longstanding issues that also affect other Arm-based systems.

One is the decision to trial [16k page size](https://twitter.com/never_released/status/1334196423869558784), which gives slightly improved performance at the expense of long-tail compatibility with old armv7/32-bit binaries. I don't know if Pi OS 12 will ship with 16k pagesize enabled or not, but there are ways to shim compatibility with older software if necessary.

Another is deprecating libraries and utilities like `tvservice` and `wpa_supplicant` in favor of more modern alternatives like `kmsprint` and NetworkManager. I'll be publishing a post on `nmcli` use on Raspberry Pi OS 12 soon, so make sure you're subscribed to [this blog's RSS feed](https://www.jeffgeerling.com/blog.xml)!

## Exploring PCIe on the Pi 5

But now we get to it—my favorite new feature of the Pi 5: PCI Express exposed directly to the end user!

{{< figure src="./pi-5-pcie-fpc-connector-flat-cable.jpeg" alt="Raspberry Pi 5 PCIe external FPC Connector - Flat cable" width="700" height="394" class="insert-image" >}}

A close inspection of the RP1 specs indicate it uses 4 lanes of PCIe Gen 2.0 from the BCM2712 SoC... meaning the board _actually_ has five lanes of PCIe bandwidth available. But only one lane is exposed to the user via the FPC connector pictured above.

By default, the external PCIe header is not enabled, so to enable it, you can add one of the following options into `/boot/firmware/config.txt` and reboot:

```
# Enable the PCIe External connector.
dtparam=pciex1

# This line is an alias for above (you can use either/or to enable the port).
dtparam=nvme
```

And the connection is certified for Gen 2.0 speed (5 GT/sec), but you can force it to Gen 3.0 (10 GT/sec) if you add the following line after:

```
dtparam=pciex1_gen=3
```

I did that in much of my testing and never encountered any problems, so I'm guessing that outside of more exotic testing, you can run devices at PCIe Gen 3.0 speeds if you test and they run stable.

Currently there aren't any PCIe HATs (M.2, card slot, Mini PCIe, etc.), but I was able to borrow a debug adapter from Raspberry Pi for my testing. My hope is there will be new HATs adding on various high speed peripherals soon (just like we saw a massive growth in [Compute Module 4 boards](https://pipci.jeffgeerling.com/boards_cm) once the CM4 exposed PCIe to the masses).

One caveat if you plan on building your _own_ PCIe HAT: the FPC connector only provides up to 5W on its 5V line, so you won't be able to power too many PCIe devices directly off the connector. I used a 12V barrel plug to provide power to the debug board I used.

I'm going to run through the devices I've tested so far—noting I have not had near enough time to do real debugging yet, like I have on the Compute Module 4. Eventually I plan on moving all this data into the [Raspberry Pi PCIe Devices](https://pipci.jeffgeerling.com) website.

### NVMe SSDs

{{< figure src="./pi-5-pcie-nvme.jpg" alt="Pi 5 PCIe NVMe Kioxia XG8 SSD" width="700" height="408" class="insert-image" >}}

Booting from an NVMe SSD instead of the built-in microSD card slot is probably going to be the main use case for PCIe on the Pi 5, at least early on.

I tried a few different Gen 3 and Gen 4 SSDs, and settled on the above KIOXIA XG8, as it seems to run cool compared to some of my other SSDs.

I was able to get about 450 MB/sec under the default PCIe Gen 2.0 speed, and very nearly 900 MB/sec forcing the unsupported Gen 3.0—almost exactly a 2x speedup.

I ran most of my testing on the Pi 5 booting from this drive, and I'll publish a separate blog post on NVMe boot on the Pi 5. It's supported out of the box, though you need to modify the boot order in the EEPROM.

One issue I did run into—which I was still debugging with the Pi engineers at the time of this writing—is the WiFi `brcfmac` interface would not intialize properly while the NVMe SSD was powered and in use (whether booting from NVMe, microSD, or USB). With any other PCIe device I tested, built-in WiFi initialized properly. <strike>The current theory is it could be an issue with how the prototype PCIe adapter board I'm using is powered.</strike> (Edit: there was a bug in the BOOT_ORDER initialization that has since been fixed!)

I hope to see a first party NVMe HAT—and if not, whoever builds one first is going to get some of my cash immediately. It will be extremely handy to pop an M.2 slot on a Pi 5. Powering the SSD could be interesting, since many NVMe devices consume more than 5W.

### Coral TPU / AI Accelerators

{{< figure src="./pi-5-pcie-coral-tpu.jpg" alt="Pi 5 PCIe Google Coral TPU" width="700" height="394" class="insert-image" >}}

Coral TPUs are popular in tandem with Frigate for AI object detection. USB Coral devices have worked with all the Pi models for years, but PCIe versions [had problems](https://pipci.jeffgeerling.com/cards_m2/coral-accelerator-ae-key.html) on the Compute Module 4's slightly-broken PCIe bus.

On the Pi 5, I was able to get the `apex` kernel module installed following [the official Coral install guide](https://coral.ai/docs/m2/get-started#2a-on-linux), but noticed every once in a while I'd get a PCIe packet error message in the system logs:

```
[   72.418344] apex 0000:01:00.0: Apex performance not throttled due to temperature
[   77.534508] apex 0000:01:00.0: Apex performance not throttled due to temperature
[   77.534543] pcieport 0000:00:00.0: AER: Corrected error received: 0000:00:00.0
[   77.534554] pcieport 0000:00:00.0: PCIe Bus Error: severity=Corrected, type=Data Link Layer, (Transmitter ID)
[   77.534557] pcieport 0000:00:00.0:   device [14e4:2712] error status/mask=00001000/00002000
[   77.534560] pcieport 0000:00:00.0:    [12] Timeout               
[   82.654615] apex 0000:01:00.0: Apex performance not throttled due to temperature
```

_Aside_: I hate it when production code spams status messages to the system logs... I don't think I need to be reminded the TPU _isn't_ overheating every five seconds!

After finding [pycoral is incompatible with Python 3.11](https://github.com/google-coral/pycoral/issues/85) (the version in Bookworm), I decided to [test the Coral TPU in Docker](/blog/2023/testing-coral-tpu-accelerator-m2-or-pcie-docker).

After a bit more debugging—and re-seating everything, since signal integrity seemed to be more critical with the Coral—I wound up _almost_ getting it to work:

```
[  372.628183] pcieport 0000:00:00.0: AER: Corrected error received: 0000:00:00.0
[  372.628199] pcieport 0000:00:00.0: PCIe Bus Error: severity=Corrected, type=Data Link Layer, (Transmitter ID)
[  372.628204] pcieport 0000:00:00.0:   device [14e4:2712] error status/mask=00001000/00002000
[  372.628209] pcieport 0000:00:00.0:    [12] Timeout               
[  373.268131] apex 0000:01:00.0: RAM did not enable within timeout (12000 ms)
[  373.268141] apex 0000:01:00.0: Error in device open cb: -110
[  373.268160] apex 0000:01:00.0: Apex performance not throttled due to temperature
```

Apparently one of the lab Raspberry Pi 5's works with the Coral, but it seems my alpha board and a few other test boards have these link issues. With most PCIe devices, a sporadic dropped packet seems to be handled gracefully. On the Coral, it seems to want to retrain every time there's a problem, and it never works end-to-end on mine.

I tried dropping to PCIe Gen 1 speed (2.5 GT/s), with `dtparam=pciex1_gen=1` in `/boot/firmware/config.txt`, but I still hit the error. The leading theory is a better FPC connection and/or adapter board may solve this issue.

I should mention again: I'm using an early prototype PCIe adapter board—it's likely the signaling issues I've run into will be improved with production hardware!

### Network Cards

{{< figure src="./pi-5-pcie-asus-10g-nic.jpg" alt="Pi 5 PCIe Asus 10G NIC" width="700" height="406" class="insert-image" >}}

The signaling issues didn't seem to impact this Asus 10G NIC at all, however. To get it running, I [recompiled the Linux kernel](https://www.raspberrypi.com/documentation/computers/linux_kernel.html), adding in the proper Aquantia modules (see my [guide](https://pipci.jeffgeerling.com/cards_network/asus-xg-c100c-10g.html)).

Once in place, the card was immediately recognized, and at PCIe Gen 3, I was able to get 5.5-6 Gbps. I presume there may be a 10G NIC out there that will squeeze out closer to 10 Gbps through a Gen 3 x1 link, but I haven't found it.

Other NICs (like the trusty [Intel I340-T4](https://pipci.jeffgeerling.com/cards_network/intel-i340-t4-4-port-1g.html) I used on the CM4 for 4x Gigabit connections) seemed to work okay too, so I didn't spend much time on networking (yet!).

I think the Pi would pair well with a [dual-2.5G NIC like this one from Syba](https://amzn.to/3PUGhSs). I have one, but have not had a chance to test it. I hope someone creates a 'Router HAT' with two 2.5G interfaces up top. And convinces OPNsense/PFsense to release an arm64-compatible build!

You can add on more interfaces via USB 3.0 as well—though my quick test of a single 2.5G adapter resulted in only 1.5 Gbps of transfer for some reason.

### HBA/RAID Storage Cards

{{< figure src="./pi-5-pcie-hba-hdd.jpg" alt="Pi 5 PCIe HBA Broadcom" width="700" height="394" class="insert-image" >}}

I also set up a hardware RAID and HBA card with a single SATA drive, to see if the `mpt3sas` driver from Broadcom (formerly LSI) would work out of the box (the CM4 required a patch to work around [this bug](https://github.com/raspberrypi/linux/issues/4158)). I tested one of the [9405W-16i cards](https://pipci.jeffgeerling.com/cards_storage/broadcom-megaraid-9405w-16i.html) I used in the [Petabyte Pi project](https://www.youtube.com/watch?v=BBnomwpF_uY), and it seemed to be recognized in the kernel... but for some reason `storcli` didn't identify it.

I didn't have time yet for full debugging, though, and the same thing happened with the [9460-16i](https://pipci.jeffgeerling.com/cards_storage/broadcom-megaraid-9460-16i.html), so I will take up the gauntlet again soon. I'd love to try building another DIY NAS on the Pi 5 to see if I can resoundingly break the gigabit-write-over-the-network barrier (Samba held back speeds on the BCM2711!).

### Graphics Cards

{{< figure src="./pi-5-pcie-evga-nvidia-3080-ti-gpu.jpg" alt="Pi 5 PCIe Nvidia EVGA 3080 Ti Graphics Card" width="700" height="394" class="insert-image" >}}

Anyone who's followed my Pi journey knows the elusive problems I've had getting graphics cards working on the Pi CM4. After a grueling amount of work testing [various cards](https://pipci.jeffgeerling.com/#gpus-graphics-cards)—and mostly relying on other people's help—we got partial success with a few older cards, for some very basic rendering tasks.

My ADLINK Ampere Altra Max workstation can take a modern Nvidia card, and on Ubuntu at least, the official arm64 drivers load without a hitch and allow GPU-accelerated gaming and compute.

Can the Pi 5? Well, I'm hopeful. On the CM4, many driver issues would result in the Pi _completely_ locking up. Like, pull-power-and-let-it-sit-style lockups.

That is no longer the case, as the `nouveau`, `nvidia`, `amdgpu`, and `radeon` drivers all seem to identify the graphics cards I've plugged in. Nvidia's driver install succeeds without a hitch, and `lspci` shows the correct module loading.

But after all that, I'm still bumping into a darned `RmInitAdapter failed!` error message, which has [vexed](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/26) [me](https://forums.developer.nvidia.com/t/gtx-1080-drivers-fail-to-load-with-nvrm-gpu-000400-0-rminitadapter-failed-0x251211/156902/2) [before](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/480#issuecomment-1431775189). Oh how a fully-open-source driver for Linux would be helpful!

{{< figure src="./pi-5-pcie-amd-6700-xt-gpu.jpg" alt="Pi 5 PCIe AMD RX 6700 XT Graphics Card" width="700" height="394" class="insert-image" >}}

Oh wait! AMD has that! How do they fare?

Testing an RX 6700 XT with the open source AMDGPU driver included in Linux, I ran into a few errors like:

```
[drm:psp_hw_start [amdgpu]] *ERROR* PSP load kdb failed!
[drm:psp_v11_0_ring_destroy [amdgpu]] *ERROR* Fail to stop psp ring
[drm:psp_hw_init [amdgpu]] *ERROR* PSP firmware loading failed
[drm: amdgpu_device_fw_loading [amdgpu]] *ERROR* hw_init of IP block <psp> failed -22
amdgpu 0000:03:00.0: amdgpu: amdgpu_device_ip_init failed
amdgpu 0000:03:00.0: amdgpu: amdgpu: finishing device.
```

But I think we're very close. Some of the issues also seem to be around timing-related errors, which could also be down to signal integrity with my early prototype PCIe adapter. I am definitely in the market for a slightly better FFC (Flexible Flat Cable) that has some form of shielding.

From what I've heard, PCIe HATs and better cables may already be in the works, but I'm sure my Pi PCIe addiction is not priority number one right now—not when there are about 10 other subsystems and the brand new RP1 southbridge chip going into full production!

## Conclusion

This blog post only scratches the surface—I spent many more hours testing and debugging things on the Pi 5, and all that work was poured into my [video on the Raspberry Pi 5](https://www.youtube.com/watch?v=nBtOEmUqASQ), so go watch that.

If you have any questions I didn't cover, please let me know in the comments!
