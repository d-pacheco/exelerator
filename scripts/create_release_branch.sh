#!/bin/bash

# Check if version number is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <version-number>"
  exit 1
fi

# Set the branch name
BRANCH_NAME="v$1"

# Create a new orphan branch
git checkout --orphan "$BRANCH_NAME"

# Remove all files from the new branch
git rm -rf .

# Restore the desired files from the master branch
git checkout main -- README.MD Exelerator.exe

# Commit the changes
git commit -m "Initial commit with only readme.md and exelerator.exe for version $1"

# Push the new branch to the remote repository
git push origin "$BRANCH_NAME"

echo "Branch $BRANCH_NAME created and pushed successfully."
