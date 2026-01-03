---
nid: 2965
title: "Running a Github Actions workflow on schedule and other events"
slug: "running-github-actions-workflow-on-schedule-and-other-events"
date: 2020-02-11T23:48:41+00:00
drupal:
  nid: 2965
  path: /blog/2020/running-github-actions-workflow-on-schedule-and-other-events
  body_format: markdown
  redirects: []
tags:
  - actions
  - cd
  - ci
  - continuous integration
  - github
  - testing
  - yaml
---

One thing that was not obvious when I was setting up GitHub Actions on the [Ansible Kubernetes Collection repository](https://github.com/ansible-collections/kubernetes) was how to have a 'CI' workflow run both on pull requests _and_ on a schedule. I like to have scheduled runs for most of my projects, so I can see if something starts failing because an underlying dependency changes and breaks my tests.

The [documentation for `on.schedule`](https://help.github.com/en/actions/reference/events-that-trigger-workflows#scheduled-events-schedule) just has an example with the workflow running on a schedule. For example:

```
on:
  schedule:
    # * is a special character in YAML so you have to quote this string
    - cron:  '*/15 * * * *'
```

_Separately_, there's [documentation](https://help.github.com/en/actions/reference/events-that-trigger-workflows#example-using-a-list-of-events) for triggering a workflow on events like a 'push' or a 'pull_request':

```
on: [push, pull_request]
```

And even in a dict format:

```
on:
  push:
    branches:
      - master
  pull_request:
    branches:
      - master
```

But that example is only useful if you _only_ want to run on the `master` branch. What if you want it to behave the same as the previous example, `on: [push, pull_request]`?

Well, with YAML, you don't have to specify a value for a key, and GitHub Actions' parser seems to accept a key with an empty value as being the same as a string list item for events, so the following is what I came up with, that seems to work:

```
on:
  push:
  pull_request:
  schedule:
    - cron: '*/15 * * * *'
```

The above would run the GitHub Actions workflow on every push (to any branch), every pull request (against any branch), and on the cron schedule of every 15 minutes through the day. I typically run my schedules either daily or weekly, depending on how much I need to track the day-to-day changes in my project's underlying dependencies.
