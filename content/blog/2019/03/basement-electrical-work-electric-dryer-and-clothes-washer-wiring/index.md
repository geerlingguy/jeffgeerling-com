---
nid: 2913
title: "Basement electrical work - electric dryer and clothes washer wiring"
slug: "basement-electrical-work-electric-dryer-and-clothes-washer-wiring"
date: 2019-03-16T23:59:14+00:00
drupal:
  nid: 2913
  path: /blog/2019/basement-electrical-work-electric-dryer-and-clothes-washer-wiring
  body_format: markdown
  redirects: []
tags:
  - basement
  - electricity
  - home improvement
  - raspberry pi
  - timelapse
  - wiring
---

The Geerling household is preparing for the largest home project to date; and while my wife and I have decided to spend a bit extra to have a contractor do the work for the actual _kitchen_ reno, we are still doing what we can to maintain a functional household during the extensive refurbishment of our original kitchen, dining, and laundry area to make it a lot more amenable to our family lifestyle (our current layout is difficult with three kids and two kitchen peninsulas!).

'Phase 1', as I'm calling it, was the electrical work to support moving our electric dryer, clothes washer, and maybe even dishwasher to the basement during the course of the project. I installed a 75A sub-panel in the basement last year (it was my last major home improvement project before [the surgery](/blog/2018/recovering-surgery-and-living-my-friend-stoma)), and it's time to start putting the extra slots in it to good use!

As with most of my projects nowadays, I recorded the entire event as a time-lapse with a Raspberry Pi Zero, using my [Raspberry Pi Time-Lapse App](https://github.com/geerlingguy/pi-timelapse). And here it is, for you to enjoy!

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/Rj767stpsoA" frameborder='0' allowfullscreen></iframe></div>

A few notes from the project:

  - This was the first time I worked with a 10/3 circuit. I've done many 10/2 and 12/2 circuits, and even pulled the 4-4-4-2 SER wire for the subpanel (that was... interesting! Also the first time I realized how awesome a palm nailer is). 10/3 is interesting; you have to use a different NM staple, and 3/4" EMT instead of the standard NM staples and 1/2" EMT I'm used to.
  - Speaking of 10/3, I also had to pull out the 'big guns' to cut it—I used my bolt cutters since my linesman's pliers just weren't up to the task!
  - A couple years ago, after realizing the futility of using a standard 'hammer drill' on foundation concrete walls (though it worked okay with bricks), I finally splurged on a rotary hammer (specifically this [DeWalt 20V Max Rotary Hammer](https://www.amazon.com/DEWALT-DCH133B-Brushless-D-Handle-Rotary/dp/B01MF4YEIF/ref=as_li_ss_tl?keywords=dewalt+rotary+hammer+20v&qid=1552780401&s=gateway&sr=8-3&linkCode=ll1&tag=mmjjg-20&linkId=1f5f7ee88965a4c2834d7e526254da71&language=en_US)). It is _so_ worth it. If you have to drill more than one hole in any kind of masonry... there is no comparison behind a rotary hammer (and a good SDS Plus bit) and a hammer drill.
  - For anchoring the boxes to the concrete, I now default to Gardner Bender concrete anchors (drill hole, tap in anchor, then screw into the anchor through the box). I used to use Tapcon screws, but at least for applications where there can be some movement (people plugging and unplugging devices), the Tapcons would become loose or entirely dislodged over time.
  - I borrowed a combo 3/4" and 1/2" pipe bender from my Dad, and his advice about bends (which he heard from some electrician friend) is true: always bend more than you think... it's a lot harder to re-bend an existing bend, especially for a short-radius 45°-45° bend like I was attempting! Mine turned out to be more like 38°-26° or so :D
