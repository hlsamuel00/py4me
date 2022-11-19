import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = input('How many times?: ')
position = input('What position?: ')
url = input('Enter URL: ')

# Try to convert count and position provided from user to locate specific response.
try:
    count = int(count)
    position = int(position)
except:
    print('Please enter valid number for count and/or position.')
    quit()

while count > 0:
    # Try to retrieve html from url provided
    try:
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
    except:
        print('Please enter a valid url.')
        quit()

    print(url)

    # Retrieve anchor tag at requested position
    url = [tag.get('href',None) for tag in soup('a')][position - 1]
    count = count - 1

print(soup('a')[position - 1].contents[0])