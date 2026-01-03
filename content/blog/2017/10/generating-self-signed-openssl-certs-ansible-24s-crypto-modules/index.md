---
nid: 2818
title: "Generating self-signed OpenSSL certs with Ansible 2.4's crypto modules"
slug: "generating-self-signed-openssl-certs-ansible-24s-crypto-modules"
date: 2017-10-31T20:43:49+00:00
drupal:
  nid: 2818
  path: /blog/2017/generating-self-signed-openssl-certs-ansible-24s-crypto-modules
  body_format: markdown
  redirects: []
tags:
  - ansible
  - certbot
  - letsencrypt
  - openssl
  - pip
  - python
  - ssl
  - tls
  - tutorial
---

Ansible 2.4 is notable for a number of improvements and changes, but one that flew under my radar was the addition of a set of new `openssl_*` crypto-related modules.

The following modules were added in Ansible 2.4.0:

  - [`openssl_certificate` - Generate and/or check OpenSSL certificates](https://docs.ansible.com/ansible/2.4/openssl_certificate_module.html)
  - [`openssl_csr` - Generate OpenSSL Certificate Signing Request (CSR)](https://docs.ansible.com/ansible/2.4/openssl_csr_module.html)
  - [`openssl_privatekey` - Generate OpenSSL private keys](https://docs.ansible.com/ansible/2.4/openssl_privatekey_module.html)
  - [`openssl_publickey` - Generate an OpenSSL public key from its private key](https://docs.ansible.com/ansible/2.4/openssl_publickey_module.html)

In the past, when I've had to generate OpenSSL certs on my servers (usually for CI purposes or in local test environments), I've used the `command` or `shell` module and `openssl` with a bunch of flags ([example](https://serialized.net/2013/04/simply-generating-self-signed-ssl-certs-with-ansible/)), and while that technique still works, it's slightly annoying to try to make it easy to read and be configurable for different situations.

With these new Ansible modules, though, it's a lot simpler to go through the process of generating a self-signed cert:

```
- name: Ensure directory exists for local self-signed TLS certs.
  file:
    path: /etc/letsencrypt/live/{{ server_hostname }}
    state: directory

- name: Generate an OpenSSL private key.
  openssl_privatekey:
    path: /etc/letsencrypt/live/{{ server_hostname }}/privkey.pem

- name: Generate an OpenSSL CSR.
  openssl_csr:
    path: /etc/ssl/private/{{ server_hostname }}.csr
    privatekey_path: /etc/letsencrypt/live/{{ server_hostname }}/privkey.pem
    common_name: "{{ server_hostname }}"

- name: Generate a Self Signed OpenSSL certificate.
  openssl_certificate:
    path: /etc/letsencrypt/live/{{ server_hostname }}/fullchain.pem
    privatekey_path: /etc/letsencrypt/live/{{ server_hostname }}/privkey.pem
    csr_path: /etc/ssl/private/{{ server_hostname }}.csr
    provider: selfsigned
```

I used the above set of tasks to generate example letsencrypt/certbot certs for use when developing locally on some infrastructure which has HSTS enabled, so all requests to the domain and it's subdomains requires working SSL. Note that you might need to install pyOpenSSL if it's not already present; you can use the `pip` module to do that prior to running the `openssl_*` tasks:

```
- name: Ensure python OpenSSL dependencies are installed.
  pip:
    name: pyOpenSSL
    state: present
```

And if you need `pip`, you can install it with my [`geerlingguy.pip` role](https://github.com/geerlingguy/ansible-role-pip)!

Certbot still has a bit of a chicken-and-egg problem when it comes to [fully automating the cert and webserver setup process](https://github.com/geerlingguy/ansible-role-certbot/issues/12), but using tasks like the ones above can make it easier to shim in some valid (but self-signed) certs when Let's Encrypt can't work (e.g. in CI infrastructure, or in infrastructure behind proxies or NAT).
