import requests
import json
import os
import time
import schedule

# Grafana Configuration
GRAFANA_HOST = "http://localhost:3000"  # Change to your Grafana instance URL
API_TOKEN = "your_api_token_here"  # Replace with your API token
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}
EXPORT_DIR = "grafana_dashboards"  # Directory to store exported dashboards

# Ensure export directory exists
if not os.path.exists(EXPORT_DIR):
    os.makedirs(EXPORT_DIR)

def list_dashboards():
    """ Fetches the list of all dashboards from Grafana """
    url = f"{GRAFANA_HOST}/api/search?query="
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        dashboards = response.json()
        return [d["uid"] for d in dashboards]
    else:
        print(f"❌ Failed to fetch dashboards: {response.text}")
        return []

def export_dashboard(dashboard_uid):
    """ Exports a Grafana dashboard and saves it as a JSON file """
    url = f"{GRAFANA_HOST}/api/dashboards/uid/{dashboard_uid}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        dashboard_data = response.json()
        file_path = os.path.join(EXPORT_DIR, f"{dashboard_uid}.json")
        
        with open(file_path, "w") as f:
            json.dump(dashboard_data, f, indent=4)

        print(f"✅ Exported: {dashboard_uid} -> {file_path}")
    else:
        print(f"❌ Failed to export {dashboard_uid}: {response.text}")

def import_dashboard(file_path):
    """ Imports a Grafana dashboard from a JSON file """
    with open(file_path, "r") as f:
        dashboard_data = json.load(f)

    dashboard_data["overwrite"] = True  # Overwrite existing dashboards
    url = f"{GRAFANA_HOST}/api/dashboards/db"
    response = requests.post(url, headers=HEADERS, json=dashboard_data)

    if response.status_code == 200:
        print(f"✅ Imported: {file_path}")
    else:
        print(f"❌ Failed to import {file_path}: {response.text}")

def export_all_dashboards():
    """ Exports all dashboards periodically """
    dashboard_uids = list_dashboards()
    if dashboard_uids:
        for uid in dashboard_uids:
            export_dashboard(uid)

def import_all_dashboards():
    """ Imports all dashboards from stored JSON files """
    for file in os.listdir(EXPORT_DIR):
        if file.endswith(".json"):
            file_path = os.path.join(EXPORT_DIR, file)
            import_dashboard(file_path)

# Schedule periodic execution
schedule.every(10).minutes.do(export_all_dashboards)  # Adjust the time interval as needed

print("🚀 Grafana Dashboard Manager Running... Press Ctrl+C to Stop")

# Run indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)
o