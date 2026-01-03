---
nid: 3217
title: "Resetting IPMI and upgrading BIOS on a Supermicro motherboard under FreeBSD (or not)"
slug: "resetting-ipmi-and-upgrading-bios-on-supermicro-motherboard-under-freebsd-or-not"
date: 2022-07-12T17:22:53+00:00
drupal:
  nid: 3217
  path: /blog/2022/resetting-ipmi-and-upgrading-bios-on-supermicro-motherboard-under-freebsd-or-not
  body_format: markdown
  redirects:
    - /blog/2022/resetting-ipmi-on-supermicro-motherboard-ipmicfg-under-freebsd
    - /blog/2022/resetting-ipmi-on-supermicro-motherboard-ipmicfg-under-freebsd-or-not
aliases:
  - /blog/2022/resetting-ipmi-on-supermicro-motherboard-ipmicfg-under-freebsd
  - /blog/2022/resetting-ipmi-on-supermicro-motherboard-ipmicfg-under-freebsd-or-not
tags:
  - freebsd
  - homelab
  - ipmi
  - linux
  - servers
  - supermicro
---

That title is awfully specific.

{{< figure src="./aspeed-soc-supermicro-ipmi-motherboard.jpeg" alt="ASPEED SoC on Supermicro Motherboard powering IPMI" width="700" height="467" class="insert-image" >}}

But I was building a new FreeBSD server with a used SuperMicro motherboard with IPMI. The default password was changed from `ADMIN` (or maybe it's a new enough board that it's a random password), and when I was booted into FreeBSD, I wanted to reset the IPMI settings so I could be sure I was starting fresh.

`ipmitool` that came with my FreeBSD install doesn't seem to be able to reset IPMI to factory defaults, so I tried running `ipmicfg` from Supermicro's website (which is annoying to download—you have to fill out a form and a Captcha for the privilege).

I put it on a flash drive, since I didn't have networking set up yet, and ran `mkdir /mnt/usb &amp;&amp; mount_msdosfs /dev/da0s1 /mnt/usb` to open it up.

But when I tried running the executable, I got:

```
# ./IPMICFG-Linux.x86_64
ELF binary type "0" not known.
zsh: exec format error: ./IPMICFG-Linux.x86_64
```

Stuff built for Linux doesn't necessarily run on *BSD. Therefore, I had to [enable Linux binary compatibility](https://docs.freebsd.org/en/books/handbook/linuxemu/):

```
# nano /etc/rc.conf

linux_enable="YES" # Add this line to the file

# reboot
```

(In my case, I actually had to add the `linux_enable` line inside `/conf/base/etc/rc.conf` since I was running TrueNAS on this build.)

After the reboot, run:

```
# service linux start
```

Then you should be able to run the binary and reset to factory defaults:

```
# ./IPMICFG-Linux.x86_64
ELF interpreter /lib64/ld-linux-x86-64.so.2 not found, error 2
zsh: abort ./IPMICFG-Linux.x86_64
```

...or not. That didn't work because FreeBSD's Linux compatibility layer is apparently missing the libraries required for `ipmicfg` to run. Oh well, it was worth a try!

## Switching gears - booting DOS!

So instead, I flashed FreeDOS to a USB flash drive using [Rufus](https://rufus.ie/en/) on my Windows PC. I then copied the `DOS` directory from the IPMICFG Supermicro download to the USB flash drive, then plugged that into my Supermicro motherboard, rebooted, and made sure to boot off that flash drive in the BIOS settings.

Once booted, I got the all-too-familiar `C:\>` prompt, and ran the following commands:

```
# Change into the DOS directory.
C:\> cd DOS

# Check the current IPMI user listing.
C:\DOS> ipmicfg -user list

# Change the ADMIN user password.
C:\DOS> ipmicfg -user setpwd 2 [password]
```

That worked!

Though, in my case, I found out the ADMIN user had been disabled somehow (it showed 'No' under the Enable column), so I ended up just resetting the entire BMC using the command:

```
# WARNING: This will wipe your BMC config entirely!
C:\DOS> ipmicfg -fd 2
```

And there... I could _finally_ log into this used motherboard (which apparently came from OVH) and set my own password.

[This answer](https://serverfault.com/a/608868) on ServerFault was very helpful in figuring out `ipmicfg`, as well as the article on ServeTheHome titled [Reset Supermicro IPMI Password to Default – Physical Access](https://www.servethehome.com/reset-supermicro-ipmi-password-default-lost-login/).

## Updating the BIOS

At the same time, it might be a good idea to update your motherboard's BIOS:

  1. [Search for your motherboard model number on this page](https://www.supermicro.com/support/resources/bios_ipmi.php?vendor=1)
  2. Download the BIOS .zip file
  3. Copy the contents to a `BIOS` directory on the FreeDOS boot drive
  4. Reboot the server from that boot drive.
  5. In the BIOS directory, run `C:\BIOS> FLASH.BAT [BIOSFILE.###]` (e.g. `X10SDVF1.604` for the BIOS filename, in my case).

It'd be nice if you didn't need a license to update the BIOS through IPMI... but here we are. I mean, if you search for "SuperMicro IPMI License Generator", you can probably find a way to get the key for your server... but it'd be nice if the motherboard were unlocked by default.
