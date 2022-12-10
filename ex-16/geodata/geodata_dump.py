import sqlite3
import json
import codecs

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Locations')
file_handle = codecs.open('where.js', 'w', 'utf-8')
file_handle.write("myData = [\n")
count = 0

for row in cur:
    print(str(row[0].decode()))
    data = str(row[1].decode())
    try: 
        js = json.loads(str(data))
    except: 
        continue
    
    if len(js['features']) == 0: continue

    lat = js['features'][0]['properties']['lat'] if 'lat' in js['features'][0]['properties'].keys() else 0
    lon = js['features'][0]['properties']['lon'] if 'lon' in js['features'][0]['properties'].keys() else 0

    if lat == 0 or lon == 0: continue

    city = js['features'][0]['properties']['city'] if 'city' in js['features'][0]['properties'].keys() else js['features'][0]['properties']['state_district'] if 'state_district' in js['features'][0]['properties'].keys() else None
    
    state = js['features'][0]['properties']['state'] if 'state' in js['features'][0]['properties'].keys() else js['features'][0]['properties']['district'] if 'district' in js['features'][0]['properties'].keys() else None
    
    country = js['features'][0]['properties']['country']

    if city and state:
        where = f"{city}, {state}, {country}"
    elif state:
        where = f"{state}, {country}"
    else:
        where = country

    where = where.replace("'","")
    
    print(where)
    
    try:
        print(where,'[Latitude: '+ str(lat) +', Longitude: '+ str(lon) +']')

        count = count + 1

        if count > 1: file_handle.write('\n')
        
        output = f"[{lat}, {lon}, '{where}']"
        file_handle.write(output)
    except:
        continue

file_handle.write("\n];\n")
cur.close()
file_handle.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")