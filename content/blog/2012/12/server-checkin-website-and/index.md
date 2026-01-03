---
nid: 2140
title: "Server Check.in - Website and Server uptime monitoring"
slug: "server-checkin-website-and"
date: 2012-12-10T15:40:53+00:00
drupal:
  nid: 2140
  path: /blog/2012/server-checkin-website-and
  body_format: full_html
  redirects: []
tags:
  - design
  - drupal
  - drupal planet
  - midwestern mac
  - server
  - services
---

<a href="https://servercheck.in/">Server Check.in</a> is a simple and inexpensive server and website uptime monitoring service I've recently launched.

<p style="text-align: center;"><a href="https://servercheck.in/">{{< figure src="./server-checkin-logo-300.jpg" alt="Server Check.in logo" width="300" height="300" class="blog-image" >}}</a></p>

If you have a website or online service you need to make sure is running, Server Check.in is a great way to get notified when there's a problem. Unlike most other monitoring solutions, Server Check.in offers free SMS (text) messages and email notifications, and it only costs $15/year (just $1.25/month!).

<h2>The Motivation</h2>

There are probably thousands of other uptime monitoring services on the web, and it's typically a good idea to use existing tools rather than build your own—if they're practical for your needs!

I had three main requirements for any service I wanted to use:

<ol>
<li>I needed to monitor a few websites (at least three).</li>
<li>I didn't want to spend more than ~$20/year.</li>
<li>I needed SMS (text message) notifications, and I didn't want to pay a bunch extra to get them.</li>
</ol>

Many services hit one or two of these marks—some extremely well! However, no service I found could meet all three of these requirements, though a few did come close.

Knowing that SMS messaging is relatively cheap (typically around $0.01 or less per message), and knowing that I needed a new challenge, I decided to build myself the best possible server monitoring and notification system I could—for myself. I built every feature I wanted, and made it fit my workflow perfectly. It's ridiculously simple, it lets me get email and SMS notifications, and it even shows me how my sites are performing over the past day and month.

Unlike many of my personal projects, though, I noticed that this service is one that would be good to share with others—I believe it's the simplest and most inexpensive solution for individuals and small businesses who want to monitor their servers and websites.

It doesn't have all the fancy bells and whistles of other more 'enterprise-level' solutions, but I don't need that. I just need to know when one of my sites goes down, so I can react to the outage quickly. Downtime is lost money!

<h2>The Execution</h2>

I often think of <a href="http://drupal.org/">Drupal</a> as a bit of a <a href="http://en.wikipedia.org/wiki/Law_of_the_instrument">golden hammer</a>, but it really is a flexible tool that can do a wide array of things very well. Drupal helped me build the core components of Server Check.in—user management, login, content management, and user interface—quickly and easily. The site is running on Drupal 7 (though I'm beginning testing with Drupal 8), along with a few stable contrib modules to fill out the UI.

<p style="text-align: center;">{{< figure src="./responsive-server-check-in-iphone.png" alt="Responsive design on Server Check.in website." width="213" height="400" class="blog-image" >}}</p>

I used the excellent <a href="http://drupal.org/project/zen">Zen</a> theme framework to build a fully-responsive HTML5 theme, and jQuery (baked into Drupal) to add a little UI goodness here and there. I spent a lot of time trying to make sure that users on any device or viewport would receive an optimal overview of all the information they needed to see.

For the back end—the server checks, notifications, etc.—I have a mixture of a few custom Drupal modules, some drush scripts, and some other custom glue. I find a real value in using Drupal's APIs (Batch API, Queue API, Form API, Database API, etc.) along with drush to scale out certain kinds of services, instead of starting from scratch (though, at some point, I will probably need to break a few services away completely).

I've built everything in a modular fashion so it should be relatively easy to scale horizontally as I get constrained by the number of users. (Right now everything's running on one server, and I've projected that I can keep it this way for the first batch of users—hopefully I'll be able to expand soon, but I'll consider Server Check.in a success if it pays enough to cover the costs of email, hosting, and SMS (remember, I really just built it for myself ;).

I'm also experimenting with Python and Node.js to see if I can get HTTP checks and pings to happen more efficiently. In the end, though, I will stick with whatever's simplest, even if it doesn't incorporate the most amazing new technologies programming languages. (Notably, the majority of Server Check.in runs on MySQL, PHP, Apache and CentOS. I know this stack well, and I am loathe to change unless I have a good reason, or until the performance, scalability or structure is a crutch. So far this has not been the case on any project I've worked on in my career.)

Currently, I'm using <a href="http://curl.haxx.se/">cURL</a> for HTTP checks, and a custom-built class for PHP, <a href="https://github.com/geerlingguy/Ping">Ping</a> for simple IP/domain pings.

Payments are processed through <a href="https://stripe.com/">Stripe</a>, and this is the first time I've ever actually built something on top of Stripe's excellent API—in the past I've used PayPal and some other payment processors who used SOAP, XML, or other protocols, and had very poor DX (developer experience). Many services don't have a test environment, or have a very poor test environment (<em>cough</em> PayPal), and barely comprehensible API documentation. And you can forget about helper libraries for common languages (Ruby, Python, PHP, Java...). Not so with Stripe. I'm extremely satisfied with Stripe so far, and I think their platform is a major boon to online payment acceptance.

<h2>Sign up now!</h2>

If you're interested in knowing when your servers or websites are down, or tracking their performance over time, please consider <a href="https://servercheck.in/user/register">signing up for Server Check.in</a>—it only takes one minute!

Any questions about the service, or suggestions to make it better? Please let me know below or in <a href="http://news.ycombinator.com/item?id=4901350">this Hacker News thread</a>.
