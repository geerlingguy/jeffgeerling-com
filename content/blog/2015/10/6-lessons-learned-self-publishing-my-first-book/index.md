---
nid: 2614
title: "6 Lessons learned self-publishing my first book"
slug: "6-lessons-learned-self-publishing-my-first-book"
date: 2015-10-19T13:33:47+00:00
drupal:
  nid: 2614
  path: /blog/6-lessons-learned-self-publishing-my-first-book
  body_format: full_html
  redirects: []
tags:
  - ansible
  - ansible for devops
  - books
  - essay
  - leanpub
  - self publishing
  - writing
---

<a href="http://www.ansiblefordevops.com/">Ansible for DevOps</a>, my first book, is finally available for sale on Amazon and iTunes (in addition to LeanPub, where it's been available as an in-progress work since last February!).

<p style="text-align: center;"><a href="http://www.ansiblefordevops.com/">{{< figure src="./ansible-for-devops-cover_0.jpg" alt="Ansible for DevOps cover - Book by Jeff Geerling" width="301" height="391" class="inserted-image" >}}</a></p>

I've written quite a bit about the my writing process, book sales pre-publication, and motivation in previous blog posts, linked here:

<ul>
<li><a href="http://www.jeffgeerling.com/blog/25k-book-sales-and-im-almost-ready-publish">$25K in book sales, and I'm almost ready to publish</a></li>
<li><a href="http://www.jeffgeerling.com/blog/writing-leanpub-021-word">Writing on LeanPub - $0.21 per word</a></li>
<li><a href="http://www.jeffgeerling.com/blog/self-publishing-my-first-technical-book-leanpub">Self-publishing my first technical book on LeanPub</a></li>
</ul>

Reading through those posts, everything I said is still perfectly valid—from the importance of getting early feedback to the caution about how much luck is involved in building a successful project (be it a book or anything else).

It's a huge relief having the book complete, and I wanted to jot down a few of the lessons I learned self-publishing my first book.

<h2>Write about something in which you have a deep interest</h2>

Gleaned from my first post about the book, this lesson rings even more true today than it did two years ago. Had I not been highly invested in infrastructure management and automation, the entire project would've fizzled out a few times. I've been building up my Ansible Galaxy roles, submitting bug reports and documentation fixes for the Ansible project, and helping many developers and sysadmins with their adoption of Ansible—often just through Twitter and email.

If I didn't have any real passion for Ansible or automation, I would've stopped writing once I got past the intro-level chapters, and I wouldn't have spent hours working on a fully-automated Docker orchestration example, varied application deployment examples, and HA/HP environments on AWS and DigitalOcean.

<h2>Plan for at least 3 weeks to finish your book—after you think it's 'complete'</h2>

After I had my final edit—what I believed was a 'locked' edit that would be my 1.0 release—I found that there were still many tasks requiring changes, wait periods, etc.:

<ul>
<li>I had to change the page size from 8.5" x 11" to 7.44" x 9.68", resulting in a week-long process of cleaning up dozens of code blocks and paragraphs which were laid out improperly.</li>
<li>I had to wait 3 days for an expedited shipment of the paperback proof copy... which I had to make changes to, meaning 3 more days of waiting.</li>
<li>Apple's iBooks store had trouble verifying my email (I had to set up a new Apple ID just for books, since my existing ID is used for App distribution), then had trouble with some of my book's images (a few days' worth of churn).</li>
<li>In two final proofreadings, I found dozens of tiny bugs or improvements that required more tweaking.</li>
<li>...and the list goes on...</li>
</ul>

The most amazing part of this process, though, is that readers who paid for early access to the book on LeanPub were still getting their full value from their purchase, from the day they bought the book until now (and forever, since I'll be publishing regular updates to the book on LeanPub!).

But know that the process takes a while, and be patient!

<h2>Capture email addresses</h2>

The biggest boosts in sales numbers <em>always</em> came from emails to my (severely neglected) Ansible for DevOps email list. I didn't even manage a list until the past few months, but even so, any time I would send a note with new updates in the book, Ansible news, and a coupon link, I'd see a bump of a few more sales per day that week.

Tweets generated a little buzz, and having an official Twitter account (<a href="https://twitter.com/ansible4devops">@ansible4devops</a>) was helpful as an extra resource for readers, but ultimately, few sales were a direct result of a tweeted link.

Almost every book author I know has a carefully-curated email list that they use to promote their work, deliver interesting news and articles, etc., and the key is to keep the emails you send relevant and helpful for the reader, and remind them to spread a good word about your book to their friends and co-workers!

<h2>Luck is important—so create some of your own</h2>

Ansible for DevOps was the right book in front of the right audience at the right time—when I started writing the book, there was only one other published book available, and while Ansible's documentation was (and still is) stellar, there were few bloggers who had thorough introductions to using Ansible in certain ways.

I capitalized on this opportunity by publishing the first few chapters of the book on LeanPub as quickly as I could, and spread the word through Hacker News, Reddit, Twitter, the #ansible IRC channel, and a few other people in the Ansible community I thought would be interested.

One important thing to note—at the time, I was actually just beginning writing on a <em>different</em> book on Drupal (another open source project). When I started to work more with Ansible and noticed the dearth of Ansible books, I decided to switch tracks and focus on <em>Ansible for DevOps</em>—creating <em>my own</em> luck.

<h2>Track metrics, and refocus</h2>

There were a few different metrics I tracked to help me focus in the right areas of the book, and to help me focus on getting to a 1.0 release:

<ul>
<li><strong>Web traffic via Google Analytics</strong>: I added a tracking code on day one so I could see, generally, the sources of traffic, how long they were staying on the page, etc. I tried some variations of descriptions, subtitles, etc., and did notice significant differences in some instances.</li>
<li><strong>Purchases over time, and in relation to significant events</strong>: promotion after talks, mentions in blog posts, or emails to my book's email list.</li>
<li><strong>Total word count, and words written per [unit of time]</strong>: I needed to motivate myself to continue writing, so these metrics helped me see when I was slacking too much—usually because I was spending more time messing with an example than actually <em>writing</em>.</li>
</ul>

Make sure you don't spend <em>too</em> much time on metrics, though. I'd estimate about 2-4% of my entire time was spent on metric gathering and analysis.

<h2>Money shouldn't be your primary objective</h2>

With qualifications, money shouldn't be the motivation behind almost any writing project. For me, writing a book has been a goal for a long time, and I'm so happy to finally have that checked off my list. I will likely do more books, but still, the reason will be the desire to write more than the desire to make money.

A mildly-successful book like Ansible for DevOps couldn't sustain someone for a full year—most authors who make a living <em>writing</em> have multiple projects and paid engagements in a given year. For me, all the money earned from the book is going straight into an index fund investment account (after the large chunk of taxed income is removed), and my wife and I will likely decide what to do with it five or ten years down the road.

Money <em>is</em> a motivator—I can't say the idea of a small amount of passive income from this book project isn't pleasing to me—but it's not a primary motivator.

<h2>Summary</h2>

In summary, this has been an amazing experience, and I would recommend self-publishing a book to anyone daring enough to try. It's not a bad experience at all, and it can be pretty rewarding, especially if you can get a little lucky!

Before wrapping up this post, I'd especially like to thank the following contributors who have submitted bugfixes, PRs, and suggestions that have made the book better: @LeeVanSteerthem, @ibluebag, @diermakeralch, @jonathanhle, @dan_bohea, @lekum, @wimvandijck @39digits, @aazon, @andypost, @michel_slm, @erimar77, @geoand, @b_borysenko, @chesterbr, @mrjester888, @gkedge, @opratr, @briants5, @tybstar, @laserllama

<p><em>Purchase Ansible for DevOps on <a href="https://leanpub.com/ansible-for-devops">LeanPub</a>, <a href="http://www.amazon.com/Ansible-DevOps-Server-configuration-management-ebook/dp/B016G55NOU/">Amazon</a>, or <a href="https://itunes.apple.com/us/book/ansible-for-devops/id1050383787?ls=1&mt=11">iTunes</a></em>.</p>
