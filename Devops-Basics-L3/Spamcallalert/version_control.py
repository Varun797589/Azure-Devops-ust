# Versioning models and configurations in Azure DevOps

# Steps to set up version control:
# 1. Initialize a Git repository if not already done.
# 2. Add the trained model and configuration files to the repository.
# 3. Commit the changes with a meaningful message.
# 4. Push the changes to an Azure DevOps repository.

import os
import subprocess

def initialize_git_repo():
    try:
        if not os.path.exists(".git"):
            subprocess.run(["git", "init"], check=True)
            print("Initialized a new Git repository.")
        else:
            print("Git repository already initialized.")
    except Exception as e:
        print(f"Error initializing Git repository: {e}")

def add_files_to_repo(files):
    try:
        subprocess.run(["git", "add"] + files, check=True)
        print("Files added to Git repository.")
    except Exception as e:
        print(f"Error adding files to Git repository: {e}")

def commit_changes(message):
    try:
        subprocess.run(["git", "commit", "-m", message], check=True)
        print("Changes committed to Git repository.")
    except Exception as e:
        print(f"Error committing changes: {e}")

def push_to_azure_repo(remote_url, branch="main"):
    try:
        subprocess.run(["git", "remote", "add", "origin", remote_url], check=True)
        subprocess.run(["git", "branch", "-M", branch], check=True)
        subprocess.run(["git", "push", "-u", "origin", branch], check=True)
        print("Changes pushed to Azure DevOps repository.")
    except Exception as e:
        print(f"Error pushing to Azure DevOps repository: {e}")

# Example usage
if __name__ == "__main__":
    model_file = "random_forest_model.joblib"
    config_file = "config.yaml"  # Replace with your actual configuration file
    remote_repo_url = "https://dev.azure.com/your_organization/your_project/_git/your_repo"  # Replace with your Azure DevOps repo URL

    try:
        initialize_git_repo()
        add_files_to_repo([model_file, config_file])
        commit_changes("Add trained model and configuration files.")
        push_to_azure_repo(remote_repo_url)
    except Exception as e:
        print(f"Error during version control setup: {e}")