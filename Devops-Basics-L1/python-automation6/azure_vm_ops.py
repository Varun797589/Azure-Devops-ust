
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

SUBSCRIPTION_ID = "ab9b448f-07ad-4039-b26d-e74b90b60272"
RESOURCE_GROUP = "MyResourceGroup"
VM_NAME = "MyVM"

credential = DefaultAzureCredential()
client = ComputeManagementClient(credential, SUBSCRIPTION_ID)

print("Deallocating Azure VM...")
client.virtual_machines.begin_deallocate(
    RESOURCE_GROUP,
    VM_NAME
).wait()

print("VM deallocated (billing stopped)")
print("Starting Azure VM...")

