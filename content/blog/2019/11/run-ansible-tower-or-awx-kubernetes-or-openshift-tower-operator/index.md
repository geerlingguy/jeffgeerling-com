---
nid: 2952
title: "Run Ansible Tower or AWX in Kubernetes or OpenShift with the Tower Operator"
slug: "run-ansible-tower-or-awx-kubernetes-or-openshift-tower-operator"
date: 2019-11-26T15:29:54+00:00
drupal:
  nid: 2952
  path: /blog/2019/run-ansible-tower-or-awx-kubernetes-or-openshift-tower-operator
  body_format: markdown
  redirects: []
tags:
  - ansible
  - automation
  - awx
  - kubernetes
  - openshift
  - operator
  - tower
---

> **Note**: Please note that the Tower Operator this post references is currently in early alpha status, and has _no_ official support from Red Hat. If you are planning on using Tower for production and have a Red Hat Ansible Automation subscription, you should use one of the [official Tower installation methods](https://docs.ansible.com/ansible-tower/latest/html/quickinstall/index.html). Someday the operator may become a supported install method, but it is _not_ right now.

I have been building a variety of Kubernetes Operators using the [Operator SDK](https://github.com/operator-framework/operator-sdk). Operators make managing applications in Kubernetes (and OpenShift/OCP) clusters very easy, because you can capture the entire application lifecycle in the Operator's logic.

{{< figure src="./awx-tower-operator-sdk-screenshot.png" alt="AWX Tower Operator SDK built with Ansible for Kubernetes" width="650" height="470" class="insert-image" >}}

[Ansible Tower](https://www.ansible.com/products/tower) is a central system for Ansible automation scheduling and inventory management, with robust RBAC and many other useful features for managing automation tasks for teams. [AWX](https://github.com/ansible/awx) is the open source upstream project where Tower's bleeding-edge development takes place. The relationship between the two is similar to Fedora (the less stable open source upstream which requires no license to use) and Red Hat Enterprise Linux (which is more stable and requires a license).

I am working on an [Ansible Tower/AWX Operator](https://github.com/geerlingguy/tower-operator) for Kubernetes which makes installing and managing instances of Tower _or_ AWX in your Kubernetes clusters easy.

## Why an Operator?

Since there's already an [install playbook](https://docs.ansible.com/ansible-tower/latest/html/quickinstall/download_tower.html) for Ansible Tower [on Kubernetes or OpenShift](https://docs.ansible.com/ansible-tower/latest/html/administration/openshift_configuration.html#ag-openshift-configuration), why would there be a need for an Operator that does the same thing? There are a few good reasons:

  - There equivalent installation playbook for AWX is a little different than the one that ships with Tower, so it can be hard to see where things differ between the two systems.
  - The [Operator pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) is the most Kubernetes-native way to manage complex applications like Tower.
  - Operators do more than just install and reconfigure applications; they can manage backups, upgrades, and even more, and they do it in real-time, all the time.

To the last point, the Operator doesn't yet manage the full lifecycle of Tower—it just does installation, configuration, and updates—but over time the hope is the Operator can do more and make it easy for you to concentrate on using Tower, not managing it.

## Using the Operator

The Operator requires a Kubernetes cluster; if you just want to try it out, the best way to get a Kubernetes cluster locally is to [Install Minikube](https://minikube.sigs.k8s.io/docs/start/), then start a Minikube instance:

    $ minikube start --memory 6g --cpus 4

After a few minutes, you should have a Kubernetes environment running (and you'll probably know it by the sound of your computer's fans revving up!). Now it's time to install the Tower Operator, which is done by applying its manifest:

    $ kubectl apply -f https://raw.githubusercontent.com/geerlingguy/tower-operator/master/deploy/tower-operator.yaml

After you run this command, you should be able to see the Tower Operator running in your Kubernetes cluster:

```
$ kubectl get pods
NAME                             READY   STATUS    RESTARTS   AGE
tower-operator-894f44fdb-wfrkv   2/2     Running   0          92s
```

To create an instance of Ansible Tower, create a manifest file for it named `tower.yml`, with the following contents:

```
---
apiVersion: tower.ansible.com/v1alpha1
kind: Tower
metadata:
  name: tower
  namespace: tower
spec:
  tower_hostname: tower.test
  tower_secret_key: aabbcc
  
  tower_admin_user: admin
  tower_admin_email: admin@example.com
  tower_admin_password: changeme
```

> If you want to install AWX instead of Tower, add the following two variables in `spec` to override the default Tower images:
>
> ```
> tower_task_image: ansible/awx_task:9.0.1
> tower_web_image: ansible/awx_web:9.0.1
> ```

Create the namespace for your Ansible Tower instance:

    $ kubectl create namespace tower

Run the following command to deploy this instance of Ansible Tower into your cluster:

    $ kubectl apply -f tower.yml

At this point, the Tower Operator will notice the existence of this new Tower resource, and then it will start setting it up in the `tower` namespace. You can watch as the Tower pods are brought up:

    $ watch kubectl get pods -n tower

After a few minutes, you should see a number of pods running Postgres, RabbitMQ, Memcached, Tower, etc. After they are in `Running` status, Tower should be functional and responding to web requests. To access tower from your browser, you will need to make sure Minikube is exposing it at the `tower_hostname` you defined earlier. To do that, enable the `ingress` addon in Minikube:

    $ minikube addons enable ingress

Then you need to get the IP address of the Minikube environment:

    $ minikube ip

And [edit your hosts file](https://support.rackspace.com/how-to/modify-your-hosts-file/) (usually `/etc/hosts`), adding a line like the following:

    MINIKUBE_IP_HERE  tower.test

Finally, go into your web browser and open up [http://tower.test/](http://tower.test/). On its first run (or after a version upgrade, when database migrations are running), you may see the "Tower is upgrading..." screen:

{{< figure src="./ansible-tower-is-upgrading.png" alt="Ansible Tower is Upgrading screenshot" width="650" height="450" class="insert-image" >}}

After the database migrations are complete, you should be redirected to the login screen:

{{< figure src="./ansible-tower-login-screen.png" alt="Ansible Tower login screen" width="650" height="450" class="insert-image" >}}

At this point, you can log in using the credentials in the Tower resource spec (in the example above, `admin` for username and `changeme` for password), and start using Tower! Note that use of Tower requires a license—you can [get a free trial license here](https://docs.ansible.com/ansible-tower/latest/html/installandreference/updates_support.html#trial-evaluation) if you're evaluating Tower. If you use AWX, you will not be prompted for a license.

## What the future holds

This operator was built using Ansible and the Operator SDK; so it's installing Ansible Tower on Kubernetes by running Ansible in an Operator on Kubernetes! Using Ansible for the operator makes it easy for anyone—not just Go developers—to build Kubernetes-native automation. I've written more about this in my book, [Ansible for Kubernetes](https://www.ansibleforkubernetes.com), which should be available soon.

There are a number of improvements I hope to make in the Tower operator (see the [Tower operator issue queue](https://github.com/geerlingguy/tower-operator/issues)), to make it more robust and helpful for those who want to manage one or more instance of Tower or AWX in a Kubernetes or OpenShift cluster. I also hope to get the operator listed on [OperatorHub.io](https://operatorhub.io), and to see if I can grow it to become a supported installation method for Ansible Tower.

But even if not, the operator is a good example of the possibilities of Ansible-based operators in Kubernetes!
