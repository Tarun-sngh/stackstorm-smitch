import sys
import json 
import dns
import requests

from st2common.runners.base_action import Action

class SmitchPlugAction(Action):
    def run(self, xApiKey, userId, deviceId, powerStatus):

        header = {
            'Accept': 'application/json',
            'x-api-key': 'TEST##bf322a1afa1b4d02986ea4c0bd75251d##eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBfaWQiOiJBUFBfN2E3Yzk0MWVlZjA0NGI0ZGIyMzEyNmNjMjQ1YjdkNWEiLCJzY29wZXMiOlsiKiJdfQ.G7IxzGyoao6h6EdFpD_6a4crELsY6TKYJt94CCs0Guo'
        }
        url = 'https://app.api.developer.mysmitch.com/v1/app/job/device'
        myobj = {
            'user_id': userId,
            'commands':[ 
                {
                    'device_id': deviceId,
                    'device_settings': {
                        'power_status': powerStatus
                    }
                }
            ]
        }

        plug = requests.post(url, json = myobj, headers = header)
        return(True, plug.json())