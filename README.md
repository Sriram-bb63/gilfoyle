# gilfoyle

![Gilfoyle from Silicon Valley](gilfoyle.webp)

This is a system logger named after a character from Silicon Valley. It logs RAM used (in %), battery level (in %), CPU temperature (in °C) and fan RPM. The time interval between each log can be changed in `config.json`->`'frequency'`.

- Service file: ``/etc/systemd/system/gilfoyle.service``
- Source file:  ``/usr/local/bin/gilfoyle/main.py``
- Log file:     ``/var/log/gilfoyle/database.db``
- Config file:  ``/usr/local/etc/gilfoyle/config.json``

## Installtion

1. Clone this repository somewhere you won't delete.
2. ```sh
    cd Gilfoyle
    ```
3. ```sh
    chmod +x ./deploy.sh
    ./deploy.sh
    ```
4. ```sh
    systemctl status gilfoyle
    ```

## Updating the code

1. Pull latest code.
2. Run the `deploy.sh` file.
3. A backup of existing log will be created and a new log will start after running the deploy script.

## Contribution

Contributions to this project are always welcome. Please refer to [todo.md](/todo.md) for additional details.