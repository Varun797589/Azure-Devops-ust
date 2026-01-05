#1️⃣ Creates a Resource Group
#2️⃣ Creates a Virtual Machine (Ubuntu Linux)
#3️⃣ Opens port 80 for web traffic
#All using commands, not UI.



# PowerShell Script for Azure VM Deployment

# Variables
$resourceGroupName = "MyResourceGroup"
$location = "EastUS"
$vmName = "MyVM"
$vmSize = "Standard_DS1_v2"
$imagePublisher = ""
$imageOffer = "Ubuntu2204"
$imageSku = ""
$adminUsername = "azureuser"
$adminPassword = "<YourPasswordHere>" # Replace with a secure password

# Create Resource Group
Write-Host "Creating Resource Group..."
az group create --name $resourceGroupName --location $location

# Create Virtual Machine
Write-Host "Creating Virtual Machine..."
az vm create `
  --resource-group $resourceGroupName `
  --name $vmName `
  --image "Ubuntu2204" `
  --size $vmSize `
  --admin-username $adminUsername `
  --admin-password $adminPassword

# Open Port 80 for Web Traffic
Write-Host "Opening Port 80..."
az vm open-port --resource-group $resourceGroupName --name $vmName --port 80

Write-Host "Deployment Complete!"