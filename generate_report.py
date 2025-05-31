
# Copyright © 2025, Hazem Ali
# GitHub: DrHazemAli
import pandas as pd
import json
import os
from datetime import datetime

def generate_report(data_file='datasets/SigninLogs.json', output_file='reports/security_report.html'):
    os.makedirs('reports', exist_ok=True)
    with open(data_file, 'r') as f:
        data = [json.loads(line) for line in f]

    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['TimeGenerated'], errors='coerce')
    report = df.groupby('Location').size().reset_index(name='EventCount')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html_content = f"""
    <html><head><title>CyberPulse AI Security Report</title></head><body>
    <h1>CyberPulse AI Security Report</h1>
    <p>Generated: {timestamp}</p>
    {report.to_html(index=False)}
    </body></html>
    """

    with open(output_file, 'w') as f:
        f.write(html_content)

    print(f"Report generated: {output_file}")

if __name__ == '__main__':
    generate_report()
