---
nid: 2340
title: "Configure sendmail on CentOS to allow sending of email from localhost"
slug: "configure-sendmail-centos"
date: 2011-11-02T18:14:50+00:00
drupal:
  nid: 2340
  path: /blogs/jeff-geerling/configure-sendmail-centos
  body_format: full_html
  redirects: []
tags:
  - email
  - hosting
  - sendmail
  - vps
---

For some of my Drupal sites and PHP scripts (and shell scripts) that I run on a VPS I manage, I need to simply be able to send outgoing emails from arbitrary email addresses. I could go into all the details of DNS SPF records and MX records here, but that's something you'll need to research on your own. This post simply shows how to install and configure sendmail on a CentOS box to just allow outgoing mail from php's mail() function, the mail command line utility, etc., and only from localhost (127.0.0.1):

First, install sendmail with <code>$ sudo yum install sendmail sendmail-cf</code>.

Then, configure sendmail by editing the file <code>/etc/mail/sendmail.mc</code> (don't edit the sendmail.cf file - we'll auto-generate that after setting things correctly in sendmail.mc).

<ul>
<li>Configure DAEMON_OPTIONS to only allow sending from localhost/smtp: <code>DAEMON_OPTIONS(`Port=smtp,Addr=127.0.0.1, Name=MTA')dnl</code></li>
<li>Set the LOCAL_DOMAIN option to your hostname: <code>LOCAL_DOMAIN(`example.com')dnl</code></li>
</ul>

Now, to update sendmail's configuration, enter <code>$ sudo make -C /etc/mail</code>, and then restart sendmail with <code>$ sudo service sendmail restart</code>.

You'll also want to make sure your hostname is set correctly (this will be the default from address domain); check it by entering <code>$ hostname</code>... if it's incorrect, you can set it explicitly in <code>/etc/sysconfig/network</code> as the HOSTNAME variable. You might also want to add your hostname to /etc/hosts as the first result for 127.0.0.1.

(This guide assumes you're using RHEL or CentOS/Fedora...).
