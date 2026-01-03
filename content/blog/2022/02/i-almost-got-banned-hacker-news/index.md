---
nid: 3180
title: "I almost got banned from Hacker News"
slug: "i-almost-got-banned-hacker-news"
date: 2022-02-10T23:12:27+00:00
drupal:
  nid: 3180
  path: /blog/2022/i-almost-got-banned-hacker-news
  body_format: markdown
  redirects:
    - /blog/2022/time-i-almost-got-banned-hacker-news
aliases:
  - /blog/2022/time-i-almost-got-banned-hacker-news
tags:
  - community
  - ddos
  - etiquitte
  - hacker news
  - internet
---

{{< figure src="./hacker-news-front-page.png" alt="Hacker News frontpage - logged in as geerlingguy" width="700" height="153" class="insert-image" >}}

I started submitting my blog posts to Hacker News around 2016, but only ones I thought relevant to the HN community.

Until 2020, I would do this about once a week, and most submissions would fall off `/newest` within an hour, never to be seen again. But a problem arose (well, 'problem' depends on your perspective 😉): over time, more of my posts started hitting HN's front page.

HN is an interesting community—unlike Reddit, on which most material considered 'self-promotion' is _verboten_ (because so much is spammy resumé-boosting or corporate material), HN encourages _genuine_ self-promotion (at least judging by what hits the front page).

I think that comes down the the more entrepreneurial community surrounding the site—most of us have pretty good BS filters for pitches, and can tell when someone is only trying to sell something.

Most HN links aren't submitted by the original author—but many _are_, which _I_ tend to like. It feels like HN still has a real sense of online community (though I doubt I'll ever meet anyone I've conversed with on HN in real life—especially considering I live in 'flyover country').

## A `dang` warning

Back to my story, though: earlier this year, I think a critical mass of users were bothered by the fact that `(jeffgeerling.com)` links posted `by geerlingguy` kept hitting the front page—one time I think two articles frontpage'd on the same day! Eventually, this resulted in an email from dang (HN's primary moderator) cautioning against 'spammy' behavior, and encouraging me to 'slow my roll' so-to-speak.

Not to toot my own horn, but I'm a decent writer. I tend to be honest and open in my writing, and cover topics popular with HN users. That's a potent combo for hitting the front page.

Because of that, plus the fact that I now have some 'fans' in the HN audience, many of my posts get enough upvotes to hit the bottom of the front page, at least. And some of the more interesting ones rise up to the top before their rank decays over the next few hours.

> Prediction: This post will hit front page at some point, mostly because we HN users love nothing greater than navel-gazing and discussing our own little community :)

All that is to say, when you get an email from a site's main moderator<sup>1</sup>, you should probably take the words to heart. Which I did.

For the past few months, I limited submitting _my own_ content to a couple times per month.

Heck, at this point, there are probably enough people following this blog's RSS that someone will post an article within a day or two if it's interesting enough. Maybe I should just make a rule to never post any of my own content now that I have enough (albeit small-time) notoriety?

## But what about the ban?

Well, an interesting series of events played out over the past week, and it almost led to dang laying down the banhammer on my account—and I wanted to convey a bit of the story in hopes it can help people who _don't_ get to frontpage on HN but want to, to know how to do it _without_ risking the wrath of the HN community (and/or a permaban)!

Last week, I posted a video and blog post that complained of four issues I had with SpaceX's Starlink satellite Internet service. In the video itself, I even mentioned how discussing any Musk-related venture is—and I quote—"risky business."

That video quickly racked up more comments than any other video I've posted. The comments quickly separated into either "you are an entitled young white guy so stop whining" or "I totally agree that Starlink is evil and has no redeeming qualities" (I'm not even paraphrasing here...). Welcome to modern online discourse, I guess.

Anyways, with that backdrop, I also uploaded a video yesterday about [running _this website_ on a Raspberry Pi cluster on a farm](/blog/2022/hosting-website-on-farm-or-anywhere). And in the video I mentioned I'm _still_ hosting it over 4G (but at my home for now), and two risks are high data overage charges, and comments being a potential problem since they punch through my caching layer (and result in slower requests through the Pi's instances of Drupal and MariaDB).

I posted the story to HN, and within an hour it was rising up the front page. But it suddenly disappeared. Around the same time, I had a massive DDoS. At first I thought it was just a DoS and could be thwarted with some IP blocking... but then it got a lot more massive to the point I had to jump over to Cloudflare and limit all traffic to Cloudflare IPs—[full story for another day](https://github.com/geerlingguy/jeffgeerling-com/issues/141).

{{< figure src="./nginx-requests-before-ddos_0.png" alt="Nginx requests before and during DDoS" width="700" height="394" class="insert-image" >}}

Munin couldn't even catch up, but by my own log file reckoning, the VPS was handling at times over 4,000 requests per second, all punching through cache to my PHP/Drupal backend, and about 90% of the requests were erroring out.

It took an hour to figure out I wasn't going to be able to handle the new 2,000 requests per second average using Nginx and on-VPS firewall tricks. So I spent the next hour getting traffic routed through Cloudflare and putting a CDN-level block on all POST requests until the attack stopped.

After the mayhem resided (and I calculated about 350 Mbps of HTTP requests was hitting the server for over an hour), I got the following email from dang:

> [https://news.ycombinator.com/item?id=30273905](https://news.ycombinator.com/item?id=30273905) was heavily upvoted by a criminal spam service that steals accounts from HN users and then sells upvotes and comments using the stolen accounts. That's basically the equivalent of a capital offense on HN and we ban accounts and sites that do it.
> 
> Can you tell us about this?

Well, that's a fun message to read right after a DDoS attack...

## There's no shortcut to success

I've heard of places like "upvote club" (there are dozens of such services), but I have never and will never pay for a like, follow, or anything like that. I think that's some of the lowest scummy behavior on the Internet, and I strongly agree it's a "capital offense" in any online community.

Fortunately for me, dang gave me a chance to plead my case.

I explained my situation, reiterated that I'd never do it, and also asked around to make sure nobody in any of the communities I'm in ordered the upvotes. Nobody _said_ they did, so my current theory is it's _possible_ someone wanted to take me down a rung (maybe relating to Starlink, maybe trying to hit my wallet by throwing a ton of data through my 4G connection?), and this was definitely a good way to try ruining my Wednesday.

Fortunately, dang was satisfied with my informal investigation (though I still have no leads on what exactly happened in either case), and did not lay down the banhammer.

But he and I had a conversation about the problem in general, and we both agreed it might be good to post my experience.

Unlike many other communities, HN is still relevant and moderated enough that spammy behavior is almost always caught and punished. And as someone who's had a number of posts _organically_ hit HN's front page, I can give you the best advice for hitting the front page:

Write interesting, relevant content that the entrepreneurial community on Hacker News would like, and don't fill it with sales-y BS.

Also: most of your submissions will never make it to the front page.

Any kind of upvote ring (whether paid or an informal groups you ask to spam the upvote button on every post) will eventually get flagged, and often results in a ban.

There is no service—no matter how good their marketing sounds—that can push your post to the front page _and keep it there_. And for the tiny percentage that do stay, 99% of the time those posts wouldn't even need an illegal push!

Enough people read `/newest` that you should take no upvotes as a sign the content just wasn't as interesting as you thought. If you really want, wait a couple days and post it again (there's even a [second chance pool](https://news.ycombinator.com/pool) for hand-picked links that get picked up in a manual review process). If your submission stays off a few times in a row, move on to the next thing. It's no use beating a dead horse.

---

<sup>1</sup> [dang is superhuman](https://news.ycombinator.com/item?id=25225775); I honestly have no idea how he and the rest of the tiny group (is it still just him and sctb?) that moderates HN keeps it a _mostly_ civil place.
