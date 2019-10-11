How do I add new dependencies/libraries/frameworks to the project?
==================================================================

If we use a new library or framework, we need to **install it as a dependency** in the project.
Dependencies are specific versions of third-party software we want to use in the project.
Sometimes we want to test something out, without adding it to the project for everyone.
Other times, we want to install something to the project for everyone.
This guide explains both below:


## Set up a Pipenv shell

First, for either option, start a new Pipenv shell for your local development.
The Pipenv shell sets up a **Python virtual environment (virtualenv)** for you.
This way, you can install Python packages via `pip` without special user privileges, among other reasons.

Using a command-line tool of your preference, change directories to the project git directory and run the following commands:

```sh
pip3 install --user pipenv
pipenv shell
```

Pipenv will set up a virtualenv for you.
Once it is done, you can now install packages using `pip` into the virtualenv.


## Installing dependencies for testing

If you are trying out new libraries or third-party software, but aren't sure if you want to keep it yet, use `pip install`.

Simply use `pip install <package name>` to install any package from the Python Package Index (PyPI).
The package you install is available on your workstation, but not for everyone else.
This lets you test something out without committing everyone to using it yet.


## Installing dependencies for the team

If you are confident in using a library or third-party software, use `pipenv install`.

Once you know a package and are confident in keeping it, install it as a project dependency.
This makes it available for everyone when they run `docker-compose build` again.
Otherwise, when someone runs your changes, the Django app will crash because of a missing dependency.

There are two steps to installing new dependencies:

1. `pipenv install [--dev] <package name>`
2. `pipenv update --dev`

Run the first command with the `--dev` flag if installing a dependency only for development environments, not production.
The second command updates the `Pipfile.lock` file with your changes and ensures the versions installed locally match what is specified in `Pipfile.lock`.
