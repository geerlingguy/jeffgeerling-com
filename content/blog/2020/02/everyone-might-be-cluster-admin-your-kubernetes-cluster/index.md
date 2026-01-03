---
nid: 2971
title: "Everyone might be a cluster-admin in your Kubernetes cluster"
slug: "everyone-might-be-cluster-admin-your-kubernetes-cluster"
date: 2020-02-27T21:51:32+00:00
drupal:
  nid: 2971
  path: /blog/2020/everyone-might-be-cluster-admin-your-kubernetes-cluster
  body_format: markdown
  redirects: []
tags:
  - k8s
  - kubernetes
  - rbac
  - roles
  - security
---

Quite often, when I dive into someone's Kubernetes cluster to debug a problem, I realize whatever pod I'm running has _way_ too many permissions. Often, my pod has the `cluster-admin` role applied to it through its default ServiceAccount.

Sometimes this role was added because someone wanted to make their CI/CD tool (e.g. Jenkins) manage Kubernetes resources in the cluster, and it was easier to apply `cluster-admin` to a default service account than to set all the individual [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) privileges correctly. Other times, it was because someone found a new shiny tool and blindly installed it.

One such example I remember seeing recently is the [spekt8](https://github.com/spekt8/spekt8) project; in it's installation instructions, it tells you to apply an rbac manifest:

    kubectl apply -f https://raw.githubusercontent.com/spekt8/spekt8/master/fabric8-rbac.yaml

What the installation guide doesn't tell you is that this manifest grants `cluster-admin` privileges to _every single Pod in the default namespace_!

At this point, a more naive reader (and I mean that in the nicest way—Kubernetes is a complex system and you need to learn a lot!) might say: "All the Pods I run are running trusted applications and I know my developers wouldn't do anything nefarious, so what's the big deal?"

The problem is, if any of your Pods are running _anything_ that could potentially result in code execution, it's trivial for a bad actor to script the following:

  1. Download `kubectl` in a pod
  2. Execute a command like:


```
kubectl get ns --no-headers=true | sed "/kube-*/d" | sed "/default/d" | awk '{print $1;}' | xargs kubectl delete ns
```

If you have your RBAC rules locked down, this is no big deal; even if the application inside the Pod is fully compromised, the Kubernetes API will deny any requests that aren't explicitly allowed by your RBAC rules.

However, if you had blindly installed `spekt8` in your cluster, you would now have no namespaces left in your cluster, besides the default namespace.

## Try it yourself

I created a little project called [k8s-pod-rbac-breakout](https://github.com/geerlingguy/k8s-pod-rbac-breakout) that you can use to test whether your cluster has this problem—I typically deploy a script like this [58-line index.php](https://github.com/geerlingguy/k8s-pod-rbac-breakout/blob/master/index.php) script to a Pod running PHP in a cluster and see what it returns.

You'd be surprised how many clusters give me all the info and no errors:

{{< figure src="./rbac-breakout-page-example.png" alt="RBAC Breakout page example" width="650" height="456" class="insert-image" >}}

Too many Kubernetes users build snowflake clusters and deploy tools (like `spekt8`—though there are _many_, many others) into them with no regard for security, either because they don't understand Kubernetes' RBAC model, or they needed to meet a deadline.

If you ever find yourself taking shortcuts to get past pesky `User "system:serviceaccount:default:default" cannot [do xyz]` messages, think twice before being promiscuous with your cluster permissions. And consider automating your cluster management (I'm writing a [book](https://www.ansibleforkubernetes.com) for that) so people can't blindly deploy insecure tools and configurations to it!
