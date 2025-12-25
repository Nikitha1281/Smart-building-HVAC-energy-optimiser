import time
import random
import json
import urllib.request
from datetime import datetime

URL = "https://script.google.com/macros/s/AKfycbxhJvp-f2iQdRMJspeL93g77L3Ssn5CAKYRMKELFU1WOFMbLaCa10d9jpRlMZbI_-w/exec"
hysteresis = 0.5
wings = ["Wing-A", "Wing-B", "Wing-C"]

def decide_hvac(avg_body_temp):
    if avg_body_temp >= 37.5:
        return  22 #high body temp people
    elif avg_body_temp >= 36.5:
        return 24 #moderate body temp people
    else:
        return 26 #less body temp people

for i in range(10):

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    

    for wing in wings:

        avg_body_temp = round(random.uniform(36.0, 38.5), 2)
        hvac_set_temp = decide_hvac(avg_body_temp)

        inside_temp = round(random.uniform(hvac_set_temp - 2, hvac_set_temp + 3), 2)
        outside_temp = round(random.uniform(30, 40), 2)

        if inside_temp > hvac_set_temp + hysteresis:
            ac_status = "ON"
        elif inside_temp < hvac_set_temp - hysteresis:
            ac_status = "OFF"
        else:
            ac_status = "NO CHANGE"

        print(f"\n {wing}")
        print(f"Time: {current_time}")
        print(f"Inside Temperature: {inside_temp} ")
        print(f"Outside Temperature: {outside_temp} ")
        print(f"Average Body Temperature: {avg_body_temp} ")
        print(f"hvac Set Temperature: {hvac_set_temp} ")
        print(f"AC Status: {ac_status}")

        payload = {
            "time": current_time,
            "wing": wing,
            "inside_temp": inside_temp,
            "outside_temp": outside_temp,
            "avg_body_temp": avg_body_temp,
            "hvac_set_temp": hvac_set_temp,
            "ac_status": ac_status
        }

        try:
            data = json.dumps(payload).encode("utf-8")
            req = urllib.request.Request(
                URL,
                data=data,
                headers={"Content-Type": "application/json"},
                method="POST"
            )
            urllib.request.urlopen(req)
        except:
            pass

    time.sleep(2)

