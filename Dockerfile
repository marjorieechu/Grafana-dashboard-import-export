# Use Python as base image
FROM python:3.9

# Set working directory
WORKDIR /opt/grafana

# Install required Python libraries
RUN pip install requests schedule

# Copy Grafana dashboard manager script
COPY grafana_dashboard_manager.py /opt/grafana_dashboard_manager.py

# Copy dashboards folder (if needed)
COPY dashboards/ /opt/grafana/dashboards/

# Set environment variables (can be overridden)
ENV GRAFANA_HOST="http://localhost:3000"
ENV API_TOKEN="your_api_token_here"
ENV DASHBOARD_UID="UID"

# Run the script
CMD ["python3", "/opt/grafana_dashboard_manager.py"]
