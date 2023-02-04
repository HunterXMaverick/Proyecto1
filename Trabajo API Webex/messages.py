import requests

url = "https://webexapis.com/v1/messages"

payload = "{\"roomId\": \"Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vMDNkZTg5NTAtOTQyNS0xMWVkLWJjZDgtNDU1M2IyZDg3ZGYw\",\"text\": \"Ya funciona esto\",\"markdown\": \"Hola desde python\"}"
headers = {
    'user-agent': "vscode-restclient",
    'content-type': "application/json",
    'authorization': "Bearer YTMyNWViM2ItMmEyMC00MmY1LTg2OWUtZmQ5ZjU4MDY3YTRjYWFjYzE3ZGQtZWIy_P0A1_ff79c397-9d79-44f7-8296-8858b58f5ba8"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)