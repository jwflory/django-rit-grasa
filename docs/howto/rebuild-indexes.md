How to: Rebuild search indexes
==============================

This is a how-to article to rebuild the Whoosh/Haystack search indexes when new events are added to the database.


## Background

New events are added to the database periodically.
For the new events to appear in search, the index needs to be rebuilt.
Once the index is rebuilt to include new events, they will appear in searches.

### Development note

Automatic rebuilding of search indexes is planned.
These steps are mostly intended for local development or to force a index rebuild.


## Pre-requirements

If running the project as a container, use `docker exec` to open a shell inside the web app container.
See the [How to: Exec into a container](/howto/exec-container) doc for more info of how to do this.

If not running the project as a container, get to the environment where your Python 3 + Django installation exists.


## Commands

If building index for first time:

```sh
python3 manage.py rebuild_index
```

If refreshing for new data, e.g. a new event:

```sh
python3 manage.py update_index
```
