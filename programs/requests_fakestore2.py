

import requests 


payload = {'title': 'New Product', 'price': 29.99}

url = "https://fakestoreapi.com/"    # url = "https://www.api.instagram.com"
endpoint = "products"
finalurl = url + endpoint  

response = requests.post(finalurl, json=payload)
print(response.status_code)
print(response.json())


'''
response = requests.get(finalurl)
for item in response.json():
    print("ID:", item['id'])
    print("Title:", item['title'])
    print("Price:", item['price'])
    print("Category:", item['category'])
    print("Description:", item['description'])
    print("Image URL:", item['image'])
    print("-" * 40)
'''