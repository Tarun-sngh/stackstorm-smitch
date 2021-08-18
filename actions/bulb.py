import sys
import json
import dns
import requests

from st2common.runners.base_action import Action

class smitchBulbAction(Action):
    def run(self, xApiKey, userId, deviceId, powerStatus, red, green, blue):

        header = {
            'Accept': 'application/json',
            'x-api-key': xApiKey
        }
        url = 'https://app.api.developer.mysmitch.com/v1/app/job/device'
        myobj = {
            'user_id': userId,
            'commands': [
                {
                    'device_id': deviceId,
                    'device_settings': {
                        'power_status': powerStatus,
                        'colour': {
                            'r': red,
                            'g': green,
                            'b': blue
                        }
                    }
                }
            ]
        }

        light = requests.post(url, json = myobj, headers = header)
        return(True, light.json())