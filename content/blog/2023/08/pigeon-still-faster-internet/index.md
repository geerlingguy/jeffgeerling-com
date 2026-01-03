---
nid: 3306
title: "A Pigeon is still faster than the Internet"
slug: "pigeon-still-faster-internet"
date: 2023-08-28T13:01:25+00:00
drupal:
  nid: 3306
  path: /blog/2023/pigeon-still-faster-internet
  body_format: markdown
  redirects: []
tags:
  - bandwidth
  - birds
  - internet
  - pigeon
  - test
  - video
  - youtube
---

{{< figure src="./jeff-hold-homing-pigeon.jpeg" alt="Jeff Geerling holding a homing pigeon" width="700" height="394" class="insert-image" >}}

In 2009, a company in South Africa [proved a homing pigeon was faster than an ADSL connection](https://phys.org/news/2009-09-carrier-pigeon-faster-broadband-internet.html), flying a 4 GB USB flash drive to prove it.

Besides [IEEE's speculative work](https://spectrum.ieee.org/pigeonbased-feathernet-still-wingsdown-fastest-way-of-transferring-lots-of-data), nobody's actually re-run the 'bird vs. Internet' race in over a decade.

Now that I have gigabit fiber, I thought I'd give it a try.

## Video

I published a video with all the details—and even more background on the graceful birds used in the experiment—over on my YouTube channel:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/4pz2kMxCu8I" frameborder='0' allowfullscreen></iframe></div>
</div>

## Ground Rules

The idea is simple: strap as much physical storage media on a bird as you possibly can.

And the IEEE article, along with most current speculation, postulates microSD cards as the best option for volume of data per gram.

While that's not a _bad_ option, nobody seems to take into account the data transfer _on and off_ the storage media. Most microSD cards falter when you try writing to them full tilt for an hour at a time, falling to tens of MB/sec.

{{< figure src="./three-sandisk-extreme-pro-1tb.jpeg" alt="SanDisk Extreme PRO 1TB USB flash drives" width="700" height="394" class="insert-image" >}}

So I went with three [1TB SanDisk Extreme PRO](https://amzn.to/3qG8X8h) flash drives, and ripped them out of their enclosures to get them down to 5g each. They're expensive, but they use a for-real SSD controller and fast flash storage inside, capable of sustaining 250-300 MB/second writes for the full terabyte.

Getting data on and off them was also a challenge, since I'd need to do it from my MacBook Air, which only has two USB 4 / Thunderbolt 4 ports.

Using any of my portable USB-C hubs, I ran into a bottleneck: the USB-A and USB-C ports are almost always sharing the same USB root hub, meaning 5 Gbps of data transfer is shared among all the drives.

So I had to also buy an [OWC 5-port Thunderbolt 3 hub](https://amzn.to/3qNW4sI), which allowed me to saturate all the flash drives.

{{< figure src="./macbook-air-copying-owc-thunderbolt-3-usb-c-flash-nvme.jpeg" alt="MacBook Air copying to Thunderbolt 3 USB-C flash drives and NVMe" width="700" height="394" class="insert-image" >}}

But as my MacBook Air only has a 512 GB SSD inside, I also had to purchase a [huge Sabrent Rocket Q NVMe drive](https://amzn.to/3OWkOqL), and stick it on an [NVMe to USB 3.1 Gen 2 adapter](https://amzn.to/44nrfJ6) so I could read and write around 750 MB/sec.

There were some caveats on the Internet copy too: I had to mess with SSH, `scp`, `rsync`, `wormhole`, and even `croc` to try to get a full gigabit of bandwidth to be utilized.

Unfortunately, likely due to the non-datacenter ISPs involved, I could only ever get an average of 75 MB/sec over the Internet, point to point.

I even wrote up [this blog post on my own wormhole relay server](/blog/2023/my-own-magic-wormhole-relay-zippier-transfers) trying to solve that challenge!

## Birds

I worked with Greg from [St. Louis Doves](http://www.stldoves.com) to attach the three 1TB flash drives to one of his homing pigeons, a less-than-happy grey dove that we brought about a mile away, and had fly back to the coop:

{{< figure src="./grey-pigeon-returning-to-coop-with-payload-flash-storage.jpg" alt="Grey dove homing pigeon flying back to coop with storage" width="700" height="394" class="insert-image" >}}

I learned a lot of fascinating stuff about these beautiful birds, and if you want to know more, go [watch the video](https://www.youtube.com/watch?v=4pz2kMxCu8I), but what's relevant to our discussion is that one of these birds _can_, in fact, carry these three high-speed 1TB USB flash drives. Probably one or two more, if I'm being honest!

But the pigeons weren't that comfortable with the size of the flash drives—it would be better to find some that are half the length, as that would allow them to bend their little legs for easier landings.

I could extrapolate some data about homing pigeon flight based on their average cruising speed, about 60-80 mph (90-120 km/h), but I really wanted to give the pigeons an assist.

So I became _Pijeff_, and carried the flash drives from St. Louis all the way to the 45Drives headquarters in Nova Scotia, and raced against the Internet copy across the same distance:

{{< figure src="./jeff-pigeon-airplane.jpeg" alt="Jeff is a Pigeon or Pijeff on the airplane" width="700" height="394" class="insert-image" >}}

<em>Yes</em>, I did wear that mask in Toronto, but <em>no</em>, I did not leave it on the entire journey.

## Results

Once in Nova Scotia, I wound up with the following results:

  - Pigeon (jet-assisted) total time: 6 hours, 53 minutes
  - Internet total time: 10 hours, 54 minutes

So, the Pigeon still wins! Well, at least a jet-assisted pigeon.

{{< figure src="./pigeon-data-transfer-equation.png" alt="Pigeon Data Transfer Equation" width="700" height="394" class="insert-image" >}}

Using my new Pigeon Data Transfer Equation, I can estimate a pigeon would win under its own power out to about 500 miles (800 km). And a jet-assisted pigeon like _Pijeff_ could win out to around 5,000 miles (8000 km):

{{< figure src="./pigeon-vs-internet-jeff-geerling.jpg" alt="Pigeon vs Internet Jeff Geerling chart" width="700" height="390" class="insert-image" >}}

## IPoAC

The next logical step is [IPoAC](https://en.wikipedia.org/wiki/IP_over_Avian_Carriers)—IP over Avian Carriers. This communication protocol would provide more robust data transfer guarantees, though there are some potential issues.

Only one serious implementation has taken flight, and [that was back in 2001, in Norway](https://blug.linux.no/rfc1149/writeup/):

<blockquote>...it turned out that things had been so busy at the other end that they forgot to shut the pigeon cage, and the remaining two pigeons escaped without an IP packet. There was only six return pigeons, thus we got four ping replys, with ping times varying from 3211 to 6389 seconds. I guess this is a new record for ping times…</blockquote>

55% packet loss isn't all that great, especially if we are attaching nearly $400 of data payloads per bird, but technology has advanced quite a bit since 2001...

Watch the video over on my YouTube channel: [Is a pigeon STILL faster than the Internet?](https://www.youtube.com/watch?v=4pz2kMxCu8I).
