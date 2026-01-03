---
nid: 2461
title: "Can't Disable Annoying Chrome Notifications menu bar item on Mac OS X"
slug: "cant-disable-annoying-chrome"
date: 2013-10-03T16:01:48+00:00
drupal:
  nid: 2461
  path: /blogs/jeff-geerling/cant-disable-annoying-chrome
  body_format: full_html
  redirects: []
tags:
  - Chrome
  - google
  - mac
  - menu bar
  - notifications
aliases:
  - /blogs/jeff-geerling/cant-disable-annoying-chrome
---

<strong>Update (7/20/14)</strong>: You can finally disable the notifications icon by selecting "Hide Notifications Icon" from the Chrome menu:

<p style="text-align: center;">{{< figure src="./disable-chrome-notifications-mac-os-x.png" alt="Disable Chrome Notifications on Mac OS X" width="319" height="308" >}}</p>

<em>Original post below.</em>

Today, I received a mysterious notification from one of my Chrome extensions that popped up under a generic alarm bell icon in my Mac OS X menu bar:

<p style="text-align: center;">{{< figure src="./chrome-notifications.png" alt="Chrome Notifications" width="406" height="83" >}}</p>

No thanks. I have Notification Center (built into Mac OS X), and if I <em>wanted</em> to see spammy notifications from Chrome extensions, I would enable them there. I know I can disable individual (or all) extensions from this Chrome Notification Center, but that doesn't make the icon go away. Nor does the standard trick of holding down the command key and dragging the icon off the menu bar.

No... Google seems to think that every Chrome user on a Mac wants this non-UI-conforming precious-menu-bar-real-estate-consuming icon sucking up resources and precious space, without any way of disabling it. And when <a href="https://code.google.com/p/chromium/issues/detail?id=247814">users point out that Chrome should use the system's built in notifications system</a> (like every other mainstream app nowadays), Google says no, we'll use our confusing menubar icon instead.

Unfortunately, going to <code>about:flags</code> doesn't allow disabling of the desktop notification center (since it's managed in the main Chrome settings area now), and explicitly excluding all plugins inside <em>Chrome's settings > Show advanced settings... > Content settings... > Notifications</em> doesn't do a thing either.

Switching back to FireFox or Safari is looking more appealing every day.

[<strong>Update</strong>: It looks like if you go to <code>chrome://flags</code> and set the 'rich desktop notifications' flag to Disabled, then restart Chrome, the icon goes away. I guess that's an okay temporary fix, but still...]
