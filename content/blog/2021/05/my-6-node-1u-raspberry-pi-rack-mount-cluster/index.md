---
nid: 3098
title: "My 6-node 1U Raspberry Pi rack mount Cluster"
slug: "my-6-node-1u-raspberry-pi-rack-mount-cluster"
date: 2021-05-20T14:01:53+00:00
drupal:
  nid: 3098
  path: /blog/2021/my-6-node-1u-raspberry-pi-rack-mount-cluster
  body_format: markdown
  redirects: []
tags:
  - 3d printing
  - network
  - rack
  - raspberry pi
  - servers
  - video
  - youtube
---

Now that I have a half-height rack and a 3D Printer, I figured I should finally move all my Raspberry Pis from sitting in odd places in my office to the rack. And what better way than to print my own 1U Raspberry Pi Rack mount unit?

{{< figure src="./6-node-rackmount-1u-raspberry-pi-enclosure.jpeg" alt="6 Node Raspberry Pi 1U Rack Mount enclosure - 3D Printed for Pi 4 model B" width="600" height="400" class="insert-image" >}}

The rack unit you see above was assembled from 6 'frames', 6 hot-swappable Pi carrier trays, 2 rack mount ears, and a couple lengths of threaded rod for rigidity.

It was printed from [these plans from russross on Thingiverse](https://www.thingiverse.com/thing:4125055); Russ Ross _also_ made an [assembly video](https://www.youtube.com/watch?v=auzATw-i8Lk), and shows how you can [build a 2U 12-Pi enclosure](https://www.youtube.com/watch?v=splC57efBFQ) using the same basic design, with interchangeable Pi trays!

## Video

There is more detail and a full walkthrough of my home rack in this video:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/LcuNc4jz-iU" frameborder='0' allowfullscreen></iframe></div>
</div>

## Rack printing and assembly

Firstly, I should note that I still consider myself a 3D Printing novice. It's not like you can go to the store, buy a 3D Printer, unbox it, plug it in, and get good prints right away. Even the more expensive models require a lot of 'tuning' to get right, and that assumes you also know at least a decent amount about slicing and at least have rudimentary 3D CAD skills!

My first attempt at printing the frame resulted in the printer trying to bridge 10cm gaps and printing on air. It tried, but I've found time and time again, if you ask the printer to do the impossible, it'll blindly trust your input, no matter the result:

{{< figure src="./3d-print-spaghetti-messed-up-no-support.jpg" alt="3D Printer Spaghetti - Messed up with no support and printing on air" width="599" height="337" class="insert-image" >}}

But once I figured out I needed supports, and to be extra careful about bed leveling and shrinkage—compensated for by using a brim in this case—I was able to get the frames, trays, and ears printed without issue. The full process involved:

  1. Printing 6 'frames' that hold the Pi trays and are put together through threaded rod running underneath.
  2. Printing 6 'trays' that hold the Raspberry Pis using 12mm M2.5 screws.
  3. Printing 2 'ears' that allow the trays to be mounted to a standard 1U rack space.
  4. Assembling everything together using 2 #10-24 threaded rods cut to precisely 17 5/8", and secured with a #10-24 nut on each side

It came together very well after I sorted the frame printing issues:

{{< figure src="./pi-rack-1u-ear-closeup.jpeg" alt="Pi Rack ear closeup" width="600" height="400" class="insert-image" >}}

You can see the whole structure gets its rigidity from the two threaded rods running underneath:

{{< figure src="./pi-rack-1u-side-view.jpeg" alt="Pi rack side closeup" width="600" height="400" class="insert-image" >}}

And while the frames in this enclosure don't block the ports on the Pi, there's not really enough room between frames to fit standard connectors in except on the left-most Pi. The rear is also open for ventilation, but don't expect to be able to pop out a microSD card unless you slide the Pi out in its tray:

{{< figure src="./pi-rack-1u-rear-view.jpeg" alt="Pi rack rear closeup" width="600" height="400" class="insert-image" >}}

The enclosure feels great, and besides being a little 'proud' of the other metal rack units on the front (there's more depth to provide more strength in the 3D print), it looks right at home in my rack:

{{< figure src="./rack-mount-pi-cluster-networking.jpeg" alt="Rack mount networking setup with 1U Raspberry Pi 6x rack" width="600" height="400" class="insert-image" >}}

## What do I do with the Pis?

The first Pi is running my [internet-pi](https://github.com/geerlingguy/internet-pi) configuration, which sets up Pi-hole for ad-blocking and DNS on my home network, and also runs a Prometheus + Grafana [internet-monitoring](https://github.com/geerlingguy/internet-monitoring) dashboard so I can see how my home Internet is doing (and whether I am getting the full speeds I pay for).

The second Pi is currently running the [Raspberry Pi Dramble](http://www.pidramble.com) website solo—at some point I'll migrate my K3s Kubernetes cluster into the rack, and it will be running that way again, but right now the site is just running on one Pi with Docker and Docker Compose.

The Pi at the end is monitoring my Starlink Internet connection, and is on a separate PoE switch.

In the video, I go into a little more detail about the rack itself, as well as some of the other things I intend to do with my rack and home network in general, so [check it out](https://www.youtube.com/watch?v=LcuNc4jz-iU) if you haven't watched it already.
