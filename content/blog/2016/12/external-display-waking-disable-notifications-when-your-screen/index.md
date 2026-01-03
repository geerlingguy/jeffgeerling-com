---
nid: 2721
title: "External display waking up? Disable notifications when your screen is off"
slug: "external-display-waking-disable-notifications-when-your-screen"
date: 2016-12-23T05:16:02+00:00
drupal:
  nid: 2721
  path: /blog/2016/external-display-waking-disable-notifications-when-your-screen
  body_format: markdown
  redirects:
    - /blog/2016/external-display-waking-disable-smart-notifications-when-your-mac-asleep
aliases:
  - /blog/2016/external-display-waking-disable-smart-notifications-when-your-mac-asleep
tags:
  - energy efficiency
  - mac
  - macos
  - notifications
---

Since a week or so ago, I noticed that even when my Mac's display was put to sleep, my external display would sometimes turn on and remain on for long periods of time if I had a calendar reminder or some other type of non-dismissible notification. It would even come on (and turn off shortly thereafter) for quick notifications.

This was highly annoying, especially when I'd come to my computer in the morning and realize the external monitor had been on displaying a notification all night!

Apparently macOS 10.12.2 includes a new feature called [Enhanced notifications](https://support.apple.com/en-us/HT204353), and they can wake up internal or external displays to show notifications. Annoyingly, this new feature is enabled by default. To disable it, you need to go into the Notifications System Preference, and inside the 'Do Not Disturb' section, and check the "When the display is sleeping" option under "Do Not Disturb":

<p style="text-align: center;">{{< figure src="./display-notifications-enhanced-external-display-sleep.png" alt="Don&#39;t display notifications using Do Not Disturb&#39;s When the display is sleeping option" width="650" height="514" class="insert-image" >}}</p>
