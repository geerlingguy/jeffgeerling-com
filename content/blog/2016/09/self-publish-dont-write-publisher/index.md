---
nid: 2692
title: "Self-Publish, don't write for a Publisher"
slug: "self-publish-dont-write-publisher"
date: 2016-09-18T00:39:19+00:00
drupal:
  nid: 2692
  path: /blog/2016/self-publish-dont-write-publisher
  body_format: markdown
  redirects: []
tags:
  - amazon
  - ansible
  - ansible for devops
  - books
  - ebook
  - leanpub
  - publishing
  - self publishing
  - writing
---

I'm not a writer. I'm a software developer who communicates well. Because I'm a developer and software architect, I spend time evaluating solutions to find the best one. There are often multiple good options, but I try to pick the best among them.

When I chose to write a book two years ago, I evaluated whether to self-publish or seek out a publisher. I spent a _lot_ of time evaluating my options, and chose the self-publishing route.

Because I'm asked about this a lot, I decided to summarize my reasons in a blog post, both to posit why **self-publishing is almost always the right option for a beginning author**, and to **challenge publishers to convince me I'm wrong**.

## First, the Facts

Book writing is not often lucrative. Most technical author have full-time jobs, and write on the side. For every [Steve McConnell](http://cc2e.com/), [Donald Knuth](http://www-cs-faculty.stanford.edu/~uno/taocp.html), and [Fred Brooks](https://en.wikipedia.org/wiki/The_Mythical_Man-Month), there are a thousand writers whose books have sold less than a few thousand copies, and who will never write or even speak on the topic of their books again.

I knew this fact going into my project. I chose to take a very safe approach: _publish a few chapters, see the interest, then see if I want to continue writing_. There are some excellent platforms for this new form of self-publishing—allowing authors to test the waters before committing thousands of hours to a book project. I chose [LeanPub](https://leanpub.com/), and starting with just 3 chapters and a few dozen buyers, sales grew into more than 7,000 book sales in less than a year.

I initially targeted 100-200 book sales. At $9.99 minimum and $19.99 suggested (even without the complete book at that time), that would net between $1,500-3,500 (LeanPub's variable pricing and extremely generous royalty rates are very good if you've ever compared to other platforms, and especially publishers!).

_Before I finished writing the book_, I had sold over 2,000 _paid_ copies on LeanPub, for over $25,000 in net profit (ASP of $12.50)—that's _after_ LeanPub's small cut.

I 'published' the book in October 2015 (meaning I locked in a first edition and published it on Kindle, CreateSpace (for paperback), and iBooks), and have added another 5,000 sales since. Here's a breakdown of sales by channel:

<p style="text-align: center;">{{< figure src="./sales-over-time-ansible-for-devops.png" alt="Sales over time - Ansible for DevOps" width="650" height="389" class="insert-image" >}}</p>

Note the jump in volume once I started selling the 'first edition' in additional marketplaces. LeanPub sales have been consistent but flat since I finished about half the book, while other channels have grown over time—most notably CreateSpace (paperback sales through Amazon) and Kindle. iBooks is probably not even worth the effort—less than 100 sales in almost a year—but at least it's not nothing!

The book has been a wild success, judging by my original hope of 200 sales on the high end!

## Keys to Success

Some of the reasons my book has done much better than I imagined were:

  - **Luck.** You can't get around it—most runaway successes became so due to in large part to luck. That doesn't mean you have no control—you have to make your own luck by positioning yourself in the right place at the right time, honing your skills, building your network, etc. I was lucky to have started my book at a time when LeanPub and CreateSpace were both fairly mature publishing platforms, and I was also lucky to have one of the first substantial books on the software I was writing about. But luck carries only so far.
  - **Ease of updating the book.** This is the main reason my book has taken off and carried its sales momentum for many months. All the other books on the market are written for a specific version of software, published, then are irrelevant after a few more releases. I've completely rewritten 20% of the book based on a major version change, and I've re-tested and honed many examples based on improvements in the underlying software. Readers appreciate that they spent money on a text that _improves_ over time, and _remains relevant_.
  - **The desire to keep my book current.** I like to think of my book as a 'BaaS' (Book-as-a-Service). Just like SaaS products I maintain, I have a desire to keep the book relevant and keep all the contents well-tested and working. Not only for the readers who have already paid for the book (some generous readers have paid $50-100+ on LeanPub to prod me to keep up the good work!), but also to make sure my book is _always the best_ book available, from version 1.0 to whatever version I can make it!
  - **Flexible editorial workflow.** I dislike writing in a print page layout application (Pages, Word, InDesign, etc.); I write everything in a text editor—currently Sublime Text—in Markdown. None of the publishers I've talked to accept work in any format other than Word or something like it. Self-publishing and working with flexible technical editors who are okay using whatever tool suits the job means I can experiment and choose the tools most efficient for _me_. I experienced almost zero friction writing the book in LeanPub-flavored Markdown in Sublime Text, editing with some freelance editors through [Authorea](https://www.authorea.com/), and publishing to different channels via LeanPub's excellent book export tools.
  - **Ability to set lower prices** (with great royalty rates). Because there is no middleman, I can aggressively undercut other books in the genre. I chose to sell the book at $9.99 for the eBook, and $19.99 for the paperback. I get between $7-9 each eBook sale, and ~$6 for each paperback. If using a traditional publisher, I would only get $1/eBook and $2/paperback at typical rates. Not only that, traditional publishers jack up the price to make a huge margin, so my book (a ~400 page technical book) would sell for $30-40 (instead of $10-20) if I distributed through a publisher! A good technical book is well worth the price (I have a few thousand dollars worth of technical books on my shelves)... but when you see a well-reviewed book at _half the price_ of all the other books in its class, it's easier to hit the 'buy' button and give it a try.

## The Lure of the Publisher

There are four main reasons any author is tempted to submit work to a publisher. I admit, I've been tempted to hand over the rights to my book to a publisher for these reasons:

  - **Marketing**: Publishers can get your book into booths at conventions, dozens or hundreds of online and retail sales channels, and they can promote you as an author. Sometimes, this can boost your profile beyond what you can do on your own, but more often, you might get to go to one or two extra conferences, sign a few dozen copies of your book, and otherwise have your book sitting in a stack on a table densely populated with _all the other_ tech books from that publisher.
  - **Editing**: Publishers have a strong process and workflow, and one of their greatest strengths is editorial staff—individuals who are strong technical editors and will make your writing go from muddy to crystal clear. This ability differs widely by publisher, though—the bigger publishers have much better, dedicated editors, while some of the lower end use random techies who get a free copy of your book and a credit for their efforts and nothing more.
  - **Prestige**: In some ways, this is the biggie. I learned much about programming through books published by O'Reilly, IDG, Pearson, et all, and the idea of having my own work passed on to others with the same imprint does sound interesting. It's also a situation where external validation (a publisher _chose_ my work, therefore I'm not just a nobody) can be a motivator.
  - **Motivation**: Speaking of motivation... Publishers have formal schedules, and since they line up editors, reviewers, and launch dates, you are beholden to those dates (lest you lose out on some of the advance, or lose the book deal entirely). This can be beneficial, because without imposed deadlines, some writers may never achieve a 'first edition'. Writing is _hard_, and takes lots of time. You have to be motivated, and if you can't motivate yourself, external motivation can help.

## The Things You Leave Behind

There are a few major downsides to writing for a publisher—some things you usually have to give up at some point in the process:

  - **All your rights to the book**: both domestic and foreign copyright. The book is no longer yours once you hand it over. There are exceptions—but not usually for first-time authors.
  - **Writing for fun**: Writing a book is _hard work_... writing a book as a hobby or for fun goes out the window when there are mandatory deadlines, editorial reviews, and authoring tools. It just becomes _work_. And it's work done _for someone else's benefit_, just like a day job.
  - **The Ability to Update Your Book**: _If_ your book is highly successful and _if_ the publisher likes you, you _might_ get a chance to write a 2nd edition... which requires all the publishing process rigamarole (deadlines, editorial process, authoring tools, etc.). Even if you get to publish more editions, it can take months per edition, and all those little bugs and typos that slip through the editorial process (but are readily found/emailed to you by readers!) will be stamped into the text forever.
  - **Analytics**: You generally don't get to see sales numbers by channel, region, etc. You have to divine these numbers from what little public data is available on sites like Amazon, like book rankings.
  - **Money**: If your book is a mild success (3,000-7,000 sales), you will barely earn anything over your advance in royalties. If your book is a wild success (10-100,000 sales), you'll likely get a 10-15% cut. (You can get 70%+ when you self-publish). Taking 7,000 sales as an example: self-publishing will net you ~$60k in royalties (with no advance). Publishing traditionally will net you ~$5k in royalties (with a $3k advance). Even if a publisher gets you enough exposure to sell 10x more copies of the book (highly unlikely unless you do absolutely zero promotion on your own), the math isn't in your favor.

## Conclusion

For myself, the choice to self-publish is even more clear now than it was in early 2014—the tools and technology are to a point where there is little redeeming value to writing for a publisher. The hardest part of writing a book is... _writing_ the book. And a publisher can't do much to help with that. Some individual paragraphs require three days researching bugs in upstream projects I was writing about or learning something entirely new, and nobody at a publishing house is going to sit with me and figure it out!

For you, the choice may not be as clear, especially if you aren't comfortable doing _any_ self promotion (you have to have a tiny bit of diva in you to be a successful author...), and can't be motivated to complete a project as daunting as a full-length book.

Whatever the case, writing and publishing a book, then holding a copy of the book in my hands last October, was one of the most exhilarating things I've done in the tech realm. Knowing that I can amplify my own knowledge and guide others towards better software development and deployment practices is a huge side benefit.

## To Publishers

Do you represent a traditional publisher? The gauntlet has been laid down—please convince me I'm wrong. Every time I've received an offer to publish with one of the publishing companies, I ask these questions:

  1. _Can I retain rights to the text?_ Or do you require I assign you all rights so I have no control over my work or its derivatives?
  2. _Can I publish updates to my book—at least quarterly, if not more frequently?_ In tech publishing, books that are published once die quickly as the software and techniques written about change every year.
  3. _Can I get a reasonable royalty rate higher than 10-15%?_ And will this rate apply to every sale or only once my advance is covered?
  4. _Can I get a reasonable advance?_ Knowing most books don't become blockbusters, the advance should be meaty enough to at least cover a tiny bit of my massive time investment in the project. And not the simple $3,000 offered to almost all first-time authors, regardless of merit.

Sadly, every publisher I've dealt with has given a resounding no to not one or two, but _all_ of these questions. If you want me to donate hundreds or thousands of hours of my family and hobby time towards writing a book for _you_, you need to at least meet me halfway.

## My Book

<p style="text-align: center;"><a href="https://www.ansiblefordevops.com/">{{< figure src="./ansible-for-devops-cover.jpg" alt="Ansible for DevOps cover" width="301" height="391" class="insert-image" >}}</a></p>

I didn't link to my book in the body of this post, because I want the advice to stand on it's own without it seeming self-promotional. I also don't link to the book prominently on my blog, partly because I cringe when I see the insane amount of self-promotion many self-published authors do, and partly because the book is only relevant to a small portion of my blog's audience. The book is [Ansible for DevOps](https://www.ansiblefordevops.com/), and I posted three chapters to LeanPub in Februrary 2014, then finished writing the 'first edition' in October 2015. Since that time, I've published another 14 versions of the book (mostly corrections, but also a few new sections and a complete rewrite of a couple chapters).

I've been blown away by the book's success, and am considering another book, but I'm taking my time. Especially since I just had major surgery (yay for finally having time to write a post like this!) and I have a baby on the way!

## Other Resources

Some other good reads on technical book publishing/writing:

  - [Writing A Technical Book: Is It Worthwhile?](http://www.fasterj.com/articles/bookwriting.shtml)
  - [Advice to Prospective Book Authors](http://www.aristeia.com/authorAdvice.html)
  - [Negotiating Book Contract Terms and Royalties](http://www.fonerbooks.com/contract.htm)
