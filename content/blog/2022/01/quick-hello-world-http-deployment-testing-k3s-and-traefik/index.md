---
nid: 3167
title: "Quick 'Hello World' HTTP deployment for testing K3s and Traefik"
slug: "quick-hello-world-http-deployment-testing-k3s-and-traefik"
date: 2022-01-12T21:02:02+00:00
drupal:
  nid: 3167
  path: /blog/2022/quick-hello-world-http-deployment-testing-k3s-and-traefik
  body_format: markdown
  redirects: []
tags:
  - hello world
  - http
  - ingress
  - k3s
  - kubernetes
  - load balancing
  - networking
---

Recently I needed to test the full HTTP stack between a Kubernetes cluster's member nodes and an external Internet routing setup, and so I wanted to quickly install K3s (which includes Traefik by default, and load balances through ports 80 and 443 on all nodes), then get a quick 'hello world' web page up, so I could see if the traffic was routing properly all the way from the external host through to a running container exposed via Traefik Ingress.

Here's how I set up a basic 'Hello World' web page on my K3s cluster:

First, I created an HTML file to be stored as a ConfigMap. Create a file named `index.html` with the following contents:

```html
<html>
<head>
  <title>Hello World!</title>
</head>
<body>Hello World!</body>
</html>
```

Create a ConfigMap with the HTML from the file you just created:

```
$ kubectl create configmap hello-world --from-file index.html
```

Save the following to Kubernetes resource definitions into a file named `hello-world.yml`:

```yaml
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: hello-world
  annotations:
    kubernetes.io/ingress.class: "traefik"
spec:
  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: hello-world
            port:
              number: 80

---
apiVersion: v1
kind: Service
metadata:
  name: hello-world
spec:
  ports:
    - port: 80
      protocol: TCP
  selector:
    app:  hello-world

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-world-nginx
spec:
  selector:
    matchLabels:
      app: hello-world
  replicas: 3
  template:
    metadata:
      labels:
        app: hello-world
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
        volumeMounts:
        - name: hello-world-volume
          mountPath: /usr/share/nginx/html
      volumes:
      - name: hello-world-volume
        configMap:
          name: hello-world
```

Then deploy the Nginx container deployment, Service, and Traefik Ingress resources with:

```
$ kubectl apply -f hello-world.yml
```

After a few seconds, you should be able to access port 80 on any member nodes (assuming networking is working), and get back:

```
$ curl localhost:80
<html>
<head>
  <title>Hello World!</title>
</head>
<body>Hello World!</body>
</html>
```

And in my case, I could test out the external routing and make sure that same response was making it through. Yay!
