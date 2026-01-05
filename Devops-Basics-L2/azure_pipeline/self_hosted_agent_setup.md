# Custom Self-Hosted Agent Setup for Azure Pipelines

This guide explains how to set up a self-hosted agent for Azure Pipelines and run a simple code example tailored for the insurance domain.

## Prerequisites
1. An Azure DevOps organization.
2. A machine to act as the self-hosted agent (Linux, macOS, or Windows).
3. Install the following on the machine:
   - .NET SDK
   - Git

## Steps to Set Up the Self-Hosted Agent

### 1. Register the Agent
1. Navigate to your Azure DevOps organization.
2. Go to **Project Settings** > **Agent Pools**.
3. Select **Add Pool** and create a new agent pool.
4. Select the newly created pool and click **New Agent**.
5. Follow the instructions to download and configure the agent.

### 2. Configure the Agent
Run the following commands on the machine:
```bash
mkdir myagent && cd myagent
curl -O https://vstsagentpackage.azureedge.net/agent/2.220.0/vsts-agent-osx-x64-2.220.0.tar.gz
tar zxvf vsts-agent-osx-x64-2.220.0.tar.gz
./config.sh
```

### 3. Run the Agent
Start the agent:
```bash
./svc.sh install
./svc.sh start
```

## Simple Code Example for Insurance Domain

### YAML Pipeline
```yaml
trigger:
  branches:
    include:
      - main

pool:
  name: Self-Hosted

variables:
  - name: environment
    value: production

steps:
  - script: |
      echo "Processing insurance claims..."
      dotnet run --project InsuranceApp
    displayName: 'Run Insurance App'
```

### Sample .NET Code
Create a new .NET project:
```bash
dotnet new console -n InsuranceApp
```

Replace the `Program.cs` file with the following:
```csharp
using System;

namespace InsuranceApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Insurance Claims Processing Started...");
            // Add domain-specific logic here
            Console.WriteLine("Processing Complete.");
        }
    }
}
```

Build and run the application:
```bash
dotnet build
```

## How to Run the Self-Hosted Agent Setup Code

1. **Set Up the Self-Hosted Agent**:
   - Follow the steps in the guide to configure and start the agent.

2. **Run the Pipeline**:
   - Commit the YAML file to your repository.
   - Navigate to Azure Pipelines in your DevOps project.
   - Select the repository and branch containing the YAML file.
   - Choose the self-hosted agent pool and click **Run Pipeline**.

3. **Execute the .NET Code**:
   - Ensure the `InsuranceApp` project is in the repository.
   - The pipeline will automatically build and run the application.

4. **Monitor Execution**:
   - View the pipeline logs to verify the application output.

---

Your self-hosted agent is now ready to run pipelines, and the example demonstrates a simple insurance domain application.