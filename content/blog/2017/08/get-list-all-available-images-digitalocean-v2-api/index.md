---
nid: 2800
title: "Get a list of all available images in the DigitalOcean v2 API"
slug: "get-list-all-available-images-digitalocean-v2-api"
date: 2017-08-17T02:41:14+00:00
drupal:
  nid: 2800
  path: /blog/2018/get-list-all-available-images-digitalocean-v2-api
  body_format: markdown
  redirects:
    - /blog/2017/get-list-all-available-images-digitalocean-v2-api
aliases:
  - /blog/2017/get-list-all-available-images-digitalocean-v2-api
tags:
  - api
  - digitalocean
  - image
  - json
---

I frequently need to check the `slug` or `id` of a particular Droplet image (or in AWS parlance, an AMI) that I can use to launch new DigitalOcean droplets via Ansible. And seeing as tonight I had to search for 'how to get a list of all DigitalOcean images' about the hundredth time, I figured I'd publish this in a blog post so I can find it more easily in the future.

Without further ado:

    curl -X GET --silent "https://api.digitalocean.com/v2/images?per_page=999" -H "Authorization: Bearer $DO_API_TOKEN"

This assumes you have `export`ed a valid `$DO_API_TOKEN` previously. If not, just paste your DigitalOcean API token in place of `$DO_API_TOKEN`, and then run the command.

It dumps out a ton of JSON, so you can either paste it through something like [http://jsonprettyprint.com](http://jsonprettyprint.com), or try reading it in all it's unformatted glory. And if the latter, _are you a robot?_

Bonus trick: If you're on a Mac, you can add ` | pbcopy` to the end of that command to have the output stuck into your clipboard, for easy pasting. Or no matter where you are, if you have `jq` installed, you can add `| jq '.'` to the end to get it pretty-printed in your console.
