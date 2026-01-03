---
nid: 3255
title: "Ubuntu's settings won't open after setting CPU to 'performance'"
slug: "ubuntus-settings-wont-open-after-setting-cpu-performance"
date: 2022-11-17T02:28:54+00:00
drupal:
  nid: 3255
  path: /blog/2022/ubuntus-settings-wont-open-after-setting-cpu-performance
  body_format: markdown
  redirects: []
tags:
  - benchmarking
  - gnome
  - linux
  - performance
  - settings
  - tutorial
  - ubuntu
---

Recently I was doing some benchmarking on my Ubuntu 22.04 PC, and as part of that benchmarking, I tried setting the CPU performance profile to `performance`. In the old days, this was not an issue, but it seems that modern Ubuntu only 'knows' about `balanced` and `power-saver`. Apparently performance is forbidden these days!

```
$ powerprofilesctl list
* balanced:
    Driver:     placeholder

  power-saver:
    Driver:     placeholder
```

The problem was, I had set the profile to `performance`:

```
$ powerprofilesctl set performance
```

But suddenly the 'Settings' GUI app would no longer open (at least not after I had opened it and clicked into the 'power' section). A reboot didn't work, and even reinstalling control center (`sudo apt-get install --reinstall gnome-control-center`) didn't help!

When I tried opening the settings GUI from the command line, I got the following critical error:

```
$ gnome-control-center display

(gnome-control-center:4710): cc-power-profile-row-CRITICAL **: 20:12:10.458: cc_power_profile_row_get_radio_button: assertion 'CC_IS_POWER_PROFILE_ROW (self)' failed
**
power-cc-panel:ERROR:../panels/power/cc-power-panel.c:1122:performance_profile_set_active: assertion failed: (button)
Bail out! power-cc-panel:ERROR:../panels/power/cc-power-panel.c:1122:performance_profile_set_active: assertion failed: (button)
Aborted (core dumped)
```

After finding [this issue in the Gnome bug tracker](https://gitlab.gnome.org/GNOME/gnome-control-center/-/issues/1504), I found that the problem was that the version of the control center I had in my Ubuntu release seems to have a bug. When it encounters the 'performance' setting, it just crashes.

It looks like it was fixed recently, but the fix hasn't made its way into a stable Ubuntu release. So for now, the fix to getting Settings to display again is to set the power mode back into one of the two modes Settings is comfortable with, e.g. `balanced`:

```
$ powerprofilesctl set balanced
```

Now settings opens up, and I can move along with my day again :)
