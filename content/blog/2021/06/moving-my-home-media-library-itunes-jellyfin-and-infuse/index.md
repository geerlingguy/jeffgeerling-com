---
nid: 3108
title: "Moving my home media library from iTunes to Jellyfin and Infuse"
slug: "moving-my-home-media-library-itunes-jellyfin-and-infuse"
date: 2021-06-10T16:48:20+00:00
drupal:
  nid: 3108
  path: /blog/2021/moving-my-home-media-library-itunes-jellyfin-and-infuse
  body_format: markdown
  redirects:
    - /blog/2021/finally-moving-on-my-home-media-library-jellyfin-and-infuse
aliases:
  - /blog/2021/finally-moving-on-my-home-media-library-jellyfin-and-infuse
tags:
  - asustor
  - home theater
  - itunes
  - jellyfin
  - media
  - nas
  - plex
  - streaming
---

Since 2008, I've ripped every DVD and Blu-Ray I bought to my Mac, with a collection of SD and HD media totaling around 2 TB today. To make that library accessible, I've always used iTunes and the iTunes Shared Library functionality that—while it still exists today—seems to be on life support, in kind of a "we still support it because the code is there" state.

The writing's been on the wall for a few years, especially after the split from iTunes to "Music" and "TV" apps, and while I tested out Plex a few years back, I never really considered switching to another home media library system, mostly due to laziness.

{{< figure src="./jeff-with-mac-mini-nas.jpg" alt="Jeff with Mac mini NAS" width="627" height="352" class="insert-image" >}}

I have a 2010 Mac mini (see above) that's acted as my de-facto media library/NAS for over a decade... and it's still running strong, with an upgraded 20 TB of total storage space. But it's been unsupported by Apple for a few years, and besides, I have a new [ASUSTOR Lockerstor 4](https://amzn.to/3pDJnvk) with 16 TB of always-online NAS storage!

So I was looking at my options for a media library—in aggregate, I need it to serve up hundreds of movies, and potentially thousands of TV show episodes. And I'd like to make sure I can easily browse all that content on my iPad and Apple TV, at a minimum.

My music and audio track needs are met well enough by Apple's iCloud Music Library—I'm not some super audiophile nut, but I do have at least a few thousand songs that aren't part of 'Apple Music' I'm loathe to lose. Don't put blind trust in any of Apple's cloud services, and always maintain your own backups—I learned that lesson especially back in the .Mac and MobileMe days :)

> A few readers might wonder why I'd be so 'dumb' as to use Apple's cloud services if I don't trust their reliability. First, I use them for the convenience and deep integration with Apple hardware—Apple builds integrated software usable by techies and non-techies alike. Second, I keep my own backups of all the data that I store in iCloud—but I'd do the same for any cloud service. No matter what vendor, you should never put 100% of your faith into _any_ of them, especially the so-called free ones!

## Home Media Library Options

The main options I considered are [Plex](https://www.plex.tv), [Kodi](https://kodi.tv), and [Jellyfin](https://jellyfin.org).

I don't care too much about transcoding or metadata retrieval services, mostly because I've always been meticulous using [MetaZ](https://metaz.maven-group.org) (and formerly MetaX) to label every detail about every media item I've imported. And I already subscribe to what feels like 50 TV/streaming/media services (whether I want to or its part of a package deal I'm forced into getting), so I don't care about useless add-on TV channels or media partnerships.

My main goal is to have something free, easy to run, and as stable as possible—I don't want to have to switch to something else again in a few years if the ecosystem dries up!

I was familiar with Plex (if only a little) from running it a few years ago, but I wanted to see if the open source alternatives were up to snuff.

I had heard a lot about Kodi in my Raspberry Pi work, so I was checking into it, but didn't see a simple app install for it on the ASUSTOR App Center, so by default I decided to check out Jellyfin.

Jellyfin seems to be an open source fork of [Emby](https://emby.media), which started up in 2018 after Emby switched to a paid model. To be honest, I'm sure there are 'home media server historians' who could regale you with great stories about how these projects have evolved over the years...

...but I just want a media server to replace iTunes.

## Setting up Jellyfin

The first step was getting all my media onto the NAS. I've always copied my media into my own folders (not inside iTunes' Library), so it was just a matter of copying everything into a 'Media' shared folder on my NAS.

Then I installed Jellyfin from ASUSTOR's App Central, and went to the web UI to check on it. It took about 15 minutes to scan all the Movies and TV Shows I had just moved to the Media folder, and once that was done, I was up and running:

{{< figure src="./jellyfin-web-ui.jpg" alt="Jellyfin Web UI" width="600" height="375" class="insert-image" >}}

I did have to re-identify some of the movies and TV-shows, because it looks like Jellyfin just grabs the title of the file and grabs the first movie or TV database result from that.

For example, "X-Men 2" is _actually_ titled "X-2: X-Men United", even though X-Men '1' was just called X-Men, and X-Men 3 was called "X-Men: The Last Stand". Sheesh. So I had to manually identify them so they'd pull in the correct cover art and metadata.

## Viewing the content with Infuse

Jellyfin's web UI is decent, and I didn't have any real gripes with it. But I wanted a nice, streamlined app for my kids and family to use on the Apple TV, and for me to use if I wanted to pop open a movie on my iPad.

It seems like [Firecore's Infuse](https://firecore.com/infuse) is one of the best (and simplest—which I like!), so I grabbed it from the App Store, connected it to my Jellyfin library, and was off to the races on my Apple TV:

{{< figure src="./apple-tv-firecore-infuse.jpeg" alt="Apple TV running Firecore Infuse 7" width="600" height="450" class="insert-image" >}}

One nice side effect of using Jellyfin is that the library seems to come up slightly faster than when I used iTunes Shared Libraries.
