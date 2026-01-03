---
nid: 2809
title: "Get started using Ansible AWX (Open Source Tower version) in one minute"
slug: "get-started-using-ansible-awx-open-source-tower-version-one-minute"
date: 2017-09-08T17:19:47+00:00
drupal:
  nid: 2809
  path: /blog/2017/get-started-using-ansible-awx-open-source-tower-version-one-minute
  body_format: markdown
  redirects: []
tags:
  - ansible
  - ansible tower
  - automation
  - awx
  - ci
  - docker
  - docker compose
  - open source
  - tower
---

Since yesterday's announcement that [Ansible had released the code behind Ansible Tower, AWX, under an open source license](//www.jeffgeerling.com/blog/2017/ansible-open-sources-ansible-tower-awx), I've been working on an [AWX Ansible role](http://galaxy.ansible.com/geerlingguy/awx/), a demo [AWX Vagrant VM](https://github.com/geerlingguy/ansible-vagrant-examples/tree/master/awx), and an [AWX Ansible Container project](https://galaxy.ansible.com/geerlingguy/awx-container/).

As part of that last project, I have published two public Docker Hub images, [`awx_web`]() and [`awx_task`](), which can be used with a `docker-compose.yml` file to build AWX locally in about as much time as it takes to download the Docker images:

    curl -O https://raw.githubusercontent.com/geerlingguy/awx-container/master/docker-compose.yml
    docker-compose up -d

After `docker-compose` is finished, wait a couple minutes for the initial database migration to run, then you should be able to access AWX at `http://localhost/` (the default login is `admin`/`password`):

{{< figure src="./awx-dashboard-startup.png" alt="Ansible AWX Dashboard - after initialization - with Angry Potato" width="650" height="427" class="insert-image" >}}

You can find out all the details as to how this works, and how you can build the Docker images _yourself_ using Ansible Container in the project repository: [AWX (Built with Ansible Container)](https://github.com/geerlingguy/awx-container).
