How This Script Works:
Import Dashboard:

The import_dashboard() function is used to import a single dashboard.

It reads the JSON file (e.g., uid1.json), sends a POST request to Grafana’s API endpoint (/api/dashboards/db), and creates or updates the dashboard.

It checks the API response for a "status": "success" message to confirm that the import was successful.

Main Loop:

The script looks for all .json files in the Dashboard/ folder (for file in "$DASHBOARD_FOLDER"/*.json).

It imports each dashboard file.

It waits for 24 hours (using sleep $POLLING_INTERVAL) before running again.

Setup:
Replace your_grafana_api_key with your actual Grafana API key.

Ensure that the Dashboard/ folder contains the JSON files you want to import.

Save this script as import_dashboards.sh.

Make it executable: chmod +x import_dashboards.sh
Run the script: ./import_dashboards.sh