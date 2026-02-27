

import requests
from bs4 import BeautifulSoup


try:
    #step1: read the webpage
    response = requests.get("https://www.google.com/")
    # if the page is accesible then status code will be 200
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a'):
            print(link.get('href'))
            print("---------------")
except Exception as e:
    print("An error occurred:", e)




