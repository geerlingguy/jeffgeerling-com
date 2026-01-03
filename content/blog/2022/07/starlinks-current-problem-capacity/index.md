---
nid: 3224
title: "Starlink's current problem is capacity"
slug: "starlinks-current-problem-capacity"
date: 2022-07-27T14:02:42+00:00
drupal:
  nid: 3224
  path: /blog/2022/starlinks-current-problem-capacity
  body_format: markdown
  redirects: []
tags:
  - internet
  - isp
  - satellite
  - spacex
  - starlink
  - video
  - youtube
---

This blog post is a lightly edited transcript from my most recent YouTube video, in which I explain some of Starlink's growing pains: slower speeds due to oversubscription, design challenges with their v2 hardware, and a major bet on much larger v2 sats and a rocket (Starship) that has yet to complete an orbital flight.

The video is embedded below, and the transcript follows:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class="embed-container"><iframe src="https://www.youtube.com/embed/6-q1fcOa8P4" frameborder="0" allowfullscreen=""></iframe></div>
</div>

I got Starlink during the Public beta, a little over a year ago.

I set up Dishy on my roof, I set up some advanced monitoring and tested it as a backup Internet connection, but ultimately passed it along to my cousin, who's using it on her farm.

## Performance and Oversubscription

{{< figure src="./starlink-speeds-grafana.jpg" alt="Starlink Speeds monitored in Grafana" width="700" height="394" class="insert-image" >}}

When I first got Starlink, I was getting speeds above 100 Mbps down, and 15 up. But now? My cousin's consistently getting lower speeds, about half what I got last year. It's not bad _at all_ compared to her old DSL, which had upload speeds in the _Kbps_ and cost about the same as Starlink.

But it _is_ less. And that seems to be a universal issue for Starlink's early adopters, at least in the US. [People are experiencing slower speeds](https://starlinkstatus.space) as the satellites and ground stations get more saturated.

But that's to be expected. Starlink likely has [500,000 customers now](https://twitter.com/elonmusk/status/1493358044989767683), and [SpaceX is currently making 20,000 new terminals per week](https://www.reddit.com/r/Starlink/comments/v9ad72/20000_terminals_manufactured_each_week/).

The day after I posted my last Starlink video, SpaceX announced official roaming support—users could officially move their Starlink Terminal to locations away from their service address. And just this month, the FCC approved [dishes in motion](https://arstechnica.com/tech-policy/2022/07/spacex-gets-fcc-approval-for-starlink-on-moving-vehicles-ships-and-aircraft/).

The privilege of roaming comes with a fee—$25 a month. But this created a bit of a loophole for people who live in places where [Starlink isn't currently available, but has coverage](http://starlink.com/map). People are buying Starlink at one address, turning on roaming, then using it at a different address in a cell that's already full.

And what problem does that create? Oversubscription.

[Capacity is SpaceX's number one challenge](https://www.pcmag.com/news/starlinks-massive-growth-results-in-congestion-slow-speeds-for-some-users), and it'll still be a challenge with tens of thousands of satellites up in the air. Because despite laser links, more ground stations, and better software, physics just can't be beat—at least not in any short term time-scale.

There are tons of reports of Starlink users who _aren't_ roaming, but they're getting lower speeds and higher latency:

  - [Example 1](https://www.reddit.com/r/Starlink/comments/v21m6f/quantitative_data_on_my_download_performance/)
  - [Example 2](https://www.reddit.com/r/Starlink/comments/uib72d/its_not_all_sunshine_and_happiness_with_starlink/)
  - [Example 3](https://www.reddit.com/r/Starlink/comments/v1axb3/seriously_starlink_wtf/)

And sure, SpaceX has some toggles to deprioritize traffic for roaming users, but all networking equipment has capacity limits. Once you reach a certain number of connected devices, performance drops off for _everyone_.

Elon Musk even acknowledged the problem:

<blockquote class="twitter-tweet" data-dnt="true" data-theme="dark"><p lang="en" dir="ltr">The Bay Area is already saturated with user terminals, which is why wait time for a terminal is long. <br><br>Rush hour speeds will improve as more satellites reach operational orbits, with a giant improvement with V2 sats. <br><br>Note, speeds outside of rush hour times should be very high.</p>— Elon Musk (@elonmusk) <a href="https://twitter.com/elonmusk/status/1535461608889241600?ref_src=twsrc%5Etfw">June 11, 2022</a></blockquote> <script async="" src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

We'll get to v2 sats later.

My best guess is in really popular areas, or travel destinations where lots of RV users congregate, Starlink performance might be a lot less than the 100+ Mbps I was originally getting—at least for now.

_Even with_ slower speeds, for many customers, it's such an improvement over what they had before, _they don't care_. [This Reddit user](https://www.reddit.com/r/Starlink/comments/ul46ir/dishy_mountain_camping_zero_cell_service_testing/) is perfectly happy getting 30 Mbps.

And for every rant over on Reddit, there are probably a dozen more happy customers like [this one from Western Colorado](https://www.reddit.com/r/Starlink/comments/viw7eo/starlink_sometimes_gets_a_worse_rap_than_it/), who don't see performance issues at all.

## Roaming and Preorders

Outside speeds, I'm a little disappointed with a couple other things.

People who preordered years ago are often still waiting, while people who buy with roaming at a different address can cut in line. Sadly, outside of disabling roaming, there's not a whole lot Starlink can do. The saying is cheaters never prosper... but in the case of getting Starlink sooner, they _do_.

## The new router

{{< figure src="./starlink-new-v2-router-orbit-diagram.jpg" alt="Starlink's new v2 router with mars earth transfer orbit" width="212" height="296" class="insert-image" >}}

Also, remember how the new Starlink router [doesn't have Ethernet built-in](https://spaceexplored.com/2021/11/11/spacex-launches-new-starlink-user-terminal-router-loses-ethernet/), so you have to buy a separate accessory just to get a LAN port?

I didn't notice at first, but it's _also_ missing a visible _status light_! Unless you pick it up, the only thing you'll see on it is a [picture of the Earth to Mars transfer orbit](https://www.reddit.com/r/Starlink/comments/v2gode/lights_are_the_lights_on_the_front_faceplate/). To even see if it has power, you have to [pick it up and look at the status LED _on the bottom_](https://www.reddit.com/r/Starlink_Support/comments/ru0fgy/router_lights/)!

Status LEDs are step 1 in diagnosing any problem. The posts linked above are proof you shouldn't take away literally the only indication if something is working or not.

Even though the old router fell over if you looked at it wrong, at least it had a status LED. And a network jack!

While we're on the topic: some users are [building their _own_ PoE boards for the router](https://www.reddit.com/r/Starlink/comments/vdssbb/a_friend_created_these_custom_starlink_poe/). Kudos to them, but if Starlink used more standard connections, you wouldn't have to do it at all.

## Firmware hell

Another fun 'feature' I was reading about recently is Starlink's inability to run local firmware updates. [If you stow your dish too long](https://www.reddit.com/r/Starlink/comments/v20amw/im_desperate_pls_help_me_get_back_online_after_a/), [there's a chance it'll never connect again](https://www.reddit.com/r/Starlink/comments/uw0p2x/support_told_me_to_throw_away_my_working_but_out/). And Starlink support will tell you there's nothing you can do about it!

There's a wired router—surely Starlink could build in a local firmware update mechanism, right?

Firmware updates are electronics design 101. It's ridiculous the answer to someone storing their dish for too long is "throw it away!", especially when the hardware costs thousands of dollars to manufacture!

## Starlink support

That's all assuming you get a response from Starlink support in the first place.

Now, let me be clear: every support rep I've worked with has been awesome, but there are _not enough support reps_!

[Users have reported delays up to a _month_](https://www.reddit.com/r/Starlink/comments/uu233g/no_internet_for_27_days_no_response_from_support/) before they get a response! That's not acceptable.

He'll never see this, but Elon: [spend less time choreographing dancing robots](https://www.youtube.com/watch?v=TsNc4nEX3c4), and focus on your users. They still love Starlink, but it's like you're trying to make them hate it!

## Refurbished dishes

I can't verify this, but [it _seems_ some users are getting refurbished or used Starlink terminals](https://www.reddit.com/r/Starlink/comments/vfhupo/16_months_and_550_later_i_receive_a_busted_up_box/).

It would be _good_ for SpaceX to sell refurbished gear. That's less e-waste, it's good for users since existing gear can be reused... but if they do it, they _have_ to tell the customer.

A lot of customers would be perfectly fine getting a used terminal instead of a brand new one. But if it's refurbished, SpaceX has to be upfront about it.

## Starlink Business and V2 Sats

Starlink also launched [Starlink for _Business_](https://www.starlink.com/business) recently. You pay about 5x as much for a better dish and about twice the performance.

But I can't really judge the business plan yet. As far as I've seen, [this video from tabGeeks](https://www.youtube.com/watch?v=UeCuYkRpOmc) is one of the first installs with the actual square dish, and that video didn't really have any performance data, so I'm waiting to see how Starlink Business pans out.

{{< figure src="./starlink-sat-v2-starship.jpg" alt="Starlink v2 Satellite production Starlink pez dispenser" width="700" height="394" class="insert-image" >}}

And how about those fabled Gen 2 satellites, that are supposed to solve many of the performance problems with Starlink? Well, [they're about _five times heavier_](https://gizmodo.com/spacex-elon-musk-starlink-satellites-starlink-2-0-1848995490) than the original sats.

Because of that, they can't be launched on a Falcon 9. SpaceX is betting Starlink's future on a Gen 2 satellite that hasn't been tested in orbit, and it requires a rocket—the Starship—that hasn't even launched yet.

I _do_ think Starship will launch—but there are definite concerns over the Gen 2 satellites.

SpaceX's original goal was to launch tens of thousands of V1 sats. People rightly worried about short-term effects of a satellite collision or unplanned deorbits. Some of those concerns were overblown, but that was with a 500 lb satellite.

What happens if a few of these 1.2-ton satellites break up? The orbit will decay, but can SpaceX guarantee it'll still burn up before it hits the ground? How will they prevent at least short-term issues in their current LEO orbital plane in the case of a collision?

A lot of Starlink's future rides on the combined success of both Starship and the V2 satellite. A lot has to go right to get both of those in orbit quickly. Otherwise, Starlink's going to suffer from performance problems _all the time_, not just during 'rush-hours'.

## Better but not great

[Starlink is NOT in beta anymore](https://www.pcmag.com/news/starlink-website-nixes-beta-wording-warns-chip-shortage-is-delaying-orders). Even if it feels like it for many customers.

SpaceX doesn't have an excuse, they have to figure out how to provide a decent level of service to existing customers, and help the thousands of people waiting in the preorder queue. And Musk fans need to realize that [just because Starlink is better than the DSL or dial-up rural customers had _before_](https://www.reddit.com/r/Starlink/comments/vkzxjq/starlink_its_all_about_perspective/), that doesn't give SpaceX any right to slack off on customer service, or provide worse latency and bandwidth than originally promised.

In the end, like I said before, I _want_ Starlink to succeed. If nothing else, I want it to spur competition again, so our Internet infrastructure can improve in the US and around the world. Even for—_especially for_—people who far from cities.

After the last three Starlink videos I posted, the next day there was some major announcement from SpaceX...

## They did an announcement

And yes... they did it again—though this time it as just after I recorded the initial script above.

{{< figure src="./maritime-coverage-map.jpg" alt="Starlink Maritime Coverage Map" width="700" height="442" class="insert-image" >}}

Starlink just announced [Starlink Maritime](https://www.starlink.com/maritime), a service that costs _$10,000_ upfront, and $5,000/month.

They'll send two terminals for sea vessels, with download speeds around 350 Mbps, and uploads capped at 40.

This isn't for your average houseboat, it's meant for people who have 'marine vessels' and need high-speed on the high seas. The best thing is, if they can figure out laser links so they can get Starlink beyond just the coastlines, landlubbers probably won't affect speeds way out in the ocean. At least as long as you don't get waves crashing over your dish!
