---
nid: 2304
title: "Sending Recurring Emails to Thousands, using Simplenews as a Backend"
slug: "sending-thousands-automated-sc"
date: 2010-12-13T19:32:58+00:00
drupal:
  nid: 2304
  path: /blogs/jeff-geerling/sending-thousands-automated-sc
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal planet
  - email
  - performance
  - simplenews
---

<p>I recently had a rather unique project requirement on one of my sites: I needed to send out a weekly email to hundreds (soon to be thousands) of site users, with the same template each week, but with the latest data from the website.</p>
<p>Basically, what I wanted to do was create a <a href="http://drupal.org/project/views">View</a> on my site of the latest 10-12 items, and have that view be sent out to everyone (along with the views header/footer) in HTML (with a plain text alternative, of course), but I didn't want to have to create a new newsletter by hand each week to do this (this is something at which the <a href="http://drupal.org/project/simplenews">Simplenews</a> module excels... minus the automation).</p>
<p>After debating over whether I should write my own module to do the dirty work of sending out batches of emails, using modules like Views Send along with Rules and Views Bulk Operations, and some other crazy ideas, I finally found a potent combination for sending out automated weekly newsletters in a highly performant and optimal way, using the following modules:</p>
<ul>
<li><a href="http://drupal.org/project/simplenews">Simplenews</a> (for queuing/sending emails, managing subscriptions)</li>
<li><a href="http://drupal.org/project/rules">Rules</a> (for scheduling the newsletters)</li>
<li><a href="http://drupal.org/project/elysia_cron">Elysia Cron</a> (for easy cron scheduling and performance)</li>
<li><a href="http://drupal.org/project/views">Views</a> (to build the body of the newsletter)</li>
<li><a href="http://drupal.org/project/mimemail">Mime Mail</a> (to send HTML emails, and to be able to easily have a custom email-friendly stylesheet)</li>
</ul>
<h3>Making the Newsletter</h3>
<p>I knew I wanted to have a simple list of a certain content type, laid out as a table (historically, tables are easy to work with in HTML emails—divs are out, and HTML5 is way, way out), with one field as one column, another field as another column, etc.</p>
<p>The easiest way to do this? <a href="http://drupal.org/project/views">Views</a>, by a mile.</p>
<p>However, I needed an easy way to send the view I created to hundreds or thousands of people, so I investigated many different methods for sending views programmatically by email... <a href="http://drupal.org/project/views_send">Views Send</a> + <a href="http://drupal.org/project/rules">Rules</a> seemed promising, but didn't work. Views Send + Rules + <a href="http://drupal.org/project/views_bulk_operations">Views Bulk Operations</a> could've possibly worked, but I found I would still have to find a way to cope with sending hundreds/thousands of emails.</p>
<p>I ended up using <a href="http://drupal.org/project/simplenews">Simplenews</a>—I simply created a new newsletter, used <code>views_embed_view()</code> to embed the view in the body of the newsletter, <a href="http://archstldev.com/node/712#comment-1267">subscribed all users to the newsletter</a> (using the <code>simplenews_subscribe_user()</code> function), and <a href="http://archstldev.com/node/712#comment-1264">set up a function on hook_user()</a> $op 'insert' that would automatically subscribe new users, whether they are created programmatically or by a real person.</p>
<h3>Setting Up Cron</h3>
<p>I wanted to have cron-like control over the times when the newsletter would be sent, but I also didn't want to have to set up a separate script or functionality in my custom module to be called by system cron—I wanted to be able to control the frequency of the emails (basically, Fridays at 10:30 a.m. or thereabouts) and do so with Rules.</p>
<p>Rules has a great conditional trigger that allows you to have your rule run any time Rules' cron task is run... of course, with out-of-the-box Drupal, you don't have a lot of control over individual cron tasks—you can simply call cron.php at a preset time, and all cron tasks are run. For performance reasons, this is a very bad idea on larger/active sites.</p>
<p>Enter <a href="http://drupal.org/project/elysia_cron">Elysia Cron</a>.</p>
<p>Using Elysia Cron, I had very fine-grained control on how often each module's cron task is run. Basically, I set up my system cron to hit Drupal's cron.php every minute... but Elysia Cron lets me define how often individual cron tasks run. I set Rules to run every 10 minutes (so I can make my own Rule run at 10:30 a.m. (which is on a 10 minute mark), and Simplenews to run every 7 minutes. This guarantees that I can get the Rule to set up the Simplenews newsletter, and Simplenews to start sending it, within a few minutes of 10:30 a.m.</p>
<p>I also have set other cron tasks to occur more or less frequently, for performance reasons: search indexing every 5 minutes, watchdog cron once a day, and update.module cron every week. This makes for a much snappier cron run across the board, and lets me send out more simplenews newsletters, since on simplenews cron runs, nothing else will take up precious seconds of my PHP script time limit.</p>
<h3>Adding a Scheduled Rule</h3>
<p>Now that I had Rules' cron firing every ten minutes, I had to make the Rule I set up work correctly.</p>
<p>The first step was to add a Rule that ran on the Event "Cron maintenance tasks are performed."</p>
<p>The condition I added was of the type "Execute custom PHP code," and I used the following to check whether it's 10:30 a.m. on Friday (and, in that case, return 'TRUE' — otherwise, 'FALSE'):</p>

```
<?php
/* Get the current time/date/day */
$time = getdate();

/* Set up our comparison variables */
$current_day = $time['weekday']; // Sunday, Monday, Tuesday...
$24_hour_time = sprintf("%02d", $time['hours']) . sprintf("%02d", $time['minutes']);
$24_hour_time = (int) $24_hour_time; // Cast $24_hour_time to an integer

/* CHANGE THESE TO SUIT YOUR FANCIES: */
$range = range(1027, 1033, 1); // Time is inside this window, in one-minute increments
$day = "Friday"; // Set this to whichever day of the week you'd like

/* Check if the day is correct, and the time is in our predefined range */
if (($current_day == $day) && in_array($24_hour_time, $range)) {
  return TRUE;
}
else {
  return FALSE;
}
?>
```

<p>The action I added was again "Execute custom PHP code," and I used the following to tell Simplenews to re-send a particular newsletter (I could've created a new newsletter node, then had Simplenews send that, but it's easier for my purposes to simply tell Simplenews to re-send the original newsletter. Basically, changing the status of a row in simplenews_newsletters to '1' makes Simplenews send out the newsletter to everyone. (After the newsletter is sent, the status switches back to '2'):</p>

```
<?php
$nid = 1503; // nid of newsletter to re-send here.
$node = node_load($nid); // Load the newsletter node
db_query("UPDATE {simplenews_newsletters}
                SET s_status = '1'
                WHERE nid = %d", $nid);
module_load_include('inc', 'simplenews', 'includes/simplenews.mail'); // Function below is not in simplenews.module
simplenews_send_node($node); // Tell Simplenews to queue the node for sending
?>
```

<p>I had tested all this code first using <a href="http://drupal.org/project/devel">Devel</a>'s "Execute PHP Code" page (which is a godsend!).</p>
<h3>HTML Email Woes</h3>
<p><em>(or... Microsoft Outlook 2007 is worse than Internet Explorer 6 and much worse than Outlook 2003!)</em></p>
<p>I am using <a href="http://drupal.org/project/mimemail">Mime mail</a> to send out HTML-formatted emails (with plain-text equivalents), because I really want the emails to be readable to the people in this organization. Almost all the users have Outlook 2007, and a few are still running 2003.</p>
<p>So, I thought, "As long as the HTML email works in Mail (Mac OS X—which I use) and Outlook 2003, it should probably also work in Outlook 2007, which is newer than 2003. But Microsoft came back and bit me for the nth time. Outlook 2007 rendered HTML with the same engine as Microsoft Word, which doesn't allow half of the CSS2 selectors/features that were implemented even in Internet Explorer 6!</p>
<p>This meant that my custom styling I had added via Mime mail in my theme's mail.css file had to be rewritten. I had to use only the first selector in a series. For instance, in cck fields, classes for a particular item are usually defined as <code>class="class1 class2 field-name-class3"</code> - but Outlook 2007 only recognizes <code>.class1</code>, not <code>.class2</code> or <code>.field-name-class3</code>. Yikes!</p>
<p>After a bit of fiddling and re-theming the view embedded in my email, I was able to get Outlook 2007 to show the email just as beautifully as Mail for Mac, Gmail online, or Outlook 2003.</p>
<h3>The Finished Product</h3>
<p>We now have a website capable of sending thousands of automated emails on a scheduled basis; users can opt-in or opt-out of emails (we have user accounts automatically set to be subscribed to this particular newsletter when they create an account (<a href="http://www.jeffgeerling.com/blogs/jeff-geerling/drupal-simplenews-automaticall">see this post for more</a>); and our server's CPU/memory is barely nudged on cron runs when the emails are sent.</p>
