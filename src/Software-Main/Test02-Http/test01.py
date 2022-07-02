
import requests

request = requests.get("https://httpbin.org/get")
#print(request.text)
#print(request.status_code)
#print(request.headers['Server'])
#print(request.json())
response = request.json()
print(response['url'])

payload = {'username':'administrator','password':'password'}
r=requests.get('http://httpbin.org/get', params=payload)
print(r.text)

payload = {'username':'administrator','password':'password'}
r=requests.post('http://httpbin.org/post', data=payload)
print(r.url)
print(r.text)