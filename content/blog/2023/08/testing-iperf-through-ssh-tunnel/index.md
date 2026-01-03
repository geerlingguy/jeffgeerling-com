---
nid: 3303
title: "Testing iperf through an SSH tunnel"
slug: "testing-iperf-through-ssh-tunnel"
date: 2023-08-16T14:11:47+00:00
drupal:
  nid: 3303
  path: /blog/2023/testing-iperf-through-ssh-tunnel
  body_format: markdown
  redirects: []
tags:
  - benchmarking
  - iperf3
  - linux
  - networking
  - performance
  - ssh
  - testing
---

I recently had a server with some bandwidth limitations (tested using `scp` and `rsync -P`), where I was wondering if the problem was the data being transferred, or the server's link speed.

The simplest way to debug and verify TCP performance is to install `iperf3` and run an iperf speed test between the server and my computer.

On the server, you run `iperf3 -s`, and on my computer, `iperf3 -c [server ip]`.

But `iperf3` requires port 5201 (by default) to be open on the server, and in many cases—especially if the server is inside a restricted environment and only accessible through SSH (e.g. through a bastion or limited to SSH connectivity only)—you won't be able to get that port accessible.

So in my case, I wanted to run iperf through an SSH tunnel. This isn't ideal, because you're testing the TCP performance _through an encrypted connection_. But in this case both the server and my computer are extremely new/fast, so I'm not too worried about the overhead lost to the connection encryption, and my main goal was to get a performance baseline.

Without further ado, here's how I set up the SSH-tunneled iperf3 run:

On my machine, I set up a tunnel for port 7001:

```
$ ssh -p [ssh port on server] -L7001:localhost:7001 jeffgeerling@[server ip]
```

Then, SSH'ed into the server, I started an instance of `iperf3` listening on port 7001:

```
$ iperf3 -s -p 7001
```

Finally, on my machine, I ran some iperf3 tests:

```
$ iperf3 -c localhost -p 7001
Connecting to host localhost, port 7001
[  7] local ::1 port [port here] connected to ::1 port 7001
[ ID] Interval           Transfer     Bitrate
[  7]   0.00-1.00   sec  23.9 MBytes   200 Mbits/sec                  
[  7]   1.00-2.00   sec  20.9 MBytes   176 Mbits/sec   
```

[This answer](https://unix.stackexchange.com/a/303594/16194) on the Unix stack exchange was helpful in writing this post, and it also goes one level deeper showing how to tunnel through a bastion server instead of just directly through SSH to the server.
