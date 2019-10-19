How to: Create initial admin user
=================================

This how-to article explains how to create the first admin user in a new installation.


## Background

There is no admin user built into the application.
The first admin user must be manually created via a SQL query.
It is planned for a later development phase to do this automatically.


## Pre-requirements

You need access to the MySQL server used for the application.
If in production, this is wherever your database server is hosted.
If in local development with **Docker Compose**, this requires opening a shell inside of the database (`db`) container.
See [_How to: Exec into a container_](/howto/exec-container) for more help on how to do this.


## Commands

```sql
UPDATE grasa_event_locator_userinfo SET isAdmin=1, isPending=0, isActive=1;
```

This lets you log into the site.
Once logged in, go to the _Admin_ page and click the _Database_ button.
This populates the categories table before proceeding further.

Eventually, it is intended to replace this with an admin user configured from a file.
