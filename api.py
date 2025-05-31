
# Copyright © 2025, Hazem Ali
# GitHub: DrHazemAli
from fastapi import FastAPI
import subprocess

app = FastAPI(title="CyberPulse AI API", version="1.0")

@app.get("/status")
def get_status():
    return {"status": "CyberPulse AI is running smoothly!"}

@app.get("/generate-report")
def generate_report():
    subprocess.run(["python", "generate_report.py"])
    return {"message": "Report generated!"}

@app.get("/download-dataset")
def download_dataset():
    subprocess.run(["python", "cli.py", "download-dataset"])
    return {"message": "Dataset downloaded!"}

@app.get("/init-azure")
def init_azure():
    subprocess.run(["python", "cli.py", "init-azure"])
    return {"message": "Azure resources initialized!"}

