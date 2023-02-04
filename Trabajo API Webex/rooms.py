import requests

url = "https://webexapis.com/v1/rooms"

payload = "{\"title\": \"Test python\"}"
headers = {
    'user-agent': "vscode-restclient",
    'content-type': "application/json",
    'authorization': "Bearer YTMyNWViM2ItMmEyMC00MmY1LTg2OWUtZmQ5ZjU4MDY3YTRjYWFjYzE3ZGQtZWIy_P0A1_ff79c397-9d79-44f7-8296-8858b58f5ba8"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
