---
nid: 3022
title: "Ansible 101 live streaming series - a retrospective"
slug: "ansible-101-live-streaming-series-retrospective"
date: 2020-06-26T19:37:28+00:00
drupal:
  nid: 3022
  path: /blog/2020/ansible-101-live-streaming-series-retrospective
  body_format: markdown
  redirects: []
tags:
  - ansible
  - livestream
  - statistics
  - video
  - youtube
---

{{< figure src="./ansible-101-retrospective.jpg" alt="Ansible 101 Retrospective" width="600" height="338" class="insert-image" >}}

In late March, as the COVID-19 pandemic hit the US, I decided to [make my Ansible books free](/blog/2020/you-can-get-my-devops-books-free-rest-month) to help people level-up their skills at home. That offer was generously [extended](/blog/2020/my-devops-books-are-free-april-thanks-device42) by Device42 in April.

Something happened that I never expected, but in hindsight is pretty amazing: [while the books were free, paid sales went up 400%!](/blog/2020/i-gave-away-my-books-free-and-sales-increased-4x).

Anyways, in the midst of that, I also realized after [getting my equipment in order for live streaming](/blog/2020/how-i-livestream-obs-sony-a6000-and-cam-link), I could teach a free 'Ansible 101' course on YouTube. So I [asked people if they'd be interested](https://twitter.com/geerlingguy/status/1241538147126775809), got a very enthusiastic 'YES', and tried to make a concise but somewhat entertaining live series on all things Ansible.

{{< figure src="./ansible-101-livestream-episode-7.jpg" alt="Ansible 101 Live Stream Episode 7 - Jeff Geerling" width="600" height="348" class="insert-image" >}}

I wanted to make the series relevant as a live stream, but also relevant for people watching after the fact. To that end, I actually updated many parts of [Ansible for DevOps](https://www.ansiblefordevops.com) while prepping for each week's stream, and will be releasing the 24th revision of the book in a couple weeks.

I also used YouTube's new [chapters](https://support.google.com/youtube/answer/9884579?hl=en) feature, and added topical chapter markers to _every_ video. This took... a long time, but I hope it helps people navigate the 15 hours of video content I've put together.

If you want to see _all_ the videos with chapter markers linking to each section on one overview page, head to my original [Ansible 101 blog post](/blog/2020/ansible-101-jeff-geerling-youtube-streaming-series), which I've kept updated every week.

## Statistics

{{< figure src="./watch-hours-per-episode.png" alt="Watch Hours Per Episode on YouTube Live streams" width="498" height="233" class="insert-image" >}}

For the above graph, keep in mind that the longer an episode is available, the more time it has to accrue views. This graph will likely change a bit over time. Also Episode 1 is an outlier; YouTube's recommendation algorithm disproportionately displays that episode to people, so it's viewed by more casual viewers who may not follow the entire series.

As of June 25, here are some of the most interesting statistics:

  - In total, there have been **106,000 views** of individual episodes.
  - People have watched for **22,388 hours** (that means people watch, on average, about 21 minutes per episode)
  - There were over **2,200 live chat messages** (and I actually learned some new features of Ansible and Molecule reading those messages, thanks!)
  - YouTube AdSense revenue totaled around **$400**

### Global Reach

One of the things that most amazed me was the global audience. People from over 50 countries participated in live chat:

{{< figure src="./ansible-101-global-audience.png" alt="Ansible 101 - Global Audience" width="589" height="371" class="insert-image" >}}

Ansible is a tool that is used for infrastructure automation around the world, and even though a few of the timezones were a bit off (apparently some people in Australia were staying up at 1 a.m. local time to catch the streams live!), it was incredible getting to see all those different perspectives in chat, and the interest in learning new things together.

> Note: To generate the data above (as well as some other statistics I'll go over in the final episode), I used [YouTube Chat Crawler](https://github.com/geerlingguy/youtube_chat_crawler) to download transcripts of all the episodes' live chat.

### Making Money with YouTube

That last metric can be broken down further: on average, I spent 3.5 hours prepping for each live stream, 1 hour _doing_ the live stream, and then 1 hour doing post-production (setting chapter markers, reading chat messages, downloading the recording, etc.).

So each video averaged $30 in ad revenue, and by ad revenue alone, the total _hourly_ wage equivalent based on direct video revenue is... **$5.45/hour**.

Subtract the cost of the equipment I use for the streaming (~$1,000, most of it used, though I already owned it), and now I'm a bit in the hole!

So, kids, don't quit school and become a YouTuber. As in other walks of life, the people who make a living off video content alone (or even sponsorships) are outliers. For most people who produce video content like I do, we make the money we need to sustain our family off of other ventures, and the video content adds something of a 'halo effect' for our 'brand'. (Dang it, I'm sounding more like a marketer than a programmer now... I feel icky.)

## Overall Impressions

I'm very happy I did this. There were viewers from at least 50 different countries (just based on live stream chat history). And every now and then I'd see a message from someone in the Ansible community who _I_ look up to, thanking me for my work. That felt wonderful!

And unlike most of YouTube, the comment section was mostly supportive and helpful, as many people provided even more background or links to relevant information that I could not provide in the time-boxed videos.

I also gained a lot of experience through the series, like learning more [OBS](https://obsproject.com) tricks and techniques, and finding ways to prep for an hour-long live broadcast each week without going insane.

And thanks to Device42's sponsorship, I was also able to acquire a new 16" MacBook Pro, which came at the perfect time, since my 2016 13" non-TouchBar model had a ballooning battery and started screaming at me every time I tried to stream at 1080p.

It was also neat seeing two other friends in the open source community try their hand at streaming after seeing some of my streams. Just like my experience sharing notes about my [writing process](https://www.jeffgeerling.com/tags/writing), it's inspiring to see other people follow my path, usually doing even better! I like the phrase 'good artists copy; great artists steal'—I like to put the things I do out there, in hopes that other people see something good and make it great.

That's why I do open source work. And even though it's counter to some in the FOSS world's mindset of being in the spirit of truly 'Free' software, I license almost all my computing work with the MIT license, because I want anyone, anywhere, to be able to take, copy, and improve any of my work, no holds barred.

And to that end, I guess this post wouldn't be complete without a short plea to consider [sponsoring me on GitHub](https://github.com/sponsors/geerlingguy) or [supporting me on Patreon](https://www.patreon.com/geerlingguy).

I have the amount I get from those sources public, and it floored me to see that, through the entire run of the COVID-19 pandemic (so far... I'm in the US so we're far from over the first wave), my sponsorship revenue has increased by 10x. It's part of my goal to find a sustainable way I can support my [hundreds of automation projects](https://ansible.jeffgeerling.com) and continue publishing free educational content [on YouTube](https://www.youtube.com/c/JeffGeerling) and on this blog.
