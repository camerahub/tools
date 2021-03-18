import requests
import json
from requests.auth import HTTPBasicAuth

# Dev API
#url = 'https://camerahub.info/api/'
#url = 'https://dev.camerahub.info/api/'
#url = 'http://127.0.0.1:8000/api/'

username = 'admin'
password = 'admin'

# Endpoints
negativeEndpoint = url + 'print/'

with open('print.json') as json_file:
    data = json.load(json_file)
    for obj in data:
        response = requests.post(
            negativeEndpoint,
            json = obj,
            auth=HTTPBasicAuth(username, password),
        )
        
        if response.status_code >= 200:
            print(obj)
            print(response)
            print(response.json())
            print("\n")
