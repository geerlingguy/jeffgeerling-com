---
nid: 3017
title: "I'm booting my Raspberry Pi 4 from a USB SSD"
slug: "im-booting-my-raspberry-pi-4-usb-ssd"
date: 2020-06-09T22:35:24+00:00
drupal:
  nid: 3017
  path: /blog/2020/im-booting-my-raspberry-pi-4-usb-ssd
  body_format: markdown
  redirects:
    - /blog/2020/im-booting-my-raspberry-pi-4-usb-ssd-it-better
aliases:
  - /blog/2020/im-booting-my-raspberry-pi-4-usb-ssd-it-better
tags:
  - external
  - firmware
  - hard drive
  - performance
  - raspberry pi
  - ssd
  - usb
---

> **September 2020 Update**: USB boot is out of beta! Check out [this video](https://www.youtube.com/watch?v=8tTFgrOCsig) for simplified instructions. All you need to do now is run `sudo apt-get dist-upgrade -y`, then reboot, then your firmware should be up to date. Now, flash any USB drive with the latest Raspberry Pi OS, plug it into your Pi (unplugging any microSD card), and you're off to the races!

Recently, the Raspberry Pi Foundation announced a [USB boot beta for the Raspberry Pi 4](https://www.raspberrypi.org/forums/viewtopic.php?t=274595). For a very long time, the top complaint I've had with the Raspberry Pi is limited I/O speed (especially for the main boot volume). And on older Pis, with the maximum external disk speed limited especially by the USB 2.0 bus—which was _shared_ with the network adapter, limiting its bandwidth further—even USB booting didn't make things amazing.

But the Pi 4 not only separated the network adapter from the USB bus, it also has USB 3.0, which can be 10x faster than USB 2.0 (theoretically). So when the USB boot beta was announced, I wanted to put it through its paces. And after testing it a bit, I decided to use the Pi 4 as my full-time workstation for a day, to see whether it can cope and where it falls short. I'll be posting a video and blog post with more detail on _that_ experience very soon.

**Update**: I now have a video that goes along with this blog post:

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/B1aRGkH3bgw" frameborder='0' allowfullscreen></iframe></div>

## Getting the Pi 4 to USB boot

First, I flashed a [32GB SanDisk Extreme Pro microSD card](https://www.amazon.com/SanDisk-Extreme-microSDHC-Memory-Adapter/dp/B06XYHN68L/ref=as_li_ss_tl?dchild=1&keywords=32gb+sandisk+extreme+pro+micro+sd+card&qid=1591654877&sr=8-1&linkCode=ll1&tag=mmjjg-20&linkId=dffad95e75bc37e5164c9e66e7f11e37&language=en_US) with the latest 64-bit beta release of the Raspberry Pi OS. In the future, you'll be able to download it from the regular [Pi OS download page](https://www.raspberrypi.org/downloads/raspberry-pi-os/), but for now it's available from [this forum thread](https://www.raspberrypi.org/forums/viewtopic.php?t=275370).

To flash the card, I still rely on good old `dd` on my Mac, but you can use the [Raspberry Pi Imager](https://www.raspberrypi.org/downloads/) instead.

> **NOTE**: You could break your Pi's firmware and render it inoperable if you do something wrong here. I cannot be held responsible for anything that happens with your Pi if you try using this beta feature!

Then I followed the [USB Boot beta setup instructions](https://www.raspberrypi.org/documentation/hardware/raspberrypi/bcm2711_bootloader_config.md) and did the following:

  1. Booted the Raspberry Pi with the microSD card I just flashed.
  2. Opened Terminal in Raspberry Pi OS (note: you can do these steps from another computer via SSH if you want to set up the Pi headless).
  2. Ran the following commands:

         sudo apt update
         sudo apt full-upgrade

  3. Edited the `rpi-eeprom-update` file and changed the `"critical"` value for the `FIRMWARE_RELEASE_STATUS` option to `"stable"`, using `sudo nano /etc/default/rpi-eeprom-update`.
  4. I ran the command to update the EEPROM:

     ```
     sudo rpi-eeprom-update -d -f /lib/firmware/raspberrypi/bootloader/stable/pieeprom-2020-07-16.bin
     ```

  5. Reboot the Pi and check the bootloader version by opening Terminal and running:

     ```
     vcgencmd bootloader_version
     ```

This should output something like:

```
pi@raspberrypi:~ $ vcgencmd bootloader_version
Jul 16 2020 16:15:46
version 45291ce619884192a6622bef8948fb5151c2b456 (release)
timestamp 1594912546
```

Hooray, you're halfway there!

Next, you need to flash the Pi OS to the external USB SSD or HDD. First things first, it's a good idea to plug your drive into the Pi while it's booted and make sure the Pi recognizes it (it should appear on your desktop, or you can also look for it with `lsusb`). Not all external drives and USB to SATA adapters work out of the box.

> In case you're wondering, I'm using a cheap [Kingston A400 240GB SSD](https://www.amazon.com/gp/product/B01N5IB20Q/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=cb49f6f6102970661cbab180de1d1353&language=en_US) inside an [Inateck USB 3.0 SATA enclosure](https://www.amazon.com/gp/product/B00FCLG65U/ref=as_li_ss_tl?ie=UTF8&th=1&linkCode=ll1&tag=mmjjg-20&linkId=c18fb5b368709af53c1bcc5dbc75ddce&language=en_US) (make sure to get the one _with_ UASP support, it's [a lot faster](https://github.com/geerlingguy/turing-pi-cluster/issues/11#issuecomment-647726561)). And yes, those are affiliate links.

So plug the USB drive into your main computer (where you flashed the microSD card earlier), and flash the Raspberry Pi OS to it the same way you did to the microSD card.

Before you eject the `boot` volume, you need to replace some files on it with the latest versions from GitHub:

  1. Go to the [raspberrypi/firmware](https://github.com/raspberrypi/firmware) GitHub repository and download the zip or clone the project to your computer (get the default `master` branch). (Or use [this one-line command](https://gist.github.com/atomicstack/9c43e452c4b7cefb37c1e78f65b0b1fa) to just grab the necessary files without the entire repository.)
  2. Inside the `boot` folder, copy over _all_ the files that end in `.elf` or `.dat` to the `boot` volume of your USB drive (replacing the same-named files that already exist there).
  3. Eject the `boot` volume, and unplug the USB drive.

Now, it's time to see if everything worked!

Shut down the Pi if it's currently running from the microSD card. Then unplug the microSD card, and plug in the USB drive.

Make sure you plug the drive into a USB 3.0 port (the blue-colored ones), and not one of the USB 2.0 ports (the black-colored ones), or else you'll be severely limited in throughput.

Power up the Pi, and after a minute or so (it has to expand the USB drive to fill the volume and then reboot), it should boot up!

If you're like me, though, you may run into this screen after the soft reboot:

{{< figure src="./pi-sdcard-failed-to-open-device-stuck-soft-reboot-usb.png" alt="Raspberry Pi 4 failed to soft reboot with external USB SSD" width="640" height="480" class="insert-image" >}}

That's okay; it seems related to the bug [Bootloader can't boot via USB-HDD after system reboot](https://github.com/raspberrypi/rpi-eeprom/issues/151), and the solution (for now) is to unplug the Pi to power it down completely, then plug it back in.

Now, assuming your USB drive or SATA adapter is compatible, the Pi should boot right up, and you'll find it much faster than before, when it was booting off a microSD card!

## Benchmarks

To get a sense of the raw performance difference between disk access while booted from the microSD card (one of the best you can buy, according to my [2019 Raspberry Pi microSD card comparison](/blog/2019/raspberry-pi-microsd-card-performance-comparison-2019)) versus booting from the Kingston USB SSD.

The first benchmark gets a synthesis of large file write activity, plus small (4K) file random access read/write activity. Both are important, but in many ways, differences in the latter are amplified when using a general purpose computer like the Pi, because computers don't just read and write large files all day (lots of sequential access) like video cameras or drones do (that's the use case for which most microSD cards are optimized).

If you want to run this benchmark on your own; it's documented in the [Pi Dramble Wiki's disk access benchmark page](http://www.pidramble.com/wiki/benchmarks/microsd-cards#benchmarks). Note that for the USB SSD, I modified the `hdparm` test to use the path `/dev/sda1` instead of `/dev/mmcblk0`.

{{< figure src="./disk-benchmark-hdparm-dd-4k.png" alt="Pi 4 Disk Benchmarks comparing microSD to USB SSD" width="600" height="253" class="insert-image" >}}

> Before you ask: yes, I ran these benchmarks four times (discarding the first result). I ran them on a clean brand new just-flashed system. I flashed both the microSD card and USB drive with the exact same Raspberry Pi OS 64-bit beta image file. I had the Pi running [in a case with a fan](/blog/2019/raspberry-pi-4-needs-fan-heres-why-and-how-you-can-add-one) and the Pi did not throttle at any time. 

The results really speak for themselves. For sequential operations, using a USB SSD is 3-4x faster than using a microSD card. And for random access, random reads are a bit faster, but _writes_ are about _6x faster_! This makes a difference in many activities, like launching apps, running a web browser with many tabs. And the sequential performance means you should be able to stream and/or record 4K or HD video easily while the Pi has enough bandwidth for other things too (assuming you're not re-encoding via the CPU—[this kills the CPU](https://i.imgur.com/gMmnR5p.jpg)).

To get an idea of how the disk access affects the performance of a real-world application I'm familiar with (and am able to benchmark thoroughly with highly accurate results), I also ran a set of _Drupal_ benchmarks, using the [Pi Dramble Drupal benchmarks](http://www.pidramble.com/wiki/benchmarks/drupal) I've been running on Pis for years. I ran them against an installation of [Drupal Pi](https://github.com/geerlingguy/drupal-pi), which runs Drupal and MariaDB in Docker containers, accessed through Nginx.

Here are the results:

{{< figure src="./drupal-benchmarks-install-first-load.png" alt="Drupal PHP Installation Benchmarks on Pi 4 with microSD vs USB SSD" width="600" height="203" class="insert-image" >}}

Same as before, I ran all tests 4x, and since it was such a difference, I went ahead and rebooted and ran them again; all results were less than 0.5% apart on the same configuration, so it's pretty apparent the SSD makes a huge different in many operations—Drupal's installation and first page load result in hundreds of files being accessed and/or written to disk, so it makes sense it's a lot faster on the SSD.

I also tested another scenario: loading and reloading pages in Drupal:

{{< figure src="./drupal-benchmarks-page-load.png" alt="Drupal Page Load benchmarks - microSD vs SSD" width="600" height="180" class="insert-image" >}}

These benchmarks show that for some operations, the disk IO performance is not that important. In Drupal's case, the data required to process and return the response for each page load is cached (both in PHP's case, in the opcache, and in the database's cache, in its query caches), so actual _reads_ and _writes_ are minimized.

## Summary

So where do we go from here? For the first time, I think I'm convincing myself that a Raspberry Pi 4 could be a competent general purpose computer _for some people_. In the past it's mostly been a fun aside for general computing, with a number of severe limitations. Since the original model B, each of the limitations has been removed, and outside of a few nice-to-haves (e.g. built-in fast NVMe storage, maybe full USB-C support, and more speed from the CPU), it's actually not that bad. And it's silent, if you use it caseless or with a decent heat-sink case like the Flirc (which I reviewed alongside other options in [The best way to keep your cool running a Raspberry Pi 4](/blog/2019/best-way-keep-your-cool-running-raspberry-pi-4)).

And I'm not just speaking platitudes: today, I used the Raspberry Pi for all my daily work, to see what rough edges lay in the path towards considering it as a daily general purpose workstation.

In comparison to my Dell XPS 13 and MacBook Pro 16, the option of silence, the very low power consumption, and the comparatively low cost of entry make the Pi 4 appealing for more use cases than ever before.

> Before you dive into the comments and tear apart the last few paragraphs above, please consider that I don't need 'death star'-level power available at all times. I know a 64-core Threadripper with 1 TB of memory and a RAID array of 1 TB NVMe SSDs is going to beat the pants off a Raspberry Pi 4 at full tilt. It's even more power efficient (watts per unit of computing)!
> 
> But I like to compare it to a truck: if you want to haul 80,000 lbs of materials, you're going to need a beefy semi tractor-trailer rig (a Threadripper). But would you like to park that in your driveway for day-to-day light hauling activities when you could get a small pickup (a Pi 4) for 1/10th the cost? And is it more _fun_ (as a general rule...) to drive the pickup, or the semi?
> 
> Though stretching the analogy a bit further, the Pi is probably more like a [Chevy Aveo](https://en.wikipedia.org/wiki/Chevrolet_Aveo) compared to a Macbook Air or Dell XPS being the pickup truck.
