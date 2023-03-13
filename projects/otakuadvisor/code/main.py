import urllib.request, urllib.parse
import json
from random import choice
from selection import selectFromList
from settings import *

# Initialize the dictionary needed for the http GET params
http_params = dict()

# Determine the mood so we can select the genre
http_params['genres'] = choice(MOOD_DICT[selectFromList(list(MOOD_DICT.keys()), 'What mood are we going for?')])[1]

# Determine if we should remove explicit recommendations
http_params['sfw'] = bool(SFW_DICT[selectFromList(list(SFW_DICT.keys()), 'Does it need to be Safe for Work?')])

# Determine the type of anime to watch
http_params['type'] = TYPE_DICT[selectFromList(list(TYPE_DICT.keys()), 'What type of anime would you like?')]

# Determine if they want it still airing or complete (only for tv shows)
if http_params['type'] == 'tv':
    http_params['status'] = STATUS_DICT[selectFromList(list(STATUS_DICT.keys()), 'Do you want the show completed or still airing?')]

# Submit the GET request to obtain the data
service_url = 'https://api.jikan.moe/v4/anime'

url = f"{service_url}?{urllib.parse.urlencode(http_params)}" # -> max per page is 25
response = urllib.request.urlopen(url).read().decode()
data = []
try:
    j_son = json.loads(response)
    pagination = j_son['pagination']
    data += j_son['data']
except:
    pass

# Get full list of anime recommendations
# while pagination['has_next_page']:
#     http_params['page'] = pagination['current_page'] + 1
#     url = f"{service_url}?{urllib.parse.urlencode(http_params)}"
#     response = urllib.request.urlopen(url).read().decode()
#     j_son = json.loads(response)
#     pagination = j_son['pagination']
#     data += j_son['data']
    

if j_son:
    print(http_params, len(data), pagination['items']['total'])
