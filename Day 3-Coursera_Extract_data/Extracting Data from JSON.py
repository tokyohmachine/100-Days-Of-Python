import json
import urllib.request

url = 'http://py4e-data.dr-chuck.net/comments_1505249.json'
print(url)

with urllib.request.urlopen(url) as link:
    data = json.loads(link.read().decode())

count = 0

for item in data["comments"]:
    number = int(item["count"])
    count = count + number

print(count)