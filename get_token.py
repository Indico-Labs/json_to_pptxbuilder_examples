import requests
import json

key = "5f210efc-8898-3b6d-baee-94274cd64adb"
user = "DiogoB"
passwd = "asdf"

url = 'https://api.pptxbuilder.com/api/auth/token'

body = json.dumps({'key': key})
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=body, headers=headers,
                        auth=(user, passwd))

if response.status_code != 200:
    response_msg = response.json()
    print(response_msg['error'])
else:
    token = response.headers['Authentication-Token']
    content = response.json()
    print(content['success'],content['token_expires'],"Token:"+str(token))