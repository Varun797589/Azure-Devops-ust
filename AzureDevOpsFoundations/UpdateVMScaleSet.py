# Automate VM Scale Set Updates using Python

#What problem does it solve?
#Normally, to scale a VM Scale Set you would:
#Open Azure Portal
#Go to VMSS
#Manually change instance count


import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

# Azure credentials and subscription
subscription_id = "ab9b448f-07ad-4039-b26d-e74b90b60272"
resource_group_name = "MyResourceGroup"
vmss_name = "MyVMSS"

# Authenticate with Azure
credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id)

# Update VM Scale Set
print("Updating VM Scale Set...")

update_params = {
    "location": "East US 2",  # Set location to comply with policy
    "sku": {
        "capacity": 5  # Update the instance count
    }
}

compute_client.virtual_machine_scale_sets.begin_update(
    resource_group_name=resource_group_name,
    vm_scale_set_name=vmss_name,
    parameters=update_params
).result()

print("VM Scale Set updated successfully!")