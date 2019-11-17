Refresh existing dev environment
================================

**Document owner**: Harrison Leong ([@leong96](https://github.com/leong96))

Are you working on this project, but afraid you messed something up?
This page explains how to do a full reset and start with a fresh environment:


## Create a fresh environment

1. Make sure the application is stopped (`docker-compose down`).
2. Delete the database Docker volume (`docker volume rm django-rit-grasa_djangograsa_db`).
3. Make a copy of`config.yml.example` and name it `config.yml`.
4. Rebuild the project containers and start the app (`docker-compose up --build`).
5. In a separate shell window, run `docker ps`, which shows all running containers. They should be _mariadb_ and _django-rit-grasa_.
    * If for some reason, they are not both there, use `docker ps -a` to get the name of the list of all containers, including the non running ones, then `docker start [containerID]` to start them.
6. Run the command `docker exec -it [containerID for the django container] /bin/bash`.
7. Run `python3 manage.py migrate`
8. Run `python3 manage.py rebuild_index`
9. Visit [localhost:8000](http://localhost:8000) in a browser

## Initial app configuration

These directions only apply to local development.
See the _Admin Quickstart_ for a production deployment.

1. Visit [localhost:8000/admin_user](http://localhost:8000/admin_user)
2. Visit [localhost:8000/create_database](http://localhost:8000/create_database)
3. Site is now usable with the following admin account:
    * **Username**: `grasatest@yahoo.com`
    * **Password**: `Password1`

Note that the MySQL/MariaDB container is started automatically with a `grasa_event_locator` database, but this will not happen automatically in production.
