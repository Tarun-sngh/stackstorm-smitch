import sys
import json
import dns
import requests

from st2common.runners.base_action import Action

class smitchBulbAction(Action):
    def run(self, x_api_key, user_id, device_id, power_status, brightness, temperature, red, green, blue, delay):

        header = {
            'Accept': 'application/json',
            'x-api-key': x_api_key
        }
        url = 'https://app.api.developer.mysmitch.com/v1/app/job/device'
        my_obj = {
            "user_id": user_id,
            "commands": [
                {
                    "device_id": device_id,
                    "device_settings": {
                        "power_status": power_status,
                    }
                }
            ]
        }

        if(brightness>5 and brightness<100):
            my_obj["commands"][0]["device_settings"]["brightness"] = brightness
        if(temperature>=2700 and temperature<=6500 ):
            my_obj["commands"][0]["device_settings"]["temperature"] = temperature
        if(red>0 or green > 0 or blue>0):
            my_obj["commands"][0]["device_settings"]["colours"] = {}
            my_obj["commands"][0]["device_settings"]["colours"]["red"] = red
            my_obj["commands"][0]["device_settings"]["colours"]["green"] = green
            my_obj["commands"][0]["device_settings"]["colours"]["blue"] = blue
        if(delay>5 and delay<86400):
            my_obj["delay"] = delay

        light = requests.post(url, json = my_obj, headers = header)
        return(True, light.json())