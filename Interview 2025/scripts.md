```
#!/bin/bash
# health_backup_check.sh
# Basic system health and backup check script

# === System Health Check ===
echo "===== System Health Check ====="
echo "Hostname: $(hostname)"
echo "Date: $(date)"

echo
echo "--- CPU Load ---"
uptime

echo
echo "--- Memory Usage ---"
free -h

echo
echo "--- Disk Usage ---"
df -h

echo
echo "--- Top 5 CPU consuming processes ---"
ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head -n 6
```
--------------------------------
```
-------------------------------
backup script
------------------------------
#!/bin/bash
# simple_backup.sh
# Basic backup script to compress and store files safely

# === Configuration ===
SOURCE_DIR="/home/ubuntu/data"      # Folder you want to back up
BACKUP_DIR="/backup"                # Backup location
DATE=$(date +%Y-%m-%d_%H-%M-%S)
BACKUP_FILE="backup_$DATE.tar.gz"

# === Create backup directory if it doesn’t exist ===
mkdir -p "$BACKUP_DIR"

# === Create compressed backup ===
tar -czf "$BACKUP_DIR/$BACKUP_FILE" "$SOURCE_DIR"

# === Check if backup succeeded ===
if [ $? -eq 0 ]; then
    echo "✅ Backup successful!"
    echo "Backup file: $BACKUP_DIR/$BACKUP_FILE"
else
    echo "❌ Backup failed!"
fi
```````
--------------------------
``````````````
------------------------------
Log rotation
------------------------------
#!/bin/bash
# log_cleanup.sh
# Automates log cleanup and disk health check

# Log file for tracking cleanup activity
LOG_FILE="/var/log/cleanup_script.log"

echo "===== Log Cleanup Started at $(date) =====" >> $LOG_FILE

# 1️⃣ Check current disk usage
df -h >> $LOG_FILE

# 2️⃣ Rotate logs manually using logrotate
/usr/sbin/logrotate -f /etc/logrotate.conf >> $LOG_FILE 2>&1

# 3️⃣ Clean systemd journal logs (keep only last 500MB)
journalctl --vacuum-size=500M >> $LOG_FILE 2>&1

# 4️⃣ Optional: truncate very large specific log files
# Example for nginx or application logs
find /var/log -type f -name "*.log" -size +200M -exec truncate -s 0 {} \; >> $LOG_FILE 2>&1

# 5️⃣ Restart services if needed (optional)
systemctl restart nginx >> $LOG_FILE 2>&1
# systemctl restart myapp.service >> $LOG_FILE 2>&1

# 6️⃣ Final disk usage report
df -h >> $LOG_FILE

echo "===== Cleanup Completed at $(date) =====" >> $LOG_FILE
echo "" >> $LOG_FILE
`````
