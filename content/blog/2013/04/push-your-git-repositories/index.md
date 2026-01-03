---
nid: 2403
title: "Push your Git repositories to a central server, in a bare repository"
slug: "push-your-git-repositories"
date: 2013-04-25T16:24:24+00:00
drupal:
  nid: 2403
  path: /blogs/jeff-geerling/push-your-git-repositories
  body_format: full_html
  redirects: []
tags:
  - backup
  - git
  - github
  - repositories
  - version control
aliases:
  - /blogs/jeff-geerling/push-your-git-repositories
   - /blogs/jeff-geerling/push-your-git-repositories
---

<a href="https://github.com/">GitHub</a> is a great central repository silo for open source projects, and for private Git repositories for companies and organizations with enough cash to afford the features GitHub offers.

However, for many projects and developers, GitHub can be overkill. For my needs, I have many smaller private projects that I'd like to have hosted centrally, and backed up, but don't warrant BitBucket or GitHub accounts. Therefore, I've taken to creating bare repositories on one of my Linode servers, and pushing all my local branches and tags to these repos. That server is backed up nightly, so I know if I lose my local environment, as well as my Time Machine backup (a very unlikely occurrence, but still possible), I will have backed up and fully intact Git repos for all my projects.

I recommend you do something like the following (presuming you already have a Git repo on your local computer that you've been working with):

<h2>Step 1 - on your remote server (accessible via ssh)</h2>

```
# Create a 'repositories' directory in your user home directory.
$ mkdir ~/repositories && cd ~/repositories

# For each of your local repositories, make a directory ending in '.git'.
$ mkdir My-Project.git && cd My-Project.git

# Create a bare git repository inside this new directory.
$ git --bare init
```

Here's a good article outlining the <a href="http://gitready.com/advanced/2009/02/01/push-to-only-bare-repositories.html">why and how of pushing to bare repositories</a>.

<h2>Step 2 - on your local computer</h2>

```
# Add the 'origin' to push to. This uses the relative path for the username you were
# logged in as when you created the bare repo earlier.
$ git remote add origin [username]@[host]:repositories/My-Project.git/

# Push your master branch to the remote repo.
$ git push origin master

# Push other tags and branches, tracking them locally.
$ git push -u origin 1.x
$ git push -u origin 2.x
etc...
```

Now, after you've made some commits locally, you can just use <code>git push</code> to push the changes up to the live server. If you're working on different branches or tags, be sure to push those up as well!

Since your remote server doesn't have a checked out/live branch in the repository (it's bare, so it only contains a <code>.git</code> folder), you can check to see the latest changes in the repository by <code>cd</code>ing into the repository and using <code>git log master</code> to see the latest commits on the <code>master</code> branch, or <code>git tag</code> to see a list of all the tags. Commands like <code>git status</code> don't work on a bare repository.
