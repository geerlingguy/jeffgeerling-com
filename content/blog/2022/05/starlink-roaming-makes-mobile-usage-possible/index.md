---
nid: 3206
title: "Starlink Roaming makes mobile usage possible"
slug: "starlink-roaming-makes-mobile-usage-possible"
date: 2022-05-04T14:00:42+00:00
drupal:
  nid: 3206
  path: /blog/2022/starlink-roaming-makes-mobile-usage-possible
  body_format: markdown
  redirects: []
tags:
  - internet
  - satellite
  - spacex
  - starlink
  - video
  - youtube
---

> **May 5th Update**: this feature is now official, and is called "Portability." To enable it, you will need to pay an extra $25/month, though I haven't been charged yet despite using the feature. Starlink says mobility (using Dishy while in motion) is not yet supported and will void your kit's warranty.
>
> I've logged into my Starlink.com account, and I now see a note that reads _Click "Manage Service Options" to add Portability._ — that screen leads to this [Starlink Portability FAQ](https://support.starlink.com/?topic=1426e78a-7384-0334-3fc0-ddf5a76d7afe) page with more details. I haven't signed up for it yet, and I'm waiting to see what happens next billing cycle... I still can't update the service address to my cousin's location.
>
> **May 6th Update**: Many roaming users are getting [this email](https://www.reddit.com/r/Starlink/comments/uj2qbm/action_required_update_your_service_address_or/) now, which states they'll have until June 3, 2022 to enable Portability or update their service address, or the dish will stop working outside their service address. I haven't gotten the email yet, but expect to receive it soon.

For a year, I've tried transferring my Starlink user terminal to my cousin, who lives on a farm in rural MO.

{{< figure src="./starlink-in-yard-dishy.jpg" alt="Starlink Dishy in Yard" width="700" height="391" class="insert-image" >}}

I bought Starlink when it became available in my area, and used it for a while, but ultimately wanted to give my kit to my cousin, who has less than 1 megabit upload at her farm.

Unfortunately, transfers weren't possible during the early beta. And once they _were_ made available, you could only transfer Starlink to someone living in a [covered cell](https://www.starlink.com/map), but only if that cell _also_ has availability (which excludes most populated parts of the world right now).

But after seeing [MikeOnSpace's 'Driving with Starlink'](https://www.youtube.com/watch?v=8PDVURcvWeg) video, I decided to pull Starlink out of storage and test it around St. Louis, to see if roaming worked. If it did, I'd drive it out to my cousin's farm and see if it finally works there—even if I can't transfer ownership to her yet.

That process is documented in my latest YouTube video, embedded below:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class="embed-container"><iframe src="https://www.youtube.com/embed/I9zqGeH8EIs" frameborder="0" allowfullscreen=""></iframe></div>
</div>

Starlink _did_ finally work at my cousin's house, so I left it with her, but the account's still under my name and address. Roaming could be shut off at any time, so until the dish is fully transferred, I'll maintain ownership.

Starlink's coverage is tricky for a number of reasons, most notably per-satellite and per-cell coverage/density. This slide comes from [a Starlink presentation in India](https://drive.google.com/file/d/1UOI7b5flgAjJrPs2HDa64p_ZABckasa_/view):

{{< figure src="./Planning%20for%20Starlink%20-%20States%20and%20UTs.jpg" alt="Planning for Starlink - 100 in 300 thumb rule" width="700" height="394" class="insert-image" >}}

Due to the way the network operates, SpaceX's guidance—at least as of a few months ago—was to have around 100 Starlink customers per 300 km<sup>2</sup>.

Once a cell is saturated, Starlink doesn't open access to any new customers in that cell. Roaming may allow over-subscription, but ideally that won't cause too much disruption, since there are so few people with Starlink currently.

But if it does—if suddenly areas that have a lot of RV parks see an influx of hundreds or thousands of Starlink customers—my guess is Starlink will disable roaming and prioritize customers in that cell who are at their service address.

{{< figure src="./70-watt-starlink-power-consumption.jpg" alt="70W Starlink Power Consumption" width="700" height="407" class="insert-image" >}}

Speaking of RV parks, for anyone interested in using Starlink in a mobile configuration (in an RV, boat, or off-grid on solar power), recent firmware updates have decreased power consumption. Last year I would see averages between 80-100W. Now I'm seeing averages between 60-70W. That's a welcome improvement for a device that will likely remain powered up 24x7.

It's early days for these new features, and I'm still wondering how SpaceX will overcome the physical limitations they have with their system (at least for any populated area). I think other technologies like 5G and fiber are more economically viable for most communities, but if nothing else, maybe SpaceX's efforts will cause enough competition to make ISPs stop gouging less-advantaged customers for their terrible 90s-era Internet access.
