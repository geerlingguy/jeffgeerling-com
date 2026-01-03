---
nid: 2975
title: "Enabling a stale issue bot on my GitHub repositories"
slug: "enabling-stale-issue-bot-on-my-github-repositories"
date: 2020-03-05T04:01:26+00:00
drupal:
  nid: 2975
  path: /blog/2020/enabling-stale-issue-bot-on-my-github-repositories
  body_format: markdown
  redirects: []
tags:
  - bot
  - burnout
  - contributions
  - github
  - maintainer
  - maintenance
  - open source
  - pull requests
---

For the past few years, the number of issues and PRs across all my GitHub repositories has gone from a steady stream to an ongoing deluge. There are currently over [1,500 open issues](https://github.com/search?q=user%3Ageerlingguy+state%3Aopen&type=Issues) across my 194 GitHub repositories, and there's no way I can keep up with all of them.

Initially, I went through each issue in each project's issue queue on a monthly basis (mind you, this was—and is still—done on nights and weekends in my spare time). That slipped to a quarterly task... and has now slipped to only happening for higher-profile projects once or twice a _year_.

{{< figure src="./probot-head.png" alt="Probot Head from GitHub Probot project" width="376" height="376" class="insert-image" >}}

To keep up with the constant barrage of new issues and PRs, many open source projects have employed a 'stale issue' bot ([Probot: stale](https://github.com/probot/stale)), which marks issues/PRs with no activity stale, then later closes them. Many issues are opened and never get a follow-up visit from the original author (even if I spend a half hour providing a thorough response). Often this person found a solution elsewhere and never thought to follow-up, or they don't have notifications enabled so they never even know someone responded.

Instead of letting these zombie issues clutter up the issue queue, the stale bot helps prune them.

You may have been directed to this issue from one of the issue closure notices.

Know that I don't close issues out of spite, or anger, or because I think the bug report, feature request, or other contribution has no value. Rather, unless something is breaking stability (e.g. a project I maintain won't install anymore, or breaks completely and CI blows up), or there's a major feature or missing component that I agree would be a no-brainer to have incorporated, I simply lack the bandwidth to be able to review the issue or PR.

One way you can help me get _more_ bandwidth is to [**sponsor me on GitHub**](https://github.com/sponsors/geerlingguy) or [**Patreon**](https://www.patreon.com/geerlingguy).

I can't promise sponsorship will lead me to reviewing your issue or PR more quickly, but one major problem with today's open source development model is the income generated from the tireless effort of open source maintenance is a pittance, and until that changes, I don't have the ability to devote more time to code review and responding to the deluge of open issues.

Also, note that for my Ansible open source projects, the current maintenance status is indicated on this site: [Jeff Geerling's Ansible Content](https://ansible.jeffgeerling.com).

> _Aside_: People have often mentioned I should cede control of my projects to others if the maintenance burden is to high, but they don't realize that:
> 
>   1. That would mean I don't have control over projects I built for myself and use in projects that contribute to my own income, and
>   2. Giving control over a project in my namespace is something I don't take lightly _at all_, because I entrust all the project's users to the new maintainer.
> 
> I don't take the responsibility of maintainership lightly, as trust is a valuable asset and is easy to lose.
