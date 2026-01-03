---
nid: 2978
title: "Be careful, Docker might be exposing ports to the world"
slug: "be-careful-docker-might-be-exposing-ports-world"
date: 2020-03-15T17:29:59+00:00
drupal:
  nid: 2978
  path: /blog/2020/be-careful-docker-might-be-exposing-ports-world
  body_format: markdown
  redirects: []
tags:
  - docker
  - docker compose
  - firewall
  - iptables
  - ports
  - security
  - swarm
---

Recently, I noticed logs for one of my web services had strange entries that looked like a bot trying to perform scripted attacks on an application endpoint. I was surprised, because all the endpoints that were exposed over the public Internet were protected by some form of authentication, or were locked down to specific IP addresses—or so I thought.

I had re-architected the service using Docker in the past year, and in the process of doing so, I changed the way the application ran—instead of having one server per process, I ran a group of processes on one server, and routed traffic to them using DNS names (one per process) and Nginx to proxy the traffic.

In this new setup, I built a custom firewall using `iptables` rules (since I had to control for a number of legacy services that I have yet to route through Docker—someday it will all be in Kubernetes), installed Docker, and set up a Docker Compose file (one per server) that ran all the processes in containers, using ports like `1234`, `1235`, etc.

The Docker Compose port declaration for each service looked like this:

```
version: '3.7'
services:
  process_1234:
    ports:
      - "127.0.0.1:1234:1234"
```

Nginx was then proxying the requests routing DNS names like `service-1234.example.com` (on port 443) through to the process on port 1234, `service-1235.example.com` to port 1235, and so on.

I thought the following port declaration would only expose the port on localhost: `127.0.0.1:1234:1234`, according to the [Published ports documentation](https://docs.docker.com/config/containers/container-networking/#published-ports). And in normal circumstances, this does seem to work correctly (see a [test script proving this here](https://gist.github.com/geerlingguy/3dabf0ec3befb8c49bbed0ec7cd3d44c)).

But in my case, likely due to some of the other custom `iptables` rules conflicting with Docker's rules, Docker's iptables modifications exposed the container ports (e.g. `1234`) to the outside world, on the `eth0` interface.

I was scratching my head as to how external requests to `server-ip:1234` were working even though the port declaration was binding the port to the `localhost`, and I found that [I'm not the only person who was bumping into this issue](https://github.com/moby/moby/issues/22054#issuecomment-214496744). The fix, in my case, was to add a rule to the `DOCKER-USER` chain:

```
iptables -I DOCKER-USER -i eth0 ! -s 127.0.0.1 -j DROP
```

This rule, which I found buried in some documentation about [restricting connections to the Docker host](https://docs.docker.com/network/iptables/#restrict-connections-to-the-docker-host), drops any traffic from a given interface that's not coming from `localhost`. This works in my case, because I'm not trying to expose _any_ Docker containers to the world—if you wanted to have a mix of some containers open to the world, and others proxied, this wouldn't work for you.

After applying the rule, verify it's sticking by restarting your server and checking the `DOCKER-USER` chain:

```
$ sudo iptables -L
...
Chain DOCKER-USER (1 references)
target     prot opt source               destination         
DROP       all  -- !localhost            anywhere            
RETURN     all  --  anywhere             anywhere 
```

To be doubly-sure your firewall is intact, you can verify which ports are open (`-p-` says 'scan all ports, 1-65535) using `nmap`:

    sudo nmap -p- [server-ip-address]

This behavior is [confusing and not well-documented](https://github.com/moby/moby/issues/22054), even more so because a lot of these options behave subtly different depending on if you're using `docker run`, `docker-compose`, or `docker stack`. As another example of this maddening behavior, try figuring out how cpu and memory restrictions work with `docker run` vs. `docker-compose` v2, vs `docker-compose` v3 vs 'Swarm mode'!

I think I might be going crazy with the realization that—at least in some cases—Kubernetes is simpler to use than Docker, owing to its more consistent networking model.
