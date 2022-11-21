import urllib.request
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


while True:
    url = input('Enter a location: ')

    print('Retrieving', url)

    try: 
        data = urllib.request.urlopen(url).read().decode()
    except:
        print('Please enter a valid url.')
        continue
    
    print('Received', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
    
    print('Count:', len(js['comments']))
    print(sum([int(comment['count']) for comment in js['comments']]))
    quit()

