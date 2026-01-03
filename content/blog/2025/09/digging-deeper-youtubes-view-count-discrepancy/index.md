---
nid: 3493
title: "Digging deeper into YouTube's view count discrepancy"
slug: "digging-deeper-youtubes-view-count-discrepancy"
date: 2025-09-16T19:55:20+00:00
drupal:
  nid: 3493
  path: /blog/2025/digging-deeper-youtubes-view-count-discrepancy
  body_format: markdown
  redirects:
    - /blog/2025/digging-deeper-source-youtube-view-count-discrepancy
aliases:
  - /blog/2025/digging-deeper-source-youtube-view-count-discrepancy
tags:
  - analytics
  - level2jeff
  - video
  - views
  - youtube
---

For a great many tech YouTube channels, [views have been markedly down](/blog/2025/youtube-views-are-down-dont-panic) from desktop ("computer") users since August 10th (or so).

This month-long event has kicked up some dust—enough that two British YouTubers, [Spiffing Brit](https://www.youtube.com/watch?v=MGTKaALdHzc) and [Josh Strife Hayes](https://www.youtube.com/watch?v=YX1eEe8erkQ) are having a very British argument[^british] over who's right about the root cause.

Spiffing Brit argued it's a mix of YouTube's seasonality (it's back to school season) and channels falling off, or as TechLinked puts it, "[git gud](https://www.youtube.com/watch?v=gZ5pATTvc2o)", while Josh Strife Hayes points out the massive number of channels which identified a _historic_ shift down in desktop views (compared to mobile, tablet, and TV) starting after August 10. This data was [corroborated by this Moist Critical video](https://www.youtube.com/watch?v=8FUJwXeuCGc) as well.

{{< figure src="./penguinz0-youtube-views-decline.jpg" alt="Moist Critical YouTube view decline" width="700" height="488" class="insert-image" >}}

In any case, one thing is certain: _many_ YouTubers—most seemingly with a larger desktop audience, and many in the tech/FOSS/etc. space—have seen a drastic downturn in views counted in YouTube analytics since mid-August.

However, there is (so far) not a similar fall off in revenue (in fact, my channel's RPM, or revenue per thousand views, has almost _doubled_, as my views declined by 40-50% month-over-month).

And likes and comments have remained consistent, even with a greatly diminished number of viewers. I even pushed this theory a bit further with an [experimental video on Level 2 Jeff this morning](https://www.youtube.com/watch?v=6kDGWrm9P-U):

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/6kDGWrm9P-U" frameborder='0' allowfullscreen></iframe></div>
</div>

So... what could account for all these phantom viewers who have disappeared? Was it just YouTube cleaning up bots like [Twitch did recently](https://www.forbes.com/sites/maryroeloffs/2025/08/27/huge-drop-in-twitch-streams-explained-platforms-crackdown-on-viewbotting/)?

I don't think so, and most others I've spoken with don't either. It _felt_ more likely to be related to _ad blocking_, as it would also nicely line up with the reduction in views _only for some creators_—those who cater to a more tech-savvy audience who watch videos on desktop/laptop computers. _And_ who would be more likely to use adblock tech to make YouTube a somewhat reasonable viewing experience[^adspam].

## Ad block as a root cause?

[ThioJoe](https://x.com/thiojoe/status/1968010742151717243) put me onto a [single commit](https://github.com/easylist/easylist/commit/8f56190d0eef68b5b137d6c644962e9d0485a4fd) in the open source `easylist` filter, which seems to be used as a default by a number of ad blocking tools like [uBlock Origin](https://ublockorigin.com).

It looks like that commit was made, adding `youtube.com/api/stats/atr` to the block list, after [this brief issue was posted](https://github.com/easylist/easylist/issues/22052). There's an issue that was asking about [reverting the change](https://github.com/easylist/easylist/issues/22375), but as of right now it's closed, so not likely to happen.

What I find interesting is [back in 2021, the same URL was _removed_](https://github.com/easylist/easylist/commit/87c5b1343be6cdf9445bc08fe8177babb4b749ba) from the block list, with the commit "Temporarily disable", but without any further discussion or references as to why.

Maybe at that time (in 2021), someone else had noticed it was affecting view counts? Not sure.

But one thing that's becoming more clear: YouTube's article talking about [YouTube View count changes](https://support.google.com/youtube/thread/373195597) buries the bullet point about ad blockers _way_ down below the fold:

> **Viewers Using Ad Blockers & Other Content Blocking Tools**: Ad blockers and other extensions can impact the accuracy of reported view counts. Channels whose audiences include a higher proportion of users utilizing such tools may see more fluctuations in traffic related to updates to these tools.

But I'm 99% sure this is the reason many tech creators have seen a massive downturn in YouTube views in the past month.

## Why does this matter?

Well, in the short term, at least for _me_, it doesn't.

My AdSense revenue is flat (not going down yet), and video engagement is fine too. I love interacting with my channel's community in the comments, so it would stink if I also had way fewer comments.

_However_, there are a few things that are unanswered—and unless the block list _un-blocks_ YouTube's analytics, they could turn out poorly for content creators:

  - Do Premium subscribers who use uBlock Origin now not have _their_ views counted? (Premium views are worth more to creators than regular monetized views, so this would be a hard pill to swallow).
  - Are YouTube's recommendation algorithms tuned to views in such a way that even with consistent _engagement_ (likes, views, watch time), videos from creators with a larger desktop/ad-blocking audience will be recommended less, because the total view count is in pretty substantial decline versus those targeting mobile and less-technical audiences?
  - Will sponsors take into account this view count discrepancy across technical vs general channels when they determine sponsorship tiers for views-per-30d, and views-per-90d on videos? Only the financial channels (which make _tons_ of money) seem to get special treatment and rates for sponsors.

I take sponsors [very sparingly](https://github.com/geerlingguy/youtube?tab=readme-ov-file#sponsorships). When I do, the amount offered is tied to a metric like "average views per 90 days across the last 10 or 30 videos". And if I'm competing with a fashion influencer on views[^fashion], and that channel isn't impacted by the ad blocking change... I'm gonna lose that battle by nature of our vastly different audiences, even if my channel has similar overall reach.

I will be fine one way or the other, but a change like this can and will affect many channels that are structured differently. And (putting on my speculation hat) it will likely lead some to push out content that appeals less to a technical audience, since that audience is even less likely to lead to success on YouTube.

## A quick manual fix

If you'd like to allow YouTube to track your views even while running an ad blocker, [GitHub user Scrxtchy](https://x.com/Scrxtchy/status/1968005715282596024) created a [ReturnYoutubeView](https://github.com/Scrxtchy/ReturnYoutubeView) adblock whitelist to restore the two URLs YouTube needs to count a view. The process of applying that filter can vary depending on the ad blocking tools you use.

Most people won't go that far (defaults are probably used in 99% of all cases), so unless [this issue](https://github.com/easylist/easylist/issues/22375) is reconsidered, this may be the new normal for tech creators.

## Further Updates

{{< figure src="./youtube-views-desktop-coming-back.png" alt="YouTube views by device type showing Desktop views coming back" width="700" height="456" class="insert-image" >}}

**2025-09-19**: As of today, I (and some other creators I've spoken to) noticed a marked increase in desktop views, back to pretty much in line with what they were August 9 and earlier. It seems that both [easylist](https://github.com/easylist/easylist/commit/2d39de407dc9) and [uBO](https://github.com/uBlockOrigin/uAssets/commit/5a96b21d) stopped blocking the specific view analytics URL YouTube was using—though uBO [added back one of the URLs](https://github.com/uBlockOrigin/uAssets/commit/e0f88dbb5e1bd777a44019d40b70fb0299404b65)? It's still unclear the reasoning behind all the changes, but the original issue on the easylist repo I linked to earlier was closed and locked.

[^british]: Basically "you are wrong, but I am going to say that in the most polite way possible, with all possible deference because I respect you" (which honestly I love and we could use more of when arguing about things these days, lol).

[^adspam]: Watching without Premium or and ad-blocker is very _very_ bad these days—worse than cable TV 20 years ago!

[^fashion]: Not that there's a lot of advertiser crossover... but more appropriate might be comparing a channel that's very anti-FOSS to a channel like mine that's pro-FOSS. The anti-FOSS channel would likely attract fewer users using ad block, so counted views per video on, say, a storage appliance, may be higher compared to the actual audience viewing the video. Sponsors should probably track metrics like inbound clicks and conversions instead of basing sponsorships on subscriber or view counts, but that's sadly too much to ask many of them!
