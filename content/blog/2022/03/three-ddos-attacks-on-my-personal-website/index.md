---
nid: 3192
title: "Three DDoS attacks on my personal website"
slug: "three-ddos-attacks-on-my-personal-website"
date: 2022-03-16T14:00:29+00:00
drupal:
  nid: 3192
  path: /blog/2022/three-ddos-attacks-on-my-personal-website
  body_format: markdown
  redirects: []
tags:
  - cloudflare
  - ddos
  - hacks
  - monitoring
  - security
  - uptime
  - video
  - website
  - youtube
---

> **Update**: After posting the video yesterday, the site was hit by more low-complexity DDoS attacks, mostly just spamming one URL at a time. After I cleaned those up, the attacker finally switched to a more intelligent offense, posting _actual comments_ to the site overnight. This morning I noticed that, and the fact the attacker found I left my edit domain un-proxied, so I switched to a different IP on DigitalOcean and shored up the Cloudflare configuration a bit more.
>
> It was a good thing I did that, because about the same time, I got an email from DigitalOcean support saying they had to blackhole the other IP for [getting 2,279,743 packets/sec](https://github.com/geerlingguy/jeffgeerling-com/issues/141#issuecomment-1070990773) of inbound traffic. Sheesh.
>
> After cleaning up a few bits of fallout, the site should be running a bit better at this point, DDoS or no.

My website just got DDoSed. At first, I thought it might've just been a DoS, or Denial of Service, attack, where one person sends a bunch of traffic and makes it so the website is so overloaded it can't respond to every request.

But after digging through my logs, I found it was definitely a DDoS, or Distributed Denial of Service attack. There were thousands of computers around the world hitting my website with over 3 thousand POST requests per second.

In this post, I'll run through:

  1. What happened
  2. How I got my site back online
  3. What I learned in the process.

And I'll also briefly discuss how all this relates to Russia's invasion of Ukraine; stay tuned to the end for that!

## Video

This blog post is a lightly-edited script from my YouTube video on the same topic:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class="embed-container"><iframe src="https://www.youtube.com/embed/VPcYMgTYQs0" frameborder="0" allowfullscreen=""></iframe></div>
</div>

## How it Happened

On February 9th, at 9 a.m., I posted a new video to my YouTube channel. The video showed how I was [hosting this website on a farm](/blog/2022/hosting-website-on-farm-or-anywhere) on the Turing Pi 2 cluster over 4G LTE.

In the video, I said:

> The only major risk is if a lot of people post comments at the same time, because all that traffic has to go through to the cluster so the comments get saved in the site's database.

...Maybe I shouldn't have tempted fate. I was worried about legitimate traffic and comments, but since I haven't encountered a DDoS attack on this site in 10 years, _that_ possibility wasn't even on my radar.

So I posted the video, and after a bit, I posted a link to the blog post on Hacker News. Within a few minutes, I saw the story hit the front page on HN—which was a bit odd and [almost led to me getting banned](/blog/2022/i-almost-got-banned-hacker-news)—but, as usual the traffic on the site went up a bit, with over 150 visitors on the site at 10 a.m.

Blog posts from my site have hit HN's front page in the past, so I knew what to expect, and the cluster was handling it fine.

{{< figure src="./ddos-traffic-hn-slow-rise.jpg" alt="DDoS Traffic slow rise on HN" width="700" height="166" class="insert-image" >}}

This graph shows the slow rise in traffic to the backend as some users were commenting and hitting pages on the site that weren't cached by my VPS. I was responding to some comments on YouTube, when I got an email at 10:41 a.m. from Uptime Robot: _JeffGeerling.com was down_.

I saw a huge spike in traffic on the VPS that was proxying the Pi cluster. The monitoring stopped working once the server was overloaded, but before that happened, Munin saw over 2,000 requests per second.

{{< figure src="./hacker-news-traffic-dies-ddos-begins.jpg" alt="DDoS begins on Drupal backend" width="700" height="117" class="insert-image" >}}

I also saw a pretty sharp rise in traffic hitting the Pi cluster, but each of the Pis were actually handling the requests fast enough. Kubernetes was still responsive, so I knew the problem was on my VPS.

Ten minutes in, I logged back into my VPS and noticed it's load was really high, with hundreds of stuck `php-fpm` threads.

That was definitely the bottleneck, and somehow whoever was sending this traffic was busting through my cache layer. PHP couldn't catch a break, and Nginx had to drop requests.

{{< figure src="./ddos-post-requests.jpg" alt="DDoS - POST requests that were hitting the site" width="700" height="328" class="insert-image" >}}

Someone was sending thousands of these 'POST' requests through to my site. I ran [this command](https://github.com/geerlingguy/jeffgeerling-com/issues/141#issuecomment-1034089891) to sort requests by IP address, and found it was _definitely_ a DDoS, because thousands of requests were coming from IPs all over the world.

I knew I needed to save some of this data off so I could sort through it later, so I started screenshotting everything, and I opened up a text file to dump everything I found.

The first thing I learned many years ago the first time I dealt with a major traffic spike for an enterprise website:

Always document everything that's happening, for two reasons:

  1. You'll need it later when you try to figure out exactly what happened and how to prevent it from being a problem in the future.
  2. It helps your brain to slow down a little so it can piece together the next steps.

The first thing I tried was blocking IPs in Nginx's configuration. Initially, most requests were [from one IP in Germany](https://twitter.com/ericlacasse/status/1491466867533299720), but after I blocked that, ten more rose up in its place.

I also attempted to [add rate limiting to my Nginx config](/blog/2022/rate-limiting-requests-ip-address-nginx) using the `limit_req` feature, but that was tricky to get right and I ended up causing other problems for legitimate visitors.

So instead of spending hours playing whack-a-mole with IPs, I decided to put my site behind Cloudflare.

## Cloudflare

{{< figure src="./Nginx-Reverse-Proxy-4G-LTE.jpg" alt="Nginx reverse caching proxy over 4G LTE to Turing Pi cluster" width="700" height="396" class="insert-image" >}}

I already used Nginx to cache and proxy my Pi cluster so it would be somewhat shielded from a direct DoS attack, but my single VPS in New York couldn't handle the full onslaught of a targeted DDoS punching through the cache.

Cloudflare has thousands of servers in hundreds of data centers around the world, and a huge amount of bandwidth capacity. They handle DDoSes every day, all day, and have a fully-staffed NOC where they monitor things. I just had little old me, and I just wanted my website back up and running so I could focus on other things in life.

[Screen Shot 2022-02-09 at 11.55.40 AM.png]

Once I could confirm my DNS was migrated to Cloudflare, I set up a DigitalOcean firewall rule that only let Cloudflare's servers access my VPS over HTTP (there's unfortunately no automated way to manage it, so I'll have to reconcile Cloudflare's IP list with the firewall rule manually).

Now _all_ the traffic hitting my website went through Cloudflare. If I left the server exposed, attackers could still hit the server directly.

I added a page rule on Cloudflare to cache everything, but the POST requests were still getting through, so I added a Cloudflare Firewall rule to completely block all POST requests, at least until I could get things in order.

Thirty minutes later, Cloudflare had already blocked 6 million POST requests, and my site was stable.

Both munin's graphs and Cloudflare showed that the attack was a sustained 3,300 POST requests per second—about 40 Mbps of traffic—coming from all over the world. My server could handle that much raw traffic if it were legitimate (like a front page post on HN or Reddit), but because it was all POST requests, the server got crushed as PHP was run for each request.

At this point I opened [this GitHub issue](https://github.com/geerlingguy/jeffgeerling-com/issues/141) to document everything, and took a break for lunch.

## Cleanup

After lunch, it looked like the attacker finally gave up. So I switched the POST blocker to not block _everyone_ (including me, from logging in!), but still use a challenge to slow down bot attacks. So now people could comment on the site, but some of them might have to enable Javascript and solve a CAPTCHA (sorry for the inconvenience!).

Because I'm running a relatively complex Drupal website, I had to clean up the mess this new proxy layer created.

First of all, some users on Twitter noticed some of my subdomains were offline. They're on different servers, but when I migrated my DNS to Cloudflare, it didn't include any subdomain records. So I had to add back records for sites like [ansible.jeffgeerling.com](https://ansible.jeffgeerling.com) and my [Pi PCI Express website](https://pipci.jeffgeerling.com).

Then I realized I couldn't save new blog posts on my site, because Cloudflare's proxying interfered with the complex POST requests Drupal uses to prevent unauthorized access. So I [set up a separate Edit domain](https://github.com/geerlingguy/jeffgeerling-com/issues/144) (this is pretty common with large-scale Drupal sites that deal with multiple proxy layers).

> I know, at this point, some of you are shouting from the rooftops "use a static site generator! Drupal's not for blogs!" I know... but comments are—for me—an essential and very useful part of this blog. And so far I hate all the hosted comment solutions that make SSGs work with comments. Someday, maybe...

{{< figure src="./cloudflare-drupal-ddos-duplicate-rss-items.jpg" alt="Cloudflare and Drupal duplicate RSS items in feed" width="700" height="413" class="insert-image" >}}

Then people started reporting they were seeing duplicate stories from my site in their news readers. Yes, RSS is alive and well, and yes, I still hate that Google killed Reader. I [think I got that fixed](https://github.com/geerlingguy/jeffgeerling-com/issues/145), but there are still a couple other lingering issues.

So I've been cleaning up all the fallout, and I decided to power off the Pi servers at my house—for now. Since I'm using Cloudflare, I might bring it back up again, but using a Cloudflare Tunnel instead of an SSH tunnel to my VPS. I mentioned that feature in my farm hosting video, but didn't want to rely on an extra 3rd party service.

But if I'm going to have to use Cloudflare to shield against DDoS attacks... might as well use their Tunnel feature, too.

Speaking of shielding against DDoS attacks... after I relaxed my POST rule, I ended up getting two _more_ DDoS attacks (pretty much identical to the first):

{{< figure src="./ddos-cloudflare-requests-jeffgeerling.jpg" alt="DDoS Traffic Request log from Cloudflare" width="700" height="351" class="insert-image" >}}

So three attacks in a week, after a decade with none. Cloudflare served up over 25 million requests, and that was _after_ an hour of my VPS trying to stay alive all on its own that first day.

In the end, Cloudflare served 300 GB of traffic over the course of a few hours. By my estimation, if I'd left the Pi cluster running over 4G and didn't have any caching, that would've cost me $1,400 in data charges.

Luckily I'm not an idiot, so I didn't leave it running in that configuration since the day I released the video, and I kept my wireless usage under my plan's limits.

## Learnings

So now that I've had some time to go through the data, and clean up some of the mess, I have some thoughts.

### Monitoring and Alerting

First of all, time and time again, every time I've encountered something like this, **good monitoring and alerting** is the first line of defense, and without it, you're completely blind.

When I helped build a commerce platform for some of the most popular music artists in the world, we had detailed graphs of _everything_. We had days with hundreds of thousands of _legitimate_ requests within seconds of a merch drop.

I had the budget to throw hardware at the problem, but without the right monitoring, we would've lost millions of dollars in sales per year if it took too long to find the exact problem.

Instead, we only had a few minutes of downtime, and helped the development team fix a few bugs that made the stores scale much more quickly.

{{< figure src="./ddos-eth0-traffic-three-attempts.jpg" alt="eth0 traffic from 3 DDoS attacks via Munin" width="700" height="394" class="insert-image" >}}

On my personal projects, I've been using [Munin](https://munin-monitoring.org) (pictured above) since around 2006, and it's chugged along without any issues, giving me insights from a separate monitoring server so I can still react even if my main servers go offline.

For enterprise projects I've worked on, when budgets are more than five bucks a month, I've been able to use log monitoring services like [SumoLogic](https://www.sumologic.com), [DataDog](https://www.datadoghq.com/), [New Relic](https://newrelic.com), or [Splunk](https://www.splunk.com).

You can also self-host tools like Prometheus and Grafana, Zabbix, or even Munin like I use here. It all depends on what you need, and what you can invest in it. But in the end, you need monitoring—you need insights into exactly what's happening on your servers.

### Chilling effect?

The second thing I've learned is that I need to adjust my appetite for risk, at least a _little_.

For years, I've been cavalier showing the inner workings of my homelab setup and hosted services. I'm  open source by nature, and while I keep things secure and up-to-date, it's practically impossible to prevent DDoS attacks against public IPs unless you route everything through CDNs or have unlimited bandwidth.

I should probably be a little more careful about IP addresses and specific references in public repos. But I won't stop doing any of this stuff, because it's just too fun to share it all.

## War in Ukraine

{{< figure src="./ukraine-ddos-attacks.jpg" alt="Ukraine Bloomberg Headline about DDoS attacks" width="700" height="337" class="insert-image" >}}

What does any of this have to do with the war in Ukraine? Well, in addition to soldiers on the battlefield, Ukraine and Russia are also in the midst of one of the largest IT wars ever waged.

All around the world, there's been organic resistance to the Russian invasion through [DDoS attacks on critical Russian websites](https://www.reuters.com/technology/russian-company-websites-hit-by-increased-hacking-march-says-cyber-firm-2022-03-11/).

It's gotten to the point where the Russian government is [throwing up a massive firewall](https://www.nytimes.com/2022/03/07/technology/russia-ukraine-internet-isolation.html) around their country and giving up trying to mitigate the constant barrage of traffic.

How does it work? Well, one educational example is the [UA Cyber Shield](https://github.com/opengs/uashield) project on GitHub.

In the description, it states that they don't support unlawful attacks on anyone else's website, and that the software is provided only for educational purposes, but, well... I'm guessing there's at least a _few_ people in the world who aren't only testing their own website with tools like this.

But the point is, UA Cyber Shield is one of thousands of small programs people are running—both good and bad—on computers all around the world. Most of the computers running DDoS tools are parts of 'botnets'—they're computers, routers, and even 'smart' devices around the world that have been hacked and send a barrage of traffic at their targets.

Unless you have the bandwidth and resources to black-hole the traffic, [like Cloudflare does](https://blog.cloudflare.com/cloudflare-thwarts-17-2m-rps-ddos-attack-the-largest-ever-reported/), you have no option but to go offline until the traffic stops.

And even Cloudflare has its limits. Google, Amazon, Azure, and Cloudflare have all stopped historic DDoS attacks in the past few years. Attackers constantly adapt, and it doesn't help that the Internet is flooded with more hacked IoT 'smart devices' and old hacked routers every day.

The backbone of the Internet still has some ugly flaws that make things like DDoS attacks too easy for the attacker, and hard if not impossible for the defender.

I don't like the centralization of all Internet traffic around services like Cloudflare, AWS, and Google, but it's practically the only way to keep a website online nowadays, if you have any notoriety at all.
