---
nid: 3291
title: "Self-published Ansible book \u2013 87k copies, 300k revenue, 41 revisions"
slug: "self-publishing-technical-book-10-years"
date: 2023-06-29T17:23:52+00:00
drupal:
  nid: 3291
  path: /blog/2023/self-publishing-technical-book-10-years
  body_format: markdown
  redirects:
    - /blog/2023/self-publishing-deeply-technical-book-10-years-87k-sales
    - /blog/2023/self-publishing-technical-book-10-years-87k-sales
    - /blog/2023/self-publishing-technical-book-10-years-–-87k-sales-41-revisions
aliases:
  - /blog/2023/self-publishing-deeply-technical-book-10-years-87k-sales
  - /blog/2023/self-publishing-technical-book-10-years-87k-sales
  - /blog/2023/self-publishing-technical-book-10-years-–-87k-sales-41-revisions
tags:
  - amazon
  - ansible for devops
  - books
  - ibooks
  - leanpub
  - self publishing
  - writing
---

I just published the 41st revision of my self-published book [Ansible for DevOps](https://www.ansiblefordevops.com), which has sold 87,234 copies as of this writing across LeanPub, Amazon (Kindle and paperback), and iBooks. 

There are multiples of that number of eBooks downloaded, as I've never DMCA'ed the sites that re-host the book illegally. I just... provide new and better versions. People who download the illegal copies know they can come to me for the best reading experience. Plus, I provide free updates forever for anyone who's purchased or gotten the book free on LeanPub.

My self-published book earned $300,000+ in revenue over the past 9 years, and still earns enough every month to pay my health insurance bill (sans deductible)—which has soared to beyond $2,000/month! (Living with a [pre-existing condition](/blog/2022/crohns-disease-takes-its-toll-back-2023) in the USA is... bad.)

I've had multiple offers to license the book through traditional publishers, but every one was a raw deal for me as an author. I earn between 30-80% of each book sale (depending on the channel), and the publishers' deals paled in comparison—at best 5-10% royalties, and that's _after_ the revenue surpasses the advance royalty payment. Unless you're the next Steven King, **traditional book publishing is not a route to sustainable writing income**.

I am transparent in reporting my work, as I rely on the support of sponsors on [Patreon](https://www.patreon.com/geerlingguy) and [GitHub](https://github.com/sponsors/geerlingguy) to sustain my work and open source development.

In fact, I finally completed the open-sourcing of my book's manuscript (all the code examples were free and open source from the start)—the book is now licensed as [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/), meaning if Red Hat likes, they could take my book, and republish it in its entirety, and even sell that downstream copy, and I am okay with that. They are free to do that, as long as they abide by the license and share it with the same license.

Here are some metrics which I hope you may find useful—especially if you are considering writing your own book.

## Amazon and KDP dominate

{{< figure src="./2023-ansible-for-devops-sales-per-channel.png" alt="Ansible for DevOps - Sales per channel" width="700" height="431" class="insert-image" >}}

I started publishing my book on LeanPub, because I like the philosophy as publishing as you write. Readers can get value from the book even before it's complete, and putting your work out there early gives validation about what parts of the work are more valued than others.

Kind of the 'move fast and break things' philosophy, applied to a creative endeavor.

But once I published the first complete edition of the book to Amazon's bookstore, sales exploded—and have not let up. The book went into the top of the Linux-related Amazon rankings a few times in its lifetime, and despite Amazon's practices, it seems the majority of book readers find there way to that store.

I published on iBooks just to see what that could get, and... surprisingly there are still 10-20 people every month on that tiny platform who buy the book!

LeanPub is where I've given away the book for free numerous times—that's why you see those off-the-charts spikes—but it has also been a reliable source of sales over the years.

{{< figure src="./ansible-for-devops-leanpub-bestseller-3.jpg" alt="Ansible for DevOps - Bestsellers All Time number 3" width="700" height="394" class="insert-image" >}}

I never thought Ansible for DevOps would be so popular (it's now the [#3 bestseller all-time](https://leanpub.com/bookstore?type=book&amp;sort=bestsellers_lifetime) on LeanPub). In fact, I originally set a goal to have 100 readers by the time I completed writing the book.

## Revenue: Significant, not life-changing

{{< figure src="./2023-ansible-for-devops-royalties-per-month-full.png" alt="Ansible for DevOps - Royalties per month (total)" width="700" height="432" class="insert-image" >}}

Total revenue on the book surpassed $300,000 this year. Averaged over 10 years, that is $30,000/year, which is not insignificant.

My salary as a software developer was multiples of that, however, so if I calculate my hourly earnings as a salaried employee versus the book income, I would barely be able to afford health insurance for my family of six—much less the $14,000 deductible we pay on top of that! Unless you are a serial author, or write multiple bestsellers, it is incredibly hard to write for a living, even without a family.

In addition, my writing is only useful inasmuch as it instructs. The chief complaint against some of the other introductory Ansible books is "this is about on par with the documentation, but it doesn't solve my problem."

I worked my examples backwards from real-world scenarios encountered in my day job. And it shows, because much of the code in the book utilizes the same open source libraries and Ansible content I wrote to assist multiple Fortune 500 companies.

In that way, the book has been a positive feedback loop, especially considering I have been [testing all the book's examples in CI against every Ansible version](https://github.com/geerlingguy/ansible-for-devops/actions) for a _decade_ now.

The book is certainly good for self-marketing, though besides a short stint consulting for Red Hat, I don't think the book has led directly to any individual business contract. I think the _writing process itself_ benefitted my career more than the published work.

I wrote the book mainly because (a) writing a book was a bucket-list item for me, and (b) I already had a lot of in-depth blog posts to kick-start the first three chapters. I was not planning on writing almost 500 pages (my initial target was 100), but I became a lot more involved in the writing than I originally intended.

{{< figure src="./youtube-channel-growth-2020-2023.jpg" alt="YouTube channel growth 2020-2023" width="700" height="151" class="insert-image" >}}

As I write 2,000 word scripts for my weekly [YouTube videos](https://www.youtube.com/c/JeffGeerling), the ability to both get words on paper (well, on a screen), and hone those words down to a fine point, has helped my YouTube channel grow to the point of sustaining my family.

## Book Progress

And speaking of word counts:

{{< figure src="./2023-ansible-for-devops-word-count-over-time.png" alt="Ansible for DevOps - Word Count Over Time" width="700" height="432" class="insert-image" >}}

I wrote the following script to calculate how many words were in all .txt files in my book's manuscript over time (note that there are a few txt files full of metadata that inflates this number, but only a little):

```bash
#!/bin/bash
# Count all lines in .txt files in a repository for each commit.
for commit in `git rev-list --all`; do
    commit_date=$(git log -n 1 --pretty=%ad --date=iso-strict $commit)
    # On GNU tar, add `--wildcards --no-anchored` options
    wordcount=$(git archive $commit | tar -x -O '*.txt' | wc -w | xargs)
    echo "$commit_date,$wordcount"
done
```

I have found it useful to reflect back on the progress this book has made over the years, and I'm proud to finally have had time to make the manuscript public. I intended on doing it much earlier, but until [recent events](/blog/2023/gplv2-red-hat-and-you), I didn't have sufficient motivation to devote a few hours into the process.
