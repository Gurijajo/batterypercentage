import psutil
from plyer import notification
import time

while (True):
    battery = psutil.sensors_battery()
    percent = battery.percent

    notification.notify(
        title="Battery Perventage",
        message=str(percent) + "% Battery Reaming",
        timeout=10
    )
    time.sleep(60*60)

    continue



