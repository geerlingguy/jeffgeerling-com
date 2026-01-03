---
nid: 2352
title: "Why I don't develop for Android first"
slug: "why-i-dont-develop-android"
date: 2011-12-15T16:42:37+00:00
drupal:
  nid: 2352
  path: /blogs/jeff-geerling/why-i-dont-develop-android
  body_format: full_html
  redirects: []
tags:
  - android
  - android market
  - app store
  - apps
  - ios
---

I developed my <a href="http://itunes.apple.com/us/app/catholic-stl-archdiocese-st/id422420472?mt=8">first iOS app</a> about a year and a half ago, and it has seen over 2,500 downloads (it's a free app, and pretty useful, albeit only for a certain portion of people living in St. Louis, MO).

I developed my <a href="http://itunes.apple.com/us/app/catholic-news-live/id422525557?mt=8">second iOS app</a> (a companion to a news aggregation website that's existed since 2009) in April 2011, and in the first month alone, it was purchased ($0.99) over 300 times. In the months that followed, the app has consistently sold over 50 copies, sometimes more than 100, without—literally—<em>any</em> marketing on my part. Just an occasional plug on Twitter or at a conference. That's it.

I then decided to finally take the plunge and try my hand at <a href="https://market.android.com/details?id=com.midwesternmac.cnl">redeveloping the app</a> for Android (my first Java/Android project), and worked very hard to make the app run as good, and sometimes even <em>better</em> on Android phones (anything running 2.2+...).

<p style="text-align: center;">{{< figure src="./sales-per-marketplace.png" alt="Sales per app marketplace" width="328" height="224" >}}
Translation: <strong>Why I won't develop for Android first</strong> (no matter the marketshare).</p>
The first month of sales have been more than disappointing; after 8 sales on the first day—most to friends who I specifically asked to download the app and test it*—the app has sold maybe one or no copies each day since, and all in the U.S. (The app has four five star reviews, the market page, icon, etc. are all very good quality—I spent a lot of time on the text, design, icon, etc., even forming everything to Android Market/platform standards instead of reusing iOS resources).

My takeaway (so far): If you want to sell an app and make money, put it on the App Store. If you want to make a free app that gives you no income, put it on the Android Market. (And if you want to maybe make one or two more sales, also stick it on the Amazon Appstore... but you're asking for a heaping helping of hurt there).

Don't get me started on how bad the software emulator for Android development is, how annoyingly hard it is to test on different versions of Android (especially since later versions don't come out for older phones unless you <a href="http://www.jeffgeerling.com/blogs/jeff-geerling/rooting-android-general">root the phone</a>), or how difficult it is to design around the (possibly-going-away?) <a href="http://www.jeffgeerling.com/blogs/jeff-geerling/problems-androids-back-button">hardware back button</a>.

<a href="http://daringfireball.net/linked/2011/12/08/eric-schmidt-really-said">Eric Schmidt</a> needs to make the Android Market more appealing and get some of those millions of Android users to pay for apps before I'll reconsider developing for iOS first.

<span style="text-color: #999;">* There's no way to generate free download codes for reviewers on the Android Market; so I have to either ask reviewers to buy the app or email them an .apk file that they have to manually install on their phones (and over which I have no control for updating, etc.). Stupid...</span>
