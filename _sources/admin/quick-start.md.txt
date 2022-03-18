Admin quick start guide
=======================

This page explains how to install and set up the application for a production environment.
These instructions focus on _new installations only_.

## Dependencies

The following dependencies must be satisfied for the app to work:

1. CentOS 7.5+
2. [Python 3](https://www.python.org/downloads/ "Download Python 3")
3. [Docker](https://docs.docker.com/install/)

Once the dependencies are in place, place a copy of the project source code (preferably with `git`) in the directory of your choice.


## Set up database

The Event Locator is designed to have a standalone database paired with it.
The database is linked to the app through the config file.

To get started, install MySQL/MariaDB and set up a login for the application.
On CentOS 7, the MariaDB package can be installed as follows:

```sh
sudo yum install -y mariadb-server mariadb
```

Create a user and database for the application.
Make sure the user has write access to the database.
Add these credentials and information (host, username, password, database name) to the config file (see [`config.yml.example`](https://github.com/jwflory/django-rit-grasa/blob/master/config.yml.example "Upstream sample config file" for config file documentation).


## Install your configuration

Copy the `config.yml.example` file to `config.yml` inside of the git repo.
Edit the config file to your preferences (see [`config.yml.example`](https://github.com/jwflory/django-rit-grasa/blob/master/config.yml.example "Upstream sample config file" for config file documentation).

**NOTE**: Any time you make changes to the config file, the container image _must_ be rebuilt.


## Container host set-up

We need to build the container with all the code and config file changes, and to do that use this command:

```sh
python3 up.py --setup
```

What this does is build the container from the Dockerfile.production file and migrates the database so that it will have all the necessary tables when the container is started.

## Start Event Locator

Choose the port to run the app on (useful for HTTP vs. HTTPS):

```sh
up.py --start -p <port number>
```
This command starts the container, and then queries the database to load any already submitted events.

### Run initialization script

When the application is installed for the first time, an initialization script must be executed.
The initialization script sets up activity filters and creates a first admin user with the `admin_email` from the config file.
The initial admin has a default password of `Password1` (please change after first login!).
The script will _only_ work if two conditions are both met:

1. No admin users already exist
2. Activity filters do not yet exist in database

Thus, it is important this step is followed first.

The initialization script is triggered by navigating to the following URL:

```
<site_name>/initial_setup
```

`_site_name` is also managed in the config file.
For example, in development, this might be [localhost:8000/initial_setup](http://localhost:8000/initial_setup).


## Stop Event Locator

If you need to stop the app for any reason, this can be done with this command:

```sh
up.py --stop
```

## Restart Event Locator

If for any reason you need to restart the container without rebuilding, you can use this command:

```sh
up.py --restart -p <port number>
