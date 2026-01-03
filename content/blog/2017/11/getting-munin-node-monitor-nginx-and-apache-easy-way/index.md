---
nid: 2821
title: "Getting Munin-node to monitor Nginx and Apache, the easy way"
slug: "getting-munin-node-monitor-nginx-and-apache-easy-way"
date: 2017-11-28T02:30:18+00:00
drupal:
  nid: 2821
  path: /blog/2017/getting-munin-node-monitor-nginx-and-apache-easy-way
  body_format: markdown
  redirects: []
tags:
  - ansible
  - apache
  - devops
  - monitoring
  - munin
  - munin-node
  - nginx
---

Since this is something I think I've bumped into at least eight times in the past decade, I thought I'd document, comprehensively, how I get Munin to monitor Apache and/or Nginx using the `apache_*` and `nginx_*` Munin plugins that come with Munin itself.

Besides the obvious action of symlinking the plugins into Munin's plugins folder, you should—to avoid any surprises—forcibly configure the `env.url` for all Apache and Nginx servers. As an example, in your munin-node configuration (on RedHat/CentOS, in `/etc/munin/plugin-conf.d`, add a file named something like `apache` or `nginx`):

```
# For Nginx:
[nginx*]
env.url http://localhost/nginx_status

# For Apache:
[apache*]
env.url http://localhost/server-status?auto
```

Now, something that often trips me up—especially since I maintain a variety of servers and containers, with some running ancient forms of CentOS, while others are running more recent builds of Debian, Fedora, or Ubuntu—is that `localhost` doesn't always mean what you'd _think_ it means.

Sometimes `curl http://localhost/server-status?auto` will work, but `munin-run apache_accesses --debug` will turn up an annoying:

```
# Environment url = http://localhost/server-status?auto
# About to run '/etc/munin/plugins/apache_accesses'
accesses80.value U
```

That `U` means it's not picking up the value. So the most reliable way to get things working, in my experience, is to explicitly add a 'localhost' server (Nginx) or VirtualHost (Apache), allowing access only from localhost to the respective status endpoint.

So, for Apache, add a virtualhost like:

```
<VirtualHost *:80>
  ServerName localhost
</VirtualHost>
```

And then also make sure you configure the ExtendedStatus endpoint, like so:

```
<IfModule mod_status.c>
  ExtendedStatus On
  <Location /server-status>
      SetHandler server-status
      Order deny,allow
      Deny from all
      Allow from 127.0.0.1 localhost ::1 ip6-localhost
  </Location>
</IfModule>
```

On RedHat derivatives, those Apache config files should be placed in `/etc/httpd/conf.d/[vhost filename here].conf` and `/etc/httpd/conf.modules.d/15-status.conf`, respectively. On Debian derivatives, in `/etc/apache2/sites-enabled/[vhost filename here].conf` and `/etc/apache2/mods-enabled/status.conf`, respectively.

For Nginx, you just need to add an extra `server {}` configuration to your Nginx hosts, like so:

```
server
{
    listen 127.0.0.1;
    server_name localhost;

    location /nginx_status {
        stub_status on; # activate stub_status module
        access_log off;
        allow 127.0.0.1; # localhost
        allow ::1; # localhost
        deny all;
    }
}
```

After adding these configs, make sure you restart the webserver (e.g. `systemctl restart httpd` (or `apache2`), or `systemctl restart nginx`).

Test that you can connect using curl first:

```
# Apache
$ curl http://localhost/server-status?auto

# Nginx
$ curl http://localhost/nginx_status
```

Then make sure `munin-node` will be able to pick up the values as well:

```
# Apache
$ munin-run apache_accesses --debug
...
# Environment url = http://localhost/server-status?auto
# About to run '/etc/munin/plugins/apache_accesses'
accesses80.value 15

# Nginx
$ munin-run nginx_request --debug
...
# Environment url = http://localhost/nginx_status
# About to run '/etc/munin/plugins/nginx_request'
request.value 2809
```

To automate much of this setup and configuration process, I use the following Ansible roles:

  - [geerlingguy.munin](https://galaxy.ansible.com/geerlingguy/munin/)
  - [geerlingguy.munin-node](https://galaxy.ansible.com/geerlingguy/munin-node/)
  - [geerlingguy.apache](https://galaxy.ansible.com/geerlingguy/apache/)
  - [geerlingguy.nginx](https://galaxy.ansible.com/geerlingguy/nginx/)
