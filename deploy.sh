#!/bin/bash

rm -f /var/log/gilfoyle/database.db
echo Database deleted

cp ./main.py /usr/local/bin/gilfoyle/main.py
cp ./models.py /usr/local/bin/gilfoyle/models.py
cp ./grapher.py /usr/local/bin/gilfoyle/grapher.py
cp ./alert.py /usr/local/bin/gilfoyle/alert.py
cp ./config.json /usr/local/bin/gilfoyle/config.json
echo Latest code updated

chmod +x /usr/local/bin/gilfoyle/main.py
chmod +x /usr/local/bin/gilfoyle/models.py
chmod +x /usr/local/bin/gilfoyle/grapher.py
chmod +x /usr/local/bin/gilfoyle/alert.py
echo Persmissions updated

systemctl daemon-reload
systemctl enable gilfoyle
systemctl start gilfoyle
systemctl status gilfoyle