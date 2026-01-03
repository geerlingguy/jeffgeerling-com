---
nid: 1268
title: "Review: Logos' Verbum Bible Software"
slug: "logos-bible-software"
date: 2014-02-05T17:32:11+00:00
drupal:
  nid: 1268
  path: /review/logos-bible-software
  body_format: full_html
  redirects: []
tags:
  - application
  - bible
  - catholic
  - logos
  - mac
  - reviews
---

<p><div class="rating" itemprop="Rating" itemscope="itemscope" itemtype="http://schema.org/Rating">
        <strong>Jeff's Rating:</strong> <span class="rating-value" itemprop="ratingValue">4</span>/5
      </div></p>

<blockquote class="tldr"><strong>tl;dr</strong>: A great, albeit pricey, resource for expanding anyone's knowledge of sacred scripture. The basic package is an excellent option for most any Catholic.</blockquote>

A few months ago, I was given the opportunity to try out Logos' Verbum, the <em>de facto</em> Bible study software. I tried out Verbum 5 for the Mac, and will share my thoughts on the platform below.

<p style="text-align: center;">{{< figure src="./logos-logo.jpg" alt="Logos Logo" width="250" height="250" class="blog-image" >}}</p>

<h2 id="initial-setup">Initial setup</h2>

First, a <em>major</em> caveat: though I go on a bit about my initial impressions being less-than-stellar, please read through to the end of this review—the software itself, once installed and configured, more than makes up for its initial warts.

Making a good first impression is important, so I hope one goal of the next version of Verbum is a better onboarding experience. It took—I kid you not—over five hours from the time I started downloading the installer from Logos' website to the time I could start using the application.

I have a stable 40 Mbps Internet connection, and can typically download 5 GB worth of data in under half an hour. I also have a very new Mac with an i7 processor, 8 GB of RAM, and a very fast 256 GB SSD. That said, the initial download maxed out around 1-2 MB/second, and then the process of downloading all the resources in my package (around 5 GB in all) took another hour and a half. During the process, I sat watching this loading screen for quite some time:

<p style="text-align: center;">{{< figure src="./1-logos-downloading-resource.png" alt="Downloading Resource loading screen" width="488" height="208" class="blog-image" >}}</p>

Then, after all the resources had downloaded (with pauses every now and then during which my processor usage spiked), I had to wait for another loading dialog:

<p style="text-align: center;">{{< figure src="./2-logos-preparing-library.png" alt="Preparing your library loading screen" width="412" height="210" class="blog-image" >}}</p>

One more minor quibble was that the login box that appeared after all this didn't let me paste in a password, so I had to manually type my 20-character random generated password by hand (a little frustrating, since I can just paste it in with my password manager on the Logos website). When Verbum finally opened to the home screen, I thought I could dive right in, but I then had to wait another two <em>hours</em> before indexing completed. I could've delayed the indexing and started working right away, but I wouldn't be able to search the 5+ GB of data I just downloaded, so I let it go and worked on other things. During the entire time, my processor usage was very high and the fan on my poor little laptop was spinning as fast as it could.

Additionally, many times when starting the application again, the app would take about 20 seconds to fully load, then it would download updated resources, need to be restarted again, and then reindex content, making the daily grind take an extra 3-5 minutes.

I only mention these annoyances because they soured my initial few minutes actually using Verbum; I knew it would take some time, but multiple hours to install the software on a brand new, high-end laptop with a decent Internet connection? Not a chance. I hope Logos can focus on making initial download and install much faster, especially for users of the higher-end packages with much more content. Perhaps Logos can make the initial download contain an indexed copy of all the data, or have all the main sources pre-indexed with the initial application download. Additionally, it would be nice if Logos' servers could let me download the files as fast as my connection could sustain. I can't imagine the experience for someone using a 3-5 year old computer with a slower hard drive, less RAM, and a 3 or 5 Mbps Internet connection.

Additionally, the main reason this review was delayed so long was that I had only 20 GB of free space on my old MacBook Air, which was almost immediately consumed once I had installed Verbum—between the applications and resources (downloaded to <code>~/Library/Application Support/Logos4/Data</code>, over 11 GB of disk space was used.

After a little while using the software, my worries that the rest of the experience would be similarly disappointing quickly subsided, as the software works great for its intended purpose.

<h2 id="first-impressions">First impressions</h2>

I'm an extremely technical computer user; I develop web applications, and have done a bit of programming on Mac OS X and on iOS, so I know a lot of the nitty-gritty details when it comes down to interface design and responsiveness.

Verbum has a pretty good interface. It tends to favor the busy slightly more than the simple, as there are many little 'icing' features I think could be excluded without upsetting many users (like a full WYSIWYG interface for writing notes on passages, or a fading hover effect on tabs—both of which are illustrated below). The interface is designed more generically than a typical OS X app, using custom icons and design elements most places. While it's obvious the interface was designed in a platform-agnostic manner, it <em>is</em> mostly intuitive, and works with most Mac mouse and keyboard paradigms, and that's a very good thing.

<p style="text-align: center;">{{< figure src="./3-logos-ui-stuff.png" alt="UI Flourishes and WYSIWYG in Logos Verbum" width="550" height="277" class="blog-image" >}}</p>

<blockquote>Aside for more technical readers: Parts of the application seem to have been written in .NET, so it uses Mono on non-Windows platforms to run the code, so that may account for some general sluggishness. Additionally, much of the interface seems to be driven by HTML and JS, using <a href="http://www.awesomium.com/">Awesomium</a> and some other HTML extensions. There are dozens of open source frameworks, SDKs, and runtimes included with Verbum—this is probably a large reason for the time it takes to launch and open new tabs.</blockquote>

The home screen is a little busy for my liking, but is a good starting-off point. You can open the main portions of the application from here, or just type in a topic or scripture passage in the search box in the top left.

<p style="text-align: center;">{{< figure src="./4-logos-home-screen.png" alt="Verbum home screen" width="600" height="440" class="blog-image" >}}</p>

Once you get into the application, the interface works pretty well. You can have notes on the left, scripture on the right, extra resources on the bottom (like I usually do when I'm using it on my large 24" monitor), or you could just have a scripture passage open full screen if you're focusing on the text itself. You can rearrange tabs by dragging them into different portions of the screen, and it works like you'd expect.

<p style="text-align: center;">{{< figure src="./5-logos-overview.png" alt="Verbum UI overview" width="600" height="332" class="blog-image" >}}</p>

No matter where you are in the interface, you can always type in a book or verse, a command, or a search word in the search bar at the top and bring up results in a new tab. The search options are very deep, and this is the main reason I think anyone who uses scripture for anything more than simple <em>Lectio Divina</em> would greatly benefit from using this software.

If you're working on a thesis that relates to scripture, if you're preparing sermons or religious talks on any kind of regular basis, or if you're simply trying to expand your knowledge of scripture beyond hearing it at Sunday Mass, Verbum can supercharge your study.

<h2 id="using-logos-as-a-former-seminarian-now-husband-and-father">Using Verbum (as a former seminarian, now husband and father)</h2>

I attended Kenrick-Glennon Seminary for almost five years, and did my fair share of scripture study, but never with a tool like Verbum. Imagine being able to look up hundreds of relevant Catholic sources concerning a particular passage, and see them all on one screen, then (if needing a citation) being able to copy and paste references into your work with the citations in whatever standard format you choose.

<p style="text-align: center;">{{< figure src="./6-logos-preferences-citations.png" alt="Logos Verbum preferences - citation style" width="500" height="395" class="blog-image" >}}</p>

The references included in the package I used ('Verbum Master', which includes all Papal encyclicals since 1740, all Pope Benedict's works, UBS handbooks on the Old and New Testaments, and a ton of extra content to provide background for the original biblical languages. This software can help a biblical neophyte become a scholarly exegete in a few months' time!

There are also some other nice bonuses. There are some really neat topical reading lists, sermon starter guides, and even some nice reading plans. For example, I am trying out the 30 Days on Marriage reading plan, which has a great selection of marriage-related passages for a month-long reflection:

<p style="text-align: center;">{{< figure src="./7-logos-marriage-reading-guide.png" alt="Verbum reading guide - marriage in 30 days" width="550" height="465" class="blog-image" >}}</p>

You can even export the reading plan straight to iCal so you don't get lazy and forget—a handy feature for me!

The notes feature is helpful for me, because I'm used to writing in the margins of my study Bible, but have no simple way of indexing those notes. With Verbum, I can just select some text, right-click on it, and create a new note. At that point, I can write as much or as little as I want, and easily browse my notes later.

You can organize notes into multiple topical notebooks; I like to have one for a particular book, one for life-related topics, one for marriage, etc., and Verbum is flexible enough to let me organize my notes how I like.

There are some other neat tools for exploring sacred scripture, like the Bible Timeline, which lets you scroll through time, or search for a date, and see all the events that occurred in that period. You can click on the event and bring up a quick list of references, or open up a window with a full treatment of the event and events surrounding it.

<p style="text-align: center;">{{< figure src="./8-logos-tools-timeline.png" alt="Logos Verbum tools - Timeline" width="525" height="382" class="blog-image" >}}</p>

Verbum is positively brimming with great texts for scripture study. For almost every passage I looked up, there were at least two or three very helpful explanations in the various texts included with Verbum, and they were always a click away.

<p style="text-align: center;">{{< figure src="./9-logos-resource-ot-commentary.png" alt="Logos Verbum OT commentary resource" width="525" height="318" class="blog-image" >}}</p>

For any kind of serious Catholic Bible study, I've never seen a tool—analog or digital—that comes close to Verbum. I wish it had been as fully-developed when I was in the Seminary; it would've saved me hours of work cross-referencing things and researching scriptural topics, and would've been well worth the price (especially if I could use it freely on the library computers).

<h2 id="conclusion-and-pricing">Conclusion and pricing</h2>

Verbum is a little rough in a few areas, and crashed twice during the course of my first week's usage, but works pretty well for such an ambitious application. The interface is mostly intuitive (if a little bloated in some places), and the content and searchability are top-notch.

The price of the software is a little bit of a non-starter in today's App Store bargain bin pricing environment, but is not unreasonable for what is included. Especially considering there's nothing on the market that comes close to the breadth of content, community, and cross-platform support you get with Verbum.

If you're a student, or you work in or around academia, there's a good chance you can get a nice discount. See the <a href="https://www.logos.com/academic/program">Academic Discount Program</a> for more information. For anyone working on a thesis that involves scripture, Verbum is a no-brainer—it will save you hours of work. For the general population, the price is definitely worth it for one of the lower-end packages (basically, the more you pay, the more resource you get); I consider it a small price for a better understanding of one of the pillars of my faith.

The <a href="https://www.logos.com/product/37596/verbum-basic">Verbum Basic package</a> would be the sweet spot for most Catholics I know. Buying it for your family, if only for the ability to find some good scripture to read at family prayer, or to explore topics your kids are talking about, would be a great idea. And if the price is a non-starter, the <a href="https://www.logos.com/product/18543/catechism-of-the-catholic-church-collection">Catechism Collection</a> may be more desirable; it includes the Catechism, the RSV bible, Vatican II documents, and many other essentials for understanding Catholic teaching.

All the other packages are targeted towards people who do more than cursory study of the Bible—priests, scholars, authors, speakers, etc. As a seminarian, being able to use the 'Advanced Original-Language Tools' would've been a tempting reason to upgrade to the Platinum package. But it's a matter of finding the sweet spot between how much money Verbum would save you over having to invest in a good set of references (if you don't already own them), plus the time spent flipping through said resources in search of information. And on top of that, consider that Verbum may highlight things you'd miss if you weren't using it!

In addition to what you get with base packages, you can also add on extra books and resources from <a href="https://www.logos.com/products/search?Status=Community+Pricing">Logos' large collection</a>, with generally good pricing. Most prices seem to come in a bit below what you could find on Amazon or other sites for the paperback editions.

TL;DR

Logos' Verbum is a great, albeit pricey, resource for expanding anyone's knowledge of sacred scripture. The starter package is an excellent option for most any Catholic, while the other, more expensive options are worth the price for those who spend more than a little time studying, speaking, or writing about the Bible.

Purchase Verbum online: <a href="https://www.logos.com/catholic">Verbum Bible Software</a> by Logos.
