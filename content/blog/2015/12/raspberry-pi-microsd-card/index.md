---
nid: 2519
title: "Raspberry Pi microSD card performance comparison - 2015"
slug: "raspberry-pi-microsd-card"
date: 2015-12-01T16:45:51+00:00
drupal:
  nid: 2519
  path: /blogs/jeff-geerling/raspberry-pi-microsd-card
  body_format: full_html
  redirects: []
tags:
  - comparison
  - microsd
  - performance
  - raspberry pi
aliases:
  - /blogs/jeff-geerling/raspberry-pi-microsd-card
---

<blockquote><strong>2018 Update</strong>: Please see the <a href="//www.jeffgeerling.com/blog/2018/raspberry-pi-microsd-card-performance-comparison-2018">latest benchmarks in 2018 using a Raspberry Pi model 3 B+</a>.</blockquote>

<p style="text-align: center;">{{< figure src="./microsd-cards-all-tested-raspberry-pi.jpg" alt="Variety of microSD cards tested with the Raspberry Pi model 2 B" width="400" height="310" >}}</p>

<blockquote>This post's benchmarks were performed on a Raspberry Pi 2; for all the latest benchmarks, on Raspberry Pi 3 or later revisions, check out the official <a href="http://www.pidramble.com/wiki/benchmarks/microsd-cards">Pi Dramble microSD card Benchmarks</a> page.</blockquote>

<p>In my experience, one of the highest-impact upgrades you can perform to increase Raspberry Pi performance is to buy the fastest possible microSD card—especially for applications where you need to do a lot of random reads and writes.</p>

<p>There is an <strong>order-of-magnitude difference</strong> between most cheap cards and the slightly-more-expensive ones (even if both are rated as being in the same class)—especially in small-block random I/O performance. As an example, if you use a normal, cheap microSD card for your database server, normal database operations can literally be <em>100x slower</em> than if you used a standard microSD card.</p>

<p>Because of this, I went and purchased over a dozen different cards and have been putting them through their paces. Here are the results of those efforts, in a nice tabular format:</p>

<hr />

<table>
<thead>
<tr>
<th>Card Make/Model</th>
<th><code>hdparm</code> buffered</th>
<th>
<code>dd</code> write</th>
<th>4K rand read</th>
<th>4K rand write</th>
</tr>
</thead>
<tbody>
<tr>
<td>OWC Envoy SSD (USB) 64GB</td>
<td>34.13 MB/s</td>
<td>34.4 MB/s</td>
<td>7.06 MB/s</td>
<td>8.20 MB/s</td>
</tr>
<tr>
<td>SanDisk Ultra Fit (USB) 32GB</td>
<td>31.72 MB/s</td>
<td>14.5 MB/s</td>
<td>4.99 MB/s</td>
<td>1.07 MB/s</td>
</tr>
<tr>
<td>Samsung EVO+ 32GB</td>
<td>18.45 MB/s</td>
<td>14.0 MB/s</td>
<td>8.02 MB/s</td>
<td>3.00 MB/s</td>
</tr>
<tr>
<td>Samsung Pro+ 32GB</td>
<td>18.46 MB/s</td>
<td>18.5 MB/s</td>
<td>8.10 MB/s</td>
<td>2.35 MB/s</td>
</tr>
<tr>
<td>Samsung Pro 16GB</td>
<td>18.39 MB/s</td>
<td>18.2 MB/s</td>
<td>7.66 MB/s</td>
<td>1.01 MB/s</td>
</tr>
<tr>
<td>Samsung EVO 16GB</td>
<td>17.39 MB/s</td>
<td>10.4 MB/s</td>
<td>5.36 MB/s</td>
<td>1.05 MB/s</td>
</tr>
<tr>
<td>SanDisk Extreme Pro 8GB</td>
<td>18.43 MB/s</td>
<td>17.6 MB/s</td>
<td>7.52 MB/s</td>
<td>1.18 MB/s</td>
</tr>
<tr>
<td>SanDisk Extreme 16GB</td>
<td>18.51 MB/s</td>
<td>18.3 MB/s</td>
<td>8.10 MB/s</td>
<td>2.30 MB/s</td>
</tr>
<tr>
<td>SanDisk Ultra 16GB</td>
<td>17.73 MB/s</td>
<td>7.3 MB/s</td>
<td>5.34 MB/s</td>
<td>1.52 MB/s</td>
</tr>
<tr>
<td>NOOBS (1.4, C6) 8GB</td>
<td>17.62 MB/s</td>
<td>6.5 MB/s</td>
<td>5.63 MB/s</td>
<td>1.01 MB/s</td>
</tr>
<tr>
<td>Transcend Premium 300x 32GB</td>
<td>18.14 MB/s</td>
<td>10.3 MB/s</td>
<td>5.21 MB/s</td>
<td>0.84 MB/s</td>
</tr>
<tr>
<td>PNY Turbo (C10 90MB/s) 16GB</td>
<td>17.46 MB/s</td>
<td>TODO</td>
<td>6.25 MB/s</td>
<td>0.62 MB/s</td>
</tr>
<tr>
<td>Toshiba 16GB</td>
<td>17.66 MB/s</td>
<td>11.2 MB/s</td>
<td>5.21 MB/s</td>
<td>0.21 MB/s</td>
</tr>
<tr>
<td>Sony (C10) 16GB</td>
<td>15.38 MB/s</td>
<td>8.9 MB/s</td>
<td>2.47 MB/s</td>
<td>0.24 MB/s</td>
</tr>
<tr>
<td>Kingston (C10) 16GB</td>
<td>17.78 MB/s</td>
<td>9.0 MB/s</td>
<td>5.75 MB/s</td>
<td>0.21 MB/s</td>
</tr>
<td>Kingston (C10) 8GB</td>
<td>12.80 MB/s</td>
<td>7.2 MB/s</td>
<td>5.56 MB/s</td>
<td>0.17 MB/s</td>
</tr>
<tr>
<td>Nasya C10 16GB</td>
<td>16.05 MB/s</td>
<td>8.4 MB/s</td>
<td>2.28 MB/s</td>
<td>0.38 MB/s</td>
</tr>
<tr>
<td>No-name (C4) 4GB</td>
<td>13.37 MB/s</td>
<td>&lt; 1 MB/s</td>
<td>&lt; 0.1 MB/s</td>
<td>&lt; 0.01 MB/s</td>
</tr>
</tbody>
</table>

<hr />

After using most of these cards in different situations over the past year or so (some for Pis running MySQL, others for file shares, and yet others just doing data logging and web dashboard displays), I've also noted that reliability-wise, <em>all</em> of the 16 cards I've used so far (even the no-name C4 card) have been flawless.

However, judging by performance vs. price, there are a couple clear standout cards—one is the Samsung Evo+, which is the fastest card for random access by a mile. And this year, I've seen it on sale for $10-20 for 32 or 64 GB, so it's a steal. Other than that, I'd go with the SanDisk Extreme, as it can be had for about the same price, or the Samsung Evo (without the +), as it can be had for even less if you just need 8 or 16 GB.

<strong>2015 Winner</strong>: <a href="https://www.amazon.com/Samsung-Class-Micro-Adapter-MB-MC32DA/dp/B00WR4IJBE/ref=as_li_ss_tl?ie=UTF8&qid=1467843453&sr=8-5&keywords=samsung+evo++microsd&linkCode=ll1&tag=mmjjg-20&linkId=bc986cc99177f24ca4b05bca3322ad89">Samsung Evo+ 32 GB</a> (~$12 on Amazon)
<h2>
<a id="user-content-benchmarks" class="anchor" href="#benchmarks" aria-hidden="true"><span class="octicon octicon-link"></span></a>Benchmarks</h2>

<h3>
<a id="user-content-hdparm-buffered" class="anchor" href="#hdparm-buffered" aria-hidden="true"><span class="octicon octicon-link"></span></a><code>hdparm</code> buffered</h3>


```
sudo hdparm -t /dev/mmcblk0
```

<p>Rationale: <code>hdparm</code> gives basic raw throughput stats for buffered reads (by the disk/device itself). You could also test with <code>-T</code> instead of <code>-t</code> to test the OS filesystem cache performance (which allows the OS to dramatically speed up certain read operations), but for our purposes we just want to test the device itself.</p>

<p>Setup:</p>

<ol>
<li>Install hdparm: <code>sudo apt-get install -y hdparm</code></li>
</ol>

<h3>
<a id="user-content-dd-write" class="anchor" href="#dd-write" aria-hidden="true"><span class="octicon octicon-link"></span></a><code>dd</code> write</h3>

```
sudo dd if=/dev/zero of=/drive/output bs=8k count=50k conv=fsync; sudo rm -f /drive/output
```

<p>Rationale: <code>dd</code> simply copies data from one place (<code>if</code>) to another (<code>of</code>). If your filesystem caches are big enough, this is a pretty poor disk speed comparison test. Because of that, make sure that <code>count</code> is set to a parameter large enough to cause the OS to actually write data to the drive (e.g. <code>50k</code> <code>8k</code> blocks ~= 400 MB, which shouldn't be able to be cached on a microSD card in a Pi!.</p>

<h3>
<a id="user-content-iozone-4k-random-readwrite" class="anchor" href="#iozone-4k-random-readwrite" aria-hidden="true"><span class="octicon octicon-link"></span></a><code>iozone</code> 4K Random read/write</h3>


```
iozone -e -I -a -s 100M -r 4k -r 512k -r 16M -i 0 -i 1 -i 2 [-f /path/to/file]
```

<p>Rationale: <code>iozone</code> is a very robust filesystem benchmark tool, which does a lot of useful tests that make sure you're getting a broad overview of read and write performance for a variety of block sizes and situations. I like the lower block size random I/O tests especially, because many operations (like logging data, writing a row to an ACID-compliant database, or bulk loading of data) require as fast of small-block-size random I/O as possible.</p>

<p>Most cheap microSD cards, even if rated as being 100MB/sec+ class 10 cards, can't sustain anywhere near that rate when writing random data—especially on the Raspberry Pi's measly data bus. (Note that most of the above benchmarks, when run on a USB 3.0 card reader on my MacBook Air, show 5, 10, or 15 times greater performance in that environment).</p>

<p>Setup:</p>

<ol>
<li>Download the <a href="http://www.iozone.org/">latest version</a>: <code>wget http://www.iozone.org/src/current/iozone3_434.tar</code>
</li>
<li>Expand the tarfile: <code>cat iozone3_434.tar | tar -x</code>
</li>
<li>Go into the <code>src</code> folder: <code>cd iozone3_434/src/current</code>
</li>
<li>Build the executable: <code>make linux-arm</code>
</li>
<li>Symlink the executable into your local bin folder: <code>sudo ln -s /home/pi/iozone_434/src/current/iozone /usr/local/bin/iozone</code>
</li>
</ol>

<h2>More Information</h2>

Check out the source for these benchmarks (which is updated every few months as I test new cards and newer versions of Raspbian): <a href="http://www.pidramble.com/wiki/benchmarks/microsd-cards">microSD card benchmarks - part of the Raspberry Pi Dramble Wiki</a>.
