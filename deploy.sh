#!/bin/bash


# Add grapher alias
if grep -q "^alias gilfoyle" ~/.bash_aliases;
then 
    echo "Alias already exiss"
else
    echo "alias gilfoyle='/usr/bin/python3 /usr/local/bin/gilfoyle/grapher.py'" >> ~/.bash_aliases
    echo "Added alias"
fi

# Create gilfyle directory to save reports
mkdir -p ~/Documents/gilfoyle

# Add service files
cp ./gilfoyle.service /etc/systemd/system/gilfoyle.service
echo "Created service file"

# # Create a backup of existing log
mkdir -p /var/log/gilfoyle/backup
backupName=gilfoyle_backup_$(date +"%Y-%m-%d_%T").db
cp /var/log/gilfoyle/database.db /var/log/gilfoyle/backup/$backupName
echo Backup stored as /var/log/gilfoyle/backup/$backupName

# # Delete existing log
rm -f /var/log/gilfoyle/database.db
echo Database deleted

# # Copy latest code to source directory
cp ./src/main.py /usr/local/bin/gilfoyle/main.py
cp ./src/models.py /usr/local/bin/gilfoyle/models.py
cp ./src/grapher.py /usr/local/bin/gilfoyle/grapher.py
cp ./src/alert.py /usr/local/bin/gilfoyle/alert.py
mkdir -p /usr/local/etc/gilfoyle && cp ./src/config.json /usr/local/etc/gilfoyle/config.json
echo Latest code updated

# # Grant execution permissions
chmod +x /usr/local/bin/gilfoyle/main.py
chmod +x /usr/local/bin/gilfoyle/models.py
chmod +x /usr/local/bin/gilfoyle/grapher.py
chmod +x /usr/local/bin/gilfoyle/alert.py
echo Persmissions updated

# # Reload and start daemon
systemctl daemon-reload
systemctl enable gilfoyle
systemctl start gilfoyle
systemctl status gilfoyle
echo "systemctl reloaded"

# # Reload bash
# ~/.bashrc
# echo ".bashrc reloaded"