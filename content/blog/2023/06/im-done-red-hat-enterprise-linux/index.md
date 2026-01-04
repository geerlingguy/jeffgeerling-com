---
nid: 3294
title: "I'm done with Red Hat (Enterprise Linux)"
slug: "im-done-red-hat-enterprise-linux"
date: 2023-06-26T13:59:30+00:00
drupal:
  nid: 3294
  path: /blog/2023/im-done-red-hat-enterprise-linux
  body_format: markdown
  redirects: []
tags:
  - linux
  - open source
  - red hat
  - video
  - youtube
aliases:
  - /comment/32434
  - /comment/32309
  - /comment/32286
  - /comment/32298
---

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/kF5pyVUQBH8" frameborder='0' allowfullscreen></iframe></div>
</div>

Two years ago, Red Hat killed CentOS, a widely-used free version of their Enterprise Linux distribution.

The community of CentOS users—myself included—were labeled as 'freeloaders', using the work of the almighty Red Hat corporation, without contributing anything back. Don't mind all the open source developers, Linux kernel contributors, and software devs who used CentOS for testing and building their software. Also ignore the fact that Red Hat builds their product on top of _Linux_, which they didn't build and don't own.

> **Update**: I had forgotten about this, but Red Hat had, in fact, promised to keep the git sources open following the CentOS move in 2020. See [LearnLinuxTV's post](https://www.learnlinux.tv/how-red-hats-open-source-negligence-is-doing-actual-harm-to-the-linux-community-and-enterprise-it-in-general/) for more on that. This change is also causing considerable grief downstream for distros like [SDL/PUIAS](https://groups.google.com/g/springdale-users/c/53hFsR7oLEQ?pli=1) (a RHEL downstream that's been maintained since before even CentOS existed)—but they are collateral damage at this point.

I almost wrote off Red Hat back then. It felt like someone stuck a knife in my back.

This past week, Red Hat took that knife and twisted it _hard_, when they published [this blog post](https://www.redhat.com/en/blog/furthering-evolution-centos-stream). Let there be no mistake: this was meant to destroy the distributions the community built to replace what Red Hat took away.

There were only two things that kept me around after Red Hat betrayed us the first time: First, instead of attacking the community of open source users, many Red Hatters reached out and asked, "How can we do better?" It didn't heal the wound, but it meant something, knowing someone at Red Hat would at least listen.

Second—and more importantly—[Rocky Linux](https://rockylinux.org) and [AlmaLinux](https://almalinux.org) stepped in. They prevented a mass-exodus from the Red Hat ecosystem, giving developers like me a stable target for my open source work. But Rocky and Alma relied on Red Hat sharing their source code.

Here's how it used to work:

  1. Red Hat would grab a copy of Linux
  2. They would add magic sauce that makes it Red Hat Enterprise Linux
  3. They would release a new version
  4. They would update a source code repository with all the data required to build it from scratch

That's kinda the status quo because in open source, the source... is open! And it doesn't matter if someone who uses your source benefits from it too... that's kind of what it's all about! We all benefit from sharing our work, and in this case, the [GPL license](https://www.gnu.org/licenses/old-licenses/lgpl-2.0.html) Linux uses legally _requires_ us to share it!

Without that sharing, there would be no Debian, Arch, Mint, Ubuntu, PopOS, Fedora... or any of the other hundreds of Linux distros that build on each other and prop up the community.

But Red Hat decided to put the source code behind a paywall. Now, this _is_ legal. Technically, the GPL allows it. But it's generally rude and annoying to do that when the code you're locking down is largely based on _other people's_ open source code.

But... it's within their rights, so I won't argue that point. What I _will_ argue is the current subscription agreement, which might not be legal. Red Hat currently says they can cancel any user's account if they download the source code and redistribute it.

Let's say someone downloads the source through a Red Hat subscription, and uses that to build a new version of Rocky Linux. If Red Hat retailiated by _cancelling_ that subscription, I'd definitely tune into that court case.

I don't know if the community could front the money to take on IBM's powerful laywers—maybe that's what Red Hat's banking on. But there's another player in this game who might, and that's Oracle. Wouldn't it be ironic if _Oracle_ were the ones who knocked Red Hat down a peg for being so uppity with their abuse of their community!

But let me be clear: everything I've seen points to Red Hat trying to choke out downstream distros like Rocky, Alma, and Oracle Linux. I think their hope is users of those distros would get scared and sign up for a Red Hat subscription. They need this to happen to lock in some short-term profits to please their IBM overlords. That's my cynical take on it.

What Red Hat's doing is skirting right on the edge of legality the terms of Linux's GPL License. If you wanna dig into that, read [this post](https://sfconservancy.org/blog/2023/jun/23/rhel-gpl-analysis/) from the Software Freedom Conservancy.

{{< figure src="./rhel-ghandi-quote.jpg" alt="RHEL Gandhi Quote" width="700" height="386" class="insert-image" >}}

Red Hat used to be the company of rebels. They used to have edgy ads [quoting Gandhi](https://youtu.be/FztGWaP8v2Q?t=182) and positioning Red Hat as the plucky underdog, using open source to upend the old proprietary software companies.

It's funny they used to be so devoted to that Gandhi quote in particular. In one sense, Red Hat kinda won, they're the default choice for running Linux in big companies.

The irony is that Cory Doctorow recently [wrote this](https://www.wired.com/story/tiktok-platforms-cory-doctorow/) about a _different_ company, but I think it applies here:

> HERE IS HOW platforms die: First, they are good to their users; then they abuse their users to make things better for their business customers; finally, they abuse those business customers to claw back all the value for themselves. Then, they die.

What a juxtoposition!

They built up so much goodwill in the open source community through the years and used to be known as the 'open source company.'

But they're throwing away that goodwill—at least as far as Linux is concerned—all in the name of profit.

Developers like me, [maintainers of the EPEL repository](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/F35UTCBYF25XRE2HX32UEIRVZGMAXIBO/), [Fedora maintainers](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/Q6LJZKB24D3IQZ7AMKO35NW6VIWENEK2/) who are rightfully worried about the long-term impacts...

We're all being told to go sign up for a Red Hat Developer Account so we can snag our 16 licenses[^1] of Red Hat Enterprise Linux for testing.

Oh boy!

Thanks, I guess I'll drop doing something _actually productive_ and spend a week retooling my test infrastructure and automation to work with Red Hat licensing.

You know who _doesn't_ require me to do that?

Debian. Ubuntu. FreeBSD. Not even Rocky Linux!

And please tell your employees to stop patronizing me, saying I should just use CentOS Stream. There's a reason Rocky and Alma linux have been downloaded _millions_ of times. Stream is not a substitute for CentOS.

So I've [dropped support for Enterprise Linux](/blog/2023/removing-official-support-red-hat-enterprise-linux) on all my work, effective last Friday.

And people are asking me about Ansible. That's the Red Hat Ansible Automation Platform (by IBM), by the way.

I don't _think_ Ansible's gonna try locking down access, but the fact I have to spend even a _second_ considering that possibility is insane!

Who wants to build around an ecosystem where the open source users are called freeloaders and where massive disruptions are implemented in the middle of a release cycle, _two times in a row_, with _no warning_?

I don't see this helping Red Hat in any way in the long term.

In the end, this is just sad:

  - It's sad for users like me who used CentOS and developed tools on it that on-ramped folks into Red Hat's ecosystem.
  - It's sad for Red Hat, which used to fight for open source, but now puts up barriers around their own source code.
  - It's sad for everyone still _in_ their ecosystem, because they're now _forced_ to deal with Red Hat's licensing shenanigans and the loss of so many in the open source community.

[Rocky Linux](https://rockylinux.org/news/brave-new-world-path-forward/) and [AlmaLinux](https://almalinux.org/blog/impact-of-rhel-changes/) both announced they'll find a way forward. I hope they can, if nothing else so people who stuck with Red Hat don't get burned again.

But as for me? I'm done with Red Hat Enterprise Linux.

I'll keep up support for Rocky Linux and AlmaLinux on a best-effort basis, but I have no confidence I'll be able to support Enterprise Linux moving forward.

Fool me once, shame on you. Fool me twice...

[^1] Red Hat _seemed_ to be [upping the limit to 240 sockets per developer](https://twitter.com/fareszr/status/1673145072714665984), but now it seems that was just a bug.
