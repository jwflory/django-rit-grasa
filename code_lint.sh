#!/bin/sh
#
# This script is used to lint our code according to a specific standard. For
# this script to work, you must install the project development dependencies:
#
#   $ pipenv shell
#   $ pipenv sync --dev
#

black .
