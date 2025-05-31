
#!/bin/bash

# Deploy CyberPulse AI resources in Azure
echo "Logging into Azure..."
az login

echo "Creating Resource Group..."
az group create --name CyberPulseRG --location eastus

echo "Creating Log Analytics Workspace..."
az monitor log-analytics workspace create --resource-group CyberPulseRG --workspace-name CyberPulseWorkspace

echo "Creating Event Hub Namespace and Hub..."
az eventhubs namespace create --name CyberPulseEHNamespace --resource-group CyberPulseRG --location eastus
az eventhubs eventhub create --name CyberPulseEvents --namespace-name CyberPulseEHNamespace --resource-group CyberPulseRG

echo "Deploying Azure ML Workspace..."
az ml workspace create --name CyberPulseMLWorkspace --resource-group CyberPulseRG --location eastus

echo "Azure Deployment Complete."
