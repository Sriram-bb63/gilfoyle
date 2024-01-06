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
- [ ] Alert during abnormal surges
- [ ] Export data as excel/pdf?
- [ ] ``data = pd.DataFrame.from_records([row.to_dict() for row in data])`` This is O(n). This will be a bottleneck when db becomes big
- [ ] Make a config file to define frequency, alert levels etc

---


# NOTES

First we need to read the db in the grapher program
Create a static graph
Create a live graph
Make graph program as a command (Add alias using script?)

Issue alert during surges in main program
Create config files to set alert levels


Options
Use list comprehension
Create a pd df
Better to create a pd df since it will be able to handle large data better