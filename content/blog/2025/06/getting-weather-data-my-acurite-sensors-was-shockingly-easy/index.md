---
nid: 3473
title: "Getting weather data from my Acurite sensors was shockingly easy"
slug: "getting-weather-data-my-acurite-sensors-was-shockingly-easy"
date: 2025-06-28T01:46:38+00:00
drupal:
  nid: 3473
  path: /blog/2025/getting-weather-data-my-acurite-sensors-was-shockingly-easy
  body_format: markdown
  redirects: []
tags:
  - acurite
  - home assistant
  - nooelec
  - rtl-sdr
  - sdr
  - weather
  - weewx
  - wireless
---

I've had a Pi and SDR earmarked for 'getting weather data from my weather station' for a long time now. I don't know why I waited so long, because it was shockingly easy.

I have a [Acurite 5-in-1 weather station (with separate lightning detector)](https://amzn.to/44p0yFV) mounted about 15' in the air in my back yard. It comes with a fancy little LCD display to show all the stats it transmits over the 433 MHz wireless frequency.

But I want to ingest that data into my Home Assistant installation, so I can have better access to historical data, set up alerts (like if wind speed is above 50 mph, or there's lightnining less than 10 miles away), etc.

I'll work on the HA integration later, likely using MQTT. But for now, just getting the data to decode on a Raspberry Pi 5 was quick:

  1. Plug my [Nooelec NESDR](https://amzn.to/46k7Yga) into my Pi, and the cheap dipole antenna that came in the kit into the NESDR's antenna jack
  2. Install [`rtl_433`](https://github.com/merbanan/rtl_433) on the Pi: `sudo apt install -y rtl-433`
  3. Run it: `rtl_433`

Bingo! It automatically picked up both of my Acurite sensors, and started displaying the data every few seconds:

{{< figure src="./rtl-433-acurite-weather-data-pi-5.jpg" alt="RTL 433 Acurite weather data on Jeff's Pi 5" width="700" height="306" class="insert-image" >}}

It's a rare treat to just install something and have it work immediately. Especially if it uses RF!

## Bonus - weewx

I will still be working to integrate into Home Assistant, but at least for now, I'm running WeeWX on my Pi so I have a full web dashboard for the Acurite sensors. Installation was easy, following the [WeeWX documentation for Debian](https://weewx.com/docs/5.1/quickstarts/debian/):

```
# Add the WeeWX GPG key.
sudo apt install -y wget gnupg
wget -qO - https://weewx.com/keys.html | \
    sudo gpg --dearmor --output /etc/apt/trusted.gpg.d/weewx.gpg

# Set up the WeeWX apt repository.
echo "deb [arch=all] https://weewx.com/apt/python3 buster main" | \
    sudo tee /etc/apt/sources.list.d/weewx.list

# Install WeeWX.
sudo apt update
sudo apt install -y weewx
```

The installer has a few prompts for setup. Complete those steps manually. I just entered the defaults for location; if you want to place it on a map, get the coordinates and altitude using a tool like [Elevation.place](https://elevation.place).

You can reconfigure weewx later with `sudo systemctl stop weewx`, then `weectl station reconfigure` (then `systemctl start` it again). Configuration is stored in `/etc/weewx/weewx.conf`.

To get WeeWX to use `rtl_433` to get sensor data, install the [`weewx-sdr` plugin](https://github.com/matthewwall/weewx-sdr):

```
sudo weectl extension install https://github.com/matthewwall/weewx-sdr/archive/master.zip
```

Confirm that you want to install it, then once it's done, configure the driver and restart WeeWX:

```
sudo weectl station reconfigure --driver=user.sdr --no-prompt
sudo systemctl restart weewx
```

At this point, WeeWX will have the plugin running but no data will get captured until you manually configure which sensors you want to use, in a `[[sensor_map]]` in the `/etc/weewx/weewx.conf` file. Follow the directions in the Installation section of the [weewx-sdr](https://github.com/matthewwall/weewx-sdr) README to do that.

Here is the configuration I used after monitoring my station to get the ID values (which... apparently can change when you change batteries, so beware!):

```
[SDR]
    driver = user.sdr
    [[sensor_map]]
        windDir = wind_dir.0C2D.Acurite5n1PacketV2
        windSpeed = wind_speed.0C2D.Acurite5n1PacketV2
        rain_total = rain_total.0C2D.Acurite5n1PacketV2
        outTemp = temperature.0C2D.Acurite5n1PacketV2
        outHumidity = humidity.0C2D.Acurite5n1PacketV2
        lightning_distance = distance.0008.AcuriteLightningPacket
        strikes_total = strikes_total.0008.AcuriteLightningPacket
```

If you have an Acurite lightning detector like I do, you may also need to [configure an `Accumulator` and `Corrections`](https://groups.google.com/g/weewx-user/c/DFY4QEIH2QY/m/3H38HxZWAAAJ) to the data so it displays correctly in WeeWx.

Even after all that, `weewx` will run under a `weewx` user account, which may not have access to the USB hardware you're using for `rtl_433`, so you need to add a `udev` rule to give permission.

Create a udev rule file with `sudo nano /etc/udev/rules.d/sdr.rules`, and put the following inside:

```
SUBSYSTEM=="usb",ATTRS{idVendor}=="0bda",ATTRS{idProduct}=="2832",MODE="0664",GROUP="weewx"
SUBSYSTEM=="usb",ATTRS{idVendor}=="0bda",ATTRS{idProduct}=="2838",MODE="0664",GROUP="weewx"
```

(The vendor and product IDs may differ depending on your SDR stick — the above values are for most cheap RTL-SDR and Nooelec sticks. Check yours with `lsusb`.)

Then restart the Pi entirely. You can live reload udev rules but restarting is honestly easier than remembering how to do that :)

Finally, after all that (and waiting 5+ minutes for the first report to be generated, we get a weather dashboard! On the same Pi, load up the `/var/www/html/weewx/index.html` file in your web browser, and you can browse the report locally:

{{< figure src="./weewx-dashboard-jeffgeerling-shrewsbury-acurite-sdr-433.jpg" alt="WeeWX Dashboard for Shrewsbury, MO" width="700" height="425" class="insert-image" >}}

If you want to serve it up to the local network, you can [use Apache or another webserver](https://github.com/weewx/weewx/wiki/Configure-a-web-server-(Apache,-NGINX-or-lighttpd)), but that exercise is left to the reader.

### Fixing Weewx soft lockups in rendering thread

After running this setup for a few months, I noticed Weewx must have a memory leak or some other bug, as CPU usage would often spike to 25% (one full CPU core at 100%) continuously, and then the reporting threads would lock up, leaving the rendered web content stale until a reboot.

The log messages (seen with `journalctl -u weewx`) would reveal:

```
Feb 19 22:55:27 pi-sdr weewxd[1167]: WARNING weewx.engine: Previous report thread has been running 896.363573551178 seconds.  Launching report thread anyway.
```

If I just restart `weewx` (with `sudo systemctl restart weewx`), after 5 minutes when it tries to update the report, it will show:

```
Feb 19 23:05:26 pi-sdr weewxd[963732]: INFO weewx.engine: Launch of report thread aborted: existing report thread still running
```

So to fix that, I decided to completely reboot the Pi every night at 2 AM. I ran `sudo crontab -e`, and added the following crontab entry:

```
0 2 * * * /usr/sbin/shutdown -r now
```

After saving this file, the Pi reboots itself every night. It's not ideal, but _so far_ it seems to work.
