---
nid: 2315
title: "Declustering Markers in Google Maps with Drupal?"
slug: "declustering-markers-google"
date: 2011-04-15T15:47:42+00:00
drupal:
  nid: 2315
  path: /blogs/jeff-geerling/declustering-markers-google
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal planet
  - geolocation
  - gmap
  - location
  - mapping
  - maps
---

{{< figure src="./location-marker.png" alt="Location Marker" width="112" height="168" >}}I recently received a question from a friend who's setting up a new site in Drupal 7, and is using the <a href="http://drupal.org/project/gmap">GMap Module</a>, <a href="http://drupal.org/project/location">Location</a>, and <a href="http://drupal.org/project/views">Views</a>, to set up a map of upcoming events for his website.

My response (posted below) basically gives some pointers for what other people (often creating custom implementations of Google Maps on their sites) are doing to avoid the problem of 'decluttering' or 'declustering' multiple points at the same location (same coordinates). My question is: how do you handle declustering on your Drupal site? Are there any perferred techniques? Luckily for me, this is a problem I have yet to encounter, as I've only had to map locations of stores, <a href="http://archstl.org/parishes">parishes</a>, etc., that are already spread out evenly over some area of a map :-)

My response to his question follows:

With regard to your question about making a map more usable when there are multiple markers on one specific geolocation (same latitude and longitude):

I know that there's one thing that the <a href="http://drupal.org/project/mapstraction">Mapstraction</a> module does, called 'declutter points', that might be able to help. I've also found some good hints when looking up clustering and Google Maps on Google search.

But, this is definitely not an easy problem to solve. On the iPhone, if there are two markers with the same lat/lon values, I can tap on the same marker multiple times, and each time it will cycle through to the next marker underneath... also, the more markers I place in the same location, the darker the shadow beneath the marker. This is not entirely intiutive, but at least it doesn't completely hide secondary markers that are on top of each other.

However, there's also a few other issues I found online that might be helpful for you:

<ul>
	<li>http://code.google.com/p/gmaps-api-issues/issues/detail?id=119</li>
	<li>http://www.svennerberg.com/2009/01/handling-large-amounts-of-markers-in-google-maps/</li>
</ul>

If you can't find what you're looking for in one of the Drupal modules you're using, I would highly suggest posting an issue to the issue queue requesting options for declustering/decluttering.
