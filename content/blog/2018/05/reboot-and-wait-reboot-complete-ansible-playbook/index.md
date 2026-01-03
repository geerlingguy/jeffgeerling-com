---
nid: 2849
title: "Reboot and wait for reboot to complete in Ansible playbook"
slug: "reboot-and-wait-reboot-complete-ansible-playbook"
date: 2018-05-24T15:09:11+00:00
drupal:
  nid: 2849
  path: /blog/2018/reboot-and-wait-reboot-complete-ansible-playbook
  body_format: markdown
  redirects: []
tags:
  - ansible
  - automation
  - orchestration
  - playbook
  - reboot
  - restart
  - server
  - tutorial
---

> **September 2018 Update**: Ansible 2.7 (to be released around October 2018) will include a new [reboot](https://docs.ansible.com/ansible/devel/modules/reboot_module.html) module, which makes reboots a heck of a lot simpler (whether managing Windows, Mac, or Linux!):
> 
>     - name: Reboot the server and wait for it to come back up.
>       reboot:
>
> That's it! Much easier than the older technique I used in Ansible < 2.7!

One pattern I often need to implement in my Ansible playbooks is "configure-reboot-configure", where you change some setting that requires a reboot to take effect, and you have to wait for the reboot to take place before continuing on with the rest of the playbook run.

For example, on my [Raspberry Pi Dramble](https://github.com/geerlingguy/raspberry-pi-dramble) project, before installing Docker and Kubernetes, I need to make sure the Raspberry Pi's `/boot/cmdline.txt` file contains a couple cgroup features so Kubernetes runs correctly. But after adding these options, I also have to reboot the Pi.

If you just add a task like `command: reboot` (run with become/sudo), you might run into this annoying error during a playbook run:

```
TASK [Reboot immediately if cgroup features changed.] ******************************************************************
fatal: [10.0.100.44]: UNREACHABLE! => changed=false 
  msg: |-
    Failed to connect to the host via ssh: Shared connection to 10.0.100.44 closed.
  unreachable: true

PLAY RECAP *************************************************************************************************************
10.0.100.44                : ok=4    changed=2    unreachable=1    failed=0
```

When that happens, the playbook fails and you have to run it again to get back to the point where you can start configuring things again.

Luckily, Ansible has a way of dealing with this special case where you are basically dropping the ability to connect to the server Ansible is managing, at least temporarily, using `async` and the special [`wait_for_connection` module](http://docs.ansible.com/ansible/latest/modules/wait_for_connection_module.html).

Here's how I rewrote my tasks so they would correctly reboot the Raspberry Pi, then wait for it to be available again before proceeding with the rest of the playbook:

```
---
- name: Do something that requires a reboot when it results in a change.
  ...
  register: task_result

- name: Reboot immediately if there was a change.
  shell: "sleep 5 && reboot"
  async: 1
  poll: 0
  when: task_result is changed

- name: Wait for the reboot to complete if there was a change.
  wait_for_connection:
    connect_timeout: 20
    sleep: 5
    delay: 5
    timeout: 300
  when: task_result is changed

...
```

## Notes

  1. I don't want to reboot the Pi _every_ time my playbook runs, but instead only when it needs to reboot. So I registered `task_result` and used `task_result is changed` as a condition for the reboot. This way, the second time I run my playbook I don't have to sit around and wait for an unnecessary reboot!
  2. I used the `shell` module instead of `command` for the reboot task, because `shell` supports builtins like `&&`. And I used `sleep 5 && reboot` instead of just `reboot`, because Ansible needs a couple seconds to wrap up it's connection so the task can complete. If you just do a `reboot` or `shutdown -r now`, then the server will drop the SSH connection before Ansible can close it cleanly, and you'll get the same error I mentioned earlier.
  3. You may need different values for your `wait_for_connection` task; my Raspberry Pis usually reboot within a minute or so; but some cloud servers and other types of servers could take much longer.

## Running with `ansible` as an ad-hoc command

Sometimes I also need to do the same thing using a quick ad-hoc command. This is pretty easy to translate using the `-B [seconds]` ('background' option, with timeout in seconds) and `-P [seconds]` ('polling' option, with delay in seconds; 0 to disable polling):

    ansible all -i inventory -b -B 1 -P 0 -m shell -a "sleep 5 && reboot"
