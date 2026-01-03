---
nid: 3302
title: "Fork Yeah! Examining open source history after Red Hat's move"
slug: "fork-yeah-examining-open-source-history-after-red-hats-move"
date: 2023-08-09T15:31:16+00:00
drupal:
  nid: 3302
  path: /blog/2023/fork-yeah-examining-open-source-history-after-red-hats-move
  body_format: markdown
  redirects:
    - /blog/2023/fork-yeah-examining-open-source-history-light-red-hats-move
aliases:
  - /blog/2023/fork-yeah-examining-open-source-history-light-red-hats-move
tags:
  - centos
  - linux
  - open source
  - oracle
  - red hat
  - solaris
---

We're at the stage in the Red Hat drama where everyone is consulting history, trying to figure out what parts are being repeated in 2023 after [Red Hat effectively locked down the sources used to build RHEL clones](/blog/2023/im-done-red-hat-enterprise-linux).

One talk linked quite often was [Fork Yeah! The Rise and Development of illumos](https://www.youtube.com/watch?v=-zRN7XLCRhc), by Bryan Cantrill over a decade ago. Bryan was a software engineer at Sun, who went over to Oracle after the buyout, then left to join Joyent, and now resides as CTO of Oxide.

The talk focuses on Sun Microsystem's handling of Solaris and OpenSolaris, both before and after their Oracle acquisition, and the whole talk is worth a listen—so much context about the history of ZFS, Solaris, Illumos, dtrace, and even UNIX and Linux history are contained within.

But there was one section (around the 32:00 mark) where if you substitute "Red Hat" for "Sun," rhymes with this year's "open source company" drama:

> I went back and looked at some of the mail trails about this and like, "oh, my God!"
> 
> It's like you look at the number of words spent on this—words from bright people that can actually write code instead of writing this, and they're writing just this—huge screens and so on, and it was just sad. Very, very sad, and a huge waste of time.
> 
> And it was entirely avoidable on the one hand, understandable on the other, because _those strings were just too tempting for Sun to pull_.
> 
> And sadly, what this ultimately ended up doing is really deflating the community because it was clear Sun couldn't tolerate an independent OGB. And I don't think this is necessarily a problem with Sun.
> 
> I actually think that Sun's intentions were as good as a company's could possibly be. But it's just a company has it's own interests.
> 
> And it's very hard, when that company has created this open-source community from scratch, populated it effectively from scratch, it's very hard for it to not think of that community as belonging to it.
> 
> And that's not the way the community thinks. So this is really a challenge you have when you're leaving this proprietary chasm.
> 
> But the community was very deflated by this.

I was especially saddened the way Red Hat leadership—and even in some interpretations, [long-time veterans of Linux and the open source movement](https://www.lpi.org/blog/2023/07/30/ibm-red-hat-and-free-software-an-old-maddogs-view/)—has positioned the downstream "community" of those who build and run distributions like AlmaLinux and Rocky Linux. I won't deal with Oracle here because they are such a different entity and—well, listen to the video linked earlier starting around 33 minutes for a good screed against Oracle!

But when I read the following line in Red Hat's blog post:

> Simply rebuilding code, without adding value or changing it in any way, represents a real threat to open source companies everywhere. This is a real threat to open source, and one that has the potential to revert open source back into a hobbyist- and hackers-only activity.

I was especially crushed. Bryan's speech especially highlighted the importance of hobbyists and hackers to a healthy OS distribution. Projects like ZFS, dtrace, vim, et all are often the brainchild of one or two developers, and would never happen based solely on bureaucratic development practices of a giant software corporation.

Many said Red Hat's _communication_ is the problem, not the decisions themselves. I'd agree to a small extent, but with the caveat that the _timing_ has been excruciatingly poor, considering the RHEL release cycles and community expectations.

Mike McGrath pointed out Red Hat never promised 10 years of support for CentOS 8 in a [recent LinkedIn post](https://www.linkedin.com/feed/update/urn:li:activity:7092971748249251841?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7092971748249251841%2C7093188261388423169%29&replyUrn=urn%3Ali%3Acomment%3A%28activity%3A7092971748249251841%2C7093377246446424064%29):

> **Red Hat never said CentOS8 would be supported for 10 years and were careful not to.** We should have made it clear that we were in negotiations with the board at that time about its lifecycle and that was the major folly. A community member, not knowing better updated the wiki to say 8 would last for 10 years because he simply thought that's what it would be (which was an entirely reasonable thing to do).

In this case, it sounds like the intention was to drop CentOS 8 but not all internally were willing, so it got released, then nerfed a couple years in.

Then, after [promising sanitized RHEL git sources on git.centos.org](https://www.centos.org/distro-faq/#q3-will-the-source-code-for-red-hat-enterprise-linux-continue-to-appear-on-gitcentosorg), that was revoked a couple years into the RHEL 9 release cycle—and this time, the change was implemented behind the scenes a couple weeks _before_ it was announced publicly.

Regardless of the worth of the downstream 'rebuilder' communities, the fact that an open source project's community has expectations that are continually unmet—whether or not they pay Red Hat—has a chilling effect on non-paying users of any software projects touched by Red Hat.

That's what saddens me. Just like the downfall of Sun, and the subsequent [lawn-mowering](https://news.ycombinator.com/item?id=15886728) of their open source assets by Oracle, I can't help but draw some parallels with the viewpoint that GPL licensed projects at Red Hat are viewed as being compliant if they upstream development, but [chill the sharing of downstream source code](/blog/2023/i-was-wrong) with restrictive service agreements.

It is only RHEL today, but this pernicious behavior towards downstream community doesn't leave a good taste in the mouth. And the response from many Red Hat employees was not one of compassion and reconciliation, but one of vitriol and defensiveness.

Community projects like Alma and Rocky Linux have gone their different ways, but in hindsight, both downstream communities have proven (at least to _me_) the value of the individual contributors within—from submitting patches to Stream, to maintaining EPEL repositories, to promoting and contributing to Fedora, there is a lot of value pointed _directly_ into Red Hat's own projects from downstream rebuilder communities.

It saddens me that the first instinct within Red Hat is to defend the business concerns, while barely listening to community concerns. Red Hat must make a profit—and indeed, [they just increased revenue 11% quarter-over-quarter](https://techcrunch.com/2023/07/21/red-hat-ibm-earnings/) (one of the few bright spots on IBM's balance sheet this year).

But it's especially saddening to see the extreme defense of the business after that 11% increase, the quarter after the first mass layoff at Red Hat in over a decade, when [4% of staff were fired](https://www.redhat.com/en/blog/message-red-hat-associates-today).
