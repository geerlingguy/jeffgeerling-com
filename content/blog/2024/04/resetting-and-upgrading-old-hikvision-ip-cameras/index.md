---
nid: 3366
title: "Resetting and upgrading old Hikvision IP Cameras"
slug: "resetting-and-upgrading-old-hikvision-ip-cameras"
date: 2024-04-18T16:40:12+00:00
drupal:
  nid: 3366
  path: /blog/2024/resetting-and-upgrading-old-hikvision-ip-cameras
  body_format: markdown
  redirects: []
tags:
  - cameras
  - frigate
  - hikvision
  - ip
  - nvr
  - poe
  - surveillance
---

{{< figure src="./hikvision-security-camera-in-drop-ceiling.jpeg" alt="Hikvision security camera installed in drop ceiling" width="700" height="auto" class="insert-image" >}}

This guide isn't definitive, but it is a good reference point as I am wiping out some Hikvision IP cameras I inherited in my new office space. They were all paired with an annoying proprietary Hikvision NVR, and I wanted to wipe them and use them on a new isolated VLAN with my new [Raspberry Pi Frigate-based NVR setup](https://github.com/geerlingguy/pi-nvr).

The cameras I have are Hikvision model number [DS-2CD2122FWD-IS](https://us-legacy.hikvision.com/en/products/cameras/network-camera/value-series/outdoor-dome/fixed-focal/2-mp-fixed-network-dome-camera), but this guide should apply to many of the cameras from that era.

{{< figure src="./hikvision-camera-reset-button-location.jpg" alt="Hikvision security camera reset button location" width="700" height="auto" class="insert-image" >}}

The process to reset a camera to factory defaults, update it to the latest firmware, and get it going on my network is as follows:

  1. Remove the dome cover (mine was held on with three torx T10 screws).
  1. Hold down reset button (see image above) while plugging in PoE cable, and keep it held for at least 10 seconds.
  1. Wait a minute or so for the camera to reset and boot up.
  1. Set your computer's network interface to 192.168.1.X subnet (I set mine to the manual IP `192.168.1.2`).
  1. Visit http://192.168.1.64/ in browser, and set an admin password (be sure to save this password somewhere!)
  1. Install [Hikvision's iVMS-4200 software](https://www.hikvision.com/en/support/download/software/ivms4200-series/) on your computer.
  1. Launch iVMS-4200 and add the camera in there (with IP address `192.168.1.64`).
  1. Select the camera from the device list, and click 'Remote Configuration'.
  1. In the 'System Maintenance' tab, under 'Remote Upgrade', select the `digicap.dav` file from your device's firmware download (for my camera, [5.5.82](https://us-legacy.hikvision.com/en/products/cameras/network-camera/value-series/outdoor-dome/fixed-focal/2-mp-fixed-network-dome-camera)), and upgrade the camera. (Note: the interface greys out, and then after a minute the progress bar will start filling up. Be patient.)
  1. After the upgrade is complete, grab the camera's MAC address and configure DHCP and local DNS for it in your router (if that's your thing), or if not, skip to the next step.
  1. Log into the camera in the browser (at `http://192.168.1.64/`), click on the Configuration tab, then go to Network > Basic Settings, check the 'DHCP' checkbox, and click 'Save'.
  1. Reboot the unit when the prompt to reboot appears, then after it reboots, it should pick up an IP address from your router using DHCP.

Obviously, if you want to set a static IP for the camera separately, you can go ahead and do that too. I'm setting all my VLAN and IP configuration on the router, though. Especially as these cameras get older and more outdated (though they still work fine), it's best to separate them off on their own VLAN, since old firmware likely has exploits that could be hacked.
