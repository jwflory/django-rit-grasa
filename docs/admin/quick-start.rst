######################
Admin quickstart guide
######################

This page explains how to install and set up the Event Locator for a new production deployment.


************
Dependencies
************

#. CentOS 7.5+ / Docker_ **OR** CentOS 7.6+ / Podman_ [#]_
#. `Python 3`_

Once dependencies are installed, clone a copy of the project source code (preferably with ``git``) in the directory of your choice.


**************
Database setup
**************

The Event Locator is designed to have a standalone database paired with it.
The database is linked to the app through the config file.

First, install MySQL/MariaDB.
On CentOS 7, the MariaDB package can be installed as follows::

    sudo yum install -y mariadb-server mariadb

Create a new user and database for the Event Locator.
Make sure the user has write access to the database.
Add these credentials (host, username, password, database name) to the config file (see `config.yml.example`_ for config file documentation).


*********************
Install configuration
*********************

.. warning:: Any time changes are made to the config file, the container image *must* be rebuilt.

Copy the `config.yml.example`_ file to ``config.yml`` inside of the project source code directory.
Edit the config file to your preferences.


********************
Container host setup
********************

Build the container with all the code and config file changes::

    python3 up.py --setup

This builds the container from the ``Dockerfile.production`` file and initializes database schema, so the necessary tables exist when the container is started.

Proxy server
============

It is strongly recommended to run the Event Locator behind a proxy server, preferably like NGINX.
**See** `Gunicorn deployment documentation`_ **for a detailed overview of how to do this.**

Why is a proxy server needed?
The Event Locator container runs the application with Gunicorn_, a Python WSGI HTTP Server for UNIX.
For best performance and sustainability over time, Gunicorn recommends deploying with a proxy server.


*******************
Start Event Locator
*******************

Choose the port to run the app on (useful for HTTP vs. HTTPS)::

    python3 up.py --start -p <port number>

This command starts the container, and then queries the database to load any already submitted events.

Run initialization script
=========================

The initialization script must be triggered on a new installation by navigating to the following URL::

    <site_name>/initial_setup

When the application is installed for the first time, an initialization script must be executed.
The initialization script sets up activity filters and creates a first admin user with the ``admin_email`` from the config file.
The initial admin has a default password of ``Password1`` (*please change after first login!*).
The script *only* works if two conditions are both met:

1. No admin users already exist
2. Activity filters do not yet exist in database

Thus, it is important this step is followed first.

.. note::
    ``site_name`` is also managed in the config file.
    For example, in development, this might be `localhost:8000/initial_setup <http://localhost:8000/initial_setup>`_.


******************
Stop Event Locator
******************

If you need to stop the app for any reason::

    python3 up.py --stop


*********************
Restart Event Locator
*********************

If you need to restart the container without rebuilding::

    python3 up.py --restart -p <port number>


.. [#] Podman_ is a new container run-time developed by Red Hat.
       It aims to be a drop-in replacement for Docker.
       Some of its more interesting features include `rootless containers`_: containers that can be ran safely and securely by any unprivileged user.
       Docker requires cautious configuration for use in production, if not using container orchestration tools (e.g. Kubernetes/OpenShift).
       Podman leverages the `user namespaces`_ feature of the Linux kernel to spawn new containers safely under the same UID as a user.
       If you are not already using containers and are interested in an easier production pathway without container orchestration, Podman is an interesting and effective tool.

.. _`config.yml.example`: https://github.com/jwflory/django-rit-grasa/blob/master/config.yml.example
.. _`Docker`: https://docs.docker.com/install/
.. _`Gunicorn`: https://gunicorn.org/
.. _`Gunicorn deployment documentation`: http://docs.gunicorn.org/en/stable/deploy.html
.. _`Podman`: https://podman.io/
.. _`Python 3`: https://www.python.org/downloads/
.. _`rootless containers`: https://blog.justinwflory.com/2019/08/hpc-workloads-containers/
.. _`user namespaces`: http://man7.org/linux/man-pages/man7/user_namespaces.7.html
