

import requests 

url = "https://fakestoreapi.com/"    # url = "https://www.api.instagram.com"
endpoint = "products"
finalurl = url + endpoint 

response = requests.get(finalurl,auth=('user', 'pass'))
if response.status_code == 200:
    data = response.json()
    for item in data:
        print("ID:", item['id'])
        print("Title:", item['title'])
        print("Price:", item['price'])
        print("Category:", item['category'])
        print("Description:", item['description'])
        print("Image URL:", item['image'])
        print("-" * 40)

#########################################################################

endpoint = "users"
finalurl = url + endpoint
response = requests.get(finalurl)
if response.status_code == 200:
    data = response.json()
    for user in data:
        print("ID:", user['id'])
        print("Name:", user['name']['firstname'], user['name']['lastname'])
        print("Username:", user['username'])
        print("Email:", user['email'])
        print("Phone:", user['phone'])
        print("Address:", user['address']['street'], user['address']['city'], user['address']['zipcode'])
        print("-" * 40)





import requests
response = requests.get("https://www.api.github.com", auth = ('giridhar276', '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'))