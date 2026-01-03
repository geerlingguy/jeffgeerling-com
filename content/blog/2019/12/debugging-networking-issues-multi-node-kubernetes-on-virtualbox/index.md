---
nid: 2957
title: "Debugging networking issues with multi-node Kubernetes on VirtualBox"
slug: "debugging-networking-issues-multi-node-kubernetes-on-virtualbox"
date: 2019-12-18T16:10:53+00:00
drupal:
  nid: 2957
  path: /blog/2019/debugging-networking-issues-multi-node-kubernetes-on-virtualbox
  body_format: markdown
  redirects:
    - /k8s-cni-virtualbox
aliases:
  - /k8s-cni-virtualbox
tags:
  - calico
  - cni
  - debian
  - debugging
  - flannel
  - kubernetes
  - networking
  - ubuntu
  - vagrant
  - virtualbox
---

Since this is the third time I've burned more than a few hours on this particular problem, I thought I'd finally write up a blog post. Hopefully I find this post in the future, the fourth time I run into the problem.

What problem is that? Well, when I build a new Kubernetes cluster with multiple nodes in VirtualBox (usually orchestrated with Vagrant and Ansible, using my [geerlingguy.kubernetes](https://github.com/geerlingguy/ansible-role-kubernetes) role), I get everything running. `kubectl` works fine, all pods (including CoreDNS, Flannel or Calico, kube-apiserver, the scheduler) report `Running`, and everything in the cluster _seems_ right. But there are lots of strange networking issues.

Sometimes internal DNS queries work. Most of the time not. I can't ping other pods by their IP address. Some of the debugging I do includes:

  - Run through everything in the [Debug Services](https://kubernetes.io/docs/tasks/debug-application-cluster/debug-service/) documentation. Determine services are configured fine, and see that my service endpoint are registering correctly.
  - Run through everything in the [Debugging DNS Resolution](https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/) documentation. Determine DNS is not working fine, but hit the end of the rope when I've tried every solution under the sun, and determine host DNS is fine, and CoreDNS is configured correctly... it's just not getting results.

One of the things that finally tipped me off to the problem was debugging DNS.

I started a debug pod running busybox:

    $ kubectl run -i --tty --rm debug --image=busybox --restart=Never -- sh

Once it came up, I ran nslookup, but it said 'no servers could be reached':

    / # nslookup kubernetes.default
    ;; connection timed out; no servers could be reached

If I looked at the pod's `/etc/resolv.conf`, it seemed to be configured correctly:

    / # cat /etc/resolv.conf
    nameserver 10.96.0.10
    search default.svc.cluster.local svc.cluster.local cluster.local
    options ndots:5

But it couldn't reach CoreDNS running on `10.96.0.10`. Hmm. I also tried `ping [ip of another pod]` and couldn't ping any other pods. This pointed to a general networking issue on the cluster, because you should be able to ping other pods by IP address in the same namespace.

I could also enable logging in CoreDNS (by editing the DNS ConfigMap) and then monitor DNS logs with `kubectl logs -f -n kube-system -l k8s-app=kube-dns`, and I would sometimes see many messages like:

    2018/11/12 07:40:00 [ERROR] 2 AAAA: unreachable backend: read udp 192.168.18.1:36161->10.0.2.3:53: i/o timeout

Then I remembered a while back, while working on my local development environment for the [Raspberry Pi Dramble](https://www.pidramble.com) cluster, I encountered similar networking issues. And the problem is VirtualBox creates a number of virtual network interfaces. Flannel and Calico, at least, both pick the _first_ interface on a server, and use that to set up their own virtual networks. If they pick the default first VirtualBox network, they'll use a `10.0.2.x` network that's used for the default NAT interface (`enp0s3`), and not the external bridge interface you configure (in my case, 192.168.7.x, or `enp0s8` on Debian).

For Flannel, you need to edit the `kube-flannel-ds-amd64` DaemonSet, adding the cli option `- --iface=enp0s8` under the `kube-flannel` container spec.

For Calico, you need to edit the `calico-node` DaemonSet, adding the `IP_AUTODETECTION_METHOD` environment variable with the value `interface=enp0s8`.

After doing that, the networking should work correctly, and your Pods should be able to see each other. Your services (NodePorts, LoadBalancers, etc.) should also start magically working! Note that, even without this fix, iptables routes may be working correctly (they're configured via `kube-proxy`), so it may _look_ like a NodePort is open and ready, but you won't get a response if the CNI (Flannel, Calico, Weave) is not configured correctly for your cluster.

A few of the issues / resources that were also helpful in debugging this problem:

  - [Comment by @tmjd in "pod calico-node on worker nodes with 'CrashLoopBackOff'" thread](https://github.com/projectcalico/calico/issues/2720#issuecomment-511598371)
  - [Flannel Vagrant troubleshooting docs](https://github.com/coreos/flannel/blob/master/Documentation/troubleshooting.md#vagrant)
  - [@lalo's answer on Stack Exchange for 'configuring flannel to use non-default interface'](https://stackoverflow.com/questions/47845739/configuring-flannel-to-use-a-non-default-interface-in-kubernetes)

## Addendum

One other note: I'm using Debian 10 in this particular instance, and it uses nftables for the iptables backend... which is [not currently compatible with Kubernetes' network proxying setup](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#ensure-iptables-tooling-does-not-use-the-nftables-backend). So in addition to the Flannel/Calico CNI changes to use the correct interface, I had to set iptables to use `iptables-legacy` instead of nftables:

    sudo update-alternatives --set iptables /usr/sbin/iptables-legacy
    sudo update-alternatives --set ip6tables /usr/sbin/ip6tables-legacy

If using Fedora, you just need the first of those two commands. With Ansible, I used the `alternatives` module to make the changes.
