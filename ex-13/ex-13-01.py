import urllib.request
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')

while True:
    try:
        data = urllib.request.urlopen(url).read()
    except:
        print('Please enter valid url.')
        continue
    tree = ET.fromstring(data).findall('comments/comment/count')

    total = 0
    for count in tree:
        total = total + int(count.text)

    print(total)
    quit()
