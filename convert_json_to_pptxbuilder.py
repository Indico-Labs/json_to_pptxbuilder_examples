import json
import sys
import requests

def setup(token):
    url = 'https://api.pptxbuilder.com/api/v2/convert_data_to_pptx'
    headers = {}
    headers['Authorization'] = 'Bearer ' + token
    with open('example_data/bar.json', 'r') as f:
        content = f.read()
    return url, headers, content

def send_data_without_pptx(url, headers, content):
    return requests.post(
            url=url,
            files={'json_data': (None, content)},
            headers=headers
    )

def send_data_with_pptx(url, headers, content):
    mime_type = (
        'application/vnd.openxmlformats-officedocument.'
        'presentationml.presentation'
    )
    file_name = 'example.pptx'
    with open(file_name, 'rb') as f:
        output = f.read()

    return requests.post(
            url=url,
            files={
                'pptx_file': (file_name, output, mime_type),
                'json_data': (None, content)
            },
            headers=headers
    )

if __name__ == "__main__":
    """Usage:
    1. With predefined token and without pptx file:
        $ python convert_json_to_pptxbuilder.py
    2. With predefined token and with pptx file:
        $ python convert_json_to_pptxbuilder.py pptx
    3. With token and without pptx file:
        $ python convert_json_to_pptxbuilder.py <your token>
    4. With token and pptx file:
        $ python convert_json_to_pptxbuilder.py <your token> pptx
        or
        $ python convert_json_to_pptxbuilder.py pptx <your token>
    """

    try:
        token = sys.argv[1]
        if token == 'pptx':
            token = sys.argv[2]
    except IndexError:
        token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NDF9.R0ZwDSa919oa7lkBErhUOsom-F551g12btxMF2q8qN0'
    try:
        arg = sys.argv[1]
        if arg != 'pptx':
            arg = sys.argv[2]
        if arg == 'pptx':
            with_pptx_file = True
    except IndexError:
        with_pptx_file = False

    url, headers, content = setup(token)

    if with_pptx_file:
        print('***Sending content with pptx file***')
        response = send_data_with_pptx(url, headers, content)
    else:
        print('***Sending only content***')
        response = send_data_without_pptx(url, headers, content)
    if response.status_code == 200:
        print('~~~Successfully received data!~~~\n')
        content = json.loads(response.content)
        url = content.get('url')
        if not url:
            print('Ups, try again')
        print('New Project URL: \n')
        print(url, '\n')
    else:
        print('~~~Something went wrong!~~~')
        print(response.status_code, response.content)