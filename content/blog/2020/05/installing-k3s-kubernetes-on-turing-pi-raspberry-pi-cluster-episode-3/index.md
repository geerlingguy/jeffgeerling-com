---
nid: 3010
title: "Raspberry Pi Cluster Episode 3 - Installing K3s Kubernetes on the Turing Pi"
slug: "installing-k3s-kubernetes-on-turing-pi-raspberry-pi-cluster-episode-3"
date: 2020-05-21T15:01:23+00:00
drupal:
  nid: 3010
  path: /blog/2020/installing-k3s-kubernetes-on-turing-pi-raspberry-pi-cluster-episode-3
  body_format: markdown
  redirects:
    - /blog/2020/pi-cluster-episode-3-installing-k3s-kubernetes-on-turing-pi
aliases:
  - /blog/2020/pi-cluster-episode-3-installing-k3s-kubernetes-on-turing-pi
tags:
  - ansible
  - cluster
  - k3s
  - kubernetes
  - raspberry pi
  - turing pi
  - video
  - youtube
---

> This is the third video in a series discussing cluster computing with the Raspberry Pi, and I'm posting the video + transcript to my blog so you can follow along even if you don't enjoy sitting through a video :)

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/N4bfNefjBSw" frameborder='0' allowfullscreen></iframe></div>

In the [first episode](/blog/2020/raspberry-pi-cluster-episode-1-introduction-clusters), I talked about how and why I build Raspberry Pi clusters like the [Raspberry Pi Dramble](https://www.pidramble.com). In the [second episode](/blog/2020/raspberry-pi-cluster-episode-2-setting-cluster), I spoke about how to put everything together in a [Turing Pi](https://turingpi.com) cluster and get the [Raspberry Pi Compute Modules](https://www.raspberrypi.org/products/compute-module-3-plus/) ready to boot.

In this episode, I'm going to show you how to find and connect to all the Raspberry Pis, then how to install [Kubernetes](https://kubernetes.io) on the Turing Pi cluster.

## Find your Pis

When I flashed all the Compute Modules with Hypriot OS, I set a unique hostname for each Pi, like `master`, `worker-01`, and `worker-02`.

I didn't just do that for fun; it helps me find them on my network, when I boot them up and plug the Turing Pi into the network. It also helps me associate the Pi's IP addresses with their hostnames, which may come in handy later.

After you plug in the Turing Pi, you have to wait a few minutes for all the Pis to fully boot. The first boot can take a while, because Hypriot or even Raspbian has to do a bit of housekeeping the first time it boots up. Usually, you'll know the Pis are booted when the red activity LED next to each board is mostly 'off' instead of 'on'. Once booted, assuming you have the Turing Pi plugged into your network, you can go to another Mac or Linux computer on the _same network_ and run the following command:

    nmap -sn 10.0.100.1/24 | grep 'turing\|worker'

In this command, I'm calling the `nmap` utility, which is a utility used for Network Mapping. I'm telling it to look for any devices with IP addresses in the same range as my main network. For _my_ network, the network ID and subnet mask is `10.0.100.1/24`. Your own network is probably different, like `192.168.0.1/24`. You can find out your own ID and mask using `ifconfig` on a Mac, or `ip a` on most Linux machines.

If you run this command without the `grep`, then it will return a list of _all_ the devices on your network, including the seven Pis installed in the Turing Pi! Because I piped the output through `grep`, though, I could easily filter the list to just get the worker Pis and the master pi.

I can grab their IP addresses from the list, noting which IP corresponds to which hostname, for example: `worker-03` is `10.0.100.197`, and `turing-master` is `10.0.100.163`.

I can then use `ssh` to log into each server, using either their hostname or their IP addresses, and verify I can connect successfully. You will probably have to accept the new host key for each server as you connect to it. Type `yes` and press enter to accept the host key. The [host key](https://www.ibm.com/support/knowledgecenter/SSLTBW_2.2.0/com.ibm.zos.v2r2.foto100/hostch.htm) is used so your computer can verify it's connecting to the same server every time, and not an imposter that's trying to steal your data.

Once you connect to one of the Pi servers, you can explore if you want, or type `exit` to get back to the command line and test the connection to the next server.

Once you confirm all the servers are running and able to be accessed, it's finally time to install Kubernetes!

## Introduction to Kubernetes

But let's not get ahead of ourselves! We have all these Pis running, but I'd forgive you if you're a little like the kid in the Incredibles:

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/QFsFiDRwPqc" frameborder='0' allowfullscreen></iframe></div>

Just like with a single Pi, there are seemingly infinite possibilities with a cluster of Raspberry Pis. But we need some software to make it easier to run applications on the cluster without having to log into each Pi all the time.

And one bit of clustering software that's become extremely popular is Kubernetes.

But... what the heck is _Kubernetes_. Well, I put together this little animation for a presentation I did last year at [Flyover Camp](https://www.flyovercamp.org) in Kansas City, Missouri.

At the very basic level, you have applications you want to run, like a web CMS, a database, a chat system, search, and redis caching. And then you have a bunch of servers—in this case, Raspberry Pis—that you want to run things on:

{{< figure src="./kubernetes-explainer-slide-1.png" alt="Kubernetes Explainer Slide 1 - Applications and Servers" width="650" height="auto" class="insert-image" >}}

Kubernetes takes those applications, and gets them running on your servers, and then keeps them running on your servers, even when there's trouble.

{{< figure src="./kubernetes-explainer-slide-2.png" alt="Kubernetes Explainer Slide 2 - Kubernetes Puts Apps on Servers" width="650" height="auto" class="insert-image" >}}

That's about the most basic description possible, because Kubernetes can do a whole lot more, and can be very complicated for large scale clustering. But for basic needs, Kubernetes isn't as daunting as you might think.

## Picking the right flavor of Kubernetes

So let's install Kubernetes!

Simple, right? We'll just go to the [Kubernetes website](https://kubernetes.io), download it, and install it. Easy peasy, all done.

Well, not so fast. As with all things in life, installing Kubernetes can be a little bit complicated, mainly because there are many different flavors of Kubernetes you can install. Each one has its own benefits and drawbacks, just like with different Raspberry Pi OSes like Raspbian and HypriotOS.

There are large scale, enterprise Kubernetes flavors, like [OpenShift](https://www.openshift.com) or the full [Kubernetes](https://kubernetes.io) stack. And there are more lightweight, trimmed down Kubernetes flavors, like [K3s](https://k3s.io) by Rancher, or [MicroK8s](https://microk8s.io), by Canonical. And these are only a few of the many options.

The full Kubernetes installation runs on a Raspberry Pi—but just barely. I've run it on my clusters, and found that sometimes Kubernetes would start failing on Pis that only had one gigabyte of memory, like the Compute Modules do. And all the services that run with a full Kubernetes installation take a toll on a mobile CPU like the one in the Raspberry Pi.

A distribution of Kubernetes like OpenShift has a ton of great features for usability, but it comes at a cost: at a minimum, you need three master servers running with _16 GB_ of RAM each! Not gonna happen with our little Pis.

MicroK8s and K3s both run on lighter weight hardware, but K3s focuses more on the extreme end of 'lightweight', and is easier to set up with more advanced configurations for HA, or 'high availability'.

And then when you finally choose a distribution of Kubernetes, you realize there are dozens of ways to actually install it. You could use [`kubeadm`](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/) on the command line to set up a cluster, or you could use the [AWS CLI](https://docs.aws.amazon.com/eks/latest/userguide/create-cluster.html) to build an Amazon EKS cluster. You could install a cluster with [Terraform](https://www.terraform.io) or [Ansible](https://www.ansible.com), or run something like [Kubespray](https://kubespray.io/)!

If it seems like there's a lotta similar options when you research things with Kubernetes, well, it's because there are. There are often too many ways, in my opinion, to do something with Kubernetes, and it can be overwhelming! Just look at all the tools highlighted by the Cloud Native Computing Foundation (which maintains Kubernetes) in the [Cloud Native Landscape](https://landscape.cncf.io).

In our case, I'm sticking with K3s. It runs great on Raspberry Pis and installs really fast.

So let's go the K3s website and work on getting it set up.

## Installing K3s on the Turing Pi

Some people might go and run some random shell script off the Internet to install K3s. But we're a little more advanced than that. Instead of blindly running a complex bash script, I like to know what's happening.

I also hate doing things more than once. So I use Ansible, which is the easiest way to maintain automated processes to manage my servers.

And lucky for me, Rancher has a [fully functional Ansible playbook](https://github.com/rancher/k3s-ansible) that builds a Kubernetes cluster with K3s!

You just need to download or clone the `k3s-ansible` repository, modify the playbook inventory, and run it:

  1. Download using the 'Download ZIP' link on GitHub on [https://github.com/rancher/k3s-ansible](https://github.com/rancher/k3s-ansible)
  2. Edit the Ansible inventory file `inventory/hosts.ini`, and replace the examples with the IPs or hostnames of your master and nodes. This file describes the K3s masters and nodes to Ansible as it installs K3s.
  4. Edit the `inventory/group_vars/all.yml` file and change the `ansible_user` to `pirate`.
  3. Run `ansible-playbook site.yml -i inventory/hosts.ini` and wait.

To connect to the cluster, once it's built, you need to grab the `kubectl` configuration from the master:

    scp pirate@turing-master:~/.kube/config ~/.kube/config-turing-pi

Make sure you have `kubectl` installed on your computer (you can install it following [these directions](https://kubernetes.io/docs/tasks/tools/install-kubectl/)).

Then set the `KUBECONFIG` environment variable, and start running `kubectl` commands:

    export KUBECONFIG=~/.kube/config-turing-pi
    kubectl get nodes

You should get a list of all the Pi servers; if you do, congratulations! Your cluster is up and running, ready to run workloads!

## Resetting K3s

If you mess anything up in your Kubernetes cluster, and want to start fresh, the K3s Ansible playbook includes a `reset` playbook, that you can run from the same directory. Just run:

    ansible-playbook reset.yml -i inventory/hosts.ini

I like to make a habit of resetting the entire cluster from time to time, just to make sure I've automated every application deployment into the cluster, but that's a topic for another day!

## Shutting down the Turing Pi Cluster

Instead of just unplugging the Turing Pi, it's best to safely shut down all the Raspberry Pis. Instead of logging into each Pi and running the `shutdown` command, you can use Ansible, since it already knows how to connect to all the Pis. Just run this command:

    ansible all -i inventory/hosts.ini -a "shutdown now" -b

Ansible will report failure for each server since the server shuts down and Ansible loses the connection, but you should see all the Pis power off after a minute or so. Now it's safe to unplug the Turing Pi.

## Conclusion

So now we have a running Kubernetes cluster. That's great! But again, we come back to the question, what can we do with it?

Well, for that, you'll have to wait for the next episode, where I'll deploy some applications to the cluster and show you some of the amazing things you can do with the Turing Pi cluster running K3s!

Make sure you [subscribe to my YouTube channel](https://www.youtube.com/c/JeffGeerling) so you don't miss the next episode.

If there's anything I missed or questions you have about the Turing Pi and clustering, please feel free to ask in the comments below.
