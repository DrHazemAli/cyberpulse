
# Copyright © 2025, Hazem Ali
# GitHub: DrHazemAli
import argparse
import subprocess
import os

def init_azure():
    print("Initializing Azure Resources...")
    subprocess.run(["az", "login"], check=True)
    subprocess.run(["az", "group", "create", "--name", "CyberPulseRG", "--location", "eastus"], check=True)
    subprocess.run(["az", "monitor", "log-analytics", "workspace", "create", "--resource-group", "CyberPulseRG", "--workspace-name", "CyberPulseWorkspace"], check=True)
    subprocess.run(["az", "eventhubs", "namespace", "create", "--name", "CyberPulseEHNamespace", "--resource-group", "CyberPulseRG", "--location", "eastus"], check=True)
    subprocess.run(["az", "eventhubs", "eventhub", "create", "--name", "CyberPulseEvents", "--namespace-name", "CyberPulseEHNamespace", "--resource-group", "CyberPulseRG"], check=True)
    print("Azure Resources Created.")

def download_dataset():
    print("Downloading Sample Dataset...")
    url = "https://raw.githubusercontent.com/Azure/Azure-Sentinel/master/Sample%20Data/SigninLogs.json"
    os.makedirs("datasets", exist_ok=True)
    subprocess.run(["curl", "-L", url, "-o", "datasets/SigninLogs.json"], check=True)
    print("Dataset Downloaded to ./datasets")

def run_gui():
    print("Starting CyberPulse AI GUI...")
    subprocess.run(["python", "gui/app.py"], check=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CyberPulse AI Command Line Interface")
    parser.add_argument("command", choices=["init-azure", "download-dataset", "run-gui"], help="Command to execute")
    args = parser.parse_args()

    if args.command == "init-azure":
        init_azure()
    elif args.command == "download-dataset":
        download_dataset()
    elif args.command == "run-gui":
        run_gui()
