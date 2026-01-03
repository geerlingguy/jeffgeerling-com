---
nid: 3393
title: "Getting Started with Meshtastic"
slug: "getting-started-meshtastic"
date: 2024-07-24T15:00:45+00:00
drupal:
  nid: 3393
  path: /blog/2024/getting-started-meshtastic
  body_format: markdown
  redirects: []
tags:
  - geerling engineering
  - mesh
  - meshtastic
  - node
  - p2p
  - radio
---

After seeing the Meshtastic booth at Open Sauce, my Dad and I thought it would be fun to learn more about the low power radio tech by getting our own radios and experimenting.

{{< figure src="./meshtastic-nodes.jpg" alt="Meshtastic nodes" width="700" height="auto" class="insert-image" >}}

Then, we were contacted by Simon from [Muzi Works](https://muzi.works), and he offered to send a few units of R1 and H1, his company's pre-built Meshtastic nodes.

What's a node, and what is Meshtastic? Excellent question.

## What is Meshtastic?

Simply put—and copied shamelessly from the [official website](https://meshtastic.org):

> An open source, off-grid, decentralized, mesh network built to run on affordable, low-power devices

Meshtastic nodes are often tiny gumstick-size PCBs with a LoRa radio module, a couple buttons, a tiny OLED display, and a USB port.

[Most of the nodes I've seen](https://meshtastic.org/docs/hardware/devices/) are built around the ESP32, but you can find LoRa modules for almost anything, [even the Raspberry Pi Pico](https://meshtastic.org/docs/hardware/devices/raspberry-pi/)! There are [3D printable cases](https://www.printables.com/model/741974-h1-case-for-heltec-v3-running-meshtastic) to protect the bare PCBs and even make them look classy, like the Muzi Works H1 pictured above.

You flash the Meshtastic firmware to the device, connect to it using Bluetooth, Serial, or WiFi, and then you're on the mesh! The mesh is peer-to-peer, which has a great benefit... and a great drawback.

**Benefit**: These devices can route communications entirely 'off-grid'. No need even for a smartphone or computer! There's no 4G or 5G connection, no need for WiFi or Bluetooth. The mesh is automatically structured over LoRa, using public frequencies (e.g. around 915 MHz in the US; see [this chart for regional frequencies](https://meshtastic.org/docs/getting-started/initial-config/#region-codes)). Just like the Internet (but disconnected from it), the network is self-healing, and you can route communications through the mesh so you don't have to be within line-of-sight from the device you're connected to.

**Drawback**: Being an entirely new communications platform / network, the mesh only reaches as far as there are people deploying nodes within range of each other. And... so far [there aren't many of us](https://meshtastic.liamcottle.net)—at least not in most cities.

As an illustration, I have so far never made contact with anyone—except for with my Dad, to whom I gave a node for testing.

{{< figure src="./meshtastic-testing-empty.jpg" alt="Meshtastic testing empty conversation" width="150" height="auto" class="insert-image" >}}

You can choose to [hook your node up to MQTT](https://meshtastic.org/docs/software/integrations/mqtt/), which is like an 'Internet gateway' for the device, but there are some caveats—most notably, you're no longer running entirely 'off-grid'!

## Acquiring a Meshtastic node (LoRa hardware)

The first node I bought was the Heltec V3. It's so popular it's frequently sold out on US distributors [like Rokland](https://store.rokland.com/collections/heltec-products/products/heltec-wifi-lora-32v3), but I bought mine (902-928 MHz model for US region) [from AliExpress](https://www.aliexpress.us/item/3256805256690400.html), which is inexplicably both cheaper and with less expensive shipping than ordering from a US supplier.

Once you get it in the mail, you should plug the antenna into the tiny antenna jack, pop the module into the case, and plug it into your computer's USB port using a USB-C cable.

> **Note**: Some vendors, like [Muzi Works](https://muzi.works), now sell pre-assembled, pre-flashed nodes, like my favorite, the [H1 with upgraded whip antenna](https://muzi.works/products/h1-complete-device-with-upgraded-whip-antenna-heltec-v3-running-meshtastic). It's still a good idea to upgrade the firmware once you get it, using the guide below!

## Flashing a node with Meshtastic firmware

Assuming you have a V3 like I do (or something similar), you can visit the [Meshtastic Web Flasher](https://flasher.meshtastic.org) in Chrome or Edge, select your device, choose a version (I usually choose the latest 'Stable' release), and click 'Flash'.

Depending on your device, it will either write over serial, or it will download a UF2 file to your computer that you need to drag to the device (it should mount as a 'USB mass storage device').

After the flashing is complete, the board will reboot, and will be running Meshtastic, ready for you to connect and configure it.

> **A note on firmware upgrades**:
> 
> For a while, I was confused about people saying to upgrade by flashing the firmware. I feared that would wipe out my custom name, region, and settings every time I upgraded.
> 
> Luckily, flashing the firmware only updates the Meshtastic code, it does not wipe out your user data and settings—unless you choose to wipe all data while flashing!

## Hello Mesh

Again in Chrome or Edge, head to https://client.meshtastic.org, and then connect to your device either via Serial (if it's plugged in via USB), or Bluetooth (if not). When you try connecting via Bluetooth, it will ask you to input a PIN for pairing. That PIN should be shown on the node's OLED display.

> **Meshtastic App**: You can also install the Meshtastic app for iOS or Android, and connect to your node using the app for mobile messaging. The app has the same configuration options exposed, so you can manage things either through the web client or the app—or technically even via serial directly without using any app/UI at all, but this blog post won't go that deep.

I won't go over all the configuration options here, because it's a doozy, but you will at _least_ have to set a 'Region' for your device. For me, it's the US. You can also configure the LoRa settings to choose a different radio preset, but most people seem to use the default (Long Range - Fast), and if you change your preset, you'll only be able to communicate with other nodes on that same preset.

Try sending out a message, over in the 'Messages' section, on the default Primary channel. Chances are, you will just be shouting into the void... but if you're lucky, someone else with a node will be within range, and you might be able to join their mesh!

I handed my Dad one of the Muzi Works nodes, and he and I will be having some fun experimenting in St. Louis. Check out the video of his first time setup over on Geerling Engineering:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/X4Akj5qF-3Q" frameborder='0' allowfullscreen></iframe></div>
</div>

Check out the [Meshtastic Community pages](https://meshtastic.org/docs/community/) to see if you can find a Meshtastic group in your area. And consider joining the [Meshtastic Discourse](https://meshtastic.discourse.group)!

## Bonus round - quirks

  - There are a few quirks with the app, radios, and devices still... it's very much a beta system right now, so get used to running into some strange or buggy interfaces.
  - At least on the V3 nodes I have, if I turn on WiFi (e.g. so I can communicate with the radio over my network instead of having to be within Bluetooth range), this disables Bluetooth, since the radios are exclusive to each other. The WiFi connection has some limitations, like the iOS app only works with Bluetooth right now, and I can't set a GPS location over WiFi from desktop or the iOS browser!
  - The devices can do AES 128/256-bit encryption, which is... adequate. If you enter into licensed Ham mode, you can broadcast with more power, though encryption is switched off. But if you want to have end-to-end private encryption that can't be cracked—this isn't the technology for that!
  - Speaking of privacy—if you choose to use precise location, or set a WiFi password, or store any other sensitive information on your node (passwords, private server connections for MQTT, etc.), make sure you keep physical control of the device. There's currently no protection if someone else grabs it—they could connect to it and retrieve your passwords in plain text!
  - There are people talking about distance records and 100s of kilometers of range—that's not going to be possible with one of these radios in the default configuration in an urban environment unless you're dozens of floors up in a high-rise building going through clear air! So far my Dad and I have gotten the mesh to work in a somewhat hilly part of St. Louis within a few hundred yards—but we haven't been trying _too_ hard, or optimizing our antennas yet :)
