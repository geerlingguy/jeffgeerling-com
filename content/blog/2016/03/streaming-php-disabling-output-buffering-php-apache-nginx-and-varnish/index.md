---
nid: 2640
title: "Streaming PHP - disabling output buffering in PHP, Apache, Nginx, and Varnish"
slug: "streaming-php-disabling-output-buffering-php-apache-nginx-and-varnish"
date: 2016-03-31T03:14:08+00:00
drupal:
  nid: 2640
  path: /blog/2016/streaming-php-disabling-output-buffering-php-apache-nginx-and-varnish
  body_format: markdown
  redirects: []
tags:
  - apache
  - bigpipe
  - drupal
  - drupal planet
  - lamp
  - lemp
  - nginx
  - output buffering
  - php
  - streaming
  - varnish
---

For the past few days, I've been diving deep into testing Drupal 8's experimental new [BigPipe](https://www.drupal.org/documentation/modules/big_pipe) feature, which allows Drupal page requests for authenticated users to be streamed and loaded in stages—cached elements (usually the majority of a page) are loaded almost immediately, meaning the end user can interact with the main elements on the page very quickly, then other uncacheable elements are loaded in as Drupal is able to render them.

Here's a very quick demo of an extreme case, where a particular bit of content takes five seconds to load; BigPipe hugely improves the usability and perceived performance of the page by streaming the majority of the page content from cache immediately, then streaming the harder-to-generate parts as they become available (click to replay):

<p style="text-align: center;">{{< figure src="./bigpipe-demo-one.gif" alt="BigPipe demonstration in an animated gif" width="640" height="360" >}}<br />
<em>Drupal BigPipe demo - click to play again.</em></p>

BigPipe takes advantage of streaming PHP responses (using <code>flush()</code> to flush the output buffer at various times during a page load), but to ensure the stream is delivered all the way from PHP through to the client, you need to make sure your entire webserver and proxying stack streams the request directly, with no buffering. Since I maintain [Drupal VM](http://www.drupalvm.com/) and support Apache and Nginx as webservers, as well as Varnish as a reverse caching proxy, I [experimented with many different configurations](https://github.com/geerlingguy/drupal-vm/issues/527) to find the optimal way to stream responses through any part of this open source stack.

And because my research dug up a bunch of half-correct, mostly-untested assumptions about output buffering with PHP requests, I figured I'd set things straight in one comprehensive blog post.

## Testing output buffering

I've seen a large number of example scripts used to test output_buffering on Stack Overflow and elsewhere, and many of them assume output buffering is disabled completely. Rather than doing that, I decided to make a little more robust script for my testing purposes, and also to document all the different bits for completeness:

```
<code>
<?php
// Set a valid header so browsers pick it up correctly.
header('Content-type: text/html; charset=utf-8');

// Emulate the header BigPipe sends so we can test through Varnish.
header('Surrogate-Control: BigPipe/1.0');

// Explicitly disable caching so Varnish and other upstreams won't cache.
header("Cache-Control: no-cache, must-revalidate");

// Setting this header instructs Nginx to disable fastcgi_buffering and disable
// gzip for this request.
header('X-Accel-Buffering: no');

$string_length = 32;
echo 'Begin test with an ' . $string_length . ' character string...<br />' . "\r\n";

// For 3 seconds, repeat the string.
for ($i = 0; $i < 3; $i++) {
  $string = str_repeat('.', $string_length);
  echo $string . '<br />' . "\r\n";
  echo $i . '<br />' . "\r\n";
  flush();
  sleep(1);
}

echo 'End test.<br />' . "\r\n";
?>
```

</code>

If you place this file into a web-accessible docroot, then load the script in your terminal using PHP's cli, you should see output like (click to replay):

<p style="text-align: center;">{{< figure src="./php-cli-streaming-noloop.gif" alt="PHP CLI streaming response test" width="540" height="271" class="insert-image" >}}<br />
<em>PHP response streaming via PHP's CLI - click to play again.</em></p>

And if you view it in the browser? By default, you won't see a streamed response. Instead, you'll see nothing until the entire page loads (click to replay):

<p style="text-align: center;">{{< figure src="./web-response-nostreaming-noloop.gif" alt="PHP webserver streaming response test not working" width="500" height="292" class="insert-image" >}}<br />
<em>PHP response not streaming via webserver in the browser - click to play again.</em></p>

That's good, though—we now have a baseline. We know that the script works on PHP's CLI, but either our webserver or PHP is not streaming the response all the way through to the client. If you change the `$string_length` to 4096, and are using a normal PHP/Apache/Nginx configuration, you should see the following (click to replay):

<p style="text-align: center;">{{< figure src="./web-response-streaming-noloop.gif" alt="PHP webserver streaming response test not working" width="500" height="292" class="insert-image" >}}<br />
<em>PHP response streaming via webserver in the browser - click to play again.</em></p>

The rest of this post will go through the steps necessary to ensure the response is streamed through your entire stack. 

## PHP and `output_buffering`

Some guides say you _have_ to set `output_buffering = Off` in your php.ini configuration in order to stream a PHP response. In some circumstances, this is useful, but typically, if you're calling <code>flush()</code> in your PHP code, PHP will flush the output buffer immediately after the buffer is filled (the default value is `4096`, which means PHP will flush it's buffer in 4096 byte chunks).

For many applications, 4096 bytes of buffering offers a good tradeoff for better transport performance vs. more lively responses, but you can lower the value if you need to send back much smaller responses (e.g. tiny JSON responses like `{setting:1}`).

One setting you definitely _do_ need to disable, however, is `zlib.output_compression`. Set it to `zlib.output_compression = Off` in php.ini and restart PHP-FPM to make sure gzip compression is disabled.

There are edge cases where the above doesn't hold absolutely true... but in most real-world scenarios, you won't need to disable PHP's `output_buffering` to enable streaming responses.

## Nginx configuration

I recommend using Nginx with PHP-FPM for the most flexible and performant configuration, but still run both Apache and Nginx in production for various reasons. Nginx has a small advantage over Apache for PHP usage in that it doesn't have the cruft of the old `mod_php` approach where PHP was primarily integrated with the webserver, meaning the proxied request approach (using FastCGI) has always been the default, and is well optimized.

All you have to do to make streaming responses work with Nginx is set the header `X-Accel-Buffering: no` in your response. Once Nginx recognizes that header, it automatically disables `gzip` and `fastcgi_buffering` _for only that response_.

```
header('X-Accel-Buffering: no');
```

You can also manually disable gzip (`gzip off`) and buffering (`fastcgi_buffering off`) for an entire `server` directive, but that's overkill and would harm performance in any case where you _don't_ need to stream the response.

## Apache configuration

Because there are many different ways of integrating PHP with Apache, it's best to discuss how streaming works with each technique:

### `mod_php`

Apache's `mod_php` seems to be able to handle streaming without disabling deflate/gzip for requests out of the box. No configuration changes required.

### `mod_fastcgi`

When configuring `mod_fastcgi`, you must add the `-flush` option to your `FastCgiExternalServer` directive, otherwise if you have `mod_deflate`/gzip enabled, Apache will buffer the entire response and delay until the end to deliver it to the client:

```
# If using PHP-FPM on TCP port 9000.
FastCgiExternalServer /usr/lib/cgi-bin/php5-fcgi -flush -host 127.0.0.1:9000 -pass-header Authorization
```

### `mod_fcgi`

I've never configured Apache and PHP-FPM using `mod_fcgi`, and it seems cumbersome to do so; however, according to the [Drupal BigPipe environment docs](https://www.drupal.org/documentation/modules/big_pipe/environment), you can get output buffering disabled for PHP responses by setting:

```
FcgidOutputBufferSize 0
```

### `mod_proxy_fcgi`

If you use `mod_proxy_fcgi` with PHP-FPM, then you have to disable gzip in order to have responses streamed:

```
SetEnv no-gzip 1
```

In all the above cases, PHP's own output buffering will take effect up to the default `output_buffering` setting of 4096 bytes. You can always change this value to something lower if absolutely necessary, but in real-world applications (like Drupal's use of BigPipe), many response payloads will have flushed output chunks greater than 4096 bytes, so you might not need to change the setting.

## Varnish configuration

Varnish buffers output by default, and you have to explicitly disable this behavior for streamed responses by setting `do_stream` on the backend response inside `vcl_backend_response`. Drupal, following Facebook's lead, uses the header `Surrogate-Control: BigPipe/1.0` to flag a response as needing to b streamed. You need to use Varnish 3.0 or later (see the [Varnish blog post announcing streaming support in 3.0](http://info.varnish-software.com/blog/streaming-varnish-30)), and make the following changes:

Inside your Varnish VCL:

```
sub vcl_backend_response {
    ...
    if (beresp.http.Surrogate-Control ~ "BigPipe/1.0") {
        set beresp.do_stream = true;
        set beresp.ttl = 0s;
    }
}
```

Then make sure you output the header anywhere you need to stream a response:

```
header('Surrogate-Control: BigPipe/1.0');
```

## Debugging output streaming

During the course of my testing, I ran into some strange and nasty networking issue with a VMware vagrant box, which was causing HTTP responses delivered through the VM's virtual network to be buffered no matter what, while responses inside the VM itself worked fine. After trying to debug it for an hour or two, I gave up, rebuilt the VM in VirtualBox instead of VMware, couldn't reproduce the issue, then rebuilt again in VMware, couldn't reproduce again... so I just put that there as a warning—your entire stack (including any OS, network and virtualization layers) has to be functioning properly for streaming to work!

To debug PHP itself, and make sure _PHP_ is delivering the stream even when your upstream webserver or proxy is not, you can analyze packet traffic routed through PHP-FPM on port 9000 (it's a lot harder to debug via UNIX sockets, which is one of many reasons I prefer defaulting to TCP for PHP-FPM). I used the following command to sniff port 9000 on localhost while making requests through Apache, Nginx, and Varnish:

```
tcpdump -nn -i any -A -s 0 port 9000
```

You can press `Ctrl-C` to exit once you're finished sniffing packets.
