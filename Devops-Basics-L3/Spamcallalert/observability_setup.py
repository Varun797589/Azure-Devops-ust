# Observability setup for Azure Monitor, Grafana, and Power BI

# Steps to integrate observability:
# 1. Enable Azure Monitor for the AKS cluster.
# 2. Set up Grafana to visualize metrics from Azure Monitor.
# 3. Connect Power BI to Azure Monitor logs for advanced reporting.

import subprocess

def enable_azure_monitor(resource_group, aks_cluster):
    try:
        subprocess.run([
            "az", "aks", "enable-addons",
            "--addons", "monitoring",
            "--resource-group", resource_group,
            "--name", aks_cluster
        ], check=True)
        print("Azure Monitor enabled for AKS cluster.")
    except Exception as e:
        print(f"Error enabling Azure Monitor: {e}")

def setup_grafana():
    print("Follow these steps to set up Grafana:")
    print("1. Deploy Grafana in your AKS cluster.")
    print("2. Configure Grafana to pull metrics from Azure Monitor.")
    print("3. Use Azure Monitor plugin for Grafana.")

def connect_power_bi():
    print("Follow these steps to connect Power BI:")
    print("1. Export Azure Monitor logs to a Log Analytics workspace.")
    print("2. Use Power BI to connect to the Log Analytics workspace.")
    print("3. Create dashboards and reports in Power BI.")

# Example usage
if __name__ == "__main__":
    resource_group = "your-resource-group"  # Replace with your Azure resource group
    aks_cluster = "your-aks-cluster"  # Replace with your AKS cluster name

    enable_azure_monitor(resource_group, aks_cluster)
    setup_grafana()
    connect_power_bi()