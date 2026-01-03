---
nid: 2964
title: "Saying 'No' to burnout as an open source maintainer"
slug: "saying-no-burnout-open-source-maintainer"
date: 2020-02-07T19:45:23+00:00
drupal:
  nid: 2964
  path: /blog/2020/saying-no-burnout-open-source-maintainer
  body_format: markdown
  redirects:
    - /blog/2020/preventing-burnout-maintaining-200-oss-projects-and-writing-2-books
aliases:
  - /blog/2020/preventing-burnout-maintaining-200-oss-projects-and-writing-2-books
tags:
  - burnout
  - essay
  - github
  - maintainer
  - open source
  - pull requests
---

There's been a ton of writing about OSS stewardship, sustainability, funding, etc. in the past year, along with story after story of burnout. In this time, I've become very strict in my open source maintainership:

> Unless it's generating income, it's for me and I'm not going to spend more than a couple hours a month looking at it—if that.

There are a number of projects that I maintain, which I'm not actively using on money-generating projects. I don't normally touch or even look at the issue queues on these projects until a CI test fails, or unless someone who contributes to my Patreon or GitHub supporters—or who I know from previous contributions—pings me directly about them. Every now and then I'll run through the list of PRs and merge a bugfix or docs fix here and there, but that only happens maybe once per repository per year.

I have [Patreon](https://www.patreon.com/geerlingguy) and [GitHub Sponsors](https://github.com/sponsors/geerlingguy) set up, but unless you already have 'celebrity' status or are really good at marketing (hint: I'm not that good, and most people who are more prolific maintainers than me spend even less time marketing themselves... most of us hate doing it at all), you make maybe $10-20/month, tops. That's a pittance.

You can usually see which repos I actively nurture by viewing my GitHub activity feed. Currently, that list includes projects like the [Kubernetes collection for Ansible](https://github.com/ansible-collections/kubernetes), my [Ansible for DevOps](https://github.com/geerlingguy/ansible-for-devops) and [Ansible for Kubernetes](https://github.com/geerlingguy/ansible-for-kubernetes) book repos, or my [solr-container](https://github.com/geerlingguy/solr-container) project, used by [Hosted Apache Solr](https://hostedapachesolr.com). All of those projects are directly related to revenue streams that make it possible for me to have a roof over my head and feed my family.

Some people complain that "if you aren't willing to _actively_ maintain your projects, you should let them go and give them to other maintainers." Sounds reasonable, right? But, if you put yourself in the shoes of a maintainer, you realize:

  1. The project already has a very liberal open source license, so anyone who wants can fork it. I encourage forking heartily, and at least [11,000 people](https://stldevs.com/developers) have done it.
  2. Granting maintainership rights to a repo under my namespace means I trust the new maintainer to safeguard the project's users the same as I would—this level of trust is hard to establish, and there are only a dozen or so people on this planet I know well enough to grant that status.
  3. Of those dozen or so people, all of them are in the same situation as me, and they have learned to say no to taking on more projects which are not directly generating income for them.
  4. I _have_ shared responsibility and given commit access to others at least a dozen times in the past. On only _one_ of those projects did the new maintainer do anything beyond the first month or so's worth of maintenance.

There's no silver bullet here. There are very few individuals willing to dedicate the (vast) amount of time it takes to _actively_ maintain and improve open source projects, especially if the projects do not contribute back to that individual's bottom line in some way or another (be it influence, revenue, or ability to achieve a particular goal). These people exist, and I love them, but they are extraordinarily rare, and even more prone to burnout.

A few years ago, I wrote [Why I close PRs (OSS project maintainer notes)](https://www.jeffgeerling.com/blog/2016/why-i-close-prs-oss-project-maintainer-notes). Since writing that, I've gotten even stricter about protecting my time. One major reason is I now have _three_ young children (ages 3, 5, and 7!), and family always comes before code. I also came close to burnout in a previous position, and have implemented a number of changes in my work and lifestyle to prevent that from happening again.

The main change was:

> Be liberal with your 'no', be judicious with your 'yes'.

And part of that 'no', for me, is to unwatch any GitHub repository I don't actively maintain, and to ignore and redirect support requests for anything outside of revenue-generating projects<sup>1</sup>.

Large organizations with a dozen or more developers committing 40+ hours a week struggle to keep up with issue queues and support requests—how can you expect smaller projects maintained by individuals in their spare time for no pay would be any better off?

<hr>

<sup>1</sup> I receive five to ten emails to my personal email daily asking for free help with one of my open source projects, outside the 5-10 GitHub issues opened daily.
