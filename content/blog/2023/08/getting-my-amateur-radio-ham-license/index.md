---
nid: 3307
title: "Getting my amateur radio (ham) license"
slug: "getting-my-amateur-radio-ham-license"
date: 2023-08-30T14:28:53+00:00
drupal:
  nid: 3307
  path: /blog/2023/getting-my-amateur-radio-ham-license
  body_format: markdown
  redirects:
    - /blog/2023/getting-amateur-radio-ham-license
aliases:
  - /blog/2023/getting-amateur-radio-ham-license
tags: []
---

After four decades in the broadcast radio industry, I finally convinced my Dad to join me in getting an amateur radio license this summer.

In the US, there's a huge community of amateur radio operators, or 'Hams' for short. There's a whole history to how they got that name, but to me, radio's a lot of black magic.

Throw on top of that the fact that Hams are always slinging around weird terms like QRT, using morse code—or as they call it, CW—and they call themselves weird things like [NK7U](https://www.qrz.com/db/NK7U)!

But we cut through all that jargon and learned the basics—well, I did. My Dad went the 'Extra' mile and ran through all three tests, relying on his 40 years of radio experience! We both have licenses now (I'm KFØMYB, and my Dad's KFØMYJ) and made our first contact. Here's a video documenting that entire journey (up to the point I sent out my first [QSL card](https://en.wikipedia.org/wiki/QSL_card)!):

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/PIeavEhUhSw" frameborder='0' allowfullscreen></iframe></div>
</div>

I'll leave it to the video to document our journey (starting about halfway through), but will talk a little more about amateur radio here:

Agencies like the FCC in the US police the airwaves.

We have FM radio here, and _technically_ there's nothing preventing me from grabbing [a little 15W transmitter I bought on Amazon](https://amzn.to/44zqfSd) and broadcasting my _own_ signal over another station.

But that's not legal. Even if there isn't a station broadcasting on a certain frequency, I can't just turn on my own transmitter, that's called _pirate radio_, and while that sounds cool, it can create a lot of headaches.

In the US, we have licenses for radio operators because the idea is people who know what they're doing can _use the radio waves responsibly_. A licensed Ham wouldn't blast out a bunch of noise and interfere with other people's signals (well, at least not intentionally!).

Hams even help in emergencies, when other communications are down. There's the [SKYWARN program](https://www.weather.gov/oun/amateurradio) supporting weather forecasters when there are big storms. There's [ARES](http://arrl.org/ares), the Amateur Radio Emergency Service, a bunch of volunteer Hams who help when disaster strikes.

And a lot of advancements in radio, from antenna design, to digital communication protocols, come out of the Ham community.

There are three levels of Ham operators in the US: 'Technician', 'General', and 'Extra'. Basically, as you skill up, you get access to more frequencies.

And the more frequencies, the more chance you have to do long distance and experimental communication. Like did you know you can bounce a radio signal off the moon from your own backyard? Or there's a ham radio setup on the ISS, whizzing overhead! That thing's called ARISS, or Amateur Radio on the ISS, and it lets you [talk directly to astronauts in space](https://youtu.be/NLFCK5_ouiA?t=151)!

To say radio offers a ton of fertile ground for learning for a couple guys who love tech is an understatement.

## Strange things about Ham Radio

And it's not all deep science, either. Ham radio has all kinds of fun quirks to it.

Like did you know it's illegal to broadcast _music_ over amateur radio bands? Well, except _maybe_ [if you sing Happy Birthday directly to another Ham](https://ham.stackexchange.com/a/367/24057).

On the topic of illegal things: you can't do any business on amateur bands, and what about swearing? **** no! Not allowed.

And what if one of my Dad's radio stations has a transmitter that breaks down. Could you switch to broadcasting on an amateur frequency temporarily? No! Well, unless doing so would prevent harm to humans in immediate danger or for the protection of property.

Ham radio has a ton of fascinating history, and the community is probably smaller today with how ubiquitous the Internet is, but it's still ripe for advancing the science and wonder of RF.

## Studying / Preparing

{{< figure src="./ham-radio-technician-manual.jpg" alt="Ham radio license manual" width="700" height="394" class="insert-image" >}}

Studying for my exam was actually quite daunting for me. I do software development, and I know my way around code. I also know the basics of electronics.

But take a look at a map like [this](https://aprs.fi/#!lat=38.6287&lng=-90.1988). This is a map of the [APRS](http://www.aprs.org), the Automatic Packet Reporting System. Hams eat this stuff up, but what does any of this mean?

{{< figure src="./aprs-st-louis-mo.jpg" alt="APRS map of St. Louis MO" width="700" height="394" class="insert-image" >}}

I know from meteorology that WX means weather, and if I click on one of those, it looks like a little weather station. So that's cool. But if I click on one of the towers... R60m? antenna HAAT 80ft? C141.3? What does all _that_ mean?

It means a lot. And the Ham community communicates a _lot_ of info in a _tiny_ amount of space.

That was borne out of necessity back in the day, because communication was slow and limited early on, but all that terminology stuck. So studying is really important, if you wanna pass the exam and become a Ham.

{{< figure src="./jeff-and-joe-geerling-ham-radio-handheld.jpg" alt="Jeff and Joe Geerling holding handheld amateur radios" width="700" height="394" class="insert-image" >}}

And now I have a beginner Technician license, and will work my way up to General after some time. My Dad's already an Extra, so maybe we can work on an [EME/moonbounce](https://help.remotehamradio.com/help/eme-operation-moonbounce) sometime!

There are definitely many possibilities to explore with digital mode, SDR, and Raspberry Pis, too!
