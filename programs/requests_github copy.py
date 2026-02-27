

import requests

try:
    token = "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"

    reponame = "apidemos"
    
    data = {
        "name": reponame,
        "description": "This is a test repository created via API",
        "private": False
    }

    response = requests.post("https://api.github.com/user/repos", json=data, auth=("giridhar276", token))

    print(response.status_code)
except Exception as e:
    print("An error occurred:", e)