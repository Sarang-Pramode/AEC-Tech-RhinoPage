#!/bin/bash

# Directory of your repository
REPO_DIR="/Users/sarangpramode/Desktop/AECTech/RhinoPage/AEC-Tech-RhinoPage"

# File to watch
FILE_TO_WATCH="$REPO_DIR/output.mmd"

# Change to repository directory
cd "$REPO_DIR"

# Check if there are any changes
if git diff --exit-code "$FILE_TO_WATCH"; then
    # No changes
    exit
else
    # Add changes to the index
    git add "$FILE_TO_WATCH"

    # Commit changes
    git commit -m "Auto-commit: $(date '+%Y-%m-%d %H:%M:%S')"

    # Push to remote repository
    git push
fi
