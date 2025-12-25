import json
import time
import random
import urllib.request
from datetime import datetime

URL = "https://script.google.com/macros/s/AKfycbz_jcnveXDycNDeG20cawBugmy1tRrVa5unO_N7M-JbKJaXUFwrnjx7K5ktvmmg-5dW/exec"
set_temp = 24#considering own room temp
hysteresis=0.1#to avoid continuous on and off


def send_data(dt, in_temp, out_temp, ac):
    payload = {
        "datetime": dt,
        "inside_temperature": in_temp,
        "outside_temperature": out_temp,
        "ac_status": ac
    }

    req = urllib.request.Request(
        URL,
        json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    urllib.request.urlopen(req)


for _ in range(10):
    inside_temp = round(random.uniform(26, 36), 2)#detected using DHT11
    outside_temp = round(random.uniform(30, 40), 2)#detected using climate sensor
    
    if inside_temp > set_temp+hysteresis:
        ac_status = "ON"
    elif inside_temp < set_temp-hysteresis:
        ac_status = "OFF"

    current_time = datetime.now().strftime("%Y:%m:%d %H:%M:%S")

    print(f"Time: {current_time}")
    print(f"Inside Temp: {inside_temp}")
    print(f"Outside Temp: {outside_temp}")
    print(f"AC Status: {ac_status}")
   

    send_data(current_time, inside_temp, outside_temp, ac_status)
    time.sleep(2)