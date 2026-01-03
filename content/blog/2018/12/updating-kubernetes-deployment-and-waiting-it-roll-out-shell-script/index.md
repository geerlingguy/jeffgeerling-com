---
nid: 2901
title: "Updating a Kubernetes Deployment and waiting for it to roll out in a shell script"
slug: "updating-kubernetes-deployment-and-waiting-it-roll-out-shell-script"
date: 2018-12-28T18:22:40+00:00
drupal:
  nid: 2901
  path: /blog/2018/updating-kubernetes-deployment-and-waiting-it-roll-out-shell-script
  body_format: markdown
  redirects: []
tags:
  - automation
  - bash
  - deployment
  - kubernetes
  - namespace
  - script
---

For some Kubernetes cluster operations (e.g. deploying an update to a small microservice or app), I need a quick and dirty way to:

  1. Build and push a Docker image to a private registry.
  2. Update a Kubernetes Deployment to use this new image version.
  3. Wait for the Deployment rollout to complete.
  4. Run some post-rollout operations (e.g. clear caches, run an update, etc.).

There are a thousand and one ways to do all this, and many are a bit more formal than this, but sometimes you just need a shell script you can run from your CI server to do it all. And it's not too hard, nor complex, to do it this way:

```
#!/bin/bash
# Build, push, deploy, and run post-deploy tasks for myapp.

# Define the version to be deployed (e.g. a git hash or semver tag).
version="1.0.0"

# Build and push the container image.
docker build -t registry-url:namespace/myapp:$version .
docker push registry-url:namespace/myapp:$version
docker tag registry-url:namespace/myapp:$version registry-url:namespace/myapp:latest
docker push registry-url:namespace/myapp:latest

# Update the myapp deployment in Kubernetes, in the namespace 'namespace'.
kubectl set image deployment/app myapp=registry-url:namespace/myapp:$version -n namespace

# Check deployment rollout status every 10 seconds (max 10 minutes) until complete.
ATTEMPTS=0
ROLLOUT_STATUS_CMD="kubectl rollout status deployment/myapp -n namespace"
until $ROLLOUT_STATUS_CMD || [ $ATTEMPTS -eq 60 ]; do
  $ROLLOUT_STATUS_CMD
  ATTEMPTS=$((attempts + 1))
  sleep 10
done

# Run other post-deployment tasks, now that all new Pods are present, and old ones are gone.
MYAPP_POD=$(kubectl get pods -l app=myapp -n namespace | grep "^myapp.*Running" | awk '{print $1}')
kubectl exec "$MYAPP_POD" -n namespace -- bash -c "vendor/bin/drush --uri myapp.com cr"
```

The example above achieves all the tasks I need to do for a common app deployment; note that it's better to have a more formal process in place for most things... but when you just need a system that works, and is easy to debug and/or run manually as needed, this works fine.

Note that I also tried getting `kubectl wait` to work in this situation, but couldn't find a way to make it work with the rollout. It works great for deployment status:

```
kubectl wait --for=condition=available --timeout=600s deployment/myapp -n namespace
```

...but this will happily return once the deployment is _available_, but there could still be old pods in Terminating status, or new pods that are not fully online yet.
