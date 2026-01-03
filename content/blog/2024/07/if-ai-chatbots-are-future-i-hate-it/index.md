---
nid: 3389
title: "If AI chatbots are the future, I hate it"
slug: "if-ai-chatbots-are-future-i-hate-it"
date: 2024-07-11T01:08:00+00:00
drupal:
  nid: 3389
  path: /blog/2024/if-ai-chatbots-are-future-i-hate-it
  body_format: markdown
  redirects: []
tags:
  - ai
  - artificial intelligence
  - att
  - chatbot
  - internet
  - support
---

{{< figure src="./speedtest-graph-att-dropoff.png" alt="AT&T Fiber Internet - speedtest graph" width="500" height="auto" class="insert-image" >}}

About a week ago, my home Internet (AT&T Fiber) went from the ~1 Gbps I pay for down to about 100 Mbps ([see how I monitor my home Internet with a Pi](/blog/2021/monitor-your-internet-raspberry-pi)). It wasn't too inconvenient, and I considered waiting it out to see if the speed recovered at some point, because latency was fine.

But as you can see around 7/7 on that graph, the 100 Mbps went down to about _eight_, and that's the point where my wife starts noticing how slow the Internet is. Action level.

So I fired up AT&T's support chat. I'm a programmer, I can usually find ways around the wily ways of chatbots.

Except AT&T's AI-powered chatbot seems to have a fiendish tendency to equate 'WiFi' with 'Internet', no doubt due to so many people thinking they are one and the same.

{{< figure src="./att-chatbot-slow-internet-not-wifi.png" alt="ATT Chatbot - Slow Internet not WiFi" width="500" height="auto" class="insert-image" >}}

We were stuck in that loop for about 5 minutes.

> It looks like you're having trouble with your WiFi.
>
> _No._

After working a few different angles, I finally 'spammed 0'[^olddays] by entering some variation of 'connect me to a support rep'.

I'll cut to the chase—after repeating some variation of that about 8 times, eventually I got queued up in the 20 minute line to a human support rep.

Unfortunately for me, the human support rep, like so many in the industry, promptly ignored the data I provided in my first chat message to him[^message], and told me switching WiFi channels on the device (on which WiFi is currently disabled completely) would solve my issue. _At no cost._

{{< figure src="./att-chat-support-wifi.png" alt="ATT Support Rep - WiFi is not the problem" width="300" height="auto" class="insert-image" >}}

Maybe I should welcome our AI overlords?

[^olddays]: In the old days of phone support, if you got stuck in the automated menus, you could resort to spamming '0', and in _most_ systems that weren't set up by nefarious managerial overlords, that would get you to a human. Eventually.

[^message]: The entire contents of my message, prior to his turned-off-WiFi channel twiddling: "Hello! I just received and installed the new AT&T router/fiber modem, and ... the Internet speed is just as slow as before. I pay for 1 Gbps symmetric, and I'm getting 8 Mbps down and 6 Mbps up. On 6/28, the average connection speed went from 1 Gbps down to 100 Mbps. On 7/8 the average speed went from 100 Mbps to 8 Mbps.
This is all measured both on the device at the fiber, and through a separate monitor I have wired into the 1 Gbps network."
