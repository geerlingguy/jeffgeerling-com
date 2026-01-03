---
nid: 2811
title: "Using MaxMind's free GeoIP databases with the official Docker PHP image"
slug: "using-maxminds-free-geoip-databases-official-docker-php-image"
date: 2017-09-15T05:14:56+00:00
drupal:
  nid: 2811
  path: /blog/2017/using-maxminds-free-geoip-databases-official-docker-php-image
  body_format: markdown
  redirects: []
tags:
  - apache
  - docker
  - geoip
  - geolocation
  - ip
  - maxmind
  - php
---

I recently had to add support for the MaxMind free GeoIP database to a PHP container build that was based on the [official Docker PHP image](TODO) on Docker Hub. Unfortunately, it seems nobody else who's added this support has documented it, so I figured I'd post this so that the next poor soul who needs to implement the functionality doesn't have to spend half a day doing it!

First, you need the PHP `geoip` extension, which is available [via PECL](TODO) (note: if you can make the PHP project itself use a composer library, there are a few better/more current geoip libraries available via Packagist!). Here's how to install it in one of the php 5.6 or 7.0-apache images (note that 7.1 uses Debian Stretch instead of Jessie... but the instructions should be the same there):

```
FROM php:7.0-apache

# Install GeoIP PHP extension.
RUN apt-get update \
    && apt-get install -y  libgeoip-dev wget \
    && rm -rf /var/lib/apt/lists/* \
    && pecl install geoip-1.1.1 \
    && docker-php-ext-enable geoip
```

Then you also need to install MaxMind's tool, `geoipupdate`, to get the databases and put them in the right place. First, the installation (in the Dockerfile):

```
# Install GeoIPUpdate.
RUN apt-get update \
    && apt-get install -y automake autoconf libtool \
    && cd /tmp \
    && wget https://github.com/maxmind/geoipupdate/archive/master.tar.gz \
    && tar -xzf master.tar.gz \
    && cd geoipupdate-master \
    && ./bootstrap \
    && ./configure \
    && make \
    && make install \
    && apt-get purge --auto-remove -y automake autoconf libtool \
    && rm -rf /var/lib/apt/lists/*
```

You could also get the codebase using git if you want, but in my case I don't need git on the container, so I just used `wget` (which I installed earlier). The above process follows the [official build instructions from MaxMind's repo](TODO).

Finally, you need to configure the `geoipupdate` tool so it pulls the right databases and puts them in the right location. Create a file in your docker build directory named `GeoIP.conf`, and put the contents below inside:

```
UserId 999999
LicenseKey 000000000000

ProductIds GeoLite2-City GeoLite2-Country GeoLite-Legacy-IPv6-City GeoLite-Legacy-IPv6-Country 506 517 533

DatabaseDirectory /usr/share/GeoIP
```

This places the dat files in the proper location for the PHP pecl extension to pick them up. Now make sure you add that file by copying it into the container:

```
COPY GeoIP.conf /usr/local/etc/GeoIP.conf
```

Now do a <code>docker build</code> and you should end up with PHP's GeoIP extension, and all the required libraries. Add a scheduled job or manually run inside a running container `geoipupdate`, then there's only one step left before the PHP extension works correctly: manually symlink the PHP-expected dat file location to the one that MaxMind downloads: `ln -s /usr/share/GeoIP/GeoLiteCity.dat /usr/share/GeoIP/GeoIPCity.dat`.

Now, you can run this command on the CLI to see if everything's working: `php -r "print_r(geoip_record_by_name('YOUR_IP_HERE'));"` (replace `YOUR_IP_HERE` with your IP address).
