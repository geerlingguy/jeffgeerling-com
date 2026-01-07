---
nid: 66
title: "Don't Wait, Delegate! Proper use of threading and queueing"
slug: "dont-wait-delegate-proper-use"
date: 2012-06-19T02:06:15+00:00
drupal:
  nid: 66
  path: /articles/computing/2012/dont-wait-delegate-proper-use
  body_format: full_html
  redirects:
    - /2012/dont-wait-delegate-proper-use
aliases:
  - /2012/dont-wait-delegate-proper-use
  - /articles/computing/2012/dont-wait-delegate-proper-use
tags:
  - computing
  - latency
  - performance
  - programming
  - queues
---

There are hundreds of ways you can improve your app or website's performance, but few have the potential to improve your app or website's responsiveness as much as queueing or using background processes. There are so many complex operations that can be improved by looking at them in a new way. For example:

<h3>Not-so-Instant Oil Change</h3>

I like changing the oil in my car, but it often takes a bit of time (definitely not an 'instant!'), and involves the following:

<ul>
	<li>Drive to auto parts store, pick up oil and oil wrench, and drive back (30 minutes).</li>
	<li>Jack up front of car on stands (5 minutes).</li>
	<li>Drain oil into oil pan, remove old filter, prep new filter (5 minutes).</li>
	<li>Install new filter, refill oil reservoir (2 minutes).</li>
	<li>Remove jack stands, clean up mess (5 minutes).</li>
	<li>Drive to oil disposal center with old oil in pan, and drive back (20 minutes).</li>
</ul>

Total elapsed time: Over 1 hour!&nbsp;Maybe it's worth spending a few extra bucks on an 'instant' oil change to get back 45 minutes of my life.

But, could I make my own oil changes happen more quickly if I wanted? Of course! The key to speeding up the process is to stop using a serial (sequential—one after another) order of operations, and be creative.

<p style="text-align: center;">{{< figure src="./serial-vs-batch-background-processing.png" alt="Serial vs. Batch background processing" width="500" height="177" >}}</p>

There are really only four steps that <em>have</em> to be done in order, during the actual oil change operation, and they only take about 10 minutes. Here are the steps I can cut out to save time:

<ul>
	<li><strong>Drive to auto parts store for oil and parts</strong>: Instead of holding up the entire oil change to do this, I could either store extra oil in my garage ('batch' purchase oil), or have someone else go and do this step (a 'background task'). I could start getting my car prepped straightaway, and drain the oil. Then, when the parts and oil arrive, I can finish the steps that use the new oil. (<strong>Time saved: 30 minutes</strong>).</li>
	<li><strong>Drive to oil disposal center</strong>: Another operation that I could either do in batch (instead of going every time I get my oil changed, I could store all the oil in a larger pan, then take it when I have a full pan), or have someone else do during cleanup time. (<strong>Time saved: 20 minutes</strong>).</li>
</ul>

Notice how the two longest-running tasks in my oil change are the two easiest tasks to remove from the process? In computing, web development, and programming, the same is almost always true for a complex or high-latency task.

If you've memorized the <a href="http://serverfault.com/a/238534">Numbers Everyone Should Know</a>, you'll know there are some tasks that take much more time than others to complete when dealing with computers. For example, retrieving a small bit of information from another server over the internet is thousands of times slower than retrieving the same information from local memory, or even a slow hard drive.

There are many ways we can slim down the time it takes to complete a complex task—in real life&nbsp;<em>and</em> in computing.

<h3>Programming with Threads</h3>

I was recently working on a simple activity in an Android app, and I noticed that when the activity started, the entire app would become unresponsive until the activity's data was loaded. This non-responsive interface made for a horrible user experience, and made it look like the app might be crashing (especially on slow 3G connections).

The problem is that Android runs every single line of code in an app directly on the UI thread, meaning any slow-running bits of code in an activity will completely freeze the app's interface.

Luckily, Android allows us to use multiple application threads, and has a special class (<a href="http://developer.android.com/reference/android/os/AsyncTask.html">AsyncTask</a>) to help long-running processes (like retreiving information from the web) not interfere with the UI thread at all, but to pass back information at the end of the process. Great! I just moved the part of the code that retrieved data into Asynctask, and set a 'Downloading data...' progress dialog box to show while the data was downloading. When the task completed, I had AsyncTask update the interface with the proper data, and turned off the progress dialog.

Using threads allows your app (or website, or whatever you're programming) to do more than one thing at a time (in this simple example, show a progress dialog while downloading data), and has a side-effect of making your app feel <em>much</em> more responsive.

<h3>Using Queues</h3>

There was a form on a client's Drupal site that took about 5-10 seconds to submit after the user clicked the 'Save' button. Looking into the submit handling code on the site, I noticed that many operations were run before the page request could be completed. While all these operations happened, the user simply waited without anything happening. A lot of website visitors would close their browser window or try refreshing the page in frustration (I see this problem on a LOT of sites).

As it turns out, the longest part of the operation was a set of three emails that were sent after the form was submitted; and the emails were sent using a third party service, meaning network latency came into play, and made the performance very unstable.

Putting the emails into a separate queue (in this case, using Drupal's <a href="http://api.drupal.org/api/drupal/modules%21system%21system.queue.inc/group/queue/7">Queue operations</a>) allowed us to immediately finish the form submission process and get the user moving along to the next page, and then we just had a queue consumer send out the emails in its own time.

There were two positive consequences of this change: First, the user gets the next page in less than a second (not 3-5 seconds), and second, even if the email sending service is down, the emails will eventually get sent, since the queue will simply keep trying to send the email at a later time if it fails the first time.

Using queues allows your web application or service respond quickly, fail gracefully, and shift more demanding or slow operations to the background or to entirely separate servers.

<h3>Simple Strategy, Major Gains in Performance</h3>

The simple use of delegation can help with almost any site or app, no matter how big or small. If you just have a tiny app that downloads a list of news stories from an RSS feed and displays it to the user, the app becomes much better when you use a background thread to retrieve the data. If you have a huge web application that sends thousands of emails per hour, processes hundreds of records every minute, etc., then queueing and batch processing helps you scale from thousands to millions of requests, while also providing a more responsive site.

Do you have any of your own stories where a simple change has made your app or website perform exponentially faster?
