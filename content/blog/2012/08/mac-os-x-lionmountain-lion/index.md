---
nid: 2372
title: "Mac OS X Lion/Mountain Lion - Could not join network/timeout"
slug: "mac-os-x-lionmountain-lion"
date: 2012-08-10T15:12:51+00:00
drupal:
  nid: 2372
  path: /blogs/jeff-geerling/mac-os-x-lionmountain-lion
  body_format: filtered_html
  redirects: []
tags:
  - airport
  - lion
  - mac
  - macbook air
  - migration assistant
  - mountain lion
  - setup assistant
  - wifi
---

I was migrating all the data from a friend's old MacBook (which was running Mac OS X Tiger) to her new MacBook Air (running Mac OS X Mountain Lion), and besides a WiFi hiccup, everything went smoothly (I had to clone the old MacBook's drive to a USB disk, then use Setup Assistant to migrate the data from that disk to the new MacBook Air).

During the Setup Assistant, I could easily connect to my WiFi network, but after the migration was complete, I couldn't connect anymore. I kept getting a pesky error: "Could not join [network]. A connection timeout has occurred." (<a href="http://www.johnvarghese.com/could-not-join-network-name-a-connection-timeout-occurred/">see picture of error dialog here</a>). Looking through Apple's forums and elsewhere was not much help, because this message seems to be a very generic 'something weird happened' error, happening in many different circumstances.

However, knowing that the keychain and old WiFi connection data from the old Mac had transferred over to the new Mac, and knowing that something might've gone screwy with the network information, I decided to do the following:

<ol>
<li>Open Keychain Access and delete the password for my WiFi network from the Keychain.</li>
<li>Open System Preferences, and click on Network. Then select 'Join Other Network...', but type in the name of my own network, but with an incorrect password. Click connect, and the connection will fail... but next time, it won't!</li>
</ol>

I think Apple may have some bug that causes Keychain items and WiFi network data to get corrupt or outdated, and that's what probably caused the problem in my case. Now I can successfully log into my WiFi network on the new MacBook Air!
