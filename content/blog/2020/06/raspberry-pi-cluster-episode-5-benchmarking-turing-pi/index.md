---
nid: 3021
title: "Raspberry Pi Cluster Episode 5 - Benchmarking the Turing Pi"
slug: "raspberry-pi-cluster-episode-5-benchmarking-turing-pi"
date: 2020-06-29T14:12:48+00:00
drupal:
  nid: 3021
  path: /blog/2020/raspberry-pi-cluster-episode-5-benchmarking-turing-pi
  body_format: markdown
  redirects: []
tags:
  - benchmarking
  - benchmarks
  - cluster
  - drupal
  - raspberry pi
  - turing pi
  - video
  - youtube
---

At this point, I've showed you how you can use the Turing Pi as a Kubernetes cluster to run different things. I barely scratched the surface of what's possible with Kubernetes, but I'm planning on doing another series exploring Kubernetes itself later this year. [Subscribe to my YouTube channel](https://www.youtube.com/c/JeffGeerling) if you want to see it!

In this post, I'm going to talk about the [Turing Pi](https://turingpi.com)'s performance. I'll compare it to a more traditional Raspberry Pi cluster, my [Pi Dramble](http://www.pidramble.com), and talk about important considerations for your cluster, like what kind of storage you should use, or whether you should run a 32-bit or 64-bit Pi operating system.

As with all the other work I've done on this cluster, I've been documenting it all in my open source [Turing Pi Cluster project on GitHub](https://github.com/geerlingguy/turing-pi-cluster).

## Video version of this post

This blog post has a companion video embedded below:

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/IoMxpndlDWI" frameborder='0' allowfullscreen></iframe></div>

## Benchmarks

The first thing I want to talk about is benchmarks. But before I get into benchmarks on the Turing Pi, it's important to introduce the topic of benchmarking and explain why I choose certain benchmarks, and how I run them.

There are plenty of sites out there that run every benchmark under the sun on computers ([example](https://www.tomshardware.com/reviews/intel-xeon-w-3175x-cpu,5976.html)), and while that's great for some cases, raw benchmarks out of context are not helpful to me.

If you don't focus on what's important, benchmarking will make you mad, and you'll start just benchmarking anything and everything.
When I benchmark a cluster like the Turing Pi, I test on two layers:

First, I test on the system level, to see raw performance potential. I can test the maximum theoretical performance of all the major subsystems: disk, network, and CPU.

Second, I test on the application level, so I can see how raw performance translates into real-world use.

Both types of benchmarks are helpful to understand the full performance of a cluster, and no matter what system I'm building, I want to have a baseline so I can understand how it performs. And I can quickly see if it will meet my needs or not.

### How I benchmark

So I have a few things I want to benchmark, how can I make sure my benchmarks are good and useful?

Well, the first and most important thing, as with any scientific endeavor, is to make sure the benchmark is _reproducible_.

If I run it now, and I run it tomorrow, and I run it a thousand more times, will it be within a close range every time I run the benchmark? If not, there are two possibilities: one, it could be a bad benchmark, and I should try something different, or two, it could be exposing a flaw in the system, like poor temperature control, or a flaky processor. Typically it's the former, but whenever I see a result that surprises me, I spend a lot of time trying to make sure that it's not a mistake I made in my benchmark.

And to make sure that the numbers I present are accurate, I run every benchmark at _least_ three times. And I usually run the benchmark once to 'warm up' the system. Then I run it three times, giving a brief 'cool down' period between each run.

Every benchmark I've done is documented in excruciating detail [in my Pi Cluster repository](https://github.com/geerlingguy/turing-pi-cluster/issues/11), so if you want to try the benchmarks on your own, it's easy to do.

If anyone presents performance benchmarks but doesn't provide a way to exactly reproduce the testing environment and run the benchmark, then you shouldn't trust the benchmark. A lot of tech companies do this by posting graphs without scales or references to the benchmark they used. Don't trust them! Always research on your own if you want to know the true performance of a system.

You might be wondering why I spent so much time talking about _how_ I benchmark. That's because I try to make my results bulletproof. If you find a flaw in one of these benchmarks, please mention it in the comments below, or open an issue on the Turing Pi Cluster repository. I'd love to make them even better!

### Disk Performance

One of the most interesting things I discovered benchmarking the Turing Pi cluster is the performance of different disk options. Over the past few years, I've done [extensive testing on hundreds of microSD cards](/blog/2019/raspberry-pi-microsd-card-performance-comparison-2019), because they are the easiest means to boot up most Raspberry Pis.

Some people boot their Raspberry Pis [using an external USB hard drive](/blog/2020/im-booting-my-raspberry-pi-4-usb-ssd), and that offers better performance and potentially better endurance over long periods of time, but it also adds to the footprint of a Raspberry Pi and makes for a bit of a cabling nightmare.

The Raspberry Pi Compute Module, which is used in the Turing Pi, has the most flexibility of all the Pi models in choosing what kind of persistent storage you want to use. You have the options of:

  - Onboard eMMC, which is fast for random access, more durable than microSD, and a little slower for large file reads and writes.
  - microSD cards, which are slow for random access, not as durable with heavy use, but are cheap and often fast enough for general use.
  - External USB storage, which is hampered a bit on the older Compute Module 3+ in comparison to the latest Pi 4, but still offers comparable performance to eMMC with much faster large file reads and writes.

But how much of a difference are we talking about?

{{< figure src="./1-cm3-disk-io.png" alt="Compute Module 3+ Disk IO benchmarks" width="600" height="317" class="insert-image" >}}

Well, this first graph shows all three options used with a Compute Module 3+. In all the tests, using a microSD card is the slowest option.

The 'hdparm' test checks how fast large files can be written to the disk with a buffer. If you use a Pi as a NAS or media server, this is a good benchmark to see how quickly files can be transferred to and from your Pi's storage.

The 'dd' test checks how fast large files can be written, without buffering. Paired up with the 'hdparm' test you can get a good idea of relative performance for sequential disk access, which is useful for copying big files around.

The '4K' tests are a better indicator for how well the storage will perform for most tasks, though. On a Raspberry Pi, opening a browser, checking email, running a webserver, and the like all require fast random access performance—the faster the better.

So judging by these graphs, it's a good idea to buy the Compute Module 3+ with onboard eMMC storage, because it's anywhere between 25-50% faster than using a microSD card.

And an external SSD and the performance is almost doubled, especially when you're copying large files, but even doing things like writing lots of tiny files, which is something I do a lot when I'm working on my web projects.

The nice thing about the Turing Pi is you can choose whichever option you'd like. Each Compute Module gets its own microSD card slot, so whether you buy the Compute Module with eMMC or go the cheaper route and get it without eMMC, you can use it in the Turing Pi. For USB, only four of the Compute Modules get dedicated USB ports, but you can still configure the cluster so there is faster persistent USB storage available to your applications.

To get an idea of where the current Compute Module generation suffers compared to the latest and greatest Raspberry Pi 4, I also ran these tests on one of my Pi 4s:

{{< figure src="./2-cm3-pi4-sequential.png" alt="Compute Module 3+ vs Pi 4 Sequential Access Disk Benchmarks" width="600" height="274" class="insert-image" >}}

For large files, you can see the blazing speed difference you get from the Pi 4's USB 3.0 ports, which are many times faster than the USB 2.0 ports you get out of a Compute Module.

{{< figure src="./3-cm3-pi4-random.png" alt="Compute Module 3+ vs Pi 4 Random Access Disk Benchmarks" width="600" height="284" class="insert-image" >}}

The difference is slightly less pronounced for random access, but the Pi 4 still outshines the Compute Module 3+ there, especially for random write performance on USB.

Note that there is no eMMC option for the Pi 4, so you basically have to choose between much-slower microSD storage, or much-faster external SSD. There's no middle ground like there is with the Compute Module.

So while the Pi 4 wins by a mile for raw performance, the Compute Module wins for convenience and flexibility, and hopefully the next Compute Module version will catch up to its larger and newer sibling.

In the end, there are two main things that crippled the Pi's older models compared to the Pi 4: first, USB 3.0 has ten times the bandwidth that USB 2.0 had. Second, the Pi 4 supports UASP, or the USB-Attached SCSI Protocol. This makes transfers even faster. I ran tests on the Pi 4 with UASP off and on, and it not only made file transfers 20-30 percent faster, it even shaved off almost 10% of the power consumption, since it's lighter on the Pi's CPU.

#### Booting via USB or the Network

I won't dive into netboot performance yet, as there are some peculiarities I'm still exploring, but I'll probably cover netboot in a separate post.

Regarding USB boot, it is not too hard to get the Compute Module to boot over USB. And for the Pi 4, booting via USB is currently in beta, but by the time you read this, it's probably also supported natively. I have a separate blog post that talks about my experience [booting the Pi 4 from a USB SSD](/blog/2020/im-booting-my-raspberry-pi-4-usb-ssd).

One interesting thing I discovered was the Pi Foundation's [documentation states](https://www.raspberrypi.org/documentation/hardware/raspberrypi/bootmodes/msd.md) the Compute Module 3+ doesn't explicitly need USB boot mode enabled, but when I was testing it, I did have to enable it like on other Pi models.

Also, if you have a flashed eMMC Compute Module and want to boot off a USB drive, you have to move or delete the `bootcode.bin` file off the eMMC's `boot` volume so the Compute Module searches for a USB boot volume. There are some other quirks with USB booting on the Compute Module, but I won't get too much into the weeds here.

I will say that for best performance, you should consider at least booting the master Pi from a USB SSD, no matter what kind of Pi-based cluster you're building. And if possible, set up Kubernetes Persistent Volumes to use an SSD for the storage backend, even if it's as simple as configuring NFS on the master Pi.

### Network Performance

Moving on from disk IO to network IO, we see a similar story play out for the Compute Module 3+ versus the Pi 4. The 3+ shares one bus for both USB and Networking, so if you do a file copy over the network, it actually makes the theoretical maximum speed slower!

{{< figure src="./4-network-cm3-pi4.png" alt="Network benchmarks - CM3+ vs Pi 4" width="600" height="248" class="insert-image" >}}

This graph shows the raw throughput you can get through a single Compute Module 3+, through all 7 Compute Modules in the Turing Pi at once, and then through a single Raspberry Pi 4 with its dedicated gigabit ethernet interface.

Even combined, and in the best-case scenario, 7 Turing Pis transferring data at full tilt can't match a single Pi 4 with its Gigabit interface. An important thing to note is that, luckily, the Turing Pi has a Gigabit network backplane, so you can use all of the Compute Modules at full speed simultaneously.

Also remember that you may not be able to stack multiple Pi 4's together to get more than one gigabit of bandwidth, unless you have a fast 10 Gbps network. And in either case, you'd likely be limited by Internet bandwidth if what you're doing requires data transfer over the Internet.

I hope the Compute Module 4 will have the same kind of networking performance seen in the Pi 4, as that will open up massive new capabilities. And depending on how the next version is built, it could also save on the cost of the Turing Pi, if the board itself doesn't have to build in 7 separate network interfaces like it currently does!

### CPU Performance

All right, so the Compute Module 3+ has some big limitations against the newest Pi 4 when it comes to disk and network performance. How does it compare in terms of the processor?

The Compute Module 3+ has a CPU that's capped at 1.2 GHz due to power supply limitations, so it's even a tiny bit slower than the regular Pi 3+ model B, which runs at 1.4 GHz. And it will certainly run slower than the Pi 4, which has a newer architecture and runs at 1.5 GHz.

To get a sense of the raw CPU performance, I ran some tests using [Phoronix](https://www.phoronix-test-suite.com), which is an open source automated benchmarking tool that is used for many different systems.

I ran three tests: a video encoding test, an MP3 encoding test, and a PHP performance benchmark.

Since the Raspberry Pi 64-bit beta was also introduced, I ran these tests on both the 32-bit and 64-bit versions of Pi OS, to see whether the 64-bit operating system would make a difference with system performance.

{{< figure src="./5-x264-video-encode.png" alt="x264 video encode Phoronix benchmark - CM3+ vs Pi 4" width="600" height="194" class="insert-image" >}}

This test illustrates how much of an improvement a new chip architecture can make, like the one in the Pi 4. It has optimizations for things like video encoding that make a bigger difference than the chip speed would indicate. Going from 1.2 to 1.5 GHz is a 22% difference in clock cycles, but the different chip architecture means real world performance—at least for encoding video—is a whopping 80% faster!

It was also interesting to see that running the 64-bit OS made this test run about 7% faster. We'll see if that holds up in other tests.

{{< figure src="./6-lame-mp3-encoding.png" alt="Lame MP3 audio encode Phoronix benchmark - CM3+ vs Pi 4" width="600" height="203" class="insert-image" >}}

The MP3 encoding shows the race is a little closer, but the Pi 4 still shows a sizeable performance increase. This graph shows that the Pi 4 takes about half the amount of time to encode an MP3 as the Compute Module 3+. In this test, the difference between running a 32-bit and 64-bit Pi OS is very pronounced, though, with a 30% performance increase when running in 64-bit mode.

{{< figure src="./7-phpbench.png" alt="PHPBench Phoronix benchmark - CM3+ vs Pi 4" width="600" height="193" class="insert-image" >}}

The final CPU test I did was this PHPBench run. It tests the raw potential of a PHP application doing CPU-heavy tasks, but it's not necessarily representative of what a real-world PHP application like Wordpress or Drupal would do. But it also shows the Pi 4 as running more than twice as fast as the Compute Module 3+. And again if you want the best performance for CPU-intense tasks, then you should run the 64-bit version of Pi OS.

#### Thermal Management

One other thing I wanted to mention: earlier I talked about the importance of rigorous benchmarking techniques. Another thing that I like to test is the thermal performance of different setups. One problem that you might run into if you test Raspberry Pis is thermal throttling.

In Grafana, in the previous episode, we created a graph to track the CPU temperature of all the Pis, so we could confirm they weren't throttling. You can also use an IR camera, like the [Seek Thermal camera](https://www.amazon.com/Seek-Thermal-Compact-All-Purpose-MicroUSB/dp/B00NYWABAA/ref=as_li_ss_tl?th=1&linkCode=ll1&tag=mmjjg-20&linkId=a30c2765f811de7312548a370934d35b&language=en_US) I have, to measure the temperature across all parts of the Pi.

<p style="text-align: center;"><video width="400" height="300" controls="controls">
<source src="./bootup-thermal-seek-turing-pi.mp4" type="video/mp4">
</video></p>

In this thermal video, I'm showing how the Turing Pi cluster looks as it boots up. The video is sped up a bit, but you can see that nothing on the board gets above 50 to 60 degrees celsius. The Turing Pi cluster and the Compute Module 3+ both seem to do well even under load, and even when I put them inside my Mini ITX case, for long periods of time.

I never encountered thermal throttling even after running multi-hour CPU benchmarks on multiple Compute Modules at the same time.

The same can't be said for the Pi 4, though; when I use it inside a case, I have to use a fan or a special heat sink case like a [Flirc case](https://www.amazon.com/Flirc-Raspberry-Pi-Case-Silver/dp/B07WG4DW52/ref=as_li_ss_tl?crid=3JHCBO5SSVU6T&cv_ct_cx=flirc+case+raspberry+pi+4&dchild=1&keywords=flirc+case+raspberry+pi+4&pd_rd_i=B07WG4DW52&pd_rd_r=57f92354-90b4-4dcd-aea6-5fed418fd706&pd_rd_w=cBzu5&pd_rd_wg=LgrXJ&pf_rd_p=1da5beeb-8f71-435c-b5c5-3279a6171294&pf_rd_r=PEC781A88TD47PFJR514&psc=1&qid=1592923012&sprefix=flirc+,aps,170&sr=1-1-70f7c15d-07d8-466a-b325-4be35d7258cc&linkCode=ll1&tag=mmjjg-20&linkId=698a701342765aba0cfb8caff6c6d1ee&language=en_US), otherwise the Pi 4 starts throttling the CPU and making the benchmarks much slower.

{{< figure src="./electrical-tape-to-show-cpu-temp.jpg" alt="Electrical tape to show CPU surface temperature" width="480" height="360" class="insert-image" >}}

One more note on measuring thermals with an infrared camera like the one I have: reflective surfaces like the metal cover on the Pi's SoC (System on a Chip) are kind of 'invisible' to thermal cameras, because they do not have high thermal emissivity. When I measure temperatures, I make sure to put a piece of electrical tape or [high-temperature kapton tape](https://www.amazon.com/ELEGOO-Polyimide-Temperature-Resistant-Multi-Sized/dp/B072Z92QZ2/ref=as_li_ss_tl?dchild=1&keywords=kapton+tape&qid=1592923097&sr=8-3&linkCode=ll1&tag=mmjjg-20&linkId=ad4ec588033d6a39fd0f6c787b34c7dd&language=en_US) over the SoC like I did in the image above so the actual surface temperature can be picked up by my camera.

### Application Benchmarks

Putting everything together, I also measured some simple application-level benchmarks, for programs that were running on the cluster. Note that some applications may be more or less impacted by individual node performance in a Kubernetes cluster, as some applications can scale better than others across multiple servers.

{{< figure src="./8-drupal-operations.png" alt="Drupal operations benchmark - CM3+ vs Pi 4" width="600" height="268" class="insert-image" >}}

This graph seems consistent with the CPU benchmarks, but there are two important differences. The graph shows how long it takes to do certain things in Drupal, like installing it, and loading a page with the default installation. But with real-world applications, the Compute Module 3+ is only about 40% slower than the Pi 4. It's still not a speed champ, but this graph highlights the fact that real world applications paint a more complex picture when it comes to benchmarking. You can't take one benchmark—like a video encoder or something like Geekbench—and apply it universally.

Also, contrary to what we saw in previous benchmarks, the 64-bit OS actually performed _slower_ than the 32-bit OS. How can that be? Well, even if you have more RAM available, there are some operations which tend to run more efficiently—even if only slightly—when you have 32-bit memory addresses. And it seems that Drupal is not tuned for the highest performance memory management on 64-bit operating systems.

But the performance difference is more pronounced on a computer like the Compute Module 3+, because the Compute Module 3+ only has one gigabyte of memory. On larger Pis, like the 8 GB Pi 4, the greater availability of RAM makes memory-constrained performance differences much less noticeable.

{{< figure src="./9-drupal-page-requests.png" alt="Drupal page requests benchmark - CM3+ vs Pi 4" width="600" height="260" class="insert-image" >}}

And that performance difference translates also to page load performance, which is more purely CPU and memory-bound than Drupal installation or first page load operations.

In this graph, you can see the Pi 4 is slightly more than twice as fast. And in an interesting twist, the Compute Module shows a lot less performance under the 64-bit OS, but mostly that's down to process tuning: with PHP running under Apache, the default configuration I used creates more threads than are optimal for a small server with 1 GB of RAM, so there is slightly more RAM-to-disk swapping that goes on when running a 64-bit OS.

If properly tuned, the numbers would likely be much closer, as they are in the Pi 4 test, which shows only a 5% difference.

{{< figure src="./wordpress-page-requests-cm3-pi4.png" alt="Wordpress page request benchmarks CM3+ vs Pi 4" width="600" height="269" class="insert-image" >}}

And looking at Wordpress, you can see that the performance difference is even closer between the Pi 4 and the Compute Module 3+. In this case, I just ran the benchmark on each cluster running 32-bit Hypriot OS for a direct comparison, but for Wordpress, the difference between running on 32-bits and 64-bits was much less than with Drupal, likely because Wordpress requires less RAM overall.

### Compared to Cloud and my own laptop

Up to now, I've only been comparing things on the Turing Pi cluster and on my Pi Dramble cluster. But you might be wondering, how do both of these clusters stack up against the same sort of cluster running in AWS in the cloud, or against a fast modern laptop?

{{< figure src="./10-drupal-cloud-comparison-1.png" alt="Drupal operations benchmark - Pi 4 vs AWS T3 vs Mac i9" width="600" height="228" class="insert-image" >}}

{{< figure src="./10-drupal-cloud-comparison-2.png" alt="Drupal page requests benchmark - Pi 4 vs AWS T3 vs Mac i9" width="600" height="233" class="insert-image" >}}

Well, I did some more tests, and compared Drupal running on a Single Pi 4 versus an AWS T3 small instance versus my own Intel i9 laptop, and here are those results.

You can see the Pi itself—even the most high-end model you can buy today—has a bit of a ways to go before it will be as fast as a common cloud computing instance.

And I put in my own laptop just as a reference. You'd need to run at least four of the fastest Raspberry Pi 4 models (in a cluster that likely costs $500 or more in total), and you'd still not hit the same performance as a modern Core i7 or i9 laptop with a fast SSD and 16 GB of RAM.

So while the Pi is an excellent platform for testing, discovery, and learning—and a machine like the Turing Pi can even be used to run production applications, if you're looking for the most performance you can get for a decent price, the Raspberry Pi is not a great option.

## Conclusion

Does that mean you shouldn't build a Pi cluster? Not at all! Also, does the fact that the Pi 4 is much faster in many ways make the Compute Module 3+ and current Turing Pi a bad choice? Not necessarily. I'm going to cover some of the unique features of the Turing Pi that make it a useful tool regardless of the performance in the next video, and I'll also discuss what's next for the Compute Module, the Turing Pi, and why you still might want to build a Pi cluster.

Make sure you're [subscribed to my YouTube channel](https://www.youtube.com/c/JeffGeerling) don't miss any of my Pi Cluster series videos! And if you want me to keep making blog posts and videos like this, please consider supporting me on [GitHub](https://github.com/sponsors/geerlingguy) or [Patreon](https://www.patreon.com/geerlingguy).
