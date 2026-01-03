---
nid: 3251
title: "Why I use Jellyfin for my home media library"
slug: "why-i-use-jellyfin-my-home-media-library"
date: 2022-10-27T16:01:28+00:00
drupal:
  nid: 3251
  path: /blog/2022/why-i-use-jellyfin-my-home-media-library
  body_format: markdown
  redirects:
    - /blog/2022/why-i-chose-jellyfin-my-home-media-library
aliases:
  - /blog/2022/why-i-chose-jellyfin-my-home-media-library
tags:
  - jellyfin
  - open source
  - plex
  - video
  - youtube
---

The blog post [Streaming services lost the plot](/blog/2022/streaming-services-lost-plot) detailed how streaming services have become the thing they were made to destroy.

Like cable networks and satellite companies before, they're raising rates (at a rate higher than inflation), stuffing their content libraries with filler that's not even worth the bandwidth to stream it, and shoving ads in paying users' faces.

And in my first video of this two-part series, I [showed how I rip Blu-Rays and DVDs into my computer](https://www.youtube.com/watch?v=RZ8ijmy3qPo).

{{< figure src="./jellyfin-collections-listing.jpg" alt="Jellyfin - Collections listing with many movies" width="700" height="394" class="insert-image" >}}

Today, I posted a new video, showing [how I set up Jellyfin on my NAS](https://www.youtube.com/watch?v=4VkY1vTpCJY), and explaining a bit more about transcoding, legal issues around breaking DRM, and acquiring DVDs and Blu-Rays on the cheap.

But I wanted to explain a little more about _why I chose Jellyfin_.

Many people never heard of it, and those who have often don't know why someone would choose Jellyfin over Plex, considering Plex's legacy.

## Open Source vs Proprietary

On a basic level, as a very strong proponent of (free and) open source software, the community behind Jellyfin is more palatable to me. Their [contribute](https://jellyfin.org/contribute) page emphasizes the fact that Jellyfin is powered by community. I like this. I also like how the source code (and major components) are all open source, and freely available on GitHub.

Plex, on the other hand, is run by a commercial entity, and is closed-source software—even though parts of it are built around open source components (notably, `ffmpeg`). While there's nothing inherently _wrong_ with that, it feels like some of the major features and initiatives are more... 'corporate.' Especially around content partnerships and the way Plex markets itself.

Plex also paywalls some of the most useful features, like hardware transcoding and app downloads. The price isn't excessive, but it does cost extra, either $5/month or $120 for permanent use.

## Quality and Reliability

Many articles comparing Jellyfin to Plex contain a bit of anti-open-source FUD: "because Jellyfin is developed by a community and not a company, updates could be slow, or never happen, since nobody's really controlling it."

I've heard that refrain so many times, and yes—if we're talking about a hobby project run by one passionate individual—that's a possibility.

But if you glance for half a second at the activity around Jellyfin, from [GitHub](https://github.com/jellyfin) to [Reddit](https://www.reddit.com/r/jellyfin/) to [Matrix chat](https://matrix.to/#/+jellyfin:matrix.org), you'll see a vibrant and active userbase with many individual contributors.

That's not to say it will stay that way. But there are no guarantees for Plex, either. Companies come and go, and just because Plex, Inc. currently holds the crown, that doesn't mean they will forever. A lot of the reason Plex seems to be the top choice for most people (besides marketing) is longevity: the project was started in 2007—almost _15 years ago_!

Jellyfin was launched as a fork of Emby only four years ago, in late 2018.

That does speak to Plex's staying power, but again, just because it's existed for a long time doesn't mean it is automatically better than Jellyfin. In fact, longevity induces baggage (whether technical or institutional), and that can drag down a project, too. Especially when profit must be increased, therefore features and paywalls are built with little regard for maintenance and stability!

Again, I'm not saying that's happening, I'm just trying to make a point: there is plenty of FUD to go around in all the comparisons between Jellyfin and Plex, just as in any open source vs. proprietary software discussion.

## Client Support

{{< figure src="./jellyfin-app-iphone.jpg" alt="Jellyfin app on iOS on iPhone" width="500" height="300" class="insert-image" >}}

We're a mostly-Apple household, so we have Apple TVs, iPads, iPhones, etc. Plex and Jellyfin have great first-party apps for most popular devices, whether iOS or Android. The Web UIs are both decent, so client support is only a sticky point if you're using specific devices like Roku, Fire TV stick, or Chromecast.

Traditionally a weakness, Jellyfin's device support caught up quickly with Plex, as they now have an [Android TV client](https://github.com/jellyfin/jellyfin-androidtv), a [Roku client](https://github.com/jellyfin/jellyfin-roku), and most any other type of native client you can ask for.

In addition, I've successfully [integrated Jellyfin with LibreELEC (Kodi) on a Raspberry Pi](https://www.youtube.com/watch?v=-epPf7D8oMk) built into an NEC/Sharp commercial display, and am also using it through Firecore's [Infuse](https://firecore.com/infuse) app, a highly rated media player for Apple TV.

The Jellyfin community kicked development into gear, to the point where every popular media player has some form of integration—usually first-party!

## Conclusion

This post is not a comprehensive comparison between Plex and Jellyfin. I have been using Jellyfin for the past year, and used Plex for a couple years prior, but not as heavily as I'm using Jellyfin now.

Therefore take what I say with a grain of salt. Jellyfin has made a significant impact on the space, as it has become more mature. And I'm a happy user.

Check out my video to see how I set up Jellyfin on my NAS, and how I use it to organize my media library:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/4VkY1vTpCJY" frameborder='0' allowfullscreen></iframe></div>
</div>
