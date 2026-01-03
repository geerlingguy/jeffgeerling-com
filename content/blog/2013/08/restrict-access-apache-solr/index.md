---
nid: 2423
title: "Restrict access to the Apache Solr admin interface"
slug: "restrict-access-apache-solr"
date: 2013-08-25T15:47:02+00:00
drupal:
  nid: 2423
  path: /blogs/jeff-geerling/restrict-access-apache-solr
  body_format: full_html
  redirects: []
tags:
  - firewall
  - iptables
  - jetty
  - security
  - solr
  - tomcat
aliases:
  - /blogs/jeff-geerling/restrict-access-apache-solr
---

I've helped many people set up or fix a botched install of Apache Solr on their VPSes and web servers. Most of the time, I've noticed that people leave the administrative frontend to Solr wide open for anybody on the internet to access, by just accessing <code>http://example.com:8983/solr</code>. This is <em>very dangerous</em>, as not only can anyone browse and query your search indexes, they can even add, delete, or change your search cores, and see sensitive system information that can be used to gain further access!

<p style="text-align: center;">{{< figure src="./solr-dashboard-resized.png" alt="Solr Dashboard" width="300" height="131" >}}
<em>The Apache Solr admin dashboard</em></p>

There are a few different ways you can lock down access to a solr server, and besides <a href="http://telligent.com/support/telligent_evolution_platform/w/documentation/securing-solr-on-tomcat.aspx">setting up basic HTTP authentication in Tomcat</a> for Solr access, the simplest way is to limit access to port 8983 to either localhost (if solr/tomcat is running on the same server as your website that's using solr), or a specific IP address (if solr/tomcat is on a separate server), using iptables.

The two commands to configure this are:

```
sudo iptables -A INPUT -p tcp -s localhost --dport 8983 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 8983 -j DROP
```

The first command tells iptables, "accept all connections from localhost on port 8983", and the second tells iptables, "drop all traffic to port 8983"—since iptables obeys rules in order from top to bottom, localhost traffic is let through, while other traffic is denied.

To save these rules permanently (so they'll persist after a reboot) on CentOS 6.x, make sure you save the firewall configuration with <code>sudo service iptables save</code>

If you ever need to access the administrative Solr dashboard again, you could insert another rule earlier in the iptables rule chain allowing access to port 8983 to your computer's IP address, then delete that rule when you're finished working on the dashboard.

<em>Note: If you're using Jetty instead of Tomcat, just substitute port 8080 for 8983 in all the above directions.</em>
