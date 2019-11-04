Troubleshooting
===============

<!--
    Style rule: one sentence per line please!
    This makes git diffs easier to read.
-->

This page is a collection of miscellaneous tips, tricks, and other tidbits of info to make it easier to do troubleshooting on the application.


## Database change issues

Occasionally, you'll get an error that comes from the database changing (field not found, category matching query does not exist).
You may be able to check for this by going to GitHub Desktop and seeing if `models.py` was changed in the recent commits.

The first thing to try is click the _Wipe Events and Recreate Categories_ button in the header.
See if this helps.
If not, then in a Terminal window, run `python3 manage.py makemigrations`, and `python3 manage.py migrate`.
Try the task again.

If that doesn't work, go into the mySQL container, drop the database, create it again.
Then in the django container, go to the migrations folder with `cd`, and delete all files/folders using `rm` and `rm -r` except for `__init.py__`.
Run `python3 manage.py makemigrations` and `python3 manage.py migrate`, which should work.
Go to the website, click the _Create Administrator_ header button and _Wipe Events and Recreate Categories_.
This gives you a fresh start.
