---
nid: 2456
title: "Debugging Varnish VCL configuration files"
slug: "debugging-varnish-vcl"
date: 2014-01-22T17:45:07+00:00
drupal:
  nid: 2456
  path: /blogs/jeff-geerling/debugging-varnish-vcl
  body_format: full_html
  redirects: []
tags:
  - debugging
  - drupal
  - drupal planet
  - varnish
  - varnishlog
  - varnishtop
  - vcl
aliases:
  - /blogs/jeff-geerling/debugging-varnish-vcl
---

<p>If you're a Drupal or PHP developer used to debugging or troubleshooting some code by adding a <code>print $variable;</code> or <code>dpm($object);</code> to your PHP, and then refreshing the page to see the debug message (or using XDebug, or using watchdog logging...), debugging Varnish's VCL language can be intimidating.</p>

<p>VCL uses C-like syntax, and is compiled when varnish starts, so you can't just modify a .vcl file and refresh to see changes or debug something. And there are only a few places where you can simply stick a debug statement. So, I'll explain four different ways I use to debug VCLs in this post (note: don't do this on a production server!):</p>

<h2>Simple Error statements (like <code>print</code> in PHP)</h2>

<p>Sometimes, all you need to do is see the output of a variable, like <code>req.http.Cookie</code>, inside <code>vcl_recv()</code>. In these cases, you can just add an <code>error</code> statement to throw an error in Varnish and output the contents of a string, like the Cookie:</p>


```
error 503 req.http.Cookie;
```

<p>Save the VCL and restart Varnish, and when you try accessing a page, you'll get Varnish's error page, and below the error message, the contents of the cookie, like so:</p>

<p style="text-align: center;">{{< figure src="./varnish-error-debug-message.png" alt="Varnish error debug message" width="500" height="233" >}}</p>

<p>This debugging process works within <code>vcl_recv()</code> and <code>vcl_fetch()</code>, but causes problems (or crashes Varnish) in any other functions.</p>

<h2>Debugging with syslog</h2>

You can also log debug messages to the system log (<code>/var/log/messages</code> on RedHat/CentOS, or <code>/var/log/syslog</code> on Debian/Ubuntu) using the <a href="https://www.varnish-cache.org/docs/3.0/reference/vmod_std.html"><code>syslog()</code></a> function provided by <code>vmod_std</code>.

In your VCL (at the top), add in <code>import std;</code> to import the std library. Then, anywhere in the vcl, you can log messages to the system log using something like:


```
std.syslog(0, req.http.Cookie);
```

Restart varnish, and then <code>tail -f /var/log/messages</code> to watch a steady stream of varnish log messages!

<h2>Actively monitoring Varnish with <code>varnishlog</code></h2>

<p><code>varnishlog</code> is another simple command-line utility that dumps out every bit of information varnish processes and returns during the course of it's processing, including backend pings, request headers, response headers, cache information, hash information, etc.</p>

<p>If you just enter <code>varnishlog</code> and watch (or dump the info into a file), be prepared to scroll for eons or grep like crazy to find the information you're looking for. Luckily, <code>varnishlog</code> also lets you filter the information it prints to screen with a few options, like <code>-m</code> to define a regular expression filter. For example:</p>


```
# Display all Hashes.
varnishlog -c -i Hash

# Display User-Agent strings.
varnishlog -c -i RxHeader -I User-Agent
```

<p>There are <a href="https://www.varnish-cache.org/trac/wiki/VarnishlogExamples">more examples</a> available on the Varnish cache Wiki.</p>

<h2>Monitoring Varnish with <code>varnishtop</code>
</h2>

<p><code>varnishtop</code> is a simple command-line utility that displays varnish log entries with a rolling count (ranking logged entries by frequency within the past minute). What this means in laymans terms is that you can easily display things like how many times a particular URL is hit, different bits of information about requests (like Hashes, or headers, etc.).</p>

<p>I like to think of varnishtop as a simple way to display the incredibly deep stats from varnishlog in realtime, with better filtering.</p>

<p>Some example commands I've used when debugging scripts:</p>


```
# Display request cookies.
varnishtop -i RxHeader -I Cookie

# Display varnish hash data ('searchtext' is text to filter within hash).
varnishtop -i "Hash" -I searchtext

# Display 404s.
varnishlog -b -m "RxStatus:404"
```

<p>You can change the length of time being monitored from the default of 60 seconds by specifying <code>-p period</code> (note that this setting only works for Varnish &gt; 3.0).</p>

<p>There are a few other common monitoring commands in <a href="http://stackoverflow.com/a/15549577">this StackOverflow answer</a>.</p>

<h2>Dry-run Compiling a VCL</h2>

<p>Sometimes you may simply have a syntax error in your .vcl file. In these cases, you can see exactly what's wrong by using the command <code>varnishd -Cf /path/to/default.vcl</code>, where <code>default.vcl</code> is the base VCL file you've configured for use with Varnish (on CentOS/RHEL systems, this file is usually <code>/etc/varnish/default.vcl</code>).</p>

<p>The output of this command will either be a successfully-compiled VCL, or an error message telling you on exactly what line the error occurs.</p>

<h2>Other debugging techniques</h2>

<p>Are there any other simple debugging techniques you use that I didn't cover here? Please let me know in the comments. I wanted to compile these techniques, and a few examples, because I've never really seen a good/concise primer on debugging Varnish configuration anywhere—just bits and pieces.</p>
