---
nid: 3435
title: "CaribouLite SDR HAT for SDR on a Raspberry Pi"
slug: "cariboulite-sdr-hat-sdr-on-raspberry-pi"
date: 2025-01-24T15:00:33+00:00
drupal:
  nid: 3435
  path: /blog/2025/cariboulite-sdr-hat-sdr-on-raspberry-pi
  body_format: markdown
  redirects:
    - /blog/2025/testing-cariboulite-pi-hat-on-pi-os-bookworm
    - /blog/2025/testing-cariboulite-pi-hat-sdr-on-pi-os-bookworm
aliases:
  - /blog/2025/testing-cariboulite-pi-hat-on-pi-os-bookworm
  - /blog/2025/testing-cariboulite-pi-hat-sdr-on-pi-os-bookworm
tags:
  - cariboulite
  - ham
  - hat
  - radio
  - raspberry pi
  - rtl-sdr
  - soapysdr
  - software defined radio
---

{{< figure src="./cariboulite-hat-pi-4.jpg" alt="CaribouLite HAT mounted on Pi 4 in rackmount" width="700" height="394" class="insert-image" >}}

A couple years ago, after I heard about the [CaribouLite on CrowdSupply](https://www.crowdsupply.com/cariboulabs/cariboulite-rpi-hat), I pre-ordered one.

I've dabbled in SDR with an [RTL-SDR v3](https://amzn.to/3Ckxh5d) for a few years, even [using one with nrsc5 to listen to baseball games OTA](/blog/2019/hospital-stay-and-mlb-blackouts-led-me-rtl-sdr-radio) because of silly MLB blackout restrictions.

But low-cost SDRs like the RTL-SDR v3 are receive-only, and have a limited frequency range, and lower quality RF filtering, so it can be frustrating if you're trying to work with lower-power RF... or trying to transmit at all!

So the CaribouLite's hackable FPGA, the open source firmware, and it's much better frequency range (30 MHz up to 6 GHz) combined with TX capabilities to make it enticing.

Well, I received my CaribouLite back in March... of _2023_. And it was sitting in my 'RF' box since then. I decided to pull it out and plug it into a Pi to see how it works or if it's worth the extra $100 I spent on it over another RTL-SDR v3!

## Video

I also published a video showing the CaribouLite in action—though the rest of this blog post after the video embed covers setup and usage in more detail:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/Hz2WqhWmjZE" frameborder='0' allowfullscreen></iframe></div>
</div>

## Choosing a Pi

This being a Raspberry Pi HAT—and one that relies on a [Broadcom SoC feature that's not well documented (SMI)](https://github.com/cariboulabs/cariboulite?tab=readme-ov-file#smi-interface), you _have_ to use it with a Pi. The Pi has to have a 40-pin GPIO header, and it also can't be a Pi 5—since that uses the RP1 chip for GPIO access, and doesn't give you direct SMI integration into the Broadcom SoC :(

But a Pi 4 is still plenty powerful enough—honestly even a Pi 3 B+ or Pi Zero 2 would work in many scenarios—so I went with a 1 GB Pi 4, which currently costs $35 (and people say Pis are so expensive!).

I flashed the latest 64-bit Pi OS 12 ('Bookworm') onto a microSD card, and plugged in the CaribouLite to the GPIO header.

## Installing CaribouLite Drivers on Pi OS Bookworm

Following Caribou Labs' guide for setting up the driver necessary to communicate with CaribouLite for software like Soapy SDR and GQRX (among others), I found there were two additional patches required to get the driver to work on Debian 12/Bookworm.

So here are all the commands I ran to install it:

```
# Clone CaribouLite repository to the Pi.
git clone https://github.com/cariboulabs/cariboulite.git
cd cariboulite

# Apply patch for Bookworm: https://github.com/cariboulabs/cariboulite/pull/210
curl -L https://patch-diff.githubusercontent.com/raw/cariboulabs/cariboulite/pull/210.patch | git apply -v

# Apply patch to fix compile error: https://github.com/cariboulabs/cariboulite/pull/176
# (THIS WILL FAIL—SEE MY NOTE FOR INSTRUCTIONS HOW TO APPLY IT MANUALLY:
#   - https://github.com/cariboulabs/cariboulite/pull/176#issuecomment-2596019689)
curl -L https://github.com/cariboulabs/cariboulite/pull/176.patch | git apply -v

# Run the installer.
./install.sh

# During installation, it will prompt "Did not find SoapySDRUtil"
# Enter 'y'
```

The compilation will take a few minutes (at least, it did on my Pi 4), then it will install drivers and link a number of libraries on the system for CaribouLite to work on the Pi.

On my installation, it flagged two warnings at the end:

```
3. I2C-VC Configuration...  Warning
To communicate with CaribouLite EEPROM, the i2c_vc device needs to be enabled
Please add the following to the /boot/firmware/config.txt file: 'dtparam=i2c_vc=on'

4. SPI1-3CS Configuration...  Warning
To communicate with CaribouLite Modem, FPGA, etc, SPI1 (AUX) with 3CS needs to be to be enabled
Please add the following to the /boot/firmware/config.txt file: 'dtoverlay=spi1-3cs'
```

So add those options by editing the config.txt file, with `sudo nano /boot/firmware/config.txt`. Add these lines above the `dtparam=audio=on` line:

```
# CaribouLite
dtparam=i2c_vc=on
dtoverlay=spi1-3cs
```

Save that file, and reboot. Once rebooted, make sure `smi_stream_dev` is loaded:

```
pi@pi4-sdr:~ $ lsmod | grep smi
smi_stream_dev         16384  2
bcm2835_smi            20480  1 smi_stream_dev
```

## Updating issues with `xtrx-dkms`

After running CaribouLite's installer, I noticed my `apt` operations would bail out after trying to update `xtrx-dkms`:

```
Setting up xtrx-dkms (0.0.1+git20190320.5ae3a3e-3.2) ...
Removing old xtrx-0.0.1+git20190320.5ae3a3e-3.2 DKMS files...
Deleting module xtrx-0.0.1+git20190320.5ae3a3e-3.2 completely from the DKMS tree.
Loading new xtrx-0.0.1+git20190320.5ae3a3e-3.2 DKMS files...
Building for 6.6.51+rpt-rpi-v8
Building initial module for 6.6.51+rpt-rpi-v8
Error! Bad return status for module build on kernel: 6.6.51+rpt-rpi-v8 (aarch64)
Consult /var/lib/dkms/xtrx/0.0.1+git20190320.5ae3a3e-3.2/build/make.log for more information.
```

Looking in that log, I found the same error indicated by the CaribouLite compile error:

```
/var/lib/dkms/xtrx/0.0.1+git20190320.5ae3a3e-3.2/build/xtrx.c:1523:35: note: in expansion of macro ‘THIS_MODULE’
 1523 |         xtrx_class = class_create(THIS_MODULE, CLASS_NAME);
      |                                   ^~~~~~~~~~~
```

It looks like that error is fixed as of early 2024. See [commit `d218d3e` in `myriadrf/xtrx_linux_pcie_drv`: xtrx.c: fix build error with kernel 6.4](https://github.com/myriadrf/xtrx_linux_pcie_drv/commit/d218d3e8be3f723000bdfff6b6235a85f7b10e42).

But getting that patched into the `0.0.1+git20190320.5ae3a3e-3.2` version in Debian Bookworm may be a little annoying. I haven't looked into this much, I'm just ignoring it for now, because other apt operations and installs still work, it just always errors out on this package.

## Remote SDR via SoapySDR

{{< figure src="./cariboulite-soapysdr-gqrx-pi.jpg" alt="GQRX showing remote signal from SoapySDR CaribouLite" width="700" height="394" class="insert-image" >}}

If you want to access the CaribouLite across the network from another computer (I typically launch [GQRX](https://www.gqrx.dk) on my Mac at my desk), launch SoapySDRServer:

```
sudo systemctl start SoapySDRServer.service
```

You can check on the status of the service with `status` instead of `start`, or observe the logs in real time with:

```
sudo journalctl --follow -u SoapySDRServer.service 
```

I was able to use both frequency/antenna options:

  - HiF (High Frequency): 30 MHz-6 GHz
  - S1G (Sub-1 GHz): 389.5-510 MHz and 779-1020 MHz

During operation, while I was streaming the SDR over to GQRX on my Mac, `btop` showed between 50-150 Mbps of bandwidth, and CPU activity was around 15-20% (pretty low system load). While not streaming, load is practically nothing.

I could even see 2.4 GHz WiFi traffic on my local network, which was operating on channel 6 (2437 MHz center frequency):

{{< figure src="./cariboulite-24-ghz-wifi.jpg" alt="CaribouLite 2.4 GHz WiFi signal in GQRX" width="700" height="394" class="insert-image" >}}

If you want SoapySDRServer to be running at boot, run:

```
sudo systemctl enable SoapySDRServer.service
```

One thing I did notice: I initially had both WiFi and Ethernet enabled on the Pi 4 while I was testing. Even though the WiFi connection could put through at least 100 Mbps with no problem, it messed up the SDR stream, to the point I would hear very choppy audio when decoding anything in GQRX.

To fix that, I disabled WiFi (you could use `nmtui`, but I used `nmcli` instead):

```
sudo nmcli radio wifi off
```

## Local SDR with GQRX

I also wanted to test SDR software directly on the Pi, so I installed GQRX:

```
sudo apt install gqrx-sdr
```

After installation, open up GQRX and control it on the Pi the same as you would any computer.

I had two issues with the `apt` version of GQRX:

  1. It seems after getting some data, the UI would freeze, though the CPU indicated it was still decoding the signal. So maybe an issue with CaribouLite's driver + Debian packaged GQRX?
  2. If I went anywhere near higher FFT/decoding quality settings, the Pi's CPU would either max out one core (single thread), or use a high amount of CPU resources to try rendering things...

So it may be better to run the SDR UI on another machine or via a Web UI, so the Pi doesn't have to render everything! I'm guessing the Pi 5 would cope much better, as it has 2-3x faster performance both per core and multicore.

## SDR Web UI

I may also install [OpenWebRX](https://www.openwebrx.de/download/debian.php?version=12) so I can have the Pi host a little Web UI SDR interface, instead of having to run SDR software either directly on the Pi, or remotely on another computer.

For some additional CaribouLite tutorials, like using it for ADS-B reception with a Pi Zero, check out [David Michaeli's YouTube channel](https://www.youtube.com/@davidmichaeli3387/videos).
