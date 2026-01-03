---
nid: 2603
title: "$25K in book sales, and I'm almost ready to publish"
slug: "25k-book-sales-and-im-almost-ready-publish"
date: 2015-09-18T10:16:47+00:00
drupal:
  nid: 2603
  path: /blog/25k-book-sales-and-im-almost-ready-publish
  body_format: full_html
  redirects:
    - /blog/25k-sales-and-im-almost-ready-publish-book
aliases:
  - /blog/25k-sales-and-im-almost-ready-publish-book
tags:
  - ansible
  - ansible for devops
  - books
  - self publishing
  - statistics
  - writing
---

<p>I started writing my first book almost two years ago. At the beginning of the project, I set an ambitious goal: Write a 90-page introductory-level technical book on some relatively new software, and sell 200 copies.</p>

<p>As a developer and dabbling entrepreneur, I calculated that if I sold the book for around $10-20, and wrote the book based on real-world scenarios I'd already encountered (meaning very little extra research/discovery required), I could make enough money to keep things interesting while helping a few hundred developers pick up the new software more quickly.</p>

<p>Almost two years later, <em>Ansible for DevOps</em> is almost 400 pages long and has sold over 2,000 copies—and I haven't yet published the book.</p>

<p style="text-align: center;">{{< figure src="./books-sold-per-month.png" alt="Books sold per month" width="628" height="342" class="inserted-image" >}}</p>

<p>What follows is an analysis of what led to this success, and some cautions for those considering writing a book.</p>

<p>Also, as you'll likely find is a theme running through every "how to do <em>x</em>" post on HN, Reddit, and blog, this blog post serves to shamelessly plug <a href="http://www.ansiblefordevops.com/">Ansible for DevOps</a>[1].</p>

<h2>
<a id="user-content-the-right-place-and-the-right-time" class="anchor" href="#the-right-place-and-the-right-time" aria-hidden="true"><span class="octicon octicon-link"></span></a>The right place and the right time</h2>

<p>One of the largest factors in my book's sales, and in fact in pretty much every project I've seen that's way more successful than originally planned, is <strong>luck</strong>. In this case, it was a matter of publishing the right book at the right time.</p>

<p>Ansible was created in 2012, and for the first year or so, it wasn't clear if it would rise to the adoption of heavyweight CM tools like CFEngine, Puppet, and Chef. It was also created with many of the same ideas as Salt (now SaltStack), another fledgling YAML-based CM tool. However, Ansible had three <em>major</em> advantages over the incumbents:</p>

<ul>
<li>It uses SSH for transport (instead of a proprietary protocol), so you don't have to install stuff on all your managed servers/systems.</li>
<li>It uses YAML for configuration, which means serious work can be done with it without learning a custom DSL or parts of a programming language.</li>
<li>It was promoted as an <em>infrastructure</em> management tool, not a <em>configuration</em> management tool, during the (ongoing) explosion of microservices and container-based infrastructure, where orchestration is sometimes more important than configuration.</li>
</ul>

<p>Ansible was in the right place at the right time, and my book was one of the first two books available to help people learn Ansible.</p>

<p>Being involved in the Ansible community helped me to build a small network of contacts who helped spread the world (a little here, a little there, and it adds up), and it also helped me to get some <em>amazing</em> early reviews and suggestions that guided the rest of the book in the right direction.</p>

<p>My book had one other huge advantage over the other existing book, and over all the other Ansible-focused books that have since been published—it was published not once, but <em>hundreds</em> of times. I've published updates to the book while Ansible has evolved. When I started writing the book, Ansible 1.2 was the latest version. At the time of this writing, Ansible 2.0 is just around the corner, and the book is 100% current with the latest best practices and newest functionality. Which leads me to...</p>

<h2>
<a id="user-content-the-right-process" class="anchor" href="#the-right-process" aria-hidden="true"><span class="octicon octicon-link"></span></a>The right process</h2>

<p>Two years is an eternity in the tech world. Infrastructure has evolved so rapidly, with Ansible alongside. The traditional publishing model doesn't offer the agility necessary to publish and maintain a technical book that responds to rapid change.</p>

<p>Some publishers are making massive strides in this regard, but the traditional publication process works against many authors:</p>

<ol>
<li>After a hot new technology gets out of the early adopter stage, all the major publishing houses decide it's time to publish an introductory book on the technology.</li>
<li>High-profile early adopters or technical writers are contracted to write the book.</li>
<li>A compact 3-to-6-month cycle of writing, editing, reviewing, and finally publishing the first (and often <em>only</em>) edition of the book takes place.</li>
<li>The book is finished, and within a few months to a year, half the examples fail on the latest version of the software, and developers the world over toss the book into a waste bin, or set it on the shelf to collect dust.</li>
</ol>

<p>I know about this process because I spent a <em>lot</em> of time considering the traditional publishing workflow. I talked to representatives at all the major technical book publishing companies, and was considering quitting LeanPub for a quick first-time-author advance (something like $5K to $10K max), and a promise of a tiny percentage of all book sales.</p>

<p>I'm glad I didn't go that route, because Ansible for DevOps has netted me over $25,000 in sales (so far).</p>

<p>LeanPub is a publishing platform that allows authors to publish in-progress books, and allows readers to purchase the book once, then download DRM-free copies of <em>every</em> update, <em>ever</em>.</p>

<p>I found out about LeanPub because I bought <em><a href="https://leanpub.com/nodebeginner">The Node Beginner Book</a></em> a couple years ago, and loved how the book was updated as the author gained more knowledge, as Node.js grew, and as readers submitted corrections. It was one of the best and most cost-effective technical book purchases I've ever made, even at a meager 54 pages.</p>

<p>Some of Leanpub's most attractive traits include:</p>

<ol>
<li>All sales are 100% refundable for 45 days. Did you judge the book by its cover then read the first chapter and realize it's not for you? No problem, just return it and nobody bats an eye.</li>
<li>All downloads are DRM-free. This needs no explaining, I hope.</li>
<li>LeanPub books are written in Markdown (the idea of laying out or editing a book in Word makes me shiver), and LeanPub has some great and customizable formatting defaults so your text looks great in ePub, .mobi, PDF, and (optional) HTML formats.</li>
<li>LeanPub takes a very small slice of the sale (~10%) for what I get out of it.</li>
</ol>

<p>Some authors, and pretty much <em>all</em> the publishers, shudder when they hear about 45-day refund policies, <em>especially</em> in tandem with DRM-free downloads. What's to prevent someone from downloading the book and making infinite copies? In the old publishing world, where there's one and only one edition (at least for a long while), I see how that can be devestating.</p>

<p>But with LeanPub, the first person who purchased my book for $9.99 almost two years ago (and only received a preface, and two short intro chapters) has had access to almost every bit of knowledge I've gained in those two years, and <em>that's</em> the value. Once my book hits '1.0' and I publish a static '1.0' edition on Amazon, iBooks, and elsewhere (platforms about which I'm less excited), I'll still be updating it on LeanPub.</p>

<h2>
<a id="user-content-caution" class="anchor" href="#caution" aria-hidden="true"><span class="octicon octicon-link"></span></a>Caution</h2>

<p style="text-align: center;">{{< figure src="./word-count-over-time.png" alt="Word Count over time" width="544" height="309" class="inserted-image" >}}
Word count over time. This graph took way too long to make[2].</p>

<p>You may be thinking to yourself, "I know technology <em>xyz</em> pretty well, and I could use $25K, so I'll write my own book!" More power to you, and by all means, pursue your passion... but be warned:</p>

<ul>
<li>
<strong>Don't do it (only) for the money.</strong> I spent around 1,000 hours writing Ansible for DevOps. With no deduction for the (meager) marketing I've done (about $500 total), this equates to about $25/hour. Almost any other job or contract work I've done has paid two to four (or more!) times that rate, so most of the time I spend writing the book I cut out of other time—time with family, time relaxing, time I could be working on other opportunities.</li>
<li>
<strong>Book sales requires some skill and a lot of luck.</strong> I picked the right topic at the right time, and I had a (small but effective) network of relationships to promote the book. Had I started my book today, I would have far fewer sales in the more saturated Ansible book market. If you're writing a book on Java, it better be the best Java book in history, or you shouldn't expect a huge number of sales.</li>
<li>
<strong>Self-publishing requires more effort than the traditional route.</strong> I had to find my own editors, design my own cover, find reviewers, do all the marketing. On the flip side, I have full control over the entire process, which can be a benefit.</li>
<li>
<strong>Finding time to focus on writing is a constant battle.</strong> Early on, I had a lot of passion for the book, and I would wake up an hour early every day to write. That initial burst of energy died out, and there were a couple dry periods where a word wasn't written for a few <em>weeks</em>. Without the pressure of a publication deadline, your writing can fizzle. Find a routine and stick to it.</li>
<li>
<strong>Writing is work.</strong> Even tutorial/cookbook-based writing can be a huge drain, and writers' block applies to technical writing as much as any other style. I've been writing documentation and posts for many blogs for over 10 years, with some regularity (at least a few thousand words per week), so writing the book was not an entirely new endeavor—just <em>different</em>.</li>
<li>
<strong>Choose an audience, and be ruthless in writing for only <em>that</em> audience.</strong> I have a large list of topics I considered writing about, but in the end left out since they weren't the core problems <em>my</em> audience wanted to solve. I might add a few of those topics to version 1.2, 1.3, etc., but if you ever want to finish your book, cut out anything that's not directly relevant to your audience.</li>
</ul>

<p>If you want to write a book, but all means do so. But don't expect to toss some words on the screen and get rich quickly.</p>

<p>I'll be publishing Ansible for DevOps on other bookstores soon (there will be a printed edition available, too!), but you can get it now (and always have the latest version, DRM-free) from LeanPub.</p>

<p>I hope to write a few more posts about the publication process and book sales as I get time in the coming months, but please excuse me for now as I work on finishing up the last few changes!</p>

<h3>Footnotes:</h3>

<p>
<ol>
<li>At least I don't have a distracting newsletter popover like other authors!</li>
<li>Seriously. For anyone interested, here's a bash script to count all the words inside .txt files in each commit in a git repository:
<code>
#!/bin/bash
# Count all lines in .txt files in a repository for each commit.
for commit in `git rev-list --all`; do
    git log -n 1 --pretty=%ad --date=short $commit
    git archive $commit *.txt | tar -x -O | wc -w
done
</code></li>
</ol>
</p>

<p><em>Purchase Ansible for DevOps on <a href="https://leanpub.com/ansible-for-devops">LeanPub</a>, <a href="http://www.amazon.com/Ansible-DevOps-Server-configuration-management-ebook/dp/B016G55NOU/">Amazon</a>, or <a href="https://itunes.apple.com/us/book/ansible-for-devops/id1050383787?ls=1&mt=11">iTunes</a></em>.</p>
