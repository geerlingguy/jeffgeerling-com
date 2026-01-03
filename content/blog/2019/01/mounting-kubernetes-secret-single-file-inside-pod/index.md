---
nid: 2905
title: "Mounting a Kubernetes Secret as a single file inside a Pod"
slug: "mounting-kubernetes-secret-single-file-inside-pod"
date: 2019-01-15T22:07:12+00:00
drupal:
  nid: 2905
  path: /blog/2019/mounting-kubernetes-secret-single-file-inside-pod
  body_format: markdown
  redirects: []
tags:
  - deployment
  - k8s
  - kubernetes
  - manifest
  - secrets
---

Recently I needed to mount an SSH private key used for one app to connect to another app into a running Pod, but to make sure it was done securely, we put the SSH key into a Kubernetes Secret, and then mounted the Secret into a file inside the Pod spec for a Deployment.

I wanted to document the process here because (a) I know I'm going to have to do it again and this will save me a few minutes' research, and (b) it's very slightly unintuitive (at least to me).

First I defined a secret in a namespace:

```
apiVersion: v1
kind: Secret
metadata:
  name: ssh-key
  namespace: acme
data:
  id_rsa: {{ secret_value_base64_encoded }}
```

Note the key of `id_rsa` for the secret data—I used this because when you mount a secret into a volume, the mount point will be a directory, and each file in that directory corresponds to a key in the Secret's `data`. So in this case, if I set a mount path of `/var/my-app`, then Kubernetes would place a file in there named `id_rsa`, with the value from the Secret. (Note that I'm using Ansible to template and apply manifests, so I'm actually using a value like `{{ ansible_vault_encrypted_string | b64encode }}`, which uses Ansible Vault to decrypt an encrypted private key in a playbook variable—though that's besides the point here).

To get that file to mount in the path `/var/my-app/id_rsa`, I add the volume like so in my Deployment `spec`:

```
spec:
  template:
    spec:
      containers:
      - image: "my-image:latest"
        name: my-app
        ...
        volumeMounts:
          - mountPath: "/var/my-app"
            name: ssh-key
            readOnly: true
      volumes:
        - name: ssh-key
          secret:
            secretName: ssh-key
```

Note that you can control the secrets files permissions using `defaultMode` in the `volumes` definition, or even individually per file (if there are multiple keys in the Secret's `data`), but that exercise is left up to the reader. See the [Secrets documentation](https://kubernetes.io/docs/concepts/configuration/secret/) for more on that (specifically, the section on `Secret files permissions`).

## Mounting a secret to a single file in an existing directory

One thing that is not supported, unfortunately, is mounting a single secret to a single file in a directory which already exists inside the container. This means secrets can't be mounted as files in the same way you'd do a file-as-volume-mount in Docker or mount a ConfigMap item into an existing directory. When you mount a secret to a directory (like `/var/my-app` in the above example), Kubernetes will mount the entire directory `/var/my-app` with _only_ the contents of your secret / secretName items.

To overcome this issue, you can mount the secret somewhere else (e.g. `/var/my-app-secrets`), then use a `postStart` lifecycle hook to copy it into place:

```
        lifecycle:
          postStart:
            exec:
              command:
                - /bin/sh
                - -c
                - cp /var/my-app-secrets/id_rsa /var/my-app/id_rsa
```

That way, existing contents of the `/var/my-app` directory are be preserved.
