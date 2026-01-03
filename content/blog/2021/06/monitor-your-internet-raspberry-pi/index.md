---
nid: 3111
title: "Monitor your Internet with a Raspberry Pi"
slug: "monitor-your-internet-raspberry-pi"
date: 2021-06-23T13:59:59+00:00
drupal:
  nid: 3111
  path: /blog/2021/monitor-your-internet-raspberry-pi
  body_format: markdown
  redirects: []
tags:
  - grafana
  - internet
  - isp
  - monitoring
  - prometheus
  - raspberry pi
  - starlink
---

Internet Service Providers are almost universally despised. They've pushed for the FCC to continue [defining 25 Mbps as "high use" broadband](https://www.telecompetitor.com/fcc-hangs-on-to-25-3-mbps-broadband-definition-for-2021-broadband-deployment-report/), and on top of that they overstate the quality of service they provide. A recently-released map of [broadband availability in the US](https://broadbandusa.maps.arcgis.com/apps/webappviewer/index.html?id=ba2dcd585f5e43cba41b7c1ebf2a43d0) paints a pretty dire picture:

{{< figure src="./broadband-desert-usa.jpg" alt="USA map showing areas with limited high speed broadband availability" width="600" height="343" class="insert-image" >}}

Here in St. Louis—where I guess I should count my lucky stars we have 'high use' broadband available—I have only two options: I can get 'gigabit' cable Internet from Spectrum, or 75 megabit DSL from AT&T.

That's it.

And you're probably thinking, "Gigabit Internet is great, stop complaining!"

But Spectrum's "gigabit" Internet is 930 megabits down—in _ideal_ conditions—but only 40 megabits up. And that's the highest plan that costs about $150 a month!

Some would die for those speeds (see the map above), but much of the world is better off. And are you really getting the speeds you pay for? You probably don't know.

{{< figure src="./grafana-speedtest-dashboard.jpg" alt="Grafana speedtest Internet monitoring dashboard" width="700" height="424" class="insert-image" >}}

Well, I do, thanks to a $35 Raspberry Pi! And you don't even need a Pi, you could run the software I use on any computer. I just like having a dedicated computer to run all my Internet connection tools, so it's easy to backup or replace, and it doesn't get bogged down.

## Video

I have a video that goes along with this blog post, and it's embedded below; skip past it if you prefer reading over viewing.

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/rIUc4C4TXog" frameborder='0' allowfullscreen></iframe></div>
</div>

## My Internet Pi

This is my "Internet Pi" (hostname `geerli.net`):

{{< figure src="./internet-pi-rackmount-pi-4.jpeg" alt="Internet Raspberry Pi in Rackmount case" width="600" height="400" class="insert-image" >}}

I have it installed in a rack (here's a [video on the Pi rack](https://www.youtube.com/watch?v=LcuNc4jz-iU)), but it could just as easily be on my desk, or sitting by my Internet router.

The most important thing for measuring a network connection is that it's wired. WiFi, especially on the Pi, fluctuates quite a bit and is terrible for monitoring anything besides maybe WiFi signal strength.

The Internet Pi runs [Pi-hole](https://pi-hole.net) for DNS privacy and ad-blocking, and [Prometheus](https://prometheus.io/docs/introduction/overview/) and [Grafana](https://grafana.com/oss/grafana/) to provide Internet connection monitoring dashboards.

Having a Pi monitoring my Internet continuously makes it easy to see trends over time, or confirm outages. If you just spot check by running a Speedtest every now and then, you don't have much data to go on.

## Setting up Internet Pi

I built the free and open source [internet-pi project on GitHub](https://github.com/geerlingguy/internet-pi). It's simple to set up, and you can choose which parts of the platform you want to use.

I set up my Internet Pi from another computer, but you could also run the Internet Pi playbook on the Pi itself. Following the install instructions, you need to have a Pi set up with Raspberry Pi OS running on your network, and be able to SSH into the Pi.

Here are the steps to get it going:

  1. Make sure you have Ansible installed:
     1. (If `pip3` is not installed) `sudo apt-get install -y python3-pip`
     1. `pip3 install ansible`
  1. Download the internet-pi repository to your computer: `git clone https://github.com/geerlingguy/internet-pi.git && cd internet-pi`
  1. Install the Ansible Galaxy content that's required to make the playbook work: `ansible-galaxy install -r requirements.yml`
  1. Make copies of the `example.inventory.ini` and `example.config.yml` files (dropping the `example.` from the filenames) and modify them for your own needs
  1. Run the playbook: `ansible-playbook main.yml`

The playbook installs all the tools you choose in your configuration file, and once that's done, you should be able to access your Pi's IP address in a web browser to see Pi-hole, or visit the IP address with the port `:3030` on the end to see the Grafana dashboards.

{{< figure src="./pihole-geerli-net.jpg" alt="Pi-hole - Geerli.net" width="700" height="362" class="insert-image" >}}

## Setting up Pi-hole

If you wanna use Pi-hole as your home network's DNS server, you should configure your router to advertise the Pi's IP address as the primary DNS server for your whole home network. For extra redundancy, you could actually configure two Pis running Pi-hole, but that's a topic for another post!

But the great thing is, that allows you to see all the DNS requests your devices are making, and make sure (for the most part) things like so-called 'smart' TVs don't [send tons of information to advertisers](https://www.cbsnews.com/news/smart-tv-spying-fbi-says-the-device-may-be-spying-on-you-today-2019-12-03/).

Pi-hole is a great _first_ line of defense for your Internet privacy, at least at home, and it even has some other neat tools like a simple DNS server, if you want to use them.

## Internet monitoring

The Internet monitoring dashboard is automatically configured for you, but it can take up to an hour before you start seeing data.

{{< figure src="./grafana-speedtest-dashboard.jpg" alt="Grafana speedtest Internet monitoring dashboard" width="700" height="424" class="insert-image" >}}

In my case, it's been running for a couple months, so I can see the Internet connection for the past day, week, or even longer!

The monitoring configuration runs one container that connects to Speedtest.net. Every 30 minutes or so, another container running Prometheus tells the first container to run a speed test.

> **NOTE**: If you run this monitoring on your own network, be aware that these Speedtest.net checks will consume a good amount of data, especially if you run them more frequently. If you have data caps and want to use this monitoring solution, make sure to modify the check interval so you don't get an unexpected overage. ISPs, gotta love 'em!

It stores that data on the Pi, and the Grafana dashboard displays it over time. There's another service that does simple checks on websites you can configure for uptime and HTTP request timing stats—those lightweight checks are performed every few seconds, to give a detailed view when there is more latency in your Internet connection.

One thing I found interesting was my Cable internet connection—which is _supposed_ to be one 930 Mbps—is only really about 700 Mbps on average.

Upload speeds are more consistent, so I begrudgingly pay for this high-tier plan... But I'd be a _lot_ happier with 50 or 100 Mbps of asymmetric data, since I'm not downloading terabytes of files every day.

## Starlink monitoring

The main reason I set this stuff up was to compare my Gigabit Cable Internet to SpaceX's Starlink Internet.

{{< figure src="./starlink-cable-comparison-graph.png" alt="Cable Spectrum ISP vs Starlink performance graph" width="600" height="442" class="insert-image" >}}

I'll get more into Starlink in a future review, but it looks like on average, when it has a stable connection, I get over 150 Mbps down, and 15 Mbps up, with 40 milliseconds of latency.

Those numbers _are_ less than my Cable ISP; but Starlink also costs less—it's $99/month. And Starlink is also beaming the Internet through satellites up in the sky! For someone who doesn't have a fast Cable option (like rural customers), that's a mind-blowing upgrade from dial-up speeds.

But I mentioned earlier, there's also a Starlink-specific dashboard that gives all the details you'd normally find in the Starlink App.

{{< figure src="./starlink-dashboard.jpg" alt="Starlink connection dashboard" width="600" height="338" class="insert-image" >}}

I haven't been actively using the Starlink connection today, so it's a little barren, but it gives a ton of detail, and I'd like to thank Daniel Willcocks ([DanOpsTech](https://github.com/danopstech)) for making this possible; I'm using his Docker image and dashboard, and he even [adjusted it to work on the Raspberry Pi](https://github.com/danopstech/starlink_exporter/issues/1) after I asked about it!

## Power monitoring

I also monitor Starlink's power consumption using a [Shelly Plug US](https://shopusa.shelly.cloud/shelly-plug-us-wifi-smart-home-automation) and a [custom Shelly Plug Prometheus exporter](https://github.com/geerlingguy/shelly-plug-prometheus) I wrote:

{{< figure src="./shelly-plug-power-consumption-grafana-starlink.jpg" alt="Shelly Plug power monitoring Starlink router and dishy dashboard Grafana" width="600" height="338" class="insert-image" >}}

Starlink's dish and router use a _lot_ of power (more than you might expect)—but I'll discuss more about that in my Starlink review coming soon! I have a [blog post](https://www.jeffgeerling.com/blog/2021/using-shelly-plug-monitor-starlinks-power-consumption) with more about how I set up the Shelly Plug power monitoring.

## Conclusion

Now I know exactly how much my ISP is fleecing me for Internet. In Spectrum's case, it looks like they're only giving me about 3/4ths of what I pay for.

I wish I could just pay them $110 a month instead of $150, but if I did that, they'd cancel my service!

I'd like to thank [Max Andersen](https://github.com/maxandersen/internet-monitoring) for the original inspiration for the original monitoring configuration, the developers behind Pi-hole for making it free and open source, and especially [Miguel](https://github.com/MiguelNdeCarvalho) who maintains the speedtest exporter, for his help [getting some bugs fixed](https://github.com/MiguelNdeCarvalho/speedtest-exporter/issues/48)!
