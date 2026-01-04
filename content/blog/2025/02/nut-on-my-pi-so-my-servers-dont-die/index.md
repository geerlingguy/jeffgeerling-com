---
nid: 3444
title: "NUT on my Pi, so my servers don't die"
slug: "nut-on-my-pi-so-my-servers-dont-die"
date: 2025-02-24T16:00:57+00:00
drupal:
  nid: 3444
  path: /blog/2025/nut-on-my-pi-so-my-servers-dont-die
  body_format: markdown
  redirects:
    - /blog/2025/i-have-nut-on-my-pi-so-my-servers-dont-die
aliases:
  - /blog/2025/i-have-nut-on-my-pi-so-my-servers-dont-die
  - /comment/35106
tags:
  - homelab
  - nut
  - power
  - rack
  - raspberry pi
  - server
  - sysadmin
  - ups
---

{{< figure src="./nut-pi-rack.jpg" alt="NUT Pi in Rack" width="700" height="394" class="insert-image" >}}

A few weeks ago, [power went out for the first time in my studio space](https://www.youtube.com/watch?v=fLt5YhOubxk&t=207s), and that meant all my servers just had power cut with no safe shutdown.

Handling power outages is never a top priority... until it's the _only_ priority! And by then it's usually too late! Luckily for me, no data was lost, and my servers all came back up safely.

This week the power company emailed and said they'd be cutting power for maintenance next week, but they don't have an exact time. So it's even more excuse to finally set up NUT on a Pi!

NUT, short for [Network UPS Tools](https://networkupstools.org), is an open source tool you run on an old Pi or whatever old computer, and it monitors UPSes like the Lowell Power UPS in my main rack. NUT clients, then, can monitor the UPS _through_ the Pi, and safely shut down before the battery is depleted.

## Video

I have a full video going over my setup, along with a walkthrough of my end-to-end UPS power fail test, over on my YouTube channel. You can also watch it below (or scroll past and read through the instructions on the blog!):

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/yFnItLSRpLI" frameborder='0' allowfullscreen></iframe></div>
</div>

## Setting up a Pi as a NUT server

First, flash Pi OS (I used Pi OS Bookworm 'Lite') to a microSD card and plug that into your Pi. Boot up the Pi, make sure you can log into it over SSH, and then begin the process of setting up NUT.

For my Pi, I mounted it in the back of my rack with [this Raspberry Pi Rack Mount on Printables](https://www.printables.com/model/843677-raspberry-pi-5-rack-mount-right-sided) (printed in ASA), and I just powered it off a USB-C power adapter, which is plugged into the PDU behind my rack UPS.

Since NUT doesn't require much in the way of resources, you can run it on most any Pi model—the Pi I used was an old Compute Module 4 with 1 GB of RAM I had laying around, mounted in a [BigTreeTech Pi4B CM to Pi 4 adapter board](https://amzn.to/4gIYGvX).

### Configuring a UPS for NUT

Before doing anything else, install NUT with `sudo apt install -y nut`. This will install `nut-client`, `nut-server`, and other UPS tools you will use later

Then, assuming you have your UPS plugged into a USB port on your Raspberry Pi, run `nut-scanner`, and see what it finds:

```
$ sudo nut-scanner -U
Scanning USB bus.
[nutdev1]
	driver = "nutdrv_qx"
	port = "auto"
	vendorid = "0665"
	productid = "5161"
	product = "UPS"
	bus = "001"
```

You can take those values, and use them in your UPS configuration (assuming you just have one UPS connected). Edit NUT's `ups.conf` file with `sudo nano /etc/nut/ups.conf` and add your UPS configuration. For example:

```
[server-room-rack]
    driver = nutdrv_qx
    product = UPS
    desc = "Server Room Lowell Power Rack UPS"
    port = auto
    vendorid = 0665
    productid = 5161
    bus = 001
```

The name of the UPS (in my case, `server-room-rack`) should be ASCII characters with no spaces or special characters besides `-`.

Save that file and close it.

> **Note**: If you can't connect to your UPS, or the scanner doesn't find it, read through the [NUT documentation on UPS drivers](https://networkupstools.org/docs/man/nutupsdrv.html) to see if you might be missing something. You don't _have_ to use a USB connection, though it's the most common across all the modern UPSes I've used.

### Setting up NUT server

To make the Pi run as a NUT Server, and not just for local monitoring, edit the `upsd.conf` file with `sudo nano /etc/nut/upsd.conf` and add a `LISTEN` directive:

```
LISTEN 0.0.0.0 3493
```

Save that file and close it.

You'll also need to define a list of NUT users who will be able to manage the UPS either locally or over the network. Edit `upsd.users` with `sudo nano /etc/nut/upsd.users` and add something like the following:

```
[admin]
    password = ADMIN_PASSWORD_HERE
    actions = set
    actions = fsd
    instcmds = all
    upsmon primary

[observer]
    password = OBSERVER_PASSWORD_HERE
    upsmon secondary
```

The `admin` user will have full access to do anything, including immediately send out a shutdown command (`fsd`) to all connected systems. So... don't use that account for all the clients, it's just for admin tasks!

The `observer` account is what I use on all my NUT clients to connect back and monitor the main UPS.

Configure the UPS monitor on the NUT Pi by editing `upsmon.conf`, using `sudo nano /etc/nut/upsmon.conf`:

```
# Make sure you use your actual admin password...
MONITOR server-room-rack@localhost 1 admin ADMIN_PASSWORD_HERE primary

# You might also want to configure FINALDELAY and set it to a period long enough
# for your servers to all shut down, prior to the primary node shutting down and
# triggering the UPS to switch off its load, e.g. for 3 minutes:
FINALDELAY 180
```

Save and close the file, then edit `nut.conf` (with `sudo nano /etc/nut/nut.conf`) and change the `MODE` from `none` (default) to `netserver`:

```
MODE=netserver
```

Restart the NUT server and make sure it is enabled at system boot:

```
sudo systemctl restart nut-server
sudo systemctl enable nut-server
sudo systemctl restart nut-monitor
sudo systemctl enable nut-monitor
```

### Confirm NUT works

Check if you can see all your UPS details with `upsc [ups-name-here]`:

```
$ upsc server-room-rack
Init SSL without certificate database
battery.charge: 24
battery.energysave: no
battery.packs: 1
battery.protection: yes
battery.runtime: 0
battery.voltage: 50.60
battery.voltage.nominal: 48.0
device.model: LILVX2K0
device.type: ups
driver.name: nutdrv_qx
...
```

If you want to see a fancy web UI, a few of those exist (like [nut_webgui](https://github.com/SuperioOne/nut_webgui)), but in my case, I have Home Assistant, and monitor all the vitals in there. Home Assistant has an [official NUT integration](https://www.home-assistant.io/integrations/nut/) that automatically identified the NUT Pi over the network after I added the Integration to my HA install. All I had to do was add the `observer` username and password.

Then I created a simple card with the most important UPS statistics in one of my HA dashboards:

{{< figure src="./nut-home-assistant-ups-card.png" alt="NUT - Home Assistant UPS card" width="400" height="397" class="insert-image" >}}

The YAML for that card, in case you want to replicate it, is:

```yaml
type: vertical-stack
title: Server Room Rack UPS
cards:
  - type: history-graph
    entities:
      - name: Status
        entity: sensor.server_room_rack_status
    hours_to_show: 4
  - type: gauge
    entity: sensor.server_room_rack_battery_charge
    name: Battery Charge
    severity:
      green: 50
      yellow: 20
      red: 0
```

Just to show what the Docker-base [nut_webgui](https://github.com/SuperioOne/nut_webgui) looks like, though, I launched an instance on my Mac (localhost) using the command:

```
docker run \
  -e UPSD_ADDR=10.0.2.10 \
  -e UPSD_USER=observer \
  -e UPSD_PASS=PASSWORD_HERE \
  -p 9000:9000 \
  ghcr.io/superioone/nut_webgui:latest
```

And it has a pretty complete dashboard with stats for all connected UPSes. Clicking on one brings up a fancy details page with every metric and configurable option available:

{{< figure src="./nut-web-monitor-docker.png" alt="NUT Web Monitor running in Docker" width="700" height="394" class="insert-image" >}}

## Setting up a NUT Client on other nodes

The NUT Server will shut down last, after sending an `fsd` notice out to all connected clients. But your other servers need to be configured with `nut-client` before they will connect!

On each of your servers you want to have shut down cleanly with your primary UPS, set up the client and configure it to connect back:

  1. Install `nut-client`: `sudo apt install nut-client`
  2. Verify connection to server: `upsc server-room-rack@IP_ADDRESS` (where `IP_ADDRESS` is the IP of the NUT Pi server)
  3. Configure NUT's UPS monitor for client: `sudo nano /etc/nut/upsmon.conf` and add a `MONITOR` line:
    - `MONITOR server-room-rack@IP_ADDRESS 1 observer PASSWORD secondary` (where `IP_ADDRESS` is the IP of the NUT Pi server, and `PASSWORD` is the observer password)
  4. Edit `/etc/nut/nut.conf` and set `MODE=netclient` (change from default `none`)
  5. Restart and enable `nut-client`:
    - `sudo systemctl restart nut-client`
    - `sudo systemctl enable nut-client`

Each server where you have `nut-client` running should be tracking the primary NUT server, and _should_ shut down if it sends out an `fsd` notice.

## Monitoring NUT server and clients

If you want more verbose logs, you can set the `NUT_DEBUG_LEVEL` environment variable when restarting the NUT services, but by default, it will log important notifications and things like the UPS going from 'online' to 'battery'.

```
# On server
journalctl -f -u nut-server

# On client
journalctl -f -u nut-monitor
```

## Managing the connected UPS

On the NUT Pi server, you can use `upscmd` to manage the connected UPS, using the `admin` user, for example:

```
# List commands supported on this UPS
upscmd -l server-room-rack

# Run a quick battery test (requires password)
upscmd -u admin server-room-rack test.battery.start.quick
```

### Debian 12 upsmon bug

When I did this last command, I unintentionally triggered a bug with the current version of `nut-client` on Debian 12... if a UPS self-test is run, the 'CAL' flag is set (calibration), and while it's set, any critical UPS battery alerts are ignored! (See the [original NUT bug report](https://github.com/networkupstools/nut/issues/2168).)

There's a bug report in Debian currently: [CAL flag in UPSMON never cleared, shutdown procedure will not be triggered](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1056190), and one workaround is to restart `nut-client` (`sudo systemctl restart nut-client`) on a cron job, maybe every hour, or if you know your UPS self-test schedule, immediately following.

## Testing NUT

There are three different layers of testing you can do, to verify NUT is running correctly.

> **NOTE**: These options could result in data loss! Make sure you're not doing any critical activities on the systems while you're testing your power setup...

### 1 - NUT Debug / test mode

I... never tried this, but apparently you can do a 'soft test' following the instructions in Dan Langille's blog: [nut – testing the shutdown mechanism](https://dan.langille.org/2020/09/10/nut-testing-the-shutdown-mechanism/)

### 2 - Live test of NUT without unplugging UPS

You can trigger the `fsd` event manually on the NUT Pi server with:

```
upsmon -c fsd
```

That will immediately emulate the condition of the UPS status `OB LB` (On Battery / Low Battery), which tells all connected systems to run their shutdown command.

### 3 - Live end-to-end test with UPS on battery

Unplug your UPS. Monitor the stats with `upsc` (like `upsc server-room-rack`, for mine), and validate the various parameters are correct for your UPS.

Wait a while, and keep an eye on metrics like:

```
$ upsc server-room-rack
battery.charge: 32
...
battery.voltage: 51.30
...
ups.load: 11
...
ups.status: OL
```

At some point, the UPS will have a status like `OL LB` or `ALARM OB`, and NUT _should_ trigger shutdowns on all your connected NUT clients.

## Conclusion

There are a number of options you can set on both the NUT server and clients which I've not covered in this post. The documentation is pretty dense, but readable.

The defaults are good for _most_ use cases, but you might want to trigger an FSD earlier, before your UPS goes into 'LB' or Low Battery state. This might be useful if you have a high-power-draw server that takes 5-10 minutes to shut down. You could have it shut down when the battery's at 50% or has X minutes remaining, instead of waiting to the very end.

I'm automating my NUT setup, so it's easier to apply uniformly against all my servers, and here are the Ansible projects I'm using:

  - [Pi NUT project on GitHub](https://github.com/geerlingguy/pi-nut)
  - [`geerlingguy.nut_client` Ansible role](https://github.com/geerlingguy/ansible-role-nut_client)
