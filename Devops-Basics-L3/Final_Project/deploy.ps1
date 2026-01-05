# PowerShell script for Azure VM and Network Deployment

# Login to Azure
Write-Host "Logging in to Azure..."
Connect-AzAccount

# Set variables
$resourceGroupName = "example-resources"
$location = "East US"
$vnetName = "example-vnet"
$subnetName = "example-subnet"
$nicName = "example-nic"
$vmName = "example-vm"

# Create Resource Group
Write-Host "Creating Resource Group..."
New-AzResourceGroup -Name $resourceGroupName -Location $location

# Create Virtual Network
Write-Host "Creating Virtual Network..."
$vnet = New-AzVirtualNetwork -ResourceGroupName $resourceGroupName -Location $location -Name $vnetName -AddressPrefix "10.0.0.0/16"

# Create Subnet
Write-Host "Creating Subnet..."
Add-AzVirtualNetworkSubnetConfig -Name $subnetName -VirtualNetwork $vnet -AddressPrefix "10.0.1.0/24"
$vnet | Set-AzVirtualNetwork

# Create Network Interface
Write-Host "Creating Network Interface..."
$subnet = $vnet.Subnets[0]
$nic = New-AzNetworkInterface -Name $nicName -ResourceGroupName $resourceGroupName -Location $location -SubnetId $subnet.Id

# Create Virtual Machine
Write-Host "Creating Virtual Machine..."
$securePassword = ConvertTo-SecureString "P@ssw0rd1234" -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential ("adminuser", $securePassword)
New-AzVM -ResourceGroupName $resourceGroupName -Location $location -VMName $vmName -Credential $credential -ImageName "Win2019Datacenter" -Size "Standard_DS1_v2" -NetworkInterfaceId $nic.Id

Write-Host "Deployment completed successfully!"