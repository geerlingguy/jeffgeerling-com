---
nid: 3177
title: "Enable the external antenna connector on the Raspberry Pi Compute Module 4/5"
slug: "enable-external-antenna-connector-on-raspberry-pi-compute-module-45"
date: 2022-02-04T22:31:10+00:00
drupal:
  nid: 3177
  path: /blog/2022/enable-external-antenna-connector-on-raspberry-pi-compute-module-45
  body_format: markdown
  redirects:
    - /blog/2022/enable-external-antenna-connector-on-raspberry-pi-compute-module-4
aliases:
  - /blog/2022/enable-external-antenna-connector-on-raspberry-pi-compute-module-4
tags:
  - antenna
  - cm4
  - compute module
  - config
  - raspberry pi
  - wifi
---

{{< figure src="./external-antenna-raspberry-pi-compute-module-4.jpeg" alt="Raspberry Pi Compute Module 4 external U.FL antenna" width="700" height="466" class="insert-image" >}}

The internal WiFi module on the Compute Module 4 (that's the bit under the metal shield in the picture above) routes its antenna signal via software. You can route the signal to either:

  1. The built-in PCB triangle antenna (this is the default).
  2. The external U.FL connector (which has an external antenna plugged into it in the picture above)

To switch the signal to the U.FL connector (for example, if you're installing your CM4 in a metal box where the PCB antenna would be useless), you need to edit the boot config file (`sudo nano /boot/firmware/config.txt`, and add the following at the bottom:

```
# Switch to external antenna.
dtparam=ant2
```

Then reboot the Pi.

To switch back, comment out or delete the `dtparam` line above. Note that you can actually disable the WiFi antenna route _entirely_ (even without disabling the WiFi chip); here are the docs [straight from the firmware repository](https://github.com/raspberrypi/firmware/blob/master/boot/overlays/README):

```
Params:
        ant1                    Select antenna 1 (default). CM4/5 only.

        ant2                    Select antenna 2. CM4/5 only.

        noant                   Disable both antennas. CM4/5 only.
```

See my [original review of the Compute Module 4](/blog/2020/raspberry-pi-compute-module-4-review) for more information about antenna performance, and a recommendation of an external antenna to buy (though you can't go wrong with the one from Raspberry Pi themselves!).
