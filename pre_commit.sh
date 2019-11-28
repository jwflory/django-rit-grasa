#!/bin/sh
#
# Stash unstaged changes and lint Python files to PEP-8/Black standard
#
# This script is used to enforce style changes before a commit is saved. This
# means this script is executed automatically before a commit is made. The
# script does the following:
#
# * Stores unstaged changes in a git stash
# * Lints code using Black
# * Pops stashed changes back to staging
#
# You must install development dependencies for this script to work:
#
#   $ pipenv shell
#   $ pipenv sync --dev
#

# If the git pre-commit script does not exist yet, create it.
if [ -d ".git" ] && [ ! -f ".git/hooks/pre-commit" ]; then
    ln -s ../../pre_commit.sh .git/hooks/pre-commit
fi

# Stash any unstaged changes to avoid overwriting ongoing work.
STASH_NAME="pre-commit-$(date +%s)"
git stash save -q --keep-index $STASH_NAME

# Lint code according to PEP-8/Black rules.
black . --exclude=grasa_event_locator/migrations

# Pop stashed changes back into staging.
STASHES=$(git stash list)
if [[ $STASHES == "$STASH_NAME" ]]; then
    git stash pop -q
fi
