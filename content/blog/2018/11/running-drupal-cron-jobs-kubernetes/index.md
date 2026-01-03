---
nid: 2893
title: "Running Drupal Cron Jobs in Kubernetes"
slug: "running-drupal-cron-jobs-kubernetes"
date: 2018-11-28T17:34:59+00:00
drupal:
  nid: 2893
  path: /blog/2018/running-drupal-cron-jobs-kubernetes
  body_format: markdown
  redirects: []
tags:
  - ansible
  - cron
  - cronjob
  - drupal
  - drupal 8
  - drupal planet
  - kubernetes
---

There are a number of things you have to do to make Drupal a first-class citizen inside a Kubernetes cluster, like adding a shared filesystem (e.g. PV/PVC over networked file share) for the files directory (which can contain generated files like image derivatives, generated PHP, and twig template caches), and setting up containers to use environment variables for connection details (instead of hard-coding things in settings.php).

But another thing which you should do for better performance and traceability is run Drupal cron via an external process. Drupal's cron is essential to many site operations, like cleaning up old files, cleaning out certain system tables (flood, history, logs, etc.), running queued jobs, etc. And if your site is especially reliant on timely cron runs, you probably also use something like [Ultimate Cron](https://www.drupal.org/project/ultimate_cron) to manage the cron jobs more efficiently (it makes Drupal cron work much like the extensive job scheduler in a more complicated system like Magento).

The reason you want to run cron via an external process—instead of having it be triggered by front-end page visits (this is how Drupal sets up cron by default, to run every few hours based on someone hitting the site)—is so you can make sure cron job runs don't interfere with any normal page visits, and so you can trace any issues with cron separately from normal web traffic.

Inside of Kubernetes, you can't (well, at least you _shouldn't_) have a `crontab` set up on any of your Kubernetes nodes running against your Drupal site(s). And while you could have an external system like Jenkins run cron jobs against your Drupal site, it's much easier (and simpler) to just run Drupal cron as a Kubernetes `CronJob`, ideally within the same Kubernetes namespace as your Drupal site.

The most robust way to run Drupal cron is via Drush, but running a separate Drush container via CronJob means that the CronJob must schedule a beefy container running at least PHP and Drush, and likely also your app codebase if you run Drush as a project dependency. CronJob Pods should be as lightweight as possible so they could be scheduled on any system node and run very quickly (even if your Drupal container hasn't been pulled on that particular Kubernetes node yet).

Drupal's cron supports being run from outside the site by hitting a URL, and as long as your cron runs can complete before PHP/Apache/Nginx's timeout, this is the simplest option for working with Kubernetes (IMO). For my Drupal sites running in Kubernetes, I configure a CronJob similar to the following:

```
---
apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: drupal-cron
  namespace: {{ k8s_resource_namespace }}
spec:
  schedule: "*/1 * * * *"
  concurrencyPolicy: Forbid
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: drupal-cron
            image: {{ curl_image }}
            args:
            - -s
            - {{ drupal_cron_url }}
          restartPolicy: OnFailure
```

In my case, I'm templating the Kubernetes manifest using Ansible and Jinja2 (deployed via my [K8s Manifests role](https://github.com/geerlingguy/ansible-role-k8s_manifests)), so I have Ansible replace the three variables with values like:

```
k8s_resource_namespace: my-drupal-site
curl_image: byrnedo/alpine-curl:0.1
drupal_cron_url: http://www.my-drupal-site.com/cron/cron-url-token
```

The `drupal_cron_url` is the URL specific to your site, which you can find by visiting `/admin/config/system/cron`. Make sure you also have "Run cron every" set to "Never" under the cron settings, so that cron is only triggered via Kubernetes' CronJob.

I use the `byrnedo/alpine-curl` docker image, which is extremely lightweight—only 5 or 6 MB in total—since it's based on Alpine Linux. Most of the other containers I've seen base on Ubuntu or Debian and are at least 30-40 MB (so they'll take _that_ much longer to download the first time the `CronJob` is run on a new node).

You can check on the status of the CronJob with:

    kubectl describe cronjob drupal-cron -n my-drupal-site
