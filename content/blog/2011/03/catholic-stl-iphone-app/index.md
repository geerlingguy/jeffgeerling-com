---
nid: 2314
title: "Catholic STL - iPhone App for Archdiocese of St. Louis"
slug: "catholic-stl-iphone-app"
date: 2011-03-04T18:30:28+00:00
drupal:
  nid: 2314
  path: /blogs/jeff-geerling/catholic-stl-iphone-app
  body_format: full_html
  redirects: []
tags:
  - apps
  - iphone
  - mobile
---

{{< figure src="./Icon-114.png" alt="Archdiocese of St. Louis - Mobile App Icon" width="114" height="114" >}}Midwestern Mac, LLC worked with the Archdiocese of St. Louis to build a location-aware, news aggregating, and content submission app for the iPhone and iPod Touch. The app, <a href="http://archstl.org/mobile-app">Catholic STL</a>, has three main features, and leverages many different iOS APIs.

The Parishes view (and subviews) shows all parishes (about 200) in the Archdiocese on a map (MKMapView), as annotations, and when a user taps on an annotation's details, he is shown the parish's address, various parish event times, and more links for the parish website and location. The Parishes view also has two different types of search: the user can enter an arbitrary address, and the map will show parishes around that address, or the user can search for a parish by name or by city.

Parish data is managed through Core Data, and was originally imported using a standard SQLite database, using a template provided by our app's core data model (the Base app for the Mac was very helpful in this regard!). We're working on more advance OTA syncing of this data for a point-release.

The News view (and subview) shows the latest 'Around the Archdiocese' news from the Archdiocesan website. This is a pretty basic view, and it uses NSXMLParser to parse an up-to-date (but cached) XML file generated from Views on archstl.org. We use a custom XML feed instead of an RSS-compliant feed, simply to keep things simpler in the parser on the iPhone.

The Prayers view shows prayers from the Archdiocesan website's prayer section, and also has a WebView that shows the website's 'Request a Prayer' form, optimized for the iPhone.

We may post more details about this App's development in the future, as well as a few other apps; mobile is the current forefront of web development, and being able to integrate web content with native app content is going to be a very important trait of larger websites and organizations. This app is on the right track towards that goal!
