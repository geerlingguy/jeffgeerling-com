---
nid: 2455
title: "Simple Git-based multi-server deployments"
slug: "simple-git-based-multi-server"
date: 2014-05-14T02:06:24+00:00
drupal:
  nid: 2455
  path: /blogs/jeff-geerling/simple-git-based-multi-server
  body_format: full_html
  redirects: []
tags:
  - deployment
  - git
  - hooks
  - infrastructure
aliases:
  - /blogs/jeff-geerling/simple-git-based-multi-server
---

Ansible is used to manage most of Midwestern Mac's infrastructure and deployments, and while it's extremely easy to use, there are a couple situations where a project just needs a little code to be updated across two or more servers, from a central Git repository, or from one master application server.

All Git repositories include a <code>hooks</code> folder, which contains sample <a href="http://git-scm.com/book/en/Customizing-Git-Git-Hooks">git hook</a> scripts. Inside this folder are a series of sample hook files like <code>post-commit.sample</code> and <code>pre-rebase.sample</code>. If you add a shell script of the same name as any of these files (excluding the <code>.sample</code>) to this folder, Git will run the script when the particular action runs (e.g. git will run a <code>post-commit</code> script after a commit).

Instead of deploying a codebase to multiple servers by copying it manually via SFTP or rsync, or by logging into the servers and pulling down changes from a remote Git server, you can add a <code>post-receive</code> script in the hooks folder of your main git remote repository, and have it synchronize the codebase with one or more remote servers:

```
#!/bin/sh

# Check out the code on this server.
GIT_WORK_TREE=/opt/my-app git checkout -f

# Define an array of servers to which the code will be deployed.
SERVERS="abc.example.com, xyz.example.com"

# Push codebase to the servers via rsync.
for SERVER in $SERVERS
do
  /usr/bin/rsync -av --delete --exclude file-to-exclude.txt -e ssh /opt/my-app/ username@$SERVER:/opt/my-app/
done
```

I wouldn't use this except for the simplest of configurations or in rare situations where Ansible (or another deployment solution) wouldn't be suitable... but it does the job well. You'll need to make sure the user under which git is run has an SSH key configured to connect to all the remote servers.

Read more about <a href="http://git-scm.com/book/en/Customizing-Git-Git-Hooks">Git Hooks</a> on git-scm.com, and if you're interested in using Ansible for your deployments, check out my book, <a href="https://leanpub.com/ansible-for-devops">Ansible for DevOps</a>!
