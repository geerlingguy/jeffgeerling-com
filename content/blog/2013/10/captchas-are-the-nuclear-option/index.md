---
nid: 2436
title: "reCAPTCHAs are easier to read\u2014but they're still a bad idea"
slug: "captchas-are-the-nuclear-option"
date: 2013-10-26T02:35:13+00:00
drupal:
  nid: 2436
  path: /blogs/jeff-geerling/captchas-are-the-nuclear-option
  body_format: full_html
  redirects: []
tags:
  - captcha
  - forms
  - honeypot
  - rants
  - spam
  - ux
---

From the article <a href="http://arstechnica.com/information-technology/2013/10/recaptchas-are-finally-readable-by-normal-humans/">reCAPTCHAs are finally readable by normal humans</a>:

<blockquote>
Google today announced that reCAPTCHAs served up to humans are finally readable without the need to squint your eyes or bang your keyboard in frustration after typing the wrong sequence of letters five times in a row. Who can even read those things, amirite?
</blockquote>

I'm glad Google is making CAPTCHAs easier for humans to read. For the very, very rare times when they're necessary, that's a good thing.

However, I want to make an appeal to the thousands of developers who are thinking of implementing a CAPTCHA to deal with their site's form/registration spam: <strong>use CAPTCHAs only as a last resort</strong>.

<p style="text-align: center;">{{< figure src="./captcha-nuclear-option-bomb.jpg" alt="CAPTCHAs - the Nuclear Form Spam Prevention Technique" width="475" height="316" >}}
<em>CAPTCHAs: The nuclear option.</p>

I maintain of one of the top 5 spam prevention modules for Drupal (<a href="https://drupal.org/project/honeypot">Honeypot</a>) and of dozens of websites with varying levels of community involvement (registration, forms, comments, etc.), so I've dealt with lots of spam. I also have user accounts on hundreds of different websites, and know that CAPTCHAs are maddeningly difficult for me to use (even if they're simple things like "type the fifth word in this sentence"), sometimes to the point that I abandon the form/site.

CAPTCHAs <a href="http://www.youtube.com/watch?v=FPOezLL398U">punish the user</a>. They are a way of your site telling the user: "I don't trust you, so I'm going to make <em>you</em> do extra work to prove you're not a spammer, <em>then</em> you can accomplish what you were trying to do."

Shouldn't we first try punishing the spammers, then only as a last resort punish normal users?

I've written a few articles on form spam prevention techniques that are effective yet retain usability for 'real' users: <a href="http://www.jeffgeerling.com/articles/web-design/2011/preventing-form-spam">Preventing Form Spam</a>, and <a href="http://www.jeffgeerling.com/blogs/jeff-geerling/introducing-honeypot-form-spam">Introducing the Honeypot form spam prevention module for Drupal</a>. I'll summarize my earlier posts here:

Your first priority should be getting users to enjoy using every aspect of your website—from registration, to comments, to surveys, etc. But to keep your own sanity, and save your own time, you also have to find a balance between preventing spammers from flooding your inbox or moderation queues, and maintaining form usability.

For most websites I've been involved with (even some pretty large ones), CAPTCHAs are major overkill. Using the Honeypot and timestamp-checking techniques like the Honeypot module uses catches at least 95% of automated spam posts, usually more. Using CAPTCHAs can sometimes provide a slight advantage to spam prevention, but <a href="http://moz.com/blog/having-a-captcha-is-killing-your-conversion-rate">leads to fewer conversions</a>. I'd rather deal with a few percent more spam messages in my inbox than lose even one paying customer or valuable feedback for any of my services.

For human-based spam, which usually targets high-traffic sites, CAPTCHAs are still an insufficient defense, as there are services which can help solve thousands of CAPTCHAs for pennies on the dollar... Mixing honeypots, timestamps, and CAPTCHAs with varying custom recipes and rules for when each is employed is often the best solution for these larger sites. As an alternative, there are paid services like <a href="http://mollom.com/">Mollom</a> and <a href="http://akismet.com/">Akismet</a> that also prevent most spam using different techniques that only punish spammers.

<strong>tl;dr - CAPTCHAs are the nuclear option for preventing form spam. They should be the last—not the first, as is often the case—line of defense.</strong>

Do you have any other ideas for form spam prevention, or do you think I'm misguided in my dislike of CAPTCHAs? Let me know in the comments or in <a href="https://news.ycombinator.com/item?id=6616015">this Hacker News discussion</a>.
