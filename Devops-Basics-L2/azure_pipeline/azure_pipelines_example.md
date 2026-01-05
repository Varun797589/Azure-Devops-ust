# Azure Pipelines Deep Dive: YAML, Variables, Triggers, Environments

This guide provides a simple example to understand the core concepts of Azure Pipelines, including YAML, variables, triggers, and environments.

## Example Pipeline YAML File

```yaml
trigger:
  branches:
    include:
      - main

pool:
  vmImage: 'ubuntu-latest'

variables:
  - name: buildConfiguration
    value: Release

steps:
  - script: echo "Building the project..."
    displayName: 'Build Step'

  - script: echo "Running tests..."
    displayName: 'Test Step'

  - script: echo "Deploying to environment..."
    displayName: 'Deploy Step'
    env:
      DEPLOY_ENV: production
```

## Key Concepts

### 1. YAML
YAML is used to define the pipeline structure. The above example includes:
- **trigger**: Specifies the branch that triggers the pipeline.
- **pool**: Defines the agent pool to use.
- **steps**: Lists the tasks to execute.

### 2. Variables
Variables allow you to reuse values across the pipeline. In the example, `buildConfiguration` is defined as a variable.

### 3. Triggers
Triggers define when the pipeline should run. The `trigger` section specifies that the pipeline runs on changes to the `main` branch.

### 4. Environments
Environments represent deployment targets. In the example, the `DEPLOY_ENV` variable is used to specify the deployment environment.

## How to Run

1. **Commit the YAML File**:
   Save the above YAML content as `azure-pipelines.yml` in the root of your repository.

2. **Set Up the Pipeline**:
   - Navigate to Azure DevOps.
   - Go to **Pipelines** > **Create Pipeline**.
   - Select your repository and choose the YAML file.

3. **Run the Pipeline**:
   - Click **Run Pipeline**.
   - Monitor the execution in the Azure DevOps interface.

---

This example demonstrates the basics of Azure Pipelines. For more advanced scenarios, refer to the [official documentation](https://learn.microsoft.com/en-us/azure/devops/pipelines/).