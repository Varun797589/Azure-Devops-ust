# Python script to parse Azure logs and classify issues

import json
import logging
from azure.identity import DefaultAzureCredential
from azure.monitor.query import LogsQueryClient

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_azure_logs(workspace_id, query):
    """Fetch logs from Azure Log Analytics workspace."""
    credential = DefaultAzureCredential()
    client = LogsQueryClient(credential)

    logging.info("Fetching logs from Azure...")
    response = client.query_workspace(
        workspace_id=workspace_id,
        query=query,
        timespan=None
    )

    if not response.tables:
        logging.warning("No logs found.")
        return []

    logs = []
    for table in response.tables:
        for row in table.rows:
            logs.append(dict(zip(table.columns, row)))

    logging.info(f"Fetched {len(logs)} log entries.")
    return logs

def classify_logs(logs):
    """Classify logs into categories."""
    logging.info("Classifying logs...")
    classified_logs = {
        "errors": [],
        "warnings": [],
        "info": []
    }

    for log in logs:
        if "error" in log.get("Level", "").lower():
            classified_logs["errors"].append(log)
        elif "warning" in log.get("Level", "").lower():
            classified_logs["warnings"].append(log)
        else:
            classified_logs["info"].append(log)

    logging.info("Classification complete.")
    return classified_logs

def main():
    workspace_id = "<Your-Workspace-ID>"  # Replace with your Azure Log Analytics Workspace ID
    query = "<Your-KQL-Query>"  # Replace with your KQL query

    logs = fetch_azure_logs(workspace_id, query)
    classified_logs = classify_logs(logs)

    # Save classified logs to JSON files
    with open("errors.json", "w") as error_file:
        json.dump(classified_logs["errors"], error_file, indent=4)

    with open("warnings.json", "w") as warning_file:
        json.dump(classified_logs["warnings"], warning_file, indent=4)

    with open("info.json", "w") as info_file:
        json.dump(classified_logs["info"], info_file, indent=4)

    logging.info("Logs saved to JSON files.")

if __name__ == "__main__":
    main()