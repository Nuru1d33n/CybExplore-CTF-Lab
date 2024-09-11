#!/bin/bash

# Navigate to your project directory (adjust if needed)
# cd /path/to/your/project

# Add all changes to the staging area
git add .

# Commit changes with a message
git commit -m "Automated commit message"

# Push changes to the remote repository
git push -u origin main --force
