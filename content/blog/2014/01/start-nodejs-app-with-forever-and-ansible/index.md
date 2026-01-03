---
nid: 2612
title: "Start a Node.js app with Forever and Ansible"
slug: "start-nodejs-app-with-forever-and-ansible"
date: 2014-01-27T15:59:26+00:00
drupal:
  nid: 2612
  path: /blog/start-nodejs-app-with-forever-and-ansible
  body_format: full_html
  redirects:
    - /blog/start-and-run-nodejs-app-forever-and-ansible
aliases:
  - /blog/start-and-run-nodejs-app-forever-and-ansible
   - /blog/start-nodejs-app-with-forever-and-ansible
tags:
  - ansible
  - ansible for devops
  - forever
  - node.js
---

<a href="https://npmjs.org/package/forever">Forever</a> is a really simple and flexible tool to daemonize Node.js apps. Instead of running them with <code>nohup node /path/to/app.js &</code>, run them with forever (so you can <code>forever start [app]</code> and <code>forever stop [app]</code>, among other things). Server Check.in uses <a href="http://www.ansible.com/">Ansible</a> to deploy our Node.js apps, and there's currently no Ansible module to control <code>forever</code> like you control <code>service</code>, but you can still use the following plays to install forever and run your app:

```
    - name: "Install forever (to run Node.js app)."
      npm: name=forever global=yes state=present
    
    - name: "Check list of Node.js apps running."
      command: forever list
      register: forever_list
      changed_when: false

    - name: "Start example Node.js app."
      command: forever start /path/to/app.js
      when: "forever_list.stdout.find('/path/to/app.js') == -1"
```

This is completely idempotent, and works great for us. You could program a little <code>forever</code> module for Ansible to do this stuff for you (like the <code>service</code> module), but this works well enough for our purposes.

Using Forever to run Node.js apps is also covered in <a href="http://www.ansiblefordevops.com/">Ansible for DevOps</a>, in an example playbook that deploys and configures a Node.js app server.

This topic was also posted to Stack Overflow in <a href="http://stackoverflow.com/a/21385202/100134">this answer</a>.
