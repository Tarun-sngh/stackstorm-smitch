# import sys
# import json
# import dns
import requests

from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, xApiKey, userId, deviceId, powerStatus):

        auth = {"headers": { "x-api-key": xApiKey } }
        url = 'https://app.api.developer.mysmitch.com/​/v1​/app​/users'

        users = requests.get(url, auth = auth)
        return(True,users.status_code, users.json())