# This file creates a dictionary of state abbreviations and their latitude and longitude coordinates
# Then, creates a function to get color of state
import json
import pprint
from us_state_abbrev import abbrev_to_us_state
import states

# pp = pprint.PrettyPrinter(width=41, compact=True)
# print(abbrev_to_us_state) #Dict: (state abbr: fullname)

# remove uneeded data
for state in ["DC", "AS", "GU", "MP", "PR", "UM", "VI"]:
    del abbrev_to_us_state[state]

# print(abbrev_to_us_state) #Dict: (state abbr: fullname)

with open('USstates_avg_latLong.json', 'r') as f:
    latlong = json.load(f)
# pp.pprint(latlong)


def getLatLong(state_name, list_of_dicts):
    return [(state['latitude'], state['longitude']) for state in list_of_dicts if state['state'] == state_name][0] # should only be one result anyways..

state_latlong = []
for state_name in abbrev_to_us_state.values():
    state_latlong.append(getLatLong(state_name, latlong))

state_data = dict(zip(abbrev_to_us_state,state_latlong))


########################################################################################################################
# go through each state, if bad request, go to next state. Store result.

def createCache(state_data: dict, request_limit: int):
    cache = []
    for key, value in state_data.items():
        #print(f'Key: {key}, Value: {value}')

        temp = states.getForecast(value)
        if temp is not None:
            color = states.getColor(temp)
            cache.append((key.lower(), color))
        if len(cache) > request_limit:
            print(f'Here are the {request_limit} states: {cache}')
            break
