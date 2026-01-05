
'''
provider "azurerm" {
     subscription_id ="your-subscription-id" # variable value in terraform 
}
'''


provider = {
    "subscription_id":"your-subscription-id" # key value python
    # subscription_id="your-subscription-id" # variable value in terraform 
}

'''
keyword           resourename        object 
  ||            ||                  ||
resource "azurerm_resource_group" "example" {
    
    name     = "example-resources"
    location = "West Europe"
    }

'''

resource = {
       "name"     : "example-resources",
      "location"    :  "West Europe"
}

resource1 = {
         "addressspace": resource["location"]
}

print(resource1)

resource = {
    
}