
# 🚀 CyberPulse AI

**CyberPulse AI** is a next-generation, AI-powered security monitoring system that **detects anomalies**, **analyzes threats**, and **provides real-time insights** to protect your digital assets.  
Designed for **production use** with **cloud-native architecture**, **Docker support**, **CI/CD pipelines**, and **state-of-the-art AI models**.

![CyberPulse AI](https://github.com/DrHazemAli/cyberpulse/blob/main/assets/inforgraphic.png)


## 🌐 What is CyberPulse AI?

CyberPulse AI watches over your network, systems, and data like a heartbeat monitor for your digital world.  
It uses advanced AI models, cloud services, and a user-friendly interface to detect security threats **before they strike**.

---

## 🏗️ Architecture

```
+------------------------------------+
|          User & Data Sources       |
| (AD, Firewalls, NSGs, Custom Logs) |
+------------------------------------+
                |
                v
+------------------------------------+
|      Azure Event Hubs (Streaming)   |
+------------------------------------+
                |
                v
+------------------------------------+
|    AI Anomaly Detection Models     |
| (Isolation Forest, LOF, OCSVM)     |
| Deployed via Azure ML API          |
+------------------------------------+
                |
                v
+------------------------------------+
|     CyberPulse AI Backend (API)    |
|   REST API | Flask GUI | CLI       |
+------------------------------------+
                |
                v
+------------------------------------+
| Azure Sentinel + Log Analytics     |
| Prometheus + Grafana Dashboards    |
+------------------------------------+
```

---

## 🚀 Features

✅ **AI-Powered Threat Detection**: Isolation Forest, Local Outlier Factor, One-Class SVM.  
✅ **Azure-Native**: Sentinel, Event Hubs, ML, Key Vault (configurable).  
✅ **Real-Time Dashboards**: Prometheus + Grafana, pre-configured templates.  
✅ **REST API**: Expose services via FastAPI with SSL/TLS support.  
✅ **CLI Tools**: Automate Azure setup, dataset downloads, and more.  
✅ **Docker-Ready**: Run the entire stack in containers.  
✅ **CI/CD Pipelines**: GitHub Actions workflows included.  
✅ **Deployment Guide**: Step-by-step instructions for setup.  
✅ **Extensible Architecture**: Add models, data sources, and integrations.

---

## 📂 Repository Structure

```
/CyberPulse-AI
|-- azure-functions/          # Event Hub consumer code
|-- azure-ml/                 # ML training & scoring
|-- cli.py                    # CLI interface
|-- api.py                    # REST API (FastAPI)
|-- gui/                      # Flask GUI
|-- datasets/                 # Sample data
|-- reports/                  # Generated reports
|-- monitoring/               # Prometheus & Grafana configs
|-- deployment/               # Deployment scripts & guides
|-- Dockerfile                # Docker container setup
|-- docker-compose.yml        # Orchestrated deployment
|-- requirements.txt          # Python dependencies
|-- .github/workflows/        # CI/CD pipelines
|-- README.md                 # This file!
```

---

## 🛡️ Security & Best Practices

- **Secrets Management**: Use `.env` and `Azure Key Vault` for credentials.  
- **RBAC & Access Control**: Integrate with Azure AD for role-based permissions.  
- **SSL/TLS**: Secure API endpoints with HTTPS.  
- **Monitoring**: Real-time metrics with Prometheus & Grafana.  
- **Alerting**: Azure Sentinel rules + custom queries.

---

## 🛠️ Deployment Steps

1️⃣ **Azure Setup**:

```bash
bash deployment/deploy_azure.sh
```

2️⃣ **Docker Build & Run**:

```bash
docker build -t cyberpulse-ai .
docker-compose up
```

3️⃣ **API & Reports**:

```bash
python api.py
python generate_report.py
```

4️⃣ **Grafana**: Import `monitoring/dashboards/cyberpulse_dashboard.json`.

---

## 📊 Dashboards

| Service    | URL                    | Default Credentials |
|------------|------------------------|---------------------|
| Flask GUI  | http://localhost:5000  | -                   |
| Grafana    | http://localhost:3000  | admin / admin       |
| Prometheus | http://localhost:9090  | -                   |

---

## 📈 Extending CyberPulse AI

- Add ML models in `azure-ml/train_model.py`.
- Configure API endpoints in `api.py`.
- Create new CLI commands in `cli.py`.
- Expand datasets in `datasets/`.
- Define new dashboards in `monitoring/dashboards/`.

---

## 🎓 License & Credits

© Hazem Ali | 2025
GitHub: [DrHazemAli](https://github.com/DrHazemAli)
Licensed under the MIT License.  

---

🚀 Stay vigilant. Stay secure. Welcome to CyberPulse AI.

