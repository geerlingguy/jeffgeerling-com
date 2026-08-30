---
date: '2026-08-30T17:09:00-05:00'
tags: ['rfc 867', 'rfc 868', 'time', 'daytime', 'ntp', 'history', 'timing', 'linux', 'internet']
title: 'Before NTP there were Time and Daytime'
slug: 'rfc-867-868-time'
---
In building an NTP time demo on old Macs for [VCF Midwest](https://vcfmw.org), I came across [RFC 867](https://www.rfc-editor.org/info/rfc867/) and [RFC 868](https://www.rfc-editor.org/info/rfc868/), for the 'Daytime' and 'Time' Protocols, respectively.

{{< figure
  src="./rfc-867-daytime-protocol.png"
  alt="RFC 867 Daytime Protocol"
  width="700"
  height="auto"
  class="insert-image"
>}}

My first exposure to any form of network time was when I upgraded from a used PowerBook 180c to my first 'new' computer, a Power Mac G3, in 2000. With the introduction of Mac OS 8.5, Apple added a 'Network Time Server' option in the Date & Time Control Panel.

I remember dialing up the Internet via PPP, then clicking the 'Set Time Now' button, and seeing my computer's clock update. I didn't think much of it at the time, but this was way more than setting my wristwatch using the 'Time and Temperature' phone line, which was previously the most precise time source I could access regularly.

But prior to NTP ([RFC 1059](https://www.rfc-editor.org/info/rfc1059/) in 1988), there was a much more informal way of requesting time from a remote server. With the Time Protocol (RFC 868), a time request was as simple as:

  1. Open a connection to the server on port 37 (TCP connect, or send an empty UDP datagram)
  2. Receive the time as a 32-bit binary number

That's it!

In the mid-80s, this was an extremely efficient method of time transfer, which was helpful since network bytes were precious, and you didn't need a complex routine to handle the 32-bit time.

But there are downsides to this simplistic approach. Especially if you were routing the request through the Internet, with multiple non-deterministic hops:

  - The 32-bit number was just "seconds since 00:00 (midnight) 1 January 1900
GMT", so the _best_ timing resolution you could ever get is 1 second (NTP gives 64-bit resolution, which can scale past microseconds).
  - There is no timestamping of the actual request or response, so there's no way to account for network delays, or average them out over time.
  - The 32-bit integer value will run out on February 7, 2036, resulting in a 'Y2K36' bug similar to the [Unix Y2K38 Epochalypse](https://en.wikipedia.org/wiki/Year_2038_problem). (NTP has the same problem but introduced [Eras](https://www.ntp.org/reflib/y2k/) to deal with it.)

But in 1983, when the RFC was introduced, it was just a convenient way for a computer on a network to get time from a server with a stable clock (many computers didn't have a real-time clock). It wasn't used for critical services like distributed databases, especially since timing resolution beyond 1 second wasn't that common in computing (assuming you even _had_ a world clock!).

The Daytime protocol (RFC 867) is succinct, but ambiguous. It defines a protocol by which an entire day and timestamp can be returned in human-readable output, for example:

```
Tuesday, February 22, 1982 17:37:43-PST
```

The ambiguity comes with the format, which is left to the implementor:

> ```
> There is no specific syntax for the daytime.  It is recommended that
> it be limited to the ASCII printing characters, space, carriage
> return, and line feed.  The daytime should be just one line.
>
>     One popular syntax is:
>
>         Weekday, Month Day, Year Time-Zone
>
>         Example:
>
>            Tuesday, February 22, 1982 17:37:43-PST

Immediately following, it suggests the alternative `dd mmm yy hh:mm:ss zzz`, which was used for SMTP!

Fun fact: [NIST still runs RFC 867/868 Daytime services](https://www.nist.gov/pml/time-and-frequency-division/time-distribution/internet-time-service-its#daytime-protocol-rfc-867) on `time.nist.gov`!

```
$ nc time.nist.gov 13

61281 26-08-29 23:31:43 50 0 0 771.1 UTC(NIST) *
```

This is using a customized response that matches neither of the RFC formats:

```
JJJJJ YR-MO-DA HH:MM:SS TT L H msADV UTC(NIST) OTM
```

Where `JJJJJ` is the [Modified Julian Date](https://en.wikipedia.org/wiki/Julian_day), and the OTM is an 'on-time marker', which marks that the time should be correct the moment you receive it... but from my research is more of a 'best guess' that was more useful in older [telephone time systems](https://www.nist.gov/pml/time-and-frequency-division/time-distribution/automated-computer-time-service-acts)[^telephone], which were in _some_ ways more deterministic.

NIST's is definitely one of the stranger [time formats](http://www.leapsecond.com/java/gpsclock.htm) I've seen!

The Time and Daytime Protocols were both shepherded by [Jon Postel](https://en.wikipedia.org/wiki/Jon_Postel), a.k.a. the 'God of the Internet', known for other hits like SMTP, IANA, and [Postel's law](https://en.wikipedia.org/wiki/Robustness_principle).

I often wonder what it was like to be on the ground floor when these protocols and services were written. I was more worried about getting time on my family's Nintendo. Not that my toddler brain could've comprehended network time transfer back then!

## Run your own Time and Daytime Server

After taking a nice long detour learning about Time and Daytime, I decided I would add some easter eggs at my booth at VCF Midwest—one of them being Time/Daytime services on ports 37 and 13, respectively.

If you want to run your _own_ Time/Daytime server, it's easy in Linux—they're built into [`xinetd`](https://linux.die.net/man/8/xinetd). These instructions are for Pi OS / Debian, but it's similar on other distros:

```
# Install and enable xinetd
sudo apt install xinetd
sudo systemctl enable xinetd

# Edit time and daytime configurations
sudo nano /etc/xinetd.d/time
  -> service time tcp set disable to "no"
  -> service time udp set disable to "no"

sudo nano /etc/xinetd.d/daytime
  -> service daytime tcp set disable to "no"
  -> service daytime udp set disable to "no"

# Restart xinetd
sudo systemctl restart xinetd
```

Make sure ports 37 and 13 are open on your firewall, then from another computer on the network:

```
# Time
$ nc 10.0.37.60 37 | xxd -g 1
00000000: ee 3f 24 b3                                      .?$.

# Verify the Time value by passing it into `date`:
$ date -r $(( 0xee3f24c8 - 2208988800 ))
Sun Aug 30 16:53:12 CDT 2026

# Daytime
$ nc -v 10.0.37.60 13
Connection to 10.0.37.60 port 13 [tcp/daytime] succeeded!
30 AUG 2026 16:49:26 CDT
```

The `2208988800` in the `date` translation command above is the difference (in seconds) between 1900 and 1970, required because [UNIX time](https://en.wikipedia.org/wiki/Unix_time)'s epoch is in 1970 (versus 1900 for Time and NTP).

If you'll be at VCF Midwest—especially if you have a vintage computer with Networking attached to the show's network—I can give you a good Time. Or Daytime, for that matter!

[^telephone]: Apparently NIST's [ACTS dial-up time service](https://www.nist.gov/pml/time-and-frequency-division/time-distribution/automated-computer-time-service-acts#software) is still used 200-300 times per day!
