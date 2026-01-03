---
nid: 3039
title: "Enabling TRIM on an external SSD on a Raspberry Pi"
slug: "enabling-trim-on-external-ssd-on-raspberry-pi"
date: 2020-09-09T16:42:31+00:00
drupal:
  nid: 3039
  path: /blog/2020/enabling-trim-on-external-ssd-on-raspberry-pi
  body_format: markdown
  redirects: []
tags:
  - debian
  - performance
  - raspberry pi
  - raspbian
  - ssd
  - trim
  - uasp
  - usb
---

I've been doing a lot of benchmarking and testing with the Raspberry Pi 4 and SSDs connected via USB. I explored [UASP Support](/blog/2020/uasp-makes-raspberry-pi-4-disk-io-50-faster), which [USB SSDs are the fastest](/blog/2020/fastest-usb-storage-options-raspberry-pi), and I'm now [booting my Pis from USB SSDs](/blog/2020/im-booting-my-raspberry-pi-4-usb-ssd).

Anyways, one thing that I have wondered about—and some people have asked me about—is TRIM support.

I'm working on a new video for [my YouTube channel](https://www.youtube.com/c/JeffGeerling) that will go into some more detail on which of the drives I tested support TRIM, but while I was researching for that video, I also found that TRIM support in Linux is not as simple as it seems at first glance—it's definitely not plug-and-play, in my experience.

While internal microSD cards seem to support TRIM out of the box, none of the external USB drives I tested supported it out of the box. They all needed a little help!

Much of the data in this post I attribute to [this excellent comment by tom.ty89 on the Pi Forums](https://www.raspberrypi.org/forums/viewtopic.php?p=1708655#p1708655).

## What is TRIM? Why should I care about it?

This blog post is not going to get into the weeds on TRIM; I recommend [this article on Crucial.com](https://www.crucial.com/articles/about-ssd/what-is-trim) if you want to learn about it.

## Does my SSD support TRIM?

In Linux, you can check if TRIM is currently supported by running one of the following commands (this blog post assumes you're booting off the SSD, so it's device `/dev/sda`—if you are not booting from the SSD you're checking, substitute accordingly!):

```
$ sudo fstrim -v /
```

If this reports back `fstrim: /: the discard operation is not supported`, then TRIM is not enabled.

You can also check with:

```
$ lsblk -D
```

If the `DISC-MAX` value is `0B`, then TRIM is not enabled.

Now, being _enabled_ and being _supported in firmware_ are two different things. Some of my drives actually support TRIM even if it's not enabled out of the box.

For example, testing with my [Corsair Flash Voyager GTX](https://www.amazon.com/dp/B079NVJPKV/ref=as_li_ss_tl?_encoding=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=d1351d0d353580ce5e05cb9ef174bdcc&language=en_US) flash drive, I was able to determine the _firmware_ supports TRIM, and I was then able to manually enable TRIM following tom.ty89's instructions.

### Checking if the Firmware supports TRIM

To check if the device firmware supports TRIM, switch to the root user (otherwise you'll need to use `sudo` before most of the rest of the commands in this post), and install a couple utilities we'll need for the rest of this process:

```
$ sudo su
# apt-get install -y sg3-utils lsscsi
```

Run the following command and check the `Maximum unmap LBA count`:

```
# sg_vpd -p bl /dev/sda
Block limits VPD page (SBC):
...
  Maximum unmap LBA count: 4194240
  Maximum unmap block descriptor count: 1
...
```

Take note of it, then run the following command and check the `Unmap command supported (LBPU)`:

```
# sg_vpd -p lbpv /dev/sda
Logical block provisioning VPD page (SBC):
  Unmap command supported (LBPU): 1
...
```

If the `Maximum unmap LBA count` is greater than `0`, and `Unmap command supported (LBPU)` is `1`, then the device firmware _likely_ supports TRIM.

> **Warning**: A few devices seemed to indicate they supported TRIM in firmware, like my [Arcanite USB 3.1 Flash Drive](https://www.amazon.com/dp/B07RWPF43G/ref=as_li_ss_tl?_encoding=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=8cef944962be8f68cbdd98bb6c78ded7&language=en_US)... but when I tried enabling it I got a few errors. Then I tried running `fstrim -v /` on a whim, and ended up corrupting the drive's firmware, to the point it won't mount and can't be formatted anymore. So make sure you have a backup of any important data before you try on a drive that might not actually support TRIM!

## Enabling TRIM

Now, if you know your device firmware supports TRIM, but it's just not in use currently, we can work on enabling TRIM.

Check on the current `provisioning_mode` for all drives attached to the Pi:

```
# find /sys/ -name provisioning_mode -exec grep -H . {} + | sort
/sys/devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb2/2-1/2-1:1.0/host0/target0:0:0/0:0:0:0/scsi_disk/0:0:0:0/provisioning_mode:full
```

We're going to need to change the `provisioning_mode` from `full` to `unmap`; but if you have more than one drive attached, you need to confirm which drive you need to change. You can do that using `lsscsi`:

```
# lsscsi
[0:0:0:0]    disk    Corsair  Voyager GTX      0     /dev/sda
```

Once you've confirmed which drive you need to change (in my case, there's only one, making this very easy), change the value from `full` to `unmap` in the path that the `find` command returned:

```
echo unmap > /sys/devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb2/2-1/2-1:1.0/host0/target0:0:0/0:0:0:0/scsi_disk/0:0:0:0/provisioning_mode
```

Run the `find` command again to confirm the `provisioning_mode` is now `unmap`.

Now, you need to update the `discard_max_bytes` value for the drive, based on the `Maximum unmap LBA count` value you got from the `sg_vpd -p bl /dev/sda` command earlier, times the `Logical block length` value you get from the `sg_readcap -l /dev/sda` command. In my case (your values may be different):

```
# echo $((4194240*512))
2147450880
```

Then write that value into the drive's `discard_max_bytes` setting. In my case:

```
# echo 2147450880 > /sys/block/sda/queue/discard_max_bytes
```

Now, to confirm TRIM is enabled, run:

```
# fstrim -v /
/: 117.6 MiB (123346944 bytes) trimmed
```

It should not give an error, and depending on how many blocks it needs to clean up, it could take a few seconds (or longer!).

## Making it stick

These values will all be reset next time you reboot the Pi. After a reboot, you get:

```
# fstrim /
fstrim: /: the discard operation is not supported
```

So, to make the rules stick, you need to add a udev rule:

```
# nano /etc/udev/rules.d/10-trim.rules
```

And add the following in that file:

```
ACTION=="add|change", ATTRS{idVendor}=="1b1c", ATTRS{idProduct}=="1a0e", SUBSYSTEM=="scsi_disk", ATTR{provisioning_mode}="unmap"
```

Now, you're probably wondering, _where the heck did he get the `idVendor` and `idProduct`? I used the handy `lsusb` utility:

```
# lsusb
Bus 002 Device 002: ID 1b1c:1a0e Corsair 
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 002: ID 2109:3431 VIA Labs, Inc. Hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

And looking at the 'Corsair' line, the vendor is the first part of the identifier (`1b1c`), and the product is the second part (`1a0e`). If you want a ton of detailed information about a USB device, use `lsusb -vd 1b1c:1a0e` (with the `vendor:product` specified).

Anyways, make sure to save your `10-trim.rules` file, then reboot the Pi. Try running `fstrim` again, and make sure it works:

```
$ sudo fstrim -v /
/: 111.4 GiB (119574462464 bytes) trimmed
```

The first time `fstrim` is run after a reboot, it will trim all the free space, which is why it gives such a large number. From that point on, the kernel will track changed blocks and trim only that data until the next boot.

### Automatic trimming

The last thing you will need to do to make sure the TRIM command is run automatically in the background (so you don't need to run `fstrim` manually) is to enable the built-in `fstrim.timer`.

To do that, run the command:

```
$ sudo systemctl enable fstrim.timer
```

By default, it will run weekly. Yay, now you have TRIM! That is, if your drive supports it. Check back in later and [subscribe to my blog](https://www.jeffgeerling.com/blog.xml) or [YouTube channel](https://www.youtube.com/c/JeffGeerling)—I'll be posting a video and blog post with data on which drives support TRIM!
