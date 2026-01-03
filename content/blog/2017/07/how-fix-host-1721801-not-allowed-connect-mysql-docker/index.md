---
nid: 2796
title: "How to fix \"Host '172.18.0.1' is not allowed to connect\" with MySQL Docker"
slug: "how-fix-host-1721801-not-allowed-connect-mysql-docker"
date: 2017-07-18T14:10:23+00:00
drupal:
  nid: 2796
  path: /blog/2017/how-fix-host-1721801-not-allowed-connect-mysql-docker
  body_format: markdown
  redirects: []
tags:
  - database
  - docker
  - mysql
  - volumes
---

Using the [official MySQL Docker image](https://hub.docker.com/_/mysql/) from Docker Hub, I recently ran into the error:

    Host '172.18.0.1' is not allowed to connect to this MySQL server

The only change I had made to my `docker-compose.yml` file was:

    mysql:
      image: mysql:5.6
      ports:
        - '3306'
      volumes:
        # Use this option to persist the MySQL DBs in a shared volume.
        - ./mysqldata:/var/lib/mysql:rw,delegated
        # Use this option to persist the MySQL DBs in a data volume.
        # - db_data:/var/lib/mysql

I switched from using a data volume (`db_data`) to mounting a volume from my host (`mysqldata` in the current directory), and after the next time I did a `docker-compose down` and `docker-compose up`, I started seeing the error about my host not being allowed to connect to the MySQL server.

I'm not 100% sure why a data volume works, while a shared volume doesn't, but the fix is to make sure you clear out the contents of the shared directory between rebuilds of the Docker environment. See [this comment](https://github.com/docker-library/mysql/issues/275#issuecomment-292243855) in the MySQL image's GitHub issue queue for more details.
