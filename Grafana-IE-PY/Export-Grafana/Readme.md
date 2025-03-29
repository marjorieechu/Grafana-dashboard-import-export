get_dashboards():

This function fetches all dashboards from Grafana by making a GET request to the /api/search endpoint.

It will return a list of all dashboards available on the Grafana instance.

export_dashboard(uid):

This function exports each dashboard by its UID, making a GET request to /api/dashboards/uid/{uid} to get the JSON representation of the dashboard.

The dashboard is saved as a .json file in the Dashboard/ folder.

Main Loop:

The script runs continuously and will export all dashboards from Grafana every 24 hours (using polling_interval = 86400).

It fetches all the dashboards using the get_dashboards() function, and then iterates through them to export each one using the export_dashboard() function.

The script will fetch all dashboards from Grafana and export them to the Dashboard/ folder.

It will continue running in a loop, fetching and exporting dashboards every 24 hours.