#!/bin/bash
# Backup script for PostgreSQL

# Environment variables
# DB_HOST, DB_NAME, DB_USER, and DB_PASSWORD should be set via Kubernetes secrets or environment variables

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backups"
BACKUP_FILENAME="postgres_backup_$DATE.sql.gz"

# Set the database password environment variable
export PGPASSWORD="$DB_PASSWORD"

# Execute pg_dump to backup PostgreSQL database
pg_dumpall -h "$DB_HOST" -U "$DB_USER" | gzip > "$BACKUP_DIR/$BACKUP_FILENAME"

echo "Backup completed: $BACKUP_FILENAME"

