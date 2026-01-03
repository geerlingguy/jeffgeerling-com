---
nid: 3342
title: "SimpliSafe Video Doorbell: Halt and Catch Fire"
slug: "simplisafe-video-doorbell-halt-and-catch-fire"
date: 2024-02-01T15:00:55+00:00
drupal:
  nid: 3342
  path: /blog/2024/simplisafe-video-doorbell-halt-and-catch-fire
  body_format: markdown
  redirects: []
tags:
  - doorbell
  - simplisafe
  - video
  - youtube
---

{{< figure src="./simplisafe-video-doorbell-burnt-wires.jpg" alt="SimpliSafe Video Doorbell Pro burnt wires" width="700" height="auto" class="insert-image" >}}

This SimpliSafe doorbell burned up less than a week after I installed it. I never would've thought a doorbell would be the most dangerous thing I set up at my studio!

I learned a LOT about powering 'smart' doorbells, and talked directly to SimpliSafe about it. They did sent a replacement, but it has it's own problems.

I'm still happy with SimpliSafe overall, but I don't like how I've spent about 8 hours troubleshooting a 'smart' doorbell. The only thing that's been 100% reliable on this thing is the basic ding dong I could've gotten with a [five dollar dumb doorbell](https://amzn.to/4987S9w)!

<blockquote>
<p>This blog post is based off my latest moving vlog, episode 12, where I talk about my SimpliSafe doorbell problems, the new 10G and 25G networking gear I'm testing, and a new 'retro corner' in my office. Check it out below:</p>
<div class="yt-video">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/sxA4zKwHHgY" frameborder='0' allowfullscreen></iframe></div>
</div>
<p>The saga continues—see also: <a href="/blog/2023/my-simplisafe-doorbell-lit-its-own-fire-winter">My SimpliSafe doorbell lit its own fire this winter</a>.</p>
</blockquote>

Before I dive into exactly what happened, I will mention SimpliSafe was responsive, not only in online chat, but [after I posted about this on Twitter](https://twitter.com/geerlingguy/status/1737256067510177793), they reached out through email, _without_ making a public show about it, and they eventually called and we talked about the problem at length.

Why am I pointing that out? Surely a company needs to get on top of any bad PR, or potential product safety issues, right?

Well, yeah... but sadly many companies _don't_, and SimpliSafe _did_, so at least they're doing something!

That doesn't mean their response was perfect. Far from it.

SimpliSafe markets this thing as being compatible in _any type of home_, old or new.

Now... yes, my studio space is a _business_, not a home. So they got me there.

But it says right on the website, "Compatible with any 8-24V AC transformer."

{{< figure src="./simplisafe-website-every-type-of-home.jpg" alt="Simplisafe website - every type of home transformer" width="700" height="auto" class="insert-image" >}}

And I made sure to read through the installation instructions, there's no warning about what kind of transformer you need, just a range of 8 to 24 volts.

So since this was a new install, I put in a [24v Reliapro doorbell transformerReliapro](https://amzn.to/3OEKkl9) from Jameco. It's rated 50W at 24v, and I've seen these things all over the place for doorbell wiring.

In a typical doorbell circuit, you'd have a transformer, a doorbell button, and a chime in the middle. A mechanical chime is basically a solenoid that slaps a couple metal bars to make that iconic 'ding dong' sound.

When you press the doorbell button, the circuit closes, and the solenoid whacks one note. Let go, and the solenoid releases, so the metal bounces back and hits the other note.

That's great, but I didn't really need a chime, I just wanted a smart doorbell so I could get a notification on my phone whenever someone was at the door.

That's the whole point—and I saw no warnings about a chime being a _requirement_ for the doorbell to work. Just that it's "compatible."

To confirm that, I checked their website—which actually changed since my tweet in December. The Wayback machine [shows what it originally said](https://web.archive.org/web/20231204135842/https://simplisafe.com/video-doorbell-pro), which was that it's a wired doorbell and it's "compatible with analog-slash-mechanical chimes."

To _me_, that indicated it would work with a chime, but it wasn't a requirement.

But... after a week having it installed with my 24v transformer, the wires were burnt to a crisp, and I guess that idea didn't hold water.

{{< figure src="./simplisafe-camera-disconnected.jpg" alt="SimpliSafe Camera Disconnected in app" width="700" height="auto" class="insert-image" >}}

I started seeing 'Camera offline' in the SimpliSafe app, and eventually I couldn't even press the button! It wouldn't even click, as the little clicky button inside had melted.

After another day or so, I started smelling burnt plastic, so I immediately cut power to the doorbell, pulled it off the wall, and tried to reset it inside. If you do this, have a bucket of sand nearby; there's a lithium battery inside, and fire and lithium batteries don't mix well.

But I pulled it apart—and score one for SimpliSafe actually making repairable units and not sealing them up with glue. Once open, I was greeted by a horrible burning electronics smell, and these crispy wires:

{{< figure src="./simplisafe-doorbell-crispy-wires.jpg" alt="SimpliSafe doorbell crispy wires" width="700" height="auto" class="insert-image" >}}

I don't have more footage because SimpliSafe wanted the burnt up doorbell back for testing. And to make it safe in shipping, I cut out the battery, buried it in sand, and sent the doorbell itself back.

Apparently [this is not an isolated experience](https://support.simplisafe.com/conversations/cameras/video-doorbell-pro-new-installation-transformer-failing-issues/6190c6768ea41ebb06234cfb). Other people, even hired _electricians_, ran into the same problem. SimpliSafe's recommendation so far seems to be to just install a mechanical chime.

And like I said, they even [changed the wording on the website](https://simplisafe.com/video-doorbell-pro) after my Tweet—now it says it "_requires_ an existing standard wired doorbell system with a mechanical chime and a transformer with 8-24 VAC, 30VA max"

So I went the extra mile. I re-wired my entire system with a 16V 40VA transformer _and_ a mechanical door chime:

{{< figure src="./doorbell-chime-upgrade-jeff-geerling.jpg" alt="Jeff Geerling holds a mechanical doorbell chime" width="700" height="auto" class="insert-image" >}}

And it worked!

For about a week.

After a week I started getting the 'Camera offline' errors. Plus, the chime was making a buzzing sound.

I took the doorbell apart again, and everything _except_ the camera was fine... the doorbell chime would ring ('ding dong'), the button and motion sensor worked, and I even would get a 'Ding Dong' notification from the app. My network also showed it active on my WiFi.

But for some reason, the camera just stopped working entirely after a week. I can't even get it to do a connection test because the app thinks it's offline.

So I had a glorified $99 doorbell that's about as useful as a five dollar button, except I'd be less nervous that button would start a fire!

What are some other things I can try? Well, I could ask for another replacement, though the one they sent me needed some cleaning up. The button was grungy, and it had some deep scratches on it I can't get out.

And some people online said they had success using the [OhmKat](https://amzn.to/3vTwynX), a power supply made _specifically_ to overcome the shortcomings of the Video Doorbell Pro... for another $35 bucks!

But I don't know. Maybe I'll go through support again. Maybe SimpliSafe will call back again after they see this blog post. I'm not sure.

All I know is if you advertise a voltage range, like 8-24 volts, and say it's a drop-in, and it's actually _not_. That's... a bit annoying.

A bunch of people who replied to [my original Twitter post](https://twitter.com/geerlingguy/status/1737238264484884677) mentioned, when you use a range like that, you have to allow for a range above and below. If you wind up with 25 or 26 volts, that shouldn't result in your product burning itself out.

Otherwise, narrow the voltage range.

I did ask SimpliSafe about the buzzing chime, and they sent over a ['Chime Connector'](https://support.simplisafe.com/articles/video-doorbell-pro/my-doorbell-wont-ringdo-i-need-a-chime-connector/634492954a42432bbd44f9f1).

{{< figure src="./lbc710-optomos-relay-chime-connector-simplisafe.jpg" alt="LCB710 OptoMOS relay in Chime Connector from SimpliSafe" width="700" height="auto" class="insert-image" >}}

I popped it open and saw this little chip labeled LCB710. [It's an OptoMOS Relay](https://ixapps.ixys.com/DataSheet/LCB710.pdf), and it looks like it might help with separating out the chime from the doorbell [when you press the button](https://lo.calho.st/posts/doorbell-adapter-revised/), but I'm not 100% sure.

I asked my Dad about it and he said he'd need some time to mess with the whole setup on a scope to figure out exactly what it's doing.

But after reading [this forum post](https://support.simplisafe.com/conversations/cameras/chime-connector-what-is-it/6190c66e8ea41ebb0622bf72) I decided to give it a go, and miracle of miracles, the camera started working again.

<s>Will it last? We'll see. If it _doesn't_, maybe I'll get _another_ replacement, just hopefully it'll look a little less used next time.</s>

It did not last. I'm now getting the same old 'Camera offline' message in the app, though 'Ding Dong' notifications and motion sensing works fine. Honestly, not sure what I'll do at this point. At least my Raspberry Pi-based NVR using Frigate has been stable, so I can see when the doorbell is rung, then quickly hop over to that for video footage.

I'll continue to document my saga here. Maybe a Video Doorbell Pro Max will be released, and it will fix some of these problems. Honestly I'd love if they just had a 12v DC version of the doorbell, or something along those lines—it would solve a lot of the issues with the impossible task of designing tiny hardware compatible with 100 years of doorbell wiring.
