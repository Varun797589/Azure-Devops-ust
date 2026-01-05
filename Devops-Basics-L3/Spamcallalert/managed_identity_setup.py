# Governance and Identity Management with Managed Identities

# Steps to implement Managed Identities:
# 1. Enable system-assigned or user-assigned managed identity for the AKS cluster.
# 2. Assign appropriate Azure roles to the managed identity.
# 3. Use the managed identity to access Azure resources securely.

import subprocess

def enable_managed_identity(resource_group, aks_cluster):
    try:
        subprocess.run([
            "az", "aks", "update",
            "--enable-managed-identity",
            "--resource-group", resource_group,
            "--name", aks_cluster
        ], check=True)
        print("Managed Identity enabled for AKS cluster.")
    except Exception as e:
        print(f"Error enabling Managed Identity: {e}")

def assign_role_to_identity(identity_name, role, scope):
    try:
        subprocess.run([
            "az", "role", "assignment", "create",
            "--assignee", identity_name,
            "--role", role,
            "--scope", scope
        ], check=True)
        print(f"Role '{role}' assigned to identity '{identity_name}' for scope '{scope}'.")
    except Exception as e:
        print(f"Error assigning role: {e}")

# Example usage
if __name__ == "__main__":
    resource_group = "your-resource-group"  # Replace with your Azure resource group
    aks_cluster = "your-aks-cluster"  # Replace with your AKS cluster name
    identity_name = "your-identity-name"  # Replace with your managed identity name
    role = "Contributor"  # Replace with the desired Azure role
    scope = "/subscriptions/your-subscription-id/resourceGroups/your-resource-group"  # Replace with the desired scope

    enable_managed_identity(resource_group, aks_cluster)
    assign_role_to_identity(identity_name, role, scope)