---
nid: 2928
title: "A hospital stay and MLB blackouts led me to RTL-SDR radio"
slug: "hospital-stay-and-mlb-blackouts-led-me-rtl-sdr-radio"
date: 2019-08-28T21:24:42+00:00
drupal:
  nid: 2928
  path: /blog/2019/hospital-stay-and-mlb-blackouts-led-me-rtl-sdr-radio
  body_format: markdown
  redirects: []
tags:
  - am
  - baseball
  - fm
  - ibiquity
  - mlb
  - radio
  - rf
  - rtl-sdr
  - software defined radio
  - sports
---

Last year I spent a lot of time in the hospital. Between multiple surgeries and outpatient visits and follow-ups (either intentional or through an unexpected ER visit), I probably spent at least a month or two in a hospital room. For a time, you could see the exact date ranges I was checked in by the holes in my [GitHub contribution graph](https://github.com/geerlingguy/)! Such is the life of an open source developer.

<p style="text-align: center;">{{< figure src="./jeff-yay-hospital.jpg" alt="Jeff Geerling holding yay sign in hospital bed after surgery" width="325" height="325" class="insert-image" >}}<br>
<em>Despite appearances, <a href="/blog/2018/recovering-surgery-and-living-my-friend-stoma">this was not a very fun recovery</a>!</em></p>

In the hospital, every room had at least a small television with all the local cable channels—including Fox Sports Midwest, the official TV home of the St. Louis Cardinals baseball team. I'm not a huge Cardinals fan, by any means, but most everyone in St. Louis is a Cardinals fan, to some extent. Anyways, I realized that every Cardinals game was broadcast on Fox Sports Midwest. In my youth, I remember watching games with my dad on local TV stations like KPLR or KTVI. Long since, watching games died out as it went from a free family-friendly affair to the domain of the (expensive) for-pay cable TV providers.

I decided I wanted to follow along the rest of the season, but it was wrapping up by the time my health was coming around, so I dropped my research for the 2018 season.

During the first part of the 2019 season, the St. Louis Blues were doing great—enough to win the Stanley Cup—so I didn't care to follow the Cardinals much, especially when I noticed after the end of the Blues historic run that the Cardinals had a middling performance, at best.

But a couple months ago, after the All Star break, the Cardinals were again hot; they played some exciting games (well, as exciting as baseball gets, I guess—you don't normally have guys ramming each other through plexiglass panels like in hockey), and I started looking into my options.

Aaaand I found that there are zero low-cost ways to follow a baseball team.

This Amazon Prime MLB channel ad sums up why quite succinctly:

{{< figure src="./mlb-tv-blackout-ad.jpg" alt="MLB.tv blackout and out of market only ad from Amazon Prime" width="650" height="278" class="insert-image" >}}

Note, especially, the grey "Blackout and other restrictions apply" text in the bottom right.

MLB blackouts are pretty ridiculous—what I think I've figured out is, if the game is being broadcast on the local sports cable channel (e.g. Fox Sports Midwest), and you're geographically near the city the baseball game is played in, you can't watch it on MLB.tv. Even if you pay for MLB.tv, and even if the game is an away game. It gets complicated, but in practice, I've found about half the regular season games are subject to blackout restrictions. So MLB.tv is a complete non-starter unless you don't care about half the season or you cheer for a team far from where you live. (I guess there is an advantage for those living in Idaho!)

It's [more complicated than that](https://en.wikipedia.org/wiki/Major_League_Baseball_blackout_policy), but any service with this many caveats is not worth my investment.

## Options for following the Cardinals

So what options exist, barring a paid service with severe blackout restrictions?

  - MLB At-Bat stat cast? It's okay for a quick glance at the current game stats, but it requires constant attention and is also delayed by up to a minute.
  - MLB.tv? Nope, due to major blackout restrictions.
  - Sling? Nope. Hulu? Nope. Both of these lower-cost services used to carry Fox Sports Midwest but somehow that deal fell through this year.
  - Fox Sports Midwest direct? Nope.
  - Expensive ($80+) cable network packages including over 100 channels I will never watch? Nope.

I then realized we have some great radio broadcasters in St. Louis, on KMOX-AM. [One of them](https://kmox.radio.com/articles/kmoxs-best-moments-cardinals-broadcasts-mike-shannon) might be a bit past his prime, but overall the commentators on the radio are better at conveying the atmosphere and stats via voice alone, so it's easier for me to follow a baseball game in the background while working on a project or reading a book.

## Surely blackouts don't apply to radio?

I found that KMOX was freely available to stream on the Radio.com iOS app, so I downloaded it and got ready to listen to my first Cardinals game one evening.

Except... the MLB blackout also covers online streaming—therefore you can't listen to the games on a computer or mobile device.

I didn't want to lug a portable AM/FM radio around the house when I had an already-capable phone on me all day, and was even more discouraged from this approach when I found the [cheapest HD Radio units are over $50](https://www.amazon.com/s/ref=as_li_ss_tl?k=hd+radio&ref=nb_sb_noss_2&linkCode=ll2&tag=mmjjg-20&linkId=cbdac9fc9965d9e3555bb1a60198b48e&language=en_US)! And unless you pay a hefty amount for a premium (and huge) HD Radio, you can't use bluetooth at all!

I didn't really want to listen to analog AM radio since the signal can be impacted quite severely by household electronics, and the basement foundation (my home workshop and office are downstairs), so that also ruled out a cheap AM receiver.

> [HD Radio](https://en.wikipedia.org/wiki/HD_Radio) itself is a topic rich in history; it's kind of crazy (IMO) how the radio industry rolled it out in the US, and it's sad how restricted it was (many manufacturers and cars still don't support it because of the licensing scheme associated with iBiquity). It's kind of the opposite of what happened with HD television, which rolled out across the United States in less than five years. Part of the problem is HD Radio is arguably only slightly better (and sometimes worse) in quality than analog radio (depending on the type of audio you're listening to, and how you listen). At the same time, podcasting and streaming services (Spotify, Pandora, Apple Music) have been eating radio's lunch. It's a weird time in the broadcast radio industry.

## Enter RTL-SDR

For the past few years I have noticed 'RTL-SDR' ("Software Defined Radio") appearing in more publications I follow, notably on [Hackaday](https://hackaday.com/tag/rtl-sdr/) and in suggested communities on Reddit. And I figured maybe I could find a way to listen to KMOX-AM on a computer via RTL-SDR via an FM station simulcast.

After some preliminary research, much of it on [RTL-SDR.COM](https://www.rtl-sdr.com) and Google searches, it seemed the best general purpose receiver I could start with was the [RTL-SDR Blog v3](https://www.amazon.com/gp/product/B011HVUEME/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=9aeac8cb4109f9c6bf96949e952affbd&language=en_US) kit, which comes with a USB tuner, dipole antenna, and tripod stand.

{{< figure src="./rtl-sdr-radio-and-dipole-antenna.jpg" alt="RTL-SDR Blog v3 software defined radio with dipole antenna on desk" width="390" height="583" class="insert-image" >}}

This hardware has its lineage in older USB TV Tuner cards: even though the TV spectrum was fairly narrow, the chips used in many of the tuners were capable of receiving a much wider band of frequencies, and could be controlled via software after some reverse engineering.

The analog AM band is in the frequency range 540 to 1600 kHz, while the analog and digital FM band is in the frequency range 88 to 108 MHz. I won't get into the technical details of how AM (Amplitude Modulation) and FM (Frequency Modulation) work—partly because my own understanding is quite rudimentary—but one thing I quickly discovered was the RTL-SDR Blog v3 hardware works down to 500 kHz, but decoding the NRSC-5 (that's the standard for the HD signal) encoding for AM radio is difficult (in comparison to FM), since the data is packed into the narrower per-station AM bandwidth allotment differently.

## Listening to AM and FM Radio Stations on a Mac

I found a decent Mac GUI app, [LocalRadio](https://github.com/dsward2/LocalRadio), that allows listening to analog FM directly on the Mac, and streams the audio to other devices on the network via HTTP. But this app did not work with HD or AM signals, therefore it would only tune in the main analog FM stations (none of which carry a simulcast of KMOX-AM, which broadcasts the Cardinals games). It also had a few bugs which made it difficult to use.

In my preliminary exploration, I also found very helpful bandwidth visualization software, [Gqrx SDR](http://gqrx.dk/download), which was easy to install on my Mac with `brew cask install gqrx`. This software let me not only tune analog FM signals, but also visualize the spectrum so I could see the sidebands (in the image below, you can see two sidebands on the signal at 102.5 MHz) containing the HD subchannels:

{{< figure src="./gqrx-kezk-fm-spectrum-analyzer-rtl-sdr-hd-sidebands.png" alt="gqrx software analyzing frequency spectrum around KEZK-FM in St. Louis" width="488" height="482" class="insert-image" >}}

This was nice, and the tool is great for general frequency exploration (you're not limited to AM and FM radio signals, there's a whole world to explore with SDR!), but I was really interested in listening to HD radio so I could hear Cardinals ballgame broadcasts.

So I started looking for any software which would decode the HD radio sidebands, and eventually found [nrsc5](https://github.com/theori-io/nrsc5), named after the [NRSC 5](https://www.nrscstandards.org/standards-and-guidelines/documents/standards/nrsc-5-d/nrsc-5-d.asp) radio standard, which is used by HD Radio in the US. It was pretty easy to get started with it:

    # Install with Homebrew.
    $ brew install --HEAD https://raw.githubusercontent.com/theori-io/nrsc5/master/nrsc5.rb
    
    # Tune a station (102.5 FM) on HD 3 (which in St. Louis is a KMOX-AM simulcast)
    nrsc5 102.5 2

And bingo! Out of my Mac's speakers pops KMOX-AM, and I can listen to a Cardinals baseball game with a $30 USB radio dongle and open source software!

{{< figure src="./listening-to-hd-radio-1025-kezk-fm-kmox-am-stl-min.png" alt="Listening to HD Radio 102.5 KEZK-FM subchannel 3 in St. Louis - KMOX-AM" width="650" height="381" class="insert-image" >}}

## Streaming the radio through IP

This is great if I have my laptop nearby, but a lot of times the games are on at night, when I'm working on a house project, reading a book, or otherwise in a spot where carrying around an open laptop would not be prudent. So I want to be able to listen to the broadcast on my iPhone or iPad—neither of which have the software support (at least as of 2019) to directly interface with the RTL-SDR dongle.

Luckily, `nrsc5` has the built-in ability to output the stream as WAV data, which is extremely helpful if you want to stream it to other devices.

To demonstrate the basic ability, instead of listening to the audio directly from nrsc5 to the Mac's audio hardware, I can stream the output through VLC with the command:

    nrsc5 -o - 102.5 2 -l 3 | vlc -vvv -

This opens up VLC and starts playing the audio stream directly from `nrsc5`.

Once I have the stream in VLC, I can re-stream it over my home network:

    nrsc5 -o - 102.5 2 -l 3 | vlc - -I dummy --sout '#standard{access=http,mux=ogg,dst=10.0.100.119:8080/audio.ogg}'

(The `-l 3` squelches a lot of INFO log level output from `nrsc5`, and the `-I dummy` option for `vlc` prevents the UI from opening while the stream is going.)

After downloading the VLC app for iOS, I can connect to the stream using the 'Open Network Stream' feature, with the stream URL: `http://10.0.100.119:8080/audio.ogg` (The IP address is the IP of my Mac's main network interface. You can find that IP in the Network system preference pane.)

{{< figure src="./iphone-vlc-client-open-stream.png" alt="iPhone iOS VLC client opening audio stream" width="179" height="360" class="insert-image" >}}

Now I have HD Radio on my iPhone, all for a one-time $30 investment, using open source software. Take _that_, MLB blackouts and DTS/iBiquity! I just hope they don't read this blog post then find a way to add blackout restrictions for HD Radio...

## Future Improvements

The HD stream contains some extra metadata, including a couple lines of text describing the current show or event (though I've noticed no local radio stations seem to keep this updated correctly—the text is often wrong), and an image. Some higher-end HD Radio receivers display all this data, and I can see the information streaming past in the `nrsc5` log output, but it's time-consuming to get this data muxed properly into a stream through VLC.

It would also be nice if an app like LocalRadio could integrate with nrsc5 and allow changing of radio stations and HD subchannels directly via a mobile phone. Right now, if I want to switch stations, I have to go back to my Mac and re-start the stream on a new station/subchannel—not an ideal process.

In the end, I'm bewildered by the fact that it's so difficult to follow professional sports teams in 2019, but I'm happy since I now have the ability to listen to all Cardinals games, no matter what, and follow my home team. Hopefully they make the playoffs and have a successful run this year!
