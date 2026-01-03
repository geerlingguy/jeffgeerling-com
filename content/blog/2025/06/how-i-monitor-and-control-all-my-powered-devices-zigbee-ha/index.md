---
nid: 3470
title: "How I monitor and control all my powered devices (Zigbee + HA)"
slug: "how-i-monitor-and-control-all-my-powered-devices-zigbee-ha"
date: 2025-06-14T14:01:00+00:00
drupal:
  nid: 3470
  path: /blog/2025/how-i-monitor-and-control-all-my-powered-devices-zigbee-ha
  body_format: markdown
  redirects: []
tags:
  - home assistant
  - power
  - smart home
  - zigbee
---

Any time I show power consumption graphs for the SBCs, computers, and servers I test, I get a number of comments asking for more details about the setup.

{{< figure src="./thirdreality-zigbee-smart-outlet-in-hand.jpg" alt="ThirdReality Zigbee Smart Outlet in Hand" width="700" height="394" class="insert-image" >}}

It's quite simple, really: using my [Home Assistant Yellow](https://www.home-assistant.io/yellow/)'s built-in Zigbee radio, I connect a number of [ThirdReality Zigbee Smart Outlets](https://amzn.to/45oROls) to it, and then I use [ApexCharts Cards](https://github.com/RomRider/apexcharts-card) to add graphs of power consumption over time on my Home Assistant dashboards.

I can then monitor power consumption, accumulate long-term energy use data, and even remotely power on and off devices, all through Home Assistant:

{{< figure src="./zigbee-apexcharts-home-assistant-power-graph.jpg" alt="Home Assistant power graph with ApexCharts card" width="700" height="394" class="insert-image" >}}

I've tried a number of smart outlets, including some cheap Z-Wave ones that would lose connection more frequently, and a set of [Shelly Plug US](https://amzn.to/4mZMTxu) WiFi outlets.

{{< figure src="./hl15-zigbee-power-monitor.jpg" alt="Zigbee graph of power information on Home Assistant with ThirdReality plug" width="700" height="394" class="insert-image" >}}

But Zigbee has been extremely reliable and consistent for me. And the ThirdReality outlets have survived on any kind of load, giving me pretty accurate results. I've been using them for over a year now on:

  - My clothes washer at home (peaking around 1500W of instant power draw)
  - My laser printer at home (peaking around 1200W)
  - My main 120 TB rackmount NAS (using a steady 110W of power, running 24x7)
  - My old retro Macs and Apple computers (they have high 'off' power draw, so I like to switch off the systems entirely when not in use)
  - My 3D printers (which I like to keep 'off' when not in use since they could be an attack vector connected to my network!)
  - SBCs, fans, mini PCs, etc.

Basically any time I want to monitor overall power consumption and/or switch it off remotely, I throw a ThirdReality outlet between the device and the wall.

{{< figure src="./matrix-power-meter-mpm-1010-geerling.jpg" alt="Matrix MPM-1010 Power Monitor on Jeff Geerling's desk" width="700" height="394" class="insert-image" >}}

Comparing measurements for a few devices between the ThirdReality reading and my [Matrix MPM-1010](https://amzn.to/441F41F), it seems like the ThirdReality outlets are always within a watt or so—even at very low power draw (like a Raspberry Pi pulling 2-3W at idle).

The two main drawbacks to these outlets _for me_ are:

  1. Because of Zigbee network limitations, you don't get 'real time' data, it only updates every couple seconds. So some types of power measurement requires a different device.
  1. When there's a firmware update (which is easy to apply thanks to Home Assistant), the update process takes about 1-2 minutes—and then the device reboot requires it power cycling. A little annoying for my NAS or the clothes washer (if it's in the middle of a cycle!), but not an issue on many devices (like lights).

Otherwise, I wholeheartedly recommend them. They certainly blew my expectations out of the water, and I've now installed 16 of them throughout my home and studio.

It's also nice they act as Zigbee repeaters, so if you distribute them through a space, you'll have a very strong Zigbee connection anywhere within! And the Home Assistant entity you get when you add one of these outlets includes stats for Volts, Amps, Power Factor, and a resettable kWh metric.

Here's the ApexCharts Card YAML I use for my 'Utility Power Monitor' which I almost always have plugged in at my desk, to get some metrics on new devices I test, either for review or so I have the data for a deployment:

```yaml
type: custom: apexcharts-card
apex_config:
  chart:
    height: 300px
header:
  show: true
  title: Power
  show_states: true
  colorize_states: true
update_interval: 3s
graph_span: 30m
yaxis:
  - min: 0
series:
  - entity: sensor.utility_power_monitor_power
    stroke_width: 2
    curve: stepline
    fill_raw: zero
    type: area
    opacity: 0.2
```

I usually buy the [ThirdReality Zigbee Outlets in a 4-pack](https://amzn.to/45oROls) on Amazon, I just buy a new pack when I'm down to the last one in the box.

See the smart outlets in action in my Level2Jeff video today:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed//URdTVrkz5jk" frameborder='0' allowfullscreen></iframe></div>
</div>

## How I added the 'Are you sure?' option

Someone on the YouTube video asked how I added the confirmation dialog to some of my switches in Home Assistant. Since I have my main NAS powered through one of these outlets, I don't want to accidentally shut it down by an accidental button press on the switch on my power dashboard!

In the Home Assistant card configuration, I manually edited the YAML to add a `tap_action` with a confirmation, like the following:

```yaml
  - show_name: true
    show_icon: true
    type: button
    tap_action:
      action: toggle
      confirmation:
        text: Toggle power on HL15 NAS01?
    entity: switch.hl15_switch
    name: HL15 NAS01
```
