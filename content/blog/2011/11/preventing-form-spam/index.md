---
nid: 63
title: "Preventing Form Spam"
slug: "preventing-form-spam"
date: 2011-11-03T04:35:56+00:00
drupal:
  nid: 63
  path: /articles/web-design/2011/preventing-form-spam
  body_format: full_html
  redirects: []
tags:
  - cms
  - drupal
  - drupal planet
  - forms
  - honeypot
  - spam
  - websites
  - wordpress
---

<p style="text-align: center;">{{< figure src="./spam-mail-folder.png" alt="Spam email folder - Gmail interface" width="333" height="128" class="blog-image" >}}</p>
There are many different techniques for preventing form spam on your website, and an important component of the battle against spam is your constant struggle between giving your 'real' users a good experience while preventing spammers and automated bots from spamming you and lowering the quality of the content on your website.

<h3>A Constant User-Experience Battle</h3>

Usually, the first thing someone will do after having trouble fighting spammers by manual comment/content moderation is place a complex CAPTCHA system on their forms. Something like this:
<p style="text-align: center;">{{< figure src="./spam-captcha-difficult.png" alt="Spam CAPTCHA text difficult to read" width="163" height="71" class="blog-image" >}}</p>
Besides the fact that this kind of text is difficult for a normal person to read, it's even harder so for those with poor eyesight. In addition, many (if not most) CAPTCHA implementations are inaccessible to blind people or those using assistive devices to read your website.

What happens, in essence, is you end up completely silencing a large portion of the people who may be wanting to comment on your post or send you feedback—not just the disabled, but those who would rather not waste an extra ten seconds of their lives leaving a comment!

<p style="text-align: center;"><strong>Form Usability vs. Spam Deterrence</strong>
{{< figure src="./form-spam-prevention-ux-chart.png" alt="Form Spam prevention vs. Usability Chart" width="325" height="240" class="blog-image" >}}</p>
In the chart above, I illustrate the conundrum that web developers and content administrators must face when dealing with all types of forms—article submissions, forums, comments, etc. You can usually steer your forms towards either more user-friendliness, or better spam prevention, but there's no way to get the best of both worlds. You'll always need to compromise in some way; the rest of this article will lead you through my typical process for determining where, exactly, the happy medium resides.

So, what can we do? Spend hours moderating content? Disable comment forms? Those options aren't necessarily wrong in every situation, but I'd propose a more level approach—take small steps towards spam prevention, and only use CAPTCHAs (or other techniques which require extra user attention/time) in the most dire circumstances.

<h3>Before the CMS; Basic Principles in Spam Prevention</h3>

There are a few common-sense approaches to spam prevention that require minimal effort but can already go a long way towards preventing spam.

<ul>
	<li><strong>Stop it before it starts.</strong>
On many of my sites, I use a 'comment disabler' system that automatically sets comments to 'read only' on my posts after a few weeks. By that time, all relevant discussion has already been had... and I can turn comments back on if the post is a more timeless post or deserves more time for discussion. Spammers can't spam when there's no comment form!</li>
	<li><strong>Don't Give Comments Center Stage.</strong>
Many spammers only spam to get links back to their websites. If you can hide your comments on a separate page, separate from your main post, or have them not display until the user clicks a 'show comments' link (used by many news sites), that will help make spammers' links less potent. (You should also always add a rel="nofollow" attribute to all links posted in comments).</li>
	<li><strong>Don't allow anonymous comments/posts (require a login).</strong>
This can be a good thing and a bad thing; if you have a smaller site, and want to encourage people to post, requiring a user account can be a difficult barrier. However, many sites and communities can effectively reduce spam by requiring users to create an account or log into the site using Facebook or Twitter (or a commenting system like Disqus).&nbsp;</li>
</ul>

Obviously, these are very low-tech methods, and they only work in certain cases... but they're very effective if you don't need to leave comments open, and if you want to radically reduce the amount of spam you're getting with minimal effort.

<h3>Basic Form Protections</h3>

The first thing I usually do on any website (no matter how small) is enable one or two minimal form spam prevention techniques (for Drupal sites, I always turn on the <a href="http://drupal.org/project/honeypot">Honeypot</a> module and at least enable it for the user registration form and comment forms), and make sure that all comments and publicly-visible postings on the site are emailed to myself or another moderator (along with quick links to remove the post or in some cases approve it.

The Honeypot module is a very basic defense that works very well against weaker spammers who prey on smaller sites that typically don't have any spam protection.

The module is aptly named: the module adds an invisible field to comment forms (and other forms), and if that invisible field has any data entered into it, the form is not accepted. Like a pot of honey in front of Pooh (a spammer), a field in a form is irresistable to a spam script, which goes through the form and throws a value into any field it can find. An illustration:
<p style="text-align: center;">{{< figure src="./add-comment-form-hidden.jpg" alt="Add a hidden field in a comment form" width="425" height="268" class="blog-image" >}}</p>
Honeypot also adds 'timestamp' protection, which basically requires a time limit be passed before the form can be submitted (by default, 5 seconds). Usually, humans can't read an article, type a comment, and click 'Submit' within 5 seconds. However, spam scripts that want to post spam comments on hundreds of forms every second will try submitting the form within less than a second, and Honeypot will stop that from happening.

So, at a basic level (preventing spam from automated scripts and bots), two protections are pretty effective:

<ul>
	<li>A 'honeypot' field (with a common title like 'homepage' or 'url', to make it even more tantalizing) that is hidden from normal users using CSS or JavaScript, and is not allowed to have any content entered into it.</li>
	<li>A time-based protection, which attaches a time value to a form, and requires a certain amount of time to pass before form submission is accepted.</li>
</ul>

<h3>Advanced Form Protections</h3>

Unfortunately, there are many situations where simple spam prevention techniques will fail. Typically, the more popular a site gets, and the more PageRank it gets, the more likely spammers will outsmart your protections.

Spammers may customize their spam scripts to wait five seconds before posting a comment, and they may be able to detect invisible fields and work around them.

In these cases, you need to start using more intelligent spam prevention. There are three systems I've tested (and use) on my sites, and all three are highly effective in preventing spam, but come with a price:

<ul>
	<li><strong><a href="http://mollom.com/">Mollom</a></strong> - a newer spam prevention service that analyzes content and also offers accessible CAPTCHAs either by default, or if a form was submitted and flagged as potential spam. Has a <a href="http://drupal.org/project/mollom">Drupal module</a> and <a href="http://wordpress.org/extend/plugins/wp-mollom/">Wordpress plugin</a>.</li>
	<li><strong><a href="http://akismet.com/">Akismet</a></strong> - a well-established service used for spam prevention, has a <a href="http://drupal.org/project/antispam">Drupal module</a> and <a href="http://wordpress.org/extend/plugins/akismet/">Wordpress plugin</a>, among others.</li>
	<li><strong>External comment services</strong>: My favorites (and the most spam-free, in my experience) are <a href="http://disqus.com/">Disqus</a> and <a href="http://www.livefyre.com/">LiveFyre</a>. Both have integrations with most CMSes, and both have many different pricing options.</li>
</ul>

Hosting comments externally has many benefits, but it means you may not have as much control over the comment integration, display, and data, as you would if you keep the comments on-site. For-pay spam prevention services can allow you to keep your comments on-site and high quality.

<h3>When the Going Gets Rough</h3>

I would highly recommend you consider following the same progression of spam prevention techniques that I outline above rather than blindly install a CAPTCHA or other usability nightmare. Doing so will encourage real people to comment without distractions that may cause them to discard their comments—especially if your CAPTCHA system is broken.

However, there are certain cases where I still employ CAPTCHAs, and believe them to be helpful (especially on smaller forms or registration forms that won't have enough data for a spam prevention service like Mollom to work effectively). When I do use CAPTCHAs, I make sure they are accessible and not too difficult to read; I'd rather have to do some work moderating new users and have some false positives than deny a real person access to my site!

If you do use a CAPTCHA or something else that requires extra end-user work, add an audible CAPTCHA alternative so people with eyesight problems can still submit your forms. And make sure it's not impossible to decipher the images! One final thing to make sure of: don't lose the form data if a user submits the form with an incorrect CAPTCHA answer (that's quite annoying—having to fill out a form all over again).

There are also alternatives to CAPTCHAs that are easier to complete; one example is <a href="http://www.vouchsafe.com/">VouchSafe</a>. Another is a simple addition or subtraction challenge. Yet another is a question like 'click the third word in this sentance'. Creative CAPTCHA alternatives are a very good way to keep forms extremely secure while making life easier for your site's users.
