---
nid: 3085
title: "Setting up a Pi for remote Internet connection monitoring"
slug: "setting-pi-remote-internet-connection-monitoring"
date: 2021-03-24T21:16:56+00:00
drupal:
  nid: 3085
  path: /blog/2021/setting-pi-remote-internet-connection-monitoring
  body_format: markdown
  redirects: []
tags:
  - internet
  - monitoring
  - ssh
  - starlink
  - tunnel
---

So... recently I acquired a Starlink 'Dishy', and I'm going to be installing it at a rural location near where I live, but since it's a bit of a drive to get to it, I wanted to set up a Raspberry Pi to monitor the Starlink connection quality over time.

{{< figure src="./internet-monitoring-dashboard.jpg" alt="Internet monitoring dashboard in Grafana" width="700" height="459" class="insert-image" >}}

I know the Starlink app has its own monitoring, but I like to have my own fancy independent monitoring in place too.

The wrinkle with a Starlink-based Internet connection, though, is that SpaceX is using [Carrier-Grade NAT (CGNAT)](https://en.wikipedia.org/wiki/Carrier-grade_NAT) on their network, so there won't be any kind of IPv4 address I could reach the Pi at, nor does SpaceX yet have IPv6 set up in their network.

So to make remote access possible, I would have to find a way to have the Pi reach out to one of my servers with a persistent connection, then I could 'tunnel' through that server from other locations to reach the Pi.

## Internet Monitoring on the Pi

For the first task, I had plans to build a Prometheus and Grafana-based dashboard for metrics on the Pi, and run everything inside Docker containers. So I started looking into it, and found someone already did it for me—I found the [maxandersen/internet-monitoring](https://github.com/maxandersen/internet-monitoring) project on GitHub, and used that (though I made a [slightly modified fork](https://github.com/geerlingguy/internet-monitoring) that works better on Raspberry Pi).

To prep my Pi, I had to make sure I had Docker installed, so I followed the steps:

```
wget https://get.docker.com -O get-docker.sh
sudo sh get-docker.sh
```

Once that was done, I added my `pi` user to the Docker group:

```
sudo usermod -aG docker pi
```

I logged out and logged back in so the new group would apply, and installed docker-compose:

```
sudo apt-get install -y libffi-dev libssl-dev python3-dev python3-pip git
sudo pip3 install docker-compose
```

Next, I cloned the internet-monitoring project from my fork (which is tuned for Raspberry Pi) and ran the included `docker-compose` file:

```
git clone https://github.com/geerlingguy/internet-monitoring
cd internet-monitoring
docker-compose up -d
```

This exposes a number of ports on the Pi—so make sure you lock things down as you see fit on your own network—but the most important is the Grafana URL, which is:

```
http://10.0.100.127:3030/
```

(Substitute your Pi's IP address or hostname for the `10.x` IP address I am using here.)

If you visit that URL and log in with the default credentials (`admin` / `wonka`—configure the default password in the `grafana/config.monitoring` file), then you should be able to go to the dashboards (go to Dashboards > Manage), and click on the 'internet connection' dashboard.

It could take 5-10 minutes for statistics to start populating; be sure to refresh the dashboard (or turn on auto-refresh) to see the metrics start coming in.

## SSH to the Pi through a tunnel

So the monitoring was one half of the task; the other part is being able to log into the Pi remotely and view Grafana from my home.

To do that, I was going to set up `autossh`, to configure up a persistent SSH connection from the Pi to a server under my control outside the local Starlink network. However, I noticed that plain old `ssh` can be used in the same fashion, when paired with a properly-configured systemd service.

### Exchanging SSH keys

The first thing I did was create an SSH key on my Pi under the `pi` user account using the following command (using all the defaults when prompted):

```
ssh-keygen -t ed25519 -C "pi-starlink"
```

After the key is generated, run `cat ~/.ssh/id_ed25519.pub` to see the public key. Copy that key and paste it in a new line in the `~/.ssh/authorized_keys` file on the remote host under your control that you'll use for the persistent tunnel.

Once it was added, I tried to connect to the remote host from the Pi using an SSH tunnel:

```
/usr/bin/ssh -NT -o ExitOnForwardFailure=yes -o ServerAliveInterval=60 -o ServerAliveCountMax=3 -p 22 -R 6666:localhost:22 -i ~/.ssh/id_ed25519 geerlingguy@myserver.com
```

> See an [explanation of this SSH command](https://explainshell.com/explain?cmd=ssh+-NT+-o+ExitOnForwardFailure%3Dyes+-o+ServerAliveInterval%3D60+-o+ServerAliveCountMax%3D3+-p+22+-R+6666%3Alocalhost%3A22+-i+%7E%2F.ssh%2Fid_ed25519+geerlingguy%40myserver.com) from explainshell.com.

I was prompted to accept the host key the first time I connected, so I entered `yes`, and then was connected to the server (there was no output or prompt, it just hangs on the terminal until you press Ctrl-C to close the connection).

So I know the connection from my Pi to my remote host works, yay!

### Connecting back to the Pi through the remote host

Next, I created another key to connect from the remote host back to the Pi. I did the same thing as earlier—created a key on the remote host under user `geerlingguy` with `ssh-keygen`, copied out the contents of the `.pub` file, and pasted them into the end of the `.ssh/authorized_keys` file in the `pi` user account on the Pi.

Now, on the remote host, I can `ssh` into the Pi through the local tunnel (assuming it's still running from the Pi):

```
ssh -p 6666 pi@127.0.0.1
```

You can press Ctrl-C to quit out of the `ssh` tunnel on the Pi at this point.

### Set up the SSH tunnel on boot

With that done, the next step is to make sure the tunnel is configured to run at system boot, and to reconnect if the connection is dropped for whatever reason.

To do that, I used a systemd service, which is created by adding a file like so:

```
sudo nano /etc/systemd/system/ssh-tunnel.service
```

With the following inside:

```
[Unit]
Description=SSH tunnel for Raspberry Pi remote access.
After=network-online.target

[Service]
User=pi
ExecStart=/usr/bin/ssh -NT -o ExitOnForwardFailure=yes -o ServerAliveInterval=60 -o ServerAliveCountMax=3 -p 22 -R 6666:localhost:22 -i ~/.ssh/id_ed25519 geerlingguy@myserver.com
RestartSec=5
Restart=always

[Install]
WantedBy=multi-user.target
```

Make sure you change the ports, username, and server from the above example to match your own values.

Enable and start the service:

```
sudo systemctl daemon-reload
sudo systemctl enable ssh-tunnel
sudo systemctl start ssh-tunnel
```

At this point, the tunnel should be running, so confirm it is by connecting to the Pi from the remote host again:

```
ssh -p 6666 pi@127.0.0.1
```

If it's not working, check what went wrong with `systemctl status ssh-tunnel`.

## View the Internet Monitoring dashboard remotely

Being able to log into the Pi via SSH remotely is nice, but as a final step, I wanted to be able to view the Internet connection monitoring dashboard in my browser remotely as well.

First I manually started a tunnel between the Pi's port `3030` and the remote host, with the command:

```
ssh -NT -o ExitOnForwardFailure=yes -o ServerAliveInterval=60 -o ServerAliveCountMax=3 -p 22 -R 3030:localhost:3030 -i ~/.ssh/id_ed25519 geerlingguy@myserver.com
```

I left that running, then on my _local_ workstation, I created a _separate_ tunnel to the remote host:

```
ssh -A -t geerlingguy@myserver.com -L 3030:127.0.0.1:3030 -N
```

Then I accessed `http://localhost:3030/` in my browser and voila! There was Grafana!

When finished, I was sure to press Ctrl-C in my local tunnel, as well as in the remote tunnel on the Pi. Then I disconnected from the remote server and all was well!

## Rebooting the Pi every night for fun and profit

The last thing I did on this Pi was added an automatic reboot every night at 2 a.m. It might be online for days or weeks where someone wouldn't be able to log in locally and reboot it, so I wanted to be certain if any really weird things happened, it could reboot itself and get back into a mostly-happy state on its own.

This is a form of percussive maintenance that I wish I didn't have to do, but it's easier this than driving the distance to reboot the thing by hand if I need to.

I ran `sudo crontab -e` to edit the root user's cron file, and added the line:

```
0 2 * * * sudo shutdown -r
```

This reboots the server at 2 a.m. every day, and uses `shutdown -r` with no argument, which is a little more polite than `reboot` or `shutdown -r now`, because it emits a warning to any logged in users that the reboot is imminent.

## Conclusion

I'll be testing out this setup for the next few months. If there are any things that need changing or end up not working so well, I'll be sure to update the post!
