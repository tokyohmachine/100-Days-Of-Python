
import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
from urllib.request import urlopen

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode = ssl.CERT_NONE

# http://py4e-data.dr-chuck.net/comments_1505246.html

url = input('Enter the file: ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
counts = 0
for tag in tags:
    count = str(tag)
    x = re.findall("[0-9]+", count)
    for i in x:
        i = int(i)
        counts = counts + i
        print(counts)

    #Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)


