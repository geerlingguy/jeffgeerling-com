---
nid: 3088
title: "Setting up Starlink, SpaceX's Satellite Internet"
slug: "setting-starlink-spacexs-satellite-internet"
date: 2021-04-09T15:01:19+00:00
drupal:
  nid: 3088
  path: /blog/2021/setting-starlink-spacexs-satellite-internet
  body_format: markdown
  redirects: []
tags:
  - broadband
  - internet
  - internet access
  - isp
  - satellite
  - spacex
  - starlink
---

{{< figure src="./starlink-dishy-and-box.jpg" alt="Starlink Dishy and box from SpaceX" width="700" height="394" class="insert-image" >}}

In March, I got an email from SpaceX saying Starlink was available at my address, and I could pre-order. I paid $500 for the equipment, plus $25 for a Volcano Roof Mount, and $99 for the first month of service, and a few weeks later, I got the kit you see in the image above.

I was a little too excited about getting Starlink, though, because I realized after I started looking for mounting locations that Starlink needed a 100° view of the northern sky, and my house is literally surrounded by 70-80 ft trees.

So I thought, why not let a cousin who lives out in a rural area try it out while I figure out what to do about mounting 'Dishy' (a common nickname for the Starlink satellite dish) on my own house?

After all, my cousin Annie, who lives in Jonesburg, MO, currently pays for the maximum available DSL plan to her farm ([Haarmann Farms](https://haarmannfarms.com)), and gets a measly 5 Mbps down, and 0.46 Mbps up—on a good day:

{{< figure src="./speed-test-rural-dsl-slow.jpg" alt="Rural DSL Slow Speed Test" width="700" height="394" class="insert-image" >}}

> **Video**: I have a full video outlining Starlink, an interview with Annie, and the unboxing and hardware setup process, on YouTube: [SpaceX's Starlink Internet - rural broadband GAME CHANGER](https://www.youtube.com/watch?v=U-VfAFj4jYw).

I asked her about her Internet options, and she said since her husband likes gaming, and she is on a lot of online video calls through the day (she works remotely for [Reputation](https://reputation.com)), costly satellite plans like HughesNet were not an option, due to their very high latency (since the satellites were in a very high geostationary orbit).

{{< figure src="./leo-meo-geostationary-orbit-diagram.jpg" alt="LEO MEO GEO geostationary satellite orbits around earth vs low earth orbit" width="700" height="394" class="insert-image" >}}

SpaceX aims to take away the stigmas associated with satellite Internet by launching _thousands_ of satellites into a much-closer (and thus lower-latency) Low Earth Orbit. There are some challenges and potential pitfalls associated with the building of an entire constellation of satellites so close to earth, and SpaceX is supposedly working with the space and astonomy communities to try to find solutions that prevent risk (e.g. [Kessler Syndrome](https://en.wikipedia.org/wiki/Kessler_syndrome)) and keep the skies clear for astonomy... and we'll see where that ends up in a few years' time.

But I went ahead and installed Dishy at my cousin's farm, and we plugged everything in to see if Starlink would connect:

{{< figure src="./setting-up-dishy-router-spacex.jpg" alt="Setting up the Starlink Router from SpaceX" width="700" height="394" class="insert-image" >}}

> Aside: The router design is as impractical as it is futuristic. The thing would fall over if you looked at it sideways, and the solitary LED on the front was hard to see unless in a dark room or looking closely, straight at it. Hopefully a 2nd iteration will be better!
> 
> At least the cables and PoE injector/switch provided feel rugged and better put-together. And I should mention the router runs OpenWRT, though it exposes precious few options to end-users.

After you plug in the gear, Dishy points straight up (turning into some sort of retro-futuristic side table... just don't put your drink on it!), then after finding a satellite, it aligns itself to a slight Northern inclination, so it can get the best signal. Inside Dishy is a flat PCB with an array of beam-forming antennas and a network SoC that controls everything about the connection. It's powered through PoE++ (using around 100W of power continuously), and has two motors inside to control tilt+rotation.

{{< figure src="./dishy-points-up-to-north.jpg" alt="Starlink Dishy satellite points north on a farm" width="700" height="394" class="insert-image" >}}

After a while, we saw brief moments with successful pings, and Starlink indicated a connection, but it was always brief, and the app would go back to 'Connecting...'. After a few minutes, this message appeared:

{{< figure src="./starlink-app-unexpected-rural-location.jpg" alt="Starlink App complains about location not being registered address" width="700" height="394" class="insert-image" >}}

Unfortunately, since Annie's farm was 60 miles (100 km) away from my house, she seemed to be outside my assigned 'cell' of coverage:

{{< figure src="./annie-is-100km-away-from-me.jpg" alt="Annie is 100 kilometers or 60 miles away from me as the crow flies" width="700" height="394" class="insert-image" >}}

I knew from reading some forum posts that Starlink dishes are assigned a cell for coverage, but I didn't know how big (or small!) the cell was. Apparently it's smaller than 60 miles.

So my next plan? Bring Dishy back home (after apologizing to Annie for getting her hopes up...), and find one spot on the back of the roof where _most_ of the Northern sky was visible—with some obstruction to the West:

{{< figure src="./jeff-on-roof.jpg" alt="jeff installing Dishy on his roof in St. Louis MO" width="600" height="338" class="insert-image" >}}

I have Starlink up and running, and have been using it for my mobile phone's WiFi all this week. I would love to give you my thoughts and a full review now, but for something as critical as Internet service, I don't feel like it would do any justice to try to cram a review in after less than a month of usage.

So I'm going to be uploading a video of the complete roof/house install process next week, and I am also monitoring the quality of the connection using a Raspberry Pi, along with my [internet-monitoring](https://github.com/geerlingguy/internet-monitoring) project.

So far (and remember, this is _not_ good data yet—only a few days' worth), I am seeing the following 24h average metrics:

  - Download: 106 Mbps
  - Upload: 16.1 Mbps
  - Ping: 40.58 ms

These numbers are well within expectations, and I think the connection's been perfectly adequate. There are only infrequent total dropouts right now (to be expected, IMO), and they usually last less than 30 seconds.

Most applications seem to handle them fine (e.g. on FaceTime video calls it just shows 'Poor connection' then picks right back up), but there are some mobile apps that need a relaunch to get their heads on straight again.

Subscribe to the blog and/or my YouTube channel for more updates—I'll be using and monitoring the connection over the next few months to give a well-informed opinion.
