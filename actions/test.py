header = {
    'Accept': 'application/json',
    'x-api-key': "x_api_key"
}
url = 'https://app.api.developer.mysmitch.com/v1/app/job/device'
my_obj = {
    "user_id": "user_id",
    "commands": [
        {
            "device_id": "device_id",
            "device_settings": {
                "power_status": "power_status",
            }
        }
    ]
}
brightness = 10
temperature = 2700
red = 4
green = 0
blue = 0
delay = 10
if(brightness>5):
    my_obj["commands"][0]["device_settings"]["brightness"] = brightness
if(brightness>5 and brightness<100):
    my_obj["commands"][0]["device_settings"]["brightness"] = brightness
if(temperature>2700 and temperature<6500 ):
    my_obj["commands"][0]["device_settings"]["temperature"] = temperature
if(red>0 or green > 0 or blue>0):
    my_obj["commands"][0]["device_settings"]["colours"] ={}
    my_obj["commands"][0]["device_settings"]["colours"]["red"] = red
    my_obj["commands"][0]["device_settings"]["colours"]["green"] = green
    my_obj["commands"][0]["device_settings"]["colours"]["blue"] = blue
if(delay>5 and delay<86400):
    my_obj["delay"] = delay
# light = requests.post(url, json = my_obj, headers = header)
# return(True, light.json())
print(my_obj)