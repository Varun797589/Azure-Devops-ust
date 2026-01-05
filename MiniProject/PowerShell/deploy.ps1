# PowerShell Script for Azure VM and Network Deployment

# Login to Azure
Write-Host "Logging in to Azure..."
Connect-AzAccount

# Variables
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
Add-AzVirtualNetworkSubnetConfig -Name $subnetName -AddressPrefix "10.0.1.0/24" -VirtualNetwork $vnet
$vnet | Set-AzVirtualNetwork

# Create Network Interface
Write-Host "Creating Network Interface..."
$subnet = $vnet.Subnets[0]
$nic = New-AzNetworkInterface -Name $nicName -ResourceGroupName $resourceGroupName -Location $location -SubnetId $subnet.Id

# Create Virtual Machine
Write-Host "Creating Virtual Machine..."
$vmConfig = New-AzVMConfig -VMName $vmName -VMSize "Standard_DS1_v2"
$cred = Get-Credential -Message "Enter VM admin credentials"
$vmConfig = Set-AzVMOperatingSystem -VM $vmConfig -Linux -ComputerName $vmName -Credential $cred -DisablePasswordAuthentication
$vmConfig = Add-AzVMNetworkInterface -VM $vmConfig -Id $nic.Id
$vmConfig = Set-AzVMSourceImage -VM $vmConfig -PublisherName "Canonical" -Offer "UbuntuServer" -Skus "18.04-LTS" -Version "latest"
New-AzVM -ResourceGroupName $resourceGroupName -Location $location -VM $vmConfig

Write-Host "Deployment Complete!"