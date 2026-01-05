"""
Intelligent Decision Agent for Deployment Rollback
"""
import logging
from azure.monitor.query import LogsQueryClient
from azure.identity import DefaultAzureCredential

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Azure Logs Query Client
credential = DefaultAzureCredential()
client = LogsQueryClient(credential)

# Define the query to fetch critical metrics
query = """
AzureMetrics
| where MetricName in ('Percentage CPU', 'Network In', 'Network Out')
| summarize AvgValue = avg(MetricValue) by MetricName
"""

# Define the workspace ID
workspace_id = "<YOUR_WORKSPACE_ID>"

# Thresholds for rollback
THRESHOLDS = {
    "Percentage CPU": 80,
    "Network In": 1000,
    "Network Out": 1000
}

# Function to evaluate metrics and decide rollback
def evaluate_metrics(metrics):
    for metric in metrics:
        name = metric["MetricName"]
        value = metric["AvgValue"]
        if value > THRESHOLDS.get(name, float('inf')):
            logging.warning(f"Metric {name} exceeded threshold with value {value}. Initiating rollback.")
            return True
    return False

# Query logs
logging.info("Querying Azure metrics...")
response = client.query_workspace(workspace_id, query, timespan="PT1H")

if response.status == "Success":
    logging.info("Metrics retrieved successfully.")
    metrics = [dict(zip(response.tables[0].columns, row)) for row in response.tables[0].rows]
    if evaluate_metrics(metrics):
        logging.info("Rollback initiated.")
        # Add rollback logic here
    else:
        logging.info("System operating within normal parameters.")
else:
    logging.error(f"Failed to retrieve metrics: {response.error}")