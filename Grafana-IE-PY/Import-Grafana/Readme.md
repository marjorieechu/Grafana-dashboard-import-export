import_dashboard(file_path):

This function reads a dashboard JSON file (from the Dashboard/ folder) and sends a POST request to the Grafana API to import it.

The endpoint /api/dashboards/db is used to create or update dashboards in Grafana.

main():

This function scans the Dashboard/ folder for all .json files (which were exported previously).

For each .json file, it calls import_dashboard() to import the dashboard into Grafana.

The script will import all the dashboards found in the Dashboard/ folder (all .json files).

It does not have any interval, so it will run once and import all the dashboards in that folder.

If a dashboard is successfully imported, it will print a success message. If there is an error, it will print the error details.

Usage:
Place all the exported .json files in the Dashboard/ folder.

Update the grafana_url and grafana_api_key with the correct values.

Run the script: python import_dashboards.py