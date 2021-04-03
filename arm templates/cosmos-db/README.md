## Azure CLI Resource Group Creation

```powershell
> az group create --name rg_cloud_save_bg1 --location canadaeast
```

## Azure CLI Template Validation

```powershell
> az deployment group validate --resource-group rg_cloud_save_bg1 --template-file "./cosmosdb.json" --parameters "@cosmosdb.parameters.json"
```

## Azure PowerShell  Template Validation

```powershell
Test-AzResourceGroupDeployment -ResourceGroupName rg_cloud_save_bg1 -TemplateFile "./cosmosdb.json" -TemplateParameterFile "./cosmosdb.parameters.json"
```

## Azure CLI Template Deployment

```
> az deployment group create --name Cosmos-DB-Deployment --resource-group rg_cloud_save_bg1 --template-file "./cosmosdb.json"  --parameters "@cosmosdb.parameters.json"

> az group show --name rg_cloud_save_bg1
```

## Azure CLI Resource Group Deletion

```
> az group delete --name rg_cloud_save_bg1 -y
```