---
nid: 2911
title: "Monitoring Kubernetes cluster utilization and capacity (the poor man's way)"
slug: "monitoring-kubernetes-cluster-utilization-and-capacity-poor-mans-way"
date: 2019-02-28T15:39:32+00:00
drupal:
  nid: 2911
  path: /blog/2019/monitoring-kubernetes-cluster-utilization-and-capacity-poor-mans-way
  body_format: markdown
  redirects: []
tags:
  - cluster
  - dramble
  - k8s
  - kubernetes
  - monitoring
  - pi dramble
---

If you're running Kubernetes clusters at scale, it pays to have good monitoring in place. Typical tools I use in production like Prometheus and Alertmanager are extremely useful in monitoring critical metrics, like "is my cluster almost out of CPU or Memory?"

But I also have a number of smaller clusters—some of them like my [Raspberry Pi Dramble](http://www.pidramble.com) have very little in the way of resources available for hosting monitoring internally. But I still want to be able to say, at any given moment, "how much CPU or RAM is available inside the cluster? Can I fit more Pods in the cluster?"

So without further ado, I'm now using the following script, which is slightly adapted from a script found in the Kubernetes issue [Need simple kubectl command to see cluster resource usage](https://github.com/kubernetes/kubernetes/issues/17512#issuecomment-367212930):

<script src="https://gist.github.com/geerlingguy/b35e80ca2c72e8f90e0e2963d7f1d2e5.js"></script>

Usage is pretty easy, just make sure you have your kubeconfig configured so `kubectl` commands are working on the cluster, then run:

```
$ ./k8s-resources.sh 
hostname1: 23% CPU, 16% memory
hostname2: 26% CPU, 16% memory
hostname3: 38% CPU, 22% memory
hostname4: 98% CPU, 66% memory
hostname5: 29% CPU, 18% memory
hostname6: 28% CPU, 16% memory
Average usage: 40% CPU, 25% memory.
```

If I get some time I might make a few more modifications to allow more detailed stats. Also, there are a dozen or so other scripts and utilities you can run to get more detailed stats. But for my purposes, I am quite often setting up a small cluster, running a number of apps on it, then checking what kind of resource allocation pattern I'm getting. This helps tremendously in finding the optimal instance type on AWS, or whether I need more instances or could live with fewer.

Someday hopefully `kubectl`/Kubernetes will include some way of finding this information more simply. But for now, there's scripts like the above one!
