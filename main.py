import psutil
from time import sleep
from datetime import datetime
from models import engine, Gilfoyle
from sqlalchemy import desc
from sqlalchemy.orm import sessionmaker
import json
import sys
import os
# from alert import alert


Session = sessionmaker(bind=engine)
session = Session()


def loadConfig() -> dict:
    try:
        if os.path.realpath(__file__) == "/usr/local/bin/gilfoyle/main.py":
            with open(f"/usr/local/etc/gilfoyle/config.json", "r") as f:
                config = f.read()
        else:
            with open("config.json", "r") as f:
                config = f.read()
        return json.loads(config)
    except FileNotFoundError:
        print("Config file does not exist at _____")
        print("Gilfoyle failed to start")
        sys.exit(0)
config = loadConfig()


def getSessionId() -> int:
    lastSession = session.query(Gilfoyle).order_by(desc(Gilfoyle.id)).limit(1).first()
    if lastSession:
        return lastSession.sessionId + 1
    else:
        return 1
sessionId = getSessionId()


def getRAM() -> int:
    ram = psutil.virtual_memory()
    # svmem(total=12291612672, available=9253584896, percent=24.7, used=2099912704, free=7342551040, active=869027840, inactive=2990780416, buffers=125169664, cached=2723979264, shared=612175872, slab=292745216)
    ramUsed = int(abs((ram.available * 100 / ram.total) - 100))
    if ramUsed > config.get("ramAlertLevel"):
        # alert(f"RAM used: {ramUsed}%")
        pass
    return ramUsed


def getBatteryLevel() -> int:
    battery = psutil.sensors_battery()
    # sbattery(percent=88.64661654135338, secsleft=12338, power_plugged=False)
    batteryLevel = int(round(battery.percent, 0))
    if batteryLevel < config.get("batteryAlertLevel"):
        # alert(f"Battery level: {batteryLevel}%")
        pass
    return batteryLevel


def getTemp() -> int:
    temperatures = psutil.sensors_temperatures()
    # {'nvme': [shwtemp(label='Composite', current=31.85, high=81.85, critical=85.85), shwtemp(label='Sensor 1', current=31.85, high=65261.85, critical=65261.85)], 'coretemp': [shwtemp(label='Package id 0', current=71.0, high=100.0, critical=100.0), shwtemp(label='Core 0', current=71.0, high=100.0, critical=100.0), shwtemp(label='Core 1', current=59.0, high=100.0, critical=100.0)], 'dell_smm': [shwtemp(label='', current=58.0, high=None, critical=None), shwtemp(label='', current=38.0, high=None, critical=None), shwtemp(label='', current=40.0, high=None, critical=None)]}
    cpuTemp = int(temperatures["coretemp"][0].current) # shwtemp(label='Package id 0', current=71.0, high=100.0, critical=100.0)
    if cpuTemp > config.get("tempAlertLevel"):
        # alert(f"CPU temperature: {cpuTemp} C")
        pass
    return cpuTemp


def getFanRPM() -> int:
    fan = psutil.sensors_fans()
    # {'dell_smm': [sfan(label='', current=0)]}
    fanRPM = fan["dell_smm"][0].current
    if fanRPM > config.get("rpmAlertLevel"):
        # alert(f"Fan RPM: {fanRPM}")
        pass
    return fanRPM


def collectData() -> Gilfoyle:
    data = Gilfoyle(
        sessionId=sessionId,
        date=datetime.now().date(),
        time=datetime.now().time(),
        ram=getRAM(),
        battery=getBatteryLevel(),
        temperature=getTemp(),
        rpm=getFanRPM()
    )
    sleep(config.get("frequency", 2))
    return data


def batchInsert(data: list) -> None:
    session.add_all(data)
    session.commit()


def main():
    while True:
        data = [collectData() for _ in range(5)]
        batchInsert(data)


if __name__ == "__main__":
    print("Gilfoyle is running")
    main()