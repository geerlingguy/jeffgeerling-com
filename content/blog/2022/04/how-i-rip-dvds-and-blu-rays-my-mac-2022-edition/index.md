---
nid: 3203
title: "How I rip DVDs and Blu-Rays into my Mac (2022 Edition)"
slug: "how-i-rip-dvds-and-blu-rays-my-mac-2022-edition"
date: 2022-04-16T18:56:37+00:00
drupal:
  nid: 3203
  path: /blog/2022/how-i-rip-dvds-and-blu-rays-my-mac-2022-edition
  body_format: markdown
  redirects: []
tags:
  - blu-ray
  - disc
  - dvd
  - handbrake
  - jellyfin
  - mac
  - makemkv
  - media
  - nas
  - transcoding
---

It's been more than a decade since I wrote [Ripping Movies from Blu-Ray, HD-DVD and DVD, Getting them onto Apple TV, iPad, iPhone, etc.](/articles/audio-and-video/2010/ripping-movies-blu-ray-and-dvd). Heck, back then I didn't write everything as a 'blog post'—that was labeled as an 'article' :P

In a surprising twist of fate, we went from a somewhat more centralized online media situation back then (basically, Netflix) to a hellscape of dozens of streaming services today. And in many cases, older movies can only be found as used and/or pirated DVDs on eBay!

Thus, I'm writing a fresh guide to how I rip DVDs and Blu-Ray discs into my Mac, then transcode them with Handbrake. Heck, some people who are deeper into the [r/datahoarder](https://www.reddit.com/r/DataHoarder/) rabbit hole even have dedicated transcoding servers so they can generate optimal archival copies in 4K, 1080p, etc. akin to how YouTube and other online platforms set up their files!

But for me, the basic process goes:

  1. Rip the physical disc's main title (usually the longest) to an MKV file using [MakeMKV](https://makemkv.com). (I [bought a license](https://makemkv.com/buy/) years ago, since I use it so darn much, but it's also shareware that can be used for free.)
  2. Transcode the .mkv file to .mp4 using [Handbrake](https://handbrake.fr)'s 1080p or 4K presets.
  3. Edit the file metadata using [MetaZ](https://metaz.maven-group.org).
  4. Copy the file to my NAS's `Media` directory.

After that last step, [Jellyfin](https://jellyfin.org) automatically scans the new movie and adds it to my library.

TV shows are a different beast—you have to rip in each episode, transcode them in a batch, edit the metadata in a batch, then ideally stick the episodes into a folder for each season so Jellyfin picks them up correctly.

In the end, I'm mystified it's still so hard to buy older movies so I can watch them on my networked devices. You'd think Hollywood would've learned from the music industry that if you just let people legally pay for non-DRM media, and make the process easy and convenient (certainly more convenient than sailing the seven seas or ripping discs), people will pay.

But whatever. I'll keep ripping video content off physical disks until the day I die, I guess.

> Note: If you want to rip DVD content directly using Handbrake, you can install [libdvdcss](https://www.videolan.org/developers/libdvdcss.html) manually or with Homebrew: `brew install libdvdcss`. Then run the following command to copy the `libdvdcss` libraries into the path Homebrew expects:
>
> ```
> sudo cp /opt/homebrew/lib/libdvdcss.* /usr/local/lib/
> ```
