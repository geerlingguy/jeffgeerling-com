---
nid: 2379
title: "Facebook OAuthException when posting to Wall for a Page"
slug: "facebook-oauthexception-when"
date: 2012-09-17T22:06:39+00:00
drupal:
  nid: 2379
  path: /blogs/jeff-geerling/facebook-oauthexception-when
  body_format: markdown
  redirects: []
tags:
  - api
  - facebook
  - open graph
aliases:
  - /blogs/jeff-geerling/facebook-oauthexception-when
---

I integrate Facebook posting with a few different websites and services, so I've gotten to know Facebook's Open Graph and API pretty well over the past few years. A lot of sites I work with automatically post new stories straight to a Facebook Page's wall, and have a format with a message and an attached link. All of these parameters are well documented in Facebook's API under <a href="https://developers.facebook.com/docs/reference/api/post/">Post</a>.

However, lately I've been getting the following error message whenever a site uses the first method below to send a post with a link attached:

```
{
  "message" : "An unknown error has occurred.",
  "type" : "OAuthException",
  "code" : 1
}
```

I tried using the <a href="https://developers.facebook.com/tools/explorer">Open Graph Explorer</a>, the official Facebook SDK for PHP, and other methods to see if there was any other way to get around that exception, but nothing I did turned out any different response.

Here's how I sent a typical request with just a link (just using plain-vanilla PHP with cURL):

```
<code>
<?php
  // Set up params to be posted to Facebook.
  $params = array(
    'title' => $title,
    'link' => $url,
    'description' => $link_description,
    'caption' => $link_caption,
    'access_token' => FACEBOOK_APP_ID . '|' . FACEBOOK_APP_SECRET,
  );
  // Post the message to Facebook.
  $url = 'https://graph.facebook.com/' . FACEBOOK_PAGE_ID . '/feed';
  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_POST, count($params));
  curl_setopt($ch, CURLOPT_POSTFIELDS, $params);
  curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
  $result = curl_exec($ch);
  curl_close($ch);
?>
```

</code>

Now, to get the message to post without throwing the strange OAuthException, I have to send everything in the 'message' of the post (with no link attached). You can pass along other params, but if you pass anything in the 'link' param, you'll get the error at the top of this post.

```
<code>
<?php
  // Set up params to be posted to Facebook.
  $params = array(
    'message' => $title . ' — ' . substr($description, 0, 350) . '...' . "\r\n\r\n" . 'Source: ' . $url,
    'access_token' => FACEBOOK_APP_ID . '|' . FACEBOOK_APP_SECRET,
  );
?>
```

</code>

There's <a href="https://developers.facebook.com/bugs/409281805774218">an open bug for this on Facebook's Developers site</a>, but it's been triaged as 'low priority', so I don't know if it'll ever be fixed. I just wanted to post this so any other frustrated developers don't have to spend a few hours scratching their heads over the same issue.
