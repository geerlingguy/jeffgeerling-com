---
nid: 2510
title: "Setting up the Edimax EW-7811Un or Tenda W311Mi 802.11b/g/n WiFi Adapter on a Raspberry Pi"
slug: "edimax-ew-7811un-tenda-w311mi-wifi-raspberry-pi"
date: 2015-02-08T21:39:26+00:00
drupal:
  nid: 2510
  path: /blogs/jeff-geerling/edimax-ew-7811un-tenda-w311mi-wifi-raspberry-pi
  body_format: full_html
  redirects:
    - /blogs/jeff-geerling/edimax-ew-7811un-wifi-raspberry-pi
aliases:
  - /blogs/jeff-geerling/edimax-ew-7811un-wifi-raspberry-pi
   - /blogs/jeff-geerling/edimax-ew-7811un-tenda-w311mi-wifi-raspberry-pi
tags:
  - config
  - edimax
  - networking
  - raspberry pi
  - wifi
---

<blockquote>Note: On Raspberry Pi models with built-in WiFi (e.g. the Raspberry Pi 3 model B), USB WiFi interfaces will use <code>wlan1</code> (<code>wlan0</code> is reserved for the first interface, in this case the internal one).</blockquote>

Since this is maybe the fourth time I've done this process on my Raspberry Pis, I decided to document the process of setting up cheap mini WiFi adapters on a Raspberry Pi A+/B+/2.

This process works great with any USB WiFi adapter that's supported out of the box. My three favorites (due to their inexpensive price and decent connection speed/reliability) are:

<ul>
<li><a href="http://www.amazon.com/gp/product/B003MTTJOY/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B003MTTJOY&linkCode=as2&tag=mmjjg-20&linkId=XN6F5JHSUVHLOIW7">Edimax EW-7811Un 802.11b/g/n USB WiFi adapter</a> (usually available for under $10 from Amazon)</li>
<li><a href="http://www.microcenter.com/product/411056/W311Mi_Wireless_N_Pico_USB_20_Adapter">Tenda W311Mi 802.11b/g/n USB WiFi adapter</a> (usually available for under $10 from Micro Center)</li>
<li><a href="http://www.amazon.com/gp/product/B00FWMEFES/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00FWMEFES&linkCode=as2&tag=mmjjg-20&linkId=RQUVE4XMKPUGROY2">Kootek 802.11b/g/n USB WiFi adapter with Realtek RTL8188CUS chipset</a> (usually available for under $10 from Amazon)</li>
</ul>

<h2>Configuring the adapter</h2>

<ol>
<li>Make sure the Raspberry Pi sees the adapter on the USB bus: <code>$ lsusb</code>.</li>
<li>Make sure the network interfaces file (<code>/etc/network/interfaces</code>) has a <code>wlan0</code> configuration; if not, make it look somewhat like the following:
<pre>
allow-hotplug wlan0
iface wlan0 inet manual
    wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
</pre></li>
<li>Edit your wpa_supplicant.conf file (<code>/etc/wpa_supplicant/wpa_supplicant.conf</code>), and add your wireless network settings to the end of the file:
<pre>
network={
  ssid="YOUR_NETWORK_SSID"
  psk="YOUR_NETWORK_PASSWORD"
}
</pre></li>
<li>If the Pi doesn't connect automatically within 10-20 seconds, you can manually refresh the interface to connect and get an IP address: <code>$ sudo ifdown wlan0 && sudo ifup wlan0</code>. Then run <code>ifconfig</code> to find your IP address (in the <code>wlan0</code> section).</li>
</ol>

You can also reboot your Pi entirely (<code>$ sudo reboot</code>) to make sure the configuration sticks and your Pi joins the network automatically. I typically set up static IP reservations on my network router, so each Pi gets a permanent IP address.

Also, if you need to scan for a list of the WiFi networks your Pi can see, run <code>sudo iwlist wlan0 scan</code>.

Troubleshooting the wifi connection:

<ul>
<li>Make sure your Pi can see the network you're trying to connect to: use <code>$ sudo iwlist wlan0 scan | grep ESSID</code> to list all the found network SSIDs. If you're network isn't in the list, it might be a 5GHz network (the Edimax only works on 2.4GHz networks), or it might be out of range.</li>
<li>To find your IP address, MAC address, and other interface information, run the command <code>$ ifconfig -a</code>.</li>
</ul>

<h2>Ensuring the adapter doesn't go into sleep mode</h2>

One of the most annoying things that can happen with a headless wifi-connected computer is the wireless connection dropping, or hanging for 10+ seconds at a time. It seems the Edimax is configured to go into a sleep state after a few seconds of inactivity by default, but this can be disabled pretty easily:

<ol>
<li>Create a configuration file for the adapter: <code>$ sudo nano /etc/modprobe.d/8192cu.conf</code></li>
<li>Add the following two lines to the configuration file and save the file:
<pre>
# Disable power management
options 8192cu rtw_power_mgnt=0 rtw_enusbss=0
</pre></li>
<li>Reboot your Raspberry Pi: <code>$ sudo reboot</code></li>
</ol>

I've had one Pi running for almost a year now, doing nothing but some temperature data aggregation inside the house, and the Edimax WiFi adapter has been rock solid. A missed packet here or there, but way more reliable than any other cheap adapter I've used!

I've only recently started using the Tenda adapter, but so far it seems to be just as reliable as the Edimax, despite being a little less popular. It doesn't seem to require any extra configuration to stay out of sleep mode, and it's readily available at my local Micro Center!
