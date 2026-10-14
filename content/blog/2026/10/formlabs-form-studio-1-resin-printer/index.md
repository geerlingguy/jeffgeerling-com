---
date: '2026-10-14T08:00:00-05:00'
tags: ['formlabs', 'studio 1', 'resin', '3d printing', 'review', 'youtube', 'video']
title: 'Formlabs dropped the Raspberry Pi on the way to a $699 SLA printer'
slug: 'formlabs-form-studio-1-resin-printer'
---
{{< figure
  src="formlabs-form-studio-1-hero.jpeg"
  alt="Formlabs Form Studio 1"
  width="700"
  height="auto"
  class="insert-image"
>}}

Formlabs sent me a [Form Studio 1](https://formlabs.com/3d-printers/form-studio-1/?utm_source=youtube&utm_medium=refe
rral&utm_campaign=jeffgeerling-fs1-2026-07-26-global) resin 3D printer to test after years of back-and-forth about their Form 4 printer.

Like the Form 4, it's an SLA (stereolithography) printer, but unlike the Form 4 (which starts at $2,600), it's affordable for a hobbyist. It's not _cheap_, coming in at $699 (or $749 with a flex build platform, which I highly recommend), but it is affordable.

I can't say as much about this printer as people who are well-versed in resin printing and use other SLA printers (all my experience until now is with FDM, or Fused Deposition Modeling[^fdm], printers). But I can convey my first-time experience using this printer and with the entire SLA experience.

It's a more tedious process, which involves resins you can't touch, multiple gallons of IPA (Isopropyl Alcohol) for washing, and curing in UV light... but the end result has a resolution that can't be matched with FDM, and materials ranging from clear resin to flexible rubber are equally unreal to see come off the printer if you’re only used to filament printers.

Besides the tedious post-processing, resin (at least on the consumer level) can't do multi-color/multi-material prints—something that's become almost commonplace on filament printers this year, and has its own interesting use cases.

{{< figure
  src="formlabs-form-studio-1-gutbomb-macpicomodem-clear.jpeg"
  alt="GutBomb MacPicoModem clear resin enclosure"
  width="700"
  height="auto"
  class="insert-image"
>}}

But I printed a number of items, including the one I was most excited to try—GutBomb's [MacPicoModem](https://jcm-1.com/product/macpicomodem/) enclosure, but clear, and with the traditional speaker hump that is iconic on Global Village modems for old Macs.

Anyway, I posted my full experience, and a review of the Form Studio 1, in today's video on YouTube:

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/4l9xU3_36Xs' frameborder='0' allowfullscreen></iframe></div>
</div>

Formlabs also provided [this link to the Form Studio 1](https://formlabs.com/3d-printers/form-studio-1/?utm_source=youtube&utm_medium=refe
rral&utm_campaign=jeffgeerling-fs1-2026-07-26-global) that tracks where people visit from, but I don't participate in their affiliate program (I only participate in Amazon Affiliates). They are selling four 'special edition' colored plastic versions for a limited time, and I only wish those were permanent options (only grey will be permanent).

The video above goes into a few more details about their value engineering, as well—it takes a lot to go from $2,600 down to $700—and I even had the honor of speaking to KRALYN (who built the Positron, and headed the Studio 1 project) about how they tackled a number of engineering challenges.

{{< figure
  src="formlabs-form-studio-1-side-som.jpeg"
  alt="Formlabs Form Studio 1 side SoM view"
  width="700"
  height="auto"
  class="insert-image"
>}}

One of the more interesting nuggets was their decision to drop the Raspberry Pi Compute Module (used in the Form 4). The Studio 1 adopts a different Arm SoM, and that meant more work building a proper camera driver (Raspberry Pi's camera stack just worked out of the box), _and_ going through the wireless certification process (Pi CMs are pre-certified if using their approved antennas). But apparently it was worth it for the cost savings.

Between that, reducing the power output of the UV light, using a cheaper plastic hinge instead of the metal damped hinge on the Form 4, and dropping the mixing arm that is more necessary for higher-end resins (some costing $300+ per liter!), they were able to get the cost a little south of $1,000.

There are other SLA resin printers for half the cost, and some other resins that are cheaper than Formlabs' own, too. I can't speak to reliability or quality versus those printers, but at least having hardware under a grand means Formlabs can address a new audience—people like me, who had a hard time justifying a Form 4. Especially since 'Open Material Mode' is free[^omm] on this printer—it's a [$875 addon](https://formlabs.com/products/open-material-mode/) for the Form 4!

[^fdm]: The type of 3D printer that extrudes filament through a tiny hot end.

[^omm]: It requires use of the Form Studio Resin Tank Pro ($79), which is $24 more expensive than the standard Form Studio Resin Tank ($55).
