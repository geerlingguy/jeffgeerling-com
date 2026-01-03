---
nid: 2405
title: "Simple iptables rules for a typical LAMP server"
slug: "simple-iptables-rules-typical"
date: 2012-03-16T04:07:14+00:00
drupal:
  nid: 2405
  path: /blogs/jeff-geerling/simple-iptables-rules-typical
  body_format: full_html
  redirects: []
tags:
  - hosting
  - iptables
  - lamp
  - linux
  - security
  - server
  - vps
aliases:
  - /blogs/jeff-geerling/simple-iptables-rules-typical
---

[<strong>Edit</strong>: I'm leaving this post up for historical reasons, but I've since modified the way I build my iptables firewalls—I typically add the rules I need from the command line one by one, then use CentOS's <code>service iptables save</code> command (available in CentOS > 6.2) to save the rules so they'll persist after a restart.]

I've seen a ton of iptables configurations on the Internet, and none of them really got to the heart of what I need to do for the majority of my LAMP-based web servers (hosted on Linode, HostGator, Hot Drupal, and elsewhere). For these servers, I just need a really simple set of rules that restricts all incoming traffic except for web (port 80/443 for http/https traffic), ssh (usually port 22), smtp (port 25), and icmp ping requests.

The script below (save it as 'firewall.bash', <code>chmod u+x</code> it to make it executable, and run it with <code>$ sudo /path/to/firewall.bash</code>, then test your server (access websites, log on to it from another Terminal session, ping it, etc., and make sure that's all working)):

```
#!/bin/bash
#
# Script to set up iptables firewall on a Linux machine.
#
# Drop spoofed packets.
if [ -e /proc/sys/net/ipv4/conf/all/rp_filter ]
then
for filter in /proc/sys/net/ipv4/conf/*/rp_filter
do
echo 1 > $filter
done
fi
#
# Remove all rules and chains
/sbin/iptables -F
/sbin/iptables -X
#
# Accept traffic from loopback interface (localhost)
/sbin/iptables -A INPUT -i lo -j ACCEPT
#
# Accept SSH traffic (for administration)
/sbin/iptables -A INPUT -p tcp --dport ssh -j ACCEPT
#
# Accept port traffic on ports 22, 25, 80, 443 (SSH, SMTP, Apache http/https)
/sbin/iptables -A INPUT -p tcp -m multiport --destination-ports 22,25,80,443 -j ACCEPT
#
# Accept icmp ping requests
/sbin/iptables -A INPUT -p icmp -j ACCEPT
#
# Allow established connections:
/sbin/iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
#
# Log EVERYTHING (ONLY for Debug)
# /sbin/iptables -A INPUT -j LOG
#
# Uncomment to log the rest of the incoming messages (all of which are dropped)
# with a maximum of 15 log entries per minute
# /sbin/iptables -A INPUT -m limit --limit 15/minute -j LOG --log-level 7 --log-prefix "Dropped by firewall: "
#
# Drop all other traffic
/sbin/iptables -A INPUT -j DROP
/sbin/iptables -P FORWARD DROP
#
# End message
echo " [End iptables rules setting]"
```

Notes:
<ul>
<li>This script assumes iptables is located at /sbin/iptables. If it's not there, adjust the path accordingly.</li>
<li>Show your current iptables configuration by running <code>$ sudo iptables -L</code></li>
<li>Flush your iptables configuration back to allowing any traffic, anywhere, by running the attached bash script (rename to flush_iptables.bash)</li>
</ul>

The comments should hopefully help explain everything that's going on here, but for a fuller explanation of iptables, <a href="http://www.linuxhomenetworking.com/wiki/index.php/Quick_HOWTO_:_Ch14_:_Linux_Firewalls_Using_iptables">read here</a>. Note that I take no responsibility for the security of your server! Use at your own risk.
