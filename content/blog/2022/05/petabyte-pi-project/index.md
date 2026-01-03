---
nid: 3208
title: "The Petabyte Pi Project"
slug: "petabyte-pi-project"
date: 2022-05-18T14:00:56+00:00
drupal:
  nid: 3208
  path: /blog/2022/petabyte-pi-project
  body_format: markdown
  redirects: []
tags:
  - 45drives
  - broadcom
  - cm4
  - compute module
  - nas
  - raspberry pi
  - servers
  - sponsored
  - storage
  - storinator
---

I haven't had time to write up the details yet, but I wanted to share a project that's been many months in the making: [The Petabyte Pi Project](https://www.youtube.com/watch?v=BBnomwpF_uY) on YouTube.

I'm still doing follow-up testing based on feedback from Broadcom storage engineers, and will put out a much more in-depth blog post later, but the gist is:

_Can a single Raspberry Pi cosplay as an 'enterprise' storage server, directly addressing 1 PB of storage?_

Now... caveats abound here. What does 'enterprise' mean? And what does 'directly addressing' mean? Those things are all answered in the video linked above.

But to give a tl;dr: The Pi does _not_ perform swimmingly. But... I _did_ get a single array of 60 hard drives—20TB Exos HDDs to be exact—working in a 45Drives Storinator XL60 chassis, controlled only through a single Raspberry Pi Compute Module 4. Of course I had to rip out the Xeon guts and replace them with said Pi:

{{< figure src="./raspberry-pi-inside-storinator-xl60.jpeg" alt="Raspberry Pi Compute Module 4 and Broadcom LSI HBAs inside Storinator XL60 chassis" width="700" height="467" class="insert-image" >}}

Some snarky commenters will say "oh of course the Pi couldn't cope that well! It's a tiny SBC that's not built for it!"

But you're talking to the guy who's spent two years getting a GPU to work ([barely](/blog/2022/external-graphics-cards-work-on-raspberry-pi)) on a Raspberry Pi. And the guy who built a [$5,000 all-SSD Pi storage server](/blog/2021/i-built-5000-raspberry-pi-server-yes-its-ridiculous). If there was even a tiny _chance_ I could get my hands on a raw petabyte of storage, I was going to run this thing to its logical conclusion.

Watch the video linked above for the whole story (for now), and I have to say an incredibly huge thank you to 45Drives, who sponsored this project and helped in so many ways (and to some Broadcom engineers who have been immensely helpful along the way).

45Drives even shipped a custom faceplate enshrining [Red Shirt Jeff](https://redshirtjeff.com)'s favorite weapon of destruction on the front of the thing:

{{< figure src="./storinator-xl60-1.2pb-hdd.jpeg" alt="Storinator XL60 chassis - Red Shirt Jeff edition" width="700" height="467" class="insert-image" >}}
