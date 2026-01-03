---
nid: 3003
title: "Raspberry Pi Cluster Episode 2 - Setting up the Cluster"
slug: "raspberry-pi-cluster-episode-2-setting-cluster"
date: 2020-05-08T20:27:39+00:00
drupal:
  nid: 3003
  path: /blog/2020/raspberry-pi-cluster-episode-2-setting-cluster
  body_format: markdown
  redirects: []
tags:
  - ansible
  - bramble
  - cluster
  - computer
  - kubernetes
  - pi dramble
  - raspberry pi
  - turing pi
  - video
  - youtube
---

> This post is based on one of the videos in my series on Raspberry Pi Clustering, and I'm posting the video + transcript to my blog so you can follow along even if you don't enjoy sitting through a video :)

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/xNndbfxMCLo" frameborder='0' allowfullscreen></iframe></div>

In the first episode, I talked about how and why I build Raspberry Pi clusters.

I mentioned my [Raspberry Pi Dramble](https://www.pidramble.com) cluster, and how it's evolved over the past five years.

In this episode, I'm gonna show you how to use the [Turing Pi](https://turingpi.com) to build an even better Raspberry Pi-based cluster. With the Turing Pi, you don't have to buy a network switch, a bunch of network cables, a bunch of micro USB cables, a multi-port USB power supply, and a bunch of microSD cards to build your cluster.

And then you don't have to spend an hour wiring everything together and building a case to hold everything, like I did with my Dramble!

The Turing Pi is, basically, a "cluster on a board". This one board has seven slots, for seven [Raspberry Pi Compute Modules](https://www.raspberrypi.org/products/compute-module-3-plus/).

A Raspberry Pi _Compute_ Module is basically a fast Raspberry Pi model B, but without any built in IO connections. It's on a little chip the same size as standard computer RAM. A stick of RAM, a Raspberry Pi Zero, and a Compute Module are similar in size, but very different in what they can do!

The Turing Pi includes dedicated I/O connections for the first slot, so you can manage the entire cluster through the Pi in slot 1, or you can manage the cluster externally using another computer. At a minimum, you just need to plug in power and a keyboard and mouse, or power and a network cable, and you're off to the races!

Before I talk about setting up the Turing Pi, I thought I'd show you how I built my current Raspberry Pi cluster, with four Raspberry Pi 4 model B computers.

## Building a Pi Cluster

{{< figure src="./pidramble-cluster-ep2.jpeg" alt="Raspberry Pi Dramble Cluster in Episode 2" width="650" height="451" class="insert-image" >}}

I have a [full parts list for my current Dramble cluster](https://www.pidramble.com/wiki/hardware/pis) on the pidramble.com wiki. You need to buy:

  - [4 Raspberry Pi 4 model B computers](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/)
  - An [8 amp 4-port USB charger](https://www.amazon.com/AUKEY-Charger-4-Ports-Foldable-Compatible/dp/B077P1HC6H/ref=as_li_ss_tl?keywords=4+port+usb+charger&qid=1562614808&s=gateway&sr=8-22&linkCode=ll1&tag=mmjjg-20&linkId=1aafbf36b8b05e627373bad8152fff85&language=en_US)
  - A [5 pack of USB-A to C charge cables](https://www.amazon.com/Pantom-Charging-Braided-Compatible-Samsung/dp/B07MFZM8WZ/ref=as_li_ss_tl?keywords=usb-a+to+usb-c+cables+short&qid=1574870886&sr=8-20&linkCode=ll1&tag=mmjjg-20&linkId=215074e73aa768be03baaca84e5d92d4&language=en_US)
  - Four [Samsung EVO+ 32GB microSD cards](https://www.amazon.com/Samsung-Class-Micro-Adapter-MB-MC32DA/dp/B00WR4IJBE/ref=as_li_ss_tl?s=pc&ie=UTF8&qid=1467833025&sr=1-3&keywords=samsung+evo+microsd&linkCode=ll1&tag=mmjjg-20&linkId=93773bda6727ae51b4d9f379a8c2a8d2)
  - An [8-port Gigabit ethernet switch](https://www.amazon.com/TRENDnet-Unmanaged-Gigabit-GREENnet-TEG-S80g/dp/B001QUA6RA/ref=as_li_ss_tl?ie=UTF8&redirect=true&ref_=as_li_tl&linkCode=ll1&tag=mmjjg-20&linkId=ada73855f40d46033ff4a71f414d3074)
  - And a [set of stackable cases](https://www.ebay.com/itm/271648357906) to hold everything together

All of this will set you back around $300.

Once you have everything, it's time to start assembling the parts!

First, if you're using the [Power over Ethernet HAT](https://www.raspberrypi.org/products/poe-hat/) like I am, install the HAT onto each Pi board. Since one of the headers on my PoE boards failed last time I re-assembled it, I already have them installed and won't be reinstalling them in this video.

Then you'll want to put all the Pis into your stackable cases (or into some other creative chassis you build).

Then you can wire up all the network connections, one cable to each Pi. Plug the other end of each cable into your network switch.

In my case, because I'm using Power over Ethernet, my Pis get their power straight from the PoE network switch, but if you're not using a PoE switch, you should plug in the USB power connections, with one USB cable for each Pi. But don't plug the power adapter into the wall yet, because the Pis don't have any operating system to boot!

### Loading an OS onto the microSD Cards

Before we load an OS onto the Raspberry Pis, it's important to think about what you want to do with your cluster. If you want a general purpose cluster running the fully-supported [Raspbian OS](https://www.raspberrypi.org/documentation/raspbian/) from the Raspberry Pi Foundation, you can download [Raspbian Lite](https://www.raspberrypi.org/downloads/raspbian/), which doesn't include a GUI or interface, just a command line or remote access interface that lets you manage the Pis via SSH.

If you want to run certain software that requires 64-bit compatibility, you might need to consider an OS that supports 64-bit on ARM processors, like [Ubuntu's 64-bit ARM distribution](https://wiki.ubuntu.com/ARM/RaspberryPi).

If you want to have an OS meant for container workloads and that is easy to configure 'headless' (like we'll do with the Turing Pi in a bit), you might want to consider [HypriotOS](https://blog.hypriot.com/downloads/).

For my Dramble, I want a generic cluster running a fully supported distribution built just for the Raspberry Pi, so I'm sticking with Raspbian.

So for each Pi, plug a microSD card into a card reader attached to another computer (if you have a separate working Raspberry Pi, you could use it to flash cards!). Then follow the [Raspberry Pi Foundation's instructions for flashing the Raspbian disk image](https://www.raspberrypi.org/documentation/installation/installing-images/) to each microSD card.

Their instructions recommend using the Raspberry Pi Imager app, and there are other GUI alternatives like [Etcher](https://www.balena.io/etcher/), but in my case, I use Terminal on my Mac. Depending on your computer, these instructions might be a little different, but here's what I do:

  1. Insert the microSD card.
  2. Run `diskutil list` in the Terminal to verify which disk device the card is using.
  3. Run `diskutil unmountDisk /dev/disk3` to unmount the card. You can run this command even if the card isn't mounted on your Desktop. You just need to make sure the disk is unmounted or the next command will fail.
  4. Run `pv [disk image name] | sudo dd bs=1m of=/dev/rdisk3` and enter your admin password to start the flashing process. This command uses the `dd` utility to directly write the contents of a disk image to the microSD card, using a block size of one megabyte. I use the `pv` or 'progress viewer' utility so I can monitor the progress of the copy, but you could drop that and just use `dd` instead.
  5. Wait for the flashing process to complete. It could take a few minutes. When it's done you'll see a `boot` volume mounted on your desktop.
  6. Run `touch /Volumes/boot/ssh` to create a file on the `boot` volume that tells the Raspberry Pi to enable SSH access when it first boots up.
  7. Unmount the card one more time using `diskutil unmountDisk /dev/disk3`.
  8. Remove the microSD card.
  9. Realize it's gonna be a while because you have to do all of that three more times!

### Booting up the cluster the first time

After all four cards are flashed, insert them into each of the Raspberry Pis.

Now plug in your cluster's power adapter, and after a few minutes, all the Pis should be booted and ready ... but for what?

Well, the next step is finding them all on your network, connecting to them, and managing them. For now, I'm going to skip that part because it's hard [insert sarcasm here]—actually, because I want to show you how to do the same setup, but using the Turing Pi!

## Building a Turing Pi Cluster

{{< figure src="./turing-pi-hero-shot.jpeg" alt="Turing Pi Cluster in Episode 2" width="650" height="433" class="insert-image" >}}

The Turing Pi builds the power distribution and networking _directly_ into the main board, so you don't even have to worry about purchasing all the extra cables, USB multi-port power supply, or network switch.

Instead, you'll need:

  - The Turing Pi
  - A 12V Power supply compatible with the Turing Pi
  - 7 Raspberry Pi Compute Modules (I recommend the 3+, or when it someday becomes available, a newer version)

And that's it!

You plug all the Compute Modules into the Turing Pi, and you're good to go! Except, you may be wondering, what about the operating system? Oh, yeah... about that.

## Getting the right Compute Modules

{{< figure src="./compute-modules-emmc-no-emmc.jpg" alt="Raspberry Pi Compute Module 3+ with eMMC and without eMMC" width="650" height="373" class="insert-image" >}}

There are two types of Raspberry Pi Compute Modules:

  - Ones with built-in eMMC memory (allowing you to boot the Compute Module without an external microSD card)
  - Ones _without_ built-in eMMC memory (meaning you'd need to buy an additional microSD card for each node)

The Turing Pi works with any Compute Module, and has a microSD card slot for each Pi, so you can choose whichever type of Compute Module fits your needs.

I recommend buying the ones _with_ eMMC, though, because it's easier to set up and manage in a cluster.

And you don't _have_ to fill up all the slots on the Turing Pi—you can run it with any number of Pi Compute Modules. You can even _hot plug_ modules, meaning you could add or remove Compute Modules _while the cluster is running_! So you could build your cluster today with three Compute Modules, and as your needs expand or you need a faster Pi or more eMMC on a Pi, you can add more Compute Modules or replace existing ones. Pretty neat!

{{< figure src="./blade-server-ibm-bladecenter.jpg" alt="IBM BladeCenter from Flickr - IMG_0909 by Robert" width="650" height="488" class="insert-image" >}}

In fact, this is something that's commonly seen only in higher-end servers, and is known as ['blade' computing](https://en.wikipedia.org/wiki/Blade_server). But as with many things Raspberry Pi, the Turing Pi makes this cool blade technology easy for anyone to use.

So back to the topic of operating systems—you'll still need to flash the eMMC on a Compute Module so it can boot up properly. But how do you do that? You can't plug a Compute Module into your computer's USB port!

## Flashing the Compute Module eMMC

{{< figure src="./usb-slave-port-turing-pi.jpeg" alt="Turing Pi USB Slave Port" width="650" height="433" class="insert-image" >}}

The Turing Pi has a built-in 'USB slave' port, at the top of the board. This micro USB port can be plugged into another computer to allow the eMMC module on a Compute Module installed in slot 1 to be flashed, just like you would flash a microSD card in a card reader.

To put slot 1 into 'flash' mode, you need to move the top jumper into the position nearest the Compute Module. Note that the Turing Pi I'm using is a prototype, so things may have changed a little bit in the production version.

Then you plug the Turing Pi's USB slave port into your computer, and power up the Turing Pi board.

At this point, it's likely you won't actually see anything happen. That's because the Compute Module's eMMC needs to be set up in 'usbboot' mode so it can appear as a USB mass storage device, just like a microSD card. And lucky you, the Raspberry Pi Foundation has a [utility](https://github.com/raspberrypi/usbboot) to do just that!

I have a separate blog post ([Flashing a Raspberry Pi Compute Module on macOS with usbboot](/blog/2020/flashing-raspberry-pi-compute-module-on-macos-usbboot)) that details this process but here's what I did:

So first, I made sure the Turing Pi was in 'flash' mode, the Compute Module was firmly seated in slot 1, the micro USB 'slave' port was plugged into my computer, and the Turing Pi was powered on.

Second, I opened my Mac's 'System Report' and went to the USB section to make sure the "BCM2710 Boot" device appeared in the list. Note that different versions of the Compute Module appear as different device numbers, but all with the prefix 'BCM'.

Third, I downloaded `usbboot` from the Raspberry Pi Foundation's [usbboot GitHub repository](https://github.com/raspberrypi/usbboot).

I opened up the directory it was in in Terminal, and ran `make`. For this to work, I had to also make sure the `libusb` library was installed on my Mac, which I installed with [Homebrew](https://brew.sh), using `brew install libusb`.

Once the `make` process finished, there was a new `rpiboot` executable, which is what I needed to run to prep the Compute Module's eMMC for flashing.

So fourth, I ran `sudo ./rpiboot`, and entered my admin password.

This kicks off an automated script which searches for any attached Compute Modules, then writes a couple files to the eMMC, and then exits.

Once it exits, a Mac pops up an alert saying 'The disk you inserted was not readable by this computer'. You can click 'Ignore' for now. (This only happens the first time you set up a fresh Compute Module.)

Fifth, I followed the same basic directions as before, with microSD cards, to flash an OS to the Compute Module's eMMC storage. But for the Turing Pi, I decided to use Hypriot OS, which is a little easier to preconfigure for headless servers like the Compute Module:

I ran `diskutil list` to see what device the eMMC was mounted as.

I unmounted the disk with `diskutil unmountDisk`.

I wrote the image to the card, again using `pv` and `dd` so I could monitor the progress. The card write took a bit longer with the eMMC than with microSD cards.

Once it was done, I edited the `/Volumes/HypriotOS/user-data` module using `nano`. I set the hostname to something meaningful in my cluster, like `master` for the first card which would act as the Kubernetes `master` node, or `worker-05` for the fifth worker card. You can use whatever naming convention you want, just be consistent.

I also pasted in my public SSH key in a new option for the default `pirate` user. I added the property `ssh_authorized_keys`, then added a list item with my personal SSH pubkey.

> If you don't already have a public SSH key—you can check if there's already a file in the path `~/.ssh/id_rsa.pub`, then you can create one by running the command `ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`, and press enter three times. Then an SSH key will be generated in the default location `~/.ssh/id_rsa.pub`.

After I finished editing the `user-data` file, I saved the file by pressing Control-O, and closed it with Control-X.

Finally, I ran `diskutil unmountDisk` again, to 'eject' the Compute Module.

At this point, you can disconnect the USB cable from the Turing Pi, disconnect power (assuming you don't have any other Pis running at the time!), and remove the Compute Module from slot 1.

One Pi down, six to go!

### Alternative flashing method

{{< figure src="./compute-module-poe-board.jpg" alt="Raspberry Pi Compute Module PoE Board by Waveshare" width="650" height="366" class="insert-image" >}}

Now, earlier I mentioned you could hot-swap Compute Modules on a running Turing Pi. But it wouldn't be convenient to have to flash Compute Modules in the Turing Pi all the time, especially if you have an important node running in slot 1, and don't want to shut it down to flash another Compute Module.

Luckily, there are 'Compute Module IO Boards' available that can be used to interact with a Compute Module and flash it's eMMC. If you do a lot of work with Compute Modules, it's a good idea to have one of these boards available; it gives you so many options, and makes it easy to boot Compute Modules on their own and test things on them, before installing them more permanently in the Turing Pi.

The IO board that I have is called the [Waveshare Compute Module PoE Board](https://www.amazon.com/gp/product/B07PDKZ56X/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=6f2dc60428be7fe1631a080018a57980&language=en_US), and I got mine from Amazon.

## Adding a case

Now that you have all the Compute Module's ready to boot, wouldn't it be nice to have a sturdy case for the Turing Pi? You're in luck, because the Turing Pi uses an industry-standard mini ITX form factor, meaning it fits perfectly into any mini ITX computer case!

{{< figure src="./mini-itx-case-turing-pi.jpeg" alt="Turing Pi Mounted in a mini ITX case" width="650" height="496" class="insert-image" >}}

I found [this case on Amazon](https://www.amazon.com/gp/product/B07T2HKWZN/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=8f38303769904c62d40c8ebdf74fdecd&language=en_US) for about $30, but there are many options if you don't want to build your own case.

## Booting it up for the first time

Now that you have all the Compute Modules flashed with an OS, and the Turing Pi is mounted and ready to go, you just need to plug in power and a network connection, and BOOM, you have an edge cluster that will change the world! [insert more dry sarcasm here]

## On to Kubernetes!

So, we have a cluster of Raspberry Pis—or, actually, a _bramble_ of Raspberry Pis. Now, what will we do with it? And how do you even connect to it?

To find out, [subscribe to my YouTube channel](https://www.youtube.com/c/JeffGeerling)—I'm going to show you how to connect to the individual nodes, introduce [Kubernetes](https://kubernetes.io), and get Kubernetes installed on the cluster in the next video!

Before I wrap up, I wanted to call out two aspiring young engineers, Louis and Robert from Houston, Texas. In our current crazy world, their Dad reached out and asked some questions about Pi clusters, since they were building one and trying to figure out what to do with it. In discussing things further, I realized what an opportunity for growth and learning they have from a Dad who is willing to teach and experiment with them!

I also have a son and two daughters, and I find their imaginations go way beyond my own! I want to encourage them, and try to keep my own brain sharp. Projects like this help, even if they're not as practical and pragmatic as building a cluster with bigger, faster computers. So if nothing else, consider building a cluster to be a learning opportunity, and to help inspire a new generation of developers, makers, and hardware hackers!

If you liked this content and want to see more, consider supporting me on [GitHub](https://github.com/sponsors/geerlingguy) or [Patreon](https://www.patreon.com/geerlingguy).

And if there's anything I missed or questions you have about the Turing Pi and clustering, please feel free to ask in the comments below. Until next time, I'm Jeff Geerling!
