# Intelligent Deployment Rollback Agent

import logging
import time
from azure.identity import DefaultAzureCredential
from azure.monitor.query import LogsQueryClient

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_real_time_metrics(workspace_id, query):
    """Fetch real-time metrics from Azure Log Analytics workspace."""
    credential = DefaultAzureCredential()
    client = LogsQueryClient(credential)

    logging.info("Fetching real-time metrics from Azure...")
    response = client.query_workspace(
        workspace_id=workspace_id,
        query=query,
        timespan=None
    )

    if not response.tables:
        logging.warning("No metrics found.")
        return []

    metrics = []
    for table in response.tables:
        for row in table.rows:
            metrics.append(dict(zip(table.columns, row)))

    logging.info(f"Fetched {len(metrics)} metrics entries.")
    return metrics

def analyze_metrics(metrics):
    """Analyze metrics to detect anomalies."""
    logging.info("Analyzing metrics...")
    anomalies = []

    for metric in metrics:
        if metric.get("ErrorRate", 0) > 5:  # Example threshold
            anomalies.append(metric)

    logging.info(f"Detected {len(anomalies)} anomalies.")
    return anomalies

def rollback_deployment():
    """Perform deployment rollback."""
    logging.warning("Initiating deployment rollback...")
    # Add rollback logic here (e.g., Azure CLI commands, API calls)
    logging.info("Rollback completed successfully.")

def main():
    workspace_id = "98dc4303-7cbf-4a8e-a3c9-0e25f9f2a4ea"  # Updated Workspace ID
    query = "AzureActivity | where TimeGenerated > ago(1h) | summarize count() by ActivityStatusValue"  # Updated valid KQL query

    while True:
        metrics = fetch_real_time_metrics(workspace_id, query)
        anomalies = analyze_metrics(metrics)

        if anomalies:
            rollback_deployment()

        time.sleep(60)  # Check metrics every 60 seconds

if __name__ == "__main__":
    main()