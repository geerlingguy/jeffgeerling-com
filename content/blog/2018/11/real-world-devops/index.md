---
nid: 2889
title: "Real World DevOps"
slug: "real-world-devops"
date: 2018-11-17T21:07:00+00:00
drupal:
  nid: 2889
  path: /blog/2019/real-world-devops
  body_format: markdown
  redirects:
    - /blog/2018/real-world-devops
aliases:
  - /blog/2018/real-world-devops
tags:
  - appearances
  - devops
  - drupal
  - drupal planet
  - essay
  - nedcamp
  - presentations
---

> This blog post contains a written transcript of my NEDCamp 2018 keynote, _Real World DevOps_, edited to match the style of this blog. Accompanying resources: [presentation slides](https://www.slideshare.net/geerlingguy/real-world-devops-jeff-geerlings-nedcamp-2018-keynote), [video](https://www.youtube.com/watch?v=qQGEovsGbJA).

{{< figure src="./jeff-geerling-nedcamp-2018.jpg" alt="Jeff Geerling at NEDCamp 2018 - New England Drupal Camp" width="650" height="405" class="insert-image" >}}

I'm Jeff Geerling; you probably know that because my name appears in huge letters at the top of every page on this site, including the post you're reading right now. I currently work at [Acquia](https://www.acquia.com) as a Senior Technical Architect, building hosting infrastructure projects using some buzzword-worthy tech like Kubernetes, AWS, and Cloud.

I also maintain [Drupal VM](https://www.drupalvm.com), the most popular local development environment for the Drupal open source CMS. And I run two SaaS products with hundreds of happy customers, [Hosted Apache Solr](https://hostedapachesolr.com) and [Server Check.in](https://servercheck.in), both of which have had over 99.99% uptime since their inception for a combined 15 years. I also write (and continuously update) a best-selling book on Ansible, [Ansible for DevOps](https://www.ansiblefordevops.com), and a companion book about Kubernetes. Finally, I maintain a large ecosystem of Ansible roles and automation projects on GitHub which have amassed over [17,000 stars and 8,000 forks](https://stldevs.com/developers).

Oh, I also have three children under the age of six, have a strong passion for photography (see [my Flickr](https://www.flickr.com/photos/lifeisaprayer/)), maintain four Drupal websites for local non-profit organizations, and love spending time with my wife.

You might be thinking: _this guy probably never spends time with his family._

And, if you're speaking of this weekend, sadly, you'd be correct—because I'm here in Rhode Island with all of _you_!

But on a typical weeknight, I'm headed upstairs around 5-6 p.m., spend time with my family for dinner, after-meal activities, prayers, and bedtime. And on weekends, it's fairly rare I'll need to do any work. We go to the zoo, we go on family trips, we go to museums, and we generally spend the entire weekend growing together as a family.

Some nights, after the kids are settled in bed, I'll spend an hour or two jumping through issue queues, updating a section of my book—or, as is the case right now, writing this blog post.

How do I do it?

{{< figure src="./devops-keynote-cncf.jpg" alt="CNCF Cloud Native Landscape" width="650" height="366" class="insert-image" >}}

Well I apply complex self-healing, highly-scalable DevOps architectures to all my projects using all the tools shown in this diagram! I'm kidding, that would be _insane_. But have you seen this graphic before? It's the [Cloud Native Landscape](https://landscape.cncf.io), published by the Cloud Native Computing Foundation.

The reason I show this picture is because I expect everyone reading this to memorize all these tools so you know how to implement DevOps by next week.

Just kidding again! Some people think the mastery of some tools in this diagram means they're doing 'DevOps'. To be honest, you might be practicing DevOps better than someone who integrates fifty of these tools using nothing but Apache and Drupal—_neither of which are listed in this infographic!_

## What is DevOps?

The framework I use is what I call 'Real World DevOps'. But before I get into my definition, I think it's important we understand what the buzzword 'DevOps' means, according to our industry:

{{< figure src="./devops-keynote-azure-devops.jpg" alt="Azure DevOps" width="650" height="366" class="insert-image" >}}

Microsoft, apparently, packaged up DevOps and sells it as part of Azure's cloud services. So you can put a price on it, apparently, get a purchase order, and have it! Right?

{{< figure src="./devops-keynote-docker.jpg" alt="Docker" width="650" height="366" class="insert-image" >}}

And I see a lot of DevOps people talk about how Docker transformed their developers into amazing coding ninjas who can deploy their code a thousand times faster. So Docker is part of DevOps, right?

{{< figure src="./devops-keynote-no-cloud.jpg" alt="There is no cloud sticker" width="650" height="366" class="insert-image" >}}

And to do DevOps, you have to be in the cloud, because that's where all DevOps happens, right?

{{< figure src="./devops-keynote-agile-alliance.jpg" alt="Agile Alliance" width="650" height="366" class="insert-image" >}}

And DevOps requires you to strictly follow Agile methodologies, like sprints, kanban, scrums, pair programming, and pointing poker, right?

Well, let's go a little further, and see what some big-wigs in the industry have to say:

> "People working together to build, deliver, and run resilient software at the speed of their particular business."<br>
> —GitLab

So it sounds like there's a people component, and some sort of correlation between speed and DevOps.

Okay, how about Atlassian?

> DevOps "help[s] development and operations teams be more efficient, innovate faster, and deliver higher value"<br>
> —Atlassian

So it sounds like it's all about making teams better. Okay...

> "Rapid IT service delivery through the adoption of agile, lean practices in the context of a system-oriented approach"<br>
> —Gartner

(Oh... that's funny, this quote is also in one of O'Reilly's books on DevOps, in a post from Ensono, and in basically every cookie-cutter Medium post about DevOps.)

In Gartner's case, they seem to focus strongly on methodology and service delivery—but that's probably because their bread and butter is reviewing products which purportedly help people track methodology and service delivery! It's interesting (and telling) there's no mention about people or teams!

## But what do _I_ say about DevOps?

But what about me? I just claimed to practice DevOps in my work—heck, my book has the word _DevOps_ in the title! Surely I can't just be shilling for the buzzword profit multiplier by throwing the word 'DevOps' in my book title... _right_?

{{< figure src="./devops-keynote-ansible-devops-title.jpg" alt="Ansible for DevOps - is Jeff Geerling just riding the wave of the buzzword?" width="650" height="366" class="insert-image" >}}

Well, to be honest, I did use the word to increase visibility a bit. Why else do you think my second book has the word 'Kubernetes' in it!?

But my definition of DevOps is a bit simpler:

{{< figure src="./jeff-geerling-devops-definition.jpg" alt="Jeff Geerling&#39;s DevOps Definition - Making people happier while making apps better" width="650" height="401" class="insert-image" >}}

> "Making people happier while making apps better."<br>
> —Jeff Geerling (Photo above by [Kevin Thull](https://www.drupal.org/u/kthull))

I think this captures the essence of _real world_, non-cargo-cult DevOps, and that's because it contains the two most important elements:

### Making people happier

DevOps is primarily about people: every team, no matter the size, has to figure out a way to work together to make users happy, and not burn out in the process. And what are some of the things I see in teams that are implementing DevOps successfully?

  - Reduced friction between Operations/sysadmins, Developers, Project Management, InfoSec, and QA. People don't feel like it's 'us against them', or 'we will loop them in after we finish our part'. Instead, everyone talks, everyone has open communication lines in email or Slack, and requirements and testing are built up throughout the life of the project.
  - Reduced burnout, because soul-sucking problems and frustrating communications blockades are almost non-existent.
  - Frequent code deploys, and almost always in the middle of the workday—and this also feeds back into reduced burnout, because nobody's pulling all-nighters fixing a bad deploy and wrangling sleepy developers to implement hotfixes.
  - Stable teams that stay together and grow into a real _team_, not just a 'project team'; note that this can sometimes be impossible (e.g. in some agency models), but it does make it easier to iteratively improve if you're working with the same people for a long period of time.
  - There are _no heroes_! Nobody has to be a rockstar ninja, working through the weekend getting a release ready, because DevOps processes emphasize stability, enabling a better work-life balance for everyone on the team.

How many times have you seen an email praising the heroic efforts of the developer who fixed some last-minute major issues in a huge new feature that were discovered in final user acceptance testing? This should not be seen as a heroic deed—rather it should be seen as a tragic failure. Not a failure of the developer, but as a failure of the _system_ that enabled this to happen in the first place!

DevOps is about making people happier.

### Making apps better

Devops is also about apps: you can't afford to develop at a glacial pace in the modern world, and when you make changes, you should be confident they'll work. Some of the things I see in the apps that are built with a DevOps mentality include:

  - Continuous delivery: a project's master (or production) code branch is _always_ deployable, and passes all automated tests—and there _are_ automated tests, at least covering happy paths.
  - Thorough monitoring: teams know when deployments affect performance. They know whether their users are having a slow or poor experience. They get alerts when systems are impaired but not down.
  - Problems are fixed as they occur. Bugfixes and maintenance are part of the regular workflow, and project planning gives equal importance to these issues as it does features.
  - Features are delivered frequently, and usually in small increments. Branches or unmerged pull requests rarely last more than a few days, and never more than a sprint.

Small but frequent deployments are one of the most important ways to make your apps better, because it also makes it easier to fix things as problems occur. Instead of dropping an emergent bug into a backlog, and letting it fester for weeks or months before someone tries to figure out how to reproduce the bug, DevOps-empowered teams 'swarm' the bug, and prevent similar bugs from ever happening again by adding a new test, correcting their process, or improving their monitoring.

DevOps is about making apps better.

## DevOps Prerequisites

So we know that DevOps is about people and apps, and we know some of the traits of a team that's doing DevOps well, but are there some fundamental tools or processes essential to making DevOps work? Looking around online, I've found most DevOps articles mention these prerequisites:

  - Automation
  - CI/CD
  - Monitoring
  - Collaboration

I tend to agree that these four traits are essential to implementing DevOps _well_. But I think we can distill the list even further—and in some cases, some prerequisites might not be as important as the others.

I think the list should be a lot simpler. To do DevOps right, it should be:

  - Easy to make changes
  - Easy to fix and prevent problems (and prevent them from happening again)

### Easy to make changes

I'm just wondering: have you ever timed how long it takes for a developer completely new to your project to get up and running? From getting access to your project codebase and being able to make a change to it locally? If not, it might be a good idea to find out. Or just try deleting your local environment and codebase entirely, and starting from scratch. It should be very quick.

_If it's not easy and fast to start working on your project locally, it's hard to make changes._

Once you've made some changes, how do you know you won't break any existing functionality on your site? Do you have behavioral testing that you can easily run, and doesn't take very long to run, and doesn't require hours of setup work or a dedicated QA team? Do you have visual regression tests which verify that the code you just changed won't completely break the home page of your site?

_If you can't be sure your changes won't break things, it's scary to make changes._

Once you deploy changes to production, how hard is it to revert back if you find out the changes _did_ break something badly? Have you practiced your rollback procedure? Do you even _have_ a process for rollbacks? Have you tested your backups and have confidence you could restore your production system to a known good state if you totally mess it up?

_If you can't back out of broken changes, it's scary to make changes._

The easier and less stressful it is to make changes, the more willing you'll be to make them, and the more often you'll make them. Not only that, with more confidence in your disaster recovery and testing, you'll also be more confident and less stressed.

> "High performers deployed code 30x more frequently, and the time required to go from “code committed” to “successfully running in production” was 200x faster."<br>
> —The DevOps Handbook

While you might not be deploying code 300 times a day, you'll be happy to deploy code whenever you want, in the middle of the workday, if you can make changes easy.

### Easy to fix and prevent problems

Making changes _has_ to be easy, otherwise it's hard to fix and prevent problems. But that's not all that's required.

Are developers able to deploy their changes to production? Or is there a long, drawn out process to get a change deployed to production? If you can build the confidence that at least the home page still loads before the code is deployed, then you'll be more likely to make small but frequent changes—which are a lot easier to fix than huge batches of changes!

_Developers should be able to deploy to production after their code passes tests._

Once you deploy code, how do you know if it's helping or hurting your site's performance? Do you have detailed metrics for things like average end-user page load times (Application Performance Monitoring, or APM), CPU usage, memory usage, and logs? Without these metrics you can't make informed decisions about what's broken, or whether a particular problem is fixed.

_Detailed system metrics and logging is essential to fix and prevent problems._

When something goes wrong, does everyone duck and cover, finding ways to avoid being blamed for the incident? Or does everyone come together to figure out what went wrong, why it went wrong, and how to prevent it from happening in the future? It's important that people realize when something goes wrong, it's _rarely_ the fault of the person who wrote the code or pressed the 'go' button—it's the fault of the process. Better tests, better requirements, more thorough reviews would prevent most issues from ever happening.

_'Blameless postmortems' prevent the same failure from happening twice while keeping people happy._

## DevOps Tools

But what about _tools_?

> "It's a poor craftsman that blames his tools."<br>
> —An old saying

Earlier in this post I mentioned that you could be doing DevOps even if you don't use any of the tools in the Cloud Native Landscape. That may be true, but you should also avoid falling into the trap of having one of these:

{{< figure src="./devops-keynote-golden-hammer-driving-screw.jpg" alt="Golden hammer driving a screw into a board" width="650" height="409" class="insert-image" >}}

A golden hammer is a tool that someone loves _so_ much, they use it for purposes for which it isn't intended. Sometimes it can work... but the results and experience are not as good as you'd get if you used the _right_ tool for the job. I really like this quote I found on a Hacker News post:

> "Part of being an expert craftsman is having the experience and skills to select excellent tools, and the experience and skills to drive those excellent tools to produce excellent results."<br>
> —[jerf, HN commenter](https://news.ycombinator.com/item?id=2380679)

So a good DevOps practitioner knows when it's worth spending the time learning how to use a new tool, and when to stick with the tools they know.

So now that we know something about DevOps, here's a project for you: build some infrastructure for a low-profile Drupal blog-style site for a budget-conscious client with around 10,000 visitors a day. Most of the traffic comes from Google searches, and there is little authenticated traffic. What would you build?

{{< figure src="./devops-keynote-k8s-complex-architecture.jpg" alt="Complex Drupal hosting architecture in AWS VPC with Kubernetes" width="650" height="366" class="insert-image" >}}

Wow! That looks great! And it uses like 20 CNL projects, so it's definitely DevOps, right?

Great idea, terrible execution.

{{< figure src="./devops-keynote-simple-architecture.jpg" alt="Simple Drupal hosting architecture with a LAMP server and CloudFlare" width="650" height="366" class="insert-image" >}}

Just because you know how to produce excellent results with excellent tools doesn't mean you always have to use the 'best' and most powerful tools. You should also know when to use a simple hammer to nail in a few nails! This second architecture is better for this client, because it will cost less, be easier to maintain long-term, and won't require a full-time development team maintaining the infrastructure!

{{< figure src="./devops-keynote-jeff-holding-golden-hammer.jpg" alt="Jeff Geerling holding a golden hammer" width="650" height="386" class="insert-image" >}}

So know yourself. Learn and use new tools, but don't become an _architecturenaut_, always dreaming up and trying to build over-engineered solutions to simple problems!

That being said, not all the tools you'll need appear in the Cloud Native Landscape. Some of the tools I have in my toolbelt include:

### YAGNI

I don't know how many times I've had to invoke YAGNI. That is, "You Ain't Gonna Need It!" It's great that you aspire to have your site get as much traffic as Facebook. But that doesn't mean you should architect it like Facebook does. Don't build fancy, complex automations and flexible architectures until you really _need_ them. It saves you money, time, and sometimes it can even save a project from going completely off the rails!

Much like the gold plating on the hammer I was holding earlier, extra features that you don't need are a waste of resources, and may actually make your project worse off.

### Andon board

In researching motivations behind some Agile practices, I came across an interesting book about lean manufacturing, [_The Machine that Changed the World_](https://www.amazon.com/Machine-That-Changed-World-Revolutionizing/dp/0743299795/ref=as_li_ss_tl?ie=UTF8&linkCode=ll1&tag=mmjjg-20&linkId=07bf1ed7630bfdb7132e836cd4b85739&language=en_US). A lot of the ideas you may hear and even _groan_ about in Agile methodology, and even DevOps, come from the idea of _lean manufacturing_.

One of the more interesting ideas is the _andon board_, a set of displays visible to every single worker in Toyota's manufacturing plant. If there's ever a problem or blockage, it is displayed on that board, and workers are encouraged to 'swarm the problem' until it is fixed—even if it's in a different part of the plant. The key is understanding that problems should not be swept aside to be dealt with when you have more time. Instead, everyone on the team must be _proactive_ in fixing the problem before it causes a plant-wide failure to produce.

### Time to Drupal

I did a blog post after DrupalCon last year discussing how different local Drupal development environments have dramatically different results in my measurement of ["Time to Drupal"](/blog/2018/drupal-fastest-improving-evaluator-experience). That is, from not having it downloaded on your computer, to having a functional Drupal environment you can play around with, how long does it take?

If it takes you more than 10 minutes to bring up your local environment, you should consider ways to make that process much faster. Unless you have a multi-gigabyte database that's absolutely essential for all development work (and this should be an exceedingly rare scenario), there's no excuse to spend hours or days onboarding a new developer, or setting up a new computer when your old one dies!

### Dev to Prod

Similarly, how long does it take, once a feature or bugfix has been deployed somewhere and approved, for it to be deployed to production? Does this process take more than a day? Why? Are you trying to batch multiple changes together into one larger deployment?

The DevOps Handbook has some good advice about this:

> "one of the best predictors of short lead times was small batch sizes of work"<br>
> —The DevOps Handbook

And wouldn't you know, there's a lean term along this theme: _Takt time_, or the average amount of time it takes between delivering units of work.

If you batch a bunch of deployments together instead of delivering them to production as they're ready, you'll have a large _Takt_ time, and this means you can't quickly deliver value to your end users. You want to reduce that time by speeding up your process for getting working code to production.

## Conclusion

Those tools might not be the tools you were thinking I'd mention, like DevShop, Drupal VM, Lando, Docker, or Composer. But in my mind, if you want to implement DevOps in the real world, those tools might be helpful as implementation details, but you should spend _more_ time thinking about real world DevOps tools: better process, better communication, and better relationships.

If you do that, you will truly end up _making people happier while making apps better_.

Thank you.

## Resources mentioned in the presentation

  - [The DevOps Handbook](https://www.amazon.com/DevOps-Handbook-World-Class-Reliability-Organizations/dp/1942788002/ref=as_li_ss_tl?s=books&ie=UTF8&qid=1542338554&sr=1-3&keywords=The+DevOps+Handbook&linkCode=ll1&tag=mmjjg-20&linkId=ffdee2f1c5ac5516bc85653e37a3879f&language=en_US)
  - [The Phoenix Project](https://www.amazon.com/Phoenix-Project-DevOps-Helping-Business/dp/1942788290/ref=as_li_ss_tl?s=books&ie=UTF8&qid=1542338576&sr=1-1&keywords=the+phoenix+project&linkCode=ll1&tag=mmjjg-20&linkId=a15071a84ddc330c65d467ac2326b052&language=en_US) (if you're stuck in bureaucratic hell)
  - [Refactoring](https://www.amazon.com/Refactoring-Improving-Existing-Addison-Wesley-Signature/dp/0134757599/ref=as_li_ss_tl?s=books&ie=UTF8&qid=1542338593&sr=1-1&keywords=refactoring&linkCode=ll1&tag=mmjjg-20&linkId=5f9228396f39053f54d5eeec4bbfaf87&language=en_US)
  - [The Mythical Man-Month](https://www.amazon.com/Mythical-Man-Month-Software-Engineering-Anniversary/dp/0201835959/ref=as_li_ss_tl?s=books&ie=UTF8&qid=1542338611&sr=1-1&keywords=mythical+man+month&linkCode=ll1&tag=mmjjg-20&linkId=8ba71388b8013a42c2a7a39c2603e3ca&language=en_US) (not strictly mentioned here but a great read about team dynamics for software development)
  - [The Machine that Changed the World](https://www.amazon.com/Machine-That-Changed-World-Revolutionizing/dp/0743299795/ref=as_li_ss_tl?ie=UTF8&linkCode=ll1&tag=mmjjg-20&linkId=9adb7c29da6b911de8ed703c54e1773b&language=en_US)
