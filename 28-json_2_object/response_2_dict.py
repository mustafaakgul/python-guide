import requests
import json
from include.src.json_2_object.response_2_dict_alt import dict2obj
from types import SimpleNamespace


class Weather():
    def __init__(self, lon):
        self.lon = lon

response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'.format(lat=40.9910, lon=28.6498, API_KEY='21f05ca1a3538ed5f99b1df5aa1078a0'))
# print(response, type(response))
# print(response.json(), type(response.json()))
# print(type(response.text), response.text)
# print(type(response.content), response.content)
# print(response.headers)


# Hard Mapping
lon = response.json()['coord']['lon']
print(type(lon), lon)

weather = Weather(lon)
print(weather, weather.lon)

# Trying to json to python object
# x = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
# print(x.coord.lon)


# Convert the json body into a dictionary
# json_response = response.json()
# print(json_response, type(json_response))
# print(json_response['coord']['lon'])


# Convert the json to a nested object
# res_obj = dict2obj(json_response)
# print("Res obj", res_obj, type(res_obj))
# print(res_obj.coord.lon)


# Getting Errors
# json_loads = json.loads(json_response)
# print(json_loads, type(json_loads))