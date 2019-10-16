How to: Exec into a container
=============================

This how-to article explains how to open a shell inside of a Docker container for advanced debugging capabilities.


## Background

Containers add a large of abstraction to working on the project.
Or said differently, they hide many parts of your environment, compared to running it locally.
Sometimes you need more advanced commands or functionality to debug a tricky problem.
This guide teaches how to debug issues by opening a shell inside of a container.


## Pre-requirements

**Docker** and **Docker Compose** should be installed.
This guide is written for the **command-line interface** of Docker.
This varies across operating systems, but refer to [Docker docs](https://docs.docker.com/install/) for more help.

Start the local containers with `docker-compose up`.
In a new window, note the names of the running containers (`docker ps`); you will need the name of the `web` container later.


## Commands

```sh
$ docker exec -it <container name> <"echo 'Some command here'">
$ docker exec -it web_1 /usr/bin/bash
```
