---
nid: 3052
title: "Travis CI's new pricing plan threw a wrench in my open source works"
slug: "travis-cis-new-pricing-plan-threw-wrench-my-open-source-works"
date: 2020-11-05T23:48:13+00:00
drupal:
  nid: 3052
  path: /blog/2020/travis-cis-new-pricing-plan-threw-wrench-my-open-source-works
  body_format: markdown
  redirects: []
tags:
  - actions
  - continuous integration
  - github
  - open source
  - testing
  - travis ci
---

I just spent the past 6 hours migrating some of my open source projects from Travis CI to GitHub Actions, and I thought I'd pause for a bit (12 hours into this project, probably 15-20 more to go) to jot down a few thoughts.

I am not one to look a gift horse in the mouth. For almost a decade, Travis CI made it possible for me to build—and maintain, for years—[hundreds of open source projects](https://github.com/geerlingguy).

I have built projects for Raspberry Pi, PHP, Python, Drupal, Ansible, Kubernetes, macOS, iOS, Android, Docker, Arduino, and more. And almost every single project I built got immediate integration with Travis CI.

Without that testing, and the ability to run tests on a schedule, I would have abandoned most of these projects. But with the testing, I'm able to keep up with build failures induced by bit rot over the years and review PRs more easily.

## What went wrong with Travis CI?

From the outset, Travis CI was built to integrate with GitHub repositories and offer free open source CI. At one time it was showered with praise on Hacker News and elsewhere for its culture and ethos.

But as the years passed, other CI systems became much more popular, until late in 2018, GitHub dropped the bombshell that was GitHub Actions, and it seemed like the outlook for Travis CI went to:

{{< figure src="./this-is-fine-fire-dog.jpg" alt="K.C. Green - This is fine dog in fire" width="250" height="257" class="insert-image" >}}

Now, to shed a little more light on where, precisely, things went from bad to worse, I put together this little timeline of Travis CI's most important moments in relation to open source builds:

  - 2011: [Travis CI is founded](https://blog.travis-ci.com/hello_world), offering free open source CI integration with GitHub repositories.
  - July 2011: [Ruby on Rails starts testing on Travis CI platform](https://news.ycombinator.com/item?id=2811554)
  - 2012: [Travis CI raises $134k to support business operations in 'Love' crowdfunding campaign](https://love.travis-ci.org), and launches paid plans for private repositories
  - 2012-2020: I integrated over 200 of my open source project repositories into Travis CI test and build processes.
  - May 2018: [Travis CI announces open source project migration to travis-ci.com](https://blog.travis-ci.com/2018-05-02-open-source-projects-on-travis-ci-com-with-github-apps)
  - October 2018: [GitHub launches GitHub Actions](https://news.ycombinator.com/item?id=18231097)
  - **Jan 2019**: **[Idera buys Travis CI](https://news.ycombinator.com/item?id=18978251)**
  - Feb 2019: [Travis CI lays off significant portion of engineering staff](https://twitter.com/ReinH/status/1098663375985229825)
  - Oct 2020: [Travis CI .org open source build capacity significantly limited](https://travis-ci.community/t/build-delays-for-open-source-project/10272/2), causing [days-long backlogs](https://twitter.com/geerlingguy/status/1324480667984498689/photo/1).
  - Oct 2020: I moved all my ~120 remaining travis-ci.org repos to travis-ci.com so they would actually run.
  - Nov 2, 2020: [Travis CI announces new pricing model, effectively ends generous open source offering](https://blog.travis-ci.com/2020-11-02-travis-ci-new-billing)
  - Nov 2, 2020: I notice **none of my builds are working**. I ran out of credits before I even saw the new billing plan notice.
  - December 31, 2020: [Travis-ci.org will be put into read-only mode](https://docs.travis-ci.com/user/migrate/open-source-repository-migration/#frequently-asked-questions).

Note that we're not yet caught up to the end of the timeline. There are many other open source developers and projects out there still using travis-ci.org, who either haven't found the time or motivation to migrate to travis-ci.com (or elsewhere, ideally), as evidenced by this massive daily backlog of build jobs:

{{< figure src="./travis-ci-backlog-builds-open-source.jpg" alt="Travis CI backlog of open source builds" width="650" height="397" class="insert-image" >}}

Those who, like me, finished migrating to travis-ci.com in the past couple of weeks to get out of that backlog hell are now realizing that we are going to have to beg for extra build minutes after our 1000 'trial plan' build minutes run out:

> We will be offering an allotment of OSS minutes that will be reviewed and allocated on a case by case basis. Should you want to apply for these credits please open a request with Travis CI support stating that you’d like to be considered for the OSS allotment. Please include:
> 
> - Your account name and VCS provider
> How many credits (build minutes) you’d like to request (should your run out of credits again you can repeat the process to request more or discuss a renewable amount)

Sorry, but no thanks. I don't have enough time in my day to send off emails every few [days|weeks|months] requesting extra build credits so I can continue maintaining my open source projects.

## Looking in the gift horse's mouth

As I said earlier, I am appreciative of the acceleration in my own growth and career that Travis CI enabled over the past decade. And there so many other services with generous offers for open source maintainers that I appreciate and try to support in any way I can (often financially, as far as I'm able).

I just fear that, like when Google shut down [Google Code](https://en.wikipedia.org/wiki/Google_Developers#Google_Code) in 2015, this will have some cascading affects on some of the smaller and less-maintained open source projects some of us rely on, but don't think about.

And I know personally, this whole project is going to soak up around 4 weeks worth of the time I can devote to my free open source work, meaning that's a month out of my open source development time that's just vanished into thin air. Not fun, and not motivating.

I'm lucky to have many supporters on [GitHub Sponsors](https://github.com/sponsors/geerlingguy) who have helped make my work more sustainable, but most open source maintainers have either a fraction of the support I do, or none at all.

## Migrating to GitHub Actions

{{< figure src="./github-actions.png" alt="GitHub Actions logo tagline" width="581" height="178" class="insert-image" >}}

Ever since the January 2019 buyout, the writing's been on the wall—especially after so much of the existing engineering staff was laid off. I had already started building newer projects using GitHub Actions for CI instead of Travis CI.

I had planned on slowly migrating over the course of a few years, since many of my older projects still work, and are used, but are not in active development.

But the actions Travis CI took this month—without any prior notice—forced my hand, and now I'm in the middle of probably a 2-to-4-week-long process of moving everything off Travis CI as fast as possible. Getting behind on build failures for a month would lead to a pileup of small issues that will really bog me down.

Anyways, enough of my sob story. I wanted to link to some of the tools I used to migrate, and show how I automated some of the migration, so you can do your own more easily!

The majority of my open source projects are Ansible roles (a large part of the [Ansible content I maintain](https://ansible.jeffgeerling.com)), and to get them migrated, I automated as much as possible. You can see all the details in this GitHub issue: [Convert from Travis CI to GitHub Actions](https://github.com/geerlingguy/ansible-role-apache/issues/201).

For each role, I used [this Ansible playbook](https://github.com/geerlingguy/ansible-role-apache/issues/201#issuecomment-722134447) to write new GitHub Actions CI and release workflows using a template. Then I adjusted all the 'cron' values so the Actions won't all run at the same exact time each week.

Then I created [github-repo-manager](https://github.com/geerlingguy/github-repo-manager), a simple little project that uses [PyGithub](https://github.com/PyGithub/PyGithub) to make changes across all or a subset of my repositories. I used it to add a `GALAXY_API_KEY` secret to all repositories in my account that began with `ansible-role-*` (for repositories in a personal account, you have to add GitHub Actions secrets to each repo—for organizations, you can create shared organization secrets... much more convenient!).

Finally, I went in and manually migrated the small part of the Travis CI build definition that was custom to each role (e.g. some have a one-dimensional build-matrix, some have a two-dimensional, and they all have a different mix of OSes they build on).

I had already started building many new projects (both Ansible and Kubernetes-related) on top of GitHub Actions, even presenting on the process a few times (e.g. [Continuous Ansible testing with Molecule and GitHub Actions](https://www.youtube.com/watch?v=93urFkaJQ44)). The news earlier this week just accelerated my migration plans for older content from 'when I get time' to 'right now.'

Luckily, GitHub Actions does pretty much everything I could do in Travis CI (so far... I still have 36 more unique repos to go!), and the only real complaint I have is the `continue-on-error` functionality is no substitute for Travis CI's `allowed_failures` option.

There's still a bit of work to be done, and I'm trying to prioritize things so I don't leave my most widely-used projects (like [Drupal VM](https://www.drupalvm.com)) without active CI for too long, but at least this story doesn't have a bad ending.
