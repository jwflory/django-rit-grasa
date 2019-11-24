Troubleshooting
===============

<!--
    Style rule: one sentence per line please!
    This makes git diffs easier to read.
-->

This page is a collection of miscellaneous tips, tricks, and other tidbits of info to make it easier to do troubleshooting on the application.


## Q: On Fedora, Pipenv fails with MySQL config error

On Fedora, `pipenv install` may fail with the following error:

```python
OSError: mysql_config not found
```

Install the `mariadb-connector-c-devel` package.
It includes the `mysql_config`/`mariadb_config` binary needed to install the `mysqlclient` library.

On Fedora:

```sh
sudo dnf install -y mariadb-connector-c-devel
```


## Database changes during development

Occasionally, you get an error from the database changing (field not found, category matching query does not exist).
You can check this by checking if `models.py` was changed recently.

Open a shell to the Django container by [exec'ing into the app container](/dev/exec-container).
Run the following commands:

```sh
python manage.py makemigrations
python manage.py migrate
```

Try the task again.
If it works, make sure the generated database migration script is committed to the git repository along with your other changes.
If it does not work, try [refreshing your development environment](/dev/start-fresh).
