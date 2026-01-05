# Azure DevOps Pipeline for ARM Template Deployment

This repository contains an Azure DevOps YAML pipeline (`azure-pipeline.yml`) to deploy Azure infrastructure using ARM templates.

## Steps to Use the Pipeline

### 1. Prerequisites
- Ensure you have an Azure DevOps project set up.
- Authenticate your Azure subscription in Azure DevOps.
- Have the ARM template file (`azuredeploy.json`) ready in your repository.

### 2. Add the Pipeline to Your Repository
1. Place the `azure-pipeline.yml` file in the root of your repository or in a `.azure-pipelines` folder.
2. Commit and push the file to your repository.

### 3. Create the Pipeline in Azure DevOps
1. Navigate to your Azure DevOps project.
2. Go to **Pipelines** > **New Pipeline**.
3. Select your repository and point it to the `azure-pipeline.yml` file.
4. Save and run the pipeline.

### 4. Pipeline Stages
The pipeline consists of the following stages:

#### **Validate**
- Validates the ARM template using Azure CLI.

#### **Deploy**
- Creates or updates the resource group.
- Deploys the ARM template to the specified resource group.

#### **Verify**
- Verifies the deployment by listing the resources in the resource group.

#### **Rollback**
- Executes rollback steps if the deployment fails.

### 5. Variables
- `environment`: The deployment environment (e.g., `dev`).
- `armTemplate`: The path to the ARM template file (e.g., `azuredeploy.json`).

### 6. Notes
- Ensure the Azure subscription is authenticated and has the necessary permissions.
- The pipeline uses Azure CLI for all operations.
- Follow the principle of least privilege and idempotent execution.

### 7. Troubleshooting
- If the pipeline fails, check the logs for detailed error messages.
- Ensure the ARM template is valid and follows Azure standards.

### 8. Rollback Steps
- If the deployment fails, the pipeline will trigger the rollback stage.
- Implement specific rollback logic in the `Rollback` stage of the pipeline.