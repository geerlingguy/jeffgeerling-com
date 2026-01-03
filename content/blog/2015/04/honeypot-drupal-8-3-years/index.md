---
nid: 2490
title: "Honeypot for Drupal 8, 3 years in the making"
slug: "honeypot-drupal-8-3-years"
date: 2015-04-27T19:03:57+00:00
drupal:
  nid: 2490
  path: /blogs/jeff-geerling/honeypot-drupal-8-3-years
  body_format: full_html
  redirects: []
tags:
  - community
  - contributions
  - drupal
  - drupal 8
  - drupal planet
  - honeypot
  - modules
  - testing
aliases:
  - /blogs/jeff-geerling/honeypot-drupal-8-3-years
---

<p>Almost three years ago, on Feb 19, 2013, I <a href="http://cgit.drupalcode.org/honeypot/commit/?id=9f22c830dc5d75f01a63fe38b9fb56de49b4bb28">opened the 8.x-dev branch</a> of the <a href="https://www.drupal.org/project/honeypot">Honeypot</a> module (which helps prevent form spam on thousands of Drupal sites). These were heady times in the lifetime of the then-Drupal 8.x branch; <code>8.0-alpha1</code> wasn't released until three months later, on May 19. I <a href="https://www.drupal.org/node/1917700">made the #D8CX pledge</a>—when Drupal 8 was released, I'd make sure there was a full, stable Honeypot release ready to go.</p>

<p>Little did I know it would be more than 2.5 years—and counting—before I could see that promise through to fruition!</p>

<p>As months turned into years, I've kept to the pledge, and eventually decided to also port a couple other modules that I use on many of my own Drupal sites, like <a href="https://www.drupal.org/project/wysiwyg_linebreaks">Wysiwyg Linebreaks</a> and <a href="https://www.drupal.org/project/simple_mail">Simple Mail</a>.</p>

<p><a href="https://www.drupal.org/node/1917700#comment-7269776">Two years ago</a>, I mentioned in the original Honeypot D8 conversion issue that I'd likely write a blog post "about the process of porting a moderately-complex module like this from D7 to D8". Well, I finally had some time to write that post—and I'm still wondering how far off will be the release of Drupal 8.0.0!</p>

<h2>
<a id="user-content-ch-ch-changes" class="anchor" href="#ch-ch-changes" aria-hidden="true"><span class="octicon octicon-link"></span></a>Ch-Ch-Changes</h2>

<p>When working on the initial port, and when opening a new issue almost on a monthly basis to rework parts of the module to keep up with Drupal 8 core changes, I would frequently read through all the new nodes posted to the list of <a href="https://www.drupal.org/list-changes">Change records for Drupal core</a>.</p>

<p>These change records are like the Bible of translating 'how do I do Y in Drupal 8 when I did X in Drupal 7'? Most of the change records have fitting examples, contain a good amount of detail, and link back to the one, two, or ten issues that caused the particular change record to be written.</p>

<p>However, there were a few that were in a sorry state; these change records didn't have references back to all the relevant Drupal core issues, or only provided contrived examples that didn't help me much. In these cases, I took the following approach:</p>

<ol>
<li>Try to find the git commits that caused Honeypot tests or code to fail, do a git blame.</li>
<li>Find the issue(s) referenced by the breaking commits.</li>
<li>Read through the issue summary and see if it helps figure out how to fix my code.</li>
<li>If that doesn't help, read through the commit itself, then the code that was changed, and see if <em>that</em> helps.</li>
<li>If that doesn't help, read the entire issue comment history to see if <em>that</em> helps.</li>
<li>If that doesn't help, pop over to the ever-helpful #drupal-contribute IRC channel.</li>
<li>(<strong>The most important part</strong>) Go back to the deficient change record and edit it, adding appropriate issue references, code examples and documentation.</li>
</ol>

<p>In the course of the 71 distinct Honeypot 8.x commits that have been added so far, I had to go all the way to numbers 5 and 6 quite often. If it weren't for the incredible helpfulness of people like <code>webchick</code>, <code>tim.plunkett</code>, and others who seem to be living change record references, I would've probably given up the endeavor to keep Honeypot's Drupal 8 branch up to date the past three years!</p>

<h2>
<a id="user-content-automated-tests-are-a-pain-to-maintain-but-help-immensely" class="anchor" href="#automated-tests-are-a-pain-to-maintain-but-help-immensely" aria-hidden="true"><span class="octicon octicon-link"></span></a>Automated tests are a pain to maintain... but help immensely</h2>

<p>The Drupal 7 version of Honeypot had almost complete SimpleTest coverage for primary module functionality. One of the first steps in porting the module to Drupal 8—and the best way to make sure all the primary functionality was working correctly—was to port the tests to Drupal 8.</p>

<p>There have been dozens of automated testing changes in Drupal 8 that have caused tests to fail or give unexpected results. This caused some frustration in figuring out whether a particular failure was due to failing code or changes to the testing API.</p>

<p>Even with the small frustrations of broken tests every month or two, the test coverage is a huge help in ensuring long-term stability for a moderately-complex module like Honeypot. Especially when refactoring a large part of the module, or porting a feature between major Drupal versions, automated test coverage has more than made up for the extra time spent creating the tests.</p>

<h2>
<a id="user-content-the-drupal-community-is-ever-helpful" class="anchor" href="#the-drupal-community-is-ever-helpful" aria-hidden="true"><span class="octicon octicon-link"></span></a>The Drupal community is ever-helpful</h2>

<p>The other thing that's been an immense help throughout the development cycle is community involvement. Since Honeypot was one of the earliest modules with a stable Drupal 8 version (it's already seen 15 stable releases with 100% passing tests!), it's already used on many public Drupal 8 sites (over <em>80</em> at this point!). And this means there are users of the module invested in its success.</p>

<p>These early Drupal 8 adopters and other generous Drupal developers contributed code to fix a total of <em>12 of the hairest issues</em> during the D8 development cycle so far.</p>

<p><em>Come for the code, stay for the community</em>; my experience porting Honeypot to Drupal 8 (the easy part), and chasing Drupal 8 HEAD for three years (the hard part) has again provent to me the truth of this catch phrase. I hope I can say thanks in person to at least some of the following Honeypot D8 contributors over the past three years:</p>

<ul>
<li><a href="https://www.drupal.org/u/anavarre">anavarre</a></li>
<li><a href="https://www.drupal.org/u/marcingy">marcingy</a></li>
<li><a href="https://www.drupal.org/u/B%C3%A9s">Bés</a></li>
<li><a href="https://www.drupal.org/u/dawehner">dawehner</a></li>
<li><a href="https://www.drupal.org/u/rbayliss">rbayliss</a></li>
<li><a href="https://www.drupal.org/u/chris_hall_hu_cheng">chris_hall_hu_cheng</a></li>
<li><a href="https://www.drupal.org/u/tim.plunkett">tim.plunkett</a></li>
<li><a href="https://www.drupal.org/u/jpstrikesback">jpstrikesback</a></li>
</ul>

<h2>
<a id="user-content-25-years-and-counting" class="anchor" href="#25-years-and-counting" aria-hidden="true"><span class="octicon octicon-link"></span></a>2.5 years, and counting</h2>

<p>Much has been written about core contributor burnout, but I wanted to give some credit and kudos to the army of dedicated contributed module maintainers who have already made the #D8CX pledge. A major reason for Drupal's success in so many industries is the array of contributed modules available.</p>

<p>The very long development cycle between major releases—coupled with the fact that many contrib maintainers are now supporting <em>three</em> major versions of their modules—means that contributed module maintainers are at risk for burning out too.</p>

<p>I'd really like to be able to focus more of my limited time for Honeypot development on new features again, especially since a few of these new features would greatly benefit the 55,000+ Drupal 6 and 7 websites already using the module today. But until we have a solid API freeze for Drupal 8.0.x, most of my time will be spent fixing tests and code just to keep Honeypot working with HEAD.</p>

<p>I'll be at DrupalCon LA, and I hope to do whatever small part I can to get Drupal 8.0.0 out the door—will you do the same?</p>
