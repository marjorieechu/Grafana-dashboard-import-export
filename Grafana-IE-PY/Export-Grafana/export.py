import os
import requests
import time

grafana_url = "http://localhost:3000"  # Change to your Grafana URL
grafana_api_key = os.getenv("GRAFANA_API_KEY")   # Fetch from environment variable # Replace with your Grafana API key
export_folder = "Dashboard"
polling_interval = 86400  # Export every 24 hours

# Ensure the export folder exists
os.makedirs(export_folder, exist_ok=True)

def get_dashboards():
    # Fetch all dashboards from Grafana
    url = f"{grafana_url}/api/search?query=&type=dash-db"
    headers = {"Authorization": f"Bearer {grafana_api_key}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def export_dashboard(uid):
    # Export a specific dashboard by UID
    url = f"{grafana_url}/api/dashboards/uid/{uid}"
    headers = {"Authorization": f"Bearer {grafana_api_key}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    filename = os.path.join(export_folder, f"{uid}.json")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"Exported: {filename}")

def main():
    while True:
        try:
            dashboards = get_dashboards()  # Fetch all dashboards
            for dashboard in dashboards:
                export_dashboard(dashboard['uid'])  # Export each dashboard
        except Exception as e:
            print(f"Error: {e}")
        print(f"Waiting {polling_interval} seconds before the next export...")
        time.sleep(polling_interval)

if __name__ == "__main__":
    main()





# import os
# import requests
# import time
# import hvac  # Install with: pip install hvac

# # Initialize Vault client
# vault_client = hvac.Client(url="http://127.0.0.1:8200", token="your-vault-token")

# # Fetch secrets from Vault
# secret_path = "secret/data/grafana"  # Adjust based on your Vault configuration
# response = vault_client.secrets.kv.read_secret_version(path=secret_path)
# secrets = response["data"]["data"]

# grafana_url = secrets.get("grafana_url", "http://localhost:3000")
# grafana_api_key = secrets.get("grafana_api_key", "")

# export_folder = "Dashboard"
# polling_interval = 86400  # Export every 24 hours

# # Ensure the export folder exists
# os.makedirs(export_folder, exist_ok=True)

# def get_dashboards():
#     url = f"{grafana_url}/api/search?query=&type=dash-db"
#     headers = {"Authorization": f"Bearer {grafana_api_key}"}
#     response = requests.get(url, headers=headers)
#     response.raise_for_status()
#     return response.json()

# def export_dashboard(uid):
#     url = f"{grafana_url}/api/dashboards/uid/{uid}"
#     headers = {"Authorization": f"Bearer {grafana_api_key}"}
#     response = requests.get(url, headers=headers)
#     response.raise_for_status()
    
#     filename = os.path.join(export_folder, f"{uid}.json")
#     with open(filename, "w", encoding="utf-8") as f:
#         f.write(response.text)
#     print(f"Exported: {filename}")

# def main():
#     while True:
#         try:
#             dashboards = get_dashboards()
#             for dashboard in dashboards:
#                 export_dashboard(dashboard['uid'])
#         except Exception as e:
#             print(f"Error: {e}")
#         print(f"Waiting {polling_interval} seconds before the next export...")
#         time.sleep(polling_interval)

# if __name__ == "__main__":
#     main()
