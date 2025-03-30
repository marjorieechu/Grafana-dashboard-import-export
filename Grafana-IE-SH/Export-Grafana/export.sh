#!/bin/bash

GRAFANA_URL=$GRAFANA_URL  # Change to your Grafana URL
GRAFANA_API_KEY=$GRAFANA_API_KEY  # Replace with your Grafana API key
EXPORT_FOLDER="Dashboard"
POLLING_INTERVAL=86400  # 24 hours

# Ensure the export folder exists
mkdir -p "$EXPORT_FOLDER"

# Function to export a dashboard
export_dashboard() {
    local uid=$1
    local output_file="$EXPORT_FOLDER/$uid.json"
    curl -s -H "Authorization: Bearer $GRAFANA_API_KEY" "$GRAFANA_URL/api/dashboards/uid/$uid" > "$output_file"
    echo "Exported: $output_file"
}

# Main loop
while true; do
    DASHBOARDS=("uid1" "uid2" "uid3" "uid4")  # Replace with actual UIDs
    for uid in ${DASHBOARDS}; do
        export_dashboard "$uid"
    done

    echo "Waiting $POLLING_INTERVAL seconds before the next export..."
    sleep $POLLING_INTERVAL
done
