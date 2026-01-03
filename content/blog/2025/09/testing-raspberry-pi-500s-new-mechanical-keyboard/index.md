---
nid: 3498
title: "Testing the Raspberry Pi 500+'s new mechanical keyboard"
slug: "testing-raspberry-pi-500s-new-mechanical-keyboard"
date: 2025-09-25T07:00:45+00:00
drupal:
  nid: 3498
  path: /blog/2025/testing-raspberry-pi-500s-new-mechanical-keyboard
  body_format: markdown
  redirects:
    - /blog/2025/raspberry-pi-500s-new-mechanical-keyboard
    - /blog/2025/testing-raspberry-pi-500-mechanical-keyboard
aliases:
  - /blog/2025/raspberry-pi-500s-new-mechanical-keyboard
  - /blog/2025/testing-raspberry-pi-500-mechanical-keyboard
tags:
  - computer
  - keyboard
  - mechanical
  - pi 500
  - plus
  - raspberry pi
  - reviews
  - video
  - youtube
---

{{< figure src="./pi500plus-keyboard-typing.jpeg" alt="Raspberry Pi 500+ typing on keyboard rainbow LED backlight" width="700" height="394" class="insert-image" >}}

Instead of a traditional review of a new Pi product, I thought I'd split things up on my blog, and write two separate posts; this one about the Pi 500+'s new mechanical keyboard, and a separate post about [hacking in an eGPU on the Pi 500+](/blog/2025/full-egpu-acceleration-on-pi-500-15-line-patch), for a massive uplift in gaming performance and local LLMs.

The [Raspberry Pi 500+](https://www.raspberrypi.com/products/raspberry-pi-500-plus/) was announced today, sells for $200, and adds on the following over what was present in the regular Pi 500:

  - Built-in M.2 NVMe SSD (256GB, 2230-size Pi branded drive) in a 2280-size slot
  - 16 GB LPDDR4x RAM (over the Pi 500's 8)
  - Low-profile RGB-backlit mechanical keyboard with Gateron KS-33 Blue switches

I also have a full video covering the Pi 500+ up on YouTube, and you can watch it below, as well:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/Dv3RRAx7G6E" frameborder='0' allowfullscreen></iframe></div>
</div>

## A Mechanical Keyboard

{{< figure src="./pi500plus-keyboard-pulling-keycaps.jpeg" alt="Raspberry Pi 500+ replacing keycaps" width="700" height="394" class="insert-image" >}}

Like any modern mechanical keyboard, the Pi 500+'s uses standard keycaps, mounted on top of [Gateron KS-33 Low Profile Blue](https://www.gateron.co/products/gateron-low-profile-mechanical-switch-set) switches.

The keycaps feel nice, the larger keys like Space, left Shift, Enter, and Backspace all have extra bracing, and I had no problem pulling keycaps with a few different key pullers.

{{< figure src="./pi500plus-keyboard-rgb.jpeg" alt="Raspberry Pi 500+ RGB lighting effect" width="700" height="394" class="insert-image" >}}

Each key has an individually-controllable RGB LED below, and the keyboard comes preprogrammed with a dozen or so lighting effects. More can be configured in Raspberry Pi's [keyboard configuration tools](https://www.raspberrypi.com/documentation/computers/keyboard-computers.html#raspberry-pi-500-customisation) (I used a preview version of it in my testing).

The keyboard runs on an RP2040, like many other modern mechanical keyboards, running a Pi fork of the popular QMK firmware. It _should_ be compatible with tools like [VIA](https://usevia.app), for browser-based keyboard configuration, but that will require a slightly different process, and possibly a keyboard firmware update.

## How does it feel and sound?

{{< figure src="./pi500plus-keyboard-59-dba.jpg" alt="Raspberry Pi 500+ Mechanical Keyboard Typing Sound 59 dBa" width="700" height="394" class="insert-image" >}}

It's definitely a clickety-clack keyboard, with the blue switches Raspberry Pi chose (note: the plastic inside is grey, not blue).

I personally favor quieter key switches, and you can see I was getting about 60 dBa measured 1' away, but as long as you're not in a computer lab full of these things, the noise is tolerable.

It feels surprisingly good; I could type on this keyboard _much_ easier than I can on the Pi 400/Pi 500's flat keyboard, which feels like an old, cheap laptop keyboard.

One nice thing about using standard mechanical switches, though, is you can choose other keycaps to alter the look and feel of the Pi 500+'s keyboard.

## Swapping out keycaps

{{< figure src="./pi500plus-keyboard-replacement-style-1.jpeg" alt="Raspberry Pi 500+ with alternate slim keycaps 1" width="700" height="394" class="insert-image" >}}

I promise, the image above was not edited in any way; pictured above are [dagaladoo Low Profile Double Shot PBT keycaps](https://amzn.to/4gOhvzu), and from this camera angle it looks like someone just took full-height keycaps and squished them down to 25% height!

It took about 20 minutes to swap out all the keycaps—though I left the power button in place. The Pi 500+ keyboard firmware keeps that key green when power is on, and red when power is off, and it's nice to have it shine the light through on the little light pipe built into Raspberry Pi's key.

You _can_ install full-height keys on the low-profile switches, but many will bottom out when pressed. This works on some keys, like my spare Keychron set (pictured below), but it didn't feel great, so I would stick with low profile keycaps.

{{< figure src="./pi500plus-keyboard-keycap-full-height.jpeg" alt="Escape key full height on Raspberry Pi 500+" width="700" height="394" class="insert-image" >}}

I also tried a set of [KBDiy 9009 Retro Keycaps](https://amzn.to/4pJUHoA), and as I describe in the video, typing on those felt like typing on some kind of dry sugar candy. It wasn't a bad feeling, it was just weird:

{{< figure src="./pi500plus-keyboard-replacement-style-2.jpeg" alt="Raspberry Pi 500+ with alternate slim keycaps 2" width="700" height="394" class="insert-image" >}}

It's nice to be able to alter the look and feel of the Pi 500+ by swapping out keycaps. And the underlying keyboard construction seems a _lot_ nicer than the Pi 500 and Pi 400 that came before. (The Pi 500+ weighs almost 600g, nearly double the Pi 500's 385g.)

The fact the keyboard top shell is completely separate from the Pi 500+'s main body means someone might even be able to hack in an even more solid mechanical keyboard.

## Conclusion

The new keyboard is a vast improvement over the previous Pi keyboards. It's not as nice as a high-end mechanical keyboard, but I would compare it favorably to a midrange or low-end keyboard like the Razer Huntsman.

Not being able to change out the switches is a let-down, as the clickety-clack of blue switches isn't everyone's cup of tea. But having any option besides the '2000s chicklet' style of prior generations is good.

If you want a deeper dive into everything else I learned about the Pi 500+, please [watch the video](https://www.youtube.com/watch?v=Dv3RRAx7G6E).
