---
nid: 2339
title: "Problems with Android's Back Button"
slug: "problems-androids-back-button"
date: 2011-11-01T15:46:27+00:00
drupal:
  nid: 2339
  path: /blogs/jeff-geerling/problems-androids-back-button
  body_format: full_html
  redirects: []
tags:
  - ally
  - android
  - design
  - development
  - droid
  - iphone
  - mobile
  - smartphones
  - ux
aliases:
  - /blogs/jeff-geerling/problems-androids-back-button
---

Android's back button is a problem. A big problem.

Others have already identified this in a broad sense, but I wanted to give a few concrete examples of why I (as a guy who wants to simply port a couple apps from the iOS platform to Android) think the back button (especially) is a bad idea.

<h3>Disorientation</h3>

Mobile phones, and tablets especially, require a lot of UX work in the area of interface orientation. For my extremely-basic CNL app, I've spent hours tweaking little interface elements that change when the interface is rotated from portrait to landscape.

The tendency in iOS is to use a 'back' button with the label of the previous function/screen in a given app in a navigation bar at the top of the current screen. This allows a user to freely move about inside an app, and is pretty much consistent across all apps. Additionally, this 'universal back button' is <em>always</em>&nbsp;at the top left of the screen—just like a web browser.

Now, let's look at Android's back button situation:
<p style="text-align: center;">{{< figure src="./droid-back-button.jpg" alt="Droid back button interface rotation." width="550" height="255" >}}</p>
As you can see, when you rotate the phone, the back button changes position. In left-to-right places like the U.S., this is a UX faux pas - the back button is in the 'forward' position... and if we rotate the interface the other way, the back button is finally in the correct/expected position... but that's the opposite of the way most of the 'slider' phones (like the Droid pictured above) work.

<h3>Context Lost</h3>

I've seen a lot of posts about this, and I've had the same opinion: the back button's contextual behavior is broken. Is it an in-app back button? App-to-app back button, operation-to-operation, page to page?

It's a good idea in theory, but in execution, this universal back button leaves much to be desired. Because the Android's screen has no contextual information as to what the user was doing previously, the back button could do any number of things the user doesn't want to do. If you hit it one too many times (especially considering the laggy responsiveness on most Android phones), you could end up out of the Browser or some other app entirely, and there's no 'forward' button to get you back. You have to start over.

<h3>Capacative hardware buttons</h3>

Apple discovered this with the iPod. There's a great article on designdare.com highlighting <a href="http://designdare.com/the-capacitive-button-cult-must-be-stopped">many of the problems inherent in capacative button design</a> and implementation. Capacative touch hardware buttons are horrible.

The first few days using a Droid and an LG Ally (both have touch back buttons just south of the screen), I kept hitting the back button just because of the way I was holding the phone while browsing the web. I had to train myself to hold the phone differently, just to avoid losing my work. That, and the lack of a forward button (there may be one in a menu somewhere, but I couldn't find it on the screen) make it difficult to use an Android phone to simply browse the web.

The Droid's 'haptic feedback' feature at least made it obvious I was hitting the back button... but it's really annoying having the phone vibrate every time I did anything. I tried using the phone without the haptic feedback, but then it was hard to know when I actually hit a button (due to lagginess).

It's interesting to note that buttons are in different places on different phones, too... I started with the original iPhone and have had all models since. The hardware, on a basic level, is <em>exactly</em>&nbsp;the same. My fingers have never had to re-learn what to do. From Android phone to android phone, the back button, home button, power button, etc. are often in different places, or just aligned slightly differently.

<h3>So why develop for Android?</h3>

I've decided to go ahead and work on a few smaller projects (nothing big right now), mostly to see how sales compare to my iOS apps. CNL has been a moderate success on the App Store, and I'm guessing I can at least make it worth my while to release a version for Android Market—hopefully.

Also, Ice Cream Sandwich, and the latest Android hardware (most of which won't run ICS for a while... groan), looks like it may take some steps towards fixing some of these problems. But this post highlights one of the small frustrations I've already encountered with the Android ecosystem—mostly from an <em>end user's</em>&nbsp;perspective.

Over on Life is a Prayer.com, I've also posted on the issue of <a href="http://www.jeffgeerling.com/blog/2011/developing-android-or-not">Developing for Android... or Not?</a>
