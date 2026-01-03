---
nid: 3183
title: "Testing Raspberry Pi's new Network Install feature"
slug: "testing-raspberry-pis-new-network-install-feature"
date: 2022-02-16T15:02:18+00:00
drupal:
  nid: 3183
  path: /blog/2022/testing-raspberry-pis-new-network-install-feature
  body_format: markdown
  redirects: []
tags:
  - imager
  - install
  - linux
  - network
  - pi os
  - raspberry pi
  - usability
  - ux
---

> **Video**: This blog post is a companion piece to my video: [Raspberry Pi does what Microsoft can't!](https://www.youtube.com/watch?v=qlBIfpBwqKY)

With a new Network Install feature, a Raspberry Pi can now set itself up—without any flash drive or other computer—directly over the Internet.

{{< figure src="./pi-4-network-install.jpeg" alt="Raspberry Pi 4 Network Install" width="700" height="394" class="insert-image" >}}

Like Apple's [Internet Recovery](https://support.apple.com/en-us/HT204904), you don't have to have any OS installed on your computer to use it. And you don't need to run a separate server to boot your Pi and image its drive. (Note: There are also some PC vendors who have specific image-over-Internet services for certain devices like the Microsoft Surface, but they're not universally applicable to all PC builds.)

This feature is NOT netbooting. The Pi supports that too. This is similar, in a sense, but this goes deeper.

What this new feature means is you could walk into a store, buy a Raspberry Pi and any old microSD card, go home, plug it into your network, and the Pi could set itself up.

Sort of. I mean, you [might not be able to _find_ a new Raspberry Pi](https://rpilocator.com) right now. And since the feature's in beta, it's not actually running on existing Pis unless you update their firmware.

But soon. Once it's out of beta, that scenario will be possible.

And heck, even Macs don't go as far as the new Pi feature does! Their Internet Recovery feature is only possible because Apple burns that alongside the OS that's preinstalled on a Mac's soldered-in storage. On the Pi, you can use any storage you want. Heck, you can set up a Pi with just a thumb drive—no other computer required!

At this point, you can boot a Pi a number of ways:

  - From a microSD cards
  - From built-in eMMC (on certain Compute Module models)
  - From a USB drive, like a flash drive, hard drive, or SSD
  - Via netboot using PXE boot / TFTP
  - From NVMe SSDs (with the Compute Module)

And now, you can also boot a Pi directly over the Internet, using the Network Installer mode.

## Update to beta EEPROM

First I'll show you how to update your existing Pi to be able to do network install.

{{< figure src="./pi-4-400-cm4.jpeg" alt="Raspberry Pi 4, Pi 400, CM4" width="700" height="439" class="insert-image" >}}

You have to have a Pi 4, Pi 400, or Compute Module 4, though. Older Pis don't have the EEPROM that makes this possible.

> See my earlier post on [how the Pi 4 boots itself up using the bootloader in the EEPROM](/blog/2021/getting-raspberry-pi-boot-after-cutting-it-half).

While this feature's in beta, you actually _do_ need another computer to update your Pi's firmware, which is ironic, because the whole point of the feature is to _not_ require another computer... but I'd rather Raspberry Pi iron out more bugs _before_ they stamp it into new units at the factory.

On my Mac, I did the following:

  1. Open Raspberry Pi Imager
  2. Click 'Choose OS'
  3. Click 'Misc utility images' &gt; 'Beta Test Bootloader' &gt; 'SD Card boot'
  4. Pop a microSD card into a card reader, and choose it with 'Choose storage'
  5. Click 'write', and enter your password when prompted

Now pop out the microSD card, insert it into your Pi, then boot up the Pi, ideally with a monitor connected.

{{< figure src="./raspberry-pi-eeprom-update-green-screen.jpg" alt="Raspberry Pi EEPROM bootloader update green screen" width="700" height="394" class="insert-image" >}}

The activity LED should start flashing pretty rapidly for a few seconds. Once that's done, the green LED starts flashing in a steady pattern, and if you have a monitor plugged in, it should show a green screen, meaning flashing was successful.

Unplug the Pi, and take out the microSD card.

At this point, you're running the beta bootloader, and it should be able to do a Network Install.

## Netinstall to a microSD card

Make sure you have a keyboard and Ethernet cable plugged in, and pop in a microSD card that _doesn't_ already have Pi OS or another operating system on it.

If you want use the same microSD card you just used to update the bootloader, you can actually do that without even erasing it. Just pull it out of the Pi, do the next few steps, and then pop the card back in once Pi Imager's running.

But assuming you have a different card or erased your original card, power on the Raspberry Pi with it installed.

{{< figure src="./raspberry-pi-imager-boot-select-screen-network-install.jpg" alt="Raspberry Pi Network Install boot select screen" width="700" height="394" class="insert-image" >}}

This is the new screen that pops up when the Pi doesn't detect an operating system. Hold down the Shift key for a few seconds, then when it asks, press Space.

The Network Installer will connect to the Internet, then download the Raspberry Pi Imager to RAM.

The Imager download was pretty slow for me, and heck, [right now it doesn't even work with IPv6](https://forums.raspberrypi.com/viewtopic.php?p=1971960#p1971960), but hopefully those things get fixed before it gets out of beta.

Once that download's finished, Raspberry Pi Imager will boot from RAM, and you can flash the microSD card—straight from the Pi itself!

The entire UI is accessible via keyboard alone, which is nice, but the installer isn't yet accessible for blind users. According to Raspberry Pi, they [might integrate Orca](https://www.raspberrypi.com/news/network-install-beta-test-your-help-required/#comment-1580743), so assistive devices could work with the Imager's UI.

Select an OS, select the microSD card, and hit 'Write', then wait as the Pi simultaneously downloads and writes your image to the card. How much RAM you have on your Pi shouldn't be an issue, even if you choose a big OS image, because the image is actually decompressed and written straight through to the microSD card.

Once it's done writing, the Pi will automatically reboot, and since there's an operating system on the card now, the Pi should boot from it!

## Other niceties

I also tested flashing a USB SSD and flash drive, and that worked without a hitch (just make sure you remove any valid boot drives like the microSD card flashed earlier, if it's still in).

And what about custom Pi OS images, like a special RetroPie build, or another OS not available in the Imager's defaults?

I copied some OS images on a USB thumb drive, plugged that into the Pi while it was booted into Imager, and when I chose the 'Use custom' option in the Operating System menu, it showed all the image files on my flash drive.

> Note: I formatted my flash drive as FAT32. I'm not sure if it'll work with other formats.

## Security

For anyone who's really concerned about it, I'd recommend never installing something over the Internet regardless—always use local images you've independently verified.

But for most users, the security in place is adequate; the Imager that runs in the Pi's RAM is verified using a self-signed certificate that Raspberry Pi created, and it looks like the [cert they're currently using](https://fw-download-alias1.raspberrypi.com/net_install/boot.sig) is valid for about 24 years.

And the Imager itself is [signed with a separate key](https://forums.raspberrypi.com/viewtopic.php?p=1971537&amp;sid=38ab4096a0d2c3b4f30d32769dd76a49#p1971537) so it can be verified before the Pi boots it.

Once rebooted, the Imager actually [fetches the current date and time over the web](https://forums.raspberrypi.com/viewtopic.php?p=1971542#p1971542), not using NTP but using HTTP, since it needs to have a somewhat accurate time and date so the image downloads work correctly.

Is the end-to-end security absolutely bulletproof? No, but it's good enough for me.

Also, since I know some of you will ask: the source code that actually builds the Raspberry Pi Imager buildroot image that makes this all work is [up on GitHub](https://github.com/raspberrypi/rpi-imager/blob/qml/embedded/build.sh), in the Imager project's embedded directory.

## Limitations

There are a few limitations with the current Network Install process. Some people have asked about fully headless automated provisioning. That's actually been possible [on the Compute Module 4](https://github.com/raspberrypi/cmprovision) for almost a year.

But right now, at least, [it still requires extra steps](https://forums.raspberrypi.com/viewtopic.php?p=1972490#p1972490) on a Pi 4 or Pi 400.

Also, you can't use WiFi for Network Install yet. The Pi's EEPROM is already a bit space constrained—I've been told that's part of the reason why [they can't add SATA boot to the Compute Module 4](https://github.com/raspberrypi/firmware/issues/1653). So adding more code to support WiFi for Network Install might be impossible, at least with the current generation of Raspberry Pis.

And what about the Compute Module 4? Updating _it's_ bootloader is [a little more complicated](https://forums.raspberrypi.com/viewtopic.php?p=1971537&amp;sid=38ab4096a0d2c3b4f30d32769dd76a49#p1971537), because it's [EEPROM works a bit different](https://www.raspberrypi.com/documentation/computers/compute-module.html#cm4bootloader). On the CM4, you need to use the [rpiboot tool to flash the beta bootloader](/blog/2022/how-update-raspberry-pi-compute-module-4-bootloader-eeprom).

## Conclusion

It's great Raspberry Pi is adding this feature. I think back ten years ago, when Apple released iOS 5 for the iPhone.

Sure there were big new features like iCloud and iMessage, but the biggest update—the one that took the iPhone from a glorified iPod to the behemoth it is today? That feature was _independence from iTunes_. With iOS 5, you could activate and update iPhones without connecting them to another computer.

Once Network Install is out of beta, a major barrier to first-time Pi owners will disappear: they won't have to set it up from another computer. And heck, it works well enough that I'll be using it a lot, now, too.

> Note: Yes, I know NOOBS is a thing, but I see that going away as this new functionality comes to new Pis.

Power users like me will still use Imager on another computer, but I think for many people, this new way of setting up a Pi might be the only way they ever do it.

If you try it out and find a problem, there's a [forum topic where Raspberry Pi's asking for feedback](https://forums.raspberrypi.com/viewtopic.php?p=1972945).

Also, I mentioned at the beginning of this post this feature _isn't_ netboot. That's a different beast, and Wendell over at Level1Techs posted a [thorough blog post covering netbooting a Raspberry Pi](https://forum.level1techs.com/t/the-ultimate-home-server-herd-of-netboot-raspberry-pi-sure/181022), so check that out if you're interested. I plan on covering it in a future video, too, so be sure to [subscribe to my YouTube channel](https://www.youtube.com/c/JeffGeerling) or [this blog's RSS feed](/blog.xml)!
