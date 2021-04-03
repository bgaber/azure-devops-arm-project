## Azure CLI Resource Group Creation

```powershell
> az group create --name rg_cloud_save_bg1 --location canadacentral
```

## Azure CLI Template Validation

```powershell
> az deployment group validate --resource-group rg_cloud_save_bg1 --template-file "./function.json" --parameters "@function.parameters.json"
```

## Azure PowerShell  Template Validation

```powershell
Test-AzResourceGroupDeployment -ResourceGroupName rg_cloud_save_bg1 -TemplateFile "./function.json" -TemplateParameterFile "./function.parameters.json"
```

## Azure CLI Template Deployment

```
> az deployment group create --name Function-App-Deployment --resource-group rg_cloud_save_bg1 --template-file "./function.json"  --parameters "@function.parameters.json"

> az group show --name rg_cloud_save_bg1
```

## Azure CLI Resource Group Deletion

```
> az group delete --name rg_cloud_save_bg1 -y
```