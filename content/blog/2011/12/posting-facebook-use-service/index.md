---
nid: 2353
title: "Posting to Facebook: Use a service or DIY via the Open Graph API?"
slug: "posting-facebook-use-service"
date: 2011-12-15T17:33:03+00:00
drupal:
  nid: 2353
  path: /blogs/jeff-geerling/posting-facebook-use-service
  body_format: full_html
  redirects: []
tags:
  - facebook
  - open graph
  - sharing
  - social
aliases:
  - /blogs/jeff-geerling/posting-facebook-use-service
---

For a very long time, for my simple <a href="https://www.facebook.com/catholicnewslive">Catholic News Live fan page</a> on Facebook, I was using <a href="https://www.facebook.com/RSS.Graffiti">RSS Graffiti</a> to post new stories to Facebook (usually in batches of 3-5). RSS Graffiti is super-easy to set up, and it simply ties into your existing site's RSS feed to post new stories from your site to Facebook.

However, after I redesigned the <a href="http://catholicnewslive.com/">Catholic News Live website</a> in Drupal 7, I decided I'd take a few extra minutes to rework the site's social integration for Twitter and Facebook (I was using <a href="http://hootsuite.com/">HootSuite</a> for Twitter postings—a batch of 5 stories per hour maximum—and RSS Graffiti for Facebook.

People who followed both accounts weren't engaging, liking, or even sharing/retweeting stories too much. The twitter account was doing okay, because Twitter doesn't seem to hide tweets from other users as much as Facebook likes hiding certain posts (especially those from automated apps like RSS Graffiti).

<p style="text-align: center;">{{< figure src="./viral-facebook-reach.png" alt="Viral Facebook Reach Graph" width="368" height="238" >}}
Other graphs, like the shares, likes, etc. are similarly aligned.</p>
Once I wrote a little module to post stories straight to my Facebook page and Twitter account throughout the day, social engagement and visibility went through the roof (see above graph)! Partly due to the fact that stories would organically show up in the timelines (rather than a batch of 3-5 stories), and partly (I surmise) due to the fact that Facebook was less prone to hide multiple stories from Catholic News Live since they were being posted straight from my site.

<h2>The Personal Touch</h2>

If I wanted to increase engagement even more (say, if I actually had time on my hands to do anything more), I would personally cull through stories and select only those which have more of a 'shareability' to them (top ten lists, well-titled stories, stories with good 5W's in their opening paragraphs, etc.). Then I would have my site only post <em>those</em>&nbsp;stories to Facebook/Twitter. People (and probably Facebook, too) would see that CNL is a good/high quality information source, and would be more prone to pay attention to all the stories...

Some articles about the effectiveness of the personal touch:

<ul>
	<li><a href="http://www.insidefacebook.com/2011/09/06/hootsuite-tweetdeckdecreases-feedback/">Auto-Posting to Facebook Decreases Likes and Comments by 70%</a></li>
	<li><a href="http://www.socialbakers.com/blog/145-automated-facebook-posting-can-make-your-page-fail-engadget-now-knows/">Automatic Facebook posting can make your page fail</a></li>
	<li><a href="http://fbforbusinessmarketing.com/2011/05/30/automated-status-updates-facebook/">Automated Status Updates on a Facbook page: Pros and Cons</a></li>
</ul>

But I don't have time for that, and CNL is a side project for me. Therefore I'm pretty happy with a 1000% increase in social engagement due to switching from automated posting tools to my own API integration.
