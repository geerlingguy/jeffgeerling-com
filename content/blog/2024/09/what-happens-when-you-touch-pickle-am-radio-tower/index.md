---
nid: 3402
title: "What happens when you touch a Pickle to an AM radio tower?"
slug: "what-happens-when-you-touch-pickle-am-radio-tower"
date: 2024-09-03T16:25:33+00:00
drupal:
  nid: 3402
  path: /blog/2024/what-happens-when-you-touch-pickle-am-radio-tower
  body_format: markdown
  redirects:
    - /blog/2024/experiments-rf-safety-am-radio-meat-pickle-edition
    - /blog/2024/experiments-rf-safety-meat-pickles-demonstrate-foldback
    - /blog/2024/rf-safety-experiments-meat-pickles-demonstrate-foldback
aliases:
  - /blog/2024/experiments-rf-safety-am-radio-meat-pickle-edition
  - /blog/2024/experiments-rf-safety-meat-pickles-demonstrate-foldback
  - /blog/2024/rf-safety-experiments-meat-pickles-demonstrate-foldback
tags:
  - am
  - geerling engineering
  - plasma
  - radio
  - rf
  - science
  - video
  - youtube
---

A few months ago, our [AM radio hot dog experiment](https://www.instagram.com/insights/media/3333127873529510767/) went mildly viral. That was a result of me asking my Dad 'what would happen if you ground a hot dog to one of your AM radio towers?' He didn't know, so one night on the way to my son's volleyball practice, we tested it. And it was _awesome_.

There's a video and some pictures in my [hot dog radio blog post](/blog/2024/talking-hot-dog-gives-new-meaning-ham-radio) from back in March.

<div style="text-align: center;">
<video style="max-width: 95%; width: 640px; height: auto;" preload autoplay loop playsinline muted>
  <source src="./bratwurst-am-tower.mp4" type="video/mp4" />
  Your browser does not support the video tag.
</video>
</div>

Fast forward a few months and one Open Sauce later, and Jay from [Plasma Channel](https://www.youtube.com/@PlasmaChannel) visited us in St. Charles, MO, for round two—where my Dad and I were prepared to measure (almost) everything: SWR, RF forward power, SDR on site, AM field intensity 25km (16mi) away, meat thermals, and—courtesy of Jay—some taste testing!

Our full experience is documented in today's Geerling Engineering video:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/wzDEIBpbLRk" frameborder='0' allowfullscreen></iframe></div>
</div>

But I'll also summarize all our test results in this blog post, for easier reference:

## Test Setup and Safety Precautions

{{< figure src="./rf-safety-hotdog.jpg" alt="RF Safety - Hot Dog AM radio tower" width="700" height="auto" class="insert-image" >}}

**DO NOT ATTEMPT**. Don't mess with towers, especially AM broadcast towers.

We consulted with an experienced broadcast antenna designer before any testing. Using [conservative FCC guidelines](https://transition.fcc.gov/Bureaus/Engineering_Technology/Documents/bulletins/oet65/oet65.pdf) (also see [Supplement A](https://transition.fcc.gov/oet/info/documents/bulletins/oet65/oet65a.pdf)), we determined a safe exposure distance _for the tower and transmitter at this single tower site_. Every tower, station, and frequency will be different, so again, _do not attempt_ what we did. It was for educational purposes only. And science.

## Experiment 1 - Hot Dog

{{< figure src="./rf-safety-hotdog-measurements.jpg" alt="RF Safety - Hot Dog device measurements" width="700" height="auto" class="insert-image" >}}

**Hypothesis**: Well, we already knew the hot dog would make some noise. This time, we brought all our instrumentation, and measured how it affected the signal.

**Observations**: The hot dog did, indeed, produce copious noise through plasma-air interaction. It did an excellent job demodulating the AM signal into audible sound, and the entire hot dog was heated to around 80°C—which is luckily a safe internal temperature for eating.

What may be _less_ safe is eating whatever charred remains were left on the end of the hot dog. The transmitter RF output (as measured on the control panel) rose to 14 kW (from a nominal 12) briefly, before the internal [foldback protection](https://electronics.stackexchange.com/a/2936/9952) cut power to around 6 kW (until we stopped shorting the hot dog to ground, after which the Nautel XR12 raised power back to 12 kW).

## Experiment 2 - Pickle (Gherkin)

{{< figure src="./rf-safety-pickle-plasma-shockwave.jpg" alt="RF Safety - Plasma shockwave coming off gherkin pickle on AM tower" width="700" height="auto" class="insert-image" >}}

**Hypothesis**: Some commenters believed the salt content of a fresh gherkin would cause the arc to change from orange-ish (hot dog) to green-ish (pickle). We speculated it may turn more reddish...

**Observations**: The gherkin was quite a pickle. While testing, there was a loud spark, then the transmitter quickly got _very_ quiet. We originally thought it cauterized itself and caused less conduction, but were very wrong. As it turns out, the pickle was an _excellent_ conductor, with much lower internal resistance than any of the meats we tested. The salt-saturated watery interior provided an excellent path from tower to ground!

This was the only object we tested which caused the transmitter to completely disable its RF output, if only momentarily. The end of the pickle glowed orange, and we also observed a plasma _shockwave_ (pictured above) in a few frames. Would love to see this with a high-speed camera!

{{< figure src="./rf-safety-jay-pickle-eat.jpg" alt="Jay from Plasma Channel Taste-Tests a Pickle" width="700" height="auto" class="insert-image" >}}

In the category of 'what-were-you-thinking' comes Jay from the [Plasma Channel](https://www.youtube.com/@PlasmaChannel). He decided to taste-test the pickle, and immediately spat it out as he said it tasted strongly of copper. He speculates the taste may have resulted from the electrolysis of the copper we used to ground the pickle. We speculate he may be a little crazy—our kind of crazy. Jay has his own video on the experience here: [Creating A Plasma Shockwave Using Wireless Energy](https://www.youtube.com/watch?v=NowhPAMDOTo).

## Experiment 3 - Bratwurst

{{< figure src="./rf-safety-bratwurst.jpg" alt="RF Safety - Bratwurst on AM radio tower" width="700" height="auto" class="insert-image" >}}

**Hypothesis**: Many commenters speculated a bratwurst would translate the normally-English radio signal into German. We had our doubts.

**Observations**: The bratwurst did indeed translate the signal into German! Or, well... it broadcast the german phrases the [on-air talent](https://adamwrightstl.com/about/) spoke during his morning show.

The bratwurst was the floppiest of the tested meats, and had a rather phallic look as it was hanging off the end of our probe. The 'droop' resulted in a large contact patch, which produced more smoke than the hot dog, but not any perceptible difference in sound. The transmitter reacted about the same as it did with the hot dog.

## Experiment 4 - Vegan Hot Dog

{{< figure src="./rf-safety-vegan-hot-dog.jpg" alt="RF Safety - vegan hot dot" width="700" height="auto" class="insert-image" >}}

**Hypothesis**: We expected the vegan hot dog to perform similarly to the all-beef hot dog, though were wondering if it could surprise us. [Soybeans and sugar](https://lightlife.com/product/jumbo-smart-dogs/) may react differently than beef or turkey!

**Observations**: The sound was a bit louder, the vegan hot dog was a bit cooler, and the end burned off a bit more quickly. The more disgusting bit was the end near the copper insertion point—some white substance oozed out the backside and did not look very appetizing (see photo above).

Jay taste-tested the cooked vegan hot dog (this time biting off a section from the middle, not a part that came in contact with the copper) and described the taste as 'pretty good'.

## Experiment 5 - Corn Dog

<div style="text-align: center;">
<video style="max-width: 95%; width: 640px; height: auto;" preload autoplay loop playsinline muted>
  <source src="./corn-dog-am-tower-shrunk.mp4" type="video/mp4" />
  Your browser does not support the video tag.
</video>
</div>

**Hypothesis**: We speculated the corn layer surrounding the hot dog may provide enough insulation to prevent a serious reaction with the tower. This item also was a physical manifestation of our sometimes 'corny' dad jokes.

**Observations**: Copious amounts of smoke, followed by large bursts of flame. Honestly, this was the most surprising of the bunch. The smoke seemed to follow the leg of the tower at a fairly large distance from the point of contact!

Unlike the other meats, the smell of the burnt corn dog was pleasant–almost sugary. The sound was not that loud, and apparently the corn layer provided enough resistance the transmitter's foldback protection circuit never activated; the transmitter continued at 12 kW power throughout our corn dog test.

Nobody was brave enough to taste-test the corn dog.

## Experiment 6 - Breakfast Sausage

{{< figure src="./rf-safety-breakfast-sausage.jpg" alt="RF Safety - AM breakfast sausage" width="700" height="auto" class="insert-image" >}}

**Hypothesis**: Will a meat meant for the 'a.m.' perform any better on an AM radio tower?

**Observations**: Yes, in fact—this smaller bit of meat was louder than the rest, and seemed to burn _very_ evenly. The breakfast sausage stayed under 70°C, and it quickly kicked the transmitter back to 6 kW (half) output, but was stable at that power output.

The end was quite crispy.

## Experiment 7 - Hot Dog Warmer

We also tested holding a hot dog on the stick within about 1" of the base of the tower for approximately 60 seconds, but found there to be no significant heating at that distance. Part of the hot dog had to be touching the tower, creating the plasma arcs, to heat the hot dog at the 1460 kHz frequency of this broadcast station. At least at the 7 kW or so this tower was putting out.

## Conclusion

{{< figure src="./rf-safety-transmitter-status-display.jpg" alt="RF Safety - transmitter status log" width="700" height="auto" class="insert-image" >}}

If we ran the tests again, I would very much like to bring a sound pressure level meter. It would be interesting to more quantitatively measure the sound of each object.

Some have also suggested using a better insulating rod—something like [this $300 fiberglass rod](https://amzn.to/3z41UKv). It would be an improvement over our wooden stick, though with the power at _this_ antenna, the risk is extremely small that RF would arc through the stick, into a human holding it (especially with our thick rubber gloves), versus through the copper in the end. The bigger risk is heating and near-field RF exposure, which follows the [inverse-square law](https://en.wikipedia.org/wiki/Inverse-square_law). Distance is safety.

I would love to get a high speed camera (capable of at least 10,000 fps) to capture the plasma interaction between the tower and the meat to see if we could visualize the amplitude modulation in plasma. Maybe also repeating the experiment at dusk, so the plasma is brighter.

As it is, there are just lots of bright bursts of plasma that look interesting but mask the hidden modulation causing them! (If you're a Slow Mo Guy and you're reading this... DMs are open, lol.)
