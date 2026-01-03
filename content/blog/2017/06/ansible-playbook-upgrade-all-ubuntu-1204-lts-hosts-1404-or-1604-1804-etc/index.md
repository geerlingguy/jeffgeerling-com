---
nid: 2789
title: "Ansible playbook to upgrade all Ubuntu 12.04 LTS hosts to 14.04 (or 16.04, 18.04, 20.04, etc.)"
slug: "ansible-playbook-upgrade-all-ubuntu-1204-lts-hosts-1404-or-1604-1804-etc"
date: 2017-06-22T04:24:41+00:00
drupal:
  nid: 2789
  path: /blog/2018/ansible-playbook-upgrade-all-ubuntu-1204-lts-hosts-1404-or-1604-1804-etc
  body_format: markdown
  redirects:
    - /blog/2017/ansible-playbook-upgrade-all-ubuntu-1204-lts-hosts-1404-or-1604
aliases:
  - /blog/2017/ansible-playbook-upgrade-all-ubuntu-1204-lts-hosts-1404-or-1604
tags:
  - ansible
  - end of life
  - linux
  - precise
  - trusty
  - tutorial
  - ubuntu
  - upgrade
---

Generally speaking, I'm against performing major OS upgrades on my Linux servers; there are often little things that get broken, or configurations gone awry, when you attempt an upgrade... and part of the point of automation (or striving towards a 12-factor app) is that you don't 'upgrade'—you destroy and rebuild with a newer version.

But, there are still cases where you have legacy servers running one little task that you haven't yet automated entirely, or that have data on them that is not yet stored in a way where you can tear down the server and build a new replacement. In these cases, assuming you've already done a canary upgrade on a similar but disposable server (to make sure there are no major gotchas), it may be the lesser of two evils to use something like Ubuntu's `do-release-upgrade`.

Since Ubuntu 12.04 LTS was end-of-lifed earlier this year, and I had about a dozen servers for one of my services that were still running 12.04, I decided to bite the bullet (I've been procrastinating replacing these servers a while!), and perform the in-place upgrade. I also ensured that a fresh backup was taken as part of the upgrade process (using my simple [geerlingguy.backup](https://galaxy.ansible.com/geerlingguy/backup/) role for Ansible.

Here's the playbook I used—note that it will only perform a release upgrade on Ubuntu 12.04 LTS servers. If you want to upgrade from 14.04 to 16.04, then you'd need to change a few numbers in the playbook to '14.04' instead of '12.04':

```
---
- hosts: legacyservers
  gather_facts: yes
  become: yes

  tasks:

    # Use a block to perform tasks conditionally—only if running Ubuntu 12.04.
    - block:

      - debug:
          msg: 'This server is running Ubuntu 12.04 LTS and will be upgraded to 14.04 LTS.'

      # Now would be a good time to take a backup if you can trigger an
      # automated backup!

      - name: Remove the EOL message of the day if one exists.
        file:
          path: "{{ item }}"
          state: absent
        with_items:
          - /etc/update-motd.d/99-esm
          - /run/motd.dynamic

      - name: Upgrade all packages to the latest version
        apt: update_cache=yes upgrade=full

      - name: Ensure update-manager-core is installed.
        apt: name=update-manager-core state=present

      - name: Run do-release-upgrade non-interactively.
        command: do-release-upgrade -f DistUpgradeViewNonInteractive

      - name: Reboot the server.
        reboot:

      when:
        - ansible_distribution == 'Ubuntu'
        - ansible_distribution_version == '12.04'

# After the playbook is finished, it's a good idea to confirm all the servers
# are actually upgraded. Run something like:
#     ansible [group] -a "lsb_release -a"
```

This idempotent* playbook does the following:

  1. Prints a message indicating an inventory server will be upgraded.
  2. Clears out the pesky 'Ubuntu 12.04 has reached end-of-life' message of the day (MOTD) so you don't see it next time you log into one of these servers.
  3. Upgrades everything to the latest package versions.
  4. Ensures `update-manager-core` is installed so `do-release-upgrade` can be run.
  5. Runs the release upgrade, reboots the server, and waits for the server to respond on port 22 (SSH) before completing.

After you run a playbook like this, you may want to manually verify the servers are all upgraded. You can use an ad-hoc command to do that:

    ansible [group] -a "lsb_release -a"

Technically, you could add a task in the playbook that performs this confirmation task... but whatever way works, works!

<em>* Idempotent = you can run the playbook multiple times and once it gets things in a certain state (e.g. 12.04 hosts upgraded to 14.04), it will change nothing else and report 'ok' instead of 'changed' during `ansible-playbook` runs.</em>
