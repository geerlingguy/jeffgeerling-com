---
nid: 3072
title: "Kubernetes 101 series retrospective, and a new book!"
slug: "kubernetes-101-series-retrospective-and-new-book"
date: 2021-02-10T15:49:23+00:00
drupal:
  nid: 3072
  path: /blog/2021/kubernetes-101-series-retrospective-and-new-book
  body_format: markdown
  redirects:
    - /blog/2021/kubernetes-101-series-and-my-new-self-published-book
aliases:
  - /blog/2021/kubernetes-101-series-and-my-new-self-published-book
tags:
  - devops
  - kubernetes
  - self publishing
  - video
  - writing
  - youtube
---

Early in 2020, I kicked off the [Ansible 101](/blog/2020/ansible-101-jeff-geerling-youtube-streaming-series) live streaming series. I wrote an [Ansible 101 retrospective post](/blog/2020/ansible-101-live-streaming-series-retrospective) and decided to give it another go, this time covering _Kubernetes_.

Starting late in 2020 and wrapping things up today, I streamed a new 10-episode series, [Kubernetes 101](https://kube101.jeffgeerling.com) (the first episode is embedded below).

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/IcslsH7OoYo" frameborder='0' allowfullscreen></iframe></div>

This time I had an official series sponsor, I built a [custom website](https://kube101.jeffgeerling.com) and [dedicated GitHub repo](https://github.com/geerlingguy/kubernetes-101) for the project, and poured in 3-4x more hours per episode... which resulted in a marginal increase in viewership, but not nearly as much as I'd hoped going into my second tech livestream series.

Let's dive into some numbers:

## Statistics

Here's a breakdown of watch hours per episode (through the first nine):

{{< figure src="./watch-hours-per-episode_0.png" alt="Watch Hours Per Episode for Kubernetes 101" width="800" height="500" class="insert-image" >}}

You can see a pretty big drop-off after the first episode. I've found that to be typical with any kind of episodic content on YouTube (I see a similar thing for my [Raspberry Pi Cluster series](https://www.youtube.com/watch?v=kgVz4-SEhbE&list=PL2_OBreMn7Frk57NLmLheAaSSpJLLL90G) and my [Drupal 7 to 8 Upgrade series](https://www.youtube.com/watch?v=EyI_OwhufNk&list=PLABA8061522EEA245&index=17). YouTube seems to promote the first episode a _lot_, and barely even suggests any others.

Here are a few other relevant stats a couple months in (note that these numbers will go up over time—these are as of Feb 9, 2021):

  - Kubernetes 101 episodes have had **124,500 views**
  - People have watched for **23,684 hours**
  - YouTube AdSense revenue totaled around *$699.33**

Compare that to the [Ansible 101 live streaming series retrospective](/blog/2020/ansible-101-live-streaming-series-retrospective) (when my YouTube channel was around 10x smaller). The revenue is appreciably higher, but so was the number of hours I worked prepping these ten episodes!

## Is it worth it (money-wise)?

Each video averaged $69 in ad revenue (nice), and required around 10 hours of work to produce (including the time spent live streaming each Wednesday). By ad revenue alone, the total hourly wage equivalent is **$7/hour**.

Sponsorship bumps that number a bit, but we're still talking less than a quarter my consulting rate.

That number also doesn't account for the ~$1,000 of extra equipment I use to live stream. As I've been [transitioning from blogging to YouTube](/blog/2020/transition-blogging-youtube-my-experience), I've learned that episodic or open-ended livestreams don't tend to do well in tech, even though they can often do so for other genres like gaming.

It's always good to look back on projects like this and question at the end if it's worth it—both in terms of the monetary reward, and the intangibles.

## Is it worth it (otherwise)?

So here's the million-dollar-question: would I have rather built a pre-recorded course for one of the traditional learning platforms like Pluralsight or Udemy, or done this streaming series?

Well, this year my goal has been to break out and do my own thing. Being put into a schedule and content framework controlled by others is not _that_.

So I think it was worth it from the 'I accomplished this' perspective, but slightly less worth it from the 'the immediate benefit is worth the investment' perspective.

However...

## Publishing a new book using the series' content

I decided that I could extend the shelf-life of the content I spent so many hours building up (I mean, who else builds full CI coverage for examples in _video_ content?). So I turned the series into [a book with the same name](https://www.kubernetes101book.com):

<p style="text-align: center;"><a href="https://www.kubernetes101book.com">{{< figure src="./kubernetes-101-cover-2x.jpg" alt="Kubernetes 101 Book Cover" width="260" height="390" class="insert-image" >}}</a></p>

Like my two current self-published books ([Ansible for DevOps](https://www.ansiblefordevops.com) and [Ansible for Kubernetes](https://www.ansibleforkubernetes.com)), I'm a firm believer in _self-publishing_ so I can write—and keep updated—the best technical content.

So I'm translating all the content I made for the video series into written form, in the book [Kubernetes 101](https://www.kubernetes101book.com), which I've already started publishing on LeanPub (pre-completion). If you get the book from LeanPub, you get DRM-free updates to the book, free forever.

Once I finish writing the first 'final' version, I'll also be publishing on Amazon and iTunes, along with a paperback version through Amazon's Kindle Direct Publishing.

I've [blogged quite a bit about self-publishing in the past](/tags/self-publishing), and I'd encourage you to consider it. Most of the time, especially for first-time tech authors, the terms of a publishing deal are tilted _extraordinarily_ heavy in the publisher's favor. If you have a breakout success, wouldn't it be nice to see some of the profits from it?

And if not, it's better to get 70% of a pittance than almost nothing.
