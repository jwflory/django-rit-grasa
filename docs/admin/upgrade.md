# Upgrade guide

## Why you might want to upgrade
1. if a new version were released or
2. You have new features you have developed that you would like to move into production.

Note: If you're adding your own development features, this guide assumes you have fully tested everything.

## Database Concerns
It is _highly_ recommended to make a backup of your database before making any upgrades.  
If the new version you are upgrading to has database schema changes, then you will need to upgrade your migrations file and remigrate your database.  
This will most likely wipe your data. 
The following scenarios are examples of where data may or may not be deleted:
- Deleting a model.
    If the user is doing this, there's guaranteed data loss for the obvious reason; you're deleting a table that had app data; that's the reason the table was there in the first place.
- Adding a model.
    There's no data loss from this; adding a table shouldn't affect the app's behavior, at least assuming no changes to the code.
- Removing columns from an existing table.
    Obvious data loss here, a whole column is being removed.
- Adding columns to an existing table.
    Adding some types of columns to a table will force you to also specify a default value (ie contact_name = models.CharField(max_length=255, default="Name not Specified")). 
    Some will not (ie models.TextField). 
    No data is lost, though if a column that requires a default is added to a table, existing entries will now have that default value in the column post-migration.

It is recommended to start a new database alongside your current database and update your config file with the new database information.  
Then you can copy your old data over. 
__This should be tested before moving new code to production using a copy of your data__.  
You have been warned.

 ## How To Actually Upgrade 

The upgrade process is rather simple.
The steps for upgrading to a new version of the GRASA Event Locator are as follows:

1. Stop the current running application by running:
    ```sh
    ./up.py --stop
    ``` 

2. Move the new code into location.
    This can either be done by copying all the code into the directory using git, and downloading the new production code from a   remote repository, or by downloading a zip file with all the code into a new directory and esentially starting over.
3. Rebuild the container to now include the new code using this command:
    ```sh
    ./up.py --setup
    ```
4.  If the rebuild step is successful, then start the application with this command:
    ```sh
    ./up.py --start --port <port number>
_If_ your data is going to remain intact and all your users are still there, then you should not need to go to <site_name>/initial_setup again.  
However if you're starting with a new, empty, database you will need to browse to <site_name>/initial_setup again.
