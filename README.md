# gilfoyle

<div align="center"><img src="gilfoyle.webp" alt="Gilfoyle from Silicon Valley" width="500"/></div>

This is a system logger named after a character from Silicon Valley. It logs RAM used (in %), battery level (in %), CPU temperature (in °C) and fan RPM. The time interval between each log can be changed in `config.json`->`'frequency'`.

- Service file: ``/etc/systemd/system/gilfoyle.service``
- Source file:  ``/usr/local/bin/gilfoyle/*``
- Log file:     ``/var/log/gilfoyle/database.db``
- Config file:  ``/usr/local/etc/gilfoyle/config.json``
- Report file   ``~/Documents/gilfoyle/*.csv``

## Installtion

1. Clone this repository somewhere you won't delete.
2. ```sh
    cd Gilfoyle
    ```
3. ```sh
    chmod +x ./deploy.sh
    sudo ./deploy.sh
    ```
4. ```sh
    systemctl status gilfoyle
    ```

> Note: You might need to restart your terminal (or run ``~/.bashrc``) after using the deploy script for the first time.

## Configurations

All configurations are meant to be stored at `config.json` file. For any changes to take place, you must do either of the following actions:

1. Use the `deploy.sh` script. But doing so, the log will be broken but a backup will be saved.
2. Use systemctl to restart the service:
    ```sh
    sudo systemctl restart gilfoyle
    ```



## Updating the code

1. Pull latest code.
2. Run the `deploy.sh` file.
3. A backup of existing log will be created and a new log will start after running the deploy script.

## Contribution

Contributions to this project are always welcome. Please refer to [todo.md](/todo.md) for additional details.