


import requests
import json
response = requests.get("https://api.github.com/",header)
#print(type(response.text))
data = json.loads(response.text)
for key,value in data.items():
    print(key,value)



requests.get()