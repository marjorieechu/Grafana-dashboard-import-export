#!/bin/bash

GRAFANA_URL=$GRAFANA_URL  # Change to your Grafana URL
GRAFANA_API_KEY=$GRAFANA_API_KEY  # Replace with your Grafana API key
DASHBOARD_FOLDER="Dashboard"

# Function to import a dashboard
import_dashboard() {
    local file=$1
    local uid=$(basename "$file" .json)

    echo "Importing dashboard: $uid"

    # Read the dashboard JSON file
    dashboard_json=$(<"$file")

    # Create or update the dashboard in Grafana
    response=$(curl -s -H "Authorization: Bearer $GRAFANA_API_KEY" -X POST -H "Content-Type: application/json" -d @- "$GRAFANA_URL/api/dashboards/db" <<< "$dashboard_json")
    
    # Check if import was successful
    if echo "$response" | grep -q '"status":"success"'; then
        echo "Successfully imported: $uid"
    else
        echo "Failed to import: $uid"
        echo "$response"
    fi
}

# Import all dashboards once
for file in "$DASHBOARD_FOLDER"/*.json; do
    import_dashboard "$file"
done

echo "Import complete. Exiting script."
