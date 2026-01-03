---
nid: 2822
title: "Properly deploying updates to or shutting down Jenkins"
slug: "properly-deploying-updates-or-shutting-down-jenkins"
date: 2017-12-08T17:36:36+00:00
drupal:
  nid: 2822
  path: /blog/2017/properly-deploying-updates-or-shutting-down-jenkins
  body_format: markdown
  redirects: []
tags:
  - ansible
  - automation
  - ci
  - continuous integration
  - curl
  - devops
  - jenkins
---

One of my most popular Ansible roles is the [`geerlingguy.jenkins`](https://galaxy.ansible.com/geerlingguy/jenkins/) role, and for good reason—Jenkins is pretty much _the_ premiere open source CI tool, and has been used for many years by Ops and Dev teams all over the place.

As Jenkins (or other CI tools) are adopted more fully for automating all aspects of infrastructure work, you begin to realize how important the Jenkins server(s) become to your daily operations. And then you realize you need CI for your CI. And you need to have version control and deployment processes for things like Jenkins updates, job updates, etc. The `geerlingguy.jenkins` role helps a lot with the main component of automating Jenkins install and configuration, and then you can add on top of that a task that copies config.xml files with each job definition into your `$JENKINS_HOME` to ensure every job and every configuration is in code...

But what happens when you need to push up an update (or update Jenkins itself!), and there are numerous ongoing scheduled jobs, as well as developers kicking off builds wily-nily? Or what if you need to shut Jenkins down but don't want to terminate any builds that are in-progress?

Jenkins has a nice little feature called 'quietDown' mode that allows any running jobs to complete, but which queues any other scheduled or manually triggered jobs, to be run after the next Jenkins restart.

{{< figure src="./jenkins-quietdown-going-to-shut-down.png" alt="Jenkins in quietDown mode - Jenkins is going to shut down" width="650" height="135" class="insert-image" >}}

In the _old_ days of Jenkins, before there was any CSRF protection in place, you could just go to https://your-jenkins-url/quietDown and put Jenkins in quietDown mode. But with CSRF protection, you'll get a 403 and a warning about a Crumb not being present in the URL.

So, here's how I currently set Jenkins into quietDown mode in my automation scripts that handle Jenkins job changes, updates, upgrades, etc.:

```
# Get a valid crumb from Jenkins:
CRUMB=$(curl -u user:pass -s 'https://jenkins.example.com/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,":",//crumb)')

# Use the crumb in the quietDown request:
curl -X POST -H "$CRUMB" -u user:pass https://jenkins.example.com/quietDown
```

If you need to get Jenkins back into normal mode without restarting or shutting down Jenkins, use `cancelQuietDown` in the 2nd request instead of `quietDown`.

References:

  - [How to Start, Stop or Restart your Instance?](https://support.cloudbees.com/hc/en-us/articles/216118748-How-to-Start-Stop-or-Restart-your-Instance-) (Cloudbees Support)
  - [How to disable a Jenkins job via curl?](https://stackoverflow.com/a/38314286/100134) (Stack Overflow)
