---
nid: 3081
title: "Ignore noisy logs with fluentd in EKS or other Kubernetes clusters"
slug: "ignore-noisy-logs-fluentd-eks-or-other-kubernetes-clusters"
date: 2021-03-16T21:04:18+00:00
drupal:
  nid: 3081
  path: /blog/2021/ignore-noisy-logs-fluentd-eks-or-other-kubernetes-clusters
  body_format: markdown
  redirects:
    - /blog/2021/skipping-noisy-logs-fluentd-eks-or-other-kubernetes-clusters
aliases:
  - /blog/2021/skipping-noisy-logs-fluentd-eks-or-other-kubernetes-clusters
tags:
  - eks
  - elasticsearch
  - fluentd
  - kubernetes
  - logging
  - optimization
---

Recently, I decided to use the [fluentd-kubernetes-daemonset](https://github.com/fluent/fluentd-kubernetes-daemonset) project to easily ship all logs from an EKS Kubernetes cluster in Amazon to an Elasticsearch cluster operating elsewhere.

The initial configuration worked great out of the box—just fill in details like the `FLUENT_ELASTICSEARCH_HOST` and any authentication info, and then deploy the RBAC rules and DaemonSet into your cluster, and you're off to the races (assuming your Elasticsearch instance is configured to allow access from the cluster!).

But once I did that, I noticed the brand new EKS cluster was sending **over 16,000 log messages per second** to Elasticsearch. Doing a tiny bit of analysis (not much was required, honestly), I found that over 98% of the logs were coming from two EKS-specific noisy containers, `efs-csi-node` and `ebs-snapshot-controller`.

Reading through the docs for the fluentd daemonset, I found the environment variable `FLUENT_CONTAINER_TAIL_EXCLUDE_PATH`, which can be used to specify Fluentd's `exclude_path` configuration. Using that variable, you can tell Fluentd to ignore any paths matching an array of strings.

So in my case, I added the following configuration to the DaemonSet, and all the noise died down (and my poor Elasticsearch cluster breathed a sigh of relief—this was the first of six K8s clusters I was about to start shipping longs from!):

```
---
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd
  ...
spec:
  ...
  template:
    spec:
      serviceAccount: fluentd
      serviceAccountName: fluentd
      containers:
      - name: fluentd
        image: fluent/fluentd-kubernetes-daemonset:v1-debian-elasticsearch
        env:
          - name:  FLUENT_ELASTICSEARCH_HOST
            value: "192.168.0.10"
          - name:  FLUENT_ELASTICSEARCH_PORT
            value: "9200"
          - name: FLUENT_ELASTICSEARCH_SCHEME
            value: "http"
          - name: FLUENT_ELASTICSEARCH_LOGSTASH_PREFIX
            value: "my-cluster"
          - name: FLUENT_CONTAINER_TAIL_EXCLUDE_PATH
            value: >
              [
              "/var/log/containers/efs-csi-node-*",
              "/var/log/containers/ebs-snapshot-controller-*"
              ]
```

Once a fluentd Pod starts up on one of the nodes, if you inspect the logs, you'll notice the config file then gets an entry like:

```
exclude_path [ "/var/log/containers/efs-csi-node-*", "/var/log/containers/ebs-snapshot-controller-*" ]
```

And you don't have to pay for many gigabytes of extra log storage!
