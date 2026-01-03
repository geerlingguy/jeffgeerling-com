---
nid: 3453
title: "I won't connect my dishwasher to your stupid cloud"
slug: "i-wont-connect-my-dishwasher-your-stupid-cloud"
date: 2025-03-24T16:47:52+00:00
drupal:
  nid: 3453
  path: /blog/2025/i-wont-connect-my-dishwasher-your-stupid-cloud
  body_format: markdown
  redirects: []
tags:
  - apps
  - bosch
  - cloud
  - dishwasher
  - home
  - internet of things
  - iot
  - kitchen
  - security
---

This weekend I had to buy a new dishwasher because our old GE died.

I bought a Bosch 500 series because that's what Consumer Reports recommended, and more importantly, I could find one in stock.

{{< figure src="./bosch-dishwasher-open.jpg" alt="Bosch dishwasher open control panel" width="700" height="394" class="insert-image" >}}

After my dad and I got it installed, I went to run a rinse cycle, only to find that _that_, along with features like delayed start and eco mode, require an app.

{{< figure src="./bosch-dishwasher-home-connect.jpg" alt="Bosch dishwasher Home Connect logo" width="700" height="394" class="insert-image" >}}

Not only that, to _use_ the app, you have to connect your dishwasher to WiFi, set up a cloud account in something called Home Connect, and then, and only then, can you start using all the features on the dishwasher.

## Video

This blog post is a lightly-edited transcript of my latest YouTube video on <a href="https://www.youtube.com/@Level2Jeff">Level 2 Jeff</a>:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/5M_hmwBBPnc" frameborder='0' allowfullscreen></iframe></div>
</div>

## GE Dishwasher - Planned Obsolescence

So getting back first to that old GE dishwasher, it was, I don't know, I think that [planned obsolescence](https://en.wikipedia.org/wiki/Planned_obsolescence) is something that applies to many consumer products today.

Companies know if they design something to last only 5 or 10 years, that means in 5 or 10 years someone's going to have to buy a whole new one.

And on my GE Amana dishwasher, it started having weird power issues, like the controls would just not light up unless I reset the circuit breaker for a few minutes. That started happening more often, and this past Saturday it just wouldn't come on no matter what, even after I tested and re-wired it all the way from the panel up to the dishwasher's internal power connector.

So it was dead.

Next up, I looked at what it took to get a control board. Well... [$299 for a control board](https://www.repairclinic.com/PartDetail/Control-Board/WD21X24901C/4980378) that was 'special order' and might not even fix the problem? That's a non-starter for my $600, 8-year-old dishwasher.

Even if I got it fixed, the front panel was starting to rust out at the hinge points (leaving some metal jaggies that my soon-to-be-crawling 6 month old could slice his fingers on), and other parts of the machine were showing signs of rust/potential future leaks...

It was Saturday night, and for a family of five, a dishwasher is kinda important. We don't have 1.5 hours every night to spend hand-washing dishes (not to mention the water bill!).

So I needed to get a new one, and it's really hard for me to schedule a few hours for my Dad and I to get it done in the middle of the week (plus that's multiple days without a dishwasher!).

So I did some research, and I found Bosch _seemed_ to have the best bet for under $1,000, available locally on a Sunday.

Consumer Reports, random Redditors, etc. seemed to have some praises for Bosch—on Reddit many also praised Miele, but I couldn't find any of those available locally. And Consumer Reports especially praised _all_ the Bosch units, with them topping all their reliability and customer satisfaction charts!

I remembered five or ten years ago, whenever I had bought my old GE, I remembered Bosch topped the charts too, but back then I settled for GE to save a few bucks...

## Installation was (mostly) great!

So I spent a little more this time, hoping for a better experience. And installation was actually great—it was a lot easier to install the Bosch than it was that the GE.

It has a plastic base that slides better on the floor, and there's easier routing of the drain hose, inlet hose, and power wire that makes it less risky when you're pushing the thing into the blind cutout under the counter.

The one weird thing was that whoever like tightened the feet on the bottom at the factory must've used an impact driver or something because they were all practically embedded, and wouldn't budge.

I was turning the little screw on the front that pushes the rear foot down through a little gearing, but the worm gear slipped out and kinda shoved the long rod that connects the front to the back out of place. I had to buy a 10mm hex socket to wiggle the foot loose enough the gearing would actually work.

But once that was done, the rest of the install was seamless. (Thanks especially to some help from my Dad).

## First use, encountering the Cloud requirement

So I turned it on, and immediately hated the new touch sensor stuff on it.

The old GE had buttons: you press them in, they click and you know that you pressed a button.

The touch sensor, you kind of touch it and the firmware—like this new dishwasher actually takes time to boot up! I had to reset it like three times and my wife meanwhile was like laughing at me like look at this guy who does tech stuff and he can't even figure out how to change the cycle on it.

That took about five minutes, sadly.

But eventually I pulled out the manual book because I was like... "this is actually confusing."

It should be like: I touch the button and it changes to that mode! But that was not how it was working.

I wanted to run just a rinse cycle to make sure the water would go in, the water would pump out through the sump, and everything worked post-install.

But I couldn't find a way to do a rinse cycle on the control panel.

So I looked in the manual and found this note:

{{< figure src="./bosch-dishwasher-manual-features-home-connect.jpg" alt="Bosch dishwasher manual mention of Home Connect" width="700" height="394" class="insert-image" >}}

It says options with an asterisk—including Rinse, Machine Care (self-cleaning), HalfLoad, Eco, and Delay start, are "available through Home Connect app only and depending on your model."

The 500 series model I bought isn't premium enough to feature a 7-segment display like the $400-more-expensive _800_ series, so these fancy modes are hidden behind an app and cloud service.

I was like, "Okay, I'll look up this app and see if I can use it over Bluetooth or locally or whatever."

Nope! To use the app, you have to connect your _dishwasher_ to your _Wi-Fi_, which lets the dishwasher reach out on the internet to this Home Connect service.

You have to set up an account on Home Connect, set up the Home Connect app on your phone, and _then_ you can control your dishwasher _through the Internet_ to run a rinse cycle.

That doesn't make any sense to me.

An app? I mean, I can understand maybe adding some neat convenience features for those _who want them_. Like on my new fridge—which I chose not to connect to WiFI—it has an app that would allow me to monitor the inside temperature or look up service codes more easily. If I wanted those add-on features, which my old fridge didn't have, I could get them.

But requiring an app to access features that _used_ to be controllable via buttons on the dishwasher itself—or _are still_ if you pay $400 more for the fancy "800" model? That's _no bueno_.

## What can I do?

Well, first of all, I could just not use those features. That's kind of annoying because I bought it with the assumption that I could run the cleaning cycle, that I could run the rinse cycle without having to have an app and Wi-Fi.

Another option is I could just connect it to my Wi-Fi, maybe on an IoT VLAN.

But it's not like a video doorbell, where an Internet connection adds on functionality, like being able to see who rang while you're on vacation, or storing security footage clips on the cloud so you have them available even after someone robs your house...

But a dishwasher... I'm not going to remote control my dishwasher and like, run an extra rinse cycle while I'm on a beach somewhere.

I don't need Internet on my dishwasher.

Another _third_ option is somebody has reverse engineered this protocol and built [HCPY](https://github.com/osresearch/hcpy), a Home Connect Python library.

But here's the problem: I already spent like four hours getting this dishwasher installed in my kitchen. I don't want to spend another four hours configuring my own web UI for it—which still requires at least a one-time connection through Home Connect!—and maintaining that as a service on my local network, relying on an unauthorized third party library using reverse-engineering to get at the private dishwasher API!

## What can _we_ do?

I don't think we should let vendors get away with this stuff.

First, it lets product designers get lazy.

A feature like a little display, a little seven segment display that can show like two letters and a number of minutes remaining or something like that... How much does that cost?

How hard is it to integrate that into every model, even the cheap ones?

A lot of cheap dishwashers actually _have_ those things, but not Bosch!

With Bosch, you have to pay $400 for the privilege of a little display!

Second, this might be a little bit conspiracy theory or whatever, but it feels like it's part of planned obsolescence. Just like with the GE, where a lot of parts are designed to rust out after 5 or 10 years.

If you have a cloud app, that means there's a cloud service that has to be running. That costs money to maintain.

And if there's no subscription fee right now, that means one of two things:

  1. They could be selling our data already.
  2. At some point, they'll either close the service because it's a cost center (so the rinse cycle and eco mode on all these dishwashers just goes "POOF!"), _or_ they're going move to a subscription model.

All of a sudden, if you want to run the self-cleaning cycle, you better start paying five bucks to Bosch every month. _Forever_.

That's insane.

Third, it's a security hole in your local network.

Bosch might be a _little_ better than some no-name light bulb company making IoT light bulbs on Amazon, but only a little.

I don't want to have Bosch having full internet access on my local network.

Their API would be able to talk back to my dishwasher, and the dishwasher—unless I put it on a VLAN, which 99% of consumers have no clue how to do that...

That's just something that shouldn't have to happen.

This is a dishwasher!

I don't know.

## What _should_ be done?

When I posted on social media about this, a lot of people told me to return it.

But I spent four hours installing this thing built into my kitchen.

I hooked it up to the water, it's running through cycles... it _is_ working. I'll give them that. It does the normal stuff, but you know, there are some features that don't work without the app.

At a minimum, I think what Bosch should do is make it so that the dishwasher can be accessed locally with no requirement for a cloud account. (Really, it'd be even better to have all the functions accessible on the control panel!)

Anyone building an IoT device, here is my consumer-first, e-waste-reduction maxim:

> **First local, _then_ cloud.**

Cloud should be an add-on.

It should be a convenience for people who don't know how to do things like connect to their dishwasher with an app locally.

And it's not _that_ hard.

A little ESP32, a little $1 chip that you can put in there could do all this stuff locally with no cloud requirement at all.

I think that there might be some quants or people who want to make a lot of money building all these cloud services.

I don't think that it's people who are consumer-first and eco-conscious because if they were, they would give _us_ control first and _then_ add on 'nice' quality of life features through a cloud service.

With my Bosch 500 series dishwasher, I was excited after the easy install (besides those leveling feet), then was let down _so hard_ once I found out I couldn't use all the features it came with.
