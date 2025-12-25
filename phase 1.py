import json
import urllib.request
import time


URL = "https://script.google.com/macros/s/AKfycbwDU7iXDJNRoA6P7grOPl9hCYglZPnpIijwhRUiQU0ONl_MX0K_boIsoyiRleq7r1wH/exec"

class Room:
    def __init__(self, temp):
        self.temp = temp

    def update_temp(self, ac_power, ambient_heat, occupant_heat):
        cooling_rate = 0.5
        self.temp = self.temp - (cooling_rate * ac_power) + ambient_heat + occupant_heat
        return round(self.temp, 2)

def send_to_appscript(temp, ac_status, occupants):
    payload = {
        "temperature": temp,
        "ac_status": ac_status,
        "occupants": occupants
    }

    data = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    urllib.request.urlopen(request)

room = Room(50)
occupants = 2  # number of people in room

print("AC OFF")
for i in range(5):
    temp = room.update_temp(ac_power=0,ambient_heat=0.3,occupant_heat=occupants * 0.1)
    print(temp)
    send_to_appscript(temp, "OFF", occupants)
    

print("\nAC ON")
for i in range(5):
    temp = room.update_temp(ac_power=1,ambient_heat=0.3,occupant_heat=occupants * 0.1)
    print(temp)
    send_to_appscript(temp, "ON", occupants)