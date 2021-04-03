## Azure CLI Resource Group Creation

```powershell
> az group create --name rg_cloud_save_bg1 --location canadaeast
```

## Azure CLI Template Validation

```powershell
> az deployment group validate --resource-group rg_cloud_save_bg1 --template-file "./app svc banquet.json" --parameters "@app svc banquet.parameters.json"
```

## Azure PowerShell  Template Validation

```powershell
Test-AzResourceGroupDeployment -ResourceGroupName rg_cloud_save_bg1 -TemplateFile "./app svc banquet.json" -TemplateParameterFile "./app svc banquet.parameters.json"
```

## Azure CLI Template Deployment

```
> az deployment group create --name App-Svc-Deployment --resource-group rg_cloud_save_bg1 --template-file "./app svc banquet.json"  --parameters "@app svc banquet.parameters.json"

> az group show --name rg_cloud_save_bg1
```

## Azure CLI Resource Group Deletion

```
> az group delete --name rg_cloud_save_bg1 -y
```