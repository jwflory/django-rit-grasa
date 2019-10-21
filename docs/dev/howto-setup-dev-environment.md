Create a local development environment
======================================

<!--
    Please write each sentence on its own line.
    This makes changes easier to review in pull requests because of how git diffs work.
    More info here:
      https://asciidoctor.org/docs/asciidoc-recommended-practices/#one-sentence-per-line
  -->

This page explains how to set up a local development environment to test the GRASA Event Locator system.


## Requirements

* [Docker](https://docs.docker.com/install/)
* [docker-compose](https://docs.docker.com/compose/install/)


## Setup

A configuration file must be provided at start, either as a `config.yml` in the root directory of the project or a path specified as a `CONFIGPATH` environment variable.
For local development, run the following command to get started with development:

```sh
cp config.yml.example config.yml
```


## Run project with docker-compose

`docker-compose` is used for local development.
It is convenient since it gives you a MySQL container to work alongside the application; you do not have to set one up.
Use the following commands to build the containers and then start them:


```sh
docker-compose build
docker-compose up
```

These commands may require `sudo` depending on your operating system and installation option.

#### Run docker-compose in detached mode

Detached mode disables an output stream to your terminal.
In other words, detached mode will not display logs in the terminal window while running.
Use the following command to run in detached mode:

`docker-compose up --detach`

To shut down `docker-compose` in detached mode, use this command:

`docker-compose down`


## Open in web browser

Once `docker-compose` is running, open a web browser.
Visit [localhost:8000](http://localhost:8000/) to view the site running locally.


## Troubleshooting

### Q: On Fedora, `pipenv install` fails with an error: `OSError: mysql_config not found`

Install the `mariadb-connector-c-devel` package.
It includes the `mysql_config`/`mariadb_config` binary needed to install the `mysqlclient` library.

```sh
sudo dnf install -y mariadb-connector-c-devel
```
