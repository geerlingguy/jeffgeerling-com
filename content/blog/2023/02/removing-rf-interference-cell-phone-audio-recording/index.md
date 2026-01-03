---
nid: 3270
title: "Removing RF interference from a cell phone from audio recording"
slug: "removing-rf-interference-cell-phone-audio-recording"
date: 2023-02-01T16:32:09+00:00
drupal:
  nid: 3270
  path: /blog/2023/removing-rf-interference-cell-phone-audio-recording
  body_format: markdown
  redirects: []
tags:
  - audio
  - izotope
  - recording
  - software
  - sound
  - wireless
---

I made the mistake of putting my [Wireless Go II](https://amzn.to/3JtBQeI) mic transmitter in the same pocket as my iPhone for a recent video recording, and as a result, I had a lot of RF interference in the recorded track.

Thinking I could just use the nice feature of the Wireless Go II's built-in recording, I grabbed the track off the body pack itself—but found that it, too, had the RFI sound, meaning the iPhone's interference made it into the mic circuit itself, not just the wireless mic signal to my camera!

I tried Final Cut Pro's built-in voice isolation, and that helped mute the noise between speech, but during speech it was omnipresent.

I also tried accusonus' denoise plugin (RIP after [accusonus was bought out by Meta](https://www.pro-tools-expert.com/production-expert-1/meta-facebook-parent-company-acquires-accusonus)), and it did better, but left the sound feeling 'watery'.

Finally, after a bunch of research, I found [iZotope RX 10](https://www.izotope.com/en/products/rx.html), which is a standalone audio editor meant for deep processing of recorded audio. Their [online example](https://www.izotope.com/en/learn/removing-high-frequency-buzz-and-interference-from-audio.html#remove-buzz) impressed me enough to give the Trial a shot, so I loaded up my audio and played around with the Denoise plugin:

{{< figure src="./denoise-audio-izotope-rx-advanced.jpg" alt="Denoise in iZotope Audio Editor" width="700" height="414" class="insert-image" >}}

Miraculously, I was able to get my speech to not sound watery or muddy, and remove about 95% of that background RFI.

I know Nvidia has their new speech processing AI, and Adobe I think is also in that game, but I like tools that are built more for high-fidelity tweaking and noise processing rather than full-on speech synthesis / re-production like those AI tools do (though they are quite impressive regardless!).

I am always happy to pay for software that solves major problems, though it would be cool to explore options in the open source arena. In this case, one difficulty was there weren't many silent portions with the RFI that I could sample to remove it from the speech portions—if there were, I may have been able to mangle this together with some open source editors.

But all's well that ends well. I am quite impressed with how much you can clean up a bad audio recording these days.
