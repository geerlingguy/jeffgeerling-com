---
nid: 2311
title: "Scaling the Drupal Community - Notes and Reflections"
slug: "scaling-drupal-community-notes"
date: 2011-03-10T18:58:04+00:00
drupal:
  nid: 2311
  path: /blogs/jeff-geerling/scaling-drupal-community-notes
  body_format: full_html
  redirects: []
tags:
  - community
  - development
  - drupal
  - drupal planet
  - open source
---

The sparsely-attended '<a href="http://chicago2011.drupal.org/sessions/scaling-drupal-community">Scaling the Drupal Community</a>' session, led by webchick and heyrocker, was one of the few sessions I've attended at DrupalCon Chicago that held my interest throughout. And, since a few people on IRC asked me to post my session notes, I thought I'd do so and put them up on the Planet.

If you, like me, thought there were too many awesome sessions during this timeslot that you decided to go to another one, then this post is for you—I believe that anyone invested in Drupal's future stands to gain something from reflecting on what webchick said at the session.

Now, on to the notes. I will give a summary of a statement by webchick, then my reflection (kind of a Q&amp;A format):

<h3>On 'Drupal Answers' vs. a drupal.org solution for Drupal Support</h3>

<em><a href="http://drupal.stackexchange.com/">Drupal Answers</a> is a new Stack Exchange site for answering Drupal questions, and it's in public beta right now. The site is hosted off the 'drupal.org' family of sites, and has a few hundred users so far...</em>

<strong>Webchick:</strong> Webchick basically stated that she's leaning towards what we already have (with slight adjustments). She mentioned that there's no good answer for the question of motivating people to help support drupal newbies without incentives (a karma or reputation system).

Also, she said that moving the support away from drupal.org is potentially very dangerous; this could lead the 'newbie' community away from the 'expert' community (which tends to discuss things in drupal.org issue queues. Right now, 'newbies' typically hang around in drupal.org forums, and 'experts' typically stick to their trackers and issue queues.

She said that right now, to form an idea of a particular drupal.org user's reputation, you can visit their drupal.org profile page and see: number of commits, commit log, user id number (lower is better!)... basically, you judge the user based on the user's actions/work.

If we use an incentive system whereby you can compare two users based on karma, points, or badges, then (especially for developers—who lean towards being gamers) things turn into a culture of competition (rather than collaboration)—everybody "plays to win".

It boils to this: We have to ask ourselves, "What is the cultural impact of using the Stack Exchange based site instead of drupal.org forums or another internal solution?" — don't just think "Well, it's a better tool."

<strong>My Thoughts</strong>: As was mentioned in IRC during the talk, some good background material on our current situation comes from the SE founder himself, Jeff Atwood; check out his "<a href="http://www.codinghorror.com/blog/2009/07/code-its-trivial.html">Code: It's Trivial</a>" post.

I think it's very important we move on this issue asap, before we see major fragmentation in the Drupal support arena. I think that new users may have a tendency to move to Stack Exchange to seek help, especially after they post to the drupal.org forum and receive no replies after a few days.

The question I would pose is: How do we incentivize user support? How do we make people want to help newbies in the Drupal community? The job doesn't reward much, except for personal satisfaction... do we use a karma/points system? Badges? I don't know...

<h3>On 'Big Money' coming to Drupal</h3>

<strong>Webchick</strong>:&nbsp;As funded startups and larger corporations try to get more features into core, we'll have more struggles with collaborative atmosphere. (Heyrocker adds:) This DrupalCon feels much more like a trade show than previous ones... and that's mostly due to the fact that Drupal has grown out of being a tight-knit developer community.

Drupal has become less centered around individual initiatives (at least, in core), and companies and startups getting funding are able to devote resources to shepherding initiatives. Examples: Acquia hiring Boulton design group to help with Admin UX, Examiner.com core patches to help with scalability, Commerce Guys core work to help support Drupal Commerce platform...

Sometimes, it feels like the collaborative atmosphere fades away (especially, for example, with regard to the admin overlay). This is a real problem, and a new one for the Drupal community. As time progresses, we need to work on refining our methods of attacking these problems, and maintaing a collaborative atmosphere. Alternatively, though, 'design by committee is not design at all' - sometimes, decisions do need to be made, and feelings will get hurt.

Webchick mentioned that the key to helping / improving Drupal, for a small developer or hobbyist, is to have a strong will, and get the ball rolling. For starters, just creating an issue will kick things off, and hopefully start a dialog with a maintainer to fix a problem or improve something. Don't be shy!

Realistically, though, small developers and hobbyists don't have the time or resources to shepherd large projects or initiatives. Thus, the ratio of smaller/individual developers contributing to Drupal core (vs. enterprise developers) is probably something like 99:1.

<strong>My Thoughts</strong>: In my own experience, as a developer of many personal websites, as well as many very large sites, I have found it to be the case that I simply couldn't do a lot of things I do with Drupal if I didn't rely on Drupal to help me with my full-time job. That's just a realistic observation of how Drupal is built (at least, on the core level).

<h3>On The Great Git Migration - Phase 1 vs. Phase 2</h3>

<strong>Webchick</strong>: One problem that we may see crop up is the expectation that people will be paid to help with major drupal.org infrastructure changes from here on out, because the Drupal Association had to pay developers to help with Phase 1 of the git migration.

What happens with phase 2? Will it ever get finished? This is a real worry in the Drupal community, and something to monitor in the coming year.

Another note: someone mentioned that we need to get out of the mindset that the Drupal Association will automatically kick in and pay for major initiatives. Rather, we all need to share responsibility for these things...

Webchick also mentioned the Git migration in relation to the current Stack Exchange situation... "Why did we not just use GitHub for our repositories? It's already built..." We wanted to maintain the collaborative community on drupal.org, for one, but more importantly, since all Drupal code must be GPL, we couldn't use GitHub—they have no requirement that code be GPLed.

<strong>My Thoughts</strong>: Unfortunately, during the major parts of this migration, I was doing work outside of Drupal, so I don't have much to say here, other than I love Git, and it's awesome :-)

<h3>On Having More Voices in the Drupal Community</h3>

<strong>Webchick</strong>: Does more voices mean more 300+ issue queues? More groupthink? Hopefully not. We need to continue to maintain a collaborative atmosphere, and help individuals and corporations both realize that they have a voice. The key, for the smaller voices, is to be willful, patient, and willing to be persistent.

Also, many times, someone will become unruly. If you find someone like this, try to find some common ground, work with the person, and guide them towards ways they can be more constructive. The person is probably trying to help, or do something, but is just frustrated.

We need to spread the word to everyone in the Drupal community: Helping with issues, and policing the community (argument resolution, solution finding) is not one person's responsibility—it's a shared responsibility.

<strong>My Thoughts</strong>: If we could <a href="http://drupal.org/node/1080494">get subscriptions working</a> on drupal.org, that would at least delay the problem of 300+ comment issues ;-)

<h3>Recommendation: Make drupal.org Better</h3>

Webchick's final word: "Help us make drupal.org better!" (She said that's where she'll be focusing her efforts for the near future). Basically, work on making the tool we use to collaborate better, and everyone profits!

<em>You can see my raw notes from this session in the attached text file below...</em>
