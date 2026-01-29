---
date: '2026-01-29T11:00:00-06:00'
tags: ['aa', 'battery', 'rechargeable', 'li-ion', 'lithium', 'ion', 'power', 'repairability', 'waste']
title: 'Ode to the AA Battery'
slug: 'ode-to-the-aa-battery'
---
Recently [this post from @Merocle](https://x.com/Merocle/status/2015496917472489751) caught my eye:

> I'm fixing my iFixit soldering station. I haven't used it for a long time and the battery has gone overdischarge. I hope it will come back to life. Unfortunately, there are no replacements available for sale at the moment.

{{< figure
  src="./ifixit-soldering-usb-battery-merocle-torn-down.jpg"
  alt="iFixit soldering hub torn down - used with permission"
  width="500"
  height="auto"
  class="insert-image"
>}}

Devices with built-in rechargeable batteries have been bugging me a lot lately. It's convenient to have a device you can take with you and use anywhere. And with modern Li-ion cells, battery life is remarkable.

But for years, I've noticed the same thing happening to many devices as Merocle mentions above:

  1. I purchase the device, charge it to 100%, use it a bit.
  2. Knowing Li-ion cells are better off in the 40-80% range, I store the device with the battery at that charge level.
  3. The next time I go to use the device (a few months later), it won't power on.
  4. I plug the device in to charge, and 1 in 4 times the device won't start charging!

One problem is many devices don't have a proper BMS integrated into the charging circuit, that will cut power _before_ the battery is below a critical threshold. Li-ion cells start to have problems below 3V, and often suffer permanent damage below 2.5V.

Devices from even the most stalwart right-to-repair companies suffer from undervoltage issues.

You [can sometimes revive 'dead' Li-ion batteries](https://www.eevblog.com/forum/beginners/reviving-a-0v-lithium-ion-battery/), but I don't recommend it unless you know what you're doing.

Assuming most people _don't_ know what they're doing, when they pull out a piece of gear that won't turn on and has no obvious way of being repaired (especially with odd pouch-cell batteries, much less 18650 cells), these devices will [most often end up in the trash](https://www.epa.gov/facts-and-figures-about-materials-waste-and-recycling/frequent-questions-regarding-epas-facts-and#CellPhones). Or if you're _lucky_, some people will try recycling them.

## Enter the AA

Because of this trend, if I need portability, I look for devices that use AA and AAA batteries.

{{< figure
  src="./eneloop-aa-batteries.jpeg"
  alt="eneloop AA batteries"
  width="700"
  height="auto"
  class="insert-image"
>}}

Each year for the past 14 years, I buy sets of [Panasonic eneloop batteries](https://amzn.to/49Gatuz) to replace disposable AA batteries as they die. Eneloops have around 2000 mAh of capacity (versus 2100+ mAh for good alkaline batteries[^projectfarm]), and run at a nominal 1.2V instead of the 1.5V of alkaline batteries.

But they can be recharged. Over and over. They can be pulled out of a device, with new batteries swapped in quickly. For long term storage, I can pop the batteries out and use them in _other_ devices.

So far, across 128 batteries, I have not had a single incident of leakage, fire, etc., and even the cells I reserve for outdoor use (in devices that go from -12°F in the winter to 105°F+ in the summer) are still holding a charge, over a decade later.

Only _one_ cell has had to be retired, out of all the eneloops I've purchased.

What prompted me to write this post is the soldering project I worked on during this weekend's snowstorm.

## Universal Standards

I was putting together [this clock](https://amzn.to/4qD2LHz) at my workbench, and at one point I needed to determine which resistor was 100KΩ and which was 1MΩ. I pulled out my Fluke multimeter, inserted two AAA batteries I had sitting on my bench (I keep 8 AA and 8 AAA batteries charged and ready at my workbench, and don't store them in my tools), and measured the resistors.

Upon doing so, I realized the clamp meter I was using ([Fluke 323 True RMS Clamp Meter](https://amzn.to/4bgJSFH)) only measures between 400-4000Ω, so I switched to my old Craftsman meter that worked a treat—and uses a replaceable 9V battery!

It would be faster to leave the batteries in my tools, but over 40 years of sacrificing devices to alkaline cell leakage, it's my habit not to. So far I've never had leakage problems with the eneloops, but old habits die hard.

{{< figure
  src="./sony-walkman-wm-fx281.jpg"
  alt="Sony Walkman WM-FX281 FM radio in use"
  width="700"
  height="auto"
  class="insert-image"
>}}

When I put away the meter, I noticed my wife's and old Sony Walkman sitting nearby. Just for fun, I popped in two AA batteries.

My wife had both a [WM-EX150](https://walkman.land/sony/wm-ex150) (made in 1995) and a [WM-FX281](https://retrospekt.com/products/sony-walkman-wm-fx281-am-fm-portable-cassette-player). These are 31 and 25 years old, respectively—and outside the rubber belts being shot, the devices both work. The radio works good as new, and it would play cassettes again after a little maintenance.

The AAs might not last 32 hours, and the Walkman doesn't fit in tight jeans pockets, but they can still be as useful today as they were decades ago.

Looking at my stack of old tech, _every_ device uses one of the standard AA, AAA, or C-sized batteries. And thinking of all the new devices I've purchased, the ones that worry me the least (regarding fire safety, and whether they're work the next time I pull them out)... are the ones with easily-replaceable batteries.

## No Batteries at All

If I don't need portability, I prefer USB-C powered tools (with no battery). USB-C is ubiquitous enough I _always_ have a plug available with at least 5, 9, or 12V of power.

At every workbench and desk, and in my car and backpack, I have either USB battery packs, or wall plugs, that supply any voltage a device would need, and can supply up to 100W (sometimes _more_) through a small USB-C connector.

If I truly need portability, I can rubber-band a battery pack to the device I'm using.

It's not always ideal, and I wouldn't want a smartphone with such a battery pack, but many of my battery-less devices will outlive me, I am sure, with no risk of [burning down my house](https://www.usfa.fema.gov/a-z/lithium-ion-batteries/risks-and-response-strategies/).

## Energy Density and Weight

There _are_ cases where the energy density, portability, and weight tradeoffs of traditional battery cells don't work out: laptops, tablets, smartphones, watches, extremely lightweight computer mice...

Considering wireless input devices, though, Apple's [1st gen Magic Trackpad](https://en.wikipedia.org/wiki/Apple_pointing_devices#1st_generation) was AA-powered. Apparently Apple considered battery swaps so convenient they didn't even include a USB or Lightning connector[^wired]!

I can understand when you need a more exotic or thin layout that doesn't lend itself well to cylindrical battery cells. There are [laptops that exist with exposed 18650 cells](https://www.jeffgeerling.com/blog/2024/mnt-reform-hackable-laptop-not-everyone/), but they're certainly not for everyone (unless you like portable computing [like it's 1999](https://www.jeffgeerling.com/blog/2024/build-log-macintosh-powerbook-3400c/)).

{{< figure
  src="./lithium-ion-battery-packs-in-box.jpeg"
  alt="Li-ion battery packs in a box on my desk"
  width="700"
  height="auto"
  class="insert-image"
>}}

As I build my own devices, I find myself relying on USB power (if the device lives near a desk or workbench), or integrated [AA battery holders](https://amzn.to/4rd7YWz) (if the device is meant to be portable). Not having to keep a few dozen cheap Li-ion packs sitting in close proximity to my [sand bucket](https://eridirect.com/blog/2022/11/ways-to-prevent-lithium-ion-battery-fires/) is a neat side-benefit.

[^projectfarm]: Project Farm has a great video exploring [which AA battery provides the best value / power / longevity](https://www.youtube.com/watch?v=7eloV0mp6CE).

[^wired]: I still prefer wired connections for my peripherals, though.
