---
nid: 2354
title: "Simple Git feature branch workflow"
slug: "git-simple-feature-branch"
date: 2011-12-07T17:33:41+00:00
drupal:
  nid: 2354
  path: /blogs/jeff-geerling/git-simple-feature-branch
  body_format: full_html
  redirects: []
tags:
  - branch
  - development
  - drupal
  - drupal 7
  - drupal planet
  - git
  - merge
  - workflow
aliases:
  - /blogs/jeff-geerling/git-simple-feature-branch
---

After reading <a href="http://nvie.com/posts/a-successful-git-branching-model/">A successful Git branching model</a> [nvie.com], which I consider one of the best graphical/textual depictions of the ideal Git model for development teams (and most large projects), I simply wanted to adapt a similar (but way less complex) model for some of my smaller sites and multisite Drupal installs.

Since I'm (almost always) the only developer, and I develop locally, I don't want the complexity of working on many branches at once (master, hotfixes, develop, release, staging, etc...), but I do want to have a clean separation between what I'm working on and the actual live master branch that I deploy to the server.

So, I've adopted a simple 'feature branch model' for my smaller projects:

<ul>
	<li><strong>master</strong> - the live/production code. Only touch when merging in a feature or simply fixing little bugs or really pressing problems.</li>
	<li><strong>[issue-number]-feature-branches</strong> - Where I work on stuff.</li>
</ul>

Graphically:

<p style="text-align: center;">{{< figure src="./feature-branch-graphic.jpg" alt="Feature branch model" width="600" height="85" >}}</p>

Any time I work on something more complicated than a simple styling tweak, or a fix for a WSOD or something like that, I simply create a feature branch (usually with an issue number that matches up to my internal tracking system). Something like 374-add-node-wizard:

```
# create (-b) and checkout the 374-add-node-wizard branch.
$ git checkout -b 374-add-node-wizard
```

While I'm working on the node wizard (which could take a week or two), I might make a couple little fixes on the master branch. After I make the fixes on master (switch to it using <code>$ git checkout master</code>), I switch back to my feature branch and rebase my feature branch:

```
$ git checkout 374-add-node-wizard # switch back to the feature branch
$ git rebase master # pull in all the latest code from the master branch
```

I can also create simple .patch files off a branch to pass my work to another server or a friend if I want (I like using patches instead of pushing around branches, simply because patch files are easier for people to grok than more complicated git maneuvers):

```
# create a diff/patch file from the checked out branch.
$ git diff master..374-add-node-wizard > 374-add-node-wizard-patch.patch
```

When I finish my work on the feature branch, I switch back to master, merge in the branch, and delete the branch. All done!

```
$ git checkout master # switch back to master
$ git merge --no-ff 374-add-node-wizard # merge feature branch back into master
$ git branch -d 374-add-node-wizard # delete the feature branch
```

Finally, I test everything to make sure it's working fine in master, and then push the code changes up to the server.

Since I'm developing alone, this is a lot easier than a more complicated branching setup, and it allows me to work on as many features as I want, without fear of messing things up on master, or having merge conflicts (I rebase early and often).

(Note: I usually work in the command line, because I'm more comfortable knowing what git is doing that way... but I often open up <a href="http://www.git-tower.com/">Tower</a> (imo, the best application for visual Git) to inspect branches, commits, and merges/rebases... some people would probably rather just use Tower for everything).

(Note 2: When creating patches to send to someone that include binary files (like a png or a gif, jpeg, whatever), make sure you use <code>$ git diff --full-index --binary [old]..[new] > patchfile.patch</code> so git doesn't barf when you try applying the patch on someone else's end...).
