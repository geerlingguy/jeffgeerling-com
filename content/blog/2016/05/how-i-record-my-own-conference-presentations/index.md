---
nid: 2656
title: "How I record my own conference presentations"
slug: "how-i-record-my-own-conference-presentations"
date: 2016-05-27T16:21:58+00:00
drupal:
  nid: 2656
  path: /blog/2018/how-i-record-my-own-conference-presentations
  body_format: markdown
  redirects:
    - /blog/2016/how-i-record-my-own-conference-presentations
aliases:
  - /blog/2016/how-i-record-my-own-conference-presentations
tags:
  - how-to
  - iphone
  - ishowu
  - lavaliere
  - mac
  - microphone
  - presentations
  - recording
  - screen capture
  - screencast-o-matic
  - tutorial
---

At this year's php[tek] conference, I decided to record my own sessions (one on a [cluster of Raspberry Pis](//www.jeffgeerling.com/blog/2016/highly-available-drupal-on-raspberry-pi-cluster-phptek-2016-session), and another on [tips for successfully working from home](http://www.jeffgeerling.com/blog/2016/protips-staying-sane-while-working-home-phptek-2016-session)). Over the years, I've tried a bunch of different methods of recording my own presentations, and I've settled on a pretty good method to get very clear audio and visuals, so I figured I'd document my method here in case you want to do the same.

If you're looking for a great method of recording sessions at a camp, conference, etc., then this method isn't the most efficient—you'd instead want to purchase equipment that records one or two audio feeds, has easy start/stop support, uses removable media (so you can back things up throughout the day), and uses an HDMI-based video recorder (inline with the projector). A friend and excellent Drupal community member, Kevin Thull, has many blog posts devoted to his [Camp Session Recording Kit](http://bluedropshop.com/blog/drupal-camp-session-recordings-year-review), and his kit is very reliable, and probably the best way to do event-wide session recordings.

That being said, _many conferences and camps don't have the budget to use a recording solution this nice_, so only the main keynotes, or sessions in one particular room with a video camera and audio recorder, will be recorded and posted online.

I always like having a recording of my sessions—both to post online and share, and to use to evaluate my own presentation, speech style, audience reactions, etc. so I can improve my public speaking skills. So even if a conference is doing it's own recordings, I'll usually make a redundant recording with my own equipment, including:

## Recording the screen (video)

<p style="text-align: center;">{{< figure src="./ishowu-hd-screenshot-recording.png" alt="iShowU HD Pro for Mac - Screencast recording of a Keynote presentation" width="550" height="309" class="insert-image" >}}</p>

The first thing you need is high-quality screen recording software, running on the computer I'm using for the presentation, recording the screen that's on the projector. There are many different apps available, but I tend to prefer [iShowU HD Pro](https://www.shinywhitebox.com/ishowu-hd-pro) for Mac, or [Screencast-O-Matic](https://screencast-o-matic.com/) for Windows.

The features that are most important to making a good recording and having an efficient workflow (e.g. being able to upload/mix the video ASAP after the session):

  - Ability to quickly select an entire display (e.g. external display) for recording
  - Ability to either use a microphone/audio input, or internal system sound, or both, for audio recording
  - Ability to record in 1080p or 720p easily (and using a codec like H.264 so it's efficient in size and playback)

Besides these features, being able to monitor audio (for setup), check levels, use shortcuts for start/stop, and easily preview the recording are also very helpful features to have.

I always start the screen recording 3-5 minutes before the presentation starts (so I can have the first slide on the screen as people filter into the room). I use at least the external mic—sometimes as my primary audio feed, but more often just as a method to sync the audio with my external lavaliere mic recording—or the internal system audio in sessions where I'll be playing any audio or video during the presentation (so I can use that clean audio feed when that media is playing, and silence my external lavaliere mic in post).

After the presentation is over, I stop the recording, and drag the recording into a folder where I stick all the presentation media (just for convenience's sake). If there's enough bandwidth, I put all the files into Dropbox, so they're immediately backed up in the cloud.

## Recording the speech and audience (audio)

<p style="text-align: center;">{{< figure src="./iphone-mic-lavaliere-rode-rec-recording.jpg" alt="iPhone with Rode Rec and the Noyce One lavaliere microphone" width="500" height="333" class="insert-image" >}}</p>

I've actually spent _a lot_ of time in the past testing out different ways of recording audio with iPhones, various Android phones, Macs, and other devices. In a former life, I did a ton of work as an audio engineer, building and maintaining both permanent and temporary audio installs for lecture halls, churches, auditoriums, etc. I've had a lot of exposure to some of the best and most expensive audio equipment, as well as the low-end cheapest equipment that barely worked!

One of the many fruits of that experience was the (so far) most popular and commented-on post on this site, [External Microphones for iPhone, iPad, and iPod Touch](//www.jeffgeerling.com/articles/photography/iphone-4-ipad-external-mic-audio-input). Since I carry my iPhone everywhere, I use it as a mobile audio recorder instead of carrying along a dedicated device like a Zoom. And I've tried many different lapel mics with the iPhone, and lately have settled on my new favorite, the [Noyce One](http://www.noycelabs.com/), which was a pre-production sample that will unfortunately not go to production. Some other options for decent lavaliere mics that should work with iPhone or most Android phones:

  - [Rode SmartLav+](https://www.amazon.com/Rode-smartLav-Lavalier-Microphone-Smartphones/dp/B00EO4A7L0/ref=as_li_ss_tl?ie=UTF8&ref_=as_li_ss_tl&linkCode=ll1&tag=mmjjg-20&linkId=e0ee60c6e62acb9938981de5fe721a90) for $79
  - ['Best' Lavaliere for smartphones](https://www.amazon.com/Lavalier-Microphone-Mic-Smartphones-iPads-Omnidirectional/dp/B01736U1VG/ref=as_li_ss_tl?ie=UTF8&qid=1464364295&ref_=as_li_ss_tl&s=musical-instruments&sr=1-13&linkCode=ll1&tag=mmjjg-20&linkId=4e83d7f5cae508889d8daf093a08d922) for $21 (cheap lav, but something like this works in a pinch)

Once you have a microphone, you could use the Voice Memos app included with the iPhone, or a similar free recording app for your OS. For my own needs, I use a more advanced app, [Hindenburg Field Recorder](https://hindenburg.com/products/hindenburg-field-recorder). It's a little expensive, but it's got it where it counts. There are some other options that are cheaper—in the past I used [Rode Rec](https://itunes.apple.com/us/app/r-de-rec/id528642521?mt=8) quite often. Note that most of the audio recording apps have mixed reviews—Rode Rec has, currently, 2/5 stars—so you really have to experiment with what works best for you (both budget and quality-wise).

Make sure whatever app you use works reliably with whatever microphones you use—and do this _before_ your presentation!

## Short summary of my process (and post-production)

  1. 5-10 minutes prior to presentation:
    1. Start iShowU HD full screen recording.
    2. Put iPhone in airplane mode (a phone call will interfere with the recording).
    3. Plug in my lavaliere, start recording in Hindenburg Field Recorder (after level check).
  2. Immediately following presentation:
    1. Stop screen recording, and move movie file into Dropbox for immediate backup (if bandwidth allows).
    2. Stop iPhone recording, and share file to Dropbox (if bandwidth allows).
  3. Post-production (hopefully very soon after presentation):
    1. Import both the video recording and the audio recording into a new event in Final Cut Pro.
    2. Select both media elements, right-click, and choose the 'Synchronize Clips' option*.
    3. Create a new Final Cut Pro project in the event and drag the synchronized clip into it.
    4. Open the synchronized clip in the Timeline so you can disable the screen recording's audio track (and just use the lav mic recording).
    5. Edit as desired, then export as a 1080p or 720p video (depending on the resolution of the screen being recorded).

_* This option only works if you recorded the external mic audio with your screen recording—Final Cut Pro intelligently compares the audio attached to the screen recording with the audio from your iPhone, and syncs the clips._

## Examples

Here are two sessions I've recorded using this process, both at php[tek] 2016 in St. Louis, MO—I think they turned out pretty good!

  - [Highly Available Drupal on a Raspberry Pi Cluster](https://www.youtube.com/watch?v=p4O0VW0qPVE)
  - [ProTips for Staying Sane while Working from Home](https://www.youtube.com/watch?v=RcWaxAhBr4A)
