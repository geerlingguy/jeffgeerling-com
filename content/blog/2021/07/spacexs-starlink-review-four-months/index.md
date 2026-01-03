---
nid: 3117
title: "SpaceX's Starlink Review - Four months in"
slug: "spacexs-starlink-review-four-months"
date: 2021-07-22T14:00:14+00:00
drupal:
  nid: 3117
  path: /blog/2021/spacexs-starlink-review-four-months
  body_format: markdown
  redirects: []
tags:
  - cable
  - internet
  - internet access
  - spacex
  - starlink
  - video
  - youtube
---

SpaceX's Starlink internet service uses satellites in low-earth orbit to provide high-speed Internet to underserved parts of the world, especially places without easy access to cable or fiber.

{{< figure src="./jeff-with-starlink-dishy-on-roof.jpg" alt="Jeff Geerling with SpaceX Starlink Dishy" width="550" height="379" class="insert-image" >}}

SpaceX's Starlink beta opened up in my area, so I installed Dishy—that's the nickname for the large white satellite dish above—and I've been testing it and comparing it to my Cable internet.

I have [Raspberry Pis monitoring my Internet](https://github.com/geerlingguy/internet-pi)—one on Starlink, and one on Spectrum. And I also have a power monitor measuring power usage. And I've tracked everything since day one to see if weather like snow and thunderstorms affect service, and how Starlink compares to Cable.

Here's the bottom line: Most of the time, I couldn't tell I was using Starlink. And that's good. Everything felt the same.

But that was _most_ of the time. I have _eight_ trees around my house, and there's literally nowhere I could put Dishy that allows it a full view of the sky with no 'obstructions'.

{{< figure src="./obstructions-starlink-app.jpg" alt="Starlink App Obstructions view" width="175" height="379" class="insert-image" >}}

Reality hits when I'd notice a page not loading. I'd open up the Starlink app and see "Obstructed." At my house, that happens for a minute or two, a few times per hour, because of the trees.

And as pictured above, a recent app update lets it show _exactly_ where the obstructions are. (Though it's estimation about the frequency is a bit off—I would have a very brief obstruction (< 10 seconds) every 5 minutes or so, and then a longer obstruction (20-40 seconds) every 10-20 minutes).

## Caveats

Before I get into the review, there are three MAJOR caveats:

  1. I live in a suburb outside a large city. Starlink isn't made for people like me who already have good Internet, but I plan on passing on Starlink to my cousin once it's available at her farm.
  2. If I had no other Internet options, I'd trim up my tree for a more reliable connection.
  3. Starlink is currently in beta, so reviews should be taken with a grain of salt. There are no guarantees, and a lot will change before it goes public.

If you want the whole story, and enjoy videos, here's the video I made for this review:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/spD4FLfi2a4" frameborder='0' allowfullscreen></iframe></div>
</div>

## Dishy - Starlink's terminal

First I'll talk about the Starlink Terminal, nicknamed 'Dishy McFlatface'. If you look at the guts inside the dish, it's a LOT different from a normal passive dish.

<p style="text-align: center;"><a href="https://www.youtube.com/watch?v=iOmdQnIlnRo">{{< figure src="./starlink-teardown-youtube.jpg" alt="Dishy internal Starlink antenna array" width="500" height="278" class="insert-image" >}}</a></p>

Dishy is more of a computer with a array of tiny antennae than a satellite dish. And that's the reason why the hardware currently costs $500—and SpaceX is actually losing money on every dish they sell!

[At Mobile World Congress](https://arstechnica.com/information-technology/2021/06/musk-aims-to-cut-starlink-user-terminal-price-from-500-to-as-low-as-250/), Elon Musk said the terminal costs SpaceX over $1000, but they're working on a new version that could be a little bit closer to $300—someday.

The dish uses dozens of antennae for _beam-forming_, to target a tiny satellite whizzing by in low earth orbit. Then the array locks onto another satellite, and another, and so on.

In addition to the complex antenna control, there's also a full modem and basically an entire little computer inside. COSIC, a research group in Belgium, [extracted the firmware from the dish](https://www.esat.kuleuven.be/cosic/blog/dumping-and-extracting-the-spacex-starlink-user-terminal-firmware/), and found it runs Linux on a 4-core System on a Chip.

And on top of all that, it also has a self-aiming mechanism that orients the dish at the right angle when you first turn it on.

For all its technical marvels, the dish has a few shortcomings.

The hard-wired 100' Cat6 Ethernet cable is _technically_ not supposed to be cut and reterminated. So installation and cable routing can be annoying, especially if you need more than 100' of cable.

And the dish gets fairly hot in use. Because it houses a computer and a lot of electronics, it has thermal limits that can cause issues in areas with extreme cold or extreme heat.

The recent heat wave in the US resulted in some Dishies [shutting down after they reached 122°F](https://arstechnica.com/information-technology/2021/06/starlink-dish-overheats-in-arizona-sun-knocking-user-offline-for-7-hours/) (50°C).

{{< figure src="./jeff-watering-dishy-on-roof.jpg" alt="Jeff Geerling waters Dishy on roof - Starlink Satellite Internet" width="626" height="352" class="insert-image" >}}

Some users watered Dishy to keep it cool, or raised it off the ground more. But luckily I haven't run into that issue yet.

I'll mention more about power consumption later, but during extreme cold, the dish has a sort of 'snow' mode where it heats up to melt off ice and snow. And in the one snow storm we got here in St. Louis, that's exactly what happened—with no Internet dropouts!

My dish survived four months of every type of weather St. Louis has to offer:

  - Two weeks of a record-breaking heat wave.
  - Four severe thunderstorms, with pea-sized hail and winds over 60 miles per hour.
  - A freak spring snow storm with a couple inches of snow in an hour.
  - And a few heavy rainfalls with more than 1" of rain per hour.

Dishy comes with a small tripod stand you could stake into the ground or onto a flat roof, but as I showed in my [Starlink roof install video](https://www.youtube.com/watch?v=ynsCVOz7jv4), I mounted it directly on my asphalt shingle roof using the volcano mount. There's also a flashing mount and pole adapters available, so you can mount it most anywhere.

A lot of people also ask how easy it is to move Dishy.

And... that's still an open question. Right now, Starlink is being rolled out slowly, by geographical 'cells', around select parts of the world. They can't roll it out everywhere because the satellite constellation is not yet complete, there aren't enough ground stations, and satellites can't communicate directly with each other, so each satellite has to be able to see both a ground station and your terminal to get a connection.

What this means is you couldn't just pick up Dishy and drop it anywhere and get service. Each Dishy is tied to a service address, and if you go more than few miles away, you might not get a connection. I tested this at my cousin's farm, 60 miles from my house, and while the dish could get a few bytes here and there, it wasn't giving any reliable signal.

SpaceX _does_ allow you to change the service address, but the the new address must be in a covered cell.

But until more infrastructure is built out and a new terminal is available, Starlink is definitely not going to be convenient for travel, like onboard RVs, airplanes, or boats.

## The Starlink Router

{{< figure src="./starlink-router.jpg" alt="SpaceX Starlink Router" width="498" height="413" class="insert-image" >}}

The other main piece of hardware you get with Starlink is this router. The router isn't anything to write home about, but at least it's a halfway-decent wireless and wired router.

I learned from [TurtleHerding's teardown](https://www.youtube.com/watch?v=ObCTB8ol3Ng) that the router runs on Qualcomm's IPQ4018 System on a Chip, which is _another_ 4-core ARM CPU, in addition to the one inside Dishy, and it runs a custom build of OpenWRT; you can even see the code SpaceX uses to build the router software—well, at least most of it—[on GitHub](https://github.com/SpaceExplorationTechnologies/starlink-wifi)!

I haven't tried too hard to hack my way into it, but it was fun to see an [ASCII-art version of SpaceX's logo](https://twitter.com/geerlingguy/status/1395411868462854155) when I tried logging in over SSH. It even had this fun little quote as the banner:

{{< figure src="./ssh-into-starlink-router.jpg" alt="SSH into Starlink Router - ASCII Art Logo of SpaceX and Bee Movie Quote" width="388" height="325" class="insert-image" >}}

For the astute reader, the quote is a variation on a line from Bee Movie.

While I was in that deep, I checked [one hop further](https://www.reddit.com/r/Starlink/comments/mrshrt/easter_egg/guqj4e0/?utm_source=reddit&utm_medium=web2x&context=3), and tried to access what's presumably the Starlink base station, and got this lovely rendition of the Nyan Cat:

{{< figure src="./ssh-into-starlink-base-station.jpg" alt="SSH into Starlink Base Station - Nyan Cat" width="413" height="325" class="insert-image" >}}

Jokes aside, the best way to configure Starlink is through the mobile App. If you visit `192.168.100.1` in your browser, you can access some features, like stowing dishy, restarting the router, and seeing connection stats, but that's about it.

But the mobile app has all the functionality on the web, and then some: once you sign in, you can manage the WiFi network name, separate the 2.4 and 5 GHz networks, and access all the Starlink support FAQs.

The router isn't complicated, which is a blessing and a curse. You can't get a static IPv4 address, if that's something you care about, since Starlink uses [CGNAT](https://en.wikipedia.org/wiki/Carrier-grade_NAT), but VPNs do work. And you technically can get a static routable IPv6 address if you use your own router and toss out Starlink's, but that's not something the average user would care about.

I should also note that a lot of these things have changed since I first started using the beta.

I'm happy with the router's simplicity, and also happy you can use your own if you want. But from a hardware standpoint, there are two major downsides:

  1. There's only one gigabit network port on the back, so you'd need a switch to plug in more than one wired device.
  2. The router is very top-heavy. I don't know _how_ many times I've accidentally knocked it over. It got annoying enough I [3D printed this base](https://www.thingiverse.com/thing:4855254) to keep it standing up.

## Power Consumption

{{< figure src="./starlink-dishy-poe-power-supply.jpg" alt="Starlink Dishy Power Supply PoE++" width="577" height="356" class="insert-image" >}}

The hefty power supply has no problem staying put. Inside this black brick is an understated two-port PoE++ switch, capable of supplying over 100W to Dishy!

It also powers the router via PoE, so you don't have to have an extra wall wart AC adapter plugged in for the router.

This high power rating means it's doubly important to use the right cabling, especially for Dishy. If you splice Dishy's wire, use Cat6A or better cable, and keep the run less than 100', otherwise the power to the Dish might not be adequate, or you could even overheat Dishy's cable!

I wanted to see just how much power Starlink uses, especially since people have asked how well it would work off-grid with solar or battery power, and the results were surprising.

{{< figure src="./shelly-plug-us_0.jpg" alt="Shelly Plug US in UPS" width="551" height="354" class="insert-image" >}}

I popped a [Shelly Plug](https://shelly.cloud/products/shelly-plug-us-smart-home-automation-device/) into my UPS that sends power usage data over my network, then set up my Raspberry Pi to track Starlink's power consumption, and I've been monitoring since day one.

{{< figure src="./dishy-power-consumption-100w-avg.jpg" alt="Starlink Dishy Power Consumption 100W average" width="700" height="394" class="insert-image" >}}

The dish plus the router consumes almost 100W of power, all day long. Compare that to the 5-10 Watts my cable modem and ASUS router consume, and it's definitely something to consider.

The other thing that surprised me was what happened on April 21 this year. We had a freak late-spring snowstorm with a few inches of snow falling in a short period of time.

{{< figure src="./dishy-snow-power-graph.jpg" alt="Starlink Dishy power usage graph during a snow storm" width="600" height="419" class="insert-image" >}}

During the heavy snowfall, Dishy quickly spiked up to 125W, peaking at 175W towards the end of the snowstorm.

According to support, Dishy has a kind of 'snow mode', where it heats itself up enough to melt snow off the top, and it seems like it automatically goes into that mode when snow starts obstructing the sky.

Dishy consumes a lot of power. If you want to run off solar power, adding an extra 90-plus watts to your load isn't nothing. Other satellite-based Internet providers use a bit of energy too, but Starlink is in a league of its own.

> Starlink's 2.4 kWh of daily power consumption means running Starlink 24x7 would cost around $10 a month, on average, in the USA. That's about the same as a modern mid-size refrigerator.

## Performance - subjective

Starlink is worth that extra energy consumption if it performs, though.

And I'm splitting this part of my review into two sections: subjective, and objective. You don't need me to tell you that I can make FaceTime calls, play Halo, manage my open source projects, and watch YouTube all day.

Because that's about it, subjectively-speaking. It's boring, because Starlink is basically what I'm used to: A mostly-online high speed Internet connection.

But what's boring to me is revolutionary to some people. My cousin, whose house I visited earlier this year, gets _5 Mbps_ of download bandwidth, and less than 1 Mbps up. Having 20x faster Internet is life-changing for someone with a low-quality Internet connection.

The one thing that wasn't always pleasant was how some software handled dropouts, especially some streaming platforms and video conferencing apps. Since that happens a couple times an hour at my house, I would have to call someone back, or refresh a page and watch an ad again to get back into a stream.

Most well-known apps like Netflix, FaceTime, and Zoom, handled things well without any incident. It was really the apps and services that are obviously outsourced, like poorly-made TV network apps, that would have strange issues requiring a relaunch.

Subjectively, I really like Starlink. I've been able to leave my iPhone and iPad connected only through Starlink, and I hardly ever notice the obstructions.

The dropouts have gotten less frequent, too, as SpaceX launches more satellites (which means more sky coverage), and has updated Dishy's software to be better at switching between satellites.

## Performance - objective

But how does Starlink _really_ perform? I covered in detail how I [use Raspberry Pis to monitor my Internet](/blog/2021/monitor-your-internet-raspberry-pi). I wanted raw numbers with lots of data over time, so I could form a solid opinion about Starlink.

{{< figure src="./starlink-monitor-raspberry-pi.jpg" alt="Starlink Monitor Raspberry Pi 4 model B in a Rack with PoE" width="600" height="367" class="insert-image" >}}

So I've been running this Raspberry Pi since the day I installed Starlink, and every 30 minutes, it runs a Speedtest, and charts the result. It also checks for latency, and tracks all of Starlink's own statistics, thanks to some [code from Dan Willcocks](https://github.com/danopstech/starlink_exporter)!

{{< figure src="./starlink-metrics.jpg" alt="Starlink Metrics monitored by Internet Pi Monitoring project" width="700" height="394" class="insert-image" >}}

On average, over the past few months, I've gotten about 150 Mbps down, and 20 Mbps up, with 40 ms of latency.

I could get peak download speeds just over 300 Mbps, and peak upload of around 30 Mbps, and according to Elon, [ping times could someday be as low as 20 milliseconds](https://twitter.com/elonmusk/status/1415480145830465539), but I'm more interested in what I can measure _right now_.

So how does Starlink do against my cable connection?

{{< figure src="./starlink-vs-cable.png" alt="Starlink vs Cable Internet speeds and latency ping time" width="700" height="394" class="insert-image" >}}

(The results above were an average for an entire 7-day period.) It's not a fair fight, since Starlink isn't made to compete against urban Cable Internet, but then again, I _do_ pay 1.5 times more for Cable, and while it gives me a lot faster downloads, it's only a tiny bit faster on the upload speeds, in terms of the upload:download ratio.

{{< figure src="./starlink-vs-cable-latency.png" alt="Starlink vs Cable Internet latency or jitter HTTP response time graph" width="700" height="394" class="insert-image" >}}

The best measure of how it _feels_, though, is jitter, and using the Request Duration graph, it's easy to see there's more jitter, or variation in the response times, from Starlink. But it's not as bad as I thought it would be.

If I were a competitive gamer, or was trying to livestream something important, I wouldn't rely on Starlink just yet. I [did a full livestream](https://www.youtube.com/watch?v=Xx4s02w4kgA) on my unstable prone-to-obstruction connection... and it worked! But there were some blank spots during dropouts and times when YouTube knocked down the bitrate.

How about comparing Starlink to my cousin's DSL on the farm?

{{< figure src="./starlink-vs-rural-dsl.png" alt="Starlink vs Rural DSL speeds" width="700" height="394" class="insert-image" >}}

Starlink comes out way better there, since the DSL connection is a paltry 6 Mbps down, and .5 up! 150 down with 15 up, it's not even a competition!

## Starlink Pricing and Contract

The last thing I'll mention is the price and contract. Right now, the basic Starlink kit is $500, and the service costs $99 a month. Most people will need another $100-200 worth of mounting gear, and if you want it professionally installed, expect to pay a few hundred more.

But the contract is straightforward, which is usually _not_ the case with ISPs in America: unlimited data, with [supposedly no plans to add data caps](https://www.reddit.com/r/Starlink/comments/jybmgn/we_are_the_starlink_team_ask_us_anything/gd3x2l8/), and no hidden fees or early termination charges.

You can cancel any time with a support ticket, and the main catch with the service right now is the fact it's a beta, so SpaceX doesn't really have to guarantee any level of service, and the network can temporarily turn go offline at any time for any reason.

## Drawbacks to Starlink

Before I wrap up, there are two major issues some people have with Starlink, and really any low-earth constellation like it, and that's it's impact on earth-based astronomy, and it's potential to increase the risk of the [Kessler syndrome](https://en.wikipedia.org/wiki/Kessler_syndrome), a catastrophic increase in space debris.

But for both issues, SpaceX has been working to mitigate the risks—as much as they can. See my [first Starlink video](https://www.youtube.com/watch?v=U-VfAFj4jYw) for a deeper discussion of both issues, and follow the news for updates on both—it seems like every month there's a new development in these areas.

And with the potential of Amazon launching their own low-earth-orbit [Kuiper system](https://www.amazon.jobs/en/teams/projectkuiper), these issues must be dealt with, because even if the risk is managed, things that happen in orbit affect the entire planet, not just the USA.

## Verdict

My hope is that any satellite-based Internet can be as open and inexpensive as possible, to give people equal access to high-speed Internet, no matter where they live or work.

To sum up my review, I really like, but don't _love_ Starlink. At the beginning, I had thoughts of switching to Starlink and ditching my cable ISP, just because how poorly they've treated me as their customer over the years. And Starlink performed well, and their support has been great...

But the performance just isn't where I need it _for what I do_. If I didn't have decent cable Internet, like my cousin, that'd be a different story. And judging by many people's reaction to getting Starlink, it can be life-changing.

The nice thing is, for now I have two Internet connections at my house, and I'm going to aggregate them so I can get more than 50 Megabits of upload speed. At least when my maple tree isn't standing in the way!
