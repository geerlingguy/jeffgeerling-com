---
nid: 3004
title: "Getting colorized output from Molecule and Ansible on GitHub Actions for CI"
slug: "getting-colorized-output-molecule-and-ansible-on-github-actions-ci"
date: 2020-05-11T17:11:54+00:00
drupal:
  nid: 3004
  path: /blog/2020/getting-colorized-output-molecule-and-ansible-on-github-actions-ci
  body_format: markdown
  redirects: []
tags:
  - actions
  - ansible
  - ci
  - color
  - github
  - molecule
  - testing
  - tty
  - workflow
---

For many new Ansible-based projects, I build my tests in Molecule, so I can easily run them locally or in CI. I also started using GitHub Actions for many of my new Ansible projects, just because it's so easy to get started and integrate with GitHub repositories.

I'm actually going to talk about this strategy in my next [Ansible 101](/blog/2020/ansible-101-jeff-geerling-youtube-streaming-series) live stream, covering [Testing Ansible playbooks with Molecule and GitHub Actions CI](https://www.youtube.com/watch?v=CYghlf-6Opc), but I also wanted to highlight one thing that helps me when reviewing or observing playbook and molecule output, and that's _color_.

By default, in an interactive terminal session, Ansible colorizes its output so failures get 'red' color, good things / ok gets 'green', and changes get 'yellow-ish'. Also, warnings get a magenta color, which flags them well so you can go and fix them as soon as possible (that's one core principle I advocate to [make your playbooks maintainable and scalable](/blog/2019/make-your-ansible-playbooks-flexible-maintainable-and-scalable-ansiblefest-austin-2018)).

But by default, in a CI environment like GitHub Actions, there is no interactive TTY, so Ansible doesn't output color codes. Molecule doesn't either, since it's following standard convention, and as a result, when you review the logs for your workflow run, you see output like this:

{{< figure src="./molecule-no-color-no-tty-output-default.png" alt="Molecule and Ansible GitHub workflow non-colorized output - no-tty" width="650" height="375" class="insert-image" >}}

This is from the following build step in a GitHub Actions job:

```
      - name: Run Molecule tests.
        run: molecule test
```

There are two different environment variables you need to pass—one for Molecule, and one for Ansible—to make the output pretty and colorful, so it's easier to glance through a test run's output:

  - `PY_COLORS`: This is a somewhat standard way to tell Python-based tools to force color output, even without TTY. This forces _Molecule_ to generate colorized output, but not Ansible.
  - `ANSIBLE_FORCE_COLOR`: This forces _Ansible_ to generate colorized output.

So, add these two variables to the GitHub Actions step in the `env`:

```
      - name: Run Molecule tests.
        run: molecule test
        env:
          PY_COLORS: '1'
          ANSIBLE_FORCE_COLOR: '1'
```

And now, after a workflow run, you get pretty colors!

{{< figure src="./molecule-color-no-tty-output-colorized.png" alt="Molecule and Ansible GitHub workflow colorized output - no-tty" width="650" height="378" class="insert-image" >}}

Learn more about running GitHub Actions workflows to test your Ansible content with Molecule in chapter 12 of [Ansible for DevOps](https://www.ansiblefordevops.com).
