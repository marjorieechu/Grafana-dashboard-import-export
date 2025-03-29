import os
import requests

grafana_url = "http://localhost:3000"  # Change to your Grafana URL
grafana_api_key = "your_grafana_api_key"  # Replace with your Grafana API key
dashboard_folder = "Dashboard"

# Ensure the folder exists
if not os.path.exists(dashboard_folder):
    print(f"Error: Folder '{dashboard_folder}' does not exist!")
    exit(1)

def import_dashboard(file_path):
    # Read the dashboard JSON file
    with open(file_path, "r", encoding="utf-8") as f:
        dashboard_json = f.read()

    # Create or update the dashboard in Grafana
    response = requests.post(
        f"{grafana_url}/api/dashboards/db",
        headers={"Authorization": f"Bearer {grafana_api_key}", "Content-Type": "application/json"},
        data=dashboard_json
    )

    if response.status_code == 200:
        print(f"Successfully imported: {file_path}")
    else:
        print(f"Failed to import: {file_path}. Error: {response.text}")

def main():
    # Get all JSON files in the dashboard folder
    for file in os.listdir(dashboard_folder):
        if file.endswith(".json"):
            file_path = os.path.join(dashboard_folder, file)
            import_dashboard(file_path)

if __name__ == "__main__":
    main()
