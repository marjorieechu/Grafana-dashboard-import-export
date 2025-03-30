Replace your_grafana_api_key with a valid API key.

Ensure jq is installed = sudo apt install jq or sudo yum install jq

Save this script as export.sh.

Make it executable = chmod +x export_dashboards.sh
run the script with = ./export/*.sh

Fetches up to 4 dashboards using get_dashboards().

Exports each dashboard as a JSON file using export_dashboard().

Waits for 24 hours (sleep 86400).

Repeats the process indefinitely.