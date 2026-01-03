---
nid: 2807
title: "Git gives 'ERROR: Repository not found.' when URL is correct and SSH key is used"
slug: "git-gives-error-repository-not-found-when-url-correct-and-ssh-key-used"
date: 2017-09-06T19:23:05+00:00
drupal:
  nid: 2807
  path: /blog/2017/git-gives-error-repository-not-found-when-url-correct-and-ssh-key-used
  body_format: markdown
  redirects: []
tags:
  - git
  - github
  - ssh
  - ssh-agent
---

I had a fun problem that made me spin my wheels an hour or so today. I was having no issue cloning a remote repository a number of times in the morning while debugging a Jenkins build job that runs a git clone + Docker image build and push operation.

Suddenly, when I was doing some final testing, I started to get the following:

```
git clone git@github.com:geerlingguy/my-project.git                             
Cloning into 'my-project'...
ERROR: Repository not found.
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

I know that I had the repository's SSH key loaded (via `eval "$(ssh-agent -s)" && ssh-add ~/.ssh/deploy-key`), and if I unloaded the key, I would instead get:

```
Permission denied (publickey).
fatal: Could not read from remote repository.
```

...but after doing test after test, and confirming I could access GitHub itself just fine with `ssh -T git@github.com`, I began to wonder if I was delusional. I went back to the GitHub repo's GitHub page, and copied and pasted the URL using both HTTPS and SSH endpoints, and kept hitting the same issue.

Then I realized that this particular project was able to be run for a variety of different codebases, each one with it's own deploy key (GitHub requires a universally unique deploy key for each usage). And my local environment had the wrong codebase deploy key loaded. D'oh! I replaced the key in `~/.ssh/deploy-key` with the correct one, and now I am able to `git clone` without an issue.

I wouldn't have posted this blog post but for the fact that 99.9% of all the other "Repository not found" posts in Google search said "check your repository URL". Well, this blog post points out another way you can run into the issue, even if the repo URL is correct.
