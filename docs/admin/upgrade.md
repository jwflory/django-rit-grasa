# Upgrade guide

## Why you might want to upgrade
1. if a new version were released
2. you have new features you have developed that you would like to move into production.

Note: If you're adding your own development features, this guide assumes you have fully tested everything

## Database Concerns
It is _highly_ recommended to make a backup of your database before making any upgrades.  If the new version you are upgrading to has database schema changes, then you will need to upgrade your migrations file and remigrate your database.  This will most likely wipe your data.  It is recommended to start a new database alongside your current database and update your config file with the new database information.  Then you can copy your old data over.  __This should be tested before moving new code to production using a copy of your data__.  You have been warned.

 ## How To Actually Upgrade 

The upgrade process is rather simple.
The steps for upgrading to a new version of the GRASA Event Locator are as follows:

1. Move the new code to the application folder.  This can either be done by copying all the code into the directory using git, and downloading the new production code from a remote repository, or by downloading a zipfile with all the code into a new directory and esentially starting over.
2. Stop the current running application by running
    ```sh
    ./up.py --stop
    ```
3. Rebuild the Container to now include the new code using this command:
    ```sh
    ./up.py --setup
    ```
4.  If the rebuild step is successful, the start the application with this command:
    ```sh
    ./up.py --start --port <port number>
_If_ your data is going to remain intact and all your users are still there, then you should not need to go to <site_name>/initial_setup again.  However if you're starting with a new, empty, database you will need to browse to <site_name>/initial_setup again.
