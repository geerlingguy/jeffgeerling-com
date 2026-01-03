---
nid: 2842
title: "Use Ansible's YAML callback plugin for a better CLI experience"
slug: "use-ansibles-yaml-callback-plugin-better-cli-experience"
date: 2018-04-19T21:46:28+00:00
drupal:
  nid: 2842
  path: /blog/2018/use-ansibles-yaml-callback-plugin-better-cli-experience
  body_format: markdown
  redirects: []
tags:
  - ansible
  - callback
  - cli
  - how-to
  - plugin
  - terminal
  - tutorial
  - ux
---

Ansible is a great tool for automating IT workflows, and I use it to manage hundreds of servers and cloud services on a daily basis. One of my small annoyances with Ansible, though, is its default CLI output—whenever there's a command that fails, or a command or task that succeeds and dumps a bunch of output to the CLI, the default visible output is not very human-friendly.

For example, in a Django installation example from chapter 3 of my book [Ansible for DevOps](https://www.ansiblefordevops.com), there's an ad-hoc command to install Django on a number of CentOS app servers using Ansible's `yum` module. Here's how it looks in the terminal when you run that task the first time, using Ansible's default display options, and there's a failure:

{{< figure src="./ansible-25-default-callback-plugin.png" alt="Ansible 2.5 default callback plugin" width="650" height="381" class="insert-image" >}}

...it's not quickly digestible—and this is one of the shorter error messages I've seen!

Ansible introduced [callback plugins](https://docs.ansible.com/ansible/2.5/plugins/callback.html) a while ago, but I just noticed there's a new YAML callback plugin introduced with Ansible 2.5—meaning any machine running Ansible 2.5.0 or later can automatically start using this wonderfully-optimized-for-humans format, without you needing to install a custom plugin on the machine, or include it with all your projects!

> **Note**: As of Ansible 2.13, the proper way to use yaml output is to set the following in ansible.cfg:
>
> ```
> callback_result_format = yaml
> ```
>
> See [Ansible YAML output: community.general.yaml has been deprecated](https://forum.ansible.com/t/ansible-yaml-output-community-general-yaml-has-been-deprecated/39480/7).

If you're using Ansible < 2.13:

To use it, edit your `ansible.cfg` file (either global, in `/etc/ansible/ansible.cfg`, or a local one in your playbook/project), and add the following lines under the `[defaults]` section:

```
# Use the YAML callback plugin.
stdout_callback = yaml
# Use the stdout_callback when running ad-hoc commands.
bin_ansible_callbacks = True
```

Now, let's try the same Ansible command from earlier, this time using the YAML callback plugin:

{{< figure src="./ansible-25-yaml-callback-plugin.png" alt="Ansible 2.5 YAML callback plugin" width="650" height="381" class="insert-image" >}}

Ah, much better! Now I can easily read through the error message, just as if it was streamed from the server into my terminal. And if you need to parse the data, it's valid YAML, so it's just as easy as the JSON you'd get previously. If you're looking for a usable CLI experience, there are a few other good built-in callback plugins you might want to try, too, like `unixy`, `dense`, or `debug`.

If you want to go even deeper, and maybe even write your _own_ callback plugins, check out this presentation from AnsibleFest San Francisco 2017: [The Power of Callback Plugins](https://www.ansible.com/power-of-callback-plugins).
