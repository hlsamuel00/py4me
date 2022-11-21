import urllib.request, urllib.parse
import json


service_url = 'http://py4e-data.dr-chuck.net/json?'
address = input('Enter location: ')

url = service_url + urllib.parse.urlencode({ 'address': address, 'key': 42 })
print('Retrieving', url)

data = urllib.request.urlopen(url).read().decode()
print('Retrieved', len(data), 'characters')

place_id = json.loads(data)['results'][0]['place_id']

print('Place id:', place_id)

