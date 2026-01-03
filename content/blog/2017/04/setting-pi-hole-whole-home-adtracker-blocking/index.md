---
nid: 2762
title: "Setting up a Pi Hole for whole-home ad/tracker blocking"
slug: "setting-pi-hole-whole-home-adtracker-blocking"
date: 2017-04-03T19:26:44+00:00
drupal:
  nid: 2762
  path: /blog/2017/setting-pi-hole-whole-home-adtracker-blocking
  body_format: markdown
  redirects: []
tags:
  - advertising
  - dns
  - network
  - performance
  - pi hole
  - raspberry pi
  - server
  - tutorial
---

{{< figure src="./pi-hole-safari-dashboard-admin.png" alt="Pi Hole - Admin DNS query request dashboard page in Safari" width="650" height="387" class="insert-image" >}}

[Pi Hole](https://pi-hole.net/) is a nifty open source project that allows you to offload the task of blocking advertisements and annoying (and often malicious) trackers to a Raspberry Pi. The installation is deceptively simple (a `curl | bash` affair), but I wanted to document how I set up mine headless (just plugging the Pi into power and the network).

## Set up Raspbian Lite

I bought a Raspberry Pi model 2 B along with the official Raspberry Pi foundation Case. Then I bought a [Samsung Evo+ 32GB microSD card](https://www.amazon.com/Samsung-Class-Micro-Adapter-MB-MC32DA/dp/B00WR4IJBE/ref=as_li_ss_tl?ie=UTF8&qid=1491239012&sr=8-1&keywords=samsung+evo++micro+sd&linkCode=ll1&tag=mmjjg-20&linkId=1610d88b7c0bdc18d2a6552cf6983ee7) (which comes with a full-size SD card adapter), and did the following steps on my MacBook Pro to set up the Pi's OS:

  1. Download [Raspbian Jessie Lite](https://www.raspberrypi.org/downloads/raspbian/). Expand the downloaded Zip file.
  2. Insert the microSD card (in the SD adapter) into your SD card reader.
  3. Open Terminal, and run `diskutil list`
  4. See which disk the microSD card is (e.g. `/dev/disk2`), then unmount the card: `diskutil unmountDisk /dev/disk2`).
  5. Change directories into the directory where you downloaded Raspbian Jessie Lite (e.g. `cd ~/Downloads`).
  6. Run the following command to write the disk image to the microSD card: `sudo dd if=2017-03-02-raspbian-jessie-lite.img of=/dev/rdisk2 bs=1m`
    - Use the filename for the image version you downloaded; it might be different than the `if` shown above.
    - Note that the `of` (output) is using `/dev/rdisk2`—don't use `/dev/disk2` because that will result in a much slower copy operation.
    - If you have pipeviewer installed, you can use `pv yyyy-mm-dd-raspbian-jessie.img | sudo dd of=/dev/rdisk2 bs=1m` instead to show copy progress.
  7. After the copy is finished, you should see a new `boot` SD card mounted on your computer.
  8. Create an 'ssh' file to tell Raspbian to enable SSH on boot (so you can log into the Pi remotely): in Terminal, run `touch /Volumes/boot/ssh`
  9. Eject the boot volume, and put the microSD card into your Raspberry Pi.

> Note: Don't use WiFi for Pi Hole, because that would introduce a lot of latency for DNS calls. It's better to plug your Pi (no matter what flavor) into the wired network so it doesn't become a bottleneck for your Internet connection!

## Set up the Raspberry Pi

  1. Plug your Pi into the network, and plug in power so the Pi will boot.
  2. Use `nmap` (e.g. `sudo nmap -sP 10.0.1.1/24`) or `fing` (e.g. `sudo fing 10.0.1.1/24`) to discover your Raspberry Pi's IP address (see how in my post on [setting up a Pi as a remote time-lapse camera](//www.jeffgeerling.com/blog/2017/raspberry-pi-zero-w-headless-time-lapse-camera)).
  3. Log into the Pi via SSH: `ssh pi@ip_address` (where `ip_address` is the IP of the Pi) — accept the hostkey by typing `yes` when prompted, then enter the default Pi password, `raspberry`.
  4. Set a static IP address: `sudo nano /etc/dhcpcd.conf` to edit the configuration, then add the following to the end (using the settings specific to your network/IP):

        interface eth0
        static ip_address=10.0.1.24
        
        static routers=10.0.1.1
        static domain_name_servers=10.0.1.1

  5. Reboot the Pi (`sudo reboot`) and log back in via SSH.
  4. Run `sudo raspi-config` to configure basic settings:
    - Set a new (secure) password.
    - Set a hostname (e.g. `pi-hole`).
  5. Restart the Pi after changing those settings.

> It's a good idea to [set a static IP address for your Pi](https://www.modmypi.com/blog/how-to-give-your-raspberry-pi-a-static-ip-address-update)—either in the Pi's own settings, or (preferably) on your network's router (if the router allows you to assign static IP addresses to devices based on MAC address).

## Set up Pi Hole

  1. Install Pi Hole with `curl -sSL https://install.pi-hole.net | bash`
  2. Follow the entire Pi Hole setup process (it will ask you to confirm settings at a few different points).
  3. Note the admin dashboard password at the end of the install process; you can visit the dashboard afterwards and see DNS statistics.

## Tell your router to use Pi Hole (for network-wide protection)

If you have a decent network router (in my case, I have an AirPort Extreme), you can use its administration interface to set up DNS settings for the entire network. Point the DNS at the Pi Hole's IP address, and then you should start seeing that all the network's DNS requests are routed through the Raspberry Pi's DNS. You should also note a lack of advertisements in your browsing :)

Alternatively, you can configure any of your computers to use the Pi Hole's DNS (instead of the router) if you don't want the Pi Hole to be used on the entire network.
