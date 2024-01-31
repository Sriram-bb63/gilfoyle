#!/bin/bash

# Pip install requirements
pip install -r requirements.txt

# Create a backup of existing log
mkdir -p /var/log/gilfoyle/backup
backupName=gilfoyle_backup_$(date +"%Y-%m-%d_%T").db
cp /var/log/gilfoyle/database.db /var/log/gilfoyle/backup/$backupName
echo Backup stored as /var/log/gilfoyle/backup/$backupName

# Delete existing log
rm -f /var/log/gilfoyle/database.db
echo Database deleted

# Copy latest code to source directory
cp ./main.py /usr/local/bin/gilfoyle/main.py
cp ./models.py /usr/local/bin/gilfoyle/models.py
cp ./grapher.py /usr/local/bin/gilfoyle/grapher.py
cp ./alert.py /usr/local/bin/gilfoyle/alert.py
mkdir -p /usr/local/etc/gilfoyle && cp ./config.json /usr/local/etc/gilfoyle/config.json
echo Latest code updated

# Grant execution permissions
chmod +x /usr/local/bin/gilfoyle/main.py
chmod +x /usr/local/bin/gilfoyle/models.py
chmod +x /usr/local/bin/gilfoyle/grapher.py
chmod +x /usr/local/bin/gilfoyle/alert.py
echo Persmissions updated

# Reload nd start daemon
systemctl daemon-reload
systemctl enable gilfoyle
systemctl start gilfoyle
systemctl status gilfoyle