---
nid: 2664
title: "Reintroducing the sanity of CM to container management"
slug: "reintroducing-sanity-cm-container-management"
date: 2016-06-24T21:57:01+00:00
drupal:
  nid: 2664
  path: /blog/2016/reintroducing-sanity-cm-container-management
  body_format: markdown
  redirects: []
tags:
  - ansible
  - ansible container
  - ansible for devops
  - docker
  - infrastructure
  - kubernetes
  - mesos
  - orchestration
---

Recently, Ansible introduced [Ansible Container](https://github.com/ansible/ansible-container), a tool that builds and orchestrates Docker containers.

While tools that build and orchestrate Docker containers are a dime a dozen these days (seriously... Kubernetes, Mesos, Rancher, Fleet, Swarm, Deis, Kontena, Flynn, Serf, Clocker, Paz, Docker 1.12+ built-in, not to mention dozens of PaaSes), many are built in the weirdly-isolated world of "I only manage containers, and don't manage other infrastructure tasks."

The cool thing about using Ansible to do your container builds and orchestration is that Ansible can also do your networking configuration. And your infrastructure provisioning. And your legacy infrastructure configuration. And on top of that, Ansible is, IMO, the best-in-class configuration management tool—easy for developers and sysadmins to learn and use effectively, and as efficient/terse as (but much more powerful than) shell scripts.

From Ansible Container's own [README](https://github.com/ansible/ansible-container#why-not-just-use-standard-docker-tools):

> A `Dockerfile` is not much more than a script with hand-crafted shell commands. We're well past the point where we should be managing build processes with manually maintained series of shell scripts. That's why we wrote Ansible in the first place, and this is just as applicable to containers.

Discounting the fact that there are dozens of other reasons you might want to use a tool outside the standard Docker ecosystem to configure your application containers, this alone is one of my biggest gripes with what I see most development-teams-turned-sysadmins doing: they take a shoddy system of manual build steps and shell scripts... and turn it into a shoddy system of manual infrastructure provisioning and Dockerfiles.

We can (and will, in time) do better. I think Ansible Container is a sort-of call to arms to get development teams who are building Docker containers (or any kind of containers) to reconsider their decision to codify their infrastructure with shell scripts and Dockerfiles, and consider using a more robust and purpose-built CM tool to build and maintain images. Even more exciting would be pairing Ansible's orchestration with NixOS' configuration approach to make infrastructure that's even simpler to define, update, and replicate.

> Note: I cover a basic use case of building and orchestrating Docker images using plain Ansible (without `ansible-container`) in my book, [Ansible for DevOps](http://www.ansiblefordevops.com/). You can also view two example playbooks for Docker + Ansible on GitHub: [Simple Docker/Ansible Example](https://github.com/geerlingguy/ansible-for-devops/tree/master/docker), [Ansible Vagrant profile for Docker](https://github.com/geerlingguy/ansible-vagrant-examples/tree/master/docker).
