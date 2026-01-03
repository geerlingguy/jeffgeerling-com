---
nid: 2915
title: "Running 'php artisan schedule:run' for Laravel in Kubernetes CronJobs"
slug: "running-php-artisan-schedulerun-laravel-kubernetes-cronjobs"
date: 2019-03-27T17:17:57+00:00
drupal:
  nid: 2915
  path: /blog/2019/running-php-artisan-schedulerun-laravel-kubernetes-cronjobs
  body_format: markdown
  redirects: []
tags:
  - cron
  - cronjob
  - infrastructure
  - kubernetes
  - laravel
  - php
  - threading
---

I am working on integrating a few Laravel PHP applications into a new Kubernetes architecture, and every now and then we hit a little snag. For example, the app developers noticed that when their cron job ran (`php artisan schedule:run`), the MySQL container in the cluster would drop an error message like:

```
2019-03-27T16:20:05.965157Z 1497 [Note] Aborted connection 1497 to db: 'database' user: 'myuser' host: '10.0.76.130' (Got an error reading communication packets)
```

In Kubernetes, I had the Laravel app CronJob set up like so:

```
---
apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: cron
  namespace: my-laravel-app
spec:
  schedule: "*/5 * * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - image: my_laravel_app_image:latest
            name: cron
            command: ["php", "artisan", "schedule:run"]
            imagePullPolicy: Always
            envFrom:
            - configMapRef:
                name: laravel-app-config
            - secretRef:
                name: laravel-app-secret
          restartPolicy: OnFailure
```

The container spec is identical to the Laravel app's `Deployment` so the container will run in an identical manner. And when I looked into the CronJob's logs, it always showed it ran correctly and exited cleanly:

```
Running scheduled command: Custom Command Here
Running scheduled command: Thread Clean
Running scheduled command: alert
```

So I started diving into MySQL, and I enabled the general query log temporarily (not recommended in production!): `SET global general_log = 1; SET global log_output = 'table';`

I was monitoring the log with `SELECT event_time, command_type, argument FROM mysql.general_log ORDER BY event_time DESC LIMIT 15;` to see the last few commands, and ran that query right after a cronjob ran. _Usually_ I would see Laravel do some stuff, then I'd see a `Close stmt` and `Quit`, which means the connection was cleaned up properly.

But in the case of the cron, after it ran, there were some queries... then nothing!

So I immediately started wondering if it might be related to the way Laravel was running the schedule. If it ran additional threads in the _background_ then this could cause the following sequence of events to happen:

  1. CronJob kicks off with command `php artisan schedule:run`
  1. Laravel starts some php sub-threads in the background, and prints to stdout that it's `Running scheduled command`s.
  1. Sub-threads start doing their work, running MySQL queries, etc.
  1. `php artisan schedule:run` exits cleanly (with status `0`)
  1. Docker kills the container since the main process exited

...but the sub-threads were still working and didn't finish.

It looks like the easiest way to fix this is to, in your Laravel app, remove `$schedule->runInBackground()` anywhere you're using that for scheduled commands. But if that _isn't_ an option, for whatever reason, the next best fix would be to either use an entrypoint script or hack together a command that does something like what user 'patant' did in this thread, [Run the scheduler in a docker image?](https://laracasts.com/discuss/channels/servers/run-the-scheduler-in-a-docker-image):

> Solved it by running `php artisan schedule:run >> /dev/null 2>&1 && while pgrep php > /dev/null; do sleep 1; done`

Anyways, un-backgrounding the scheduled jobs was an adequate fix in our case, so I didn't have to modify the CronJob to fix it. But we did have a 'fun' day spent figuring out why things would just kind of die off sometimes when cron was run as a Kubernetes `CronJob` vs being run inside a persistent container!
