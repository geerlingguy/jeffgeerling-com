---
nid: 3280
title: "Secure Computing with Zymbit's D35"
slug: "secure-computing-zymbits-d35"
date: 2023-04-06T15:00:59+00:00
drupal:
  nid: 3280
  path: /blog/2023/secure-computing-zymbits-d35
  body_format: markdown
  redirects:
    - /blog/2023/learning-about-secure-computing-zymbits-d35
aliases:
  - /blog/2023/learning-about-secure-computing-zymbits-d35
tags:
  - compute module
  - hardware
  - security
  - video
  - youtube
  - zymbit
---

Every few months, I try to test a number of new Raspberry Pi Compute Module 4-based projects, and at this point I've looked at [over 100](https://pipci.jeffgeerling.com/boards_cm) boards that use the CM4 to fill some need—general computing, industrial controls, media playback, or even clustered computing!

This month, [among other projects](https://www.youtube.com/watch?v=xp7JqUJgsXQ), I spent a bit of time with Zymbit's [Secure Edge Node D35](https://store.zymbit.com/products/secure-compute-node-d35):

{{< figure src="./zymbit-sata-side-hero.jpg" alt="Zymbit Secure Edge Node D35 SATA side view" width="700" height="394" class="insert-image" >}}

It's built in the same form factor as a 3.5" hard drive, but the guts are entirely different. Because of the form factor, it can be installed in a drive bay in another computer, or it can operate standalone or on a DIN rail mount.

It uses the eMMC storage on a CM4 as its primary built-in storage, but also has an internal M.2 NVMe SSD slot. It is powered either via PoE, SATA, or a 12v barrel plug.

Besides the massive heatsink and the I/O ports, nothing on the exterior betrays the purpose of this little black box.

{{< figure src="./zymbit-overview-port-side.jpg" alt="Zymbit Secure Edge Node D35 Port Side" width="700" height="394" class="insert-image" >}}

> Note: Most of my testing was performed on an alpha version of the unit. The production unit differs slightly in appearance, and Zymbit sent me one for testing, but it didn't arrive in time for this blog post. I may follow-up in the future as I go more in-depth on physically-secure computing!

It's only if you take one apart that you start to glimpse all the security integrated in the system:

{{< figure src="./zymbit-cover-open-tamper-switches.jpg" alt="Zymbit Secure Edge Node cover removed - tamper switches and battery" width="700" height="394" class="insert-image" >}}

Besides exposing the 'user' side of the board with it's integrated M.2 NVMe slot, if you look closely you'll see four pressure-sensitive tamper switches, a header for an extra external perimeter tamper circuit, a SIM tray, and a coin cell battery.

{{< figure src="./zymbit-internal-motherboard.jpeg" alt="Zymbit Secure Compute Node D35 - internals with SCM Raspberry Pi CM4" width="700" height="467" class="insert-image" >}}

In addition, if you remove that board and flip it over, you'll find a 'sandwich-style' Compute Module 4, encapsulated onto another board. This 'Zymbit hardware security supervisor' board includes more hardware security features: hardware wallets, external key storage, a hardware cryptographic engine, and a secure boot solution (requiring Zymbit's custom Pi firmware).

Here's the backside of the 'Secure Compute Module' (after removal from the motherboard pictured above):

{{< figure src="./zymbit-scm-cm4-backside.jpeg" alt="Backside of Zymbit Secure Compute Module" width="700" height="467" class="insert-image" >}}

Note that these pictures were taken with an early alpha version of the Secure Edge Node—there are minor differences in the production version.

If this Secure Edge Node were set to 'production' mode, any of the teardown actions I performed would've resulted in a paperweight.

In fact, the [documentation](https://docs.zymbit.com/getting-started/sen/production-mode/) has tons of warnings about this:

> THE BINDING PROCESS IS PERMANENT AND CANNOT BE REVERSED. PAY ATTENTION TO THE FOLLOWING:
> 
> If you are using the Perimeter Detect features, then the sequence in which you arm and disarm this feature is very important. Be sure to carefully follow the process steps below.

And digging into the docs, you'll find there are multiple 'tamper' events which you can react to, including:

  - Physical tamper (two channels - removal of cover or breaking the extra tamper circuit)
  - Low temperature threshold
  - High temperature threshold
  - Low battery voltage threshold
  - Supervised boot failure

In addition, there's a built-in accelerometer that can be used alongside other tamper prevention methods if you so choose, to detect if the device was picked up, or was subject to shock attacks. There's an entire [API](https://docs.zymbit.com/api/) to interact with the physical security features.

{{< figure src="./zymbit-perimeter-timestamps.jpg" alt="Zymbit perimeter detect Python script" width="700" height="394" class="insert-image" >}}

If you activate any of the tampers, and the device is set to production mode, it will brick itself immediately. 'Disarming' is the only way to make hardware changes in the future.

This all begs the question: _who is this for?_

Well, you certainly have to trust Zymbit, since they are the sole provider of this hardware, and they also control the hardware encryption and firmware on the device (outside of any cryptographic keys you generate on the device, or any items you add to the [Supervised Boot manifest](https://docs.zymbit.com/tutorials/supervised-boot/).

Assuming you do, if you need to deploy a computer with any sensitive data into a 'low-trust' environment, this computer would be an ideal solution. Such is the case for many 'IoT' or 'Edge' deployments, or even something as simple as a custom vending machine deployed into a public space! Check out this [2018 AWS re:Invent presentation with Phil Strong](https://www.youtube.com/watch?v=ATJ87z7g7xA) for more background.

The achilles heel—which Zymbit can do nothing about—is the _software_ you deploy to this thing. If you deploy insecure software that stores secure credentials in memory, or exposes data from the now-decrypted filesystem while it's running, well... it's still game over.

So while Zymbit's Secure Edge Node can certainly help you verify your hardware and boot process is secure, you still need to perform your own security hardening on the software you deploy.

Check out my overview of the Secure Edge Node, along with many other new Compute Module 4-based products, in my latest video:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/xp7JqUJgsXQ" frameborder='0' allowfullscreen></iframe></div>
</div>
