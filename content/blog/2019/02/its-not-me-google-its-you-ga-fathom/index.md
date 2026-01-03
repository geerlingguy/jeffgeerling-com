---
nid: 2907
title: "It's not me, Google, it's you - from GA to Fathom"
slug: "its-not-me-google-its-you-ga-fathom"
date: 2019-02-08T03:53:50+00:00
drupal:
  nid: 2907
  path: /blog/2019/its-not-me-google-its-you-ga-fathom
  body_format: markdown
  redirects: []
tags:
  - analytics
  - ansible
  - automation
  - digitalocean
  - docker
  - fathom
  - google
  - privacy
---

> **tl;dr**: I'm now using Fathom for my personal website analytics, and it's easy to self-host and maintain, better for privacy, and can lead to better site performance.

Since the mid-2000s, right after it became available, I started using [Google Analytics](https://analytics.google.com/analytics/web/) for almost every website I built (whether it be mine or someone else). It quickly became (and remains) the de-facto standard for website usage analytics and user tracking.

{{< figure src="./google-analytics_0.png" alt="Google Analytics UI" width="650" height="421" class="insert-image" >}}

Before that you basically had web page visit counters (some of them with slightly more advanced features ala [W3Counter](https://www.w3counter.com) and [Stat Counter](https://statcounter.com/free-hit-counter/)), and then on the high end you had Urchin Web Analytics (which is what Google acquired and turned into a 'cloud' version, naming the new product Google Analytics and tying it deeply into the Google AdWords ecosystem).

<p style="text-align: center;">{{< figure src="./urchin-web-analytics-logo.gif" alt="Urchin Web Analytics Logo" width="150" height="95" class="insert-image" >}}<br>
<em>With such a fun logo, how could Google resist acquiring it?</em></p>

The amount of data you can get out of GA is pretty amazing, and you can add custom event tracking, track website goals and conversion rates, and program your own metrics and events. But this all comes at a cost; sure, Google Analytics is _free_, but Google uses the gobs of data about Internet usage it gets from [tracking half the Internet](https://en.wikipedia.org/wiki/Google_Analytics#Popularity) for it's own purposes (much like it uses free-to-upload Google Photo data for AI training purposes). Not only that, trying to get just the data that I care about out of Google Analytics can be a time sink. Plus, I have to disable my ad blocker every time I go to view analytics!

So in the interest of going back to a simpler time, when I ran my own Urchin server and tracked analytics locally, I've decided to give [Fathom](https://usefathom.com) a chance, and started sending all the analytics for my personal and SaaS websites to a new Fathom server:

{{< figure src="./fathom-analytics.png" alt="Fathom Analytics UI" width="650" height="420" class="insert-image" >}}

In this blog post, I'll document how I did it, how it's working out, and compare it to Google Analytics. Maybe by the end you'll want to try it out, too!

## Building a reproducible Fathom server

Many people know me as 'the Ansible guy'—either for my [book](https://www.ansiblefordevops.com), or for one of a zillion posts I've written on Ansible (mostly for my own memory, but luckily they're helpful for others too!). I noticed that there so far was no Ansible role on Galaxy for Fathom, so I went ahead and added [`geerlingguy.fathom`](https://galaxy.ansible.com/geerlingguy/fathom).

Using that role (alongside a few others), you can install a production-grade Fathom instance in just a few lines of YAML:

```
---
- hosts: analytics
  become: true

  vars_files:
    - vars/main.yml

  roles:
    - geerlingguy.repo-epel
    - geerlingguy.security
    - geerlingguy.firewall
    - geerlingguy.fathom
    - geerlingguy.certbot
    - geerlingguy.nginx
    - geerlingguy.git
```

I set the appropriate variables for fathom, nginx, and certbot in `vars/main.yml`, but other than that, it's a tiny Ansible playbook (this is _literally_ the playbook I am using, right now, for that server), and I coupled that with another short provisioning playbook which builds a Digital Ocean 1 GB VPS running CentOS 7 and adds a user account for me, and in less than 1.5 hours I went from never having downloaded Fathom to having a nice little production-grade Fathom analytics server!

If you want to use my Ansible role to build your own Fathom server, I'd encourage you to check out the [role's documentation](https://github.com/geerlingguy/ansible-role-fathom/blob/master/README.md) and try it yourself. Fathom also offers an open source [Docker image](https://hub.docker.com/r/usefathom/fathom) you can use if you want to deploy it even more easily. In fact, if you have Docker installed and want to try Fathom in less than a minute, just run:

    docker run -d -p 8080:8080 usefathom/fathom:latest

Then visit http://localhost:8080/ enter the domain for a website you want to track. Note that you would only be able to track websites which can hit your localhost, and the data stored would be wiped out when you remove the container (the above is just for testing).

## Using Fathom

One thing I look for in software (especially if I don't have time to dive too deep into the source code) is simplicity—is the initial experience well-though-out, and easy to understand, or are there a lot of roadblocks?

Fathom ticks off the box for both being dead-simple to install and run (most Go apps seem to be, since they're just binaries you download), and easy to get started tracking your first website (it comes up and asks you for a domain to track, then shows a box where you can copy out the tracking code to put on the site).

There are a few little UI issues I've found which will likely get ironed out in coming months:

  - It's not obvious that you can't add more sites until you've created a user account (command line only right now)
  - There are animations which occur on graphs and data every time you click on things (this will be able to be turned off soon)
  - The UI has a few elements which aren't very accessible (e.g. font size is small and it has grey-on-grey... it looks like they copied _one_ bad feature from Google Analytics ?).

But overall the UI is consistent, and didn't take long at all to master (especially owing to its spartan feature set).

### Features

In its current state, Fathom is almost the polar opposite to a tool like Google Analytics. Whereas in GA you can quickly get lost eight levels deep in a certain metric, Fathom can feel quite spartan in the fact that there isn't yet a concept of 'drilling down'.

Right now the UI exposes a few things:

  - Date selection
  - Hourly or daily graph frequency
  - Basic metrics (unique visits, pageviews, avg. time on site, and bounce rate)
  - A list of top pages
  - A list of top referrers
  - The ability to track more than one site
  - The ability to add more than one user to access the UI

While there's a [public roadmap](https://trello.com/b/x2aBwH2J/fathom-roadmap) for new features and an [issue queue on GitHub](https://github.com/usefathom/fathom/issues) (Fathom is open source, licensed with the MIT license), progress is slow but steady.

A few of the little things that I _do_ actually miss from GA so far (which hopefully will show up in a future version of Fathom) include:

  - Browser / OS metrics (right now they're not exposed in any way)
  - The ability to drill into referrer data (right now every site's top referrer is "Google"... but you have no way of seeing the previous URL or search that led to the site)
  - The ability to see the graph in near-real time (though there _is_ a nice continuously-updating "current visitors" metric)

All that said, I'm actually a lot happier with Fathom than I have been with Google Analytics, because the three metrics I care about most (time on site, visits, and referrers) are there, and 'above the fold'. With Google Analytics I rarely even visited the dashboard anymore because it felt like I had to spend 10 minutes getting all the data I needed—and I wasn't going to spend hours building custom dashboards for all my sites in different accounts!

## Privacy

This was actually my main motivation behind actually making the move this year. Last year I deleted my Facebook account, and this year I'm trying to make sure my websites are even more divorced from 'social tracking'. I have removed social integration from most of them (just sticking a 'like' or 'tweet this' button means social giants get to track all users who hop through your site!), and my page size and overall page load times are so much the more better.

Not to mention, people's data and privacy are better-protected.

Google has traditionally been good (as far as I can tell) about not-being-evil, but in the past few years my faith (and many others, if the Hacker News crowd is to be believed) has really been shaken and much of the goodwill and trust developers and techies used to give Google has been lost—especially as they [sunset project after beloved project](https://killedbygoogle.com) without much regard for the end users!

The main benefit of running Fathom on my own server, from a privacy perspective, is that every ounce of the user's tracking data is only stored, transmitted, and tracked by my own website—and I don't have to [agree to share that data with Google and Third Parties](https://www.google.com/analytics/terms/us.html). I no longer have to sacrifice my site's users' privacy to Google's data-hungry advertising AIs.

If I were to use the paid cloud/hosted version of Fathom instead of the self-hosted version, I can at least evaluate the tracking code myself, and see exactly what data is flowing from my site's users into Fathom's systems. And judging by their past actions and words, I have a fair bit of trust that Fathom's founders will stick by their privacy-first stance.

## Performance

Wondering how analytics trackers (most of which load asynchronously these days) affect overall page performance and bandwidth usage, I tested with both Google Analytics and Fathom to see how large the payload is and how fast the tracker javascript loaded, and whether it made any noticeable difference in overall page load time.

Google Analytics JS takes around 30-40ms to load (TTFB 20ms) on my home Internet connection, and after a test of loading a full static HTML page (comparable to jeffgeerling.com) a few hundred times with and without Google Analytics, the difference in full page load time was around 60ms. The JS that is returned totaled 17.2 KB gzipped (43.1 KB uncompressed).

Using Fathom running on a separate 1 GB VPS on Digital Ocean, I am able to load the `tracker.js` file in around 50ms (TTFB 45ms), and it affects the entire page load time similarly to the GA js, adding around 60ms total to render/processing time. The JS that is returned totaled 1.5 KB gzipped (2.7 KB uncompressed).

<table>
  <tr>
    <th>Analytics Tool</th>
    <th>tracker load time</th>
    <th>tracker size (gzipped)</th>
  </tr>
  <tr>
    <td>Google Analytics</td>
    <td>40ms</td>
    <td>17.2 KB</td>
  </tr>
  <tr>
    <td>Fathom</td>
    <td>50ms</td>
    <td>1.5 KB</td>
  </tr>
  <tr>
    <td>Difference</td>
    <td>1.25x slower</td>
    <td>11x smaller</td>
  </tr>
</table>

Now, if you're a content marketer who's used to tossing a veritable soup of tracking systems into every website you work on (hey let's add Tealium! And Adobe Analytics! We need click heatmaps, so we should have HotJar too. Oh and Mixpanel is all the rage, so need that too...), then the difference of 15 KB might not mean much.

But I'm an _engineer_. I care about _performance_. I often browse the web on my phone in a waiting room, or a car on a road trip... and Internet is slow. Like dial-up slow. So if your website takes more than 30 seconds to load because you have over 1 MB in gzipped Javascript, I'm going to close out that window and go elsewhere.

I also ran the test using one of the most lightweight websites I maintain, a static site for my book, [Ansible for DevOps](https://www.ansiblefordevops.com). Using Pingdom Tools a few times during the day to check before (with Google Analytics) and after (with Fathom), here are the results (averaged from three tests at a time each, spaced out by about 30 minutes, so 9 tests total for each analytics tool):

<table>
  <tr>
    <th>Tool</th>
    <th>Page Size</th>
    <th>Load time</th>
  </tr>
  <tr>
    <td>Google Analytics</td>
    <td>128.6 KB</td>
    <td>367ms</td>
  </tr>
  <tr>
    <td>Fathom</td>
    <td>112.2 KB</td>
    <td>226ms</td>
  </tr>
  <tr>
    <td>Difference</td>
    <td>16.4 KB smaller</td>
    <td>1.6x faster</td>
  </tr>
</table>

You should have a strategy for analytics, a budget for how much page weight and performance you're willing to sacrifice to get that sweet, sweet analytics data juice—most of the time the web developers just roll over when marketing or sales requires the addition of _yet another analytics tool_. But it shouldn't be so.

### Performance of Fathom (server)

There's also the question of performance of Fathom, the open source Go application itself; I'm currently using it with an SQLite database (which gains about 300-500 KB/day so far), and the system has rarely been over 0.03 avg load, with fathom only consuming ~42 MB of RAM after a week of analytics.

If you're concerned you wouldn't be able to host it yourself, and maintain a decent backup, Fathom also offers paid plans—though they're a bit expensive for my taste, especially if you're considering using it for some tiny sites that only get a few dozen or a few hundred pageviews a day.

I'm currently monitoring the Fathom server long-term with munin and will see how events like traffic spikes affect performance. Maybe this blog post will be the first test of that!

## Summary

I set out to see if it would be painless to transition my personal web analytics from Google Analytics—the 800-pound gorilla of the web analytics world—to Fathom, an upstart which has yet to prove its mettle.

The experience has been extremely positive. The performance of Fathom on a 1 GB VPS, even while tracking 2 moderate-traffic and 4 light-traffic sites, has been much better than I expected. And even when that server is offline (I tested this, of course!), page load times and page weight have gotten better for every site I've tested.

If you aren't required to track and store all the data that Google Analytics stores, and you can live without a few of the niceties, you should definitely consider using [Fathom](https://usefathom.com)!
