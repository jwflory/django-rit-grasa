Start with a fresh environment
==============================

**Document owner**: Harrison Leong ([@leong96](https://github.com/leong96))

Are you working on this project, but afraid you messed something up?
This page explains how to do a full reset and start with a fresh environment:


## Create a fresh environment

- Copy the file `config.yml.example` and rename it `config.yml`.
- Run `docker-compose up --build`.
- The site is now viewable at [localhost:8000](http://localhost:8000), but wait!
- In a separate shell window, run `docker ps`, which shows all running containers. They should be _mariadb_ and _django-rit-grasa_.
    - If for some reason, they are not both there, use `docker ps -a` to get the name of the list of all containers, including the non running ones, then `docker start [containerID]` to start them.
- Run the command `docker exec -it [containerID for the mariadb container] /bin/bash`
- Run `mysql -u grasaadmin -p`.
- Password is `djangoGrasa2019`.
- In mySQL, `DROP DATABASE grasa_event_locator`, and `CREATE DATABASE grasa_event_locator`.
- Type `exit;` to exit mySQL, and `exit` again to leave the mariadb container.
- Run the command `docker exec -it [containerID for the django container] /bin/bash`.
- Run `python3 manage.py makemigratons`
- Run `python3 manage.py migrate`
- Visit [localhost:8000](http://localhost:8000) in a browser

## Initial app configuration

The following three steps will need to be redone for deployment - as clearly clicking links will not be ideal.

- Click the **Create Administrator Account** button in the header.
- Click **Wipe Events & Recreate Categories** button in the header.
- Site is now usable with the following admin account:
    - Username: `grasatest@yahoo.com`
    - Password: `Password1`

Note that for some reason, even if there is no migration file present in the migration folder, the `docker-compose` command still produces a `grasa_event_locator` database.
Though right now, it is out of date, which warrants dropping it first before doing anything else.
