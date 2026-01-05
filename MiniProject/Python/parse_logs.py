"""
Python Pipeline to Parse Azure Logs and Classify Issues
"""
import json
import logging
from azure.identity import DefaultAzureCredential
from azure.monitor.query import LogsQueryClient

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Azure Logs Query Client
credential = DefaultAzureCredential()
client = LogsQueryClient(credential)

# Define the query
query = """
AzureActivity
| where Level == "Error"
| project TimeGenerated, ResourceGroup, OperationName, Status, EventName, Properties
"""

# Define the workspace ID
workspace_id = "<YOUR_WORKSPACE_ID>"

# Function to classify issues
def classify_issue(log):
    if "unauthorized" in log.get("Properties", "").lower():
        return "Authorization Error"
    elif "timeout" in log.get("Properties", "").lower():
        return "Timeout Error"
    else:
        return "General Error"

# Query logs
logging.info("Querying Azure logs...")
response = client.query_workspace(workspace_id, query, timespan="PT1H")

if response.status == "Success":
    logging.info("Logs retrieved successfully.")
    for log in response.tables[0].rows:
        log_data = dict(zip(response.tables[0].columns, log))
        issue_type = classify_issue(log_data)
        logging.info(f"Time: {log_data['TimeGenerated']}, Issue: {issue_type}, Details: {log_data}")
else:
    logging.error(f"Failed to retrieve logs: {response.error}")