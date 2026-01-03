---
nid: 3381
title: "Saying a lot while saying nothing at all about Ansible AWX"
slug: "saying-lot-while-saying-nothing-all-about-ansible-awx"
date: 2024-06-02T23:25:26+00:00
drupal:
  nid: 3381
  path: /blog/2024/saying-lot-while-saying-nothing-all-about-ansible-awx
  body_format: markdown
  redirects: []
tags:
  - ansible
  - awx
  - ciq
  - enterprise
  - open source
  - red hat
  - software
---

A few days ago, the post [Upcoming Changes to the AWX Project](https://www.ansible.com/blog/upcoming-changes-to-the-awx-project/) came across my feed. An innocuous title, but sometimes community-impacting changes are buried in posts like this. So, as an interested Ansible user, I read through the post.

In 1,610 words, almost nothing of substance was written.

A lot about how it's not 2014 anymore, so 2014-era architecture doesn't suit AWX. Then a big bold disclaimer at the bottom:

> Before we conclude, we should be clear about what will not happen.
>
> - We are not changing the Ansible project
> - We are not adjusting our OSS license structure
>
> Ultimately, we need to make some changes to the way our systems work and our projects are structured. Not a rewrite but a refactoring and restructuring of how some of the core components connect and communicate with each other.

The only references to the blog post I can find—_anywhere_—are a bunch of LinkedIn reposts, mostly parroting bits of the article like "Red Hat continues to innovate to drive the platform forward" and "it's not 2014 any more, so things need to change."

> **Disclaimer**: I don't use the community AWX automation platform, or Ansible Automation Platform (AAP) which uses AWX at its heart. I'm just an Ansible community member who used to work on AWX a little, and built the initial version of the AWX Kubernetes Operator.

I even asked on a couple posts—as an interested member of the Ansible community (Ansible is a core part of the AWX/AAP platforms)—if anyone had an idea of what kind of changes _could_ be coming. So far I haven't heard a response.

[One post](https://www.linkedin.com/posts/nathan-gore-932806123_upcoming-changes-to-the-awx-project-activity-7201977444222808065-6ldn/) from a Red Hat Solutions Architect may offer a clue:

> The open source AWX project will begin making significant changes to the way they develop and release updates. Although these changes will allow for faster innovation, it could impact future stability **making AWX a less attractive option for production environments**. [Emphasis mine]

The above statement, in tandem with the specific mention of not changing the OSS licensing structure, could point to AWX's releases not being quite as easy to run stably for production purposes. Not that a ton of people _do_ that—I tried a couple years ago and realized maintaining Jenkins (of all things) was easier for my small-business-sized Ansible automation needs.

This post isn't about the utility of AWX or AAP though. It's about figuring out what Red Hat means. I still don't know, but one commenter who replied to my question on LinkedIn might be on to something:

> Could this be related to CIQ's Ascender Automation product which is based on AWX, potentially pulling the rug from under their feet?

I honestly have never looked at [Ascender](https://ciq.com/products/ascender/) but it looks like it's a productized version of AWX, likely intended to compete with AAP, similar to how CIQ offers paid support for Rocky Linux, which competes with Red Hat Enterprise Linux. (_That_ fact stirred up quite a brouhaha last year...)

I've had zero confirmation about any of this, so it's entirely speculation... but I do wonder now, if CIQ is triggering another shift in Red Hat's product/community focus.

I don't think AWX has even a _fraction_ of the adoption CentOS used to, so I don't expect radical changes to the packaging/release will make as many waves. But it is something I'm intently following, since I rely on Ansible for a lot of my infrastructure—hopefully there are no ripple effects there!

It's also important to note Ansible (pre-buyout) maintained AWX née Ansible Tower as a proprietary product for many years, and after Red Hat purchased Ansible, they eventually open sourced AWX—which I [wrote about in 2017](/blog/2017/ansible-open-sources-ansible-tower-awx).
