# Power BI Dashboard Configuration
# This file outlines the steps to create a Power BI dashboard for live metrics visualization.

1. Connect to Azure Monitor Logs:
   - Open Power BI Desktop.
   - Go to "Get Data" > "Azure" > "Azure Monitor Logs".
   - Enter your Azure credentials and workspace ID.

2. Import Queries:
   - Use the following KQL queries to fetch data:
     - CPU Usage: `AzureMetrics | where MetricName == 'Percentage CPU'`
     - Network Throughput: `AzureMetrics | where MetricName == 'Network In' or MetricName == 'Network Out'`

3. Design Visuals:
   - Create a line chart for CPU usage over time.
   - Create a bar chart for network throughput.

4. Publish Dashboard:
   - Save and publish the dashboard to the Power BI service.
   - Share the dashboard with stakeholders.