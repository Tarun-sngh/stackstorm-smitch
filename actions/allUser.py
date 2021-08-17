import sys
import json
import dns
import requests

from st2common.runners.base_action import Action

class SmitchGetUsers(Action):
    def run(self, xApiKey):
        auth_string = f"x-api-key:{xApiKey}"
        header= {'headers' : f"{auth_string}"}
        url = 'https://app.api.developer.mysmitch.com/​v1​/app​/users'

        users = requests.get(url, auth = header)
        return(True,users)