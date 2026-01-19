---
draft: true
date: '2026-01-18T16:08:49-06:00'
# lastmod: '2026-01-18T16:08:49-06:00'
# tags: ['tag_here']
title: 'Migrating 13,000 Comments from Drupal to Hugo'
slug: 'migrating-13000-comments-from-drupal-to-hugo'
---
Earlier this year, I finished [migrating this website from Drupal to Hugo](/blog/2026/migrated-to-hugo/), after 16 years running the LAMP stack (well, technically LEMP for the last few years).

What's old is new, as this blog was _originally_ built with [Thingamablog](https://github.com/hyphanet/Thingamablog-Freenet), a Java-based Static Site Generator (SSG) that I would run on my Mac to generate HTML and FTP it up to my first webserver, over 20 years ago.

The main reason I moved from an SSG to Drupal was to add 'Web 2.0' functionality—namely, _comments_. I wanted my blog to have the same level of interactivity I had pre-Thingamablog, when I was (briefly) on Xanga.com.

For many years, Drupal comments were fine.

But over time...

  - **2009**: I finished manually migrating my old Thingamablog site [into Drupal](/blog/2009/moved-drupal-hello-drupal/).
  - **2011**: Spam became more prevalent, so for both JeffGeerling.com and [Flocknote](https://flocknote.com), I built the [Honeypot](https://www.drupal.org/project/usage) spam prevention module, which is one of the [top 50 installed projects](https://www.drupal.org/project/usage) across all Drupal sites.
  - **2020**: I [live-streamed the entire Drupal 7 to 8 migration](https://www.jeffgeerling.com/blog/2020/migrating-jeffgeerlingcom-drupal-7-drupal-8-how-video-series/), a process which spanned 16 streams and ultimately led me to focus on [my YouTube channel](https://www.youtube.com/c/JeffGeerling).
  - **2022**: After dealing with [three major DDoS attacks](/blog/2022/three-ddos-attacks-on-my-personal-website/), I decided to start the process of moving to a static site, to make it easier to stave off such attacks. Drupal has many caching mechanisms (which I've [written](/blog/2016/use-drupal-8-cache-tags-varnish-and-purge/) [about](/blog/2015/always-getting-x-drupal-cache/) [frequently](/blog/2022/clearing-cloudflare-and-nginx-caches-ansible/)), and can scale quite well—but it's easier to not have _any_ backend attack surface, however limited it may be.

And that brings us to **2026**: the blog is running on Hugo, and I _just_ finished migrating 13,189 comments across 1,119 Drupal posts.

Since the process isn't documented elsewhere, and since I hadn't heard of the comment system I'm now using ([Remark42](https://remark42.com)) until I got serious about a static site migration, I figured I'd write it up here.

## LLMs as coding assistants

After the last major migration [from a SSG _into_ Drupal](/blog/2009/moved-drupal-hello-drupal/), I noted:

> As a sad side-effect, all the blog comments are gone. Forever. Wiped out. But have no fear, we can start new discussions on many new posts! I archived all the comments from the old 'Thingamablog' version of the blog, but can't repost them here (at least, not with my time constraints... it would just take a nice import script, but I don't have the time for that now).

That would still be the case today, were it not for my desire to test out some local AI models, to assist in the migration process. I'd label myself an 'AI skeptic', but it's impressive how well LLMs can achieve certain tasks, especially if you treat them like junior devs on a small development team, break down work into reasonable-sized tasks, review the work in stages (checking in code in a VCS)—as you would if you were a technical architect.

I've had experience working with a number of teams, and I'd say the two models I was using on my Mac (gpt-oss-20b and qwen3-coder:30b, via Ollama) are on the lower-to-midrange end of dev teams I've worked with. "Frontier" models might be better than that, but they still don't solve all the issues prevalent in computer science!

> It's important to note: not one word of this blog post (nor any post on this blog, either in the past or in the future) was written by, or with the assistance of an LLM—and yes, I use em-dashes, which are easy to type on a Mac (⇧ + ⌥ + `-`). [Sosumi](https://alxwntr.com/classic-mac-os-sounds/)!

As a technical architect, I encountered:

  - **Missed requirements**: Sometimes this was my own fault, but often it was a sign of a feature that was missing something important. The code would implement a feature, but lack one or two of the important bits required to get it across the line for stakeholder approval. Sometimes it was something nobody considered, but was obvious in hindsight.
  - **Working, but suboptimal implementations**: After building at least a few hundred Drupal sites, a few of which I _guarantee_ everyone reading this has visited at least once in their lifetime, I learned a ton of design patterns that either lead to an unmaintainable disaster, or an efficient, maintainable site. The more junior the developer, the more often I'd spend more time with them trying to help them see how one approach will do better, not just now, but in the future.
  - **Premature optimizations**: The paradoxical flip-side is when someone spends _too much_ time making a feature 'right' or 'perfect'. Sometimes you just need a little feature done to move on to more pressing work. Or you know the module that it's part of is only going to be required for the migration work, and it'll be irrelevant the day after, so you don't need to spend hours optimizing it's [Big O](https://en.wikipedia.org/wiki/Big_O_notation) to shave off 3 minutes in a 7 hour process!
  - **Burnout**: Seeing patterns that lead to burnout both for myself and other members of the team, I could usually identify signs of it and tried to help project managers to lighten a load or go a little easier on devs who were in the thick of it. Sometimes it was just a matter of taking a task off that developer's back, other times pulling a feature and reworking the requirements.

The LLMs I enlisted for help seemed to hit all four of these things, at various times (yes, even 'burnout', as their context windows would grow too large for my meager Mac mini, and I'd reset and start from a fresh angle).

The big difference? I could supply a set of requirements[^requirements], and within 30-45 seconds, I would have code that runs. Maybe not code that _works_, but it would be in close proximity to the code that meets all my requirements.

With some initial successes in getting the code I needed (which is about 20% of the migration process), I was a little troubled:

_I was able to finish this entire comment migration in the span of a few evenings._

Being able to do that felt great, sure. But the fact 'senior' developers can be so productive, _without the useful work of mentoring junior devs through this process_, is a little troubling.

AI/LLMs—even the best 'frontier' models—cannot and I believe _will never_ be good at the other 80% of work involved in a content migration.

The best projects—the ones that don't go over budget and timeline—require technical and project management from people who ran the gauntlet as beginners.

We need people who've brought down the entire site with a bad query or migration step. We need people who've had to withstand the ire of an angry sysadmin on a weekend night their Friday deployment wiped out a database...

You don't just get that for free.

With AI/LLMs, and without the mentorship aspect, you end up with two types of developers:

  1. **Expert beginners**: Junior devs who (justifiably) feel like they can achieve practically _anything_ with AI coding tools. (But don't see the numerous footguns they just deployed which will all come back to bite them later.)
  2. **(Actual) 10x Developers**: Devs who _did_ go through the ringer earlier in their career, and have the tools to play AI / LLM tools like an orchestra, building great software, _fast_—and _alone_. And who now have no excuse to work on teams with junior devs and be the curmudgeons[^curmudgeons] they were meant to be.

The tough thing is, there's less of a path from #1 to #2. And that's even assuming you should strive to become a #2. I'd argue we need 'middle class' developers: devs who want to earn a living, clock in and clock out, and build software that helps the world run.

These developers also benefit from the mentorship (and sometimes consternation) they'd traditionally get early in their careers.

Sycophant LLMs are not a substitute for senior devs.

And they're also about the exact _opposite_ of what you'd want for QA[^qa].

_ANYWAY_, I went off on a bit of a tangent there. Sorry for waxing a bit on the state of AI coding today.

## Why Remark42

My requirements for a commenting system were:

  - Able to handle thousands of blog posts, and tens of thousands of comments, with threading and some form of moderation.
  - Must be self-hosted, relying on zero 3rd party APIs or websites (so, no Disqus, no [giscus](https://giscus.app), etc.).
  - Must allow anonymous (or at most, email-based) comments—no 3rd party signin or cookies required.
  - Some form of spam mitigation.
  - Can have all my Drupal comments migrated across to the new system.

[Remark42](https://remark42.com) was one of two static-site-comment systems I evaluated that met those requirements. The other one was [Meh](https://github.com/splitbrain/meh), by GitHub user splitbrain. Remark42 won out based on its history: it's been maintained for nearly a decade, versus one year for Meh.

When measuring my own site in terms of decades, I'm reluctant to incorporate software without a bit of history (even if it's great, like Meh seems!).

Remark42 was:

  - Easy to get running quickly with Docker
  - Was very fast in my testing (most pages rendered in well under 1 ms)
  - API-driven, so I know I can get data in and out fairly easily

## Remark42 Setup

I wrote up [all the details of my comment migration](https://github.com/geerlingguy/jeffgeerling-com/issues/167) on GitHub, but I'll give the quick rundown here:

  - In Hugo, I created [this `comments.html` partial](https://github.com/geerlingguy/jeffgeerling-com/blob/master/layouts/partials/comments.html) with the `remark_config` embedded for the frontend. This was fairly straightforward.
  - On my comments.jeffgeerling.com server, I built it on a DigitalOcean VPS, used Ansible to set up Docker, then used Ansible to manage the Docker Compose environment running Remark42. This was fairly straightforward.
  - For some amount of spam prevention, and for general protection for things like DDoS attacks, I have the comments server behind Cloudflare. I also have Fail2Ban running on the server, and a set of fairly strict DigitalOcean firewall rules restricting access to the VPS.
  - I wanted to have an email debugging environment for local development, so I [configured Mailpit](/blog/2026/mailpit-local-email-debugging/) in my Remark42 Docker Compose configuration as a 'dev' profile option. When I run Remark42 locally, I use the command `docker compose --env-file .env.dev --profile dev up`, which also loads in a set of environment variables (including a local SMTP configuration) stored in `.env.dev`.

## Implementation Quirks

TODO:

  - Doesn't have a ['must be approved before publish by default'](https://github.com/umputun/remark42/discussions/1019) option, which is how I moderated comments on my Drupal site (this discourages bad actors who spam out dozens or hundreds of comments in a short period of time...)
  - Doesn't have any integrated spam prevention option (I used CleanTalk on Drupal, but there's also Akismet); see https://github.com/umputun/remark42/issues/754 for any progress there
    - One possible way to combat that is turning off completely anonymous comments and requiring email verification to post; this also (by default) pulls in avatars via Gravatar... for better or worse.
  - Ran into issue where [I can't force plain text email by setting `AUTH_EMAIL_CONTENT_TYPE=text/plain`](https://github.com/umputun/remark42/issues/1988).
  - It seems like the comment form can be either light or dark — no option to set automatically based on system? So I'm using [this workaround for automatic light/dark mode](https://hndrk.blog/comments-are-there/) in lieu of that.
  - [Mailpit](https://mailpit.axllent.org) is awesome. Using it now instead of Mailgun, which has been unmaintained for like 4 years :(
  - There doesn't seem to be a global UI that I can access? (See that same ['must be approved before publish'](https://github.com/umputun/remark42/discussions/1019) discussion I linked to earlier.)
    - There's [an issue for premoderation](https://github.com/umputun/remark42/issues/1300), and an [open PR](https://github.com/umputun/remark42/pull/1966), but without a global UI, it would still be a little annoying to manage—I guess I can just rely on email notifications to know when a comment is posted, and be sure to click through from there.
    - It just lets me observe comments on posts directly. So if a spammer came in and blasted 500 blog posts, I'd have to visit each post and delete those comments? Or maybe build my own separate backend?
  - I might disable user avatars, but didn't find an efficient way to do that in Remark42 (short of editing a template or using CSS—it seems like the Gravatar stuff would still run and cache avatars regardless...). So I opened [Allow disabling avatar functionality?](https://github.com/umputun/remark42/issues/1989).

## Custom Drupal-to-Remark42 Migration Notes

TODO: More notes.

  - I initially thought there would be a global admin UI (see above), but it looks like there's just the API, and admin on individual comment pages. So failing that, I'll have to dig around the Docker container to see how the schema works for a migration/import...
  - It looks like a file is created on the host in `./var/jeffgeerling_com.db`, and it's a [Bolt (bbolt)](https://github.com/etcd-io/bbolt) key/value database. There are a few browsers out there like [boltdbweb](https://github.com/evnix/boltdbweb), [boltbrowser](https://github.com/br0xen/boltbrowser), and [bolt-ui](https://github.com/boreq/bolt-ui), should I want to go spelunking myself.

TODO...

## The final migration

For the final migration process, I created a separate issue on GitHub to track progress: [Final comment migration steps (Drupal to Remark42)](https://github.com/geerlingguy/jeffgeerling-com/issues/184).

I generally use this format (just an issue with checkboxes, or a text file with markdown-based checkboxes) when performing any potentially-destructive tasks, so I can put in exact steps, including the commands to run, and follow them in the correct order.

Having done all the steps multiple times in a dev or staging environment helps a _lot_, but there are some tasks that can only be done in prod, at least when you're like me and don't have a _true_ prod-like staging environment, with separate servers and infrastructure at every level.

TODO...

[^requirements]: Like "Here is my python export script. Add a database query that pulls all comments from a Drupal 10 database, along with comment information including email address and username, and sort that data by the node the comment is attached to, including heirarchical 'parent' information."

[^curmudgeons]: I don't mean this in a negative way (at least, most of the time). Much of my career (and personal) development resulted from conversations I've had with people who _vehemently_ disagreed with my take on a topic, feature, bug report, etc. Most people I initially thought were standoffish or ill-tempered were amazing to work with and helped me see something in an entirely different way. (This still happens regularly.)

[^qa]: Sadly, the battle for proving QA's worth is already lost in many companies. QA folks have often been the lynchpin that saves a project, in my experience, uncovering major faults well before they have a seismic impact on said project.
