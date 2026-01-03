---
nid: 3369
title: "Corporate Open Source is Dead"
slug: "corporate-open-source-dead"
date: 2024-04-25T16:38:43+00:00
drupal:
  nid: 3369
  path: /blog/2024/corporate-open-source-dead
  body_format: markdown
  redirects: []
tags:
  - cla
  - freedom
  - ibm
  - open source
  - programming
  - red hat
  - video
  - youtube
---

IBM is [buying HashiCorp for $6.4 _billion_](https://www.reuters.com/markets/deals/ibm-buy-hashicorp-64-billion-deal-expand-cloud-software-2024-04-24/).

That's four months after [HashiCorp rugpulled their _entire_ development community](https://www.hashicorp.com/blog/hashicorp-adopts-business-source-license) and ditched open source for the 'Business Source License.'

As [someone on Hacker News](https://news.ycombinator.com/item?id=40135490) pointed out so eloquently:

> IBM is like a juicer that takes all the delicious flavor out of a fruit

skywhopper replied:

> HashiCorp has done a good job of pre-draining any flavor it once had.

[Some people wonder](https://twitter.com/jgunnink/status/1783303926042996928) if HashiCorp's decision to drop open source was _because_ they wanted to juice the books for a higher price. I mean, _six billion dollars?_ And they're not even a pointless AI company!

> This blog post is a transcript of the video I posted today, [Corporate Open Source is Dead](https://www.youtube.com/watch?v=hNcBk6cwim8). You can watch it on YouTube.

Meanwhile, [Redis dropped the open BSD license](https://redis.io/blog/redis-adopts-dual-source-available-licensing/) and invented their own 'Source Available' license.

And last year, I covered how [Red Hat found a way to just _barely_ comply](https://www.jeffgeerling.com/blog/2023/im-done-red-hat-enterprise-linux) with the open source GPL license for their Enterprise Linux distro.

Other companies like MongoDB, Cockroach Labs, Confluent, Elasticsearch, and Sentry [also went 'Source Available'](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/). It started with some of the smaller players, but as rot sets in at even the biggest 'open source' companies, open source devs are choosing the nuclear option.

When a company rug pulls? Fork 'em. Literally!

Terraform, HashiCorp's bread and butter, was [forked into OpenTofu](https://opentofu.org/blog/the-opentofu-fork-is-now-available/), and adopted by the Linux Foundation. Companies who built their businesses on top of Terraform quickly switched over. Even juicier, OpenBao—a fork of HashiCorp's other big project Vault—is [backed by IBM](https://www.techtarget.com/searchitoperations/news/366563095/IBM-engineers-hatch-Linux-Foundation-HashiCorp-Vault-fork)! What's going to happen with _that_ fork now?

At least forks seem pretty straightforward in Hashi-land. In the wake of Redis' wanton destruction, it seems like there's a [new fork every week](https://arstechnica.com/information-technology/2024/04/redis-license-change-and-forking-are-a-mess-that-everybody-can-feel-bad-about/)!

And some developers are even exploring ditching the Redis code entirely, like [redka](https://github.com/nalgeon/redka)'s an API-compatible wrapper on top of SQLite!

After Red Hat closed its door—most of the way, at least they didn't try pulling a switcheroo on the license itself! Oracle, SUSE, and CIQ [scrapped together the OpenELA alliance](https://www.suse.com/news/OpenELA-for-a-Collaborative-and-Open-Future/) to maintain forks of Enterprise Linux. And CentOS users who'll be left in a lurch as June marks the end of CentOS 7 support have to decide whether to use AlmaLinux or one of the ELA projects now.

All these moves shattered the playbook startups and megacorps used—and now we're seeing, abused—to build up billions in revenue over the past decade.

It was all in the name of 'open source'.

As free money dries up and profits slow, companies [slash headcount](https://www.cnbc.com/2024/03/12/ibm-tells-employees-of-job-cuts-in-marketing-and-communications.html) almost as fast as community trust.

## 2024 is the year corporate open source died

2024 is the year Corporate Open Source—or at least any remaining illusions about it—finally died.

It's one thing to build a product with a proprietary codebase, and charge for licenses. You can still build communities around that model, and it's worked for decades.

But it's totally different when you build your product under an open source license, foster a community of users who then build their own businesses on top of that software, then yoink the license when your revenue is affected.

That's called a bait-and-switch.

Bryan Cantrill's been sounding the alarm for years—yes, _that Bryan Cantrill_, the one who posted this gem:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/tDacjrSCeq4" frameborder='0' allowfullscreen></iframe></div>
</div>

[Brian's presentation](https://www.youtube.com/watch?v=-zRN7XLCRhc) from 12 years ago is worth a watch, and the bottom line is summed up by [Drew DeVault](https://drewdevault.com/2023/07/04/Dont-sign-a-CLA-2.html):

> [Contributor License Agreements are] a strategy employed by commercial companies with one purpose only: to place a rug under the project, so that they can pull at the first sign of a bad quarter. This strategy exists to subvert the open source social contract.

By working on a project with a CLA, where you sign away your code, you're giving carte blanche for the company to take away your freedom to use their software.

From a company's perspective, if they want CLAs or if they want to use an anti-open-source license, they do _not_ care about your freedoms. They're protecting revenue streams. They'll often talk about freeloaders, whether it's Amazon building a competing hosted solution, or some startup that found a way to monetize support.

But in the end, even if you have GPL code and you charge people to get it, it's not truly free as in freedom, if the company restricts how you can use, modify, and share the code.

But there's a distinction here, and I know a few people watching this are already yelling at me. There's "free" software, and there's "open source."

People in the free software community [correctly identified the danger](https://www.gnu.org/philosophy/open-source-misses-the-point.html) of calling free software 'open source.'

I don't think we have to be so dogmatic about it, but there _is_ a fundamental _philosophical_ difference between the free software community, with organizations like the Free Software Foundation and Software Freedom Conservancy behind it, and the more business-oriented 'open source' culture.

Open source culture relies on trust. Trust that companies _you and I helped build_ (even without being on the payroll) wouldn't rugpull.

But time and time again, that trust is shattered.

Is this slow death of corporate open source _bad_? Well, it's certainly been annoying, especially for devs like me who felt connected to these communities in the past. But it's not _all_ bad.

## Why it's not bad for corporate open source to die

In fact, this could be a huge opportunity; what happened to the spunky startups like Ansible, HashiCorp, Elasticsearch, or Redis? They were lighting their industries on fire with great new software.

What happened to building up communities of developers, crossing cultural and economic barriers to make software that changed the world?

There are still projects doing that, but so many succumb to enterprise money, where eye-watering amounts of revenue puts profit over philosophy.

But as money dries up, as more developers get laid off after the insane hiring trends of the past five years, maybe small dev teams can move the needle.

The AI bubble hasn't popped yet, so some great people are getting sucked into that vortex.

But someone else could be on the cusp of the next great open source project. Just... don't add a CLA, okay?

And it's not just devs; big companies can join in. Historically bad players like Microsoft and _maybe even Oracle_—man, it pains me to say that. They've even made strides in the past decade!

IBM could even mend some wounds, like they could reunite OpenTofu and Terraform. There's precedent, like when [IO.js merged back into Node.js](https://thenewstack.io/io-js-and-node-js-have-united-and-thats-a-good-thing/) after a fork in 2015.

People asked what Red Hat could do to get me interested in Enterprise Linux again. It's simple: stop treating people who don't bring revenue to the table like garbage. Freeloaders are part of open source—whether they're running homelab or a competing business.

Companies who want to befriend open source devs need to show they care about more than just money. Unfortunately, the trend right now is to rugpull to juice the quarterlies, because money line always goes up!

But you know what? I'd just prefer honesty. If revenue is so dependent on selling software, just... make the software proprietary. Don't be so coy!

But to anyone who's not a multi-billion dollar corporation, don't be a victim of the next rugpull. The warning signs are clear: Don't sign a CLA. Stay away from projects that require them.

Stick to open source licenses that respect your freedom, not licenses written to juice revenue and prep a company for a billion-dollar-buyout.

Maybe it's time for a new open source rebellion. Maybe this time, money _won't_ change company culture as new projects arise from the ash heap. Maybe not, but at least we can try.
