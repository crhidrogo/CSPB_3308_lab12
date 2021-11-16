import urllib.request
import urllib.error
import json

# Now we make it a function!
def getForecast(longlat: tuple[float]):
    response = urllib.request.urlopen(f'https://api.weather.gov/points/{longlat[0]},{longlat[1]}')
    data = json.load(response)
    forecast_link = data['properties']['forecast']

    try:
        temp_res = urllib.request.urlopen(forecast_link)
    except urllib.error.HTTPError as errh:
        print("Http Error:", errh)
        return None
    temp_data = json.load(temp_res)
    temp = temp_data['properties']['periods'][1]['temperature']
    return temp

def getColor(temp: int):
    if isinstance(temp, int | float):
        if temp < 10:
            return 'blue'
        elif temp <= 30:
            return 'cyan'
        elif temp <= 50:
            return 'green'
        elif temp <=80:
            return 'orange'
        else:
            return 'red'
    else:
        return 'gray'

# # give a latitude and longitude
# lat, lon = 36.1700,-119.7462
#
# # call first API
# response = urllib.request.urlopen(f'https://api.weather.gov/points/{lat},{lon}')
# data = json.load(response)
#
# # Below is for exploring API
# '''
# pp = pprint.PrettyPrinter(width=41, compact=True)
# keys = [key for key in data.keys()]
# print(f"Top level keys are {keys}")
# print()
# values = [vals for vals in data.values()]
# for key, val in data.items():
#     print(f"The key is {key}\n\n\nAnd the value is {val}\nThe type of the value is {type(val)}\n\n")
# '''
#
# # get second API link
# forcast = data['properties']['forecast']
# print(f'forcast link is: {forcast}')
#
# # Open second API link
# temp_res = urllib.request.urlopen(forcast)
# temp_data = json.load(temp_res)
#
# # get data from API
# temp = temp_data['properties']['periods'][1]['temperature']
#
# # print. dat. SHIT. OUT.
# print(f'Temperature is {temp}')