import requests
import json

key = "<A_VALID_COMPANY_KEY>"
user = "<A_VALID_USER>"
passwd = "<A_VALID_PASS>"

url = 'https://api.pptxbuilder.com/api/auth/update_token'

body = json.dumps({'key': key})
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=body, headers=headers,
                        auth=(user, passwd))

if response.status_code != 200:
    response_msg = response.json()
    print(response_msg['error'])
else:
    response_msg = response.json()
    token = response.headers['Authentication-Token']
    print(response_msg['success'])
    print("Token expiration Date: "+str(response_msg['token_expires']))
    print(token)