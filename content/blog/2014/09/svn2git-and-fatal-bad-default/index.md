---
nid: 2465
title: "SVN2Git and \"fatal: bad default revision 'HEAD'\""
slug: "svn2git-and-fatal-bad-default"
date: 2014-09-04T20:29:42+00:00
drupal:
  nid: 2465
  path: /blogs/jeff-geerling/svn2git-and-fatal-bad-default
  body_format: full_html
  redirects: []
tags:
  - git
  - svn
  - svn2git
  - vcs
---

I was recently converting a repository from SVN to Git <a href="/blogs/jeff-geerling/switching-svn-repository-svn2git">using KDE's SVN2Git</a>, and after the conversion was done, the repository didn't seem to work that well. Inside the bare repo, if I tried <code>git log</code>, I received:

```
fatal: bad default revision 'HEAD'
```

I also tried <code>git fsck</code>, which resulted in:

```
notice: HEAD points to an unborn branch (master)
```

After trying a few different methods to resurrect the git repository, I noticed that my SVN2Git rules file defined the name of the resulting git repository as <code>example-example</code> (note the dash). Removing the dash fixed the issue, and now I have a happy git repository!

<strong>tl;dr</strong>: Don't use special characters in the name of the resulting git repository in SVN2Git's rules file.
