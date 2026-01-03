---
nid: 2680
title: "What to do if Twitter won't allow Verification because of unconfirmed email"
slug: "what-do-if-twitter-wont-allow-verification-because-unconfirmed-email"
date: 2016-08-06T04:24:19+00:00
drupal:
  nid: 2680
  path: /blog/2016/what-do-if-twitter-wont-allow-verification-because-unconfirmed-email
  body_format: markdown
  redirects:
    - /blog/2016/what-do-if-twitter-wont-allow-verification-because-invalid-or-unconfirmed-email
aliases:
  - /blog/2016/what-do-if-twitter-wont-allow-verification-because-invalid-or-unconfirmed-email
tags:
  - accounts
  - email
  - gmail
  - icloud
  - twitter
  - verification
---

I recently learned that account verification is now generally available on Twitter... but when I went to [verify my account](https://verification.twitter.com/welcome), I got a notice that I needed to confirm my email address. I went into my account settings, and my account (which has existed since 2008, and has had a confirmed email address entered since the beginning!) showed my email was in working order.

So, knowing that sometimes you just need to give software a little [percussive maintenance](https://www.google.com/#q=percussive+mainenance), I decided to try changing my email address (using another email alias for my normal iCloud account). Well, I got the confirmation email, clicked the link... and found a wonderful 500 error page:

<p style="text-align: center;">{{< figure src="./something-is-technically-wrong-twitter.jpg" alt="Something is technically wrong - Twitter 500 server error page" width="450" height="368" class="insert-image" >}}</p>

Undaunted, I tried some other email aliases. I tried copying and pasting the link in many different browsers. I tried using curl to run the link (thinking it may be some JS error or something). I then naïvely tried to contact Twitter support. Twice. Both times ended up getting some support person to trigger a password reset. Which did nothing (besides let me click on 1Password a few extra times).

So finally, after giving up for a few weeks, I ran into [this Twitter developer forum thread](https://twittercommunity.com/t/cant-create-new-app-email-not-confirmed-error/34066), in which [@madebyjenni](https://twitter.com/madebyjenni) mentioned that _using a different email from a different provider_ allowed her to finally re-confirm her email address and get a dev app set up successfully.

So, I used a Gmail address alias instead of one of my iCloud aliases... and wouldn't you know, I could confirm my email address on Twitter! I switched back to my original email address, and the email confirmation worked there too. So something must've been funky with my account that is now cleared up.

I've finally been able to request verification! Hopefully I'll get that beautiful blue checkmark on my Twitter profile soon :)
