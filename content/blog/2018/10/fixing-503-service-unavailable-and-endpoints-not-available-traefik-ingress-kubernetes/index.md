---
nid: 2882
title: "Fixing '503 Service Unavailable' and 'Endpoints not available' for Traefik Ingress in Kubernetes"
slug: "fixing-503-service-unavailable-and-endpoints-not-available-traefik-ingress-kubernetes"
date: 2018-10-24T18:53:41+00:00
drupal:
  nid: 2882
  path: /blog/2018/fixing-503-service-unavailable-and-endpoints-not-available-traefik-ingress-kubernetes
  body_format: markdown
  redirects: []
tags:
  - debugging
  - infrastructure
  - ingress
  - k8s
  - kubernetes
  - service
  - traefik
---

In a Kubernetes cluster I'm building, I was quite puzzled when setting up Ingress for one of my applications—in this case, Jenkins.

I had created a `Deployment` for Jenkins (in the `jenkins` namespace), and an associated `Service`, which exposed port `80` on a `ClusterIP`. Then I added an `Ingress` resource which directed the URL `jenkins.example.com` at the `jenkins` `Service` on port 80.

Inspecting both the `Service` and `Ingress` resource with `kubectl get svc -n jenkins` and `kubectl get ingress -n jenkins`, respectively, showed everything seemed to be configured correctly:

```
$ kubectl get svc -n jenkins
NAME      TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
jenkins   ClusterIP   172.20.3.104   <none>        80/TCP    17m

$ kubectl get ing -n jenkins
NAME      HOSTS                                 ADDRESS   PORTS     AGE
traefik   jenkins.example.com                                   80        17m
```

But when I visited the URL, I would get a 503:

```
$ curl -I http://jenkins.example.com/
HTTP/1.1 503 Service Unavailable
Vary: Accept-Encoding
Date: Wed, 24 Oct 2018 18:23:42 GMT
Content-Length: 19
Content-Type: text/plain; charset=utf-8
```

The Traefik logs weren't all that helpful (I have Traefik running as a `DaemonSet`), but did point to some sort of disconnect between the `jenkins` `Service` and the `jenkins` `Deployment`:

```
$ kubectl logs -l app=traefik -n ingress-controller
...
{"level":"warning","msg":"Endpoints not available for jenkins/jenkins","time":"2018-10-24T18:33:11Z"}
{"level":"warning","msg":"Endpoints not available for jenkins/jenkins","time":"2018-10-24T18:33:13Z"}
{"level":"warning","msg":"Endpoints not available for jenkins/jenkins","time":"2018-10-24T18:33:13Z"}
```

Eventually my Googling led me to [this GitHub issue comment](https://github.com/kubernetes/kubernetes/issues/11795#issuecomment-124325266), which stated:

> The likely culprit is that your Service's selector doesn't match any Pod's labels.

Sure enough, when I _described_ the full `jenkins` `Service`, I noticed it had no associated Endpoints!

```
$ kubectl describe svc jenkins -n jenkins
Name:              jenkins
Namespace:         jenkins
Labels:            app=jenkins
Annotations:       <none>
Selector:          app=jenkins,tier=frontend
Type:              ClusterIP
IP:                172.20.3.104
Port:              jenkins  80/TCP
TargetPort:        8080/TCP
Endpoints:         <none>
Session Affinity:  None
Events:            <none>
```

I realized the `Selector` labels I had defined did not match the `jenkins` `Deployment` labels I had defined. I changed the labels to match by editing the `Service` definition (`kubectl edit svc -n jenkins`), and then Traefik immediately started serving the traffic, and the `Endpoints` value was filled in with the Jenkins pod's IP address!
