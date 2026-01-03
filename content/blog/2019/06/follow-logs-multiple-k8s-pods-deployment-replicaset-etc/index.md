---
nid: 2921
title: "Follow logs from multiple K8s Pods in a Deployment, ReplicaSet, etc."
slug: "follow-logs-multiple-k8s-pods-deployment-replicaset-etc"
date: 2019-06-18T22:01:55+00:00
drupal:
  nid: 2921
  path: /blog/2019/follow-logs-multiple-k8s-pods-deployment-replicaset-etc
  body_format: markdown
  redirects: []
tags:
  - debugging
  - k8s
  - kubectl
  - kubernetes
  - logging
---

For production applications running in containerized infrastructure (e.g. Kubernetes, ECS, Docker Swarm, etc.)—and even for more traditional infrastructure with multiple application servers (for horizontal scalability), it is important to have centralized, persistent logging of some sort or another.

Some services like the ELK/EFK stack, SumoLogic, and Splunk offer a robust feature set for full text searching, filtering, and 'log intelligence'. On the other end of the spectrum, you can use a simple aggregator like rsyslogd or CloudWatch Logs without a fancy system on top if you just need basic central log storage.

But when I'm debugging something in a Kubernetes cluster—especially something like an internal service which I may not want to have logging everything to a central logging system (for cost or performance reasons)—it's often helpful to see _all_ the logs from _all_ pods in a Deployment or Replication Controller at the same time.

You can always stream logs from a single Pod with the command:

    kubectl logs -f -n namespace pod-id-here

But what if there are 3 replicas of that Pod? There are some bash scripts and other utilities like [Kubetail](https://github.com/johanhaleby/kubetail) and [Stern](https://github.com/wercker/stern) that make it somewhat easy to do... but `kubectl` has a built-in feature that allows streaming of multiple Pods' logs to your local console. Assuming your Pods have a label associated with them (e.g. `app=myapp`), you can use that label to view logs from all Pods with the label in the namespace:

    kubectl logs -f -n namespace -l app=myapp

Now it will stream all the Pods' logs straight to your console.

> **Note**: If you get the error `error: you are attempting to follow 9 log streams, but maximum allowed concurency is 5`, then add the option `--max-log-requests N` to the end of the `kubectl logs` command, where `N` is the number of Pods in the replica set. If there is a very large number of Pods, though... it might not be a good idea to stream them all via `kubectl`.

Thanks to [this answer by Adrian Ng](https://stackoverflow.com/a/44448420) on Stack Overflow for pointing this feature out to me.
