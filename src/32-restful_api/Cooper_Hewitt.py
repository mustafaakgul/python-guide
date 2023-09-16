# https://collection.cooperhewitt.org/api/methods/
# https://collection.cooperhewitt.org/api
import requests

url = "https://api.collection.cooperhewitt.org/rest/?method=cooperhewitt.search.objects&query=clock%20radio&page=1&per_page=100&access_token=yourtoken"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))