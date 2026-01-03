---
nid: 3418
title: "Popular Rockchip SBC distro in limbo after maintainer burns out"
slug: "popular-rockchip-sbc-distro-limbo-after-maintainer-burns-out"
date: 2024-11-12T16:04:35+00:00
drupal:
  nid: 3418
  path: /blog/2024/popular-rockchip-sbc-distro-limbo-after-maintainer-burns-out
  body_format: markdown
  redirects: []
tags:
  - burnout
  - essay
  - level2jeff
  - open source
  - rockchip
  - sbc
  - ubuntu
  - video
  - youtube
---

Recently Joshua Riek posted [he's dropping off from GitHub](https://github.com/Joshua-Riek/ubuntu-rockchip/discussions/1104). If you haven't heard of him, he's one of the few reasons working with Linux on Rockchip SBCs is so much easier today than it was just a few years ago.

His [Ubuntu Rockchip distribution](https://github.com/Joshua-Riek/ubuntu-rockchip) is built for Ubuntu 22 and 24, and they've been maybe the most popular and stable way to run Ubuntu on Rockchip devices.

So popular, in fact, that manufacturers who use Rockchip, like [Turing Pi](https://docs.turingpi.com/docs/turing-rk1-flashing-os#image-types-and-download-source), build their own official images on top of Joshua's.

<p style="text-align: center;"><a href="https://xkcd.com/2347/">{{< figure src="./dependency-141873485.png" alt="XKCD Dependencies" width="300" height="auto" >}}</a></p>

Now, if you're reminded of [XKCD #2347](https://xkcd.com/2347/), yeah, I am too.

Basically, Rockchip, a company valued in the billions of dollars, can't be bothered to help SBC makers like Turing Pi with an official Linux distribution, so Turing Pi turned to Joshua's project and actually worked with him to try to get their hardware working better with it.

But from what I've heard, some other vendors—and I'm guessing a lot of individuals in the community—didn't treat Joshua with the respect that he deserves or with financial support in return for the help that he gave.

Sure, there are also other community distros like [Armbian](https://www.armbian.com), but when I think back to like five or so years ago before Joshua's distro and before Armbian was his mainstream, it was sometimes impossible to get Linux running stable on many Rockchip boards.

They usually support older LTS Linux kernels like 5.10 now and 6.1, and their RK3588 _might_ get support for 6.11 soon.

But that's all besides the point.

Today I wanted to talk a little bit about the maker-taker problem in open source.

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/4aaF2HgTVe8" frameborder='0' allowfullscreen></iframe></div>
</div>

## The Maker-Taker Problem in Open Source

Specifically, why Joshua is stepping away from his extremely popular distro and why this is happening more broadly in many areas of the open source ecosystem.

Because this problem with open source has only gotten worse, while the stakes get higher.

And just thinking back a few years, there's been Elasticsearch who changed their licensing after Amazon repackaged their products and sold hosting for them on AWS.

Red Hat took CentOS and changed the way it was packaged so it was much more difficult for downstream users to use that as their server OS.

Redis Labs changed Redis's license to make it harder for people to host it and sell that hosting.

Those are commercial enterprises that saw people reproductizing their own offerings and making money off of them. This problem reached a crescendo as we've witnessed Matt Mullenweg drag the Wordpress community through the mud this year in response to some WP Engine trademark issues that would've been better handled in court.

I'm not going to get deep into it, but it was a similar problem.

There are people who _make_ these products and the people who invest a lot of time and resources and people who might not put as much time and resources into making, but they _take_ from it and earn a lot of money off of it.

And the thing is that in all these cases, the license is the most important part for someone who's philosophical about open source or free software.

Sometimes these companies will even change their licensing.

And I think that's a pretty shady way of going about things.

If you license something free open source software with GPL or with some license that gives users freedoms, to attract developers to your ecosystem, then you start taking away those freedoms over time, that's pretty shady.

On the flip side, [most of my software](https://github.com/geerlingguy) is either MIT or GPL licensed.

I do a lot of work to build my software. People can take the work that I do and build a product that makes 20-40x the amount of money I'm ever going to make off of them.

Is that fair?

I mean, for me, I don't care that much, but for a lot of people, they _do_ care.

And a lot of people don't have the [safeguards that I've built up over the years](https://www.jeffgeerling.com/blog/2022/just-say-no) to prevent the burnout.

And, you know, that licensing side is one thing, but the open source community, I think is even more important, the community that you foster around your projects.

## Community

And my open source philosophy and my introduction to free software came out of Drupal, an open source CMS that's written in PHP.

It's still very popular. It's a lot different today than it was when I found out about it back when it was version 5.

The leader of Drupal, Dries Buytaert, wrote Drupal and he still is the [BDFL](https://en.wikipedia.org/wiki/Benevolent_dictator_for_life).

He works at a company called Acquia. I worked there for a short time, too; but they don't _own_ Drupal.

It's a little bit different approach than a lot of other open source software projects.

Drupal is a _community_ first.

There used to be a saying—I don't know how true this is anymore because I'm not as active in that community—but it was _come for the code, stay for the community_.

For a lot of software developers who are deep into the FOSS or open source ecosystem, it depends on where you came into it from.

For those of us in Drupal land, we came and saw this community of people working together to build up this project.

And we all found ways to monetize it for our own goals.

There are tons of companies that still exist that they do full-time Drupal development, and all of them are making tons of money off of it. Some of them contribute back more, some of them contribute back less.

But in Drupal, that community was part of the core part of what made you someone who did Drupal stuff. Many of the Drupal-centric company leadership were invested in the community.

Drupal has over the years built up this idea of contributions giving a company or individuals more prominence within the community, to the point where it's [incentivized through the tooling and development process](https://www.drupal.org/drupalorg/docs/marketplace/contribution-credit-weight-and-impact-on-ranking).

But that's not the only reason I think that Drupal has succeeded where a lot of other projects have floundered.

You have a central company that is not necessarily in control of it, Acquia, but they also _do_ have a lot of the people that are in the project's central kind of command structure.

But they all delegate that responsibility, to people in other companies, even some individuals working independently. Sure there's a board, there are political structures in place now... some of that can get annoying.

But it's worked over the years, it's different than a lot of other communities.

A _lot_ more wealth is created outside of just the core people who built Drupal or maintain it today.

And that's not a bad thing in the Drupal community—that's a _good_ thing.

My own personal software philosophy has always been, if I can build something that's cool, and someone else can take that and do something way cooler and way better and make tons of money off of it?

That's awesome.

I created more wealth in the world than I could have made personally—as long as I have food on my table, as long as I have mental health.

For _me_, I've built up safeguards to prevent burnout.

Plus, I have a YouTube channel and my books to supplement the income I get through [Patreon](https://www.patreon.com/c/geerlingguy) and [GitHub Sponsors](https://github.com/sponsors/geerlingguy).

But I'm always happy to see people build off my stuff.

Now, I don't want people stealing things that I _don't_ release with an open source license, like the text of my blog or my video content—even though that happens too.

But anything I release as open source, I'm glad when people take that and build off of it.

But some of this is tangential.

## Be liberal with your 'No'

The point I want to make today is some communities—especially communities that revolve around hardware like SBCs or electronics projects—sometimes people have roadblocks to that mentality that we had in Drupal that leads to a sustainable environment of contribution and support for each other.

Sometimes people are kind of prone to wearing themselves out and burning themselves out, especially if you don't have a community or don't have people around you that are watching for warning signs and trying to get you out of a rut like that.

And you know, I really hope that Joshua can come back and get the financial and emotional support he needs to thrive in his development process. For my part, I [sponsored him on GitHub](https://github.com/sponsors/Joshua-Riek) since I've benefitted from his work in the past.

Maybe we can get that Ubuntu project back up and running someday.

But I don't blame him for a second if he never comes back at all. That would be fine with me.

It can be harsh, especially coming from me who I maintain a ton of open source projects.

But for my own protection, I usually come in pretty hot and heavy and I close issues; I [use the stale bot](/blog/2020/enabling-stale-issue-bot-on-my-github-repositories), and I say no, probably more often than yes. And if something if a thread gets angry or discussion gets heated, I just ignore it.

It's not worth my time.

[I wrote in 2020](/2020/saying-no-burnout-open-source-maintainer):

> Be liberal with your no, and be judicious with your yes.

For me, that led to a ton of freedom to pursue my YouTube career. And also still maintain all the little open source projects that I want to use for my own good.

And if other people benefit from them, that's great.

If you don't like the way that I do it, _fork it_.
