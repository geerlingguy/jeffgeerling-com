---
nid: 3084
title: "The Raspberry Pi can boot off NVMe SSDs now"
slug: "raspberry-pi-can-boot-nvme-ssds-now"
date: 2021-03-23T19:02:47+00:00
drupal:
  nid: 3084
  path: /blog/2021/raspberry-pi-can-boot-nvme-ssds-now
  body_format: markdown
  redirects: []
tags:
  - boot
  - compute module
  - mirkopc
  - nvme
  - pi os
  - raspberry pi
  - ssd
---

When the Compute Module 4 was released (see [my CM4 review here](/blog/2020/raspberry-pi-compute-module-4-review)), I asked the Pi Foundation engineers when we might be able to boot off NVMe storage, since it was trivially easy to use with the exposed PCIe x1 lane on the CM4 IO Board.

The initial response in October 2020 was "we'll see". Luckily, after more people started asking about it, [beta support was added for direct NVMe boot](https://www.raspberrypi.org/documentation/hardware/raspberrypi/bootmodes/nvme.md) just a couple weeks ago.

{{< figure src="./mirkopc-cm4-with-wd-black-sn750-ssd-nvme.jpeg" alt="MirkoPC with SN750 WD_BLACK NVMe SSD and Raspberry Pi Compute Module 4" width="600" height="369" class="insert-image" >}}

And in a stroke of perfect timing, I also received a hand-made [MirkoPC board](https://pipci.jeffgeerling.com/boards_cm/mirkopc.html) from Mirek in Poland last week, which among other features includes a full-size M.2 M-key slot, meaning I could test out NVMe boot on it with a Compute Module 4 and a [WD_black SN750 500GB SSD](https://pipci.jeffgeerling.com/cards_m2/wd-black-sn750.html) I use for testing.

## Video version of this post

I also posted a video about booting from NVMe on my YouTube channel; it's embedded below:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/4Womn10v71s" frameborder='0' allowfullscreen></iframe></div>
</div>

## Setting up NVMe Boot

The setup process is a little involved right now, since you have to set the correct boot order, update the Pi's bootloader, update the Pi's firmware, but it's not too crazy.

Because I had some trouble with the MirkoPC's built-in microSD card slot, I chose to use an eMMC-powered Compute Module 4, so I flashed Pi OS to it, then [set the Pi to USB mass storage mode](https://www.jeffgeerling.com/blog/2020/how-flash-raspberry-pi-os-compute-module-4-emmc-usbboot).

> **September 2022 Update**: NVMe boot is no longer in beta: see the [new NVMe boot documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#nvme-ssd-boot) for more details. I am currently using boot order `BOOT_ORDER=0xf25416`. See [all available `BOOT_ORDER` options here](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#BOOT_ORDER).
>
> The new process for updating the boot order is to:
>
> 1. Clone `rpiboot`: `git clone --depth=1 https://github.com/raspberrypi/usbboot`
> 2. Build `rpiboot`: `cd usbboot && make`
> 3. Open the `recovery/boot.conf` file and update the `BOOT_ORDER` variable so it reads: `BOOT_ORDER=0xf25416`
> 4. Run `./update-pieeprom.sh` to update the `pieeprom.bin` file with the new settings
> 5. Connect your CM4 in USB boot mode ([see detailed guide](https://www.jeffgeerling.com/blog/2022/how-update-raspberry-pi-compute-module-4-bootloader-eeprom)) and run: `../rpiboot -d .`
>
> After a few seconds it should successfully update the EEPROM and the new boot order should be ready. The activity LED should start blinking rapidly once complete.

I followed the [beta instructions](https://www.raspberrypi.org/documentation/hardware/raspberrypi/bootmodes/nvme.md) to change the `BOOT_ORDER`, but I had to modify the `sed` command on my Mac, since the arguments are different for the non-GNU version of `sed` shipped with macOS:

```
sed -i '' 's/\(BOOT_ORDER=.*\)6\(.*\)/\1\26/' boot.conf
```

(Note the addition of the `''`.)

For the firmware update, I used the built-in SD Card Copier utility to copy all data from the eMMC storage over to the NVMe SSD, and made sure to check the "New Partition UUIDs" option when doing so.

After that, I rebooted the Pi, and used `lsblk` to verify the NVMe was mounted as `/` and `/boot`, and then got on to benchmarking.

## Cloning Raspberry Pi OS from microSD to NVMe

The easiest way to migrate from microSD to an NVMe drive (or, really, any other boot volume) on the Raspberry Pi is to use [`rpi-clone`](https://github.com/geerlingguy/rpi-clone). (The commands below use my fork of `rpi-clone` instead of [the original](https://github.com/billw2/rpi-clone), since that version is no longer maintained.)

All you have to do is install `rpi-clone`, then clone the disk:

```
# Install rpi-clone.
git clone https://github.com/geerlingguy/rpi-clone.git
cd rpi-clone
sudo cp rpi-clone rpi-clone-setup /usr/local/sbin

# Clone to the NVMe drive (usually nvme0n1, but check with `lsblk`).
sudo rpi-clone nvme0n1
```

Confirm that you would like to format the NVMe drive, then wait for the clone to complete. Assuming you have the `BOOT_ORDER` configured with NVMe taking priority, your Raspberry Pi should boot off the NVMe.

## Benchmarking NVMe vs microSD, eMMC, and USB adapters

The two main things I wanted to test were boot times and app launch/use times, to see what kind of impact the NVMe storage would have.

I already know from my [World's tiniest NVMe RAID](https://www.youtube.com/watch?v=AoNxDe1a-X8) video that NVMe storage is, on average, _12x faster_ on the Pi for normal file operations (copies, random read/write), but how much does it affect everyday performance?

Well, boot times are hardly affected by disk IO, it seems; after realizing I had to disable Bluetooth in `/boot/config.txt` and disable the `hciuart` service, since my CM4 didn't have a wireless module, I got pretty much the exact same boot time across NVMe, eMMC, and microSD bootups:

{{< figure src="./bench-avg-boot.png" alt="Boot time benchmarks for NVMe, eMMC, and microSD on Pi" width="746" height="333" class="insert-image" >}}

But the next test reveals more of the typical speedup you'd encounter on a Pi, day-to-day. I wrote a [Node.js benchmark script for Chromium](/blog/2020/testing-how-long-it-takes-chromium-open-load-web-page-and-quit-on-debian) to test how long it takes to launch Chromium, load a webpage, and quit last year, for some other testing.

I ran that same benchmark on each storage device (three times, restarting the Pi between each test, with < 2% standard deviation in the results), and got the following times:

{{< figure src="./bench-chromium.png" alt="Chromium usage benchmarks for NVMe, eMMC, and microSD on the Pi" width="738" height="327" class="insert-image" >}}

In this test, NVMe storage is _44% faster_ than microSD, and around 20% faster than eMMC. The bigger surprise was how much better eMMC fares than microSD; the 8-bit configuration on the CM4 (vs. 4-bit on the CM3+ and earlier) makes a big difference, especially for random IO.

But 44% is a pretty significant difference. You will definitely notice the speedup from NVMe boot on the Pi, and that's not even considering the fact that you can get 4 TB (or larger) NVMe SSDs, and they have much better write longevity compared to all but the most expensive microSD cards.

And I *know* people will ask about it, so I also compared the _exact same NVMe drive_ in a USB 3.0 to NVMe adapter, on the _exact same Pi_, using the _exact same VL805_ USB 3.0 chipset, to see what overhead there is when running NVMe storage through USB 3.0 on a Pi 4 model B:

{{< figure src="./bench-chromium-usb.png" alt="Chromium benchmark with NVMe native vs USB 3.0 to NVMe adapter with UASP" width="813" height="310" class="insert-image" >}}

So yes, there is a measurable difference—as I've found across many tests these past few months. Using native NVMe (vs. through USB adapters) is about 10% faster.

Anyway, I thought the MirkoPC would be a great little board to test NVMe boot on, though it works on any CM4 board (look at the [list of Compute Module 4 project boards I am maintaining here](https://pipci.jeffgeerling.com/boards_cm)), as long as you can adapt an M.2 NVMe SSD to the board's PCI Express connection (many boards have M.2 slots built-in!).

Check out the YouTube video for more details about my tests, and stay tuned (maybe subscribe to the blog's RSS!), as I'll continue exploring more storage options for the Pi, and I'll also be posting more about the MirkoPC soon!

> Note: While booting directly off an NVMe SSD works, I and others found that if you use a PCIe bridge/switch, it doesn't seem to work (e.g. if you want to plug both an NVMe SSD and NIC into the Pi's PCIe bus). I opened up this issue on the bootloader repo to track progress: [Can't boot CM4 via NVMe behind PCIe switch / bridge](https://github.com/raspberrypi/firmware/issues/1684).
