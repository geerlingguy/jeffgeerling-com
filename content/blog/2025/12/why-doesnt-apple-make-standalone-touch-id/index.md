---
nid: 3516
title: "Why doesn't Apple make a standalone Touch ID?"
slug: "why-doesnt-apple-make-standalone-touch-id"
date: 2025-12-03T22:38:04+00:00
drupal:
  nid: 3516
  path: /blog/2025/why-doesnt-apple-make-standalone-touch-id
  body_format: markdown
  redirects: []
tags:
  - 3d printing
  - apple
  - hacks
  - keyboard
  - level2jeff
  - mac
  - touch id
  - video
  - youtube
---

I finally upgraded to a mechanical keyboard. But because Apple's so protective of their Touch ID hardware, there aren't any mechanical keyboards with that feature built in.

{{< figure src="./apple-touch-id-external-3d-printed-sensor.jpg" alt="Apple Touch ID - external 3D printed sensor" width="700" height="394" class="insert-image" >}}

But there _is_ a way to hack it. It's incredibly wasteful, and takes a bit more patience than I think _most_ people have, but you basically take an Apple Magic Keyboard with Touch ID, rip out the Touch ID, and install it in a 3D printed box, along with the keyboard's logic board.

I'm far from the first person to do this—the first time I saw it done was [this Snazzy Labs video](https://www.youtube.com/watch?v=hz9Ek6fxX48). But I thought I'd share my own experience.

If you don't know what Touch ID is, it's basically Apple's version of a fingerprint sensor. But it's integrated really well into macOS, for login, unlocking password managers, and Apple Pay.

## Video

I published a video covering the full process on my 2nd channel, Level 2 Jeff:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/tzB6m2VTxAg" frameborder='0' allowfullscreen></iframe></div>
</div>

## Teardown

Tearing apart the Magic Keyboard is much more daunting than it should be. Apple puts layers and layers of adhesives, from the back cover (which needs to be heated up a bit before it will start coming apart—somewhat destructively), to the battery (good luck getting it out without bending it at all), and even the tiny flexible PCB ribbon cables—one of which I was almost certain I'd rip (thankfully it didn't rip).

But Apple and repairability are not usually on good terms, so that's to be expected.

If you want the full story, watch the video above. But following along with the [guide on the Printables page for the 3D printed Touch ID sensor case I made](https://www.printables.com/model/355924-clickable-touch-id-box-tkl-board-wired#instructions), here are a few things I think I should highlight for anyone else attempting the procedure:

{{< figure src="./apple-magic-keyboard-sticky_0.jpeg" alt="Apple Magic Keyboard - back sticky adhesive residue open" width="700" height="394" class="insert-image" >}}

  - Use some heat to get the back of the keyboard off. It's literally just _tons of adhesive_. Like... see the photo above. You could set the keyboard on a 3D printer heat bed, use a heat gun or [iOpener](https://amzn.to/4iAyExj), or do what I did and lean the keyboard against a space heater (just... don't melt it).
  - Use a tiny [curved-tip tweezers](https://amzn.to/443cldQ) made for electronics to do things like remove the little stickers holding connectors on the logic board, or to lift the flex PCB (very, very thin ribbon cables) off the adhesive holding it in place.
  - Use extreme care around the flat part of the flex PCB with little surface-mount circuits on it that goes from the logic board all the way over to the Touch ID button. It was stuck _very_ firmly on my keyboard, and I was 50/50 whether it would rip or not as I pulled it off.
  - Make sure to follow the directions for printing the Touch ID backing plate especially—I had to re-print mine at 0.1mm layer height, as the default setting I was using at 0.12mm made it just too high, and trying to sand a tiny 3D printed part is no fun.

{{< figure src="./touch-id-sensor-logic-board-in-3d-printed-box.jpeg" alt="Touch ID and logic board in 3D printed case" width="700" height="394" class="insert-image" >}}

The last part of the assembly in the 3D print was the most annoying, as you're putting M1.2-size nuts over M1.2-size screws, in a tight space. I could've used a couple more hands, but eventually I balanced the nut on the end of the screw, got my finger in position on top of it, then got the threads started with a screwdriver from below.

## Why doesn't Apple make this?

Touch ID is a great feature that you grow to rely on over time. It feels like a bit of a let down if you decide to use a non-Apple keyboard, and you can't use Touch ID at all.

So _why doesn't Apple make a little Touch ID box_? They could charge $50 and I'd begrudgingly pay it. That way I (and at least hundreds if not thousands of other people) wouldn't have to sacrifice a $150 keyboard (and a few hours of time) to get one 'smart' key off it.
