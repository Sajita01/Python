print("Hi")
print("Github Setup")

"""
# 1. Configure Git

# Set your Git username
git config --global user.name "Sajita Khadka"

# Set your Git email
git config --global user.email "sajitakhadka21@gmail.com"

# Check configuration
git config --global --list

# 2. Install GitHub CLI

# Install GitHub CLI on Windows
winget install --id GitHub.cli

# Check installation
gh --version

# 3. Login to GitHub

# Login to GitHub
gh auth login

# Check login status
gh auth status

# 4. Create a Git Repository

# Create a project folder
mkdir myproject

# Enter the project folder
cd myproject

# Initialize Git
git init

# Check repository status
git status

# 5. Add and Commit Files

# Add a specific file
git add hello.py

# Add all changed files
git add .

# Save changes with a commit
git commit -m "Add hello.py"

# 6. Check Commit History

# Display complete commit history
git log

# Display short commit history
git log --oneline

# 7. Create a .gitignore File

# Create .gitignore
touch .gitignore

# Add the following inside .gitignore:
# Ignore virtual environment
.venv/

# Ignore Python cache files
__pycache__/

# Ignore environment variables
.env
# Add .gitignore
git add .gitignore

# Commit changes
git commit -m "Add .gitignore"

# 8. Connect Local Repository to GitHub

# Connect local repository to GitHub
git remote add origin https://github.com/username/myproject.git

# Check remote connection
git remote -v


# 9. Push Code to GitHub

# Push code for the first time
git push -u origin main

# Push future changes
git push

# 10. Clone a GitHub Repository

# Download a repository from GitHub
git clone https://github.com/username/myproject.git

# Enter the cloned project
cd myproject

# 11. Pull Latest Changes

# Download latest changes from GitHub
git pull

# Pull from a specific branch
git pull origin main

# 12. Create and Switch Branches
# View available branches
git branch

# Create and switch to a new branch
git switch -c feature-login

# Switch back to main
git switch main

# Alternative older command
git checkout -b feature-login

# 13. Merge Branches
# Switch to main branch
git switch main

# Merge feature branch into main
git merge feature-login

# Push merged changes
git push

# Delete completed branch
git branch -d feature-login

# 14. Resolve Merge Conflicts
# If a merge conflict occurs, open the conflicting files and resolve the issues.
# After manually editing and resolving the conflict:

# Stage the corrected file
git add hello.py

# Commit the resolved changes
git commit -m "Resolve merge conflict"

"""