# Use a base Ubuntu image
FROM ubuntu:20.04

# Install necessary dependencies (curl)
RUN apt-get update && apt-get install -y curl bash

# Set the working directory in the container
WORKDIR /app

# Copy the bash script into the container
COPY import_dashboards.sh /app

# Set the environment variables for Grafana API and URL
ENV GRAFANA_URL=http://localhost:3000
ENV GRAFANA_API_KEY=your_grafana_api_key

# Make the script executable
RUN chmod +x /app/import_dashboards.sh

# Run the bash script
CMD ["./import.sh"]
