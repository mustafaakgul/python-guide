
import requests

url = "http://api.fixer.io/latest?base="

first = input("birincidoviz")
second = input("ikincidoviz")
miktar = float(input("mktar"))

response = requests.get(url + first)

print(response)

json_data = response.json()

print(float(json_data["rates"][second]) * miktar)
