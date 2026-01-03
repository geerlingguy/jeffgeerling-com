---
nid: 3051
title: "Cross-compiling the Raspberry Pi OS Linux kernel on macOS"
slug: "cross-compiling-raspberry-pi-os-linux-kernel-on-macos"
date: 2020-11-04T16:47:29+00:00
drupal:
  nid: 3051
  path: /blog/2020/cross-compiling-raspberry-pi-os-linux-kernel-on-macos
  body_format: markdown
  redirects: []
tags:
  - arm64
  - compile
  - debian
  - linux
  - mac
  - macos
  - raspberry pi
  - vagrant
  - virtualbox
---

After doing a video testing different [external GPUs on a Raspberry Pi](https://www.youtube.com/watch?v=ikpgZu6kLKE) last week, I realized two things:

  1. Compiling the Linux kernel on a Raspberry Pi is slow. It took 54 minutes, and I ended up doing it 7 times during the course of testing for that video.
  2. If you ever want to figure out a better way to do something, write a blog post or create a video showing the less optimal way of doing it.

To the second point, about every fifth comment was telling me to cross-compile Linux on a faster machine instead of doing it on the Pi itself. For example:

{{< figure src="./cross-compile-comment.png" alt="cross compile raspberry pi kernel youtube comment" width="762" height="131" class="insert-image" >}}

And on the Pi Forums, it seems like nobody worth their salt compiles the kernel on the Pi either, so I figured—since I'm probably going to have to do it again another thousand times in my life—I might as well put together a guide for how to do it on a Mac.

And my first attempt was to use Docker for Mac, but that attempt faltered once I realized there's no way to mount a microSD card ('device') into Docker for Mac, unless you hack things through VirtualBox with Docker inside or use Docker Machine. And that's a lotta layers of abstraction.

And my second attempt was to see if osxfuse could be made to help ([I've used osxfuse to mount Raspberry Pi microSD cards before...](/blog/2017/mount-raspberry-pi-sd-card-on-mac-read-only-osxfuse-and-ext4fuse)). That didn't pan out, and I didn't want to rely on something that used paid ext4 software that may or may not work with virtualization, so ultimately I went back to my old faithful, Vagrant + VirtualBox.

I wanted to compile the Raspberry Pi OS kernel with support for 9000 MTU on the built-in Gigabit network interface for some ethernet benchmarking I was doing (it only supports 1500 MTU out of the box, and the driver doesn't allow changing MTU on the fly), and I had to put that kernel on four Pi 4 model Bs, so this was the perfect time to start cross-compiling on my fast Core i9 Mac.

## Setting up a Debian VM

I wanted my cross-compile environment to be close to the Pi OS, and work with the [Raspberry Pi Kernel Building](https://www.raspberrypi.org/documentation/linux/kernel/building.md) directions out of the box, so I created a [Vagrantfile](https://github.com/geerlingguy/raspberry-pi-pcie-devices/blob/master/extras/cross-compile/legacy-vagrant/Vagrantfile) that used the `debian/buster64` base box.

See the entire Vagrantfile using the link in the previous paragraph, but one of the more important bits is the enabling of the XHCI USB 3.0 interface in the VM, so you can attach USB devices—and thus access and mount the fat32 and ext4 partitions on a microSD card directly within the VM:

```
    vb.customize ["modifyvm", :id, "--usb", "on"]
    vb.customize ["modifyvm", :id, "--usbxhci", "on"]
```

I initially tried using the USB 2.0 EHCI option instead of USB 3.0 and xHCI, but when I did that, and tried attaching my card reader (detailed later in this post), I got the error message `VERR_PDM_NO_USB_PORTS`:

{{< figure src="./VirtualBox-VERR_PDM_NO_USB_PORTS.png" alt="VirtualBox error message VERR_PDM_NO_USB_PORTS" width="674" height="384" class="insert-image" >}}

So if you get that error, try out the USB 3.0 XHCI option instead.

I also put in an inline `shell` provisioner in the Vagrantfile that installs all the build dependencies:

```
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y git bc bison flex libssl-dev make libc6-dev libncurses5-dev crossbuild-essential-armhf crossbuild-essential-arm64
  SHELL
```

Again, check out the [linked Vagrantfile in my GitHub repo](https://github.com/geerlingguy/raspberry-pi-pcie-devices/blob/master/extras/cross-compile/Vagrantfile) to find the whole thing.

With that Vagrantfile, assuming you have [Vagrant](https://www.vagrantup.com) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads) installed on your computer, along with the VirtualBox Extension Pack (required for USB support), you can run `vagrant up`, and you'll end up with a VM ready to cross-compile ARM Linux!

## Getting USB working

The next step for me was to get my external USB card reader (in my case, built into my [CalDigit TS3 Plus](https://www.amazon.com/CalDigit-TS3-Plus-Thunderbolt-Dock/dp/B07CZPV8DF/ref=as_li_ss_tl?dchild=1&keywords=caldigit&qid=1604507207&sr=8-5&linkCode=ll1&tag=mmjjg-20&linkId=efbf6a3b55b293650f2367d18a743043&language=en_US) ThunderBolt hub) attached to the VM so when I put in a microSD card, it would show up inside Debian.

To do this, I shut down the VM with `vagrant halt`, then I opened VirtualBox, went into the Settings for the new 'cross-compile' VM, then to 'Ports', then 'USB', then in the 'USB Device Filters' section, I added my 'CalDigit Card Reader [1038]'.

{{< figure src="./VirtualBox%20USB%203%20CalDigit%20Card%20Reader.png" alt="VirtualBox USB 3 CalDigit Card Reader added to USB ports on VM" width="651" height="503" class="insert-image" >}}

> You can specify USB device directly in the Vagrantfile (see the comments on [this older blog post](/blogs/jeff-geerling/mounting-raspberry-pis-ext4-sd)), but since I move my Mac between different locations, with different card readers, I didn't want to hardcode anything in the Vagrantfile.

Now that the card reader is attached, I started up the VM again, with `vagrant up`.

## Logging in and compiling the Linux kernel

> For the rest of this blog post, I'm assuming you'll be building Linux for the Raspberry Pi 4 (or Compute Module 4, or Pi 400), and for 64-bit ARM, not 32-bit. If you need to build for 32-bit, or for a different Pi model, please make sure you use the right environment variables and build args as outlined in the [Kernel building](https://www.raspberrypi.org/documentation/linux/kernel/building.md) cross-compiling documentation.

Log into the VM using `vagrant ssh`, then start the process of compiling Linux and copying everything to your microSD card or USB drive:

  1. Clone the linux repo (or clone a fork or a different branch):

     ```
     git clone --depth=1 https://github.com/raspberrypi/linux
     ```

  1. Run the following commands to make the .config file:

         cd linux
         KERNEL=kernel8
         make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- bcm2711_defconfig

  1. (Optionally) Either edit the .config file by hand or use menuconfig:

     ```
     make menuconfig
     ```

  1. Compile the Kernel:

     ```
     make -j4 ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- Image modules dtbs
     ```

> For 32-bit Pi OS, use `KERNEL=kernel7l`, `ARCH=arm`, `CROSS_COMPILE=arm-linux-gnueabihf-`, and `zImage` instead of `Image`.

## Mounting the Pi microSD or USB drive

Mount the FAT and ext4 partitions of the USB card to the system. First, insert your microSD card into the reader you attached to the VM earlier, then run the following commands:

```
mkdir -p mnt/fat32
mkdir -p mnt/ext4
sudo mount /dev/sdb1 mnt/fat32
sudo mount /dev/sdb2 mnt/ext4
```

## Installing modules and copying the built Kernel

Install the kernel modules onto the drive:

```
sudo env PATH=$PATH make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- INSTALL_MOD_PATH=mnt/ext4 modules_install
```

> For 32-bit Pi OS, use `sudo env PATH=$PATH make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- INSTALL_MOD_PATH=mnt/ext4 modules_install`

Copy the kernel and DTBs onto the drive:

```
sudo cp mnt/fat32/$KERNEL.img mnt/fat32/$KERNEL-backup.img
sudo cp arch/arm64/boot/Image mnt/fat32/$KERNEL.img
sudo cp arch/arm64/boot/dts/broadcom/*.dtb mnt/fat32/
sudo cp arch/arm64/boot/dts/overlays/*.dtb* mnt/fat32/overlays/
sudo cp arch/arm64/boot/dts/overlays/README mnt/fat32/overlays/
```

## Unmounting the drive

Unmount the disk before you remove it from the card reader or unplug it.

```
sudo umount mnt/fat32
sudo umount mnt/ext4
```

Now you can pull the card out of the reader, or disconnect your USB drive, and put it in the Pi!

## Conclusion

{{< figure src="./cross-compile-17m-vagrant-virtualbox.png" alt="cross compile takes 17 minutes on macbook pro in VM" width="427" height="239" class="insert-image" >}}

In total, compiling the kernel on my MacBook Pro only takes about 18-20 minutes (whereas it took over an hour on the Pi 4 model B). I can probably optimize the VM layout and CPU utilization better to bring that number down a bit more, and probably will at some point.

Since I'm making a lot of tweaks right now to multiple Pis at a time (and currently testing a new GPU, a 10 Gbps network adapter, and a 4x 1 Gbps network adapter on the Compute Module 4), this is a much more efficient way to build custom Pi kernels.

Please check out the [Raspberry Pi PCI Express Card Database](https://pipci.jeffgeerling.com) project for the latest configuration and documentation for everything mentioned in this blog post, in the [cross-compile](https://github.com/geerlingguy/raspberry-pi-pcie-devices/tree/master/extras/cross-compile) directory.
