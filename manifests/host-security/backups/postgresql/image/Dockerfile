# Use the official PostgreSQL image as the base image
FROM postgres:latest

# Install any dependencies you might need
RUN apt-get update && apt-get install -y net-tools

# Add the backup script
COPY backup-script.sh /usr/local/bin/backup-script.sh

# Make the script executable
RUN chmod +x /usr/local/bin/backup-script.sh

# Create a directory for the backups
RUN mkdir /backups

# Set the backup script as the entrypoint
ENTRYPOINT ["/usr/local/bin/backup-script.sh"]
