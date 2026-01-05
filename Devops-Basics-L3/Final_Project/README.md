# Deployment Rollback Agent

## Overview
The Deployment Rollback Agent is a Python-based script designed to monitor Azure Log Analytics metrics in real-time, detect anomalies, and trigger rollback actions when necessary. It uses the Azure SDK for Python to interact with Azure services.

## Prerequisites
Before running the script, ensure the following:

1. **Azure Subscription**:
   - You must have an active Azure subscription.

2. **Log Analytics Workspace**:
   - A Log Analytics workspace must be created. The Workspace ID should be updated in the script.

3. **Azure CLI**:
   - Install and log in to Azure CLI:
     ```bash
     az login
     ```

4. **Python Environment**:
   - Python 3.13 or higher is required.
   - Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

5. **Azure SDK Authentication**:
   - Ensure the script can authenticate with Azure using `DefaultAzureCredential`.

## Configuration

1. **Update Workspace ID**:
   - Open the `deployment_rollback_agent.py` file and update the `workspace_id` variable with your Log Analytics Workspace ID.

2. **Update KQL Query**:
   - Replace the `query` variable with a valid KQL query. For example:
     ```python
     query = "AzureActivity | where TimeGenerated > ago(1h) | summarize count() by ActivityStatusValue"
     ```

## Execution

1. **Activate Virtual Environment**:
   - If using a virtual environment, activate it:
     ```bash
     source .venv/bin/activate
     ```

2. **Run the Script**:
   - Execute the script:
     ```bash
     python deployment_rollback_agent.py
     ```

3. **Monitor Logs**:
   - The script logs its actions to the console. Look for messages indicating metrics fetched, anomalies detected, and rollback actions triggered.

## Troubleshooting

1. **No Data in Workspace**:
   - Ensure Azure resources are configured to send logs to the Log Analytics workspace.

2. **Authentication Issues**:
   - Verify Azure CLI is logged in and has the necessary permissions.

3. **KQL Query Errors**:
   - Test the query in the Azure Portal under the "Logs" section of the workspace.

## Example Output

- **Metrics Fetched**:
  ```
  2026-01-02 18:03:48,364 - INFO - Fetched 10 metrics entries.
  ```

- **Anomalies Detected**:
  ```
  2026-01-02 18:03:50,123 - INFO - Detected 2 anomalies.
  ```

- **Rollback Triggered**:
  ```
  2026-01-02 18:03:51,456 - WARNING - Initiating deployment rollback...
  ```

## License
This project is licensed under the MIT License.