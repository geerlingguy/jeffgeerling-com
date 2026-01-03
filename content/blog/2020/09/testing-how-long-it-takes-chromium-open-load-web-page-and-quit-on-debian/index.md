---
nid: 3040
title: "Testing how long it takes Chromium to open, load a web page, and quit on Debian"
slug: "testing-how-long-it-takes-chromium-open-load-web-page-and-quit-on-debian"
date: 2020-09-09T20:27:56+00:00
drupal:
  nid: 3040
  path: /blog/2020/testing-how-long-it-takes-chromium-open-load-web-page-and-quit-on-debian
  body_format: markdown
  redirects: []
tags:
  - apps
  - benchmarking
  - Chrome
  - chromium
  - performance
  - raspberry pi
---

Something I've long been meaning to benchmark, but never really got around to, is benchmarking the amount of time it takes on a Raspberry Pi to open a browser, load a page, and quit.

This is a relatively decent thing to benchmark, compared to other raw performance metrics, because it's something that probably 99% of Raspberry Pi users who use it with a GUI will do, with some frequency (well, probably loading more than one page before quitting, but still...).

So I asked on Twitter:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">So... if I want to measure how long it takes to:<br><br>1 Open Chrome/Chromium<br>2 Load a web page<br><br>And I want to do this in Linux (Debian), and have an objective measure of that time (until the page finishes loading)... is there any way to do that?<br><br>CLI opens then sits until you quit.</p>&mdash; Jeff Geerling (@geerlingguy) <a href="https://twitter.com/geerlingguy/status/1303779579228717057?ref_src=twsrc%5Etfw">September 9, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

And quickly, I received a number of responses about headless chromium or selenium, which I have used before and are great—but doesn't measure the full cycle of opening a browser in the GUI, loading a page, and quitting it.

I was trying to script it with some bash, but trying to get `chromium-browser` to open, load a page, and exit in a way that I could time it was futile. And unlike the `open` command on my Mac (paired with some other tools), I couldn't figure out a way to launch Chromium, have it load a page, then drop to something else to quit it and measure the time automatically.

And there's no way I was going to go to the old school stopwatch method—too inaccurate!

## Using puppeteer

One of the responses in my Twitter thread, [from @ericjduran](https://twitter.com/ericjduran/status/1303782175859503107), mentioned [puppeteer](https://github.com/puppeteer/puppeteer/), a 'headless Chrome Node.js API'. I thought it might be hard to get it to work with a fully-loaded, non-headless instance, but it wasn't.

And it was a heck of a lot simpler (and faster) to configure than Selenium, which is kind of a pain to get started with (IMO).

On Raspberry Pi OS, Node.js (10.x) is preinstalled, so I didn't have to install it manually—but if you're on stock Debian, you can get it with `sudo apt-get install -y nodejs npm`.

To get puppeteer, or more specifically, `puppeteer-core`, since I didn't need the training-wheels version that downloads another copy of Chromium too, I installed it with `npm`:

```
npm install puppeteer-core
```

Once it was installed, I created a `benchmark.js` script with the following contents:

```
const puppeteer = require('puppeteer-core');

(async () => {
  const browser = await puppeteer.launch({
    headless: false,
    executablePath: '/usr/bin/chromium'
  });
  const page = await browser.newPage();
  await page.goto('https://www.jeffgeerling.com/');
  await page.screenshot({path: 'example.png'});

  await browser.close();
})();
```

This should work on a Raspberry Pi, and it will launch a visible Chromium browser, load the page `https://www.jeffgeerling.com/` (I picked my site since it loads _very_ fast and doesn't rely on a ton of external resources), saves a screenshot, and then closes the browser.

To run it, with timing results:

```
time node benchmark.js
```

And in action:

{{< figure src="./puppeteer-chromium-benchmark.gif" alt="Puppeteer loading a site in Chromium and exiting" width="500" height="376" class="insert-image" >}}

I'll be compiling some benchmarks pitting different USB drives against each other on a Raspberry Pi 4, and I'll be posting a video on the topic to [my YouTube channel](https://www.youtube.com/c/JeffGeerling) soon, so subscribe there if you want to see my results!

(**Edit**: I benchmarked some drives on the Raspberry Pi and [here's the part that discusses browser benchmarks](https://youtu.be/oufXAysaywk?t=188).)
