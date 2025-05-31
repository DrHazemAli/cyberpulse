
import json
import logging
import os
import requests
from azure.identity import DefaultAzureCredential
import azure.functions as func
import yaml

# Load configuration
with open(os.path.join(os.path.dirname(__file__), '../config/config.yaml'), 'r') as f:
    config = yaml.safe_load(f)

ML_ENDPOINT = os.getenv('ML_ENDPOINT', config['ml_endpoint'])
ML_KEY = os.getenv('ML_KEY', config['ml_key'])
SENTINEL_WORKSPACE_ID = os.getenv('SENTINEL_WORKSPACE_ID', config['sentinel_workspace_id'])
SENTINEL_SHARED_KEY = os.getenv('SENTINEL_SHARED_KEY', config['sentinel_shared_key'])

def main(event: func.EventHubEvent):
    try:
        event_body = event.get_body().decode('utf-8')
        data = json.loads(event_body)

        payload = {
            "input_data": {
                "columns": ["user_id", "ip", "timestamp", "location"],
                "values": [[data.get("user_id"), data.get("ip"), data.get("timestamp"), data.get("location")]]
            }
        }

        headers = {"Authorization": f"Bearer {ML_KEY}", "Content-Type": "application/json"}
        response = requests.post(ML_ENDPOINT, json=payload, headers=headers, timeout=10)

        if response.status_code == 200:
            result = response.json()
            anomaly_score = result['result'][0]['score']
            risk_level = result['result'][0]['risk_level']
            logging.info(f"Anomaly Detected: Score={anomaly_score}, Risk={risk_level}")

            # Optional: Send to Sentinel (add Data Collector API call here)
            # send_to_sentinel(data, anomaly_score, risk_level)

        else:
            logging.error(f"ML API Error: {response.status_code} - {response.text}")

    except Exception as e:
        logging.error(f"Error processing EventHub message: {str(e)}")
