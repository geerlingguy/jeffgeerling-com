---
nid: 2851
title: "Kubernetes' Complexity"
slug: "kubernetes-complexity"
date: 2018-06-15T03:06:35+00:00
drupal:
  nid: 2851
  path: /blog/2018/kubernetes-complexity
  body_format: markdown
  redirects: []
tags:
  - automation
  - cluster
  - dramble
  - hosting
  - infrastructure
  - k8s
  - kube
  - kubernetes
  - pi dramble
  - raspberry pi
---

Over the past month, I started rebuilding the [Raspberry Pi Dramble](http://www.pidramble.com) project using Kubernetes instead of installing and configuring the LEMP stack directly on nodes via Ansible ([track GitHub issues here](https://github.com/geerlingguy/raspberry-pi-dramble/issues?q=is%3Aissue+label%3Akubernetes+)). Along the way, I've hit tons of minor issues with the installation, and I wanted to document some of the things I think turn people away from Kubernetes early in the learning process. Kubernetes is definitely not the answer to all application hosting problems, but it is a great fit for some, and it would be a shame for someone who could really benefit from Kubernetes to be stumped and turn to some other solution that costs more in time, money, or maintenance!

{{< figure src="./raspberry-pi-dramble-cluster-green-led-kubernetes.jpg" alt="Raspberry Pi Dramble cluster running Kubernetes with Green LEDs" width="520" height="334" class="insert-image" >}}

<p style="text-align: center;"><em>The <a href="http://www.pidramble.com">Raspberry Pi Dramble</a> cluster; a green LED indicates the node is <code>Ready</code>.</em></p>

I wanted to write this blog post while I'm in the middle of learning and implementing my first 'prod ready' Kubernetes cluster. If I wait until the end, I'll forget many of the hurdles I've encountered. One of the reasons [Ansible for DevOps](https://www.ansiblefordevops.com) resonates with beginners is the book started as my own notes written _while learning Ansible myself!_—It's a lot harder to understand the beginner's perspective if you write about a subject after you've mastered it (though in truth, the more you know, often the more [you feel you _don't know_](https://en.wikipedia.org/wiki/Impostor_syndrome)!).

## Hello World (Minikube)

Every software project should have a "here's how you can get this thing running and start poking at it in 5 minutes" intro. I have spent a lot of time helping in the Drupal community with our (currently pretty abysmal) onboarding/first touch experience... and it's improved quite a bit! But especially for open source software, it can be hard to have a great, simple, reliable onboarding experience when you have to hit a moving target, and when few of the core developers spend time working with the 'beginner level' tooling.

A year or so ago, I remember trying out Minikube on my Mac and running into problem after problem. It worked okay on Linux, but the experience running it through a VirtualBox VM in any kind of non-cookie-cutter networking environment meant you spent more time fighting Minikube than tinkering with Kubernetes.

Luckily, the situation has improved quite a bit, and I was able to run through the [Hello Minikube](https://kubernetes.io/docs/tutorials/hello-minikube/) tutorial pretty quickly, with no errors (but a few warnings) on my Mac, using `xhyve` as the VM driver that runs Minikube.

But the abstractions quickly become painful, as you realize that much of the Kubernetes documentation applies to larger clusters, and won't work correctly in a Minikube environment... or some of the things you learn while testing in Minikube don't apply to real-world Kubernetes clusters (e.g. almost every blog post I've ever seen that assumes you're running everything on a single 'master' node or inside Minikube!).

I think it was Larry Wall who put it best, "make the easy things easy, and the hard things possible"—the problem is, the easy things can sometimes feel impossible once you break out of Minikube and work with a multi-node Kubernetes cluster! (Later though, I'll follow up to mention that once you grasp certain concepts, the hard things can sometimes become _easy_, and that's part of the magic of Kubernetes!)

## To Swap or Not to Swap

The first snag I hit in almost every environment when either installing Kubernetes via `kubeadm` or running `kubelet` is the deluge of error messages that occurs when you have swap enabled on a VM. For years, I've always sized cloud VMs so they are cost-effective: just enough RAM for a working set of applications, with a little headroom, then maybe 512 MB or 1 GB of swap space, for those times when some idiotic Java app wants to grab a little extra.

If I had unlimited money, I would double the RAM on every server I purchase... but as it is, I'd rather be a little conservative and save half the cost.

Anyways, [I'm not the only one with this opinion](https://github.com/kubernetes/kubernetes/issues/53533), and though GCE, Azure, and AWS would love for everyone to just buy the next instance tier up, it seems like allowing swap (but still maybe throwing one warning on install that performance may not be _optimal_) would be a much more developer-friendly default.

Almost every new environment I build, I forget about the default swap restriction, so I have to decide whether to use the `--fail-swap-on` option or not. Unless there's proof that swap is always and everywhere a huge issue with Kubernetes, I don't think it should be so strict about wanting swap off. Especially when, in some environments (like a Docker container) it can be much more difficult to manage swap in a way Kubernetes likes.

## Documentation

Kubernetes' documentation has improved quite a bit in the past year... but has a very long way to go before I would call it 'user-friendly'. The problem is not depth—there's plenty of that! Rather, the main problem I have is the non-working examples littered throughout.

The problem here is that getting real-world Kubernetes infrastructure running still requires some provider-specific bits, and implementations can vary from provider to provider. Much of the documentation (especially any older examples) assume you're running a cluster on Google Cloud (whether it's explicitly stated or not), while other guides have separate sections for Google Cloud, AWS, Minikube, Azure, bare metal, and even other providers.

This gets to be especially thorny when dealing with things like ingress controllers, load balancers, and any other method of getting traffic _into_ a Kubernetes cluster. It's fairly easy to follow docs run a bunch of pods via deployments, stateful sets, daemon sets, or jobs on nodes—when you don't need to allow external access to the applications running on those pods. It needs to get easier to make sure that examples work everywhere, especially in Minikube and bare metal deployments, because this is often where people will tinker if they don't already have a corporate account with a major hosting provider.

There's also the problem of blog posts—many of which are severely outdated if posted before 2017—which are misleading, incomplete, or have terrible example code, poorly explained. But this problem can only really be overcome with time. Drupal 8's release had the same issue for the first year or so; it takes time for people to adopt the most recent and efficient Kubernetes features, then write comprehensive guides to how they did it.

## "Just grab this Helm chart"

Speaking of blog posts (and many forum topics), all to often I see someone ask about a specific feature or attribute that's giving them trouble, to which someone replies "oh, there's a Helm chart for that; just run it!"

There are three issues I have with the 'use Helm at the start' technique:

  1. It masks a lot of the primitives that someone starting out with Kubernetes should be learning.
  2. Helm is an additional tool that must be installed on top of Kubernetes.
  3. It can (and maybe will) lead to the first 'leftpad moment' for the containerized infrastructure movement.

Regarding the third point, if you don't know, the [leftpad debacle](https://arstechnica.com/information-technology/2016/03/rage-quit-coder-unpublished-17-lines-of-javascript-and-broke-the-internet/) was what happened when the publisher of the Node.js NPM 'leftpad' library decided to delete his library... and break the builds of hundreds of thousands of Node apps.

If we tell people to grab a Helm chart and/or copy and paste random Kubernetes manifests with forked (or heck, even library) Docker images, we're effectively telling them to run arbitrary code completely outside their control or any formal, vetted build process, inside their clusters. If that doesn't scare you, you should probably not be managing any production infrastructure.

Even if you stick to library or 'official' Docker images, there are often changes in them which can, at best, cause a bit of churn (e.g. when the PHP library image decided to upgrade all images to use Debian Stretch instead of Jessie recently). At worst, a malicious party could inject code into the image that gets automatically deployed to all your servers next time your Pods are replaced!

> While writing this post, an article showing evidence of this exact problem in the wild was published by Kromtech: [Cryptojacking invades cloud. How modern containerization trend is exploited by attackers](https://kromtech.com/blog/security-center/cryptojacking-invades-cloud-how-modern-containerization-trend-is-exploited-by-attackers). Don't run untrusted code on your infrastructure!

Helm can be a great aid to Kubernetes deployments, but 'library' Helm charts should most often be relegated to test or learning use, not necessarily recommended for production.

> Note: This early in my Kubernetes learning experience, I've only barely used Helm... so my thoughts may be a bit biased and I'm willing to change my mind.

## Single node vs Multi node

Many practical examples assume you're using Minikube (which is a single node Kubernetes deployment), and many blog posts seem to have only been tested on a single node Kubernetes cluster (Minikube or plain Kubernetes installed via `kubeadm`).

In real-world usage, you'll have more than one node—that's kind of the point of using Kubernetes. And in real-world usage, many if not most applications you'll run are not 100% 'container native', meaning there will need to be some form of networking, shared state, persistent data... and that means the nodes must be able to communicate in various ways:

  - The `kube-proxy` layer must be working
  - `kubectl` on the nodes must be advertising the correct network interface/IP so the Kubernetes master can communicate with it properly
  - NFS, Gluster, Ceph, or some other shared filesystem is often required
  - A CNI-compatible networking layer must be installed and working correctly
  - Many applications require local volumes, persistent volumes, or node affinity configuration for persistence

In general, these more complex scenarios are often glossed over in examples, and the documentation (especially surrounding non-Google Cloud, non-Azure, and non-AWS usage) is often a little thin, leaving the beginner down a winding path of blog posts, forum topics, and IRC chats to figure out how to put everything together for a truly node-agnostic, highly-available, performant application deployment.

These problems aren't that much easier in a traditional multi-server environment... but add on all the acronym soup of PVCs, PVs, LocalVolumes, NodePorts, CNI, LoadBalancers, Ingress, etc., and it can be a bit bewildering!

## Ingress

On the topic of Ingress—since this is one area which seems to have improved quite a bit in the past year, it seems many blog posts are outdated, which can lead to some confusion. Basically, one of my first questions with Kubernetes was "I'm building a web app. How can I get access to it from outside the cluster at webapp.mysite.com, in an automated, deployable manner?"

If you want to pay a monthly fee for a cloud load balancer and run Kubernetes inside a managed environment, you can use an external LoadBalancer and IngressController to route traffic for domains into the cluster. But if you're running your own cluster bare-metal, or without using (very expensive in large quantities) cloud LoadBalancers, you kind of have to figure out a lot of things on your own. And if you want high availability, you still need to manage a load balancer (e.g. Nginx, Traefik, etc.) on your own in front of the Kubernetes cluster! (At least, AFIACT).

I've been experimenting with both the official Nginx and Traefik Ingress Controller manifests, and both seem pretty decent for basic use cases, but go outside the mapping of single domains to services, or domains to application paths, and things can start getting complicated.

I'm hoping the initial complexity in wrapping my mind around the entire Ingress situation is just a problem of time—it looks like a lot of work went into improving the Ingress Controller interface and default implementations over the past year.

## Networking

Networking is complicated enough when you need to worry about IP allocation, physical links, routers, firewalls, WANs, VPNs, NAT, and other traditional networking primitives. Throw on the 'cloud layers' like VPCs, Security Groups, ELBs, EIPs, and Peering, and it's a complicated landscape.

Kubernetes requires an additional virtual networking layer on top of all this, so the nodes can communicate with each other, and with the master. But even here, there are different layers—there's `kube-proxy`, which manages relatively complex sets of `iptables`-based firewall rules to route traffic around the cluster, then there is the CNI layer, which requires the use of a tool like Flannel, Weave, Calico, etc. (all of which are likely completely new to a Kubernetes beginner). Finally, many examples and real-world configurations require other layers like cluster DNS or Ingress Controllers, which also affect how Kubernetes' networking model works.

I'm not suggesting that Kubernetes can make complex networking easy. On the contrary, once everything is set up, it makes pod-to-pod, and pod-to-outside networking _easier_ than most other cluster networking tools I've seen.

But it _is_ complex, and a lot of the documentation doesn't really take sides; for example, the first time I read through the [Cluster Networking](https://kubernetes.io/docs/concepts/cluster-administration/networking/#how-to-implement-the-kubernetes-networking-model) documentation, it felt like one of those design-by-committee docs, especially with the notice:

> The following networking options are sorted alphabetically - the order does not imply any preferential status.

The problem is, for documentation, there should be some sort of preference, even if it offends some random vendor who implemented CNI for their niche product. I've found Flannel or Weave are the typical choices for those starting out, or with the most general cloud-agnostic needs... but that was only after reading a ton more documentation than I'd like, as well as many forum topics and blog posts which were more opinionated—and thus more helpful.

Especially if there's a solution that's endorsed by the CNCF, it might be best to show some preferential treatment towards that tool, with a link off to the 'comprehensive list of all the tools'.

## Raspberry Pi

Admittedly, this is a super-niche complaint, but there are a number of examples which won't work on the default Raspberry Pi OS (Raspbian), due to its arm32 architecture. Additionally, the first time I tried to run Kubernetes on my Pi cluster, I found that Kubernetes itself wouldn't run unless pinned at a slightly older version; see [my gist comment here](https://gist.github.com/alexellis/fdbc90de7691a1b9edb545c17da2d975#gistcomment-2598596) for more details.

After getting over that hurdle, I found a number of containers used in examples would not start on my Pi cluster, and it took some digging (logging into the machine itself and debugging via `docker`) to figure out the base image didn't have any arm32-compatible build. Luckily, for most things there is a compatible build, or at least a way to build one myself if I need to.

But, it's something to keep in mind. Hopefully the situation gets a _lot_ better once Raspbian finally releases an arm64 variant.

## Positive impressions

I don't want people to come away from this post thinking I hate Kubernetes, or wouldn't recommend it. Rather, I deeply appreciate it for what it is. It is _not_ a tool I'd recommend to someone building a small to medium size web app or single website without already having huge scalability needs. But it is perfect for a few of my use cases, e.g. for PaaS products, or for hosting a large number of websites or SaaS services which may need to individually scale.

Some of the greatest benefits in my limited use:

  - Kubernetes feels as close to 'Infrastructure-as-Code' as I've ever seen—as long as you also have the automation in place to build and destroy the entire cluster, and do `etcd` disaster recoveries in an automated fashion!
  - Massively-scalable container management is easy—once you get past the first month or two learning nomenclature.
  - Infrastructure development and architecture becomes more standardized and efficient.
  - The complete production infrastructure stack can be replicated on baremetal, local VMs, other clouds, etc. This is huge for me, as I hate having to spin up separate (and expensive) complete sets of services to do some real 1:1 infrastructure testing.
  - Architecting for Kubernetes means my time spent learning is (mostly) cloud-agnostic, and applies to many more scenarios, including _on-premise_ 'private cloud' hosting.

## Summary

Kubernetes is a complex beast. Most of the complexity is necessary, but as someone starting out in the Kubernetes ecosystem, it can be very difficult to go from newbie to deploying a real production application, even in the best of circumstances. I hope some of the things I mentioned in this blog post may help others starting out, or inspire people authoring documentation to improve things for beginners (or even anyone!).

I recently rearchitected the entire infrastructure of [Hosted Apache Solr](https://hostedapachesolr.com), a SaaS tool I have been running for a decade. If I were building it today, with no legacy restrictions, I would've used Kubernetes to manage the containers without hesitation. As it stands, [I built kind of a hybrid system](https://www.jeffgeerling.com/blog/2018/hosted-apache-solrs-revamped-docker-based-architecture) which will hold me over until I am able to fix some legacy decisions which make it hard to integrate everything with Kubernetes.

The nice thing is, Kubernetes has improved dramatically since the first time I heard about it, and again since the first time I tried Minikube a year ago. The future looks very bright, and I'm excited to be working on a few new Kuberenetes-based projects this year. For one of them, I'm working on it completely in the open, so you can follow along in the [Raspberry Pi Dramble issue queue](https://github.com/geerlingguy/raspberry-pi-dramble/issues?q=label%3Akubernetes+).
