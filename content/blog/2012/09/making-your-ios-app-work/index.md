---
nid: 2380
title: "Adapting Your iOS App to work with iPhone 5/iOS 6"
slug: "making-your-ios-app-work"
date: 2012-09-18T16:49:04+00:00
drupal:
  nid: 2380
  path: /blogs/jeff-geerling/making-your-ios-app-work
  body_format: full_html
  redirects: []
tags:
  - cocoa touch
  - ios
  - ios6
  - iphone 5
  - ipod touch
  - objective-c
  - xcode
aliases:
  - /blogs/jeff-geerling/making-your-ios-app-work
---

{{< figure src="./iphone-5-specs-size.jpg" alt="iPhone 5 Specs and Dimensions" width="289" height="262" >}}For the non-Retina to Retina changes, most developers simply needed to add a bunch of <code>@2x</code> graphics, and maybe change a few little things here and there. Most parts of an app Just Worked™ on the higher resolution display, as long as the app used native controls and views, and didn't have a ton of custom interface elements.

However, with the iPhone 5, there are some other things that are changing a bit more radically—there's a bit of extra height (or width, in landscape), and iOS 6 is introducing a new way of handling device rotation and display changes.

Since most of the apps I manage are relatively simple, and only contain a few UIScrollViews, UITableViews, and UIViews, I only have to perform a few quick changes to my apps to get them ready for iOS 6 and the iPhone 5:

<ol>
<li>To make your app stretch to fit the iPhone 5/iPod Touch's taller display, just add in a <code>Default-568h@2x.png</code> image (along with your existing iPhone <code>Default</code> and <code>Default@2x</code> graphics), and make sure it's 640px x 1136px.</li>
<li>To handle autorotation, you now need to implement <code>supportedInterfaceOrientations</code> and <code>shouldAutorotateToInterfaceOrientation:interfaceOrientation</code>, and return the supported orientations*. See Apple's iOS 6 Release Notes (developer account required) for more info. (Note that if you're using the base UITableViewController or UITabBarController classes, you will need to subclass them with your own (I use something like <code>JJGTableViewController</code>) and implement these new rotation methods, then use your subclass in any code or XIB files instead of the base classes.)</li>
<li>TableViews, MapViews, WebViews, etc. should implement <code>shouldAutorotate</code>. Again, see Apple's iOS 6 Release Notes for more info.</li>
<li>When you submit your app update for review, you might get an error about 'Missing screenshots' and 'Languages - En English'—this just means you forgot to upload screenshots for the iPhone 5/Tall iPod Touch. You need to generate new screenshots at the new resolutions to get your app to switch to 'Waiting for Review'.</li>
</ol>

*Note that you can still leave in other deprecated rotation methods in your subviews for backwards (iOS 4, iOS 5) compatibility. In fact, if you make no changes to your code, the interface will rotate just the same in iOS 4/5, but it will remain firmly fixed in portrait orientation until you implement the new iOS 6 rotation methods.

For someone with a game, or with more complicated and customized views, you might need to do a bit more work detecting the screen size and rendering things appropriately, but for apps with more basic views, the above steps should get your app ready for the new iPhone 5 and iPod Touch in no time!
