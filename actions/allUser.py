import sys
import json
import dns
import requests

from st2common.runners.base_action import Action

class SmitchGetUsers(Action):
    def run(self, xApiKey):

        header = {
            'Accept': 'application/json',
            'x-api-key': xApiKey
        }
        url = 'https://app.api.developer.mysmitch.com/​v1​/app​/users'

        users = requests.get(url, headers = header)
        return(True,users.status_code)