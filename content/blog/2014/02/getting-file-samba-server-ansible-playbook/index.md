---
nid: 2589
title: "Getting a file from a Samba server in an Ansible playbook"
slug: "getting-file-samba-server-ansible-playbook"
date: 2014-02-07T15:45:28+00:00
drupal:
  nid: 2589
  path: /blog/getting-file-samba-server-ansible-playbook
  body_format: full_html
  redirects: []
tags:
  - ansible
  - file copy
  - filesystem
  - samba
aliases:
  - /blog/getting-file-samba-server-ansible-playbook
---

For a project I'm working on, I needed to make one of my Ansible playbooks grab an archived file off a Windows share using <code>smbclient</code>.

There are a few concerns when doing something like this:

<ol>
<li>There are a few required dependencies that need to be installed and configured.</li>
<li>Unless you have a really insecure windows share, you need a username and password to access the share—and you should never put credentials into any kind of plaintext file!</li>
<li>Many Windows-based environments also need the appropriate workgroup set in Samba's configuration file.</li>
</ol>

I'll dive right in and show you how to set up samba and grab a file from a share in an Ansible playbook:

```
---
- hosts: all

  # See note below.
  vars_prompt:
    - name: smb_username
      prompt: "Enter samba share username"
    - name: smb_password
      prompt: "Enter samba share password"
      private: yes

  tasks:
  - name: Ensure Samba-related packages are installed.
    yum: pkg={{ item }} state=installed
    environment: proxy_env
    with_items:
    - samba
    - samba-client
    - samba-common
    - cifs-utils

  # See note below.
  - name: Copy in Samba configuration.
    template: src=templates/etc/samba/smb.conf dest=/etc/samba/smb.conf owner=root group=root mode=0644

  - name: Copy archive from samba_share.
    command:
      smbclient //hostname/samba_share/ {{ smb_password }} -U {{ smb_username }} -c "recurse;lcd /local/path;get archive.zip"
      creates=/local/path/archive.zip
```

Note 1: We use <code>vars_prompt</code> to ask the user for a network username and password. Instead of storing these values in a playbook or vars file, we ask for them. If you want to use some sort of environment variable, you could do that as well, but I don't like permanently storing credentials in any retrievable format, <del>and there's no simple way to store encrypted passwords and use them in this situation</del> you can now use Ansible's <a href="http://blog.ansibleworks.com/2014/02/19/ansible-vault/">Vault</a> to store encrypted data!

Note 2: For the smb.conf file, you should grab the default smb.conf that was created when Samba was installed, and modify it to your needs; in my case, I was also adding a local share, and changing the <code>workgroup</code> to my local domain. You could use Ansible's <code>lineinfile</code> if you just need to modify a few lines in this file, but I had to do more extensive modifications, and it was easier to just use <code>template</code> and copy the file to the server.
