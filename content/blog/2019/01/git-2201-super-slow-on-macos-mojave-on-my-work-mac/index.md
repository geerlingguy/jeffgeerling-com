---
nid: 2903
title: "Git 2.20.1 is super slow on macOS Mojave on my work Mac"
slug: "git-2201-super-slow-on-macos-mojave-on-my-work-mac"
date: 2019-01-09T20:14:53+00:00
drupal:
  nid: 2903
  path: /blog/2019/git-2201-super-slow-on-macos-mojave-on-my-work-mac
  body_format: markdown
  redirects:
    - /blog/2019/git-2201-super-slow-on-macos-mojave
aliases:
  - /blog/2019/git-2201-super-slow-on-macos-mojave
tags:
  - cli
  - git
  - homebrew
  - macos
  - performance
  - terminal
---

> **Update**: I just upgraded my personal mac to 2.20.1, and am experiencing none of the slowdown I had on my work Mac. So something else is afoot. Maybe some of the 'spyware-ish' software that's installed on the work mark is making calls like `lstat()` super slow? Looks like I might be profiling some things on that machine anyways :)

I regularly use Homebrew to switch to more recent versions of CLI utilities and other packages I use in my day-to-day software and infrastructure development. In the past, it was necessary to use Homebrew to get a much newer version of Git than was available at the time on macOS. But as Apple's evolved macOS, they've done a pretty good job of keeping the system versions relatively up-to-date, and unless you need bleeding edge features, the version of Git that's installed on macOS Mojave (2.17.x) is probably adequate for now.

But back to Homebrew—recently I ran `brew upgrade` to upgrade a bunch of packages, and it happened to upgrade Git to `2.20.1`.

Later in the day when I was doing some heavy Git activity, I noticed everything felt... so... sluggish. And it was even sluggish on tiny git repos with less than 100 files, so either something was seriously wrong with my filesystem—which should've shown problems elsewhere—or Git was being funny.

So I benchmarked it:

```
$ time git status
On branch master
nothing to commit, working tree clean

real	0m1.037s
user	0m0.004s
sys	0m0.009s
```

That's... suspicious. A full second just to check the working directory? And I ran `git gc` and `git status` again, no difference. I ran it a bunch of times and it was always ± 0.1% of that timing.

I went ahead and unlinked the Brew-installed Git:

    brew unlink git

Then opened a new Terminal window, and ran the same test:

```
$ time git status
On branch master
nothing to commit, working tree clean

real	0m0.018s
user	0m0.005s
sys	0m0.010s
```

Ahh... much better. Special thanks to [Steven Wichers](https://www.drupal.org/u/stevenwichers) for putting the idea in my head that the Git version could be the problem—I remember a couple weeks ago in a tech chat at Acquia he mentioned something similar. If it weren't for that, I would've spent a few hours trying to profile and debug git traces, most likely! Seconds count, when you run like 5,000 `git` commands a day!
