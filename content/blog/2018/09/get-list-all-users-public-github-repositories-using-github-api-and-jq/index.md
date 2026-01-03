---
nid: 2878
title: "Get a list of all a user's public GitHub repositories using GitHub API and jq"
slug: "get-list-all-users-public-github-repositories-using-github-api-and-jq"
date: 2018-09-26T01:41:44+00:00
drupal:
  nid: 2878
  path: /blog/2018/get-list-all-users-public-github-repositories-using-github-api-and-jq
  body_format: markdown
  redirects: []
tags:
  - api
  - command line
  - github
  - jq
  - list
  - repositories
  - users
---

I recently needed to do a quick audit on all my Ansible roles, and the easiest way (since almost every one is on GitHub, and that's the main source of truth I use) was to grab a list of all my GitHub repositories. However, it can be a little tricky if you have hundreds of repos. I'm guessing most people don't have this problem, but whether you do or not, the easiest way to get all of any given user's repositories using the GitHub v3 API is to run the following command:

```
curl "https://api.github.com/users/geerlingguy/repos?per_page=100&page=1" | jq -r '.[] | .name'
```

Example output:

```
 20:36:48 ~ $ curl "https://api.github.com/users/geerlingguy/repos?per_page=100&page=1" | jq -r '.[] | .name'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  608k  100  608k    0     0   480k      0  0:00:01  0:00:01 --:--:--  481k
acquia-cloud-api-scripts
acquia-cloud-vm
Android-Map-Marker-Drawables
ansible
ansible-container
ansible-examples
ansible-for-devops
ansible-meetup-lab
ansible-modules-core
ansible-modules-extras
ansible-newrelic
ansible-role-adminer
ansible-role-ansible
ansible-role-apache
...
```

This will output up to the first 100 repositories. Grab another 100 by changing to `page=2`, and so on, and then concatenate the lists together, and _voila_, you'll have list of all the user's repos.

This command assumes you have `curl` and `jq` installed (on a Mac, just use `brew install jq` if it's not already there), and the `-r` option passed to `jq` strips out quotes so the list is ready for whatever you need to do with it!
