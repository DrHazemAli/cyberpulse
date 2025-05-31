
# 🚀 CyberPulse AI Deployment Guide

This guide walks you through setting up CyberPulse AI in your environment.

---

## 🏗️ Step 1: Prerequisites

- Azure CLI installed (`https://learn.microsoft.com/en-us/cli/azure/install-azure-cli`)
- Docker installed
- Python 3.11+
- Git

---

## ☁️ Step 2: Azure Resource Setup

You can deploy resources automatically via the CLI:

```bash
bash deployment/deploy_azure.sh
```

Or manually:
- Create Resource Group: `az group create`
- Create Log Analytics Workspace: `az monitor log-analytics workspace create`
- Create Event Hubs Namespace and Event Hub: `az eventhubs namespace create`, `az eventhubs eventhub create`
- Create Azure ML Workspace: `az ml workspace create`

---

## 🐳 Step 3: Docker Deployment (Local)

1️⃣ Build the Docker image:

```bash
docker build -t cyberpulse-ai .
```

2️⃣ Run the stack (includes Prometheus, Grafana):

```bash
docker-compose up
```

Visit:
- CyberPulse AI GUI: `http://localhost:5000`
- Grafana: `http://localhost:3000` (admin/admin)
- Prometheus: `http://localhost:9090`

---

## 🌐 Step 4: Run REST API

```bash
python api.py
```

Or run with SSL/TLS:

```bash
uvicorn api:app --host 0.0.0.0 --port 443 --ssl-keyfile=path/to/key.pem --ssl-certfile=path/to/cert.pem
```

---

## 🧭 Step 5: Generate Reports

```bash
python generate_report.py
```

Reports will be saved in `/reports/security_report.html`.

---

## ✅ You're ready to go!
