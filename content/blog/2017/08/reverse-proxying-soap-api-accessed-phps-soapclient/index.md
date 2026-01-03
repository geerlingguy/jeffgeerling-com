---
nid: 2805
title: "Reverse-proxying a SOAP API accessed via PHP's SoapClient"
slug: "reverse-proxying-soap-api-accessed-phps-soapclient"
date: 2017-08-29T17:03:04+00:00
drupal:
  nid: 2805
  path: /blog/2017/reverse-proxying-soap-api-accessed-phps-soapclient
  body_format: markdown
  redirects: []
tags:
  - api
  - debugging
  - nginx
  - php
  - proxy
  - soap
  - tutorial
---

I'm documenting this here, just because it's something I imagine I might have to do again someday... and when I do, I want to save myself hours of pain and misdirection.

A client had an old SOAP web service that used IP address whitelisting to authenticate/allow requests. The new PHP infrastructure was built using Docker containers and auto-scaling AWS instances. Because of this, we had a problem: a request could come from one of millions of different IP addresses, since the auto-scaling instances use a pool of millions of AWS IP addresses in a wide array of IP ranges.

Because the client couldn't change their API provider (at least not in any reasonable time-frame), and we didn't want to throw away the ability to auto-scale, and also didn't want to try to build some sort of 'Elastic IP reservation system' so we could draw from a pool of known/reserved IP addresses, we had to find a way to get all our backend API SOAP requests to come from one IP address.

The solution? **Reverse-proxy all requests to the backend SOAP API**.

Now, before I get started, know that this should be a last resort option—it's painful to get working, it's painful to debug, and it's painful to maintain. That said, if you find yourself in the same situation, here's how to reverse-proxy a SOAP API!

## Using Nginx as a reverse proxy

Nginx is often used when proxying things, because it's simple to set up and offers enough configuration to work for most use cases.

The main thing you need to do is set up a `server` to proxy the requests, then restart Nginx. In the example below, I am setting up a proxy on port 80 (api-proxy.example.com), and it will rewrite all requests to the backend api.upstream.com. In the application configuration, wherever you originally requested api.upstream.com, you'd need to switch it to request api-proxy.example.com.

```
server {
    listen 80;
    server_name api-proxy.example.com;

    proxy_connect_timeout 60s;
    proxy_send_timeout 120s;
    proxy_read_timeout 120s;

    location / {
        set $backend "http://api.upstream.com";
        proxy_pass $backend;
    
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
    }
}
```

Note that if you need to proxy HTTPS requests (over port 443), you'd need to change the `listen` directive to `listen 443 ssl`, and also add a valid `ssl_certificate` and `ssl_certificate_key`. Finally, you also should set the appropriate headers in the forwarded request:

```
        proxy_set_header X-Forwarded-Proto https;
        proxy_set_header X-Forwarded-Port 443;
```

Now, this is all wonderful... and if doing that, restarting Nginx, and re-pointing your API requests in your backend application works right away, you're done! But in my case, I kept running into different error messages from PHP's SoapClient at different points, like:

```
Could not connect to host
#0 [internal function]: SoapClient->__doRequest("/index.php/api/path/here/")
```

Or:

```
SOAP-ERROR: Parsing WSDL: Couldn't load from 'http://api-proxy.example.com/SOAP.asmx?wsdl' : failed to load external entity "http://api-proxy.example.com/SOAP.asmx?wsdl"
```

So I needed to go a level deeper and see what was actually being requested, when.

## Debugging Nginx requests

Nginx (like Apache) has a lot of nice logging capabilities, and they're relatively easy to configure. First, I wanted to add logging in a separate log file so I could tail the log file for proxy requests. So I added the following configurations, then restarted Nginx:

```
# Inside Nginx http {} config.
log_format apilog '$remote_addr - $remote_user [$time_local] '
    '"$request" $status $body_bytes_sent '
    '"$http_referer" "$http_user_agent" $request_time req_body:"$request_body"';

# Inside our proxy api server {} config.
access_log /var/log/nginx/api-proxy.log apilog buffer=4k flush=1s;
```

I could technically drop the access_log buffering entirely, but I habitually leave some buffering in on any production infrastructure on AWS, just to prevent any possibility of disk IO slowing the system down. This will write a log entry to the `api-proxy.log` file at least once every second (assuming there's been a request), and the entry looks like:

```
1.2.3.4 - - [29/Aug/2017:15:10:05 +0000] "HEAD /SOAP.asmx?wsdl HTTP/1.1" 200 0 "-" "curl/7.54.0" 0.372 req_body:"-"
```

That's helpful to at least see what kind of traffic is coming through, but I was really interested in reading the _response body_, because I had a sneaking suspicion something may be going awry when PHP's SoapClient gets the WSDL, caches the response, then likely switches to using the URL defined in the `wsdl:service`'s `soap:address location` instead of continuing to use the original request URL.

So I did two things next:

  1. Disabled PHP's soap module wsdl cache (add `soap.wsdl_cache_enabled = 0` to php.ini), so that it would always get new data from the endpoint (I found that PHP would sometimes switch to another host and not try my proxy host if the wsdl defined a different URL).
  2. Started monitoring the raw response body.

## Monitoring HTTP response bodies

To monitor the response body, I first looked into logging it using the `body_filter_by_lua` option provided by the [`lua-nginx-module`](https://github.com/openresty/lua-nginx-module#body_filter_by_lua), but I didn't want to have to rebuild the Nginx version on the production server where I was debugging this issue (don't ask my why I couldn't do all this work on a non-prod server ?).

So I used the ever-useful `ngrep` to monitor TCP requests on port 80: `ngrep tcp and port 8080`.

This printed to my console all data flowing through the port, and let me identify where my final issue was—in my case, the `soap:address location` was using the correct URL, but the `wsdl:port` must've been hardcoded in the backend, because it would not change no matter what port I ran my proxy on. So once I fixed the proxy to use port 80, requests started working (I was originally using a high port like `8080`, which is why I had to get into this detailed response debugging).

One other thing I considered briefly was using Nginx's [`ngx_http_sub_module`](http://nginx.org/en/docs/http/ngx_http_sub_module.html) to rewrite the response body, replacing the bit that needed to change for requests to work (using a `sub_filter` directive). But I know from past experience, _there be dragons_, so I avoided it and in the end didn't need it anyways.

## Summary

If you can avoid it, don't proxy 3rd party APIs. It's a hassle, and it's difficult to debug. If you have to do it, be prepared for an afternoon of debugging to see what's going on with the request routing and response delivery!
