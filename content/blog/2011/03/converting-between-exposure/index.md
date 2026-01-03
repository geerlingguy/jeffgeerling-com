---
nid: 2313
title: "Converting between Exposure Value and LUX"
slug: "converting-between-exposure"
date: 2011-03-19T11:45:05+00:00
drupal:
  nid: 2313
  path: /blogs/jeff-geerling/converting-between-exposure
  body_format: filtered_html
  redirects: []
tags:
  - ev
  - exposure value
  - light
  - light meter
  - lux
  - measurement
  - photography
---

For a recent project, I had to make some rough LUX measurements (LUX is a more international standard for light measurement than candlepower, which is traditionally used in the U.S.) of an environment to help determine what kind of video cameras to use. Problem was, all I had was a spot meter—an incident light meter for film/digital photography, that would give me a reading of, say "1/15 second exposure at f/5.6 and ISO 100."

After looking around online a while, I found a simple method to get a rough estimate of the LUX measurement from these photography measurements.

First, though, it's important to know the distinction between 'incident' light (a measurement of light hitting a certain surface or area) and 'reflected' light (the light you can measure from bouncing off the surface). It's better, for determining EV (Exposure Value) or LUX values, to measure the incident light... and you can only do this accurately with a spot/light meter. (You can estimate the reflected light by taking a picture with your camera, and glancing at the exposure at given settings. If the exposure is decent, look at the meter settings you used—ISO, aperture, and shutter speed).

Once you have a reading, you can do two conversions to reach the approximate LUX value. First, you need to convert to an EV (Exposure Value), then to LUX.

For the first conversion, use your aperture and shutter speed readings, at ISO 100, and get the resulting EV. Use the table under the "EV as an indicator of camera settings" heading in <a href="http://en.wikipedia.org/wiki/Exposure_value">this Wikipedia article</a>.

For the second conversion, use <a href="http://www.intl-lighttech.com/support/calculator/evluxconvert">this simple EV to LUX converter</a>, and input the value you determined in the first conversion. (Alternatively, <a href="http://www.fredparker.com/ultexp1.htm#evfclux">here's a simple chart of the conversions</a>).
