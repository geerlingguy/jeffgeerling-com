---
nid: 2773
title: "AirPort Extreme showing 'Device Not Found'? Here's a fix"
slug: "airport-extreme-showing-device-not-found-heres-fix"
date: 2017-05-07T19:54:59+00:00
drupal:
  nid: 2773
  path: /blog/2017/airport-extreme-showing-device-not-found-heres-fix
  body_format: markdown
  redirects: []
tags:
  - airport
  - apple
  - mac
  - router
  - tutorial
  - wifi
---

If you've had an AirPort Extreme for a while, and recently (within the past year or two) had it go missing from your network (when you open AirPort Utility you get 'Device Not Found'), there's a good chance you ran into the same issue I did. Basically, everything was running great, then one day around August 2016, my Extreme disappeared from the network—even though it was routing Internet traffic for all the devices in my house just as good as ever!

The fix?

  1. Open AirPort utility (it will likely show "Device Not Found").
  2. Unplug your AirPort Extreme, and wait 10 seconds.
  3. Plug it back in, and connect to the WiFi network as soon as possible, then immediately go to the AirPort Utility.
  4. The AirPort should appear and be manageable (by clicking on it) for a brief period—quickly click on it, click Edit, then clear out any Apple IDs in the 'Back to My Mac' section.

{{< figure src="./airport-extreme-back-to-my-mac.jpg" alt="AirPort Extreme Back to My Mac Apple ID listing" width="650" height="550" class="insert-image" >}}

It seems there's a bug in at least the 7.7.7 and 7.7.8 firmware revisions that causes the AirPort Extreme to become unmanageable (though still functional as a router) if you sign into one of your Apple IDs to use Back to My Mac :/

See related MacWorld article: [Does your AirPort Extreme Base Station work but is unreachable via AirPort Utility?](http://www.macworld.com/article/3109308/networking/does-your-airport-extreme-base-station-work-but-is-unreachable-via-airport-utility.html).
