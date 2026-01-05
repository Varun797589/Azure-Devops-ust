# Project Documentation

## Overview
This repository contains the following files to manage and deploy Azure resources:

1. **`virtual_network.tf`**: Terraform configuration file to provision Azure virtual networks.
2. **`DeployAzureVM.ps1`**: PowerShell script to deploy Azure Virtual Machines.
3. **`UpdateVMScaleSet.py`**: Python script to update Azure Virtual Machine Scale Sets.
4. **`azure-pipelines.yml`**: Azure DevOps pipeline configuration for CI/CD workflows.
5. **`Jenkinsfile`**: Jenkins pipeline configuration for CI/CD workflows.

---

## Prerequisites
Ensure the following tools are installed on your system:

- **Terraform**: Install using Homebrew:
  ```bash
  brew install terraform
  ```
- **Azure CLI**: Install using Homebrew:
  ```bash
  brew install azure-cli
  ```
- **Python**: Ensure Python 3.x is installed. Install dependencies using:
  ```bash
  pip install -r requirements.txt
  ```
- **PowerShell**: Install PowerShell Core (`pwsh`) if not already installed.

---

## Suggested Execution Order

### 1. Provision Infrastructure with Terraform
1. Navigate to the directory containing `virtual_network.tf`.
   ```bash
   cd /Users/venkatesh/Devops-GenAI_UST/AzureDevOpsFoundations
   ```
2. Initialize Terraform:
   ```bash
   terraform init
   ```
3. Plan the infrastructure:
   ```bash
   terraform plan
   ```
4. Apply the configuration:
   ```bash
   terraform apply
   ```

### 2. Deploy Azure Virtual Machines
1. Open a terminal that supports PowerShell (e.g., `pwsh`).
2. Run the PowerShell script:
   ```bash
   pwsh DeployAzureVM.ps1
   ```

### 3. Update Virtual Machine Scale Sets
1. Ensure Python dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Python script:
   ```bash
   python UpdateVMScaleSet.py
   ```

### 4. Configure CI/CD Workflows
#### Azure DevOps Pipeline
1. Commit `azure-pipelines.yml` to your Azure DevOps repository.
2. Trigger the pipeline in Azure DevOps.

#### Jenkins Pipeline
1. Commit `Jenkinsfile` to your Jenkins repository.
2. Trigger the pipeline in Jenkins.

---

## Steps Executed

### 1. Provision Infrastructure with Terraform
- Initialized Terraform: `terraform init`
- Planned the infrastructure: `terraform plan`
- Applied the configuration: `terraform apply`

### 2. Deploy Azure Virtual Machines
- Ran the PowerShell script: `pwsh DeployAzureVM.ps1`

### 3. Update Virtual Machine Scale Sets
- Installed required Python packages: `azure-identity`, `azure-mgmt-compute`
- Updated the Python script with subscription ID and location.
- Ran the Python script: `python UpdateVMScaleSet.py`

### 4. Configure CI/CD Workflows
- Committed `azure-pipelines.yml` to Azure DevOps repository and triggered the pipeline.
- Committed `Jenkinsfile` to Jenkins repository and triggered the pipeline.

---

## Notes
- Ensure you are authenticated with Azure CLI before running Terraform or scripts:
  ```bash
  az login
  ```
- Follow the logs for each step to ensure successful execution.

---

## Troubleshooting
- If Terraform fails, ensure Azure CLI is installed and authenticated.
- For Python scripts, verify dependencies are installed and the Python version is compatible.
- For PowerShell scripts, ensure you have the necessary permissions to deploy resources.

---

## Contact
For any issues, please contact the repository maintainer.