---
nid: 2959
title: "Ansible for Kubernetes, my second self-published book"
slug: "ansible-kubernetes-my-second-self-published-book"
date: 2019-12-20T15:01:24+00:00
drupal:
  nid: 2959
  path: /blog/2019/ansible-kubernetes-my-second-self-published-book
  body_format: markdown
  redirects: []
tags:
  - ansible
  - ansible for devops
  - ansible for kubernetes
  - books
  - self publishing
  - writing
---

<p style="text-align: center;"><a href="https://www.ansibleforkubernetes.com">{{< figure src="./ansible-for-kubernetes-cover-blog-post.jpg" alt="Ansible for Kubernetes book cover - by Jeff Geerling" width="308" height="399" class="insert-image" >}}</a></p>

Five years ago, I set out to write a book. For a topic, I picked Ansible, since I was familiar with the software, and noticed there weren't any other books about it. I struck gold with [Ansible for DevOps](https://www.ansiblefordevops.com), and have since sold over 22,000 copies between eBook and paperback copies.

I've [written about self-publishing before](/tags/self-publishing), and my opinion about publishing technical works is stronger than ever:

  - Don't write for a publisher (usually)
  - Use the [Lean Publishing](https://leanpub.com/manifesto) process

I wrote an entire article ([Self-Publish, don't write for a Publisher](/blog/2016/self-publish-dont-write-publisher)) on the first topic. Regarding the second topic, I see writing a technical book on the same plane as building a software project:

[_Version 1 sucks, but ship it anyway_](https://blog.codinghorror.com/version-1-sucks-but-ship-it-anyway/).

If I didn't start publishing Ansible for DevOps when I only had three rocky chapters, I wouldn't have gotten the early feedback that made the book a hundred times better. I also wouldn't have realized the demand there was for the book—I hoped for 100 sales, and planned on writing around 100 pages. Before I released version 1.0, I had [sold 2,000 copies and written 400 pages](/blog/25k-book-sales-and-im-almost-ready-publish)!

That blew my mind (and still does). Since releasing 1.0, I've published more than 20 major revisions. I update the book regularly across LeanPub, Amazon (Kindle and paperback), and iBooks<sup>1</sup>, and have received tons of feedback from my book's readers, who continue improving the book's relevance. I also have automated test coverage for the majority of the examples used in the book, so I can maintain and keep relevant all the different 'infrastructure cookbooks' inside.

## Building on success with my second book

With that in mind, I started working on a second book in late 2017. Unfortunately, [life got in the way](/blog/2018/colons-semicolons-and-crohns-surgery-oh-my). My body was almost literally committing seppuku, so I had a major surgery. My job was not helping much, as I got caught up juggling three concurrent stressful projects<sup>2</sup>.

Writer's block can be crushing when you don't have the strength to push through. It also didn't help that I have three active kids under 7, whereas I had one sleepy newborn while writing _Ansible for DevOps_! Luckily, I have been doing (mostly) good health-wise since mid-2018, and moved on from the stressful work environment.

And now I'm writing. I have almost four complete chapters, and an outline and material for at least five more. Just like _Ansible for DevOps_, I'm publishing book as I write it on LeanPub. And my book will always be DRM-free<sup>3</sup>, available in any format you like, with free updates forever.

## When will the book be complete?

That's a good question! If you asked me the same about Ansible for DevOps, I might say "never!", as the book has had four new chapters added throughout its 20 revisions, with two or three complete chapter rewrites for new Ansible versions. I don't use 'Editions' because that would gobble up precious ISBN numbers, require a drawn out process to get the new editions listed properly in all the bookstores, and is generally a heavyweight process that doesn't jive with lean publishing.

But I do hope to reach a version 1.0 by the end of next year.

So then the question is: _why should I buy the book today if it's not yet complete_?

The answer to that is easy: lean publishing means I already provide value through the partially-complete book—and you will get continuous improvements to the book as I update it. Another early-mover advantage is you can help shape the content of the book. There are a number of sections in _Ansible for DevOps_ which wouldn't be there without readers requesting their addition, and it will be the same for _Ansible for Kubernetes_.

## Why should I care about Ansible and Kubernetes?

One question I get a lot: _Ansible seems irrelevant in a cloud-native Kubernetes environment. Why write a book on these two orthogonal<sup>4</sup> technologies?_

I'd reply that I've never seen a complete, functional, maintainable, real-world infrastructure at a company which is 100% cloud-native, and integrates with zero extra-K8s-cluster resources, and requires no form of orchestration. Sure, there are a few apps which can run completely independent and stateless, and some teams can glue things together using serverless technologies.

But you almost always have to do things like tie an application into a separate cloud service, or link two systems together. Ansible excels at multi-cloud orchestration, and even integrates with Windows hosts and networking gear. It has thorough Kubernetes integration, and can be used to manage infrastructure resources and applications either standalone, or in tandem with other tools like Terraform.

The book explores the question in-depth, offering many solutions to common Kubernetes problems using Ansible. Though, I quote from the book itself:

> While Ansible _can_ do almost everything for you, it may not be the right tool for _every_ aspect of your infrastructure automation. Sometimes there are other tools which may more cleanly integrate with your application developers' workflows, or have better support from app vendors.
>
> Ansible is rarely used for everything in a cloud-native app lifecycle, but it's good to know that it _can be_ used, and is often easier to implement and maintain than other solutions.

Don't let 'cloud-native' become your [golden hammer](https://en.wikipedia.org/wiki/Law_of_the_instrument)<sup>5</sup>.

Some of the topics I cover or will cover in the book include:

  - Building Kubernetes clusters with Ansible
  - Managing managed Kubernetes (EKS, AKS, GKE, etc.) clusters with Ansible
  - Using Ansible in your container build, test, and deployment (CI/CD) workflows
  - Integrating Kubernetes apps with external resources with Ansible
  - The Operator SDK and Ansible-based Kubernetes operators

You might even learn a little bit of Go in the course of the first chapter!

## Where can I buy it?

You can [purchase Ansible for Kubernetes from LeanPub](https://leanpub.com/ansible-for-kubernetes) today, and no matter when you purchase it, you will get free updates for as long as I keep updating the book—hopefully until I'm no longer able to write!

<iframe width='160' height='400' src="https://leanpub.com/ansible-for-kubernetes/embed" frameborder='0' allowtransparency='true'></iframe>

---

<sup>1</sup>iBooks barely moves the needle on sales. I'm still not sure if it's worth the ~30 minutes per quarter it takes to update the book on iBooks, for the paucity of sales I see on that platform.

<sup>2</sup>What corporate software project _isn't_ that way? My problem was I was in the midst of _three_ of these... I could maybe handle one at a time!

<sup>3</sup>I see _Ansible for DevOps_ PDFs published to all kinds of seedy sites on a weekly basis, and some people have asked why I don't use DRM or file DMCA takedowns. Two reasons: that's a huge time commitment, and I just keep updating the book, so the free archived PDFs people find are never going to be as good as 'the real deal'!

<sup>4</sup>I avoid using this term, but found it funny it popped into my head here; I think the only times I've ever seen the term used is on Hacker News, when someone complains that two things everyone else are relating are, indeed, unrelated and should never be related. I imagine if this post gains any traction there, someone on HN will ask that exact question... and maybe use 'orthogonal' to describe Ansible and Kubernetes.

<sup>5</sup>Some argue Ansible is _my_ golden hammer. And they're probably right. But hey, I started out with PHP. Golden hammers are kind of our specialty.
