---
nid: 2814
title: "CI for Ansible playbooks which require Ansible Vault protected variables"
slug: "ci-ansible-playbooks-which-require-ansible-vault-protected-variables"
date: 2017-09-29T22:16:20+00:00
drupal:
  nid: 2814
  path: /blog/2017/ci-ansible-playbooks-which-require-ansible-vault-protected-variables
  body_format: markdown
  redirects: []
tags:
  - ansible
  - ci
  - encryption
  - security
  - testing
  - travis ci
  - vault
---

I use [Ansible Vault](TODO) to securely store the project's secrets (e.g. API keys, default passwords, private keys, etc.) in the git repository for many of my infrastructure projects. I also like to make sure I cover everything possible in automated tests/CI, using either Jenkins or Travis CI (usually).

But this presents a conundrum: if some of your variables are encrypted with an Ansible Vault secret/passphrase, and that secret should be _itself_ store securely... how can you avoid storing it in your CI system, where you might not be able to guarantee it's security?

The method I usually use for this case is including the Vault-encrypted vars at playbook runtime, using `include_vars`:

```
    - name: Include private key from Ansible Vault encrypted file.
      include_vars: vars/private_key.yml
      when: not test_mode
```

That way, in my CI environment, I can make sure the `test_mode` variable is set to `True`, and it won't include the encrypted variable. Great! But there's still one more issue. Even though you're not using the included variable file, if you have a `vault_password_file` defined in your project `ansible.cfg`, then Ansible will always look for that file prior to beginning playbook execution (since the `include_vars` will be dynamically performed later in the execution, and Ansible needs to load in the password at the beginning).

So, in a CI environment, you can do something like:

```
mkdir -p ~/.ansible && touch ~/.ansible/vault-password.txt
```

So, what happens if you run `ansible-playbook` in CI now?

```
[WARNING]: Error in vault password file loading (default): Invalid vault
password was provided from file (/root/.ansible/vault-password.txt)
```

D'oh! Not quite what we were expecting. This _used_ to work, but in Ansible 2.3.2+, a check was added to [verify the vault_password_file is not empty](https://github.com/ansible/ansible/pull/28186/files#diff-fda286154055176d387a08c17e2967f2R357). So, we have to make sure the file is not empty. Change the earlier command to:

```
mkdir -p ~/.ansible && echo \"test-password\" > ~/.ansible/J2-vault-password.txt"
```

Ahh... now `ansible-playbook` will execute and skip decrypting any included vars files that you put the `test_mode` conditional on!

For completeness, here's an example Travis CI `.travis.yml` file that will test a playbook in a Docker container running Ubuntu 16.04:

```
---
services: docker

script:
  - container_id=test
  - set -e
  # Start a Docker container.
  - 'docker run --detach --volume=${PWD}:/etc/ansible/playbook:rw --name ${container_id} --privileged --volume=/sys/fs/cgroup:/sys/fs/cgroup:ro geerlingguy/docker-ubuntu1604-ansible:latest /lib/systemd/systemd'

  # Prep the container.
  - 'docker exec --tty ${container_id} env TERM=xterm bash -c "mkdir -p ~/.ansible && echo \"test-password\" > ~/.ansible/vault-password.txt"'

  # Install dependencies.
  - 'docker exec --tty ${container_id} env TERM=xterm bash -c "cd /etc/ansible/playbook; ansible-galaxy install -r requirements.yml"'

  # Run Ansible playbook (first with a syntax check, then for real).
  - 'docker exec --tty ${container_id} env TERM=xterm bash -c "cd /etc/ansible/playbook; ansible-playbook -i inventory/travis main.yml --syntax-check"'
  - 'docker exec --tty ${container_id} env TERM=xterm bash -c "cd /etc/ansible/playbook; ansible-playbook -i inventory/travis main.yml --extra-vars \"{test_mode: True}\""'
```

If you liked this post, you'll love my book on Ansible, [Ansible for DevOps](https://www.ansiblefordevops.com/)!
