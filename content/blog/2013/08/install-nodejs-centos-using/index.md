---
nid: 2420
title: "Install Node.js on CentOS 6 using yum"
slug: "install-nodejs-centos-using"
date: 2013-08-08T02:06:56+00:00
drupal:
  nid: 2420
  path: /blogs/jeff-geerling/install-nodejs-centos-using
  body_format: full_html
  redirects: []
tags:
  - centos
  - node.js
  - yum
---

If you're running CentOS 6.x (I use 6.4 currently), and you have <a href="http://www.rackspace.com/knowledge_center/article/installing-rhel-epel-repo-on-centos-5x-or-6x">installed the EPEL yum repository</a>, you can install Node.js simply with:

```
$ sudo yum install npm
```

Done. Check for node's successful installation by running <code>$ node -v</code> (it should return something like <code>v0.10.4</code>).

Adapted from <a href="http://serverfault.com/a/509086/15673">my answer on Server Fault</a>.
