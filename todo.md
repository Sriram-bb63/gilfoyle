# TODO

- [x] Rename from syslog to something else
- [x] Check what happened to og syslog
- [x] Move db to /var/log/syslog
- [x] Move script to apt location
- [x] Auto run script on startup
- [x] Make requirements file for installation
- [ ] Ship with environment?
- [x] Push it to github
- [ ] Installation and setup script
- [x] Add time column
- [ ] Build data explorer application
- [x] Alert during abnormal surges
- [ ] Export data as excel/pdf?
- [ ] ``data = pd.DataFrame.from_records([row.to_dict() for row in data])`` This is O(n). This will be a bottleneck when db becomes big
- [x] Make a config file to define frequency, alert levels etc
- [ ] README.md
- [ ] About
- [ ] Make it flexible. Test with dual fan system, other makes etc
- [ ] Make alerts non blocking
- [ ] gitignore is not working
- [ ] Write a script to keep the daemon upto date
- [ ] Create a config python file to find own path
- [ ] Move config.json to /etc/gilfoyle/config.json

---

## Notes

Source file:  /usr/local/bin/gilfoyle/main.py
Service file: /etc/systemd/system/gilfoyle.service
Log file:     /var/log/gilfoyle.database.db

