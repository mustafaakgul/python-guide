
import requests
s=requests.Session()
s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
print(s)
r=s.get('https://httpbin.org/cookies')
print(r.text)

s.auth=('user','pass')
s.headers.update({'test':'true'})
s.get('https://httpbin.org/headers', headers={'test','true'})