import urllib.request, urllib.parse, urllib.error
import json

service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'   
google_api_key = '&key=AIzaSyAFpdGG-XF7po5MgaOcEI4irxK8ocXTT1E'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    if address == 'done': break

    url = service_url + urllib.parse.urlencode({ 'address': address }) + google_api_key

    print('Retrieving', url)

    url_handle = urllib.request.urlopen(url)
    data = url_handle.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('=== Failure to Retrieve ===')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)

    location = js['results'][0]['formatted_address']
    print(location)
