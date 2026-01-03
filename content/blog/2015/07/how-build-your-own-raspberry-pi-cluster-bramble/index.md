---
nid: 2211
title: "How to Build Your Own Raspberry Pi Cluster ('Bramble')"
slug: "how-build-your-own-raspberry-pi-cluster-bramble"
date: 2015-07-31T18:21:02+00:00
drupal:
  nid: 2211
  path: /blog/2015/how-build-your-own-raspberry-pi-cluster-bramble
  body_format: markdown
  redirects:
    - /blog/2016/how-build-your-own-raspberry-pi-cluster-bramble
aliases:
  - /blog/2016/how-build-your-own-raspberry-pi-cluster-bramble
tags:
  - cluster
  - dramble
  - drupal
  - drupal planet
  - guide
  - led
  - raspberry pi
  - raspbian
  - tutorial
---

<p style="text-align: center;">{{< figure src="https://raw.githubusercontent.com/geerlingguy/raspberry-pi-dramble/master/images/raspberry-pi-dramble-hero.jpg" alt="Rasbperry Pi Dramble" width="271" height="350" >}}</p>

One of the first questions I'm asked by those who see the Dramble is, "How do I build my own?" Since I've been asked the question many times, I put together a detailed parts list, and maintain it on the Dramble's project wiki on GitHub: [Raspberry Pis and Accessories](https://github.com/geerlingguy/raspberry-pi-dramble/wiki/Raspberry-Pis-and-Accessories).

For a little over $400, you can have the exact same setup, with six Raspberry Pi 2s, a network switch, a rack inside which you can mount the Pis, microSD cards for storage, a 6-port USB power supply, and all the required cables and storage!

<p style="text-align: center;">{{< figure src="https://raw.githubusercontent.com/geerlingguy/raspberry-pi-dramble/master/images/led-boards/led-boards-six-assembled.jpg" alt="Raspberry Pi RGB LED boards" width="450" height="313" >}}</p>

I also include detailed instructions for building a small breakout board for the Raspberry Pi's GPIO with a software-controlled RGB LED, so you can do things like monitor web requests using the RGB LED, show server status, or even use your Raspberry Pi as a flashlight in the dark!

But what if you just want to tinker with Drupal (or other software), or play around with RGB LEDs and other hardware through a Raspberry Pi GPIO, but you don't want to purchase six of them?

<p style="text-align: center;">{{< figure src="https://raw.githubusercontent.com/geerlingguy/drupal-pi/master/images/drupal-pi-model-2.jpg" alt="Drupal Pi - Drupal 8 on a Single Raspberry Pi" width="400" height="300" >}}</p>

I have a separate project, that I use for smaller-scale testing, [Drupal Pi](https://github.com/geerlingguy/drupal-pi). This project aims at configuring a single Raspberry Pi with the LEMP stack (again, using Ansible), and then installing Drupal 8 on the Pi.

I used to also maintain a lightweight Raspbian distribution, [Diet Raspbian](https://github.com/geerlingguy/diet-raspbian), specifically tailored for headless Pi servers, but now Raspbian has an official 'lite' version, so use that instead!
