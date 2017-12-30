import time
from datetime import datetime as dt
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours...!")
        time.sleep(5)
    else:
        print("Happy hours...!")
        time.sleep(5)
