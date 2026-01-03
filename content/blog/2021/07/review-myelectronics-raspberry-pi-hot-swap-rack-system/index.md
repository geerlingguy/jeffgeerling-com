---
nid: 3118
title: "Review: MyElectronics Raspberry Pi hot-swap rack system"
slug: "review-myelectronics-raspberry-pi-hot-swap-rack-system"
date: 2021-07-28T19:15:09+00:00
drupal:
  nid: 3118
  path: /blog/2021/review-myelectronics-raspberry-pi-hot-swap-rack-system
  body_format: markdown
  redirects: []
tags:
  - homelab
  - myelectronics
  - rack
  - raspberry pi
  - video
  - youtube
---

{{< figure src="./myelectronics-raspberry-pi-rack-units.jpeg" alt="MyElectronics Raspberry Pi Rack mount system" width="600" height="338" class="insert-image" >}}

MyElectronics, a small business in the Netherlands, specializes in small computer rackmount solutions. They sent me these two racks (a 1U and 2U Raspberry Pi rack) and asked me to test them out and compare them to the [3D Printed Raspberry Pi Rack](https://www.youtube.com/watch?v=LcuNc4jz-iU) I built earlier this year, based on a [design by Russ Ross](https://www.thingiverse.com/thing:4125055).

They also have a [3U Raspberry Pi rackmount unit](https://www.myelectronics.nl/us/19-inch-rack-mount-3u-for-12-16x-raspberry-pi.html), but I won't be reviewing that here.

The contents of this review are summarized in this video I posted on YouTube:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/87lAQtML2FQ" frameborder='0' allowfullscreen></iframe></div>
</div>

## MyElectronics' Rack system

The slot-based rack units are available in three sizes: 1U for 5 Pis, 2U for 16, or 3U for 16 Pis plus accessory jacks.

The big difference between this rack solution and older designs on the market, like [this UCTRONICS rack on Amazon](https://amzn.to/2WxkTJV), or [52Pi's 1U rack mount](https://wiki.52pi.com/index.php/1U_19%27%27_Rack_Mount_for_Raspberry_Pi_4B_SKU:_EP-0143), is that you can hot-swap Pis from the front without removing the whole thing, just like the [3D-printed Pi Rack](/blog/2021/my-6-node-1u-raspberry-pi-rack-mount-cluster) I built earlier this year.

But unlike my 3D printed rack, the stamped metal has the strength to add in keystone jacks and plastic retainers that hold the Pis securely in place. My plastic 3D printed rack has no retention mechanism, so Pis can slide out if the rack is tipped forward.

{{< figure src="./raspberry-pi-in-rackmount-tray-port-side-screws.jpg" alt="Raspberry Pi in Rackmount tray with no screws on rear" width="551" height="310" class="insert-image" >}}

To install a Pi, you screw in two screws on the port side into the metal frame. It holds the Pi secure enough, though I wish there were at least one more rigid standoff on the rear of the Pi for even better stability.

The plastic retainers compress against the metal to hold the Pi in, but they're the weak point in this system—I already broke one. Luckily MyElectronics sends a few replacements with every order, but I have to wonder if a screw-based retaining mechanism would be better in the long-term.

{{< figure src="./keystone-jacks-in-raspberry-pi-rack.jpg" alt="Keystone Jacks in Raspberry Pi Rackmount" width="601" height="338" class="insert-image" >}}

The keystone IO panels let you add things like an HDMI port or network jack on the front, so you can cable manage from the front, or even plug in a display for debugging a Pi without removing it.

## Pricing

Probably the biggest downside to these rack units is price. The 1U enclosure for 5 Pis costs a little over $100, and while worldwide shipping is free, it can take some time to arrive. If you want faster shipping, it'll cost more.

I estimate my 3D printed enclosure cost around $40-50 in materials, plus my time putting it together. This enclosure is at least double the price, and more if you want to get it within a week or less. So if you already have a 3D printer and the time to put together a rack, you might not love the price.

But if you're serious about racking a lot of Pis, MyElectronics' modular rack system—especially the 2 and 3U versions—is the best I've seen. They look great, and their whole system is a great way to introduce Pis into the datacenter—or your premium homelab rackmount setup.

MyElectronics also builds custom rack solutions, but something custom might be out of the price range of budget-minded homelabbers!

{{< figure src="./2u-rackmount-myelectronics-raspberry-pi.jpeg" alt="2U MyElectronics Raspberry Pi Rackmount Unit" width="600" height="338" class="insert-image" >}}

Anyways, I liked this rack enough that I replaced my 3D printed Pi rack with it, and I'm hoping I'll be able to fill in the 2U rack with a new clustering project soon!

And, well, I'm also a sucker for all things Dutch, so besides the price, there's not much to complain about. [Hup Holland Hup!](https://www.youtube.com/watch?v=ZTN02KuzNPo)
