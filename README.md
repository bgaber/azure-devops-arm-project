# Azure DevOps ARM Project
![Alt text](readme_images/February-Cloud-Guru-Challenge-diagram.webp?raw=true "Azure DevOps CICD")

All the ARM Templates in this repository are used to create the infrastructure required in the github.com/bgaber/azure-devops-cicd-project repository.

ARM Templates
-------------
Three ARM templates were required to build the infrastructure required in the github.com/bgaber/azure-devops-cicd-project repository.  These three templates are summarized below:

1. The first ARM template creates a new Azure App Service with the following properties.
  * Integrate with an Azure Virtual Network named “ACGVnet”
  * Integrate Azure Front Door
  * Add a deployment slot named “staging”
  * Custom auto-scaling with 1–3 instances, defaulting to 1.
  * A scale rule which triggers the scale action at 70% CPU usage.
2. The second ARM template creates a Cosmos DB instance with following properties:
  * Enable Geo-Redundancy
  * API type should be Core (SQL)
3. The third ARM template creates a Storage Account with Blob Storage.