---
nid: 3032
title: "Self-publishing and the 2nd edition of Ansible for DevOps"
slug: "self-publishing-and-2nd-edition-ansible-devops"
date: 2020-08-13T01:02:51+00:00
drupal:
  nid: 3032
  path: /blog/2020/self-publishing-and-2nd-edition-ansible-devops
  body_format: markdown
  redirects: []
tags:
  - amazon
  - ansible for devops
  - books
  - leanpub
  - self publishing
  - writing
---

Five years, 834 commits, and 24 major revisions later, I've just published the [2nd edition of Ansible for DevOps](https://www.ansiblefordevops.com), a book which has now sold over 60,000 copies and spawned a popular free [Ansible 101 video series](/blog/2020/ansible-101-jeff-geerling-youtube-streaming-series) on YouTube.

<a href="https://www.ansiblefordevops.com">{{< figure src="./ansible-for-devops-2nd-edition-cover-2x.jpg" alt="Ansible for DevOps, 2nd Edition - Cover" width="297" height="391" class="insert-image" >}}</a>

Making good on my promise to make the ebook updates free, forever, I've published a new revision of the book at least once a quarter since I published the first revision (version `0.42`) on LeanPub in 2014, and the second edition begins the `2.x` series of book revisions.

The book covers the basics of managing Linux servers, then dives deeper into continuous integration, application deployments, container image management, and even Kubernetes cluster management with Ansible.

## On Publishing, and 2nd Editions

I'd have been happy to keep the 'first edition' of the book updated free, forever, for everyone, on every platform. However, Amazon follows the old publishing tradition of "editions"—that is, any time you make more than a minor edit to a book (e.g. grammar and spelling corrections), you are supposed to publish an entire new edition, with a new (expensive) ISBN number, a new product listing, the whole nine yards.

It's a laborious process to publish a new edition, and if you purchase a book from most mainstream publishing companies, you might expect a good book to get updated once or twice in its lifetime—requiring a re-purchase of each new edition.

Since I discovered LeanPub, I knew that publishing model was outmoded, at least for tech books. I look at my bookshelf and see all the old hopelessly-outdated tech books, on 'Python 2', 'PHP 5', 'Red Hat 5 Server Administration'. Barring the fact that you can't push updates to paperbacks, people who buy digital copies should be able to take advantage of the fact that ebooks can update the contents of a book over time, and authors should be able to update their books easily (if they choose to do so).

What I set out to do—and I think I have accomplished, with Ansible for DevOps—was to maintain an evergreen definitive text for a particular piece of software that has evolved rapidly over the last five years. I've added chapters, and rewritten some chapters multiple times, and made the examples relevant, correct, and updated to follow evolving best practices and deprecation cycles as architecture shifts.

{{< figure src="./a4d-github-repo-contributors.jpg" alt="Ansible for DevOps on GitHub - Contributors" width="600" height="492" class="insert-image" >}}

The book even has a [companion GitHub repository](https://github.com/geerlingguy/ansible-for-devops), with its own set of [CI tests](https://travis-ci.org/github/geerlingguy/ansible-for-devops) for all examples in the book which runs weekly, alerting me to any examples which break due to bit rot over time.

Readers can also post issues to that repository and submit patches to fix any examples they find broken or confusing.

## Self-publishing makes sense for tech books

I've written on this topic a number of times, for example [Self-publish, don't write for a publisher](/blog/2016/self-publish-dont-write-publisher). It can be hard to get a book off the ground, but using a lean publishing platform like LeanPub allows you to begin writing and publishing your work immediately. Even while still writing, you can sell the partial book or engage interested readers to find whether there's interest in the book.

And self-publishing allows you to recoup at least 30-70% of the revenue from the book, instead of the meager 2-5% you usually get writing for a publisher.

In my case, I have what I'd call a very successful book, earning nearly $200,000 in royalties over the past five years<sup>1</sup>. If I had gone with one of the original publishing deals I had negotiated with a major publisher, where I would've gotten a few thousand dollars' advance, plus a 5% royalty rate, I'd have gotten less than $50,000.

Putting it in perspective, $200,000 over five years averages $40,000 per year. It's definitely something, but that revenue would not be enough to replace my salary, nor do I think my other book projects will match its success (though I'd love to be surprised!).

What I guess I'm saying is, if you have the talent to write a _good_ book on a specific cloud/computing topic, the salary you'd likely be able to get would be five or more times more valuable than the maximum revenue you'd get from publishing the book on the same topic.

So... don't quit your day job to write a book.

The best tech books I've read on any given subject come from daily practitioners knee-deep in the subject they write about, in real-world, money-on-the-line situations.

Many 'fluff' tech books (especially those written to fulfill a publisher's "we need a book on software X in our catalog" checklist) are written by light users of software or 'serial authors' who mostly write for a living and can't offer the deep insight or invaluable small tips that will save you hours and amplify your work by much more than the asking price of the book.

## Buy the book

You can buy Ansible for DevOps, 2nd Edition on [Amazon](https://www.amazon.com/gp/product/0986393428/ref=as_li_ss_tl?pf_rd_r=F7A7N736K694CX19J600&pf_rd_p=edaba0ee-c2fe-4124-9f5d-b31d6b1bfbee&linkCode=ll1&tag=mmjjg-20&linkId=c52e06824a0f3b4109e5d811b4d02116&language=en_US), [LeanPub](https://leanpub.com/ansible-for-devops), or [iBooks](https://books.apple.com/us/book/ansible-for-devops/id1050383787).

I'm also writing another book, [Ansible for Kubernetes](https://www.ansibleforkubernetes.com), that dives deeper into Kubernetes and container automation with Ansible, and you can purchase it while I'm still writing it on LeanPub—and just like with Ansible for DevOps, you'll get updates free, forever.

<sup>1</sup> That is, after 30-70% fees from Amazon, iBooks, and LeanPub—the latter being the most generous to authors. Note that royalty rates from publishers are usually on _top_ of store fees, so you get a proportionally worse amount per book—and often only after a certain number of sales (e.g. you get nothing until the book has earned at least $5 or $10k).
