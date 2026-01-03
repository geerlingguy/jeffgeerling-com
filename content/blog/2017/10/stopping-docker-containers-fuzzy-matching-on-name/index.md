---
nid: 2816
title: "Stopping Docker containers via fuzzy matching on the name"
slug: "stopping-docker-containers-fuzzy-matching-on-name"
date: 2017-10-26T19:13:49+00:00
drupal:
  nid: 2816
  path: /blog/2017/stopping-docker-containers-fuzzy-matching-on-name
  body_format: markdown
  redirects: []
tags:
  - awk
  - command line
  - docker
  - garbage collection
  - grep
  - xargs
---

I recently needed to hack together a setup where Docker containers are spawned by an automated process, then later, a garbage collector runs and kills off all spawned containers. This is on a system where there could be anywhere from tens to hundreds of containers running at any given moment, and I needed traceability of different containers while they're running.

One of the easiest ways to have at-a-glance traceability is to have named containers, e.g. `spawned-worker-1`, `spawned-worker-2`, etc.

So if I do a `docker ps --format '{{.Names}}'`, I can get a full list of all running containers by name. And then if I want to filter that list to _only_ show me `spawned-worker-` prefixed container names, I can pipe the output through grep, awk, and xargs to use the container names in a Docker command, like so:

    docker ps --format '{{.Names}}' | grep "^spawned-worker-" | awk '{print $1}' | xargs -I {} docker stop {}

In this case, I'm stopping all containers with `spawned-worker-` as the start of the name.

There are other, better ways to manage a fleet of containers (Swarm, k8s, ECS, Rancher, etc.), but in this case, I needed something quick and dirty to spawn a bunch of containers, and I needed a job to clean them up at the end of a cycle. This works a treat!
