---
nid: 2972
title: "Quick and dirty way to strip ANSI terminal output in PHP"
slug: "quick-and-dirty-way-strip-ansi-terminal-output-php"
date: 2020-02-27T21:00:57+00:00
drupal:
  nid: 2972
  path: /blog/2020/quick-and-dirty-way-strip-ansi-terminal-output-php
  body_format: markdown
  redirects: []
tags:
  - ansi
  - color
  - exec
  - php
  - regex
  - tutorial
---

From time to time, I write up little PHP scripts to run a command via `exec()` and dump the output to the screen. Most of the time these are quick throwaway scripts, but sometimes I need them to persist a little longer, or share the output with others, so I make them look a _little_ nicer.

One annoying thing that happens if you interact with CLI tools that generate colorized output is that PHP doesn't translate the terminal (ANSI) color codes into HTML colors, so you end up looking at output like:

```
[0;32mKubernetes master[0m is running at [0;33mhttps://10.96.0.1:443[0m
```

Sensio Labs maintains an excellent [ansi-to-html](https://github.com/sensiolabs/ansi-to-html) PHP library, and if you're building anything that should be persistent or robust, you should use it. But I wanted a one-line solution for one simple script I was working on, so I spent a couple minutes building out the following regex:

```
exec("kubectl cluster-info 2>&1", $output, $return);
$output = preg_replace('/\e[[][A-Za-z0-9];?[0-9]*m?/', '', $output);
echo '<pre class="border">';
foreach ($output as $line) {
  echo $line . "\r\n";
}
echo '</pre>';
```

Now the output from the PHP script is more or less what you'd see in the terminal (minus any colorization, of course):

```
Kubernetes master is running at https://10.96.0.1:443
```

Test and see how this regular expression works on regular expressions 101: [https://regex101.com/r/feuyoS/2](https://regex101.com/r/feuyoS/2).
