# http://localhost:3000/objects
import requests

url = "localhost:3000/objects"

payload = "{\n        \"id\": 5,\n        \"item\": \"The Fiancés\",\n        \"artist\": \"Pierre Auguste Renoir\",\n        \"collection\": \"Wallraf–Richartz Museum, Cologne, Germany\",\n        \"date\": \"1868\"\n    }"
headers = {
  'content-type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))