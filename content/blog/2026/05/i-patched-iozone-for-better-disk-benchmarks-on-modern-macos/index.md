---
date: '2026-05-26T20:32:00-05:00'
tags: ['iozone', 'benchmark', 'pyinfra', 'mac', 'macos', 'c', 'open source']
title: 'I patched iozone for better disk benchmarks on modern macOS'
slug: 'i-patched-iozone-for-better-disk-benchmarks-on-modern-macos'
---
A decade ago, I settled on [`iozone`](https://iozone.org) for disk benchmarking on all my systems. Tools like `fio` ('Flexible IO' tester) are a little more capable for raw disk performance testing, and other tools test network-scale filesystems better, but `iozone` gives me an easy overview of real-world disk performance across hard drives and SSDs, and runs on Mac, Windows, and Linux (and a smattering of other OSes).

{{< figure
  src="./iozone-website.jpg"
  alt="iozone Website with filesystem performance graph"
  width="700"
  height="auto"
  class="insert-image"
>}}

It's been around [since 1991](https://www.iozone.org/src/stable/iozone.c), and is still updated today—in fact, the two latest updates (version 509 and 510) contain patches I sent in to get iozone to compile on Apple Silicon Macs running newer releases of macOS.

I was benchmarking a MacBook Neo, and the `iozone` compilation step broke my [PyInfra benchmarking scripts](https://github.com/geerlingguy/sbc-reviews/tree/master/benchmark). I think MacPorts and Homebrew tweaked their build scripts to override any errors, but it's better to just fix the upstream code.

I'm pretty bad with C, so I used a local Qwen model to help validate my fixes; see my patches in [this GitHub issue](https://github.com/geerlingguy/sbc-reviews/issues/102#issuecomment-4047219198).

I emailed the patches to Don Capps, who maintains `iozone`, and he incorporated them into the source. Version 510 contains the fix, and builds on all my Macs running macOS 26 with Clang 21.0.0.

```
cd ~/Downloads
curl "http://www.iozone.org/src/current/iozone3_510.tar" | tar -x
cd iozone3_510/src/current
make --quiet macosx
```

The clang compiler still spits out a number of deprecation warnings, but you can ignore those.

After a few seconds, you should be able to run iozone to benchmark any storage device on your Mac (set the `-f` parameter to a file path in any connected volume, to test the filesystem performance on that volume).

Here I'm running it in my Downloads directory, to benchmark the SSD built into the Mac:

```
./iozone -e -I -a -s 1g -r 4k -r 1024k -i 0 -i 1 -i 2 -f ~/Downloads/iozone
```

With a 1GB test file size on my MacBook Neo, testing at 4k and 1M block sizes, I get the result:

```
$ ./iozone -e -I -a -s 1g -r 4k -r 1024k -i 0 -i 1 -i 2 -f ~/Downloads/iozone
  Iozone: Performance Test of File I/O
          Version $Revision: 3.510 $
    Compiled for 64 bit mode.
    Build: macosx 

  Contributors:William Norcott, Don Capps, Isom Crawford, Kirby Collins
               Al Slater, Scott Rhine, Mike Wisner, Ken Goss
               Steve Landherr, Brad Smith, Mark Kelly, Dr. Alain CYR,
               Randy Dunlap, Mark Montague, Dan Million, Gavin Brebner,
               Jean-Marc Zucconi, Jeff Blomberg, Benny Halevy, Dave Boone,
               Erik Habbinga, Kris Strecker, Walter Wong, Joshua Root,
               Fabrice Bacchella, Zhenghua Xue, Qin Li, Darren Sawyer,
               Vangel Bojaxhi, Ben England, Vikentsi Lapa,
               Alexey Skidanov, Sudhir Kumar.

  Run began: Tue May 26 16:17:26 2026

  Include fsync in write timing
  F_NOCACHE=1 - Turns data caching off
  Auto Mode
  File size set to 1048576 kB
  Record Size 4 kB
  Record Size 1024 kB
  Command line used: ./iozone -e -I -a -s 1g -r 4k -r 1024k -i 0 -i 1 -i 2 -f /Users/jgeerling/Downloads/iozone
  Output is in kBytes/sec
  Time Resolution = 0.000001 seconds.
  Processor cache size set to 1024 kBytes.
  Processor cache line size set to 32 bytes.
  File stride size set to 17 * record size.
                                                                    random    random      bkwd     record     stride                                        
              kB  reclen    write    rewrite      read    reread      read     write      read    rewrite       read    fwrite  frewrite     fread   freread
         1048576       4    666141    188600   1465976   8232715   4415111    915494                                                                
         1048576    1024    859037   1358016   1449306  16421172  15936521   1087545                                                                

iozone test complete.
```

An average of 1.5 GB/sec for 1MB reads and writes isn't bad. Though writing that... it's mind-numbing how fast local storage has gotten in the past decade since we switched from HDD to SSD, and then from SATA to NVMe. 1.5 GB/sec is insanely fast, historically speaking. But it's rather slow for a single NVMe drive compared to my other machines!

Huge thanks to Don Capps for incorporating my patches into `iozone`, so it can be used on all flavors of macOS, in addition to Windows, Linux, FreeBSD, etc.
