---
nid: 2910
title: "Expanding K8s PVs in EKS on AWS"
slug: "expanding-k8s-pvs-eks-on-aws"
date: 2019-02-21T22:15:00+00:00
drupal:
  nid: 2910
  path: /blog/2019/expanding-k8s-pvs-eks-on-aws
  body_format: markdown
  redirects: []
tags:
  - aws
  - ebs
  - eks
  - kubernetes
  - pv
  - pvc
  - storage
  - volumes
---

If that post title isn't a mouthful...

I'm excited to be moving a few EKS clusters into real-world production use after a few months of preparation. Besides my [Raspberry Pi Dramble](http://www.pidramble.com) project (which is pretty low-key), these are the only production-grade Kubernetes clusters I've dealt with—and I've learned a _lot_. Enough that I'm working on a new book.

Anyways, back to the main topic: As of Kubernetes 1.11, you can auto-expand PVs from most cloud providers, AWS included. And since EKS now runs Kubernetes 1.11.x, you can have your EBS PVs automatically expand by just increasing the PVC claim size in `spec.resources.requests.storage` to a larger size (e.g. `10Gi` to `20Gi`).

To make sure this works, though, you need to make sure of a few things:

## Make sure you have the proper setting on your StorageClass

You need to make sure the StorageClass you're using has the `allowVolumeExpansion` setting enabled, e.g.:

```
---
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: standard
  annotations:
    storageclass.beta.kubernetes.io/is-default-class: "true"
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp2
reclaimPolicy: Delete
allowVolumeExpansion: true
mountOptions:
  - debug
```

## Edit your PVC

Increase the storage request of your PVC (note that you cannot _decrease_ the request... that's a lot weirder a use case and is not something trivial to do on most storage systems!) by editing the pvc:

```
$ kubectl edit pvc -n [namespace] [claim-name]
...
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 20Gi # increased from 10Gi
  storageClassName: standard
```

Save the edit, then wait, and monitor the PV associated with the PVC:

```
$ kubectl get pv pvc-d2adc816-d0c7-11e8-80aa-0ef7083fecf8 --watch
```

Once it's done, you're ready for the final step!

## Delete/restart the Pod(s) which mount the PVC

This may seem unintuitive, but in order for Kubernetes to expand the actual volume on the disk to fill the newly-available free space, it has to detach the volume (so the running Pod has to be terminated), then it expands the PVC, then it attaches it to a new Pod:

```
$ kubectl delete pod -n [namespace] [pod identifier]
```

After a minute or two (or longer if the volume is huge), the new pod should be up with the now-larger PVC attached.

No need to use `fdisk` or anything arcane like that... just make the claim request larger, wait for it to expand, then delete pods using it, and things come back with the new larger size. Nice!
