---
nid: 3469
title: "Self-hosting your own media considered harmful (updated)"
slug: "self-hosting-your-own-media-considered-harmful-updated"
date: 2025-06-06T04:19:42+00:00
drupal:
  nid: 3469
  path: /blog/2025/self-hosting-your-own-media-considered-harmful-updated
  body_format: markdown
  redirects:
    - /blog/2025/self-hosting-media-libraries-considered-harmful
    - /blog/2025/self-hosting-your-own-media-considered-harmful
aliases:
  - /blog/2025/self-hosting-media-libraries-considered-harmful
  - /blog/2025/self-hosting-your-own-media-considered-harmful
tags:
  - content
  - guidelines
  - jellyfin
  - libreelec
  - open source
  - video
  - youtube
---

I just received my [second community guidelines violation](https://github.com/geerlingguy/youtube/issues/12) for my video demonstrating the use of LibreELEC on a Raspberry Pi 5, for 4K video playback.

{{< figure src="./community-guidelines-strike.jpg" alt="Community Guidelines Strike - YouTube" width="700" height="469" class="insert-image" >}}

I purposefully avoid demonstrating any of the tools (with a suffix that rhymes with "car") that are popularly used to circumvent purchasing movie, TV, and other media content, or any tools that automatically slurp up YouTube content.

In fact, in my own house, for multiple decades, I've purchased physical media (CDs, DVDs, and more recently, Blu-Rays), and only have legally-acquired content on my NAS. Streaming services used to be a panacea but are now fragmented and mostly full of garbage—and lots of ads. We just wanted to be able to watch TV shows and movies without hassle (and I'm happy to pay for physical media that I want to watch).

But this morning, as I was finishing up work on a video about a new mini Pi cluster, I got a cheerful email from YouTube saying my video on LibreELEC on the Pi 5 ([here's the original YouTube link - now dead](https://t.co/qR9s0UZzon)) was removed because it promoted:

> **Dangerous or Harmful Content**  
> Content that describes how to get unauthorized or free access to audio or audiovisual content, software, subscription services, or games that usually require payment isn't allowed on YouTube.

I never described any of that stuff, only how to self-host your own media library.

> **Update** (one day later):
>
> YouTube has just reinstated [the video](https://www.youtube.com/watch?v=3hFas54xFtg), after what I presume is a human review process. I wish it didn't take making noise on socials to get past the 'AI deny' process :(
>
> Go forth, and self-host all the things! I'll post further updates in [this issue in my YouTube project](https://github.com/geerlingguy/youtube/issues/12).

This wasn't my first rodeo—in October last year, I got a [strike for showing people how to install Jellyfin](https://github.com/geerlingguy/youtube/issues/13)!

In _that_ case, I was happy to see my appeal granted within an hour of the strike being placed on the channel. (Nevermind the fact the video had been live for _over two years_ at that point, with nary a problem!)

So I thought, this case will be similar:

  - The video's been up for over a year, without issue
  - The video's had over a million views
  - The video doesn't promote or highlight any tools used to circumvent copyright, get around paid subscriptions, or reproduce any content illegally

Slam-dunk, right? Well, not according to whomever reviewed my appeal. Apparently self-hosted open source media library management is harmful.

Who knew open source software could be so _subversive_?

## The video

So along that theme, I've re-uploaded the video to Internet Archive, free for anyone to download and view at their leisure.

_Yes, even those rebels running LibreELEC on their Raspberry Pis!_

Here it is: [LibreELEC on the Raspberry Pi 5 - Internet Archive](https://archive.org/details/libreelec-raspberry-pi-5).

<a href="https://archive.org/details/libreelec-raspberry-pi-5">{{< figure src="./jeff-geerling-video-libreelec-pi-5.jpg" alt="LibreELEC on Pi 5 video thumbnail with play button" width="400" height="auto" class="insert-image" >}}</a>

I've also uploaded it [on Floatplane](https://www.floatplane.com/post/bNx4Mhzqvu), for subscribers.

## Alternatives

I've been slowly uploading my back catalog to [my channel on Floatplane](https://www.floatplane.com/channel/JeffGeerling/home), though not all my content is there yet.

Some in the fediverse ask why I'm not on Peertube. Here's the problem (and it's not insurmountable): _right now_, there's no easy path towards sustainable content production when the audience for the content is 100x smaller, and the number of patrons/sponsors remains proportionally the same.

I was never able to sustain my open source work based on patronage, and content production is the same—just more expensive to maintain to any standard (each video takes between 10-300 hours to produce, and I have a family to feed, and [US health insurance companies to fund](https://www.jeffgeerling.com/tags/crohns)).

YouTube was, and still is, a creative anomaly. I'm hugely thankful to my [Patreon](https://www.patreon.com/c/geerlingguy), [GitHub](https://github.com/sponsors/geerlingguy), and [Floatplane](https://www.floatplane.com/channel/JeffGeerling/home) supporters—and I hope to have direct funding fully able to support my work someday. But until that time, YouTube's AdSense revenue and vast reach is a kind of 'golden handcuff.'

The handcuff has been a bit tarnished of late, however, with Google recently adding AI summaries to videos—which _seems_ to indicate maybe [Gemini is slurping up my content and using it in their AI models](https://www.msn.com/en-us/news/technology/google-gemini-s-ai-video-summary-implies-youtube-doesn-t-care-about-content-creators/ar-AA1rMsoy)?

Maybe the handcuffs are fools-gold, and I just don't see it yet.
