import urllib.request
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_1688332.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')

print( sum([int(tag.contents[0]) for tag in tags]) )


# for tag in tags:
#     sum = sum + int(tag.contents[0])

# print(sum)