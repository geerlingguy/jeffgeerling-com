---
nid: 3491
title: "YouTube views are down (don't panic)"
slug: "youtube-views-are-down-dont-panic"
date: 2025-09-07T17:51:20+00:00
drupal:
  nid: 3491
  path: /blog/2025/youtube-views-are-down-dont-panic
  body_format: markdown
  redirects:
    - /blog/2025/youtube-views-are-down
aliases:
  - /blog/2025/youtube-views-are-down
tags:
  - analytics
  - data
  - ltt
  - revenue
  - statistics
  - youtube
---

> **September 15 update**: [@YouTubeInsider confirmed](https://x.com/YouTubeInsider/status/1967588485201600800) that the issue is related to viewers who have adblockers enabled—YouTube's [been in an arms race with ad blocking tools](https://www.youtube.com/watch?v=YX1eEe8erkQ), and the fallout is a substantial cut in counted views for creators who have a large audience watching from desktop.

Many YouTube content creators, myself included, noticed something in early to mid-August: views were down.

After being on the platform since 2006 (though for me, not being a 'professional' YouTuber until about 5 years ago), I'm used to seasonal dips, adjustments after new tweaks to the algorithm or layout/design changes.

But this was _substantial_.

{{< figure src="./youtube-jeffgeerling-views-down.jpg" alt="YouTube Jeff Geerling views down" width="700" height="350" class="insert-image" >}}

I had 4 10/10 videos _in a row_, which is unprecedented. I mean, my content could just be terrible all the sudden, and I've lost all but my core audience. But there are other explanations. Especially when _the exact same thing_ happened to a large number of my peers on YouTube.

## What happened (anecdotally)

For my own channels, [Jeff Geerling](https://www.youtube.com/c/JeffGeerling), [Geerling Engineering](https://www.youtube.com/@GeerlingEngineering), and [Level 2 Jeff](https://www.youtube.com/@Level2Jeff), the view counts on new long-form videos took an absolute nosedive sometime in early August. And they haven't recovered.

What's strange is the raw count of _likes_ (people who watched the video and appreciated it enough to hit 'thumbs up') was consistent. And stranger still, overall _revenue_ was consistent.

And this meant the ratio of likes per view and revenue per view went _way_ up. Which, I mean... outside of finance creators and scammers (sometimes hard to distinguish the two), it's hard to break past a $3-5 RPM (revenue per mille), so I can't complain _there_.

But that's just my anecdata. One YouTuber's feelings aren't much to go on.

The problem is tons of other creators noticed the same change, for example [DarkViperAU](https://www.youtube.com/watch?v=zjphsaR75Jk), [Second Wind](https://www.youtube.com/watch?v=cpVnx4_yqTo), [HAINBACH](https://www.youtube.com/post/UgkxZHE1LeJKXY_kVC932bugOmoulYjstt78), [DankPods](https://www.youtube.com/watch?v=E1Dai1Qy2eo), and more.

And after [discussing the problem on last week's WAN show](https://www.youtube.com/watch?v=KqCV6Rk8kOA), [Dan Besser from LTT](https://x.com/BuhDan) started analyzing the numbers for LTT and a number of other channels, seeing a strong correlation between views, likes, revenue, and other markers, with a sudden, statistically significant change, always in early August.

## What happened (scientifically)

Go [watch _this_ week's WAN show, starting at 15:48](https://youtu.be/qPen-cHdYmk?&t=949), to see a bit more explanation, but Dan pulled the numbers for all three of my channels to correlate views and likes, to build a view:like ratio, and found a pretty surprising change—which syncs up with the same change he's noticed on a number of other channels.

First, my main Jeff Geerling channel:

{{< figure src="./youtube-views-down-jeffgeerling.jpg" alt="Jeff Geerling - YouTube views to likes data analytics" width="700" height="356" class="insert-image" >}}

Then, Geerling Engineering:

{{< figure src="./youtube-views-down-geerling-engineering.jpeg" alt="Geerling Engineering - YouTube views to likes data analytics" width="700" height="307" class="insert-image" >}}

And finally, Level 2 Jeff:

{{< figure src="./youtube-views-down-level2jeff.jpeg" alt="Level 2 Jeff - YouTube views to likes data analytics" width="700" height="308" class="insert-image" >}}

> Thanks to Dan from LTT for these graphs—again, go [check out the WAN show for more background](https://youtu.be/qPen-cHdYmk?&t=949).

I think there's more to the data, and there are some creators who seem unaffected. Theories for this abound, but it doesn't seem like it's related to a 'fall off' in interested viewers for any of the affected channels. It feels a lot more like what YouTube's done before, like separating "engaged" views from "views" on Shorts, or something like that.

The fact that other numbers are similar in quantity, but much higher in ratio, like watch time per video, RPM, likes, etc., indicates maybe YouTube is doing an A/B test tweaking what counts for the displayed view count... or something is just broken, which is also not without precedent! But usually they announce these things beforehand.

## What's the problem?

The _problem_, at least for many creators, is views are currently king when it comes to things like sponsorship deals, promotions, etc.

For _me_, it's less a problem, as I take sponsorships sparingly (see [my sponsorship policies here](https://github.com/geerlingguy/youtube?tab=readme-ov-file#sponsorships)), and don't rely on that revenue for business continuity. I also have other sources of income, so even if YouTube revenue goes to $0, I will still be on my feet, financially (though I would likely have to take on a 401k job to afford health insurance).

For many creators, especially those who have multiple employees, debts to pay channel expenses, etc., a downturn in views could spell doom. Especially if sponsorship deals they rely on are tied to metrics like 'views per 24h' or 'views over 30/60/90 days'.

As an industry, marketing firms have mostly untied _subscriber counts_ from ad spend decisions, since subscribers are less an indicator of channel health. Maybe this is an indication they need to adjust expectations when it comes to _views_ as well...

Many readers of this blog think all this stuff is hogwash and meaningless anyway (the Internet was better before it was all monetized!), but it is nice to earn an income and get paid for the work I do, in the form of YouTube AdSense.

I, of course, don't begrudge anyone for ad blocking. And I offer all my videos in full 4K resolution downloads [on Floatplane](https://www.floatplane.com/channel/JeffGeerling/home)—some viewers even integrate it automatially with Plex or Jellyfin, and skip YouTube entirely! I've even considered experimenting with PeerTube, but I'm not sure whether I'll test those waters or not.

In the end, whether you like modern YouTube or not, it view counts are down, possibly for Shorts as well (I only post one or two shorts a month, so have less data to go on there), but it's not clear why.

I strongly suggest following [BuhDan](https://x.com/BuhDan) for more updates, and I'm sure there will be more discussion on future WAN shows, and around other corners of YouTube, on this matter.

It'd be amazing if we had even an acknowledgment of the issue from YouTube, much less an explanation...
