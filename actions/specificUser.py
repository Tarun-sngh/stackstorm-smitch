import sys
import json 
import dns
import requests

from st2common.runners.base_action import Action

class SmitchGetUser(Action):
    def run(self, xApiKey, userId):

        auth = {"headers": { "x-api-key": xApiKey } }
        url = f"https://app.api.developer.mysmitch.com/​v1​/app​/user?user_id={userId}"

        user = requests.get(url, auth = auth)
<<<<<<< HEAD
        return(True)
=======
        return(True)
>>>>>>> 5d8096effd43d1a426ee656b55cf14da47eef79d
