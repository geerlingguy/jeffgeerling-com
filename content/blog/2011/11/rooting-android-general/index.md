---
nid: 2341
title: "Rooting Android - General Observations and OG Droid + LG Ally"
slug: "rooting-android-general"
date: 2011-11-04T14:19:05+00:00
drupal:
  nid: 2341
  path: /blogs/jeff-geerling/rooting-android-general
  body_format: full_html
  redirects: []
tags:
  - android
  - apple
  - bugless beast
  - droid
  - froyo
  - gingerbread
  - google
  - ios
  - rom
  - root
aliases:
  - /blogs/jeff-geerling/rooting-android-general
---

<h2>Background and Comparison to iOS Jailbreaking</h2>

After a couple years having had no experience with an Android phone of any variety, a generous Twitter follower I had met donated two older Android phones, an original Motorola Droid (running Froyo 2.2.2) and an LG Ally (also running 2.2.2), so I could learn the Android UI and work on porting a couple of my iOS apps.

One unfortunate reality of the Android ecosystem is that phones are often abandoned by their manufacturers after only a year (or less time), and even if not, they are not kept up to date past one or two minor Android OS releases. For instance, both the Ally and Droid are more than capable of running Android 2.3 Gingerbread (and I'm now running 2.3.7 on the Droid, faster than 2.2.x ever ran), but Motorola has ended support for the device.

Contrast this with the iOS platform; the same-age iPhone 3GS is <em>still</em> for sale by Apple, and it runs iOS 5.x (the latest OS) fast (I still have a 3GS to play with, in addition to my 4S and my wife's 4), and received the OS upgrade the day it came out. Additionally, jailbreaking iOS is trivial compared to trying to figure out how to root, then get a ROM and install it, for an Android phone of most varieties. All but the most expensive Android phone models are dependent on generous souls to do the work of adapting a ROM to the phone.

Since all I could find for Android rooting were a bunch of blog posts and forum topics that had scattered information, I thought I'd compile my experiences rooting and upgrading two Android phones.

<h2>Finding a ROM for Gingerbread/etc.</h2>

Unfortunately, this is the most difficult part for many Android phones. Lucky for me and my Droid, <a href="http://www.peteralfonso.com/">Peter Alfonso</a> creates regular 'Bugless Beast' Gingerbread ROMs for the Droid, and posts them on his website. Here's the link to <a href="http://www.peteralfonso.com/2011/10/download-bugless-beast-v-gpa18-android.html">2.3.7 of Bugless Beast</a>.

For the LG Ally, since it's a more entry-level phone, and must not've been as popular as the Droid, ROMs are few and far between. I thought I had found a good ROM <a href="http://www.xpgamesaves.com/topic/18310-how-to-upgrade-update-lg-ally-to-android-23-gingerbread/">here</a>, but it seems I was mistaken — the ROM didn't boot :(

<h2>Upgrading the Droid OG</h2>

The first step in getting 2.3.x on the Droid is to 'root' your phone. The simplest way of doing this is to use a one-click rooting application, of which there are a variety. The only one I found to work on both phones, though, was GingerBreak (<a href="http://www.itsmyiphoneworld.com/uploaded-files">download GingerBreak from this page</a>) (v1.20). Open that app and tap the 'root my phone' option.

The second step is re-flashing your phone's ROM. Here's how to do that:

<ol>
	<li>Install ROM Manager (free or paid version) from the Android Market.</li>
	<li>Open ROM Manager and flash your phone using Clockwork recovery. (Note: You may need to keep doing this over and over if you get an error, until it downloads and flashes all the way).</li>
	<li>Copy the .zip file you downloaded with the appropriate ROM file to the your phone's Micro SD card.</li>
	<li>Use ROM Manager to install the zip file from your SD card.</li>
	<li>Wait a while while the upgrade completes... and then after your phone restarts, enjoy running a newer OS!</li>
</ol>

<h2>Upgrading the LG Ally</h2>

The Ally should be about the same, but, unfortunately, I still cannot find a 2.3.x ROM for the Ally.
