---
nid: 2810
title: "Patching or using a forked version of an Ansible Galaxy role"
slug: "patching-or-using-forked-version-ansible-galaxy-role"
date: 2017-09-11T17:11:17+00:00
drupal:
  nid: 2810
  path: /blog/2017/patching-or-using-forked-version-ansible-galaxy-role
  body_format: markdown
  redirects: []
tags:
  - ansible
  - ansible-galaxy
  - fork
  - github
  - maintenance
  - open source
  - patches
  - roles
---

I maintain a _lot_ of Ansible Galaxy roles. I probably have a problem, but I won't admit it, so I'll probably keep adding more roles :)

One thing I see quite often is someone submitting a simple Pull Request for one of my roles on GitHub, then checking in here and there asking if I have had a chance to merge it yet. I'm guessing people who end up doing this might not know about one of the best features of Ansible Galaxy (and more generally, open source!): you can fork the role and maintain your changes in the fork, and it's pretty easy to do.

I just had to do it for one project I'm working on. I am using the `rvm_io.ruby` role to install specific versions of Ruby on some servers. But there seems to have been a breaking change to the upstream packages RVM uses, summarized in [this GitHub issue](https://github.com/rvm/rvm1-ansible/issues/157). I found a pretty simple fix (removing one array item from a variable), and submitted [this PR](https://github.com/rvm/rvm1-ansible/pull/158).

So far, so good, but _how can I tell my Ansible playbooks to patch in this fix_? If I can't do that, I'll either have to download and commit a forked version of the role to my repository (yuck! Don't include dependencies in your codebase except in extreme cases!), or wait until the maintainer merges the PR and tags a new release.

But I need this working _today_! Otherwise, my project will be at a standstill.

Luckily, I can change one thing in my Galaxy `requirements.yml` file, and all will be well. Instead of asking for the `rvm_io.ruby` role from Galaxy, like this:

```
---
# Ansible Galaxy roles.
- src: rvm_io.ruby
  version: v2.0.0
...
```

I can instead reference my fork and branch (from which I generated the earlier-mentioned pull request):

```
---
# Ansible Galaxy roles.
# - src: rvm_io.ruby
#   version: v2.0.0
...
# Forked Ansible Galaxy roles.
- src: https://github.com/geerlingguy/rvm1-ansible # URL to my fork of the Galaxy role's GitHub repository.
  version: 157-remove-testrb # the name of my patch branch.
  name: rvm_io.ruby # save the role with the name it had when downloaded from Galaxy.
```

Or if you have any trouble getting the forked role from git, you can just download a .tar.gz file for the role instead:

```
- src: https://github.com/geerlingguy/rvm1-ansible/archive/157-remove-testrb.tar.gz
  name: rvm_io.ruby
```

Then update your downloaded dependencies with: `ansible-galaxy install -r requirements.yml --force` (the `--force` is necessary if you've already downloaded dependencies, so that your new forked role overwrites the existing downloaded role version).

The nice thing is, this kills two birds with one stone:

  1. I've submitted an upstream PR so that others can benefit from my fix.
  2. I have a fork that's easier to maintain than a separate patch file or diffing the codebase, since I can just do a `git pull upstream master` then do a `rebase` on my branch to update with the latest upstream fixes.

If you _don't_ do it this way, you're basically creating a hard fork of the upstream role and taking on the _entire_ maintenance responsibility for the role. 99% of the time, I don't want to do that—I just want to patch a role until the upstream maintainer merges my patch. So every month or so, when I update role dependencies in my projects, I go back and check if I can switch back from my forked/patched repository to the original Galaxy role!
