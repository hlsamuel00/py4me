import urllib.request, urllib.parse
import sqlite3
import json
import time

service_url = 'https://py4e-data.dr-chuck.net/opengeo?'

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Locations(address TEXT, geodata TEXT)''')

file_handle = open('where.data')
count = 0
not_found = 0

for line in file_handle:
    if count > 500:
        print('Retrieved 500 locations, restart to retrieve more.')
        break

    address = line.strip()
    print('')
    cur.execute('''SELECT geodata FROM Locations WHERE address = ?''', (memoryview(address.encode()), ))
    
    try:
        data = cur.fetchone()[0]
        print('Found in database', address)
        continue
    except:
        pass

    
    url = service_url + urllib.parse.urlencode({ 'q': address })
    print('Retrieving...', url)

    data = urllib.request.urlopen(url).read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count += 1

    try:
        js = json.loads(data)
    except:
        print(data)
        continue

    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        not_found = not_found + 1

    cur.execute('''INSERT INTO Locations(address, geodata) VALUES(?,?)''', (memoryview(address.encode()), memoryview(data.encode())))
    conn.commit()

    if not count % 50:
        print('Pausing for a bit...')
        time.sleep(2.5)
if not_found > 0:
    print('Number of features for which the location could not be found:', not_found)
    
print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
