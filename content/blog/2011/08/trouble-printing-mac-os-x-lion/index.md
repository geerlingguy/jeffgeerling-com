---
nid: 2327
title: "Trouble Printing in Mac OS X Lion? Reinstall the driver"
slug: "trouble-printing-mac-os-x-lion"
date: 2011-08-09T18:12:52+00:00
drupal:
  nid: 2327
  path: /blogs/jeff-geerling/trouble-printing-mac-os-x-lion
  body_format: filtered_html
  redirects: []
tags:
  - brother
  - drivers
  - hl-2140
  - mac
  - printers
  - usb
aliases:
  - /blogs/jeff-geerling/trouble-printing-mac-os-x-lion
---

It always seems to happen after a major OS upgrade—no matter what the operating system... You go to print, and all the sudden you get a warning saying your printer drivers are not up-to-date or are not installed correctly.

In my case, I tried printing to my trusty and reliable Brother HL-2140 (laser printer), and I got a warning that Apple needed to update its drivers via Software Update. I let it try, but that failed. Any time I sent a new print job, the printer dialog simply told me there was an error, and the drivers were out of date.

I then deleted and added the printer in the Print & Scan system preference pane, which sometimes helps, but in this case did not. My printer is listed as being compatible with OS X 10.6 / Lion (check your own printer <a href="http://support.apple.com/kb/ht3669#brother">here</a>), so that shouldn't be a problem. But, as is the case almost always, giving things a big konk in the head works.

I went to brother.com, found the 10.7 CUPS driver for the HL-2140 in Brother's downloads section, and installed from the disk image I downloaded. Then I deleted the printer and re-added it again, and all was well. I don't know if this would be different had I plugged the printer directly into my MacBook Pro... I originally had it that way, but had recently (before upgrading to Lion) switched to plugging it into my Airport Express router.
