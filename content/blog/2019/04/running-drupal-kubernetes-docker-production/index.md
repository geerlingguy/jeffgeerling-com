---
nid: 2917
title: "Running Drupal in Kubernetes with Docker in production"
slug: "running-drupal-kubernetes-docker-production"
date: 2019-04-12T23:00:49+00:00
drupal:
  nid: 2917
  path: /blog/2019/running-drupal-kubernetes-docker-production
  body_format: markdown
  redirects: []
tags:
  - docker
  - dramble
  - drupal
  - drupal 8
  - drupal planet
  - kubernetes
  - pi dramble
  - production
---

> **Update**: Since posting this, there have been some interesting new developments in this area, for example:
> 
> - There is now a [Drupal/Kubernetes SIG](https://github.com/drud/sig-drupal) which meets every other Wednesday.
> - There are Kubernetes Drupal Operators which can manage Drupal instances in Kubernetes; I maintain the [geerlingguy/drupal-operator](https://github.com/geerlingguy/drupal-operator) but there are a couple others out there in development.

Since 2014, I've been working on various projects which containerized Drupal in a production environment. There have always been a few growing pains—there will for some time, as there are so few places actually _using Docker or containers in a production environment_ (at least in a 'cloud native' way, without tons of volume mounts), though this is changing. It was slow at first, but it's becoming much more rapid.

You might think that Drupal and Docker work together nicely. They definitely can and do, in many cases, as we see with local development environments built around Docker, like [Docksal](https://docksal.io/), [Ddev](https://www.drud.com/what-is-ddev/), [Lando](https://docs.devwithlando.io), and even [Drupal VM](https://www.drupalvm.com). But local development environments, where the Drupal codebase is basically mounted as a volume into a Docker container that runs the code, differ radically from production, where the goal is to 'contain' as much of production into a stateless container image as possible, so you can scale up, deploy, and debug most efficiently.

If you have to have your Drupal code in one place, and a docker container running elsewhere, you have to manage both separately, and rolling out updates can be challenging (and requires most of the same tools you'd use in old-style Drupal-on-a-normal-server approaches, so there's no streamlining this way).

Throw Kubernetes into the mix—where anything and everything is almost _forced_ to operate as a [12-factor app](https://12factor.net), and you really have to be on your game in the world of containerized-Drupal-in-production!

## 12 Factor Apps

You may wonder, "What is a _12 Factor App_?" The link to the website above has all the details, but on a very basic level, a **12-factor app** is an application which is easy to deploy into scalable, robust, cloud-based environments.

Many applications need things like environment-specific database credentials, a shared filesystem for things like uploaded or generated files shared between multiple instances, and other things which may make deploying in a scalable, flexible way more difficult.

But a _12 Factor App_ is an application which can do some fancy things which make it easier to deploy and manage:

  - It stores all its configuration in some sort of declarative format, so there aren't manual or non-automatable setup steps.
  - It is not tied too tightly to one type of operating system or a complex tangle of language and environment configurations.
  - It can scale from one to many instances with minimal (ideally zero) intervention.
  - It is identical in almost every way between production and non-production environments.

A 12 Factor  App _can_ require database credentials, shared filesystems, etc.—but ideally it can work in ways that minimizes the pain when dealing with such things.

## Challenges with Drupal

There are five major challenges to turning a Drupal application or website into a more 'stateless' 12-factor app:

  1. The database must be persistent.
  1. The Drupal files directory must be persistent and shared among all web containers.
  1. Drupal installation and features like CSS and JS aggregation needs to be able to persist data into certain directories inside the Drupal codebase.
  1. Drupal's settings.php and other important configuration is challenging to configure via environment variables.
  1. Drupal's cron job(s) should be run via Drush if you would like to be able to run it in the most efficient, scalable fashion.

With each one of these challenges, you can choose whether to use an _easy-to-implement_ but _hard-to-scale_ solution, or a _hard-to-implement_ but _easy-to-scale_ solution. And in the case of Drupal installation, you can even avoid the problem altogether if you're only ever going to run one Drupal site, and never reinstall it—you could install outside of production, then move some things around, and copy the database into production. (Though you can solve the 'how do I install Drupal in a mostly-stateless environment' problem too; it's just not easy-to-implement).

## Meeting the Challenges with Kubernetes and Drupal

I'll walk you through some solutions to these problems, drawing from my experience building the [Raspberry Pi Dramble](http://www.pidramble.com/) (a 4-node Kubernetes cluster running Drupal), the Drupal website that runs on it ([Drupal for Kubernetes](https://github.com/geerlingguy/drupal-for-kubernetes)) and also running a fairly large Drupal web application for an internal project I work on at Acquia inside an Amazon EKS Kubernetes cluster.

### Solving Database Persistence

There are a number of ways you can solve the problem of database persistence when running in Kubernetes—and this is not just a challenge with Drupal, but with any database-backed web service. One answer the cloud providers have, and which is often the easiest option, is to use a 'managed database', for example, RDS or Aurora in AWS, or Cloud SQL in Google Cloud. You can connect your Drupal sites directly to the managed database backend.

The downside to a managed service approach is that it is often more expensive than a self-managed solution. Also, it requires the opening of a communications channel from inside your Kubernetes cluster to an outside service (which increases your security attack surface).

The upside to a managed service is that managed databases can be a _lot_ faster, better optimized, and more robust than a self-managed solution. Consider Aurora, which I have personally witnessed handling thousands of writes per second, over 400,000 iops, on a large Magento site I manage. It is set up to be geographically redundant, snapshotted nightly (and even more frequently if desired), can scale up or down very easily, and is automatically patched and upgraded.

Where cost is a major concern, or cloud portability, you can still run databases inside a Kubernetes cluster. I do this quite a bit, and the default [mysql](https://hub.docker.com/_/mysql) Docker library image actually runs smaller sites and apps quite well, sometimes with a few small tweaks. But if you want to be able to have highly-available, writer/reader replicated databases inside Kubernetes, be prepared to do a lot more work. There are initiatives like the [MySQL Operator](https://github.com/oracle/mysql-operator) which aim to make this process simpler, but they are still not as stable as I would like for production usage.

When you run a database like MySQL or PostgreSQL in Kubernetes, you will need to persist the actual data somewhere, and the most common way is to attach a Kubernetes PV (PersistentVolume) to the MySQL container, usually backed by something like AWS EBS volumes (io1 storage type for better speed), or Google Cloud Persistent Disks. You can—but probably should not—run a MySQL database backed by an NFS PV... like I do on the Raspberry Pi Dramble cluster. But you want the database filesystem to be fast, easy to attach and detach to the MySQL Pod, and robust (make sure you enable backups / snapshots with something like [Heptio Velero](https://github.com/heptio/velero)!).

Looking towards the future, some database systems are actually 12 Factor Apps themselves; for example, [CockroachDB](https://www.cockroachlabs.com/campaigns/kubernetes/), which bills itself as a 'cloud-native database'. CockroachDB doesn't actually require PVs in certain configurations, and each CockroachDB instance would be able to be fully stateless, using local (and much faster, if using NVMe disks) disk access.

However, for the shorter term, Drupal works best with MySQL or MariaDB, and in most cases PostgreSQL. So for now, you will have to solve the problem of how to run a persistent database in your Kubernetes cluster if you want to go fully cloud-native.

### Making Drupal's files directory persistent and scalable

Drupal needs to be able to write to the filesystem inside the codebase in a few instances:

  - During installation, Drupal writes over the `settings.php` file (if it needs to).
  - During installation, Drupal fails the installer preflight checks if the site directory (e.g. `sites/default`) is not writeable.
  - When building theme caches, Drupal needs write access to the public files directory (by default; this can be configured post-installation) so it can store generated Twig and PHP files.
  - If using CSS and JS aggregation, Drupal needs write access to the public files directory (by default; this can be configured post-installation) so it can store generated .js and .css files.

The easiest solution to all these problems—while allowing Drupal to scale up and run more than one Drupal instance—is to use a shared filesystem (usually NFS, Gluster, or Ceph) for the Drupal files folder (e.g. `sites/default/files`). Easiest does not mean _best_, however. Shared filesystems always have their share of troubles, for example:

  - Gluster and Ceph can sometimes become 'split-brained' or have strange failure modes which require manual intervention.
  - NFS can have issues with file lock performance at certain scales.
  - NFS can be slow for certain types of file access.

For all of these reasons, many people decide to use Amazon S3 as the public filesystem for their Drupal site, using something like the [S3FS](https://www.drupal.org/project/s3fs) module. But in most cases (and for a generalized approach that doesn't require more cloud services to be used), an approach using NFS (e.g. EFS in AWS) or [Rook](https://rook.io) to manage Ceph filesystems is used.

There's an open Drupal.org issue [Make the public file system an optional configuration](https://www.drupal.org/project/drupal/issues/2724963) which can help make the public filesystem a little more flexible in a container-based environment.

Making the `settings.php` file writeable during installation is a more tricky proposition—especially if you need to install Drupal, then deploy a new container image (what happens to all the values written to `settings.php`? They go poof!—which is why it gets special treatment as its own major challenge in running Drupal in Kubernetes:

### Making Drupal Installable inside a Kubernetes Cluster

Drupal installation is an interesting process. In some cases, you may want to allow people to install Drupal via the Install wizard UI, on the frontend. In other cases, you want to automatically install via Drush.

In either case, Drupal needs to do a few things during installation; one of those things—if you don't already have all the correct variables set in `settings.php`—is appending some extra configuration to the `sites/default/settings.php` file (or creating that file if it didn't already exist).

Through a bit of trial and error on the [Drupal for Kubernetes](https://github.com/geerlingguy/drupal-for-kubernetes/) project, I found that the following settings _must_ be pre-set and correct in `settings.php` if you want Drupal to automatically skip the installation screen that asks for DB connection details, and it also conveniently doesn't require writing to the settings.php file if you have these things set:

```
// Config sync directory.
$config_directories['sync'] = '../config/sync';

// Hash salt.
$settings['hash_salt'] = getenv('DRUPAL_HASH_SALT');

// Disallow access to update.php by anonymous users.
$settings['update_free_access'] = FALSE;

// Other helpful settings.
$settings['container_yamls'][] = $app_root . '/' . $site_path . '/services.yml';

// Database connection.
$databases['default']['default'] = [
  'database' => getenv('DRUPAL_DATABASE_NAME'),
  'username' => getenv('DRUPAL_DATABASE_USERNAME'),
  'password' => getenv('DRUPAL_DATABASE_PASSWORD'),
  'prefix' => '',
  'host' => getenv('DRUPAL_DATABASE_HOST'),
  'port' => getenv('DRUPAL_DATABASE_PORT'),
  'namespace' => 'Drupal\Core\Database\Driver\mysql',
  'driver' => 'mysql',
]
```

Notice how I used environment variables (like `DRUPAL_HASH_SALT`) with PHP's `getenv()` function instead of hard-coding values in the file. This allows me to control the settings Drupal uses both for installation _and_ for new containers that are started after Drupal is installed.

In a Docker Compose file, when I want to pass in the variables, I structure the web / Drupal container like so:

```
services:
  drupal:
    image: geerlingguy/drupal-for-kubernetes:latest
    container_name: drupal-for-kubernetes
    environment:
      DRUPAL_DATABASE_HOST: 'mysql'
      [...]
      DRUPAL_HASH_SALT: 'fe918c992fb1bcfa01f32303c8b21f3d0a0'
```

And in Kubernetes, when you create a Drupal Deployment, you pass in environment variables either using `envFrom` and a ConfigMap (preferred), and/or you can directly pass environment variables in the container spec:

```
---
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: drupal
  [...]
spec:
  template:
    [...]
    spec:
      containers:
        - image: {{ drupal_docker_image }}
          name: drupal
          envFrom:
          - configMapRef:
              name: drupal-config
          env:
            - name: DRUPAL_DATABASE_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: mysql-pass
                  key: drupal-mysql-pass
```

The above manifest snippet presumes you have a ConfigMap named `drupal-config` containing all the `DRUPAL_*` variables besides the database password, as well as a Secret named `mysql-pass` with the password in the key `drupal-mysql-pass`.

At this point, if you build the environment fresh using Docker Compose locally, or in a Kubernetes cluster, you could visit the UI installer _or_ use Drush, and not have to provide any database credentials since they (and other required vars) are all pre-seeded by the environment configuration.

### Environment-driven Drupal Configuration

Expanding on the previous challenge, there may be a number of other configuration settings you would want to be able to manipulate using environment variables. Unfortunately, Drupal itself doesn't yet have a mechanism for doing this, so you would need to either build these kind of settings into your own code using something like `getenv()`, or you would need to do something like configure a [Config Split](https://www.drupal.org/project/config_split) that manipulates certain Drupal configuration based on an environment variable that you pick up on during a configuration import process.

There is a Drupal.org issue, [Provide better support for environment variables](https://www.drupal.org/project/drupal/issues/2879846#comment-13064174), which will track the work to make environment-variable-driven configuration easier to do.

Many other PHP projects use something like [dotenv](https://github.com/vlucas/phpdotenv)—which allows variables to be read from a .env file locally (e.g. while in development), or your application can use environment variables directly. This is often helpful when you want to give developers more flexibility in managing multiple projects locally, and is kind of a prerequisite to adding first-class environment variable support to Drupal.

### Running Drupal's Cron Job(s) in Kubernetes

TODO: Working on this section. See also, for a hacky-but-workable solution: [Running Drupal Cron Jobs in Kubernetes](https://www.jeffgeerling.com/blog/2018/running-drupal-cron-jobs-kubernetes).

## Conclusion and More Resources

Besides my internal project at Acquia, I also maintain three open source projects which I hope will be immensely useful to others who would like to run Drupal, containerized in production, in Kubernetes:

  - [Drupal Example for Kubernetes](https://github.com/geerlingguy/drupal-for-kubernetes/)
  - [Raspberry Pi Dramble](https://www.pidramble.com)
  - [Drupal Pi](https://github.com/geerlingguy/drupal-pi) (Uses Docker Compose on a single Pi rather than a four-node Kubernetes cluster)

I welcome conversation in those projects' issue queues (and in the comments below!), and we had a good discussion about the above topics at the DrupalCon Seattle BoF: [Drupal, Contained in Production - Docker and Kubernetes](https://events.drupal.org/seattle2019/bofs/drupal-contained-production-docker-and-kubernetes). If you're also generally interested in Drupal and Kubernetes, I had a fun presentation on how I run Drupal on Kubernetes on a cluster of Raspberry Pis at DrupalCon Seattle, just a couple days ago—the video and slides are both available if you click through the link: [Everything I know about Kubernetes I learned from a cluster of Raspberry Pis](https://events.drupal.org/seattle2019/sessions/everything-i-know-about-kubernetes-i-learned-cluster-raspberry-pis).

You can join the **#kubernetes** channel on the [Drupal Slack](https://www.drupal.org/slack) to follow some of the discussion around Kubernetes. You can also browse [issues tagged with 'kubernetes'](https://www.drupal.org/project/issues/search?issue_tags=kubernetes) in the Drupal.org issue queue to try to make some of these challenges easier to meet.
