---
draft: true
date: '2026-01-18T16:08:49-06:00'
tags: ['remark42', 'site', 'news', 'drupal', 'migration', 'hugo', 'comments', 'ai', 'llm', 'ollama', 'development', 'programming']
title: 'Migrating 13,000 Comments from Drupal to Hugo'
slug: 'migrating-13000-comments-from-drupal-to-hugo'
---
After 16 years on the LAMP stack, I finished [migrating this website from Drupal to Hugo](/blog/2026/migrated-to-hugo/) a few weeks ago.

What's old is new, as this blog was _originally_ built with [Thingamablog](https://github.com/hyphanet/Thingamablog-Freenet), a Java-based Static Site Generator (SSG) I ran on my Mac to generate HTML and FTP it up to my first webserver (over 20 years ago!).

The main reason I moved from an SSG to Drupal was to add _comments_. I wanted my blog to have the same level of interactivity I had pre-Thingamablog, when I was (briefly) on Xanga.com.

For many years, Drupal comments were fine.

But over time...

  - **2009**: I finished manually migrating my old Thingamablog site [into Drupal](/blog/2009/moved-drupal-hello-drupal/).
  - **2011**: Spam became more prevalent, so for use on both JeffGeerling.com and [Flocknote](https://flocknote.com), I built the [Honeypot](https://www.drupal.org/project/usage) spam prevention module, which grew to become one of the [top 50 installed projects](https://www.drupal.org/project/usage) across all Drupal sites.
  - **2020**: I [live-streamed the entire Drupal 7 to 8 migration](https://www.jeffgeerling.com/blog/2020/migrating-jeffgeerlingcom-drupal-7-drupal-8-how-video-series/), a process which spanned 16 streams and ultimately motivated a career shift to [my YouTube channel](https://www.youtube.com/c/JeffGeerling).
  - **2022**: After dealing with [three major DDoS attacks](/blog/2022/three-ddos-attacks-on-my-personal-website/), I decided started thinking about using an SSG to make it easier to stave off such attacks. Drupal has many caching mechanisms (which I've [written](/blog/2016/use-drupal-8-cache-tags-varnish-and-purge/) [about](/blog/2015/always-getting-x-drupal-cache/) [frequently](/blog/2022/clearing-cloudflare-and-nginx-caches-ansible/)), and can scale quite well—but it's easier to not have _any_ backend attack surface.

And that brings us to **2026**: the blog is running on Hugo, and I _just_ finished migrating 13,189 comments across 1,119 Drupal posts.

{{< figure
  src="./jeffgeerling-comments-remark42-v1.jpg"
  alt="JeffGeerling.com - Remark42 comments example"
  width="700"
  height="auto"
  class="insert-image"
>}}

Since the process isn't documented elsewhere, and since I hadn't heard of the comment system I'm now using ([Remark42](https://remark42.com)) until I got serious about a static site migration, I figured I'd write it up here.

## LLMs as coding assistants

After the last major migration [from a SSG _into_ Drupal](/blog/2009/moved-drupal-hello-drupal/), I noted:

> As a sad side-effect, all the blog comments are gone. Forever. Wiped out. But have no fear, we can start new discussions on many new posts! I archived all the comments from the old 'Thingamablog' version of the blog, but can't repost them here (at least, not with my time constraints... it would just take a nice import script, but I don't have the time for that now).

That would still be the case today, were it not for my desire to test out local LLMs to assist with the migration. I'd label myself an 'AI skeptic', but I admit it's impressive how well LLMs achieve certain tasks, especially if you treat them like junior devs on a small team, break down work into reasonable-sized tasks, review the work in stages (checking in code in a VCS)—as you would if you were a technical architect.

I've had experience working with a number of teams, and I'd say the two models I was using on my Mac (GPT-OSS 20B and Qwen3 Coder 30B, via Ollama) are on the lower-to-midrange end of dev teams I've worked with. "Frontier" models might be better than that, but they still don't solve all the issues prevalent in computer science!

> **Nota bene**: not one word of this blog post (nor any post on this blog, either in the past or in the future) was written by, or with the assistance of an LLM—and yes, I use em-dashes, which are easy to type on a Mac (⇧ + ⌥ + `-`). [Sosumi](https://alxwntr.com/classic-mac-os-sounds/)!

As a technical architect, I encountered:

  - **Missed requirements**: Sometimes this was my own fault, but often it was a sign of a feature that was missing something important. The code would implement a feature, but lack one or two of the important bits required to get it across the line for stakeholder approval. Sometimes it was something nobody considered, but was obvious in hindsight.
  - **Working, but suboptimal implementations**: After building at least a few hundred Drupal sites, I learned design patterns that lead to either unmaintainable disasters or efficient, maintainable sites. The more junior the developer, the more often I'd spend time with them trying to guide approaches down the less rocky path.
  - **Premature optimizations**: The paradoxical flip-side is spending _too much_ time perfecting a feature. Sometimes code will only be run one time in a migration, and it'll be irrelevant beyond that. So don't spend hours optimizing its [Big O](https://en.wikipedia.org/wiki/Big_O_notation) to shave 3 minutes off a 7 hour process!
  - **Burnout**: Seeing patterns that lead to burnout both for myself and other devs, I tried to help project managers lighten a load or go easier on devs in the thick of it. Sometimes it was just a matter of taking a task off that developer's back, other times pulling a feature and reworking the requirements.

The LLMs I enlisted for help seemed to hit all four of these things, at various times (yes, even 'burnout', as their context windows would grow too large for my meager Mac mini, and I'd reset and start from a fresh angle).

The big difference? I could supply a small set of requirements[^requirements], and **within 1-2 minutes, I would have code that runs**. Maybe not code that _works_, but it would be in close proximity to the code that meets all my requirements.

If I were assigning the same tasks to a small dev team, I wouldn't expect the first code back for review for at _least_ a day. Maybe two. And probably a full sprint (e.g. 2 weeks) before we'd have a solution ready for QA testing.

With some initial success in getting the code I needed (coding was only about half this project), I was a little troubled:

_I was able to finish this entire comment migration in a few evenings._

Being able to do that felt great, sure. But the fact 'senior' developers can be similarly productive, _without the useful work of mentoring junior devs through this process_, worries me.

AI/LLMs—even the best 'frontier' models—cannot and I believe _will never_ be good at the other 80% of work involved in a content migration.

The best projects—the ones that don't go over budget and timeline—require technical and project management from people who ran the gauntlet as beginners.

We need people who've brought down the entire site with a bad query or migration step. We need people who've had to withstand the ire of an angry sysadmin on a weekend night their Friday deployment wiped out a database...

You don't get that for free.

With AI/LLMs, and without the mentorship aspect, you end up with two types of developers:

  1. **Expert beginners**: Junior devs who feel like they can achieve _anything_ with AI coding tools. (But they don't see the enormous footguns lurking in their code.)
  2. **Lone Wolf Developers**: Devs who _did_ go through the ringer earlier in the pre-AI era, and have the tools to play LLMs like an orchestra, building decent software _fast_—and _alone_. And who now have no excuse to work on teams with junior devs and be the curmudgeons[^curmudgeons] they were meant to be.

There's less of a path from #1 to #2 now. And that's even assuming you should strive to become a #2. I'd argue we need 'middle class' developers: devs who want to earn a living, clock in and clock out, and build software that helps the world run.

These developers also benefit from the mentorship (and sometimes consternation) they'd traditionally get early in their careers.

Sycophant LLMs are not a substitute for senior devs.

And they're also about the exact _opposite_ of what you'd want for QA[^qa].

_ANYWAY_, I went off on a bit of a tangent there. Sorry for waxing a bit on the state of AI coding today.

## Why Remark42

My requirements for a commenting system were:

  - Able to handle thousands of blog posts, and tens of thousands of comments, with threading and some form of moderation.
  - Must be self-hosted, relying on zero 3rd party APIs or websites (no Disqus, no [giscus](https://giscus.app)).
  - Must allow anonymous (or at most, email-based) comments—no 3rd party signin required.
  - Some form of spam mitigation.
  - Can import all my old Drupal comments.

[Remark42](https://remark42.com) was one of two static-site-comment systems I evaluated that met those requirements. The other one was [Meh](https://github.com/splitbrain/meh), by GitHub user splitbrain. Remark42 won out based on its history: its been maintained for nearly a decade, versus one year for Meh.

Remark42 was:

  - Easy to get running quickly with Docker
  - Fast (responses under 1 ms locally)
  - API-driven, so I know I can get data in and out easily

## Remark42 Setup

I wrote up [all the details of my comment migration](https://github.com/geerlingguy/jeffgeerling-com/issues/167) on GitHub, but I'll give the quick rundown here:

  - In Hugo, I created [this `comments.html` partial](https://github.com/geerlingguy/jeffgeerling-com/blob/master/layouts/partials/comments.html) with the `remark_config` embedded for the frontend.
  - I built comments.jeffgeerling.com on a DigitalOcean VPS, used Ansible to configure security settings and install Docker, and also to manage Remark42's Docker Compose environment.
  - For spam prevention and DDoS protection, I put the server behind Cloudflare. I also have Fail2Ban running, and DigitalOcean firewall rules locking down the VPS even further.
  - For email debugging, I [configured Mailpit](/blog/2026/mailpit-local-email-debugging/) in my Remark42 Docker Compose configuration as a 'dev' profile option. When I run Remark42 locally, I use the command `docker compose --env-file .env.dev --profile dev up`, which also loads in a set of environment variables (including a local SMTP configuration) stored in `.env.dev`.

I use [Amazon Simple Email Service](https://aws.amazon.com/ses/) (SES) for email notifications on the public server. It's cheaper than other options like Mailgun, and I was already familiar with it. One quirk with SES is it takes at least 12-24 hours to get fully approved, and the setup process is _slightly_ more onerous than other email providers[^ses].

I stuck with email for notifications since it's ubiquitous, and I imagine it'll be around far beyond other notification services' useful lives.

## Implementation Quirks

As with all software, deploying Remark42 wasn't a perfect process. I ran into a number of quirks. None were showstoppers, but I do hope to see a few of these resolved:

### Spam prevention

  - Remark42 doesn't have a ['approve before publication'](https://github.com/umputun/remark42/discussions/1019) option, which is how I moderated comments on my Drupal site. Requiring explicit approval discourages bad actors who spam out dozens of comments in a short time.
  - There's no integrated spam prevention mechanism besides a basic 'honeypot-style' field. On my Drupal site, [I used CleanTalk](/blog/2018/post-mollom-what-are-best-options-preventing-spam-drupal/), but [Akismet](https://akismet.com) is another popular option. I'm following [this issue about backend spam filtering](https://github.com/umputun/remark42/issues/754).
  - There isn't a global admin UI, with an overview of all comments.

    - There's [an issue for premoderation](https://github.com/umputun/remark42/issues/1300), and an [open PR](https://github.com/umputun/remark42/pull/1966), but without a global UI, it would still be a annoying to manage things on days with many comments.

### Display issues

  - Remark42 comes with stylesheets for light and dark mode, but it doesn't set them automatically. So I'm using a [JS workaround for automatic light/dark mode](https://hndrk.blog/comments-are-there/).
  - I might disable user avatars, but I couldn't find an efficient way to do that in Remark42, outside of hiding them in a template or with CSS. It _seems_ like the Gravatar integration would still run and cache avatars regardless. So I opened [Allow disabling avatar functionality?](https://github.com/umputun/remark42/issues/1989).

## Getting comments out of Drupal

Remark42 comes with [importers for Disqus, Wordpress, and Commento](https://remark42.com/docs/backup/migration/). Because Drupal's built-in commenting system is conceptually similar to Wordpress, I built a [Python script](https://github.com/geerlingguy/jeffgeerling-com/blob/master/drupal-export/drupal_to_remark42.py) to export Drupal comments in the same XML format as a [Wordpress export](https://wordpress.com/support/export/).

I briefly considered migrating straight from Drupal into the [Bolt (bbolt)](https://github.com/etcd-io/bbolt) key-value database Remark42 uses. But because of the lack of familiar tooling around it (like [Sequel Ace](https://sequel-ace.com) for MariaDB or [Base](https://menial.co.uk/base/) for SQLite), I decided to stick with the Drupal -> Wordpress -> Remark42 option.

Using GPT-OSS 20B and Qwen3 30B A3B, I got a good start on the export script, but I did spend time tweaking the SQL and fiddling with the XML structure, since the AI models missed the finer details.

I built a local environment for testing on the Hugo site, and built a little configuration toggle in my `hugo.toml` file so I could enable or disable comments site-wide very quickly:

```toml
[params]
  ...
  commentsGlobalEnable = true # set to 'true' to enable Remark42 comments.
```

I then use the conditional `{{ if .Site.Params.commentsGlobalEnable }}` in my [`comments.html`](https://github.com/geerlingguy/jeffgeerling-com/blob/master/layouts/partials/comments.html) partial template, to either display the Remark42 embed, or a 'Comments disabled' message.

I spent a couple hours testing and re-testing the entire migration, spot-checking a number of posts with different features (many comments, no comments, deeply-threaded comments, etc.).

To get all features working locally, I also had to set up local domains for my website inside `/etc/hosts`:

```
127.0.0.1 dev.jeffgeerling.com
127.0.0.1 dev-comments.jeffgeerling.com
```

Otherwise you'll bump into issues testing the importer through `localhost`. I even had to force Docker to use the right IP address for the Hugo site running on my Mac host (outside the Docker environment), by adding `extra_hosts` in the `docker-compose.yml` file:

```yaml
services:
  remark:
    image: ghcr.io/umputun/remark42:v1.15.0
    container_name: "comments_jeffgeerling"
    hostname: ${HOSTNAME}
    extra_hosts:
      - "${DEV_HOST_MAPPING:-dummy:127.0.0.1}"
    ...
```

Then in my `.env.dev`:

```
HOSTNAME=dev-comments.jeffgeerling.com
DEV_HOST_MAPPING=dev.jeffgeerling.com:192.168.65.254  # host.docker.internal IP
```

## The final migration

For the final migration process, I created a separate issue on GitHub to track progress: [Final comment migration steps (Drupal to Remark42)](https://github.com/geerlingguy/jeffgeerling-com/issues/184).

{{< figure
  src="./jeffgeerling-com-remark42-migration-steps-github-issue.jpg"
  alt="JeffGeerling.com - Remark42 migration steps"
  width="700"
  height="auto"
  class="insert-image"
>}}

I use this format (just an issue with checkboxes, or a text file with markdown-based checkboxes) when performing any potentially-destructive tasks, so I can put in exact steps, including the commands to run, and follow them in the correct order.

Having done all the steps multiple times locally helped a _lot_. But there are certain tasks that can only be done in prod, at least when you're like me and don't have a _true_ prod-like staging environment, with separate servers and infrastructure at every level.

The most annoying task was getting SSL working, because I was using strict SSL through Cloudflare.

Once I got a local self-signed cert figured out, I immediately got a ton of invalid traffic on the new server. This problem ("new VPS gets flooded with traffic immediately") is a bit annoying, because VPS providers like DigitalOcean recycle IPv4 addresses quickly—and bring along the baggage of the old IP at the same time...

So I locked down the DigitalOcean Firewall on the comments VPS the same way I did my main site VPS. But then I noticed the Remark42 container was running at 100% CPU constantly.

Long story short, I realized by trying to [disable comment editing](https://github.com/geerlingguy/jeffgeerling-com/issues/184#issuecomment-3758163759), I had caused an infinite loop in the container startup process, and it ate up all my server's CPU.

Therefore I opened one final issue, [If I set EDIT_TIME=0, container uses 100% CPU forever on init](https://github.com/umputun/remark42/issues/1991), and set edit time back to '5 minutes'.

The server was finally running well, and the final snag was needing to add my self-signed comment server cert to the server's certificate store, because the Go library Remark42 uses when importing comments through Remark42's API requires a _trusted_ certificate (even when running on localhost!).

So:

```bash
/srv # cp var/cert.pem /usr/local/share/ca-certificates/
/srv # update-ca-certificates
```

And finally, the import worked:

```bash
/srv # import --url=https://comments.jeffgeerling.com:8443 -p wordpress -f /srv/var/exported-comments.xml -s jeffgeerlin
g_com
remark42 v1.15.0-307e69e-20251224T02:45:51
2026/01/15 23:54:29.727 [INFO]  import /srv/var/exported-comments.xml (wordpress), site jeffgeerling_com
2026/01/15 23:54:29.852 [INFO]  completed, status=202, {"status":"import request accepted"}
```

It took a while, because Remark42 _also_ verifies each comment post URL prior to importing the comments (you can't run the comment server standalone for an import).

After twiddling with some of my DDoS prevention rules in Cloudflare, I was able to get all Remark42 functionality running—along with all 13,000+ Drupal comments—on this website!

## The Grass is Always Greener...

Will this site go back to a CMS at some point? Maybe. But probably not.

I spoke to a former colleague in the middle of the migration—someone who's been running a personal blog on Drupal four years longer than _I_ have!

His perspective (given in the midst of the comment migration process) was useful in tempering my excitement over having gone static.

Instead of having a fully dynamic website, with native comments, a deep caching system, built-in search (with modules to improve all these things), I now have a static website, which needs a separate server for comments, and I'll soon implement a [less flexible site search solution](https://github.com/geerlingguy/jeffgeerling-com/issues/168)!

_However_, part of my goal in moving to a static site is being able to test various hosting options, some of them very exotic—and limited in processing power. Therefore a static site only requiring an HTTP server and a few MB of RAM is a bonus.

So far, I've had a good experience running Remark42 (for about a week) and Hugo (for almost three weeks). I haven't encountered DDoS-level traffic, so I have yet to see how it'll hold up in that condition.

Whatever happens, I'll continue developing my website—as I do all my projects—in the open [over on GitHub](https://github.com/geerlingguy/jeffgeerling-com).

[^requirements]: Like "Here is my python export script. Add a database query that pulls all comments from a Drupal 10 database, along with comment information including email address and username, and sort that data by the node the comment is attached to, including heirarchical 'parent' information."

[^curmudgeons]: I don't mean this in a negative way (at least, most of the time). Much of my career (and personal) development resulted from conversations I've had with people who _vehemently_ disagreed with my take on a topic, feature, bug report, etc. Most people I initially thought were standoffish or ill-tempered were amazing to work with and helped me see something in an entirely different way. (This still happens regularly.)

[^qa]: Sadly, the battle for proving QA's worth is already lost in many companies. QA folks have often been the lynchpin that saves a project, in my experience, uncovering major faults well before they have a seismic impact on said project.

[^ses]: But it's a lot easier than maintaining my own SMTP server! Email deliverability is challenging enough when using cloud email providers...
