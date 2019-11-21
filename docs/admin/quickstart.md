# Quick Start Guide

## Dependencies
The following dependencies need to be satisfied in order for the app to work.
1. CentOS machine
2. Docker
2. git
3. `$ git clone htts://github.com/jwflory/django-grasa-rit` into the directory of your choice
## Setting up the Database
The Grasa Event Locator is designed to have a stand alone database paired with it, and the database is linked to the app through the config file.

To get started, install mariadb server and login to mysql.  Create a user with the same credentials as in the config file.  Create a database also named from the config file, and gice the user you just created access to that database.

## Config File
1.  $ cp config.yml.example config.yml`
2. `$ nano config.yml` (or the editor of your choice)
3. change the setting in the config file to match the configuraion of your enviornment.
## Setup
`$ up.py --setup` 

## Starting
`$ up.py --start -p <port number>` Choose the port you'd like the app to run on.

## Initial Config
Go to a browser and go to the site to make sure it is up, the type into the url bar <site_name>/initial_setup

This step will create the first admin user specified in the config file, which can be deleted later, with the default password of `Password1`
It will also initialie the database with all the category names.  Once this step is done, it cannot be done again.  Checks are included to verify if the categories are already in the database, and will skip that if they are, and same with the admin user.

## Stopping
If you need to stop the app for any reason, this can be done with this command:
`$ up.py --stop`
