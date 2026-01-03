---
nid: 2815
title: "Ansible jenkins_plugin module and 404 'Plugin not found.'"
slug: "ansible-jenkinsplugin-module-and-404-plugin-not-found"
date: 2017-10-16T17:50:46+00:00
drupal:
  nid: 2815
  path: /blog/2018/ansible-jenkinsplugin-module-and-404-plugin-not-found
  body_format: markdown
  redirects:
    - /blog/2017/ansible-jenkinsplugin-module-and-404-plugin-not-found
aliases:
  - /blog/2017/ansible-jenkinsplugin-module-and-404-plugin-not-found
tags:
  - 404
  - ansible
  - galaxy
  - jenkins
  - role
  - security
  - update
---

Every few weeks, when some of my automated Jenkins build jobs are running (using Ansible and [my Jenkins role](https://github.com/geerlingguy/ansible-role-jenkins) on Ansible Galaxy), they hit an error while configuring Jenkins plugins. The error is something like:

```
TASK [geerlingguy.jenkins : Install Jenkins plugins using password.] ***********
ok: [server] => (item=git)
ok: [server] => (item=ansicolor)
changed: [server] => (item=blueocean)
ok: [server] => (item=role-strategy)
ok: [server] => (item=extended-choice-parameter)
ok: [server] => (item=build-timestamp)
failed: [server] (item=cloudbees-folder) => {"details": "HTTP Error 404: Not Found", "failed": true, "item": "cloudbees-folder", "msg": "Plugin not found."}
```

I originally chalked it up to bad luck, because the problem would go away on it's own, usually within a day or two. But then I realized that Jenkins checks the plugin database every so often, and if the cached listing on the Jenkins server in question is out of date, it can cause this 404 error to occur.

The easy fix? Log into Jenkins as an admin, go to Manage Jenkins > Manage Plugins, and click the 'Check Now' button:

{{< figure src="./jenkins-check-now-plugins.png" alt="Jenkins plugins - check now for updates" width="650" height="323" class="insert-image" >}}

You can also run a task through the CLI or API to do the same thing, and it might be a good idea to automate that check as part of your playbook that runs updates (or maybe open an issue in the `geerlingguy.jenkins` issue tracker so I can add that feature to my role ?).
