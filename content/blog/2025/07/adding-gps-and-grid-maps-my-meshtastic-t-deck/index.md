---
nid: 3479
title: "Adding GPS and off-grid maps to my Meshtastic T-Deck"
slug: "adding-gps-and-grid-maps-my-meshtastic-t-deck"
date: 2025-07-16T21:08:03+00:00
drupal:
  nid: 3479
  path: /blog/2025/adding-gps-and-grid-maps-my-meshtastic-t-deck
  body_format: markdown
  redirects:
    - /blog/2025/adding-gps-my-meshtastic-t-deck
    - /blog/2025/adding-gps-and-maps-my-meshtastic-t-deck
aliases:
  - /blog/2025/adding-gps-my-meshtastic-t-deck
  - /blog/2025/adding-gps-and-maps-my-meshtastic-t-deck
tags:
  - gps
  - lora
  - mesh
  - meshtastic
  - position
  - radio
  - tutorial
---

Meshtastic is still a bit touch-and-go sometimes, but the [St. Louis area Mesh](https://meshstl.org) has grown quite a bit, to the point I can regularly mesh with 10-30 other nodes. So far we can't quite get the entire metro covered wirelessly, but there are a few gaps MQTT is connecting currently.

{{< figure src="./meshmap-stl.jpg" alt="Meshmap.net - St. Louis Missouri" width="700" height="394" class="insert-image" >}}

One thing I hadn't really thought about—but can be useful, especially for [visualizing the mesh](https://meshmap.net)—is GPS positioning on the mesh node itself.

You can already [set a fixed position](https://meshtastic.org/docs/configuration/radio/position/) using your phone's GPS, if you connect to your device over Bluetooth or WiFi (or USB serial), but that means you're still tied to another device, and for a mesh network, I like having it entirely independent. Which is why I think [devices like the T-Deck are the best representation of what Meshtastic can be](/blog/2024/realizing-meshtastics-promise-t-deck).

## Adding GPS to my T-Deck

I noticed there was a Grove port on the side of the T-Deck. The port has four pins, labeled TX, RX, VCC, and GND. And conveniently, super-cheap GPS modules like the [ATGM336H](https://amzn.to/3IxMdzN) _also_ have TX, RX, VCC, and GND pins.

{{< figure src="./gps-module-t-deck-soldered.jpg" alt="GPS Module soldered onto back of T-Deck" width="700" height="394" class="insert-image" >}}

I bought a couple ATGM336H modules off Amazon, and soldered some jumper wires to the pins on the T-Deck (so everything still fits inside my [3D-printed T-Deck case](https://www.printables.com/model/741124-lilygo-t-deck-td1-case):

  - TX to RX
  - RX to TX
  - VCC to VCC
  - GND to GND

Then I used some [kapton (polyimide) tape](https://amzn.to/457qaZm) to hold things down, and secure the little GPS patch antenna inside the GPS antenna cavity at the top of the case, and re-assembled everything.

{{< figure src="./gps-module-kapton-polyimide-tape-t-deck-case.jpg" alt="GPS Module held in place with kapton tape or polyimide" width="700" height="394" class="insert-image" >}}

If it looks hacky and it works... well, at least it works!

## Enabling GPS in Meshtastic

I plugged the T-Deck into my Mac with a USB cable, opened Chrome, and launched [client.meshtastic.org](https://client.meshtastic.org).

I created a new Serial connection to the device (listed as `#0`), and then went to the 'Config > Position' tab. In there, I set:

  - GPS Mode: `ENABLED`
  - Receive Pin: `44`
  - Transmit Pin: `43`

And then clicked the floppy disk / save icon in the top right.

After the device reboots, it will start trying to get a GPS fix. In my studio, I was unable to get a fix near my desk.

## Map Tile Data

Before I went outside, I grabbed some map tile data, since the [Meshtastic Device UI uses map tile data](https://github.com/meshtastic/device-ui/blob/master/maps/README.md) to render an on-device map without Internet access.

For my local area (St. Louis, MO), I set up [tdeck-maps](https://github.com/JustDr00py/tdeck-maps):

```
# Install t-deck maps and dependencies
$ python3 -m pip install pillow requests
$ git clone https://github.com/JustDr00py/tdeck-maps.git
$ cd tdeck-maps
```

Then I used it to download the tiles for my city:

```
# Download tiles for a city
$ python3 meshtastic_tiles.py --city "St. Louis, Missouri" --min-zoom 8 --max-zoom 12
Found St. Louis: 38.6280, -90.1910
Generating tiles for: custom area
Generating tiles for bounds: N:38.80820798018018, S:38.44784761981982, E:-90.01083521981981, W:-90.37119558018018
Zoom levels: 8 to 12
Source: osm
Zoom 8: 1 tiles (x:63-63, y:98-98)
Zoom 9: 1 tiles (x:127-127, y:196-196)
Zoom 10: 4 tiles (x:254-255, y:392-393)
Zoom 11: 9 tiles (x:509-511, y:784-786)
Zoom 12: 30 tiles (x:1019-1023, y:1568-1573)
Total tiles to process: 45
Processing zoom level 8 (x:63-63, y:98-98)...
Processing zoom level 9 (x:127-127, y:196-196)...
Processing zoom level 10 (x:254-255, y:392-393)...
Processing zoom level 11 (x:509-511, y:784-786)...
Processing zoom level 12 (x:1019-1023, y:1568-1573)...
Completed! Downloaded 45/45 tiles
Metadata saved to: tiles/metadata.json
```

> Note: If there are a lot of map tiles to download, you may get rate-limited... You can narrow down the zoom levels to like 8-10 if you just want more general coverage. If you just want some basic regional maps, download [pre-formatted map data from the `meshtastic/device-ui` repo](https://github.com/meshtastic/device-ui/tree/master/maps).

Copy the `tiles` folder into a folder named `maps` on a freshly-formatted microSD card (I used a [SanDisk Ultra 16GB microSD card](https://amzn.to/4lBazaq), formatted as FAT32). Rename the `tiles` folder to whatever you want to call this map tile set (e.g. `osm` for Open Street Maps). Eject it from your computer, and stick it in the microSD card slot on the left side of the T-Deck.

Then reset (or power off and power on) the T-Deck, and head to the 'Maps' section.

## Location on the T-Deck

{{< figure src="./gps-map-t-deck-meshtastic-stlouis-missouri.jpg" alt="T-Deck showing meshtastic UI with St. Louis MO map tiles" width="700" height="394" class="insert-image" >}}

You may need to zoom out a bit to see any tile data. Also, if you don't have a GPS lock, the T-Deck will likely center you in some part of the map that's far from where you have rendered tile data.

If you walk outside, assuming you wired up your GPS module correctly, you should see yourself on a map. The home screen even shows how many satellites are visible, if you scroll down to the position section.

It'd be helpful if there was a pre-built download with the entire planet, then some packs for different regions that were updated every few months, but bandwidth isn't free—so you'll have to find your own ways to get local data for higher zoom levels (if you want it)!
