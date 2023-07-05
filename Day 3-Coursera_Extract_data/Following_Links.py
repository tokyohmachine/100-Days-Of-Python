import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# start  http://py4e-data.dr-chuck.net/known_by_Fikret.html   position 3 (the first name is 1). Follow that link. Repeat this process 4 times

# start  http://py4e-data.dr-chuck.net/known_by_Siena.html    position 18 (the first name is 1). Follow that link. Repeat this process 7 times.

url = input('Enter the file: ')
repetition = int(input('Enter a count: '))
position = int(input('Enter position: '))-1
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,"html.parser")
href = soup('a')

for tag in range(repetition):
    link = href[position].get('href', None)
    print('Contents:', href[position].contents[0])
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html, "html.parser")
    href = soup('a')
    print(href)








