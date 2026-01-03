---
nid: 2584
title: "On Low-Cost Web Hosting/VPSes"
slug: "low-cost-web-hostingvpses"
date: 2013-06-28T03:42:23+00:00
drupal:
  nid: 2584
  path: /blog/low-cost-web-hostingvpses
  body_format: full_html
  redirects: []
tags:
  - hosting
  - inexpensive
  - shared hosting
  - vps
  - web development
  - websites
aliases:
  - /blog/low-cost-web-hostingvpses
---

As most web developers have over their careers, I've often spent time researching different low-priced web hosting companies in search of a better plan than the one(s) I'm currently using.

<p style="text-align: center;">{{< figure src="./money-piggy-bank-saving.jpg" alt="Dollar in a Piggy bank" width="300" height="400" >}}
(<a href="http://www.flickr.com/photos/59937401@N07/">image courtesy of Images_of_Money on Flickr</a>)</p>

I've run servers and used shared hosting for myself and for clients I support with hosts like <a href="http://www.hostgator.com/">HostGator</a>, <a href="https://www.linode.com/">Linode</a>, <a href="http://dreamhost.com/">DreamHost</a>, <a href="http://www.softlayer.com/">SoftLayer</a>, <a href="http://aws.amazon.com/">AWS</a>, <a href="https://www.digitalocean.com/">Digital Ocean</a>, <a href="http://ramnode.com/">RamNode</a>, and more. I've had a lot of experience running a variety of websites and web applications across a variety of hosts. And I've learned <em>many</em> lessons. I'd like to highlight the most important ones here, with the hope that you can learn them without having to experience their disastrous consequences firsthand:

<h2>You get what you pay for</h2>

If a deal seems too good to be true, it most definitely is. There's no such thing as free lunch when it comes to web hosting—there is always a tradeoff when you're paying less than <em>X</em> amount for your hosting plan. Consider that every publicly-accessible web server needs to have bandwidth, climate-controlled physical space (usually in a rack in a server room), power, backup power, and physical management—even an old, slow server that hosts sites for hundreds of clients. This is not free—and there are varying levels of quality for each of these server necessities.

Recently, a few popular low-cost hosting companies like <a href="https://clientarea.ramnode.com/announcements.php?id=182">RamNode</a> and <a href="http://www.lowendtalk.com/discussion/11304/chicagovps-update/p1">ChicagoVPS</a> were hacked because of security holes in the (low-cost) VPS management software they were using (<a href="http://www.lowendtalk.com/discussion/11187/solusvm-vulnerability">SolusVM</a>). Because of the somewhat limited staff, and likely lack of a robust, well-tested disaster recovery plan, these smaller hosting providers took days to recover many servers, and some servers' data was entirely lost.

<em>Do I hold this against them?</em> No. From what I've seen, the people behind these hosting companies pour their lives into their work (especially in situations like this hack), and they deserve major kudos for the work they do for their customers.

But they are low-cost hosting providers. Don't expect 100%, or even 99.9% uptime. If you're paying a company less than $20-30/month for something, and they don't have stringent SLAs and disaster recovery agreements, expect some downtime.

<h2>Always keep your own backups</h2>

I reel every time I hear of someone who stores important data in one location, or one one server, and relies on the hosting company's backups (or has <em>no backup at all</em>!). Always have an offsite backup.

I typically purchase an extra VPS or server with a large amount of storage, or use Amazon S3 to store daily (at least) database backups and filesystem backups—at least the important stuff like the codebase and other relevant files. If you use git, you can just make sure you have a clone of your repository on the backup server, and then rsync any other files and database dumps between your servers and your backup server. Set up a simple shell script that runs via cron every night, and you're set. For more complex applications/sites, you might need a more robust backup system, but at least have <em>something</em>.

If you have your own backup, it doesn't matter if your main hosting provider has a major catastrophe. Even big hosting facilities like Colo4, SoftLayer and Amazon have major outages resulting in hours of downtime. Are you ready to fail over (even if in read-only mode) to another host quickly? You don't need an automated failover plan if you're running a small business site or some small web app... you just need a recent database backup, the codebase, and the ability to spin up a new server/servers quickly on a different hosting provider.

As a corollary, make sure you test your backups, and ensure they are actually being run daily/weekly/etc. from time to time. I've been burned before when I updated my SSH keys, or changed crontab, and accidentally disabled automated backups. Learn from my mistakes. Every month, or every quarter, or at some interval, check your backup, and make sure it is recent and can be restored successfully.

<h2>Don't host mission-critical sites and software on cheap hosts</h2>

If your company/small business will lose money when your website is down, you probably shouldn't have your website hosted on a cheap VPS or dirt-cheap shared hosting.

This doesn't mean you shouldn't consider using cheap solutions for experimental features/projects, test and development servers, auxiliary servers, and side projects (still, remember to keep backups!). For your main website/app, you should pay a little more for a hosting plan from a company with more employees (and an HR department), years of experience, and a solid track record.

<h2>Don't rely on one server, or one hosting provider</h2>

I always like to have a 'close-to-live' backup of my more important websites/apps ready to launch on servers from different hosting providers. The website you're viewing right now is being hosted on Digital Ocean; however, I could have the site running on another provider within minutes, just missing some recent (and mostly insignificant) data.

Especially if you are using lower-cost hosting providers, make sure you have at least one server from a different provider ready to go. For example, I have a few RamNodes and Digital Ocean droplets that I use for testing and development, but I can easily (and quickly) switch them over to live servers if the need arises.

They might not be able to serve as much traffic or handle as much load as my main servers, but they will ensure that my website is up instead of inaccessible. If you use automated configuration/provisioning tools like <a href="http://www.opscode.com/chef/">Chef</a> or <a href="https://puppetlabs.com/">Puppet</a>, spinning up new servers on different hosts when the need arises is even easier.

<h2>tl;dr Save money, but don't sacrifice your site</h2>

The bottom line: You should consider whether your site/app is small enough that you'd sacrifice hours, sometimes days, of uptime, to save a few bucks a month. If your revenue is less than a few hundred dollars a year, it's logical to shave a few dollars off your hosting plan. However, if your site is more valuable, don't skimp on the hosting. Pay for reliability and support.

Oh, and make sure you <a href="http://www.jeffgeerling.com/user/register">monitor your site with Server Check.in</a> so you can know when it's down :-)
