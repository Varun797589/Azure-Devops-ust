from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

SUBSCRIPTION_ID = "ab9b448f-07ad-4039-b26d-e74b90b60272"
RESOURCE_GROUP = "MyResourceGroup"
VM_NAME = "MyVM"

credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, SUBSCRIPTION_ID)

compute_client.virtual_machines.begin_start(RESOURCE_GROUP, VM_NAME)
print("VM started")
