---
nid: 3165
title: "The burden of an Open Source maintainer"
slug: "burden-open-source-maintainer"
date: 2022-01-10T15:51:42+00:00
drupal:
  nid: 3165
  path: /blog/2022/burden-open-source-maintainer
  body_format: markdown
  redirects: []
tags:
  - essay
  - github
  - maintainer
  - open source
  - sponsorship
---

Or: _Why can't you just merge my ten-line PR already?_

I maintain over 200 open source projects. Apparently (this is news to me) I am ranked in the top 200 GitHub users by followers, and there are 18,000 forks and 42,000 stars across my repos.

On an average day, I see between 50-100 emails across my repositories for issues and pull requests, and I filter those down to about 5-10 that I deem worthy of a personal follow-up.

I merge between 5-10 Pull Requests per month, and commit new code or fixes around 166 times per month.

I'm one maintainer, in a tiny corner of the Internet, maintaining a small but broad set of projects from Ansible roles for infrastructure automation to a few small but still-used PHP and Node.js libraries.

## Dealing with burnout

There have been a few times I've burned out. That's typical for many maintainers. You either learn coping strategies or burn out completely, and in the best case end up a woodworker or farmer. At least that's what I see most of the time.

My coping strategy for the past five years has been somewhat [ruthlessly closing PRs and issues](/blog/2016/why-i-close-prs-oss-project-maintainer-notes). I also wrote about [enabling the stale bot](/blog/2020/enabling-stale-issue-bot-on-my-github-repositories) two years ago, and let me tell you:

**Despite how much some people detest the stale bot, it—along with a more _laissez-faire_ attitude towards my projects—is the best burnout prevention measure I've taken.**

I license my projects as open source for two reasons:

  1. I have a _Pay-it-Forward_ philosophy when it comes to code and knowledge.
  2. It helps keep me strict about documentation, generalization, and security.

I don't publish my projects with an open source license because I want to leverage them into VC funding or build a new Silicon Valley startup. Nor do I plan on monetizing any of my projects through services or an 'open core' model.

I have a family, and I have a chronic illness, and I have to maintain some semblance of a work-life balance.

The problem is, users don't understand my project goals or life situation—not that I expect them to.

But some of these users and potential contributors take offense when an issue they post or a PR they toss over rots for a few months, eventually gets marked stale, and gets closed.

It's nothing personal.

I look at it this way: if I _didn't_ use my strategies to stave off burnout, I wouldn't maintain my projects _at all_. And having a project that works well and is maintained for 80% of the people who find it is better—in my mind—than adding on extra support and maintenance burden by dealing with every issue and PR that comes my way. And in the end, I maintain the projects for my own needs first.

Maybe that sounds callous, but it's the reality of the open source contract, whether the project in question is backed by a multi-billion-dollar corporation or a random guy in St. Louis.

## Why did you mark my PR stale?

Even a one-line PR that seems innocuous could break existing use cases, cause weird bugs that CI tests don't cover, and add maintenance overhead that _I_ will be responsible for through the life of the project.

And maybe that one line change leads to the next Log4J. But the person who submitted it isn't going to be the one staying up late on the weekend before a holiday cleaning up the mess:

<blockquote class="twitter-tweet" data-lang="en" data-dnt="true" data-theme="dark"><p lang="en" dir="ltr">Log4j maintainers have been working sleeplessly on mitigation measures; fixes, docs, CVE, replies to inquiries, etc. Yet nothing is stopping people to bash us, for work we aren&#39;t paid for, for a feature we all dislike yet needed to keep due to backward compatibility concerns. <a href="https://t.co/W2u6AcBUM8">https://t.co/W2u6AcBUM8</a></p>&mdash; Volkan Yazıcı (@yazicivo) <a href="https://twitter.com/yazicivo/status/1469349956880408583?ref_src=twsrc%5Etfw">December 10, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

The buck stops with the maintainer(s).

Therefore I never consider any PR 'simple', outside of grammar fixes in a README.

I'm very picky about which PRs I'll even spend 5 minutes on—usually I'll only look into the code changes if it's (a) fixing a bug in my project, or (b) adding a feature I would consider adding on my own.

And of those PRs, I find problems requiring a follow-up more than half the time.

I have a unique problem of maintaining a diverse set of projects, rather than one or two massive projects, so sometimes I can't be as deep in the code on each project as I'd like to... but even for maintainers of one or two projects, a seemingly innocuous change can introduce major bugs for some percentage of existing users, so that possibility always tempers your enthusiasm to merge the code.

And then there are the PRs for features that I know I'll never use. Usually (in my projects' case) for obscure functionality only needed in severely restricted enterprise environments.

Therefore I often take one of two approaches:

  1. Instead of merging the fix directly, I'll patch in some functionality that allows my project to be more flexible, so they could plug in their specific changes more easily (but not as easily as them injecting their code directly into my project—thus giving me the maintenance burden).
  2. I'll recommend they fork the project.

And option number two is honestly where things end up a lot, for features I'd consider a minority use case. When I worked in the severely restricted enterprise environment, I was used to maintaining forks and/or patches for a number of projects, so I could make them work in our strange environment.

Where I thought it might be useful to the upstream project, I would submit patches and PRs, but I fully understood there was little chance of getting the changes merged.

That's life in the open source world. That's why there are a zillion forks of the Linux kernel. That's why there are 18,000 forks of my 200-odd projects.

So sometimes, when someone gets cranky about my choice to ignore a feature or gets overly zealous in calling me out publicly in an issue for not responding, I kindly tell them to go fork themselves. The project is open source for a reason.

## Money

Every few years, there's another discussion about how, if only we could inject cash into the open source maintainer's pockets, we wouldn't have future Log4J's, or Heartbleeds, or Shellshocks. I don't think that's the case.

I'm one of the few maintainers who can actually pay my mortgage using the support from individuals and small businesses who contribute to my open source work. And I'm extremely thankful for that.

But I have two thoughts when it comes to 'compensation':

  1. Per my goals stated earlier, donations are not a contract—if `$megacorp` wanted me to make a change to my code, I'd be more amicable if they donated, but I am not beholden to them, nor do I ever want to be (if I did, I'd just work for them).
  2. I've had Patreon and other sponsorship methods for years; it was only after I shifted my approach that I started getting any significant sponsorship.

On that second point, I have to pull out the dreaded M-word that all software devs hate: _marketing_.

The only way I was finally able to venture out on my own, and devote more time to open source work, was to market things like [my books](/books) and [my YouTube channel](https://www.youtube.com/c/JeffGeerling). Book sales make up the majority of my revenue currently, and YouTube + sponsorships fill in the rest. And one could argue that most of the sponsorships I have are the result of increased visibility on YouTube.

Even still—with YouTube + book sales + donations—I make half what I made as a full time software developer, especially when I was consulting and charged a substantial hourly rate.

The truth is, money won't prevent the next Log4J vulnerability, or prevent maintainer burnout (leading to the next [`colors` and `faker` fiasco](https://www.bleepingcomputer.com/news/security/dev-corrupts-npm-libs-colors-and-faker-breaking-thousands-of-apps/)). It helps, and it's necessary to try to fund developers better—but you can't just say "Microsoft should pay developer X $80,000/year and that will prevent another Shellshock."

Corporate money often comes with expectations, and as an open source maintainer, I have enough to worry about besides trying to keep tabs on which sponsors/donors expect what, so I make it clear they are not 'buying' my time or attention. They're just removing barriers to maintaining the best open source projects I can.

I do think companies should have open source funds, and allocate them to projects and maintainers they depend on, on a monthly basis. But I don't think it will solve the funding problem, mostly because this kind of suggestion has been on the table for over a decade, and there are multiple ways to route the funds (GitHub Sponsors, Open Collective, et all), yet larger companies still allocate a pittance (if anything) to open source maintainers.

## Conclusion

This post was somewhat a stream-of-consciousness post for me, so I'm sorry it's a little disorganized. If you do want the greatest chance of me merging your code, I wrote about that back in 2018: [How can I get my PR merged into your open source project?](/blog/2018/how-can-i-get-my-pr-merged-your-open-source-project).

And if you work for a `$megacorp`, keep fighting the good fight to allocate some funding to open source projects and maintainers. A few companies _are_ willing to substantially support certain projects they depend on, but they are sadly the exception, not the norm.
