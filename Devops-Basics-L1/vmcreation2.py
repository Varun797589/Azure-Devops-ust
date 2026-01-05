from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

# ===== UPDATE THESE VALUES =====
SUBSCRIPTION_ID = "ab9b448f-07ad-4039-b26d-e74b90b60272"
RESOURCE_GROUP = "MyResourceGroup"
VM_NAME = "MyVM"

# ===============================

# Authenticate using Azure CLI login
credential = DefaultAzureCredential()

# Compute client
compute_client = ComputeManagementClient(
    credential,
    SUBSCRIPTION_ID
)

print(f"Deallocating VM: {VM_NAME} ...")

# 🔥 THIS STOPS VM + STOPS BILLING
poller = compute_client.virtual_machines.begin_deallocate(
    RESOURCE_GROUP,
    VM_NAME
)

# Wait until operation completes
poller.wait()

print("✅ VM successfully deallocated (no billing now)")
